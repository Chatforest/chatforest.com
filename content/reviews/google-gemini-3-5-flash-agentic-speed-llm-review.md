---
title: "Google Gemini 3.5 Flash Review — Flash-Tier Speed, Pro-Tier Agentic Performance"
date: 2026-05-21
description: "Google Gemini 3.5 Flash launched at Google I/O 2026 on May 19 as the first Flash-tier model to lead Pro-tier models on agentic benchmarks. It tops MCP Atlas (83.6%), MMMU-Pro, CharXiv Reasoning, and Finance Agent v2 while running at 289 tok/s — four times the speed of competing frontier models. We cover the launch, benchmarks, pricing, hallucination rate, limitations, and where Gemini 3.5 Flash fits against GPT-5.5 and Claude Opus 4.7."
tags: ["llm", "multimodal", "agentic", "google", "speed", "frontier-models", "thinking-models", "long-context", "api"]
categories: ["reviews"]
rating: 4
author: "ChatForest"
last_refreshed: 2026-05-26
---

Google launched **Gemini 3.5 Flash** at Google I/O 2026 on May 19, 2026, and the positioning is direct: this is not a Pro model with Flash's name on it, and it is not a Flash model trimmed for price. It is an argument that the Flash tier has grown up.

The specific claim is that Gemini 3.5 Flash — a Flash-tier model — now leads Pro-tier competitors from OpenAI and Anthropic on multiple agentic benchmarks. It tops MCP Atlas at 83.6%, outperforms Claude Opus 4.7 by 4.5 points and GPT-5.5 by 8.3 points on that benchmark. It leads Finance Agent v2, Toolathlon, MMMU-Pro, and CharXiv Reasoning. It does this at 289 tokens per second — four times faster than competing frontier models — and at $1.50/$9.00 per million input/output tokens, substantially below Pro-tier pricing from either competitor.

The counterclaim is also true: Gemini 3.5 Flash trails on SWE-Bench Pro (Opus 4.7 leads), on ARC-AGI-2 (GPT-5.5 leads at 84.6%), and on coding tasks where its own upcoming Pro sibling outperforms it by roughly ten points. It also carries a 61% hallucination rate — improved from Gemini 3 Flash's 92%+ but behind the hallucination leaders.

This review covers the launch, benchmarks, pricing, the hallucination picture, developer experience, safety results from the model card, and where Gemini 3.5 Flash fits in the 2026 production routing landscape.

For context on earlier models in this lineage, see our [Gemini 3 Flash review](/reviews/google-gemini-3-flash-llm-review/) and [Gemini 3.1 Pro review](/reviews/google-gemini-3-1-pro-llm-review/).

---

## The Launch

Google announced Gemini 3.5 Flash on **May 19, 2026**, at the Google I/O 2026 keynote. Unlike Gemini 3.1 Pro — which launched in preview and remained there through May 2026 — Gemini 3.5 Flash launched directly to **general availability**.

Availability at launch:

- **Gemini API** (developer access via Google AI Studio)
- **Google AI Studio** (free tier access available)
- **Google Antigravity 2.0** (Google's agent platform; 3.5 Flash is 12x faster here than prior models)
- **Gemini app** (paid subscribers: Google AI Pro and Ultra)
- **GitHub Copilot** (GA as of May 19, 2026)
- **AI Mode in Google Search** (rolling out)

The GA launch is meaningful. Gemini 3.1 Pro's preview instability — sustained 503/504 errors and latency spikes above 100 seconds through April and May 2026 — was a documented friction point for developers. Gemini 3.5 Flash shipping at GA removes that risk for teams that cannot tolerate preview-grade reliability.

Google I/O 2026 also announced several adjacent products: **Gemini Spark** (a 24/7 personal AI agent), **Managed Agents API** on the Agent Platform for hosted custom agents, and the **Antigravity 2.0** desktop agent built directly on Gemini 3.5 Flash. Gemini 3.5 Flash is the engine behind Google's agentic platform push this cycle. A Gemini 3.5 Pro is in internal testing and slated to ship next month.

---

## Benchmark Overview

The primary story in Gemini 3.5 Flash's benchmark profile is the **MCP Atlas** result: 83.6%.

MCP Atlas tests MCP-orchestrated multi-step tool use — a direct measure of how well a model performs as an agent calling external tools across multi-step workflows. It is one of the most relevant agentic benchmarks for teams building on MCP. Gemini 3.5 Flash leads the full reported field on this benchmark — including Claude Opus 4.7 (Pro tier) at ~79.1% and GPT-5.5 (Pro tier) at ~75.3%.

| Benchmark | Gemini 3.5 Flash | Claude Opus 4.7 | GPT-5.5 |
|---|---|---|---|
| MCP Atlas | **83.6%** | ~79.1% | ~75.3% |
| MMMU-Pro (multimodal) | **83.6%** | — | ~81.2% |
| CharXiv Reasoning | **84.2%** | — | — |
| Finance Agent v2 | **leads** | — | — |
| Toolathlon | **leads** | — | — |
| Terminal-Bench 2.1 | 76.2% | — | **78.2%** |
| ARC-AGI-2 | 72.1% | ~75.8% | **84.6%** |
| SWE-Bench Pro | trails | **leads** | — |
| Speed (tok/s) | **289** | ~71 | ~68 |

### The Agentic Performance Argument

The benchmark table above is the core of Google's I/O 2026 narrative: a Flash-tier model is leading on agentic and multimodal benchmarks against Pro-tier models. The headline is accurate. The important caveat is what it means.

Flash models have historically been optimized for speed and cost, with capability secondarily. Gemini 3.5 Flash represents a repositioning: Google built it to lead specifically on agentic-task benchmarks (multi-step tool use, long-horizon task completion, MCP orchestration) while accepting capability gaps in other areas. The 4x speed advantage is not incidental — it is the model's practical value proposition for agent loops that chain many model calls.

### Where GPT-5.5 Wins: ARC-AGI-2 and Terminal-Bench

GPT-5.5 leads ARC-AGI-2 at 84.6% versus Gemini 3.5 Flash at 72.1%. ARC-AGI-2 is a test of abstract reasoning designed to resist pattern recall — it measures novel reasoning rather than trained task performance. Gemini 3.5 Flash's 72.1% is a significant result for a Flash model; GPT-5.5's lead here is meaningful for teams where general reasoning quality is the primary metric.

On Terminal-Bench 2.1 (CLI-style terminal automation), GPT-5.5 leads at 78.2% versus 76.2% for Gemini 3.5 Flash — a small gap, statistically close.

### Where Claude Opus 4.7 Wins: Coding

On SWE-Bench Pro — production-scale agentic coding tasks across real repos — Claude Opus 4.7 maintains a lead. The exact Gemini 3.5 Flash score is not published as of this review, but Google acknowledges that 3.5 Flash trails its own upcoming Pro model by approximately ten points on coding benchmarks. For teams running software engineering agents, Claude Opus 4.7 remains the better production choice.

### Artificial Analysis Intelligence Index: Fifth Place

Gemini 3.5 Flash places **fifth** on the Artificial Analysis Intelligence Index as of May 2026. The Index is a composite of intelligence, accuracy, and calibration weighted together. Fifth is a legitimate frontier-model result — there are fewer than ten models in that range. However, it is below Gemini 3.1 Pro (which places higher), and below GPT-5.5 and Claude Opus 4.7 on the overall composite. The agentic benchmark leadership does not translate directly to an Intelligence Index lead.

---

## The Hallucination Picture

Gemini 3.5 Flash carries a **61% hallucination rate** on the Artificial Analysis hallucination measure.

The trajectory is meaningful: Gemini 3 Flash measured at 92%+ on this metric. A 31-point improvement generation-over-generation is a real signal that Google's post-training work is producing measurable gains in factual reliability.

The absolute number, however, requires honest framing. The hallucination leaders in the May 2026 field — MiMo-V2.5-Pro and Grok 4.3 (high) — both sit at approximately 25%. Gemini 3.5 Flash at 61% is a materially higher hallucination rate than those models.

For comparison:

| Model | Hallucination Rate (AA) |
|---|---|
| MiMo-V2.5-Pro | ~25% |
| Grok 4.3 (high) | ~25% |
| Claude Opus 4.7 | 36% |
| **Gemini 3.5 Flash** | **61%** |
| Gemini 3 Flash | ~92% |

The practical implication: Gemini 3.5 Flash is substantially improved from its predecessor and viable for a wide range of agentic tasks where hallucination is a manageable risk (retrieval, summarization, structured extraction). For high-stakes professional workflows where a confident wrong answer is worse than no answer — legal, medical, financial, compliance — the 61% rate warrants caution. Claude Opus 4.7 at 36% is the better choice for those workloads.

---

## Context Window and Modalities

Gemini 3.5 Flash accepts up to **1,048,576 input tokens** (~1M tokens, approximately 1,500 pages) with a maximum **65,536 output tokens**. This matches the 1M context window available in Gemini 3.1 Pro and is consistent with 2026 frontier-model expectations.

**Supported inputs:**
- Text, images, audio, video — all accepted in a single prompt
- PDFs and code repositories

**Output:** text only. Gemini 3.5 Flash does not generate images, audio, or video natively.

**Limitations:**
- **Computer Use not supported** — for Computer Use workloads, Google directs users to continue using Gemini 3 Flash Preview.
- **Image segmentation not supported** — for segmentation tasks, Gemini 2.5 Flash (thinking off) remains the recommended option.

These are genuine workflow constraints. Teams evaluating Gemini 3.5 Flash for multimodal agent pipelines that include screen capture analysis, UI automation, or image segmentation should test capability coverage before migrating from Gemini 3 Flash Preview.

---

## Reasoning and Thinking

Gemini 3.5 Flash uses dynamic chain-of-thought reasoning via a **`thinking_level` parameter**. Google explicitly recommends using `thinking_level` rather than `thinking_budget` for this model — the budget-based API from prior models has been superseded.

Available levels:
- **low** — minimal reasoning, lowest latency and cost
- **medium** — intermediate reasoning
- **high** — deeper chain-of-thought; the configuration used in most public benchmark results
- **max** — maximum effort

Dynamic thinking is **on by default**. The model automatically scales reasoning depth to task complexity when no level is specified.

The benchmark results reported publicly — MCP Atlas 83.6%, CharXiv Reasoning 84.2%, etc. — generally use the **high** thinking configuration. Teams benchmarking against published numbers should ensure they are running the same configuration. Lower thinking levels will produce meaningfully different latency, cost, and capability profiles.

---

## Pricing

| Tier | Input (per 1M tokens) | Output (per 1M tokens) | Cache reads |
|---|---|---|---|
| Standard (global) | **$1.50** | **$9.00** | $0.15 |
| Non-global regions | $1.65 | $9.90 | — |

**Comparative context:**
- Gemini 3 Flash: $0.50 input / $3.00 output — Gemini 3.5 Flash costs **3x more** than its predecessor
- Gemini 3.5 Flash is priced substantially below Pro-tier models from OpenAI and Anthropic
- At 289 tok/s throughput, cost-per-task (rather than cost-per-token) can be lower in agent loops where wall-clock time matters

Google claims enterprise teams running high-volume agentic workflows at competitor Pro-tier pricing can save over $1 billion annually by switching to Gemini 3.5 Flash. That number is marketing arithmetic — it assumes volume and identical capability — but directionally, the price-performance gap for agentic workloads is real.

The 3x price increase over Gemini 3 Flash is the counterpoint. Teams that built cost models around Gemini 3 Flash pricing will need to revisit those assumptions. The capability improvement is substantial, but the price increase is not trivial.

**Consumer subscriptions** *(updated May 26, 2026 per Google I/O 2026 restructuring)*:
- Google AI Pro (~$19.99/month, formerly Gemini Advanced): includes Gemini 3.5 Flash
- Google AI Ultra $100/month (new tier, announced I/O 2026): includes Gemini 3.5 Flash, 5× Pro usage limits, 20 TB storage, YouTube Premium, priority Antigravity access
- Google AI Ultra $200/month (formerly $250/month): includes Gemini 3.5 Flash, 20× Pro usage limits, Gemini 3.5 Pro preview access
- Free tier: Gemini 3 Flash; not Gemini 3.5 Flash

---

## Safety

Google published a model card for Gemini 3.5 Flash aligned with the Frontier Safety Framework (FSF). No Critical Capability Levels were reached.

Domain results from the model card:

**CBRN:** No alert threshold reached. Factual accuracy on domain questions high, but novelty and uplift remain within evaluated safe ranges.

**Cybersecurity:** Evaluated against standard challenge suites. The model shows improved performance over Gemini 3 Flash on the suite but did not reach the alert threshold. No unintended shortcut-finding behavior was noted (contrast with Gemini 3.1 Pro's model card, which flagged two instances of "hacking the test").

**Harmful Manipulation:** Not reached.

**Computer Use caveat:** Computer Use support is absent in Gemini 3.5 Flash at GA launch. Google's guidance to continue using Gemini 3 Flash Preview for those workloads suggests Computer Use evaluation may be a factor in the rollout timeline.

The model card is publicly available at Google DeepMind.

---

## Developer Experience and Context

Gemini 3.5 Flash is the first model in the Gemini 3.5 family. Google's naming signal — moving from 3.1 to 3.5 — marks a larger step than a point release. The 3.5 family is positioned around the agent deployment cycle that Google announced at I/O: Antigravity 2.0 (agent desktop app), Gemini Spark (24/7 personal agent), the Managed Agents API, and AI Mode in Search all ship on Gemini 3.5 Flash as their inference backbone.

**GA at launch** is the most significant operational benefit. Gemini 3.1 Pro's preview-period instability was a real friction point for production teams. Gemini 3.5 Flash shipping at GA means teams can build on it from day one without tolerating elevated error rates.

**GitHub Copilot integration** (GA May 19) makes Gemini 3.5 Flash available directly in the developer tool where many coding agent workflows already run, without requiring a direct Gemini API integration.

**Pricing increase vs. Gemini 3 Flash:** At 3x the per-token cost of its predecessor, teams that have been routing Gemini 3 Flash calls will see a cost jump. The capability gains are real, but workload-specific evaluation before migration is appropriate.

**Gemini 3.5 Pro is coming:** Google has confirmed internal use of Gemini 3.5 Pro with a public release slated for June 2026. Teams evaluating Gemini 3.5 Flash for coding-heavy or high-precision workloads may want to wait for Pro before committing to a migration path.

---

## AI Glasses: Audio-First, Fashion-Forward

The hardware announcement at I/O 2026 was **Android XR-powered intelligent eyewear**, developed with Samsung and fashion brands Warby Parker and Gentle Monster.

Google is calling them "audio glasses" rather than "smart glasses" — a deliberate framing to position them as fashionable accessories first, tech devices second. They integrate Gemini via voice commands for task handling, questions, and navigation.

The launch timeline is "this fall" for the audio glasses. Full Android XR capabilities — including spatial computing features — follow on a longer roadmap.

This is clearly a response to Meta's Ray-Ban glasses, which have outsold expectations and established "stylish AI glasses" as a real product category. Google's fashion brand partnerships suggest they've absorbed that lesson. But without a concrete launch date or hands-on access, the glasses remain a roadmap announcement.

---

## Who Should Use Gemini 3.5 Flash

**Strong fit:**
- MCP-based multi-agent systems where agentic benchmark performance is the primary criterion — Gemini 3.5 Flash leads MCP Atlas
- High-throughput agent pipelines where latency and token-level speed matter — 289 tok/s, 4x faster than frontier alternatives
- Multimodal pipelines (image, audio, video input) that do not require Computer Use or image segmentation
- Teams routing Pro-tier traffic today who want lower cost with competitive agentic capability

**Consider alternatives:**
- SWE-Bench Pro and high-precision agentic coding: Claude Opus 4.7 leads
- ARC-AGI-2 and abstract reasoning: GPT-5.5 leads at 84.6%
- High-stakes professional use cases requiring low hallucination rates: Claude Opus 4.7 at 36% vs. Gemini 3.5 Flash at 61%
- Computer Use and screen automation: Gemini 3 Flash Preview remains the recommended option
- Teams sensitive to cost versus Gemini 3 Flash: 3x price increase requires workload review

---

## Summary

Gemini 3.5 Flash is a genuine milestone: it is the first Flash-tier model to lead Pro-tier competitors on key agentic benchmarks. The MCP Atlas result (83.6%) is the headline, and it is earned on a benchmark that directly measures multi-step tool-use performance. The 289 tok/s throughput advantage is structurally meaningful for agent loops that chain many model calls.

The limitations are real and documented: 61% hallucination rate, no Computer Use support, a pending Pro model that will outperform it on coding, and a 3x price increase over Gemini 3 Flash. These are not dealbreakers for the workloads where Gemini 3.5 Flash is strongest — they are routing signals that help teams decide where it belongs in their stack.

For teams building MCP-orchestrated agents, multimodal pipelines, or high-throughput inference systems where agentic capability and speed are the primary criteria, Gemini 3.5 Flash is the best option from the Gemini family in May 2026 and competitive with the frontier at lower cost.

**Rating: 4/5** — Strong agentic performance and GA launch execution offset by the hallucination rate, missing Computer Use support, and the imminent Gemini 3.5 Pro that will raise the ceiling on what this family can do.
