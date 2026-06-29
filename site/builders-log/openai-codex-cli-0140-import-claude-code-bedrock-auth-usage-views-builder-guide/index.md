# Codex CLI 0.140.0: Import from Claude Code, Managed Bedrock Auth, and Usage Views

> OpenAI's Codex CLI 0.140.0 ships four builder-facing changes: /import for migrating from Claude Code, managed Bedrock API-key auth with encrypted MCP OAuth storage, /usage token dashboards, and permanent session deletion.


Codex CLI version 0.140.0 shipped June 15, 2026, with 208 changes across 50 features and 46 improvements. Most are internal plumbing. Four are worth a builder's attention: cross-tool import from Claude Code, managed AWS Bedrock authentication, token usage views, and session deletion with safeguards.

This is an AI-researched guide based on published changelogs and documentation. ChatForest does not have hands-on access to these tools.

---

## The headline: `/import` reads your Claude Code setup

The most visible new capability is `/import`, a command that detects and migrates configuration from Claude Code into Codex-native formats.

What it reads:
- User-level setup (`~/.claude/`) — skills, hooks, MCP servers
- Project-level setup (`.claude.json`, `CLAUDE.md`) — instructions, agent definitions
- Session history — up to 30 days of recent chats

The import is selective, not automatic. When you run `/import`, Codex presents a lightweight preview showing what it found: MCP server names, hook event names, generated skill names. You choose what transfers. After migration, you get a markdown report with three statuses per artifact: **Added**, **Check before using**, or **Not Added**.

### What doesn't transfer

The import is deliberately conservative. Items that don't move:
- Conditional hook groups (Codex hooks don't support conditionals)
- Async and HTTP hooks (only synchronous command hooks transfer)
- Any configuration that's ambiguous rather than partially translated

The philosophy is explicit: partial translation that changes behavior is worse than no translation.

### Why this matters

Import tooling signals that OpenAI is competing directly for Claude Code's installed developer base. The effort to read CLAUDE.md specifically — a format Claude Code uses for project-level agent instructions — indicates how seriously OpenAI is treating switching friction as a barrier.

For builders, this is useful if you're evaluating both tools on the same project: you can set up your context once in Claude Code and then explore how the same project config feels in Codex, without manual duplication.

---

## Managed Bedrock API-key auth with encrypted OAuth storage

Previous Codex CLI versions required manual AWS credential setup for Bedrock. v0.140 adds managed authentication:

- Codex handles Bedrock API-key auth directly in the CLI flow, without requiring OPENAI_API_KEY
- CLI credentials and MCP OAuth tokens are now stored encrypted locally rather than in plaintext config files
- MCP OAuth: tokens acquired via `codex mcp login` now persist securely across sessions

This matters for teams with strict credential hygiene requirements. Unencrypted token storage in CLI tools has been a compliance friction point in enterprise environments — finance, healthcare, and regulated sectors in particular. Encrypted local storage doesn't eliminate all credential risk (the decryption key still lives on the machine), but it removes the immediate plaintext exposure that shows up in security scans.

### Bedrock channel for AWS-native stacks

If your production infrastructure runs on AWS and your team is already managing IAM roles and Bedrock access, this removes a manual step. The managed auth path means onboarding a new engineer to Codex CLI on a Bedrock deployment no longer requires walking them through separate AWS credential setup — the CLI guides the flow.

---

## `/usage` — token consumption dashboards

New in 0.140: `/usage` opens views for daily, weekly, and cumulative account token activity.

This is primarily a cost-tracking and budget-awareness feature. The application-server integration also exposes usage data — meaning apps built on Codex's app server can now surface token consumption to end users.

Builder uses:
- **Team cost allocation**: If multiple engineers share a Codex deployment, `/usage` gives rough visibility into who's consuming how much without leaving the tool
- **Model evaluation**: When comparing model backends (GPT-5.5, GPT-5.6, Bedrock models), `/usage` lets you see consumption deltas without switching to a billing console
- **Client billing**: Apps built on the app server can now plumb token data into client-facing usage dashboards

Note: these are account-level views, not per-project or per-repository. Project-level breakdown requires external tooling.

---

## Session deletion with safeguards

`codex delete`, `/delete`, and app-server `thread/delete` now offer permanent session removal — with confirmation prompts and subagent cleanup.

The safeguard matters: long-running Codex sessions can spawn subagents that hold state separately. Naive deletion of the parent session would orphan those subagents. The new deletion path includes subagent cleanup as part of the flow.

Practical cases where this matters:
- Sessions containing sensitive context (credentials, PII, internal project details) that shouldn't persist
- Cleaning up before handing off a machine or development environment
- Reducing clutter in teams where shared session lists accumulate over months

---

## The other changes worth noting

**`@` mentions unified**: Typing `@` now opens a unified menu for files, plugins, and skills. Previously, these were separate entry points. Reduces context-switching when composing a multi-resource prompt.

**`/app` handoff**: The CLI can now hand off the current session into Codex Desktop on macOS and Windows. If you started a session in the terminal and want the richer desktop UI, `/app` migrates the thread instead of requiring you to restart.

**Image paths in model context**: Local image attachments and generated images now expose their saved file paths back to the model. This makes follow-up edits work more reliably — the model knows where the file landed rather than inferring it.

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

