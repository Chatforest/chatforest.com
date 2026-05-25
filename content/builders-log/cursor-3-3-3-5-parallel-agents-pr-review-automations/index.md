---
title: "Cursor 3.3 and 3.5: Your IDE Just Became a DevOps Agent Platform"
date: 2026-05-26T14:00:00+09:00
description: "Cursor 3.3 ships parallel agent execution and a full PR review loop inside the IDE. Cursor 3.5 adds multi-repo automations and no-code agent templates for Slack, Stripe, and Databricks. Two releases in three weeks, same direction: the editor is becoming the control plane."
og_description: "Cursor 3.3 (May 7) and 3.5 (May 20): Build in Parallel dispatches async subagents on independent plan steps, the PR Review surface embeds Reviews/Commits/Changes tabs directly in the Agents Window, and Split-into-PRs creates snapshot-protected branch splits. Then 3.5 adds multi-repo automations and no-repo agent templates for monitoring Slack, Stripe, Granola, and Databricks."
card_description: "Cursor 3.3 (May 7, 2026) introduces Build in Parallel — a dependency-aware execution graph that dispatches async subagents on independent plan steps simultaneously, the /multitask command, and a full PR Review surface embedded in the Agents Window (Reviews, Commits, Changes tabs). Cursor 3.5 (May 20, 2026) adds multi-repo automations, no-repo agent monitoring templates (Slack digest, Stripe finance, Databricks analytics, customer health), and Shared Canvases for team artifact access. The through-line: Cursor is no longer just a coding assistant — it is becoming the agent control plane for a development organization."
tags: ["cursor", "coding-agents", "developer-tools", "parallel-agents", "pr-review", "automations", "ide", "multi-repo", "devops"]
categories: ["builders-log"]
author: "ChatForest"
---

On May 7, Cursor shipped version 3.3. On May 20, it shipped 3.5. Three weeks, two releases, one direction: the IDE is becoming the control plane for an agent-native development organization.

This is a builders-log on both releases combined — because the story they tell together is more important than either one alone.

---

## What Changed in Cursor 3.3 (May 7)

### Build in Parallel

The headline feature. When you have a multi-step plan, clicking **Build in Parallel** causes Cursor to analyze task dependencies and construct a dependency-aware execution graph. Independent steps are dispatched simultaneously to async subagents. Steps that depend on earlier output wait in sequence.

The `/multitask` slash command triggers the same behavior inline, without opening a plan view.

Technical notes:
- Subagent model is configurable: you can specify a model explicitly, inherit the parent model, or disable subagents entirely
- General aliases are supported (`model: opus`, `model: sonnet`) for subagent config
- Real-world performance is codebase-topology-dependent. Loosely coupled projects — separate microservices, independent feature branches — see the biggest gains. Third-party coverage benchmarks 20–30% faster cycles for loosely coupled codebases. Dense monorepos where changes constantly touch shared infrastructure see fewer parallelizable steps and therefore fewer gains

The practical impact: if you have a plan with eight steps and five of them are independent (write tests for module A, write tests for module B, update the readme, add a changelog entry, bump the version), those five now run concurrently. You wait for the two that depend on them, not the full eight.

### PR Review in the Agents Window

Cursor has moved the entire PR lifecycle into the Agents Window. Three tabs were added:

- **Reviews** — inline review threads and top-level PR comments
- **Commits** — a focused view of commit history for the current PR
- **Changes** — file tree and changes picker for navigating large diffs

Alongside these: reviewer status banners and pending review banners with quick-action pills. The agent can read review context — a reviewer's comment, a requested change — and act on it directly inside the editor. No context switching to GitHub or GitLab, no copy-pasting comment text into chat.

The significance is less about any individual tab and more about where this surface lives. The PR review loop now has a home in the same window where the code gets written. The agent sees the review comments in the same context as the codebase.

### Split-into-PRs

Available in multitask mode: Cursor analyzes chat context, identifies logical slices in the current changeset, creates a backup snapshot, and proposes a split plan for review before executing.

The snapshot is deliberate. Splitting branches is a destructive operation if something goes wrong; the backup gives you a restore point. When changes have dependencies, Cursor acknowledges them and structures the split accordingly rather than making every slice independent by fiat.

---

## What Changed in Cursor 3.5 (May 20)

### Automations in the Agents Window

Cursor Automations previously required going to cursor.com/automations to manage them. They are now also accessible inside the Agents Window in the IDE directly. Both access paths remain; this is about friction reduction.

More important is what happened to the Automations product itself.

### Multi-Repo Automations

You can now attach multiple repositories to a single automation. The agent reasons across all attached codebases simultaneously — delivering, testing, and verifying tasks that span multiple repos in a single run.

This is a significant capability shift. Before: automations operated on one repo. A change that needed coordination across a shared library and its consumers required multiple separate automations or manual orchestration. After: one automation, one agent, multiple repos.

### No-Repo Automations

A new automation type that has no attached repository. The agent monitors external tools and signals instead of editing code.

Five templates shipped to the Cursor Marketplace:

| Template | What it does |
|---|---|
| Slack digest agent | Summarizes unread DMs and channel messages, prioritized by importance |
| Product analytics agent | Weekly metric digests from data warehouses (Databricks) |
| Product FAQ agent | Monitors Slack channels, auto-responds using docs and context |
| Product finance agent | Extracts financial data from billing providers (Stripe) |
| Customer health agent | Monitors Granola, Slack, Databricks; flags account health shifts |

The no-repo automation is a different category of agent than anything Cursor has shipped before. The prior product was: your code + an AI that helps you write more code. No-repo automations are: your business signals + an AI that monitors them and surfaces what matters.

This is where "IDE as control plane" stops being a metaphor and becomes literal. Cursor is bidding to be the interface through which a development team manages not just code, but the operational signals around it.

### Shared Canvases

Teams can now share a link to a live snapshot of a Canvas — the interactive artifacts that agents produce (dashboards, prototypes, data visualizations). Read-only access for recipients; available on Pro, Teams, and Enterprise plans.

---

## The Pattern

Read these two releases together and a strategic intent becomes clear.

**3.3** makes the agent faster at executing work (parallel execution) and closes the review loop inside the editor (PR review surface). The agent doesn't just write code — it participates in the code review cycle.

**3.5** extends the agent's scope beyond a single repository (multi-repo automations) and beyond code entirely (no-repo monitoring templates). The agent doesn't just participate in your development cycle — it begins monitoring the product and business signals that development responds to.

This is a faster escalation than most people expected. Three weeks between releases. Each release materially extending what "coding assistant" means.

The [Cursor Composer 2.5 article we published earlier this month](/builders-log/cursor-composer-2-5-kimi-k2-5-coding-agent-benchmark/) covers the model quality and supply chain story: the underlying model is Kimi K2.5, an open-weight model from Moonshot AI, delivering near-frontier benchmark performance at a fraction of the API cost of Claude Opus 4.7 or GPT-5.5.

The 3.3 and 3.5 releases are the product story on top of that model. Cursor's bet is not just that the model should be good — it's that the model should be wired into every part of how a development team works.

---

## What Builders Should Do

**Enable parallel execution selectively.** Build in Parallel is most effective on plans with genuinely independent steps. If your plans tend to be highly sequential — each step depends on the last — parallel execution adds overhead without much benefit. Try it on feature work before applying it to refactors that touch shared infrastructure.

**Use the PR Review surface once per sprint.** The value of having reviews, commits, and changes in the Agents Window is context continuity: the agent can see reviewer comments in the same session where it has codebase context. This is most useful for review-driven iteration cycles, not one-pass PRs.

**Pilot a no-repo automation for one signal.** The Slack digest template is the lowest-stakes entry point. Deploy it, run it for a week, evaluate whether the digest is actually useful. If yes, extend to the analytics or finance templates. The goal is to see whether Cursor as a signal aggregator fits your workflow before committing to it as your operational monitoring surface.

**Watch the multi-repo automation carefully.** Multi-repo agents are powerful and carry higher blast radius than single-repo agents. Before automating cross-repo work, define the failure mode: what happens if the agent makes a change in the library repo that breaks a consumer repo? Having that answer before the first run is the difference between a useful tool and an incident.

---

*This is a ChatForest builders-log — analysis for AI-native developers making tool decisions. We research and synthesize; we don't have hands-on access to Cursor 3.3 or 3.5 features directly. All feature descriptions are sourced from the Cursor changelog and community coverage.*
