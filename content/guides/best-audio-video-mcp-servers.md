---
title: "Best Audio & Video MCP Servers in 2026"
date: 2026-03-22T22:00:00+09:00
description: "ElevenLabs, MiniMax, DaVinci Resolve, Ableton, REAPER, FFmpeg, Premiere Pro, and more — we've reviewed 45+ audio and video MCP servers across 9 categories."
og_description: "45+ audio and video MCP servers reviewed across text-to-speech, transcription, video editing, music production, and creative applications. The definitive comparison with honest ratings."
content_type: "Comparison"
card_description: "The definitive guide to audio and video MCP servers in 2026. We've reviewed 45+ servers across text-to-speech (ElevenLabs, MiniMax, Kokoro, multi-provider), transcription (Whisper, Deepgram CLI, local STT, YouTube), FFmpeg video processing, professional NLEs (DaVinci Resolve, Premiere Pro, After Effects), music production (Ableton, REAPER, Logic Pro, SuperCollider), music licensing (Epidemic Sound), and streaming platforms (Mux). Every recommendation links to a full review."
last_refreshed: 2026-04-23
---

Audio and video is where MCP servers get creative. Instead of querying databases or managing infrastructure, these servers generate speech, transcribe meetings, edit video timelines, produce music, and control professional creative applications — all through natural language.

We've researched 45+ audio and video MCP servers across the full landscape. This guide covers what's production-ready, what's experimental, and where significant gaps remain.

*Note: Our recommendations are based on documentation review, GitHub analysis, and community feedback — not hands-on testing of every server. Star counts were verified in April 2026.*

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| Text-to-speech (cloud) | [elevenlabs/elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp) | 1,100 | [MiniMax-AI/MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) (1,400 stars, TTS + video + image) |
| Text-to-speech (local) | [mberg/kokoro-tts-mcp](https://github.com/mberg/kokoro-tts-mcp) | 51 | [aparsoft/kokoro-mcp-server](https://github.com/aparsoft/kokoro-mcp-server) (Kokoro-82M + audio enhancement) |
| Multi-provider TTS | [blacktop/mcp-tts](https://github.com/blacktop/mcp-tts) | 49 | [CodeCraftersLLC/local-voice-mcp](https://github.com/CodeCraftersLLC/local-voice-mcp) (Chatterbox + Kokoro) |
| Transcription (cloud) | [arcaputo3/mcp-server-whisper](https://github.com/arcaputo3/mcp-server-whisper) | 48 | Deepgram CLI (`dg mcp`, 25+ tools, dynamic loading) |
| Transcription (local) | [SmartLittleApps/local-stt-mcp](https://github.com/SmartLittleApps/local-stt-mcp) | 11 | [shreyaskarnik/voice-mcp](https://github.com/shreyaskarnik/voice-mcp) (bidirectional) |
| YouTube transcripts | [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) | 494 | [jkawamoto/mcp-youtube-transcript](https://github.com/jkawamoto/mcp-youtube-transcript) (490 stars, pagination) |
| FFmpeg / video processing | [video-creator/ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp) | 124 | [misbahsy/video-audio-mcp](https://github.com/misbahsy/video-audio-mcp) (65 stars, 27 tools) |
| Professional video editing | [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) | 700+ | [mikechambers/adb-mcp](https://github.com/mikechambers/adb-mcp) (355 stars, Adobe multi-app) |
| Music production (DAW) | [ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp) | 2,100 | [jpoindexter/ableton-mcp](https://github.com/jpoindexter/ableton-mcp) (200+ tools, REST API) |
| Music licensing | [Epidemic Sound MCP](https://www.epidemicsound.com/blog/mcp-server/) | — | — |
| Video streaming | [Mux MCP](https://mcp.mux.com) | — | — |

## Why audio & video MCP servers matter

Creative work is repetitive in ways people don't discuss. A podcast editor trims silence from every episode. A video producer adds the same lower-third template to every interview. A music producer creates the same drum pattern skeleton in every session before making it unique. MCP servers automate the repetitive parts so humans focus on the creative decisions.

The value comes in three forms:

1. **Voice and speech.** Generate narration, clone voices for consistency, transcribe meetings with speaker identification — ElevenLabs' official MCP server turns a single API into a complete audio production pipeline. MiniMax MCP (1,400 stars) goes further, adding video and music generation to the same server.
2. **Video production.** Trim, transcode, overlay, and concatenate video through FFmpeg — or control professional NLEs like DaVinci Resolve and Premiere Pro directly, with hundreds of tools mapping their full scripting APIs.
3. **Music production.** Create tracks, load instruments, edit MIDI, and control DAW transport — Ableton MCP (2,100 stars) proved the demand, spawning five competing implementations. REAPER's 600+ tool server shows the depth possible.

### What changed since March 2026

| Server/Category | March 2026 | April 2026 | Change |
|----------------|------------|------------|--------|
| MiniMax MCP | Not listed | 1,400 stars, TTS+video+image+music | **NEW** — fastest-growing creative MCP server |
| Epidemic Sound MCP | Not listed | Beta launch | **NEW** — first music licensing MCP server |
| Deepgram CLI MCP | Community-only | Official CLI with 25+ tools | **NEW** — dynamic tool loading |
| ElevenLabs MCP | 1,300 stars | 1,100 stars, v0.4.0 | Updated SDK, new tools |
| DaVinci Resolve MCP | 641 stars, 26/342 tools | 700+ stars, Fusion node graph, universal installer | Significant feature expansion |
| Ableton MCP (ahujasid) | 2,300 stars | 2,100 stars | Ecosystem fragmented into 5+ competitors |
| jpoindexter/ableton-mcp | Not listed | 200+ tools, REST API | **NEW** — most comprehensive Ableton server |
| Kokoro TTS ecosystem | 1 server (6 stars) | 3+ servers (mberg 51 stars, scottschram Apple Silicon) | Ecosystem expansion |
| Spotify MCP servers | Not listed (gap) | Multiple community servers | Gap partially filled |
| MCP Security | Not discussed | 30+ CVEs, 82% vulnerable | Crisis documented |

The landscape splits into nine categories: **text-to-speech** (cloud and local), **transcription** (cloud, local, YouTube), **FFmpeg video processing**, **professional video editing** (DaVinci Resolve, Adobe), **dedicated Premiere Pro**, **dedicated After Effects**, **music production** (Ableton, REAPER, Logic Pro, SuperCollider), **media generation** (AI video/image creation), and **video streaming** (Mux).

---

## Text-to-speech servers

Text-to-speech is the most mature audio MCP category, with cloud APIs, multi-provider wrappers, and local open-weight models all available.

### The winner: elevenlabs/elevenlabs-mcp

**Stars:** 1,100 | **Language:** Python | **License:** MIT | **Tools:** 10+ | **Latest:** v0.4.0

[elevenlabs/elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp) is the official ElevenLabs MCP server and the most feature-rich audio-focused API server in the ecosystem. It covers the full ElevenLabs platform: **Text-to-Speech** with configurable voices, languages, and output formats. **Voice Cloning** from audio samples. **Voice Design** for creating new synthetic voices. **Transcription** with speaker identification. **Sound Effects** generation from text. **Audio Isolation** to separate speech from noise. **Conversational AI** for voice agents. **Outbound Calls** for voice agents that can make phone calls.

Three output modes: `files` (save to disk), `resources` (return via MCP resources), or `both`. Enterprise data residency control via `ELEVENLABS_API_RESIDENCY`. Free tier provides 10,000 credits/month. The v0.4.0 release (May 2026) added new tools and updated the SDK.

**Why it wins:** No other audio MCP server combines TTS, STT, cloning, isolation, sound effects, and voice agents in a single server. This is effectively a complete audio production API accessible through natural language.

**The catch:** Requires an API key and sends audio data to ElevenLabs' servers. For privacy-sensitive use cases, consider the local alternatives below.

**Best for:** Anyone who wants the broadest audio capability from one server and is comfortable with a cloud API.

### Runner-up: MiniMax-AI/MiniMax-MCP (multi-modal)

**Stars:** 1,400 | **Language:** Python | **License:** MIT | **Tools:** 9+

[MiniMax-AI/MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) is the official MiniMax MCP server — and the broadest multi-modal creative server in the ecosystem, covering **Text-to-Speech** (30+ voices with speed, volume, and pitch controls plus subtitle timing), **Voice Cloning** from samples, **Voice Design** from descriptive text prompts, **Text-to-Image**, **Text-to-Video** (MiniMax-Hailuo-02, 6s/10s at 768P/1080P), **Image-to-Video**, and **Music Generation** (music-1.5/2.5 models with genre, mood, tempo, instrument, and key parameters plus AI watermark flag).

The 1,400 stars accumulated in under a month since March 25 launch, making it the fastest-growing creative MCP server. MiniMax also released MMX-CLI (1,200 stars) — a companion CLI that exposes all seven modalities as shell commands without MCP, giving developers two integration paths.

**Why it's significant:** No other single MCP server spans TTS, voice cloning, video generation, image generation, and music creation. Where ElevenLabs focuses deeply on audio, MiniMax covers the full creative media pipeline at the cost of less audio depth.

**Best for:** Teams that need multi-modal generation (speech + video + image + music) from a single server.

### Best multi-provider: blacktop/mcp-tts

**Stars:** 49 | **Language:** Go | **License:** MIT | **Tools:** 4

[blacktop/mcp-tts](https://github.com/blacktop/mcp-tts) takes a different approach — instead of one provider, it offers four TTS backends with automatic fallback: `say_tts` (macOS built-in, zero cost, offline), `elevenlabs_tts` (high-quality synthesis), `google_tts` (Google Gemini, 30 voices), and `openai_tts` (10 voices, speed control 0.25x–4.0x).

The standout feature is **sequential TTS enforcement** — system-wide file locking prevents concurrent speech from multiple AI agent instances. Includes a "speak" skill for Claude Code, Codex CLI, and Gemini CLI.

**Best for:** Multi-agent setups or teams that want provider flexibility without lock-in.

### Best local option: mberg/kokoro-tts-mcp

**Stars:** 51 | **Language:** Python | **License:** MIT

[mberg/kokoro-tts-mcp](https://github.com/mberg/kokoro-tts-mcp) wraps Kokoro TTS for local speech synthesis, generating MP3 files with optional S3 upload. The 51 stars make it the most adopted Kokoro MCP server, ahead of aparsoft/kokoro-mcp-server (which adds audio enhancement, Docker, and a Streamlit Web UI) and scottschram/kokoro-tts-mcp (Apple Silicon optimized via MLX, lazy-loads the ~600MB model).

The Kokoro ecosystem has expanded significantly — multiple implementations now cover different platforms and deployment models, all built on the Kokoro-82M open-weight model with zero cloud dependencies.

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

**[Deepgram CLI (`dg mcp`)](https://developers.deepgram.com/cli/mcp-server)** — Deepgram released a CLI (April 15, 2026) with a **built-in MCP server** offering 25+ tools for transcription, TTS, text analysis, and account management. The standout feature is **dynamic tool loading** — the server fetches its tool list from Deepgram's API at runtime, so new capabilities appear without package upgrades. Real-time transcripts with interim results, word-level timing, speaker diarization. Uses stored credentials via `dg login`. This effectively replaces the older [deepgram-devs/deepgram-mcp](https://github.com/deepgram-devs/deepgram-mcp) as the official Deepgram MCP integration.

**[cogell/assembly-ai-mcp](https://github.com/cogell/assembly-ai-mcp)** — AssemblyAI transcription services via MCP. Standard interface for AssemblyAI's API including the Slam-1 speech-language model.

**[BigUncle/Fast-Whisper-MCP-Server](https://github.com/BigUncle/Fast-Whisper-MCP-Server)** — High-performance speech recognition MCP server based on Faster Whisper, providing efficient local audio transcription.

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

**Stars:** 700+ | **Language:** Python | **License:** MIT | **Tools:** 26/342

[samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) has the deepest API coverage of any creative application MCP server — **100% of the DaVinci Resolve Scripting API** (324/324 methods), with 98.5% live-tested.

Two modes: **Compound Server** (default, 26 tools) groups related operations to keep context windows lean — project management, media pool, timeline editing, color grading, Fusion compositions, render pipeline. **Full Server** (342 tools) exposes one tool per API method for maximum precision. Auto-detects OS and Resolve installation. Supports 10+ MCP clients.

**What's new (April 2026):** New `fusion_comp` tool provides a 20-action interface exposing the full Fusion composition node graph API — add/delete/find nodes, wire connections, set/get parameters, manage keyframes, control undo grouping, set render ranges, and trigger renders. Timeline item Fusion cache actions added (get/set cache on timeline items). Universal installer (`python install.py`) now supports macOS/Windows/Linux across 10 MCP clients. Dedicated timeline_item actions for retime/speed, transform, crop, composite, audio, and keyframes with validation.

**Why it wins:** No other creative application MCP server maps 100% of its host application's API. The compound/granular dual-mode approach is an excellent pattern — practical defaults with full power available. The Fusion composition tool alone exposes the entire node graph API.

**Best for:** Professional video editors who want AI-assisted DaVinci Resolve workflows.

### Runner-up: mikechambers/adb-mcp (Adobe multi-app)

**Stars:** 355 | **Language:** JavaScript/Python | **License:** MIT | **Tools:** Multi-app

[mikechambers/adb-mcp](https://github.com/mikechambers/adb-mcp) enables AI control of multiple Adobe applications through a unified interface: **Photoshop** (layers, text, image generation, selections, filters), **Premiere Pro** (clips, transitions, effects, audio, timeline editing), **After Effects** (ExtendScript automation), **InDesign**, **Illustrator**.

Architecture: AI → MCP Server → Node Proxy → Adobe Plugin → Application. Tested with Claude Desktop (Mac and Windows) and OpenAI Agent SDK. Not endorsed by Adobe — proof-of-concept, but with growing adoption.

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

**Stars:** 2,100 | **Language:** Python | **License:** MIT | **Tools:** 15+

[ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp) is the most popular music production MCP server and one of the highest-starred creative MCP servers overall. It pioneered the creative tools MCP movement, featured in a16z and Fireship coverage.

Two-way socket-based communication: MIDI and audio track creation, instrument and effect loading from Ableton's library, MIDI clip creation and note editing, playback/session transport control, tempo adjustment and parameter management.

**Why it leads:** The 2,100 stars reflect genuine demand for AI-assisted music production. The server proved the concept and inspired an entire wave of creative tool MCP servers — including multiple Ableton-specific competitors (see below).

**The catch:** Relatively modest tool count compared to specialized alternatives. Limited depth in areas like arrangement view, recording, and plugin parameter control.

**Best for:** Ableton Live users who want a well-supported, battle-tested entry point to AI-assisted music production.

### The depth leader: shiehn/total-reaper-mcp

**Stars:** 29 | **Language:** Python | **License:** MIT | **Tools:** 600+

[shiehn/total-reaper-mcp](https://github.com/shiehn/total-reaper-mcp) is the most comprehensive DAW MCP server in the entire ecosystem. 600+ tools across 40+ categories: track management, media items, MIDI editing, effects/FX management, automation, transport control, bounce/rendering, groove quantization, bus routing, audio analysis, and video integration.

The key innovation is **deployment profiles**: `dsl-production` (default, 53 tools combining natural language with essential production), `dsl` (15 minimal tools), `groq-essential` (~146 ReaScript functions), `mixing` (~120 mixing tools), `full` (600+ complete toolkit). The natural language DSL supports flexible references: track names ("bass", "track 3"), volume specs ("-6dB", "50%"), and time references ("8 bars", "selection").

**Why it matters:** The profile system solves the tool-count problem that plagues large MCP servers. Many LLMs have tool count limits (Groq: 128, OpenAI: 128), and profiles keep you within them while focusing on what you need. Other large MCP servers should study this approach.

**Best for:** REAPER power users who want full DAW control with intelligent tool management.

### Also notable

**[jpoindexter/ableton-mcp](https://github.com/jpoindexter/ableton-mcp)** (200+ tools) — The most comprehensive Ableton MCP server by tool count, with near-complete Ableton Live Object Model (LOM) coverage. Includes REST API and Max for Live device. Works with Claude, Ollama, OpenAI, and Groq. If ahujasid's server proved the concept, this one fills in the depth.

**[xiaolaa2/ableton-copilot-mcp](https://github.com/xiaolaa2/ableton-copilot-mcp)** (71 stars, TypeScript, 78 commits) — Deeper Ableton functionality: Arrangement View, clip properties with piano roll, note management, audio recording, plugin loading, and operation history with rollback. Best for users who've outgrown the base Ableton MCP.

**[uisato/ableton-mcp-extended](https://github.com/uisato/ableton-mcp-extended)** — Extended Ableton Live MCP server compatible with Claude Desktop, Cursor, and Gemini CLI.

**[itsuzef/reaper-mcp](https://github.com/itsuzef/reaper-mcp)** (40 stars, Python) — Simpler REAPER interface: project creation, track management, MIDI notes, project info. Supports OSC and ReaScript dual modes. Best for REAPER beginners.

**[dschuler36/reaper-mcp-server](https://github.com/dschuler36/reaper-mcp-server)** (85 stars, Python) — Project analysis focus for REAPER.

**Logic Pro MCP servers** — [koltyj/logic-pro-mcp](https://github.com/koltyj/logic-pro-mcp) (8 tools, 7 resources, Swift) uses 5 native macOS control channels (CoreMIDI, Accessibility, CGEvent, AppleScript, OSC) with smart routing and fallback. [kiki830621/che-logic-pro-mcp](https://github.com/kiki830621/che-logic-pro-mcp) offers AppleScript + MIDI + Scripter templates. Both require macOS 14+ and Swift 6.0+.

**[Tok/SuperColliderMCP](https://github.com/Tok/SuperColliderMCP)** (17 stars, Python, 11 tools) — Algorithmic audio synthesis via OSC: melodies, drum patterns, synths, granular textures, ambient soundscapes, chord progressions, generative rhythms. Unique in the ecosystem as the only generative audio MCP server.

**[cafeTechne/ableton-11-mcp](https://github.com/cafeTechne/ableton-11-mcp)** (38 commits, Python, 220+ tools) — The most comprehensive Ableton toolset with music theory generators, chord progressions, intelligent basslines, and genre-aware drum patterns. Low stars but deep functionality.

---

## Media generation, music licensing, and streaming

### AI media generation

**yuvalsuede/agent-media** — CLI and MCP server with unified access to 7 AI models (Kling, Veo, Sora, Seedance, Flux, Grok Imagine) for video and image generation with 9 tools.

**burningion/video-editing-mcp** — MCP interface for Video Jungle enabling AI-driven video editing, analysis, and search within a video collection. Add videos, build projects, generate edits from multiple sources, and search for relevant clips.

### Music licensing: Epidemic Sound MCP (NEW)

**[Epidemic Sound MCP Server](https://www.epidemicsound.com/blog/mcp-server/)** (Beta) — The first music licensing MCP server. Epidemic Sound's server connects AI creative tools directly to their catalog of royalty-free music, sound effects, and voiceovers. AI agents can search by text description, then filter by BPM range, duration, mood, featured instruments, musical key, artist, and vocal presence.

Epidemic Sound owns 100% of the rights to its catalog (master, neighboring, and composition rights), which means clean licensing without the complexity of traditional music clearance. Monthly subscription pricing with no per-use fees.

**Why it matters:** This is the first time a music licensing company has offered an MCP server. For video and podcast producers, the workflow of "find the right background music" is one of the most time-consuming creative tasks — having an AI agent search a licensed catalog by mood and tempo changes it fundamentally.

**Best for:** Content creators, podcast producers, and video editors who need royalty-free music and want AI-assisted soundtrack selection.

### Video streaming

**[Mux MCP](https://mcp.mux.com)** — Official Mux remote MCP server for video infrastructure management. Upload videos, create live streams, generate thumbnails, add captions, manage playback policies, and query engagement analytics. Hosted at mcp.mux.com with automatic OAuth authentication. Supports query parameters to customize which tools are exposed.

**Best for:** Teams using Mux for video hosting who want AI-assisted video infrastructure management.

---

## How to choose

Use this decision flowchart:

**Need speech synthesis?** → Start with [ElevenLabs MCP](https://github.com/elevenlabs/elevenlabs-mcp) for the deepest audio capability. Need TTS + video + image + music from one server? → [MiniMax MCP](https://github.com/MiniMax-AI/MiniMax-MCP). Need multi-provider flexibility? → [blacktop/mcp-tts](https://github.com/blacktop/mcp-tts). Need local/private TTS? → [kokoro-tts-mcp](https://github.com/mberg/kokoro-tts-mcp).

**Need transcription?** → [mcp-server-whisper](https://github.com/arcaputo3/mcp-server-whisper) for cloud quality with audio analysis. [Deepgram CLI](https://developers.deepgram.com/cli/mcp-server) for 25+ tools with dynamic loading. [local-stt-mcp](https://github.com/SmartLittleApps/local-stt-mcp) for local privacy. [mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) for YouTube videos.

**Need video processing?** → [video-creator/ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp) for common operations. [misbahsy/video-audio-mcp](https://github.com/misbahsy/video-audio-mcp) for podcast/editing workflows. [dubnium0/ffmpeg-mcp](https://github.com/dubnium0/ffmpeg-mcp) for advanced streaming/stabilization.

**Need professional NLE control?** → [DaVinci Resolve MCP](https://github.com/samuelgursky/davinci-resolve-mcp) for the deepest API coverage (now with full Fusion node graph tools). [adb-mcp](https://github.com/mikechambers/adb-mcp) for multi-app Adobe control. [leancoderkavy/premiere-pro-mcp](https://github.com/leancoderkavy/premiere-pro-mcp) for dedicated Premiere Pro with 269 tools.

**Need music production?** → [Ableton MCP](https://github.com/ahujasid/ableton-mcp) for the safest, most supported entry point. [jpoindexter/ableton-mcp](https://github.com/jpoindexter/ableton-mcp) for 200+ tools with REST API. [total-reaper-mcp](https://github.com/shiehn/total-reaper-mcp) for maximum depth. Logic Pro MCP servers for macOS-only workflows.

**Need royalty-free music?** → [Epidemic Sound MCP](https://www.epidemicsound.com/blog/mcp-server/) for AI-assisted soundtrack selection from a licensed catalog.

**Need video streaming infrastructure?** → [Mux MCP](https://mcp.mux.com) for upload, live streams, and analytics.

---

## Four trends worth watching

**1. Multi-modal servers are consolidating creative workflows.** MiniMax MCP (1,400 stars in under a month) combines TTS, voice cloning, video generation, image generation, and music creation in a single server. ElevenLabs (1,100 stars) owns audio depth. The pattern is clear: vendors are racing to become the single creative MCP server teams install, not just a point tool.

**2. The Ableton ecosystem has fragmented — in a good way.** What started as one server (ahujasid/ableton-mcp, 2,100 stars) has spawned at least five serious competitors: jpoindexter (200+ tools), xiaolaa2 (copilot with arrangement view), uisato (extended), LofiFren (33 personalities), and nozomi-koborinai (OSC). Competition is producing genuine innovation: REST APIs, personality systems, rollback, and LOM coverage that the original never attempted.

**3. Music licensing enters the MCP ecosystem.** Epidemic Sound's MCP server (Beta) is the first licensed music catalog accessible via MCP. This is a new category — not generating audio, but *finding and licensing existing audio*. Expect more content licensing platforms to follow.

**4. Security is the elephant in the room.** The 2026 MCP security crisis (30+ CVEs in 60 days, 82% of file-operation servers vulnerable to path traversal) hits audio/video servers hard. Most FFmpeg servers pass user input to shell commands — the dominant attack vector (43% of all MCP vulnerabilities). Most creative tool servers allow arbitrary file operations without sandboxing. The convenience of "AI controls my video editor" has real security implications that the ecosystem hasn't addressed.

---

## What's missing

The audio and video MCP ecosystem has narrowed some gaps but significant ones remain:

- **Spotify MCP servers exist but none dominate** — Multiple community implementations now offer playlist management, playback control, and search (marcelmarais, thebigredgeek, igorgarbuz, and others). However, none have significant adoption, and Spotify has not released an official MCP server. Apple Music still has zero MCP integration.
- **No professional audio effects processing** — No VST/AU plugin hosting or mastering chain automation beyond what DAW servers provide.
- **No real-time audio streaming** — All servers work with files. None handle live audio streams or real-time processing.
- **Deepgram now has official MCP** (via CLI) — ~~No official Deepgram MCP~~ The Deepgram CLI (April 2026) includes a built-in MCP server with 25+ tools and dynamic tool loading. AssemblyAI still lacks an official MCP server.
- **FFmpeg servers remain fragmented** — Six or more implementations, none dominant. The ecosystem needs consolidation, and the security implications of passing user input to FFmpeg shell commands are increasingly concerning.
- **No end-to-end subtitle pipeline** — Transcription and subtitle burning exist separately but no single server handles "transcribe this video and burn in the captions."
- **No GarageBand MCP server** — Apple's most accessible music tool has no MCP integration.
- **Security is now a documented crisis** — 82% of MCP servers with file operations are vulnerable to path traversal. 43% of all MCP CVEs involve shell/exec injection — exactly the pattern FFmpeg and creative tool servers exhibit. Most audio/video servers lack sandboxing, confirmation prompts, or input validation.

The Deepgram and Spotify gaps have partially closed since our last review. The security gap has widened into a documented crisis.

---

*Last updated: April 2026. Have a correction or suggestion? [Open an issue on GitHub](https://github.com/grove/chatforest.com).*
