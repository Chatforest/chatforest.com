---
title: "Podcasting & Audio Content MCP Servers — MimikaStudio, ElevenLabs, MiniMax, Reaper DAW, Kokoro TTS, Suno Music, Podcast Workflows, and More"
date: 2026-03-16T18:00:00+09:00
sources_audited: 2026-08-16
description: "Podcasting and audio content MCP servers are giving AI agents full audio production capabilities — text-to-speech synthesis, voice cloning, audio transcription, music generation, DAW control, and podcast publishing workflows"
og_description: "Podcasting & Audio Content MCP servers: MiniMax-MCP EXPLODED 421→1,600 stars multi-modal audio/video/music. MimikaStudio NEW 727 stars 50+ MCP tools multi-engine TTS voice cloning from 3 seconds. ElevenLabs 1,500 stars. total-reaper-mcp 73 stars 600+ tools. Suno MCP NEW AI music generation. Podcast workflow gap FILLING — Podigee FIRST hosting platform MCP, podcast-generator-mcp, podcast-assistant-mcp publishing automation. 45+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Podcasting and audio content MCP servers for AI-powered audio production, speech synthesis, voice cloning, transcription, music generation, DAW control, and podcast publishing workflows. **MiniMax-MCP EXPLODED 421→1,600 stars (+280%)** — MiniMax-AI/MiniMax-MCP (1,600 stars, Python, official) is now the most-starred audio MCP server, combining TTS, voice cloning, voice design from text descriptions, music generation (music-1.5 model), image generation, and video generation (MiniMax-Hailuo-02) in one server. NEW JavaScript implementation MiniMax-MCP-JS (125 stars). The only MCP server covering this many audio+visual modalities. **MimikaStudio is the biggest NEW arrival** — BoltzmannEntropy/MimikaStudio (727 stars, Python, BSL-1.1 source license) is a local-first macOS application with 50+ MCP tools covering TTS generation on multiple engines (Qwen3-TTS 0.6B/1.7B, Kokoro-82M, Chatterbox multilingual 23 languages, Supertonic-2), voice cloning from just 3 seconds of audio, voice sample management, audiobook generation with queueable chapters, and system monitoring. v2026.04.1. The most comprehensive local audio production MCP server. **ElevenLabs grew to 1,500 stars** — elevenlabs/elevenlabs-mcp (1,500 stars, Python, MIT, v0.12.2) remains the most comprehensive cloud audio AI platform with TTS, voice cloning, transcription, sound effects, and soundscapes. NEW data residency configuration for enterprise users. Free tier includes 10,000 credits/month. **blacktop/mcp-tts matured significantly** — grew to 65 stars, 137 commits, now supports Agent Skills open standard, concurrent TTS operation mode alongside sequential, audio file saving, and multi-instance protection via file locks. 4 TTS backends: macOS say, ElevenLabs, Google Gemini TTS (30 voices), OpenAI TTS. **Kokoro TTS ecosystem EXPANDED** — multiple new dedicated servers emerged: scottschram/kokoro-tts-mcp (Apple Silicon MLX acceleration, 28 voices, Claude Code/Codex support), aparsoft/kokoro-mcp-server (14 stars, librosa audio enhancement, YouTube creators, batch processing, Docker), mberg/kokoro-tts-mcp (S3 cloud integration), ard1102/kokoro-tts-mcp-server (Docker Hub production deployment). Kokoro-82M has become the de facto open-source TTS model for MCP. **REAPER DAW coverage expanded** — total-reaper-mcp grew 27→73 stars (+170%) with expanded DSL profiles. NEW wegitor/reaper-reapy-mcp (79 stars, 40+ tools) is now the second-most-starred REAPER server. bonfire-systems/reaper-mcp (118 stars, 58 tools, renamed from itsuzef). TwelveTake-Studios/reaper-mcp (42 stars, 130 tools, v1.6.4). **Suno MCP servers are NEW** — AI music generation from text prompts via Suno API with support for v3.5 through v5.5 ([Suno v5.5 launched March 26, 2026](https://suno.com/blog/v5-5) with voice cloning and custom models), custom lyrics and style, song extension, covers/remixes. lioensky/MCP-Suno (28 stars), CodeKeanu/suno-mcp (11 stars, Docker, WAV conversion). **mcp-music-studio is a NEW standout** — linxule/mcp-music-studio (65 stars) offers dual-mode composition: scored music via ABC notation with 30+ instruments and 8 style presets, plus live performance via Strudel with 72 drum machine banks, 128 GM instruments, and built-in synths. Real-time sheet music rendering in Claude Desktop. **PODCAST WORKFLOW GAP IS FILLING** — Podigee launched the FIRST podcast hosting platform MCP server (analytics, natural language queries, workflow automation). adamanz/podcast-generator-mcp provides a complete Script→Audio→Final Podcast pipeline with 20+ ElevenLabs voices. kaslin.rocks podcast-assistant-mcp automates publishing workflows (show notes, social media, blog posts). walid-koleilat/mcp-podcast-scraper scrapes and transcribes via Deepgram Nova-2. eugenechae/podcast-index-mcp searches millions of podcasts. dingkwang/podcast-transcriber-mcp parses RSS and transcribes via Whisper. **Deepgram OFFICIAL MCP arrived** — deepgram/mcp (v0.1.1, April 2026) fetches tools from Deepgram's API at runtime — new tools appear automatically, no package upgrade needed. STT, TTS, diarization, sentiment, language detection. **Speech-to-text gained multi-speaker narration** — Kvadratni/speech-mcp (83 stars) added multi-speaker narration in JSON/Markdown formats and audio/video transcription with timestamps. **Spotify MCP marked inactive** — varunneal/spotify-mcp (612 stars) went inactive March 2026 as Spotify deprecated API features. Rating upgraded to 4.5/5 — MiniMax explosion to 1,600 stars, MimikaStudio's 727-star 50+ tool arrival, Kokoro ecosystem expansion, Suno music generation, podcast workflow gap finally filling with Podigee and dedicated podcast MCP servers, and Deepgram's official entry all demonstrate this category has matured from 'strong building blocks' to 'near-complete audio production ecosystem.' The podcast-specific gap is narrowing significantly."
last_refreshed: 2026-04-29
---

*Part of the [Media & Entertainment](/categories/media-entertainment/) category.*

Podcasting and audio content MCP servers let AI assistants produce speech, transcribe audio, generate music, control DAWs, clone voices, create sound effects, and now increasingly manage podcast publishing workflows. Instead of manually juggling audio editors, transcription services, and TTS APIs, you can wire these capabilities directly into your AI workflow through the Model Context Protocol.

This review covers the **podcasting and audio content** vertical — text-to-speech, speech-to-text transcription, music generation, DAW control, voice interaction, podcast feed management, and podcast-specific production tools. For video production, see our [Video & Streaming review](/reviews/video-production-streaming-mcp-servers/). For general content creation, see our [Content & Copywriting review](/reviews/cms-content-management-mcp-servers/).

The headline findings: **MiniMax-MCP EXPLODED to 1,600 stars** (+280% from 421) and is now the most-starred audio MCP server. **MimikaStudio arrived at 727 stars** with 50+ MCP tools — the most comprehensive local audio production server with multi-engine TTS, voice cloning from 3 seconds, and audiobook generation. **ElevenLabs grew to 1,500 stars**. **Kokoro TTS spawned an ecosystem** of dedicated MCP servers. **Suno music generation is NEW** — AI music from text prompts. **The podcast workflow gap is finally filling** — Podigee launched the first hosting platform MCP, and dedicated podcast production servers handle script-to-audio pipelines, publishing automation, and podcast search. **REAPER DAW has 600+ tools** across an expanded server ecosystem including a 79-star reaper-reapy-mcp entry.

## Text-to-Speech

### elevenlabs/elevenlabs-mcp (Professional Cloud Platform)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp) | 1,500 | Python | MIT | ~10 |

The **official ElevenLabs MCP server** — provides access to their full AI audio platform, now at [v0.12.2](https://github.com/elevenlabs/elevenlabs-mcp/releases) (78 commits) — *updated 2026-08-16 from the previously cited v0.9.1/14-releases figure, which was stale*:

- **Text-to-Speech** — convert text to natural-sounding speech with fine-grained control over stability, style, and similarity
- **Voice Cloning** — clone voices from audio samples or generate new voices from text descriptions (age, gender, accent, tone)
- **Audio Isolation** — separate speech from background noise
- **Voice Conversion** — make audio sound like a different voice
- **Transcription** — speech-to-text with speaker identification
- **Sound Effects** — generate effects from text descriptions
- **Soundscapes** — create ambient audio environments from descriptions
- **Data Residency** — NEW enterprise configuration for data location preferences
- **Configurable Output Modes** — file output, resource output, or both

Free tier includes [10,000 credits/month](https://elevenlabs.io/pricing). Requires ElevenLabs API key. Works with Claude Desktop, Cursor, Windsurf, and OpenAI Agents. Also available as a community-maintained server: mamertofabian/elevenlabs-mcp-server (118 stars) with SQLite voice generation history tracking and a SvelteKit web client.

### blacktop/mcp-tts (Multi-Engine)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-tts](https://github.com/blacktop/mcp-tts) | 65 | Go | MIT | 4 |

The **Swiss Army knife of TTS** — supports 4 backends through a single MCP server (137 commits, actively maintained):

- **say_tts** — macOS built-in `say` command (free, no API key, offline)
- **elevenlabs_tts** — ElevenLabs API for high-quality speech
- **google_tts** — Google Gemini TTS with 30 high-quality voices (Zephyr, Puck, Charon, Kore, Fenrir, Leda, and more)
- **openai_tts** — OpenAI TTS API with speed control from 0.25x to 4.0x

NEW: Sequential or concurrent TTS operation modes (configurable), audio file saving with format-specific outputs, output suppression to prevent LLM interference, multi-instance protection via system-wide file locks, and **Agent Skills support** — automatically announces completion events across Claude Code, Codex CLI, and Gemini CLI following the Agent Skills open standard.

### MiniMax-AI/MiniMax-MCP (Multi-Modal — EXPLODED)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) | 1,600 | Python | — | 8 |
| [MiniMax-MCP-JS](https://github.com/MiniMax-AI/MiniMax-MCP-JS) | 125 | TypeScript | — | 6 |

**EXPLODED from 421→1,600 stars (+280%)** — now the most-starred audio MCP server. Official MiniMax server combining audio, image, and video generation:

- **text_to_audio** — natural voice synthesis with language boost and subtitle options
- **voice_clone** — replicate voice using audio samples
- **voice_design** — NEW: generate custom voices from text descriptions of desired characteristics
- **music_generation** — high-quality music creation via the enhanced music-1.5 model
- **generate_image** — text-to-image
- **generate_video** — text-to-video with MiniMax-Hailuo-02 (6s/10s duration, 768P/1080P)
- **list_voices** — display available voice options
- **query_video_generation** — check task status

NEW JavaScript implementation (MiniMax-MCP-JS, 125 stars) provides the same capabilities in TypeScript with npm distribution. Supports both stdio and SSE transport. The only MCP server covering this many audio+visual modalities in a single package. Requires MiniMax API key.

### BoltzmannEntropy/MimikaStudio (Local Multi-Engine — NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MimikaStudio](https://github.com/BoltzmannEntropy/MimikaStudio) | 727 | Python | BSL-1.1 (source) | 50+ |

**Correction (2026-08-16 audit):** this table previously listed the license as Apache 2.0. The [repository's own README](https://github.com/BoltzmannEntropy/MimikaStudio) states source code is licensed under the **Business Source License 1.1 (BSL-1.1)** — free for personal/internal use and production use under BSL terms, converting to GPL-2.0-or-later after a stated change date — with binary distributions under a separate proprietary MimikaStudio Binary Distribution License that requires a paid license for commercial use and disallows redistribution. That is materially different from the permissive Apache 2.0 grant this page previously implied. Star count also updated from 540 to the [current 727](https://github.com/BoltzmannEntropy/MimikaStudio).

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
| [kokoro-mcp-server](https://github.com/aparsoft/kokoro-mcp-server) | 14 | Python | Apache 2.0 | YouTube creators — librosa audio enhancement, batch processing, Streamlit UI, Docker |
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
| [speech-mcp](https://github.com/Kvadratni/speech-mcp) | 83 | Python | — | ~5 |

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
| [total-reaper-mcp](https://github.com/shiehn/total-reaper-mcp) | 73 | Python | — | 600+ |

The **most comprehensive DAW MCP server** — 100% ReaScript API coverage for REAPER (114 commits):

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
| [wegitor/reaper-reapy-mcp](https://github.com/wegitor/reaper-reapy-mcp) | 79 | 40+ | NEW — reapy-based, dual position format (seconds + measure:beat), MIDI/audio/effects/routing |
| [bonfire-systems/reaper-mcp](https://github.com/bonfire-systems/reaper-mcp) | 118 | 58 | renamed from itsuzef, project/track/MIDI/FX/mixing/mastering/rendering/analysis |
| [TwelveTake-Studios/reaper-mcp](https://github.com/TwelveTake-Studios/reaper-mcp) | 42 | 130 | v1.6.4 — built by working producer (7+ albums), workflow automation, setup_sidechain_compression() |
| [Aavishkar-Kolte/reaper-daw-mcp-server](https://github.com/Aavishkar-Kolte/reaper-daw-mcp-server) | — | — | Intelligent music production assistant with automated project control |
| [dschuler36/reaper-mcp-server](https://github.com/dschuler36/reaper-mcp-server) | — | — | Audio analysis for mixing feedback — connects Reaper projects to Claude |

**Correction (2026-08-16 audit):** the reaper-mcp entry above was previously listed as "bonfire-audio/reaper-mcp." The [itsuzef/reaper-mcp](https://github.com/itsuzef/reaper-mcp) URL this page links to now redirects to **bonfire-systems/reaper-mcp**, not bonfire-audio — the org name was wrong. Star counts across this table also updated to current figures (all three named servers gained 30-180% in stars since the 2026-04-29 refresh).

REAPER has the best DAW MCP coverage of any audio production software with 5+ dedicated servers and 800+ total unique tools. No equivalent exists for Ableton Live, Logic Pro, FL Studio, or Pro Tools.

### Suno MCP Servers (AI Music Generation — NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lioensky/MCP-Suno](https://github.com/lioensky/MCP-Suno) | 28 | TypeScript | — | 1 |
| [CodeKeanu/suno-mcp](https://github.com/CodeKeanu/suno-mcp) | 11 | Python | — | 6 |

**AI music generation from text prompts** via the Suno API — the dominant text-to-music platform ([Suno v5.5 released March 26, 2026](https://suno.com/blog/v5-5) with voice cloning and custom model fine-tuning; [Suno Studio DAW launched with v5 on September 25, 2025](https://www.prnewswire.com/news-releases/suno-introduces-suno-studio-a-generative-audio-workstation-built-for-all-creatives-from-seasoned-pros-to-aspiring-artists-302567486.html)):

- **Custom mode** — provide lyrics, style tags, and title for precise control
- **Inspiration mode** — describe what you want and get a fully produced song
- **Song extension** — continue generating from any timestamp
- **Cover/remix creation** — transform existing songs
- **Multiple model versions** — v3.5, v4, v4.5, v4.5plus, v5 (v5 recommended)

CodeKeanu's version adds Docker deployment, WAV conversion, track status monitoring, and credit management. Fully produced songs generated in under a minute.

### linxule/mcp-music-studio (Dual-Mode — NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-music-studio](https://github.com/linxule/mcp-music-studio) | 65 | TypeScript | — | 5 |

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

**[Podigee launched the world's first podcast hosting platform MCP server](https://www.podigee.com/en/blog/unlock-the-future-of-podcast-analytics-with-podigees-mcp-server/)** (April 2025). Instead of navigating traditional dashboards, podcasters can ask natural language questions like "What were my top episodes this month?" Capabilities include:

- **Natural Language Analytics** — trend analysis, episode comparisons, listener behavior patterns
- **Workflow Automation** — content distribution, show notes generation, social media posting
- **Multi-Podcast Support** — access data across multiple shows or focus on individual podcasts

This is the first time a podcast hosting platform has offered MCP integration — a significant gap closure.

### Other Podcast-Specific Servers (NEW)

| Server | Stars | Focus |
|--------|-------|-------|
| [adamanz/podcast-generator-mcp](https://github.com/adamanz/podcast-generator-mcp) | 5 | Complete Script→Audio→Final Podcast pipeline — 20+ ElevenLabs voices, conversation/interview/educational/debate styles, audio normalization with fades and transitions |
| [walid-koleilat/mcp-podcast-scraper](https://github.com/walid-koleilat/mcp-podcast-scraper) | — | YouTube podcast scraping + Deepgram Nova-2 transcription, RSS tracking, customizable summary prompts |
| [eugenechae/podcast-index-mcp](https://github.com/eugenechae/podcast-index-mcp) | — | Search millions of podcasts — 6 tools for podcast/episode discovery, detailed metadata, value block support |
| [dingkwang/podcast-transcriber-mcp](https://github.com/dingkwang/podcast-transcriber-mcp) | — | RSS feed parsing + OpenAI Whisper transcription — fetch_rss_feed, list_episodes, transcribe_audio |
| [Kaslin Fields' podcast-assistant-mcp](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/containers/podcast-assistant-mcp/README.md) | — | Publishing workflow automation — show notes, social media drafts (X, LinkedIn), blog posts from transcripts, Cloud Run deployment. Built by the [Kubernetes Podcast from Google](https://kubernetespodcast.com/) co-host; see her [writeup](https://medium.com/google-cloud/how-i-made-an-mcp-server-that-saves-me-an-hour-per-week-d316fb903ad0) |

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
| [varunneal/spotify-mcp](https://github.com/varunneal/spotify-mcp) | 612 | Claude + Spotify — **marked INACTIVE March 2026**, Spotify deprecating API features |
| [marcelmarais/spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server) | — | Lightweight — Cursor & Claude playback control |
| [Carrieukie/spotify-mcp-server](https://github.com/Carrieukie/spotify-mcp-server) | — | Kotlin — natural language access to Spotify Web API |

Note: varunneal/spotify-mcp reached [612 stars](https://github.com/varunneal/spotify-mcp) but went inactive in March 2026 — the repo's own README states: *"[Notice March 2026]: Inactive project. Most PRs will not be merged"* — as Spotify deprecated several API features. Alternative implementations remain available.

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

**MiniMax-MCP's explosion to 1,600 stars** (+280% from 421) makes it the most popular audio MCP server — multi-modal TTS, voice cloning, voice design, music generation, image, and video in one package. **MimikaStudio arrived at 727 stars** as the most comprehensive local audio production server with 50+ MCP tools, multi-engine TTS (including the cutting-edge Qwen3-TTS), and voice cloning from just 3 seconds of audio (source code under BSL-1.1, not a permissive license — see correction above). **ElevenLabs grew to 1,500 stars** with enterprise data residency. **Kokoro-82M spawned a full ecosystem** of dedicated MCP servers for Apple Silicon, Docker production, YouTube creators, and cloud upload. **REAPER DAW expanded** to 5+ servers with 800+ total unique tools, including the 79-star reaper-reapy-mcp. **Suno music generation arrived** with AI-produced songs from text prompts. **mcp-music-studio** provides dual-mode composition with 30+ instruments and 72 drum banks.

Most importantly, **the podcast-specific workflow gap is filling**. Podigee launched the first podcast hosting platform MCP server. Dedicated servers now handle script-to-audio pipelines, podcast transcription from RSS feeds, publishing workflow automation, and podcast discovery across millions of shows. The gap to 5/5 remains in multi-platform distribution, broad hosting platform coverage (beyond Podigee), and interactive transcript editing — but the trajectory is clear. For audio production broadly, the ecosystem is production-ready. For podcast production specifically, the manual pipeline assembly is giving way to purpose-built tools.

*This review's citations were last audited on 2026-08-16 using Claude Sonnet 5 (Anthropic); content was last substantively refreshed 2026-04-29 using Claude Opus 4.6 (Anthropic). Originally published 2026-03-16.*
