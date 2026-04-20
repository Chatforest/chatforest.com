# Best Audio & Video MCP Servers in 2026

> ElevenLabs, DaVinci Resolve, Ableton, REAPER, FFmpeg, Premiere Pro, and more — we've reviewed 40+ audio and video MCP servers across 9 categories.


Audio and video is where MCP servers get creative. Instead of querying databases or managing infrastructure, these servers generate speech, transcribe meetings, edit video timelines, produce music, and control professional creative applications — all through natural language.

We've researched 40+ audio and video MCP servers across the full landscape. This guide covers what's production-ready, what's experimental, and where significant gaps remain.

*Note: Our recommendations are based on documentation review, GitHub analysis, and community feedback — not hands-on testing of every server. Star counts were verified in March 2026.*

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| Text-to-speech (cloud) | [elevenlabs/elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp) | 1,300 | [blacktop/mcp-tts](https://github.com/blacktop/mcp-tts) (50 stars, multi-provider) |
| Text-to-speech (local) | [aparsoft/kokoro-mcp-server](https://github.com/aparsoft/kokoro-mcp-server) | 6 | [CodeCraftersLLC/local-voice-mcp](https://github.com/CodeCraftersLLC/local-voice-mcp) (Chatterbox + Kokoro) |
| Transcription (cloud) | [arcaputo3/mcp-server-whisper](https://github.com/arcaputo3/mcp-server-whisper) | 48 | [cogell/assembly-ai-mcp](https://github.com/cogell/assembly-ai-mcp) (AssemblyAI) |
| Transcription (local) | [SmartLittleApps/local-stt-mcp](https://github.com/SmartLittleApps/local-stt-mcp) | 11 | [shreyaskarnik/voice-mcp](https://github.com/shreyaskarnik/voice-mcp) (bidirectional) |
| YouTube transcripts | [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) | 494 | Multiple alternatives |
| FFmpeg / video processing | [video-creator/ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp) | 124 | [misbahsy/video-audio-mcp](https://github.com/misbahsy/video-audio-mcp) (65 stars, 27 tools) |
| Professional video editing | [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) | 641 | [mikechambers/adb-mcp](https://github.com/mikechambers/adb-mcp) (505 stars, Adobe multi-app) |
| Music production (DAW) | [ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp) | 2,300 | [shiehn/total-reaper-mcp](https://github.com/shiehn/total-reaper-mcp) (29 stars, 600+ tools) |
| Video streaming | [Mux MCP](https://mcp.mux.com) | — | — |

## Why audio & video MCP servers matter

Creative work is repetitive in ways people don't discuss. A podcast editor trims silence from every episode. A video producer adds the same lower-third template to every interview. A music producer creates the same drum pattern skeleton in every session before making it unique. MCP servers automate the repetitive parts so humans focus on the creative decisions.

The value comes in three forms:

1. **Voice and speech.** Generate narration, clone voices for consistency, transcribe meetings with speaker identification — ElevenLabs' official MCP server turns a single API into a complete audio production pipeline.
2. **Video production.** Trim, transcode, overlay, and concatenate video through FFmpeg — or control professional NLEs like DaVinci Resolve and Premiere Pro directly, with hundreds of tools mapping their full scripting APIs.
3. **Music production.** Create tracks, load instruments, edit MIDI, and control DAW transport — Ableton MCP (2,300 stars) proved the demand, and REAPER's 600+ tool server shows the depth possible.

The landscape splits into nine categories: **text-to-speech** (cloud and local), **transcription** (cloud, local, YouTube), **FFmpeg video processing**, **professional video editing** (DaVinci Resolve, Adobe), **dedicated Premiere Pro**, **dedicated After Effects**, **music production** (Ableton, REAPER, Logic Pro, SuperCollider), **media generation** (AI video/image creation), and **video streaming** (Mux).

---

## Text-to-speech servers

Text-to-speech is the most mature audio MCP category, with cloud APIs, multi-provider wrappers, and local open-weight models all available.

### The winner: elevenlabs/elevenlabs-mcp

**Stars:** 1,300 | **Language:** Python | **License:** MIT | **Tools:** 10+

[elevenlabs/elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp) is the official ElevenLabs MCP server and the most feature-rich audio API server in the ecosystem. It covers the full ElevenLabs platform: **Text-to-Speech** with configurable voices, languages, and output formats. **Voice Cloning** from audio samples. **Voice Design** for creating new synthetic voices. **Transcription** with speaker identification. **Sound Effects** generation from text. **Audio Isolation** to separate speech from noise. **Conversational AI** for voice agents. **Outbound Calls** for voice agents that can make phone calls.

Three output modes: `files` (save to disk), `resources` (return via MCP resources), or `both`. Enterprise data residency control via `ELEVENLABS_API_RESIDENCY`. Free tier provides 10,000 credits/month.

**Why it wins:** No other audio MCP server combines TTS, STT, cloning, isolation, sound effects, and voice agents in a single server. This is effectively a complete audio production API accessible through natural language.

**The catch:** Requires an API key and sends audio data to ElevenLabs' servers. For privacy-sensitive use cases, consider the local alternatives below.

**Best for:** Anyone who wants the broadest audio capability from one server and is comfortable with a cloud API.

### Runner-up: blacktop/mcp-tts (multi-provider)

**Stars:** 50 | **Language:** Go | **License:** MIT | **Tools:** 4

[blacktop/mcp-tts](https://github.com/blacktop/mcp-tts) takes a different approach — instead of one provider, it offers four TTS backends with automatic fallback: `say_tts` (macOS built-in, zero cost, offline), `elevenlabs_tts` (high-quality synthesis), `google_tts` (Google Gemini, 30 voices), and `openai_tts` (10 voices, speed control 0.25x–4.0x).

The standout feature is **sequential TTS enforcement** — system-wide file locking prevents concurrent speech from multiple AI agent instances. Includes a "speak" skill for Claude Code, Codex CLI, and Gemini CLI.

**Best for:** Multi-agent setups or teams that want provider flexibility without lock-in.

### Best local option: aparsoft/kokoro-mcp-server

**Stars:** 6 | **Language:** Python | **License:** Apache 2.0 | **Tools:** 5+

[aparsoft/kokoro-mcp-server](https://github.com/aparsoft/kokoro-mcp-server) wraps the Kokoro-82M open-weight TTS model — 82 million parameters delivering good speech synthesis entirely locally, with no API keys or cloud dependencies. Twelve voices (American and British accents). Audio post-processing: normalization, noise reduction, silence trimming, fade effects. Batch and script processing. Multi-voice podcast generation. Docker deployment.

**Best for:** Compliance, privacy, or air-gapped environments where no audio can leave the machine.

### Also notable

**[notsointresting/gemini-tts-mcp](https://github.com/notsointresting/gemini-tts-mcp)** — Gemini 2.5 Flash/Pro TTS with 30+ premium voices and natural language style control. For teams already on Google's ecosystem.

**[CodeCraftersLLC/local-voice-mcp](https://github.com/CodeCraftersLLC/local-voice-mcp)** — Supports both Chatterbox Turbo TTS and Kokoro engines for local voice synthesis with voice cloning capabilities.

**[shreyaskarnik/voice-mcp](https://github.com/shreyaskarnik/voice-mcp)** — Bidirectional voice MCP server for Claude Code with STT and TTS on Apple Silicon via mlx-audio.

**[bmorphism/say-mcp-server](https://github.com/bmorphism/say-mcp-server)** — Minimal macOS text-to-speech via the built-in `say` command. Zero dependencies, zero cost.

---

## Transcription servers

### The winner (cloud): arcaputo3/mcp-server-whisper

**Stars:** 48 | **Language:** Python | **License:** MIT | **Tools:** 8

[arcaputo3/mcp-server-whisper](https://github.com/arcaputo3/mcp-server-whisper) is the most comprehensive cloud-based transcription MCP server, built on OpenAI's Whisper and GPT-4o models. Eight tools cover the full pipeline: audio file search with regex, format conversion, compression, multi-model transcription with timestamps, interactive GPT-4o audio analysis, enhanced output modes (detailed, storytelling, professional, analytical), and text-to-speech generation.

The `chat_with_audio` tool is unique — it enables conversational analysis of audio content, not just transcription. "What language is being spoken?" or "Summarize the key points discussed."

**Best for:** Teams that want the highest quality cloud transcription with audio analysis capabilities.

### The winner (local): SmartLittleApps/local-stt-mcp

**Stars:** 11 | **Language:** TypeScript | **License:** MIT | **Tools:** 6

[SmartLittleApps/local-stt-mcp](https://github.com/SmartLittleApps/local-stt-mcp) provides completely local transcription using whisper.cpp, optimized for Apple Silicon with 15x+ real-time transcription speed. Six tools: basic transcription, long audio with chunking, speaker diarization, model listing, health check, version info. Handles MP3, M4A, FLAC, OGG, WMA through automatic conversion. Under 2GB memory usage.

**Best for:** Local transcription with speaker diarization — ideal for meeting notes where you need to know who said what.

### YouTube transcripts: kimtaeyoon83/mcp-server-youtube-transcript

**Stars:** 494 | **Language:** TypeScript | **License:** MIT | **Tools:** 1

[kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) is the most popular YouTube transcript server. One tool with smart defaults: language fallback, optional timestamps, and built-in ad/sponsorship filtering. Accepts standard URLs, Shorts URLs, and raw video IDs.

The 494 stars — higher than many full-featured MCP servers — reflects a common workflow: AI agents analyzing video content by reading transcripts rather than processing raw audio.

### Also notable

**[cogell/assembly-ai-mcp](https://github.com/cogell/assembly-ai-mcp)** — AssemblyAI transcription services via MCP. Standard interface for AssemblyAI's API including the Slam-1 speech-language model.

**[deepgram-devs/deepgram-mcp](https://github.com/deepgram-devs/deepgram-mcp)** — Official Deepgram MCP server wrapping text-to-speech. Deepgram also offers agentic developer tools with an MCP skills marketplace.

**[r-lz/video-digest](https://github.com/r-lz/video-digest)** — Extracts and transcribes audio from YouTube, Bilibili, TikTok, and Twitter. Multi-provider support: Deepgram, Gladia, Speechmatics, AssemblyAI.

---

## FFmpeg video processing servers

FFmpeg MCP servers are plentiful but fragmented — no single dominant implementation exists. Here are the three strongest approaches.

### Best for common workflows: video-creator/ffmpeg-mcp

**Stars:** 124 | **Language:** Python | **License:** MIT | **Tools:** 8

[video-creator/ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp) provides the core FFmpeg operations most workflows need: `find_video_path` (recursive directory search), `get_video_info` (metadata), `clip_video` (trimming), `concat_videos` (combining), `play_video` (playback with speed/loop control), `overlay_video` (layering), `scale_video` (resizing with aspect ratio preservation), `extract_frames_from_video` (PNG/JPG/WEBP export).

**Best for:** Simple video processing tasks — trimming, concatenation, format conversion. The focused tool set keeps context window usage low.

### Best for professional editing: misbahsy/video-audio-mcp

**Stars:** 65 | **Language:** Python | **License:** MIT | **Tools:** 27

[misbahsy/video-audio-mcp](https://github.com/misbahsy/video-audio-mcp) is the most tool-rich FFmpeg MCP server with 27 tools spanning video operations, audio processing, creative effects (subtitles, overlays, b-roll insertion, transitions), and editing (concatenation, speed change, silence removal).

The `remove_silence` tool is particularly useful for podcast/video editing. B-roll insertion and transitions go beyond basic conversion into actual editing.

**Best for:** Podcast and video editing workflows that need more than format conversion.

### Best for advanced processing: dubnium0/ffmpeg-mcp

**Stars:** 15 | **Language:** Python | **License:** MIT | **Tools:** 40+

[dubnium0/ffmpeg-mcp](https://github.com/dubnium0/ffmpeg-mcp) has the largest FFmpeg tool count at 40+ across eight categories: media analysis (scene detection, keyframe extraction), format conversion (batch processing, GIF generation), audio processing (loudness normalization, waveform visualization), visual effects (picture-in-picture, split-screen, slideshows), subtitle management, streaming (HLS/DASH, adaptive multi-bitrate, RTMP), and advanced operations (two-pass encoding, video stabilization, denoising, custom FFmpeg commands).

**The catch:** Single commit suggests early-stage development. The breadth is impressive but maturity is unproven.

**Best for:** Advanced workflows needing streaming, stabilization, or batch processing — if you're willing to accept early-stage software.

### Also notable

**[kevinwatt/ffmpeg-mcp-lite](https://github.com/kevinwatt/ffmpeg-mcp-lite)** — Lightweight FFmpeg server for conversion, compression, trimming, audio extraction, and subtitles.

**[ctaylor86/rendi-mcp-server](https://github.com/ctaylor86/rendi-mcp-server)** — Cloud-based FFmpeg via Rendi API. No local FFmpeg installation needed.

**[video-dev/ffmpeg-mcp-comp](https://github.com/video-dev/ffmpeg-mcp-comp)** — Comprehensive FFmpeg server with format conversion, resizing, compression, trimming, concatenation, framerate changes, rotation, and frame extraction.

---

## Professional video editing

### The winner: samuelgursky/davinci-resolve-mcp

**Stars:** 641 | **Language:** Python | **License:** MIT | **Tools:** 26/342

[samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) has the deepest API coverage of any creative application MCP server — **100% of the DaVinci Resolve Scripting API** (324/324 methods), with 98.5% live-tested.

Two modes: **Compound Server** (default, 26 tools) groups related operations to keep context windows lean — project management, media pool, timeline editing, color grading, Fusion compositions, render pipeline. **Full Server** (342 tools) exposes one tool per API method for maximum precision. Auto-detects OS and Resolve installation. Supports 10+ MCP clients.

**Why it wins:** No other creative application MCP server maps 100% of its host application's API. The compound/granular dual-mode approach is an excellent pattern — practical defaults with full power available. The Fusion composition tool alone exposes the entire node graph API.

**Best for:** Professional video editors who want AI-assisted DaVinci Resolve workflows.

### Runner-up: mikechambers/adb-mcp (Adobe multi-app)

**Stars:** 505 | **Language:** JavaScript/Python | **License:** MIT | **Tools:** Multi-app

[mikechambers/adb-mcp](https://github.com/mikechambers/adb-mcp) enables AI control of multiple Adobe applications through a unified interface: **Photoshop** (layers, text, image generation, selections, filters), **Premiere Pro** (clips, transitions, effects, audio, timeline editing), **After Effects** (ExtendScript automation), **InDesign**, **Illustrator**.

Architecture: AI → MCP Server → Node Proxy → Adobe Plugin → Application. Not endorsed by Adobe — proof-of-concept, but with significant adoption (505 stars, 212 commits).

**Best for:** Teams already in the Adobe ecosystem who want one server for multiple Creative Cloud apps.

### Dedicated Premiere Pro servers

**[leancoderkavy/premiere-pro-mcp](https://github.com/leancoderkavy/premiere-pro-mcp)** (269 tools across 28 modules) — The most comprehensive Premiere Pro server. Covers project operations, ingest, sequence creation, timeline editing, transitions, effects, keyframes, metadata, exports, and assembly workflows via CEP/ExtendScript. Live instance at premiere-pro-mcp.fly.dev.

**[hetpatel-11/Adobe_Premiere_Pro_MCP](https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP)** (97 tools, 43 live-tested) — Covers project operations, ingest, sequence creation, timeline editing, transitions, effects, keyframes, metadata, and exports.

**[jordanl61/premiere-pro-mcp-server](https://github.com/jordanl61/premiere-pro-mcp-server)** — For power users, workflow automation, and AI/scripting integration.

### Dedicated After Effects servers

**[sunqirui1987/ae-mcp](https://github.com/sunqirui1987/ae-mcp)** (7 stars, Go/JavaScript, 9+ tools) — Composition creation, text/solid/shape layers, properties, effects, ExtendScript execution, and Manim integration for mathematical animations as WebP layers. The Manim integration is unique.

**[Dakkshin/after-effects-mcp](https://github.com/Dakkshin/after-effects-mcp)** — Remote control for compositions, text, shapes, solids, and properties via ExtendScript. Optimized for practical automation including effects, presets, keyframing, markers, and audio-aware tooling.

**[VoidChecksum/adobe-mcp](https://github.com/VoidChecksum/adobe-mcp)** — Full Adobe Creative Cloud automation covering Photoshop, Illustrator, Premiere Pro, After Effects, InDesign, Animate, and more from Claude.

---

## Music production servers

Music production is where MCP servers show the widest range in depth — from Ableton MCP's 15 tools (2,300 stars) to total-reaper-mcp's 600+ tools (29 stars). Adoption and comprehensiveness don't always correlate.

### The adoption leader: ahujasid/ableton-mcp

**Stars:** 2,300 | **Language:** Python | **License:** MIT | **Tools:** 15+

[ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp) is the most popular music production MCP server and one of the highest-starred creative MCP servers overall. It pioneered the creative tools MCP movement, featured in a16z and Fireship coverage.

Two-way socket-based communication: MIDI and audio track creation, instrument and effect loading from Ableton's library, MIDI clip creation and note editing, playback/session transport control, tempo adjustment and parameter management.

**Why it leads:** The 2,300 stars reflect genuine demand for AI-assisted music production. The server proved the concept and inspired an entire wave of creative tool MCP servers.

**The catch:** Relatively modest tool count compared to specialized alternatives. Limited depth in areas like arrangement view, recording, and plugin parameter control.

**Best for:** Ableton Live users who want a well-supported, battle-tested entry point to AI-assisted music production.

### The depth leader: shiehn/total-reaper-mcp

**Stars:** 29 | **Language:** Python | **License:** MIT | **Tools:** 600+

[shiehn/total-reaper-mcp](https://github.com/shiehn/total-reaper-mcp) is the most comprehensive DAW MCP server in the entire ecosystem. 600+ tools across 40+ categories: track management, media items, MIDI editing, effects/FX management, automation, transport control, bounce/rendering, groove quantization, bus routing, audio analysis, and video integration.

The key innovation is **deployment profiles**: `dsl-production` (default, 53 tools combining natural language with essential production), `dsl` (15 minimal tools), `groq-essential` (~146 ReaScript functions), `mixing` (~120 mixing tools), `full` (600+ complete toolkit). The natural language DSL supports flexible references: track names ("bass", "track 3"), volume specs ("-6dB", "50%"), and time references ("8 bars", "selection").

**Why it matters:** The profile system solves the tool-count problem that plagues large MCP servers. Many LLMs have tool count limits (Groq: 128, OpenAI: 128), and profiles keep you within them while focusing on what you need. Other large MCP servers should study this approach.

**Best for:** REAPER power users who want full DAW control with intelligent tool management.

### Also notable

**[xiaolaa2/ableton-copilot-mcp](https://github.com/xiaolaa2/ableton-copilot-mcp)** (71 stars, TypeScript, 78 commits) — Deeper Ableton functionality: Arrangement View, clip properties with piano roll, note management, audio recording, plugin loading, and operation history with rollback. Best for users who've outgrown the base Ableton MCP.

**[itsuzef/reaper-mcp](https://github.com/itsuzef/reaper-mcp)** (40 stars, Python) — Simpler REAPER interface: project creation, track management, MIDI notes, project info. Supports OSC and ReaScript dual modes. Best for REAPER beginners.

**[dschuler36/reaper-mcp-server](https://github.com/dschuler36/reaper-mcp-server)** (85 stars, Python) — Project analysis focus for REAPER.

**Logic Pro MCP servers** — [koltyj/logic-pro-mcp](https://github.com/koltyj/logic-pro-mcp) (8 tools, 7 resources, Swift) uses 5 native macOS control channels (CoreMIDI, Accessibility, CGEvent, AppleScript, OSC) with smart routing and fallback. [kiki830621/che-logic-pro-mcp](https://github.com/kiki830621/che-logic-pro-mcp) offers AppleScript + MIDI + Scripter templates. Both require macOS 14+ and Swift 6.0+.

**[Tok/SuperColliderMCP](https://github.com/Tok/SuperColliderMCP)** (17 stars, Python, 11 tools) — Algorithmic audio synthesis via OSC: melodies, drum patterns, synths, granular textures, ambient soundscapes, chord progressions, generative rhythms. Unique in the ecosystem as the only generative audio MCP server.

**[cafeTechne/ableton-11-mcp](https://github.com/cafeTechne/ableton-11-mcp)** (38 commits, Python, 220+ tools) — The most comprehensive Ableton toolset with music theory generators, chord progressions, intelligent basslines, and genre-aware drum patterns. Low stars but deep functionality.

---

## Media generation and streaming

### AI media generation

**yuvalsuede/agent-media** — CLI and MCP server with unified access to 7 AI models (Kling, Veo, Sora, Seedance, Flux, Grok Imagine) for video and image generation with 9 tools.

**burningion/video-editing-mcp** — MCP interface for Video Jungle enabling AI-driven video editing, analysis, and search within a video collection. Add videos, build projects, generate edits from multiple sources, and search for relevant clips.

### Video streaming

**[Mux MCP](https://mcp.mux.com)** — Official Mux remote MCP server for video infrastructure management. Upload videos, create live streams, generate thumbnails, add captions, manage playback policies, and query engagement analytics. Hosted at mcp.mux.com with automatic OAuth authentication. Supports query parameters to customize which tools are exposed.

**Best for:** Teams using Mux for video hosting who want AI-assisted video infrastructure management.

---

## How to choose

Use this decision flowchart:

**Need speech synthesis?** → Start with [ElevenLabs MCP](https://github.com/elevenlabs/elevenlabs-mcp) for the broadest capability. Need multi-provider flexibility? → [blacktop/mcp-tts](https://github.com/blacktop/mcp-tts). Need local/private TTS? → [kokoro-mcp-server](https://github.com/aparsoft/kokoro-mcp-server).

**Need transcription?** → [mcp-server-whisper](https://github.com/arcaputo3/mcp-server-whisper) for cloud quality with audio analysis. [local-stt-mcp](https://github.com/SmartLittleApps/local-stt-mcp) for local privacy. [mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) for YouTube videos.

**Need video processing?** → [video-creator/ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp) for common operations. [misbahsy/video-audio-mcp](https://github.com/misbahsy/video-audio-mcp) for podcast/editing workflows. [dubnium0/ffmpeg-mcp](https://github.com/dubnium0/ffmpeg-mcp) for advanced streaming/stabilization.

**Need professional NLE control?** → [DaVinci Resolve MCP](https://github.com/samuelgursky/davinci-resolve-mcp) for the deepest API coverage. [adb-mcp](https://github.com/mikechambers/adb-mcp) for multi-app Adobe control. [leancoderkavy/premiere-pro-mcp](https://github.com/leancoderkavy/premiere-pro-mcp) for dedicated Premiere Pro with 269 tools.

**Need music production?** → [Ableton MCP](https://github.com/ahujasid/ableton-mcp) for the safest, most supported entry point. [total-reaper-mcp](https://github.com/shiehn/total-reaper-mcp) for maximum depth. Logic Pro MCP servers for macOS-only workflows.

**Need video streaming infrastructure?** → [Mux MCP](https://mcp.mux.com) for upload, live streams, and analytics.

---

## Three trends worth watching

**1. Official vendor servers are raising the bar.** ElevenLabs' official MCP server (1,300 stars) combines TTS, STT, voice cloning, sound effects, and voice agents in one package. Mux offers hosted remote MCP. When vendors invest in their own MCP servers, the quality and maintenance trajectory are fundamentally different from community projects.

**2. The creative tools MCP movement is real.** Ableton MCP (2,300 stars) didn't just create a music production server — it sparked an entire category. DaVinci Resolve, Premiere Pro, After Effects, Logic Pro, REAPER, SuperCollider, and more followed. Creative professionals are genuinely adopting AI assistants for production workflows, not just experimentation.

**3. Local/private alternatives exist for everything.** Kokoro-82M for TTS. whisper.cpp for STT. FFmpeg servers for video processing. You can build a complete audio/video pipeline with zero cloud dependencies. This matters for compliance, air-gapped environments, and teams that can't send content to external APIs.

---

## What's missing

The audio and video MCP ecosystem has significant gaps:

- **No Spotify or Apple Music MCP server** — No playlist management, music metadata, or listening history integration.
- **No professional audio effects processing** — No VST/AU plugin hosting or mastering chain automation beyond what DAW servers provide.
- **No real-time audio streaming** — All servers work with files. None handle live audio streams or real-time processing.
- **No official Deepgram or AssemblyAI MCP servers** — Only community implementations exist. Given these are the two leading speech AI APIs, official servers would be impactful.
- **FFmpeg servers remain fragmented** — Six or more implementations, none dominant. The ecosystem needs consolidation.
- **No end-to-end subtitle pipeline** — Transcription and subtitle burning exist separately but no single server handles "transcribe this video and burn in the captions."
- **No GarageBand MCP server** — Apple's most accessible music tool has no MCP integration.
- **Limited safety controls** — Most video/audio servers allow arbitrary file operations without sandboxing or confirmation prompts.

These gaps represent real opportunities. An official Deepgram MCP server, a unified FFmpeg standard, or a Spotify integration would immediately fill market needs.

---

*Last updated: March 2026. Have a correction or suggestion? [Open an issue on GitHub](https://github.com/grove/chatforest.com).*

