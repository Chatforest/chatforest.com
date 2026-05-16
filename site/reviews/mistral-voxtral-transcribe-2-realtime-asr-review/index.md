# Mistral Voxtral Transcribe 2 & Realtime — Open-Weight Real-Time ASR at $0.003/Min

> Voxtral Transcribe 2 pairs a batch model with word-level timestamps and speaker diarization against an open-weight real-time streaming model that hits sub-200ms latency — both released February 4, 2026.


**At a glance:** Two-model family released February 4, 2026 — **Voxtral Mini Transcribe V2** (`voxtral-mini-2602`, batch transcription with word-level timestamps, speaker diarization, and context biasing) and **Voxtral Realtime** (`mistralai/Voxtral-Mini-4B-Realtime-2602`, Apache 2.0 open-weight 4B streaming model, sub-200ms configurable latency). Pricing: $0.003/min batch, $0.006/min realtime API. Beats Whisper large-v3 on FLEURS multilingual WER (~5.9% vs 7.4%). 13 languages. arXiv paper for Realtime architecture: [2602.11298](https://arxiv.org/abs/2602.11298). Follows the original [Voxtral Small & Mini](/reviews/mistral-voxtral-small-speech-understanding/) (July 2025). Part of our **[AI Models & LLM Reviews](/categories/llm-reviews/)** section.

Mistral AI's Voxtral Transcribe 2, announced February 4, 2026 under the headline "Voxtral transcribes at the speed of sound," is a deliberate pivot from the original Voxtral's broad audio understanding mission toward production ASR. The July 2025 Voxtral Small and Mini were versatile: transcription, translation, audio Q&A, voice function-calling. Voxtral Transcribe 2 narrows that scope and deepens it — two specialized models optimized for the specific needs of transcription pipelines: speaker attribution, precise timing, domain vocabulary, and real-time streaming.

The result is one of the most cost-competitive ASR offerings available as of this writing, with the notable distinction that the Realtime model runs fully open-weight under Apache 2.0.

This is a research-based review. We have not tested Voxtral Transcribe 2 or Voxtral Realtime hands-on.

## Two Models, One Release

The Voxtral Transcribe 2 announcement bundles two architecturally distinct models:

**Voxtral Mini Transcribe V2** — `voxtral-mini-2602`

A batch transcription model, available via the Mistral API at $0.003 per minute. The focus is maximum accuracy with rich metadata: word-level timestamps, multi-speaker diarization, and context biasing. This model processes complete audio files (not live streams) and returns structured transcripts. The batch model inherits the offline bidirectional encoder architecture from the original Voxtral series.

**Voxtral Realtime** — `mistralai/Voxtral-Mini-4B-Realtime-2602`

A streaming ASR model with a different architecture — a 4B-parameter fully causal encoder/decoder optimized for low-latency inference. Open weights on Hugging Face under Apache 2.0. Self-hostable on a single GPU with ≥16 GB VRAM via vLLM. Available via Mistral's API at $0.006 per minute. Configurable latency from 80ms to 2.4s; 480ms is the documented practical sweet spot that keeps word error rate within 1–2% of the offline model.

The two models serve genuinely different use cases: Transcribe V2 for post-production workflows (captioning, meeting transcripts, content indexing) and Realtime for live applications (voice assistants, live captioning, real-time call analytics).

## Voxtral Mini Transcribe V2: What's New

The original Voxtral Mini (3B, July 2025) could transcribe but lacked some features that production transcription pipelines require. Voxtral Mini Transcribe V2 adds:

### Word-Level Timestamps

Every word in the transcript gets a precise start and end time. This is the foundation for subtitle generation, audio search, and content alignment workflows where sentence-level timing isn't granular enough. The Mistral Studio audio playground exposes timestamp granularity as a user-selectable parameter — word-level or segment-level depending on the use case.

Word-level timestamps are available in the batch model only. The Realtime model does not currently expose timestamps (the architecture is optimized for latency, which conflicts with the post-processing needed for alignment).

### Speaker Diarization

Voxtral Mini Transcribe V2 identifies and labels distinct speakers in the audio — outputting speaker attribution alongside each transcript segment. The original Voxtral Mini 3B (July 2025) did not include diarization; this addition makes Transcribe V2 suitable for meeting transcripts, interview recordings, and call center analytics where speaker identity matters.

Diarization is a batch-only feature. Voxtral Realtime does not support speaker attribution — a meaningful limitation for live multi-speaker use cases like conference calls.

### Context Biasing

Applications with specialized vocabulary — medical terms, product names, proprietary jargon, people's names — frequently encounter higher error rates in general ASR models. Context biasing lets callers inject up to 100 domain-specific terms or proper nouns that the model should prioritize when making transcription decisions.

Practical example: a medical transcription service can inject "ondansetron," "tachycardia," or physician names to reduce misrecognition on specialized terminology. Zoho DataPrep, by contrast, would not otherwise know whether "Fivetran" or "five-tran" was intended.

Context biasing is optimized for English. Support for other languages is described as experimental.

### Language Expansion

The original Voxtral supported 8 languages at highest quality. Voxtral Transcribe 2 expands to 13, adding Arabic, Russian, Japanese, and Korean to the original English, Spanish, French, Portuguese, Hindi, German, Dutch, and Italian.

## Voxtral Realtime: Architecture and Latency Trade-Offs

Voxtral Realtime is architecturally distinct from the batch model. The [arXiv paper 2602.11298](https://arxiv.org/abs/2602.11298) describes a 4B-parameter model using:

- A **causal encoder** with sliding-window attention (750 frames per window) — unlike the bidirectional encoder used in offline models, causal attention processes each frame only with knowledge of past frames, enabling streaming without waiting for the full utterance
- **Configurable emission delay**: the model can emit predictions at delays ranging from 80ms to 2.4 seconds; shorter delays mean faster output but higher word error rate
- Total parameter split: approximately 3.4B in the LM decoder, 0.6B in the causal encoder

The latency-accuracy trade-off curve:

| Emission Delay | Word Error Rate vs. Offline |
|---|---|
| 80ms | Highest degradation |
| 480ms | Within 1–2% of offline model |
| 960ms | Exceeds ElevenLabs Scribe v2 Realtime |
| 2,400ms | Near-offline quality |

At 480ms — below the 500ms threshold that feels instantaneous in a conversation — Voxtral Realtime is competitive with offline models. At 960ms it outperforms ElevenLabs Scribe v2 Realtime entirely. The 80ms floor exists for hard real-time applications where responsiveness takes priority over accuracy.

### Self-Hosting

Voxtral Realtime's open weights enable self-hosting — a major differentiator versus proprietary alternatives like ElevenLabs Scribe v2 or AssemblyAI Universal. Requirements:

- Single GPU with ≥16 GB VRAM (RTX 3090, RTX 4090, A10, A100 40GB, or equivalent)
- vLLM nightly build (not yet in the stable release as of the Feb 2026 launch)
- Serve via the `/v1/realtime` endpoint
- Community GGUF quantizations are available (`freddm/Voxtral-Mini-4B-Realtime-2602-GGUF`) for quantized deployments on lower-VRAM hardware

Red Hat published a day-1 deployment guide for running Voxtral Realtime on vLLM. The Apache 2.0 license permits unrestricted commercial use without attribution requirements or royalties.

Note: the batch model (Voxtral Mini Transcribe V2) does not have open weights published. Only Voxtral Realtime is available for self-hosting.

## Benchmark Performance

Mistral's benchmark reporting for Voxtral Transcribe 2:

**Multilingual (FLEURS benchmark):**
- Voxtral Mini Transcribe V2: ~5.9% average WER across top languages
- Whisper large-v3: ~7.4% average WER
- Improvement: ~20% relative error reduction

**English Long-Form (Earnings-21 dataset):**
- Voxtral: 7.1% WER
- Whisper large-v3: 10.3% WER

**English Read Speech (LibriSpeech Clean):**
- Voxtral 24B: 1.2% WER
- Whisper large-v3: 1.9% WER

**Claimed outperformance over:** GPT-4o mini Transcribe, Gemini 2.5 Flash (ASR mode), AssemblyAI Universal, Deepgram Nova.

**Voxtral Realtime (at 960ms delay):** Exceeds ElevenLabs Scribe v2 Realtime accuracy.

**Important caveat:** These benchmarks are sourced from Mistral's own reporting. Independent third-party evaluations had not been published at the time of this research. Benchmark conditions (audio quality, noise levels, speaker demographics) can significantly affect real-world results. The LibriSpeech Clean benchmark is a particularly favorable test condition (read speech, clean recording environment) that rarely reflects production audio quality.

## Pricing Comparison

| Model | Price | Per-hour equivalent |
|---|---|---|
| Voxtral Mini Transcribe V2 (batch) | $0.003/min | $0.18/hr |
| Voxtral Realtime (API) | $0.006/min | $0.36/hr |
| ElevenLabs Scribe v2 | ~$0.0037/min est. | ~$0.22/hr |
| OpenAI Whisper-1 | $0.006/min | $0.36/hr |
| Deepgram Nova-2 | ~$0.0043/min | ~$0.26/hr |

Mistral claims Voxtral processes audio 3× faster than ElevenLabs Scribe v2 at one-fifth the cost. The batch pricing ($0.003/min) undercuts ElevenLabs by approximately 20% at list, with the streaming tier ($0.006/min) matching OpenAI's Whisper-1.

For self-hosted Realtime deployments (on-premise or cloud VM), the per-minute cost collapses to GPU compute only — typically $0.001–0.003/min on spot A10 instances, depending on utilization.

## What Was in the Original Voxtral That's Not Here

Voxtral Transcribe 2 is a specialization, not a superset. Features present in [Voxtral Small & Mini](/reviews/mistral-voxtral-small-speech-understanding/) (July 2025) that are not part of the Transcribe 2 models:

- **Audio understanding and Q&A**: The original Voxtral could answer questions about audio content ("what was the main topic of this recording?"). Transcribe 2 produces transcripts, not semantic analysis.
- **Voice function-calling**: The July 2025 models could trigger backend APIs from spoken commands. Transcribe 2 does not expose this capability.
- **Translation**: The original Voxtral set SOTA on FLEURS multilingual speech translation. Voxtral Transcribe 2 focuses on transcription within each language, not cross-language translation.
- **Large model size**: Voxtral Small (24B) remains the higher-accuracy option for full audio comprehension. Transcribe 2 is built around the Mini (4B-class) architecture.

Practical guidance: if you need raw transcription with timestamps and speaker labels, Voxtral Transcribe 2 is the right choice. If you need audio understanding, translation, or voice-driven function calling, the original Voxtral Small or Mini 3B remains available.

## Limitations and Caveats

**Diarization not available in Realtime.** Speaker attribution requires post-processing that adds latency. For live multi-speaker applications, there is currently no low-latency path that also provides speaker labels.

**Context biasing is English-optimized.** The 100-term injection feature works best for English content. Other languages are described as experimental, which limits usefulness for specialized multilingual vocabulary.

**vLLM nightly required for self-hosted Realtime.** Using a nightly build in production introduces stability risk. vLLM stable may not have incorporated the Realtime model as of the April–May 2026 timeframe.

**Batch model not open-weight.** Unlike Voxtral Realtime, the batch Voxtral Mini Transcribe V2 is API-only. Organizations that require data sovereignty for their audio transcription cannot self-host the batch model.

**Benchmark provenance.** All primary performance comparisons come from Mistral's own reporting. Third-party benchmark validation was not available at time of research. The claimed 3× speed advantage over ElevenLabs Scribe v2 is a processing-speed claim (audio processed per second), not a latency claim.

**13 language ceiling.** Compared to OpenAI Whisper large-v3 (99 languages) or Gemini's multilingual transcription (50+ languages), Voxtral's 13-language coverage is limited. For teams handling diverse global audio, this may be a blocking constraint.

## Mistral Studio Playground

Mistral Studio includes a dedicated audio playground for Voxtral Transcribe 2. It exposes diarization toggle, timestamp granularity selection (word vs. segment), and supports file upload testing. This is useful for evaluating quality on domain-specific audio before committing to API integration.

## Who Should Use Voxtral Transcribe 2

**Voxtral Mini Transcribe V2 (batch) is a strong choice for:**
- Meeting transcript pipelines needing speaker labels and word-level timing
- Subtitle generation workflows (aligned timing, clean accuracy)
- Podcast and video captioning with multi-speaker identification
- Content indexing that requires searchable, timestamped transcripts
- Teams already using Mistral's API who want to consolidate providers

**Voxtral Realtime is a strong choice for:**
- Voice assistants and live transcription overlays
- Real-time call analytics and monitoring
- On-premise deployments with data-sensitivity requirements (Apache 2.0 open weights)
- Teams that want streaming ASR without a proprietary vendor dependency
- Cost-sensitive high-volume streaming workloads where self-hosting reduces per-minute cost by 50–70%

**Voxtral Transcribe 2 is not the right choice for:**
- Teams needing 99+ language coverage (use Whisper or Gemini)
- Applications requiring audio understanding or semantic Q&A over audio (use original Voxtral Small)
- Real-time diarization (no path available)
- Batch transcription with self-hosting (only Realtime has open weights)

## Rating

**4 / 5**

Voxtral Transcribe 2 delivers on its production-ASR mandate. The batch model's combination of word-level timestamps, speaker diarization, and context biasing covers the core requirements of transcription pipelines at a competitive price. The Realtime model is the standout: sub-200ms open-weight streaming ASR under Apache 2.0, self-hostable on a single consumer GPU, with an arXiv-backed architecture.

The one-point deduction reflects real gaps: diarization cannot be streamed, context biasing works reliably only in English, the batch model lacks open weights, and language coverage (13 languages) is meaningfully narrower than alternatives. For global or multi-speaker live use cases, these gaps matter.

For English-first transcription pipelines or teams building streaming voice applications who value vendor independence, Voxtral Transcribe 2 is among the most compelling options available at this price point.

---

*For coverage of the original Voxtral speech understanding models (July 2025), see the [Mistral Voxtral Small & Mini review](/reviews/mistral-voxtral-small-speech-understanding/). For the synthesis side of Mistral's voice stack, see the [Voxtral TTS review](/reviews/mistral-voxtral-tts-open-weight-text-to-speech/).*

