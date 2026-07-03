---
title: "Claude Code Week 28: Background Agents Go Autonomous, Chrome GA, and a Permission-Mode Breaking Change (v2.1.198–200)"
date: 2026-07-04
description: "Three Claude Code versions shipped July 1–3. Background agents now commit, push, and open draft PRs on their own. Claude in Chrome is generally available. And the permission mode default changed from 'default' to 'Manual' — a silent breaking change for any CI or automation that relied on the old behavior."
tags: ["claude-code", "developer-tools", "anthropic", "ai-agents", "browser-automation"]
---

Three Claude Code releases landed between July 1 and July 3, 2026 — v2.1.198, v2.1.199, and v2.1.200. They cover a lot of ground: a workflow-changing upgrade to background agents, a milestone for browser automation, a behavior change that will break some CI setups, and a long list of daemon and streaming reliability fixes.

Here is what matters for builders.

---

## The Headline: Background Agents Now Deliver Work Without Being Asked (v2.1.198)

The most significant shift in this batch is how background agents finish.

Previously, a background agent working in a worktree would stop when it completed its code task and wait — you had to come back, review, and tell it to commit. Starting with v2.1.198, that workflow is gone. When a background agent finishes code work in a worktree, it now **automatically commits the changes, pushes the branch, and opens a draft pull request** before the session ends.

This changes the practical unit of work. You can now send a background agent into a worktree, walk away, and come back to a draft PR ready for review — no follow-up prompt needed. For teams running multiple parallel agents across features or bug fixes, this removes a manual handoff step from every session.

Two companion changes make the autonomous path more observable:

- **Background-agent notifications are now wired into the Notification hook.** When a session needs input or finishes, it fires `agent_needs_input` or `agent_completed`. If you have external tooling watching your Claude Code sessions — a dashboard, a Slack alert, a CI trigger — you now have a clean event to react to.
- **Subagents run in the background by default.** Previously this was a gradual rollout; it is now the baseline. Claude keeps running while subagents work and is notified when they finish. You do not need to configure anything.

**What does not change:** background agents still run in worktrees, still respect your `.claude.json` configuration, and still require your normal authentication. The draft PR is created against whatever base branch your repo is configured to target. Review it like any other PR.

---

## Claude in Chrome: Generally Available (v2.1.198)

Claude in Chrome moved from rollout to general availability in v2.1.198.

The integration lets you use Claude Code's CLI or VS Code extension to drive a Chrome browser session — navigate, interact, read page state — without leaving your editor context. The practical case is test-and-debug: you build your code change, then hand off to Claude to open the browser, run through a flow, and report what happened, all in the same session.

No Playwright, no Node.js runtime, no separate test harness required on the Claude Code side. The underlying mechanism uses Chrome for Testing.

If your workflow includes any browser-dependent verification — checking that a UI renders, that a redirect lands, that an API response surfaces correctly in a page — this is worth enabling. Instructions for connecting Claude Code to Chrome are at `code.claude.com/docs/en/chrome`.

---

## Breaking Change: Permission Mode Now Defaults to Manual (v2.1.200)

This is the change most likely to cause unexpected breakage in existing setups.

Before v2.1.200, Claude Code's permission mode defaulted to `"default"`. As of July 3, it defaults to `"manual"`. This affects:

- The CLI (`claude --help` now shows `--permission-mode manual` as the default)
- VS Code extension
- JetBrains extension
- Any `"defaultMode"` value in `.claude.json` that was previously relying on the implicit `"default"` behavior

**Why this matters:** The old `"default"` mode auto-allowed many tool calls without asking. The new `"manual"` mode requires explicit approval for state-changing operations. If you have scripts, CI jobs, or automation that invoke Claude Code and expected it to proceed without prompts, those sessions will now pause and wait for input that never comes.

**The fix is explicit:** set `"defaultMode": "auto"` in your `.claude.json` (or pass `--permission-mode auto` on the CLI) to restore the previous behavior. Do not rely on the implicit default going forward — it has now changed once and could change again.

The release notes also change `AskUserQuestion` dialogs to no longer auto-continue by default. Previously these dialogs had an idle timeout that would resolve them automatically. That behavior is now opt-in via `/config`. Any workflow that counted on auto-continue as a fallback needs to be updated.

---

## Stacked Slash Skills (v2.1.199)

A smaller but useful pattern change: you can now stack multiple slash-skill invocations in a single prompt.

```
/skill-a /skill-b do XYZ
```

Previously only the first skill in the chain was loaded. Now Claude Code loads all leading slash-skill calls (up to 5) before processing the prompt. If you have a workflow that combines a context-loading skill with an action skill, this removes the extra turn required to invoke them separately.

---

## SSL Error Handling: Fail Fast (v2.1.199)

If Claude Code is running behind a TLS-inspecting proxy, or if `NODE_EXTRA_CA_CERTS` is not set for a custom CA, you used to get a string of failed retries before the actual certificate error surfaced. That delay is gone. SSL certificate errors now fail immediately with a fix hint pointing to the likely cause.

This is relevant for anyone in a corporate network environment where Claude Code traffic passes through a man-in-the-middle proxy. If sessions were previously silently consuming retries, they will now surface the TLS error on the first attempt and tell you what to fix.

---

## Streaming Recovery: Partial Responses Preserved (v2.1.199)

v2.1.199 fixes a class of silent data loss that affected long streaming responses. Previously, if the API emitted a mid-stream error (overloaded response, server error) after partial output was already delivered, that partial output was discarded. You would see an error with nothing to show for the portion that had streamed successfully.

The fix keeps the partial output and appends an incomplete-response notice. For long agentic tasks that hit an overload mid-run, you now have something to work with instead of starting from scratch.

The same logic applies to subagents cut off by rate limits or server errors — they now return their partial work rather than an empty result.

---

## /dataviz Skill (v2.1.198)

A new built-in skill, `/dataviz`, provides chart and dashboard design guidance including a runnable color-palette validator. If you are building data visualization UIs or generating charts from agent output, this gives you a starting point for accessible, production-ready color choices without a separate design review step.

---

## Daemon and Background-Agent Reliability Fixes

The three versions collectively close out a long list of background-agent reliability issues that had been accumulating. The key ones for builders:

**From v2.1.200:**
- Fixed background sessions silently stopping mid-turn after sleep/wake or stalled session reopening
- Fixed background sessions re-running cancelled turns (Esc) after stall respawn
- Fixed background agents failing to restart after crash left stale `daemon.lock` with a reused PID
- Fixed daemon handover — reinstalled older builds can no longer take over active sessions; build recency is now judged by embedded timestamp rather than filesystem metadata

**From v2.1.199:**
- Fixed background-agent daemon on Linux killing itself and every running agent every ~50 seconds after unclean shutdown left a corrupted worker record — this was causing complete loss of active agents on any Linux machine that had ever had an unclean shutdown
- Fixed `claude stop` being silently undone when it raced background-agent respawn

**From v2.1.198:**
- Fixed brief network drops mid-response aborting the turn — transient ECONNRESET errors now retry with backoff
- Fixed background tasks in web, desktop, and VS Code task panels getting stuck on "Running" after finish or session resume

If you have been seeing background agents vanish, re-run cancelled work, or fail silently after crashes, this batch addresses most of those cases.

---

## Explore Agent Model Upgrade (v2.1.198)

The built-in Explore agent — used for read-only codebase search — previously ran on haiku regardless of your session's configured model. It now inherits the main session's model (capped at opus). For large codebases where Explore was returning incomplete or shallow results, this is a meaningful quality improvement. You do not need to do anything to get this change.

---

## What to Review in Your Setup

- **Check your permission mode.** If any automation passes through Claude Code without explicit permissions configured, set `"defaultMode": "auto"` or `--permission-mode auto` before the v2.1.200 upgrade reaches your environment.
- **Review AskUserQuestion auto-continue dependencies.** If any workflow relied on idle-timeout auto-continue, opt back in via `/config`.
- **Wire up the Notification hook.** If you are running background agents and want external visibility into their state, `agent_needs_input` and `agent_completed` events are now available.
- **Test draft PR output.** Background agents in worktrees will now create PRs automatically. Make sure your `.claude.json` is pointed at the right base branch and that the agent's commit message convention matches your repo's expectations.
- **Enable Claude in Chrome.** If your workflow includes browser verification, follow the setup at `code.claude.com/docs/en/chrome` to connect the extension.
