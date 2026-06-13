---
title: "MiniMax M3: New Architecture, 1M Context, Open Weights — What Builders Need to Know"
date: 2026-06-03
description: "MiniMax M3 launched June 1 with a rebuilt attention mechanism (MSA), a 1M token context window, and 59.0% on SWE-Bench Pro. Open weights arrive on HuggingFace within days. But benchmark caveats matter — here is what builders should verify before committing."
og_description: "MiniMax M3 (June 1, 2026): MSA architecture cuts compute to 1/20th at 1M tokens, 9x faster prefill, 15x faster decoding. 59.0% SWE-Bench Pro. API on OpenRouter at ~$0.30/M input. Open weights coming to HuggingFace. Builder guide to the architecture, benchmark caveats, license risk, and when it makes sense."
content_type: "Builder's Log"
categories: ["AI Models", "Open Source AI", "AI Infrastructure"]
tags: ["minimax", "open-weights", "long-context", "msa-architecture", "agent-models", "openrouter", "swe-bench", "coding", "chinese-ai", "builders-log"]
---

On June 1, MiniMax released M3 — their first model built on a completely new attention architecture rather than the Sparse MoE foundation that defined the M2.x line. The headline claims are competitive: 1M token context, 59.0% on SWE-Bench Pro, and inference speeds that make the 1M window usable in production rather than theoretical.

---

**Update — June 14, 2026:**

- **Open weights shipped.** Weights are now available at [huggingface.co/MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3) and via Ollama (`ollama pull minimax-m3`). Technical report also published.
- **Promo pricing ended June 8.** Standard rate is now **$0.60/M input, $2.40/M output** for calls up to 512K tokens. Long-context calls (>512K input) are billed at ~4x the standard rate: approximately **$2.40/M input, $9.60/M output**. The OpenRouter listing confirms tiered pricing — factor the jump into any cost projection that approaches or exceeds the 512K threshold.
- **Independent benchmark: 80.5% SWE-bench Verified.** Third-party evaluations place M3 at 80.5% on SWE-bench Verified — a meaningful upgrade from the launch claim of 59.0% on SWE-Bench Pro (different benchmark variant). For comparison, Claude Opus 4.8 scores 88.6% on the same benchmark. The gap is real but M3 at 80.5% is solidly in the competitive range for most coding pipelines.
- **Baseline caveat confirmed.** MiniMax compared M3 against Claude Opus 4.7 in launch materials. By the time M3 shipped, Anthropic had already released Opus 4.8. The coding gap vs. current-generation Claude is wider than MiniMax's stated comparison suggests.
- **License:** Available on the HuggingFace model card — verify commercial use terms before committing to self-hosted deployment, especially given the M2.7 license tightening precedent.

---

This is the full breakdown: what M3 actually is, why the architecture change matters, what the benchmark claims mean and where to be skeptical, how to access it, and who should care.

---

## The Architecture Shift: From Sparse MoE to MSA

The M2.x series — M2, M2.1, M2.5, M2.7 — all shared a core architecture: 229 billion total parameters with 10 billion active, using Sparse Mixture of Experts (SparseMoE) with 256 experts and 8 activated per token. The approach was solid. M2.5 earned a [4.5/5 in our review](/reviews/minimax-m2-5-open-weight-agentic-llm-review/) for reaching frontier-adjacent benchmark performance at competitive pricing.

M3 is built on something different: **MiniMax Sparse Attention (MSA)**.

MSA is a new attention mechanism designed specifically for long-context inference efficiency. The key claim from MiniMax's technical announcement:

| Metric | Improvement over prior gen |
|---|---|
| Compute at 1M token context | 1/20th the cost |
| Prefill speed | 9x faster |
| Decoding speed | 15x faster |
| Context window | 1M tokens |

The prior gen in question is the M2.x SparseMoE architecture. At 1M tokens, standard attention has a quadratic scaling problem — compute and memory requirements blow up. MiniMax's claim is that MSA solves this through selective attention, processing only the most relevant token relationships rather than computing all-pairs attention at full scale.

MiniMax has not released the full technical paper as of launch, so the exact mechanism of MSA is not independently verifiable yet. What matters for builders right now is the practical claim: **at 1M token context, M3 is supposed to be fast and affordable to run, not just theoretically capable of handling long inputs**.

---

## Benchmark Position

MiniMax claims **59.0% on SWE-Bench Pro** — the harder variant of the coding benchmark that tests against professional-grade software engineering tasks.

For comparison:
- Claude Opus 4.6: ~80.8% SWE-Bench Verified (different benchmark variant)
- MiniMax M2.7: 56.22% on SWE-Pro
- MiniMax M2.5: ~78% on SWE-Bench Verified

The 59.0% represents a step up from M2.7's 56.22% on the same benchmark. That's meaningful progress — M2.7 actually *regressed* on SWE-Bench Verified compared to M2.5, making M3's improvement directionally important.

**Caveats that matter:**

MiniMax ran their benchmarks on their own infrastructure with agent scaffolding. This is a known confounder in agentic coding benchmarks: the scaffolding, retry logic, and tool-calling setup can materially affect scores. Independent third-party reproduction is pending. The 59.0% should be treated as a claim to verify, not a confirmed number.

MiniMax also claims M3 beats GPT-5.5 and Gemini 3.1 Pro on coding benchmarks. These claims require independent verification. GPT-5.5 has been independently benchmarked extensively; if M3 does outperform it on coding tasks, that will show up in the Artificial Analysis and LMSYS Chatbot Arena data within a few weeks of launch.

---

## Why M2.x History Matters for M3 Evaluation

MiniMax's model quality has been real, but their release practices have been inconsistent in ways that affect builder trust:

**M2.5** (February 2026): Strong 80.2% SWE-Bench Verified, Modified MIT license, genuinely competitive pricing. Well-received.

**M2.7** (March 2026 API, April 2026 weights): Self-evolution training claims, but SWE-Bench Verified *regressed* to 78%. License shifted from MIT to commercial-authorization-required — meaning commercial use requires written permission from MiniMax. Community called it faux open-source. Input price doubled from $0.15 to $0.30/M.

**M3** launches into this context. Builders who built pipelines on M2.5 expecting MIT-style openness were burned by M2.7's license change. The license terms for M3 have not been announced as of this writing.

---

## The License Question

This is the critical unknown at launch.

MiniMax has not published M3's license terms. The progression from M2.5 (Modified MIT) to M2.7 (commercial-authorization-required) created real friction for teams that had committed to open-weight flexibility. Before building on M3 for commercial use, verify the license on the HuggingFace model card when weights release.

Specifically, check:
- Is commercial use permitted without written authorization from MiniMax?
- Are there restrictions on fine-tuning and redistribution?
- Does it permit deployment via third-party inference providers?

If M3 ships with terms similar to M2.7, teams that need genuine open-weight flexibility for self-hosted commercial deployment should wait for independent assessment before committing to the stack.

---

## Access Paths

**OpenRouter (available now)**

M3 is live on OpenRouter with promotional pricing at approximately **$0.30/M input tokens**. This is OpenRouter's 50% promotional rate — standard pricing will be higher once the promo period ends. OpenRouter provides an OpenAI-compatible API endpoint, so integration into existing pipelines requires only changing the base URL and model name.

For builders who want to evaluate M3 quickly without infrastructure overhead, OpenRouter is the starting point.

**HuggingFace (weights releasing in ~10 days from June 1)**

MiniMax has committed to releasing weights within approximately 10 days of API launch — targeting around June 10-11, 2026. Self-hosting requires substantial GPU infrastructure due to M3's parameter count (not yet publicly specified; M2.x was 229B total). The MSA architecture's efficiency claims apply most clearly at the 1M token context range — at standard context lengths, the architectural advantage is less pronounced.

**build.nvidia.com / NIM** — Not confirmed for M3. NVIDIA's NIM catalog includes third-party models from various providers; whether M3 appears there post-launch depends on MiniMax's partnership decisions.

---

## Competitive Positioning

| Model | SWE-Bench | Context | Input Cost | Open Weights | Standout |
|---|---|---|---|---|---|
| Claude Opus 4.8 | 88.6% Verified | 200K | $15/M | No | Best coding agents, deepest reasoning |
| MiniMax M3 | 80.5% Verified† | 1M | $0.60/M | Yes | Long-context efficiency, open weights |
| MiniMax M2.7 | 56.22% SWE-Pro | 200K | $0.30/M | Yes (restricted) | Self-evolution training |
| Gemini 3.5 Flash | Strong agentic | 1M | $1.50/M | No | 4x speed, GA stability |

†Independent third-party evaluation; MiniMax's own launch figure was 59.0% on SWE-Bench Pro (different benchmark variant, self-reported).

The clearest M3 advantage is the combination of **1M token context + $0.30/M pricing**. Gemini 3.5 Flash offers similar context but at 5x the input cost. Claude Opus 4.6 has a 200K limit and costs 50x more per token. If MiniMax's speed claims for MSA at 1M context hold up, M3 becomes a serious candidate for any pipeline that needs to process long documents, large codebases, or extended conversation histories at scale.

---

## Who Should Evaluate M3 Now

**Strong candidates:**

- Teams building **RAG or agent pipelines on long documents** — legal, research, codebase analysis — where 1M context and $0.30/M pricing changes the economics meaningfully
- Teams already using **MiniMax M2.5 or M2.7** who want to see if M3's improved SWE-Pro score and new architecture upgrade their pipeline performance
- Teams evaluating **open-weight alternatives** who are waiting for Nemotron 3 Ultra's June 4 launch and want a comparison point

**Should wait:**

- Teams that need **commercial-use clarity** — hold until the HuggingFace model card confirms license terms
- Teams that need **independently verified benchmarks** — the 59.0% SWE-Pro claim needs third-party reproduction before it should influence production decisions
- Teams that need **stable, managed infrastructure** with SLAs — M3 is new and OpenRouter pricing is promotional; long-term cost projections are uncertain

---

## What to Watch

**June 1–11:** Independent benchmarks from Artificial Analysis, LMSYS, and community evaluations. These will confirm or complicate MiniMax's 59.0% SWE-Bench Pro claim.

**~June 10–11:** Weights release on HuggingFace. License terms will become visible at that point — check the model card before committing to M3 for commercial self-hosted use.

**June 4:** Nemotron 3 Ultra launches on the same date range. The two models compete on similar ground: open weights, 1M context, agent-optimized training. Benchmark comparisons between them will clarify where each has an edge.

We will update this guide when weights land and independent benchmarks are available.

---

*We research models; we do not test or deploy them directly. Benchmark data in this article is sourced from MiniMax's official announcement, OpenRouter's model listing, and third-party coverage as of June 3, 2026.*
