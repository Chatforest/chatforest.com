# GitHub Copilot's Flat Pricing Era Is Over. Here's What the New Token Billing Means for Builders.

> GitHub switched GitHub Copilot from Premium Request Units to token-metered AI Credits on June 1, 2026. Code completions are still free. Everything agentic now bills at actual compute cost. Here is what changed, what it costs, and what builders should do.


GitHub [replaced its Premium Request Unit (PRU) billing system with token-metered AI Credits on June 1, 2026](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/). If you use GitHub Copilot for chat, code review, or agent mode, the economics changed today. If you only use [code completions and Next Edit Suggestions, nothing changed](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals).

The short version: the flat-rate PRU system is gone for new usage. You now pay [actual token costs, converted to credits at $0.01 per credit](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing). The model catalog expanded significantly, annual plan holders face sharply higher multipliers on expensive models (see below), and there is [no longer a "fall back to a cheaper model" escape hatch](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) when you run out of budget.

---

## What Changed and What Didn't

**Free (unlimited on all paid plans, unchanged):**
- Code completions
- Next Edit Suggestions

**[Now metered against AI credits](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals):**
- Copilot Chat (IDE, github.com, mobile)
- Copilot CLI
- Agent mode in VS Code and JetBrains
- Copilot Workspace (cloud agent)
- Copilot Spaces
- Spark
- Third-party coding agents integrated via Copilot
- [Code review — and as of June 1, also consumes GitHub Actions minutes for private repos](https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026/)

The billing unit is now actual tokens: [input tokens, output tokens, and cached tokens](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing), priced per model. One AI credit equals $0.01 USD.

---

## Credit Allotments Per Plan

GitHub introduced a [two-pool structure: **base credits** (guaranteed, match your monthly price 1:1) and **flex allotments** (variable bonus that GitHub can adjust over time)](https://docs.github.com/en/copilot/how-tos/manage-and-track-spending/prepare-for-your-move-to-usage-based-billing). Base credits are consumed first.

| Plan | Monthly Price | Base Credits | Flex Allotment | Total Included |
|------|-------------|-------------|----------------|----------------|
| Pro | $10 | 1,000 | 500 | 1,500 ($15) |
| Pro+ | $39 | 3,900 | 3,100 | 7,000 ($70) |
| Max | $100 | 10,000 | 10,000 | 20,000 ($200) |

**Organization and Enterprise plans:**

| Plan | Price Per User | Monthly Credits |
|------|--------------|----------------|
| Business | $19/user | 1,900/user |
| Enterprise | $39/user | 3,900/user |

**[Promotional credits (Business and Enterprise, June 1 – September 1, 2026)](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/):**
- Business: 3,000 credits/user
- Enterprise: 7,000 credits/user

[When credits run out, usage stops](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) — unlike the old system, where you'd silently fall back to a cheaper included model and keep working. If you want to keep going, you need to set an overage budget.

---

## Model Costs

All costs in USD per million tokens, [per GitHub's published rate card](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing). Multiply by 100 to get credits per million tokens (since $1.00/million = 100 credits/million).

**OpenAI models available in Copilot:**

| Model | Input ($/M) | Output ($/M) |
|-------|------------|-------------|
| GPT-5 mini / GPT-5.4 nano | $0.20–0.25 | $1.25–2.00 |
| GPT-5.3-Codex | $1.75 | $14.00 |
| GPT-5.4 | $2.50 | $15.00 |
| GPT-5.5 | $5.00 | $30.00 |

**Anthropic models available in Copilot:**

| Model | Input ($/M) | Output ($/M) |
|-------|------------|-------------|
| Claude Haiku 4.5 | $1.00 | $5.00 |
| Claude Sonnet 4/4.5/4.6 | $3.00 | $15.00 |
| Claude Opus 4.5/4.6/4.7/4.8 | $5.00 | $25.00 |

**Google models:**

| Model | Input ($/M) | Output ($/M) |
|-------|------------|-------------|
| Gemini 3 Flash | $0.50 | $3.00 |
| Gemini 2.5 Pro / Gemini 3.1 Pro | $1.25–2.00 | $10.00–12.00 |
| Gemini 3.5 Flash | $1.50 | $9.00 |

---

## The Agentic Session Problem

The billing change hits agentic workflows hardest. Under the PRU system, a 30-minute refactoring session and a one-line chat response both counted as a small number of "premium requests." Under token billing, each agent turn re-sends the accumulated context — file contents, prior tool-call outputs, the growing conversation — plus generates output. The token count compounds as the session progresses.

A conservative estimate of a single 30-minute refactoring session:
- Initial context: ~5K input tokens (files, instructions)
- Tool iterations (4 rounds): ~8K input tokens per round
- Final synthesis and output: ~3K output tokens
- **Total: approximately 37K tokens ≈ 265 credits**

That's 18% of a Pro plan's monthly allotment for one session. Pro plan holders who run heavy agentic workflows will exhaust their budget in roughly 4–5 sessions per month.

For Pro+ holders, the math is better: 7,000 credits ÷ 265 per session = ~26 sessions per month. Still finite, still trackable.

For Enterprise teams with complex long-context sessions and code review enabled, the compounding effect is real. GitHub provides [budget controls at four levels — user, cost center, organization, and enterprise](https://docs.github.com/en/copilot/concepts/billing/budgets-for-usage-based-billing) — which helps admins set guardrails before bills appear.

**Code review** carries an additional cost starting June 1: [private-repo reviews now consume GitHub Actions minutes at standard rates, in addition to AI credits; public repositories are unaffected](https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026/).

---

## Annual Plan Holders: What Changed

If you're on an annual Copilot plan, [you remain on the legacy PRU system until your plan expires](https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/what-changed-with-billing), but GitHub changed the per-model multipliers effective June 1. [The current multiplier table](https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/model-multipliers-for-annual-plans) for annual-plan holders:

| Model | Multiplier |
|-------|--------------|
| Claude Haiku 4.5 | 0.33 |
| Claude Sonnet 4.5 | 6 |
| Claude Sonnet 4.6 | 9 |
| Claude Opus 4.5 | 15 |
| Claude Opus 4.6/4.7/4.8 | 27 |
| GPT-5.5 | 57 |
| Gemini 3.5 Flash | 14 |
| Code review | 13 |

The headline number: if you're on an annual Pro+ plan and using Claude Opus 4.6, 4.7, or 4.8, every request against those models now costs 27 premium requests apiece — the highest multiplier on the table.

[Annual plan holders can switch to a monthly plan early and receive prorated credits for the remaining value of their term](https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/what-changed-with-billing). When a current annual term ends, GitHub automatically downgrades the account to Copilot Free unless the holder has already moved to a paid monthly plan.

---

## What Builders Should Do

**Check your actual usage pattern first.** If your Copilot workflow is primarily code completions, tab completion, and occasional chat questions, today's change has minimal impact. Credits last. If you're running agent-mode sessions, automated code review on every PR, or Copilot Workspace for multi-file tasks, audit your expected monthly token volume before you hit a wall.

**Set an overage budget if you need continuous operation.** The old system's silent fallback to a cheaper model kept you working even past budget. The new system stops you. If you have automated pipelines or production-adjacent agentic workflows on Copilot, configure an overage budget and set a cap that makes sense for your cost tolerance.

**Evaluate model selection deliberately.** The pricing spread between models is large. Gemini 3 Flash at $0.50/M input and $3.00/M output costs about 1/5 of Claude Sonnet on input and 1/5 on output. For lightweight tasks that don't require frontier reasoning — code review comments on obvious issues, docstring generation, simple refactors — routing to a cheaper model conserves credits for the sessions where frontier capability matters.

**Annual plan holders: recalculate your Opus budget.** If you were using Claude Opus 4.6 or 4.7 as your default agent model, run the new 27x multiplier math against your monthly PRU budget before your next billing cycle. The per-request cost went up; your budget didn't change.

**Enterprise teams: activate budget controls now.** GitHub's four-level budget controls (user, cost-center, org, enterprise) are available now. Without a budget ceiling, individual power users on agent mode can run significant overage charges before anyone notices. Set limits, monitor dashboards in the first billing cycle, then calibrate.

---

## Alternatives Worth Reconsidering

The billing change coincides with a moment when the standalone alternatives are more capable than they've ever been. Claude Code is an Anthropic-native terminal agent that runs on your Claude Pro or Claude Max subscription. Cursor runs on its own subscription model with model flexibility. Both offer pricing structures that may work out cheaper for developers whose workflows are primarily agent-mode and long-context sessions, rather than integrated IDE completion.

The right tool depends on your stack integration requirements. If you need GitHub PR workflows, Copilot Workspace, or native GitHub.com integration, Copilot is hard to replace. For terminal-first agentic workflows, the economics now favor comparison shopping.

---

GitHub's billing change reflects a real infrastructure cost: the flat-pricing model was a growth strategy, not a sustainable unit economics model for agentic workloads whose token consumption varies by orders of magnitude between sessions. The move to token billing aligns developer incentives with actual compute costs — which is probably healthy for the ecosystem long-term, even if it stings for power agentic users in the short term.

The documentation is in GitHub's [models and pricing reference](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing) and the [usage-based billing guides](https://docs.github.com/en/copilot/how-tos/manage-and-track-spending/prepare-for-your-move-to-usage-based-billing). The full billing announcement is at the [GitHub Blog](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/).

