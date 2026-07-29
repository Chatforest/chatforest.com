---
title: "Gemini 3.5 Live Translate Is a Speech-to-Speech API That Skips the Transcript"
date: 2026-06-10
description: "Google released Gemini 3.5 Live Translate on June 9, 2026 — a streaming audio-to-audio translation model covering 70+ languages, accessible via the Gemini Live API today. No text intermediate. No separate STT+TTS pipeline. Here is the full builder breakdown."
og_description: "Gemini 3.5 Live Translate (June 9, 2026): model ID gemini-3.5-live-translate-preview, WebSocket Live API, 70+ languages, SynthID-watermarked output, preserves intonation/pitch/pacing. Dedicated preview pricing: ~$0.0368/min. Agora/LiveKit/Pipecat partners ready. No function calling, no batch, no caching. Builder guide."
content_type: "Builder's Log"
categories: ["AI Models", "Voice AI", "Google"]
tags: ["gemini", "live-api", "voice", "translation", "speech-to-speech", "google", "builders-log", "multilingual", "real-time-ai", "syntHId", "livekit", "pipecat", "agora"]
sources_audited: 2026-07-30
---

Google [released Gemini 3.5 Live Translate on June 9, 2026](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/). It is a streaming speech-to-speech translation model — audio in, translated audio out — available in [public preview via the Gemini Live API and Google AI Studio](https://ai.google.dev/gemini-api/docs/live-api/live-translate).

Google's own [model card](https://deepmind.google/models/model-cards/gemini-3-5-audio/) describes it as a "low-latency, audio-to-audio model optimized for real-time translation of spoken conversations" — distinct from a pipeline that transcribes to text, translates the text, and then synthesizes speech. That audio-native design is why it can preserve intonation, pacing, and pitch rather than delivering robot-flat translated output.

The [consumer rollout is happening simultaneously](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/) — Google Translate (Android/iOS) and Google Meet (enterprise private preview, broader rollout later this year). But the builder story is the Live API, which is publicly accessible now.

---

## What It Does

Gemini 3.5 Live Translate handles [low-latency, real-time speech-to-speech translation](https://ai.google.dev/gemini-api/docs/live-api/live-translate). You stream audio in over a WebSocket; the model auto-detects the source language and continuously translates into one configured target language, returning translated audio and optional text transcripts.

Key capabilities:
- **[70+ languages](https://ai.google.dev/gemini-api/docs/live-api/live-translate)**, auto-detected on input — you set the target language (`targetLanguageCode`), not the source
- **[Voice-quality preservation](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/)** — pitch, intonation, and pacing from the source speaker carry through to the translated output
- **[SynthID watermarking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/)** — all generated audio is watermarked with Google's imperceptible audio watermark, which is relevant for compliance and provenance tracking
- **Continuous streaming, not turn-based** — the [docs are explicit](https://ai.google.dev/gemini-api/docs/live-api/live-translate) that the model "translates as the speaker talks without waiting for turns." Each session translates one direction (source → the configured target language); a true two-way conversation between two speakers requires running a session per direction, not a single session that "tracks speaker turns."

Consumer product integrations as of June 9:
- **Google Translate app** — [global rollout on Android and iOS](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/); Android adds a "listening mode" (phone-to-ear, earpiece audio)
- **Google Meet** — private preview for select Workspace Enterprise customers; [expanding from the previous limit of five languages (English-only) to 70+ languages and 2,000+ language combinations per meeting](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/); general Workspace rollout later in 2026

---

## API Access

The model is in **[public preview](https://ai.google.dev/gemini-api/docs/live-api/live-translate)** via the Gemini Live API.

| Field | Value |
|---|---|
| Model ID | [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/live-api/live-translate) |
| Access | Gemini Live API (WebSocket), Google AI Studio |
| Status | Public preview |
| AI Studio direct link | `aistudio.google.com/live?model=gemini-3.5-live-translate-preview` |

The Live API is WebSocket-based. Per [Google's own docs](https://ai.google.dev/gemini-api/docs/live-api/live-translate), audio in is raw 16-bit PCM at 16kHz and translated audio out is raw 16-bit PCM at 24kHz, sent in ~100ms chunks. The model handles language detection, translation, and voice synthesis in one pass.

**Context window** (per [Google's model card](https://deepmind.google/models/model-cards/gemini-3-5-audio/), which lists ~128K input / ~64K output):

| Capacity | Tokens |
|---|---|
| Input | 131,072 |
| Output | 65,536 |

At the [general Live API audio-token rate](https://ai.google.dev/gemini-api/docs/pricing) of 32 tokens per second of input audio and 25 tokens per second of output audio, the 131K input limit represents roughly 68 minutes of continuous input before the context fills. In practice, translation sessions reset or roll over before that point — and separately, [Live API sessions default to a 15-minute cap for audio-only use](https://ai.google.dev/gemini-api/docs/live-api/capabilities) unless configured for extension.

---

## What Is Not Supported

This is a specialized model, not a general-purpose one. [Features absent](https://ai.google.dev/gemini-api/docs/live-api/live-translate) from `gemini-3.5-live-translate-preview`:

| Feature | Supported |
|---|---|
| Batch API | No |
| Caching | No |
| Function calling | No |
| Code execution | No |
| Search grounding | No |
| Structured outputs | No |
| Thinking mode | No |
| Image generation | No |
| URL context | No |
| File search | No |

The model does one thing: translate spoken audio in real time. If you need a voice agent that also calls tools, queries your database, or does anything beyond translation, you need a different Live API model alongside this one.

---

## Pricing

Contrary to earlier assumptions that this model would ride generic Live API rates, [Google's pricing page](https://ai.google.dev/gemini-api/docs/pricing) lists dedicated preview pricing for `gemini-3.5-live-translate-preview`:

- **Input audio**: $3.50 per million tokens (32 tokens/sec), ≈ $0.0053/minute
- **Output audio**: $21.00 per million tokens (25 tokens/sec), ≈ $0.0315/minute
- **Combined effective rate**: ≈ **$0.0368 per minute** of translated conversation

For context: a 10-minute live translation session costs roughly $0.37. A 60-minute session costs about $2.21. This is preview pricing per Google's published rate card — it may change when the model exits preview, but it is not an estimate; it is the current published rate.

Google Workspace Meet integration pricing and tier requirements for enterprise have not been announced. Expect those details when Meet moves to general availability, currently targeted for later in 2026.

---

## Partner Ecosystem

Google [called out five platforms](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/) as Live API partners for building voice translation apps with this model:

- **[Agora](https://www.agora.io/)** — real-time voice/video SDK, widely used in consumer and enterprise apps
- **[Fishjam](https://fishjam.io/)** — media server platform
- **[LiveKit](https://livekit.io/)** — open-source WebRTC infrastructure, popular with voice AI builders
- **[Pipecat](https://www.pipecat.ai/)** — open-source framework for building real-time voice AI pipelines (Python)
- **[Vision Agents](https://getstream.io/blog/vision-agents-by-stream/)** — open-source voice/vision agent framework from Stream, with day-one Gemini Live support

If you are already using LiveKit or Pipecat for voice agents, the integration path to Live Translate is short: swap in the model ID, connect the audio stream, and you have translation instead of (or in addition to) voice interaction.

---

## The Architecture Difference

Every mainstream translation pipeline before this followed the same three-step path:

1. Speech-to-Text (transcribe the speaker)
2. Text-to-Text (translate the transcript)
3. Text-to-Speech (synthesize the translated text)

Each step introduces latency and throws away information. The transcription step loses prosody — tone, emphasis, hesitation. The translation step operates on flattened text. The synthesis step invents a new voice that sounds nothing like the speaker.

Gemini 3.5 Live Translate replaces all three steps with a single [audio-to-audio pass](https://deepmind.google/models/model-cards/gemini-3-5-audio/), preserving the features that make voice communication feel human. (Google has not published architecture or training-methodology details beyond describing it as audio-to-audio, so specifics of how that translation is learned internally aren't public.)

The practical result: translated output that carries emotional tone and sounds like a reasonable representation of the speaker rather than a neutral TTS voice narrating a transcript. This matters most in high-stakes use cases — customer service, medical interpretation, live events — where flat robotic output damages trust.

---

## Builder Use Cases

**Voice agents in multilingual markets.** If you have a voice assistant deployed in one language and want to expand to others without rebuilding the STT/TTS stack, Live Translate can sit in front of or behind your agent. Audio enters, gets translated, the agent responds in the translation language, gets translated back.

**Live customer support interpretation.** A support agent who speaks English can handle a Spanish-speaking customer in real time. Since [each session translates one direction into a single configured target language](https://ai.google.dev/gemini-api/docs/live-api/live-translate), a genuine two-way conversation needs a session per direction (agent→customer and customer→agent) rather than one session doing both.

**Conference and event interpretation.** The 2,000+ language combination support in Google Meet is the clearest signal of the target: large organizations running multilingual meetings where real-time interpretation infrastructure is expensive and hard to staff.

**Content localization pipelines.** Where you have pre-recorded audio in one language and want natural-sounding output in another, the audio-to-audio approach produces more natural results than traditional pipelines. The model ID ending in `-preview` means this is not yet the right choice for high-volume production batch work (batch API is unsupported), but for interactive or streaming content this applies.

**Accessibility tools.** For users who are hard of hearing, or for cross-language accessibility in live settings, streaming translation without transcript latency opens use cases that transcript-based pipelines made impractical.

---

## What to Watch

**Preview exit timeline.** The `-preview` suffix signals this model is not yet at production stability or pricing. Google has not given a specific GA date. Watch the Gemini API changelog (`ai.google.dev/gemini-api/docs/changelog`) for the `gemini-3.5-live-translate` (dateless) model ID that will mark stable release.

**Pricing changes at GA.** Google has already [published preview pricing](https://ai.google.dev/gemini-api/docs/pricing) ($3.50/M input audio tokens, $21/M output audio tokens), but preview rates on Google APIs commonly change at general availability, especially as the model goes enterprise-grade for Meet.

**Google Meet GA.** The enterprise Workspace integration is in private preview now. Google's own announcement says only that [broader rollout follows "later this year"](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/) — no specific quarter has been given, so treat any more precise date as speculation.

**SynthID implications.** The mandatory audio watermarking on all Live Translate output is novel territory for translation products. If you are building with this API, your [translated audio will carry a Google-generated SynthID mark](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/). That is relevant for broadcast use, legal proceedings, and any context where provenance of the audio matters.

---

## Bottom Line

Gemini 3.5 Live Translate is a generally accessible speech-to-speech translation API that takes voice quality seriously. The public preview is open today. Published preview pricing (≈$0.037/minute) is low enough that it is viable for most production voice use cases at current rates.

The absence of function calling, batch, and caching means it is purpose-built for interactive streaming translation — not a general-purpose voice model you can extend. If that is your use case, the model ID is `gemini-3.5-live-translate-preview` and the Live API WebSocket is the entry point.

For everything else — tools, agents, grounding — use the standard `gemini-3.5-flash` or `gemini-3.5-pro` Live API variants.
