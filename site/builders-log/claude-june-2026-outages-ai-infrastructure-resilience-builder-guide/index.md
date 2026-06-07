# Claude Went Down Twice in One Week. Here's How to Stop Building Like It Won't Happen Again.

> Claude had two outages in June 2026 — nearly six hours on June 2, roughly two hours on June 5 — plus a third in March. Three outages in four months is a pattern. Here's what broke for builders and the four architecture patterns that would have prevented downtime.


Claude went down twice in the same week. On June 2, 2026, nearly six hours of elevated errors hit Claude Chat, Claude Code, and the Anthropic API. On June 5, a second outage ran roughly two hours — this time with staggered recovery by model, so Opus 4.6 came back in 17 minutes while Opus 4.8 was dark for nearly two hours.

Add the March 2026 outage — attributed to "unprecedented demand" from the Import Memory feature launch — and you have three production incidents across four months.

That is no longer a one-off. That is a baseline failure rate. The builders who got through June without user impact had one thing in common: they had not built single-vendor AI pipelines.

---

## What Failed and When

| Date | Duration | What Went Down |
|------|----------|----------------|
| March 2, 2026 | Several hours | Claude.ai, API, mobile; Anthropic cited unprecedented demand |
| June 2, 2026 | ~6 hours | Claude Chat (web + mobile), Claude Code, Anthropic API — 500 and 529 errors |
| June 5, 2026 | ~2 hours | All models; staggered recovery: Opus 4.6 first (17 min), Sonnet 4.6 (75 min), Opus 4.8 (111 min) |

Claude for Government was reportedly unaffected during the June 2 incident. Claude Cowork was also not listed among the primary affected services during that event — a hint that isolated tenancy environments fare better than the shared platform during capacity issues.

The June 5 pattern is telling. Models recovered independently over nearly two hours, which suggests the issue was at the model-serving layer rather than routing. When recovery is model-by-model and some models come back two hours before others, you cannot rely on Anthropic's status page to tell you which of your specific model calls will work.

---

## What This Broke for Builders

**Real-time user-facing features.** Any product that calls Claude for responses users see immediately went silent. Support bots, writing assistants, semantic search, and AI-generated content pipelines all returned errors. Users saw failures or were silently blocked.

**Background processing jobs.** Data pipelines doing classification, summarization, entity extraction, or semantic analysis froze. Jobs that could not queue accumulated backlog or lost work entirely.

**Claude Code workflows.** This is the hardest category. Claude Code is a Claude-native tool — there is no built-in fallback model. Developers lost their pair programmer mid-session, mid-PR, and mid-agentic loop. Unlike most API integrations, there is no drop-in substitute for the IDE experience.

**CI/CD pipelines using Claude Code.** Any continuous integration step using Claude Code for code review, test generation, or documentation stopped passing or timed out.

---

## The Four Patterns That Would Have Helped

### 1. Provider-level failover for synchronous calls

The production failover stack: Anthropic (primary) → OpenAI (secondary) → Gemini or Cohere (tertiary) → local or cached response (last resort).

Tools that implement this at the gateway layer:

**LiteLLM** is a drop-in OpenAI-compatible proxy that supports provider fallback with a single config change. When your primary provider returns a 5xx or exceeds a timeout, LiteLLM automatically routes to the next entry in your fallback list:

```python
from litellm import completion

response = completion(
    model="claude-opus-4-6",
    messages=[{"role": "user", "content": prompt}],
    fallbacks=["gpt-5.5", "gemini-3-5-flash"],
    context_window_fallback_dict={"claude-opus-4-6": "claude-sonnet-4-6"}
)
```

**OpenRouter** routes requests to available providers automatically and has its own reliability layer. For builders who do not want to run their own proxy, OpenRouter is the fastest path to multi-provider routing without infrastructure work.

**Portkey** adds fallback, retries, and load balancing via a lightweight SDK wrapper. It also provides a dashboard for tracking provider reliability over time — useful for auditing your own fallback history after incidents.

**Cloudflare AI Gateway** caches responses, logs requests across providers, and can route around provider failures. If you are already using Cloudflare Workers or have your infrastructure on Cloudflare, this requires almost no setup.

---

### 2. Graceful degradation instead of hard failure

Not all features need the same model tier. Mapping your features to model requirements before an outage lets you downgrade intentionally rather than error out.

A tiered mapping looks like:

| Feature | Primary | Degraded | Minimal |
|---------|---------|----------|---------|
| Long-form document analysis | Claude Opus 4.8 | GPT-5.5 | Skip / queue |
| User-facing chat response | Claude Sonnet 4.6 | GPT-5.5 Instant | Cached template |
| Real-time classification | Claude Haiku 4.5 | Gemini 3.5 Flash | Rule-based regex |
| Code review in CI | Claude Code | Codex on Bedrock | Skip, flag for manual |

When Claude is down, your system should detect the failure and automatically shift to the next column — not return an error to the user.

---

### 3. Queue-and-retry for background jobs

For any non-real-time AI processing, treat the AI call as an unreliable external service:

- Write job inputs to a durable queue (SQS, Redis, BullMQ, Celery) before calling the API
- Workers consume from the queue with exponential backoff on 5xx responses
- A dead-letter queue captures jobs that exhaust retries for manual inspection or replay

This pattern handles outages and rate limit events equally — both produce 5xx or 429 responses that should trigger the same retry logic. The June 5 outage lasted two hours. A well-configured queue-and-retry setup would have delivered all jobs within 20 minutes of Claude recovering.

---

### 4. Monitoring that alerts you before your users do

Subscribe to the Anthropic status feed at [status.anthropic.com](https://status.anthropic.com/) and configure a webhook or email alert. The status page flagged the June 5 outage at 8:08 PT — before most users reported issues. Builders who subscribed to alerts had 10–15 minutes of advance notice to flip feature flags or redirect traffic.

Beyond the provider's own status page, monitor your application's own error rate for 5xx responses on AI provider calls. A spike in 529s (Anthropic's rate-limit-and-overload code) is the earliest signal that something is wrong — often before it appears on the official status page.

Minimum monitoring setup:
- Alert if `anthropic_api_errors_5xx` rate exceeds 5% over a 2-minute window
- Alert if median latency on AI calls exceeds 3× the baseline P50
- Alert when Anthropic posts a new status incident

---

## The 30-Minute Hardening Checklist

You do not have to solve multi-provider routing today. But you can reduce exposure to the next outage in one focused session:

1. **Identify your load-bearing Claude calls.** Which three features would break most visibly if Claude returned 500s for two hours?
2. **Add exponential backoff and retry.** This is free and handles transient errors without a gateway. Most HTTP clients support it natively.
3. **Pick one gateway tool.** LiteLLM and OpenRouter both have free tiers. Pick whichever matches your stack and configure a single fallback model.
4. **Map graceful degradation for your top three features.** Write down what "good enough" looks like without Claude — a cached response, a rule-based answer, a simplified output.
5. **Subscribe to Anthropic status alerts.** Takes two minutes. Gives you early warning that an incident is active.

---

## Why This Is Getting More Likely, Not Less

Anthropic is in the fastest growth phase of its existence. Revenue went from $10 billion annual run rate last year to $47 billion this year. The company raised $65 billion in Series H funding and filed a confidential S-1 in June. It signed a $1.25-billion-per-month compute deal for SpaceX's Colossus 1 facility — 220,000-plus GPUs migrating onto new infrastructure during peak demand growth.

Every infrastructure migration, every new model launch, every new compute cluster introduces coupling risk. The March outage came from demand spikes driven by a feature launch. The June 2 outage came during the same week as Microsoft Build and multiple model announcements across the industry — the highest-traffic week in AI developer activity this year.

This is the same pattern AWS showed in 2011–2013: rapid growth, new infrastructure, growing dependencies, periodic incidents. The answer then was resilient architecture. The answer is the same now.

Claude is excellent. It is also a single point of failure if you let it be. The outages are not a reason to stop using it — they are a reason to use it the same way you use any other critical infrastructure dependency.

---

*The Anthropic status page is at [status.anthropic.com](https://status.anthropic.com/). The Cloudflare AI Gateway article on this site covers one implementation path for gateway-level routing.*

