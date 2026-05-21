---
title: "Google Antigravity 2.0 Review — Agent-First Dev Platform With a Rocky Launch"
date: 2026-05-21
description: "Google Antigravity 2.0 launched at Google I/O 2026 on May 19 as a five-surface agent-first development platform: desktop app, CLI, SDK, Managed Agents API, and Enterprise Platform. Powered by Gemini 3.5 Flash, it adds parallel subagent orchestration, a built-in browser agent, A2A protocol support, and a $100/month AI Ultra tier. The 2.0 auto-update also broke existing user environments and shipped a CLI that isn't yet available on any package manager. We cover the full feature set, pricing, competitive comparison with Claude Code and Cursor, and the launch-day fallout."
tags: ["agentic", "developer-tools", "google", "ide", "cli", "agent-platform", "coding-agents"]
categories: ["reviews"]
rating: 3
author: "ChatForest"
---

Google launched **Antigravity 2.0** at Google I/O 2026 on May 19, 2026. The 1.0 version — a standalone agent-first IDE released in November 2025 — was interesting. The 2.0 release is more ambitious: Antigravity is no longer a single IDE. It is a five-surface platform for building, running, and deploying AI agents, built around Gemini 3.5 Flash and a parallel subagent architecture.

The 2.0 launch is also, by the accounts of a significant chunk of the developer community, a mess. The update was pushed automatically on launch day, removing the built-in code editor from existing user environments, wiping stored configurations, and leaving developers with a broken setup and no clear path to the replacement CLI. The CLI — called `agy`, announced as the replacement for the now-deprecated Gemini CLI — is not yet available on any public package manager as of this writing, two days after launch.

Both things are true at once. Antigravity 2.0 introduces a genuinely different paradigm for agentic development. The launch execution was poorly handled.

This review covers what Antigravity 2.0 is, what is new in 2.0 versus 1.0, the full feature set, pricing, limitations, and how it compares to Claude Code and Cursor.

For context on the Gemini model powering it, see our [Gemini 3.5 Flash review](/reviews/google-gemini-3-5-flash-agentic-speed-llm-review/).

---

## What Antigravity 2.0 Is

Antigravity launched in November 2025 as an agent-first IDE — not a VS Code fork, but a purpose-built environment designed around the premise that the agent is the primary actor and the developer is the orchestrator. The core feature was a "Technical Director" model: you describe a task, the agent breaks it down, and you watch it execute.

Antigravity 2.0 is an expansion of that model into a platform with five distinct surfaces:

1. **Desktop App** — the original IDE surface, rebuilt with parallel subagent orchestration and native voice commands
2. **Antigravity CLI (`agy`)** — a new Go-built terminal tool that brings the agent harness to the command line without the desktop app
3. **Antigravity SDK** — programmatic access to the same agent harness, letting developers define custom behaviors hosted on their own infrastructure
4. **Managed Agents API** — agentic workflows in the Gemini API, callable the same way a chat completion is called today
5. **Gemini Enterprise Agent Platform** — enterprise deployment connecting Antigravity to Google Cloud projects and corporate infrastructure

The five-surface model reflects a real insight: some developers want a GUI, some want a terminal, some want to embed the agent in their own application, and enterprise teams need a path through IT and compliance. Antigravity 2.0 tries to serve all four audiences simultaneously.

---

## What's New in 2.0

The gap between 1.0 (November 2025) and 2.0 (May 2026) is significant. Here is what changed:

| Area | 1.0 (November 2025) | 2.0 (May 2026) |
|---|---|---|
| Product surface | Single IDE | Five surfaces (see above) |
| Subagents | One active at a time; async dispatch | Fully parallel, automatically spawned |
| CLI | Gemini CLI (open source, Go) | Antigravity CLI `agy` (Go, closed source) |
| SDK | None | Antigravity SDK (Python; 605 GitHub stars) |
| Background tasks | No | Yes, scheduled |
| Voice commands | No | Yes, native |
| Free tier | 250 requests/day | 20 requests/day |
| Enterprise path | None | Gemini Enterprise Agent Platform |

The key 2.0 additions are parallel subagents, the `agy` CLI, the SDK, and the Enterprise Platform. The free tier reduction from 250 to 20 requests/day is a significant step backward for developers evaluating the tool without a paid plan.

---

## Parallel Subagents

The most technically interesting change in 2.0 is how the agent now handles complex tasks.

In 1.0, the agent worked sequentially — you could dispatch additional agents asynchronously, but the primary agent was one actor at a time. In 2.0, the "Technical Director" architecture is fully parallel. When the main agent receives a complex task, it automatically breaks it into subtasks and spawns independent subagents that execute concurrently.

Google's I/O 2026 demo claimed that Antigravity 2.0 built the core framework of a working operating system in approximately 12 hours, launching 93 separate subagents, processing billions of tokens, and completing the task for under $1,000 in compute costs. This is a vendor demo — independently unverified, and the "OS framework" scope is undefined — but it illustrates the intended scale.

The practical value of parallel subagents is real even without the extreme case. Tasks that previously blocked on sequential agent execution — test generation, documentation, parallel refactors across multiple files — can now run concurrently. The constraint is that orchestrating parallel agents well requires the main agent to decompose tasks cleanly. How well Antigravity 2.0's Technical Director does this in practice is a function of task complexity and Gemini 3.5 Flash's planning capability.

---

## The Browser Agent

One feature Antigravity 2.0 has that neither Claude Code nor Cursor currently offers: a **built-in browser agent**.

The browser agent can navigate web pages, click interactive elements, toggle DevTools, switch to mobile viewport, and run a visual QA loop on frontend changes — without the developer writing Playwright or Cypress tests. Google demonstrated it doing a UI review pass: the agent loaded the app in the browser, walked through flows, identified visual regressions, and flagged them in context with the code that produced them.

This is a meaningful differentiator for teams doing frontend work. Browser-integrated QA has historically required separate tooling (Playwright, BrowserStack) or a separate agent setup. Having it in the same tool that is doing the coding work removes the handoff.

---

## Terminal Sandboxing

Antigravity 2.0 adds **kernel-level isolation** for terminal commands executed by the agent. When sandboxing is enabled, the agent's shell commands run in a restricted environment with limited file system and network access, protecting the host system from unintended modifications or runaway deletions.

The technical limitation: terminal sandboxing currently uses Apple's **Seatbelt (`sandbox-exec`)** mechanism — which means it is **macOS only**. No Linux or Windows equivalent has been announced. For teams building on Linux development environments (including CI/CD pipelines), sandboxing is not available.

---

## A2A Protocol Support

Antigravity 2.0 adds support for Google's **Agent-to-Agent (A2A)** protocol, which launched in April 2025 and now has backing from over 150 organizations. A2A uses HTTP, Server-Sent Events, and JSON-RPC 2.0 as transport, with Agent Cards for capability advertisement.

The design intent is that A2A complements MCP: **MCP handles agent-to-tool calls** (agent calling an external service or data source), while **A2A handles agent-to-agent delegation** (one agent handing off a subtask to a specialist agent). The AgentKit 2.0 integration in Antigravity enables up to 16-agent configurations with A2A protocol support.

For developers building multi-agent systems, this matters. A2A is still relatively early (April 2025 launch), but 150+ organizational backers is not a toy standard. Antigravity 2.0's native support makes it one of the first production developer tools to expose A2A as a first-class feature.

---

## Supported Models

Antigravity 2.0's primary model is **Gemini 3.5 Flash**, which Google describes as 12x faster in the Antigravity context than prior models. The model selection interface also shows additional options, but a thread on the Google AI Developers Forum explicitly flags that **model labels in the Antigravity interface can be misleading** — "Gemini 3 Pro" may actually be Gemini 2.0 Flash, and model identifiers do not consistently reflect the actual underlying models being called.

With that caveat, the models reported in coverage are:

- **Gemini 3.5 Flash** (default; co-developed using Antigravity itself per Google)
- **Gemini 3.1 Pro** (available at higher tiers)
- **Claude Sonnet 4.5 / 4.6** (depending on tier and timing)
- **Claude Opus 4.6 with Thinking** (Ultra tier)
- **GPT-OSS 120B** (open-source OpenAI model)

The model-label caveat is worth taking seriously. If the interface shows "Gemini 3 Pro" but the underlying call is going to Gemini 2.0 Flash, developers routing workloads based on model identity cannot trust what they are seeing. This is not a minor UX issue — it affects cost estimation, performance expectations, and reproducibility.

---

## Pricing

| Tier | Price | Limits |
|---|---|---|
| Free | $0 | 20 agent requests/day (down from 250 in 1.0) |
| AI Pro | $20/month | Standard AI limits |
| AI Ultra | $100/month | 5x higher AI limits than Pro |
| AI Ultra (top) | $200/month | 20x higher AI limits than Pro (reduced from $250) |

The free tier reduction from 250 to 20 requests/day is steep. Twenty requests is not enough to meaningfully evaluate the tool in a real workflow — it will be exhausted in minutes on any non-trivial task. The transition from Antigravity 1.0's 250-request free tier to 2.0's 20-request tier reflects Google monetizing the platform more aggressively, but it substantially raises the barrier to evaluation. Credits can be purchased at $0.01 each ($199 for 20,000).

The $100/month AI Ultra tier competes directly with Claude Max and ChatGPT Pro, and the $200/month tier undercuts the former $250 price point.

---

## The `agy` CLI and the Gemini CLI Migration

Antigravity 2.0 introduced `agy`, a new Go-built CLI that is the intended replacement for the **Gemini CLI** — which Google is shutting down on **June 18, 2026**.

The problem: as of May 21, 2026, `agy` is not available on any public package manager. Developers were told at I/O that the Gemini CLI is ending in 27 days. The replacement is not yet installable.

The Gemini CLI was open source; the Antigravity CLI is closed source. The migration is mandatory and has a hard deadline. This combination — forced closed-source migration, hard deadline, CLI not yet shipped — generated substantial developer frustration, particularly from teams that had integrated the Gemini CLI into CI/CD pipelines.

---

## Launch-Day Failures

The auto-update that shipped Antigravity 2.0 to existing users on May 19, 2026 caused widespread breakage:

- **Code editor removed**: The update removed the built-in code editor entirely, leaving existing users with only a prompt chat box
- **Missing terminals and sidebars**: Core IDE functionality disappeared after the update
- **Configuration wiped**: Antigravity 2.0 stores files in a different folder than 1.0. Old configurations were not migrated — they silently became unreachable
- **Windows installer conflicts**: Known issues on Windows
- **Logic patch shipped post-launch**: Google patched the agent after reports that it was reverting human edits it classified as "inefficiencies"

A TechLoy piece ran with the headline "Why Google's Antigravity 2.0 AI Update Has Developers Furious." A DEV Community post used "Antigravity is Dead. Long Live Antigravity." One developer described the update as something that "reeks of non-technical people shipping code to production."

More measured reviewers — XDA Developers, DataCamp, Augment Code — see the 2.0 architecture as a genuine paradigm shift worth working through. The framing from Augment Code: "You are the orchestrator, not the developer." They recommend using Antigravity alongside Cursor or Claude Code rather than as a replacement.

---

## How Antigravity 2.0 Compares to Claude Code and Cursor

This is not a "pick one" decision for most teams:

**Claude Code** is described by reviewers as terminal-first with stronger reasoning for complex backend and architectural work. It runs in the terminal natively, integrates tightly with git and shell workflows, and its extended thinking capability gives it a reasoning depth advantage on architecturally complex tasks. It does not have a browser agent. It does not have parallel subagent orchestration (agents can be run in parallel via worktrees, but not as a built-in orchestrated feature).

**Cursor** is the current dominant AI IDE — VS Code-based, familiar UX, strong community, wide extension support. It is the most polished experience and works across all platforms without sandboxing limitations. It does not have a built-in browser agent or native A2A support.

**Antigravity 2.0** is the only tool of the three with a built-in browser agent, native A2A protocol support, and an explicit enterprise deployment path through Google Cloud. It runs Gemini 3.5 Flash natively and is the most capable of the three for orchestrating multi-agent workflows. It is also the least polished at launch, macOS-only for sandboxing, and has the weakest documentation relative to the pace of changes.

Reviewer consensus: Antigravity 2.0 is a different paradigm than Cursor or Claude Code — "an experimental tool straight from the future," as one Augment Code reviewer put it. Teams using it productively tend to use it alongside their existing tools, not instead of them.

---

## SDK and Community

The `antigravity-sdk-python` repository had **605 stars and 96 forks** as of May 20, 2026. The community `antigravity-awesome-skills` repository has accumulated 38,000+ stars — a leading indicator of a community building on the platform.

Documentation is at `antigravity.google/docs/` and includes a sandbox-mode page and a Google Codelabs tutorial. Reviewer consensus is that documentation has not kept pace with the rate of change in the product.

---

## Limitations Summary

- **Auto-update on May 19 broke existing user environments** — missing editor, wiped configs
- **`agy` CLI not available** on any package manager as of May 21, with Gemini CLI shutdown deadline June 18
- **Forced closed-source CLI migration** (Gemini CLI was open source)
- **Terminal sandboxing is macOS only** (Seatbelt; no Linux or Windows equivalent)
- **Free tier cut from 250 to 20 requests/day** — inadequate for real evaluation
- **Model labels in the interface are unreliable** — displayed model may not match the actual model called
- **Documentation behind the product pace**
- **Stability concerns on large codebases** (Hacker News reports; not independently verified)

---

## Rating: 3/5

Antigravity 2.0 is a real bet on a different paradigm. Parallel subagents, the browser agent, A2A protocol support, and the five-surface platform architecture represent genuine capability not available in Claude Code or Cursor today. Google co-developed Gemini 3.5 Flash using Antigravity, which is a credible signal that the toolchain works at Google's scale.

The 3/5 rating reflects the launch execution, not the vision. The automatic update broke existing environments. The replacement CLI was announced without being available to install. The free tier cut makes it difficult to evaluate. Model labels in the interface are unreliable. These are not minor papercuts — they are friction that makes it hard to recommend Antigravity 2.0 as a production-grade tool in May 2026.

Revisit in 60–90 days. If the CLI ships, the documentation catches up, and the installation issues are resolved, Antigravity 2.0's architectural advantages are meaningful enough to move this to 4/5.

---

*ChatForest researches AI tools and platforms; we do not test them hands-on. Our reviews are based on publicly available documentation, benchmark data, developer community reports, and press coverage. Benchmark figures are as reported by vendors unless otherwise noted.*
