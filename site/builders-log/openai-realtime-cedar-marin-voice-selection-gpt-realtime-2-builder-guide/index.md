# Realtime API Voice Selection: Cedar, Marin, and the Updated Catalog for gpt-realtime-2

> gpt-realtime-2 ships with ten voices including two Realtime-exclusive additions, Cedar and Marin, which OpenAI recommends for best quality. Here is what builders need to know about voice selection, session lock-in, and cache pricing.


When OpenAI shipped gpt-realtime-2 on May 7, 2026, the voice catalog expanded to ten options and two of them — Cedar and Marin — are available exclusively in the Realtime API. OpenAI's own documentation recommends them over the other eight for best quality. That recommendation has practical implications for how you configure new voice agents and whether existing ones should be updated.

This guide covers what changed in the voice catalog, what Cedar and Marin are, how voice assignment works in sessions, and how prompt caching affects voice agent economics.

---

## The Full Voice Catalog

gpt-realtime-2 supports ten voices:

**alloy, ash, ballad, coral, echo, sage, shimmer, verse** — Available in both the Realtime API and the standard TTS API (`tts-1`, `tts-1-hd`). These eight voices were updated alongside the gpt-realtime-2 launch to benefit from the same speech quality improvements.

**cedar, marin** — Available only in the Realtime API. Not accessible via the TTS endpoint. If you try to use them in a standard TTS call, the request will fail.

---

## Cedar and Marin

OpenAI describes Cedar and Marin as representing "the most significant improvements to natural-sounding speech" in the API. The official documentation recommends: "For best quality, we recommend using `marin` or `cedar`."

Both voices are designed for the professional-empathetic register — the tone that reads as competent and trustworthy rather than either stiff or casual. This makes them well-suited for B2B and professional use cases: intake agents, medical or legal Q&A, financial support, and customer success workflows where synthetic-voice feel is a meaningful friction point.

The rest of the catalog continues to serve consumer-casual and specific character personas. Ash, Ballad, Coral, and Verse in particular offer more expressive range that may be more appropriate for entertainment or informal consumer apps. The choice depends on the persona you are building toward, not objective quality alone.

That said, if you are building a professional voice agent and have not specifically reason to pick a different voice, Cedar or Marin is the current recommended default.

---

## Voice Lock-In During Sessions

The voice is set at session initialization and **cannot be changed once the model has emitted audio in that session**. This is a hard constraint, not a soft one — the session is committed to a voice the moment the first audio output is generated.

This has a few practical consequences:

**You cannot A/B test voices within a live call.** Route different user cohorts to different sessions if you want to test voice performance. Do not try to dynamically swap voices mid-conversation.

**Set it explicitly in your session init.** The voice field is optional — if omitted, the model uses a default — but relying on defaults creates unpredictable behavior as OpenAI updates the API. Always set the voice explicitly:

```json
{
  "type": "session.update",
  "session": {
    "model": "gpt-realtime-2",
    "voice": "cedar",
    "audio": {
      "output": {
        "format": "pcm16"
      }
    }
  }
}
```

**Voice selection is a session-level design decision, not a per-response parameter.** Build your session factory to take voice as a configuration parameter, not a hardcoded string. You will want to change it per product, per market, or per user segment without touching the rest of your WebSocket logic.

---

## Cache Pricing and Voice Agent Economics

gpt-realtime-2 supports prompt caching on both text and audio inputs. Cache hits dramatically reduce the cost of sessions that share substantial context.

Current pricing:

| Input type | Uncached | Cached |
|---|---|---|
| Audio input | $32.00 / 1M tokens | $0.40 / 1M tokens |
| Text input | $4.00 / 1M tokens | $0.40 / 1M tokens |

The primary cache opportunity for voice agents is the system prompt. If your agent uses a long system prompt (instructions, persona definition, domain knowledge, tool descriptions), that prompt is present at the start of every session. If it hits the cache on a given session, the text input cost for that section drops from $4.00 to $0.40 per million tokens — a 90% reduction.

For audio, the cache applies primarily to sessions with a shared audio context prefix. This is more relevant to specific architectures (e.g., agents with a pre-recorded intro that plays first) than to general conversational agents.

**Practical math:** A voice agent with a 2,000-token system prompt running 50,000 sessions per month generates about 100M text input tokens per month in system prompt alone. At uncached pricing that is $400/month. With cache hits, $40/month. The leverage scales linearly with session volume and system prompt size.

The cache is populated automatically — there is no separate API call to prime it. OpenAI's infrastructure caches prompts that appear frequently. For high-volume deployments, you should see cache hits accumulate quickly; for low-volume or highly varied system prompts, cache hits will be minimal.

---

## Choosing a Voice: A Decision Framework

The voice decision is mostly a product decision, not a technical one. A few questions to work through:

**Professional vs. consumer tone?** Cedar and Marin land in professional-empathetic. If your agent is front-facing for enterprise users, legal/medical contexts, or customer success, start here. If you are building for consumer apps, entertainment, or youth-skewing products, consider ash, ballad, or verse.

**Persona requirements?** Some product brands have a defined voice personality. Map the voice to the persona rather than picking the "best" voice in abstract. The eight standard voices offer more personality range; Cedar and Marin are optimized for naturalness and trust over expressiveness.

**Language?** Cedar and Marin both support Italian with particularly good prosodic quality. If your agent handles Italian as a primary language, they are the better choice over the standard catalog.

**Testing:** You cannot A/B voices mid-session, but you can route a percentage of new sessions to a different voice for a production A/B test. Run sessions in parallel with different voices and compare completion rates, user satisfaction signals, or downstream conversion.

---

## What This Means for Existing Builds

If you migrated from `gpt-4o-realtime-preview` to `gpt-realtime-2` after the May 7 GA launch, your voice selection likely carried over from your beta configuration. The beta only offered a subset of voices — most commonly `alloy` was the default.

Two actions worth taking:

1. **Audit your current voice config.** If you are running `alloy` or another standard voice by default (or by inertia), evaluate whether `cedar` or `marin` would better serve your use case. The quality improvement is meaningful for professional deployments.

2. **Verify your system prompt cache hit rate.** Check your usage logs for cached vs. uncached token counts on text input. If your system prompt is not hitting the cache, investigate whether its content is changing between sessions (timestamps embedded in prompts, user-specific injections, etc.) — dynamic injection breaks caching.

---

## Configuration Reference

Set the voice in your session initialization payload:

```json
{
  "type": "session.update",
  "session": {
    "model": "gpt-realtime-2",
    "voice": "marin",
    "reasoning_effort": "medium",
    "audio": {
      "output": {
        "format": "pcm16"
      }
    }
  }
}
```

Valid voice values: `alloy`, `ash`, `ballad`, `cedar`, `coral`, `echo`, `marin`, `sage`, `shimmer`, `verse`

`cedar` and `marin` values will fail if used with the standard TTS endpoint. They are Realtime API only.

---

*Cedar and Marin launched with gpt-realtime-2 on May 7, 2026. If you are using the GA Realtime API and have not evaluated these voices, the evaluation is a ten-minute task: swap the voice string in your session config, run a test session, and listen.*

