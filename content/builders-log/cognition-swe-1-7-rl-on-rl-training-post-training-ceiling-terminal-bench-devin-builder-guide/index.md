---
title: "SWE-1.7: Cognition's RL-on-RL Training Lands at 81.5% Terminal-Bench — And Why You Can't Call It Directly"
date: 2026-07-09
description: "Cognition's SWE-1.7 challenges the post-training ceiling by stacking RL on an already-RL-trained model (Kimi K2.7). It scores 81.5% on Terminal-Bench 2.1 — below Opus 4.8 and GPT-5.5 but above Kimi K2.7 Code and Composer 2.5 — at a reported ~$1.97 per task. But it's only accessible through Devin, not via API."
tags: ["cognition", "devin", "swe-bench", "agentic-coding", "rl-training", "benchmarks", "model-comparison", "july-2026"]
categories: ["builders-log"]
sources_audited: 2026-08-05
---

Cognition shipped [**SWE-1.7**](https://cognition.com/blog/swe-1-7) on July 8, 2026 — "the most capable model we've trained so far," in the company's own words, available today in Devin at 1,000 tokens per second via Cerebras. The headline is benchmark performance at a fraction of frontier cost. But the more interesting story is how they got there: reinforcement learning on top of a model that was already heavily RL-trained. That breaks with the conventional assumption that RL has a ceiling.

Here's what builders need to know.

---

## Where SWE-1.7 Sits in the July 2026 Model Landscape

The benchmark that matters for direct comparison is **Terminal-Bench 2.1**. Cognition's own release post puts SWE-1.7 against its own base model and its closest frontier competitors — not against Grok or Sonnet, which don't appear in Cognition's comparison at all:

| Model | Terminal-Bench 2.1 | Provider |
|---|---|---|
| Claude Opus 4.8 | 86.9% | Anthropic |
| GPT-5.5 | 84.2% | OpenAI |
| Claude Opus 4.7 | 83.0% | Anthropic |
| GLM-5.2 | 81.0% | Zhipu |
| **SWE-1.7** | **81.5%** | Cognition |
| Kimi K2.7 Code (base) | 72.7% | Moonshot AI |
| Composer 2.5 | 76.0% | Cursor |
| SWE-1.6 | 39.7% | Cognition |

*(All scores as self-reported in [Cognition's SWE-1.7 announcement](https://cognition.com/blog/swe-1-7).)*

SWE-1.7 lands just above GLM-5.2 and well above its own Kimi K2.7 Code base, Composer 2.5, and Cognition's prior model SWE-1.6 — but it's still behind Opus 4.7, GPT-5.5, and Opus 4.8. The story isn't "beats frontier models," it's "closes most of the gap to frontier models at a fraction of the cost."

Cognition's own **FrontierCode 1.1** benchmark, [also from the same release post](https://cognition.com/blog/swe-1-7), gives a fuller picture of agentic coding specifically:

| Model | FrontierCode 1.1 |
|---|---|
| Claude Opus 4.8 | 46.5% |
| GPT-5.5 | 43.0% |
| **SWE-1.7** | **42.3%** |
| Kimi K2.7 Code (base) | 30.1% |
| Composer 2.5 | 25.6% |

SWE-1.7 sits 0.7 points behind GPT-5.5 and 4.2 points behind Opus 4.8. More strikingly, it's 12.2 points above its own starting point — the Kimi K2.7 Code base model it was trained on.

It also scores [**77.8% on SWE-Bench Multilingual**](https://cognition.com/blog/swe-1-7), Cognition's cross-language coding benchmark.

---

## The RL-on-RL Breakthrough

This is the technical claim worth taking seriously.

The conventional wisdom has been that once a base model is extensively RL post-trained, you approach a ceiling. Additional RL training on an already-RL-optimized model yields diminishing returns, partly because the model's entropy collapses — the policy becomes too deterministic and stops exploring new strategies.

**Kimi K2.7 Code** — [Moonshot AI's 1-trillion-parameter MoE model with 32 billion active parameters](https://www.kimi.com/resources/kimi-k2-7-code), [released as open weights on June 12, 2026](https://www.marktechpost.com/2026/06/12/moonshot-ai-releases-kimi-k2-7-code-a-coding-model-reporting-21-8-on-kimi-code-bench-v2-over-k2-6/) — had already undergone extensive RL post-training before Cognition touched it. That makes SWE-1.7 a direct test of whether additional RL training stacks.

The result: a 12.2-point jump on FrontierCode 1.1 over the base model. Cognition's own framing: "the large additional gains from our own training challenge the idea of a 'post-training ceiling' and suggest that [RL can push capabilities much further than previously believed](https://cognition.com/blog/swe-1-7)."

### How They Avoided Entropy Collapse

The key technical innovation is **entropy preservation** using top-p sampling with sampling distribution replay. During RL training, as the model improves, it tends to become overconfident — repeatedly choosing the same high-probability actions and losing the diversity that drives further learning. [Cognition's approach](https://cognition.com/blog/swe-1-7) replays the sampling distribution from earlier in training, keeping policy entropy high enough to keep learning.

### Self-Compaction for Long Agentic Tasks

Agentic coding tasks can run for hours. [SWE-1.7's training rollouts ran up to six hours](https://cognition.com/blog/swe-1-7) — far beyond what fits in a raw context window. Cognition solved this with **self-compaction**: the model periodically summarizes its own working state and picks up from that summary, using an alternating length penalty to drive efficient compression. This means SWE-1.7 can maintain coherent task progress across very long horizons without hitting context limits.

### Multi-Cluster Training Infrastructure

To run RL at this scale, [Cognition trained on clusters across three continents, shipped weight updates through object storage, and built fault tolerance so that hardware failures never stalled the run](https://cognition.com/blog/swe-1-7).

### Data Curation

[Cognition built an automated data-quality pipeline that runs each task through execution tests, filters out tasks with low learning signal, and hardens tasks against reward-hacking](https://cognition.com/blog/swe-1-7) — preventing the model from gaming its training rewards rather than learning genuine task completion.

---

## Cost: $1.97 Per Task

On FrontierCode's Main evaluation set, [Cognition reports SWE-1.7 costs roughly **$1.97 per task**](https://officechai.com/ai/cognition-releases-swe-1-7-says-it-is-close-to-frontier-performance-at-a-fraction-of-the-cost/) on average — a figure attributed to Cognition but presented as a chart data point in [their release post](https://cognition.com/blog/swe-1-7) rather than a plain-text price. Cognition frames this as advancing the cost-performance Pareto curve, meaning you'd pay significantly more per task with GPT-5.5 or Opus 4.8 for a small additional benchmark gain.

At 1,000 tokens/second via Cerebras, the model is also fast enough for interactive coding workflows rather than just batch background work.

---

## The Caveat Builders Need to Know

**SWE-1.7 is not an API model. You cannot call it directly.**

It's exclusively available through **Devin** — Cognition's agentic coding product (web, desktop, and CLI). This is a deliberate product decision: Cognition is not selling model API access, they're selling a coding agent service.

What that means for your stack:
- If you're already using Devin for agentic coding tasks, you get SWE-1.7 automatically — it's the new default model
- If you want to build agents with this architecture yourself, you need to wait for the techniques (RL-on-RL, self-compaction, entropy preservation) to appear in open-weights or API-accessible models
- Kimi K2.7 Code itself is open weights, so the base model is available — but SWE-1.7's trained weights are not

---

## What This Means for Builders Not on Devin

Even if you're not a Devin user, this release matters for a few reasons:

**The RL-on-RL insight will spread.** If Cognition's entropy preservation technique works, other labs will replicate it. Expect to see "extended RL post-training" appear as a differentiator in future model releases from Mistral, DeepSeek, and others working with open base models.

**Self-compaction is an architecture builders should watch.** The idea of a model that summarizes its own working state to extend effective task horizon is directly applicable to agentic system design — not just as a training technique but as an inference-time strategy. If you're building long-horizon agents today, you're doing a manual version of this with prompt engineering; future models may do it natively.

**Benchmark positioning matters.** SWE-1.7 at 81.5% Terminal-Bench makes the case that frontier-competitive agentic coding performance is no longer exclusive to the top-tier API models. If Cognition eventually opens an API (or if the techniques appear in open models), the competitive dynamics of the model routing market change.

---

## Bottom Line for Builders

SWE-1.7 is a legitimate technical achievement. The RL-on-RL result challenges conventional assumptions about post-training ceilings, the self-compaction technique is novel, and the Terminal-Bench position (81.5%, within a few points of GPT-5.5 and Opus 4.8) is credible at a claimed $1.97/task cost.

The access constraint is real: you get SWE-1.7 by using Devin, not by calling an API. If Devin fits your workflow, this upgrade is meaningful. If you're building directly on model APIs, track the techniques rather than the model.

---

*ChatForest covers AI model releases and builder implications as they happen. The benchmark data in this article is sourced from [Cognition's official SWE-1.7 announcement](https://cognition.com/blog/swe-1-7) and cross-referenced against [BenchLM.ai](https://benchlm.ai/models/swe-1-7).*
