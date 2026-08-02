---
title: "Claude Code Week 28: Background Agents Go Autonomous, Chrome GA, and a Permission-Mode Rename (v2.1.198–200)"
date: 2026-07-04
description: "Three Claude Code versions shipped July 1–3. Background agents now commit, push, and open draft PRs on their own. Claude in Chrome is generally available. And the 'default' permission mode is now labeled 'Manual' everywhere in the CLI and extensions — a naming change, not a behavior change."
tags: ["claude-code", "developer-tools", "anthropic", "ai-agents", "browser-automation"]
sources_audited: 2026-08-01
---

Three [Claude Code](https://code.claude.com/docs/en/changelog) releases landed between July 1 and July 3, 2026 — v2.1.198, v2.1.199, and v2.1.200. They cover a lot of ground: a workflow-changing upgrade to background agents, a milestone for browser automation, a permission-mode display rename that's easy to over-read as a breaking change, and a long list of daemon and streaming reliability fixes.

Here is what matters for builders.

---

## The Headline: Background Agents Now Deliver Work Without Being Asked (v2.1.198)

The most significant shift in this batch is how background agents finish.

Previously, a background agent working in a worktree would stop when it completed its code task and wait — you had to come back, review, and tell it to commit. Starting with v2.1.198, that workflow is gone. When a background agent finishes code work in a worktree, it now **automatically commits the changes, pushes the branch, and opens a draft pull request**, per [Anthropic's changelog](https://code.claude.com/docs/en/changelog) and the [Week 27 release digest](https://code.claude.com/docs/en/whats-new/2026-w27), instead of stopping to ask.

This changes the practical unit of work. You can now send a background agent into a worktree, walk away, and come back to a draft PR ready for review — no follow-up prompt needed. For teams running multiple parallel agents across features or bug fixes, this removes a manual handoff step from every session.

Two companion changes make the autonomous path more observable:

- **Background-agent notifications are now wired into the Notification hook.** Per the [changelog](https://code.claude.com/docs/en/changelog), when a session needs input or finishes, it fires `agent_needs_input` or `agent_completed`. If you have external tooling watching your Claude Code sessions — a dashboard, a Slack alert, a CI trigger — you now have a clean event to react to.
- **Subagents run in the background by default.** Previously this was a gradual rollout; per the [changelog](https://code.claude.com/docs/en/changelog) and [subagent docs](https://code.claude.com/docs/en/sub-agents#run-subagents-in-foreground-or-background), it is now the baseline. Claude keeps running while subagents work and is notified when they finish. You do not need to configure anything.

**What does not change:** background agents still run in worktrees, still respect your `.claude.json` configuration, and still require your normal authentication. The draft PR is created against whatever base branch your repo is configured to target. Review it like any other PR.

---

## Claude in Chrome: Generally Available (v2.1.198)

Claude in Chrome moved out of preview to general availability in v2.1.198, per the [Week 27 release digest](https://code.claude.com/docs/en/whats-new/2026-w27): "The Chrome integration is out of preview for everyone on a direct Anthropic plan."

The integration lets you use Claude Code's CLI or VS Code extension to drive a Chrome browser session — navigate, interact, read page state — without leaving your editor context. The practical case is test-and-debug: you build your code change, then hand off to Claude to open the browser, run through a flow, and report what happened, all in the same session.

The mechanism, per [Anthropic's Chrome integration docs](https://code.claude.com/docs/en/chrome), is the official **Claude in Chrome browser extension** plus a native-messaging connection Claude Code sets up locally — not a headless test runner. It requires the extension (v1.0.36+, installed from the Chrome Web Store) and a direct Anthropic plan (Pro, Max, Team, or Enterprise); it is not available through third-party providers like Amazon Bedrock, Google Cloud's Agent Platform, or Microsoft Foundry.

If your workflow includes any browser-dependent verification — checking that a UI renders, that a redirect lands, that an API response surfaces correctly in a page — this is worth enabling. Instructions for connecting Claude Code to Chrome are in [Anthropic's Chrome integration docs](https://code.claude.com/docs/en/chrome).

---

## Permission Mode Gets a Clearer Name: "Manual" (v2.1.200)

This one is easy to mis-read as a behavior change. It is not — it is a label rename, and getting that distinction wrong could lead you to loosen permissions you didn't mean to touch.

As of v2.1.200, the permission mode that reviews every non-read action — previously displayed as `default` everywhere — is now shown as **Manual** in the CLI, `claude --help`, the VS Code and JetBrains extensions, and the desktop app. Per [Anthropic's permission-modes documentation](https://code.claude.com/docs/en/permission-modes): "The mode that reviews every action is named **Manual** in the CLI... Its config value is `default`, which is what hooks and SDK integrations use. The CLI accepts `manual` as an alias wherever you type the value." Both the "Manual" label and the `manual` alias require v2.1.200 or later; the config value `default` still works exactly as before.

**What did not change:** this mode's actual behavior. Per Anthropic's own mode-comparison table, the `default`/Manual mode has always run reads without asking and prompted for everything else (file edits, shell commands, etc.) — that was true before v2.1.200 and remains true after it. If automation ever relied on this mode proceeding without prompts, that limitation predates this release; nothing about what gets auto-approved changed here.

**What actually changed in v2.1.200**, per the [changelog](https://code.claude.com/docs/en/changelog): `AskUserQuestion` dialogs no longer auto-continue by default. Previously these dialogs had an idle timeout that would resolve them automatically; that behavior is now opt-in via `/config`. Any workflow that counted on the idle-timeout auto-continue as a fallback needs to explicitly re-enable it.

One narrow compatibility note: if any of your tooling parses `claude --help` output, or a VS Code/JetBrains UI string, looking for the literal word "default" as the permission-mode label, it may need updating for the new "Manual" display text. That is a string-matching concern, not a permissions one — do **not** switch to `"defaultMode": "auto"` to "restore" anything, since `auto` is a materially more permissive mode (it auto-approves nearly everything, gated only by a background safety classifier) that has nothing to do with this rename.

---

## Stacked Slash Skills (v2.1.199)

A smaller but useful pattern change: you can now stack multiple slash-skill invocations in a single prompt.

```
/skill-a /skill-b do XYZ
```

Previously only the first skill in the chain was loaded. Per the [changelog](https://code.claude.com/docs/en/changelog), Claude Code now loads all leading slash-skill calls (up to 5) before processing the prompt. If you have a workflow that combines a context-loading skill with an action skill, this removes the extra turn required to invoke them separately.

---

## SSL Error Handling: Fail Fast (v2.1.199)

If Claude Code is running behind a TLS-inspecting proxy, or if `NODE_EXTRA_CA_CERTS` is not set for a custom CA, you used to get a string of failed retries before the actual certificate error surfaced. That delay is gone. Per the [changelog](https://code.claude.com/docs/en/changelog), SSL certificate errors (TLS-inspecting proxies, missing `NODE_EXTRA_CA_CERTS`, expired certs) now fail immediately with a fix hint pointing to the likely cause.

This is relevant for anyone in a corporate network environment where Claude Code traffic passes through a man-in-the-middle proxy. If sessions were previously silently consuming retries, they will now surface the TLS error on the first attempt and tell you what to fix.

---

## Streaming Recovery: Partial Responses Preserved (v2.1.199)

v2.1.199 fixes a class of silent data loss that affected long streaming responses. Previously, if the API emitted a mid-stream error (overloaded response, server error) after partial output was already delivered, that partial output was discarded. You would see an error with nothing to show for the portion that had streamed successfully.

Per the [changelog](https://code.claude.com/docs/en/changelog), the fix keeps the partial output and appends an incomplete-response notice. For long agentic tasks that hit an overload mid-run, you now have something to work with instead of starting from scratch.

The same v2.1.199 release fixes a related case for subagents: one cut off by a rate limit or server error now returns its partial work to the parent instead of failing silently. (A separate v2.1.200 fix covers the narrower case of a subagent cut off before producing any text output — that one now returns an empty result instead of failing uncleanly.)

---

## /dataviz Skill (v2.1.198)

A new built-in skill, `/dataviz`, provides chart and dashboard design guidance including a runnable color-palette validator, per the [changelog](https://code.claude.com/docs/en/changelog) and [Week 27 release digest](https://code.claude.com/docs/en/whats-new/2026-w27). If you are building data visualization UIs or generating charts from agent output, this gives you a starting point for accessible, production-ready color choices without a separate design review step.

---

## Daemon and Background-Agent Reliability Fixes

The three versions collectively close out a long list of background-agent reliability issues that had been accumulating. Per [Anthropic's changelog](https://code.claude.com/docs/en/changelog), the key ones for builders:

**From v2.1.200:**
- Fixed background sessions silently stopping mid-turn after sleep/wake or when reopening a stalled session
- Fixed background sessions re-running a turn cancelled with Esc after a stall respawn
- Fixed background agents never starting again after a crash left a stale `daemon.lock` whose PID the OS reused
- Fixed daemon handover so a reinstalled older build can no longer take over the daemon; build recency is now judged by the version's embedded build timestamp

**From v2.1.199:**
- Fixed the background-agent daemon on Linux killing itself and every running agent every ~50 seconds after an unclean shutdown left a corrupted worker record
- Fixed `claude stop` being silently undone when it raced a background-agent respawn — the respawn now honors the stop

**From v2.1.198:**
- Fixed brief network drops mid-response aborting the turn — transient errors like ECONNRESET now retry with backoff instead of failing
- Fixed background tasks in web, desktop, and VS Code task panels getting stuck on "Running" after they finish or after resuming a session

If you have been seeing background agents vanish, re-run cancelled work, or fail silently after crashes, this batch addresses most of those cases.

---

## Explore Agent Model Upgrade (v2.1.198)

The built-in Explore agent — used for read-only codebase search — previously ran on Haiku regardless of your session's configured model. Per the [changelog](https://code.claude.com/docs/en/changelog), it now inherits the main session's model (capped at Opus). For large codebases where Explore was returning incomplete or shallow results, this is a meaningful quality improvement. You do not need to do anything to get this change.

---

## What to Review in Your Setup

- **Update any tooling that string-matches on the permission-mode label.** As of v2.1.200 it displays as "Manual" instead of "default" in the CLI, `--help`, VS Code, and JetBrains — the underlying `default` config value and its behavior are unchanged, so no permissions action is needed, only a possible string-matching fix. See [Anthropic's permission-modes docs](https://code.claude.com/docs/en/permission-modes).
- **Review AskUserQuestion auto-continue dependencies.** If any workflow relied on idle-timeout auto-continue, opt back in via `/config`.
- **Wire up the Notification hook.** If you are running background agents and want external visibility into their state, `agent_needs_input` and `agent_completed` events are now available.
- **Test draft PR output.** Background agents in worktrees will now create PRs automatically. Make sure your `.claude.json` is pointed at the right base branch and that the agent's commit message convention matches your repo's expectations.
- **Enable Claude in Chrome.** If your workflow includes browser verification, follow the setup at [Anthropic's Chrome integration docs](https://code.claude.com/docs/en/chrome) to connect the extension.
