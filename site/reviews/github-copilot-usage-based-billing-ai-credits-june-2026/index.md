# GitHub Copilot's New Billing Starts June 1: What Your $10 and $39 Actually Buy Now

> GitHub Copilot moves to token-based AI Credits on June 1, 2026. Premium requests are gone. Here's what changes, what stays free, and how to calculate your actual budget before the switch.


On **June 1, 2026**, GitHub Copilot's billing model changes fundamentally. The [Premium Request Units](https://github.com/features/copilot/plans) (PRUs) that have defined plan limits since Copilot launched are being replaced by **GitHub AI Credits** — a token-based system where your plan includes a dollar-denominated credit pool, and each model interaction draws from it.

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

Business and Enterprise plans get a promotional bonus for the first three months: Business users receive $30/user (instead of $19), Enterprise users receive $70/user (instead of $39). After that it drops to standard.

---

## What's an AI Credit?

**1 AI Credit = $0.01 USD.**

When you have a chat session or run an agentic task, the interaction consumes input tokens, output tokens, and cached tokens. GitHub converts those token counts to dollar amounts using published per-model API rates, then deducts from your credit pool.

Code completions and Next Edit Suggestions — the autocomplete features that fill in lines as you type — are **not billed in AI Credits**. They remain included in all paid plans at no additional cost.

The billing shift affects everything else: Copilot Chat in your IDE, Copilot in the browser, Copilot Workspace, agent mode sessions, and AI-powered code review.

---

## Model Pricing

These are the per-million-token rates that determine your credit consumption. (Rates are in USD and convert directly to AI Credits at $0.01/credit.)

### OpenAI Models

| Model | Input ($/1M) | Cached Input | Output ($/1M) |
|-------|-------------|--------------|---------------|
| GPT-5 mini | $0.25 | $0.025 | $2.00 |
| GPT-4.1 | $2.00 | $0.50 | $8.00 |
| GPT-5.4 mini | $0.75 | $0.075 | $4.50 |
| GPT-5.2 | $1.75 | $0.175 | $14.00 |
| GPT-5.4 | $2.50 | $0.25 | $15.00 |
| GPT-5.5 | $5.00 | $0.50 | $30.00 |

### Anthropic Models

| Model | Input ($/1M) | Cached Input | Cache Write | Output ($/1M) |
|-------|-------------|--------------|-------------|---------------|
| Claude Haiku 4.5 | $1.00 | $0.10 | $1.25 | $5.00 |
| Claude Sonnet 4.6 | $3.00 | $0.30 | $3.75 | $15.00 |
| Claude Opus 4.7 | $5.00 | $0.50 | $6.25 | $25.00 |

### Google Models

| Model | Input ($/1M) | Cached Input | Output ($/1M) |
|-------|-------------|--------------|---------------|
| Gemini 2.5 Pro | $1.25 | $0.125 | $10.00 |
| Gemini 3.5 Flash | $1.50 | $0.15 | $9.00 |

Note: Gemini models were [removed from Copilot Chat on the web](https://github.blog/changelog/2026-05-20-updates-to-available-models-in-copilot-on-web/) in May 2026 but remain available via the API.

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

One independent analysis found a typical Pro+ user doing a full day of mixed agentic workflow could consume $10–14 in credits. At that rate, a **$39 monthly Pro+ budget runs out in 3–4 days** of heavy use.

---

## Who's Most Affected

**Unaffected or better off:**
- Developers who use Copilot primarily for autocomplete (completions are free)
- Light chat users who stick to budget models like GPT-5 mini
- Business/Enterprise teams who benefit from credit pooling — no more stranded per-seat allowances
- Annual subscribers — you keep your existing rate until your plan expires

**Most affected:**
- Pro ($10/mo) users running agentic tasks with flagship models (GPT-5.4, Claude Sonnet, GPT-5.5)
- Developers who previously relied on "fallback models" — GitHub is eliminating fallbacks; you now choose a model and pay its rate
- Anyone who interpreted "1,500 premium requests" as meaning "unlimited within reason" — the new system exposes the real cost directly

---

## What Happens If You Run Out

When your included credit pool is exhausted:

- **Individual plans:** Copilot pauses AI Credit-consuming features until the next billing cycle. Code completions continue.
- **Business/Enterprise:** Admins can configure budget controls and set whether to allow overage spending (at published rates) or cap usage at the included pool.

If you're on a **monthly Pro or Pro+ plan**, the transition to AI Credits is automatic on June 1. No action required.

If you're on an **annual Pro or Pro+ plan**, you keep your existing pricing and premium request structure until your plan expires. When it does, you transition to a monthly plan with AI Credits.

---

## The Bigger Picture

GitHub's move mirrors what OpenAI, Anthropic, and Google have been doing on their platforms for years: align developer costs with actual model usage. The old request-based system was designed for autocomplete-era Copilot — a model that answered individual questions. The agentic Copilot that runs multi-step tasks across your codebase is fundamentally different, and the economics needed to catch up.

The criticism is valid: for heavy agentic users, the included credit pools are thin. A Pro user doing serious agentic work with flagship models will likely run out before mid-month. The old "1,500 premium requests" felt generous partly because it was vague — it was easy not to know you were burning through it. Token pricing makes the cost explicit.

For developers comparing options after the switch:

- **Cursor Pro ($20/mo)** operates on a credit pool for premium models, with auto mode unlimited on GPT-4.1-level models and premium model selections drawing credits
- **Claude Code** (included with Claude Max at $20–$200/mo) uses Anthropic's native token pool
- **OpenAI Codex** (included with ChatGPT Plus/Pro) similarly draws from a usage pool

The market is converging on token-based pricing with tiered credit pools. GitHub Copilot is late to this transition, not pioneering it.

---

## Our Take

The shift is structurally sound — token pricing is fairer than opaque request counts when models and session sizes vary this much. But the included credit pools feel sized for a Copilot that doesn't yet exist for most users: one where agents handle complete features autonomously. In the current reality, where agentic sessions still require significant steering, the pool runs out fast if you're doing serious work.

If you're a light-to-moderate Copilot user who relies on autocomplete and occasional chat, June 1 changes almost nothing. If you're running agentic sessions daily with Claude Sonnet or GPT-5.4 on a Pro plan, you'll hit the wall before the month is half over.

The practical advice before June 1: know which model you actually use. If it's a budget model, you'll be fine. If it's a flagship model and you're agentic, do the math on your usage and consider whether Pro+ or Business pricing makes sense.

---

*For a broader comparison of how Copilot stacks up against Cursor, Claude Code, Windsurf, and others, see our [AI coding assistants comparison guide](/guides/ai-coding-assistants-compared/).*

