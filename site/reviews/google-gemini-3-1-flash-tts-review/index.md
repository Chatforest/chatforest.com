# Google Gemini 3.1 Flash TTS Review — Prompt-Steerable Speech with 30 Voices and 100+ Languages

> Gemini 3.1 Flash TTS launched April 15, 2026 as a Preview model offering prompt-steerable text-to-speech, inline audio tags for expressive control, 30 prebuilt voices, 100+ auto-detected languages, and $1.00/$20.00 per million token pricing — with no native streaming and PCM-only output.


**At a glance:** Preview since April 15, 2026. Model ID: `gemini-3.1-flash-tts-preview`. 30 voices (astronomically named), 100+ languages auto-detected from input text, $1.00/1M input tokens / $20.00/1M output tokens ($0.03 per minute of audio output). PCM-only output (24kHz mono). No streaming — use Live API for real-time. Max 2 speakers per session. Part of our **[AI Models & LLM Reviews](/categories/llm-reviews/)** section.

Gemini 3.1 Flash TTS, launched April 15, 2026, is Google's third-generation API-native text-to-speech model. It follows `gemini-2.5-flash-preview-tts` and `gemini-2.5-pro-preview-tts` (both launched May 2025) with a stated focus on improved naturalness, multilingual coverage, and a novel inline control mechanism called audio tags. The fundamental design philosophy separates it from every major TTS competitor: instead of SSML parameters or numeric pitch/rate controls, you steer performance using natural language instructions and bracket-style tags embedded directly in your transcript.

This approach has real advantages for LLM-native workflows and significant tradeoffs for production applications that need streaming, format flexibility, or deterministic voice consistency. This review covers both.

This is a research-based review. We have not tested Gemini 3.1 Flash TTS hands-on.

---

## Launch Context

Google has operated two parallel text-to-speech product lines for years:

- **Google Cloud TTS** (legacy) — WaveNet, Neural2, Studio, and Chirp 3 HD voice families. SSML-based, per-character pricing, production-stable with SLA backing, 30+ languages.
- **Gemini TTS** (new) — LLM-native, prompt-steerable, per-token pricing, Preview status, 100+ languages.

These lines are not converging on the same architecture. Cloud TTS remains the enterprise choice for applications that need streaming, format control, and contractual uptime guarantees. Gemini TTS is the experimentation-forward choice for developers who want to express voice performance in plain language rather than XML.

`gemini-3.1-flash-tts-preview` is positioned as the cost-efficient tier of the new line, analogous to `gemini-3.1-flash` in the text model family. Google's announcement described it as "cost-efficient, expressive, and steerable" — the same adjectives used to position Flash models relative to Pro across the Gemini lineup.

---

## The Audio Tag System

The headline differentiator is audio tags — a mechanism with no direct equivalent in other major TTS APIs.

**How they work:** You embed bracketed keywords inline in the text you want synthesized. The model interprets each tag as a local performance instruction for the words that follow.

```
Say: "I've been thinking about what you said. [sighs] 
You're right, actually. [pauses] And I hate that you're right. [laughs softly]"
```

Google documents a set of commonly effective tags:

`[amazed]`, `[crying]`, `[curious]`, `[excited]`, `[sighs]`, `[gasp]`, `[giggles]`, `[laughs]`, `[mischievously]`, `[panicked]`, `[sarcastic]`, `[serious]`, `[shouting]`, `[tired]`, `[trembling]`, `[whispers]`

But the list is explicitly not exhaustive. Google's documentation states: "There is no exhaustive list on what tags do and don't work — we recommend experimenting with different emotions and expressions." The API accepts open-ended tag strings, including creative instructions like `[like a cartoon dog]`, `[like dracula]`, `[sarcastically, one painfully slow word at a time]`, and `[very fast]`.

This is intentional design. Rather than maintaining a finite tag vocabulary, Google exposes the model's underlying instruction-following capability through the bracket syntax. Whether a given tag works is a function of what the model learned to respond to — not a hard-coded list.

**Two-level control architecture:**

Gemini TTS uses a layered system for performance direction:

1. **Director's Notes (system instruction)** — global style, tone, accent, pacing, character identity for the entire output. Set once and applied throughout.
2. **Audio Tags** — inline, granular control per sentence or phrase.

Google recommends a five-component structure for the system instruction:
- Audio Profile (character name and role)
- Scene (environmental context and mood)
- Director's Notes (style, pacing, accent)
- Sample Context (relational framing)
- Transcript (the actual text, with embedded audio tags)

This prompt engineering overhead is worth noting. Getting consistent, expressive output from Gemini TTS requires intentional prompt construction — more so than competitors that control performance via a numeric API parameter.

---

## Voices

Gemini 3.1 Flash TTS ships with 30 prebuilt voices, all named after astronomical objects (stars and moons). The full roster:

| Voice | Character | Voice | Character |
|---|---|---|---|
| Zephyr | Bright | Algieba | Smooth |
| Puck | Upbeat | Despina | Smooth |
| Charon | Informative | Erinome | Clear |
| Kore | Firm | Algenib | Gravelly |
| Fenrir | Excitable | Rasalgethi | Informative |
| Leda | Youthful | Laomedeia | Upbeat |
| Orus | Firm | Achernar | Soft |
| Aoede | Breezy | Alnilam | Firm |
| Callirrhoe | Easy-going | Schedar | Even |
| Autonoe | Bright | Gacrux | Mature |
| Enceladus | Breathy | Pulcherrima | Forward |
| Iapetus | Clear | Achird | Friendly |
| Umbriel | Easy-going | Zubenelgenubi | Casual |
| — | — | Vindemiatrix | Gentle |
| — | — | Sadachbia | Lively |
| — | — | Sadaltager | Knowledgeable |
| — | — | Sulafat | Warm |

All 30 voices are previewable interactively in **Google AI Studio's Voice Library** before writing a line of code — a practical workflow feature that saves trial-and-error API calls during voice selection.

Voice is specified in the API via `PrebuiltVoiceConfig(voice_name="Kore")` — a named constant, not a numeric ID. The character descriptions (Bright, Firm, Gravelly, etc.) are Google's characterizations; individual voices respond differently to audio tags and director's note prompts.

**Multi-speaker:** Two simultaneous speakers are supported via `MultiSpeakerVoiceConfig`. Each speaker is assigned a voice and identified by name in the transcript. The two-speaker cap is a hard limit.

---

## Language Coverage

Gemini 3.1 Flash TTS supports 80–100+ languages, depending on which documentation page you consult (Google's own pages list varying counts). Language detection is **automatic** — the model infers the language from input text with no language parameter required.

The documented range includes:

Afrikaans, Albanian, Amharic, Arabic, Armenian, Azerbaijani, Basque, Bengali, Bulgarian, Catalan, Chinese (Mandarin), Croatian, Czech, Danish, Dutch, English, Estonian, Filipino, Finnish, French, Georgian, German, Greek, Gujarati, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Javanese, Kannada, Korean, Lao, Latvian, Lithuanian, Malay, Malayalam, Marathi, Mongolian, Nepali, Norwegian, Odia, Persian, Polish, Portuguese, Punjabi, Romanian, Russian, Serbian, Sinhala, Slovak, Slovenian, Spanish, Swahili, Swedish, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu, Vietnamese — and more.

This breadth is one of the strongest differentiators against ElevenLabs (28 languages), OpenAI TTS (approximately 50+), and Google's own Cloud TTS legacy system (30+ with WaveNet coverage varying significantly by language).

**Audio tag language note:** For non-English input, Google recommends writing audio tags in English for best results. The expressive control system appears trained primarily on English-language performance data.

---

## Pricing

| Mode | Input (per 1M tokens) | Output (per 1M tokens) |
|---|---|---|
| Paid (standard) | $1.00 | $20.00 |
| Batch API | $0.50 | $10.00 |
| Free tier | Available | Available |

**Audio token conversion:** 25 tokens = 1 second of audio output.

Practical benchmarks at paid rates:
- 1 minute of audio output = 1,500 tokens = **$0.03**
- 1 hour of audio output = 90,000 tokens = **$1.80**
- Input text for 1 hour of narration is typically 45,000–60,000 words ≈ 60,000–80,000 tokens ≈ **$0.06–$0.08**

At Batch API rates, hour-long audio generation costs approximately **$0.90 in output** plus input — under $1 per hour of narration. For high-volume audiobook or podcast production pipelines, this is significantly more cost-effective than ElevenLabs (where 1 hour of audio at 24kHz quality would consume 150,000–200,000 characters at $0.016/1k chars = $2.40–$3.20).

**Context caching:** Not available for any Gemini TTS model. This means repeated system instructions are billed on every request.

Free-tier quotas are not publicly published. They appear in AI Studio's rate limits panel and vary by account tier.

---

## API Access

Three methods are confirmed:

**Python SDK (`google-genai`):**

```python
from google import genai
from google.genai import types

client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

response = client.models.generate_content(
    model="gemini-3.1-flash-tts-preview",
    contents="Say warmly: Thanks for joining us today.",
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name="Aoede"
                )
            )
        )
    )
)

# Extract base64-encoded PCM audio from response
audio_data = response.candidates[0].content.parts[0].inline_data.data
```

**JavaScript SDK (`@google/genai`):** Supported with equivalent structure.

**REST API:**

```
POST https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent
Headers: x-goog-api-key: YOUR_KEY, Content-Type: application/json
```

The response body contains **base64-encoded PCM audio data** — not a binary stream. You decode the base64, then convert from raw PCM to a playable format using FFmpeg:

```bash
# Decode base64, then convert PCM to WAV
ffmpeg -f s16le -ar 24000 -ac 1 -i output.pcm output.wav
```

The PCM spec: signed 16-bit little-endian, 24,000 Hz sample rate, mono. No native WAV, MP3, OGG, FLAC, or AAC output. Post-processing is a required step for any production pipeline that serves audio to end users.

---

## Technical Specifications

| Spec | Value |
|---|---|
| Model ID | `gemini-3.1-flash-tts-preview` |
| Status | Preview (as of May 2026) |
| Input | Text only |
| Output | Audio only (PCM) |
| Sample rate | 24,000 Hz |
| Bit depth | 16-bit signed, little-endian |
| Channels | Mono |
| Context window | 32,768 tokens |
| Max input | 8,192 tokens |
| Max output | 16,384 tokens |
| Max speakers | 2 |
| Streaming | Not supported |
| Thinking | Not supported |
| Caching | Not supported |
| Function calling | Not supported |

---

## Limitations and Known Issues

Google's own documentation lists several limitations for Gemini TTS models. These are honest acknowledgments worth reviewing before committing to a production integration:

**1. No streaming.** The standard TTS API generates a complete audio clip and returns it as a single response. For real-time applications — voice assistants, live narration, interactive fiction — Google's **Live API** is the alternative (also outputs 24kHz PCM, supports bidirectional streaming).

**2. Quality drift in long outputs.** "Speech quality and consistency may begin to drift with generated outputs that are longer than a few minutes." The documented workaround is to split content into chunks rather than submitting very long transcripts as a single request.

**3. Voice inconsistency.** "The model's output may not always strictly match the selected speaker, causing the audio to sound different than expected." This is a probabilistic limitation — the model can occasionally diverge from a voice's expected character profile.

**4. Rare 500 errors from text token returns.** "The model occasionally returns text tokens instead of audio tokens, causing the server to fail the request." This requires retry logic in production.

**5. Prompt classifier failures.** Vague system instructions can cause the model to "read your style instructions aloud" instead of synthesizing speech in that style. The fix is an explicit preamble instructing the model to synthesize audio.

**6. Two-speaker ceiling.** Multi-speaker support is capped at two simultaneous voices. Ensemble narration with three or more characters requires session splitting.

**7. PCM-only output.** Every production use case needs a format conversion step. This adds operational complexity compared to ElevenLabs or OpenAI TTS, which return MP3 natively.

**8. Rate limits unpublished.** Quota limits vary by usage tier and are only visible in AI Studio — not in public documentation.

**9. Preview status.** No GA date is announced. Breaking API changes are possible before the model reaches general availability.

---

## SynthID: What's Confirmed

Google's [SynthID](https://deepmind.google/technologies/synthid/) technology embeds inaudible watermarks in AI-generated content. It has documented support for:
- AI-generated **images** (Imagen)
- AI-generated **video**
- AI-generated **text** (Gemini app)
- AI-generated **music** (Lyria)
- **NotebookLM podcast audio**

SynthID audio watermarks survive MP3 compression, added noise, and playback speed changes — detectable via the SynthID Detector portal.

**Important:** As of this review, Google's TTS API documentation makes **no mention of SynthID** for `gemini-3.1-flash-tts-preview`. The SynthID technology page does not list the TTS API as a covered product. We cannot confirm that audio generated via the Gemini TTS API carries SynthID watermarking. Organizations with AI disclosure requirements should not rely on SynthID detection as their compliance mechanism for Gemini TTS output.

---

## Comparison: Gemini TTS vs. the Field

### vs. Google Cloud TTS (Legacy)

| Dimension | Gemini 3.1 Flash TTS | Google Cloud TTS (Chirp 3 HD) |
|---|---|---|
| Control method | Natural language + audio tags | SSML + numeric parameters |
| Languages | 100+ (auto-detected) | 30+ (varies by voice tier) |
| Streaming | No | Yes (Chirp 3 HD) |
| Voice count | 30 (single product) | 300+ across all tiers |
| Output formats | PCM only | MP3, WAV, OGG, mulaw, alaw |
| Pricing model | Per token (input + output) | Per character |
| Production status | Preview | GA / SLA-backed |

The two systems are architecturally distinct and optimized for different users. Cloud TTS is the right choice for applications that need streaming, format flexibility, and enterprise SLAs. Gemini TTS is the right choice for developers who want to express creative performance direction in natural language and can tolerate Preview status.

### vs. ElevenLabs

ElevenLabs offers voice cloning from 3-second reference clips, 28 languages, native MP3/WAV/PCM output, streaming via WebSockets, and fine-grained latency settings. The Creator plan ($11/mo for 121,000 credits) is competitive for moderate-volume use cases. At high volume, Gemini TTS's Batch API pricing ($0.90/hour of audio output) undercuts ElevenLabs significantly.

ElevenLabs wins on: voice cloning, format support, streaming, production stability.  
Gemini TTS wins on: language range, audio tag expressiveness, cost at scale.

### vs. OpenAI TTS

OpenAI TTS (`gpt-4o-mini-tts`) supports streaming, multiple native output formats, and approximately 50+ languages. It uses a similar natural-language prompting model for voice performance. OpenAI has 6 built-in voices versus Gemini's 30.

---

## Use Cases

**Well-suited for:**
- **Podcast production and audiobook narration** — Google explicitly targets these use cases. The audio tag system shines for long-form content with varied tone and emotion. Batch API pricing makes high-volume production economical.
- **Multilingual content production** — 100+ languages with auto-detection is a strong capability for localization workflows. No per-language voice library management required.
- **LLM-native pipelines** — If your workflow already uses Gemini for content generation, feeding that output directly to `gemini-3.1-flash-tts-preview` in the same API call is architecturally clean.
- **Experimental voice performance** — Audio tags with open-ended instructions (`[like dracula]`) enable creative voice work that rule-based SSML systems cannot express.

**Less suited for:**
- **Real-time voice assistants** — No streaming; use the Live API instead.
- **Applications requiring deterministic output** — Voice inconsistency and rare 500 errors require retry logic and quality validation.
- **Mobile or edge applications** — PCM-only output means post-processing is mandatory; no embedded format support.
- **Enterprise deployments with SLA requirements** — Preview status carries no uptime guarantees.

---

## Rating: 3.5 / 5

Gemini 3.1 Flash TTS makes a genuine case for prompt-steerable speech synthesis as a production paradigm. The audio tag system is the most interesting TTS control mechanism we've reviewed — open-ended, natural language, and capable of expressing nuances that no SSML vocabulary can encode. The language coverage (100+, auto-detected) is a real competitive advantage. The Batch API pricing undercuts alternatives for high-volume production.

The deductions are real, though. PCM-only output adds operational friction to every deployment. The absence of streaming limits applicability to non-real-time use cases. Voice consistency is explicitly documented as unreliable. And Preview status means the API surface can change before stabilization.

For teams building LLM-native content pipelines — audiobooks, podcasts, multilingual narration — this is worth evaluating today. For anything requiring streaming, format flexibility, or guaranteed uptime, it's a model to watch rather than deploy.

---

*This is a research-based review. ChatForest has not tested Gemini 3.1 Flash TTS hands-on. Information is sourced from Google's official API documentation, pricing pages, and changelog entries as of May 2026.*

