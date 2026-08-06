---
title: "GitHub Copilot July 2026: App Open to All Plans, Browser Tools GA, JetBrains Agent Sessions, Credit Controls — Builder's Guide"
date: 2026-07-12
sources_audited: 2026-08-06
description: "GitHub Copilot shipped four significant updates in the first week of July 2026: the Copilot app is now available to Free and Education accounts, browser tools reached GA, Codex agent sessions landed in JetBrains IDEs for paid users, and new credit controls let you cap per-session and per-cost-center spend. Here is what changed and what it means for your setup."
tags: ["github-copilot", "copilot-app", "agentic-coding", "browser-tools", "jetbrains", "ai-credits", "developer-tools", "enterprise-ai", "cost-management"]
---

GitHub Copilot shipped four updates in the first week of July 2026, covering access expansion, browser automation stability, a new IDE, and cost controls. None of them require a model upgrade — they are platform and billing changes. But the access expansion in particular changes who can use Copilot's agent features, and the credit controls change how enterprise teams deploy agents without surprise invoices.

This is a research-based guide. We reviewed [GitHub's changelog](https://github.blog/changelog/2026-07-07-github-copilot-app-available-to-all/), [official blog posts](https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/), and the documentation. We did not run these features ourselves.

---

## 1. Copilot App Now Available on Every Plan (July 7)

Since June, the GitHub Copilot desktop app has been in technical preview for paid users. On July 7, [GitHub opened it to **all Copilot plans**](https://github.blog/changelog/2026-07-07-github-copilot-app-available-to-all/) — including Copilot Free and GitHub Education accounts.

What the app offers:

- **My Work view** — a single dashboard tracking active sessions, open issues, PRs, and automations across repositories
- **Sessions** — each session runs in an isolated git worktree: a physically separate directory with its own branch, so multiple sessions on the same codebase can run in parallel without file conflicts
- **Canvases** — a shared surface where agents update content and developers can edit, reorder, approve, or redirect agent work without restarting the task
- **Agent Merge** — automation that monitors CI, tracks required reviewers, addresses failing checks, and handles the PR-through-merge pipeline without continuous supervision
- **Cloud sandboxes** — ephemeral Linux environments for agent execution

**Access notes:**
- Free and Education users: sign in at github.com/features/copilot to download the app; you can also bring your own model provider API keys for sessions
- Business and Enterprise users: admins must enable **Copilot CLI** in the organization's Copilot policy settings before the desktop app is available to members

The Copilot Free tier has usage limits. The desktop app session features consume AI credits; [Free users have a limited monthly AI credit allowance](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals) that constrains how many agent sessions they can run.

---

## 2. Browser Tools Reach General Availability (July 1)

[Copilot's browser tools in VS Code moved from preview to GA on July 1](https://github.blog/changelog/2026-07-01-browser-tools-for-github-copilot-in-vs-code-are-generally-available/). The tools let an agent drive a real browser instance during a session.

**What agents can do with browser tools** (per the [GA changelog](https://github.blog/changelog/2026-07-01-browser-tools-for-github-copilot-in-vs-code-are-generally-available/)):

| Action | Description |
|--------|-------------|
| Navigate | Open pages, follow links, navigate back/forward |
| Click / type / hover / drag | Interact with buttons, links, form elements, and dialogs |
| Screenshot | Capture the current view for inspection or logging |
| Console inspection | Read page content, capture console errors, and take screenshots; DevTools are also available in the browser toolbar for manual inspection |
| Scripted flows | Run a scripted sequence of steps when that's more efficient than individual tool calls |

**Security model:**

- Sensitive permissions — camera, microphone, location, notifications, clipboard reads — require explicit per-site user approval; agents cannot self-approve
- Each agent-opened tab runs in an isolated session with no access to your existing cookies or personal browsing context; your own tabs stay private until explicitly shared
- Enterprise admins can restrict which domains agents may navigate to via `chat.agent.allowedNetworkDomains` / `chat.agent.deniedNetworkDomains` settings (denied domains take precedence), and can toggle the feature off org-wide via `workbench.browser.enableChatTools`

**Availability at GA:** VS Code only, enabled by default for paid Copilot subscribers. JetBrains browser tool support has not been announced.

**Why this matters:** Before GA, builders using Copilot's browser tools in automation pipelines had to treat the feature as unstable — behavior could change, and support was limited. GA means the API and behavior are locked for production use.

---

## 3. Codex as an Agent Provider in JetBrains (July 7)

[Codex is now available as an agent provider in public preview inside JetBrains IDEs](https://github.blog/changelog/2026-07-07-codex-as-agent-provider-and-agentic-enhancements-in-jetbrains-ides/), through the **GitHub Copilot plugin** for JetBrains — not a separate plugin.

**How it works:** you install the Codex CLI locally, then go to **Settings > Tools > GitHub Copilot > Chat**, enable Codex, and set the Codex CLI path. Once configured, you select Codex from the agent picker in the Copilot Chat panel to start a session. If you're a Copilot Business or Enterprise subscriber, an admin must enable the editor preview features policy before you can use it.

GitHub's changelog does not specify Codex-in-JetBrains availability by individual plan tier (Free vs. Pro vs. Pro+), so we are not going to guess at a table here — check [GitHub's own JetBrains documentation](https://github.blog/changelog/2026-07-07-codex-as-agent-provider-and-agentic-enhancements-in-jetbrains-ides/) for your specific plan before relying on it.

---

## 4. AI Credit Session Limits (July 1)

Agentic Copilot sessions — especially multi-step Codex tasks — can use substantially more AI credits than simple chat completions. Before session limits, a single runaway agent task could exhaust a user's monthly included credits unexpectedly.

As of July 1, [users can set a per-session credit cap in Copilot CLI and the Copilot SDK](https://github.blog/changelog/2026-07-01-set-ai-credit-session-limits-in-copilot-cli-and-sdk/).

**How to set limits** (syntax per [GitHub's docs](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/set-session-limit)):

```bash
# CLI: cap this run at 50 AI credits ($0.50 at $0.01/credit)
copilot -p "refactor the payment module to accept Stripe webhooks" --max-ai-credits 50

# Interactive sessions: set the current limit
/limits set max-ai-credits 50

# Interactive sessions: remove the limit
/limits unset
```

**Behavior when the limit is hit:**

| Mode | Behavior |
|------|----------|
| Interactive (`/limits`) | Copilot pauses and prompts you to raise or adjust the limit, then continues from where it stopped — no task restart needed |
| Non-interactive (`--max-ai-credits`) | The run ends immediately when the limit is reached |

**Important caveat:** These are **soft caps**. Because credit usage is only known after a response is returned, a response already in progress finishes before enforcement kicks in. Actual spend may slightly exceed the number you set.

**Requirements:** Copilot CLI 1.0.66+ or Copilot SDK 1.0.5+. Public preview — behavior is subject to change.

**Pricing reference:** [1 AI Credit = $0.01 USD](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing). Credit cost varies by model and token type; GitHub's docs note session limits work best set above 30 credits, since most individual model calls already cost more than 20.

---

## 5. AI Credit Pools for Enterprise Cost Centers (July 2)

Separate from per-session limits, GitHub also shipped [**AI credit pools** for enterprise cost centers on July 2](https://github.blog/changelog/2026-07-02-cost-centers-now-support-included-usage-caps/). This is an enterprise billing control, not a developer-facing feature.

**The problem it solves:** Enterprise organizations with multiple cost centers (teams, departments, clients) had no way to prevent one cost center from consuming the entire organization's included AI credit budget. A single high-volume team running long Codex sessions could exhaust the budget before other teams got their allocation.

**How it works:**

- GitHub automatically calculates each cost center's pool limit from the number of Copilot Business or Copilot Enterprise licenses assigned to that cost center
- The pool adjusts automatically as you add or remove licenses — no manual number entry
- When a cost center reaches its pool limit, the admin configures the behavior: **block** further included usage until the next billing cycle, or **allow overages** if the enterprise's billing settings permit additional spend
- Pool management is available today via the GitHub REST API; the cost center settings UI is coming in a future release

**Practical implication:** If you have 10 Business licenses assigned to a cost center, that cost center's included usage is capped at what 10 licenses cover. Another cost center with 50 licenses gets proportionally more. Total included credits across all cost centers equal the organization's total purchased entitlement.

---

## Builder Action List

**If you are on Copilot Free:**
- Download the Copilot app if you want desktop agent sessions — it now supports your plan
- Set expectations: your monthly credit budget is small; long Codex sessions will exhaust it quickly
- Use `--max-ai-credits` or `/limits` to avoid unexpected budget exhaustion when experimenting

**If you are on a paid individual plan (Pro / Pro+):**
- JetBrains users: install or update the GitHub Copilot plugin, install the Codex CLI locally, and enable it under Settings > Tools > GitHub Copilot > Chat to access Codex as an agent provider without switching to VS Code
- Browser tools are now stable — if you were avoiding them in production pipelines due to preview status, GA removes that blocker
- Set per-session limits on any automated script or CI-triggered agent run

**If you are a Copilot Business / Enterprise admin:**
- Enable **Copilot CLI** in policy settings to unblock the desktop app for your members
- Implement AI credit pools via the REST API before agentic usage scales — reactive cost controls are harder to enforce mid-billing-cycle
- Set per-cost-center pools proportional to each team's license count; let GitHub calculate the ceiling automatically

---

## What's Not Yet Available

The following are not yet shipped, per GitHub's own changelogs:
- Cost center credit pool management in the GitHub web UI — currently **API only**, UI coming soon (per the [July 2 changelog](https://github.blog/changelog/2026-07-02-cost-centers-now-support-included-usage-caps/))
- Browser tools GA in JetBrains — no announced timeline; the [July 1 GA changelog](https://github.blog/changelog/2026-07-01-browser-tools-for-github-copilot-in-vs-code-are-generally-available/) scopes the feature to VS Code only

---

*Research-based guide. ChatForest reviewed [GitHub changelog entries](https://github.blog/changelog/2026-07-07-github-copilot-app-available-to-all/), [the GitHub Blog](https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/), and third-party coverage. We did not run these features or administer a GitHub Enterprise organization.*
