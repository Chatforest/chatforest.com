---
title: "Antigravity 2.0: Google's Five-Surface Agent Platform Builder Guide"
date: 2026-06-02
description: "Google Antigravity 2.0 ships a five-surface agentic dev platform: desktop app, CLI, SDK, Managed Agents API, and Enterprise Agent Platform. The desktop app adds parallel subagent orchestration, cron-scheduled background tasks, and session-persistent context. Here's the builder map."
og_description: "Antigravity 2.0 is no longer an IDE plugin. It's a five-surface platform. Desktop app runs parallel agents on cron. SDK exposes the same harness. Enterprise tier plugs into Google Cloud. Here's how builders navigate it."
content_type: "Builder's Log"
categories: ["Google", "Agent Infrastructure", "Developer Tools"]
tags: ["google", "antigravity", "gemini", "agentic-coding", "multi-agent", "desktop-app", "sdk", "scheduled-tasks", "google-io-2026", "ai-ultra", "enterprise-ai", "builders-log"]
draft: false
---

Google shipped Antigravity 2.0 at Google I/O 2026 on May 19, and the scope of the release is easy to underestimate if you only read the headline. This is not an IDE plugin update. Antigravity 2.0 is a five-surface agentic development platform — desktop app, CLI, SDK, Managed Agents API, and an Enterprise Agent Platform — all running on the same underlying agent harness and the same Gemini 3.5 Flash model.

We already have separate guides on two of those surfaces:

- [Google Is Killing Gemini CLI on June 18 — Migration Checklist to Antigravity CLI](/builders-log/gemini-cli-dead-june-18-antigravity-cli-agy-migration/) covers the `agy` CLI replacement and the MCP config trap.
- [Gemini API Managed Agents: Hosted Sandbox Execution in One Call](/builders-log/gemini-api-managed-agents-antigravity-sandbox-builder-guide/) covers the API-based hosted execution model.

This guide covers what those two don't: the desktop app architecture, parallel subagent orchestration, scheduled background tasks, the SDK, the enterprise tier, and the AGENTS.md convention that replaces the old `.gemini/` directory.

---

## What Changed Between Antigravity 1.x and 2.0

Antigravity 1.x was fundamentally a single-agent coding assistant that lived inside your IDE — you prompted it, it responded, you reviewed. The implicit mental model was a smarter autocomplete with terminal access.

Antigravity 2.0 changes the model in two ways. First, agents can now spawn and coordinate subagents. A single top-level prompt can trigger parallel workstreams — one agent writes code, another runs tests, a third checks documentation consistency — without the main agent blocking on any of them. Second, agents can run without the user present: scheduled tasks fire on cron syntax, the agent executes, and results surface when you reopen the desktop app. Together these two changes move Antigravity from a tool you use to infrastructure you operate.

---

## The Desktop App

The Antigravity 2.0 desktop app is a standalone application — not an IDE extension, not a web panel. It functions as a centralized workspace for agent orchestration.

### Parallel Agents

The app's headline feature is multi-agent parallelism. You can launch multiple agents on different tasks simultaneously. Each agent has its own session context and conversation transcript. Agents can view each other's transcripts, which means a coordinating agent can read the output of a specialist subagent without explicit message-passing boilerplate.

When an idle agent receives a message — from a user or from another agent — it is automatically re-awakened to process the new information. Session context persists across re-activations: the agent retains everything from its prior work when awakened.

### Subagent Workflows

Subagents are the mechanism for parallelizing within a single workflow. An agent can delegate subtasks — running tests, searching the codebase, drafting documentation — to dedicated subagents and continue on its own work while they execute. Subagents preserve the context of the main agent, so the main agent doesn't need to reload state from subagent output; it receives a structured result and continues.

The practical effect: tasks that previously required sequential attention (write → test → document → review) can be structured as parallel delegations. Latency on a complex task can drop significantly if the bottleneck was context-switching across steps.

### Scheduled Tasks

Scheduled tasks are a new capability in 2.0 with no equivalent in 1.x. They use standard cron syntax and run agents in the background automatically. Google frames scheduled background automation as "a first-class feature" — the agent keeps running after the desktop app is closed, and results surface in the Agent Manager view when you next open the app.

This converts the agent from a single-turn tool into a persistent automation pipeline. Use cases:

- Nightly codebase consistency checks against a style guide
- Hourly pulls from a data source with summarization to a shared document
- Automated test suite runs on a branch with results posted to a PR comment
- Weekly changelog drafts based on commit history

---

## File Convention: AGENTS.md Replaces .gemini/

The old convention for customizing Antigravity behavior was a `.gemini/` directory at repo root. Antigravity 2.0 deprecates that in favor of a single `AGENTS.md` file at repo root and a `.agents/skills/` directory for custom skills.

The `AGENTS.md` file works the same way conceptually as `CLAUDE.md` in Claude Code — it contains project-level instructions the agent reads at session start. Skills live in `.agents/skills/` as Markdown files and can be invoked by name in prompts or referenced in scheduled task definitions.

Custom agent templates are now available in Google AI Studio, giving teams a starting point for common use cases (code review agent, documentation agent, data pipeline agent) without writing AGENTS.md from scratch.

---

## The SDK

The Antigravity SDK provides programmatic access to the same agent harness that powers Google's products. It is optimized for Gemini models and lets developers define custom agent behaviors, chain them together, and host them on their own infrastructure.

The SDK is the right surface when:
- You are embedding agent capabilities into an existing product rather than using the desktop app interactively
- You need agents to run inside your own infrastructure (VPC, on-prem, specific cloud region) rather than Google's managed environment
- You want full control over the agent execution loop — retry logic, error handling, state management — without relying on Google's hosted sandbox

The SDK uses the same `AGENTS.md` / `.agents/skills/` conventions as the desktop app, so skills developed interactively can be extracted and deployed programmatically without rewriting.

---

## The Enterprise Agent Platform

The Gemini Enterprise Agent Platform is the fifth surface, aimed at Google Cloud customers. It lets organizations connect Antigravity directly to their Google Cloud projects — agents run inside the customer's cloud environment with access to Cloud Storage, BigQuery, and other GCP services.

The enterprise tier adds organizational governance: access controls, audit logs, and agent deployment policies managed at the organization level. This is the path for teams that need to operate agents inside existing compliance boundaries — not a separate hosted environment that IT has to evaluate and approve from scratch.

---

## Pricing Changes in AI Ultra

Antigravity 2.0 shipped alongside a pricing restructure for Google's consumer AI plans. The AI Ultra plan, previously priced at $250/month, dropped to $200/month and offers 20x higher limits in Antigravity compared to the Pro plan. A new $100/month AI Ultra tier launched with 5x higher limits than Pro.

The plans are:

| Plan | Monthly Price | Antigravity Limits |
|---|---|---|
| Pro | $20 | Baseline |
| AI Ultra | $100 | 5x Pro |
| AI Ultra Pro | $200 | 20x Pro (formerly $250) |

For teams doing serious agentic work — multi-agent workflows, scheduled tasks running overnight, long-context sessions — the 5x and 20x multipliers matter in practice. Hitting rate limits mid-session on a scheduled task means the task either fails silently or queues, depending on how error handling is configured.

---

## Choosing the Right Surface

All five surfaces run on the same harness, but they optimize for different contexts:

| Surface | Best for |
|---|---|
| Desktop app | Interactive development, multi-agent orchestration, scheduled background tasks, experimenting with subagent workflows |
| CLI (`agy`) | CI/CD pipelines, scripted automation, terminal-native workflows, git hooks |
| SDK | Embedding agent capabilities in products, custom infrastructure requirements, programmatic orchestration |
| Managed Agents API | Serverless agent execution, no infra to manage, state persistence between calls, compute-free during preview |
| Enterprise Agent Platform | GCP-native deployment, organizational governance, compliance boundaries, Cloud integration |

The typical progression: start with the desktop app to develop and test workflows interactively, extract working patterns into AGENTS.md, then move them to CLI for CI or SDK for product integration. Managed Agents is the alternative to SDK if you don't want to manage the execution environment.

---

## The Broader Ecosystem Signal

The five-surface architecture matters beyond the feature list. Google built Antigravity so that Gemini Spark — Google's AI assistant across Search, Workspace, and Android — runs on the same agent harness. When a Gemini Spark action executes a complex task, it is using the same infrastructure as your Antigravity 2.0 scheduled task.

This alignment is deliberate. It means skills and behaviors developed for Antigravity 2.0 are architecturally compatible with the direction Google is moving its entire product stack. The platform bet Google is making is not "developers build here, consumers experience elsewhere." The platform bet is that the same agent harness underlies both, and developers who build on it are building skills that surface in Google's consumer products.

---

## Action Items for Builders

**1. Migrate to AGENTS.md.** If you have a `.gemini/` directory in any repo using Antigravity, move those instructions to an `AGENTS.md` file at repo root. The old convention is deprecated and will eventually stop being read.

**2. Set up one scheduled task.** The quickest way to evaluate whether scheduled agents make sense for your workflow is to automate one existing manual task. Nightly changelog drafts and weekly dependency audit summaries are low-risk starting points that demonstrate value without requiring significant setup.

**3. Evaluate the AI Ultra tier.** If you're running multi-agent workflows or scheduled tasks that fire multiple times per day, check whether you're hitting rate limits. The $100/month AI Ultra tier's 5x limit multiplier may eliminate interruptions that currently require manual retry.

**4. Read the parallel agents documentation.** The subagent coordination model is different from sequential tool-use. The [Antigravity parallel agents guide](https://antigravity.google/docs/subagents) documents the transcript-sharing mechanism and message-passing conventions. Understanding this before building complex workflows avoids architectural mistakes that are expensive to refactor.

**5. For SDK users: check the AGENTS.md skill compatibility.** Skills defined in `.agents/skills/` as Markdown files are portable across surfaces — skills work in the desktop app, CLI, and SDK. If you have custom behavior defined only in code, consider externalizing it into skill files for easier iteration.

**6. For GCP customers: register for the Enterprise Agent Platform.** The enterprise tier connects agents to Cloud Storage, BigQuery, and GCP services with organizational governance. If your team already uses GCP for data infrastructure, the integration path is substantially simpler than standing up an alternative.
