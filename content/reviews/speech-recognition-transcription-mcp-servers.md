---
title: "Speech Recognition & Transcription MCP Servers — Whisper, Deepgram, Gemini, and More"
date: 2026-03-19T18:00:00+09:00
description: "Speech recognition and transcription MCP servers let AI agents convert audio to text through local Whisper models, cloud APIs, and multimodal LLMs. We reviewed 14+ servers across three approaches: local Whisper-based (speech-mcp with 76 stars leads, plus faster-whisper and whisper.cpp options), cloud API wrappers (Deepgram, OpenAI Whisper API), and multimodal LLM-based transcription (Gemini, GPT-4o Audio, Voxtral). The ecosystem is fragmented — no official vendor server dominates — but local options are surprisingly capable, with Apple Silicon optimization reaching 15x real-time speed."
og_description: "Speech recognition MCP servers: speech-mcp (76 stars, Goose voice interface, faster-whisper + Kokoro TTS, 54 voices), local-stt-mcp (whisper.cpp, Apple Silicon 15x real-time, speaker diarization), Fast-Whisper-MCP-Server (CUDA acceleration, batch processing, VTT/SRT/JSON), voice-to-text-mcp (Rust, Metal/CoreML/CUDA), Deepgram MCP (official devs, Aura TTS), Cloud-ASR-MCP (Gemini/GPT-4o Audio/Voxtral multimodal). 14+ servers across 3 approaches. Rating: 3.5/5."
content_type: "Review"
card_description: "Speech recognition and transcription MCP servers across local Whisper models, cloud APIs, and multimodal LLMs. The speech-mcp project leads with 76 stars and bidirectional voice interaction. Local options offer privacy and zero API cost — whisper.cpp on Apple Silicon hits 15x real-time. Cloud wrappers add convenience with Deepgram and OpenAI APIs. Multimodal approaches using Gemini and GPT-4o Audio are the newest frontier, transcribing with LLM-guided cleanup in a single pass."
---

Speech recognition is the other half of voice AI — and the half that's harder to get right. While text-to-speech has a clear MCP leader (ElevenLabs, covered in our [Audio & Video Processing review](/reviews/audio-video-processing-mcp-servers/)), speech-to-text is fragmented across a dozen small projects with no dominant vendor server.

This review covers MCP servers specifically built for **converting audio to text** — speech recognition, transcription, and dictation. The ecosystem splits into three approaches: **local Whisper-based servers** (run entirely on your hardware, zero API cost), **cloud API wrappers** (Deepgram, OpenAI Whisper API), and **multimodal LLM transcription** (Gemini, GPT-4o Audio, Voxtral). Several servers also include text-to-speech capabilities, but we evaluate them primarily on their STT quality.

The headline: **local Whisper-based servers are surprisingly capable** — whisper.cpp on Apple Silicon hits 15x real-time transcription speed with speaker diarization, entirely offline. **speech-mcp is the most popular** (76 stars) with bidirectional voice interaction. **Cloud-ASR-MCP introduces the most novel approach** — using multimodal LLMs that understand audio natively, skipping the traditional ASR pipeline entirely.

## Local Whisper-Based Servers

These servers run speech recognition entirely on your machine using variants of OpenAI's Whisper model. Zero API cost, full privacy, but require local compute resources.

### speech-mcp (Kvadratni)

| Detail | Info |
|--------|------|
| [Kvadratni/speech-mcp](https://github.com/Kvadratni/speech-mcp) | ~76 stars |
| License | Not specified |
| Language | Python |
| STT Engine | faster-whisper (base model) |
| TTS Engine | Kokoro TTS (54+ voices) |
| Transport | stdio |

The most popular speech recognition MCP server, designed as a voice interface for the Goose AI agent framework. Bidirectional: transcribes your speech and speaks responses aloud, creating a natural conversational loop.

### What Works Well

**Full voice conversation loop.** Goose launches the speech interface, listens for voice input, processes it, speaks the response, then listens again. No manual switching between modes — silence detection handles turn-taking automatically.

**54+ voice models via Kokoro TTS.** The text-to-speech side uses Kokoro, an open-weight 82M parameter model, with a wide selection of voices. Responses are spoken, not just transcribed.

**100% local processing.** Both STT (faster-whisper) and TTS (Kokoro) run locally. No audio data leaves your machine. Good for sensitive conversations or air-gapped environments.

**Audio/video transcription.** Beyond live microphone input, it can transcribe audio and video files with optional timestamps and speaker detection.

### What Doesn't Work Well

**Goose-specific.** Designed for Block's Goose framework. Works with other MCP clients for transcription, but the voice conversation loop is Goose-specific.

**Base Whisper model only.** Uses the faster-whisper "base" model by default for speed. Accuracy is decent but not as good as the "large-v3" model for difficult audio (accents, background noise, technical jargon).

**No license specified.** The GitHub repo has no license file.

### local-stt-mcp (SmartLittleApps)

| Detail | Info |
|--------|------|
| [SmartLittleApps/local-stt-mcp](https://github.com/SmartLittleApps/local-stt-mcp) | Low stars |
| License | Not specified |
| Language | TypeScript |
| STT Engine | whisper.cpp |
| Platform | Apple Silicon optimized |

A high-performance local transcription server using whisper.cpp, the C/C++ port of Whisper. Specifically optimized for Apple Silicon with impressive benchmarks.

### What Works Well

**15.8x real-time on Apple Silicon.** The benchmarks are compelling — 15.8x real-time processing speed via the Apple Neural Engine, compared to 5.5x for WhisperX. A 10-minute audio file transcribes in under 40 seconds.

**Speaker diarization.** Identifies and separates multiple speakers in audio — critical for meeting transcriptions, interviews, and podcasts. Most Whisper MCP servers skip this.

**Under 2GB memory.** Light enough to run alongside other applications on a Mac. WhisperX needs ~4GB for comparison.

**Universal audio support.** Automatic conversion from MP3, M4A, FLAC, WAV, and other formats before transcription. No manual preprocessing needed.

### What Doesn't Work Well

**Apple Silicon only (practically).** While it may work on other platforms, the optimization and benchmarks are specifically for Apple Neural Engine. Linux/Windows users won't see the same performance.

**New project, low adoption.** Limited community feedback and issue history. The performance claims are from the author's benchmarks.

### Fast-Whisper-MCP-Server (BigUncle)

| Detail | Info |
|--------|------|
| [BigUncle/Fast-Whisper-MCP-Server](https://github.com/BigUncle/Fast-Whisper-MCP-Server) | Low stars |
| License | Not specified |
| Language | Python |
| STT Engine | faster-whisper |
| GPU | CUDA acceleration |

A Faster Whisper server targeting NVIDIA GPU users. Supports multiple model sizes from tiny to large-v3, batch processing, and multiple output formats.

### What Works Well

**CUDA acceleration.** If you have an NVIDIA GPU, this is the fastest local option on Linux/Windows. Automatic CUDA detection with CPU fallback.

**Multiple model sizes.** Choose from tiny (fastest, least accurate) to large-v3 (slowest, most accurate) based on your quality/speed requirements. The flexibility matters — transcribing meeting notes doesn't need the same accuracy as medical dictation.

**Multiple output formats.** VTT subtitles, SRT, and JSON. Useful for subtitle generation workflows beyond just raw transcription.

**Batch processing.** Process multiple audio files in a single operation. Good for transcribing a batch of recorded interviews or podcast episodes.

### What Doesn't Work Well

**NVIDIA-only for GPU.** No Metal (macOS) or ROCm (AMD) support. CPU fallback works but is much slower.

**Low adoption.** Few stars, limited community validation.

### voice-to-text-mcp (acazau)

| Detail | Info |
|--------|------|
| [acazau/voice-to-text-mcp](https://github.com/acazau/voice-to-text-mcp) | Low stars |
| License | Not specified |
| Language | Rust |
| STT Engine | whisper-rs (whisper.cpp bindings) |
| GPU | Metal, CoreML, CUDA |

The only Rust-based speech MCP server. Cross-platform hardware acceleration — Metal/CoreML on macOS, CUDA on Linux/Windows, with CPU fallback everywhere.

### What Works Well

**True cross-platform GPU acceleration.** The only server that supports both Apple Metal/CoreML and NVIDIA CUDA. Wherever you run it, it uses whatever GPU is available.

**Rust performance.** Lower overhead than Python-based alternatives. The whisper-rs bindings are well-maintained.

**Claude Code integration.** Designed to work directly with Claude Code for voice-to-code dictation. Dictate code, comments, and documentation by voice within your development workflow.

### What Doesn't Work Well

**Long build times.** First build with CUDA takes 6+ minutes due to whisper-rs-sys compilation. Metal/CoreML takes 2-3 minutes. Not a quick install.

**Early project.** Limited documentation and community adoption.

## Cloud API Wrappers

These servers call external speech recognition APIs. Better accuracy on difficult audio, no local compute needed, but require API keys and incur costs.

### Deepgram MCP Servers

| Server | Stars | Language | Type |
|--------|-------|----------|------|
| [deepgram-devs/deepgram-mcp](https://github.com/deepgram-devs/deepgram-mcp) | Low | TypeScript | TTS (official devs) |
| [reddheeraj/Deepgram-MCP](https://github.com/reddheeraj/Deepgram-MCP) | Low | Python | STT + TTS + diarization |

Two Deepgram MCP implementations with different scopes:

**deepgram-devs/deepgram-mcp** is from Deepgram's developer team but focuses on **text-to-speech** using Deepgram's Aura voices. It generates audio files from text — not a transcription server despite the Deepgram brand.

**reddheeraj/Deepgram-MCP** is a community server that covers the full Deepgram API: audio transcription, text-to-speech, speaker diarization, language detection, and multiple model support. This is the one to use for speech recognition.

### What Works Well (reddheeraj)

**Deepgram's recognition quality.** Deepgram is one of the fastest and most accurate commercial ASR services, particularly strong on conversational speech, phone calls, and noisy audio. The MCP wrapper gives you access to this quality.

**Speaker diarization + language detection.** Automatically identifies speakers and detects the language of audio — features that require significant additional work with local Whisper.

**Smart audio compression.** Automatically compresses generated audio files for efficient transfer between the MCP server and client.

### What Doesn't Work Well

**API costs.** Deepgram charges per audio minute. Fine for occasional use, expensive for bulk transcription.

**No official vendor MCP server for STT.** The deepgram-devs server is TTS-only. The full-featured community server lacks official backing.

### OpenAI Whisper API Servers

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [arcaputo3/mcp-server-whisper](https://github.com/arcaputo3/mcp-server-whisper) | ~2 | Python | Multiple |
| [Ichigo3766/audio-transcriber-mcp](https://github.com/Ichigo3766/audio-transcriber-mcp) | Low | Python | 1 |
| [mfleurival/whisper-mcp-v2](https://github.com/mfleurival/whisper-mcp-v2) | Low | Python | Multiple |

Three servers wrapping OpenAI's Whisper API:

**arcaputo3/mcp-server-whisper** is the most architecturally sophisticated — well-documented Domain-Driven Design with Pydantic models, regex-based file searching, batch processing, format conversion, automatic compression for oversized files, and enhanced transcription with specialized prompts. Also includes TTS capabilities via OpenAI's speech services. The architecture is over-engineered for its adoption (2 stars), but the code quality is high.

**mfleurival/whisper-mcp-v2** supports multiple output formats: JSON, text, SRT, VTT, and verbose JSON. Good for subtitle generation. Language support for non-English audio.

**Ichigo3766/audio-transcriber-mcp** is the simplest — a clean, focused transcription tool using the OpenAI Whisper API. One tool, one job.

All three require an OpenAI API key. The Whisper API is relatively cheap ($0.006/minute) but not free.

## Multimodal LLM-Based Transcription

The newest approach: skip traditional ASR entirely and use multimodal LLMs that understand audio natively.

### Cloud-ASR-MCP (danielrosehill)

| Detail | Info |
|--------|------|
| [danielrosehill/Cloud-ASR-MCP](https://github.com/danielrosehill/Cloud-ASR-MCP) | Low stars |
| License | Not specified |
| Language | Python |
| Models | Gemini, GPT-4o Audio, Voxtral |
| Status | Work in progress |

Uses audio-capable multimodal models — Gemini, GPT-4o Audio, and Voxtral — that process audio in a single pass. The key innovation: you can provide text prompt guidance to clean up transcripts on the fly.

### What Works Well

**Prompt-guided transcription.** Tell the model "this is a medical interview, fix any medical terminology" or "remove filler words and false starts" — the LLM applies contextual understanding during transcription, not after. This is genuinely different from traditional ASR + post-processing pipelines.

**Multiple model backends.** Switch between Gemini (Google), GPT-4o Audio (OpenAI), and Voxtral (Mistral) depending on quality/cost requirements. Each model has different strengths.

### What Doesn't Work Well

**Work in progress.** The project is explicitly WIP. Expect rough edges.

**Higher cost.** Multimodal LLM inference is more expensive per minute than dedicated ASR APIs. Best for small volumes where accuracy matters more than cost.

**Latency.** LLM inference adds latency compared to purpose-built ASR models. Not suitable for real-time transcription.

### Gemini-Transcription-MCP (danielrosehill)

| Detail | Info |
|--------|------|
| [danielrosehill/Gemini-Transcription-MCP](https://github.com/danielrosehill/Gemini-Transcription-MCP) | Low stars |
| License | Not specified |
| Language | Python |
| Model | Gemini multimodal |

A focused implementation using only Gemini's multimodal audio capabilities, with built-in post-processing. By the same author as Cloud-ASR-MCP — this is the single-model version for teams standardized on Google.

## Desktop Voice Agents

These go beyond transcription to provide complete voice-controlled agent experiences.

### t2t (acoyfellow)

| Detail | Info |
|--------|------|
| [acoyfellow/t2t](https://github.com/acoyfellow/t2t) | Low stars |
| License | Not specified |
| Language | TypeScript |
| STT Engine | Whisper (local) |
| Platform | Cross-platform desktop |

A cross-platform desktop application combining system-wide dictation with MCP agent integration. Two modes: hold `fn` for plain dictation (voice-to-text anywhere), hold `fn+ctrl` for agent mode (voice commands routed to any connected MCP server).

### What Works Well

**System-wide dictation.** Works in any application — not just MCP clients. Hold the fn key, speak, release, and text appears wherever your cursor is. This alone makes it useful as a general dictation tool.

**Agent mode.** The `fn+ctrl` mode connects to any MCP server(s), letting you give voice commands that trigger tool calls. Multiple simultaneous MCP servers supported via stdio, HTTP, and SSE transports.

**Visual feedback.** Red bar while recording dictation, cyan for agent mode, amber while processing. Simple but effective.

**Fully local STT.** Only the OpenRouter API calls for agent responses go to the cloud. Transcription stays local.

### What Doesn't Work Well

**Not code-signed.** macOS shows security warnings on first launch. Users need to manually allow execution in System Settings.

**Early stage.** Featured on Hacker News in late 2025 but still maturing. Limited documentation.

## Also notable

- **ElevenLabs MCP** (1,300 stars, official) — covered in our [Audio & Video Processing review](/reviews/audio-video-processing-mcp-servers/). Includes transcription alongside TTS/voice cloning/sound effects. The strongest vendor server touching speech, but transcription isn't its primary focus.
- **Vexa** (1,800 stars) — meeting transcription with real-time Whisper, covered in our [Video Conferencing review](/reviews/video-conferencing-mcp-servers/). Specialized for meeting contexts.
- **speaches-ai/speaches** — OpenAI API-compatible server for STT (faster-whisper) and TTS (piper/Kokoro) with streaming. Not MCP-native, but can be used as a backend for MCP servers.
- **blacktop/mcp-tts** — multi-engine TTS server supporting macOS say, ElevenLabs, Google TTS, and OpenAI TTS. Purely text-to-speech, no recognition.
- **kristofferv98/MCP_tts_server** — Kokoro + OpenAI TTS with streaming and fallback between engines.
- **mberg/kokoro-tts-mcp** — Kokoro TTS with S3 upload for generated audio files.

## The bottom line

Speech recognition MCP servers are plentiful but fragmented. No single project has achieved the adoption or polish of ElevenLabs on the TTS side. The ecosystem splits cleanly:

**Local Whisper servers** are the practical choice for most users. They're free, private, and faster than you'd expect — especially on Apple Silicon (15x real-time) or NVIDIA GPUs. The tradeoff is setup complexity and accuracy on difficult audio.

**Cloud API wrappers** offer better accuracy with less setup, but add cost and external dependencies. Deepgram's community MCP server is the most capable, though it lacks official vendor backing for STT.

**Multimodal LLM transcription** is the most interesting emerging approach. Prompt-guided transcription — where the model understands context and cleans up output in one pass — could eventually make traditional ASR pipelines obsolete for low-volume, high-accuracy use cases. But it's early and expensive.

**Best for local transcription:** speech-mcp (76 stars, bidirectional voice, Goose integration)
**Best for Apple Silicon:** local-stt-mcp (whisper.cpp, 15x real-time, speaker diarization)
**Best for NVIDIA GPUs:** Fast-Whisper-MCP-Server (CUDA acceleration, batch processing)
**Best for cross-platform:** voice-to-text-mcp (Rust, Metal + CUDA support)
**Best for accuracy:** reddheeraj/Deepgram-MCP (commercial ASR + diarization + language detection)
**Best for context-aware transcription:** Cloud-ASR-MCP (multimodal LLMs with prompt guidance)
**Best for system-wide dictation:** t2t (desktop app, fn-key dictation + agent mode)

Rating: **3.5/5** — A working ecosystem with solid local options and interesting cloud/multimodal approaches, but held back by low adoption across the board (no server above 76 stars), missing official vendor servers (Deepgram's official MCP is TTS-only, OpenAI has no Whisper MCP at all), and fragmentation that forces users to evaluate many similar low-star projects. The local Whisper options are genuinely useful today; the multimodal LLM approach is where the category gets exciting.

---

*This review was researched and written by an AI agent. We have not personally tested these servers — our analysis is based on documentation, source code, GitHub metrics, and community adoption. See our [methodology](/about/) for details.*

*This review was last edited on 2026-03-19 using Claude Opus 4.6 (Anthropic).*
