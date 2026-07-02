# Gemini 3.1 Flash TTS Streaming: Audio Tags, Output Format, 30 Voices, and the Known 500 Error

> Streaming support arrived for gemini-3.1-flash-tts-preview on June 17. PCM 24kHz output, 200+ inline audio tags, 30 voices, 70+ languages. One known bug to handle before shipping: occasional 500 errors require retry logic.


Streaming support for `gemini-3.1-flash-tts-preview` arrived June 17, 2026. The model itself launched in April — this changelog entry is specifically about streaming via `streamGenerateContent` becoming available. Before June 17, TTS on this model required a non-streaming call that returned the full audio blob at completion. Now you can stream audio chunks and begin playback before the full generation is done.

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

Note the $20/1M output token rate. Compare to Gemini 3.5 Flash TTS at $6/1M — the 3.5 Flash model is newer and cheaper. The 3.1 Flash TTS is the model to use when you need the 200+ audio tag system for fine-grained delivery control; 3.5 Flash TTS is the cost-efficient option for straightforward narration.

---

## How Streaming Works

Use `streamGenerateContent` instead of `generateContent`. In the Interactions API, set `stream: true` in the request.

Audio arrives as `step.delta` events. When `event.delta.type == "audio"`, the data field contains base64-encoded PCM. Decode and pipe directly to your audio output:

```python
import base64
import wave

audio_chunks = []

for event in client.models.stream_generate_content(
    model="gemini-3.1-flash-tts-preview",
    contents="[excited] We just shipped streaming TTS support.",
    config={"speech_config": {"voice": "Puck"}}
):
    if event.delta and event.delta.type == "audio":
        audio_chunks.append(base64.b64decode(event.delta.data))

# Write PCM chunks to WAV
with wave.open("output.wav", "wb") as f:
    f.setnchannels(1)
    f.setsampwidth(2)   # 16-bit
    f.setframerate(24000)
    f.writeframes(b"".join(audio_chunks))
```

The output is always 24000 Hz, 16-bit, mono PCM. You do not need to negotiate the format — it is fixed.

---

## Audio Tags

The audio tag system lets you embed delivery instructions directly in the input text. Tags are inline, surrounded by square brackets:

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
- **Accent and register:** vary by tag — the full list is in Google's TTS documentation

Tags are processed inline — you can switch style mid-sentence or per paragraph. This is the primary differentiator from Gemini 3.5 Flash TTS, which handles narration but does not support the 200+ tag system.

---

## Voice Selection

30 prebuilt voices are available. A subset of named voices:

- **Kore** — Firm
- **Puck** — Upbeat
- **Enceladus** — Breathy

Set voice in `speech_config.voice`. Voice selection affects the base character; audio tags control delivery on top of the voice. You can run two independent speakers in the same request with separate voice and style configuration per speaker.

---

## The Known 500 Error

Google's own documentation warns: the model occasionally returns text tokens instead of audio tokens, causing the server to fail with a 500 error.

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

For outputs longer than a few minutes, the documentation notes that "speech quality and consistency may begin to drift." If you need long-form TTS (podcast narration, audiobook chapters), split your input at natural paragraph or section boundaries and stitch the output chunks rather than submitting the entire document in one call. This also reduces the impact of a mid-generation 500 error, since you only retry the failed chunk rather than the entire input.

---

## vs. Gemini 3.5 Flash TTS

| | 3.1 Flash TTS Preview | 3.5 Flash TTS |
|---|---|---|
| Audio tags | 200+ inline tags | Not supported |
| Pricing | $20/1M output tokens | $6/1M output tokens |
| Status | Preview | GA |
| Multi-speaker | Yes, 2 speakers | Check docs |
| Use case | Expressive, steerable narration | Cost-efficient narration |

Use 3.1 Flash TTS when fine delivery control matters (character voices, expressive training data, styled narration). Use 3.5 Flash TTS when you need reliable, cheap, scalable narration without style complexity.

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

