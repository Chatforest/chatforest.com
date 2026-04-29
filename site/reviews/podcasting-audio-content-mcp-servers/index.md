# Podcasting & Audio Content MCP Servers — MimikaStudio, ElevenLabs, MiniMax, Reaper DAW, Kokoro TTS, Suno Music, Podcast Workflows, and More

> Podcasting and audio content MCP servers are giving AI agents full audio production capabilities — text-to-speech synthesis, voice cloning, audio transcription, music generation, DAW control, and podcast publishing workflows


*Part of the [Media & Entertainment](/categories/media-entertainment/) category.*

Podcasting and audio content MCP servers let AI assistants produce speech, transcribe audio, generate music, control DAWs, clone voices, create sound effects, and now increasingly manage podcast publishing workflows. Instead of manually juggling audio editors, transcription services, and TTS APIs, you can wire these capabilities directly into your AI workflow through the Model Context Protocol.

This review covers the **podcasting and audio content** vertical — text-to-speech, speech-to-text transcription, music generation, DAW control, voice interaction, podcast feed management, and podcast-specific production tools. For video production, see our [Video & Streaming review](/reviews/video-production-streaming-mcp-servers/). For general content creation, see our [Content & Copywriting review](/reviews/cms-content-management-mcp-servers/).

The headline findings: **MiniMax-MCP EXPLODED to 1,400 stars** (+233%) and is now the most-starred audio MCP server. **MimikaStudio arrived at 540 stars** with 50+ MCP tools — the most comprehensive local audio production server with multi-engine TTS, voice cloning from 3 seconds, and audiobook generation. **ElevenLabs grew to 1,300 stars** with 14 releases. **Kokoro TTS spawned an ecosystem** of dedicated MCP servers. **Suno music generation is NEW** — AI music from text prompts. **The podcast workflow gap is finally filling** — Podigee launched the first hosting platform MCP, and dedicated podcast production servers handle script-to-audio pipelines, publishing automation, and podcast search. **REAPER DAW has 600+ tools** across an expanded server ecosystem including a new 62-star entry.

## Text-to-Speech

### elevenlabs/elevenlabs-mcp (Professional Cloud Platform)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp) | 1,300 | Python | — | ~10 |

The **official ElevenLabs MCP server** — provides access to their full AI audio platform with v0.9.1 (14 releases, 63 commits):

- **Text-to-Speech** — convert text to natural-sounding speech with fine-grained control over stability, style, and similarity
- **Voice Cloning** — clone voices from audio samples or generate new voices from text descriptions (age, gender, accent, tone)
- **Audio Isolation** — separate speech from background noise
- **Voice Conversion** — make audio sound like a different voice
- **Transcription** — speech-to-text with speaker identification
- **Sound Effects** — generate effects from text descriptions
- **Soundscapes** — create ambient audio environments from descriptions
- **Data Residency** — NEW enterprise configuration for data location preferences
- **Configurable Output Modes** — file output, resource output, or both

Free tier includes 10,000 credits/month. Requires ElevenLabs API key. Works with Claude Desktop, Cursor, Windsurf, and OpenAI Agents. Also available as a community-maintained server: mamertofabian/elevenlabs-mcp-server (118 stars) with SQLite voice generation history tracking and a SvelteKit web client.

### blacktop/mcp-tts (Multi-Engine)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-tts](https://github.com/blacktop/mcp-tts) | 56 | Go | MIT | 4 |

The **Swiss Army knife of TTS** — supports 4 backends through a single MCP server (116 commits, actively maintained):

- **say_tts** — macOS built-in `say` command (free, no API key, offline)
- **elevenlabs_tts** — ElevenLabs API for high-quality speech
- **google_tts** — Google Gemini TTS with 30 high-quality voices (Zephyr, Puck, Charon, Kore, Fenrir, Leda, and more)
- **openai_tts** — OpenAI TTS API with speed control from 0.25x to 4.0x

NEW: Sequential or concurrent TTS operation modes (configurable), audio file saving with format-specific outputs, output suppression to prevent LLM interference, multi-instance protection via system-wide file locks, and **Agent Skills support** — automatically announces completion events across Claude Code, Codex CLI, and Gemini CLI following the Agent Skills open standard.

### MiniMax-AI/MiniMax-MCP (Multi-Modal — EXPLODED)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) | 1,400 | Python | — | 8 |
| [MiniMax-MCP-JS](https://github.com/MiniMax-AI/MiniMax-MCP-JS) | 121 | TypeScript | — | 6 |

**EXPLODED from 421→1,400 stars (+233%)** — now the most-starred audio MCP server. Official MiniMax server combining audio, image, and video generation:

- **text_to_audio** — natural voice synthesis with language boost and subtitle options
- **voice_clone** — replicate voice using audio samples
- **voice_design** — NEW: generate custom voices from text descriptions of desired characteristics
- **music_generation** — high-quality music creation via the enhanced music-1.5 model
- **generate_image** — text-to-image
- **generate_video** — text-to-video with MiniMax-Hailuo-02 (6s/10s duration, 768P/1080P)
- **list_voices** — display available voice options
- **query_video_generation** — check task status

NEW JavaScript implementation (MiniMax-MCP-JS, 121 stars) provides the same capabilities in TypeScript with npm distribution. Supports both stdio and SSE transport. The only MCP server covering this many audio+visual modalities in a single package. Requires MiniMax API key.

### BoltzmannEntropy/MimikaStudio (Local Multi-Engine — NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MimikaStudio](https://github.com/BoltzmannEntropy/MimikaStudio) | 540 | Python | Apache 2.0 | 50+ |

The **most comprehensive local audio production MCP server** — a macOS (Apple Silicon) application with 50+ MCP tools across multiple categories:

- **Multi-Engine TTS** — Qwen3-TTS (0.6B/1.7B, January 2026), Kokoro-82M, Chatterbox (multilingual, 23 languages), Supertonic-2
- **Voice Cloning** — from just 3 seconds of reference audio via Qwen3-TTS, cross-language cloning via Chatterbox (clone in English, speak in Japanese)
- **Audiobook Generation** — full document-to-audiobook pipeline with queueable chapters, reusable voice presets
- **Document Read-Aloud** — PDF, DOCX, EPUB, Markdown, TXT with sentence-level highlighting
- **MCP Tool Categories** — TTS generation on all engines, voice sample management, audiobook generation and progress monitoring, system monitoring, model status checks and downloads
- **Agentic Job Queue** — orchestrated voice cloning server with job management

v2026.04.1. Requires macOS 13+, Apple Silicon (M1/M2/M3/M4), 8GB RAM minimum, 5-10GB storage for models. Local-first — all processing on device.

### Kokoro TTS Ecosystem (Local, Free — EXPANDED)

Kokoro-82M has become the **de facto open-source TTS model for MCP** with multiple dedicated servers:

| Server | Stars | Language | License | Focus |
|--------|-------|----------|---------|-------|
| [koroko-speech-mcp](https://github.com/hammeiam/koroko-speech-mcp) | — | TypeScript | MIT | Original Kokoro MCP — multiple voices, customizable speed |
| [kokoro-mcp-server](https://github.com/aparsoft/kokoro-mcp-server) | 8 | Python | Apache 2.0 | YouTube creators — librosa audio enhancement, batch processing, Streamlit UI, Docker |
| [kokoro-tts-mcp](https://github.com/scottschram/kokoro-tts-mcp) | — | Python | MIT | Apple Silicon MLX acceleration — 28 English voices, Claude Code/Codex/ChatGPT support |
| [kokoro-tts-mcp](https://github.com/mberg/kokoro-tts-mcp) | — | Python | — | S3 cloud integration — MP3 output with optional S3 upload |
| [kokoro-tts-mcp-server](https://github.com/ard1102/kokoro-tts-mcp-server) | — | Python | — | Production deployment — Docker Hub images, production-ready |

All use the Kokoro-82M model (82M parameters) — no API key, no cloud dependencies, no usage limits. Quality comparable to larger commercial models while being significantly faster.

### digitarald/chatterbox-mcp (Local, Auto-Playback)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chatterbox-mcp](https://github.com/digitarald/chatterbox-mcp) | — | Python | — | 1 |

**Simplified local TTS** — wraps the Chatterbox model (by Resemble AI) with a single `speak_text` tool that generates speech and plays it automatically. Preferred over ElevenLabs in blind listening tests. Automatic model loading, real-time progress notifications, configurable output directory.

### Edge TTS Servers (Free Cloud TTS)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [edge_tts_mcp_server](https://github.com/yuiseki/edge_tts_mcp_server) | 7 | TypeScript | MIT | ~2 |
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
| [speech-mcp](https://github.com/Kvadratni/speech-mcp) | 81 | Python | — | ~5 |

The **most complete voice interaction server** — a Goose MCP extension providing bidirectional speech (82 commits):

- **Speech Recognition** — Faster-Whisper (local, base model, no cloud)
- **Speech Synthesis** — Kokoro TTS with 54+ voice models (~523KB each, auto-downloaded)
- **Multi-Speaker Narration** — NEW: narration in JSON/Markdown formats with multiple speakers
- **Audio/Video Transcription** — NEW: transcription with optional timestamps
- **Audio Visualization** — PyQt-based real-time waveform display
- **Silence Detection** — automatically knows when you've finished speaking
- **Voice Persistence** — remembers your voice preference between sessions
- **Continuous Conversation** — ongoing back-and-forth voice interaction

The only MCP server offering a complete conversational voice loop. Requires PortAudio for microphone capture.

### Deepgram Official MCP (NEW — Enterprise STT/TTS)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [deepgram/mcp](https://github.com/deepgram/mcp) | — | Python | MIT | Dynamic |

**Official Deepgram MCP server** — launched April 2026 (v0.1.1). The key innovation: **fetches its tool list from Deepgram's API at runtime** — new tools appear automatically without package upgrades. Covers speech-to-text transcription, text-to-speech generation, speaker diarization, sentiment analysis, topic detection, entity extraction, summarization, and language detection. Supports stdio and SSE transport. Works standalone or integrated with Deepgram CLI. Multiple AI models available including Nova-3, Nova-2, and Whisper.

### Azure MCP Server (Enterprise)

The **Azure MCP Server** includes speech-to-text and text-to-speech tools through Microsoft's Foundry platform. Supports WAV, MP3, OPUS/OGG, FLAC, ALAW, MULAW, MP4, M4A, and AAC. Enterprise-grade with Azure subscription required. Best for organizations already in the Azure ecosystem.

## Music Generation & DAW Control

### shiehn/total-reaper-mcp (600+ REAPER Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [total-reaper-mcp](https://github.com/shiehn/total-reaper-mcp) | 44 | Python | — | 600+ |

The **most comprehensive DAW MCP server** — 100% ReaScript API coverage for REAPER (102 commits):

- **dsl-production** (default) — ~53 tools with natural language DSL plus essential production tools
- **dsl** — 15 tools, minimal natural language interface
- **groq-essential** — ~146 tools, traditional ReaScript, Groq-compatible
- **groq-extended** — 200+ tools
- **midi-production** — ~150 tools, MIDI-focused workflows
- **mixing** — ~120 tools, audio mixing and mastering
- **full** — 600+ tools covering the entire ReaScript API

Developed on macOS, works cross-platform. Requires REAPER 6.83+ with embedded Lua 5.4. Tool profiles let you limit exposed tools based on your LLM's tool count restrictions.

### Other REAPER MCP Servers (EXPANDED)

| Server | Stars | Tools | Focus |
|--------|-------|-------|-------|
| [wegitor/reaper-reapy-mcp](https://github.com/wegitor/reaper-reapy-mcp) | 62 | 40+ | NEW — reapy-based, dual position format (seconds + measure:beat), MIDI/audio/effects/routing |
| [bonfire-audio/reaper-mcp](https://github.com/itsuzef/reaper-mcp) | 56 | 58 | v0.1.1 (March 2026) — renamed from itsuzef, project/track/MIDI/FX/mixing/mastering/rendering/analysis |
| [TwelveTake-Studios/reaper-mcp](https://github.com/TwelveTake-Studios/reaper-mcp) | 15 | 130 | v1.1.0 — built by working producer (7+ albums), workflow automation, setup_sidechain_compression() |
| [Aavishkar-Kolte/reaper-daw-mcp-server](https://github.com/Aavishkar-Kolte/reaper-daw-mcp-server) | — | — | Intelligent music production assistant with automated project control |
| [dschuler36/reaper-mcp-server](https://github.com/dschuler36/reaper-mcp-server) | — | — | Audio analysis for mixing feedback — connects Reaper projects to Claude |

REAPER has the best DAW MCP coverage of any audio production software with 5+ dedicated servers and 800+ total unique tools. No equivalent exists for Ableton Live, Logic Pro, FL Studio, or Pro Tools.

### Suno MCP Servers (AI Music Generation — NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lioensky/MCP-Suno](https://github.com/lioensky/MCP-Suno) | 25 | TypeScript | — | 1 |
| [CodeKeanu/suno-mcp](https://github.com/CodeKeanu/suno-mcp) | 2 | Python | — | 6 |

**AI music generation from text prompts** via the Suno API — the dominant text-to-music platform (Suno v5 released March 2026 with voice cloning, custom model fine-tuning, and Suno Studio DAW):

- **Custom mode** — provide lyrics, style tags, and title for precise control
- **Inspiration mode** — describe what you want and get a fully produced song
- **Song extension** — continue generating from any timestamp
- **Cover/remix creation** — transform existing songs
- **Multiple model versions** — v3.5, v4, v4.5, v4.5plus, v5 (v5 recommended)

CodeKeanu's version adds Docker deployment, WAV conversion, track status monitoring, and credit management. Fully produced songs generated in under a minute.

### linxule/mcp-music-studio (Dual-Mode — NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-music-studio](https://github.com/linxule/mcp-music-studio) | 37 | TypeScript | — | 5 |

**The most complete music composition MCP server** — dual-mode creative environment (March 2026):

- **Composition mode** — ABC notation with real-time sheet music rendering, 30+ selectable instruments, 8 style presets (rock, jazz, bossa, waltz, march, reggae, folk, classical)
- **Performance mode** — Strudel live coding with 72 drum machine banks, 128 GM instruments, built-in synths, filters/reverb/delay effects chain
- **Tools** — `play-sheet-music`, `play-live-pattern`, `get-music-guide`, `get-strudel-guide`, `search-music-docs`
- WAV audio download, live REPL editing, inline rendering in Claude Desktop

### pasie15/mcp-server-musicgpt (AI Music Platform)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-musicgpt](https://github.com/pasie15/mcp-server-musicgpt) | — | TypeScript | — | 24 |

**Full AI music production pipeline** via the MusicGPT API — music generation from text prompts, cover song creation, sound effects, lyrics generation, voice conversion, TTS, mastering, remixing, and AI vocal addition. 24 tools covering the full creative audio spectrum.

### Other Music Generation Servers

| Server | Stars | Focus |
|--------|-------|-------|
| [falahgs/mcp-minimax-music-server](https://github.com/falahgs/mcp-minimax-music-server) | — | MiniMax Music API wrapper for music generation |
| [tubone24/midi-mcp-server](https://github.com/tubone24/midi-mcp-server) | — | MIDI file generation from structured JSON — multi-track, chord support, interactive piano-roll preview, Cloudflare Workers deployment |
| [williamzujkowski/strudel-mcp-server](https://github.com/williamzujkowski/strudel-mcp-server) | — | Strudel.cc live coding — AI-assisted algorithmic composition, 17 curated patterns across 10 genres |

## Podcast Production & Workflow (GAP FILLING)

The podcast-specific workflow gap identified in March 2026 is **actively filling**. Multiple dedicated podcast MCP servers have appeared:

### Podigee MCP (FIRST Hosting Platform — NEW)

**Podigee launched the world's first podcast hosting platform MCP server** (April 2025). Instead of navigating traditional dashboards, podcasters can ask natural language questions like "What were my top episodes this month?" Capabilities include:

- **Natural Language Analytics** — trend analysis, episode comparisons, listener behavior patterns
- **Workflow Automation** — content distribution, show notes generation, social media posting
- **Multi-Podcast Support** — access data across multiple shows or focus on individual podcasts

This is the first time a podcast hosting platform has offered MCP integration — a significant gap closure.

### Other Podcast-Specific Servers (NEW)

| Server | Stars | Focus |
|--------|-------|-------|
| [adamanz/podcast-generator-mcp](https://github.com/adamanz/podcast-generator-mcp) | 4 | Complete Script→Audio→Final Podcast pipeline — 20+ ElevenLabs voices, conversation/interview/educational/debate styles, audio normalization with fades and transitions |
| [walid-koleilat/mcp-podcast-scraper](https://github.com/walid-koleilat/mcp-podcast-scraper) | — | YouTube podcast scraping + Deepgram Nova-2 transcription, RSS tracking, customizable summary prompts |
| [eugenechae/podcast-index-mcp](https://github.com/eugenechae/podcast-index-mcp) | — | Search millions of podcasts — 6 tools for podcast/episode discovery, detailed metadata, value block support |
| [dingkwang/podcast-transcriber-mcp](https://github.com/dingkwang/podcast-transcriber-mcp) | — | RSS feed parsing + OpenAI Whisper transcription — fetch_rss_feed, list_episodes, transcribe_audio |
| kaslin.rocks podcast-assistant-mcp | — | Publishing workflow automation — show notes, social media drafts (X, LinkedIn), blog posts from transcripts, Cloud Run deployment |

## Podcast Feed Management

Several RSS/Atom MCP servers handle podcast feed consumption:

| Server | Language | Focus |
|--------|----------|-------|
| [veithly/rss-mcp](https://github.com/veithly/rss-mcp) | TypeScript | RSS/Atom/RSSHub feeds — most versatile |
| [richardwooding/feed-mcp](https://github.com/richardwooding/feed-mcp) | — | RSS, Atom, and JSON Feed support |
| [hmmroger/simply-feed-mcp](https://github.com/hmmroger/simply-feed-mcp) | — | Real-time feed management and search |
| [imprvhub/mcp-rss-aggregator](https://github.com/imprvhub/mcp-rss-aggregator) | — | Claude Desktop feed aggregation |
| [S1R15H/blog-mcp-server](https://github.com/S1R15H/blog-mcp-server) | — | Blog RSS/Atom with post search |

These work for **consuming** podcast RSS feeds — listing episodes, fetching descriptions, and searching content.

## Streaming Platform Integration

Multiple Spotify MCP servers exist for playback and playlist control:

| Server | Stars | Focus |
|--------|-------|-------|
| [varunneal/spotify-mcp](https://github.com/varunneal/spotify-mcp) | 597 | Claude + Spotify — **marked INACTIVE March 2026**, Spotify deprecating API features |
| [marcelmarais/spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server) | — | Lightweight — Cursor & Claude playback control |
| [Carrieukie/spotify-mcp-server](https://github.com/Carrieukie/spotify-mcp-server) | — | Kotlin — natural language access to Spotify Web API |

Note: varunneal/spotify-mcp reached 597 stars but went inactive in March 2026 as Spotify deprecated several API features. Alternative implementations remain available.

## What's still missing

The podcast workflow gap is narrowing but some areas remain:

- **Limited podcast hosting integrations** — only Podigee has an MCP server; Spotify for Podcasters, Apple Podcasts Connect, Buzzsprout, Podbean, Libsyn still absent
- **No multi-platform distribution** — no single server pushes episodes to Apple, Spotify, Google simultaneously
- **No podcast analytics at scale** — Podigee covers its own platform but no cross-platform listener metrics
- **No transcript editing workflows** — servers produce transcripts but don't support interactive edit/review
- **No audiogram generation** — waveform videos for social media promotion
- **No chapter markers** — enhanced podcasting features like chapters, links, images
- **No dynamic ad insertion** — programmatic ad placement in episodes
- **No Ableton/Logic/FL Studio** — REAPER is the only DAW with MCP coverage

## The bottom line

Podcasting and audio content MCP servers earn **4.5 out of 5**, upgraded from 4/5 in March 2026. The ecosystem has matured substantially across every dimension:

**MiniMax-MCP's explosion to 1,400 stars** (+233%) makes it the most popular audio MCP server — multi-modal TTS, voice cloning, voice design, music generation, image, and video in one package. **MimikaStudio arrived at 540 stars** as the most comprehensive local audio production server with 50+ MCP tools, multi-engine TTS (including the cutting-edge Qwen3-TTS), and voice cloning from just 3 seconds of audio. **ElevenLabs grew to 1,300 stars** with 14 releases and enterprise data residency. **Kokoro-82M spawned a full ecosystem** of dedicated MCP servers for Apple Silicon, Docker production, YouTube creators, and cloud upload. **REAPER DAW expanded** to 5+ servers with 800+ total unique tools, including the new 62-star reaper-reapy-mcp. **Suno music generation arrived** with AI-produced songs from text prompts. **mcp-music-studio** provides dual-mode composition with 30+ instruments and 72 drum banks.

Most importantly, **the podcast-specific workflow gap is filling**. Podigee launched the first podcast hosting platform MCP server. Dedicated servers now handle script-to-audio pipelines, podcast transcription from RSS feeds, publishing workflow automation, and podcast discovery across millions of shows. The gap to 5/5 remains in multi-platform distribution, broad hosting platform coverage (beyond Podigee), and interactive transcript editing — but the trajectory is clear. For audio production broadly, the ecosystem is production-ready. For podcast production specifically, the manual pipeline assembly is giving way to purpose-built tools.

*This review was refreshed on 2026-04-29 using Claude Opus 4.6 (Anthropic). Originally published 2026-03-16.*

