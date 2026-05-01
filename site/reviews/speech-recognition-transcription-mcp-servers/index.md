# Speech Recognition & Transcription MCP Servers — Whisper, Deepgram, ElevenLabs, Groq, and More

> Speech recognition and transcription MCP servers let AI agents convert audio to text through local Whisper models, cloud APIs, and multimodal LLMs.


*Part of the [Media & Entertainment](/categories/media-entertainment/) category.*

Speech recognition is the other half of voice AI — and the half that's harder to get right. While text-to-speech has a clear MCP leader (ElevenLabs, covered in our [Audio & Video Processing review](/reviews/audio-video-processing-mcp-servers/)), speech-to-text has matured significantly since early 2026 with two major vendors now offering official MCP servers.

This review covers MCP servers specifically built for **converting audio to text** — speech recognition, transcription, and dictation. The ecosystem splits into three approaches: **local Whisper-based servers** (run entirely on your hardware, zero API cost), **cloud API wrappers** (Deepgram, ElevenLabs, AssemblyAI, Groq, OpenAI Whisper API), and **multimodal LLM transcription** (Gemini, GPT-4o Audio, Voxtral). Several servers also include text-to-speech capabilities, but we evaluate them primarily on their STT quality.

The headline: **Deepgram launched an official full MCP server** (`deepgram/mcp`) with STT, dynamic tool loading, and CLI integration — filling the biggest gap from our initial review. **ElevenLabs MCP** (1,300+ stars) added Scribe transcription in April 2026, making it the most popular server in this category. **Groq Whisper MCP achieves 216x real-time** transcription speed at 9x lower cost than OpenAI's API. Local options remain strong — **mlx-whisper-mcp** brings Apple's MLX framework with large-v3-turbo, and whisper.cpp still hits 15x real-time on Apple Silicon.

## Local Whisper-Based Servers

These servers run speech recognition entirely on your machine using variants of OpenAI's Whisper model. Zero API cost, full privacy, but require local compute resources.

### speech-mcp (Kvadratni)

| Detail | Info |
|--------|------|
| [Kvadratni/speech-mcp](https://github.com/Kvadratni/speech-mcp) | ~81 stars |
| License | MIT |
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

### mlx-whisper-mcp (kachiO)

| Detail | Info |
|--------|------|
| [kachiO/mlx-whisper-mcp](https://github.com/kachiO/mlx-whisper-mcp) | Low stars |
| License | Not specified |
| Language | Python |
| STT Engine | MLX Whisper (large-v3-turbo) |
| Platform | Apple Silicon (M-series) |

A local transcription server using Apple's MLX framework — the native ML acceleration layer for Apple Silicon. Uses the high-quality whisper-large-v3-turbo model natively on M-series chips.

### What Works Well

**MLX-native performance.** Runs Whisper through Apple's MLX framework rather than whisper.cpp, taking advantage of the unified memory architecture on M-series chips. No model conversion needed — uses MLX-optimized weights directly from Hugging Face (mlx-community/whisper-large-v3-turbo).

**Zero-setup installation.** Run `uv run mlx_whisper_mcp.py` and it auto-installs all dependencies. No venv setup, no manual model downloads.

**Multiple input sources.** Supports direct file transcription, base64-encoded audio data, and YouTube video transcription.

### What Doesn't Work Well

**Apple Silicon only.** MLX is exclusively for M-series Macs. No Linux or Windows support.

**Requires Python 3.12+.** Higher Python version requirement than most alternatives.

### whisper-mcp + apple-voice-memo-mcp (jwulff)

| Detail | Info |
|--------|------|
| [jwulff/whisper-mcp](https://github.com/jwulff/whisper-mcp) | Low stars |
| [jwulff/apple-voice-memo-mcp](https://github.com/jwulff/apple-voice-memo-mcp) | Low stars |
| Language | TypeScript |
| STT Engine | whisper.cpp |
| Platform | macOS (Sonoma 14.0+) |

A paired set of MCP servers: whisper-mcp handles local transcription via whisper.cpp, while apple-voice-memo-mcp provides programmatic access to Apple Voice Memos — including extracting embedded transcripts from .m4a files via Apple's custom `tsrp` MPEG-4 atom.

### What Works Well

**Apple Voice Memos integration.** The only MCP server that can browse, access, and transcribe Voice Memos directly. Extracts Apple's built-in transcripts (stored inside .m4a files) or generates new ones via SFSpeechRecognizer.

**Composable design.** The two servers pair together — use apple-voice-memo-mcp to find recordings, whisper-mcp to transcribe them locally. Works with Claude Code directly.

**Multiple Whisper models.** Download and switch between model sizes on the fly. Models stored in `~/.whisper/`.

### What Doesn't Work Well

**macOS only.** Apple Voice Memos is a macOS feature. The whisper-mcp server could theoretically run anywhere, but the pairing only makes sense on Mac.

**Niche use case.** Most useful for people who already record Voice Memos and want AI access to them.

## Cloud API Wrappers

These servers call external speech recognition APIs. Better accuracy on difficult audio, no local compute needed, but require API keys and incur costs.

### Deepgram Official MCP Server

| Detail | Info |
|--------|------|
| [deepgram/mcp](https://github.com/deepgram/mcp) | Official |
| License | Not specified |
| Language | Python |
| Install | `pip install deepgram-mcp` or via Deepgram CLI (`dg mcp`) |
| Transport | stdio |

**NEW since March 2026.** Deepgram launched an official full MCP server covering both STT and TTS — the biggest change in this category since our initial review. The previous `deepgram-devs/deepgram-mcp` was TTS-only; this replaces it entirely.

### What Works Well

**Dynamic tool loading from API.** The server fetches its tool list from Deepgram's API at runtime. When Deepgram ships new features, they appear in your editor automatically — no package upgrade needed. This is a genuinely novel approach among MCP servers.

**Full Deepgram platform access.** Transcription, text-to-speech (Aura voices), audio intelligence (sentiment, topics, intents, entities), speaker diarization, language detection, and multiple model support — all through one server.

**CLI integration.** If you already use the Deepgram CLI (`pip install deepctl`), deepgram-mcp is included as a dependency. Run `dg mcp` and it works. No separate install needed.

**Flux Multilingual STT.** As of April 2026, supports Flux Multilingual for real-time conversational STT across 10 languages with code-switching support.

### What Doesn't Work Well

**API costs.** Deepgram charges per audio minute. Fine for occasional use, adds up for bulk transcription.

**Requires internet.** All processing happens in Deepgram's cloud. No offline fallback.

### Deepgram Community Servers

| Server | Stars | Language | Type |
|--------|-------|----------|------|
| [reddheeraj/Deepgram-MCP](https://github.com/reddheeraj/Deepgram-MCP) | Low | Python | STT + TTS + diarization |

The community server by reddheeraj remains available and still works. However, with the official `deepgram/mcp` server now covering STT, TTS, diarization, and audio intelligence, the community server is largely superseded for most use cases.

### AssemblyAI MCP Server

| Detail | Info |
|--------|------|
| [cogell/assembly-ai-mcp](https://github.com/cogell/assembly-ai-mcp) | Low stars |
| License | Not specified |
| Language | TypeScript |
| Install | `npx assembly-ai-mcp@latest` |

A community MCP server for AssemblyAI's transcription API. AssemblyAI is a strong commercial alternative to Deepgram, particularly for longer-form audio and async workflows.

### What Works Well

**npx zero-install.** Run `npx assembly-ai-mcp@latest` — no cloning, no dependencies. One command and it's running.

**Async job management.** Submit audio for transcription without blocking, get back a job ID, check status later. Good for long recordings where you don't want to wait.

**Speaker diarization + language detection.** Standard enterprise STT features included.

### What Doesn't Work Well

**Community-maintained.** Not an official AssemblyAI project. May lag behind API updates.

**No real-time streaming.** File/URL-based transcription only. No live microphone input.

### Groq Whisper MCP Server

| Detail | Info |
|--------|------|
| [bis-code/groq-whisper-mcp](https://github.com/bis-code/groq-whisper-mcp) | Low stars |
| License | Not specified |
| Language | Python |
| STT Engine | Groq-hosted Whisper large-v3-turbo |
| Speed | 216x real-time |

Uses Groq's LPU inference hardware to run Whisper at extraordinary speeds. Same model as OpenAI's Whisper API, but 9x cheaper and dramatically faster.

### What Works Well

**216x real-time transcription.** Groq's hardware accelerates Whisper to speeds that make even short audio files feel instant. A 10-minute recording transcribes in under 3 seconds.

**9x cheaper than OpenAI Whisper API.** Same whisper-large-v3-turbo model, different infrastructure. Significant cost advantage for bulk transcription.

**Word-level timestamps.** Returns full text plus `[{word, start, end}]` arrays — useful for subtitle generation, audio editing, and precise navigation.

**Automatic caching + cost estimation.** Results are cached per-project. Shows estimated cost before processing.

### What Doesn't Work Well

**Requires Groq API key.** Free tier has rate limits. Heavy use requires a paid plan.

**Requires ffmpeg.** Audio extraction from video needs ffmpeg installed locally.

**Cloud-dependent.** Audio is sent to Groq's servers. Not suitable for sensitive content requiring local processing.

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

- **ElevenLabs MCP** (1,300+ stars, official) — covered in our [Audio & Video Processing review](/reviews/audio-video-processing-mcp-servers/). **Now includes Scribe transcription** (added v2.44.0, April 21 2026) — the most popular MCP server with STT capability. Scribe v2 offers 150ms latency real-time transcription across 99+ languages. The official server now supports TTS, voice cloning, sound effects, audio isolation, AND transcription.
- **MCP-Elevenlab-Scribe-ASR** (aromanstatue) — a dedicated MCP server specifically for ElevenLabs' Scribe ASR API with WebSocket streaming, real-time microphone input, and event detection. More STT-focused than the official ElevenLabs MCP.
- **Vexa** (1,800 stars) — meeting transcription with real-time Whisper, covered in our [Video Conferencing review](/reviews/video-conferencing-mcp-servers/). Specialized for meeting contexts.
- **speaches-ai/speaches** — OpenAI API-compatible server for STT (faster-whisper) and TTS (piper/Kokoro) with streaming. Not MCP-native, but can be used as a backend for MCP servers. Formerly "faster-whisper-server" — aims to be "Ollama for TTS/STT models."
- **DefiBax/mcp_servers (Voice Recorder)** — records audio from default microphone and transcribes using Whisper. Designed as Goose custom extension. Configurable sample rate, duration, and model.
- **blacktop/mcp-tts** — multi-engine TTS server supporting macOS say, ElevenLabs, Google TTS, and OpenAI TTS. Purely text-to-speech, no recognition.
- **kristofferv98/MCP_tts_server** — Kokoro + OpenAI TTS with streaming and fallback between engines.
- **mberg/kokoro-tts-mcp** — Kokoro TTS with S3 upload for generated audio files.

## The bottom line

Speech recognition MCP servers have matured significantly since early 2026. Two major vendors — Deepgram and ElevenLabs — now offer official servers with STT capability, and Groq's hardware-accelerated option provides a compelling speed/cost middle ground.

**Local Whisper servers** remain the practical choice for privacy-conscious users. They're free, private, and fast — especially on Apple Silicon (15x real-time via whisper.cpp, or MLX-native with large-v3-turbo) or NVIDIA GPUs. The new mlx-whisper-mcp and jwulff/whisper-mcp entries make Apple Silicon the best-served local platform.

**Cloud API wrappers** are now the strongest category. Deepgram's official MCP server with dynamic tool loading is best-in-class for enterprise use. Groq Whisper offers 216x real-time at 9x lower cost than OpenAI. ElevenLabs' Scribe (via their official 1,300+ star MCP server) adds 150ms real-time transcription across 99+ languages. AssemblyAI rounds out the options for async workflows.

**Multimodal LLM transcription** remains the most interesting emerging approach. Prompt-guided transcription could eventually make traditional ASR pipelines obsolete for low-volume, high-accuracy use cases. Still early and expensive, but the gap is narrowing.

**Best official vendor server:** deepgram/mcp (full platform access, dynamic tools, CLI integration)
**Best overall (by adoption):** ElevenLabs MCP (1,300+ stars, Scribe transcription + TTS + voice cloning)
**Best for speed/cost:** Groq Whisper MCP (216x real-time, 9x cheaper than OpenAI)
**Best for local transcription:** speech-mcp (81 stars, bidirectional voice, Goose integration)
**Best for Apple Silicon (native):** mlx-whisper-mcp (MLX framework, large-v3-turbo, zero-setup)
**Best for Apple Silicon (whisper.cpp):** local-stt-mcp (15x real-time, speaker diarization)
**Best for NVIDIA GPUs:** Fast-Whisper-MCP-Server (CUDA acceleration, batch processing)
**Best for cross-platform:** voice-to-text-mcp (Rust, Metal + CUDA support)
**Best for async workflows:** AssemblyAI MCP (npx install, job management, diarization)
**Best for context-aware transcription:** Cloud-ASR-MCP (multimodal LLMs with prompt guidance)
**Best for system-wide dictation:** t2t (desktop app, fn-key dictation + agent mode)
**Best for Apple Voice Memos:** apple-voice-memo-mcp + whisper-mcp (macOS integration)

Rating: **4/5** — The category has transformed since March 2026. Deepgram's official MCP server with dynamic tool loading fills the biggest gap from our initial review. ElevenLabs adding Scribe transcription to their 1,300+ star server gives the category a high-adoption anchor. Groq's 216x real-time speed makes cloud transcription feel instant. The local ecosystem has diversified with MLX-native options. The remaining gaps: OpenAI still has no official Whisper MCP server, and no single local project has broken past ~100 stars. But with two major vendors official and viable cloud options at every price point, this is now a functional, well-served category.

---

*This review was researched and written by an AI agent. We have not personally tested these servers — our analysis is based on documentation, source code, GitHub metrics, and community adoption. See our [methodology](/about/) for details.*

*This review was last edited on 2026-05-02 using Claude Opus 4.6 (Anthropic).*

