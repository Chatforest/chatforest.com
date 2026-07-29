---
title: "Claude Went Down Twice in One Week. Here's How to Stop Building Like It Won't Happen Again."
date: 2026-06-07
description: "Claude had two outages in June 2026 — nearly six hours on June 2, over three hours to fully resolve on June 5 — plus a third in March. Three outages in four months is a pattern. Here's what broke for builders and the four architecture patterns that would have prevented downtime."
og_description: "Two Claude outages in one week. What broke: Claude Code, API (500/529 errors), Cowork, mobile apps. Four resilience patterns every AI-dependent builder needs: provider failover, graceful degradation, queue-and-retry, and active monitoring."
content_type: "Builder's Log"
categories: ["AI Infrastructure", "Anthropic", "Developer Tools"]
tags: ["claude", "anthropic", "outage", "resilience", "ai-infrastructure", "fallback", "multi-provider", "litellm", "openrouter", "circuit-breaker", "builders-log"]
sources_audited: 2026-07-29
---

Claude went down twice in the same week. On June 2, 2026, elevated errors hit Claude.ai, the Claude Console, the Anthropic API, and Claude Code for about five hours and 45 minutes, from 06:04 to 11:49 UTC ([Anthropic status page incident](https://status.claude.com/incidents/zkr25thltwc9)). On June 5, a second incident began at 8:08am PT (15:08 UTC): Opus 4.6 recovered in 17 minutes, Sonnet 4.6 in 75 minutes, and Opus 4.8 in 111 minutes (just under two hours), but two more models (Opus 4.7, Opus 4.5) were still degraded until 17:12 and 17:29 UTC, and Anthropic didn't confirm "success rates across all models have returned to expected levels" until 18:27 UTC — just over three hours after the start ([Cyber Security News incident report](https://www.cryptika.com/anthropics-claude-services-down-claude-ai-claude-code-and-cowork-affected-updated/)).

Add the March 2, 2026 outage — during the same week Anthropic [launched its Import Memory feature](https://quasa.io/media/anthropic-introduces-memory-import-in-claude-bring-your-context-from-any-ai-tool) — and you have three production incidents across four months. Anthropic attributed the March disruption to "unprecedented demand for Claude over the last week" in its own statement to users ([Insurance Journal / AP wire report](https://www.insurancejournal.com/news/national/2026/03/02/860100.htm)).

That is no longer a one-off. That is a baseline failure rate. The builders who got through June without user impact had one thing in common: they had not built single-vendor AI pipelines.

---

## What Failed and When

| Date | Duration | What Went Down |
|------|----------|----------------|
| March 2, 2026 | Several hours | Claude.ai, API, mobile; Anthropic [cited "unprecedented demand"](https://www.insurancejournal.com/news/national/2026/03/02/860100.htm) |
| June 2, 2026 | ~5h45m (06:04–11:49 UTC) | Claude.ai (web + mobile), Claude Code, Claude Console, Anthropic API — 500 and 529 errors ([status page](https://status.claude.com/incidents/zkr25thltwc9)) |
| June 5, 2026 | ~2h (headline models) to ~3h19m (full resolution) | Five models affected; staggered recovery: Opus 4.6 (17 min), Sonnet 4.6 (75 min), Opus 4.8 (111 min), Opus 4.7 (124 min), Opus 4.5 (141 min); all-clear at 18:27 UTC ([Cyber Security News](https://www.cryptika.com/anthropics-claude-services-down-claude-ai-claude-code-and-cowork-affected-updated/)) |

Claude for Government was reportedly unaffected during the June 2 incident, and Claude Cowork stayed "operational but has occasional outages" rather than going fully down ([Sportskeeda status report](https://tech.sportskeeda.com/laptops/news-is-claude-right-now-outage-status-explored)) — a hint that isolated tenancy environments fare better than the shared platform during capacity issues.

The June 5 pattern is telling. Models recovered independently over more than two hours, which suggests the issue was at the model-serving layer rather than routing. When recovery is model-by-model and some models come back hours before others, you cannot rely on Anthropic's status page to tell you which of your specific model calls will work.

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

**[LiteLLM](https://docs.litellm.ai/docs/proxy/reliability)** is a drop-in OpenAI-compatible proxy that supports provider fallback with a config change. When your primary provider returns a 5xx or exceeds a timeout, LiteLLM automatically routes to the next entry in your fallback list:

```python
from litellm import completion

response = completion(
    model="claude-opus-4-6",
    messages=[{"role": "user", "content": prompt}],
    fallbacks=["gpt-5.5", "gemini-3-5-flash"],
    context_window_fallback_dict={"claude-opus-4-6": "claude-sonnet-4-6"}
)
```

**[OpenRouter](https://openrouter.ai/blog/insights/reliability-failover/)** deprioritizes providers with outages in the last 30 seconds and automatically falls through to the next provider serving a model on a 5xx or rate-limit response. For builders who do not want to run their own proxy, OpenRouter is a fast path to multi-provider routing without infrastructure work — though note it carries no SLA of its own.

**[Portkey](https://portkey.ai/docs/product/ai-gateway/load-balancing)** adds fallback, automatic retries (with exponential backoff), and load balancing via a lightweight SDK wrapper. It also provides a dashboard for tracking provider reliability over time — useful for auditing your own fallback history after incidents.

**[Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/)** caches responses, logs requests by default, and supports configurable retry and provider fallback on transient errors. If you are already using Cloudflare Workers or have your infrastructure on Cloudflare, this requires almost no setup.

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

This pattern handles outages and rate limit events equally — both produce 5xx or 429 responses that should trigger the same retry logic. The June 5 outage took [just over three hours to fully resolve](https://www.cryptika.com/anthropics-claude-services-down-claude-ai-claude-code-and-cowork-affected-updated/). A well-configured queue-and-retry setup would have delivered all jobs within 20 minutes of Claude recovering.

---

### 4. Monitoring that alerts you before your users do

Subscribe to the Anthropic status feed at [status.claude.com](https://status.claude.com/) (formerly status.anthropic.com) and configure a webhook or email alert. The status page flagged the June 5 outage at 8:08am PT ([Cyber Security News](https://www.cryptika.com/anthropics-claude-services-down-claude-ai-claude-code-and-cowork-affected-updated/)); for the June 2 incident, the status page recorded a start time of 06:04 UTC ([status page](https://status.claude.com/incidents/zkr25thltwc9)) while public Downdetector reports didn't climb until around 2:19am ET, roughly 15 minutes later ([sqmagazine.co.uk](https://sqmagazine.co.uk/claude-ai-down-outage-june-2026/)) — a real but modest head start for anyone subscribed directly to the status feed.

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

Anthropic is in a rapid growth phase. Run-rate revenue went from roughly $9 billion at the end of 2025 to $47 billion by late May 2026 ([Simon Willison, citing Anthropic's own figures](https://simonwillison.net/2026/May/29/anthropic/); [Anthropic Series H announcement](https://www.anthropic.com/news/series-h)). The company raised $65 billion in Series H funding at a $965 billion post-money valuation and [confidentially submitted a draft S-1](https://www.anthropic.com/news/confidential-draft-s1-sec) to the SEC on June 1, 2026. It also signed a roughly $1.25-billion-per-month compute deal for SpaceX's Colossus 1 facility — reported at 220,000-plus GPUs migrating onto new infrastructure during peak demand growth ([The New Stack](https://thenewstack.io/anthropic-spacex-claude-limits/); [BuildMVPFast, citing SpaceX's S-1 disclosure](https://www.buildmvpfast.com/blog/anthropic-xai-colossus-1-gpu-data-center-compute-deal-2026)).

Every infrastructure migration, every new model launch, every new compute cluster introduces coupling risk. The March 2 outage landed in the same week Anthropic shipped its Import Memory feature, though Anthropic's own explanation was simply "unprecedented demand," not a specific feature attribution. The June 2 outage fell on the same days as Microsoft's Build 2026 developer conference (June 2–3) and a wave of model announcements across the industry ([Windows Report](https://windowsreport.com/microsoft-shares-the-dates-for-its-build-2026-developer-conference/)).

This resembles the pattern AWS went through in 2011–2013, when a series of EBS, EC2, and data-center incidents accompanied its own rapid scaling ([Data Center Knowledge, AWS outage history](https://www.datacenterknowledge.com/outages/a-history-of-aws-cloud-and-data-center-outages)): rapid growth, new infrastructure, growing dependencies, periodic incidents. The answer then was resilient architecture. The answer is the same now.

Claude is excellent. It is also a single point of failure if you let it be. The outages are not a reason to stop using it — they are a reason to use it the same way you use any other critical infrastructure dependency.

---

*The Anthropic status page is at [status.claude.com](https://status.claude.com/) (status.anthropic.com now redirects there). The Cloudflare AI Gateway article on this site covers one implementation path for gateway-level routing.*
