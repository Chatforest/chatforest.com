---
title: "apify/mcpc — A Universal MCP Client Built for AI Code Agents"
date: 2026-05-05T22:30:00+09:00
description: "apify/mcpc reviewed: a lightweight TypeScript CLI client for MCP servers with persistent named sessions, OAuth 2.1, credential sandboxing, progressive tool discovery, and JSON output for AI code agents. Apache-2.0. Rating: 3.5/5."
og_description: "apify/mcpc (538 stars, v0.2.6, Apache-2.0): a universal MCP CLI client designed for AI agents in code mode. Persistent sessions, OAuth 2.1, OS keychain credential sandboxing, full MCP spec support (resources, prompts, async tasks), JSON output, grep across sessions. By Apify. Rating: 3.5/5."
content_type: "Review"
card_description: "apify/mcpc (538 stars, v0.2.6, Apache-2.0, TypeScript) is a universal command-line client for MCP servers designed specifically for AI agents operating in code mode. Instead of embedding an LLM, mcpc acts as infrastructure: a thin, shell-composable adapter that exposes MCP servers to any AI coding agent (Claude Code, Cursor, Codex) through standard shell commands. **Persistent named sessions** — prefixed with `@` — survive shell restarts via a lightweight bridge process. **OAuth 2.1 with PKCE** handles authentication, with credentials stored in the OS keychain (Linux Secret Service / macOS Keychain / Windows Credential Manager). An **AI sandbox proxy** lets users authenticate once and expose a local proxy endpoint, so AI-generated code can call MCP tools without ever seeing raw API tokens. **Progressive tool discovery** defers schema loading until a tool is actually needed, cutting token waste in multi-server setups. **JSON output mode** (`--json`) integrates with `jq` and shell pipelines. Full MCP spec support: tools, resources, prompts, async tasks, notifications, pagination, health checks. Experimental **x402 payment support** (USDC on Base blockchain) for Apify Actor runs. Built by Jan Curn, CEO and co-founder of Apify, the web scraping and automation platform (YC 2015, 27,000+ pre-built Actors). Not a replacement for LLM-orchestrating clients like IBM/mcp-cli — mcpc has no LLM integration by design. Part of our **Developer Tools** category. Rating: 3.5/5."
last_refreshed: 2026-05-05
---

Most MCP clients are built around a user experience: you type a prompt, a language model reasons about it, tools get called, and a response arrives in a chat interface. That model works well for humans. It works less well for AI agents operating in code mode — agents that generate shell commands, run them, inspect the output, and iterate. For those workflows, embedding a full LLM chat client inside a larger AI-orchestrated system creates redundancy and friction.

[apify/mcpc](https://github.com/apify/mcpc) takes a different approach. It is not a chat client. It is not an LLM orchestrator. It is a universal command-line adapter for the Model Context Protocol — designed to be called by AI agents, composed into shell pipelines, and integrated into code-mode workflows. The LLM stays in Claude Code, Cursor, or Codex. mcpc handles the MCP layer.

Built by Jan Curn, co-founder and CEO of [Apify](https://apify.com), the project grew from a practical need: Apify runs a hosted MCP server at mcp.apify.com that exposes their 27,000+ web-scraping Actors to AI agents, and they needed a good CLI client to connect to it. Finding none that met their requirements, they built one and open-sourced it. Part of our **[Developer Tools MCP category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Repo** | [apify/mcpc](https://github.com/apify/mcpc) |
| **Stars** | ~538 |
| **Forks** | 47 |
| **License** | Apache-2.0 |
| **Language** | TypeScript (Node.js) |
| **Install** | `npm install -g @apify/mcpc` |
| **npm** | [@apify/mcpc](https://www.npmjs.com/package/@apify/mcpc) |
| **Latest version** | v0.2.6 (April 15, 2026) |
| **Requires** | Node.js ≥ 20.0.0 |
| **First release** | December 2025 |
| **Primary author** | Jan Curn ([@jancurn](https://github.com/jancurn)), Apify |

---

## What mcpc Does

mcpc is a command-line client for MCP servers that maps MCP operations to shell commands. Connect to a server, create a named session, and then call any of the server's tools, resources, or prompts from the command line — with output formatted for human reading or machine parsing.

The design centers on three problems:

**Configuration fragmentation.** A developer using Claude Code, Cursor, and Codex must configure the same MCP servers three times in three different tools. mcpc centralizes that configuration and exposes a single session model any of them can use via shell commands.

**Token waste.** Connecting to multiple MCP servers means loading all their tool schemas upfront. With five or ten MCP servers connected, this can consume tens of thousands of tokens before any real work begins. mcpc enables progressive tool discovery — agents list tools minimally, then fetch specific schemas only when needed.

**Credential exposure.** Traditional MCP setups give AI-generated code direct access to API tokens. mcpc's proxy model changes this: the user authenticates once and mcpc exposes a local endpoint. AI agents call the proxy; they never see the underlying credentials.

---

## Persistent Named Sessions

The central concept in mcpc is the **named session**, prefixed with `@`. Sessions are named connections to MCP servers, maintained by a lightweight bridge process running in the background. They survive shell restarts and can be left open across work sessions.

```bash
# Connect to Apify's MCP server (OAuth login)
mcpc login mcp.apify.com

# Create a persistent named session
mcpc connect mcp.apify.com @apify

# Or connect via a config file (e.g., .vscode/mcp.json)
mcpc connect ./.vscode/mcp.json:filesystem @fs

# Sessions persist across shells
mcpc @apify tools-list
mcpc @fs tools-list
```

`mcpc @session tools-list` — list available tools. `mcpc @session tools-call <tool-name> key:=value` — invoke a tool. Arguments use auto-parsing: values that are valid JSON are parsed as JSON; everything else is a string.

```bash
# Call a tool with arguments
mcpc @apify tools-call search-actors keywords:="website crawler"

# JSON output for scripting
mcpc --json @apify tools-list | jq '.tools[].name'

# Interactive shell for exploration
mcpc @apify shell

# Search across all connected sessions
mcpc grep "actor"

# Manage sessions
mcpc @apify close
mcpc clean   # remove stale sessions
```

---

## Full MCP Spec Support

mcpc supports the full MCP specification, not a subset. This is a meaningful distinction: many lighter clients support only the tool-call workflow. mcpc also handles:

| MCP feature | Command |
|---|---|
| Tools | `tools-list`, `tools-call` |
| Resources | `resources-list`, `resources-read`, `resources-subscribe` |
| Prompts | `prompts-list`, `prompts-get` |
| Async tasks | `tasks-list`, `tasks-get`, `tasks-result`, `tasks-cancel` |
| Notifications | Session-level, surfaced during shell mode |
| Pagination | Automatic, transparent |
| Health check | `mcpc @session ping` |
| Server instructions | Displayed on session connect |
| Logging level | Configurable per session |

Support for async task lifecycle management (list, get result, cancel) is notable — many MCP servers for data-intensive operations (web scraping, batch processing, long-running agents) return async results rather than synchronous responses.

---

## OAuth 2.1 and Credential Sandboxing

mcpc implements OAuth 2.1 with PKCE, including three registration mechanisms: pre-registration (static client IDs), Client ID Metadata Documents (CIMD), and Dynamic Client Registration (DCR). Credentials are stored in the OS keychain — Linux Secret Service API, macOS Keychain, Windows Credential Manager — with automatic fallback to `~/.mcpc/credentials` (mode 0600) on headless systems.

The **AI sandbox proxy** is the credential security model. After logging in:

1. `mcpc proxy @apify` starts a local proxy endpoint
2. AI agents invoke MCP tools against the proxy URL
3. mcpc forwards calls to the real MCP server, handling auth transparently
4. AI-generated code never sees or handles the actual API token

For developers uncomfortable with giving AI coding agents direct API token access, this is a meaningful security boundary.

---

## JSON Mode and Shell Integration

`mcpc --json` enables machine-readable output for every command. This makes mcpc composable with standard Unix tools:

```bash
# List tool names as a JSON array
mcpc --json @apify tools-list | jq '[.tools[].name]'

# Pipe call results into further processing
mcpc --json @apify tools-call get-dataset-items datasetId:="abc123" | jq '.items[]'
```

The JSON mode is designed specifically for AI agents in code mode — Claude Code writing a Python script that calls mcpc as a subprocess, parses the JSON output, and acts on the results. This is a genuinely different workflow than "chat with an LLM," and mcpc is built to support it cleanly.

---

## Installation

```bash
npm install -g @apify/mcpc
# or
bun install -g @apify/mcpc
```

Node.js ≥ 20 is required. On Linux, keychain integration requires `libsecret` and `gnome-keyring`; headless environments fall back to the file-based credential store automatically. The `npx @apify/mcpc` invocation also works without a global install.

---

## Project Activity

mcpc went from first commit in December 2025 to v0.2.6 by April 2026 — five months of rapid development. The 0.2.0 release in March 2026 was a significant redesign (command-first CLI syntax replacing a prior subcommand layout). 179 merged PRs across that period indicates high internal velocity, though the dominant contributor is Jan Curn himself.

Security patches (XSS, DNS rebinding fixes) shipped in v0.2.4 (April 7, 2026), suggesting the project is being treated with production seriousness even at pre-1.0 stage.

---

## What mcpc Is Not

mcpc does not embed an LLM. It does not have multi-provider support. It does not run execution plans, save conversation history, or open a browser dashboard. These are not gaps — they are out of scope by design. mcpc's philosophy is that the LLM lives elsewhere (in Claude Code, in Cursor, in a custom agent); mcpc is the MCP layer that LLM controls via shell commands.

If you want a terminal-based conversational interface that routes prompts through multiple LLM providers and calls MCP tools on your behalf, **[IBM/mcp-cli](/reviews/ibm-mcp-cli/)** is that tool. If you want to add MCP connectivity to an AI coding agent workflow, centralize credentials across multiple AI tools, or handle async MCP operations from scripts, mcpc is the better fit.

---

## Known Limitations and Open Issues

- **Pre-1.0** — active development; breaking changes happened at 0.2.0 and may happen again
- **Node.js ≥ 20 required** — excludes older environments
- **No stdio server inline connection** — connecting to stdio-based MCP servers requires a config file; no `--command` flag yet (PR open)
- **macOS Keychain timeout** — 5-second timeout too short when the OS prompts for keychain access (issue #55)
- **JSON mode not fully MCP-spec-compliant** — list commands do not yet match MCP spec format exactly (issue #183)
- **Heavily Apify-oriented documentation** — all examples reference mcp.apify.com; universal capability is real but undersold in the docs
- **x402 payment feature is experimental** — requires USDC on Base blockchain; only relevant for Apify Actor runs

None of these are blockers for the core use case, but they are worth knowing before adopting mcpc for production workflows.

---

## About Apify

Apify (founded 2015, Y Combinator) is a web scraping and automation platform based in Prague. Their hosted product provides 27,000+ pre-built "Actors" — serverless scraping and automation tasks — accessible via API. Notable clients include T-Mobile, Accenture, Princeton University, OpenTable, Roche, and Siemens. Their MCP server at mcp.apify.com connects AI agents to the Actor marketplace. mcpc was built to make that connection work reliably for AI coding agents, then released as a general-purpose MCP client.

---

## Rating: 3.5 / 5

mcpc solves a real problem that IBM/mcp-cli does not address: MCP connectivity infrastructure for AI agents operating in code mode. The persistent session model, OAuth 2.1 with keychain storage, credential sandboxing proxy, and full async task support are genuinely useful additions to the MCP client ecosystem.

The deductions: pre-1.0 status with a recent breaking redesign means users should expect ongoing interface changes. Community traction (538 stars) is modest relative to its ambition. Documentation is heavily Apify-centric, which undersells the universal capability. The stdio connection gap (no inline `--command` flag) is a minor friction point for servers that require it.

For developers building AI coding agent workflows that need to call MCP servers from shell commands, or who want centralized credential management across Claude Code, Cursor, and Codex, mcpc is the tool to reach for. For users who want a conversational terminal interface with LLM provider selection and execution plans, see our **[IBM/mcp-cli review](/reviews/ibm-mcp-cli/)** instead.

---

*Reviewed 2026-05-05. Research based on public GitHub repository, npm package history, project documentation, and Hacker News discussions. We do not have hands-on testing access to rate live performance.*
