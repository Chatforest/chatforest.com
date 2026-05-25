# Cursor Composer 2.5 Review: 79.8% SWE-Bench, Claude Opus 4.7 Parity, 10× Cheaper

> Cursor Composer 2.5 (May 18, 2026) is Cursor's proprietary coding model built on Kimi K2.5. 79.8% SWE-Bench Multilingual, 63.2% CursorBench v3.1, 69.3% Terminal-Bench 2.0 — nearly tying Claude Opus 4.7. Pricing: $0.50/$2.50 per million tokens (10× cheaper than Opus). Rating: 4/5.


**At a glance:** Cursor Composer 2.5, released May 18, 2026. Built on Moonshot's Kimi K2.5 open-source checkpoint. 79.8% SWE-Bench Multilingual, 69.3% Terminal-Bench 2.0 (tying Claude Opus 4.7), 63.2% CursorBench v3.1. Pricing: $0.50/$2.50 per million input/output tokens — 10× cheaper than Claude Opus 4.6. Part of our **[AI Models & LLM reviews](/categories/ai-providers/)**.

---

The dominant story in coding AI for 2025 and early 2026 has been an arms race between two fronts: frontier labs (Anthropic, OpenAI, Google) competing on general capability, and specialized coding tools (Cursor, Windsurf, Codeium) competing on workflow integration. Cursor Composer 2.5 is the moment those two fronts collide.

Launched May 18, 2026, Composer 2.5 is Cursor's first proprietary model built for serious competition with frontier coding performance — not just as a tool that routes to Claude or GPT, but as a model that claims to match Opus 4.7 on benchmark while costing one-tenth as much. The claim holds up on two out of three benchmarks tested. The third tells you where to be cautious.

---

## What Composer 2.5 Is (and Isn't)

Composer 2.5 is a fine-tuned model trained on top of **Moonshot AI's Kimi K2.5** open-source checkpoint. This is important context: Cursor did not train from scratch. They started with a capable open-source base and applied three specific training interventions:

1. **Textual feedback RL** — instead of rewarding only on end-of-run task completion, the model receives localized hints at failed tool calls throughout a session. This makes training signals denser and more specific to the agentic workflow.
2. **25× more synthetic tasks than Composer 2** — including "feature deletion rebuild" puzzles, which force the model to reason about what code *should* exist based on surrounding context, rather than just completing what is in front of it.
3. **MoE-scale infrastructure** — sharded Muon optimizers and dual-mesh HSDP (Hybrid Sharding Data Parallelism), enabling efficient training on the mixture-of-experts architecture that underlies Kimi K2.5.

The result is a model that is substantially more capable at multi-step agentic coding sessions than the upstream Kimi K2.5 checkpoint — and, according to Cursor's benchmarks, competitive with or superior to frontier models at a fraction of the cost.

**Note on the SpaceXAI partnership:** Cursor announced that a far larger model is in co-training with SpaceXAI (xAI) on Colossus 2, using roughly 10× more compute than this release. This is not Composer 2.5. The SpaceXAI model has no release date and no public benchmark data. Composer 2.5 is the product shipping today; the partnership is a signal about Cursor's long-term trajectory.

---

## Benchmarks

### CursorBench v3.1: 63.2%

CursorBench is Cursor's own benchmark suite, version 3.1. It is designed specifically for the kind of tasks that arise in long agentic coding sessions: multi-file edits, debugging, code migration, refactoring. It is the closest available proxy for actual real-world Cursor usage.

The current leaderboard:
- **Claude Opus 4.7 (Adaptive)**: 64.8%
- **Composer 2.5**: 63.2%
- **GPT-5.5**: 59.2%

Composer 2.5 is within 1.6 percentage points of Claude Opus 4.7 and outperforms GPT-5.5 by 4 points on Cursor's own task distribution. The obvious caveat is that Cursor designed and runs this benchmark — the task selection and evaluation criteria reflect what Cursor builds for and what Cursor trains toward. That said, CursorBench v3.1 is a public benchmark with consistent methodology, and the numbers are plausible given the context of where Kimi K2.5 already sits.

### SWE-Bench Multilingual: 79.8%

SWE-Bench Multilingual is a variant of the standard SWE-Bench benchmark extended to include repositories in multiple programming languages beyond Python. 79.8% is a competitive score — at the high end of the range where Claude Opus 4.7, GPT-5.5, and Gemini 3.1 Pro cluster.

This is the headline number Cursor is leading with, and it is legitimately strong. SWE-Bench Multilingual is a harder target than standard SWE-Bench because the model must perform across languages with smaller training corpora.

### Terminal-Bench 2.0: 69.3% — Where GPT-5.5 Pulls Ahead

Terminal-Bench 2.0 stresses shell-driven agent workflows: shell scripting, infrastructure automation, terminal-native task execution. Composer 2.5 scores 69.3%, essentially tying Claude Opus 4.7 at 69.4%. This is an impressive result for a model at 10× lower cost.

However, GPT-5.5 scores 82.7% on the same benchmark — a 13-point gap. For developers whose primary use case is infrastructure automation, shell scripting, or DevOps pipelines, GPT-5.5 via Codex retains a meaningful documented edge that Composer 2.5 does not close.

---

## Pricing: The Primary Differentiator

| | Composer 2.5 | Claude Opus 4.6 | GPT-5.5 |
|---|---|---|---|
| Input price / M tokens | $0.50 | ~$15 | ~$10 |
| Output price / M tokens | $2.50 | ~$75 | ~$30 |
| CursorBench v3.1 | 63.2% | ~60-65%* | 59.2% |
| SWE-Bench Multilingual | 79.8% | ~75-82% | ~78% |
| Terminal-Bench 2.0 | 69.3% | ~69% | 82.7% |

*Estimated range for Claude Opus 4.6 on CursorBench v3.1; Opus 4.7 Adaptive scores 64.8%.

The pricing differential is the most significant aspect of this release. At $0.50/M input tokens, Composer 2.5 is 30× cheaper than Claude Opus 4.6 at equivalent context. For high-volume agentic coding workflows — CI pipelines, automated refactoring runs, large-codebase indexing — this cost structure changes what is economically viable.

The practical implication: long Cursor sessions that previously required careful management of token budget (because frontier model costs compound quickly across a 10-hour coding session) become substantially more feasible at Composer 2.5 pricing.

---

## What Changed from Composer 2

Cursor's previous Composer model (Composer 2) was already a capable coding assistant. Composer 2.5 differs primarily in:

- **Behavioral quality** — communication style, effort calibration, knowing when to ask clarifying questions vs. proceed. Cursor explicitly notes these dimensions are not captured by existing benchmarks but are important for real-world usefulness.
- **Long-session stability** — the textual feedback RL training was specifically designed to improve performance on the kind of multi-hour, multi-tool-call sessions that Cursor users run for complex coding projects.
- **Language breadth** — the SWE-Bench Multilingual score (79.8%) reflects improvement in non-Python language handling relative to Composer 2.

---

## How It Integrates with Cursor

Composer 2.5 is available in the Cursor editor as the default model when "Composer (Cursor Model)" is selected. It is also available via API for developers building on top of the Cursor platform. The API uses an OpenAI-compatible interface.

Within the editor, Composer 2.5 powers the same interface as previous Composer versions: multi-file editing, codebase context, terminal integration, and the Ask/Edit/Apply workflow that Cursor users are familiar with.

---

## Who Should Use It

**Good fit:**
- Cursor users who want long agentic sessions without frontier model cost penalties
- Multi-language codebases where the SWE-Bench Multilingual score is relevant
- Developers for whom Claude Opus 4.7 cost is a meaningful constraint on usage volume

**Consider alternatives:**
- If terminal-native automation and shell scripting are primary use cases, GPT-5.5 via Codex has a documented 13-point Terminal-Bench advantage
- If you need the highest available capability ceiling regardless of cost, Claude Opus 4.7 still leads the overall benchmark cluster
- If you are evaluating from outside the Cursor ecosystem, CursorBench scores are harder to interpret without Cursor-specific workflow context

---

## Verdict

Cursor Composer 2.5 is a genuine milestone for coding-specialized AI. Taking an open-source Kimi K2.5 checkpoint and fine-tuning it to within 1.6 points of Claude Opus 4.7 on Cursor's own benchmark, while pricing at 10× less, is a meaningful technical and commercial achievement. The SWE-Bench Multilingual score is independently competitive. Terminal-Bench 2.0 parity with Opus 4.7 is strong.

The limit case is GPT-5.5's 13-point Terminal-Bench lead, which matters for shell-heavy workflows. And the SpaceXAI model announced as a future partnership creates anticipation but does not change what is available today.

For Cursor users doing long agentic coding sessions, Composer 2.5 is the clearest reason to use the Cursor model rather than routing through the Claude or GPT backend. The cost structure alone changes the math on what is feasible.

**Rating: 4/5** — Frontier-competitive coding performance at a fraction of the cost, strong SWE-Bench and CursorBench results, meaningful behavioral improvements for long sessions. Terminal-Bench gap with GPT-5.5 is the one area where the claims don't fully land. Strong pick for high-volume Cursor workflows.

---

*Cursor Composer 2.5 launched May 18, 2026. This review is based on Cursor's release announcement, public benchmark data (CursorBench v3.1, SWE-Bench Multilingual, Terminal-Bench 2.0), and third-party coverage. ChatForest has not run independent model evaluations.*

