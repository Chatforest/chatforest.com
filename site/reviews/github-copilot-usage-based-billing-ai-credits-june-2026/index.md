# GitHub Copilot's New Billing Starts June 1: What Your $10 and $39 Actually Buy Now

> GitHub Copilot moves to token-based AI Credits on June 1, 2026. Premium requests are gone. Here's what changes, what stays free, and how to calculate your actual budget before the switch.


On **June 1, 2026**, GitHub Copilot's billing model changes fundamentally. [Premium Request Units](https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/copilot-requests) (PRUs), which GitHub [introduced on June 18, 2025](https://github.blog/changelog/2025-06-18-update-to-github-copilot-consumptive-billing-experience/) as the metering unit for paid Copilot plans (not since Copilot's original launch), are being [replaced by GitHub AI Credits](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) — a token-based system where your plan includes a dollar-denominated credit pool, and each model interaction draws from it.

Plan prices are not changing. But what those prices buy is.

---

## The Short Version

| | Before June 1 | After June 1 |
|---|---|---|
| **Pro ($10/mo)** | 300 premium requests/mo | $10 in AI Credits/mo |
| **Pro+ ($39/mo)** | 1,500 premium requests/mo | $39 in AI Credits/mo |
| **Business ($19/user/mo)** | Shared request pool | $19 in AI Credits/user |
| **Enterprise ($39/user/mo)** | Shared request pool | $39 in AI Credits/user |
| **Code completions** | Free | Still free |
| **Next Edit Suggestions** | Free | Still free |
| **Chat / agent sessions** | Counted as requests | Billed by token × model rate |

Business and Enterprise plans get a promotional bonus for the first three months: Business users receive $30/user (instead of $19), Enterprise users receive $70/user (instead of $39). After that it drops to standard. ([Source: GitHub Blog announcement](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/))

> **Update (checked 2026-08-22):** GitHub has since raised the included pools beyond what it announced for the June 1 launch, and added a new top tier. The [live Copilot plans page](https://github.com/features/copilot/plans) currently lists Copilot Pro ($10/mo) with **$15** in monthly AI Credits and Copilot Pro+ ($39/mo) with **$70** — both higher than the $10 and $39 figures GitHub announced at rollout and used throughout this piece's original analysis, and unchanged since the last check on 2026-07-29. GitHub has also since added a **Copilot Max** plan (also on the live plans page): $100/mo for **$200** in monthly AI Credits, sitting above Pro+ — this tier did not exist at the time of this piece's original analysis. If you're budgeting today, check the live plans page for current allotments; the math below reflects the numbers as announced at the June 1 launch.

---

## What's an AI Credit?

**[1 AI Credit = $0.01 USD.](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)**

When you have a chat session or run an agentic task, the interaction consumes input tokens, output tokens, and cached tokens. GitHub converts those token counts to dollar amounts using published per-model API rates, then deducts from your credit pool.

Code completions and Next Edit Suggestions — the autocomplete features that fill in lines as you type — are **not billed in AI Credits**. They remain included in all paid plans at no additional cost.

The billing shift affects everything else: Copilot Chat in your IDE, Copilot in the browser, Copilot Workspace, agent mode sessions, and AI-powered code review.

---

## Model Pricing

These are the per-million-token rates that determine your credit consumption, as published on [GitHub's Copilot model pricing reference](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing). (Rates are in USD and convert directly to AI Credits at $0.01/credit.) GitHub updates this model lineup frequently — always check the live page for current rates before budgeting.

### OpenAI Models

| Model | Input ($/1M) | Cached Input | Output ($/1M) |
|-------|-------------|--------------|---------------|
| GPT-5 mini | $0.25 | $0.025 | $2.00 |
| GPT-5.4 mini | $0.75 | $0.075 | $4.50 |
| GPT-5.4 | $2.50 | $0.25 | $15.00 |
| GPT-5.5 | $5.00 | $0.50 | $30.00 |

*(GPT-4.1 and GPT-5.2, listed in this table at original publication, no longer appear in GitHub's current pricing reference — GitHub's model lineup has turned over since May 2026. Their original rates could not be re-verified against a live primary source, so they've been removed rather than left uncited.)*

### Anthropic Models

| Model | Input ($/1M) | Cached Input | Cache Write | Output ($/1M) |
|-------|-------------|--------------|-------------|---------------|
| Claude Haiku 4.5 | $1.00 | $0.10 | $1.25 | $5.00 |
| Claude Sonnet 4.6 | $3.00 | $0.30 | $3.75 | $15.00 |
| Claude Opus 4.7 | $5.00 | $0.50 | $6.25 | $25.00 |

### Google Models

| Model | Input ($/1M) | Cached Input | Output ($/1M) |
|-------|-------------|--------------|---------------|
| Gemini 3.5 Flash | $1.50 | $0.15 | $9.00 |

*(Gemini 2.5 Pro, listed in this table at original publication, no longer appears in [GitHub's current pricing reference](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing) — it has been superseded by Gemini 3.1 Pro, a different model with different per-token rates. Its original rate could not be re-verified as still live, so it's been removed rather than left uncited.)*

Note: Gemini models were [removed from Copilot Chat on the web](https://github.blog/changelog/2026-05-20-updates-to-available-models-in-copilot-on-web/) in May 2026. That changelog covers only the web chat surface; Gemini 3.5 Flash still carries an active per-token rate in [GitHub's Copilot pricing reference](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing), indicating it remains billable on other Copilot surfaces. As of this 2026-08-22 audit, GitHub's overall model lineup has grown substantially beyond what's shown in these three tables (additional OpenAI, Anthropic, Google, and third-party model variants) — the rates above remain accurate for the models listed, but check the live pricing reference for the full current catalog before budgeting.

---

## What This Means in Practice

The critical question for any Copilot user: **how far does my monthly credit pool actually go?**

### Quick chat session (lightweight)

A typical Q&A or code explanation: ~10K input tokens, ~1K output tokens.

- With GPT-5 mini: (10K × $0.25/M) + (1K × $2.00/M) = **$0.0025 + $0.002 = ~$0.005** — basically free
- With Claude Sonnet 4.6: (10K × $3.00/M) + (1K × $15.00/M) = **$0.03 + $0.015 = ~$0.045**
- With GPT-5.4: (10K × $2.50/M) + (1K × $15.00/M) = **$0.025 + $0.015 = ~$0.04**

Quick chat with budget models is extremely cheap. The economics only shift when you go agentic.

### Agentic coding session (heavy)

An agentic task — "refactor this module," "write tests for this class" — involves a large codebase context. Realistic estimates: 150K input tokens, 15K output tokens.

- With GPT-5 mini: (150K × $0.25/M) + (15K × $2.00/M) = **$0.0375 + $0.03 = ~$0.07**
- With Claude Sonnet 4.6: (150K × $3.00/M) + (15K × $15.00/M) = **$0.45 + $0.225 = ~$0.675**
- With GPT-5.4: (150K × $2.50/M) + (15K × $15.00/M) = **$0.375 + $0.225 = ~$0.60**
- With GPT-5.5: (150K × $5.00/M) + (15K × $30.00/M) = **$0.75 + $0.45 = ~$1.20**

### Sessions per month on each plan

| Scenario | Model | Cost/Session | Pro ($10) | Pro+ ($39) |
|----------|-------|-------------|-----------|-----------|
| Light chat | GPT-5 mini | ~$0.005 | 2,000+ | 7,800+ |
| Light chat | Claude Sonnet | ~$0.05 | ~200 | ~780 |
| Agentic task | GPT-5 mini | ~$0.07 | ~143 | ~557 |
| Agentic task | Claude Sonnet | ~$0.68 | **~15** | **~57** |
| Agentic task | GPT-5.4 | ~$0.60 | **~17** | **~65** |
| Agentic task | GPT-5.5 | ~$1.20 | **~8** | **~33** |

Based on the per-session costs above, a Pro+ user running a full day of mixed agentic workflow — a handful of chat exchanges plus several agentic sessions on flagship models — could plausibly burn **$10–14** in credits in a single day. At the **$39 pool GitHub originally announced**, that pace would exhaust a monthly Pro+ budget in **3–4 days** of sustained heavy use; at the current $70 pool (see the update note above), it stretches closer to a week.

---

## Who's Most Affected

**Unaffected or better off:**
- Developers who use Copilot primarily for autocomplete (completions are free)
- Light chat users who stick to budget models like GPT-5 mini
- Business/Enterprise teams who benefit from credit pooling — no more stranded per-seat allowances
- Annual subscribers — you keep your existing rate until your plan expires

**Most affected:**
- Pro ($10/mo) users running agentic tasks with flagship models (GPT-5.4, Claude Sonnet, GPT-5.5)
- Developers who previously relied on "fallback models" — [GitHub is eliminating fallback experiences](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/); you now choose a model and pay its rate
- Anyone who interpreted "1,500 premium requests" as meaning "unlimited within reason" — the new system exposes the real cost directly

---

## What Happens If You Run Out

When your included credit pool is exhausted:

- **Individual plans:** Code completions and Next Edit Suggestions keep working regardless. AI Credit-consuming features stop once the included pool runs out unless you set a spending limit for additional usage — GitHub's billing docs put it as needing to "continue working by setting a budget for additional usage," and note that additional usage may itself be capped. ([Source: GitHub Docs — usage-based billing for individuals](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals))
- **Business/Enterprise:** Additional usage is enabled by default, billed "at published per-credit rates" and charged to the org; an admin can disable this so usage instead "is blocked until the next billing cycle when monthly amounts are refreshed." Admins get further controls via user-, cost-center-, and org-level budgets. ([Source: GitHub Docs — usage-based billing for organizations and enterprises](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises))

If you're on a **monthly Pro or Pro+ plan**, the transition to AI Credits is automatic on June 1. No action required.

If you're on an **annual Pro or Pro+ plan**, you keep your existing pricing and premium request structure until your plan expires — GitHub's announcement states annual subscribers "will remain on their existing plan with premium request-based pricing until their plan expires." When it does, you transition to a monthly plan with AI Credits. ([Source: GitHub Blog announcement](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/))

---

## The Bigger Picture

GitHub's move mirrors what OpenAI, Anthropic, and Google have been doing on their platforms for years: align developer costs with actual model usage. The old request-based system was designed for autocomplete-era Copilot — a model that answered individual questions. The agentic Copilot that runs multi-step tasks across your codebase is fundamentally different, and the economics needed to catch up.

The criticism is valid: for heavy agentic users, the included credit pools are thin. A Pro user doing serious agentic work with flagship models will likely run out before mid-month. The old "1,500 premium requests" felt generous partly because it was vague — it was easy not to know you were burning through it. Token pricing makes the cost explicit.

For developers comparing options after the switch:

- **[Cursor Pro](https://cursor.com/pricing) ($20/mo)** includes unlimited Auto mode, which routes to a cost-efficient model at no charge, while manually selecting a premium model (Claude, GPT, Gemini) draws from a $20 monthly credit pool
- **Claude Code** (included with [Claude Pro or Max plans](https://claude.com/pricing), $20–$200/mo) uses Anthropic's native token pool
- **OpenAI Codex** (included with [ChatGPT Plus and Pro](https://chatgpt.com/pricing/)) similarly draws from a usage pool

The market is converging on token-based pricing with tiered credit pools. GitHub Copilot is late to this transition, not pioneering it.

---

## Our Take

The shift is structurally sound — token pricing is fairer than opaque request counts when models and session sizes vary this much. But the included credit pools feel sized for a Copilot that doesn't yet exist for most users: one where agents handle complete features autonomously. In the current reality, where agentic sessions still require significant steering, the pool runs out fast if you're doing serious work.

If you're a light-to-moderate Copilot user who relies on autocomplete and occasional chat, June 1 changes almost nothing. If you're running agentic sessions daily with Claude Sonnet or GPT-5.4 on a Pro plan, you'll hit the wall before the month is half over.

The practical advice before June 1: know which model you actually use. If it's a budget model, you'll be fine. If it's a flagship model and you're agentic, do the math on your usage and consider whether Pro+ or Business pricing makes sense.

---

*For a broader comparison of how Copilot stacks up against Cursor, Claude Code, Windsurf, and others, see our [AI coding assistants comparison guide](/guides/ai-coding-assistants-compared/).*

