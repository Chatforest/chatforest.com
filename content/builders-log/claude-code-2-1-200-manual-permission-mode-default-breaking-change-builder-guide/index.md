---
title: "Claude Code 2.1.200: Manual Mode Is Now the Default — What Breaks and How to Fix It"
date: 2026-07-06
description: "Claude Code v2.1.200 flips the permission default from 'allow' to 'Manual' and stops AskUserQuestion from auto-continuing. Both changes break unattended workflows. Here is what changed across 2.1.199, 2.1.200, and 2.1.201, and the exact config lines to restore previous behavior."
tags: ["claude-code", "permissions", "breaking-change", "background-agents", "automation", "builder-guide"]
categories: ["builders-log"]
---

Three Claude Code releases landed between July 2 and July 4, 2026. Two are incremental. One — **2.1.200** — contains a breaking change that will silently stall any unattended pipeline running on the old defaults. Here is what happened and how to adapt.

---

## The Breaking Change: Manual Mode Is Now the Default

**Before 2.1.200**, Claude Code shipped in what was effectively an "allow" default: tool calls and shell commands ran without user confirmation unless you explicitly set a stricter mode.

**Starting with 2.1.200**, the default is **Manual** — every tool call now pauses and waits for your explicit "Allow" before executing.

This affects:
- `claude` in the CLI
- The VS Code extension
- The JetBrains extension
- Anything that passes `--permission-mode default` (which is now aliased to `manual`)

**Who is affected most:** background agents running in automated pipelines or via cron where no human is watching the terminal. Those sessions will now stall silently at the first tool call instead of proceeding.

### To restore the previous behavior

In your project's `.claude.json` or global config, set:

```json
{
  "defaultMode": "acceptEdits"
}
```

Or pass it on the command line:

```
claude --permission-mode acceptEdits
```

The accepted values are `manual` (new default), `acceptEdits` (auto-approve file edits only), and `bypassPermissions` (allow everything, requires elevated trust flag).

If you run Claude Code via a script or CI job, add `--permission-mode acceptEdits` or `--permission-mode bypassPermissions` (only if the environment is already hardened) to your invocation to avoid the stall.

---

## The Second Breaking Change: AskUserQuestion No Longer Auto-Continues

Also in 2.1.200: `AskUserQuestion` dialogs no longer auto-continue after an idle timeout. Previously, if a background agent asked the user a question and nobody answered, it would eventually self-continue and pick a default path.

Now it stalls indefinitely until you respond.

**Why this matters for builders:** any prompt in your agent's skill chain that calls `AskUserQuestion` — including many third-party skills — will block the pipeline until a human responds. If you had relied on the old idle-timeout behavior (e.g., "if nobody answers in 30 seconds, proceed with X"), that behavior is gone.

**To opt back in:** set an idle timeout in `/config`:

```
/config → idle-timeout → 30
```

This re-enables auto-continuation after 30 seconds of no input. The value is in seconds.

---

## What Fixed in 2.1.199 (Released July 2–3)

2.1.199 was a 24-change reliability release focused on streaming and background agent stability. Key fixes:

**Streaming / API errors:**
- Partial streaming responses are now preserved when the API emits a mid-stream overload or server error, rather than being discarded. You now receive the partial output with an "incomplete response" notice instead of nothing.
- Subagents cut off by a rate limit or server error now return partial work to the parent instead of silently failing.
- Subagents that hit a usage limit now report the error to the parent agent rather than reporting success.

**Linux daemon crash:**
- A Linux-specific bug where the background-agent daemon killed itself (and all running agents) roughly every 50 seconds after an unclean shutdown has been fixed. The root cause was a corrupted worker record from a prior crash.

**SSL / proxy errors:**
- SSL certificate errors — common behind TLS-inspecting proxies or when `NODE_EXTRA_CA_CERTS` is not set — previously burned all retries before surfacing a useful error message. Now they fail immediately with a clear fix hint.

**IDE and terminal:**
- JetBrains terminals (IntelliJ, PyCharm, WebStorm) no longer flicker.
- `Shift+non-ASCII` characters (e.g., Shift+ä → Ä) are no longer dropped in terminals using the Kitty keyboard protocol (WezTerm, Ghostty, kitty).

**Skills:**
- Stacked slash-skill invocations — `\skill-a \skill-b do XYZ` — now load all leading skills (up to 5). Previously only the first skill loaded.

---

## What Fixed in 2.1.200 (Beyond the Breaking Changes)

Alongside the permission defaults, 2.1.200 also shipped a batch of background-session stability fixes:

- **Sleep/wake crash**: Background sessions that silently stopped mid-turn after a macOS or Linux sleep/wake cycle are now stable through suspend-resume.
- **Daemon lock file**: Daemon crashes that left a stale `daemon.lock` with a reused PID are fixed. Previously this prevented the daemon from restarting until the lock file was manually removed.
- **MCP server config crash**: Starting Claude Code with a non-array value for `disabledMcpServers` or `enabledMcpServers` in `.claude.json` no longer crashes at startup.
- **Git worktree plugins**: Project-scoped plugins now load correctly when working inside a git worktree.
- **Control bytes**: Control bytes from background-agent output no longer reach the terminal (they caused garbled display in some terminal emulators).
- **Voice dictation**: "Voice connection failed" false positives are fixed.
- **tmux flicker**: Rendering flicker under tmux 3.4+ is resolved.
- **Accessibility**: Decorative glyphs are now hidden from screen readers; transcript symbols are read as short labels; nested tables are read as "Header: value" lines.

---

## What Fixed in 2.1.201 (July 4)

A single targeted fix: Claude Sonnet 5 sessions no longer receive mid-conversation system roles for harness reminders. This corrects an inconsistency in how the harness injected internal instructions during long Sonnet 5 sessions, which could subtly affect behavior partway through a conversation.

---

## Summary: What You Need to Do Right Now

| Scenario | Action |
|---|---|
| Running Claude Code unattended (CI, cron, scripts) | Add `--permission-mode acceptEdits` to your invocation or set `"defaultMode": "acceptEdits"` in `.claude.json` |
| Using a skill that calls `AskUserQuestion` in a pipeline | Add an idle-timeout in `/config`, or restructure the skill to not block |
| Running the VS Code or JetBrains extension interactively | No action needed — Manual mode is fine for interactive use |
| Using background agents launched with `claude agents` | Check your agent logs; add `--permission-mode acceptEdits` if agents are stalling |

The 2.1.199 stability improvements (streaming, Linux daemon, SSL) apply automatically — no config changes required to benefit from them.

---

*Claude Code 2.1.199 shipped July 2–3, 2026. Claude Code 2.1.200 shipped July 3, 2026. Claude Code 2.1.201 shipped July 4, 2026. Version numbers are visible via `claude --version`.*
