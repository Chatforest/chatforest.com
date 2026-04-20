# Podcasting & Audio Content MCP Servers — ElevenLabs, Whisper, Reaper DAW, Kokoro TTS, Music Generation, and More

> Podcasting and audio content MCP servers are giving AI agents full audio production capabilities — text-to-speech synthesis, audio transcription, music generation, DAW control


*Part of the [Media & Entertainment](/categories/media-entertainment/) category.*

Podcasting and audio content MCP servers let AI assistants produce speech, transcribe audio, generate music, control DAWs, clone voices, and create sound effects. Instead of manually juggling audio editors, transcription services, and TTS APIs, you can wire these capabilities directly into your AI workflow through the Model Context Protocol.

This review covers the **podcasting and audio content** vertical — text-to-speech, speech-to-text transcription, music generation, DAW control, voice interaction, and podcast feed management. For video production, see our [Video & Streaming review](/reviews/video-production-streaming-mcp-servers/). For general content creation, see our [Content & Copywriting review](/reviews/cms-content-management-mcp-servers/).

The headline findings: **ElevenLabs has 1,100 stars** and is the most comprehensive audio MCP server — TTS, voice cloning, transcription, and sound effects in one package. **REAPER DAW has 600+ tools** available through total-reaper-mcp. **Local TTS and STT are genuinely viable** — Kokoro, Chatterbox, and whisper.cpp mean zero cloud costs. **Podcast-specific workflows are the gap** — individual audio tools are strong, but no server handles the full podcast lifecycle.

## Text-to-Speech

### elevenlabs/elevenlabs-mcp (Most Comprehensive)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp) | 1,100 | Python | — | ~10 |

The **most starred and feature-rich audio MCP server** — the official ElevenLabs integration provides access to their full AI audio platform:

- **Text-to-Speech** — convert text to natural-sounding speech with fine-grained control over stability, style, and similarity
- **Voice Cloning** — clone voices from audio samples or generate new voices from text descriptions (age, gender, accent, tone)
- **Audio Isolation** — separate speech from background noise
- **Voice Conversion** — make audio sound like a different voice
- **Transcription** — speech-to-text with speaker identification
- **Sound Effects** — generate effects from text descriptions
- **Soundscapes** — create ambient audio environments from descriptions

Free tier includes 10,000 credits/month. Requires ElevenLabs API key. Works with Claude Desktop, Cursor, Windsurf, and OpenAI Agents.

### blacktop/mcp-tts (Multi-Engine)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-tts](https://github.com/blacktop/mcp-tts) | — | Go | — | 4 |

The **Swiss Army knife of TTS** — supports 4 backends through a single MCP server:

- **say_tts** — macOS built-in `say` command (free, no API key, offline)
- **elevenlabs_tts** — ElevenLabs API for high-quality speech
- **google_tts** — Google Gemini TTS with 30 high-quality voices (Zephyr, Puck, Charon, Kore, Fenrir, Leda, and more)
- **openai_tts** — OpenAI TTS API with various voice options

Sequential speech queuing prevents overlapping audio — subsequent requests wait in a queue until the current speech completes. Good for comparing providers or switching backends without changing your MCP setup.

### MiniMax-AI/MiniMax-MCP (Multi-Modal)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) | 421 | Python | — | ~8 |

The **multi-modal powerhouse** — official MiniMax MCP server combining audio, image, and video generation:

- **Text-to-Speech** — natural voice synthesis
- **Voice Cloning** — clone voices from audio samples
- **Music Generation** — high-quality music creation via the music-1.5 model
- **Image Generation** — text-to-image
- **Video Generation** — text-to-video and image-to-video with MiniMax-Hailuo-02 (6s/10s duration, 768P/1080P)

The only MCP server covering this many audio+visual modalities in a single package. Requires MiniMax API key.

### hammeiam/koroko-speech-mcp (Local, Free)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [koroko-speech-mcp](https://github.com/hammeiam/koroko-speech-mcp) | — | TypeScript | MIT | ~2 |

**Local TTS with no API key** — uses the Kokoro TTS model for free, offline speech synthesis:

- Multiple voice options (default: af_bella)
- Customizable speech speed (0.5–2.0x, default 1.1)
- Automatic model download on first use with retry logic
- Model status monitoring via `get_model_status` tool

No cloud dependencies, no usage limits. Best for developers wanting free, private TTS integration.

### digitarald/chatterbox-mcp (Local, Auto-Playback)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chatterbox-mcp](https://github.com/digitarald/chatterbox-mcp) | — | Python | — | 1 |

**Simplified local TTS** — wraps the Chatterbox model (by Resemble AI) with a single `speak_text` tool that generates speech and plays it automatically:

- Automatic model loading on first use
- Real-time progress notifications
- Configurable audio output directory and file TTL
- Temporary file management handled by the server

Minimal setup — one tool does everything. Good for prototyping voice workflows.

### Edge TTS Servers (Free Cloud TTS)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [edge_tts_mcp_server](https://github.com/yuiseki/edge_tts_mcp_server) | 5 | TypeScript | — | ~2 |
| [edge-tts-mcp](https://github.com/eraincc/edge-tts-mcp) | — | Python | — | ~2 |

**Free cloud TTS via Microsoft Edge's online service** — no API key required:

- Hundreds of voices across 40+ languages
- No Microsoft Edge or Windows installation needed
- Uses the edge-tts library to access Microsoft's TTS service
- Both TypeScript and Python implementations available

Best for multilingual TTS without any API costs. Quality is good but not at ElevenLabs level.

### nakamurau1/tts-mcp (OpenAI TTS)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tts-mcp](https://github.com/nakamurau1/tts-mcp) | — | TypeScript | — | ~2 |

MCP server and CLI tool for **OpenAI TTS API** — supports multiple TTS models and voice characters with customizable audio formats. Straightforward wrapper if you're already using OpenAI and want speech generation in your MCP workflow.

## Speech-to-Text / Transcription

### SmartLittleApps/local-stt-mcp (Apple Silicon Optimized)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [local-stt-mcp](https://github.com/SmartLittleApps/local-stt-mcp) | ~10 | TypeScript | — | ~3 |

**High-performance local transcription** — whisper.cpp optimized for Apple Silicon:

- 100% local processing — no cloud APIs, complete privacy
- 15x+ real-time transcription speed on Apple Silicon
- Speaker diarization to identify and separate multiple speakers
- Universal audio format support — WAV, MP3, M4A, FLAC, OGG with automatic conversion
- Multiple output formats — TXT, JSON, VTT, SRT, CSV

Best for Mac users who want fast, private transcription. The Apple Silicon optimization makes a real performance difference.

### arcaputo3/mcp-server-whisper (OpenAI Whisper + GPT-4o)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-whisper](https://github.com/arcaputo3/mcp-server-whisper) | 2 | Python | MIT | ~5 |

**Cloud-powered transcription** with multiple modes using OpenAI's services:

- Basic Whisper transcription
- GPT-4o enhanced transcription with specialized prompts
- Enhanced transcription with timestamp support
- Parallel batch processing for multiple files
- Automatic compression for files over 25MB
- Supports mp3, wav, mp4, mpeg, mpga, m4a, webm

The GPT-4o enhanced mode is the differentiator — uses prompt engineering to improve transcription quality beyond base Whisper.

### ebmarquez/audio-transcription-mcp (Speaker Diarization + Docker)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [audio-transcription-mcp](https://github.com/ebmarquez/audio-transcription-mcp) | — | Python | — | ~3 |

**Professional transcription with speaker identification** — combines Faster-Whisper with pyannote.audio:

- Speaker diarization — identifies who said what
- Markdown output with speaker labels, timestamps, summaries, and action items
- MP3/WAV input support
- Dockerized for easy CPU/GPU deployment

Best for meeting recordings, interviews, and podcast transcription where speaker identification matters.

### Kvadratni/speech-mcp (Bidirectional Voice Interface)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [speech-mcp](https://github.com/Kvadratni/speech-mcp) | ~80 | Python | — | ~5 |

The **most complete voice interaction server** — a Goose MCP extension providing bidirectional speech:

- **Speech Recognition** — Faster-Whisper (local, base model, no cloud)
- **Speech Synthesis** — Kokoro TTS with 54+ voice models (~523KB each, auto-downloaded)
- **Audio Visualization** — real-time waveform display
- **Silence Detection** — automatically knows when you've finished speaking
- **Voice Persistence** — remembers your voice preference between sessions
- **Continuous Conversation** — ongoing back-and-forth voice interaction

The only MCP server offering a complete conversational voice loop. Requires PortAudio for microphone capture.

### Azure MCP Server (Enterprise)

The **Azure MCP Server** includes speech-to-text and text-to-speech tools through Microsoft's Foundry platform. Supports WAV, MP3, OPUS/OGG, FLAC, ALAW, MULAW, MP4, M4A, and AAC. Enterprise-grade with Azure subscription required. Best for organizations already in the Azure ecosystem.

## Music Generation & DAW Control

### shiehn/total-reaper-mcp (600+ REAPER Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [total-reaper-mcp](https://github.com/shiehn/total-reaper-mcp) | 27 | Python | — | 600+ |

The **most comprehensive DAW MCP server** — 100% ReaScript API coverage for REAPER:

- **dsl-production** (default) — 53 tools with natural language DSL plus essential production tools
- **minimal** — 15 tools for basic operations
- **traditional** — 146 tools mapping directly to ReaScript functions
- **full** — 600+ tools covering the entire ReaScript API

Developed on macOS, works cross-platform. Requires REAPER 6.83+ with embedded Lua 5.4. Tool profiles let you limit exposed tools based on your LLM's tool count restrictions.

### Other REAPER MCP Servers

| Server | Focus |
|--------|-------|
| [TwelveTake-Studios/reaper-mcp](https://github.com/TwelveTake-Studios/reaper-mcp) | Built by a working producer (7+ albums) — mixing, mastering, MIDI composition |
| [Aavishkar-Kolte/reaper-daw-mcp-server](https://github.com/Aavishkar-Kolte/reaper-daw-mcp-server) | Intelligent music production assistant with automated project control |
| [itsuzef/reaper-mcp](https://github.com/itsuzef/reaper-mcp) | Fully mixed and mastered tracks — supports both OSC and ReaScript modes |
| [dschuler36/reaper-mcp-server](https://github.com/dschuler36/reaper-mcp-server) | Audio analysis for mixing feedback — connects Reaper projects to Claude |

REAPER has the best DAW MCP coverage of any audio production software. No equivalent exists for Ableton Live, Logic Pro, FL Studio, or Pro Tools.

### pasie15/mcp-server-musicgpt (AI Music Platform)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-musicgpt](https://github.com/pasie15/mcp-server-musicgpt) | — | TypeScript | — | 24 |

**Full AI music production pipeline** via the MusicGPT API:

- Music generation from text prompts with optional lyrics
- Cover song creation with different AI voices
- Sound effects from text descriptions
- Lyrics generation based on themes
- Voice conversion — change audio to sound like different voices
- Text-to-speech conversion
- Audio mastering, remixing, and speed adjustment
- AI vocal addition to instrumental tracks

24 tools covering the full creative audio spectrum. Requires MusicGPT API key.

### falahgs/mcp-minimax-music-server (MiniMax Music API)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-minimax-music-server](https://github.com/falahgs/mcp-minimax-music-server) | — | Python | — | ~3 |

Generates music and audio content using the **MiniMax Music API** through MCP. Straightforward wrapper for teams already using MiniMax's audio capabilities.

### tubone24/midi-mcp-server (MIDI Generation)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [midi-mcp-server](https://github.com/tubone24/midi-mcp-server) | — | TypeScript | — | 1 |

Generates **MIDI files from structured JSON data** — supports multiple tracks and instruments with customizable tempo, time signature, and note properties. Uses midi-writer-js and tonal libraries. Runs locally via stdio. Good for programmatic music composition without audio rendering dependencies.

### williamzujkowski/strudel-mcp-server (Live Coding)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [strudel-mcp-server](https://github.com/williamzujkowski/strudel-mcp-server) | — | TypeScript | — | ~5 |

**AI-assisted live coding and algorithmic composition** through Strudel.cc:

- Initialize Strudel live coding environment
- Generate musical patterns across genres
- Play and analyze audio in real time
- 17 curated example patterns across 10 genres

Experimental but functional. Best for creative coding and generative music exploration.

## Podcast Feed Management

Several RSS/Atom MCP servers handle podcast feed consumption:

| Server | Language | Focus |
|--------|----------|-------|
| [veithly/rss-mcp](https://github.com/veithly/rss-mcp) | TypeScript | RSS/Atom/RSSHub feeds — most versatile |
| [richardwooding/feed-mcp](https://github.com/richardwooding/feed-mcp) | — | RSS, Atom, and JSON Feed support |
| [hmmroger/simply-feed-mcp](https://github.com/hmmroger/simply-feed-mcp) | — | Real-time feed management and search |
| [imprvhub/mcp-rss-aggregator](https://github.com/imprvhub/mcp-rss-aggregator) | — | Claude Desktop feed aggregation |
| [S1R15H/blog-mcp-server](https://github.com/S1R15H/blog-mcp-server) | — | Blog RSS/Atom with post search |

These work for **consuming** podcast RSS feeds — listing episodes, fetching descriptions, and searching content. They lack podcast-specific features like episode metadata enrichment, transcript pairing, or show notes extraction.

## Streaming Platform Integration

Multiple Spotify MCP servers exist for playback and playlist control:

| Server | Focus |
|--------|-------|
| [varunneal/spotify-mcp](https://github.com/varunneal/spotify-mcp) | Claude + Spotify via spotipy API |
| [marcelmarais/spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server) | Lightweight — Cursor & Claude playback control |
| [Carrieukie/spotify-mcp-server](https://github.com/Carrieukie/spotify-mcp-server) | Kotlin — natural language access to Spotify Web API |

Useful for **podcast listening workflows** — search for podcasts, control playback, manage playlists. Not production tools.

## What's missing

The audio production building blocks are strong, but **podcast-specific workflows** are the clear gap:

- **No podcast hosting integrations** — Spotify for Podcasters, Apple Podcasts Connect, Anchor, Buzzsprout, Podbean, Libsyn have no MCP servers
- **No episode scheduling/publishing** — no server can publish an episode to a hosting platform
- **No podcast analytics** — listener metrics, download stats, demographic data
- **No show notes generation** — transcription exists but automated show notes from transcripts doesn't
- **No transcript editing** — servers produce transcripts but don't support edit/review workflows
- **No audio mastering pipeline** — individual tools exist but no end-to-end podcast mastering workflow
- **No podcast distribution** — no multi-platform publishing (push to Apple, Spotify, Google simultaneously)
- **No audiogram generation** — waveform videos for social media promotion
- **No chapter markers** — enhanced podcasting features like chapters, links, images
- **No dynamic ad insertion** — programmatic ad placement in episodes
- **No Ableton/Logic/FL Studio** — REAPER is the only DAW with MCP coverage

## The bottom line

Podcasting and audio content MCP servers earn **4 out of 5**. The building blocks are genuinely strong — ElevenLabs provides a professional-grade audio AI platform with 1,100 stars and comprehensive TTS, voice cloning, transcription, and sound effects. Local options (Kokoro, Chatterbox, whisper.cpp) mean you can do real audio work without cloud costs. REAPER DAW coverage is exceptional with 600+ tools across multiple servers. Music generation is emerging with text-to-music, MIDI creation, and live coding tools.

The weakness is the gap between having individual audio tools and having podcast-specific workflows. You can transcribe audio, generate speech, make music, and mix in REAPER — but no server helps you record, edit, write show notes, add chapters, publish to hosting platforms, distribute across directories, and track listener analytics. You'd need to chain multiple servers together and build the podcast workflow yourself. For audio production broadly, the ecosystem is ready. For podcast production specifically, you're still assembling the pipeline manually.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

