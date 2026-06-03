---
title: "GitHub Copilot App: The Standalone Agent Desktop Is Now in Technical Preview"
date: 2026-06-03
description: "GitHub's standalone Copilot app — a desktop client separate from any IDE — expanded its technical preview at Build 2026 on June 2. Sessions run in isolated git worktrees, canvases give agents and humans a shared work surface, and Agent Merge handles the PR-through-merge pipeline. Here's what it is and who should adopt now."
og_description: "GitHub expanded its standalone Copilot desktop app to all Copilot Pro, Pro+, Business, and Enterprise users on June 2. This isn't a VS Code extension. It's a new interface category: a control center for parallel agent sessions, canvases, Agent Merge, and cloud sandboxes. The Copilot SDK is now GA in 7 languages. Here's the builder decision guide."
content_type: "Builder Guide"
card_description: "GitHub's standalone Copilot app — not an IDE extension — entered expanded technical preview at Build 2026 (June 2). My Work view tracks active sessions, issues, PRs, and automations across repos. Sessions run in isolated git worktrees (no branch conflicts). Canvases are bidirectional surfaces where agents and humans share plans, PRs, terminals, and dashboards. Agent Merge handles CI, review, and merge autonomously with configurable scope. Cloud sandboxes are ephemeral Linux environments. Copilot SDK is now GA in Node, TypeScript, Python, Go, .NET, Rust, and Java. Access: Copilot Pro through Enterprise. Free users can join a waitlist."
tags: ["github", "github-copilot", "copilot-app", "agentic-coding", "build-2026", "agent-merge", "canvases", "worktrees", "sandboxes", "copilot-sdk", "developer-tools", "desktop-app"]
categories: ["builders-log"]
author: "ChatForest"
---

**At a glance:** On June 2, 2026, GitHub expanded the technical preview of the GitHub Copilot app — a standalone desktop client for macOS, Windows, and Linux — to all Copilot Pro, Pro+, Business, and Enterprise subscribers. This is not an IDE extension. It's a new interface category: a control center for managing multiple parallel agent sessions, each running in its own isolated git worktree. Key features include the My Work view, canvases, Agent Merge, and cloud sandboxes. The Copilot SDK is now generally available in seven languages. Part of our **[Builder's Log](/builders-log/)**.

---

## What This Is (and What It Isn't)

This is easy to misread, so let's be precise.

The **GitHub Copilot app** is a standalone desktop application — separate from GitHub.com, separate from VS Code, and separate from any IDE extension. It runs natively on macOS, Windows, and Linux. It connects to your GitHub account and repositories, and it's designed to be a control center for managing AI agent workflows at a level that doesn't fit inside an editor's side panel.

This is different from:

- **GitHub Copilot in VS Code** — the editor extension with chat, completions, and Copilot Edits
- **GitHub Copilot in Visual Studio 2026** — the IDE-integrated agents covered in our [Visual Studio Build 2026 article](/builders-log/github-copilot-visual-studio-agents-debug-profiler-test-build-2026/)
- **Copilot Workspace** — GitHub's browser-based task-to-PR pipeline

The Copilot app is what you run when you want to supervise multiple agents doing real work across multiple repositories, simultaneously, without living in an editor.

---

## My Work View

The central interface is the **My Work view**: a unified dashboard showing everything in motion across your connected repositories.

What it surfaces:
- Active sessions and their current state
- Open pull requests and issues
- Background automations running on your behalf
- Scheduled jobs that have run or are queued

The framing GitHub uses is that agents are handling more work per session, and the developer's role shifts to managing output: reading transcripts, reviewing diffs, making decisions, and redirecting. My Work is the surface where that oversight happens.

---

## Sessions and Worktrees: No More Branch Juggling

Each agent session in the Copilot app runs in its own **git worktree** — a real, isolated copy of a branch checked out at a separate path on your machine or in a cloud sandbox. The app creates and manages all worktrees automatically.

The practical implication: you can run ten sessions against the same repository simultaneously and they will not conflict. No manual setup, no cleanup, no stashing or switching branches between tasks.

Sessions can run:
- **Locally** — in isolated environments on your machine
- **In cloud sandboxes** — ephemeral Linux environments hosted by GitHub (more on those below)

When a session finishes, its worktree is cleaned up. The output is a pull request, a plan, or a canvas — not a pile of branches to untangle.

---

## Canvases: Shared Work Surfaces

A **canvas** is what GitHub calls a bidirectional work surface for a session. It's not just an output log — it's a structured, interactive surface where both agents and humans can read and write.

What a canvas might contain:
- A plan (structured as editable steps)
- A pull request diff with review and comment interface
- A terminal session output
- A browser session snapshot (from agentic browser control)
- A deployment state
- A dashboard or workflow visualization

The interaction model: the agent updates the canvas as it works. The developer can edit, reorder, approve, flag problems, or redirect the agent — on the same surface. It's closer to a shared document than a chat transcript.

This matters for workflows where you want to stay in the loop without driving every step. You define the destination; the agent populates the canvas; you review and unblock.

---

## Agent Merge: PR to Merged, Autonomously

**Agent Merge** handles the PR-through-merge lifecycle — specifically the part that normally requires a developer to babysit: waiting for CI, responding to review comments, re-running checks, and finally merging.

What it does:
- Monitors CI runs and responds to failures
- Tracks required reviewers and their approvals
- Addresses review comments (with configurable scope)
- Merges when all conditions are met

How much autonomy you give it is configurable. At minimum: monitor and notify. At maximum: drive CI back to green, address feedback, and merge when the conditions you specify are satisfied.

One important boundary: repository branch protection rules still apply. If your repo requires human approval on protected branches, Agent Merge waits for that approval before proceeding. It automates the mechanical parts; it doesn't override your governance policies.

---

## Sandboxes: Agents Work Without Breaking Things

The Copilot app provides two sandbox environments for agent sessions:

**Cloud sandboxes** — Fully isolated, ephemeral Linux environments hosted by GitHub. Each cloud session gets its own environment. It's torn down after the session. No shared state, no residual artifacts.

**Local sandboxes** — Isolated environments on your machine. Agents can run, test, and iterate code without touching your working environment or production infrastructure.

Both sandbox types give agents a bounded place to act. The agent can install packages, run tests, build artifacts, and make filesystem changes inside the sandbox — and none of that reaches anything outside the boundary.

---

## Copilot SDK: Now GA in Seven Languages

Alongside the app expansion, GitHub announced the **GitHub Copilot SDK** is now generally available in:

- Node.js
- TypeScript
- Python
- Go
- .NET
- Rust
- Java

The SDK exposes the same agent runtime that powers the Copilot app. If you want to build custom agent tools or integrate Copilot-style agent workflows into your own systems, the SDK is the entry point — not a preview integration, but a GA API.

Third-party integrations are already shipping: LaunchDarkly, PagerDuty, and others have built agent apps that integrate directly with the Copilot runtime.

---

## Other Features Worth Noting

**Voice input** — On-device speech-to-text for hands-free interaction in sessions.

**Chronicle** — Query prior session data. Ask the app what happened in previous sessions against a repository.

**Scheduled automations** — Set up cloud sessions to run on a schedule (similar to a cron job but scoped to agent workflows).

**Copilot CLI integration** — The CLI has a redesigned interface and connects to the same session infrastructure.

**Rubber duck skill** — Built-in `/rubberduck` for problem-solving discussion when you want to think through an issue rather than have an agent execute.

**Custom review skills** — Configurable effort levels and custom skills like `/security-review` for code review sessions.

---

## Access: Who Can Use It Now

The technical preview expanded on June 2, 2026 at Build 2026.

| Plan | Access |
|---|---|
| Copilot Free | Waitlist only |
| Copilot Pro | Technical preview — download now |
| Copilot Pro+ | Technical preview — download now |
| Copilot Business | Technical preview — rolling out across the week |
| Copilot Enterprise | Technical preview — rolling out across the week |

Platform: macOS, Windows, Windows on Arm, Linux.

---

## The Copilot Max Tier

For high-volume agent usage — sustained parallel sessions, heavy Agent Merge usage, large amounts of cloud sandbox time — GitHub has introduced **Copilot Max** at $100/month.

Copilot Max includes $100/month in GitHub AI Credits plus a $100 flex allotment, for $200 in total monthly included usage. Additional credits can be purchased beyond the allotment.

Context: agent sessions consume AI credits (token-based billing, not seat-based). For background on how GitHub's credit billing works, see our [Copilot AI credits builder guide](/builders-log/github-copilot-june-1-token-billing-ai-credits-agentic-cost-guide/).

New sign-ups for Copilot Max are temporarily paused. Existing Pro and Pro+ customers can upgrade.

---

## Builder Decision Guide

**Adopt now if:**
- Your team manages 10+ open PRs at any time and Agent Merge's CI/review automation would recover meaningful time
- You're running parallel agent workstreams (refactoring, testing, migration, docs) and need proper isolation between them
- You're building tools on the Copilot SDK — it's GA, the surface is stable

**Adopt cautiously if:**
- You're on a Copilot Business or Enterprise plan and haven't verified your security team is comfortable with cloud sandboxes processing your code
- Your workflows depend on custom branch protection policies — confirm Agent Merge respects them as documented before relying on it

**Wait if:**
- You're a light single-repository user — the IDE extension covers your use case; the app's value is in multi-repo, multi-session scale
- You're on Copilot Free — waitlist only for now
- You need Mac-specific enterprise MDM management of the app — check GitHub's documentation for current enterprise deployment support

**On Copilot Max:** Run the math against your actual session volume first. $100/month is a significant step up from Pro+. If you're running background automations and parallel sessions daily, the credit allotment may justify it. If you're primarily using it for interactive sessions, it probably doesn't yet.

---

## What to Watch

The technical preview framing means the feature set is not final. Things to watch:

- **GA timeline** — GitHub hasn't announced a GA date for the app itself
- **Enterprise deployment support** — IT-managed rollout, MDM, and network proxy support details
- **Copilot SDK ecosystem** — which third-party integrations ship and their quality
- **Chronicle and scheduling capabilities** — both were mentioned at announcement but details are thin

This is a substantive shift in what GitHub Copilot is. The IDE extension model — you write, the assistant suggests — is no longer the only offering. The Copilot app is a bet that developers increasingly want to manage agents doing work, not just get suggestions while writing code themselves.

Whether that bet lands depends on how Agent Merge, canvases, and the SDK ecosystem develop over the next several months.

---

*Sources: [GitHub Blog — Copilot App: The Agent-Native Desktop Experience](https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/), [GitHub Changelog — Expanded Technical Preview (June 2, 2026)](https://github.blog/changelog/2026-06-02-expanded-technical-preview-availability-for-the-github-copilot-app/), [GitHub Blog — Copilot Individual Plans and Max](https://github.blog/news-insights/company-news/github-copilot-individual-plans-introducing-flex-allotments-in-pro-and-pro-and-a-new-max-plan/), [GitHub Copilot Plans and Pricing](https://github.com/features/copilot/plans)*
