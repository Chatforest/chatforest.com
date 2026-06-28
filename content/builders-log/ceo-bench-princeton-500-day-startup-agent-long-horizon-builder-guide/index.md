---
title: "Princeton Ran 12 AI Agents as Startup CEOs for 500 Days — 9 Went Bankrupt: The Builder's Breakdown"
date: 2026-06-29
description: "CEO-Bench, a new Princeton benchmark, simulates a 500-day AI startup with $1M starting capital and measures which models stay solvent. Only 3 of 12 survived. A rule-based system beat most frontier LLMs. Here is what broke the rest — and what it means for your agentic deployments."
og_description: "Princeton's CEO-Bench: 12 AI agents ran a simulated startup for 500 days. 9 went bankrupt. A hardcoded rule system beat most frontier LLMs. The failure modes map directly to what breaks production AI agents."
content_type: "Builder's Log"
categories: ["AI Agents", "Research", "Benchmarks"]
tags: ["ceo-bench", "princeton", "ai-agents", "long-horizon", "benchmarks", "agentic", "builder-guide", "june-2026", "research"]
---

Princeton researchers handed 12 AI agents a startup, $1 million in simulated capital, and 500 days. Most of them failed to stay in business.

The research — **CEO-Bench: Can Agents Play the Long Game?** from Princeton's zLab (arXiv 2606.18543), published June 2026 — is not another benchmark measuring whether an AI can write a SQL query or pass a coding challenge. It measures something much harder to fake: **sustained strategic execution under uncertainty, over time, with interconnected consequences and no clean feedback signal**.

The results are a useful corrective to the current wave of agentic hype. Nine of twelve evaluated models went bankrupt before day 500. A simple rule-based system — no LLM, just hardcoded heuristics — finished third. The best model hit $47.15M. The theoretical maximum is $2.2 billion. Even the winner achieved roughly 2% of what an optimal agent could do.

---

## What CEO-Bench Tests

The benchmark is a playable Python simulation of an AI startup. Agents start with $1,000,000 in cash and run the company across 500 simulated days. They control pricing, marketing spend, product development investment, support quality, enterprise sales effort, and social media strategy. Success is measured by one number: final cash balance.

The environment is deliberately hard in ways that matter:

- **Hidden customer preferences** — agents must infer segment demand from indirect signals
- **Delayed feedback** — product improvements take weeks to move revenue; costs hit immediately
- **Competitor pressure** — market share shifts without announcement
- **Noisy data** — databases include errors; signals require interpretation
- **Coupled decisions** — pricing changes affect multiple customer segments simultaneously, with non-obvious interactions

None of these characteristics are exotic. Every one of them appears in real product businesses. CEO-Bench's authors call this "steering intelligence" — the ability to navigate toward a long-horizon objective when the path is unclear and consequences compound.

---

## The Leaderboard

| Rank | Model | Best Run Cash | Notes |
|------|-------|---------------|-------|
| 1 | Claude Fable 5 | $47.15M | 0 bankruptcies across all runs |
| 2 | Claude Opus 4.8 | $27.78M | Consistently solvent |
| 3 | GPT-5.5 | $21.30M | 2 bankruptcies out of 3 runs |
| 4 | **Rule-based baseline** | $15.76M | Hardcoded heuristics, no LLM |
| 5–12 | All others | <$500K | Most went bankrupt |

Models that went bankrupt: Claude Opus 4.7, Claude Sonnet 4.6, Kimi K2.6, Gemini 3 Flash, GLM-5.1, Claude Haiku 4.5, DeepSeek V4 Pro, Grok 4.20 Reasoning.

Two things in this table warrant attention.

**First**: The gap between ranks 3 and 4 is the model frontier versus a rule-based system. GPT-5.5 at $21.3M, then hardcoded rules at $15.76M, then everything else under $500K and mostly bankrupt. The rule-based system did not use language models at all. It applied fixed heuristics — if cash below threshold, cut marketing; if customer satisfaction low, increase product investment. It beat nine LLMs, including models that cost 10–100x more per token to run.

**Second**: Claude Fable 5 leads the leaderboard, and Claude Fable 5 has been suspended from general access since June 12 by US government directive. The best-tested model for long-horizon agentic work is currently unavailable. Builders planning agentic architectures around Fable 5's capabilities are in a holding pattern until general access is restored. The next best is Opus 4.8, available now.

---

## The Four Failure Modes

The researchers identify four structural challenges that separate models that survived from those that went bankrupt. These are not arbitrary simulation quirks — they recur in real production agentic systems.

### 1. Delayed Feedback Loops

In CEO-Bench, the cost of an action (hiring, product investment, marketing) is immediate. The revenue effect arrives weeks later. Most lower-ranked models treated the simulation as a short-horizon optimization problem: maximize this week's revenue, cut this week's costs. The result is rational-looking decisions that accumulate into structural decline — too much cost-cutting dries out product quality; delayed returns never arrive before cash runs out.

**Builder mapping**: Any agentic loop that runs actions with multi-week revenue consequences — content strategies, SEO initiatives, product development prioritization, sales pipeline nurturing — has this same mismatch. Agents evaluated on immediate outputs will optimize for visible short-term signals and hollow out long-term value.

### 2. Hidden State

Customer satisfaction in CEO-Bench is never directly observed. Agents must infer it from indirect signals: churn rates, support ticket volume, negotiation behavior. Weaker models either ignored it (treating the problem as if all state were observable) or over-anchored on noisy proxies.

Top performers wrote code to simulate customer cohorts and infer hidden preferences from negotiation outcomes — treating the inference problem explicitly rather than hoping the satisfaction signal would surface.

**Builder mapping**: Any system where ground-truth quality is measured downstream — user retention, NPS, actual conversion vs. predicted conversion — has this problem. Agents that can only optimize on directly measurable signals will fail when the important state is latent.

### 3. Non-Stationary Environments

The market in CEO-Bench drifts. Competitors respond to moves. Customer preferences evolve. Strategies that worked in month 2 fail in month 8. Models that learned early patterns and held them went bankrupt on schedule.

The researchers tracked development investment allocation as a differentiator: top models targeted 87–89% of product spend toward specific customer-segment improvements, reallocating as conditions changed. Weaker models allocated 10–44% of spend with low targeting precision — broad bets that produced diffuse results.

**Builder mapping**: Production agentic systems with fixed strategy loops — where the initial plan is never revised against new evidence — face exactly this drift. Agents need explicit re-evaluation cadences, not just execution loops.

### 4. Coupled Consequences

Pricing in the simulation affects multiple customer segments at the same time, with cross-effects. Cutting prices for one segment can cannibalize another. Marketing spend affects satisfaction and acquisition simultaneously. Models that reasoned about one dimension in isolation while ignoring cross-effects made locally rational decisions that were globally catastrophic.

Top runs showed significantly more conditional reasoning: "if-then" statements that anticipated downstream coupling before taking an action. The model wasn't just deciding; it was stress-testing the decision against interconnected effects before committing.

**Builder mapping**: In any system where actions have externalities across components — pricing, resource allocation, deployment configuration — agents need explicit multi-axis reasoning rather than sequential single-factor optimization.

---

## What the Top Models Did Differently

Three behavioral signatures distinguish the models that stayed solvent:

**Explicit simulation over implicit intuition.** Top runs generated code mid-run to forecast cash scenarios and model customer cohort behavior. They did not trust their intuition about how a decision would ripple forward — they built temporary tools to test the hypothesis before acting.

**Targeted investment over diffuse spending.** 87–89% of development spend targeted specific customer segments identified through analysis, versus 10–44% for weaker models. Frontier models produced sharper hypotheses about where investment would produce measurable return.

**Anticipatory reasoning.** Top runs contained materially more if-then conditional planning — scenarios prepared in advance, contingency triggers set before events occurred. This is different from reactive adaptation after something goes wrong.

---

## The Upper Bound Problem

The estimated theoretical maximum for CEO-Bench is approximately $2.2 billion. The best model achieved $47.15 million — about 2% of the optimum. The benchmark is far from saturated.

This is worth internalizing. The models that survived the simulation are the best available — Fable 5, Opus 4.8, GPT-5.5. Against a plausible upper bound, they're near the floor. The gap is not a narrow performance deficit. It represents the difference between surviving and thriving.

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
CEO-Bench shows a hard cliff between ranks 3 and 4: the top three models stayed solvent, everything else went bankrupt. For sustained strategic decisions — multi-week planning, resource allocation, consequential pivots — run frontier-tier models. Intermediate tiers are appropriate for execution tasks where the strategy is already decided. Mixing tiers without explicit boundary conditions is how you get a bankrupt simulation on autopilot.

---

## One More Finding

The rule-based baseline finishing third is the most uncomfortable result in the paper. A set of hardcoded heuristics — no language model, no reasoning, no token cost — beat nine state-of-the-art AI systems in a task explicitly designed to test strategic intelligence.

The likely explanation is not that LLMs are worse than rules. It's that the rule-based system doesn't hallucinate, doesn't over-fit to recent signals, and doesn't change its strategy mid-run based on convincing-but-wrong inferences. Its consistency is also its advantage.

The practical lesson: for any decision loop where the right behavior is well-understood and stable, encode it as a rule before reaching for a model. Use LLMs for decisions that genuinely require reasoning about novel situations. The boundary between those two categories is where your architecture design work should go.

---

**CEO-Bench (arXiv 2606.18543)** is open-source on GitHub at github.com/zlab-princeton/ceobench-src. The simulation is runnable. If your production system does anything that resembles sustained multi-week resource management under uncertainty, running your own agents through it will tell you more than most benchmarks.
