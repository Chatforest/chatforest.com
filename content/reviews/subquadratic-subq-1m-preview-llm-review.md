---
title: "SubQ 1M-Preview Review: The First Subquadratic LLM, 12M Context, and Why Researchers Are Skeptical"
date: 2026-05-16T10:00:00+09:00
description: "SubQ 1M-Preview (Subquadratic, May 5, 2026) is the first commercial LLM built on a fully subquadratic architecture (SSA). 1M production context, 12M research context, 81.8% SWE-Bench Verified, linear O(n) scaling. $29M seed. OpenAI-compatible API. Researchers are demanding independent proof. Rating: 3/5."
og_description: "SubQ 1M-Preview: First commercial non-transformer LLM. SSA architecture, 1M context (12M research), 81.8% SWE-Bench, 50x cheaper than frontier at 1M tokens — but no technical report, unproven at scale, researchers skeptical. API ~$0.50/$1.50 per M tokens. Rating: 3/5."
card_description: "SubQ 1M-Preview (May 5, 2026) is the first commercial LLM built on a fully subquadratic architecture — SSA, Subquadratic Sparse Attention — where compute scales linearly with context length rather than quadratically. 1 million token production context window; 12 million token research context. 81.8% SWE-Bench Verified, 95.0% RULER @128K, 65.9% MRCR v2 (8-needle, 1M). Claims: 50× cheaper than frontier models at 1M tokens, 1,000× efficiency gain at 12M tokens. OpenAI-compatible API, ~$0.50/$1.50 per million input/output tokens. $29M seed from backers including investors in Anthropic, OpenAI, Stripe, and Brex. CEO Justin Dangel; CTO Alex Whedon (ex-Meta, ex-TribeAI). No technical report released. Weights not open. Prior subquadratic architectures (Mamba, RWKV, Hyena, BASED, RetNet, Kimi Linear) all hit the same wall at frontier scale. Rating: 3/5 — architecturally significant, claims compelling, but unproven at scale and demanding independent verification."
tags: ["llm", "non-transformer", "subquadratic", "long-context", "frontier-model", "architecture", "swe-bench", "startup", "api"]
categories: ["reviews"]
rating: 3
author: "ChatForest"
last_refreshed: 2026-05-23
---

**At a glance:** SubQ 1M-Preview, released May 5, 2026. Subquadratic Sparse Attention (SSA) — linear O(n) compute scaling. 1M token production context; 12M research context. 81.8% SWE-Bench Verified. ~$0.50/$1.50 per million tokens input/output. OpenAI-compatible API. No technical report released. Weights closed. $29M seed. Part of our **[AI Models & LLM reviews](/categories/ai-providers/)**.

---

"Not a transformer."

That is the core claim from Subquadratic, the Miami-based startup that launched on May 5, 2026, with $29 million in seed funding and a single mission: build the first commercial frontier LLM that does not rely on quadratic attention.

The headline number is the context window — 12 million tokens in the research configuration, and 1 million tokens in production availability. But the number is almost a distraction. The real story is about scaling law. If you can make attention compute grow linearly with context length instead of quadratically, then long-context AI becomes fundamentally different: cheaper, faster, and accessible at scales that are economically impossible with transformer architecture. That is the bet Subquadratic is making.

Whether they have actually pulled it off is, as of today, an open question. If those claims hold under independent scrutiny, SubQ is architecturally significant. If they don't, one community commenter called it perfectly: "AI Theranos." We're currently somewhere between those two poles.

---

## Company: Miami Startup, Research Pedigree Investors

Subquadratic launched in stealth and came out publicly on May 5, 2026. It is based in Miami, Florida — notable for being outside the San Francisco AI cluster that dominates frontier model development.

**CEO Justin Dangel** is a five-time founder with a track record in health tech, insurtech, and consumer goods. He has scaled companies to hundreds of employees, secured institutional backing, and navigated liquidity events — but his background is operations and growth, not AI research. That makes the pairing with the CTO essential.

**CTO Alex Whedon** is the technical half of the founding pair. He previously worked as a software engineer at Meta and served as Head of Generative AI at TribeAI, where he led over 40 enterprise AI implementations. He designed the SSA architecture at the core of SubQ and is the named researcher behind the efficiency claims.

The $29M seed round is notable for its investor composition: Javier Villamizar, Justin Mateen (Tinder co-founder, JAM Fund founder), Grant Gittlin of Lasagna, Jaclyn Rice Nelson of Coalition Operators, and several early investors in Anthropic, OpenAI, Stripe, and Brex. That last group matters — people who backed the current frontier labs are now backing an architecture that claims to supersede them. It signals at least a credible belief that the bet is well-reasoned.

Subquadratic has not committed to open-sourcing weights and has not yet released a full technical report, though one is described as forthcoming.

---

## Architecture: What Subquadratic Sparse Attention (SSA) Actually Is

Standard Transformer attention is O(n²) with sequence length. This is not a design choice that could easily have been made differently — it reflects the fundamental operation of computing attention weights between every token and every other token. At 1 million tokens, this becomes prohibitively expensive. At 12 million, it is essentially impossible with current hardware.

Every prior attempt to solve this has made a version of the same trade-off: reduce the set of tokens each position attends to, accept that some information will be missed, and measure whether the resulting approximation is good enough for downstream performance. The approaches that have been tried include:

- **Mamba / S4 / State Space Models**: Replace attention with structured state space recurrence. Linear scaling. Underperformed transformers at scale on most downstream benchmarks.
- **RWKV**: Linear attention via kernel approximation. Competitive on some tasks; gap with transformers widened at larger scale.
- **Hyena, RetNet, BASED**: Variants on linear recurrence or kernel attention. Same pattern.
- **DeepSeek Sparse Attention**: Sparse transformer hybrid. Linear scaling in specific regimes.
- **Kimi Linear**: Linear attention in Moonshot AI's architecture. Still in hybrid configuration.

The pattern across all of these is discouraging: demonstrate linear scaling on benchmarks, show competitive results at small to medium scale, then underperform vanilla attention at frontier scale — or end up in hybrid configurations that preserve transformer attention for the critical attention heads and only achieve linear scaling on a subset.

Subquadratic's SSA is described as **content-dependent routing**: the model decides where to look based on meaning rather than position. Relevant information can be retrieved regardless of where it appears in the sequence. The company claims this avoids the degradation at scale that has plagued prior approaches, because the routing is semantically driven rather than structurally constrained.

The 7.2× prefill speedup over dense attention at 128,000 tokens (rising to 52.2× at 1 million tokens) is the efficiency claim in concrete terms. These are hardware-level numbers, not just theoretical — they reflect actual inference timing on the production system. The company also claims approximately **1,000× efficiency reduction** at the full 12 million token context window, compared to an equivalent transformer.

---

## Context Window: 1M Production, 12M Research

The practical context window for API users is **1 million tokens**. This matches the largest available windows from Gemini 3.1 Pro. In production use, 1M tokens is the relevant number.

The **12M token context** is Subquadratic's research configuration — tested and validated in the company's internal evaluations, but not currently the default API offering. Whether the full 12M context window works in practice for downstream tasks (rather than just technically processing input) is not independently verified. Subquadratic's long-context benchmark scores (65.9% on MRCR v2 at 1M) suggest functional retrieval at the production context size. Subquadratic has indicated a **50M token target for Q4 2026** — if reached, the context window stops resembling a limit and starts resembling unlimited memory.

---

## What They Launched

The May 5, 2026 launch included three products, all in private beta:

**SubQ API** — The production version exposes a 1 million token context window. The research version extends to 12 million tokens, but that isn't in the public beta. The $29M seed is in part designed to train the production 12M model.

**SubQ Code** — A CLI coding agent built on SubQ, compatible with Claude Code, Codex, and Cursor. It targets the full-codebase-in-context use case: load an entire repository, all its history, and all its documentation into a single call.

**SubQ Search** — A free long-context research tool using SubQ as the backend.

Access to all three is currently **waitlist-only** at subq.ai, with no announced general availability date.

---

## Benchmarks: What They Show and What They Don't

**SWE-Bench Verified: 81.8%**

This is SubQ's headline benchmark. SWE-Bench Verified measures the model's ability to resolve real GitHub issues in open-source software repositories — it is the closest available proxy for practical coding capability, and the leaderboard is competitive.

81.8% on SWE-Bench Verified puts SubQ in the conversation with the top frontier models. Claude Opus 4.6, GPT-5.5, and Gemini 3.1 Pro cluster in the 70–85% range on this benchmark. If SubQ's score is valid, it is competitive.

Two caveats apply, both noted by Subquadratic itself:
1. Each model was run only **once** on the benchmark suite, due to high inference cost. Standard practice is multiple runs to account for variance; single-run scores have wider error bars.
2. The margin is, in the CTO's words, "harness as much as model." SWE-Bench results are sensitive to scaffolding and prompt engineering; different harness configurations can move scores several percentage points.

**RULER @128K: 95.0%**

RULER (Realistic Uniform Long-context Evaluation for Retrieval) at 128K tokens is a needle-in-a-haystack style long-context benchmark. 95.0% is a strong score and indicates the model retrieves relevant information reliably at that context length.

**MRCR v2 (8-needle, 1M): 65.9%**

MRCR v2 at 1 million tokens with 8 needles is a harder test — multi-needle retrieval at maximum context. 65.9% is solid; it demonstrates the model actually functions at the 1M context window rather than degrading to near-random performance. This score was independently verified by a third party, which is the single most credibility-boosting data point in the launch.

**What is missing**: Standard reasoning benchmarks (GPQA Diamond, MATH, MMLU), knowledge benchmarks, and multimodal evaluations are not included in the public technical materials. The benchmarks Subquadratic released are well-suited to showing their architecture's strengths — long-context and coding. The absence of broader evals makes it hard to assess whether SSA generalizes or excels only in the specific regimes it was optimized for.

---

## The Researcher Skepticism Case

The VentureBeat headline upon launch was blunt: *"Miami startup Subquadratic claims 1,000x AI efficiency gain with SubQ model; researchers demand independent proof."*

Reaction from the AI research community split almost immediately. The **skeptical case**, articulated most sharply by AI engineer Will Depue: SubQ is "almost surely a sparse attention finetune of Kimi or DeepSeek" — meaning the architecture may not be novel, and the model may be a fine-tuned adaptation of an existing open-source model rather than a from-scratch subquadratic training. If true, the efficiency gains would be much less than advertised, since the base model still encodes quadratic training costs. No rebuttal from Subquadratic has been published.

The **supportive case**, from AI researcher John Rysana: "The work is just subquadratic attention done well which is very meaningful for long context workloads — odds of it being BS are extremely low."

The legitimacy of the research direction is not in dispute. The question is whether this specific implementation achieves the scale and quality claimed. The third-party MRCR verification sits in the middle — it validates one performance claim on one benchmark, which is evidence but not proof.

---

## Why 12M Context Actually Matters

Setting aside the verification debate: if SubQ performs as claimed, what would 12M tokens change?

**For software engineering**: 12M tokens is approximately 10 million words. A large enterprise codebase — all source files, all commit history, all documentation — typically fits in 2–8 million tokens. A 12M context model means no chunking, no RAG, no retrieval pipeline. You put the entire codebase in and ask questions directly.

**For legal**: Full case file processing — discovery documents, contract portfolios, prior art archives — in a single call. Current workflows require splitting, chunking, and retrieval-augmented pipelines that introduce errors.

**For long-running agents**: Persistent state across months of interaction without any external memory or retrieval system. The context window itself becomes the memory.

**For research**: Entire literature corpora in context. Not a RAG index, but the actual papers.

None of this matters if the model can't reason well at general tasks, which is exactly what the missing benchmarks would show.

---

## API and Pricing

The SubQ API is live and available at subq.ai. It is OpenAI-compatible — you can use it as a drop-in replacement in any system that uses the OpenAI client library, by changing the base URL.

**Reported pricing**: ~$0.50 per million input tokens, ~$1.50 per million output tokens. These figures circulate in independent coverage but are not currently listed in a clear public pricing page, which is worth noting for planning purposes.

**Inference speed**: 150+ tokens per second reported.

If the cost claims hold, the value proposition for long-context workloads is dramatic: tasks that reportedly cost $2,600 on Claude at 128K context reportedly cost $8 on SubQ at comparable context lengths. Whether this holds as the product scales out of private beta is unknown. There is no free tier currently listed in public materials.

---

## How It Compares to Frontier Models

| | SubQ 1M-Preview | Claude Opus 4.6 | GPT-5.5 | Gemini 3.1 Pro |
|---|---|---|---|---|
| Architecture | SSA (subquadratic) | Transformer | Transformer | Transformer |
| Context (production) | 1M tokens | ~1M tokens | ~256K tokens | 1M tokens |
| SWE-Bench Verified | 81.8% | ~80–85% | ~78–83% | ~75–82% |
| Input price / M tokens | ~$0.50 | ~$15 | ~$10 | ~$2.50 |
| Open weights | No | No | No | No |
| Technical report | Not yet | Yes | Partial | Yes |

The pricing differential is striking — SubQ claims approximately 30× lower input price than Claude Opus 4.6 at equivalent context lengths. The caveat: "equivalent context lengths" is doing work here. Claude Opus 4.6 and GPT-5.5 have been evaluated extensively across a broader benchmark suite, and their quality at normal coding and reasoning tasks is well-established. SubQ has not yet published comparable breadth of evaluation.

---

## What Builders Should Do

**If you're building applications bottlenecked by context length or cost**, SubQ is worth getting on the waitlist for today. Even if the headline claims are partially inflated, a model that delivers competitive RULER and SWE-Bench scores at 1/10th the cost of frontier models has real value.

**If you're evaluating SubQ for production use**, wait for three things: an independent efficiency benchmark (not just the vendor-run numbers), a peer-reviewed paper with the architecture details, and general reasoning evaluations (MMLU/GPQA class). Without those, the risk of architectural surprises in production is real.

**If you're a researcher**, the SSA approach — content-dependent sparse exact attention — is an interesting direction worth tracking regardless of how SubQ's commercial story unfolds. The architectural direction is legitimate even if this specific implementation is debated.

---

## Verdict: Architecturally Significant, But Requires Independent Validation

SubQ 1M-Preview is the most architecturally interesting LLM release of early 2026. The claim — a fully subquadratic frontier model that doesn't hit the scaling wall — is exactly the kind of breakthrough that would meaningfully change the economics of long-context AI. The SWE-Bench score is competitive. The context window is real. The API is live.

The honest uncertainty is this: every prior subquadratic architecture has failed at frontier scale. That pattern doesn't guarantee SSA will fail, but it demands that the positive result be reproducible and independently verified before it is accepted as fact. The technical report's absence is the biggest open question — the efficiency claims are extraordinary, and extraordinary claims require extraordinary evidence.

For developers, the practical read is straightforward: the API is worth experimenting with for long-context coding tasks, especially if current frontier model costs are a constraint. At $0.50/$1.50 per million tokens with a 1M context window and a functional SWE-Bench score, there is genuine value here even if some of the headline claims prove overstated.

For researchers and AI-watchers: SubQ is the most compelling reason to revisit the subquadratic architecture question since Mamba. The difference this time is that it is a commercial deployment with live inference, not just a research paper — which means the empirical record will accumulate regardless of what the technical report says.

**Rating: 3/5** — Architecturally novel and commercially significant, with competitive long-context benchmarks and attractive pricing. Held back by the absence of a technical report, no open weights, limited benchmark breadth, and the historical track record of subquadratic architectures at frontier scale. Revisit when the technical report lands and independent evaluations are available.

---

*Subquadratic launched May 5, 2026. This review is based on public announcements, the SubQ API documentation, third-party coverage, and available benchmark data. ChatForest does not have hands-on API access and has not run independent evaluations.*
