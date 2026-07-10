---
title: "Claude Code July 2026 Changelog: MCP Timeout Bug Fixed, /doctor for CLAUDE.md, and Background Agent Hardening"
date: 2026-07-10
description: "Two Claude Code releases this week (v2.1.205 July 8, v2.1.206 July 9) fixed a silent MCP timeout bug that was killing any tool call longer than 60 seconds, added /doctor to trim bloated CLAUDE.md files, and hardened background agent upgrades. Builder action items inside."
tags: ["claude-code", "mcp", "anthropic", "background-agents", "claude-md", "changelog", "builder-guide", "developer-tools", "debugging", "workflow"]
---

Two Claude Code releases shipped back-to-back this week — v2.1.205 on July 8 and v2.1.206 on July 9 — and together they fix several issues that were quietly breaking builder workflows. The most impactful: a bug where per-server MCP timeout configuration was silently ignored, forcing every long-running tool call through a 60-second wall regardless of what your config said. If you've been getting mysterious MCP tool failures on operations that should take two minutes, this is why.

Here's a breakdown of what changed and what to do about each fix.

## The MCP 60-Second Wall Is Gone

The most consequential fix in v2.1.206: MCP servers configured via `--mcp-config` or `.mcp.json` were ignoring a per-server `request_timeout_ms` field entirely. All MCP tool calls silently fell back to the 60-second default, regardless of what the config said.

This affected any MCP integration where a tool call runs longer than a minute: large database queries, image generation pipelines, code execution sandboxes, web scraping with retries, long-context document processing. You'd set a timeout, the build would pass config validation, and then your session would fail at runtime with no explanation connecting the failure to the ignored config field.

The fix is straightforward — the field now works. How to configure it in `.mcp.json`:

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["-y", "@myorg/db-mcp-server"],
      "request_timeout_ms": 300000
    },
    "sandbox": {
      "command": "python",
      "args": ["-m", "my_sandbox_server"],
      "request_timeout_ms": 120000
    },
    "fast-search": {
      "command": "npx",
      "args": ["-y", "@myorg/search-mcp"],
      "request_timeout_ms": 10000
    }
  }
}
```

One constraint to note: any value below 1000 ms is treated as invalid and floored to a 1-second watchdog that aborts the call. Set per-server values to at least 1000 ms. For operations with no predictable upper bound, omit `request_timeout_ms` entirely and let the system-level timeout govern; the global default MCP tool timeout before v2.1.206 was 60 seconds, and that has not changed — the fix is that your per-server value now overrides it as intended.

## /doctor Now Diagnoses Your CLAUDE.md

`/doctor` previously ran a basic environment check. In v2.1.206 it gained a new capability: it reads your checked-in `CLAUDE.md` files and proposes trimming content that Claude could already derive from the codebase.

The practical issue it addresses: CLAUDE.md files tend to accumulate over time. A team documents a pattern, documents an exception, documents the exception to the exception. Eventually you have a 3,000-word instruction file loaded into context on every single turn. Most of it describes things Claude can see directly in the code.

Running `/doctor` (or its alias `/checkup`) will:

1. Parse your CLAUDE.md across the project hierarchy
2. Cross-reference sections against what's observable in your file structure, imports, and conventions
3. Propose specific removals with reasoning

The goal is to keep CLAUDE.md focused on what can't be derived — organizational constraints, team conventions that don't show up in code, environment-specific quirks, non-obvious decisions and their rationale — and strip out everything else. Leaner instruction files mean faster context loading and fewer tokens consumed on every turn.

You don't have to accept every proposal. The command presents suggestions; you decide what to remove. It's most useful on projects that have had multiple contributors adding instructions over several months.

## EnterWorktree Confirmation

`EnterWorktree` now asks for explicit confirmation before entering git worktrees that live outside `.claude/worktrees/`. Previously the command would proceed silently.

The failure mode this prevents: you have a feature branch worktree checked out somewhere on disk for reference, and an agent command enters it and starts making changes. The worktree is real, the changes are real, but the session context was pointed at a different branch. Hard to catch, hard to roll back if you weren't watching.

The confirmation prompt is a speed bump, not a hard block — you can still enter external worktrees, you just have to say yes explicitly. For worktrees inside `.claude/worktrees/` (the managed path Claude Code creates for parallel sessions), no confirmation is required.

## Auth Error Clarity

An expired or revoked login token used to surface as "there is an issue with the selected model" — a misleading error that pointed at model configuration when the actual problem was authentication.

v2.1.206 fixes this: expired sessions now detect the auth state and prompt you to run `/login` directly. The old error is gone.

This was a disproportionate time sink in new-project setup and in enterprise environments where tokens expire on rotation schedules. If you've ever spent twenty minutes troubleshooting model picker settings when the real issue was a stale token, this is the fix.

## OAuth MCP Token Refresh

MCP servers that authenticate via OAuth were requiring manual re-authentication after token refresh failures. If a refresh request failed (network blip, server-side token revocation, rate limiting), the server connection would drop and stay dropped until a human ran the auth flow again.

v2.1.206 adds recovery logic: Claude Code now detects the refresh failure and attempts to re-authenticate automatically before surfacing an error to the user. For background agent sessions that can't interrupt for human input, this is the difference between a session completing and a session silently failing mid-run.

## Background Agent Upgrades (No More Stale-Session Lag)

Before v2.1.206, a Claude Code update during an active session could cause the next background agent launch to run a slow in-session upgrade — the daemon would detect the version mismatch and upgrade on startup, stalling the agent for seconds or more before doing any actual work.

Now: upgrades happen immediately in the background after a Claude Code update installs. By the time you start your next session, the upgrade is already done. Stale-session upgrade lag disappears.

For teams running many parallel agents or scripted agent pipelines, this removes an unpredictable latency source from session startup.

## v2.1.205: Auto Mode Transcript Protection

v2.1.205, which shipped the day before, added one notable security feature: a new auto mode rule that blocks tampering with session transcript files.

Session transcripts record what the agent did and said. A compromised MCP tool or injected prompt could attempt to overwrite or delete transcript records — either to hide malicious actions from audit review, or to alter the apparent history in a way that confuses future sessions.

The new rule makes transcript mutation a blocked auto mode action. Attempts to modify transcript files via agent tool calls require explicit human approval. This is part of a broader pattern of hardening the parts of Claude Code's state that should be read-only during a session.

## /commit-push-pr Respects Non-Origin Remotes

`/commit-push-pr` previously auto-allowed git push only to a remote named `origin`. v2.1.206 expands this: it now auto-allows push to the repo's configured `remote.pushDefault` value, and also to the sole configured remote if only one exists — even if it's not named `origin`.

This matters for repos that use an explicit `remote.pushDefault` (common in repos with multiple remotes: an upstream fork and a personal fork, or a CI remote alongside origin), and for self-hosted setups where the remote has a custom name. Previously you'd get a permission prompt mid-flow; now it proceeds as expected.

## /code-review Quality Improvements on Opus 4.8

`/code-review` findings quality has been improved on `claude-opus-4-8` across all effort levels (`low`, `medium`, `high`, `max`). No configuration change required — if you were already using Opus 4.8 for code review, the improvement applies automatically.

For reference: the default `/code-review` model in Claude Code is determined by your current model setting. If you've been running reviews on Sonnet 5 (the new default since v2.1.197), this change doesn't directly apply. To use Opus 4.8 for a review, pass it explicitly: `/code-review --model claude-opus-4-8`.

## Builder Action Items

**Update immediately** to pick up the MCP timeout fix:

```bash
npm install -g @anthropic-ai/claude-code@latest
claude --version  # confirm you're on 2.1.206+
```

**Add `request_timeout_ms` to your `.mcp.json`** for any MCP server that runs operations longer than 60 seconds. Set per-server values in milliseconds; the minimum effective value is 1000ms.

**Run `/doctor`** in your main project sessions. Review its proposals — trim content that Claude can infer from the code, keep content that encodes constraints, decisions, and context that isn't visible in the file structure.

**Check `/commit-push-pr`** if your repo uses a non-`origin` push remote. Test it once manually after updating to confirm the new auto-allow logic covers your remote setup.

**Nothing to do for the rest**: the EnterWorktree confirmation, auth error clarity, OAuth token refresh, background upgrade behavior, and transcript protection all take effect automatically.

## What This Update Isn't

Neither release changes model behavior, pricing, or the default model selection (still Sonnet 5 since v2.1.197). No new major features shipped — this is an infrastructure and reliability release. The MCP timeout fix is load-bearing for any production pipeline using slow MCP tools; the rest are quality-of-life improvements that compound over time.

The [official changelog](https://code.claude.com/docs/en/changelog) has the full commit-level diff if you want to audit specific changes before deploying in a controlled environment.
