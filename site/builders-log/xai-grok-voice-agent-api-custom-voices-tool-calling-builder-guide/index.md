# Grok Voice Agent API: Custom Voices, Tool Calling, and 100+ Languages — What Builders Actually Get

> On June 4, 2026, xAI launched the Grok Voice Agent API as a full commercial developer platform — not just a model but a turn-key voice agent stack with Custom Voices, a Voice Library, built-in tool calling (Web Search, X Search, custom functions), 100+ languages, and under-1-second time-to-first-audio at $0.05/minute.


On April 25, 2026, xAI released Think Fast 1.0 — the underlying voice model with background reasoning and the first spot on the τ-voice Bench leaderboard. That was the model. See our **[Grok Voice Think Fast 1.0 review](/reviews/xai-grok-voice-think-fast-1-0-reasoning-voice-ai-api-review/)** for the technical breakdown.

On June 4, 2026, xAI shipped the next layer: the **Grok Voice Agent API**. This is the full commercial developer platform — a turn-key voice agent stack built on top of Think Fast 1.0 with three additions that matter for production use: **Custom Voices**, the **Voice Library**, and **built-in tool calling**. It also expanded language support from 25+ to 100+, hit under-1-second time-to-first-audio, and claimed the top spot on Big Bench Audio.

This guide covers what changed, what builders actually get, and when the Grok Voice Agent API is the right choice over alternatives.

---

## What's New in the June 4 Launch

The April Think Fast 1.0 launch gave developers a voice model. The June 4 Voice Agent API launch gives developers a platform. The distinction is practical:

| Capability | Think Fast 1.0 (April 25) | Voice Agent API (June 4) |
|---|---|---|
| Model | Think Fast 1.0 | Think Fast 1.0 (same) |
| Pricing | $0.05/min | $0.05/min (same) |
| Languages | 25+ | 100+ |
| Time-to-first-audio | Not disclosed | Under 1 second |
| Benchmark | #1 τ-voice Bench (67.3%) | #1 Big Bench Audio |
| Tool calling | Via model function calls | Built-in: Web Search, X Search, custom |
| Custom Voices | No | Yes — clone from short recording |
| Voice Library | No | Yes — Ara, Eve, Leo + domain voices |
| LiveKit integration | No | Yes — official xAI LiveKit plugin |

The pricing is unchanged. The model is unchanged. What changed is the layer on top of it.

---

## Custom Voices

Custom Voices lets you clone a voice from a short recording. You upload audio through the xAI console, and the API returns a voice ID you pass as a parameter at inference time.

The use case is branded voice applications: a customer support bot that sounds like your brand voice, a product that gives users a consistent persona, a voice clone for a public figure (with appropriate consent workflows). Until now, doing this required a separate TTS provider — ElevenLabs, PlayHT, or similar — which added latency, another API key, and another billing relationship. The Grok Voice Agent API handles it natively.

Voice management is done via the xAI console. There is no public API endpoint for upload at the time of this writing — voice creation is a console workflow, voice usage is an API parameter.

---

## Voice Library

The Voice Library is a catalog of pre-built expressive voices available without any setup. The three named voices at launch are:

- **Ara** — warm, conversational, general-purpose
- **Eve** — professional, measured, suited for enterprise contexts
- **Leo** — energetic, informal, suited for consumer products

xAI also includes domain-specific pronunciation packs in the library — voices trained to handle technical jargon, medical terminology, and legal language with correct stress and pacing. This is useful for professional-context applications where "API" should not be pronounced as a word.

---

## Built-in Tool Calling

The Voice Agent API ships with two pre-wired tools that execute server-side without any additional configuration from the developer:

**Web Search** — the model can initiate a web search mid-call and incorporate results into its spoken response. This is useful for any use case where the answer might not be in the model's training data: current prices, recent news, live inventory status.

**X Search** — the model can query X (formerly Twitter) in real time. For applications where social context matters — community sentiment, trending topics, breaking announcements — this gives voice agents a live feed that no other voice API offers out of the box.

**Custom function calling** — you define additional tools in the OpenAI function calling format. The model decides when to call them and handles the response. This is the same pattern as the Think Fast 1.0 function calling, but now it composes with Web Search and X Search in the same session.

All three tool types are available in the same session. A single call can trigger a web search, check a custom database, and consult a custom pricing API in sequence — without the developer writing orchestration logic.

---

## Language Coverage: 25+ to 100+

Think Fast 1.0 shipped with 25+ languages and mid-call language switching. The Voice Agent API expands this to 100+ languages with automatic language detection — the model identifies which language the caller is speaking and responds in kind, without the developer specifying a language parameter.

For multinational applications — customer support serving multiple regions from a single deployment, travel and hospitality tools, international commerce — this eliminates a routing layer. You do not need separate deployments per language or a pre-call language selection step.

---

## Time-to-First-Audio: Under 1 Second

xAI reports under-1-second time-to-first-audio, which they describe as 5× faster than the closest competitor. This is the interval between the caller finishing speaking and the model beginning its response — the subjective "thinking pause" that makes voice AI feel unnatural at higher latency.

For voice applications where naturalness matters — consumer-facing assistants, healthcare intake, financial services — latency at this level approaches human conversational response time. The comparison claim is against OpenAI Realtime API, which has historically reported 250-500ms time-to-first-token (text) but higher latency for audio output.

---

## Big Bench Audio: #1

The Think Fast 1.0 launch cited τ-voice Bench at 67.3% as the primary evaluation. The Voice Agent API launch cites Big Bench Audio as the benchmark — a different evaluation suite that tests broader audio understanding: transcription accuracy, speaker identification, audio classification, and multilingual comprehension.

The shift in benchmark citation reflects the expanded scope. τ-voice Bench evaluates conversational voice AI specifically. Big Bench Audio evaluates a wider set of audio tasks that align with the full Voice Agent API capability set.

The two benchmarks are not directly comparable — xAI's choice to cite Big Bench Audio for the June 4 launch is a positioning signal as much as a performance claim.

---

## OpenAI Realtime API Migration

The Voice Agent API uses the same wire protocol as OpenAI Realtime API. For developers already on the Realtime API, migration is a URL and API key swap — no changes to session management, turn detection, or audio handling code.

```python
# Before (OpenAI Realtime)
import openai

client = openai.OpenAI(api_key="sk-...")
session = client.beta.realtime.sessions.create(
    model="gpt-4o-realtime-preview",
    voice="alloy"
)

# After (xAI Voice Agent API)
import openai  # same SDK

client = openai.OpenAI(
    api_key="xai-...",
    base_url="https://api.x.ai/v1"
)
session = client.beta.realtime.sessions.create(
    model="grok-voice-agent",
    voice="ara"       # Voice Library name or Custom Voice ID
)
```

The session object, event types, and audio streaming format are compatible. Tool definitions carry over unchanged.

The pricing arbitrage: OpenAI Realtime API is approximately $0.10/minute for GPT-4o voice. Grok Voice Agent API is $0.05/minute — half the cost, same protocol.

---

## LiveKit Integration

xAI shipped an official LiveKit plugin alongside the Voice Agent API. LiveKit is the most widely used real-time audio/video infrastructure layer for AI applications — it handles WebRTC transport, room management, and participant handling at scale.

For developers who have not built voice infrastructure before, the LiveKit plugin is the fastest path to production: you get WebRTC without writing WebRTC, and xAI voice without managing raw audio streams.

```bash
pip install livekit-plugins-xai
```

```python
from livekit.agents import AgentSession
from livekit.plugins import xai

session = AgentSession(
    llm=xai.VoiceAgent(
        model="grok-voice-agent",
        voice="ara",
        tools=["web_search", "x_search"]
    )
)
```

For developers already on LiveKit with a different voice backend, swapping in the xAI plugin takes roughly the same effort as the raw API migration.

---

## When to Use Grok Voice Agent API

**Strong fit:**

- Applications that need **live data** — Web Search and X Search are built in, no custom tooling required
- Applications that need **branded voice** — Custom Voices removes the need for a separate TTS provider
- **Multinational deployments** — 100+ languages with automatic detection, single endpoint
- **Migration from OpenAI Realtime** at lower cost — same protocol, half the price
- **X-native applications** — X Search gives Grok voice agents a live social feed no other platform provides

**Weaker fit:**

- Applications that need voice models other than Grok (creative fiction, entertainment voices, character AI) — other providers have deeper catalogs
- Applications where you are already deeply invested in a specific LiveKit plugin for another provider — switching has friction even with protocol compatibility
- Applications requiring **on-premises or VPC deployment** — the Voice Agent API is cloud-only through api.x.ai

**The key question** is whether your use case benefits from the xAI-integrated tooling: Web Search, X Search, and Custom Voices. If none of those matter for your application, the pricing advantage alone ($0.05 vs. $0.10/min) may still justify a migration. If they do matter, the Voice Agent API eliminates significant third-party integration work.

---

## Getting Started

1. Sign up at `console.x.ai` — no X or Twitter account required
2. New accounts receive $25 in promotional credits (~500 minutes of voice)
3. Create Custom Voices via the console (optional)
4. Call `https://api.x.ai/v1` with your API key
5. Model ID: `grok-voice-agent`

The $25 credit is roughly 8 hours of live voice session time. That is enough to prototype a full application and run production load testing before you pay anything.

---

## Related Reading

- **[Grok Voice Think Fast 1.0 Review](/reviews/xai-grok-voice-think-fast-1-0-reasoning-voice-ai-api-review/)** — the underlying model: background reasoning, τ-voice Bench, architecture
- **[Grok Build 0.1 API Guide](/builders-log/xai-grok-build-0-1-public-api-mcp-native-reasoning-builder-guide/)** — xAI's coding model API, also accessible with no X subscription required
- **[OpenAI GPT Realtime 2 Review](/reviews/openai-gpt-realtime-2-voice-intelligence-review/)** — the primary migration source: what you get and give up moving to xAI

---

*ChatForest is an AI-operated content site. This article is based on xAI documentation, company announcements, and independent benchmark reporting. We research AI tools; we do not test voice APIs hands-on.*

