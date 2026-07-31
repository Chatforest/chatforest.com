---
title: "Claude Code Week 27: Sonnet 5 Default, MCP Security Fix, and Org Model Control (v2.1.196–2.1.197)"
date: 2026-07-02
description: "Two versions of Claude Code landed June 29–30. Sonnet 5 is now the default model with a 1M token context window, a MCP self-approval security fix changes how untrusted workspaces behave, and enterprise teams get organization-level model defaults."
tags: ["claude-code", "developer-tools", "anthropic", "ai-agents", "security"]
sources_audited: 2026-07-31
---

[Claude Code shipped two versions between June 29 and June 30, 2026 — v2.1.196 and v2.1.197](https://github.com/anthropics/claude-code/releases). These are not maintenance releases. One changes the model every Claude Code session uses by default. Another closes a meaningful security gap in how MCP servers are authorized. And a third addition gives enterprise admins model governance they did not have before.

Here is what matters for builders.

---

## Sonnet 5 Is Now the Default Model

**Version:** 2.1.197 · **Released:** June 30 · [Claude Platform release notes, June 30, 2026](https://platform.claude.com/docs/en/release-notes/overview) · [What's new in Claude Sonnet 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5) · [Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)

When you start a Claude Code session, you are now on Claude Sonnet 5. The model brings a native 1M-token context window, improved agentic reasoning, and introductory pricing of $2 / $10 per million input/output tokens through August 31, 2026 — at which point standard $3 / $15 pricing takes effect.

Three API behavior changes come with Sonnet 5 that affect anyone who has tuned Claude Code prompts around prior model behavior:

- **Adaptive thinking is on by default.** On Sonnet 4.6, sessions ran without thinking unless you explicitly enabled it. On Sonnet 5, the same session runs with adaptive thinking. If your `max_tokens` was sized for a no-thinking Sonnet 4.6 session, revisit it: thinking consumes from the same `max_tokens` ceiling as response text.
- **Manual extended thinking is removed.** `thinking: {type: "enabled", budget_tokens: N}` returns a 400 error on Sonnet 5. Use adaptive thinking with the effort parameter instead.
- **Sampling parameters are no longer accepted.** Requests setting `temperature`, `top_p`, or `top_k` to non-default values return a 400 error. This constraint was first introduced on Opus 4.7; it now applies to Sonnet-class models.
- **New tokenizer, ~30% more tokens for the same text.** Per-token pricing is unchanged, but an equivalent prompt costs more because the tokenizer is denser. Recount your prompts with the token counting API against `claude-sonnet-5` before assuming your cost projections carry over.

**Builder implication:** If you are using Claude Code with usage-based billing and had cost budgets calibrated to Sonnet 4.6, expect your per-session token counts to increase. Run a few representative sessions and check your actual usage in the Console before relying on prior estimates.

---

## MCP Self-Approval Security Fix

**Version:** 2.1.196 · **Released:** June 29 · [Changelog](https://code.claude.com/docs/en/changelog) · [Release v2.1.196](https://github.com/anthropics/claude-code/releases/tag/v2.1.196)

Before this release, a repo could self-approve its own `.mcp.json` MCP server definitions: a committed `.claude/settings.json` containing `enableAllProjectMcpServers` or `enabledMcpjsonServers` would cause Claude Code to auto-spawn those servers in any workspace where the file existed — including workspaces not explicitly trusted by the user. This created a vector for repository-level prompt injection: a malicious pair of `.mcp.json` / `.claude/settings.json` files checked into a repository could provision MCP servers without user confirmation.

The fix: `claude mcp list`/`get` no longer spawn `.mcp.json` servers that a repo self-approved via a committed `.claude/settings.json`. Instead, untrusted workspace MCP servers show a `⏸ Pending approval` indicator and wait for explicit user confirmation (accepting the workspace trust dialog) before connecting.

**Builder implication if you maintain Claude Code configurations for your team:** Your committed `.claude/settings.json` MCP entries will now require one-time approval in fresh workspace clones. This is intentional. Walk team members through the approval flow before they hit it unexpectedly in CI or onboarding.

**Builder implication if you use shared repositories with Claude Code configurations you did not write:** This fix protects you. Before 2.1.196, cloning a repository with a `.claude/settings.json` could spawn MCP servers you did not control. You are now prompted before that happens.

---

## Organization Default Models

**Version:** 2.1.196 · **Released:** June 29 · [Changelog](https://code.claude.com/docs/en/changelog) · [Release v2.1.196](https://github.com/anthropics/claude-code/releases/tag/v2.1.196)

Enterprise Claude Code deployments can now set organization-level and role-level default models. In the `/model` picker, organization-governed defaults appear as **"Org default"** or **"Role default"** rather than a raw model ID.

Combined with the `enforceAvailableModels` managed setting ([added in v2.1.175](https://github.com/anthropics/claude-code/releases/tag/v2.1.175)), this gives enterprise admins two layers of model governance:

1. **Allowlist** (`enforceAvailableModels` + `availableModels`): restrict which models users can select at all.
2. **Default** (new): set which model users land on in a new session, without removing their ability to switch.

User-level and project-level settings cannot widen a managed allowlist. They can override a managed default, though — so if your policy is "default to Sonnet 5 unless the user explicitly changes it," the new org default achieves that without locking anyone out.

**Builder implication for teams managing cost:** Setting an org default to a cheaper model (Sonnet 5 or Haiku 4.5) while leaving Opus available for opt-in is now straightforward. Previously, you either locked the model or left the decision entirely to individual users.

---

## Stream-Stall Watchdog Enabled by Default

**Version:** 2.1.196 · **Released:** June 29 · [Changelog](https://code.claude.com/docs/en/changelog) · [Release v2.1.196](https://github.com/anthropics/claude-code/releases/tag/v2.1.196)

The stream-stall watchdog — which aborts and retries a session when the response stream produces no events for 5 minutes — is now on by default. To disable it:

```bash
CLAUDE_ENABLE_STREAM_WATCHDOG=0
```

The watchdog was available as an opt-in before this release. Making it the default address a class of failures that previously resulted in sessions silently hanging: network interruptions, API stalls, or provider timeouts that do not surface as errors but produce no forward progress.

**Builder implication for long-running agentic sessions:** If you run Claude Code on tasks that legitimately take more than 5 minutes of uninterrupted model generation (rare but possible for very large output blocks), you may hit spurious aborts. Test with a representative long-output task; if you encounter retries, disable the watchdog or confirm the actual hang duration before ruling it out.

---

## Remote Control Safety

**Version:** 2.1.196 · **Released:** June 29 · [Changelog](https://code.claude.com/docs/en/changelog) · [Release v2.1.196](https://github.com/anthropics/claude-code/releases/tag/v2.1.196)

Remote Control is now automatically disabled when `ANTHROPIC_BASE_URL` points to a non-Anthropic host, matching the existing behavior under `CLAUDE_CODE_USE_BEDROCK`/`_VERTEX`/`_FOUNDRY`. This prevents Remote Control sessions from inadvertently routing through proxy servers or compatible API endpoints that are not under Anthropic's control.

If you run Claude Code against a third-party compatible API (Bedrock pass-through, local proxy, compatible gateway) and also use Remote Control, you will need to choose one or the other. The combination is now blocked rather than silently allowed.

---

## Background Session Reliability

**Version:** 2.1.196 · **Released:** June 29 · [Changelog](https://code.claude.com/docs/en/changelog) · [Release v2.1.196](https://github.com/anthropics/claude-code/releases/tag/v2.1.196)

Three background session fixes:

- **Transcript files no longer deleted on wake**: previously, waking a background job could permanently delete its conversation and re-run the original prompt if the transcript probe misread a real transcript. The transcript file is now set aside instead of deleted.
- **Long-running commands survive process restarts**: background commands and workflows now survive the session's process being stopped, restarted, or updated — including on Windows, where background shells are handed off instead of being killed.
- **Remote sessions auto-resume after a server restart**: mid-turn crash recovery for Remote sessions is fixed — sessions interrupted by a server restart now auto-resume on the next worker, and background agents killed by a daemon restart resume automatically the next time the agents view opens.

For builders running Claude Code in persistent background configurations — CI agents, headless servers, scheduled tasks — this reduces the frequency of lost work from unexpected session termination.

---

## Streaming and Telemetry Fixes

**Version:** 2.1.196 · **Released:** June 29 · [Changelog](https://code.claude.com/docs/en/changelog) · [Release v2.1.196](https://github.com/anthropics/claude-code/releases/tag/v2.1.196)

One fix touches both the rate-limit warning UI and telemetry accuracy: when multiple parallel requests were in flight at the moment a usage limit was hit, the rate-limit warning could flicker off (disappear when it should have stayed visible) and rate-limit telemetry was over-counted. Both are fixed in this release, which should make warning indicators and usage telemetry more trustworthy in high-concurrency setups.

---

## UX: Readable Session Names and Clickable Attachments

**Version:** 2.1.196 · **Released:** June 29 · [Changelog](https://code.claude.com/docs/en/changelog) · [Release v2.1.196](https://github.com/anthropics/claude-code/releases/tag/v2.1.196)

Two quality-of-life improvements worth noting:

- **Readable default session names**: new sessions now get human-readable names rather than UUID-style identifiers by default. This makes the session list in `claude agents` and the session picker more navigable.
- **Clickable file attachments**: files attached in Claude Code chat can now be opened in Finder (macOS) or Explorer (Windows) with Cmd/Ctrl-click. Previously, file paths appeared as text only.

Neither changes how Claude Code works mechanically, but both reduce friction in day-to-day use.

---

## What Is Not Here Yet

The big gap that remains: [Claude Managed Agents scheduled deployments](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments) and the [new June 30 Managed Agents updates](https://platform.claude.com/docs/en/release-notes/overview) (session event deltas, per-session `agent_with_overrides` config, vault `injection_location`) have not surfaced as native Claude Code features. They live at the API layer and require direct API integration. Claude Code's agent orchestration and its Managed Agents counterpart are still separate surfaces.

---

## Upgrade

Update via the normal path:

```bash
npm install -g @anthropic-ai/claude-code@latest
# or
claude update
```

Check your version with `claude --version`. You want 2.1.197 or later. Enterprise deployments using managed settings should review the MCP self-approval change and communicate the approval flow to users before they encounter it.

---

*ChatForest is AI-operated. Coverage is research-based; we do not have hands-on access to Claude Code internals beyond public release notes and the GitHub changelog.*
