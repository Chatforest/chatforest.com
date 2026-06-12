---
title: "Claude Fable 5 — Anthropic's Mythos-Class Model, Now Public"
date: 2026-06-12
description: "Claude Fable 5 (June 9, 2026): Anthropic's first Mythos-class model available to the public. 80.3% SWE-bench Pro, 1M context, $10/$50 per million tokens. Same underlying model as Mythos 5 — with three classifier-based safeguards blocking cyber, bio, and distillation queries."
og_description: "Anthropic released Claude Fable 5 on June 9, 2026. SWE-bench Pro 80.3% — 11 points ahead of Opus 4.8, 21 points ahead of GPT-5.5. Same underlying model as Mythos 5. Three safeguards block high-risk queries and fall back to Opus 4.8. Free for subscribers through June 22; then usage credits required. 1M token context. $10/$50 per million tokens."
content_type: "Review"
card_description: "Claude Fable 5 is the first Mythos-class model Anthropic has released to the public. Launched June 9, 2026. It shares the same underlying model as Claude Mythos 5 — Anthropic's most capable tier — but ships with three classifier-based safeguards that block cybersecurity, biology/chemistry, and model distillation queries, falling back to Claude Opus 4.8 when triggered. Benchmark results: 80.3% SWE-bench Pro, 29.3% FrontierCode Diamond, 29.8% GDP.pdf vision. Priced at $10/$50 per million tokens. 1M context window. Available on Claude API, Claude.ai plans, and GitHub Copilot."
tags: ["anthropic", "claude", "fable-5", "mythos", "ai-safety", "project-glasswing", "swe-bench", "coding", "frontier-ai", "benchmarks", "llm-release"]
categories: ["reviews"]
rating: 0
author: "ChatForest"
---

**Editorial note:** ChatForest does not have hands-on access to Claude Fable 5 or Mythos 5. This article is based on Anthropic's official announcement, the model's API documentation, benchmark analyses published by Vellum.ai and Finout, reporting from TechCrunch, CNBC, The Decoder, and 9to5Google, and publicly available leaderboard data. We do not claim first-hand testing of these models.

---

**At a glance:** Claude Fable 5. Launched June 9, 2026. Publicly available via API and Claude.ai plans. Same underlying model as Claude Mythos 5. Companion piece to our earlier coverage: **[Claude Mythos Preview — The AI Anthropic Built But Won't Release](/reviews/claude-mythos-preview-anthropic-cybersecurity-ai-too-powerful-to-release/)**.

---

Two months ago, Anthropic built an AI model they decided was too powerful to release.

On June 9, 2026, they released it anyway — with conditions.

The model is Claude Fable 5. The conditions are three classifier-based safeguards that watch every query and fall back to an older model if they detect something dangerous. This is not a smaller, safer version of Mythos. It is the same underlying model as Claude Mythos 5, running with a set of guardrails bolted on.

Whether that is a satisfying answer to the concerns Anthropic raised in April is a question worth sitting with.

---

## The Architecture: One Model, Two Products

Anthropic released two models on June 9:

**Claude Fable 5** — the public version. Available to anyone on Claude API, Claude.ai Pro/Max/Team/Enterprise, and GitHub Copilot. Three safeguards restrict high-risk capabilities.

**Claude Mythos 5** — the same underlying model with those safeguards lifted. Available only through Project Glasswing, Anthropic's partnership program with the U.S. government for cyber defenders and critical infrastructure providers.

The distinction matters. Fable 5 is not a different model tuned for safety. It is Mythos 5 with runtime classifiers watching what comes in and out. When a classifier fires, the session falls back to Claude Opus 4.8. Anthropic reports this happens in fewer than 5% of sessions.

---

## Benchmarks

The headline numbers position Fable 5 as the strongest coding model currently available to the public:

| Benchmark | Fable 5 | Opus 4.8 | GPT-5.5 | Gemini 3.1 Pro |
|-----------|---------|----------|---------|----------------|
| SWE-bench Pro | **80.3%** | 69.2% | 58.6% | 54.2% |
| FrontierCode Diamond | **29.3%** | 13.4% | 5.7% | — |
| GDP.pdf (vision) | **29.8%** | 22.5% | 24.9% | 16.7% |
| Terminal-Bench 2.1 | **88.0%** | 82.7% | — | — |

SWE-bench Pro measures autonomous performance on production-grade software engineering tasks — real bugs, real codebases. Fable 5's 80.3% is 11 points ahead of the next closest publicly available model and roughly 22 points ahead of GPT-5.5.

FrontierCode Diamond is the hardest split of Cognition's coding evaluation, filtering for tasks that represent genuinely hard engineering problems rather than well-specified single-file changes. Fable 5's 29.3% against Opus 4.8's 13.4% suggests the performance gap widens at difficulty extremes.

The vision result (GDP.pdf, no tools) is notable: this is a finance-domain benchmark that requires interpreting complex document layouts. Fable 5 leads GPT-5.5 here by roughly five points.

### What Mythos 5 Can Do (Unblocked)

Mythos 5 — the same model with its cyber and biology safeguards removed — posts materially different numbers on the benchmarks those safeguards are designed to protect:

| Benchmark | Mythos 5 | Opus 4.8 | GPT-5.5 |
|-----------|----------|----------|---------|
| ExploitBench | **78.0%** | 40.0% | 34.0% |
| BioMysteryBench | **46.1%** | 40.0% | — |

ExploitBench measures autonomous exploitation of security vulnerabilities. A 78% capture rate — nearly double Opus 4.8 and more than double GPT-5.5 — reflects the same capability profile that led Anthropic to keep Mythos Preview internal in April. That capability now exists in production. It is just behind a classifier wall for most users.

---

## The Three Safeguards

Fable 5 ships with three classifiers operating at inference time:

**1. Cybersecurity classifier.** Watches for queries touching offensive security — exploit development, vulnerability probing, attack tooling. Falls back to Opus 4.8 when triggered.

**2. Biology/chemistry classifier.** Covers dual-use research that could enable bioweapon development or dangerous synthesis. Same fallback.

**3. Distillation classifier.** Blocks attempts to extract model capabilities by generating synthetic training data or eliciting model-mimicking completions at scale. Protects the model as a commercial asset.

The fallback mechanism — routing to Opus 4.8 rather than refusing outright — is an interesting design choice. It means restricted users get a response, just not the Mythos-class one. Whether that reduces friction enough to matter for legitimate users without creating a meaningful bypass is unclear from public information.

Anthropic's reported figure: more than 95% of Fable sessions involve no fallback at all.

---

## Availability and Pricing

**API (developers):**
- Model ID: `claude-fable-5`
- Context window: 1M tokens
- Input: $10 per million tokens
- Output: $50 per million tokens

Both figures are double Claude Opus 4.8's rates. One additional factor: Opus 4.7 and later models use a tokenizer that produces up to 35% more tokens for the same text compared to earlier Claude models. Effective per-request costs are higher than the per-token rate alone suggests.

**Claude.ai subscriptions:**
- June 9–22: Fable 5 included at no extra cost on Pro, Max, Team, and Enterprise plans
- June 23 onward: Usage credits required
- Full restoration as standard tier: planned when capacity allows

**GitHub Copilot:** Generally available as of June 9.

**Claude Mythos 5:** Not publicly available. Deployed through Project Glasswing to cyber defenders and critical infrastructure organizations. Anthropic plans to expand Glasswing and open a separate biology track (Fable 5 with biology/chemistry safeguards removed but cyber safeguards retained) for select researchers.

---

## Data Policy

Anthropic applies a 30-day data retention requirement to Mythos-class traffic. This data is not used for training or non-safety purposes, which is a notable departure from the default policies of several competing providers.

---

## What This Means for Builders

The practical implications depend on your use case:

**For software engineering agents**: Fable 5 is the strongest publicly available model for autonomous coding tasks. The 80.3% SWE-bench Pro result is not incremental. If you are building agents that operate on real codebases — PR review, bug triage, feature implementation — this is the current ceiling.

**For multimodal / document pipelines**: The vision results suggest Fable 5 handles complex, information-dense documents better than current alternatives. Finance, legal, and technical document workflows are the likely beneficiaries.

**For scientific research**: Anthropic's internally conducted comparisons found scientists preferred Mythos 5's molecular biology hypotheses 80% of the time over other models. One hypothesis — a novel mechanism for an E. coli protein — was independently corroborated by another lab. Fable 5 carries the same underlying capability; the biology classifier only triggers on dual-use synthesis, not general scientific reasoning.

**For cybersecurity**: Fable 5 with the cyber classifier active is a different tool than Mythos 5. Offensive capabilities are blocked at inference. For defenders doing authorized red-team work, the Glasswing pathway is the relevant route.

---

## The Safety Question

In April, Anthropic said Mythos Preview's cybersecurity capability represented "a step-change" that made general release inadvisable. On June 9, a model with the same underlying capability became publicly available on a $10/million-token API.

The safeguards are real. The fallback mechanism is more than a paper policy — it operates automatically at inference time and catches a measurable share of sessions. But classifiers are classifiers. They pattern-match. The capability they are guarding against exists in the model weights. The distance between "blocked by a classifier" and "not blocked by a classifier" is not the same as the distance between "capable" and "not capable."

Anthropic's argument is that the sequencing problem justifies this approach: defenders have had two months to patch vulnerabilities that Mythos Preview found. The landscape is safer now than it was in April. Restricting Mythos 5 access through Glasswing while making Fable 5 broadly available is the operational expression of that judgment.

Whether that argument holds depends on empirical questions — how many vulnerabilities have actually been patched, how quickly the classifier can be probed, and whether the defenders who needed that two-month window actually used it — that are not answerable from public information.

What is clear: Mythos-class capabilities are now in the public API. That is a consequential fact, and the reasoning behind it is worth understanding before building on top of it.

---

*Sources: [Anthropic official announcement](https://www.anthropic.com/news/claude-fable-5-mythos-5) · [TechCrunch](https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/) · [CNBC](https://www.cnbc.com/2026/06/09/anthropic-mythos-claude-fable-5.html) · [Vellum benchmark analysis](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained) · [The Decoder](https://the-decoder.com/anthropic-releases-claude-fable-5-and-mythos-5-with-major-gains-in-coding-and-science/) · [GitHub Copilot GA announcement](https://github.blog/changelog/2026-06-09-claude-fable-5-is-generally-available-for-github-copilot/)*
