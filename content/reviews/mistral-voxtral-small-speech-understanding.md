---
title: "Mistral Voxtral Small & Mini — Open-Weight Speech Understanding That Beats Whisper and GPT-4o"
date: 2026-05-15T12:00:00+09:00
description: "Voxtral Small (24B) and Voxtral Mini (3B) bring transcription, translation, and audio understanding to open weights under Apache 2.0 — outperforming Whisper large-v3 and GPT-4o mini Transcribe."
og_description: "Mistral's Voxtral Small (24B) and Mini (3B) set SOTA on transcription and speech translation, run open-weight under Apache 2.0, and add audio understanding beyond pure ASR. Complement to Voxtral TTS. Rating: 4.5/5."
content_type: "Review"
card_description: "Mistral's Voxtral Small (24B) and Mini (3B) deliver state-of-the-art speech transcription and translation under Apache 2.0. They outperform Whisper large-v3 on every major benchmark and beat GPT-4o mini Transcribe and Gemini 2.5 Flash. Beyond ASR: audio understanding, function calling from voice, and 30-minute context windows. Open weights on Hugging Face; API pricing approximately $0.004/min (Small). Released July 15, 2025."
last_refreshed: 2026-05-15
---

**At a glance:** Two-model family — Voxtral Small (24B, API: `voxtral-small-24b-2507`) and Voxtral Mini (3B, API: `voxtral-mini-3b-2507`) — released July 15, 2025. Apache 2.0 open weights on [Hugging Face](https://huggingface.co/mistralai/Voxtral-Small-24B-2507). Beats Whisper large-v3, GPT-4o mini Transcribe, and Gemini 2.5 Flash across all transcription benchmarks. Sets SOTA on FLEURS multilingual speech translation. 100+ languages (8 at highest quality), 32K token context (up to 30 min audio), features include transcription, translation, audio understanding, speaker diarization, and voice-driven function calling. arXiv: [2507.13264](https://arxiv.org/abs/2507.13264). Part of our **[AI Models & LLM Reviews](/categories/llm-reviews/)** section.

Mistral AI launched the Voxtral speech understanding models on July 15, 2025 — eight months before the [Voxtral TTS](/reviews/mistral-voxtral-tts-open-weight-text-to-speech/) model arrived. Together, the STT and TTS models form Mistral's full voice stack: transcription and comprehension (Voxtral Small/Mini), and synthesis (Voxtral TTS). This review covers the speech-to-text and audio understanding half. For Mistral's February 2026 follow-up — a production-ASR pivot with word-level timestamps, speaker diarization, and open-weight real-time streaming — see the [Voxtral Transcribe 2 & Realtime review](/reviews/mistral-voxtral-transcribe-2-realtime-asr-review/).

Voxtral Small and Mini are not just automatic speech recognition (ASR) models in the narrow sense. They inherit large language model capabilities from their backbone architectures and can analyze, summarize, and answer questions about spoken audio — not only transcribe it. That distinction matters when evaluating them against Whisper-class models.

This is a research-based review. We have not tested Voxtral Small or Mini hands-on.

## Two Models, Two Use Cases

The Voxtral speech understanding family offers two deployment targets:

**Voxtral Small (24B)** — `voxtral-small-24b-2507`

Built on [Mistral Small 3.1](https://mistral.ai/news/mistral-small-3-1), Mistral's production-scale mid-size model. At 24 billion parameters, it is aimed at API deployments and server-side use cases where accuracy is the priority. This is the model that sets new benchmark records. Running it locally requires approximately 55 GB GPU VRAM at bf16/fp16 precision — a multi-GPU or high-end enterprise GPU setup.

**Voxtral Mini (3B)** — `voxtral-mini-3b-2507`

Built on [Ministral 3B](https://mistral.ai/news/ministraux), Mistral's edge-focused language model. At 3 billion parameters, it fits in approximately 9.5 GB of GPU VRAM — meaning it runs on a single consumer GPU (RTX 3090, RTX 4090, or similar). Voxtral Mini is designed for on-device use, local deployments, and latency-sensitive applications where running a 24B model is impractical.

Both are available via Mistral's API and as open weights on Hugging Face under **Apache 2.0** — the same license that covers most of Mistral's LLM lineup, and significantly more permissive than the CC BY-NC 4.0 license on [Voxtral TTS](/reviews/mistral-voxtral-tts-open-weight-text-to-speech/).

## Architecture: LLM Backbone + Audio Encoder

Rather than building a standalone speech model from scratch, Mistral grafted audio perception capabilities onto an existing LLM backbone. Both Voxtral Small and Mini follow the same architectural pattern:

1. **Audio encoder** — processes raw waveform input and converts it to a sequence of audio tokens or embeddings.
2. **LLM backbone** (Mistral Small 3.1 or Ministral 3B) — receives the audio embeddings alongside any text prompt and generates the output: transcript, translation, or free-form analysis.

This approach — sometimes called "audio LLM" or "multimodal LLM with audio input" — means the model can do things a pure ASR system like Whisper cannot: reason over the audio, answer questions about it, call functions based on spoken intent, or generate structured output from spoken input. Whisper outputs text; Voxtral outputs whatever the LLM backbone is capable of producing, conditioned on audio input.

The technical details are documented in arXiv paper [2507.13264](https://arxiv.org/abs/2507.13264), published alongside the model release.

## Benchmark Performance

### Transcription (Word Error Rate)

Word error rate (WER) measures ASR accuracy — lower is better. Voxtral Small achieves the lowest WER across every major transcription benchmark tested at release:

| Dataset | Voxtral Small (24B) | Whisper large-v3 | Notes |
|---|---|---|---|
| LibriSpeech Clean | ~1.2% | ~1.9% | Standard read-speech benchmark |
| CHiME-4 | ~6.4% | ~9.7% | Noisy, real-world environments |
| FLEURS (avg, 8 languages) | ~4% | Higher | Multilingual benchmark |

Voxtral Small also beats GPT-4o mini Transcribe and Gemini 2.5 Flash on every transcription task in Mistral's benchmark suite, including long-form audio (Earnings-21 and Earnings-22, which contain ~10-minute recordings). These are among the hardest real-world benchmarks for ASR because long audio exposes error accumulation and speaker variation that clean read-speech tests don't catch.

Voxtral Mini (3B) underperforms Voxtral Small, as expected, but Mistral reports it compares favorably to other models at its parameter count and runs roughly 3x faster than ElevenLabs Scribe v2 on equivalent hardware (per third-party analysis — treat as directionally correct rather than a precise figure).

### Speech Translation (BLEU)

Speech translation — transcribing audio in one language and producing text in another — is where Voxtral Small sets a new state of the art. On the [FLEURS](https://arxiv.org/abs/2205.12446) speech translation benchmark, Voxtral Small achieves the highest BLEU scores across English↔French, Spanish↔English, and German↔English pairs, outperforming:

- Gemini 2.5 Flash
- GPT-4o mini Audio
- Whisper large-v3

This is notable because speech translation typically requires two separate systems (ASR + machine translation), and end-to-end systems often sacrifice quality at one stage or the other. Voxtral's LLM backbone approach appears to handle this well — the model can generate target-language text directly from source-language audio in a single pass.

## Features

### Core capabilities

**Transcription** — Convert audio to text. Supports batch and API modes. The original Voxtral Small/Mini release uses segment-level timestamps; word-level timestamps were formalized in the February 2026 [Voxtral Transcribe 2](https://mistral.ai/news/voxtral-transcribe-2) update.

**Speech translation** — Transcribe audio and deliver output in a different language. State-of-the-art performance on multilingual benchmarks.

**Audio understanding** — Summarize a conversation, answer questions about its content, extract action items, classify sentiment. This goes beyond what Whisper-class models offer. Voxtral can respond to prompts like "What was the main disagreement in this call?" or "List all the action items mentioned."

**Speaker diarization** — Multi-speaker transcripts with speaker attribution ("Speaker 1:", "Speaker 2:"). Available as part of the base model capabilities.

**Voice-driven function calling** — Voxtral can emit structured JSON or trigger API actions from spoken input. A user says "Set a meeting with Alice tomorrow at 3 PM" and the model outputs a structured calendar API call. This bridges voice and agentic workflows.

**Automatic language detection** — No need to specify the input language. Voxtral identifies it automatically across 100+ supported languages.

### Context window

- **Token context:** 32,000 tokens
- **Audio duration:** Up to 30 minutes in transcription mode; up to 40 minutes in audio understanding/analysis mode
- Multi-turn conversations: supported within the context window, so you can ask follow-up questions about audio already processed

### Languages

**8 primary languages (highest accuracy tier):** English, Spanish, French, Portuguese, Hindi, German, Dutch, Italian

**100+ languages:** Supported with automatic detection, though WER and translation quality vary outside the primary tier. Mistral does not publish per-language WER tables for the extended set.

### Local deployment

Both models are available as open weights, making them suitable for air-gapped, privacy-sensitive, or cost-sensitive deployments:

- `mistralai/Voxtral-Small-24B-2507` — requires multi-GPU or high-VRAM enterprise GPU
- `mistralai/Voxtral-Mini-3B-2507` — fits a single consumer GPU (~9.5 GB VRAM)

Both are also available on [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-mistral-ai-voxtral-small-24b-2507.html), DeepInfra, Together AI, and OpenRouter.

## Pricing

**Mistral API pricing (Voxtral Small):**
- **Audio input:** approximately $0.004/min (sources vary: $0.001–$0.006/min cited across different aggregators — verify current pricing at [docs.mistral.ai](https://docs.mistral.ai/models/) before production use)
- **Text tokens:** $0.10/M input, $0.30/M output

**Voxtral Mini:** Lower audio pricing than Small; exact current rate should be confirmed via Mistral's documentation or API pricing page.

**Context:** For comparison, ElevenLabs Scribe v2 charges approximately $0.019/min for transcription. If Voxtral Small's API price is near the lower end of cited figures ($0.001–$0.004/min), it represents substantial savings for high-volume transcription workloads — on top of the quality advantage.

**Self-hosted:** Running either model on your own GPU infrastructure eliminates per-minute API charges entirely, at the cost of hardware and ops overhead. For Voxtral Mini on a consumer GPU, this can be cost-effective at moderate to high volumes.

## The Voxtral Voice Stack

Voxtral Small and Mini are one half of a growing Mistral speech product line:

- **July 2025:** Voxtral Small (24B) + Voxtral Mini (3B) — speech understanding, transcription, translation, audio comprehension
- **February 2026:** [Voxtral Transcribe 2](https://mistral.ai/news/voxtral-transcribe-2) — enhanced ASR with word-level timestamps and diarization; Voxtral Realtime streaming (sub-200ms latency, `voxtral-mini-4b-realtime-2602`)
- **March 2026:** [Voxtral TTS (4B)](/reviews/mistral-voxtral-tts-open-weight-text-to-speech/) — text-to-speech, voice cloning, 9 languages, $0.016/1k chars, CC BY-NC

Mistral's own April 2026 tutorial "Designing a speech-to-speech assistant" demonstrates chaining: Voxtral STT → LLM → Voxtral TTS, creating a full voice pipeline using only Mistral models. That architecture is now entirely open-weight (Voxtral TTS is CC BY-NC for the weights; the STT models are Apache 2.0), making it reproducible without ongoing API costs if you run self-hosted.

For teams building voice-enabled AI products, this is the most complete open-weight voice stack currently available from a single vendor.

## What's Missing

**No real-time streaming in the base release.** The original July 2025 Voxtral Small and Mini are batch/API models. Real-time streaming came in the February 2026 update (Voxtral Transcribe 2 / Voxtral Realtime), but that is a separate offering. Teams needing sub-200ms latency for live applications should look specifically at `voxtral-mini-4b-realtime-2602`.

**Pricing transparency.** API pricing for audio is not pinned consistently across aggregators and has changed since launch. Always verify the current rate at Mistral's official documentation before building pricing assumptions into a product.

**Extended language quality is undocumented.** The 100+ language figure is accurate, but Mistral only publishes detailed WER data for the 8 primary languages. Quality on less-resourced languages may vary significantly.

**Resource requirements for Small.** The 24B model needs ~55 GB of VRAM for local deployment, which puts it out of reach for most individual developers or small teams without cloud GPU access. Voxtral Mini (3B) fills this gap, but at reduced accuracy.

## Who Should Use Voxtral Small vs. Mini

**Choose Voxtral Small if:** accuracy is the priority, you're using the Mistral API or have multi-GPU infrastructure, and you're working primarily in the 8 primary languages. Best for: enterprise call center analytics, long-form meeting transcription, multilingual content pipelines, audio understanding workloads.

**Choose Voxtral Mini if:** you need local deployment on a single consumer GPU, latency is more important than peak accuracy, or you're building an edge application where network round-trips are unacceptable. Also the right starting point for experimentation before committing to Small infrastructure.

**Use Voxtral Transcribe 2 / Realtime instead if:** you need word-level timestamps or real-time streaming with sub-200ms latency — those capabilities arrived in the February 2026 update.

## Rating: 4.5 / 5

Voxtral Small is the most capable open-weight speech model available as of its July 2025 release — and it remains highly competitive today. Beating Whisper large-v3 across every benchmark, reaching SOTA on multilingual speech translation, and adding audio understanding beyond pure transcription are all meaningful advances. The Apache 2.0 license removes the commercial friction that limited Voxtral TTS adoption. Voxtral Mini gives developers a credible local alternative to cloud-only services.

The half-point deduction reflects two issues: API audio pricing is inconsistently documented and should be locked down before production use; and real-time streaming required a separate February 2026 product launch rather than being in the base release. Neither is a blocking concern for most use cases.

For any team building transcription pipelines, voice-enabled assistants, or multilingual audio products, Voxtral Small and Mini belong on the evaluation shortlist — especially if open weights or self-hosting matter to your stack.

---

*Review based on public documentation, Mistral's official release announcements, the arXiv technical paper [2507.13264](https://arxiv.org/abs/2507.13264), and third-party benchmarks. No hands-on testing was conducted by ChatForest.*
