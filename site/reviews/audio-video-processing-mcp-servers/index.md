# Audio & Video Processing MCP Servers — ElevenLabs, FFmpeg, DaVinci Resolve, Ableton, REAPER, and More

> Audio and video processing MCP servers let AI agents generate speech, transcribe audio, edit video, produce music, and control creative applications through natural language.


Audio and video processing is one of the most practically exciting areas of the MCP ecosystem. Unlike database queries or API calls, these servers let AI agents do genuinely creative work — generate speech, transcribe meetings, edit video timelines, compose music, and control professional creative applications.

The landscape divides into seven areas: **text-to-speech** (cloud APIs and local models for voice synthesis), **speech-to-text** (transcription with speaker identification and format conversion), **video editing** (FFmpeg-based processing and professional NLE control), **creative application control** (DaVinci Resolve, Adobe Creative Suite), **music production** (DAW control for Ableton Live, REAPER, SuperCollider), **streaming services** (Spotify playlist and playback control), and **media generation** (AI-powered video and image creation).

The headline findings: **ElevenLabs' official MCP server dominates cloud audio** ([1,522 stars](https://github.com/elevenlabs/elevenlabs-mcp), 24 tools — voice cloning, TTS, speech-to-speech, music composition, transcription, sound effects, and voice agents in one server). **Deepgram now has an official MCP** (deepgram/mcp) with dynamic tool loading — speech recognition and TTS tools that automatically expand as Deepgram adds API capabilities, closing a gap noted in previous reviews. **Descript has launched an official hosted MCP** (api.descript.com/v2/mcp) covering the full Underlord editing toolkit: filler removal, Studio Sound cleanup, automatic captioning, and B-roll suggestions. **Ableton MCP has the highest adoption of any creative MCP server** ([2,903 stars](https://github.com/ahujasid/ableton-mcp)) but limited depth. **DaVinci Resolve MCP has the deepest application integration** ([2,120 stars](https://github.com/samuelgursky/davinci-resolve-mcp), 353 tools, 100% of the scripting API methods, Fusion node graph + Fairlight audio post-production). **total-reaper-mcp is the most comprehensive music production server** (600+ tools with natural language DSL), while **itsuzef/reaper-mcp** (58 tools, PyPI) provides a simpler entry point. **FFmpeg servers have a new leader** — the KyaniteLabs project (formerly `mcp-video`, [now renamed `kinocut`](https://github.com/KyaniteLabs/kinocut), 196 MCP tools + 167 CLI commands), while the original implementations show mixed maintenance. **Local/open-weight alternatives are expanding** — Kokoro, Chatterbox, and Qwen3-TTS for TTS; whisper.cpp for STT. **Spotify MCP** (424 stars) fills the streaming gap. **YouTube transcript extraction remains popular** (582 stars) with yt-dlp-mcp (268 stars) as a broader alternative.

## Text-to-Speech

### ElevenLabs (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [elevenlabs/elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp) | 1,522 | Python | 24 | stdio |

**elevenlabs/elevenlabs-mcp** ([1,522 stars](https://github.com/elevenlabs/elevenlabs-mcp), Python, MIT, 78 commits) is the official ElevenLabs MCP server and the most feature-rich audio API server in the ecosystem, with **24 tools** spanning the full platform.

Capabilities: **Text-to-Speech** — generate speech with configurable voices, languages, and output formats. **Speech-to-Speech** — voice conversion with style transfer. **Voice Cloning** — create custom voices from audio samples. **Voice Design** — create and preview new synthetic voices. **Transcription** — speech-to-text with speaker identification. **Sound Effects** — generate sound effects and soundscapes from text descriptions. **Music Composition** — `compose_music` and `create_composition_plan` for AI-generated music. **Audio Isolation** — separate speech from background noise. **Conversational AI** — create and manage voice agents with knowledge bases. **Outbound Calls** — voice agents that can make phone calls. **Voice Library** — search and browse the shared voice library. **Phone Numbers** — list available phone numbers for voice agents.

Three output modes: `files` (save to disk), `resources` (return via MCP resources), or `both`. Enterprise data residency control via `ELEVENLABS_API_RESIDENCY` with `eu`/`in` shorthand aliases. Free tier provides [10,000 credits/month](https://elevenlabs.io/pricing). MCP tool annotations on all 24 tools. Supports Gemini Extensions and Python 3.14.

This is effectively a complete audio production API accessible through natural language. The breadth is unmatched — no other audio MCP server combines TTS, STT, speech-to-speech, music composition, cloning, isolation, sound effects, and voice agents.

### Multi-Provider TTS

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [blacktop/mcp-tts](https://github.com/blacktop/mcp-tts) | 65 | Go | 4 | stdio |

**blacktop/mcp-tts** ([65 stars](https://github.com/blacktop/mcp-tts), Go, MIT) takes a different approach — instead of committing to one provider, it offers four TTS backends with automatic fallback. Notably, this is one of the few servers in the category still actively maintained (commits as recently as August 2026).

`say_tts` — macOS built-in `say` command (zero cost, offline). `elevenlabs_tts` — ElevenLabs API for high-quality synthesis. `google_tts` — Google Gemini TTS with 30 voices. `openai_tts` — OpenAI TTS API including `gpt-4o-mini-tts` with 10 voices and speed control (0.25x–4.0x).

The standout feature is **sequential TTS enforcement** — system-wide file locking prevents concurrent speech from multiple AI agent instances, solving a real problem when multiple agents run simultaneously. Concurrent mode available when explicitly enabled. Includes a "speak" skill for Claude Code, Codex CLI, and Gemini CLI that automatically announces plans and summaries. Cross-platform audio file saving (AIFF, MP3, WAV).

### Kokoro (Open-Weight)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [aparsoft/kokoro-mcp-server](https://github.com/aparsoft/kokoro-mcp-server) | 14 | Python | 5+ | stdio |

**aparsoft/kokoro-mcp-server** ([14 stars](https://github.com/aparsoft/kokoro-mcp-server), Python, Apache 2.0) wraps the Kokoro-82M open-weight TTS model — 82 million parameters delivering surprisingly good speech synthesis entirely locally, with no API keys or cloud dependencies.

Twelve voices across male and female (American and British accents). Audio post-processing pipeline: normalization, noise reduction, silence trimming, fade effects. Batch and script processing with automatic text chunking for the 510-token limit. Multi-voice podcast generation. Streaming audio output. Streamlit web interface for management. Docker deployment support. CLI, Python API, and MCP server modes.

For teams that need TTS without sending text to external APIs — compliance, privacy, air-gapped environments — this is the strongest open-weight option in the MCP ecosystem.

Other Kokoro MCP implementations: mberg/kokoro-tts-mcp (S3 upload support), giannisanni/kokoro-tts (basic generation). CodeCraftersLLC/local-voice-mcp supports both Chatterbox Turbo and Kokoro engines.

**New open-weight TTS options since March 2026:** [digitarald/chatterbox-mcp](https://github.com/digitarald/chatterbox-mcp) (12 stars, Python) wraps the Chatterbox TTS model with expressiveness controls and automatic playback. [neosun100/qwen3-tts](https://github.com/neosun100/qwen3-tts) (15 stars, Python) provides an all-in-one Docker deployment for Qwen3-TTS with 10-language support, voice cloning, and both REST API and MCP server modes. Neither has matched Kokoro's maturity yet, but they expand the local TTS options.

## Speech-to-Text

### Deepgram (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [deepgram/mcp](https://github.com/deepgram/mcp) | 1 | — | Dynamic | stdio |

**deepgram/mcp** is Deepgram's official MCP server, launched in May 2026. The defining feature is **dynamic tool loading** — tools are fetched directly from Deepgram's API at runtime, so new capabilities appear automatically without requiring a package upgrade. Current capabilities span speech recognition (transcription with language detection) and text-to-speech synthesis. Documented at [developers.deepgram.com/cli/mcp-server](https://developers.deepgram.com/cli/mcp-server).

The 1-star count reflects recency, not maturity — this is an official Deepgram product. The dynamic loading architecture is the right long-term pattern for API-backed MCP servers: the server stays current without version pinning by users. This closes a gap noted in every previous review of this category.

### OpenAI Whisper

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [arcaputo3/mcp-server-whisper](https://github.com/arcaputo3/mcp-server-whisper) | 56 | Python | 8 | stdio |

**arcaputo3/mcp-server-whisper** ([56 stars](https://github.com/arcaputo3/mcp-server-whisper), Python, MIT) is the most comprehensive cloud-based transcription MCP server, built on OpenAI's Whisper and GPT-4o models.

Eight tools cover the full audio processing pipeline: `list_audio_files` — search with regex patterns and metadata filtering. `get_latest_audio` — retrieve most recently modified file. `convert_audio` — transform between mp3/wav formats. `compress_audio` — reduce files exceeding size limits. `transcribe_audio` — multi-model transcription with timestamps. `chat_with_audio` — interactive GPT-4o audio analysis (ask questions about audio content). `transcribe_with_enhancement` — enhanced output modes (detailed, storytelling, professional, analytical). `create_audio` — text-to-speech with voice customization.

Type-safe responses via Pydantic models. Performance optimization through caching. The `chat_with_audio` tool is unique — it enables conversational analysis of audio content, not just transcription.

### Local Speech-to-Text

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [SmartLittleApps/local-stt-mcp](https://github.com/SmartLittleApps/local-stt-mcp) | 18 | TypeScript | 6 | stdio |

**SmartLittleApps/local-stt-mcp** ([18 stars](https://github.com/SmartLittleApps/local-stt-mcp), TypeScript, MIT) provides completely local transcription using whisper.cpp, optimized for Apple Silicon with 15x+ real-time transcription speed.

Six tools: `transcribe` (basic transcription with automatic format conversion), `transcribe_long` (long audio with chunking), `transcribe_with_speakers` (speaker diarization), `list_models` (available Whisper models), `health_check`, `version`. Handles MP3, M4A, FLAC, OGG, WMA through automatic conversion. Output formats: txt, json, vtt, srt, csv. Under 2GB memory usage.

The privacy advantage is clear — no audio leaves the machine. The speaker diarization capability (identifying who said what) is particularly valuable for meeting transcription.

### YouTube Transcripts

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) | 582 | TypeScript | 1 | stdio |

**kimtaeyoon83/mcp-server-youtube-transcript** ([582 stars](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript), TypeScript, MIT) is the most popular YouTube transcript server. One tool (`get_transcript`) with smart defaults: language fallback, optional timestamps, and built-in ad/sponsorship filtering enabled by default. Accepts standard URLs, Shorts URLs, and raw video IDs. Zero external dependencies for transcript fetching.

The high star count (582 — higher than many full-featured MCP servers) reflects a common workflow: AI agents analyzing video content by reading transcripts rather than processing raw audio. Multiple alternatives exist (jkawamoto, sparfenyuk, adhikasp) but this is the standard.

**[kevinwatt/yt-dlp-mcp](https://github.com/kevinwatt/yt-dlp-mcp)** (268 stars, TypeScript) takes a broader approach — bridging yt-dlp with MCP for video search, download, and transcript extraction. More actively maintained than the transcript-only servers and useful when you need the actual media files, not just text.

## Video Processing (FFmpeg)

### FFmpeg (KyaniteLabs / Kinocut)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [KyaniteLabs/kinocut](https://github.com/KyaniteLabs/kinocut) | 110 | Python | 196 + 167 CLI | stdio |

**KyaniteLabs's FFmpeg server** was launched in 2026 as `mcp-video` and has since been renamed **`kinocut`** (the old `github.com/KyaniteLabs/mcp-video` path still resolves; the project's own docs describe `mcp-video==1.6.10` as installing `kinocut==1.14.1` for backward compatibility). It's grown substantially since its debut — the README for the current 1.14.1 release documents **196 MCP tools and 167 CLI commands**, Apache 2.0 licensed, describing itself as a "guardrailed video editing MCP server for AI agents" covering trimming, captioning, repurposing, and quality-gating through typed FFmpeg tools rather than raw command flags, plus 360-degree video assembly and workflow verification receipts. This is the first FFmpeg server in the category to combine traditional FFmpeg tooling with a higher-level video creation API in a single MCP server, and its tool count and star growth now exceed the three original FFmpeg servers reviewed here.

### FFmpeg (video-creator)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [video-creator/ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp) | 142 | Python | 8 | stdio |

**video-creator/ffmpeg-mcp** ([142 stars](https://github.com/video-creator/ffmpeg-mcp), Python, MIT) provides the core FFmpeg operations most workflows need: `find_video_path` (recursive directory search), `get_video_info` (duration/fps/codec/dimensions metadata), `clip_video` (trimming), `concat_videos` (combining with quality detection), `play_video` (playback with speed/loop control), `overlay_video` (layering with positioning), `scale_video` (resizing with aspect ratio preservation), `extract_frames_from_video` (PNG/JPG/WEBP export). Currently macOS-focused (ARM64 and x86_64).

### FFmpeg (video-audio-mcp)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [misbahsy/video-audio-mcp](https://github.com/misbahsy/video-audio-mcp) | 84 | Python | 27 | stdio |

**misbahsy/video-audio-mcp** ([84 stars](https://github.com/misbahsy/video-audio-mcp), Python, MIT) is the most tool-rich FFmpeg MCP server with 27 tools spanning professional-grade editing:

**Video:** `extract_audio_from_video`, `trim_video`, `convert_video_format`, `convert_video_properties`, `change_aspect_ratio`, `set_video_resolution`, `set_video_codec`, `set_video_bitrate`, `set_video_frame_rate`. **Audio:** `convert_audio_format`, `convert_audio_properties`, `set_audio_bitrate`, `set_audio_sample_rate`, `set_audio_channels`, `set_video_audio_track_codec/bitrate/sample_rate/channels`. **Creative:** `add_subtitles`, `add_text_overlay`, `add_image_overlay`, `add_b_roll`, `add_basic_transitions`. **Editing:** `concatenate_videos`, `change_video_speed`, `remove_silence`, `health_check`.

The `remove_silence` tool is particularly useful for podcast/video editing workflows. B-roll insertion and transition effects go beyond basic conversion into actual editing.

### FFmpeg (Advanced)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [dubnium0/ffmpeg-mcp](https://github.com/dubnium0/ffmpeg-mcp) | 20 | Python | 40+ | stdio |

**dubnium0/ffmpeg-mcp** ([20 stars](https://github.com/dubnium0/ffmpeg-mcp), Python, MIT, 1 commit) has the largest tool count at 40+ across eight categories: media analysis (probing, scene detection, keyframe extraction), format conversion (transcoding, GIF generation, batch processing), video editing (trimming, merging, rotation, cropping, thumbnail generation), audio processing (volume, loudness normalization, silence removal, waveform/spectrogram visualization), visual effects (text overlays, watermarks, picture-in-picture, split-screen, slideshows), subtitle management (extraction, burning, soft insertion), streaming (HLS/DASH generation, adaptive multi-bitrate, RTMP broadcasting), and advanced operations (two-pass encoding, video stabilization, denoising, deinterlacing, custom FFmpeg command execution). The breadth is impressive but the single commit suggests early-stage development.

## Professional Video Editing

### DaVinci Resolve

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) | 2,120 | Python | 34/353 | stdio |

**samuelgursky/davinci-resolve-mcp** ([2,120 stars](https://github.com/samuelgursky/davinci-resolve-mcp), Python, MIT) has the deepest API coverage of any creative application MCP server — **100% of the DaVinci Resolve Scripting API** (361/361 methods per the current [CHANGELOG](https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/CHANGELOG.md)), with 93.6% live-tested (338/361 methods) against Resolve Studio.

The project has shipped continuously since this section was first written — the current release is **v2.95.3** (the codebase has gone through several major version lines since the v2.x series that first added Fusion node-graph and Fairlight support). Fusion composition control (add/delete/wire nodes, parameters, keyframes) and Fairlight audio post-production (mixing, effects, voice isolation) are both now established, non-experimental parts of the tool surface. A path-traversal fix for the layout-preset tools (`export_layout_preset`/`import_layout_preset`/`delete_layout_preset`), confirmed in the changelog, shipped in the v2.0.x line.

Two modes: **Compound Server** (default, 34 tools) groups related operations by action parameter to keep LLM context windows lean — `resolve` (app control, pages, layout presets), `project_manager` (project CRUD, folders, databases), `project` (timelines, render pipeline, settings), `media_pool` (clips, folders, metadata), `timeline` (tracks, markers, export, generators), `timeline_item` (properties, markers, Fusion compositions), `fusion` (node graph management), `fairlight` (audio post-production, mixing, effects), plus specialized tools for retime, transform, crop, composite, audio, keyframes, color grading, and galleries. **Full Server** (353 tools) exposes one tool per API method for maximum precision.

Auto-detection of OS and Resolve installation. Lazy connection recovery with auto-launch. Supports 10 MCP clients (Claude Desktop, Cursor, Windsurf, VS Code, Zed, and more). The compound/granular dual-mode approach is an excellent pattern — practical defaults with full power available.

Additional DaVinci Resolve MCP servers: apvlv/davinci-resolve-mcp, Tooflex/davinci-resolve-mcp (alternative implementations).

### Adobe Creative Suite

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [mikechambers/adb-mcp](https://github.com/mikechambers/adb-mcp) | 682 | JavaScript/Python | Multi-app | stdio |

**mikechambers/adb-mcp** ([682 stars](https://github.com/mikechambers/adb-mcp), JavaScript/Python, MIT, 214 commits) enables AI control of multiple Adobe applications through a unified MCP interface: **Photoshop** (layer management, text creation, image generation, selection tools, filters, color adjustments, clipping masks), **Premiere Pro** (clip management, transitions, effects, audio adjustment, timeline editing, sequence operations), **After Effects, InDesign, Illustrator** (ExtendScript API access for arbitrary automation).

Architecture: AI ↔ MCP Server ↔ Node Proxy Server ↔ Adobe Plugin ↔ Application. The proxy is necessary because UXP plugins can only connect as clients, not listen as servers. Not endorsed or supported by Adobe — this is a proof-of-concept but with significant adoption (682 stars, 214 commits).

### Adobe After Effects (Dedicated)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [sunqirui1987/ae-mcp](https://github.com/sunqirui1987/ae-mcp) | 8 | Go/JavaScript | 9+ | stdio |

**sunqirui1987/ae-mcp** ([8 stars](https://github.com/sunqirui1987/ae-mcp), Go/JavaScript, MIT) focuses specifically on After Effects with an extensible tool architecture: project information, composition creation, text and solid layers, shape layers (rectangles, ellipses, polygons, stars with vertex/tangent/feathering control), layer properties (position, scale, rotation, opacity), effects browsing and application, ExtendScript execution, and Manim integration for mathematical animations as WebP layers. The Manim integration is a unique feature — generating mathematical visualizations directly as After Effects layers.

Also: p10q/ae-mcp provides a file-based communication bridge for After Effects control.

## Music Production

### Ableton Live

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp) | 2,903 | Python | 15+ | stdio (socket bridge) |

**ahujasid/ableton-mcp** ([2,903 stars](https://github.com/ahujasid/ableton-mcp), Python, MIT) is the most popular music production MCP server and one of the highest-starred creative MCP servers overall. Two-way socket-based communication between Claude and Ableton Live.

Capabilities: MIDI and audio track creation/modification, instrument and effect loading from Ableton's library, MIDI clip creation and note editing, playback/session transport control, tempo adjustment and parameter management. The architecture uses JSON commands over TCP sockets with two components: an Ableton Remote Script (MIDI control interface) and an MCP Server (protocol implementation).

The high star count reflects genuine interest in AI-assisted music production, though the tool count is relatively modest compared to more specialized alternatives.

**April 28, 2026:** Anthropic launched an official [Claude Connector for Ableton Live](https://www.anthropic.com/news/claude-for-creative-work) — a documentation-access tool giving Claude knowledge of Ableton's full documentation library. It does not interact with Live projects directly; that's what ahujasid/ableton-mcp does. The two serve different needs.

### Ableton Live (Copilot)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [xiaolaa2/ableton-copilot-mcp](https://github.com/xiaolaa2/ableton-copilot-mcp) | 92 | TypeScript | 20+ | stdio |

**xiaolaa2/ableton-copilot-mcp** ([92 stars](https://github.com/xiaolaa2/ableton-copilot-mcp), TypeScript, MIT) builds on ableton-js for deeper functionality: Arrangement View operations, track creation/deletion/duplication, clip property configuration with piano roll integration, note management (add, delete, replace, duplicate), audio recording based on time ranges, plugin/effect loading and parameter adjustment, and operation history with rollback capability for note operations. The rollback feature is a meaningful safety addition for destructive editing operations.

Also: [cafeTechne/ableton-11-mcp-for-windows-codex-and-antigravity](https://github.com/cafeTechne/ableton-11-mcp-for-windows-codex-and-antigravity) (renamed from `ableton-11-mcp`; 2 stars, 38 commits, Python, 220+ tools with music theory generators, chord progressions, intelligent basslines, genre-aware drum patterns — the most comprehensive Ableton toolset in terms of tool count, but still early-stage by adoption).

### REAPER

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [shiehn/total-reaper-mcp](https://github.com/shiehn/total-reaper-mcp) | 72 | Python | 600+ | stdio |

**shiehn/total-reaper-mcp** ([72 stars](https://github.com/shiehn/total-reaper-mcp), Python, MIT, 114 commits) is the most comprehensive DAW MCP server in the entire ecosystem. 600+ tools across 40+ categories: track management, media items, MIDI editing, effects/FX management, automation, transport control, bounce/rendering, groove quantization, bus routing, audio analysis, and video integration.

The key innovation is **deployment profiles**: `dsl-production` (default, 53 tools combining natural language with essential production), `dsl` (15 minimal natural language tools), `groq-essential` (~146 ReaScript functions), `mixing` (~120 mixing tools), `full` (600+ complete toolkit). The natural language DSL supports flexible references: track names ("bass", "track 3"), volume specs ("-6dB", "50%"), and time references ("8 bars", "selection").

Hybrid architecture: Lua bridge for REAPER execution + Python MCP server with file-based IPC. The profile system is a mature approach to the tool-count problem that other large MCP servers should study.

### REAPER (itsuzef)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [itsuzef/reaper-mcp](https://github.com/itsuzef/reaper-mcp) | 118 | Python | 58 | stdio |

**itsuzef/reaper-mcp** ([118 stars](https://github.com/itsuzef/reaper-mcp), Python, MIT) underwent a **major rewrite in late March 2026**. The previous version offered 5 basic tools via OSC; the new version replaces the entire architecture with python-reapy, expands to **58 tools** organized across modules for project management, tracks, MIDI, FX/instruments, audio, mixing, rendering, mastering, and analysis, and is now published on PyPI as `reaper-mcp-server`. This transforms it from a minimal proof-of-concept into a credible alternative to total-reaper-mcp, though with fewer tools (58 vs 600+) in exchange for simpler setup via PyPI.

Also: [dschuler36/reaper-mcp-server](https://github.com/dschuler36/reaper-mcp-server) (116 stars, project analysis focus — level, frequency, stereo-imaging, and dynamic-range analysis for mixing feedback), wegitor/reaper-reapy-mcp (reapy-based control).

### SuperCollider

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [Tok/SuperColliderMCP](https://github.com/Tok/SuperColliderMCP) | 23 | Python | 11 | stdio |

**Tok/SuperColliderMCP** ([23 stars](https://github.com/Tok/SuperColliderMCP), Python, MIT) connects AI agents to SuperCollider for algorithmic audio synthesis via OSC messages. Eleven tools: `play_example_osc`, `play_melody`, `create_drum_pattern`, `play_synth`, `create_sequence`, `create_lfo_modulation`, `create_layered_synth`, `create_granular_texture`, `create_chord_progression`, `create_ambient_soundscape`, `create_generative_rhythm`.

The tools serve as customizable templates — designed for AI agents to extend rather than use directly. Supports procedurally generated melodies with customizable scales, granular synthesis, and ambient soundscape generation. Unique in the ecosystem as the only algorithmic/generative audio MCP server.

## Streaming & Media Services

### Descript (Official)

**Descript** has launched an official hosted MCP server at `api.descript.com/v2/mcp` (May 2026). Documented in Descript's [help center](https://help.descript.com/hc/en-us/articles/46056322186509-Descript-MCP-overview) under "Use Descript with an AI assistant." Authentication is handled via OAuth — no API token management required.

Tools cover Descript's **Underlord AI editing toolkit**: automatic filler word removal, Studio Sound background noise cleanup, automatic captioning generation, B-roll suggestions, and access to projects and compositions. Unlike most MCP servers in this list which require local installation, this is a hosted server — connect directly from your MCP client using the URL.

This is a significant arrival: Descript has the most polished AI-assisted video editing UX on the market, and its MCP brings that directly to agent workflows without any local setup.

### Spotify

**[marcelmarais/spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server)** (424 stars, TypeScript, updated July 2026) is the first notable Spotify MCP server — providing playlist management, playback control, and music metadata access through the Spotify API. Also: [iceener/spotify-streamable-mcp-server](https://github.com/iceener/spotify-streamable-mcp-server) (79 stars, TypeScript, Hono.dev-based Spotify API integration, updated July 2026).

The emergence of Spotify MCP servers is significant — music metadata and playlist management were previously absent from the ecosystem entirely.

## Media Generation & Analysis

### Agent Media

AI-powered UGC (user-generated-content-style) video generation. The project — built by Yuval Suede, [published on PyPI as `agent-media`](https://pypi.org/project/agent-media/) — now lives at [gitroomhq/agent-media](https://github.com/gitroomhq/agent-media) (its GitHub location has moved since this review was first written). It ships a CLI, Python SDK, and an MCP server ([`@agentmedia/mcp-server`](https://agent-media.ai/mcp), Apache 2.0) built on Seedance for lip-synced talking-head video, exposing a handful of tools (UGC video generation, two-character podcast generation, and subtitle/caption generation) rather than the broader multi-model roster (Kling, Veo, Sora, Flux, Grok Imagine) an earlier version of this review claimed — that broader claim could not be verified against current sources and has been removed.

### Video Editing (AI-Driven)

burningion/video-editing-mcp — MCP Interface for Video Jungle, enabling AI-driven video editing, analysis, and search within a video collection. Add videos, build projects, generate edits from multiple sources, and search for relevant clips.

## What's Missing

The audio and video MCP ecosystem has notable gaps:

- **~~No Spotify or Apple Music MCP server~~** — **Spotify MCP servers now exist** (marcelmarais at 341 stars), but Apple Music remains absent
- **~~No Deepgram official MCP server~~** — **Deepgram now has an official MCP** (deepgram/mcp, dynamic tool loading from Deepgram API). The remaining gap: **no AssemblyAI official MCP** — AssemblyAI-Community/assemblyai-mcp still has 0 stars and no official backing from the AssemblyAI org
- **No professional audio effects processing** — no VST/AU plugin hosting, no mastering chain automation beyond what DAW servers provide
- **No real-time audio streaming** — all servers work with files, none handle live audio streams
- **No video conferencing integration** — no Zoom/Teams/Meet recording or transcription MCP servers
- **No Premiere Pro dedicated MCP server** — only available through adb-mcp's multi-app approach
- **No Blender MCP server** for 3D animation and video compositing
- **Limited safety controls** — most video/audio servers allow arbitrary file operations without sandboxing or confirmation (DaVinci Resolve's layout-preset path-traversal fix, shipped in its v2.0.x line, is a welcome exception)
- **FFmpeg servers are fragmented** — KyaniteLabs's renamed `kinocut` server (196 MCP tools + 167 CLI commands) is now the clear tool-count and star leader, but maintenance is uneven among the original three: misbahsy/video-audio-mcp has had no commits in over a year and dubnium0/ffmpeg-mcp in roughly six months, while video-creator/ffmpeg-mcp has seen more recent activity (a commit within the last three months). No single server has established clear ecosystem dominance despite kinocut's lead.
- **No subtitle/caption generation pipeline** — transcription and subtitle burning exist separately; Descript's MCP now offers captioning as part of its hosted workflow, but no open-source end-to-end solution
- **Open-weight voice model coverage is thin** — major models like Sesame/CSM, Dia (Nari Labs), F5-TTS, Parler TTS, and Fish Speech have no notable MCP server implementations yet

## The Bottom Line

**Rating: 4.0 / 5**

The audio and video MCP ecosystem earns 4.0/5 for breadth, official vendor participation, and genuine creative utility. ElevenLabs provides the most complete audio API server (24 tools, now 1,522 stars). DaVinci Resolve has the deepest application integration of any creative-app server (now 2,120 stars, 100% scripting API coverage). REAPER's total-reaper-mcp demonstrates what comprehensive DAW control looks like with its profile system and 600+ tools, while itsuzef/reaper-mcp's rewrite (58 tools, PyPI-published) shows the REAPER ecosystem maturing. Ableton MCP's 2,903 stars prove real demand for AI-assisted music production.

The rating reflects both strengths and opportunities. On the positive side: **official vendor participation is broadening** — Deepgram and Descript have both launched official MCPs, joining ElevenLabs and DaVinci Resolve. Deepgram's dynamic tool loading is an architecturally notable pattern. Descript's hosted MCP lowers the barrier for AI-assisted video editing workflows. DaVinci Resolve's Fairlight audio post-production support rounds out its coverage. KyaniteLabs's renamed `kinocut` server (196 MCP tools + 167 CLI commands) provides a new, far more comprehensive FFmpeg option. Spotify at 424 stars shows streaming service access gaining traction. On the gap side: FFmpeg server dominance is still unresolved despite kinocut's growth, many open-weight voice models lack MCP integrations, no real-time audio streaming, and AssemblyAI still has no official MCP.

For **text-to-speech**, start with ElevenLabs if cloud APIs are acceptable, or Kokoro for local/private deployment (with Chatterbox and Qwen3-TTS as emerging alternatives). For **speech-to-text**, use OpenAI Whisper MCP or Deepgram's official MCP for cloud-quality transcription, or local-stt-mcp for privacy. For **video editing**, choose DaVinci Resolve MCP for professional NLE control, Descript's official hosted MCP for AI-assisted editing workflows (filler removal, captioning, B-roll), or KyaniteLabs's `kinocut` for comprehensive FFmpeg processing. For **music production**, Ableton MCP is the safe choice for adoption, but total-reaper-mcp offers dramatically more depth for REAPER users, and itsuzef/reaper-mcp now provides a quick-start option via PyPI.

**Category**: [Design & Creative MCP Servers](/categories/design-creative/)

*This review was last edited on 2026-08-14 using Claude Sonnet 5 (Anthropic) — claim-level citation re-audit: refreshed star counts and tool counts across all listed servers, corrected the KyaniteLabs/mcp-video → kinocut rename, fixed the yuvalsuede/agent-media and cafeTechne/ableton-11-mcp dead links (both repos moved/renamed), corrected an internal Adobe adb-mcp star-count inconsistency (576 vs. 505), updated DaVinci Resolve's API-coverage figures against its current changelog, and removed unverifiable growth-rate and staleness claims.*

