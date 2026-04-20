# Video Production & Streaming MCP Servers — OBS, YouTube, HeyGen, Twitch, Mux, Remotion, Dacast, and More

> Video production and streaming MCP servers are enabling AI agents to control live broadcasts, manage YouTube channels, generate AI videos, host and deliver content, create


Video production and streaming MCP servers are enabling AI agents to control live broadcasts, manage YouTube channels, generate AI-powered videos, host and deliver content at scale, create programmatic video from code, and add subtitles — all through natural language. Instead of switching between OBS, YouTube Studio, and a video editor, an AI agent can handle the entire production pipeline: "Switch to the interview scene in OBS, start recording, generate a highlights reel with subtitles when we're done, and upload it to YouTube with optimized metadata."

This review covers the **production and distribution pipeline** — live streaming, platform management, AI generation, hosting, programmatic creation, and subtitles. For post-production editing software (DaVinci Resolve, Adobe Creative Suite, FFmpeg processing) and audio production (ElevenLabs, Ableton, REAPER), see our [Audio & Video Processing MCP review](/reviews/audio-video-processing-mcp-servers/). For social media video posting, see our [Social Media & Marketing MCP review](/reviews/social-media-marketing-mcp-servers/).

The landscape spans seven areas: **live streaming** (OBS Studio control, Dacast, Bitmovin), **YouTube management** (40+ servers for upload, analytics, Shorts, channel management), **AI video generation** (HeyGen, Kling, Runway, Luma, Krea, InVideo), **video hosting & CDN** (Mux, Vimeo, Cloudflare Stream), **programmatic video** (Remotion, Plainly, chuk-motion), **subtitles & captions** (Whisper-based transcription and subtitle generation), and **Twitch & other platforms** (chat integration, Helix API).

The headline findings: **YouTube has 40+ MCP servers** — by far the most-served single platform in the entire MCP ecosystem, though no official Google server exists. **AI video generation is the fastest-growing subcategory** with official servers from HeyGen and multi-model aggregators like Krea covering 20+ generation models. **Live streaming gets strong official vendor support** from Dacast and Bitmovin. **Programmatic video has official servers** from both Remotion and Plainly Videos. **Video hosting is well-covered** by official Mux, Vimeo, and Cloudflare servers. **Subtitle generation combines FFmpeg with Whisper** for end-to-end automated captioning.

## Live Streaming

### OBS Studio MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [royshil/obs-mcp](https://github.com/royshil/obs-mcp) | 48 | TypeScript | MIT | 15+ |

The **primary MCP server for OBS Studio**, providing AI control over live broadcasts via the OBS WebSocket protocol. Tools organized by category:

- **Scene Management** — switch, create, and remove scenes on the fly
- **Source & Item Control** — toggle source visibility, mute/unmute audio inputs, reposition and resize items within scenes
- **Streaming & Recording** — start/stop stream, start/stop recording
- **General** — connection status, scene collection management

Built by Roy Shilkrot (also known for obs-localvocal, the local speech recognition plugin for OBS). The WebSocket approach means the MCP server runs alongside OBS rather than inside it, making it compatible with any OBS version that supports WebSocket 5.x. MIT licensed with active development.

An alternative exists at [yshk-mrt/obs-mcp](https://github.com/yshk-mrt/obs-mcp), built during a YC MCP hackathon.

### Dacast MCP (Official)

| Server | Type | Notes |
|--------|------|-------|
| [Dacast MCP Live Stream Server](https://www.dacast.com/blog/dacast-mcp-live-stream-server/) | Official | Cloud live streaming platform |

Dacast's **official MCP server** connects AI tools directly to their live streaming APIs. Capabilities include:

- **Stream Provisioning** — create and update live stream channels
- **Simulcast Management** — manage multiple simultaneous broadcast destinations
- **DVR & Recording** — toggle recording and DVR features
- **Playlist Management** — organize VOD content
- **Thumbnail Upload** — update stream thumbnails programmatically
- **Action Logging** — every action logged for traceability

Designed for broadcasters who want to reduce manual complexity — "create a new live stream channel, enable DVR, set up simulcast to YouTube and Facebook, and upload this thumbnail" becomes a single AI conversation. Source code available on GitHub.

### Bitmovin Stream Lab MCP (Official)

| Server | Type | Notes |
|--------|------|-------|
| [Bitmovin Stream Lab MCP](https://www.newscaststudio.com/2026/01/06/ces-2026-bitmovins-stream-lab-mcp-server-enables-llm-based-video-testing/) | Official | Video playback testing |

Launched at CES 2026, Bitmovin's Stream Lab MCP Server enables **LLM-based video playback testing** using natural language. The key differentiator: it tests on **30+ physical devices** including Samsung, LG, and Vizio smart TVs, web browsers, and gaming consoles — not just emulators.

This is a QA/testing tool rather than a production tool — AI agents can initiate and manage video playback tests, verify stream quality across device types, and report issues, all through natural language. A niche but valuable use case for video platform teams.

## YouTube Management

YouTube has **40+ MCP servers** in community directories — more than any other single platform in the MCP ecosystem. This reflects YouTube's massive creator economy but also creates significant fragmentation.

### ZubeidHendricks/youtube-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ZubeidHendricks/youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server) | 490 | TypeScript | — | 10+ |

The **most-starred YouTube MCP server**, enabling video management, Shorts creation, and advanced analytics through the YouTube Data API. At 490 stars and 59 forks, it has the largest community among YouTube MCP implementations.

### pauling-ai/youtube-mcp-server (Most Comprehensive)

| Server | Language | License | Tools |
|--------|----------|---------|-------|
| [pauling-ai/youtube-mcp-server](https://github.com/pauling-ai/youtube-mcp-server) | Python | — | 40 |

The **most comprehensive YouTube MCP server** with 40 tools spanning three APIs:

- **YouTube Data API v3** — video uploads, playlist management, comments, thumbnail setting, channel management
- **YouTube Analytics API** — channel performance, top videos/Shorts, audience retention curves, traffic sources, demographics, revenue
- **YouTube Reporting API** — bulk CSV reports for deep data analysis

Built with FastMCP. The only open-source server that provides YouTube Analytics API access for retention curves, traffic sources, and revenue data. Requires Google Cloud OAuth credentials.

### Other Notable YouTube Servers

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) | 503 | JavaScript | MIT — transcript extraction (in Social Media review) |
| [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) | 494 | TypeScript | MIT — transcript with ad filtering |
| [icraft2170/youtube-data-mcp-server](https://github.com/icraft2170/youtube-data-mcp-server) | — | — | YouTube Data API standardized interface |
| [sfiorini/youtube-mcp](https://github.com/sfiorini/youtube-mcp) | — | — | Video management and Shorts |
| [dogfrogfog/youtube-analytics-mcp](https://github.com/dogfrogfog/youtube-analytics-mcp) | — | — | Analytics with demographics |
| [CDataSoftware/youtube-analytics-mcp-server-by-cdata](https://github.com/CDataSoftware/youtube-analytics-mcp-server-by-cdata) | — | — | Read-only analytics via CData JDBC |
| [sparfenyuk/mcp-youtube](https://github.com/sparfenyuk/mcp-youtube) | — | — | General YouTube operations |

The transcript-focused servers (anaisbetts and kimtaeyoon83) overlap with the [Audio & Video Processing](/reviews/audio-video-processing-mcp-servers/) category but are listed here for completeness.

**Notable absence:** Google has not published an official YouTube MCP server despite YouTube being the world's largest video platform and Google actively participating in MCP with other products (Google Calendar, Google Analytics, Google Cloud).

## AI Video Generation

The fastest-growing subcategory, with servers that let AI agents generate videos using the latest generative AI models.

### HeyGen MCP (Official)

| Server | Type | Tools | Transport |
|--------|------|-------|-----------|
| [HeyGen MCP Server](https://docs.heygen.com/docs/heygen-mcp-server) | Official | 5+ | stdio + remote |
| [HeyGen Remote MCP](https://docs.heygen.com/docs/heygen-remote-mcp-server) | Official | 5+ | Remote (OAuth) |

HeyGen's **official MCP servers** enable AI-powered avatar video creation:

- **Avatar Generation** — create videos with AI avatars from text scripts
- **Voice Selection** — choose from available voices and languages
- **Video Creation** — end-to-end video generation from prompt to final render
- **Conversational Context** — manage context across multiple video generation requests

The **Remote MCP** variant is notable — it uses OAuth authentication and runs on HeyGen's hosted endpoint, meaning AI agents like Claude, Gemini CLI, and Cursor can create HeyGen videos without local installation. Credits come from the user's existing HeyGen plan.

### Krea MCP (Multi-Model)

| Server | Language | Models |
|--------|----------|--------|
| [keugenek/krea-mcp](https://github.com/keugenek/krea-mcp) | — | 20+ |

A **unified interface to 20+ AI generation models** through Krea.ai:

- **Image models** — Flux, Ideogram, Imagen 4
- **Video models** — Runway Gen-4, Hailuo, Kling, Pika, Veo 3
- **Capabilities** — text-to-image, text-to-video, image-to-video, custom styles

The aggregation approach is valuable — instead of configuring separate MCP servers for Runway, Kling, Pika, etc., one server provides access to all of them. Works with Claude Desktop, Claude Code, and any MCP client.

### Kling AI MCP

| Server | Language | Notes |
|--------|----------|-------|
| [199-mcp/mcp-kling](https://github.com/199-mcp/mcp-kling) | — | First complete Kling MCP |

The **first and most complete MCP server for Kling AI** — supports multiple models (v1, v1.5, v1.6, v2-master) with:

- **Video Generation** — text-to-video with configurable duration, aspect ratio, and professional mode
- **Image Creation** — text-to-image generation
- **Lip Sync** — synchronize lip movements to audio
- **Effects** — apply visual effects to existing content
- **Virtual Try-On** — clothing visualization on models

Kling 2.6 (December 2025) introduced "simultaneous audio-visual generation" — visuals, voiceovers, sound effects, and ambient atmosphere in a single pass.

### Other AI Video Generation Servers

| Server | Language | Notes |
|--------|----------|-------|
| [wheattoast11/mcp-video-gen](https://github.com/wheattoast11/mcp-video-gen) | — | Luma AI + RunwayML — video/audio/image generation |
| [felores/kie-ai-mcp-server](https://github.com/felores/kie-ai-mcp-server) | — | Kie.ai — intent detection, cost optimization, Veo3/Runway Aleph/Suno V5/ElevenLabs/Midjourney |
| [InVideo Remote MCP](https://invideo.io/ai/mcp/) | — | Official — scale YouTube Shorts production from prompts |

felores/kie-ai-mcp-server is interesting for its **intent detection** — it automatically understands what the user wants and optimizes for cost and quality without manual model selection. InVideo's official MCP focuses specifically on YouTube Shorts production at scale.

## Video Hosting & CDN

### Mux MCP (Official)

| Server | Type | Notes |
|--------|------|-------|
| [Mux MCP](https://fastmcp.me/MCP/Details/1263/mux-video-and-data-platform) | Official | Video + Data platform |

Mux's **official MCP server** integrates with their Video and Data platform:

- **Video Upload** — upload and manage video assets
- **Live Stream Management** — create and control live streams
- **Analytics** — query viewer engagement and playback metrics
- **Performance Metrics** — track video infrastructure performance

Mux is widely used by developer-focused companies (Notion, Coursera, Robinhood) for video infrastructure, making this server particularly relevant for teams already on the Mux platform.

### Vimeo MCP (Official)

| Server | Type | Notes |
|--------|------|-------|
| [Vimeo MCP Server](https://developer.vimeo.com/api/mcp-server) | Official | Video platform API |

Vimeo's **official MCP server** for their video platform API — video upload, management, and playback integration. Documentation available at developer.vimeo.com.

### Cloudflare Stream (via Cloudflare MCP)

| Server | Stars | Type | Notes |
|--------|-------|------|-------|
| [cloudflare/mcp](https://github.com/cloudflare/mcp) | — | Official | 2,500 API endpoints in 1K tokens |

Cloudflare's **official MCP server** covers Stream alongside Workers, KV, R2, D1, Pages, DNS, and more. The server is notable for being **token-efficient** — 2,500 endpoints accessible within approximately 1,000 tokens of context. Video-specific capabilities include Stream upload, management, and delivery. The breadth means you get video hosting plus your entire Cloudflare infrastructure in one MCP server.

## Programmatic Video

### Remotion MCP (Official)

| Server | Type | Notes |
|--------|------|-------|
| [Remotion MCP](https://www.remotion.dev/docs/ai/mcp) | Official | React-based video rendering |
| [mcp-use/remotion-mcp-app](https://github.com/mcp-use/remotion-mcp-app) | Community | MCP App with live player |

Remotion's **official MCP server** brings programmatic video creation (React components rendered to video) into AI workflows. The official server integrates with GitHub Copilot Chat for documentation-assisted video development.

The community **remotion-mcp-app** goes further — it's an MCP App (not just a server) with a `create_video` tool and a live Remotion Player widget embedded in the chat interface, enabling real-time preview of generated videos.

### Chuk-Motion (Remotion Components)

| Server | Language | Components | Themes |
|--------|----------|------------|--------|
| [chrishayuk/chuk-mcp-remotion](https://github.com/chrishayuk/chuk-mcp-remotion) | — | 51 | 7 |

A design-system-first approach to Remotion video generation — **51 video components** and **7 built-in themes** optimized for multiple platforms. Enables AI to create professional animated videos without building components from scratch. Think of it as a component library for AI-generated video.

### Plainly Videos MCP (Official)

| Server | Type | Notes |
|--------|------|-------|
| [plainly-videos/mcp-server](https://github.com/plainly-videos/mcp-server) | Official | After Effects template automation |

Plainly Videos' **official MCP server** for Adobe After Effects template automation. Four tools:

- `list_renderable_items` — browse available designs and projects
- `get_renderable_items_details` — get design specifications and parameters
- `render_item` — submit renders with custom parameters
- `check_render_status` — monitor render progress and get preview links

This bridges the gap between AI agents and traditional motion graphics — designers create After Effects templates, and AI agents can render personalized versions at scale.

## Subtitles & Captions

MCP servers that combine FFmpeg with OpenAI Whisper for automated subtitle generation.

### vid-subtitle

| Server | Language | Notes |
|--------|----------|-------|
| [tomoima525/vid-subtitle](https://github.com/tomoima525/vid-subtitle) | — | FFmpeg + Whisper API subtitles |

An MCP server that **adds subtitles to videos** using FFmpeg and OpenAI Whisper API. Tools include:

- Add subtitles with automatic transcription
- Embed existing SRT/VTT subtitles into video
- Extract subtitles only (without embedding)
- Refine/edit generated subtitles

The pipeline: video → FFmpeg extracts audio → Whisper transcribes → SRT generated → FFmpeg embeds subtitles back into video.

### Fast-Whisper-MCP-Server

| Server | Language | Notes |
|--------|----------|-------|
| [BigUncle/Fast-Whisper-MCP-Server](https://github.com/BigUncle/Fast-Whisper-MCP-Server) | Python | High-performance local Faster Whisper |

A **high-performance speech recognition MCP server** based on Faster Whisper (CTranslate2 optimized). Output formats include VTT subtitles, SRT, and JSON. Supports batch transcription of multiple audio files. Runs entirely locally — no cloud API calls needed.

### Video Toolkit MCP

| Server | Language | Notes |
|--------|----------|-------|
| [JamesANZ/video-toolkit-mcp](https://github.com/JamesANZ/video-toolkit-mcp) | — | Download + transcribe + subtitle |

A comprehensive video toolkit providing:

- **Transcript Retrieval** — extract transcripts from online videos
- **Video Downloading** — download videos from supported platforms
- **Auto Subtitle Generation** — using OpenAI Whisper API or local Whisper

The most end-to-end subtitle server — handles the full pipeline from fetching the video through transcription to subtitle file generation.

### Video Caption MCP

| Server | Notes |
|--------|-------|
| [ow-enj/mcp-video-last-try](https://glama.ai/mcp/servers/@ow-enj/mcp-video-last-try) | Groq Whisper API — download, extract audio, transcribe, generate SRT |

Uses Groq's Whisper API (faster inference than OpenAI) for the transcription step. Pipeline: download video → FFmpeg extracts 16kHz mono WAV → Groq Whisper transcribes → SRT subtitle file generated.

## Twitch & Other Platforms

### Twitch MCP Servers

| Server | Language | Notes |
|--------|----------|-------|
| [TomCools/twitch-mcp](https://github.com/TomCools/twitch-mcp) | Java | Chat integration — read/send Twitch chat messages |
| [mtane0412/twitch-mcp-server](https://github.com/mtane0412/twitch-mcp-server) | — | Helix API — channel info, stream details, game data, viewer counts |

Two complementary servers: TomCools/twitch-mcp handles **chat** (reading and sending messages, built with Quarkus), while mtane0412/twitch-mcp-server provides **platform data** via the Twitch Helix API (channel descriptions, stream status, game metadata, viewer counts).

Neither server provides full broadcast control — no scene switching, alert management, or stream configuration. For OBS control during Twitch streams, combine these with royshil/obs-mcp.

## What's Missing

Despite 60+ servers, significant gaps remain:

- **No official YouTube MCP from Google** — the most conspicuous absence in the entire MCP ecosystem; 40+ community servers fill the gap
- **No Kick, Rumble, or alternative streaming platforms** — Twitch is the only gaming/live streaming platform with MCP servers
- **No professional broadcast protocols** — no SRT (Secure Reliable Transport), RTMP management, NDI, or SDI workflow tools
- **No video CDN analytics beyond Mux** — no Fastly, Akamai, or AWS CloudFront video analytics
- **No caption translation** — subtitle servers generate captions but none translate them across languages
- **No video SEO tools** — no thumbnail A/B testing, title optimization, or tag suggestion servers
- **No podcast video platforms** — no Spotify Video, Riverside.fm, or Descript MCP servers
- **No video conferencing** — no Zoom, Google Meet, or Microsoft Teams recording/management MCP servers (though Teams has general MCP servers)
- **No closed captioning standards** — no CEA-608/708, TTML, or WebVTT compliance checking
- **No video accessibility** — no audio description generation, sign language overlay, or accessibility compliance tools
- **No esports/tournament streaming** — despite Twitch chat MCP servers, no tournament overlay, bracket, or production management tools

## The Bottom Line

Video Production & Streaming MCP servers earn **4.0 out of 5**. The category benefits from strong official vendor participation — Dacast, Bitmovin, HeyGen, Mux, Vimeo, Remotion, Plainly Videos, and InVideo all have official MCP servers, showing that the video industry is actively embracing AI agent integration.

YouTube's 40+ community servers demonstrate enormous market demand but also the most extreme fragmentation in the MCP ecosystem — choosing the right YouTube server requires careful evaluation of which APIs you need (Data API v3 vs. Analytics vs. Reporting). The absence of an official Google YouTube MCP server is the single most notable gap across all MCP categories given YouTube's market dominance.

AI video generation is the most exciting growth area, with HeyGen's remote MCP (OAuth-based, no local install) pointing toward the future of how MCP servers will be deployed. Multi-model aggregators like Krea (20+ models through one server) solve the real problem of model selection fatigue. The subtitle/caption pipeline is practical and production-ready — Whisper-based servers handle the full flow from audio extraction through transcription to embedded subtitles.

The weaknesses are the near-complete absence of alternative streaming platforms (Kick, Rumble), the lack of professional broadcast protocol management (SRT, RTMP, NDI), and missing video accessibility tools. The subtitle servers generate captions but none translate them, missing an obvious multilingual opportunity.

**Category**: [Design & Creative MCP Servers](/categories/design-creative/)

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

