---
title: "Gemini 3.1 Flash TTS Streaming: Audio Tags, Output Format, 30 Voices, and the Known 500 Error"
date: 2026-07-02
description: "Streaming support arrived for gemini-3.1-flash-tts-preview on June 17. PCM 24kHz output, 200+ inline audio tags, 30 voices, 70+ languages. One known bug to handle before shipping: occasional 500 errors require retry logic."
og_description: "Gemini 3.1 Flash TTS got streaming on June 17. Model: gemini-3.1-flash-tts-preview. 200+ audio tags inline in text. PCM 24kHz via streamGenerateContent. Retry for 500 errors. $20/1M output tokens."
content_type: "Builder's Log"
categories: ["Google", "Voice AI", "Developer Tools", "Audio Generation"]
tags: ["google", "gemini", "tts", "text-to-speech", "streaming", "audio-tags", "voice", "gemini-3-1", "builders-log"]
sources_audited: 2026-07-31
---

Streaming support for [`gemini-3.1-flash-tts-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview) arrived [June 17, 2026](https://ai.google.dev/gemini-api/docs/changelog). The model itself [launched in April](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-tts/) — this changelog entry is specifically about streaming, via `streamGenerateContent` and `stream: true` in the Interactions API, [becoming available](https://ai.google.dev/gemini-api/docs/changelog). Before June 17, TTS on this model required a non-streaming call that returned the full audio blob at completion. Now you can stream audio chunks and begin playback before the full generation is done.

This guide covers: how streaming works, the audio tag system, voice selection, output format, pricing, and the one known bug you need to handle before shipping.

---

## The Model

`gemini-3.1-flash-tts-preview` is Google's expressive TTS model with inline style control. It is a preview model — not yet GA, not in Flex inference, and not in Priority inference. Input is text only; output is audio only.

| Attribute | Value |
|---|---|
| Model ID | `gemini-3.1-flash-tts-preview` |
| Input | Text (max 8,192 tokens) |
| Output | Audio |
| Max output tokens | 16,384 |
| Audio format | PCM, 24 kHz, 16-bit, mono |
| Voices | 30 prebuilt |
| Languages | 70+ |
| Pricing | $20 / 1M output tokens |
| Batch API | Supported |
| Caching, function calling, structured outputs | Not supported |

Model ID, token limits, and unsupported features are from [Google's model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview). The PCM/24kHz/16-bit/mono output format is documented in the [TTS guide's](https://ai.google.dev/gemini-api/docs/speech-generation) code samples. Voice count and language coverage are from [Google's launch announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-tts/). Pricing is from [Google's Gemini API pricing page](https://ai.google.dev/gemini-api/docs/pricing).

Note the $20/1M output token rate — double the $10/1M output rate for [Gemini 2.5 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts), Google's prior-generation TTS model (same [pricing page](https://ai.google.dev/gemini-api/docs/pricing)). The premium buys the 200+ audio tag system described below.

---

## How Streaming Works

Use `streamGenerateContent` instead of `generateContent`. With the `google-genai` SDK this is `client.models.generate_content_stream()` — iterate over the returned chunks, and each chunk's audio lives at `chunk.candidates[0].content.parts[0].inline_data.data` as raw PCM bytes ([Google's TTS guide](https://ai.google.dev/gemini-api/docs/speech-generation) has the full code sample in Python, JavaScript, and REST):

```python
from google import genai
from google.genai import types
import wave

client = genai.Client()

response_stream = client.models.generate_content_stream(
    model="gemini-3.1-flash-tts-preview",
    contents="[excited] We just shipped streaming TTS support.",
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Puck")
            )
        ),
    ),
)

audio_chunks = []
for chunk in response_stream:
    try:
        audio_chunks.append(chunk.candidates[0].content.parts[0].inline_data.data)
    except (IndexError, AttributeError):
        pass

# Write PCM chunks to WAV
with wave.open("output.wav", "wb") as f:
    f.setnchannels(1)
    f.setsampwidth(2)   # 16-bit
    f.setframerate(24000)
    f.writeframes(b"".join(audio_chunks))
```

Google's newer [Interactions API](https://ai.google.dev/gemini-api/docs/speech-generation) offers the same capability via `client.interactions.create(..., stream=True)`, which emits `step.delta` events where `event.delta.type == "audio"` and `event.delta.data` is base64-encoded PCM you decode yourself. Both mechanisms shipped for this model on the same [June 17, 2026 release](https://ai.google.dev/gemini-api/docs/changelog).

The output is always 24000 Hz, 16-bit, mono PCM. You do not need to negotiate the format — it is fixed.

---

## Audio Tags

The audio tag system lets you embed delivery instructions directly in the input text. Google says the model supports [200+ audio tags](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-tts-on-google-cloud) for steering vocal style, tone, pacing, and accent. Tags are inline, surrounded by square brackets:

```
[whispers] This part is spoken softly.
[excited] And this part with energy!
```

Tags can combine:

```
[sarcastically, one painfully slow word at a time] Oh. What. A. Great. Idea.
```

Categories of control include:
- **Delivery style:** `[whispers]`, `[shouting]`, `[breathlessly]`, `[dramatically]`
- **Emotion:** `[excitedly]`, `[bored]`, `[laughing]`, `[sighs]`
- **Pacing:** `[one word at a time]`, `[quickly]`, `[pausing]`
- **Accent and register:** vary by tag — [Google's TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation) lists commonly used tags but is explicit that "there is no exhaustive list on what tags do and don't work," and recommends experimenting

Tags are processed inline — you can switch style mid-sentence or per paragraph.

---

## Voice Selection

30 prebuilt voices are available. A subset of named voices, per [Google's TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation):

- **Kore** — Firm
- **Puck** — Upbeat
- **Enceladus** — Breathy

Set voice in `speech_config.voice`. Voice selection affects the base character; audio tags control delivery on top of the voice. [Google's documentation](https://ai.google.dev/gemini-api/docs/speech-generation) describes multi-speaker configuration supporting up to two speakers in the same request, each with independent voice and style configuration.

---

## The Known 500 Error

[Google's own documentation warns](https://ai.google.dev/gemini-api/docs/speech-generation): the model occasionally returns text tokens instead of audio tokens, causing the server to fail with a 500 error.

This is a known issue in preview, not a transient infrastructure problem. Handle it with automated retry:

```python
import time

MAX_RETRIES = 3

for attempt in range(MAX_RETRIES):
    try:
        result = stream_tts(text, voice="Kore")
        break
    except Exception as e:
        if "500" in str(e) and attempt < MAX_RETRIES - 1:
            time.sleep(1)
            continue
        raise
```

Do not surface the retry to end users — one or two retries transparently handle the majority of these failures.

---

## Long Output Drift

For outputs longer than a few minutes, [the documentation notes](https://ai.google.dev/gemini-api/docs/speech-generation) that "speech quality and consistency may begin to drift." If you need long-form TTS (podcast narration, audiobook chapters), split your input at natural paragraph or section boundaries and stitch the output chunks rather than submitting the entire document in one call. This also reduces the impact of a mid-generation 500 error, since you only retry the failed chunk rather than the entire input.

---

## Streaming vs. Non-Streaming

Non-streaming (`generateContent`) is still available and remains the right choice when:
- You do not need real-time playback (batch processing, file generation)
- You want to avoid implementing chunk assembly
- Latency to first byte does not matter

Streaming (`streamGenerateContent`) is the right choice when:
- You are building a voice interface where response latency is user-visible
- You want to begin audio playback before generation completes
- You are integrating with a real-time audio output pipeline

The 500 error bug affects both streaming and non-streaming. Build retry logic regardless of which surface you use.
