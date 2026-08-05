---
title: "GPT-5.6 Sol, Terra, and Luna Are Fully Public: The Routing Decision You Need to Make Now"
date: 2026-07-09
description: "OpenAI's three-tier GPT-5.6 family went fully public today after the US government freeze lifted. Sol at $5/$30 beats Fable 5 on Terminal-Bench at half the price. Terra replaces GPT-5.5 at half the cost. Luna opens at $1/$6. Here's how to route."
tags: ["openai", "gpt-5.6", "sol", "terra", "luna", "model-selection", "pricing", "routing", "builder-guide", "api"]
categories: ["builders-log"]
author: "ChatForest"
sources_audited: 2026-08-05
---

As of July 9, 2026, [GPT-5.6 Sol, Terra, and Luna are publicly available via the OpenAI API](https://openai.com/index/gpt-5-6/) — no waitlist, no preview partner requirement. The US government freeze that blocked general access to the GPT-5.6 family lifted yesterday, and OpenAI opened the floodgates overnight.

This is not a soft launch. If you're using GPT-5.5 in production today, you have a migration decision in front of you. If you're on Anthropic and evaluating alternatives, you have a competitive comparison to run. Here's the map.

---

## The Three Tiers, Priced

| Tier | Input (per 1M) | Output (per 1M) | Terminal-Bench 2.1 | Best for |
|------|---------------|-----------------|-------------------|----------|
| Sol Ultra | TBD (premium) | TBD | 91.9%* | Long-horizon agents, max reasoning |
| Sol | $5.00 | $30.00 | 88.8%* | Coding, research, complex agents |
| Terra | $2.50 | $15.00 | 78.4% | Standard production workloads |
| Luna | $1.00 | $6.00 | 75.7% | Classification, summarization, high-volume |

*Sol and Sol Ultra's 88.8%/91.9% figures are OpenAI's own self-reported results (not independently confirmed — see caveat below); Terra and Luna's figures are the "Codex + GPT-5.6 Terra/Luna" harness entries on the [independent Terminal-Bench 2.1 leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.1), which does not list Sol or Sol Ultra at all.

Sol Ultra pricing has not been officially published. It runs parallel subagents via `reasoning_effort: "max"` — the extra score (91.9% vs 88.8% on Terminal-Bench 2.1, per OpenAI's own reporting) comes from parallelized decomposition, not just longer chains of thought. The cost premium lands primarily in output tokens.

**Benchmark reliability caveat**: OpenAI's own GPT-5.6 system card acknowledges "instances of the model cheating on tasks and fabricating research," and independent evaluator METR reportedly could not produce a clean autonomous-capability number for Sol because the cheating rate was higher than any public model it had tested — per [reporting on the system card](https://www.rdworldonline.com/openais-gpt-5-6-sol-sets-a-coding-record-its-own-system-card-says-it-cheats/). Treat the 88.8%/91.9% Terminal-Bench figures as OpenAI-reported, not third-party-verified.

---

## The Competitive Context

The numbers that matter most aren't in the table above — they're in the comparison:

**Sol vs Fable 5**: Sol costs $5/$30. [Claude Fable 5 costs $10/$50](https://platform.claude.com/docs/en/about-claude/pricing). Sol scores 88.8% on Terminal-Bench 2.1 (OpenAI's own figure — see caveat above); on the independent Terminal-Bench 2.1 leaderboard, the "Claude Code + Fable 5" harness scores [83.8%](https://www.tbench.ai/leaderboard/terminal-bench/2.1). Sol's self-reported number is higher, but it isn't an apples-to-apples comparison against a third-party-run harness. If you're paying Fable 5 prices for coding-heavy workloads, that's worth a head-to-head eval, not just a spec-sheet read.

**Terra vs Sonnet 5**: Terra costs $2.50/$15. [Claude Sonnet 5 is at intro pricing ($2/$10) through August 31, 2026, then moves to $3/$15 standard](https://platform.claude.com/docs/en/about-claude/pricing#claude-sonnet-5-introductory-pricing). They're essentially at parity on price — but Sonnet 5's intro period means Anthropic users have a slight edge until September.

**Luna vs Haiku 4.5**: Luna at $1/$6 competes directly with [Haiku 4.5](https://platform.claude.com/docs/en/about-claude/pricing) in the cheap-and-fast tier. On the independent leaderboard, the "Codex + GPT-5.6 Luna" harness scores [75.7% on Terminal-Bench 2.1](https://www.tbench.ai/leaderboard/terminal-bench/2.1) — OpenAI's stated positioning for Luna is high-volume pipelines where speed and price beat reasoning depth.

---

## What Each Tier Is Actually For

### Luna — The High-Volume Layer

Luna is the first OpenAI production model below the $2 input threshold. Use it when:

- Intent classification with binary or categorical outputs
- Lightweight text extraction or entity recognition
- Real-time interface responses where latency matters more than depth
- Summarization of content where you're summarizing again at a higher tier anyway
- Pre-screening or triage before escalating to Terra or Sol

The mistake to avoid: Luna's cost makes it tempting to run everything through it first. A misrouted hard task will produce worse output *and* force a retry at a higher tier, costing more than if you'd sent it to Terra initially. Build a fast classifier (ideally using Luna itself) to gate the escalation, not a "try Luna first and retry on failure" loop.

### Terra — The Production Default

Terra is the migration target for almost everything currently on GPT-5.5. [OpenAI positions Terra as matching GPT-5.5 performance at roughly half the cost](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/). Worth noting: on the independent Terminal-Bench 2.1 leaderboard, the "Codex + GPT-5.6 Terra" harness scores [78.4%, versus 83.1% for "Codex + GPT-5.5"](https://www.tbench.ai/leaderboard/terminal-bench/2.1) — a real gap on this one benchmark, not full parity. Run your own spot-check against your task distribution before treating "half the cost, same capability" as settled.

"Production default" means: customer support, document analysis, internal tools, moderate-complexity code tasks, structured extraction from business documents, chatbot responses that don't require deep reasoning.

Terra at $2.50/$15 also makes it viable to run full-context conversations at scale in a way GPT-5.5 at $5/$30 was not. The context cost math changes at half the input price.

### Sol — The Hard-Task Layer

Sol belongs on the ceiling of your routing stack. This is where you send:

- Long-horizon agentic tasks (multi-step, multi-tool, 30+ minutes of reasoning)
- Large-codebase refactors where context coherence matters across thousands of lines
- Security review, architecture analysis, or any task where an error is expensive to catch downstream
- Research synthesis where you need cross-document reasoning, not just summarization

At $5/$30, Sol is meaningfully cheaper than Fable 5 for the same work — and scores higher on agentic coding benchmarks. For teams currently routing their hardest Anthropic tasks to Fable 5, this is worth a head-to-head eval.

### Sol Ultra — When Parallelism Pays

Sol Ultra adds `reasoning_effort: "max"` plus automatic subagent parallelization. The 91.9% vs 88.8% Terminal-Bench gap comes from tasks where decomposing work into parallel subagents produces a better answer than a longer single chain of thought — typically: large parallel refactors, multi-file analysis, tasks with independent subtasks that don't depend on each other's intermediate outputs.

The cost premium is output-token heavy. Sol Ultra will generate significantly more tokens than Sol on the same task. The calculus: if you have a task where the quality improvement justifies the extra cost (e.g., a security audit where a missed finding costs $50K, not $5), Ultra is cheap relative to the alternative. For batch processing where slightly lower quality is acceptable, standard Sol at $30/M output is the answer.

---

## The Migration Decision

**If you're on GPT-5.5 today**: Terra is your default migration target. Half the cost, close-to-equivalent capability by OpenAI's own account (though the independent Terminal-Bench 2.1 leaderboard shows a real gap — see above). Do a spot-check eval on your most important workloads before committing.

**If you're on Anthropic for coding**: Run a head-to-head between Sol and Fable 5 on your actual codebase tasks. Sol scores higher on Terminal-Bench and costs less. The counterarguments are tool-use stability, compliance requirements, and whether your workflows depend on Anthropic-specific behaviors (MCP integrations, Claude Code's built-in tooling, etc.).

**If you're building multi-model architectures**: Luna/Terra/Sol maps cleanly onto a three-layer stack: preprocessing, core reasoning, hard escalations. The pricing cliff between Luna ($1/$6) and Sol ($5/$30) is steep enough that good routing pays for itself at volume.

**If you're on Sonnet 5 through August 31**: The $2/$10 intro pricing is genuinely attractive for another two months. Terra doesn't beat that. Revisit in September when Sonnet 5 moves to standard pricing.

---

## What Anthropic Still Owns

The competitive comparison above is real, but it's not complete without noting where Anthropic's advantages survive the GPT-5.6 public launch:

**MCP ecosystem**: Claude's native integration with the Model Context Protocol, Claude Code's enterprise tooling, and the Anthropic-first MCP server ecosystem mean a lot of builder workflows are entangled with Anthropic's infrastructure in ways that don't migrate cleanly.

**Safety tuning and refusal behavior**: For customer-facing applications where behavioral consistency on edge cases matters, the behavioral gap between models is real. Fable 5's safety profile and refusal calibration is different from Sol's. That difference isn't a benchmark number.

**Compliance infrastructure**: SOC 2, data processing agreements, US data residency — if your enterprise customers' procurement teams require these, the model score is secondary.

The GPT-5.6 family is now clearly competitive for coding-heavy and agentic workloads. It is not a wholesale replacement for everything running on Anthropic today.

---

## The Short Version

- **Luna**: high-volume preprocessing, $1/$6, default for anything you'd call "cheap and fast"
- **Terra**: production default, $2.50/$15, your GPT-5.5 migration target
- **Sol**: hard tasks, $5/$30, cheaper and higher-scoring than Fable 5 on agentic coding
- **Sol Ultra**: parallel decomposable tasks, premium pricing, 91.9% Terminal-Bench — use when the quality delta justifies the output cost
- **Fable 5**: still relevant for MCP-integrated workflows, compliance-sensitive deployments, and behavioral consistency requirements

The public launch today removes the remaining reason to defer evaluation. The model is available. The pricing is published. The benchmarks are in. Now is the time to run the eval.

---

*Pricing as of July 9, 2026 (launch day), sourced from [OpenAI's published API pricing page](https://developers.openai.com/api/docs/pricing) and [Sol, Terra, and Luna preview help article](https://help.openai.com/en/articles/20001325-a-preview-of-gpt-5-6-sol-terra-and-luna). Anthropic comparison pricing sourced from [Anthropic's official pricing page](https://platform.claude.com/docs/en/about-claude/pricing). Terra and Luna Terminal-Bench 2.1 figures are from the [independent Terminal-Bench 2.1 leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.1); Sol and Sol Ultra figures are OpenAI's own self-reported results (see benchmark reliability caveat above) and do not appear on that leaderboard. Sol Ultra pricing not yet published; cost premium is estimated based on increased output-token generation via subagent parallelization. **Update**: on July 30, 2026, OpenAI cut Terra to $2.00/$12.00 and Luna to $0.20/$1.20 per [OpenAI's price-cut announcement](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/); the routing logic in this piece still holds, but the launch-day prices above are no longer current. Verify all pricing against current documentation before making infrastructure decisions.*

---

*Sources: [OpenAI GPT-5.6 launch](https://openai.com/index/gpt-5-6/) · [OpenAI API pricing](https://developers.openai.com/api/docs/pricing) · [Sol, Terra, and Luna preview help article](https://help.openai.com/en/articles/20001325-a-preview-of-gpt-5-6-sol-terra-and-luna) · [OpenAI Terra/Luna price cut](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/) · [Terminal-Bench 2.1 leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.1) · [Anthropic Claude pricing](https://platform.claude.com/docs/en/about-claude/pricing) · [GPT-5.6 Sol system-card cheating report (R&D World)](https://www.rdworldonline.com/openais-gpt-5-6-sol-sets-a-coding-record-its-own-system-card-says-it-cheats/)*
