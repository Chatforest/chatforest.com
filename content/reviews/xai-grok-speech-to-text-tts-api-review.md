---
title: "xAI Grok Speech APIs Review: STT at $0.10/hr, TTS at $4.20/M Chars, Battle-Tested on Tesla and Starlink"
date: 2026-05-22T10:00:00+09:00
description: "xAI launched standalone Grok Speech-to-Text and Text-to-Speech APIs on April 18, 2026. STT prices at $0.10/hr batch and $0.20/hr streaming — below ElevenLabs, Deepgram, and AssemblyAI — and claims 5.0% error on phone call entity recognition vs. 12–21% for rivals. TTS delivers five voices across 20 languages at $4.20/M characters. We review the specs, pricing, and what this means for the voice developer market."
og_description: "Grok STT: $0.10/hr batch, $0.20/hr streaming, 25+ languages, speaker diarization, word-level timestamps — built on the same stack that runs Grok Voice in Tesla vehicles and Starlink support. Grok TTS: $4.20/M chars, 5 voices, 20 languages. Benchmark: 5.0% phone call entity recognition error vs. ElevenLabs 12.0%, Deepgram 13.5%, AssemblyAI 21.3%. Launched April 18, 2026."
content_type: "Review"
card_description: "xAI launched standalone speech APIs on April 18, 2026. Grok Speech-to-Text prices at $0.10/hr for batch transcription and $0.20/hr for real-time streaming — built on the same production stack handling Grok Voice in Tesla vehicles and Starlink customer support. It supports 25+ languages, speaker diarization, word-level timestamps, and file uploads up to 500 MB. xAI claims a 5.0% entity recognition error rate on phone call audio, versus ElevenLabs at 12.0%, Deepgram at 13.5%, and AssemblyAI at 21.3%. Grok TTS is priced at $4.20 per million characters with five voices (Ara, Eve, Leo, Rex, Sal) across 20 languages and speech-tag controls. For developers building voice agents, transcription pipelines, or audio search, the pricing is meaningfully below incumbents — though the benchmark is xAI's own and warrants independent verification. Rating: 3.5/5."
tags: ["ai-api", "speech-to-text", "text-to-speech", "audio-ai", "xai", "grok", "voice-ai", "developer-tools", "enterprise-ai"]
categories: ["reviews"]
rating: 4
author: "ChatForest"
last_refreshed: 2026-05-22
---

On April 18, 2026, xAI launched two standalone APIs that most observers had not anticipated: a **Speech-to-Text (STT) API** and a **Text-to-Speech (TTS) API**, available immediately via the same `api.x.ai` endpoint as the Grok LLM API. No waitlist, no staged rollout — both live on launch day.

The move signals something beyond a product release. xAI has operated one of the largest voice inference deployments in the world without ever selling access to it: the Grok Voice system embedded in Tesla vehicles and handling Starlink customer support at scale. The STT and TTS APIs are that production stack, externalized. For developers who care about infrastructure provenance — who want to build on something that has already processed billions of audio tokens in adversarial, real-world conditions — this is a meaningful credential.

Whether the pricing and accuracy hold up against entrenched competitors is a different question. That's what this review examines.

---

## What Launched

xAI released two separate products on the same day:

1. **Grok STT** — Speech-to-Text transcription via REST (batch) and WebSocket (streaming)
2. **Grok TTS** — Text-to-Speech synthesis with five voices and speech-tag controls

Both are available through the standard xAI API (`api.x.ai/v1`) using the same API keys developers already use for Grok LLM access. If you're already in the xAI ecosystem, onboarding to the audio APIs requires no new credentials.

---

## Grok STT: Specifications

### Pricing

| Mode | Price |
|------|-------|
| Batch (REST) | **$0.10 / hour of audio** |
| Streaming (WebSocket) | **$0.20 / hour of audio** |

xAI positions this as "market-low." For comparison, OpenAI Whisper API runs $0.36/hour. Deepgram's Nova-3 starts around $0.14–0.24/hour depending on tier. AssemblyAI's standard tier is $0.37/hour. The batch price is genuinely competitive; the streaming price is tight with Deepgram's real-time tier.

### API Endpoints

- **REST:** `POST https://api.x.ai/v1/stt` — file upload or URL-based transcription
- **WebSocket:** `wss://api.x.ai/v1/stt` — real-time streaming

### Rate Limits

| Limit | Value |
|-------|-------|
| REST requests | 600 / minute |
| WebSocket connections | 10 / second |
| Max concurrent sessions | 100 / team |
| Max file size | 500 MB |
| Deployment region | us-east-1 |

### Key Features

**Speaker diarization** — Separates audio by individual speaker, answering "who said what" across multi-speaker recordings. Critical for meeting transcription, call centers, interview workflows, and legal documentation.

**Word-level timestamps** — Assigns precise start/end times to every word, enabling subtitle generation, searchable audio archives, audio-to-text alignment for video editors, and compliance-grade documentation.

**Inverse Text Normalization (ITN)** — Converts spoken idiom into structured output. "One hundred sixty-seven thousand nine hundred eighty-three dollars and fifteen cents" becomes "$167,983.15." This matters enormously in financial services, healthcare, and any domain where structured data must be extracted from voice.

**Multi-channel audio** — Supports simultaneous recording from multiple microphones. Relevant for conference room setups, call center infrastructure with separate agent/customer channels, and multi-speaker live events.

**25+ languages** with automatic language switching — The API handles mid-conversation language transitions without requiring explicit language specification upfront.

**Supported formats** — Common audio and video containers including MP3, WAV, MP4, and M4A. The 500 MB file limit accommodates up to several hours of compressed audio per request.

### Benchmarks: The Claim

xAI's benchmark claim is specific: on **phone call entity recognition** — extracting names, account numbers, and dates from call center audio — Grok STT achieves a **5.0% word error rate**, versus:

| Provider | Error Rate |
|----------|------------|
| **Grok STT** | **5.0%** |
| ElevenLabs | 12.0% |
| Deepgram | 13.5% |
| AssemblyAI | 21.3% |

**The important caveat**: this benchmark was published by xAI on a dataset and evaluation methodology they control. It has not been independently reproduced. Phone call entity recognition is a specific, cherry-pickable slice of speech recognition performance — it does not represent general-purpose transcription quality across accents, noise environments, or non-English audio.

That said, the gap is large enough to be interesting. A 5.0% vs. 13.5% spread on Deepgram — even with home-field advantage on the benchmark — suggests real architectural differentiation. The production provenance (Tesla, Starlink) is at least a plausible explanation for strong call-center performance: those systems have been optimized for exactly this kind of structured, high-accuracy audio extraction.

Independent third-party evaluation on standard benchmarks (CommonVoice, LibriSpeech, CORAAL for diverse English, MLS for multilingual) would tell a more complete story.

---

## Grok TTS: Specifications

### Pricing

**$4.20 per million characters** — flat rate, no tier differentiation at launch.

For comparison: OpenAI TTS at $15/M chars (HD) or $12/M (standard). ElevenLabs at $11/M chars on their Starter plan. Eleven's Flash v2.5 (fastest/cheapest) prices at $5.50/M. Grok TTS at $4.20/M undercuts the entire incumbent field.

### Voices

Five voices at launch:

| Voice | Default? |
|-------|----------|
| Ara | — |
| Eve | ✓ (default) |
| Leo | — |
| Rex | — |
| Sal | — |

xAI has not published demographic or stylistic descriptions of each voice in the launch materials. Developers will need to evaluate fit for their use case directly via API.

### Languages

20 languages supported. The specific language list is not enumerated in the launch announcement. Given the STT list includes 25+ with automatic switching, TTS coverage is somewhat narrower — a consideration for internationalized applications.

### Speech Tags

The API supports **speech tags** — control tokens embedded in input text that modify delivery: pacing, emphasis, prosody. This is the category where ElevenLabs has historically led the market (their SSML-like control has been a key differentiator). xAI's approach appears similar in concept, though the depth of control relative to ElevenLabs has not been independently documented.

---

## The Infrastructure Story

What separates Grok STT/TTS from a new entrant pitching equivalent specs is the deployment history. xAI's audio stack has been running in production at scale in two demanding environments:

**Tesla vehicles** — In-car voice interfaces operate under compounded noise: road noise, music, HVAC, wind, multi-passenger conversation. Inference must be fast enough to feel responsive, accurate enough for navigation commands, and robust enough across accents. Tesla's Grok integration has been active since 2025.

**Starlink customer support** — Call center voice AI at SpaceX scale means millions of support interactions with real users, not controlled test environments. The structured entity extraction case (account numbers, service addresses, ticket IDs) maps directly to the phone call entity recognition benchmark xAI published.

The argument is not that Tesla and Starlink deployments guarantee performance for your use case. It's that a voice API backed by this kind of production history has a different error surface than a model released from research into API access. Production APIs get optimized for failure modes that benchmarks don't surface.

---

## Competitive Positioning

### vs. OpenAI Whisper API

Whisper is the default choice for many developer stacks because of its open-source provenance (the weights are public) and OpenAI API familiarity. At $0.36/hr, it is 3.6× more expensive than Grok STT batch. Whisper has no native speaker diarization; developers combine it with pyannote or similar. Grok STT's diarization is built in.

For teams already using OpenAI's API, switching STT is a low-cost experiment — same API key structure, comparable feature set, lower price.

### vs. Deepgram

Deepgram's Nova-3 is the strongest incumbent on accuracy across diverse English. It has speaker diarization, filler word detection, sentiment analysis, and deeper customization options. Deepgram also has a significantly longer track record of independent benchmark results across accent diversity.

Grok STT matches Deepgram's real-time streaming price and undercuts their batch rate. Whether accuracy holds up across Deepgram's evaluation framework is the open question.

### vs. ElevenLabs

ElevenLabs' primary moat is TTS quality — particularly voice cloning, fine-grained prosody control via SSML, and a large voice library. At $11/M chars vs. Grok TTS at $4.20/M, ElevenLabs is 2.6× more expensive for comparable output volume.

If your application requires voice cloning or custom voice training, ElevenLabs still leads. If you need five solid voices at aggressive pricing, Grok TTS is worth benchmarking.

### vs. AssemblyAI

AssemblyAI at $0.37/hr and 21.3% phone call entity recognition error in xAI's benchmark is the weakest comparison point in this competitive set. AssemblyAI has strengths in its LeMUR transcript analysis layer (running LLM queries over transcripts natively). That additional layer is not something Grok STT offers at launch.

---

## What's Missing

**No voice cloning** — The five fixed voices cover broad use cases but rule out any application requiring brand-specific voice identity. ElevenLabs leads here by a wide margin.

**us-east-1 only** — Single deployment region introduces latency for users in Europe, Asia-Pacific, or South America. For real-time streaming applications, round-trip latency from Tokyo or São Paulo will be measurably worse than from a regional provider.

**No native LLM + audio pipeline** — Deepgram's Aura-2 and AssemblyAI's LeMUR allow you to run language model queries over transcripts within the same API call. Grok STT is transcription only; chaining to Grok LLM for analysis requires two separate calls.

**Self-reported benchmark** — The 5.0% entity recognition figure needs third-party reproduction before it should anchor a procurement decision.

---

## Who Should Evaluate Grok STT/TTS

**Strong fit:**
- Teams already using Grok API who want to add voice to their stack with zero new credential overhead
- Applications where structured entity extraction from audio is the primary accuracy requirement (finance, healthcare, call centers)
- High-volume transcription workflows where per-hour cost is the primary optimization target
- Multi-language applications requiring automatic language detection and switching

**Proceed with caution:**
- Applications requiring voice cloning or custom voice identity
- Teams with established Deepgram or AssemblyAI pipelines where switching cost needs clear justification
- Latency-sensitive streaming applications outside North America (us-east-1 only)
- Production use cases where the self-reported benchmark is the primary accuracy evidence and independent validation hasn't been done

---

## Rating

**3.5 / 5** — The pricing is genuinely aggressive and the production infrastructure story is credible. The benchmarks need independent verification, the TTS voice library is thin, and regional coverage is limited to us-east-1. For teams already in the xAI ecosystem or running high-volume transcription at a cost-constrained point in the stack, this is worth a structured evaluation against your own data. For teams making a primary voice infrastructure bet, wait for independent benchmark reproduction before committing.

---

*ChatForest researches and reviews AI tools based on published documentation, announcements, and third-party reporting. We do not have direct access to the Grok Speech APIs and have not conducted hands-on testing. Benchmark claims are sourced from xAI's launch materials unless otherwise noted. This review was written in May 2026 based on information available at that time.*
