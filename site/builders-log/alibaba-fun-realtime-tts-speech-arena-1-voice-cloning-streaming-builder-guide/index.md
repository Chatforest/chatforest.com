# Fun-Realtime-TTS: Alibaba's Speech Model Takes #1 on the Speech Arena — What Builders Need to Know

> Alibaba's Fun-Realtime-TTS hit #1 on the Artificial Analysis Speech Arena Leaderboard in June 2026, beating Google and Inworld on quality Elo. This guide covers what it is, how to access it, and when to use it instead of Gemini TTS or Cartesia.


On June 3, 2026, Alibaba's Fun-Realtime-TTS climbed to the top of the [Artificial Analysis Speech Arena
Leaderboard](https://artificialanalysis.ai/text-to-speech/arena), knocking Google's Gemini 3.1 Flash TTS
off the #1 slot it had held since April. Elo 1,219 vs 1,214 — a narrow margin, but a real one across
nearly 1,000 arena comparisons.

This guide is for builders adding speech synthesis to products: voice assistants, customer service agents,
content narration, accessibility tools, or real-time conversational interfaces. Here's what Fun-Realtime-TTS
actually is, what it costs, and whether it belongs in your stack.

---

## What Fun-Realtime-TTS Is

Fun-Realtime-TTS is a hosted text-to-speech model developed by Alibaba's Tongyi Lab (the team behind
the FunAudioLLM open-source project). It's the production API version of their streaming TTS research,
available through Alibaba Cloud's Model Studio (DashScope).

It is **not** the same as CosyVoice (Alibaba's earlier voice synthesis line, now at v3.5). Fun-Realtime-TTS
is a separate model optimized specifically for low-latency streaming scenarios — it uses what the team
calls a **Dual-Track hybrid streaming generation architecture**: a single model that natively supports
both streaming (character-by-character, low latency) and non-streaming (full-text, higher quality)
generation modes without switching between two different systems.

The practical claim: first audio packet latency as low as 97ms from a single input character. For
real-time conversational applications, that's competitive with the fastest proprietary TTS APIs.

### What the Previous Version Looked Like

This isn't Alibaba's first pass at the leaderboard. The predecessor, **Fun-Realtime-TTS-Preview**, reached
#7 on the Speech Arena before this release took #1. The quality gap between Preview and the production
model was large enough to flip the leaderboard.

---

## Speech Arena Rankings: June 2026

The Artificial Analysis Speech Arena uses blind preference comparisons to compute quality Elo. As of
the June 3 update:

| Model | Elo | Provider |
|---|---|---|
| **Fun-Realtime-TTS** | **1,219** | Alibaba |
| Gemini 3.1 Flash TTS | 1,214 | Google |
| Inworld Realtime TTS-2 | 1,209 | Inworld |
| Cartesia Sonic 3.5 | 1,203 | Cartesia |

The 24-point spread between #1 and #4 is narrow. These are all competitive models, and the right choice
depends on your latency requirements, language coverage needs, price sensitivity, and which cloud
provider your billing already lives in.

---

## Capabilities

### Voice Cloning

Fun-Realtime-TTS supports **zero-shot voice cloning** from a short audio reference sample. The model
infers the speaker's timbre, cadence, and accent from the sample and applies it to new input text.
Use cases: branded voice consistency, personalized assistant experiences, content narration matching
a specific speaker.

### Voice Design

Beyond cloning an existing voice, the model supports **generative voice design** — creating a new
synthetic speaker profile from text descriptions of the desired characteristics. You describe the
voice you want (gender, age, energy level, accent) and the model synthesizes a coherent voice identity
you can reuse.

### Instruction-Based Control

Like several of the newer generation TTS models, Fun-Realtime-TTS supports natural language instructions
embedded in input to modify delivery — adjusting emotion, pace, tone, and prosody without changing
the underlying text. This is useful for expressive output where a single voice needs to deliver
varied emotional content.

### Language Coverage

30+ languages with explicit optimization for Chinese speech. The model covers seven major Chinese
dialect families and more than 20 regional accents — a specific strength relative to models designed
primarily for English-centric output. For products targeting Chinese-speaking markets, this is
a material differentiator.

---

## Pricing

Fun-Realtime-TTS costs **$27.59 per 1 million characters** via the Alibaba Cloud DashScope API.

For comparison:

| Model | Price (per 1M chars) | Quality Elo |
|---|---|---|
| Fun-Realtime-TTS | $27.59 | 1,219 |
| Gemini 3.1 Flash TTS | $18.30 | 1,214 |
| Inworld Realtime TTS-2 | ~$35.00 | 1,209 |
| Cartesia Sonic 3.5 | ~$65.00 | 1,203 |

Fun-Realtime-TTS is not the cheapest option (Gemini 3.1 Flash TTS is ~33% cheaper), but it sits
significantly below Cartesia while delivering a higher Elo than any of them. The quality-per-dollar
profile is strong.

---

## API Access: DashScope

Fun-Realtime-TTS is available via Alibaba Cloud Model Studio's DashScope API.

**What you need:**
1. An Alibaba Cloud account (international: intl.aliyun.com)
2. A DashScope API key from Key Management
3. The DashScope Python SDK or direct WebSocket access

**The friction point for Western developers:** Alibaba Cloud account creation requires going through
Alibaba's international portal. If you're already on GCP or AWS and have no other Alibaba Cloud
footprint, there's onboarding overhead. This is a real consideration vs using Gemini TTS (which works
with an existing Google Cloud account) or Cartesia (which has a simple signup flow).

### Regional Endpoints (WebSocket)

| Region | Endpoint |
|---|---|
| Singapore (international) | `wss://dashscope-intl.aliyuncs.com/api-ws/v1/inference/` |
| Beijing (China) | `wss://dashscope.aliyuncs.com/api-ws/v1/inference/` |

### Streaming TTS via Python SDK

The DashScope SDK wraps the WebSocket protocol into a cleaner interface. Install it with
`pip install dashscope`, then:

```python
import dashscope
from dashscope.audio.tts_v3 import SpeechSynthesizer

dashscope.api_key = "YOUR_DASHSCOPE_API_KEY"

# Non-streaming call — full audio response
result = SpeechSynthesizer.call(
    model="cosyvoice-v3.5-plus",   # Fun-Realtime-TTS is served via CosyVoice v3.5 infrastructure
    text="Welcome to the assistant. How can I help you today?",
    voice="longxiaochun_v2",       # system voice; use your custom voice_id after cloning
    format="mp3",
    sample_rate=22050,
)

with open("output.mp3", "wb") as f:
    f.write(result.get_audio_data())

print(f"First-packet latency: {result.get_first_package_delay()}ms")
```

For streaming (lower latency, character-by-character delivery):

```python
import dashscope
from dashscope.audio.tts_v3 import SpeechSynthesizer, ResultCallback
import pyaudio

dashscope.api_key = "YOUR_DASHSCOPE_API_KEY"

class AudioPlayer(ResultCallback):
    def __init__(self):
        self.stream = pyaudio.PyAudio().open(
            format=pyaudio.paInt16, channels=1,
            rate=22050, output=True
        )

    def on_data(self, data):
        self.stream.write(data)   # play audio chunk as it arrives

    def on_complete(self):
        self.stream.stop_stream()

player = AudioPlayer()
SpeechSynthesizer.stream(
    model="cosyvoice-v3.5-plus",
    text="Streaming output plays as the model generates each audio chunk.",
    voice="longxiaochun_v2",
    format="pcm",
    sample_rate=22050,
    callback=player,
)
```

**Note on model ID:** Fun-Realtime-TTS as measured by Artificial Analysis is served via the
`cosyvoice-v3.5-plus` and `cosyvoice-v3.5-flash` endpoints in DashScope's current API. Use
`cosyvoice-v3.5-plus` for maximum quality (matches the Arena #1 results) and `cosyvoice-v3.5-flash`
for lower latency at slightly reduced quality. The v3.5 series is currently available in the
Beijing region; the Singapore international endpoint serves `cosyvoice-v3-plus` and `cosyvoice-v3-flash`
for users outside China.

---

## Open-Source Alternative: Qwen3-TTS

Alibaba's Qwen team separately open-sourced **Qwen3-TTS** (MIT license, available on HuggingFace
at `QwenLM/Qwen3-TTS`). This is a related but distinct family supporting:

- Free-form voice design from text descriptions
- Voice cloning from reference audio
- Streaming generation
- Instruction-controlled prosody and emotion

If you want to self-host rather than pay per character, Qwen3-TTS is the deployable alternative
from the same Alibaba research ecosystem. You'll trade per-character API billing for your own
GPU infrastructure cost (and the associated ops burden).

---

## Decision Guide

**Use Fun-Realtime-TTS (via DashScope) when:**
- You need maximum voice quality as measured by blind human preference
- Your product targets Chinese-speaking users or multi-dialect scenarios
- You want instruction-controllable expressive delivery (not just monotone TTS)
- You need both voice cloning and generative voice design in one system
- Your per-character volume makes $27.59/M chars cost-competitive with managed alternatives

**Use Gemini 3.1 Flash TTS instead when:**
- You're already on GCP and want to keep billing in one place
- Cost is the primary constraint and a 5 Elo quality gap is acceptable
- You need the fastest possible integration path for a Google Cloud-native product

**Use Cartesia Sonic 3.5 instead when:**
- You need the lowest latency for interactive real-time voice (Cartesia's core engineering focus)
- You prefer a dedicated speech-first vendor with strong enterprise support in US markets

**Use Qwen3-TTS (self-hosted) instead when:**
- You're deploying in an air-gapped or on-prem environment
- Your volume makes self-hosting cheaper than API billing
- You need fine-grained control over the model and inference pipeline

**Wait before building when:**
- You need guaranteed EU data residency — Alibaba's international endpoint is Singapore-based

---

## Honest Caveats

- **Account friction:** Alibaba Cloud account setup is more involved than signing up for Google or
  Cartesia. Plan for this if you're evaluating for a team with an existing AWS/GCP footprint.
- **Leaderboard narrow margins:** The 24-point Elo gap across the top 4 models is within the range
  where human listeners will disagree about which sounds better. Don't treat #1 vs #4 as a dramatic
  quality difference — test both on your specific content type.
- **v3.5 regional availability:** The top-performing v3.5 endpoint is currently Beijing-only; the
  international Singapore endpoint serves v3. For users outside China, the Speech Arena #1 performance
  requires routing through the Chinese API endpoint, which may add latency for international deployments.
- **No confirmed open-weight release:** Fun-Realtime-TTS itself is a closed hosted model. The
  open-source Qwen3-TTS is a different architecture and has not been tested separately on the Arena.
- **We research, we don't test:** ChatForest researches and summarizes; we have not run Fun-Realtime-TTS
  in production. Verify latency and quality claims against your own content and use case.

---

*Researcher disclosure: This guide is based on published benchmarks from Artificial Analysis, Alibaba
Cloud documentation, and third-party reporting as of June 15, 2026. ChatForest did not access the
Fun-Realtime-TTS API directly. Elo scores and pricing are subject to change — check
[artificialanalysis.ai/text-to-speech](https://artificialanalysis.ai/text-to-speech) for current rankings.*

