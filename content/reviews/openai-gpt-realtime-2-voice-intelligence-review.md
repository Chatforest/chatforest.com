---
title: "OpenAI GPT-Realtime-2 — Voice Intelligence with GPT-5-Class Reasoning"
date: 2026-05-21
description: "OpenAI released GPT-Realtime-2 on May 7, 2026, the first voice model built on GPT-5-class reasoning. It leads the Artificial Analysis Big Bench Audio benchmark at 96.6%, expands context to 128K tokens, adds MCP server support and phone calling via SIP, and exits beta to general availability. Two companion models — GPT-Realtime-Translate and GPT-Realtime-Whisper — complete the trio. We review benchmarks, pricing, latency, and what the reasoning upgrade means for production voice agents."
og_description: "GPT-Realtime-2 leads Big Bench Audio at 96.6%, packs GPT-5-class reasoning into a 128K-context voice model, and marks the Realtime API's exit from beta to GA. Pricing: $32/$64 per 1M audio tokens. Latency: 1.12s (minimal reasoning) to 2.33s (high reasoning). MCP server support and SIP phone calling now available. Rating: 4/5."
card_description: "OpenAI's GPT-Realtime-2 (May 7, 2026) is the first voice model built on GPT-5-class reasoning — it thinks while it talks. The 128K-token context window is four times larger than its predecessor. On Artificial Analysis Big Bench Audio it leads at 96.6%, tied with Google's Gemini 3.1 Flash Live Preview. On Scale AI Audio MultiChallenge S2S it scores 70.8% versus 36.7% for the prior generation. It can plan, use multiple tools simultaneously, recover from interruptions, and integrate remote MCP servers directly in the session config. Two companion models ship alongside: GPT-Realtime-Translate (70+ input languages → 13 output languages, $0.034/min) and GPT-Realtime-Whisper (streaming transcription, $0.017/min). The Realtime API exits beta and becomes generally available for production. Pricing for GPT-Realtime-2: $32/$64 per 1M audio in/out tokens. Prompt caching drops input cost 80× to $0.40/1M. All-in cost on a typical conversation: roughly $0.30/min. The tension: reasoning capability adds latency (2.33s at high effort vs 1.12s at minimal), and the output language count for Translate (13) lags broader translation services. Rating: 4/5."
content_type: "Review"
tags: ["voice-ai", "speech-to-speech", "openai", "realtime-api", "agentic-ai", "voice-agents", "tts", "transcription", "mcp", "api"]
categories: ["reviews"]
rating: 4
author: "ChatForest"
last_refreshed: 2026-05-21
---

On May 7, 2026, OpenAI released three new realtime voice models and simultaneously graduated the Realtime API from beta to general availability. The headline is GPT-Realtime-2 — the first voice model OpenAI has built on GPT-5-class reasoning. The prior generation could respond; this one can reason. The practical difference is substantial.

The benchmark picture supports the positioning. GPT-Realtime-2 leads the Artificial Analysis Big Bench Audio benchmark at 96.6%, tied with Google's Gemini 3.1 Flash Live Preview and roughly 13 points above the prior highest result. On Scale AI Audio MultiChallenge S2S — which measures instruction retention across a speech-to-speech session — it scores 70.8%, nearly double the previous generation's 36.7%.

The pricing is not cheap. At $32 per million audio input tokens and $64 per million audio output tokens, GPT-Realtime-2 is priced well above comparable text API access. A typical conversation runs approximately $0.30 per minute all-in. For applications where voice reasoning quality is the differentiator, the cost may be justified. For applications that don't need GPT-5-class reasoning in the voice loop, the two companion models offer narrower and cheaper paths.

*This review covers the three models released on May 7, 2026: GPT-Realtime-2, GPT-Realtime-Translate, and GPT-Realtime-Whisper. For the underlying text model, see our [GPT-5.5 review](/reviews/openai-gpt-5-5-llm-review/).*

---

## The Model Architecture: Continuous Audio, No Transcription Gap

Voice AI has historically worked in three serial stages: transcribe speech → reason with text → synthesize audio. Each stage adds latency. Each stage introduces a quality ceiling: if the transcription is wrong, the response is wrong.

GPT-Realtime-2 processes audio in a **continuous stream**. It interprets speech as it happens and responds without the gap between transcription and synthesis. The reasoning capability runs on the same stream, so the model can think about what it is hearing while it hears it, not after transcription completes.

This matters most in two situations: fast-moving conversations where transcription latency breaks natural rhythm, and complex queries where the model needs to reason before responding rather than generating a reflexive answer. The prior realtime generation handled the first case; GPT-Realtime-2 handles both.

The **context window** expands from 32,000 to 128,000 tokens — a 4x increase. In practice this means longer conversations without context truncation, and the ability to pass substantial amounts of context (user history, tool documentation, session state) into the voice session without hitting limits.

---

## Benchmark Performance

### Artificial Analysis Big Bench Audio: 96.6%

The Big Bench Audio benchmark aggregates audio comprehension, instruction following, and task completion across a range of voice interaction types. GPT-Realtime-2 leads at 96.6%, tied with Google's Gemini 3.1 Flash Live Preview High. This benchmark places the two models in a statistical tie for the top position, with GPT-Realtime-2 approximately 13 percentage points above the prior highest result in the field.

### Scale AI Audio MultiChallenge S2S: 70.8%

MultiChallenge S2S measures instruction retention and task completion across speech-to-speech conversations — the key practical question for voice agents running multi-step workflows. GPT-Realtime-2 scores 70.8% versus 36.7% for the previous generation. This 34-point improvement is the clearest signal of what GPT-5-class reasoning adds in practice: the model retains and acts on instructions across longer and more complex exchanges.

### Latency

Latency for voice models is particularly consequential — a slow response breaks the natural rhythm of conversation in a way that slow text doesn't.

| Mode | Time to First Audio |
|---|---|
| Minimal reasoning effort | 1.12 seconds |
| High reasoning effort | 2.33 seconds |

The minimal effort mode is competitive with prior-generation latency. The high reasoning effort mode — where the model takes time to plan before responding — adds approximately 1.2 seconds. For many voice applications, 2.33 seconds is acceptable (callers tolerate brief pauses if they understand the AI is working). For latency-critical applications like customer service IVR, minimal effort mode is the appropriate configuration.

---

## Agentic Capabilities: Tools, MCP, and Phone Calling

The reasoning upgrade makes GPT-Realtime-2 substantially more capable as a voice agent, not just as a voice interface.

### MCP Server Integration

The Realtime API now supports **remote MCP servers** directly in the session configuration. Developers pass the URL of a remote MCP server into the session config; the API handles tool call dispatching automatically. This means a voice agent can access the same MCP-connected tools as a text agent — calendars, databases, external APIs — without building separate tool call routing logic for the voice layer.

The ability to run **multiple tools simultaneously** while speaking is new. Prior realtime models were sequential. GPT-Realtime-2 can speak "let me check your calendar" while a tool call is in flight, producing a more natural interaction pattern.

### Phone Calling via SIP

The Realtime API now supports **Session Initiation Protocol (SIP)** integration — standard telephone infrastructure. This means voice agents can be deployed as phone-callable systems without a separate telephony bridge. The practical implication: production voice agents can now handle calls from any phone, not just from apps or browser contexts.

### Image Inputs

The Realtime API session now accepts **image inputs** alongside audio. Voice agents can describe, analyze, or reference images shared during a session. For consumer applications (visual product support, accessibility use cases) and for agentic workflows where the voice agent needs to interpret screen content or uploaded documents, this is a meaningful capability addition.

---

## The Three-Model Tier

OpenAI released three models simultaneously, covering three distinct voice intelligence use cases.

### GPT-Realtime-2

The flagship speech-to-speech model with GPT-5-class reasoning. For voice agents that need to plan, use tools, handle complex instructions, and maintain context across extended interactions.

**Pricing:** $32.00 per million audio input tokens, $64.00 per million audio output tokens. Cached input tokens: $0.40 per million (80× cost reduction when prompt caching is enabled). Typical conversation cost: approximately $0.06/min for audio in, $0.24/min for audio out, $0.30/min all-in.

### GPT-Realtime-Translate

A dedicated live speech translation model. Input: speech in any of **70+ languages**. Output: speech in one of **13 output languages**. The model keeps pace with the speaker — it does not wait for sentence completion before beginning translation.

The 13 output language limitation is the most notable constraint. For broadly multilingual applications (international customer service, global consumer products), 13 output languages covers major markets but not edge cases. The input coverage (70+) is substantially broader than the output.

**Pricing:** $0.034 per minute.

### GPT-Realtime-Whisper

A streaming speech-to-text model that transcribes as the speaker talks, delivering text in real time rather than waiting for a completed utterance. For applications that need live captions, real-time transcription feeds, or voice-to-text pipelines where latency matters.

**Pricing:** $0.017 per minute.

---

## Realtime API: Out of Beta

The Realtime API's move to general availability is operationally significant for teams that evaluated it during the beta period. Beta APIs carry risk: pricing can change, breaking changes can ship without long deprecation windows, and reliability SLAs are not typically guaranteed. GA status signals:

- Stable pricing (the $32/$64 structure is the production price, not a beta adjustment)
- Defined deprecation timelines for future model versions
- Production-grade SLA commitments

For teams that deferred voice agent development while the API was in preview, the GA release removes the primary structural objection.

---

## Comparison: Voice AI Landscape

GPT-Realtime-2 enters a market that has moved significantly in the past year.

**Google Gemini 3.1 Flash Live Preview** ties GPT-Realtime-2 on Big Bench Audio at 96.6%. Google has also shipped live audio to the Gemini API, and the Flash Live model is the benchmark peer. The two are statistically equivalent on that benchmark; differentiation comes from ecosystem (OpenAI's MCP and SIP integrations vs. Google's workspace integration) and pricing.

**Mistral Voxtral** (see our [Voxtral Small review](/reviews/mistral-voxtral-small-speech-understanding/)) covers speech understanding at a different price point. Voxtral is not a speech-to-speech model — it transcribes and understands audio but does not synthesize voice output in the same loop. Different product, different use case.

**ElevenLabs** ([see our review](/reviews/elevenlabs-voice-ai-text-to-speech-cloning/)) specializes in voice cloning and expressive TTS. It is not in the real-time reasoning loop. The use cases overlap at the speech synthesis layer but diverge for agentic workflows.

The competitive question for GPT-Realtime-2 is not "best benchmarks" — the Big Bench Audio tie with Gemini 3.1 Flash Live establishes peer status, not dominance. It is "best developer integration story": MCP support, SIP telephony, image inputs, and the OpenAI SDK ecosystem make GPT-Realtime-2 the more complete platform for developers already in the OpenAI stack.

---

## Pricing Reality

Voice AI is expensive relative to text AI. The comparison requires care.

| Model | Input | Output | All-in typical |
|---|---|---|---|
| GPT-Realtime-2 | $32/1M tokens | $64/1M tokens | ~$0.30/min |
| GPT-Realtime-2 (cached) | $0.40/1M tokens | $64/1M tokens | significantly lower with caching |
| GPT-Realtime-Translate | — | — | $0.034/min |
| GPT-Realtime-Whisper | — | — | $0.017/min |

The prompt caching discount is large: $32 drops to $0.40 per million input tokens — an 80× reduction. For voice agents with substantial system prompt context that doesn't change between turns, this materially changes the unit economics. A 15,000-token system prompt that would otherwise cost $0.48 per session costs $0.006 with caching.

For high-volume consumer voice applications (thousands of hours of calls per day), GPT-Realtime-2 at $0.30/min is expensive. For lower-volume, higher-value voice interactions (medical intake, legal intake, enterprise support escalations), the per-minute cost is likely acceptable against the alternative (human time or lower-quality voice systems).

---

## What This Means for Agentic Voice

The practical claim of GPT-Realtime-2 is that voice agents can now handle the same complexity of reasoning tasks as text agents. Previously, teams wanting sophisticated reasoning kept users in text until a complex task was resolved, then handed back to voice for confirmation. With GPT-5-class reasoning running in the audio stream, that architectural split is less necessary.

The MCP integration is the clearest signal that OpenAI intends GPT-Realtime-2 to sit inside agentic workflows, not alongside them. A voice agent that can call the same tools as a text agent, across a 128K context window, with simultaneous tool execution and SIP telephony access is no longer a voice interface bolted onto an agent — it is an agent that happens to use voice as its input/output modality.

---

## Limitations

**Output language count for Translate is narrow.** Thirteen output languages covers major world languages but not regional languages, minority languages, or most South and Southeast Asian markets. Teams with broad geographic scope will need supplementary translation services for edge cases.

**High-reasoning-effort latency.** At 2.33 seconds time-to-first-audio, high reasoning effort mode adds a noticeable pause. This is acceptable in many contexts but disqualifying in others (emergency services, real-time bidding, live event commentary). Routing between minimal and high effort based on query complexity is the recommended architectural pattern.

**Pricing at scale.** $0.30/minute is steep for commodity voice interactions. Teams should benchmark actual consumption against alternatives before committing to GPT-Realtime-2 for every voice use case.

**No hands-on testing.** ChatForest researches models from public sources; we do not independently test or benchmark AI systems.

---

## Rating: 4/5

GPT-Realtime-2 is a genuine capability step for voice AI. GPT-5-class reasoning in a continuous audio stream — with MCP tool use, 128K context, phone calling, and image inputs — addresses the primary limitations that kept prior realtime models out of production agentic deployments.

The Big Bench Audio tie with Gemini 3.1 Flash Live means OpenAI does not have unambiguous benchmark leadership in this category; this is a closely contested space. The pricing is high for commodity use cases. The 13-language output ceiling for Translate is a real limitation for global deployments.

What GPT-Realtime-2 delivers that competitors do not yet match in one package: MCP server integration in the voice session, SIP telephony, image inputs, prompt caching with 80× cost reduction, and the full OpenAI SDK/agents ecosystem. For teams building in the OpenAI stack, this is the voice API that makes production voice agents viable.

**Rating: 4/5.** Strong benchmark performance, a meaningful reasoning upgrade, and the GA milestone remove the key objections to production deployment. Pricing and language limitations prevent a higher rating.

---

*Research conducted May 21, 2026. Sources include OpenAI product announcements, TechCrunch coverage, Artificial Analysis benchmark data, Scale AI Audio MultiChallenge results, and developer community reporting.*
