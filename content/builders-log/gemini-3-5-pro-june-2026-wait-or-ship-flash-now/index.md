---
title: "Gemini 3.5 Pro Is Shipping in June — Should You Wait or Build on Flash Now?"
date: 2026-05-30
description: "Google confirmed Gemini 3.5 Pro ships 'next month' from I/O 2026 — which means some time in June. No model card, no benchmarks, no pricing. But Flash's launch already tells you most of what you need to know to make the build-now-or-wait decision."
tags: ["google", "gemini", "gemini-3.5-flash", "model-selection", "api-strategy", "production-ai", "cost-analysis", "agents", "reasoning"]
content_type: "Builder's Log"
categories: ["Model Analysis", "Google", "Developer Experience"]
draft: false
---

Google confirmed at I/O 2026 that Gemini 3.5 Pro ships "next month." That was May 19. We're now in the window.

There's no model card. No pricing. No benchmark sheet. No API endpoint in the docs. Google has been deliberately silent on specifics. But Gemini 3.5 Flash shipped on launch day with full documentation — and Flash was designed to be the fast tier of a two-model family. The gap Flash deliberately left open is exactly what Pro is built to fill.

Here's what builders can conclude now, before the GA announcement.

---

## What Flash Already Tells You About Pro

Gemini 3.5 Flash launched with a specific benchmark profile. It leads on:

- **MCP Atlas** (83.6%) — ahead of Claude Opus 4.7 by 4.5 points and GPT-5.5 by 8.3 points
- **Finance Agent v2** (57.9% vs 43.0% for Gemini 3.1 Pro)
- **MMMU-Pro** and **CharXiv Reasoning** — multimodal and chart-reasoning tasks
- **Toolathlon** — multi-step tool use

It trails on:

- **SWE-bench Pro** — Opus 4.7 leads here
- **ARC-AGI-2** — GPT-5.5 leads at 84.6%; Flash doesn't lead this benchmark
- **Coding tasks** where Google's own documentation notes Flash's Pro sibling "outperforms it by roughly ten points"

This is not a general Flash weakness — it's a deliberate architectural tradeoff. Flash was tuned for speed and agentic tasks. The hard reasoning benchmarks (ARC-AGI-2, abstract problem solving, deep coding) are the exact areas Pro is designed to recover.

Sundar Pichai's framing at I/O: Pro is for tasks requiring "sustained frontier performance." Flash is for tasks requiring "fast frontier performance." The distinction is real, not just marketing.

---

## The Pricing Math

Gemini 3.5 Flash is $1.50 per million input tokens and $9.00 per million output tokens.

Historical Gemini Pro-to-Flash pricing ratios have been roughly 3–4x on input (not 10x as some estimates suggest):

| Model | Input ($/M) | Output ($/M) |
|---|---|---|
| Gemini 3.1 Flash | $0.35 | $1.05 |
| Gemini 3.1 Pro | $1.25 | $5.00 |
| Ratio | ~3.6x | ~4.8x |
| Gemini 3.5 Flash | $1.50 | $9.00 |
| **Gemini 3.5 Pro (estimated)** | **~$5–8** | **~$25–45** |

No official pricing has been published. The 3.5 generation made a large jump at the Flash tier — pricing nearly tripled from 3.1 Flash. If Pro follows the historical ratio pattern (rather than a flat 10x), it lands at $5–8 input and $25–45 output.

That range matters: at the low end, Gemini 3.5 Pro is roughly price-competitive with Claude Opus 4.8 ($5/$25). At the high end, it's a premium product that competes on capability, not cost.

---

## The Benchmark Gap Pro Needs to Close

The clearest signal is this: Google explicitly told developers that Gemini 3.5 Flash underperforms Pro "by roughly ten points" on coding tasks. That's a real gap.

On ARC-AGI-2, Flash doesn't lead. GPT-5.5 posts 84.6% on that benchmark. For Pro to be positioned as Google's frontier reasoning tier, it needs to compete with or beat GPT-5.5 on abstract reasoning tasks — the harder end of the benchmark spectrum.

What this tells you: Pro is not "Flash with more compute." It's a different model tuned for a different job. Flash is architecture optimized for latency and tool chaining. Pro is architecture optimized for quality of output on hard problems.

---

## The Decision Framework

**Use Flash now if:**

- Your use case is agentic — tool use, MCP orchestration, multi-step pipelines, real-time response
- You're price-sensitive and the $1.50/$9 pricing fits your economics
- Latency matters (Flash runs at 289 tok/s; Pro will be slower)
- Your hardest tasks are workflow coordination and tool chaining, not deep reasoning
- You're building now and can't wait

Flash's benchmark lead on agentic tasks is not a "close second." It leads the category. If your agent runs tool calls and coordinates across systems, Flash is the right model today.

**Consider waiting for Pro if:**

- Your critical path involves hard reasoning: code generation for complex algorithms, mathematical problem solving, deep codebase understanding
- You need ARC-AGI-2-class abstract reasoning performance
- You're doing large-scale migrations or security audits where a wrong answer is more expensive than a slow one
- You're comparing against Claude Opus 4.8 (which leads SWE-bench Pro) and need a Google-native alternative with competitive pricing

**Architect for both now:**

The practical answer for most production systems is: route. Design your agent routing layer so Flash handles high-volume, latency-sensitive tasks and a reasoning-capable model (Pro, Opus 4.8, or GPT-5.5 Pro) handles hard planning steps.

If you're building that routing layer today, using Flash on the fast path and Opus 4.8 or GPT-5.5 on the reasoning path is a reasonable interim architecture. When Pro launches, swapping it in as a Google-native reasoning option is one configuration change.

---

## What to Watch For at Launch

When the Pro model card drops, the numbers that will determine whether it's worth switching:

1. **SWE-bench Pro score** — does it beat Opus 4.8?
2. **ARC-AGI-2 score** — does it beat GPT-5.5's 84.6%?
3. **Final pricing** — if it lands above $8/$40, it's competing on quality, not cost
4. **Context window** — Flash is 1M tokens; Pro is expected to match or exceed
5. **Batch and caching discounts** — Flash offers 90% batch discount; Pro pricing will affect economics for large-volume use cases
6. **Model ID** — expected `gemini-3.5-pro`; whether the GA version also shares an ID with the consumer app (as Flash does) matters for stability guarantees

The June 2026 window is crowded — Microsoft Build is June 2–3 and GTC Taipei keynotes June 1. Google may time the Pro announcement around one of these, or keep it quiet. Subscribe to the [Gemini API changelog](https://ai.google.dev/gemini-api/docs/changelog) if you want to catch it without the fanfare.

---

## The Short Version

Flash is production-ready today. It leads the agentic benchmark category and is available across Google AI Studio, Vertex AI, and Antigravity 2.0 with a stable model ID.

Pro is coming in June. No date. The gap it fills is hard reasoning — ARC-AGI-2, abstract problem solving, complex coding — at approximately 3–4x Flash's price.

If your workload is agentic coordination and tool use: build on Flash now.

If your workload requires frontier reasoning quality: wait two to four weeks and see what Google posts on the model card.

If you need both: start routing now, using what's available for the reasoning path while you wait for Pro pricing.

---

*For Flash benchmarks, pricing, and hallucination rate data, see our [Gemini 3.5 Flash review](/reviews/google-gemini-3-5-flash-agentic-speed-llm-review/). For comparisons against GPT-5.5 Instant on API deployment strategy, see [GPT-5.5 Instant vs Gemini 3.5 Flash](/builders-log/gpt-5-5-instant-vs-gemini-3-5-flash-api-consumer-launch-strategy/).*
