# Audio & Video Processing MCP Servers — ElevenLabs, FFmpeg, DaVinci Resolve, Ableton, REAPER, and More

> Audio and video processing MCP servers let AI agents generate speech, transcribe audio, edit video, produce music, and control creative applications through natural language.


Audio and video processing is one of the most practically exciting areas of the MCP ecosystem. Unlike database queries or API calls, these servers let AI agents do genuinely creative work — generate speech, transcribe meetings, edit video timelines, compose music, and control professional creative applications.

The landscape divides into seven areas: **text-to-speech** (cloud APIs and local models for voice synthesis), **speech-to-text** (transcription with speaker identification and format conversion), **video editing** (FFmpeg-based processing and professional NLE control), **creative application control** (DaVinci Resolve, Adobe Creative Suite), **music production** (DAW control for Ableton Live, REAPER, SuperCollider), **streaming services** (Spotify playlist and playback control), and **media generation** (AI-powered video and image creation).

The headline findings: **ElevenLabs' official MCP server dominates cloud audio** (1,300 stars, 24 tools — voice cloning, TTS, speech-to-speech, music composition, transcription, sound effects, and voice agents in one server). **Ableton MCP has the highest adoption of any creative MCP server** (2,400 stars) but limited depth. **DaVinci Resolve MCP has the deepest API coverage and fastest growth** (866 stars, +35% since March, 342 tools, 100% of the scripting API, now with Fusion node graph control). **total-reaper-mcp is the most comprehensive music production server** (600+ tools with natural language DSL), while **itsuzef/reaper-mcp underwent a major rewrite** (5→58 tools, now on PyPI). **FFmpeg servers are plentiful but fragmented and stale** — all three reviewed implementations are dormant. **Local/open-weight alternatives are expanding** — Kokoro, Chatterbox, and Qwen3-TTS for TTS; whisper.cpp for STT. **Spotify MCP servers have arrived** (312 stars), filling a previously noted gap. **YouTube transcript extraction remains popular** (529 stars) with yt-dlp-mcp (233 stars) as a broader alternative.

## Text-to-Speech

### ElevenLabs (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [elevenlabs/elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp) | 1,300 | Python | 24 | stdio |

**elevenlabs/elevenlabs-mcp** (1,300 stars, Python, MIT, 63 commits) is the official ElevenLabs MCP server and the most feature-rich audio API server in the ecosystem, with **24 tools** spanning the full platform.

Capabilities: **Text-to-Speech** — generate speech with configurable voices, languages, and output formats. **Speech-to-Speech** — voice conversion with style transfer. **Voice Cloning** — create custom voices from audio samples. **Voice Design** — create and preview new synthetic voices. **Transcription** — speech-to-text with speaker identification. **Sound Effects** — generate sound effects and soundscapes from text descriptions. **Music Composition** — `compose_music` and `create_composition_plan` for AI-generated music. **Audio Isolation** — separate speech from background noise. **Conversational AI** — create and manage voice agents with knowledge bases. **Outbound Calls** — voice agents that can make phone calls. **Voice Library** — search and browse the shared voice library. **Phone Numbers** — list available phone numbers for voice agents.

Three output modes: `files` (save to disk), `resources` (return via MCP resources), or `both`. Enterprise data residency control via `ELEVENLABS_API_RESIDENCY` with `eu`/`in` shorthand aliases. Free tier provides 10,000 credits/month. MCP tool annotations on all 24 tools. Supports Gemini Extensions and Python 3.14.

This is effectively a complete audio production API accessible through natural language. The breadth is unmatched — no other audio MCP server combines TTS, STT, speech-to-speech, music composition, cloning, isolation, sound effects, and voice agents.

### Multi-Provider TTS

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [blacktop/mcp-tts](https://github.com/blacktop/mcp-tts) | 56 | Go | 4 | stdio |

**blacktop/mcp-tts** (56 stars, Go, MIT, 116 commits) takes a different approach — instead of committing to one provider, it offers four TTS backends with automatic fallback. Notably, this is one of the few servers in the category still actively maintained (last commit April 2026).

`say_tts` — macOS built-in `say` command (zero cost, offline). `elevenlabs_tts` — ElevenLabs API for high-quality synthesis. `google_tts` — Google Gemini TTS with 30 voices. `openai_tts` — OpenAI TTS API including `gpt-4o-mini-tts` with 10 voices and speed control (0.25x–4.0x).

The standout feature is **sequential TTS enforcement** — system-wide file locking prevents concurrent speech from multiple AI agent instances, solving a real problem when multiple agents run simultaneously. Concurrent mode available when explicitly enabled. Includes a "speak" skill for Claude Code, Codex CLI, and Gemini CLI that automatically announces plans and summaries. Cross-platform audio file saving (AIFF, MP3, WAV).

### Kokoro (Open-Weight)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [aparsoft/kokoro-mcp-server](https://github.com/aparsoft/kokoro-mcp-server) | 8 | Python | 5+ | stdio |

**aparsoft/kokoro-mcp-server** (8 stars, Python, Apache 2.0, 62 commits) wraps the Kokoro-82M open-weight TTS model — 82 million parameters delivering surprisingly good speech synthesis entirely locally, with no API keys or cloud dependencies.

Twelve voices across male and female (American and British accents). Audio post-processing pipeline: normalization, noise reduction, silence trimming, fade effects. Batch and script processing with automatic text chunking for the 510-token limit. Multi-voice podcast generation. Streaming audio output. Streamlit web interface for management. Docker deployment support. CLI, Python API, and MCP server modes.

For teams that need TTS without sending text to external APIs — compliance, privacy, air-gapped environments — this is the strongest open-weight option in the MCP ecosystem.

Other Kokoro MCP implementations: mberg/kokoro-tts-mcp (S3 upload support), giannisanni/kokoro-tts (basic generation). CodeCraftersLLC/local-voice-mcp supports both Chatterbox Turbo and Kokoro engines.

**New open-weight TTS options since March 2026:** digitarald/chatterbox-mcp (10 stars, Python) wraps the Chatterbox TTS model with expressiveness controls and automatic playback. neosun100/qwen3-tts (12 stars, Python) provides an all-in-one Docker deployment for Qwen3-TTS with 10-language support, voice cloning, and both REST API and MCP server modes. Neither has matched Kokoro's maturity yet, but they expand the local TTS options.

## Speech-to-Text

### OpenAI Whisper

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [arcaputo3/mcp-server-whisper](https://github.com/arcaputo3/mcp-server-whisper) | 52 | Python | 8 | stdio |

**arcaputo3/mcp-server-whisper** (52 stars, Python, MIT, 79 commits) is the most comprehensive cloud-based transcription MCP server, built on OpenAI's Whisper and GPT-4o models.

Eight tools cover the full audio processing pipeline: `list_audio_files` — search with regex patterns and metadata filtering. `get_latest_audio` — retrieve most recently modified file. `convert_audio` — transform between mp3/wav formats. `compress_audio` — reduce files exceeding size limits. `transcribe_audio` — multi-model transcription with timestamps. `chat_with_audio` — interactive GPT-4o audio analysis (ask questions about audio content). `transcribe_with_enhancement` — enhanced output modes (detailed, storytelling, professional, analytical). `create_audio` — text-to-speech with voice customization.

Type-safe responses via Pydantic models. Performance optimization through caching. The `chat_with_audio` tool is unique — it enables conversational analysis of audio content, not just transcription.

### Local Speech-to-Text

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [SmartLittleApps/local-stt-mcp](https://github.com/SmartLittleApps/local-stt-mcp) | 12 | TypeScript | 6 | stdio |

**SmartLittleApps/local-stt-mcp** (12 stars, TypeScript, MIT, 5 commits) provides completely local transcription using whisper.cpp, optimized for Apple Silicon with 15x+ real-time transcription speed.

Six tools: `transcribe` (basic transcription with automatic format conversion), `transcribe_long` (long audio with chunking), `transcribe_with_speakers` (speaker diarization), `list_models` (available Whisper models), `health_check`, `version`. Handles MP3, M4A, FLAC, OGG, WMA through automatic conversion. Output formats: txt, json, vtt, srt, csv. Under 2GB memory usage.

The privacy advantage is clear — no audio leaves the machine. The speaker diarization capability (identifying who said what) is particularly valuable for meeting transcription.

### YouTube Transcripts

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) | 529 | TypeScript | 1 | stdio |

**kimtaeyoon83/mcp-server-youtube-transcript** (529 stars, TypeScript, MIT, 48 commits) is the most popular YouTube transcript server. One tool (`get_transcript`) with smart defaults: language fallback, optional timestamps, and built-in ad/sponsorship filtering enabled by default. Accepts standard URLs, Shorts URLs, and raw video IDs. Zero external dependencies for transcript fetching.

The high star count (529 — higher than many full-featured MCP servers) reflects a common workflow: AI agents analyzing video content by reading transcripts rather than processing raw audio. Multiple alternatives exist (jkawamoto, sparfenyuk, adhikasp) but this is the standard.

**kevinwatt/yt-dlp-mcp** (233 stars, TypeScript, 83 commits) takes a broader approach — bridging yt-dlp with MCP for video search, download, and transcript extraction. More actively maintained than the transcript-only servers and useful when you need the actual media files, not just text.

## Video Processing (FFmpeg)

### FFmpeg (video-creator)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [video-creator/ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp) | 132 | Python | 8 | stdio |

**video-creator/ffmpeg-mcp** (132 stars, Python, MIT, 15 commits) provides the core FFmpeg operations most workflows need: `find_video_path` (recursive directory search), `get_video_info` (duration/fps/codec/dimensions metadata), `clip_video` (trimming), `concat_videos` (combining with quality detection), `play_video` (playback with speed/loop control), `overlay_video` (layering with positioning), `scale_video` (resizing with aspect ratio preservation), `extract_frames_from_video` (PNG/JPG/WEBP export). Currently macOS-focused (ARM64 and x86_64).

### FFmpeg (video-audio-mcp)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [misbahsy/video-audio-mcp](https://github.com/misbahsy/video-audio-mcp) | 71 | Python | 27 | stdio |

**misbahsy/video-audio-mcp** (71 stars, Python, MIT, 6 commits) is the most tool-rich FFmpeg MCP server with 27 tools spanning professional-grade editing:

**Video:** `extract_audio_from_video`, `trim_video`, `convert_video_format`, `convert_video_properties`, `change_aspect_ratio`, `set_video_resolution`, `set_video_codec`, `set_video_bitrate`, `set_video_frame_rate`. **Audio:** `convert_audio_format`, `convert_audio_properties`, `set_audio_bitrate`, `set_audio_sample_rate`, `set_audio_channels`, `set_video_audio_track_codec/bitrate/sample_rate/channels`. **Creative:** `add_subtitles`, `add_text_overlay`, `add_image_overlay`, `add_b_roll`, `add_basic_transitions`. **Editing:** `concatenate_videos`, `change_video_speed`, `remove_silence`, `health_check`.

The `remove_silence` tool is particularly useful for podcast/video editing workflows. B-roll insertion and transition effects go beyond basic conversion into actual editing.

### FFmpeg (Advanced)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [dubnium0/ffmpeg-mcp](https://github.com/dubnium0/ffmpeg-mcp) | 16 | Python | 40+ | stdio |

**dubnium0/ffmpeg-mcp** (16 stars, Python, MIT, 1 commit) has the largest tool count at 40+ across eight categories: media analysis (probing, scene detection, keyframe extraction), format conversion (transcoding, GIF generation, batch processing), video editing (trimming, merging, rotation, cropping, thumbnail generation), audio processing (volume, loudness normalization, silence removal, waveform/spectrogram visualization), visual effects (text overlays, watermarks, picture-in-picture, split-screen, slideshows), subtitle management (extraction, burning, soft insertion), streaming (HLS/DASH generation, adaptive multi-bitrate, RTMP broadcasting), and advanced operations (two-pass encoding, video stabilization, denoising, deinterlacing, custom FFmpeg command execution). The breadth is impressive but the single commit suggests early-stage development.

## Professional Video Editing

### DaVinci Resolve

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) | 866 | Python | 27/342 | stdio |

**samuelgursky/davinci-resolve-mcp** (866 stars, Python, MIT, 47 commits) has the deepest API coverage of any creative application MCP server — **100% of the DaVinci Resolve Scripting API** (324/324 methods), with 98.5% live-tested (319/324 methods). Star growth has been exceptional (+35% since March 2026).

**Six releases since March 2026** (v2.0.5 through v2.1.0): **v2.0.5–v2.0.6** — lazy connection recovery, null guards, crash fix in timeline_item_color. **v2.0.7** — path traversal protection for layout preset tools (security fix). **v2.0.8** — new `grab_and_export` action combining still capture + export in a single atomic call. **v2.0.9** — cross-platform sandbox path handling (macOS, Linux, Windows) with automatic cleanup. **v2.1.0** — **new Fusion composition node graph tool** (Tool 27 in compound server) with 20 actions for node management, wiring, parameters, keyframes, and composition control. Also added cache control for Fusion output on timeline items.

Two modes: **Compound Server** (default, now 27 tools) groups related operations by action parameter to keep LLM context windows lean — `resolve` (app control, pages, layout presets), `project_manager` (project CRUD, folders, databases), `project` (timelines, render pipeline, settings), `media_pool` (clips, folders, metadata), `timeline` (tracks, markers, export, generators), `timeline_item` (properties, markers, Fusion compositions), `fusion` (node graph management), plus specialized tools for retime, transform, crop, composite, audio, keyframes, color grading, and galleries. **Full Server** (342 tools) exposes one tool per API method for maximum precision.

Auto-detection of OS and Resolve installation. Lazy connection recovery with auto-launch. Supports 10 MCP clients (Claude Desktop, Cursor, Windsurf, VS Code, Zed, and more). The compound/granular dual-mode approach is an excellent pattern — practical defaults with full power available.

Additional DaVinci Resolve MCP servers: apvlv/davinci-resolve-mcp, Tooflex/davinci-resolve-mcp (alternative implementations).

### Adobe Creative Suite

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [mikechambers/adb-mcp](https://github.com/mikechambers/adb-mcp) | 576 | JavaScript/Python | Multi-app | stdio |

**mikechambers/adb-mcp** (576 stars, JavaScript/Python, MIT, 212 commits) enables AI control of multiple Adobe applications through a unified MCP interface: **Photoshop** (layer management, text creation, image generation, selection tools, filters, color adjustments, clipping masks), **Premiere Pro** (clip management, transitions, effects, audio adjustment, timeline editing, sequence operations), **After Effects, InDesign, Illustrator** (ExtendScript API access for arbitrary automation).

Architecture: AI ↔ MCP Server ↔ Node Proxy Server ↔ Adobe Plugin ↔ Application. The proxy is necessary because UXP plugins can only connect as clients, not listen as servers. Not endorsed or supported by Adobe — this is a proof-of-concept but with significant adoption (505 stars, 212 commits).

### Adobe After Effects (Dedicated)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [sunqirui1987/ae-mcp](https://github.com/sunqirui1987/ae-mcp) | 7 | Go/JavaScript | 9+ | stdio |

**sunqirui1987/ae-mcp** (7 stars, Go/JavaScript, MIT, 10 commits) focuses specifically on After Effects with an extensible tool architecture: project information, composition creation, text and solid layers, shape layers (rectangles, ellipses, polygons, stars with vertex/tangent/feathering control), layer properties (position, scale, rotation, opacity), effects browsing and application, ExtendScript execution, and Manim integration for mathematical animations as WebP layers. The Manim integration is a unique feature — generating mathematical visualizations directly as After Effects layers.

Also: p10q/ae-mcp provides a file-based communication bridge for After Effects control.

## Music Production

### Ableton Live

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp) | 2,400 | Python | 15+ | stdio (socket bridge) |

**ahujasid/ableton-mcp** (2,400 stars, Python, MIT, 25 commits) is the most popular music production MCP server and one of the highest-starred creative MCP servers overall. Two-way socket-based communication between Claude and Ableton Live.

Capabilities: MIDI and audio track creation/modification, instrument and effect loading from Ableton's library, MIDI clip creation and note editing, playback/session transport control, tempo adjustment and parameter management. The architecture uses JSON commands over TCP sockets with two components: an Ableton Remote Script (MIDI control interface) and an MCP Server (protocol implementation).

The high star count reflects genuine interest in AI-assisted music production, though the tool count is relatively modest compared to more specialized alternatives.

### Ableton Live (Copilot)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [xiaolaa2/ableton-copilot-mcp](https://github.com/xiaolaa2/ableton-copilot-mcp) | 73 | TypeScript | 20+ | stdio |

**xiaolaa2/ableton-copilot-mcp** (73 stars, TypeScript, MIT, 78 commits) builds on ableton-js for deeper functionality: Arrangement View operations, track creation/deletion/duplication, clip property configuration with piano roll integration, note management (add, delete, replace, duplicate), audio recording based on time ranges, plugin/effect loading and parameter adjustment, and operation history with rollback capability for note operations. The rollback feature is a meaningful safety addition for destructive editing operations.

Also: cafeTechne/ableton-11-mcp (38 commits, Python, 220+ tools across 21 API handler modules with music theory generators, chord progressions, intelligent basslines, genre-aware drum patterns — the most comprehensive Ableton toolset but 0 stars, suggesting it's early-stage or specialized).

### REAPER

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [shiehn/total-reaper-mcp](https://github.com/shiehn/total-reaper-mcp) | 41 | Python | 600+ | stdio |

**shiehn/total-reaper-mcp** (41 stars, Python, MIT, 102 commits) is the most comprehensive DAW MCP server in the entire ecosystem. 600+ tools across 40+ categories: track management, media items, MIDI editing, effects/FX management, automation, transport control, bounce/rendering, groove quantization, bus routing, audio analysis, and video integration.

The key innovation is **deployment profiles**: `dsl-production` (default, 53 tools combining natural language with essential production), `dsl` (15 minimal natural language tools), `groq-essential` (~146 ReaScript functions), `mixing` (~120 mixing tools), `full` (600+ complete toolkit). The natural language DSL supports flexible references: track names ("bass", "track 3"), volume specs ("-6dB", "50%"), and time references ("8 bars", "selection").

Hybrid architecture: Lua bridge for REAPER execution + Python MCP server with file-based IPC. The profile system is a mature approach to the tool-count problem that other large MCP servers should study.

### REAPER (itsuzef)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [itsuzef/reaper-mcp](https://github.com/itsuzef/reaper-mcp) | 55 | Python | 58 | stdio |

**itsuzef/reaper-mcp** (55 stars, Python, MIT, 7 commits) underwent a **major rewrite in late March 2026**. The previous version offered 5 basic tools via OSC; the new version replaces the entire architecture with python-reapy, expands to **58 tools** organized in modular tool files, and is now published on PyPI as `reaper-mcp-server` (v0.1.0). Also appears under "bonfire-audio" org branding. This transforms it from a minimal proof-of-concept into a credible alternative to total-reaper-mcp, though with fewer tools (58 vs 600+) in exchange for simpler setup via PyPI.

Also: dschuler36/reaper-mcp-server (95 stars, project analysis focus), wegitor/reaper-reapy-mcp (reapy-based control).

### SuperCollider

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [Tok/SuperColliderMCP](https://github.com/Tok/SuperColliderMCP) | 20 | Python | 11 | stdio |

**Tok/SuperColliderMCP** (20 stars, Python, MIT, 12 commits) connects AI agents to SuperCollider for algorithmic audio synthesis via OSC messages. Eleven tools: `play_example_osc`, `play_melody`, `create_drum_pattern`, `play_synth`, `create_sequence`, `create_lfo_modulation`, `create_layered_synth`, `create_granular_texture`, `create_chord_progression`, `create_ambient_soundscape`, `create_generative_rhythm`.

The tools serve as customizable templates — designed for AI agents to extend rather than use directly. Supports procedurally generated melodies with customizable scales, granular synthesis, and ambient soundscape generation. Unique in the ecosystem as the only algorithmic/generative audio MCP server.

## Streaming & Media Services

### Spotify

**marcelmarais/spotify-mcp-server** (312 stars, TypeScript, updated March 2026) is the first notable Spotify MCP server — providing playlist management, playback control, and music metadata access through the Spotify API. This fills a gap that was explicitly noted in our previous review. Also: iceener/spotify-streamable-mcp-server (78 stars, TypeScript, Hono.dev-based Spotify API integration, updated February 2026).

The emergence of Spotify MCP servers is significant — music metadata and playlist management were previously absent from the ecosystem entirely.

## Media Generation & Analysis

### Agent Media

AI-powered media generation through multiple model providers. yuvalsuede/agent-media provides CLI and MCP server with unified access to 7 AI models (Kling, Veo, Sora, Seedance, Flux, Grok Imagine) for video and image generation with 9 tools.

### Video Editing (AI-Driven)

burningion/video-editing-mcp — MCP Interface for Video Jungle, enabling AI-driven video editing, analysis, and search within a video collection. Add videos, build projects, generate edits from multiple sources, and search for relevant clips.

## What's Missing

The audio and video MCP ecosystem has notable gaps:

- **~~No Spotify or Apple Music MCP server~~** — **Spotify MCP servers now exist** (marcelmarais at 312 stars), but Apple Music remains absent
- **No professional audio effects processing** — no VST/AU plugin hosting, no mastering chain automation beyond what DAW servers provide
- **No real-time audio streaming** — all servers work with files, none handle live audio streams
- **No video conferencing integration** — no Zoom/Teams/Meet recording or transcription MCP servers
- **No Deepgram or AssemblyAI official MCP servers** — AssemblyAI-Community/assemblyai-mcp exists (0 stars, 1 commit, Feb 2026) but is barely launched. Deepgram still has only minor community wrappers
- **No Premiere Pro dedicated MCP server** — only available through adb-mcp's multi-app approach
- **No Blender MCP server** for 3D animation and video compositing
- **Limited safety controls** — most video/audio servers allow arbitrary file operations without sandboxing or confirmation (DaVinci Resolve's v2.0.7 path traversal fix is a welcome exception)
- **FFmpeg servers are fragmented** — no single dominant implementation, and all three reviewed FFmpeg servers are stale (no commits in 6+ months)
- **No subtitle/caption generation pipeline** — transcription and subtitle burning exist separately but no end-to-end solution
- **Open-weight voice model coverage is thin** — major models like Sesame/CSM, Dia (Nari Labs), F5-TTS, Parler TTS, and Fish Speech have no notable MCP server implementations yet

## The Bottom Line

**Rating: 4.0 / 5**

The audio and video MCP ecosystem earns 4.0/5 for breadth, official vendor participation, and genuine creative utility. ElevenLabs provides the most complete audio API server (24 tools). DaVinci Resolve has the deepest application integration and fastest star growth (+35%). REAPER's total-reaper-mcp demonstrates what comprehensive DAW control looks like with its profile system and 600+ tools, while itsuzef/reaper-mcp's rewrite (now 58 tools, PyPI-published) shows the REAPER ecosystem maturing. Ableton MCP's 2,400 stars prove real demand for AI-assisted music production.

The rating reflects both strengths and opportunities. On the positive side: strong official servers (ElevenLabs, DaVinci Resolve), mature multi-provider approaches (blacktop/mcp-tts — the only actively maintained TTS server), expanding open-weight options (Kokoro, Chatterbox, Qwen3-TTS), new streaming service access (Spotify at 312 stars), and innovative patterns (REAPER's deployment profiles, DaVinci Resolve's compound/granular dual mode with new Fusion support). On the gap side: FFmpeg servers are all dormant, many open-weight voice models lack MCP integrations, no real-time audio streaming, and missing official servers from major speech AI providers (Deepgram, AssemblyAI).

For **text-to-speech**, start with ElevenLabs if cloud APIs are acceptable, or Kokoro for local/private deployment (with Chatterbox and Qwen3-TTS as emerging alternatives). For **transcription**, use OpenAI Whisper MCP for cloud quality or local-stt-mcp for privacy. For **video editing**, choose DaVinci Resolve MCP for professional NLE control or misbahsy/video-audio-mcp for FFmpeg-based processing. For **music production**, Ableton MCP is the safe choice for adoption, but total-reaper-mcp offers dramatically more depth for REAPER users, and itsuzef/reaper-mcp now provides a quick-start option via PyPI.

**Category**: [Design & Creative MCP Servers](/categories/design-creative/)

*This review was last edited on 2026-04-24 using Claude Opus 4.6 (Anthropic).*

