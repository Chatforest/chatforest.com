---
title: "Claude Code v2.1.207: Three Breaking Changes Every Plugin and Hook Author Must Handle"
date: 2026-07-11
sources_audited: 2026-08-05
description: "Claude Code v2.1.207 lands today with security-driven breaking changes to hook notation, plugin config scoping, and auto mode settings location. If you distribute plugins or run hooks in CI, your setup will break on update. Here's the full migration map."
og_description: "v2.1.207 rejects ${user_config.*} in shell hooks, stops reading pluginConfigs from project settings.json, and moves autoMode out of repo settings.local.json. Three breaking changes, with migration steps for each."
content_type: "Builder's Log"
categories: ["Anthropic", "Claude Code", "Developer Tools", "Security"]
tags: ["claude-code", "anthropic", "breaking-changes", "plugin-hooks", "shell-injection", "bedrock", "vertex-ai", "mcp", "security", "auto-mode", "opus-4-8", "july-2026", "builders-log"]
---

Claude Code [v2.1.207 shipped today](https://github.com/anthropics/claude-code/releases/tag/v2.1.207) (July 11, 2026) and it is a security-heavy release: [24 changes](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md), most of them bug fixes and hardening, but three of those changes are **breaking** in ways that will silently fail if you don't migrate before updating. If you maintain a plugin, distribute hooks, or store per-project settings in `.claude/`, read this before running `npm update -g @anthropic-ai/claude-code`. Part of our **[Builder's Log](/builders-log/)**.

---

## The Three Breaking Changes

### 1. `${user_config.*}` notation is now rejected in shell hooks

If you use shell-format hook commands that interpolate plugin options via `${user_config.some_key}`, those commands will now fail with a rejection error. Anthropic's [v2.1.207 changelog entry](https://github.com/anthropics/claude-code/releases/tag/v2.1.207) lists this as a shell-injection fix for plugin hooks, monitors, and the MCP `headersHelper` — a malicious project or crafted config value could escape the substitution and execute arbitrary shell commands.

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

The exec-format approach is the cleaner permanent fix. Shell-format commands with `$VARIABLE` substitution are still allowed; only the `${user_config.*}` specific syntax is rejected. Every plugin option value is exported to the hook process as a `CLAUDE_PLUGIN_OPTION_<KEY>` environment variable (the option key, uppercased), so `api_key` becomes `CLAUDE_PLUGIN_OPTION_API_KEY` — this is [documented in the plugins reference](https://code.claude.com/docs/en/plugins-reference), not a fix-specific workaround.

---

### 2. `pluginConfigs` are no longer read from project-level `.claude/settings.json`

Previously, plugin option values could be set at any of four levels: user settings (`~/.claude/settings.json`), the `--settings` flag, managed settings (enterprise), or project-level `.claude/settings.json`. As of [v2.1.207](https://github.com/anthropics/claude-code/releases/tag/v2.1.207), the project-level source is dropped: "Plugin option values (`pluginConfigs`) are no longer read from project-level `.claude/settings.json`; only user, `--settings`, and managed settings are honored."

**What breaks:** Teams that checked plugin configuration into the repo under `.claude/settings.json` will find those values silently ignored after updating. The plugin will still load; it will just not receive the configured values, potentially falling back to defaults or failing unexpectedly.

**Why:** Repo-level plugin config means any project you open — including third-party repos or adversarially crafted repos — can inject plugin option values. Removing this source isolates plugin configuration to user-controlled and admin-controlled locations.

**Migration:** Move plugin configs from `.claude/settings.json` to `~/.claude/settings.json` (per-user) or supply them via `--settings <path>` in your CI invocation. If you need per-project variation, pass values through environment variables and read them inside the plugin script.

---

### 3. `autoMode` in `.claude/settings.local.json` inside repos is now ignored

Storing `autoMode: true` in a repo-level `.claude/settings.local.json` no longer has any effect — [the changelog](https://github.com/anthropics/claude-code/releases/tag/v2.1.207) records this as "auto mode to no longer read `autoMode` from `.claude/settings.local.json` (repo-resident); use `~/.claude/settings.json` instead." Auto mode must now be set in your user-level `~/.claude/settings.json` (or through managed/enterprise settings).

**What breaks:** Any repo where someone enabled auto mode by committing or generating a local settings file with `autoMode: true`. Those sessions will revert to interactive mode after update.

**Why:** Same threat model as above — a repo shouldn't be able to opt itself into auto mode. Auto mode allows Claude Code to bypass per-action permission prompts. The attack scenarios in this week's [Friendly Fire and HalluSquatting disclosures](/builders-log/friendly-fire-hallusquatting-ai-coding-agent-auto-mode-prompt-injection-hallucination-builder-security-guide/) both required auto mode to work without user interaction. Moving this setting to user scope means a repository cannot silently enable unattended execution.

**Migration:** If you legitimately run Claude Code in auto mode against repos — CI pipelines, overnight agents — move the `autoMode: true` to `~/.claude/settings.json` on the machine running it. Enterprise teams can push this through managed settings.

---

## New Features Worth Knowing

### The auto mode opt-in gate is removed on Bedrock, Vertex, and Microsoft Foundry

Previously, enterprise teams routing Claude Code through managed cloud infrastructure needed to set `CLAUDE_CODE_ENABLE_AUTO_MODE=1` to unlock auto mode. Starting [v2.1.207](https://github.com/anthropics/claude-code/releases/tag/v2.1.207), "auto mode is now available without `CLAUDE_CODE_ENABLE_AUTO_MODE` opt-in on Bedrock, Vertex AI, and Foundry; disable via `disableAutoMode` in settings" — that's [Microsoft Foundry](https://code.claude.com/docs/en/microsoft-foundry) (formerly Azure AI Foundry), not a separate "Azure Foundry" product. The opt-in gate is gone; auto mode itself is not turned on by default (see Breaking Change 3 above).

Note the relationship between this and Breaking Change 3: auto mode is now *available* on cloud platforms by default, but *enabling* it still requires explicit configuration in user/managed settings. The removal of the env var opt-in just unlocks the feature gate; it doesn't automatically enable unattended operation.

If you want to *disable* auto mode on cloud infrastructure (e.g., during sensitive runs), set `disableAutoMode: true` in your settings.

### Claude Opus 4.8 is now the default on Bedrock, Vertex, and Claude Platform on AWS

The [v2.1.207 changelog](https://github.com/anthropics/claude-code/releases/tag/v2.1.207) records this as "Changed Bedrock, Vertex, and Claude Platform on AWS to default to Claude Opus 4.8." If you pin model versions explicitly in your configuration, nothing changes. If you rely on the default, your sessions are now on a more capable model — but also a more expensive one. Worth checking your billing expectations if you run high-volume Claude Code automation on Bedrock or Vertex.

---

## Notable Bug Fixes

**Terminal freeze on long output.** A regression that caused Claude Code's terminal to freeze and stop accepting keystrokes when streaming responses containing very long lists, tables, paragraphs, or code blocks is [fixed](https://github.com/anthropics/claude-code/releases/tag/v2.1.207). If you've been seeing hangs on verbose tool output, this is the fix.

**AWS SSO credentials looping.** The [changelog](https://github.com/anthropics/claude-code/releases/tag/v2.1.207) lists a fix for "Bedrock repeatedly requesting fresh AWS SSO credentials from IAM Identity Center on every API request." Particularly impactful for users running Claude Code against Bedrock in long sessions with multiple tool calls.

**Non-interactive consent bug (security).** Running Claude Code non-interactively (`claude -p`, the SDK) was permanently recording remote managed settings consent without ever showing the consent dialog — the [changelog entry](https://github.com/anthropics/claude-code/releases/tag/v2.1.207) confirms this was "permanently recorded as consented without ever showing the security consent dialog." A session run in unattended mode was recording the same consent that's meant to require a human to read and accept. Fixed.

**Remote Control status loss.** Remote Control task status updates were being lost when a session's connection recovered from a network interruption or credential refresh, [per the changelog](https://github.com/anthropics/claude-code/releases/tag/v2.1.207). Fixed.

**Auto-updater clobbering custom launchers.** Every release was overwriting any custom script or symlink at `~/.local/bin/claude`. [Fixed](https://github.com/anthropics/claude-code/releases/tag/v2.1.207) — `/doctor` now reports an externally managed launcher instead of the updater silently replacing it.

---

## Builder Checklist Before Updating

Before running `npm update -g @anthropic-ai/claude-code`:

1. **Search your hooks**: `grep -r 'user_config' ~/.claude/ .claude/` — any hits in shell-format commands need migration to exec format or env vars
2. **Audit project settings.json**: If `.claude/settings.json` in any of your repos contains `pluginConfigs`, move those values to user settings
3. **Find repo-level autoMode**: `find . -name 'settings.local.json' -path '*/.claude/*' | xargs grep -l autoMode` — migrate any hits to `~/.claude/settings.json`
4. **Check Bedrock billing expectations**: Default model is now Opus 4.8 — review cost projections for automated Claude Code workloads
5. **CI env var cleanup**: Remove any `CLAUDE_CODE_ENABLE_AUTO_MODE=1` from CI configs where you're on Bedrock, Vertex, or Microsoft Foundry — it's no longer needed (but won't break if left)

---

*Claude Code v2.1.207 was released July 10–11, 2026. Release notes: [GitHub release tag](https://github.com/anthropics/claude-code/releases/tag/v2.1.207) · [full CHANGELOG.md](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) · [Claude Code changelog docs](https://code.claude.com/docs/en/changelog).*
