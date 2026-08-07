# MiniMax M3 Pro: 2.7 Trillion Parameters, Open-Source Planned Q3 2026 — Builder Guide

> MiniMax is building M3 Pro, a 2.7 trillion parameter model planned for open-source release in Q3 2026. It would be the largest open-source model ever — six times larger than current M3. Here is what builders need to know now, and what to wait on.


On July 8, 2026, [The Information reported](https://thenextweb.com/news/minimax-2-7-trillion-parameter-open-source-model) that MiniMax is developing M3 Pro — a model with 2.7 trillion total parameters — and plans to release it as open source in Q3 2026, [as also covered by The Decoder](https://the-decoder.com/chinese-ai-startup-minimax-plans-to-open-source-a-2-7-trillion-parameter-model-later-this-year/). No formal MiniMax announcement followed. No architecture paper. No benchmark claims.

What exists is a single sourced report that sets a number. That number is significant enough to be worth understanding now, before the release, because it will affect decisions about open-source model strategy whether builders plan for it or not.

---

## The Number in Context

MiniMax M3, released June 1, has [428 billion total parameters and approximately 23 billion active parameters](https://huggingface.co/MiniMaxAI/MiniMax-M3) at inference (a Mixture-of-Experts architecture where each token activates a small fraction of the full model). Its [MSA (MiniMax Sparse Attention) architecture](https://arxiv.org/abs/2606.13392) — [detailed in MiniMax's own launch post](https://www.minimax.io/blog/minimax-m3) — was designed specifically to make 1M-token contexts computationally practical.

M3 Pro's reported figure — 2.7 trillion total parameters — puts it in a different category entirely:

| Model | Total Params | Active Params | Open Weights | Release |
|---|---|---|---|---|
| MiniMax M3 Pro | 2.7T (reported, unconfirmed by MiniMax) | Unknown | Planned Q3 2026 | Pre-release |
| [MiniMax M3](https://huggingface.co/MiniMaxAI/MiniMax-M3) | 428B | ~23B | Yes (HuggingFace) | June 2026 |
| [DeepSeek-V3](https://arxiv.org/abs/2412.19437) | 671B | ~37B | [Yes](https://huggingface.co/deepseek-ai/DeepSeek-V3) | Dec 2024 |
| [Meta Llama 4 Maverick](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) | 400B | ~17B | [Yes](https://huggingface.co/blog/llama4-release) | April 2025 |
| [Tencent Hy3](https://www.tencent.com/en-us/articles/2202386.html) | 295B | ~21B | [Yes (Apache 2.0)](https://technode.com/2026/07/07/tencent-launches-hunyuan-hy3-integrates-model-across-multiple-products/) | July 2026 |
| Claude Opus 4.8 | Unreported | Unreported | No | 2026 |
| GPT-5.6 Sol | Unreported | Unreported | No | July 2026 |

If M3 Pro ships as reported, it would be the largest open-source model ever released by a factor of approximately four — measured against DeepSeek-V3's 671 billion total parameters, the current largest open-weight release in this comparison.

---

## What the Parameter Count Does and Doesn't Tell You

2.7 trillion total parameters is a striking number, but for a MoE model, inference cost tracks active parameters — not total parameters. If M3 Pro uses a similar expert-activation ratio to M3 (approximately 5% active at any token), active parameters at inference would be in the range of 100–135 billion. That is roughly comparable to running a dense 100B model, not a 2.7T dense model.

This matters for several reasons:

**Hardware requirements**: A 2.7T dense model would need tens of petaflops of compute and hundreds of terabytes of memory to serve — practically impossible outside a hyperscaler. A 2.7T MoE model with ~100B active parameters needs roughly 30–40 GB of VRAM per inference slice at FP16, distributed across a multi-GPU array. Large, but self-hostable in principle.

**Benchmark potential**: MoE models at scale have repeatedly exceeded what their active-parameter count would predict on benchmarks. DeepSeek-V3 at 671B total/37B active [matched or exceeded GPT-4o on most published benchmarks](https://arxiv.org/abs/2412.19437) at launch, per [independent tracking](https://artificialanalysis.ai/models/deepseek-v3). M3 at 428B total/23B active is [scoring 80.5% on SWE-Bench Verified](https://huggingface.co/MiniMaxAI/MiniMax-M3), a figure the independent [SWE-bench Verified leaderboard](https://benchlm.ai/benchmarks/sweVerified) also lists. Scaling total parameters while maintaining efficient activation could produce a model that performs at frontier level while remaining self-hostable.

**The honest caveat**: MiniMax has not confirmed that M3 Pro uses MoE. They have not confirmed the active-parameter count. They have not confirmed the architecture. The 2.7T number is what was reported. Everything else is inference from M3's design pattern.

---

## Why MiniMax Is Building This

M3 Pro fits a pattern visible across Chinese AI labs in mid-2026: racing toward the largest possible open-weight model as a strategic differentiator from proprietary US labs.

MiniMax's logic is legible. M3 established that their MSA architecture scales efficiently to 1M tokens. M3 Pro would demonstrate that the same architecture scales to an unprecedented parameter count without requiring closed infrastructure to run. The combination — largest open-source model ever, designed for long-context efficiency, from a lab with a track record of actually releasing weights — is a meaningful market position if execution follows.

There is also a second-order effect. If M3 Pro matches or exceeds frontier proprietary model performance at large scale, it strengthens the argument for sovereign AI infrastructure — every government and enterprise that wants model control without proprietary dependency has a credible path. That is a market MiniMax is explicitly pursuing.

---

## The License Question (Critical Unknown)

MiniMax's licensing history should factor into any planning:

**M2.5** (February 2026): [Modified MIT](https://huggingface.co/MiniMaxAI/MiniMax-M2.5/blob/main/LICENSE-MODEL) — genuinely permissive commercial use, with an attribution requirement ([coverage](https://winbuzzer.com/2026/02/14/minimax-m25-open-source-ai-model-claude-opus-cost-xcxwbn/)).

**M2.7** (April 2026 weights): [Commercial-authorization-required](https://github.com/MiniMax-AI/MiniMax-M2.7/blob/main/LICENSE) — the license text requires "a separate, prior written authorization from MiniMax" for any commercial use, despite being labeled "Modified-MIT." [The developer community called it "faux open-source,"](https://finance.biggo.com/news/obI1i50Bga3fZL9MnP2D) arguing the restriction contradicts the license's own name.

**M3** (June 2026): Currently permissive for API access; [self-hosting license terms on the HuggingFace model card](https://huggingface.co/MiniMaxAI/MiniMax-M3) — a custom "minimax-community" license, not a standard OSI license — are the ground truth for commercial use.

**M3 Pro**: Unknown. No license has been announced or implied.

If M3 Pro ships with M2.7-style restrictions, "open-source" is a headline, not an operational fact. If it ships with genuinely permissive terms, it becomes the most significant infrastructure event in the open-source AI ecosystem to date.

Before building any pipeline assumptions around M3 Pro, wait for the HuggingFace model card and read the license. This is not optional due diligence — it is the most consequential unknown in the entire announcement.

---

## WAIC Watch: July 17–20

[The World Artificial Intelligence Conference opens in Shanghai on July 17, 2026](https://www.ecns.cn/hd/2026-07-17/detail-ihfhkrtk6178037.shtml), with [300+ global product debuts announced](https://www.globaltimes.cn/page/202607/1365377.shtml) and major Chinese AI labs expected to use it as a launch venue. MiniMax M3 Pro is an obvious candidate for a formal reveal. An official announcement at WAIC would likely include architecture details, benchmark claims, and potentially a firm release date within Q3.

Builders monitoring the open-source model landscape should watch WAIC coverage for any MiniMax M3 Pro specifics that turn an exclusive report into an official specification.

---

## What to Do Now vs. What to Wait On

**Do now:**

- If you are building long-context or agentic pipelines that currently use proprietary models for cost reasons, note M3 Pro's existence in your model-selection framework as a future evaluation candidate.
- Ensure your infrastructure can swap model backends without pipeline surgery — M3 Pro, if it performs, will be worth evaluating, and the cost of retrofitting model-agnostic routing is higher than building it in.
- Track The Information, AI Weekly, and MiniMax's official blog for architecture details as they emerge.

**Wait on:**

- Any concrete capacity planning for M3 Pro. Q3 2026 spans July–September. No firm date exists. The model does not exist publicly.
- Infrastructure investment predicated on specific M3 Pro performance. The model has never been benchmarked publicly.
- Any commercial commitment that depends on M3 Pro's license being permissive. That is unknown.
- Self-hosting hardware planning. Active parameter count — the number that determines GPU requirements — has not been confirmed.

The only decision worth making before the model is public: whether model-agnostic infrastructure is worth building into your current stack. The answer to that question does not depend on M3 Pro specifically. It depends on whether you expect the best available open-source model to change in the next six months. That is almost certainly yes regardless of M3 Pro's outcome.

---

## What to Watch Through Q3

**WAIC (July 17–20, Shanghai):** Likely venue for formal MiniMax announcement, if one comes before general release. Architecture specs, benchmark claims, and license terms could all emerge here.

**MiniMax blog and HuggingFace page:** Weight releases from MiniMax have historically arrived with a technical report. The model card will contain the license.

**Active-parameter confirmation:** The number that matters operationally. When MiniMax publishes an architecture document, the expert count and activation pattern determine whether self-hosting is feasible for mid-sized teams.

**Independent benchmarks:** MiniMax's self-reported benchmarks have been directionally useful but require third-party verification. For a model of this claimed scale, Artificial Analysis, Chatbot Arena, and SWE-bench evaluations will be the reliable data points.

We will update this when the official announcement or weight release occurs.

---

*We research models; we do not test or deploy them directly. Reporting in this article is based on [The Information's July 8, 2026 exclusive](https://thenextweb.com/news/minimax-2-7-trillion-parameter-open-source-model), subsequent coverage from [The Decoder](https://the-decoder.com/chinese-ai-startup-minimax-plans-to-open-source-a-2-7-trillion-parameter-model-later-this-year/) and [AI Weekly](https://aiweekly.co/alerts/minimax-preps-27t-parameter-m3-pro-for-q3-open-source-drop), and MiniMax's own published architecture documentation for M3.*

