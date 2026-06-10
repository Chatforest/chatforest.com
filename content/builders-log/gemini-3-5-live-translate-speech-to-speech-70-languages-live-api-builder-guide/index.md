---
title: "Gemini 3.5 Live Translate Is a Speech-to-Speech API That Skips the Transcript"
date: 2026-06-10
description: "Google released Gemini 3.5 Live Translate on June 9, 2026 — a streaming audio-to-audio translation model covering 70+ languages, accessible via the Gemini Live API today. No text intermediate. No separate STT+TTS pipeline. Here is the full builder breakdown."
og_description: "Gemini 3.5 Live Translate (June 9, 2026): model ID gemini-3.5-live-translate-preview, WebSocket Live API, 70+ languages, SynthID-watermarked output, preserves intonation/pitch/pacing. Pricing: same Live API audio billing (~$0.0368/min). Agora/LiveKit/Pipecat partners ready. No function calling, no batch, no caching. Builder guide."
content_type: "Builder's Log"
categories: ["AI Models", "Voice AI", "Google"]
tags: ["gemini", "live-api", "voice", "translation", "speech-to-speech", "google", "builders-log", "multilingual", "real-time-ai", "syntHId", "livekit", "pipecat", "agora"]
---

Google released Gemini 3.5 Live Translate on June 9, 2026. It is a streaming speech-to-speech translation model — audio in, translated audio out — available today in public preview via the Gemini Live API and Google AI Studio.

The architectural difference from every prior translation pipeline matters: there is no text intermediate. The model does not transcribe to text, translate the text, and then synthesize speech. It operates directly on the audio signal, which is why it can preserve intonation, pacing, and pitch rather than delivering robot-flat translated output.

The consumer rollout is happening simultaneously — Google Translate (Android/iOS) and Google Meet (enterprise private preview, broader rollout later this year). But the builder story is the Live API, which is publicly accessible now.

---

## What It Does

Gemini 3.5 Live Translate handles bidirectional real-time spoken conversation translation. You stream audio in over a WebSocket; the model returns translated audio and optional text transcripts.

Key capabilities:
- **70+ languages**, auto-detected on input — you do not pre-declare the language pair
- **Voice-quality preservation** — pitch, intonation, and pacing from the source speaker carry through to the translated output
- **SynthID watermarking** — all generated audio is watermarked with Google's imperceptible audio watermark, which is relevant for compliance and provenance tracking
- **Bidirectional** — a single session handles back-and-forth conversation; the model tracks speaker turns

Consumer product integrations as of June 9:
- **Google Translate app** — global rollout on Android and iOS; Android adds a "listening mode" (phone-to-ear, earpiece audio)
- **Google Meet** — private preview for select Workspace Enterprise customers; expanding from 5 supported languages to 2,000+ language combinations per meeting; general Workspace rollout later in 2026

---

## API Access

The model is in **public preview** via the Gemini Live API.

| Field | Value |
|---|---|
| Model ID | `gemini-3.5-live-translate-preview` |
| Access | Gemini Live API (WebSocket), Google AI Studio |
| Status | Public preview |
| AI Studio direct link | `aistudio.google.com/live?model=gemini-3.5-live-translate-preview` |

The Live API is WebSocket-based. You open a connection, stream PCM audio frames, and receive translated audio frames back in near real time. The model handles the rest: language detection, translation, voice synthesis.

**Context window:**

| Capacity | Tokens |
|---|---|
| Input | 131,072 |
| Output | 65,536 |

These match the standard Live API context limits. At 32 tokens per second of input audio and 25 tokens per second of output audio, the 131K input limit represents roughly 68 minutes of continuous input before the context fills. In practice, translation sessions reset or roll over before that point.

---

## What Is Not Supported

This is a specialized model, not a general-purpose one. Features absent from `gemini-3.5-live-translate-preview`:

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

Gemini 3.5 Live Translate uses the same audio-token billing as other Live API models. No separate pricing has been announced for the preview period.

Audio billing rates:
- **Input audio**: 32 tokens per second of audio
- **Output audio**: 25 tokens per second of audio
- **Effective cost at standard Live API rates (~$1/M input tokens)**: approximately **$0.0368 per minute** of bidirectional conversation

For context: a 10-minute live translation session costs roughly $0.37. A 60-minute session costs about $2.20. These are estimates based on current Live API token pricing — actual Live Translate pricing may be published separately when the model exits preview.

Google Workspace Meet integration pricing and tier requirements for enterprise have not been announced. Expect those details when Meet moves to general availability, currently targeted for later in 2026.

---

## Partner Ecosystem

Google called out five platforms as Live API partners for building voice translation apps with this model:

- **[Agora](https://www.agora.io/)** — real-time voice/video SDK, widely used in consumer and enterprise apps
- **[Fishjam](https://fishjam.io/)** — media server platform
- **[LiveKit](https://livekit.io/)** — open-source WebRTC infrastructure, popular with voice AI builders
- **[Pipecat](https://www.pipecat.ai/)** — open-source framework for building real-time voice AI pipelines (Python)
- **Vision Agents** — video understanding / agentic platform

If you are already using LiveKit or Pipecat for voice agents, the integration path to Live Translate is short: swap in the model ID, connect the audio stream, and you have translation instead of (or in addition to) voice interaction.

---

## The Architecture Difference

Every mainstream translation pipeline before this followed the same three-step path:

1. Speech-to-Text (transcribe the speaker)
2. Text-to-Text (translate the transcript)
3. Text-to-Speech (synthesize the translated text)

Each step introduces latency and throws away information. The transcription step loses prosody — tone, emphasis, hesitation. The translation step operates on flattened text. The synthesis step invents a new voice that sounds nothing like the speaker.

Gemini 3.5 Live Translate replaces all three steps with a single audio-to-audio pass. The model was trained to learn translation as an audio transformation, preserving the features that make voice communication feel human.

The practical result: translated output that carries emotional tone and sounds like a reasonable representation of the speaker rather than a neutral TTS voice narrating a transcript. This matters most in high-stakes use cases — customer service, medical interpretation, live events — where flat robotic output damages trust.

---

## Builder Use Cases

**Voice agents in multilingual markets.** If you have a voice assistant deployed in one language and want to expand to others without rebuilding the STT/TTS stack, Live Translate can sit in front of or behind your agent. Audio enters, gets translated, the agent responds in the translation language, gets translated back.

**Live customer support interpretation.** A support agent who speaks English can handle a Spanish-speaking customer in real time. Neither party changes anything — the translation is in the audio stream itself.

**Conference and event interpretation.** The 2,000+ language combination support in Google Meet is the clearest signal of the target: large organizations running multilingual meetings where real-time interpretation infrastructure is expensive and hard to staff.

**Content localization pipelines.** Where you have pre-recorded audio in one language and want natural-sounding output in another, the audio-to-audio approach produces more natural results than traditional pipelines. The model ID ending in `-preview` means this is not yet the right choice for high-volume production batch work (batch API is unsupported), but for interactive or streaming content this applies.

**Accessibility tools.** For users who are hard of hearing, or for cross-language accessibility in live settings, streaming translation without transcript latency opens use cases that transcript-based pipelines made impractical.

---

## What to Watch

**Preview exit timeline.** The `-preview` suffix signals this model is not yet at production stability or pricing. Google has not given a specific GA date. Watch the Gemini API changelog (`ai.google.dev/gemini-api/docs/changelog`) for the `gemini-3.5-live-translate` (dateless) model ID that will mark stable release.

**Dedicated pricing.** The current estimate uses standard Live API audio token rates, but Google may introduce separate pricing for the translation model, especially as it goes enterprise-grade for Meet.

**Google Meet GA.** The enterprise Workspace integration is in private preview now. Watch for the broader rollout announcement in Q3 2026.

**Open weights counterpart.** MiniMax M3's technical report showed that open-weight speech-to-speech translation is feasible at frontier quality. A competitive open alternative (possibly from Meta, Alibaba, or a derivative of Whisper/SeamlessM4T architecture) would change the build-vs-buy math, especially for on-device or sovereign deployment.

**SynthID implications.** The mandatory audio watermarking on all Live Translate output is novel territory for translation products. If you are building with this API, your translated audio will carry a Google-generated SynthID mark. That is relevant for broadcast use, legal proceedings, and any context where provenance of the audio matters.

---

## Bottom Line

Gemini 3.5 Live Translate is the first generally accessible speech-to-speech translation API that takes voice quality seriously. The public preview is open today. The pricing estimate is low enough that it is viable for most production voice use cases at current rates.

The absence of function calling, batch, and caching means it is purpose-built for interactive streaming translation — not a general-purpose voice model you can extend. If that is your use case, the model ID is `gemini-3.5-live-translate-preview` and the Live API WebSocket is the entry point.

For everything else — tools, agents, grounding — use the standard `gemini-3.5-flash` or `gemini-3.5-pro` Live API variants.
