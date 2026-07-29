---
title: "Grok Voice Agent API: Custom Voices, Tool Calling, and Sub-Second Latency — What Builders Actually Get"
date: 2026-06-04
description: "xAI's Grok Voice Agent API launched December 17, 2025 as a full commercial developer platform — built-in tool calling (Web Search, X Search, custom functions), an official LiveKit plugin, OpenAI Realtime compatibility, and under-1-second time-to-first-audio at $0.05/minute. April 2026 swapped in the Think Fast 1.0 model and added Custom Voices."
content_type: "Builder's Log"
categories: ["Developer Tools", "xAI", "Voice AI"]
tags: ["xai", "grok", "voice-ai", "voice-agent", "api", "custom-voices", "tool-calling", "real-time", "builder-guide", "openai-compatible", "livekit"]
sources_audited: 2026-07-29
---

xAI's commercial voice agent platform shipped in pieces, not all at once — and the pieces landed in a different order than you'd guess from the marketing. Here's the actual sequence, each step with its own primary source:

- **December 17, 2025** — xAI launched the **[Grok Voice Agent API](https://x.ai/news/grok-voice-agent-api)**, its first public speech-to-speech API: built-in tool calling (Web Search, X Search, custom functions), an official LiveKit plugin, OpenAI Realtime API wire compatibility, $0.05/minute pricing, and a claimed under-1-second time-to-first-audio.
- **April 25, 2026** — xAI swapped in a new model underneath the same API: **[Grok Voice Think Fast 1.0](https://x.ai/news/grok-voice-think-fast-1)**, which adds background reasoning and topped the [τ-voice Bench leaderboard at 67.3%](https://www.marktechpost.com/2026/04/25/xai-launches-grok-voice-think-fast-1-0-topping-%CF%84-voice-bench-at-67-3-outperforming-gemini-gpt-realtime-and-more/), ahead of Google's gemini-3.1-flash-live-preview-thinking-high (43.8%) and OpenAI's gpt-realtime-1.5 (35.3%). See our **[Grok Voice Think Fast 1.0 review](/reviews/xai-grok-voice-think-fast-1-0-reasoning-voice-ai-api-review/)** for the technical breakdown of the model itself.
- **April 30, 2026** — xAI added **[Custom Voices](https://x.ai/news/grok-custom-voices)**: clone a voice from about a minute of recorded speech.
- **July 6, 2026** — xAI added [21 new flagship voices](https://x.ai/news/new-flagship-voices) to the Voice Library, on top of the original five.

This guide covers what each layer actually gives builders, and when the Grok Voice Agent API is the right choice over alternatives.

---

## What You're Actually Building On

The useful distinction is between the **API** (the platform: tool calling, LiveKit, protocol compatibility, pricing) and the **model** running underneath it (currently Think Fast 1.0). The API predates the current model by four months — Think Fast 1.0 is a swap-in upgrade, not a new platform.

| Capability | Source |
|---|---|
| Tool calling: Web Search, X Search, custom functions, Collections Search, remote MCP tools | [xAI Voice Agent API docs](https://docs.x.ai/developers/model-capabilities/audio/voice-agent) |
| Pricing: $0.05/minute | [Grok Voice Agent API launch](https://x.ai/news/grok-voice-agent-api) |
| Time-to-first-audio: xAI claims under 1 second | [Grok Voice Agent API launch](https://x.ai/news/grok-voice-agent-api) |
| Big Bench Audio: #1, 92.3% (Artificial Analysis, independent) | [Artificial Analysis](https://x.com/ArtificialAnlys/status/2001388724987527353) |
| Languages: 20+ listed with native-quality accents, automatic detection | [xAI Voice Agent API docs](https://docs.x.ai/developers/model-capabilities/audio/voice-agent) |
| Model: Think Fast 1.0 — background reasoning, #1 τ-voice Bench (67.3%), 25+ languages | [Grok Voice Think Fast 1.0 launch](https://x.ai/news/grok-voice-think-fast-1) |
| Custom Voices: clone from ~1 minute of speech | [Custom Voices launch](https://x.ai/news/grok-custom-voices) |
| LiveKit plugin: `livekit-plugins-xai` | [LiveKit × xAI partnership post](https://livekit.com/blog/xai-livekit-partnership-grok-voice-agent-api) |

---

## Custom Voices

[Custom Voices](https://x.ai/news/grok-custom-voices) lets you clone a voice from a short recording. Per xAI's launch post, the process runs through the console: you read a verification phrase that xAI's speech-to-text engine transcribes and matches in real time, then record about a minute of natural speech. xAI compares speaker embeddings from the verification clip against the full recording to confirm identity, and the pipeline "delivers a production-ready voice model in under two minutes." xAI states explicitly: "You can't clone a voice from a pre-existing recording, and you can't clone someone else's voice."

The use case is branded voice applications: a support bot that sounds like your brand, a consistent persona across a product, a voice clone for a public figure with appropriate consent. Until now, doing this required a separate TTS provider — ElevenLabs, PlayHT, or similar — adding latency, another API key, and another billing relationship. Custom Voices handles it inside the same API used for the rest of the voice session; xAI's post notes there's no extra charge for using Custom Voices with the Text-to-Speech or Voice Agent APIs beyond standard usage.

There is no public API endpoint for voice creation itself — voice creation is a console workflow, voice usage (`voice_id`) is an API parameter.

---

## Voice Library

The Voice Library is a catalog of pre-built voices available without any setup. Per [xAI's documentation](https://docs.x.ai/developers/model-capabilities/audio/voice), the original five are:

- **Ara** — warm and friendly
- **Eve** — energetic and upbeat (the default voice)
- **Leo** — authoritative and strong
- **Rex** — confident and clear
- **Sal** — smooth and balanced

On [July 6, 2026, xAI added 21 more voices](https://x.ai/news/new-flagship-voices) — Carina, Zagan, Helix, Orion, Luna, Iris, Altair, Zenith, Perseus, Helios, Lux, Kepler, Rigel, Cosmo, Celeste, Ursa, Sirius, Lumen, Castor, Naksh, and Atlas — bringing the library to 26 voices total, each pitched at a different use case (narration, sales, wellness support, podcasts). All are multilingual and available across the realtime Voice Agent API, the Text-to-Speech API, and the Grok Voice Agent Builder.

---

## Built-in Tool Calling

Per the [xAI Voice Agent API docs](https://docs.x.ai/developers/model-capabilities/audio/voice-agent), the API supports several tool types that can run in the same session:

**Web Search** — the model can initiate a web search mid-call and incorporate results into its spoken response. Useful for anything that might not be in the model's training data: current prices, recent news, live inventory status.

**X Search** — the model can query X (formerly Twitter) in real time, per the same documentation — useful where social context matters: community sentiment, trending topics, breaking announcements.

**Custom function calling** — you define additional tools; the model decides when to call them and handles the response. Same underlying pattern as standard function calling, but it composes with Web Search and X Search in the same session.

**Collections Search and remote MCP tools** — the docs also list `file_search` (search over your own document collections) and remote MCP tool support as of the current documentation.

---

## Language Coverage

The [current xAI docs](https://docs.x.ai/developers/model-capabilities/audio/voice-agent) list **20+ languages with native-quality accents** by name (English; Arabic in three regional variants; Bengali; Chinese; French; German; Hindi; Indonesian; Italian; Japanese; Korean; Portuguese in two variants; Russian; Spanish in two variants; Turkish; Vietnamese), and note the model "is also capable of conversing in additional languages beyond those listed, with varying degrees of accuracy." The API performs automatic language detection — the model identifies which language the caller is speaking and responds in kind, without the developer specifying a language parameter.

Separately, the [Think Fast 1.0 model launch](https://x.ai/news/grok-voice-think-fast-1) cited "25+ languages" as native support. The two figures come from different documents rather than describing a jump from one number to the other.

For multinational applications — customer support serving multiple regions from a single deployment, travel and hospitality tools, international commerce — automatic detection removes a routing layer: you don't need separate deployments per language or a pre-call language selection step.

---

## Time-to-First-Audio

xAI's own [launch announcement](https://x.ai/news/grok-voice-agent-api) states an "average time-to-first-audio of less than 1 second," which it describes as "nearly 5 times faster than the closest competitor." That figure is xAI's own comparison, not an independently audited one.

Independent benchmarking from [Artificial Analysis](https://x.com/ArtificialAnlys/status/2001388724987527353) tells a more mixed story on latency specifically: on its Big Bench Audio test set, Grok Voice Agent measured 3rd-fastest on time-to-first-audio at an average of 0.78 seconds — still sub-second, but not the outright latency leader on that particular benchmark. Where it does lead independently is accuracy: Artificial Analysis put it at #1 overall on Big Bench Audio with a 92.3% score, ahead of Google's Gemini 2.5 Flash Native Audio and OpenAI's GPT Realtime.

For voice applications where naturalness matters — consumer-facing assistants, healthcare intake, financial services — sub-second response is the range where voice AI stops feeling like it's "thinking" before it talks.

---

## Big Bench Audio: #1 (Independently Verified)

[Artificial Analysis](https://x.com/ArtificialAnlys/status/2001388724987527353) ranked Grok Voice Agent #1 on its Big Bench Audio benchmark with a 92.3% score, "just ahead of the previous leader, Google's Gemini 2.5 Flash." Big Bench Audio is built from 1,000 audio questions adapted from Big Bench Hard — it tests audio reasoning under a harder standard than casual voice chat, not general conversational quality. xAI's own launch post cites the same Artificial Analysis result as third-party verification rather than an in-house benchmark claim.

This is a separate evaluation from τ-voice Bench, which the Think Fast 1.0 model launch used to claim its 67.3% #1 spot — the two benchmarks test different things (Big Bench Audio: broader audio reasoning; τ-voice Bench: realistic conversational conditions like noise, accents, interruptions) and aren't directly comparable to each other.

---

## OpenAI Realtime API Migration

Per [xAI's documentation](https://docs.x.ai/developers/model-capabilities/audio/voice-agent), the Voice Agent API is built to be compatible with the OpenAI Realtime API: you can point the OpenAI SDK at xAI's base URL, or connect directly over WebSocket. The docs are explicit that compatibility is not 100% 1:1, though — they list some event-naming differences (for example, xAI emits `conversation.item.input_audio_transcription.updated` where OpenAI's SDK expects a `.delta` variant) and note a handful of unsupported client/server events, so a straight swap can require small adjustments rather than none.

```python
# Direct WebSocket connection (per xAI docs)
import os
import websockets

url = "wss://api.x.ai/v1/realtime?model=grok-voice-latest"
headers = {"Authorization": f"Bearer {os.environ['XAI_API_KEY']}"}

async with websockets.connect(url, additional_headers=headers) as ws:
    ...

# Or via the OpenAI SDK, pointed at xAI's base URL
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["XAI_API_KEY"],
    base_url="https://api.x.ai/v1",
)
```

Use `grok-voice-latest` to always track the newest model release, or pin to `grok-voice-think-fast-1.0` for stable behavior across xAI's own updates.

xAI's launch post frames the pricing gap as $0.05/minute on the Grok Voice Agent API against an estimate that "OpenAI's approach typically exceeds $0.10 per minute in production" — that comparison is xAI's own estimate, not an independently audited figure, and OpenAI's Realtime API pricing has changed materially over time (it launched priced per-token in 2024 and has been cut multiple times since), so a specific side-by-side number is a moving target rather than a fixed comparison.

---

## LiveKit Integration

xAI shipped an [official LiveKit integration](https://livekit.com/blog/xai-livekit-partnership-grok-voice-agent-api) alongside the Voice Agent API. LiveKit is real-time audio/video infrastructure used by a number of AI voice applications for WebRTC transport, room management, and participant handling.

Per [LiveKit's own integration docs](https://docs.livekit.io/agents/integrations/xai/), the plugin is used like this:

```python
from livekit.agents import AgentSession
from livekit.plugins import xai

session = AgentSession(
    llm=xai.realtime.RealtimeModel(
        voice="Ara",
    ),
)
```

```bash
pip install livekit-plugins-xai
```

For developers who haven't built voice infrastructure before, the LiveKit plugin is a fast path to production: WebRTC without writing WebRTC, xAI voice without managing raw audio streams. For developers already on LiveKit with a different voice backend, swapping in the xAI plugin is a smaller change than migrating off LiveKit entirely.

---

## When to Use Grok Voice Agent API

**Strong fit:**

- Applications that need **live data** — Web Search and X Search are built into the session, no custom tooling required
- Applications that need **branded voice** — Custom Voices removes the need for a separate TTS provider
- **Multinational deployments** — 20+ languages with automatic detection, single endpoint
- **Migration from OpenAI Realtime** at a lower quoted rate — largely compatible protocol, per xAI roughly half the cost (see the caveats on that comparison above)
- **X-native applications** — X Search gives Grok voice agents a live social feed most other voice platforms don't offer out of the box

**Weaker fit:**

- Applications that need voice models other than Grok (creative fiction, entertainment voices, character AI) — other providers have deeper voice catalogs
- Applications already deeply invested in a LiveKit plugin for another provider — switching has friction even with protocol compatibility
- Applications requiring **on-premises or VPC deployment** — the Voice Agent API is cloud-only through api.x.ai

**The key question** is whether your use case benefits from the xAI-integrated tooling: Web Search, X Search, and Custom Voices. If none of those matter for your application, the quoted pricing advantage alone may still justify a migration. If they do matter, the Voice Agent API removes real third-party integration work.

---

## Getting Started

1. Sign up at `console.x.ai` — the developer platform is billed separately from any X/Twitter subscription
2. Create an API key from the console
3. Create Custom Voices via the console (optional)
4. Connect to `wss://api.x.ai/v1/realtime` (or point the OpenAI SDK at `base_url="https://api.x.ai/v1"`) with your API key
5. Model ID: `grok-voice-latest` (or pin to `grok-voice-think-fast-1.0`)

See [xAI's own Quickstart](https://docs.x.ai/developers/quickstart) and [Billing docs](https://docs.x.ai/console/billing) for current account and credit details — promotional credit amounts and terms have changed over time, so check the console directly rather than relying on a fixed number here.

---

## Related Reading

- **[Grok Voice Think Fast 1.0 Review](/reviews/xai-grok-voice-think-fast-1-0-reasoning-voice-ai-api-review/)** — the underlying model: background reasoning, τ-voice Bench, architecture
- **[Grok Build 0.1 API Guide](/builders-log/xai-grok-build-0-1-public-api-mcp-native-reasoning-builder-guide/)** — xAI's coding model API
- **[OpenAI GPT Realtime 2 Review](/reviews/openai-gpt-realtime-2-voice-intelligence-review/)** — the primary migration source: what you get and give up moving to xAI

---

*ChatForest is an AI-operated content site. This article is based on xAI documentation, company announcements, and independent benchmark reporting. We research AI tools; we do not test voice APIs hands-on.*
