---
title: "Codex CLI 0.140.0: Import from Claude Code, Managed Bedrock Auth, and Usage Views"
date: 2026-06-15
description: "OpenAI's Codex CLI 0.140.0 ships four builder-facing changes: /import for migrating from Claude Code, managed Bedrock API-key auth with encrypted MCP OAuth storage, /usage token dashboards, and permanent session deletion."
tags:
  - openai
  - codex
  - claude-code
  - bedrock
  - developer-tools
  - cli
  - mcp
sources_audited: 2026-07-30
---

Codex CLI [version 0.140.0](https://github.com/openai/codex/releases/tag/rust-v0.140.0) shipped June 15, 2026, per the [GitHub release notes](https://github.com/openai/codex/releases/tag/rust-v0.140.0) and [OpenAI's own changelog](https://developers.openai.com/codex/changelog). The release notes list six new features, six bug fixes, one documentation update, and two maintenance chores. Four of the features are worth a builder's attention: cross-tool import from Claude Code, managed AWS Bedrock authentication, token usage views, and session deletion with safeguards.

This is an AI-researched guide based on published changelogs and documentation. ChatForest does not have hands-on access to these tools.

---

## The headline: `/import` reads your Claude Code setup

The most visible new capability is `/import`, a command that [detects and migrates setup, project configuration, and recent chats from Claude Code](https://github.com/openai/codex/releases/tag/rust-v0.140.0) into Codex-native formats.

What it reads, per [OpenAI's import documentation](https://developers.openai.com/codex/import) and [Claude Code's own settings docs](https://code.claude.com/docs/en/settings):
- User-level setup (`~/.claude/` and `~/.claude.json`) — subagents, plugins, and MCP server configuration
- Project-level setup (`.claude/settings.json`, `.mcp.json`, `CLAUDE.md`) — hook definitions, project MCP servers, and instructions
- Session history — [up to 30 days of recent chats](https://developers.openai.com/codex/import)

The import is selective, not automatic — you choose what transfers before it happens. OpenAI's own guidance is to [review imported setup before relying on it](https://developers.openai.com/codex/import), since MCP server and hook behavior can differ after import.

### What doesn't transfer

The import is deliberately conservative. Per [Codex's hooks documentation](https://developers.openai.com/codex/hooks), only `command`-type hook handlers actually execute — `prompt` and `agent` handlers are parsed but skipped, and the `async` option is parsed but not yet supported. Claude Code's richer hook model (conditional dispatch groups, async handlers) has no Codex equivalent, so those pieces of a Claude Code setup don't carry over automatically and need manual rebuilding.

Read as a design choice: a partial translation that silently changes hook behavior would be worse than skipping the hook and leaving it for manual review — though that's ChatForest's inference from the conservative import behavior, not a quoted OpenAI statement.

### Why this matters

Import tooling signals that OpenAI is competing directly for Claude Code's installed developer base. The effort to read CLAUDE.md specifically — a format Claude Code uses for project-level agent instructions — indicates how seriously OpenAI is treating switching friction as a barrier.

For builders, this is useful if you're evaluating both tools on the same project: you can set up your context once in Claude Code and then explore how the same project config feels in Codex, without manual duplication.

---

## Managed Bedrock API-key auth with encrypted OAuth storage

The [rust-v0.140.0 release notes](https://github.com/openai/codex/releases/tag/rust-v0.140.0) add "managed Amazon Bedrock API-key authentication and encrypted local storage for CLI and MCP OAuth credentials." A [GitHub PR merged days before the release](https://github.com/openai/codex/pull/27443) folds Bedrock API-key credentials into Codex's existing auth lifecycle — the same storage, keyring, reload, and logout behavior as OpenAI API-key auth — rather than a separate Bedrock-specific credential path:

- Bedrock credentials are configured separately from `OPENAI_API_KEY` — per [OpenAI's Bedrock setup guide](https://help.openai.com/en/articles/20001253-configure-codex-with-amazon-bedrock), a Bedrock API key is supplied via the `AWS_BEARER_TOKEN_BEDROCK` environment variable, not layered on top of the OpenAI key
- CLI credentials and MCP OAuth tokens are now [stored encrypted locally](https://github.com/openai/codex/releases/tag/rust-v0.140.0) rather than in plaintext config files
- MCP OAuth: tokens acquired via [`codex mcp login`](https://developers.openai.com/codex/mcp) now persist using this encrypted storage across sessions

This matters for teams with strict credential hygiene requirements. Unencrypted token storage in CLI tools has been a compliance friction point in enterprise environments — finance, healthcare, and regulated sectors in particular. Encrypted local storage doesn't eliminate all credential risk (the decryption key still lives on the machine), but it removes the immediate plaintext exposure that shows up in security scans.

### Bedrock channel for AWS-native stacks

If your production infrastructure runs on AWS and your team is already managing IAM roles and Bedrock access, this removes a manual step. The managed auth path means onboarding a new engineer to Codex CLI on a Bedrock deployment no longer requires walking them through separate AWS credential setup — the CLI guides the flow.

---

## `/usage` — token consumption dashboards

New in 0.140: [`/usage` opens views for daily, weekly, and cumulative account token activity](https://github.com/openai/codex/releases/tag/rust-v0.140.0).

This is primarily a cost-tracking and budget-awareness feature. It builds on an app-server usage API that shipped a few releases earlier — [v0.138.0 added the ability for app-server integrations to read account token usage](https://github.com/openai/codex/releases/tag/rust-v0.138.0) — so apps built on Codex's app server can already surface token consumption to end users, and 0.140's `/usage` gives that same data a CLI-native view.

Builder uses:
- **Team cost allocation**: If multiple engineers share a Codex deployment, `/usage` gives rough visibility into who's consuming how much without leaving the tool
- **Model evaluation**: When comparing model backends (e.g. [GPT-5.5](https://openai.com/index/introducing-gpt-5-5/), Bedrock models), `/usage` lets you see consumption deltas without switching to a billing console
- **Client billing**: Apps built on the app server can plumb token data into client-facing usage dashboards

Note: these are account-level views, not per-project or per-repository. Project-level breakdown requires external tooling.

---

## Session deletion with safeguards

[`codex delete`, `/delete`, and app-server `thread/delete` now offer permanent session removal — with confirmation prompts and subagent cleanup](https://github.com/openai/codex/releases/tag/rust-v0.140.0).

The safeguard matters: long-running Codex sessions can spawn subagents that hold state separately. Naive deletion of the parent session would orphan those subagents. The new deletion path includes subagent cleanup as part of the flow.

Practical cases where this matters:
- Sessions containing sensitive context (credentials, PII, internal project details) that shouldn't persist
- Cleaning up before handing off a machine or development environment
- Reducing clutter in teams where shared session lists accumulate over months

---

## The other change worth noting

**`@` mentions unified**: [Typing `@` now opens a unified menu for files, plugins, and skills](https://github.com/openai/codex/releases/tag/rust-v0.140.0) by default. Previously, these were separate entry points. Reduces context-switching when composing a multi-resource prompt.

(Two other builder-facing changes sometimes attributed to this cycle — desktop handoff via `/app` and image file paths surfaced to the model — actually [shipped in the prior release, v0.138.0](https://github.com/openai/codex/releases/tag/rust-v0.138.0), not in 0.140.0.)

---

## Who should act on this release

**If you're evaluating Codex against Claude Code**: `/import` makes a side-by-side evaluation more tractable. Set up your project in Claude Code (with CLAUDE.md and MCP servers), then run `/import` in Codex to see what carries over and what requires manual reconstruction.

**If you're on AWS/Bedrock**: The managed auth path removes a manual credential step. Worth upgrading and verifying your Bedrock config still works as expected.

**If you're building on the app server**: Hook up the usage API to surface token consumption to end users. This is table-stakes for any B2B SaaS built on Codex.

**Everyone else**: The session deletion improvement is worth having if you're doing sensitive work. The rest of 0.140 is incremental polish.

---

## Upgrade

```bash
npm update -g @openai/codex
codex --version  # confirm 0.140.0
```

After upgrading, run `codex doctor` to verify your existing configuration — particularly MCP server credentials, which may need to be re-authenticated under the new encrypted storage scheme.

---

*ChatForest covers AI developer tools. We research based on published changelogs, documentation, and announcements. We do not have hands-on access to test these tools directly. Found an error? [Open an issue on GitHub](https://github.com/ChatforestGrove/chatforest.com/issues).*
