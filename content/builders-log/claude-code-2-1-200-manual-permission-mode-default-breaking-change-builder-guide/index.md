---
title: "Claude Code 2.1.200: AskUserQuestion Stops Auto-Continuing — What Actually Breaks and How to Fix It"
date: 2026-07-06
description: "Claude Code v2.1.200 stops AskUserQuestion from auto-continuing on an idle timeout, which breaks unattended pipelines that rely on it. It also renames the existing default permission mode to 'Manual' — a label change, not a behavior change, despite how the release note reads. Verified against Anthropic's changelog and docs, with the exact settings to restore previous behavior."
tags: ["claude-code", "permissions", "breaking-change", "background-agents", "automation", "builder-guide"]
categories: ["builders-log"]
sources_audited: 2026-08-03
---

Three [Claude Code](https://code.claude.com/docs/en/changelog) releases — [2.1.199, 2.1.200, and 2.1.201](https://code.claude.com/docs/en/changelog) — landed between July 2 and July 3, 2026. Two are incremental. **2.1.200** contains one real breaking change for unattended pipelines: [`AskUserQuestion` dialogs stopped auto-continuing on an idle timeout by default](https://code.claude.com/docs/en/changelog). It also gave the existing default permission mode an explicit "Manual" label — a naming clarification, not a new restriction. Here is what happened and how to adapt.

---

## Correction: The Default Permission Mode Was Renamed, Not Changed

The config value you get by leaving `defaultMode` unset — `default` — already prompted for permission on first use of each tool before 2.1.200, and it still does now. That prompt-on-first-use behavior did not change. What [2.1.200 actually changed](https://code.claude.com/docs/en/permission-modes) is the *label*: the CLI, `--help`, the VS Code extension, the JetBrains extension, and the desktop app now display this mode as **Manual**, and `--permission-mode manual` / `"defaultMode": "manual"` are now accepted as aliases for the same `default` value. [Anthropic's permission-modes reference](https://code.claude.com/docs/en/permission-modes) is explicit that the Manual label and the `manual` alias "require Claude Code v2.1.200 or later" — it does not say the underlying approval behavior changed, and independent coverage of the release [describes it the same way](https://x.com/ClaudeCodeLog/status/2073091434123591872): "Permission mode changed to Manual across CLI, VS Code, JetBrains and --help."

**What this means for pipelines:** if an unattended pipeline was already running on the unmodified `default` mode, it was already stalling on the first tool call long before 2.1.200 — that has not changed. If your pipeline was running unattended *without* stalling, it was already using `acceptEdits`, `bypassPermissions`, or `auto` mode explicitly, and 2.1.200 does not affect it. The genuine new risk for automation in this release is the `AskUserQuestion` change below, not the Manual rename.

### If you need non-interactive tool approval

Set it in a settings file (note the mode lives under `permissions`, not at the top level):

```json
{
  "permissions": {
    "defaultMode": "acceptEdits"
  }
}
```

Or pass it on the command line:

```
claude --permission-mode acceptEdits
```

Per [Anthropic's permission-modes documentation](https://code.claude.com/docs/en/permission-modes): `manual` (the `default` value, standard prompt-on-first-use behavior) is the mode Claude Code has always started in unless configured otherwise; `acceptEdits` auto-approves file edits and common filesystem commands (`mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, `sed`) within the working directory; and `bypassPermissions` skips permission prompts entirely, requires the `--dangerously-skip-permissions` flag (or `--permission-mode bypassPermissions` plus `permissions.defaultMode: "bypassPermissions"` in settings), and shows a one-time warning dialog you must accept before it takes effect interactively.

If you run Claude Code via a script or CI job, add `--permission-mode acceptEdits` or `--permission-mode bypassPermissions` (only if the environment is already hardened) to your invocation to avoid stalling on tool prompts.

---

## The Real Breaking Change: AskUserQuestion No Longer Auto-Continues

This is the change that actually affects unattended pipelines. Per [Anthropic's changelog](https://code.claude.com/docs/en/changelog), 2.1.200 "changed `AskUserQuestion` dialogs to no longer auto-continue by default." Previously, if a background agent asked the user a question and nobody answered, it would eventually self-continue with whatever options were already selected.

Now, by default, it stalls indefinitely until you respond.

**Why this matters for builders:** any prompt in your agent's skill chain that calls `AskUserQuestion` — including many third-party skills — will block the pipeline until a human responds. If you had relied on the old idle-timeout behavior (e.g., "if nobody answers, proceed with the already-selected option"), that default behavior is gone.

**To opt back in:** 2.1.200 introduced a new setting, [`askUserQuestionTimeout`](https://code.claude.com/docs/en/settings), which appears in `/config` as **"Question auto-continue timeout."** It only accepts one of four fixed values — `"60s"`, `"5m"`, `"10m"`, or `"never"` (the new default) — not an arbitrary number of seconds:

```
/config → Question auto-continue timeout → 60s
```

Setting it to `60s`, `5m`, or `10m` restores auto-continuation after that fixed idle period. This setting is only read from user-level settings, not from project or local `.claude/settings.json` files.

---

## What Fixed in 2.1.199 (Released July 2)

Per [Anthropic's changelog](https://code.claude.com/docs/en/changelog), 2.1.199 was a 24-change reliability release focused on streaming and background-agent stability. Key fixes:

**Streaming / API errors:**
- Partial streaming responses are now preserved when the API emits a mid-stream overload or server error, rather than being discarded. You now receive the partial output with an "incomplete response" notice instead of nothing.
- Subagents cut off by a rate limit or server error now return partial work to the parent instead of silently failing.
- Subagents that hit a usage limit now report the error to the parent agent rather than reporting success.

**Linux daemon crash:**
- A Linux-specific bug where the background-agent daemon killed itself (and all running agents) roughly every 50 seconds after an unclean shutdown has been fixed. The root cause was a corrupted worker record from a prior crash.

**SSL / proxy errors:**
- SSL certificate errors — common behind TLS-inspecting proxies or when `NODE_EXTRA_CA_CERTS` is not set — previously burned all retries before surfacing a useful error message. Now they fail immediately with a clear fix hint.

**Skills:**
- Stacked slash-skill invocations — `/skill-a /skill-b do XYZ` — now load all leading skills (up to 5). Previously only the first skill loaded.

*Correction: an earlier version of this article also credited 2.1.199 with fixing JetBrains terminal flicker and a Shift+non-ASCII/Kitty-keyboard-protocol input bug. Those fixes are real, but they shipped in [Claude Code 2.1.166](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md), not 2.1.199 — removed here since they don't belong to this release.*

---

## What Fixed in 2.1.200 (Beyond the Breaking Changes)

Alongside the permission-mode label change, [2.1.200 also shipped](https://code.claude.com/docs/en/changelog) a batch of background-session stability fixes:

- **Sleep/wake crash**: Background sessions that silently stopped mid-turn after a sleep/wake cycle, or when reopening a stalled session, are now fixed.
- **Daemon lock file**: Background agents that could never start again after a crash left a stale `daemon.lock` with a reused PID are fixed.
- **MCP server config crash**: Starting Claude Code with a non-array value for `disabledMcpServers` or `enabledMcpServers` in `.claude.json` no longer crashes at startup.
- **Git worktree plugins**: Project-scoped plugins now load correctly when working from a git worktree of the same repository.
- **Control bytes**: Control bytes from background-agent output no longer reach the terminal in the agent view.
- **Voice dictation**: A misleading "Voice connection failed" message that appeared when a recording captured no audio is fixed.
- **tmux flicker**: Rendering flicker under tmux 3.4+ is resolved (via synchronized terminal output).
- **Accessibility**: Decorative glyphs are now hidden from screen readers; transcript symbols are read as short labels; nested tables are read as "Header: value" lines.

---

## What Fixed in 2.1.201 (July 3)

A single targeted fix, per [Anthropic's changelog](https://code.claude.com/docs/en/changelog): Claude Sonnet 5 sessions no longer use the mid-conversation system role for harness reminders. This corrects an inconsistency in how the harness injected internal instructions during long Sonnet 5 sessions, which could subtly affect behavior partway through a conversation. (Note: 2.1.201 shipped the same day as 2.1.200 — July 3, 2026, not July 4 as an earlier version of this article stated.)

---

## Summary: What You Need to Do Right Now

| Scenario | Action |
|---|---|
| Running Claude Code unattended (CI, cron, scripts) that was already stalling on tool prompts | Add `--permission-mode acceptEdits` to your invocation or set `permissions.defaultMode: "acceptEdits"` in your settings file |
| Using a skill that calls `AskUserQuestion` in a pipeline | Set "Question auto-continue timeout" (`askUserQuestionTimeout`) to `60s`, `5m`, or `10m` in `/config`, or restructure the skill to not block |
| Running the VS Code or JetBrains extension interactively | No action needed — the Manual label is just a rename of existing behavior |
| Using background agents launched with `claude agents` | Check your agent logs; add `--permission-mode acceptEdits` if agents are stalling on tool prompts |

The 2.1.199 stability improvements (streaming, Linux daemon, SSL) apply automatically — no config changes required to benefit from them.

---

*Claude Code 2.1.199 shipped July 2, 2026. Claude Code 2.1.200 and 2.1.201 both shipped July 3, 2026. [See Anthropic's changelog](https://code.claude.com/docs/en/changelog) for exact dates. Version numbers are visible via `claude --version`.*
