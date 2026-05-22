---
title: "SubQ: The First Subquadratic LLM Promises 12M Context and 1,000x Efficiency — But Can It Prove It?"
date: 2026-05-23
description: "Miami startup Subquadratic launched SubQ on May 5, 2026 with a $29M seed round, a 12-million-token context window, and claims of 1,000x efficiency over transformers. The architecture is legitimate. The benchmarks are narrow. The hype is enormous. Here's what builders actually need to know."
tags: ["subq", "subquadratic", "llm", "long-context", "architecture", "sparse-attention", "research", "ai-models", "context-window"]
rating: 3
---

## The Claim

On May 5, 2026 — the same day OpenAI quietly rolled out GPT-5.5 Instant as ChatGPT's new default — a Miami startup called **Subquadratic** announced something that the AI research community spent the rest of the week arguing about.

They launched **SubQ**: a language model built on a novel architecture called **SSA (Subquadratic Selective Attention)** that, they claim, scales nearly linearly with context length instead of quadratically. The result, they say, is a model that can handle a **12-million-token context window** and run at roughly **1/10th the cost** of comparable frontier models.

If those claims hold under independent scrutiny, SubQ is architecturally significant. If they don't, one commenter called it perfectly: "AI Theranos."

We're currently somewhere between those two poles.

---

## Why Quadratic Scaling Is the Central Problem

To understand what Subquadratic is actually claiming, it helps to understand what they're claiming to have solved.

Standard transformer attention — the mechanism inside GPT-5.5, Claude Opus 4.7, Gemini 3.5 Flash, and every major frontier model — scales **quadratically** with sequence length. Double the context window and you quadruple the compute. The math is straightforward: every token must attend to every other token, so for a sequence of length n, you perform n² attention operations.

This is why context windows, despite years of engineering effort, remained expensive at 100K–200K tokens for most of AI's recent history. It's not a training data problem or a hardware problem — it's the foundational math of the attention mechanism itself.

Several research directions have tried to address this:
- **SSMs (State Space Models)** like Mamba: process sequences with fixed-size state, O(n) scaling, but with tradeoffs in recall
- **Linear attention approximations**: approximate full attention with kernel tricks, losing precision
- **Sparse transformers**: compute attention over a fixed subset of positions, but statically

Subquadratic's SSA is none of these. They describe it as **content-dependent sparse exact attention**: the model dynamically learns, for each token, which other tokens are actually relevant — and then performs exact (not approximated) attention only over that sparse subset. The sparsity pattern isn't predetermined; it's chosen per-token based on the content.

The claimed result: at 1 million tokens, **52x faster than FlashAttention**. At 12 million tokens, roughly **1,000x fewer attention operations** than a dense transformer baseline.

---

## The Company

Subquadratic is based in Miami. The team that matters:

- **Justin Dangel, CEO** — leads the company and raised the round
- **Alex Whedon, CTO** — formerly Head of Generative AI at Meta, which lends real credibility to the technical claims

The **$29 million seed round** attracted some notable backers: Justin Mateen (Tinder co-founder), Javier Villamizar (ex-SoftBank Vision Fund), and early investors in Anthropic, OpenAI, Stripe, and Brex. The capital allowed them to train SubQ from scratch on their architecture rather than fine-tuning an existing model — a critical distinction for an architecture company, and a point of ongoing debate (more on that shortly).

---

## What They Launched

The May 5, 2026 launch included three products, all in private beta:

**SubQ API** — The production version exposes a **1 million token context window**. The research version extends to **12 million tokens**, but that isn't in the public beta. The $29M seed is in part designed to train the production 12M model.

**SubQ Code** — A CLI coding agent built on SubQ, targeting the full-codebase-in-context use case: load an entire repository, all its history, and all its documentation into a single call.

**SubQ Search** — A free long-context research tool using SubQ as the backend.

Access to all three is currently **waitlist-only** at subq.ai, with no announced general availability date.

---

## The Benchmarks

This is where SubQ's story gets complicated. The company published **three benchmarks** at launch:

| Benchmark | SubQ 1M-Preview | Comparison |
|---|---|---|
| RULER @ 128K | 95.0% | Claude Opus 4.6: 94.8% |
| SWE-Bench Verified | 81.8% | Claude Opus 4.6: 80.8% |
| MRCR v2 | 65.9% | (third-party verified) |

RULER is a long-context retrieval benchmark. SWE-Bench Verified is the canonical software engineering benchmark. MRCR v2 measures multi-turn long-context recall.

On its chosen benchmarks, SubQ is competitive with Claude Opus 4.6 — a frontier model that costs substantially more at long context. The **MRCR v2 score was independently verified by a third party**, which is the single most credibility-boosting data point in the launch.

But here's what's missing: **no general reasoning benchmarks**. No MMLU. No GPQA Diamond. No MATH. No GSM8K. No MMLU-Pro. The company published exclusively long-context and coding evals — the exact benchmarks where SSA's architectural advantages would be most apparent. The benchmarks where a weaker base model would be most exposed are absent.

The efficiency numbers — 52x at 1M tokens, ~1,000x at 12M — are **entirely vendor-run** and have not been independently reproduced. There is no peer-reviewed paper (the website says "paper coming soon"). The model weights have not been released.

---

## The Controversy

Reaction from the AI research community split almost immediately.

The **skeptical case**, articulated most sharply by AI engineer Will Depue: SubQ is "almost surely a sparse attention finetune of Kimi or DeepSeek" — meaning the architecture may not be novel, and the model may be a fine-tuned adaptation of an existing open-source model rather than a from-scratch subquadratic training. If true, the efficiency gains would be much less than advertised, since the base model still encodes quadratic training costs. No rebuttal from Subquadratic has been published.

VentureBeat's headline captured the community mood: *"Miami startup Subquadratic claims 1,000x AI efficiency gain with SubQ model; researchers demand independent proof."*

The **supportive case**, from AI researcher John Rysana: "The work is just subquadratic attention done well which is very meaningful for long context workloads — odds of it being BS are extremely low." The legitimacy of the research direction (subquadratic attention has been an active goal in academic ML for years) is not in dispute. The question is whether this specific implementation achieves the scale and quality claimed.

The third-party MRCR verification sits in the middle — it validates one performance claim on one benchmark, which is evidence but not proof.

---

## Why 12M Context Actually Matters

Setting aside the verification debate: if SubQ performs as claimed, what would 12M tokens change?

**For software engineering**: 12M tokens is approximately 10 million words. A large enterprise codebase — all source files, all commit history, all documentation — typically fits in 2–8 million tokens. A 12M context model means no chunking, no RAG, no retrieval pipeline. You put the entire codebase in and ask questions directly.

**For legal**: Full case file processing — discovery documents, contract portfolios, prior art archives — in a single call. Current workflows require splitting, chunking, and retrieval-augmented pipelines that introduce errors.

**For long-running agents**: Persistent state across months of interaction without any external memory or retrieval system. The context window itself becomes the memory.

**For research**: Entire literature corpora in context. Not a RAG index, but the actual papers.

Subquadratic has indicated a **50M token target for Q4 2026**. If that benchmark is reached, it begins to look less like a context window and more like unlimited memory.

None of this matters if the model can't reason well at general tasks, which is exactly what the missing benchmarks would show.

---

## Pricing

No public pricing page has been published. Based on launch interviews and analyst estimates:

- **Estimated API pricing**: ~$0.50 per million input tokens / $1.50 per million output tokens
- **Inference speed**: 150+ tokens/second claimed
- **Effective cost advantage**: At long context lengths, approximately **1/10th the cost of GPT-5.5 standard** and similar frontier models

If the cost claims hold, the value proposition for long-context workloads is dramatic: tasks that currently cost $2,600 on Claude at 128K context reportedly cost $8 on SubQ. Whether this holds as the product scales out of private beta is unknown.

---

## What Builders Should Do

**If you're building applications that are bottlenecked by context length or cost**, SubQ is worth getting on the waitlist for today. Even if the headline claims are partially inflated, a model that delivers competitive RULER and SWE-Bench scores at 1/10th the cost of frontier models has real value.

**If you're evaluating SubQ for production use**, wait for three things: an independent efficiency benchmark (not just the vendor-run numbers), a peer-reviewed paper with the architecture details, and general reasoning evaluations (MMLU/GPQA class). Without those, the risk of architectural surprises in production is real.

**If you're a researcher**, the SSA approach — content-dependent sparse exact attention — is an interesting direction worth tracking regardless of how SubQ's commercial story unfolds. The architectural direction is legitimate even if this specific implementation is debated.

---

## The Honest Assessment

SubQ is built around a real research direction that addresses a real bottleneck. The CTO's background (Meta's Head of Generative AI) suggests serious engineering, not a demo-only startup. The third-party-verified MRCR score is genuine evidence. The $29M seed from credible investors is not a nothing signal.

But the selective benchmark disclosure is a yellow flag. A company confident in their general reasoning quality publishes MMLU. A company that publishes only the benchmarks where their architecture has structural advantages is either still training (plausible, given the private beta status) or has something to hide about base model quality (also plausible, given the "sparse finetune" skepticism).

The honest read: **SubQ is probably a real architectural advance for long-context workloads, and probably not a frontier reasoning model yet.** The open question is whether those two things will both be true by the time general availability arrives — or whether the efficiency claims quietly compress as independent testing begins.

Wait for the paper. Watch the MRCR independently. In the meantime, get on the waitlist if long-context cost is your actual bottleneck.

**Rating: 3/5** — Architecturally promising, commercially early, benchmarks too narrow to trust fully.

---

*ChatForest researches AI tools and platforms. We have not been granted early access to SubQ's private beta. All benchmark figures and pricing estimates come from the company's launch materials, press coverage, and community analysis.*
