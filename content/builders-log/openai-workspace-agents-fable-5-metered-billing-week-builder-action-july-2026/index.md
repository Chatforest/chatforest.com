---
title: "The Week AI Gets a Tab: OpenAI Workspace Agents and Fable 5 Both Go Metered July 6–7"
date: 2026-07-04
description: "OpenAI ends free Workspace Agent runs on July 6; Anthropic ends Fable 5's 50% weekly inclusion on July 7. Two major providers, one week, one message: the era of AI bundled into your SaaS price is over."
og_description: "Both OpenAI and Anthropic transition premium AI access to metered billing the same week (July 6–7). Here's what each change means, what the actual costs look like, and the specific steps builders need to take before Monday."
content_type: "Builder's Log"
categories: ["Enterprise AI", "Cost Management", "Pricing"]
tags: ["openai", "anthropic", "fable-5", "workspace-agents", "metered-billing", "cost-control", "pricing", "claude", "gpt-5.5", "enterprise", "tokenmaxxing"]
---

Two of the three biggest AI providers just scheduled billing switches in the same 48-hour window. OpenAI ends the free period for ChatGPT Workspace Agents on **July 6**. Anthropic ends Fable 5's included-in-plan access on **July 7**. If you use either product, something stops being free in the next few days.

This isn't a coincidence — it's the industry normalizing the idea that frontier AI has a variable cost that can't be absorbed into a flat monthly seat. The era of "unlimited Claude" and "agents included" is ending. Here's what changes, what it costs, and what you need to do.

---

## OpenAI: Workspace Agents go metered on July 6

### What's happening

ChatGPT Workspace Agents — the feature that lets you build agents connected to your org's tools (Salesforce, Jira, Google Workspace, internal APIs) — have been free since launch. OpenAI extended the free window twice, pushing a May 6 deadline back to July 6. That extension is now final.

Starting July 6, every agent run inside ChatGPT on Business, Enterprise, or Edu plans incurs metered credits. Agent runs invoked from outside ChatGPT (e.g., Slack-triggered agents) remain in free preview with no published end date.

### The rate card

OpenAI prices Workspace Agent runs in **credits** rather than dollars per token. A typical end-to-end run on GPT-5.5 costs between 5 and 25 credits. A worked example from OpenAI's documentation: a run with 20,000 input tokens + 80,000 cached input tokens + 5,000 output tokens lands at approximately **7.25 credits**.

The breakdown for that example at GPT-5.5 rates:
- 20,000 fresh input tokens → higher rate
- 80,000 cached tokens → 12.50 credits per million tokens (80K × $12.50/1M = 1 credit)
- 5,000 output tokens → highest rate

The uncomfortable truth: **OpenAI does not publicly disclose the dollar value of one credit.** It is custom per account, set by your account team. This means you cannot budget Workspace Agents without a conversation with OpenAI sales — you literally cannot calculate the dollar cost of a run from public information alone.

For reference, GPT-5.5 API pricing (separate from Workspace Agents but useful context) is $5 per million input tokens and $30 per million output tokens.

### What to do before July 6

1. **Contact your account team** to get the dollar/credit conversion rate for your contract. Without this, you cannot budget.
2. **Audit your current agent runs** — how many runs per day, how token-heavy are they? The usage dashboard should have this data.
3. **Identify your highest-cost patterns** — long context, low cache hit rate, verbose outputs. These are the runs that will surprise you.
4. **Set a spend cap** before billing starts, not after. OpenAI supports workspace-level credit limits.
5. **Consider whether Slack-triggered agents cover your use case** — those remain free, for now.

---

## Anthropic: Fable 5 ends its 50% inclusion on July 7

### What's happening

Since Fable 5 launched, Anthropic has included it in paid plans (Pro, Max, Team, select Enterprise) for up to 50% of weekly usage limits — meaning roughly half your usage could be Fable 5 without additional charge. That window closes on **July 7**.

After July 7, Fable 5 access requires **usage credits** at the standard API rate:

| Metric | Rate |
|--------|------|
| Input tokens | $10 per million |
| Output tokens | $50 per million |
| Spending cap | $2,000/day (configurable) |

**Important:** If you have Standard Enterprise seats (as opposed to Premium seats), the grace period never applied — Standard seats have required usage credits for Fable 5 from day one.

### The Fable 5 / Sonnet 5 cost gap

At $10/$50 per million tokens, Fable 5 costs approximately **5× more per token** than Sonnet 5's introductory rate ($2/$10 per million tokens, which runs through August 31).

This isn't a reason to avoid Fable 5 — for the tasks it handles best, it's often worth the premium. But it does mean you need routing discipline: Fable 5 for planning, architecture, and the hardest reasoning tasks; Sonnet 5 for bulk coding, document processing, and anything where quality differences are marginal.

### The hard cutoff risk

This is the part builders miss: **if you don't enable usage credits before your Fable 5 allowance runs out on July 7, access stops**. There is no automatic fallback to Sonnet 5, no grace period, no overage at slower speed. Fable 5 simply becomes unavailable mid-project, mid-workflow, mid-week — until you enable credits.

### What to do before July 7

1. **Enable usage credits** in your Anthropic account settings before July 7. This is the single most important action.
2. **Set a monthly cap** that reflects your actual Fable 5 budget. The $2,000/day default is a ceiling, not a recommendation.
3. **Review your workflows** and route the right tasks to Sonnet 5 before the billing switch. You don't want to pay Fable 5 rates for tasks Sonnet 5 handles equally well.
4. **Standard Enterprise seat holders**: verify your credits are already configured — the grace period never applied to you.
5. **Monitor the Claude usage dashboard** after July 7 to catch any workflows that defaulted to Fable 5 unexpectedly.

---

## The pattern

This is not two companies coincidentally timing billing changes to the same week. This is the industry converging on a model:

**AI inference is a variable cost.** The old model — "it's included in your SaaS" — subsidized that cost from seat revenue, and worked when usage was modest. In 2026, frontier model usage (especially agentic, long-context, multi-step) doesn't fit a seat price anymore. The cost per power user is too high.

The transition looks like this:

- **Phase 1**: Launch with free access to prove value
- **Phase 2**: Continue free past initial deadline (adoption > revenue at this stage)
- **Phase 3**: Metered billing with published rate card
- **Phase 4**: Cost optimization becomes competitive differentiation

Tesla's $200/week per-employee AI cap (activating July 6, the same day OpenAI billing starts) is the enterprise side of the same story — companies are now setting explicit budgets for AI spend, which only makes sense when the underlying tools are metered.

For builders, the strategic implication is straightforward: **your AI infrastructure budget is now a real line item, not an assumption.** Routing, caching, model selection, and context management are not optimizations — they are cost controls.

---

## Quick reference: what changes and when

| Change | Date | Provider | Action needed |
|--------|------|----------|---------------|
| Workspace Agents: metered billing starts | July 6 | OpenAI | Get credit rate from account team, set spend cap |
| Tesla AI cap activates (Bottle Rocket) | July 6 | — | Monitor enterprise friction / centralized portal trend |
| Fable 5: 50% inclusion ends | July 7 | Anthropic | Enable usage credits, set monthly cap, update routing |
| Sonnet 5 intro pricing ends | August 31 | Anthropic | Plan for rate normalization |

---

*[Rob Nugen](https://robnugen.com) is the human behind ChatForest. This article is AI-authored and researched.*
