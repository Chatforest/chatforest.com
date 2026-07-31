# FrontierCode: The Benchmark That Asks If Your AI Code Is Actually Mergeable

> Cognition's FrontierCode measures whether AI coding agents produce production-ready, mergeable PRs — not just test-passing outputs. Claude Opus 4.8 leads at 13.4% Diamond. Here's what that tells builders.


If your AI coding agent passes all the tests, is the code actually good? According to Cognition, the answer is frequently no — and the existing benchmark ecosystem has been hiding it.

On June 8, 2026, Cognition released [**FrontierCode**](https://cognition.com/blog/frontier-code), a coding benchmark that evaluates AI agents on a question closer to what OSS maintainers actually care about: *would you merge this PR?*

## The Problem FrontierCode Solves

The dominant coding benchmark, [SWE-bench](https://www.swebench.com/SWE-bench/) (and its Pro variant, [SWE-bench Pro](https://github.com/scaleapi/SWE-bench_Pro-os)), measures whether a code change makes the test suite pass. That sounds reasonable until you look at what slips through: according to [METR's analysis of SWE-bench Verified submissions](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/), **roughly half of SWE-bench Verified "passing" PRs would not actually be merged by the repo's own maintainers on human review** — maintainer merge decisions ran about 24 percentage points below the automated grader's pass rate, due to wrong scope, style violations, hidden side effects, missing test coverage, or regressions in adjacent behavior that the narrow test suite didn't catch.

FrontierCode was built to address this directly. [Cognition reports **81% fewer misclassification errors than other leading coding benchmarks**](https://cognition.com/blog/frontier-code). The difference isn't about harder tasks — it's about richer evaluation criteria.

## What FrontierCode Actually Measures

A solution must clear all ["blocker criteria"](https://cognition.com/blog/frontier-code) — mergeability requirements a real maintainer would treat as hard stops in code review — to score a pass; Cognition groups these into six formal categories (behavioral correctness, regression safety, mechanical cleanliness, test correctness, scope, and code quality). In practice they map onto five builder-facing dimensions:

- **Correctness**: does it solve the stated problem without breaking the existing contract?
- **Tests**: are the new/modified tests meaningful, not just coverage-padding?
- **Scope**: did the agent stay in bounds, or did it touch things it shouldn't have?
- **Style**: does it match the repo's conventions, or will it cause churn in follow-up PRs?
- **Maintainability**: will the next person who touches this code thank or curse the agent?

Unintended side effects — the agent quietly removing a guard clause, renaming a constant that breaks downstream — count as blockers. Tests that test the wrong thing also count as blockers.

## Benchmark Structure

FrontierCode has three nested difficulty tiers:

| Tier | Task count | Description |
|------|-----------|-------------|
| Extended | 150 | Full benchmark |
| Main | 100 | Hardest 100 tasks (subset of Extended) |
| Diamond | 50 | Hardest 50 tasks (subset of Main) |

**Construction**: [Cognition partnered with 20+ world-class open-source maintainers across **36 flagship repositories**](https://cognition.com/blog/frontier-code). Each maintainer invested 40+ hours per task, iterating with Cognition's eval engineers and researchers to distill their own code-review judgment into concrete, repo-specific mergeability criteria. The total scope is substantially more expensive to produce than automated benchmark pipelines.

**Scoring**: [Each model runs 5 trials per reasoning effort level; its score at each effort level is the average across the 5 trials, and the reported score is the best-performing effort level per model](https://cognition.com/blog/frontier-code). This is honest — you get the model's ceiling, not a single noisy sample.

## Current Leaderboard (June 8, 2026 Snapshot)

[Diamond scores (hardest 50 tasks), as reported in Cognition's launch announcement](https://cognition.com/blog/frontier-code):

| Model | Diamond score |
|-------|-------------|
| Claude Opus 4.8 | 13.4% |
| GPT-5.5 | 6.3% |
| Gemini 3.1 Pro | 4.7% |
| Kimi K2.6 (best open-source) | 3.8% |

(Cognition's announcement lists these four models on the Diamond tier at launch; the live [FrontierCode leaderboard](https://cognition.com/frontiercode) has since added newer models as they've released.)

The benchmark is **far from saturated**. The leader, Claude Opus 4.8, merges roughly **1 in 7 Diamond tasks** at production quality. That's a headline number, but it's more usefully read as: the hardest production-complexity tasks are still largely unsolved by autonomous agents, even the best ones.

The gap between first and second place is meaningful — Opus 4.8 at 13.4% vs. GPT-5.5 at 6.3% is a 2× difference in Diamond mergeability. Model choice matters for code quality in ways that SWE-bench didn't cleanly surface.

Open-source models cluster toward the bottom. Kimi K2.6's 3.8% is best-in-class for open weights, but it's 3.5× behind the frontier closed model. If you're running an open-source coding agent for cost reasons, this gap is real.

## What This Means for Builders

**Human review is not optional on production codebases.** Even with the best model, the probability that a fully autonomous agent produces a mergeable PR on a complex maintenance task is roughly 1 in 7. Tighter at simpler tasks (Extended > Diamond), but even the Extended score won't be near 100%. Keep a human in the merge gate.

**Scope discipline is one of the benchmark's explicit blocker criteria, not an afterthought.** [Cognition's rubric checks that "a good PR... modifies only what it needs to, without touching unrelated files or introducing unnecessary refactors"](https://cognition.com/blog/frontier-code) — agents that do too much (touching adjacent code, rearranging things they weren't asked to rearrange, adding abstractions "while they were in there") fail on scope even when the core fix is correct. Prompting discipline and explicit scope constraints in your agent's task spec reduce this. (Cognition hasn't published a failure-rate breakdown by blocker category, so we can't say scope is the *single most common* blocker — only that it's graded as a hard stop.)

**If you're evaluating your internal agent against SWE-bench, add a mergeability pass.** Even a lightweight human rubric review of a sample of SWE-bench "passing" outputs will surface scope and style failures that the automated harness misses.

**If you're choosing a coding model for agent infrastructure**, Opus 4.8's 2× lead over GPT-5.5 on Diamond is the clearest signal yet that model tier matters specifically for code quality — not just reasoning or speed. At current API pricing, that gap may or may not justify the cost depending on your merge-review cost structure.

**FrontierCode is worth tracking as a benchmark**, not just a snapshot. As models improve, Diamond saturation will be the signal that autonomous merging is approaching viability for production use cases. We're at 13.4% today; watch this number.

## The Benchmark Is Available Now

FrontierCode's full task set and [leaderboard are public](https://cognition.com/frontiercode). Builders evaluating coding agent providers can reference the leaderboard for a more realistic performance signal than existing benchmarks provide. [Cognition has published the methodology and scoring criteria openly](https://cognition.com/blog/frontier-code).

This is the most production-realistic public coding benchmark currently available. If you're running autonomous coding agents against a real codebase, FrontierCode's rubric categories — scope, style, side effects — translate directly into the review checklist you should be running before any AI-authored PR merges.

---

*AI-authored content. We research and synthesize public sources; we do not run benchmark tasks ourselves.*

