---
title: "Windsurf Is Now Devin Desktop: Devin Local, ACP, and What the Rebrand Actually Changes"
date: 2026-06-04
description: "On June 2, 2026, Cognition retired the Windsurf brand and relaunched as Devin Desktop — with Devin Local (a Rust-rewritten Cascade successor), Agent Client Protocol support, and a new IDE-as-agent-manager default. Here's what changed, what happened to the Cascade removal deadline, and what ACP means for your stack."
og_description: "Windsurf becomes Devin Desktop June 2, 2026. Devin Local replaces Cascade as default (30% more token efficient, subagents, Rust rewrite) — Cascade's announced July 1 removal doesn't appear to have happened. ACP launches: open agent-editor standard adopted by JetBrains, Google, GitHub, and dozens of other agents. Plans/pricing unchanged. Builder guide inside."
content_type: "Builder's Log"
categories: ["Developer Tools", "Agentic AI", "Industry Analysis"]
tags: ["windsurf", "devin", "cognition", "devin-desktop", "devin-local", "cascade", "acp", "agent-client-protocol", "ide", "coding-agent", "mcp", "cursor", "agentic-coding", "builders-log"]
sources_audited: 2026-08-24
---

On June 2, 2026, Cognition [shipped a standard over-the-air update to Windsurf](https://devin.ai/blog/windsurf-is-now-devin-desktop/). When users restarted their editor, it opened as Devin Desktop.

The name change is the obvious part of the story. The less obvious parts — a new local agent rewritten in Rust, an old agent Cognition said would hit a hard July 1 deadline (it apparently didn't — see below), and an open protocol for connecting any AI coding agent to any compatible editor — are what matter for builders.

Here's what actually changed.

---

## What Is Devin Desktop

Devin Desktop is the new name for the product formerly called Windsurf. Cognition's repositioning is direct: Windsurf was an editor with AI bolted on. Devin Desktop is an agent manager wrapped in a full IDE.

The distinction is about the default surface. In [Windsurf 2.0](https://devin.ai/blog/windsurf-2-0/) (launched April 15, 2026), the Agent Command Center — a Kanban view showing every local and cloud agent session — was a panel you could open. In Devin Desktop, it is the primary interface. The editor is still there; you access it the same way. But when you open the product, you are looking at agent sessions first, code second.

For most existing Windsurf users, the day-to-day experience looks nearly identical. The rebrand does not change:
- Plans or pricing
- Extension compatibility
- Keybindings or editor settings
- MCP connections or workflow files
- Local language tooling (LSPs, formatters, debuggers)

The update arrived as a standard OTA push. No migration to run, no settings to re-enter.

---

## Devin Local: The Cascade Replacement

The most actionable change in the June 2 update is the replacement of **Cascade** with **Devin Local**.

Cascade was Windsurf's original agentic layer — the local AI that handled multi-file edits, code search, and terminal commands inside the editor. Devin Local is its replacement. [Cognition describes it](https://devin.ai/blog/windsurf-is-now-devin-desktop/) as a complete rewrite, not an evolution:

| | Cascade | Devin Local |
|---|---|---|
| Language | Python | Rust |
| Token efficiency | Baseline | ~30% more efficient |
| Subagents | No | Yes |
| Architecture | Cascade-specific | Same as Devin CLI |
| Status after June 2 | Available, no longer default | Default |
| Availability until | Originally announced as July 1, 2026 | Ongoing |

Cognition originally said Cascade would remain accessible only through **July 1, 2026**, after which it would be removed.

**Correction (2026-08-24):** that removal does not appear to have happened on schedule. Cognition's own [Devin Desktop changelog](https://docs.devin.ai/desktop/changelog) shows Cascade still referenced in dated release notes well past the July 1 deadline — a July 29, 2026 entry (v3.6.21) describes Cascade's model picker and panel menu, an August 10, 2026 entry (v3.7.16) describes hiding "Cascade-specific configuration" when it's disabled for a team, and an August 21, 2026 entry (v3.8.20) still references behavior "when Cascade is disabled" — language that implies Cascade is an optional, per-team toggle rather than a fully removed agent. We found no official Cognition statement confirming a changed plan. If you have workflows, scripts, or automations that explicitly call Cascade behaviors, migrating to Devin Local is still the safe move — but do not assume Cascade has been hard-removed from your instance; verify its status directly in your own Devin Desktop settings.

The 30% token efficiency improvement is the number most worth examining. For builders running high-volume agent sessions — long refactors, large codebase navigation, multi-step test generation — the reduction in token consumption translates directly to lower costs and faster sessions. At scale, that matters.

The subagent support is the architectural shift. Cascade operated as a single agent: one context window, one turn at a time. Devin Local can spawn subagents — specialized sub-sessions that handle specific parts of a task in parallel before reporting back. The pattern maps to the coordinator/managed-agent architecture that [Cognition shipped for Devin's cloud product on March 19, 2026](https://cognition.com/blog/devin-can-now-manage-devins), where a primary Devin session scopes work and assigns pieces to managed Devins running in isolated VMs.

---

## Agent Client Protocol (ACP)

Devin Desktop shipped with support for the **Agent Client Protocol (ACP)**, an open-source protocol for connecting AI coding agents to code editors. [ACP was created by Zed Industries](https://zed.dev/blog/bring-your-own-agent-to-zed) in August 2025, launching alongside Google's Gemini CLI as the first external integration. [JetBrains announced in October 2025](https://blog.jetbrains.com/ai/2025/10/jetbrains-zed-open-interoperability-for-ai-coding-agents-in-your-ide/) that it would co-develop ACP with Zed and bring native support to JetBrains IDEs. [GitHub added ACP support to Copilot CLI](https://github.blog/changelog/2026-01-28-acp-support-in-copilot-cli-is-now-in-public-preview/) in January 2026. [ACP's public directory](https://zed.dev/acp) lists JetBrains, Google (Gemini CLI), and GitHub (Copilot CLI) among its confirmed adopters; Zed does not publish an official running adopter count, but as of this audit (2026-08-24) the directory lists 47 total agent implementations.

Devin Desktop joining the ACP ecosystem is the largest single adoption event in ACP's short history, given Windsurf's install base.

### What ACP Does

ACP is often described as the **LSP for AI coding agents** — a reference to the Language Server Protocol, which standardized how editors communicate with language servers, making every language toolchain work in every editor. ACP attempts the same standardization for agent-editor interaction.

Technically: [ACP is JSON-RPC 2.0 over stdin/stdout](https://agentclientprotocol.com/protocol/overview). The editor launches the agent as a subprocess. Protocol messages flow back and forth. [The session bootstraps via a `session/new` handshake](https://agentclientprotocol.com/protocol/v1/session-setup) that can also declare which MCP servers the agent should connect to.

The result: **any ACP-compatible agent can run inside any ACP-compatible editor**, with the same interface as the editor's native agent.

At launch, [Devin Desktop's ACP support includes](https://devin.ai/blog/windsurf-is-now-devin-desktop/):
- **Codex** (OpenAI)
- **Claude Agent** (Anthropic)
- **OpenCode** (open-source)
- Any team-built agent that implements ACP

Third-party agents appear in the Kanban view alongside Devin, share the Spaces context layer, and operate with the same controls as native sessions. From the user's perspective, the agent origin — Devin, Codex, Claude, or something you built — is secondary to what it's doing.

### ACP vs MCP

These protocols are often confused because both involve AI agents. They solve different problems at different layers:

| | ACP | MCP |
|---|---|---|
| What it connects | Agents to editors | Agents to tools and data |
| Created by | [Zed Industries (Aug 2025)](https://zed.dev/blog/bring-your-own-agent-to-zed) | [Anthropic (Nov 2024)](https://www.anthropic.com/news/model-context-protocol) |
| Transport | JSON-RPC 2.0 over stdio | JSON-RPC 2.0 over stdio or HTTP |
| Adopted by | Zed, JetBrains, Google, GitHub, Devin Desktop | Most major AI providers and tool vendors |
| Analogy | LSP (Language Server Protocol) | API gateway for agent tools |

They are designed to work together. When ACP bootstraps a session, it can declare the MCP servers the agent should connect to. ACP and MCP wire up in a single handshake — the editor sets the context, MCP sets the tools.

If you're building agents: ACP is how your agent speaks to the editor. MCP is how your agent speaks to the tools.

---

## Spaces

[Spaces is Devin Desktop's new context layer](https://devin.ai/blog/windsurf-is-now-devin-desktop/), introduced alongside the June 2 rebrand. A Space groups related agent sessions, PRs, files, and context objects together, giving multi-agent workflows shared state without requiring each agent to rebuild context from scratch.

This is most useful for longer-running, multi-agent projects: a Space for a feature branch holds the relevant files, the current PR, the test results, and any agent sessions working on that branch — accessible to every agent assigned to the Space.

Spaces is an early feature; the initial release is intentionally simple. Expect it to evolve through Q3 2026.

---

## What This Means for Different Builders

**If you are a current Windsurf user:**
- You already have Devin Desktop — check for the update if it hasn't appeared.
- Switch from Cascade to Devin Local when convenient. The efficiency gains are real and the transition is low friction — and while Cognition originally set a July 1, 2026 hard deadline for this, that removal doesn't appear to have actually happened (see the correction above), so there's no confirmed cutoff forcing the move.
- Your plans, pricing, extensions, and MCP connections carry over unchanged.

**If you are evaluating AI coding tools:**
- Devin Desktop is now the clearest agent-first choice in the IDE category: it assumes you want to manage multiple agents (local and cloud) from a single interface and treats code editing as one capability among several, not the primary surface.
- Cursor remains the strongest IDE-first choice: the editor experience is the primary surface, and AI — including [parallel agents via git worktrees, introduced in Cursor 2.0](https://cursor.com/changelog/2-0) — is layered on top.
- These are different philosophies, not just feature differences. Neither is universally better; the right choice depends on how your team actually works.

**If you are building your own agents:**
- ACP adoption is accelerating. JetBrains, Google, GitHub, and now Devin Desktop all support it. If you're building an agent that developers will run inside their editors, implementing ACP gives you access to that entire ecosystem with one protocol.
- The ACP + MCP combination handles both layers: ACP for editor integration, MCP for tool access. Both use JSON-RPC 2.0 over stdio. The implementation patterns are similar.

---

## The Broader Signal

The Windsurf → Devin Desktop rebrand is the most visible signal yet of a structural shift in how the industry thinks about AI developer tools.

The original framing — AI as code completion, then AI as chat, then AI as code editor assistant — positioned the human developer as the actor and the AI as an accelerator. Every interaction was human-initiated. The developer decided what to do; the AI helped them do it faster.

The emerging framing — IDE as agent manager — positions the AI as an actor and the developer as the goal-setter and reviewer. You open the product to see what the agents are doing, not to write the next line. The code editor is still there, because you still need to read code, review diffs, and handle tasks agents can't manage. But it's no longer the primary surface.

Devin Desktop ships that framing as a product. If you use Windsurf, you experienced this shift as a software update on June 2.

---

*The Windsurf → Devin Desktop rebrand shipped June 2, 2026 as an over-the-air update. Cascade is no longer the default agent, but as of this audit (2026-08-24) Cognition's own changelog shows it still available and per-team toggleable, not hard-removed as originally announced for July 1, 2026 — see the correction above. ACP was created by Zed Industries in August 2025 and its public directory lists JetBrains, Google, GitHub, and Devin Desktop among confirmed adopters, alongside 47 total agent implementations as of this audit. Plans and pricing for existing Windsurf users are unchanged.*
