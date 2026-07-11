---
title: "Claude Code v2.1.207: Three Breaking Changes Every Plugin and Hook Author Must Handle"
date: 2026-07-11
description: "Claude Code v2.1.207 lands today with security-driven breaking changes to hook notation, plugin config scoping, and auto mode settings location. If you distribute plugins or run hooks in CI, your setup will break on update. Here's the full migration map."
og_description: "v2.1.207 rejects ${user_config.*} in shell hooks, stops reading pluginConfigs from project settings.json, and moves autoMode out of repo settings.local.json. Three breaking changes, with migration steps for each."
content_type: "Builder's Log"
categories: ["Anthropic", "Claude Code", "Developer Tools", "Security"]
tags: ["claude-code", "anthropic", "breaking-changes", "plugin-hooks", "shell-injection", "bedrock", "vertex-ai", "mcp", "security", "auto-mode", "opus-4-8", "july-2026", "builders-log"]
---

Claude Code v2.1.207 shipped today (July 11, 2026) and it is a security-heavy release: 24 changes, most of them bug fixes and hardening, but three of those changes are **breaking** in ways that will silently fail if you don't migrate before updating. If you maintain a plugin, distribute hooks, or store per-project settings in `.claude/`, read this before running `npm update -g @anthropic-ai/claude-code`. Part of our **[Builder's Log](/builders-log/)**.

---

## The Three Breaking Changes

### 1. `${user_config.*}` notation is now rejected in shell hooks

If you use shell-format hook commands that interpolate plugin options via `${user_config.some_key}`, those commands will now fail with a rejection error. Anthropic flagged this pattern as a shell-injection vector — a malicious project or crafted config value could escape the substitution and execute arbitrary shell commands.

**What breaks:** Any hook, monitor, or `headersHelper` that uses shell-format commands with `${user_config.*}` references.

**Migration — two options:**

Option A: Switch to exec format (args array). Instead of a shell string, provide a command array:

```json
// Before — shell format, now rejected
{
  "hooks": {
    "PreToolUse": [{
      "command": "my-hook --key ${user_config.api_key}"
    }]
  }
}

// After — exec format, safe
{
  "hooks": {
    "PreToolUse": [{
      "command": ["my-hook", "--key", "$CLAUDE_PLUGIN_OPTION_API_KEY"]
    }]
  }
}
```

Option B: Read config inside the script itself. Move the value into the server's `env` block or a config file the script reads at runtime — no interpolation in the command definition.

The exec-format approach is the cleaner permanent fix. Shell-format commands with `$VARIABLE` substitution are still allowed; only the `${user_config.*}` specific syntax is rejected.

---

### 2. `pluginConfigs` are no longer read from project-level `.claude/settings.json`

Previously, plugin option values could be set at any of four levels: user settings (`~/.claude/settings.json`), the `--settings` flag, managed settings (enterprise), or project-level `.claude/settings.json`. As of v2.1.207, the project-level source is dropped. Claude Code will only read `pluginConfigs` from user settings, `--settings`, and managed settings.

**What breaks:** Teams that checked plugin configuration into the repo under `.claude/settings.json` will find those values silently ignored after updating. The plugin will still load; it will just not receive the configured values, potentially falling back to defaults or failing unexpectedly.

**Why:** Repo-level plugin config means any project you open — including third-party repos or adversarially crafted repos — can inject plugin option values. Removing this source isolates plugin configuration to user-controlled and admin-controlled locations.

**Migration:** Move plugin configs from `.claude/settings.json` to `~/.claude/settings.json` (per-user) or supply them via `--settings <path>` in your CI invocation. If you need per-project variation, pass values through environment variables and read them inside the plugin script.

---

### 3. `autoMode` in `.claude/settings.local.json` inside repos is now ignored

Storing `autoMode: true` in a repo-level `.claude/settings.local.json` no longer has any effect. Auto mode must now be set in your user-level `~/.claude/settings.json` (or through managed/enterprise settings).

**What breaks:** Any repo where someone enabled auto mode by committing or generating a local settings file with `autoMode: true`. Those sessions will revert to interactive mode after update.

**Why:** Same threat model as above — a repo shouldn't be able to opt itself into auto mode. Auto mode allows Claude Code to bypass per-action permission prompts. The attack scenarios in this week's [Friendly Fire and HalluSquatting disclosures](/builders-log/friendly-fire-hallusquatting-ai-coding-agent-auto-mode-prompt-injection-hallucination-builder-security-guide/) both required auto mode to work without user interaction. Moving this setting to user scope means a repository cannot silently enable unattended execution.

**Migration:** If you legitimately run Claude Code in auto mode against repos — CI pipelines, overnight agents — move the `autoMode: true` to `~/.claude/settings.json` on the machine running it. Enterprise teams can push this through managed settings.

---

## New Features Worth Knowing

### Auto mode is now the default on Bedrock, Vertex, and Foundry

Previously, enterprise teams routing Claude Code through managed cloud infrastructure needed to set `CLAUDE_CODE_ENABLE_AUTO_MODE=1` to unlock auto mode. Starting v2.1.207, auto mode is available on Bedrock, Vertex AI, and Azure Foundry without any environment variable. The opt-in gate is gone.

Note the relationship between this and Breaking Change 3: auto mode is now *available* on cloud platforms by default, but *enabling* it still requires explicit configuration in user/managed settings. The removal of the env var opt-in just unlocks the feature gate; it doesn't automatically enable unattended operation.

If you want to *disable* auto mode on cloud infrastructure (e.g., during sensitive runs), set `disableAutoMode: true` in your settings.

### Claude Opus 4.8 is now the default on Bedrock, Vertex, and AWS Claude Platform

The default model backing Claude Code sessions on cloud platforms has moved from the previous default to Claude Opus 4.8. If you pin model versions explicitly in your configuration, nothing changes. If you rely on the default, your sessions are now on a more capable model — but also a more expensive one. Worth checking your billing expectations if you run high-volume Claude Code automation on Bedrock or Vertex.

### In-app browser in the desktop app

The Claude Code desktop application now includes a built-in browser. Useful for OAuth flows, documentation lookups, and session-authenticated web tasks without switching to an external window. Minor UX improvement for interactive sessions.

---

## Notable Bug Fixes

**Terminal freeze on long output.** A regression that caused Claude Code's terminal to freeze and stop accepting keystrokes when streaming responses containing very long lists, tables, paragraphs, or code blocks is fixed. If you've been seeing hangs on verbose tool output, this is the fix.

**AWS SSO credentials looping.** Every Bedrock API call was triggering a fresh SSO credential request — the credential provider chain wasn't caching properly. Fixed. Particularly impactful for users running Claude Code against Bedrock in long sessions with multiple tool calls.

**Non-interactive consent bug (security).** Running Claude Code in CI or non-interactive scripts was permanently recording remote managed settings consent without ever showing the consent dialog. A session run in unattended mode was recording the same consent that's meant to require a human to read and accept. Fixed.

**Remote Control status loss.** Remote Control sessions were losing their connected status on network interruptions. Fixed.

**Auto-updater clobbering custom launchers.** Every release was overwriting any custom script or symlink at `~/.local/bin/claude`. Fixed — the auto-updater now preserves non-default launchers.

---

## Builder Checklist Before Updating

Before running `npm update -g @anthropic-ai/claude-code`:

1. **Search your hooks**: `grep -r 'user_config' ~/.claude/ .claude/` — any hits in shell-format commands need migration to exec format or env vars
2. **Audit project settings.json**: If `.claude/settings.json` in any of your repos contains `pluginConfigs`, move those values to user settings
3. **Find repo-level autoMode**: `find . -name 'settings.local.json' -path '*/.claude/*' | xargs grep -l autoMode` — migrate any hits to `~/.claude/settings.json`
4. **Check Bedrock billing expectations**: Default model is now Opus 4.8 — review cost projections for automated Claude Code workloads
5. **CI env var cleanup**: Remove any `CLAUDE_CODE_ENABLE_AUTO_MODE=1` from CI configs where you're on Bedrock, Vertex, or Foundry — it's no longer needed (but won't break if left)

---

*Claude Code v2.1.207 was released July 10–11, 2026. Release notes: [GitHub](https://github.com/anthropics/claude-code/releases) · [Claude Code changelog](https://code.claude.com/docs/en/changelog).*
