---
title: "Princeton Ran 16 AI Agents as Startup CEOs for 500 Days — A Hardcoded Rule System Beat Every One: The Builder's Breakdown"
date: 2026-06-29
description: "CEO-Bench, a new Princeton benchmark, simulates a 500-day AI startup with $1M starting capital and measures which models stay solvent. A rule-based system with no LLM at all outscored all 16 frontier models tested. Here is what broke the rest — and what it means for your agentic deployments."
og_description: "Princeton's CEO-Bench: 16 AI agents ran a simulated startup for 500 days. A hardcoded rule system with zero LLM calls beat every one of them. The failure modes map directly to what breaks production AI agents."
content_type: "Builder's Log"
categories: ["AI Agents", "Research", "Benchmarks"]
tags: ["ceo-bench", "princeton", "ai-agents", "long-horizon", "benchmarks", "agentic", "builder-guide", "june-2026", "research"]
sources_audited: 2026-07-31
---

Princeton researchers handed 16 AI agents a startup, $1 million in simulated capital, and 500 days, then ran a hardcoded rule system through the same simulation as a baseline. Most of the AI agents failed to stay in business — and the baseline with no language model in it beat every single one of them.

The research — **[CEO-Bench: Can Agents Play the Long Game?](https://arxiv.org/abs/2606.18543)** by Haozhe Chen, Karthik Narasimhan, and Zhuang Liu of Princeton's zLab (arXiv 2606.18543), published June 2026 — is not another benchmark measuring whether an AI can write a SQL query or pass a coding challenge. It measures something much harder to fake: **sustained strategic execution under uncertainty, over time, with interconnected consequences and no clean feedback signal**.

The results are a useful corrective to the current wave of agentic hype. Four of sixteen evaluated models went bankrupt in all three of their runs; nine more went bankrupt in at least one of three runs. A simple rule-based system — no LLM, just hardcoded heuristics — finished with the highest cash balance of any system tested, LLM or not: $15.76M, ahead of the best LLM (Claude Fable 5, at $12.63M). The paper states plainly that this heuristic baseline is "above all evaluated model agents" ([CEO-Bench paper](https://arxiv.org/abs/2606.18543)). The theoretical maximum cash balance is approximately $2.2 billion. Even the best-performing system — the rule-based baseline — reached only about 0.7% of that optimum.

---

## What CEO-Bench Tests

The benchmark is a playable Python simulation of an AI startup. Agents start with $1,000,000 in cash and run the company across 500 simulated days. They control pricing, marketing spend, product development investment, support quality, enterprise sales effort, and social media strategy. Success is measured by one number: final cash balance.

The environment is deliberately hard in ways that matter:

- **Hidden customer preferences** — agents must infer segment demand from indirect signals
- **Delayed feedback** — product improvements take weeks to move revenue; costs hit immediately
- **Competitor pressure** — market share shifts without announcement
- **Noisy data** — databases include errors; signals require interpretation
- **Coupled decisions** — pricing changes affect multiple customer segments simultaneously, with non-obvious interactions

None of these characteristics are exotic. Every one of them appears in real product businesses. The paper frames the combined skill as [the ability to integrate](https://arxiv.org/abs/2606.18543) "navigating long horizons amid uncertainty," "acquiring information in noisy environments," "adapting to a changing world," and "orchestrating multiple moving parts toward a coherent goal" — capabilities that isolated, short-horizon benchmarks don't test at all.

---

## The Leaderboard

| Rank | System | Best Run Cash | Bankruptcies (of 3 runs) |
|------|-------|---------------|-------|
| 1 | **Rule-based baseline** | $15.76M | — (hardcoded heuristics, no LLM) |
| 2 | Claude Fable 5 | $12.63M | 1/3 |
| 3 | GPT-5.6 Sol | $11.31M | 2/3 |
| 4 | Claude Opus 4.8 | $2.40M | 1/3 |
| 5 | Qwen 3.7 Max | $365K | 0/3 |
| 6 | Gemini 3.5 Flash | $75K | 0/3 |
| 7 | Claude Opus 4.7 | $71K | 1/3 |
| 8 | Claude Sonnet 5 | $64K | 1/3 |
| 9 | Claude Haiku 4.5 | $60K | 2/3 |
| 10 | GLM 5.2 | $54K | 2/3 |
| 11 | Kimi K2.6 | $44K | 0/3 |
| 12 | Claude Sonnet 4.6 | $38K | 1/3 |
| 13 | GPT-5.5 | $33K | 2/3 |
| 14–16 | GLM 5.1, DeepSeek V4 Pro, Gemini 3 Flash, Grok 4.20 | $0 | 3/3 |

*(Source: Table 3, [CEO-Bench paper](https://arxiv.org/abs/2606.18543).)*

Only three systems finished their best run above the $1M starting balance: the rule-based baseline, Claude Fable 5, and GPT-5.6 Sol. Four models — GLM 5.1, DeepSeek V4 Pro, Gemini 3 Flash, and Grok 4.20 — were bankrupt in every one of their three runs. Only Qwen 3.7 Max, Gemini 3.5 Flash, and Kimi K2.6 never went bankrupt in any run, though none of them made much money.

Two things in this table warrant attention.

**First**: The rule-based system topped the entire leaderboard, LLM or not. It did not use a language model at all — it applied fixed heuristics such as cutting marketing spend when cash ran low and increasing product investment when satisfaction signals dropped. Its $15.76M result beat all sixteen LLM agents tested, including the best of them, Claude Fable 5, by roughly $3.1M ([CEO-Bench paper](https://arxiv.org/abs/2606.18543)).

**Second**: Claude Fable 5 was the best-performing LLM in the study, but at the time these results were circulating (late June 2026), Fable 5 itself was not generally available. On June 12, 2026, Anthropic disabled worldwide access to Fable 5 and Claude Mythos 5 after a US government directive citing a possible method for bypassing the model's cybersecurity safeguards ([Anthropic's statement](https://www.anthropic.com/news/fable-mythos-access)). That suspension was short-lived: the Commerce Department lifted the directive and Fable 5 returned to general availability on July 1, 2026 ([Anthropic's redeployment announcement](https://www.anthropic.com/news/redeploying-fable-5)). Opus 4.8, the next-best LLM in the benchmark, remained available throughout.

---

## The Four Failure Modes

The [CEO-Bench paper](https://arxiv.org/abs/2606.18543) identifies structural challenges that separate models that survived from those that went bankrupt. These are not arbitrary simulation quirks — they recur in real production agentic systems.

### 1. Delayed Feedback Loops

In CEO-Bench, the cost of an action (hiring, product investment, marketing) is immediate. The revenue effect arrives weeks later. Most lower-ranked models treated the simulation as a short-horizon optimization problem: maximize this week's revenue, cut this week's costs. The result is rational-looking decisions that accumulate into structural decline — too much cost-cutting dries out product quality; delayed returns never arrive before cash runs out.

**Builder mapping**: Any agentic loop that runs actions with multi-week revenue consequences — content strategies, SEO initiatives, product development prioritization, sales pipeline nurturing — has this same mismatch. Agents evaluated on immediate outputs will optimize for visible short-term signals and hollow out long-term value.

### 2. Hidden State

Customer satisfaction in CEO-Bench is never directly observed. Agents must infer it from indirect signals: churn rates, support ticket volume, negotiation behavior. Weaker models either ignored it (treating the problem as if all state were observable) or over-anchored on noisy proxies.

Top performers wrote code to simulate customer cohorts and infer hidden preferences from negotiation outcomes — treating the inference problem explicitly rather than hoping the satisfaction signal would surface.

**Builder mapping**: Any system where ground-truth quality is measured downstream — user retention, NPS, actual conversion vs. predicted conversion — has this problem. Agents that can only optimize on directly measurable signals will fail when the important state is latent.

### 3. Non-Stationary Environments

The market in CEO-Bench drifts. Competitors respond to moves. Customer preferences evolve. Strategies that worked in month 2 fail in month 8. Models that learned early patterns and held them went bankrupt on schedule.

The researchers tracked development investment allocation as a differentiator: Claude Fable 5, the best-performing LLM, targeted 88% of its development spend toward specific customer-segment improvements. Weaker performers were far less selective — Claude Opus 4.8 targeted 51%, Qwen 3.7 Max 25%, GLM 5.1 19%, and Grok 4.20 just 11% ([CEO-Bench paper, Section 3.4](https://arxiv.org/abs/2606.18543)).

**Builder mapping**: Production agentic systems with fixed strategy loops — where the initial plan is never revised against new evidence — face exactly this drift. Agents need explicit re-evaluation cadences, not just execution loops.

### 4. Coupled Consequences

Pricing in the simulation affects multiple customer segments at the same time, with cross-effects. Cutting prices for one segment can cannibalize another. Marketing spend affects satisfaction and acquisition simultaneously. Models that reasoned about one dimension in isolation while ignoring cross-effects made locally rational decisions that were globally catastrophic.

Top runs showed significantly more conditional reasoning: "if-then" statements that anticipated downstream coupling before taking an action. The model wasn't just deciding; it was stress-testing the decision against interconnected effects before committing.

**Builder mapping**: In any system where actions have externalities across components — pricing, resource allocation, deployment configuration — agents need explicit multi-axis reasoning rather than sequential single-factor optimization.

---

## What the Top Models Did Differently

Three behavioral signatures, [documented in the paper](https://arxiv.org/abs/2606.18543), distinguish the models that stayed solvent:

**Explicit simulation over implicit intuition.** The paper reports that Claude Fable 5 tracked payment timing, customer losses, and final-week cash under different scenarios, while Claude Opus 4.8 estimated which customers were likely to churn by analyzing payment and cancellation patterns. Top runs generated code mid-run to forecast cash scenarios and model customer cohort behavior rather than relying on intuition about how a decision would ripple forward.

**Targeted investment over diffuse spending.** Claude Fable 5 directed 88% of development spend to specific customer segments identified through analysis, versus 51%, 25%, 19%, and 11% for successively weaker performers ([CEO-Bench paper](https://arxiv.org/abs/2606.18543)). The strongest models produced sharper hypotheses about where investment would produce measurable return.

**Anticipatory reasoning.** The paper finds that Claude Fable 5 and Claude Opus 4.8 use the word "if" noticeably more often in their planning memos than lower-performing models, with qualitative examples showing explicit if-then contingencies prepared in advance rather than reactive adaptation after something goes wrong ([CEO-Bench paper, Fig. 13](https://arxiv.org/abs/2606.18543)).

---

## The Upper Bound Problem

The estimated theoretical maximum for CEO-Bench is approximately $2.2 billion ([CEO-Bench paper](https://arxiv.org/abs/2606.18543)). The best system overall — the rule-based baseline — achieved $15.76 million, about 0.7% of the optimum. The best LLM, Claude Fable 5, reached $12.63 million, roughly 0.6%. The benchmark is far from saturated.

This is worth internalizing. The only systems that finished a best run above the $1M starting balance — the rule-based baseline, Fable 5, and GPT-5.6 Sol — are the strongest performers available. Against a plausible upper bound, they're near the floor. The gap is not a narrow performance deficit. It represents the difference between surviving and thriving.

For builders, the implication is that long-horizon agentic systems should currently be designed to stay solvent, not to maximize — to avoid catastrophic failure, not to approach optimal outcomes. That is a different design objective than much of current agentic tooling assumes.

---

## Builder Audit: 4 Questions for Your Agentic Systems

**1. What is the feedback lag in your system?**
Map the time between an agent action and the signal that confirms it worked or failed. If that lag exceeds your agent's context window or evaluation cycle, the agent is optimizing blind. Add explicit tracking that bridges the lag.

**2. What state is hidden?**
Identify which quality or performance metrics matter but aren't directly observable by the agent. If the agent can't observe it, it can't optimize for it — and it may optimize against it by chasing visible proxies. Either make the hidden state observable (better instrumentation) or build explicit inference mechanisms.

**3. How does your agent re-evaluate its strategy?**
Most agentic frameworks are good at executing a plan. Few have structured re-evaluation cycles that ask: has the environment changed enough that my current strategy should change? Add explicit checkpoints at which the agent re-examines its assumptions, not just its tasks.

**4. What is your model tier for each stage?**
CEO-Bench shows a steep cliff at the top: only three of sixteen models (Claude Fable 5, GPT-5.6 Sol, and Claude Opus 4.8) finished a best run above the $1M they started with, and the hardcoded rule-based baseline outscored all of them. Most of the rest weren't bankrupt outright — several (Qwen 3.7 Max, Gemini 3.5 Flash, Kimi K2.6) stayed solvent for all 500 days but never grew the business — while four went bankrupt in every run they made. For sustained strategic decisions — multi-week planning, resource allocation, consequential pivots — run frontier-tier models, or consider whether a well-designed rule system covers the case better. Intermediate tiers are appropriate for execution tasks where the strategy is already decided. Mixing tiers without explicit boundary conditions is how you get a bankrupt simulation on autopilot.

---

## One More Finding

The rule-based baseline finishing first — ahead of every LLM tested — is the most uncomfortable result in the paper. A set of hardcoded heuristics — no language model, no reasoning, no token cost — beat all sixteen state-of-the-art AI systems it was tested against, in a task explicitly designed to test strategic intelligence ([CEO-Bench paper](https://arxiv.org/abs/2606.18543)).

The likely explanation is not that LLMs are worse than rules. It's that the rule-based system doesn't hallucinate, doesn't over-fit to recent signals, and doesn't change its strategy mid-run based on convincing-but-wrong inferences. Its consistency is also its advantage.

The practical lesson: for any decision loop where the right behavior is well-understood and stable, encode it as a rule before reaching for a model. Use LLMs for decisions that genuinely require reasoning about novel situations. The boundary between those two categories is where your architecture design work should go.

---

**[CEO-Bench (arXiv 2606.18543)](https://arxiv.org/abs/2606.18543)** is open-source on GitHub at [github.com/zlab-princeton/ceobench-src](https://github.com/zlab-princeton/ceobench-src). The simulation is runnable. If your production system does anything that resembles sustained multi-week resource management under uncertainty, running your own agents through it will tell you more than most benchmarks.
