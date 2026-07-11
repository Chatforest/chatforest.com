---
title: "GitHub Copilot July 2026: App Open to All Plans, Browser Tools GA, JetBrains Agent Sessions, Credit Controls — Builder's Guide"
date: 2026-07-12
description: "GitHub Copilot shipped four significant updates in the first week of July 2026: the Copilot app is now available to Free and Education accounts, browser tools reached GA, Codex agent sessions landed in JetBrains IDEs for paid users, and new credit controls let you cap per-session and per-cost-center spend. Here is what changed and what it means for your setup."
tags: ["github-copilot", "copilot-app", "agentic-coding", "browser-tools", "jetbrains", "ai-credits", "developer-tools", "enterprise-ai", "cost-management"]
---

GitHub Copilot shipped four updates in the first week of July 2026, covering access expansion, browser automation stability, a new IDE, and cost controls. None of them require a model upgrade — they are platform and billing changes. But the access expansion in particular changes who can use Copilot's agent features, and the credit controls change how enterprise teams deploy agents without surprise invoices.

This is a research-based guide. We reviewed GitHub's changelog, official blog posts, and the documentation. We did not run these features ourselves.

---

## 1. Copilot App Now Available on Every Plan (July 7)

Since June, the GitHub Copilot desktop app has been in technical preview for paid users. On July 7, GitHub opened it to **all Copilot plans** — including Copilot Free and GitHub Education accounts.

What the app offers:

- **My Work view** — a single dashboard tracking active sessions, open issues, PRs, and automations across repositories
- **Sessions** — each session runs in an isolated git worktree: a physically separate directory with its own branch, so multiple sessions on the same codebase can run in parallel without file conflicts
- **Canvases** — a shared surface where agents update content and developers can edit, reorder, approve, or redirect agent work without restarting the task
- **Agent Merge** — automation that monitors CI, tracks required reviewers, addresses failing checks, and handles the PR-through-merge pipeline without continuous supervision
- **Cloud sandboxes** — ephemeral Linux environments for agent execution

**Access notes:**
- Free and Education users: sign in at github.com/features/copilot to download the app; you can also bring your own model provider API keys for sessions
- Business and Enterprise users: admins must enable **Copilot CLI** in the organization's Copilot policy settings before the desktop app is available to members

The Copilot Free tier has usage limits. The desktop app session features consume AI credits; Free users have a monthly included credit budget that limits how many agent sessions they can run.

---

## 2. Browser Tools Reach General Availability (July 7)

Copilot's browser tools moved from preview to GA on July 7. The tools let an agent drive a real browser instance during a session.

**What agents can do with browser tools:**

| Action | Description |
|--------|-------------|
| Navigate | Open URLs, follow links, navigate back/forward |
| Click | Interact with buttons, links, form elements |
| Type | Fill in text fields and form inputs |
| Screenshot | Capture the current view for inspection or logging |
| Console inspection | Read browser console errors with sourcemap-resolved stack traces |

**Security model:**

- Sensitive permissions — camera, microphone, geolocation — are blocked by default and require explicit user approval before any agent call
- Each agent session runs in an isolated browser tab that cannot access tabs from other sessions or your personal browsing context
- GitHub restricts what origins the agent can navigate to in automated contexts

**Availability at GA:** VS Code. JetBrains browser tool support has not been announced.

**Why this matters:** Before GA, builders using Copilot's browser tools in automation pipelines had to treat the feature as unstable — behavior could change, and support was limited. GA means the API and behavior are locked for production use.

---

## 3. JetBrains Agent Sessions (July 7)

Codex agent sessions — the multi-step background agents that take an issue and work toward a PR — are now available inside JetBrains IDEs through the JetBrains AI Assistant plugin.

**Current availability:**

| Plan | JetBrains Agent Sessions |
|------|--------------------------|
| Copilot Free | Not yet — planned late Q3 2026 |
| Copilot Pro / Pro+ | Available |
| Copilot Business | Available (admin must enable) |
| Copilot Enterprise | Available (admin must enable) |

**How it works:** Sessions run in the same Codex cloud sandbox used by the VS Code Copilot app — an ephemeral Linux container with access to your codebase. The JetBrains integration adds a session panel inside the IDE so you can issue tasks, monitor progress, and review proposed changes without switching to a browser or a different tool.

The Copilot CLI, used from the desktop app and terminal, also reaches into JetBrains via the same session API, so you can start a session from the CLI and monitor it in the JetBrains panel.

---

## 4. AI Credit Session Limits (July 1)

Agentic Copilot sessions — especially multi-step Codex tasks — can use substantially more AI credits than simple chat completions. Before session limits, a single runaway agent task could exhaust a user's monthly included credits unexpectedly.

As of July 1, users can set a per-session credit cap.

**How to set limits:**

```bash
# CLI: cap this run at 50 AI credits ($0.50 at $0.01/credit)
copilot --max-ai-credits 50 "refactor the payment module to accept Stripe webhooks"

# Interactive sessions: view or set the current limit
/limits
```

**Behavior when the limit is hit:**

| Mode | Behavior |
|------|----------|
| Interactive (`/limits`) | Copilot pauses and prompts you to raise or adjust the limit, then continues from where it stopped — no task restart needed |
| Non-interactive (`--max-ai-credits`) | The run ends immediately when the limit is reached |

**Important caveat:** These are **soft caps**. Because credit usage is only known after a response is returned, a response already in progress finishes before enforcement kicks in. Actual spend may slightly exceed the number you set.

**Requirements:** Copilot CLI 1.0.66+ or Copilot SDK 1.0.5+. Public preview — behavior is subject to change.

**Pricing reference:** 1 AI Credit = $0.01 USD. Credit cost varies by model and token type. A typical coding session runs 5–50 credits depending on task length and model selection.

---

## 5. AI Credit Pools for Enterprise Cost Centers (July 2)

Separate from per-session limits, GitHub also shipped **AI credit pools** for enterprise cost centers on July 2. This is an enterprise billing control, not a developer-facing feature.

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
- JetBrains users: install or update the JetBrains AI Assistant plugin to access Codex agent sessions without switching to VS Code
- Browser tools are now stable — if you were avoiding them in production pipelines due to preview status, GA removes that blocker
- Set per-session limits on any automated script or CI-triggered agent run

**If you are a Copilot Business / Enterprise admin:**
- Enable **Copilot CLI** in policy settings to unblock the desktop app for your members
- Implement AI credit pools via the REST API before agentic usage scales — reactive cost controls are harder to enforce mid-billing-cycle
- Set per-cost-center pools proportional to each team's license count; let GitHub calculate the ceiling automatically

---

## What's Not Yet Available

The following were mentioned in the July 7 announcement period as planned but not yet shipped:
- JetBrains agent sessions for Copilot Free — planned **late Q3 2026**
- Cost center credit pool management in the GitHub web UI — currently **API only**, UI coming soon
- Browser tools GA in JetBrains — no announced timeline

---

*Research-based guide. ChatForest reviewed GitHub changelog entries, the GitHub Blog, and third-party coverage. We did not run these features or administer a GitHub Enterprise organization.*
