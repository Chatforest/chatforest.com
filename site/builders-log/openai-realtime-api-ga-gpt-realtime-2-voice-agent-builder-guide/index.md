# OpenAI Realtime API Is GA: GPT-Realtime-2, Translate, and Whisper — What Voice Agent Builders Need to Know

> OpenAI shipped three new voice models on May 7, 2026 and closed the beta. GPT-Realtime-2 brings GPT-5-class reasoning, 128K context, configurable latency, and parallel tool calls to real-time audio. Here is what changed and what to migrate.


On May 7, 2026, OpenAI shipped three new voice models for the Realtime API and simultaneously moved the product out of beta. The beta API (`gpt-4o-realtime-preview`) was shut down on May 12. If you have voice agents running against the old endpoint, they have already failed or will fail the next time they try to connect.

This guide covers what the three new models do, how they differ from the beta, the complete list of breaking migration changes, and how to think about cost at scale.

---

## What Shipped

Three models, three use cases:

**`gpt-realtime-2`** — The conversational voice agent model. GPT-5-class reasoning in a streaming audio loop. This is the successor to `gpt-realtime-1.5` and the replacement for `gpt-4o-realtime-preview`.

**`gpt-realtime-translate`** — A dedicated speech-to-speech translation pipe. Audio in one language comes out in another. No conversation, no reasoning — just fast bilateral translation across 70+ input languages to 13 output languages.

**`gpt-realtime-whisper`** — Live streaming transcription. Audio goes in, text comes out as the speaker talks. Purpose-built for real-time captions and live agent input pipelines. Not a replacement for the standard Whisper batch API; a complement to it.

There is also **`gpt-realtime-mini`** — a cost-optimized variant of `gpt-realtime-2` with the same 128K context at lower per-token pricing. More on this in the pricing section.

---

## GPT-Realtime-2: What Changed

The headline improvements over the beta are context, reasoning, and tooling.

### Context: 32K → 128K tokens

The old beta cap of 32,000 tokens constrained long calls. At typical conversational audio density (600 tokens per minute of user speech, 1,200 tokens per minute of assistant audio), 32K tokens lasted roughly 17–22 minutes of dense dialogue before the context window filled. The 128K window extends that to 1–2 hours for most conversational workloads.

Audio encoding is unchanged: 1 token per 100ms of user audio, 1 token per 50ms of assistant audio. Budget accordingly.

### Reasoning Effort: Five Levels

GPT-Realtime-2 exposes five reasoning effort levels via session configuration: `minimal`, `low`, `medium`, `high`, and `xhigh`. The default is `low`.

Effort level directly trades latency for quality:

| Level | Time to first audio (typical) |
|---|---|
| `minimal` | ~1.12 seconds |
| `low` (default) | ~1.3–1.5 seconds |
| `medium` | ~1.7 seconds |
| `high` | ~2.33 seconds |
| `xhigh` | 3+ seconds |

Benchmark gains are substantial at higher effort. On Big Bench Audio, `gpt-realtime-2` at `high` scores 96.6% vs. the old `gpt-realtime-1.5` at 81.4% — a 15-point improvement. On Audio MultiChallenge, `xhigh` reaches 48.5% vs. 34.7% previously.

Practical guidance: `xhigh` is perceptibly laggy for phone-call UX. Use `low` or `medium` for conversational agents; reserve `high` and `xhigh` for use cases where quality matters more than latency (medical transcription review, high-stakes intake forms, compliance scenarios).

Set effort level in your session init:

```json
{
  "type": "session.update",
  "session": {
    "model": "gpt-realtime-2",
    "reasoning_effort": "medium"
  }
}
```

### Parallel Tool Calling

The model can call multiple tools simultaneously. If a user asks "what's the weather in Tokyo and my next three calendar events," both tool calls fire in parallel rather than sequentially. More importantly, the model can emit configurable filler phrases mid-call — "checking your calendar and looking up the weather" — so users are not waiting in silence during tool execution.

This is a first-class session behavior, not just a latency trick. Configure filler phrases in the session object or leave them at defaults.

### Voice Activity Detection

VAD is integrated at the model level. When the user begins speaking while the model is speaking, VAD cancels the current output stream and waits for the user to complete. In the beta, this required coordinating three separate services. The GA architecture handles it in a single loop, which eliminates a class of timing bugs in barge-in scenarios.

---

## GPT-Realtime-Translate

Session type: `"translation"`. Use this model for speech-to-speech translation, not as a general voice agent.

**Input:** 70+ languages  
**Output:** 13 languages — English, Mandarin, Spanish, French, German, Japanese, Korean, Portuguese, Arabic, Hindi, Russian, Italian, Indonesian

**Pricing:** $0.034/minute, billed by audio duration.

The model keeps pace with the speaker. It is a pipe, not a conversation: audio goes in one language, audio comes out in another. Do not use it for Q&A, tool calling, or anything conversational — use `gpt-realtime-2` for that. Use Translate for live call translation, multilingual support queues, or real-time captioning across languages.

---

## GPT-Realtime-Whisper

Session type: `"transcription"`. Use this for streaming transcription, not translation or conversation.

**Pricing:** $0.017/minute, billed by audio duration.

The key difference from the standard `whisper-1` batch API: Realtime Whisper produces partial text as the speaker talks, not after a segment or file finishes. Latency is adjustable — lower delay settings emit text sooner with more corrections; higher delay settings hold longer before emitting for cleaner output.

Use Realtime Whisper as your voice agent's input layer when you want live text on screen, or when your agent pipeline is text-based internally (i.e., you feed transcription to a text LLM rather than using the end-to-end audio path).

---

## gpt-realtime-mini: The Cost Option

`gpt-realtime-mini` is an underdiscussed sibling model. Same 128K context window as `gpt-realtime-2`. The pricing is dramatically different:

| Model | Audio input | Audio output |
|---|---|---|
| `gpt-realtime-2` | $32/1M tokens | $64/1M tokens |
| `gpt-realtime-mini` | $0.60/1M tokens | $2.40/1M tokens |

That is a 53x gap on input, 27x gap on output. The tradeoff is capability — `gpt-realtime-mini` lacks the GPT-5-class reasoning and has narrower benchmark performance. The exact capability ceiling is not fully documented, but it appears to be positioned as a high-throughput, low-cost option for simpler voice use cases: FAQ bots, simple IVR replacements, always-on ambient agents where intelligence matters less than cost per hour.

If you are building at volume, model the math before defaulting to `gpt-realtime-2`. A contact center running 10,000 hours/month of voice agent time at `gpt-realtime-2` pricing would spend materially more than at `gpt-realtime-mini` for interactions that do not require deep reasoning.

---

## Pricing Comparison: Beta vs. GA

The pricing shift from the beta is significant and favors builders.

| | `gpt-4o-realtime-preview` (deprecated) | `gpt-realtime-2` (GA) |
|---|---|---|
| Audio input | $100/1M tokens | $32/1M tokens |
| Audio input (cached) | — | $0.40/1M tokens |
| Audio output | $200/1M tokens | $64/1M tokens |
| Text input | ~$5/1M | $4/1M |
| Text output | ~$20/1M | $24/1M |

Audio input pricing dropped 68%. Audio output dropped 68%. The caching addition for audio input is new — if your session re-uses the same system prompt or context frequently, cached audio input at $0.40/1M tokens is a significant lever.

At a typical two-way conversation density (1,200 tokens/minute combined input and output), a 30-minute session costs approximately $0.35 on `gpt-realtime-2` — down from roughly $1.05 on the old beta model.

---

## Breaking Migration Changes

The GA API is **not wire-compatible** with the beta. Seven changes require code updates.

### 1. Remove the beta header

Old sessions required:
```
OpenAI-Beta: realtime=v1
```
This header is no longer accepted. Remove it from your WebSocket handshake.

### 2. Set session.type

The GA API introduces explicit session types. Add this to your session init:

```json
{
  "session": {
    "type": "voice_agent"
  }
}
```

Valid values: `"voice_agent"`, `"transcription"`, `"translation"`. Sessions without a type will default to `"voice_agent"`, but setting it explicitly is recommended.

### 3. Update event handler names

Several events were renamed. These are breaking if you have handler functions registered by event name:

| Old event | New event |
|---|---|
| `response.text.delta` | `response.output_text.delta` |
| `conversation.item.created` | `conversation.item.added` + `conversation.item.done` |

New event types added: `response.output_audio.delta`, `response.output_audio_transcript.delta`, `output_text`, `output_audio`.

### 4. Move audio output configuration

Audio output configuration moved from the top-level session object to a nested path:

```json
{
  "session": {
    "audio": {
      "output": {
        "voice": "alloy",
        "format": "pcm16"
      }
    }
  }
}
```

### 5. Use ephemeral credentials for browser/mobile clients

For WebRTC sessions or browser-based clients, replace your previous credential approach with the ephemeral token endpoint:

```
POST /v1/realtime/client_secrets
```

Then use `/v1/realtime/calls` to establish WebRTC sessions.

### 6. Switch to the GA model ID

Replace `gpt-4o-realtime-preview` with `gpt-realtime-2` (or `gpt-realtime-mini` if appropriate). The old model ID returns an error.

### 7. Handle events concurrently

The GA protocol explicitly supports concurrent event sending and receiving. If your application serializes WebSocket events (processes one at a time), you may hit performance issues at higher throughput. Implement asynchronous concurrent event handling.

---

## Choosing a Transport

Three transport options remain from the beta, unchanged:

**WebSocket** — Server-side orchestration. Your backend manages the session. Good for agents with complex tool calling, access to internal APIs, or compliance requirements that prohibit client-side connections to OpenAI.

**WebRTC** — Browser and mobile clients. Direct browser-to-OpenAI connection. Good for voice UI where you want to minimize your own backend latency. Use ephemeral credentials from `/v1/realtime/client_secrets` to avoid exposing API keys.

**SIP** — Telephony integration. For calling platforms (Twilio, SignalWire, etc.) that can connect a SIP trunk directly to the Realtime API.

---

## Architecture Decisions for New Builds

**Single-model voice loop vs. transcription + text LLM:** GPT-Realtime-2 handles everything in one loop (audio in, audio out, tool calls), but if you need deterministic behavior from a fine-tuned text model, consider feeding `gpt-realtime-whisper` into your text pipeline and generating TTS separately. The single-model loop is simpler; the split pipeline gives you more control.

**Effort level by call type:** Do not use one effort level for all interactions. Route simple FAQ calls to `minimal` or `low` for sub-1.2-second response latency. Route complex intake or support calls to `medium` or `high`. If you have a compliance classification step, route flagged calls to `xhigh`.

**Context budget management:** At 128K tokens, you have room to let context accumulate naturally in most calls. For very long sessions (customer support calls running 60+ minutes), implement a summarization step before the context window fills. The Realtime API does not auto-truncate — it will error if context overflows.

**Cost floor for volume:** If you are modeling a large deployment, start with `gpt-realtime-mini` pricing and layer in `gpt-realtime-2` only where the capability gap is measurable. The 53x audio input price difference is not small.

---

## Builder Checklist

- [ ] Remove `OpenAI-Beta: realtime=v1` header from all WebSocket connections
- [ ] Update model ID from `gpt-4o-realtime-preview` to `gpt-realtime-2` or `gpt-realtime-mini`
- [ ] Add `session.type` to all session init payloads
- [ ] Rename event handlers: `response.text.delta` → `response.output_text.delta`
- [ ] Handle `conversation.item.added` and `conversation.item.done` instead of `conversation.item.created`
- [ ] Move audio output config to `session.audio.output`
- [ ] Switch to `POST /v1/realtime/client_secrets` for browser/WebRTC clients
- [ ] Set `reasoning_effort` in session config (default `low`; tune per use case)
- [ ] Verify concurrent event handling is async in your WebSocket client
- [ ] Audit audio token budget: user audio at 1 token/100ms, assistant audio at 1 token/50ms
- [ ] Evaluate `gpt-realtime-mini` vs. `gpt-realtime-2` for each call type by volume × capability requirement

---

*The Realtime API beta was shut down May 12, 2026. If you have production traffic on `gpt-4o-realtime-preview`, it is already failing. Migration is not optional.*

