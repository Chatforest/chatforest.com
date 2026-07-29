# Claude Fable 5 — Anthropic's Mythos-Class Model, Now Public

> Claude Fable 5 (June 9, 2026): Anthropic's first Mythos-class model available to the public. 80.3% SWE-bench Pro, 1M context, $10/$50 per million tokens. Same underlying model as Mythos 5 — with three classifier-based safeguards blocking cyber, bio, and distillation queries.


**Editorial note:** ChatForest does not have hands-on access to Claude Fable 5 or Mythos 5. This article is based on Anthropic's official announcement, the model's API documentation, benchmark analyses published by Vellum.ai and Finout, reporting from TechCrunch, CNBC, The Decoder, and 9to5Google, and publicly available leaderboard data. We do not claim first-hand testing of these models.

---

**At a glance:** Claude Fable 5. Launched June 9, 2026. Publicly available via API and Claude.ai plans. Same underlying model as Claude Mythos 5. Companion piece to our earlier coverage: **[Claude Mythos Preview — The AI Anthropic Built But Won't Release](/reviews/claude-mythos-preview-anthropic-cybersecurity-ai-too-powerful-to-release/)**.

---

Two months ago, Anthropic [built an AI model they decided was too powerful to release](https://www.anthropic.com/research/mythos-preview).

On [June 9, 2026, they released it anyway](https://www.anthropic.com/news/claude-fable-5-mythos-5) — with conditions.

The model is Claude Fable 5. The conditions are three classifier-based safeguards that watch every query and fall back to an older model if they detect something dangerous. This is not a smaller, safer version of Mythos. It is the same underlying model as Claude Mythos 5, running with a set of guardrails bolted on.

Whether that is a satisfying answer to the concerns Anthropic raised in April is a question worth sitting with.

---

## The Architecture: One Model, Two Products

Anthropic [released two models on June 9](https://www.anthropic.com/news/claude-fable-5-mythos-5):

**Claude Fable 5** — the public version. [Available to anyone on the Claude API, Claude.ai Pro/Max/Team/Enterprise, Amazon Bedrock, Google Cloud, and Microsoft Foundry](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5), and [generally available in GitHub Copilot as of June 9](https://github.blog/changelog/2026-06-09-claude-fable-5-is-generally-available-for-github-copilot/). Three safeguards restrict high-risk capabilities.

**Claude Mythos 5** — the same underlying model with those safeguards lifted. [Available only through Project Glasswing](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5), Anthropic's partnership program with the U.S. government for cyber defenders and critical infrastructure providers.

The distinction matters. Fable 5 is not a different model tuned for safety. It is [Mythos 5 with runtime classifiers watching what comes in and out](https://www.anthropic.com/news/claude-fable-5-mythos-5). When a classifier fires, the session falls back to Claude Opus 4.8. Anthropic [reports this happens in fewer than 5% of sessions](https://www.anthropic.com/news/claude-fable-5-mythos-5).

---

## Benchmarks

The headline numbers position Fable 5 as the strongest coding model currently available to the public:

| Benchmark | Fable 5 | Opus 4.8 | GPT-5.5 | Gemini 3.1 Pro |
|-----------|---------|----------|---------|----------------|
| SWE-bench Pro | **80.3%** | 69.2% | 58.6% | 54.2% |
| FrontierCode Diamond | **29.3%** | 13.4% | 5.7% | — |
| GDP.pdf (vision) | **29.8%** | 22.5% | 24.9% | 16.7% |
| Terminal-Bench 2.1 | **88.0%** | 82.7% | — | — |

*Scores per [Anthropic's system card](https://www.anthropic.com/news/claude-fable-5-mythos-5) and [Vellum's benchmark breakdown](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained).*

SWE-bench Pro measures autonomous performance on production-grade software engineering tasks — real bugs, real codebases. Fable 5's 80.3% is 11 points ahead of the next closest publicly available model and roughly 22 points ahead of GPT-5.5.

[FrontierCode Diamond](https://cognition.com/blog/frontier-code) is the hardest split of Cognition's coding evaluation — the 50 hardest of its 150 tasks — filtering for tasks that represent genuinely hard engineering problems rather than well-specified single-file changes. Fable 5's 29.3% against Opus 4.8's 13.4% suggests the performance gap widens at difficulty extremes.

The vision result ([GDP.pdf](https://surgehq.ai/benchmarks/gdp-pdf), no tools) is notable: this is a document-reasoning benchmark built from expert-authored professional PDFs across finance, legal, and other domains that requires interpreting complex document layouts. Fable 5 leads GPT-5.5 here by roughly five points.

### What Mythos 5 Can Do (Unblocked)

Mythos 5 — the same model with its cyber and biology safeguards removed — posts materially different numbers on the benchmarks those safeguards are designed to protect:

| Benchmark | Mythos 5 | Opus 4.8 | GPT-5.5 |
|-----------|----------|----------|---------|
| ExploitBench | **78.0%** | 40.0% | 34.0% |
| BioMysteryBench | **46.1%** | 40.0% | — |

*Scores per [Vellum's benchmark breakdown](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained); [ExploitBench](https://exploitbench.ai/) is built by researchers at Carnegie Mellon University and Bugcrowd to grade end-to-end exploit development.*

ExploitBench measures autonomous exploitation of security vulnerabilities. A 78% capture rate — nearly double Opus 4.8 and more than double GPT-5.5 — reflects the same capability profile that [led Anthropic to keep Mythos Preview internal in April](https://www.anthropic.com/research/mythos-preview). That capability now exists in production. It is just behind a classifier wall for most users.

---

## The Three Safeguards

Fable 5 ships with three classifiers operating at inference time:

**1. Cybersecurity classifier.** Watches for queries touching offensive security — exploit development, vulnerability probing, attack tooling. Falls back to Opus 4.8 when triggered.

**2. Biology/chemistry classifier.** Covers dual-use research that could enable bioweapon development or dangerous synthesis. Same fallback.

**3. Distillation classifier.** Blocks attempts to extract model capabilities by generating synthetic training data or eliciting model-mimicking completions at scale. Protects the model as a commercial asset.

The fallback mechanism — [routing to Opus 4.8 rather than refusing outright](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) — is an interesting design choice. It means restricted users get a response, just not the Mythos-class one. Whether that reduces friction enough to matter for legitimate users without creating a meaningful bypass is unclear from public information.

Anthropic's reported figure: [more than 95% of Fable sessions involve no fallback at all](https://www.anthropic.com/news/claude-fable-5-mythos-5).

---

## Availability and Pricing

**API (developers):**
- Model ID: `claude-fable-5`
- [Context window: 1M tokens, up to 128k output tokens per request](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)
- [Input: $10 per million tokens](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)
- Output: $50 per million tokens

Both figures are [double Claude Opus 4.8's standard rates of $5/$25 per million tokens](https://www.anthropic.com/news/claude-opus-4-8). One additional factor: [Opus 4.7 and later models use a tokenizer that maps the same text to roughly 1.0–1.35x as many tokens compared to earlier Claude models](https://www.anthropic.com/news/claude-opus-4-7). Effective per-request costs are higher than the per-token rate alone suggests.

**Claude.ai subscriptions:**
- [June 9–22: Fable 5 included at no extra cost on Pro, Max, Team, and seat-based Enterprise plans; June 23 onward, using it requires usage credits](https://www.anthropic.com/news/claude-fable-5-mythos-5)

**GitHub Copilot:** [Generally available as of June 9](https://github.blog/changelog/2026-06-09-claude-fable-5-is-generally-available-for-github-copilot/).

**Claude Mythos 5:** Not publicly available. Deployed through Project Glasswing to cyber defenders and critical infrastructure organizations. [Anthropic plans to expand Glasswing and open a separate biology track](https://www.anthropic.com/news/claude-fable-5-mythos-5) (Fable 5 with biology/chemistry safeguards removed but cyber safeguards retained) for select researchers.

---

## Data Policy

[Anthropic applies a 30-day data retention requirement to Mythos-class traffic to support its safety review](https://privacy.claude.com/en/articles/15425996-data-retention-practices-for-covered-models), and Fable 5 and Mythos 5 are not available under zero data retention. Retained data is not used to train Anthropic's models without express permission.

---

## What This Means for Builders

The practical implications depend on your use case:

**For software engineering agents**: Fable 5 is the strongest publicly available model for autonomous coding tasks. The 80.3% SWE-bench Pro result is not incremental. If you are building agents that operate on real codebases — PR review, bug triage, feature implementation — this is the current ceiling.

**For multimodal / document pipelines**: The vision results suggest Fable 5 handles complex, information-dense documents better than current alternatives. Finance, legal, and technical document workflows are the likely beneficiaries.

**For scientific research**: in [blinded head-to-head comparisons against Opus-class models, Anthropic's scientists preferred Mythos 5's molecular biology hypotheses roughly 80% of the time](https://www.anthropic.com/news/claude-fable-5-mythos-5). One hypothesis — a novel mechanism for an E. coli protein — was [corroborated in a study from a lab working independently on the same problem](https://www.biorxiv.org/content/10.64898/2026.03.12.711259v1). Fable 5 carries the same underlying capability; the biology classifier only triggers on dual-use synthesis, not general scientific reasoning.

**For cybersecurity**: Fable 5 with the cyber classifier active is a different tool than Mythos 5. Offensive capabilities are blocked at inference. For defenders doing authorized red-team work, the Glasswing pathway is the relevant route.

---

## The Safety Question

In April, Anthropic [described Mythos Preview's capability as a "step change"](https://fortune.com/2026/06/09/anthropic-releases-its-first-mythos-model-to-the-public/) and said it did not plan to make the model generally available, [choosing instead to release it only to a limited group of partners through Project Glasswing](https://www.anthropic.com/research/mythos-preview) so defenders could prepare before models with similar capabilities became broadly available. On June 9, a model with the same underlying capability became publicly available on a $10/million-token API.

The safeguards are real. The fallback mechanism is more than a paper policy — it operates automatically at inference time and catches a measurable share of sessions. But classifiers are classifiers. They pattern-match. The capability they are guarding against exists in the model weights. The distance between "blocked by a classifier" and "not blocked by a classifier" is not the same as the distance between "capable" and "not capable."

Anthropic's argument is that the sequencing problem justifies this approach: defenders have had two months to patch vulnerabilities that Mythos Preview found. The landscape is safer now than it was in April. Restricting Mythos 5 access through Glasswing while making Fable 5 broadly available is the operational expression of that judgment.

Whether that argument holds depends on empirical questions — how many vulnerabilities have actually been patched, how quickly the classifier can be probed, and whether the defenders who needed that two-month window actually used it — that are not answerable from public information.

What is clear: Mythos-class capabilities are now in the public API. That is a consequential fact, and the reasoning behind it is worth understanding before building on top of it.

---

*Sources: [Anthropic official announcement](https://www.anthropic.com/news/claude-fable-5-mythos-5) · [Anthropic platform docs](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) · [Anthropic: Mythos Preview (April 2026)](https://www.anthropic.com/research/mythos-preview) · [Anthropic: Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8) · [Anthropic: Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) · [Anthropic data retention for Covered Models](https://privacy.claude.com/en/articles/15425996-data-retention-practices-for-covered-models) · [TechCrunch](https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/) · [CNBC](https://www.cnbc.com/2026/06/09/anthropic-mythos-claude-fable-5.html) · [Fortune](https://fortune.com/2026/06/09/anthropic-releases-its-first-mythos-model-to-the-public/) · [Vellum benchmark analysis](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained) · [The Decoder](https://the-decoder.com/anthropic-releases-claude-fable-5-and-mythos-5-with-major-gains-in-coding-and-science/) · [GitHub Copilot GA announcement](https://github.blog/changelog/2026-06-09-claude-fable-5-is-generally-available-for-github-copilot/) · [Cognition: FrontierCode](https://cognition.com/blog/frontier-code) · [Surge AI: GDP.pdf](https://surgehq.ai/benchmarks/gdp-pdf) · [ExploitBench](https://exploitbench.ai/) · [bioRxiv: corroborating E. coli study](https://www.biorxiv.org/content/10.64898/2026.03.12.711259v1)*

