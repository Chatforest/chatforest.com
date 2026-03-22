---
title: "Audio & Video Processing MCP Servers — ElevenLabs, FFmpeg, DaVinci Resolve, Ableton, REAPER, and More"
date: 2026-03-15T09:10:00+09:00
description: "Audio and video processing MCP servers let AI agents generate speech, transcribe audio, edit video, produce music, and control creative applications through natural language. We reviewed 30+ servers across text-to-speech (ElevenLabs official at 1,300 stars with voice cloning and sound effects, blacktop/mcp-tts with 4-provider fallback across macOS/ElevenLabs/Google/OpenAI, Kokoro community TTS with open-weight 82M model), speech-to-text (OpenAI Whisper with multi-model transcription and GPT-4o audio chat, local whisper.cpp optimized for Apple Silicon, YouTube transcript extraction at 494 stars), video editing (FFmpeg servers for format conversion/trimming/overlays/streaming, DaVinci Resolve with 342 granular tools covering 100% of the scripting API, Adobe Creative Suite control across Photoshop/Premiere/After Effects), music production (Ableton Live at 2,300 stars with socket-based DAW control, REAPER with up to 600+ tools and natural language DSL, SuperCollider for algorithmic synthesis), and media generation (agent-media with 7 AI model access for video/image creation). ElevenLabs leads the audio API space; Ableton MCP leads adoption; DaVinci Resolve has the deepest API coverage."
og_description: "Audio & Video Processing MCP servers: ElevenLabs official (1,300 stars, Python, MIT, voice cloning/TTS/transcription/sound effects/voice agents), blacktop/mcp-tts (50 stars, Go, MIT, 4-provider TTS with macOS say/ElevenLabs/Google Gemini/OpenAI), arcaputo3/mcp-server-whisper (48 stars, Python, MIT, OpenAI Whisper+GPT-4o transcription/audio chat/TTS), SmartLittleApps/local-stt-mcp (11 stars, TypeScript, MIT, whisper.cpp with speaker diarization), aparsoft/kokoro-mcp-server (6 stars, Python, Apache 2.0, Kokoro-82M open-weight TTS with audio enhancement), misbahsy/video-audio-mcp (65 stars, Python, MIT, 27 FFmpeg tools), video-creator/ffmpeg-mcp (124 stars, Python, MIT, 8 tools with video search/clip/concat/overlay), dubnium0/ffmpeg-mcp (15 stars, Python, MIT, 40+ advanced FFmpeg tools with streaming), samuelgursky/davinci-resolve-mcp (641 stars, Python, MIT, 26 compound/342 granular tools, 100% API coverage), mikechambers/adb-mcp (505 stars, JavaScript, MIT, Adobe Photoshop/Premiere/After Effects/InDesign/Illustrator control), ahujasid/ableton-mcp (2,300 stars, Python, MIT, socket-based Ableton Live control), xiaolaa2/ableton-copilot-mcp (71 stars, TypeScript, MIT, 78 commits, arrangement view/MIDI/recording), shiehn/total-reaper-mcp (29 stars, Python, MIT, 600+ tools, natural language DSL), itsuzef/reaper-mcp (40 stars, Python, MIT, project/track/MIDI/mastering), Tok/SuperColliderMCP (17 stars, Python, MIT, algorithmic synthesis via OSC), kimtaeyoon83/mcp-server-youtube-transcript (494 stars, TypeScript, MIT, transcript extraction with ad filtering). 30+ servers reviewed. Rating: 4.0/5."
content_type: "Review"
card_description: "Audio and video processing MCP servers across speech synthesis, transcription, video editing, music production, and media generation. ElevenLabs' official MCP server (1,300 stars, Python, MIT) dominates the audio API space — voice cloning, text-to-speech, transcription with speaker identification, sound effects, voice agents, and outbound calls through a single server. For local TTS, blacktop/mcp-tts (50 stars, Go) provides 4-provider fallback across macOS say, ElevenLabs, Google Gemini, and OpenAI with sequential speech enforcement via file locking. The open-weight alternative is Kokoro-82M (Apache 2.0) with 12 voices and audio enhancement. On the video side, DaVinci Resolve MCP (641 stars) has the deepest coverage — 342 granular tools mapping 100% of Resolve's scripting API with 98.5% live-tested, while Adobe's adb-mcp (505 stars) provides multi-app control across Photoshop, Premiere, After Effects, InDesign, and Illustrator. For music production, Ableton MCP (2,300 stars) leads adoption with real-time DAW control, while total-reaper-mcp (29 stars but 102 commits) offers the most comprehensive toolset at 600+ tools with a natural language DSL. The category earns 4.0/5 — strong official vendor participation from ElevenLabs and creative software vendors, diverse approaches from cloud APIs to local open-weight models, and genuine creative workflow automation that goes beyond simple file conversion."
last_refreshed: 2026-03-15
---

Audio and video processing is one of the most practically exciting areas of the MCP ecosystem. Unlike database queries or API calls, these servers let AI agents do genuinely creative work — generate speech, transcribe meetings, edit video timelines, compose music, and control professional creative applications.

The landscape divides into six areas: **text-to-speech** (cloud APIs and local models for voice synthesis), **speech-to-text** (transcription with speaker identification and format conversion), **video editing** (FFmpeg-based processing and professional NLE control), **creative application control** (DaVinci Resolve, Adobe Creative Suite), **music production** (DAW control for Ableton Live, REAPER, SuperCollider), and **media generation** (AI-powered video and image creation).

The headline findings: **ElevenLabs' official MCP server dominates cloud audio** (1,300 stars, voice cloning, TTS, transcription, sound effects, and voice agents in one server). **Ableton MCP has the highest adoption of any creative MCP server** (2,300 stars) but limited depth. **DaVinci Resolve MCP has the deepest API coverage** (342 tools, 100% of the scripting API). **total-reaper-mcp is the most comprehensive music production server** (600+ tools with natural language DSL). **FFmpeg servers are plentiful but fragmented** — no single dominant implementation. **Local/open-weight alternatives exist for both TTS and STT**, preserving privacy without cloud API dependencies. **YouTube transcript extraction is surprisingly popular** (494 stars) — a reminder that "audio processing" often starts with getting text from video.

## Text-to-Speech

### ElevenLabs (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [elevenlabs/elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp) | 1,300 | Python | 10+ | stdio |

**elevenlabs/elevenlabs-mcp** (1,300 stars, Python, MIT, 62 commits) is the official ElevenLabs MCP server and the most feature-rich audio API server in the ecosystem.

Capabilities span the full ElevenLabs platform: **Text-to-Speech** — generate speech with configurable voices, languages, and output formats. **Voice Cloning** — create custom voices from audio samples. **Voice Design** — create new synthetic voices with specific characteristics. **Transcription** — speech-to-text with speaker identification. **Sound Effects** — generate sound effects and soundscapes from text descriptions. **Audio Isolation** — separate speech from background noise. **Conversational AI** — create and manage voice agents. **Outbound Calls** — voice agents that can make phone calls.

Three output modes: `files` (save to disk), `resources` (return via MCP resources), or `both`. Enterprise data residency control via `ELEVENLABS_API_RESIDENCY`. Free tier provides 10,000 credits/month.

This is effectively a complete audio production API accessible through natural language. The breadth is unmatched — no other audio MCP server combines TTS, STT, cloning, isolation, sound effects, and voice agents.

### Multi-Provider TTS

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [blacktop/mcp-tts](https://github.com/blacktop/mcp-tts) | 50 | Go | 4 | stdio |

**blacktop/mcp-tts** (50 stars, Go, MIT, 114 commits) takes a different approach — instead of committing to one provider, it offers four TTS backends with automatic fallback:

`say_tts` — macOS built-in `say` command (zero cost, offline). `elevenlabs_tts` — ElevenLabs API for high-quality synthesis. `google_tts` — Google Gemini TTS with 30 voices. `openai_tts` — OpenAI TTS API with 10 voices and speed control (0.25x–4.0x).

The standout feature is **sequential TTS enforcement** — system-wide file locking prevents concurrent speech from multiple AI agent instances, solving a real problem when multiple agents run simultaneously. Concurrent mode available when explicitly enabled. Includes a "speak" skill for Claude Code, Codex CLI, and Gemini CLI that automatically announces plans and summaries. Cross-platform audio file saving (AIFF, MP3, WAV).

### Kokoro (Open-Weight)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [aparsoft/kokoro-mcp-server](https://github.com/aparsoft/kokoro-mcp-server) | 6 | Python | 5+ | stdio |

**aparsoft/kokoro-mcp-server** (6 stars, Python, Apache 2.0, 62 commits) wraps the Kokoro-82M open-weight TTS model — 82 million parameters delivering surprisingly good speech synthesis entirely locally, with no API keys or cloud dependencies.

Twelve voices across male and female (American and British accents). Audio post-processing pipeline: normalization, noise reduction, silence trimming, fade effects. Batch and script processing with automatic text chunking for the 510-token limit. Multi-voice podcast generation. Streaming audio output. Streamlit web interface for management. Docker deployment support. CLI, Python API, and MCP server modes.

For teams that need TTS without sending text to external APIs — compliance, privacy, air-gapped environments — this is the strongest open-weight option in the MCP ecosystem.

Other Kokoro MCP implementations: mberg/kokoro-tts-mcp (S3 upload support), giannisanni/kokoro-tts (basic generation). CodeCraftersLLC/local-voice-mcp supports both Chatterbox Turbo and Kokoro engines.

## Speech-to-Text

### OpenAI Whisper

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [arcaputo3/mcp-server-whisper](https://github.com/arcaputo3/mcp-server-whisper) | 48 | Python | 8 | stdio |

**arcaputo3/mcp-server-whisper** (48 stars, Python, MIT, 79 commits) is the most comprehensive cloud-based transcription MCP server, built on OpenAI's Whisper and GPT-4o models.

Eight tools cover the full audio processing pipeline: `list_audio_files` — search with regex patterns and metadata filtering. `get_latest_audio` — retrieve most recently modified file. `convert_audio` — transform between mp3/wav formats. `compress_audio` — reduce files exceeding size limits. `transcribe_audio` — multi-model transcription with timestamps. `chat_with_audio` — interactive GPT-4o audio analysis (ask questions about audio content). `transcribe_with_enhancement` — enhanced output modes (detailed, storytelling, professional, analytical). `create_audio` — text-to-speech with voice customization.

Type-safe responses via Pydantic models. Performance optimization through caching. The `chat_with_audio` tool is unique — it enables conversational analysis of audio content, not just transcription.

### Local Speech-to-Text

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [SmartLittleApps/local-stt-mcp](https://github.com/SmartLittleApps/local-stt-mcp) | 11 | TypeScript | 6 | stdio |

**SmartLittleApps/local-stt-mcp** (11 stars, TypeScript, MIT, 5 commits) provides completely local transcription using whisper.cpp, optimized for Apple Silicon with 15x+ real-time transcription speed.

Six tools: `transcribe` (basic transcription with automatic format conversion), `transcribe_long` (long audio with chunking), `transcribe_with_speakers` (speaker diarization), `list_models` (available Whisper models), `health_check`, `version`. Handles MP3, M4A, FLAC, OGG, WMA through automatic conversion. Output formats: txt, json, vtt, srt, csv. Under 2GB memory usage.

The privacy advantage is clear — no audio leaves the machine. The speaker diarization capability (identifying who said what) is particularly valuable for meeting transcription.

### YouTube Transcripts

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) | 494 | TypeScript | 1 | stdio |

**kimtaeyoon83/mcp-server-youtube-transcript** (494 stars, TypeScript, MIT, 48 commits) is the most popular YouTube transcript server. One tool (`get_transcript`) with smart defaults: language fallback, optional timestamps, and built-in ad/sponsorship filtering enabled by default. Accepts standard URLs, Shorts URLs, and raw video IDs. Zero external dependencies for transcript fetching.

The high star count (494 — higher than many full-featured MCP servers) reflects a common workflow: AI agents analyzing video content by reading transcripts rather than processing raw audio. Multiple alternatives exist (jkawamoto, sparfenyuk, adhikasp) but this is the standard.

## Video Processing (FFmpeg)

### FFmpeg (video-creator)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [video-creator/ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp) | 124 | Python | 8 | stdio |

**video-creator/ffmpeg-mcp** (124 stars, Python, MIT, 15 commits) provides the core FFmpeg operations most workflows need: `find_video_path` (recursive directory search), `get_video_info` (duration/fps/codec/dimensions metadata), `clip_video` (trimming), `concat_videos` (combining with quality detection), `play_video` (playback with speed/loop control), `overlay_video` (layering with positioning), `scale_video` (resizing with aspect ratio preservation), `extract_frames_from_video` (PNG/JPG/WEBP export). Currently macOS-focused (ARM64 and x86_64).

### FFmpeg (video-audio-mcp)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [misbahsy/video-audio-mcp](https://github.com/misbahsy/video-audio-mcp) | 65 | Python | 27 | stdio |

**misbahsy/video-audio-mcp** (65 stars, Python, MIT, 6 commits) is the most tool-rich FFmpeg MCP server with 27 tools spanning professional-grade editing:

**Video:** `extract_audio_from_video`, `trim_video`, `convert_video_format`, `convert_video_properties`, `change_aspect_ratio`, `set_video_resolution`, `set_video_codec`, `set_video_bitrate`, `set_video_frame_rate`. **Audio:** `convert_audio_format`, `convert_audio_properties`, `set_audio_bitrate`, `set_audio_sample_rate`, `set_audio_channels`, `set_video_audio_track_codec/bitrate/sample_rate/channels`. **Creative:** `add_subtitles`, `add_text_overlay`, `add_image_overlay`, `add_b_roll`, `add_basic_transitions`. **Editing:** `concatenate_videos`, `change_video_speed`, `remove_silence`, `health_check`.

The `remove_silence` tool is particularly useful for podcast/video editing workflows. B-roll insertion and transition effects go beyond basic conversion into actual editing.

### FFmpeg (Advanced)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [dubnium0/ffmpeg-mcp](https://github.com/dubnium0/ffmpeg-mcp) | 15 | Python | 40+ | stdio |

**dubnium0/ffmpeg-mcp** (15 stars, Python, MIT, 1 commit) has the largest tool count at 40+ across eight categories: media analysis (probing, scene detection, keyframe extraction), format conversion (transcoding, GIF generation, batch processing), video editing (trimming, merging, rotation, cropping, thumbnail generation), audio processing (volume, loudness normalization, silence removal, waveform/spectrogram visualization), visual effects (text overlays, watermarks, picture-in-picture, split-screen, slideshows), subtitle management (extraction, burning, soft insertion), streaming (HLS/DASH generation, adaptive multi-bitrate, RTMP broadcasting), and advanced operations (two-pass encoding, video stabilization, denoising, deinterlacing, custom FFmpeg command execution). The breadth is impressive but the single commit suggests early-stage development.

## Professional Video Editing

### DaVinci Resolve

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) | 641 | Python | 26/342 | stdio |

**samuelgursky/davinci-resolve-mcp** (641 stars, Python, MIT, 42 commits) has the deepest API coverage of any creative application MCP server — **100% of the DaVinci Resolve Scripting API** (324/324 methods), with 98.5% live-tested (319/324 methods).

Two modes: **Compound Server** (default, 26 tools) groups related operations by action parameter to keep LLM context windows lean — `resolve` (app control, pages, layout presets), `project_manager` (project CRUD, folders, databases), `project` (timelines, render pipeline, settings), `media_pool` (clips, folders, metadata), `timeline` (tracks, markers, export, generators), `timeline_item` (properties, markers, Fusion compositions), plus specialized tools for retime, transform, crop, composite, audio, keyframes, color grading, and galleries. **Full Server** (342 tools) exposes one tool per API method for maximum precision.

Auto-detection of OS and Resolve installation. Lazy connection recovery with auto-launch. Supports 10 MCP clients (Claude Desktop, Cursor, Windsurf, VS Code, Zed, and more). The compound/granular dual-mode approach is an excellent pattern — practical defaults with full power available.

Additional DaVinci Resolve MCP servers: apvlv/davinci-resolve-mcp, Tooflex/davinci-resolve-mcp (alternative implementations).

### Adobe Creative Suite

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [mikechambers/adb-mcp](https://github.com/mikechambers/adb-mcp) | 505 | JavaScript/Python | Multi-app | stdio |

**mikechambers/adb-mcp** (505 stars, JavaScript/Python, MIT, 212 commits) enables AI control of multiple Adobe applications through a unified MCP interface: **Photoshop** (layer management, text creation, image generation, selection tools, filters, color adjustments, clipping masks), **Premiere Pro** (clip management, transitions, effects, audio adjustment, timeline editing, sequence operations), **After Effects, InDesign, Illustrator** (ExtendScript API access for arbitrary automation).

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
| [ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp) | 2,300 | Python | 15+ | stdio (socket bridge) |

**ahujasid/ableton-mcp** (2,300 stars, Python, MIT, 25 commits) is the most popular music production MCP server and one of the highest-starred creative MCP servers overall. Two-way socket-based communication between Claude and Ableton Live.

Capabilities: MIDI and audio track creation/modification, instrument and effect loading from Ableton's library, MIDI clip creation and note editing, playback/session transport control, tempo adjustment and parameter management. The architecture uses JSON commands over TCP sockets with two components: an Ableton Remote Script (MIDI control interface) and an MCP Server (protocol implementation).

The high star count reflects genuine interest in AI-assisted music production, though the tool count is relatively modest compared to more specialized alternatives.

### Ableton Live (Copilot)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [xiaolaa2/ableton-copilot-mcp](https://github.com/xiaolaa2/ableton-copilot-mcp) | 71 | TypeScript | 20+ | stdio |

**xiaolaa2/ableton-copilot-mcp** (71 stars, TypeScript, MIT, 78 commits) builds on ableton-js for deeper functionality: Arrangement View operations, track creation/deletion/duplication, clip property configuration with piano roll integration, note management (add, delete, replace, duplicate), audio recording based on time ranges, plugin/effect loading and parameter adjustment, and operation history with rollback capability for note operations. The rollback feature is a meaningful safety addition for destructive editing operations.

Also: cafeTechne/ableton-11-mcp (38 commits, Python, 220+ tools across 21 API handler modules with music theory generators, chord progressions, intelligent basslines, genre-aware drum patterns — the most comprehensive Ableton toolset but 0 stars, suggesting it's early-stage or specialized).

### REAPER

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [shiehn/total-reaper-mcp](https://github.com/shiehn/total-reaper-mcp) | 29 | Python | 600+ | stdio |

**shiehn/total-reaper-mcp** (29 stars, Python, MIT, 102 commits) is the most comprehensive DAW MCP server in the entire ecosystem. 600+ tools across 40+ categories: track management, media items, MIDI editing, effects/FX management, automation, transport control, bounce/rendering, groove quantization, bus routing, audio analysis, and video integration.

The key innovation is **deployment profiles**: `dsl-production` (default, 53 tools combining natural language with essential production), `dsl` (15 minimal natural language tools), `groq-essential` (~146 ReaScript functions), `mixing` (~120 mixing tools), `full` (600+ complete toolkit). The natural language DSL supports flexible references: track names ("bass", "track 3"), volume specs ("-6dB", "50%"), and time references ("8 bars", "selection").

Hybrid architecture: Lua bridge for REAPER execution + Python MCP server with file-based IPC. The profile system is a mature approach to the tool-count problem that other large MCP servers should study.

### REAPER (itsuzef)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [itsuzef/reaper-mcp](https://github.com/itsuzef/reaper-mcp) | 40 | Python | 5+ | stdio |

**itsuzef/reaper-mcp** (40 stars, Python, MIT, 3 commits) provides a simpler REAPER interface: `create_project`, `create_track`, `list_tracks`, `add_midi_note`, `get_project_info`. Supports OSC (Open Sound Control) and ReaScript dual modes. Cross-platform startup scripts for macOS, Linux, and Windows.

Also: dschuler36/reaper-mcp-server (85 stars, project analysis focus), wegitor/reaper-reapy-mcp (reapy-based control).

### SuperCollider

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [Tok/SuperColliderMCP](https://github.com/Tok/SuperColliderMCP) | 17 | Python | 11 | stdio |

**Tok/SuperColliderMCP** (17 stars, Python, MIT, 12 commits) connects AI agents to SuperCollider for algorithmic audio synthesis via OSC messages. Eleven tools: `play_example_osc`, `play_melody`, `create_drum_pattern`, `play_synth`, `create_sequence`, `create_lfo_modulation`, `create_layered_synth`, `create_granular_texture`, `create_chord_progression`, `create_ambient_soundscape`, `create_generative_rhythm`.

The tools serve as customizable templates — designed for AI agents to extend rather than use directly. Supports procedurally generated melodies with customizable scales, granular synthesis, and ambient soundscape generation. Unique in the ecosystem as the only algorithmic/generative audio MCP server.

## Media Generation & Analysis

### Agent Media

AI-powered media generation through multiple model providers. yuvalsuede/agent-media provides CLI and MCP server with unified access to 7 AI models (Kling, Veo, Sora, Seedance, Flux, Grok Imagine) for video and image generation with 9 tools.

### Video Editing (AI-Driven)

burningion/video-editing-mcp — MCP Interface for Video Jungle, enabling AI-driven video editing, analysis, and search within a video collection. Add videos, build projects, generate edits from multiple sources, and search for relevant clips.

## What's Missing

The audio and video MCP ecosystem has notable gaps:

- **No Spotify or Apple Music MCP server** for playlist management or music metadata
- **No professional audio effects processing** — no VST/AU plugin hosting, no mastering chain automation beyond what DAW servers provide
- **No real-time audio streaming** — all servers work with files, none handle live audio streams
- **No video conferencing integration** — no Zoom/Teams/Meet recording or transcription MCP servers
- **No Deepgram or AssemblyAI official MCP servers** — only community implementations exist (reddheeraj/Deepgram-MCP wraps the TTS API only)
- **No Premiere Pro dedicated MCP server** — only available through adb-mcp's multi-app approach
- **No Blender MCP server** for 3D animation and video compositing
- **Limited safety controls** — most video/audio servers allow arbitrary file operations without sandboxing or confirmation
- **FFmpeg servers are fragmented** — no single dominant implementation, making it hard to recommend one
- **No subtitle/caption generation pipeline** — transcription and subtitle burning exist separately but no end-to-end solution

## The Bottom Line

**Rating: 4.0 / 5**

The audio and video MCP ecosystem earns 4.0/5 for breadth, official vendor participation, and genuine creative utility. ElevenLabs provides the most complete audio API server. DaVinci Resolve has the deepest application integration. REAPER's total-reaper-mcp demonstrates what comprehensive DAW control looks like with its profile system and 600+ tools. Ableton MCP's 2,300 stars prove real demand for AI-assisted music production.

The rating reflects both strengths and opportunities. On the positive side: strong official servers (ElevenLabs, DaVinci Resolve), mature multi-provider approaches (blacktop/mcp-tts), open-weight alternatives for privacy (Kokoro, whisper.cpp), and innovative patterns (REAPER's deployment profiles, DaVinci Resolve's compound/granular dual mode). On the gap side: no real-time audio, fragmented FFmpeg landscape, limited safety controls, and missing official servers from major speech AI providers (Deepgram, AssemblyAI).

For **text-to-speech**, start with ElevenLabs if cloud APIs are acceptable, or Kokoro for local/private deployment. For **transcription**, use OpenAI Whisper MCP for cloud quality or local-stt-mcp for privacy. For **video editing**, choose DaVinci Resolve MCP for professional NLE control or misbahsy/video-audio-mcp for FFmpeg-based processing. For **music production**, Ableton MCP is the safe choice for adoption, but total-reaper-mcp offers dramatically more depth for REAPER users.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
