# MCP and Multimodal AI: How Agents Handle Images, Video, Audio, and Rich Media

> A comprehensive guide to multimodal content in MCP — covering ImageContent, AudioContent, EmbeddedResource content types, image generation servers (DALL-E, Stable Diffusion


AI agents are no longer text-only. The [MCP specification](https://modelcontextprotocol.io/specification/2025-06-18/schema) now defines five content types — TextContent, ImageContent, AudioContent, EmbeddedResource, and ResourceLink — enabling agents to receive screenshots, generate images, transcribe audio, analyze video, and work with binary files through standardized tool interfaces. This shift from text-only to multimodal is one of the most significant changes in the MCP ecosystem in 2026.

The practical impact is concrete. An agent debugging a UI issue can receive a screenshot through an MCP tool, analyze the layout, and suggest CSS fixes. A content creation agent can generate images with DALL-E, produce voiceovers with ElevenLabs, and analyze video footage with TwelveLabs — all through MCP tool calls. A data analysis agent can return charts as images alongside tabular results.

But multimodal MCP introduces challenges that text-based tools don't face: base64 encoding inflates payload sizes, large media files can overwhelm context windows, and not all MCP clients support all content types. This guide covers the specification, the server ecosystem, practical implementation patterns, and the gotchas. Our analysis draws on the [official MCP specification](https://modelcontextprotocol.io/specification/2025-06-18/schema), published documentation, and community implementations — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## MCP Content Types: The Foundation

The [June 2025 MCP specification (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18/schema) defines content types that tools can return in their `CallToolResult`. All five content types below are members of the [`ContentBlock` union type](https://modelcontextprotocol.io/specification/2025-06-18/schema) in the schema. Understanding these types is essential for building and consuming multimodal MCP servers.

### TextContent

The familiar text block. Every MCP server uses this — it's the default for returning strings, JSON, Markdown, or any text data.

```json
{
  "type": "text",
  "text": "Analysis complete. Found 3 accessibility issues.",
  "annotations": {
    "audience": ["user"],
    "priority": 0.8
  }
}
```

### ImageContent

Base64-encoded image data with a MIME type. This is what enables agents to "see" — receiving screenshots, charts, diagrams, or generated images as part of tool results.

```json
{
  "type": "image",
  "data": "iVBORw0KGgoAAAANSUhEUgAA...",
  "mimeType": "image/png"
}
```

Supported MIME types include `image/png`, `image/jpeg`, `image/gif`, `image/webp`, and `image/svg+xml`. The `data` field contains the raw image bytes encoded as a base64 string.

### AudioContent

Base64-encoded audio data, following the same pattern as ImageContent. This enables speech-to-text results, generated audio, and sound analysis.

```json
{
  "type": "audio",
  "data": "UklGRiQAAABXQVZFZm10...",
  "mimeType": "audio/wav"
}
```

Common MIME types include `audio/wav`, `audio/mp3`, `audio/ogg`, and `audio/webm`.

### EmbeddedResource

A wrapper for MCP resources (text or binary) embedded directly in tool results. This lets tools return file contents with their URIs preserved, so clients know where the data came from.

```json
{
  "type": "resource",
  "resource": {
    "uri": "file:///reports/q1-sales.pdf",
    "mimeType": "application/pdf",
    "blob": "JVBERi0xLjcKCj..."
  }
}
```

EmbeddedResource uses either `TextResourceContents` (with a `text` field) or `BlobResourceContents` (with a base64-encoded `blob` field). It's up to the client how to render embedded resources for the LLM or user.

### ResourceLink

A lightweight pointer to a resource without embedding its contents. Useful when the data is large and the client should fetch it on demand.

```json
{
  "type": "resource_link",
  "uri": "file:///videos/demo.mp4",
  "mimeType": "video/mp4",
  "name": "Product demo video"
}
```

### Annotations

All content types support optional annotations that provide metadata:

- **`audience`** — who the content is intended for: `["user"]`, `["assistant"]`, or both
- **`priority`** — a float from 0.0 to 1.0 indicating relative importance
- **`timestamp`** — ISO 8601 timestamp for when the content was created or modified

Annotations help clients make rendering decisions — for instance, an image annotated with `audience: ["user"]` might be displayed in the UI but not sent to the LLM to save tokens.

## The Multimodal MCP Server Landscape

### Image Generation Servers

These servers enable AI agents to create images from text prompts, edit existing images, and manipulate visual content.

#### DALL-E MCP Servers

Multiple community servers wrap OpenAI's DALL-E API for MCP access. They typically expose tools like `generate_image` (text-to-image), `edit_image` (inpainting with masks), and `create_variation`. The returned ImageContent is base64-encoded PNG or JPEG.

Key implementations include [image-generator-mcp-server](https://github.com/sammyl720/image-generator-mcp-server) by sammyl720 (11 stars) and [imagegen-mcp](https://github.com/spartanz51/imagegen-mcp) by spartanz51 (33 stars), both providing text-to-image and image-to-image capabilities through MCP tool interfaces. These connect directly to the OpenAI API, requiring an API key configured in the server environment.

#### Stable Diffusion / Flux MCP Servers

For local or self-hosted image generation:

- **image-gen-mcp** ([GitHub](https://github.com/Ichigo3766/image-gen-mcp), 34 stars) — connects to Stable Diffusion WebUI (AUTOMATIC1111 or ForgeUI) running locally, exposing text-to-image generation through MCP
- **Stability AI MCP Server** ([GitHub](https://github.com/tadasant/mcp-server-stability-ai), 83 stars) — integrates with the Stability AI API for generation, editing, upscaling, and style transfer
- **Flux-based servers** — several implementations use Replicate's Flux models for high-quality generation without local GPU requirements

#### MCPollinations

[MCPollinations](https://github.com/pinkpixel-dev/MCPollinations) (40 stars) provides a unified multimodal server covering image generation (via Pollinations API), text generation, and audio generation — all without requiring API keys or authentication. This makes it one of the most accessible multimodal MCP servers for experimentation.

#### ImgMCP

A commercial MCP server focused on image manipulation: resizing, cropping, format conversion, OCR text extraction, and object detection. Returns processed images as ImageContent blocks.

### Video Intelligence Servers

#### TwelveLabs MCP Server

| Detail | Value |
|--------|-------|
| Provider | TwelveLabs (official) |
| Models | Marengo (embeddings), Pegasus (video-to-text) |
| Capabilities | Video indexing, semantic search, summarization |
| License | Commercial (API key required) |

The [TwelveLabs MCP Server](https://www.twelvelabs.io/blog/twelve-labs-mcp-server) is the most capable video intelligence server in the MCP ecosystem. It enables AI agents to:

- **Index videos** — upload and process video content for searchability
- **Semantic search** — find exact moments across hours of footage using natural language queries
- **Generate summaries** — produce text descriptions of video content
- **Analyze scenes** — identify objects, actions, and context within video segments

TwelveLabs uses video-native models rather than frame-by-frame image analysis, understanding temporal relationships and narrative flow. When combined with video generation tools (like the Sora 2 MCP server), agents can both create and analyze video content.

The server works with Claude Desktop, Cursor, Windsurf, and custom MCP clients. It processes video asynchronously — indexing can take minutes for long videos — making it a good fit for the [MCP async tasks pattern](/guides/mcp-async-tasks-long-running/).

#### MMAudio MCP

An AI-powered server for video-to-audio and text-to-audio generation. Given a video file, it generates matching audio — useful for adding soundtracks or sound effects to video content.

### Audio and Speech Servers

#### ElevenLabs MCP Server

| Detail | Value |
|--------|-------|
| Provider | ElevenLabs (official) |
| Capabilities | TTS, transcription, voice cloning, outbound calls |
| License | Commercial (API key required) |

The [official ElevenLabs MCP server](https://elevenlabs.io/blog/introducing-elevenlabs-mcp) ([GitHub](https://github.com/elevenlabs/elevenlabs-mcp)) is the most full-featured audio server in the ecosystem. It supports:

- **Text-to-speech** — generate natural-sounding speech in multiple voices and languages
- **Audio transcription** — convert speech to text with speaker identification
- **Voice cloning** — create custom voices from audio samples
- **Sound effects** — generate sound effects from text descriptions
- **Music composition** — compose music with customizable parameters
- **Audio isolation** — separate vocals from background audio
- **Speech-to-speech** — voice conversion between different voices
- **Conversational AI agents** — create, manage, and deploy outbound voice calling agents via [Twilio/SIP integration](https://github.com/elevenlabs/elevenlabs-mcp)

The server exposes [24 tools](https://github.com/elevenlabs/elevenlabs-mcp) in total, returning AudioContent blocks with generated speech and TextContent blocks with transcription results.

#### Azure Speech MCP Server

Part of the [Azure MCP Server](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/tools/ai-services-speech) collection (page last updated March 2026). Provides two core tools — Speech-to-Text (Recognize) and Text-to-Speech (Synthesize) — through Azure AI Services, supporting multiple audio formats (WAV, MP3, OPUS/OGG, FLAC) and custom voice models.

#### Whisper-Based Servers

Several community servers wrap OpenAI's Whisper model (or the open-source whisper.cpp) for local speech-to-text:

- **[Local Speech-to-Text](https://github.com/SmartLittleApps/local-stt-mcp)** by SmartLittleApps (12 stars) — uses whisper.cpp for fully offline transcription, optimized for Apple Silicon, with speaker diarization and multiple output formats (txt, json, vtt, srt, csv)
- **Speech Interface (Faster Whisper)** — optimized for speed with CTranslate2 backend
- **Audio MCP Server** by GongRzhe — combined recording, transcription, and playback (**note:** [archived March 2026](https://github.com/GongRzhe/Audio-MCP-Server), now read-only)

These are particularly valuable for privacy-sensitive applications since audio never leaves the local machine.

#### Text-to-Speech Servers

Lightweight TTS servers include:

- **mcp-tts** — supports macOS `say`, ElevenLabs, Google Gemini TTS, and OpenAI TTS through a unified interface
- **play-sound-mcp-server** — simple audio playback for notification sounds when tasks complete
- **Epidemic Sound MCP** — searches and retrieves music from the Epidemic Sound catalog for content creation

### Screenshot and Screen Capture Servers

Screenshot servers bridge the gap between visual interfaces and text-based agents:

- **ScreenshotOne MCP** — captures website screenshots through the ScreenshotOne API, returning images as base64-encoded ImageContent
- **Playwright MCP** ([GitHub](https://github.com/microsoft/playwright-mcp)) — Microsoft's browser automation server captures page screenshots as part of its tool suite (covered in detail in our [MCP for Testing/QA guide](/guides/mcp-testing-qa/))
- **BrowserTools MCP** ([GitHub](https://github.com/AgentDeskAI/browser-tools-mcp), 7,186 stars) — captured browser screenshots and console logs (**discontinued:** the README states ["THIS PROJECT IS NO LONGER ACTIVE"](https://github.com/AgentDeskAI/browser-tools-mcp) as of March 2026; no code updates since March 2025)

### OCR and Document Processing

Servers that extract text from images and documents:

- **Image Reader MCP** — lists local image files and reads their content for LLM analysis
- **Mistral OCR servers** — leverage Mistral's vision models for document understanding
- **ModelScope-based servers** — Rust implementations providing OCR, object detection, and image analysis through ModelScope APIs

### Image Generation Comparison

| Server | Provider | Generation | Editing | Local | Auth Required |
|--------|----------|-----------|---------|-------|--------------|
| DALL-E MCP | OpenAI | Yes | Yes | No | Yes (API key) |
| Stability AI MCP | Stability AI | Yes | Yes | No | Yes (API key) |
| image-gen-mcp | SD WebUI | Yes | No | Yes | No |
| MCPollinations | Pollinations | Yes | No | No | No |
| ImgMCP | ImgMCP | No | Yes | No | Yes |

### Audio/Speech Server Comparison

| Server | Provider | TTS | STT | Voice Clone | Local | Auth Required |
|--------|----------|-----|-----|-------------|-------|--------------|
| ElevenLabs MCP | ElevenLabs | Yes | Yes | Yes | No | Yes |
| Azure Speech MCP | Microsoft | Yes | Yes | Yes | No | Yes |
| Whisper servers | Community | No | Yes | No | Yes | No |
| mcp-tts | Community | Yes | No | No | Partial | Varies |
| MCPollinations | Pollinations | Yes | No | No | No | No |

## Implementation Patterns

### Returning Images from Tools

The most common multimodal pattern is a tool that returns an image alongside descriptive text. In the Python SDK with FastMCP, this is straightforward:

```python
from fastmcp import FastMCP
from fastmcp.utilities.types import Image

mcp = FastMCP("chart-server")

@mcp.tool()
def generate_chart(data: list[float], title: str) -> Image:
    """Generate a bar chart from data."""
    # Create chart with matplotlib
    import matplotlib.pyplot as plt
    import io

    fig, ax = plt.subplots()
    ax.bar(range(len(data)), data)
    ax.set_title(title)

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return Image(data=buf.read(), format="png")
```

FastMCP automatically converts the `Image` object to an MCP `ImageContent` block with correct base64 encoding and MIME type.

For mixed content (text + image), return a list:

```python
@mcp.tool()
def analyze_page(url: str) -> list:
    """Capture and analyze a web page."""
    screenshot = capture_screenshot(url)  # returns bytes
    return [
        Image(data=screenshot, format="png"),
        "Screenshot captured successfully. Ready for analysis."
    ]
```

### Returning Audio from Tools

Audio follows the same base64 pattern:

```python
@mcp.tool()
def text_to_speech(text: str, voice: str = "alloy") -> dict:
    """Convert text to speech audio."""
    audio_bytes = generate_speech(text, voice)  # API call
    return {
        "type": "audio",
        "data": base64.b64encode(audio_bytes).decode(),
        "mimeType": "audio/mp3"
    }
```

### Resources with Binary Content

MCP resources can serve binary content through `BlobResourceContents`:

```python
@mcp.resource("images://{filename}")
def get_image(filename: str) -> bytes:
    """Serve an image file."""
    with open(f"/images/{filename}", "rb") as f:
        return f.read()
```

FastMCP detects the `bytes` return type and automatically creates a `BlobResourceContents` with base64 encoding and an appropriate MIME type based on the file extension.

### Client-Side Content Handling

Not all clients handle all content types. When building MCP servers that return multimodal content, consider graceful degradation:

```python
@mcp.tool()
def analyze_with_fallback(image_path: str) -> list:
    """Analyze an image with text fallback."""
    analysis = run_analysis(image_path)

    return [
        # Image for clients that support it
        Image(path=image_path),
        # Text description as fallback
        f"Analysis results:\n{analysis.summary}\n\n"
        f"Objects detected: {', '.join(analysis.objects)}\n"
        f"Dominant colors: {', '.join(analysis.colors)}"
    ]
```

Clients that support `ImageContent` will display the image. Those that don't will still receive the text description. The `annotations.audience` field can help here — mark the image as `["user"]` if the text description provides sufficient information for the LLM.

## Handling Large Media Files

Base64 encoding increases data size by approximately 33%. A 1 MB image becomes ~1.33 MB when base64-encoded and embedded in a JSON response. For video and audio files, this overhead quickly becomes problematic.

### The Size Problem

| Media Type | Typical Size | Base64 Size | Token Estimate |
|-----------|-------------|------------|----------------|
| Screenshot (PNG) | 200 KB | 267 KB | ~2,000 |
| High-res photo (JPEG) | 2 MB | 2.7 MB | ~20,000 |
| 30-sec audio (MP3) | 500 KB | 667 KB | ~5,000 |
| 1-min video (MP4) | 10 MB | 13.3 MB | ~100,000 |

These are rough estimates — actual token counts depend on the model and how it processes binary content. The key insight is that embedding large media files directly in tool results can consume significant context window space.

### Pattern 1: Thumbnail + Full Resolution on Demand

Return a compressed thumbnail in the tool result and offer the full-resolution version as a resource:

```python
@mcp.tool()
def capture_screenshot(url: str) -> list:
    """Capture a web page screenshot."""
    full_image = take_screenshot(url)  # Full resolution
    thumbnail = resize(full_image, max_width=800)  # Compressed

    # Store full image for on-demand access
    store_resource(f"screenshots/{url_hash}", full_image)

    return [
        Image(data=thumbnail, format="jpeg"),  # Small version
        f"Screenshot captured. Full resolution available at "
        f"screenshots://{url_hash}"
    ]
```

### Pattern 2: Process Server-Side, Return Text

For many multimodal workflows, the agent doesn't need the raw media — it needs information extracted from it:

```python
@mcp.tool()
def analyze_image(image_path: str) -> str:
    """Analyze an image and return findings."""
    # Process with vision model server-side
    results = vision_model.analyze(image_path)

    return (
        f"Image: {image_path}\n"
        f"Dimensions: {results.width}x{results.height}\n"
        f"Objects: {', '.join(results.objects)}\n"
        f"Text found: {results.ocr_text}\n"
        f"Scene: {results.scene_description}"
    )
```

This pattern avoids sending image bytes through the MCP pipeline entirely. The tradeoff is that the agent can't "see" the image — it only gets the analysis results.

### Pattern 3: Chunked Processing for Large Files

The [Large File MCP server](https://github.com/willianpinho/large-file-mcp) (10 stars, actively maintained) demonstrates intelligent chunking for files that can't be loaded into memory at once:

- **Smart chunking** — automatically determines optimal chunk size based on file type
- **Memory-efficient streaming** — processes files line-by-line without loading the entire file
- **LRU caching** — 80–90% hit rates for frequently accessed file sections
- **Seek-based access** — tools like `read_chunk(file, offset, length)` let agents request specific portions

For media files specifically, the pattern adapts:

```python
@mcp.tool()
def get_video_segment(video_path: str, start_sec: float,
                      duration_sec: float) -> list:
    """Extract and analyze a specific video segment."""
    # Extract frames from the segment
    frames = extract_key_frames(video_path, start_sec, duration_sec)
    # Return only key frames, not the full video
    return [
        Image(data=frame, format="jpeg")
        for frame in frames[:5]  # Limit to 5 key frames
    ] + [f"Extracted {len(frames)} key frames from "
         f"{start_sec}s to {start_sec + duration_sec}s"]
```

### Pattern 4: Reference-Based Workflows

For very large media, use ResourceLinks to point to files without embedding them:

```json
{
  "content": [
    {
      "type": "text",
      "text": "Video processed successfully. 3 segments identified."
    },
    {
      "type": "resource_link",
      "uri": "videos://processed/segment-1.mp4",
      "name": "Intro segment (0:00-0:45)",
      "mimeType": "video/mp4"
    },
    {
      "type": "resource_link",
      "uri": "videos://processed/segment-2.mp4",
      "name": "Main content (0:45-3:20)",
      "mimeType": "video/mp4"
    }
  ]
}
```

The client can then fetch individual segments on demand, rather than receiving all video data in a single response.

## Multimodal Workflow Examples

### Visual QA Pipeline

An agent that answers questions about images combines multiple MCP servers:

1. **Screenshot server** captures a web page → returns ImageContent
2. **OCR server** extracts text from the image → returns TextContent
3. The LLM analyzes the image + extracted text together
4. **TTS server** optionally converts the answer to speech → returns AudioContent

Each step uses standard MCP tool calls. The agent orchestrates the pipeline, passing context between servers.

### Content Creation Pipeline

An agent creating a blog post with media:

1. Agent writes the article text
2. **Image generation server** (DALL-E/Flux) creates a hero image from a prompt → ImageContent
3. **Image manipulation server** resizes and optimizes the image → ImageContent
4. **TTS server** generates an audio version of the article → AudioContent
5. Agent combines everything into a published post

### Video Analysis Pipeline

An agent reviewing video content:

1. **TwelveLabs MCP** indexes a video (async — may take minutes)
2. Agent searches for specific moments: "find scenes with the product logo"
3. TwelveLabs returns timestamps and descriptions (TextContent)
4. **Screenshot/frame extraction server** captures key frames → ImageContent
5. Agent analyzes frames and generates a report

### Accessibility Audit

An agent evaluating website accessibility:

1. **Playwright MCP** captures a page screenshot and accessibility tree
2. Agent identifies visual issues from the screenshot (color contrast, text size)
3. Agent cross-references with the accessibility tree data
4. **Image annotation server** marks problem areas on the screenshot → ImageContent
5. Agent produces a report with annotated screenshots

## Client Support for Multimodal Content

Not all MCP clients support all content types equally. This is one of the biggest practical challenges with multimodal MCP.

### Current Client Support

| Client | TextContent | ImageContent | AudioContent | EmbeddedResource |
|--------|------------|-------------|-------------|-----------------|
| Claude Desktop | Full | Full | Partial | Full |
| Cursor | Full | Partial | No | Partial |
| Windsurf | Full | Partial | No | Partial |
| Claude Code | Full | Full | No | Partial |
| Custom clients | Varies | Varies | Varies | Varies |

"Partial" typically means the client accepts the content type but may not render it optimally — for example, displaying base64 data as text rather than rendering an image.

### Implications for Server Developers

- **Always include TextContent alongside media** — provide a text description or summary so agents that can't process the media still get useful information
- **Use annotations** — mark media with `audience: ["user"]` when it's for display only, so clients can skip sending it to the LLM
- **Document supported content types** — clearly state what content types your server returns so client developers know what to expect
- **Test with multiple clients** — behavior varies significantly between Claude Desktop, IDE integrations, and custom clients

Notably, the Gemini CLI [opened an issue](https://github.com/google-gemini/gemini-cli/issues/2136) tracking support for ImageContent in MCP tool results — this has since been **resolved** via [PR #5529](https://github.com/google-gemini/gemini-cli/pull/5529), which implemented multimodal MCP tool response parsing. The pace of resolution illustrates how rapidly clients are catching up with the full multimodal specification.

## Security Considerations

Multimodal content introduces security risks that text-only MCP doesn't face.

### Image-Based Prompt Injection

Images can contain text that attempts to manipulate the LLM. An MCP server that captures screenshots or processes user-uploaded images could inadvertently pass adversarial text to the model. Mitigations:

- **Server-side scanning** — check images for embedded text before returning them
- **Content annotation** — use `audience: ["user"]` for images that should be displayed but not interpreted by the LLM
- **Sandboxed rendering** — process images in isolated environments to prevent exploits

### Data Exfiltration via Media

A malicious MCP server could encode sensitive data in image pixels or audio frequencies, exfiltrating information that wouldn't be caught by text-based security scanning. This is a variant of the broader [MCP server security](/guides/mcp-server-security/) challenge.

### Large File Denial of Service

A server that returns very large base64-encoded files can overwhelm client memory or exhaust context windows. Implement:

- **Size limits** — cap the maximum size of returned media content
- **Compression** — always compress images before base64 encoding
- **Progressive loading** — use ResourceLinks for large files instead of embedding them

### MIME Type Validation

Don't trust MIME types from untrusted MCP servers. A server could claim to return `image/png` but actually send executable content. Clients should:

- Validate that the base64-decoded content matches the declared MIME type
- Render media in sandboxed contexts
- Reject unexpected MIME types

For a comprehensive treatment of MCP security risks, see our [MCP Attack Vectors and Defense guide](/guides/mcp-attack-vectors-defense/) and [MCP Server Security guide](/guides/mcp-server-security/).

## The 2026 Multimodal Roadmap

The MCP specification is actively evolving to better support multimodal content. The [2026 roadmap](https://modelcontextprotocol.io/development/roadmap) (last updated March 2026) identifies four priority areas: Transport Evolution and Scalability, Agent Communication, Governance Maturation, and Enterprise Readiness. Multimodal improvements appear under the "On the Horizon" section rather than as a top priority, but several items are relevant:

### Result Type Improvements

Under "On the Horizon," the roadmap describes [result type improvements](https://modelcontextprotocol.io/development/roadmap) including:

- **Streamed results** — clients could receive output incrementally for interactive scenarios (generated text, audio, video frames), rather than waiting for a complete base64 blob
- **Reference-based results** — clients could decide when to pull large payloads into context, addressing the base64 size overhead problem

These are not yet prioritized for implementation but signal the direction for handling large media content more efficiently.

### Extensions Ecosystem

The roadmap mentions an extensions ecosystem where "ext-auth and ext-apps tracks are early proof that the extension mechanism works." The `ext-apps` track could potentially enable richer interactive experiences beyond request-response tool calls, though its full scope is still being defined.

### What's Not (Yet) on the Roadmap

Notably absent from the current roadmap: explicit content negotiation (where clients declare supported content types and servers adapt), and dedicated multipart message transport for binary content. These capabilities would address the client support fragmentation described above, but they haven't been formally proposed as roadmap items.

## When to Go Multimodal

### Use Multimodal MCP When:

- **The task requires visual context** — UI debugging, design review, data visualization, accessibility audits
- **You're building content creation pipelines** — blog posts with images, video scripts with thumbnails, podcasts
- **The agent needs to analyze non-text data** — medical images, architectural drawings, audio recordings
- **User experience requires media** — displaying charts, playing audio feedback, showing generated images

### Stick to Text-Only When:

- **Text descriptions suffice** — if an OCR result or image description gives the agent enough information, skip the raw image
- **Context window budget is tight** — images consume significant tokens; text summaries are cheaper
- **Your client doesn't support it** — check client support before building multimodal servers
- **The workflow is API-to-API** — if no human sees the output, text-based data transfer is more efficient

### Token Cost Awareness

Multimodal content is expensive in context window terms. A single high-resolution screenshot can consume 2,000–20,000 tokens. A practical approach:

1. **Start with text-only tools** that describe or summarize media content
2. **Add thumbnail/preview tools** that return compressed versions
3. **Offer full-resolution on demand** through resources or follow-up tools
4. **Use annotations** to prevent unnecessary media from reaching the LLM

## Getting Started

### Quick Start: Image-Capable Server

If you want to add image support to an existing MCP server:

1. Use the [FastMCP Python SDK](https://gofastmcp.com/servers/tools) — it handles base64 encoding automatically via `Image`, `Audio`, and `File` [utility classes](https://gofastmcp.com/servers/tools)
2. Return `Image(path="file.png")` or `Image(data=bytes_data, format="png")` from tools
3. Include a text description alongside every image
4. Test with Claude Desktop, which has the most complete ImageContent support

### Quick Start: Audio-Capable Server

For text-to-speech or transcription:

1. Start with MCPollinations for zero-auth experimentation
2. Move to ElevenLabs MCP for production-quality TTS
3. Use Whisper-based servers for local, private transcription

### Production Considerations

For multimodal servers in production:

1. **Implement size limits** — cap image dimensions and file sizes
2. **Compress aggressively** — use JPEG quality 80 for photos, PNG for screenshots
3. **Cache processed results** — avoid re-processing the same media
4. **Monitor token usage** — multimodal tools can dramatically increase API costs
5. **Plan for client diversity** — always provide text fallbacks
6. **Review our [MCP cost optimization guide](/guides/mcp-cost-optimization/)** for strategies to manage multimodal token budgets

## Further Reading

- [MCP for Testing/QA](/guides/mcp-testing-qa/) — browser automation servers with screenshot capabilities
- [MCP Server Security](/guides/mcp-server-security/) — security considerations for all MCP servers
- [MCP Attack Vectors and Defense](/guides/mcp-attack-vectors-defense/) — adversarial risks including image-based attacks
- [MCP Cost Optimization](/guides/mcp-cost-optimization/) — managing token usage with media-heavy workflows
- [MCP Async Tasks and Long-Running Operations](/guides/mcp-async-tasks-long-running/) — handling video processing and other async media tasks
- [Best Audio & Video MCP Servers](/guides/best-audio-video-mcp-servers/) — our review of audio and video MCP server options
- [Best Image Generation MCP Servers](/guides/best-image-generation-mcp-servers/) — our review of image generation server options

