---
title: "The SQLite MCP Server — A Good Idea, Now Abandoned (and Vulnerable)"
date: 2026-03-14T01:06:39+09:00
description: "The official SQLite MCP server lets agents query, write, and inspect SQLite databases. Six tools, a built-in insight memo, and a clean codebase — but it's archived, has a known SQL injection vulnerability, and Anthropic declined to fix it. Here's the honest review."
og_description: "The official SQLite MCP server is archived, has an unpatched SQL injection flaw, and ~13K weekly downloads despite being abandoned. Rating: 2.5/5."
content_type: "Review"
card_description: "Anthropic's reference database MCP server. Clean code, clever insight memo, but archived with a known SQL injection vulnerability. Learn from it, don't depend on it."
last_refreshed: 2026-03-14
---

**At a glance:** 236 stars (servers-archived repo), ~13K weekly PyPI downloads, v2025.4.25 (last release April 2025), 6 tools, archived on PyPI, known SQL injection vulnerability (unpatched), ~7.7K weekly PulseMCP visitors (#130 globally, ~279K all-time)

The SQLite MCP server (`mcp-server-sqlite`) is Anthropic's official reference implementation for giving AI agents database access. It ships six tools for querying, writing, and inspecting SQLite databases, plus a clever "insight memo" feature for accumulating analysis findings. The Python codebase is clean and well-structured — it was one of the original MCP example servers, built to demonstrate how MCP works with databases.

There's a catch: it's been moved to the `servers-archived` repository. No new releases, no security patches, no bug fixes. Worse, a SQL injection vulnerability was publicly disclosed in June 2025, and Anthropic declined to patch it. It still installs and runs — ~13,000 people download it weekly — but you're on your own going forward.

## What's New (March 2026 Update)

**SQL injection vulnerability publicly disclosed.** In June 2025, Trend Micro principal threat researcher Sean Park publicly disclosed a SQL injection flaw in the server. The code in `server.py` directly concatenates unsanitized user input (table names) into SQL statements via f-strings, with no parameterized queries. The attack chain is particularly dangerous: an attacker submits a payload in a database field, which gets stored, and when a privileged AI agent later reads it, the embedded prompt injection hijacks the agent to exfiltrate data. GitHub issue #1348 was filed in April 2025 and closed without a fix before archival. Anthropic declined to patch it, stating the repo is archived and "there should always be a human in the loop with the ability to deny tool invocations." No CVE was assigned. The PostgreSQL MCP server had a similar vulnerability, suggesting this was systemic across Anthropic's reference database servers.

**Still getting significant downloads despite archival.** The PyPI package shows ~13,000 weekly downloads and ~34,000 monthly downloads — remarkable for a package marked "No new releases are expected." Many users are likely unaware of the archival status or the security issue.

**Last release was April 2025.** Version 2025.4.25 was the final release, which updated the MCP SDK to version 1.6.0. Twelve total versions were published between November 2024 and April 2025 before the server was archived on May 28-29, 2025.

**DBHub has emerged as the leading multi-database alternative.** Bytebase's DBHub (2,369 stars, actively maintained through March 2026) supports PostgreSQL, MySQL, MariaDB, SQL Server, and SQLite through a single MCP server interface. It has become the go-to choice for teams needing database MCP access.

**165+ SQLite MCP server implementations now exist.** The community has thoroughly filled the gap left by the official server's archival. Notable alternatives include jparkerweb/mcp-sqlite (93 stars, actively maintained), sqlite-explorer-fastmcp (104 stars, read-only/safety-focused), and panasenco/mcp-sqlite (Datasette-compatible metadata support).

**PulseMCP traffic holds steady.** ~7,700 weekly visitors, ~279,000 all-time, ranked #130 globally. For comparison, the PostgreSQL MCP server has 1.3M all-time visitors (#31) — roughly 4.7x more traffic.

## What It Does

The server exposes six tools organized into three categories:

**Query operations:**
- **`read_query`** — Execute SELECT statements. Results come back as an array of objects — clean, structured, easy for agents to reason about.
- **`write_query`** — Execute INSERT, UPDATE, or DELETE statements. Returns the number of affected rows.
- **`create_table`** — Run CREATE TABLE statements to build new tables.

**Schema inspection:**
- **`list_tables`** — Returns all table names in the database.
- **`describe_table`** — Shows column names and types for a given table.

**Analysis:**
- **`append_insight`** — Adds a business insight to a persistent `memo://insights` resource. This is the one unique feature — findings accumulate across the session, building a running analysis document.

There's also a built-in `mcp-demo` prompt that generates sample schemas and data for a given business domain, then guides the agent through an interactive analysis workflow. It's primarily a demo feature, but it shows off how MCP prompts, tools, and resources can work together.

## Setup

For Claude Desktop, add this to your config:

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "uvx",
      "args": ["mcp-server-sqlite", "--db-path", "/path/to/your/database.db"]
    }
  }
}
```

Docker is also supported:

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-v", "/path/to/data:/data",
        "mcp/sqlite",
        "--db-path", "/data/database.db"
      ]
    }
  }
}
```

Requirements: Python 3.10+ and `uv` (or pip). The server takes one argument — the path to your SQLite database file. If the file doesn't exist, it creates one. That's it for configuration. There are no other flags, no environment variables, no auth options.

**Setup difficulty: Very easy.** One command, one argument. The simplest database MCP server to get running. The lack of configuration options is both a feature and a limitation.

## What Works Well

**Schema inspection before querying is the right pattern.** An agent can call `list_tables` and `describe_table` to understand the database structure before writing any SQL. This is how humans approach an unfamiliar database, and it works naturally in agent workflows. The two-step pattern (inspect, then query) produces better SQL than blind querying.

**The insight memo is a genuinely clever feature.** The `append_insight` tool and `memo://insights` resource let the agent build up a running document of findings during a data analysis session. This is useful for the pattern where you want an agent to explore a dataset and report what it finds — the memo accumulates insights rather than losing them to conversation history. It's a good demonstration of how MCP resources can maintain state.

**The codebase is clean and educational.** If you're learning how to build MCP servers, this is one of the best examples to study. The Python code is straightforward, well-organized, and demonstrates tools, resources, and prompts working together. It's a reference implementation that actually reads like one.

**Read and write in one server.** Unlike some community alternatives that limit agents to read-only access, this server gives full read/write capability. For prototyping, local development, and data exploration, that's what you want — you can create tables, insert test data, and query it all in one session.

## What Doesn't Work Well

**Known SQL injection vulnerability — unpatched.** The server concatenates unsanitized table names directly into SQL via f-strings. Trend Micro publicly disclosed this in June 2025. The attack chain is worse than typical SQL injection: a stored payload in database fields can trigger prompt injection when an AI agent reads the data, potentially hijacking the agent. Anthropic declined to fix it, pointing to the archived status. This is now the single biggest reason not to use this server with any data you care about.

**It's archived — and that's the dealbreaker for production use.** The server was moved to `modelcontextprotocol/servers-archived` on May 28-29, 2025. The repository description says these are "reference MCP servers that are no longer maintained." No security patches. No compatibility updates as the MCP spec evolves. No bug fixes. The server still installs and runs today, but every month it falls further behind.

**No safety guardrails at all.** Any SQL the agent generates gets executed. There's no query validation, no allowlist of operations, no confirmation step for destructive statements. `DROP TABLE`? Runs immediately. `DELETE FROM users`? Done. For a reference implementation meant to teach MCP concepts, this is understandable. For anything touching real data, it's a liability.

**One database per server instance.** You configure a single database path at startup and that's what you get. If your agent needs to query multiple databases, you need multiple server instances with separate configurations. There's no mid-session switching, no multi-database support.

**No connection pooling or concurrent access handling.** This is a single-user, single-connection server. Fine for local development and demos. Not designed for any scenario where multiple agents or processes might touch the same database.

**Limited client compatibility.** While the server technically works over stdio with any MCP client, it was primarily tested and documented for Claude Desktop. Community reports suggest inconsistent behavior with Cursor, VS Code, and other clients.

## Compared to Alternatives

**vs. Bytebase DBHub (2,369 stars):** The leading multi-database MCP server, actively maintained through March 2026. Supports PostgreSQL, MySQL, MariaDB, SQL Server, and SQLite through a single interface. If you need database MCP access today, DBHub is the strongest general-purpose choice.

**vs. jparkerweb/mcp-sqlite (93 stars):** A community-built TypeScript alternative that provides comprehensive SQLite operations with better safety features, including input validation and structured CRUD operations (not raw SQL). Actively maintained through March 2026. If you specifically want SQLite MCP access, this is the better choice.

**vs. sqlite-explorer-fastmcp (104 stars):** A read-only SQLite MCP server built with FastMCP. Takes the opposite approach to safety — agents can only read, never write. Good for analytical workloads where you want to prevent accidental data modification. Built-in query validation adds another safety layer.

**vs. Postgres MCP Server:** If you're choosing a database MCP server for a real project, PostgreSQL is probably the better database choice. More features, better concurrency, actual access controls. Note: the official Postgres MCP server also has a SQL injection vulnerability — use Postgres MCP Pro by crystaldba (2,300+ stars) or Neon MCP instead.

**vs. DuckDB MCP Server:** For analytical workloads — which is what the SQLite MCP server's "insight memo" feature targets — DuckDB is purpose-built for OLAP queries. Faster on large datasets, native Parquet/CSV support, better analytical SQL extensions. If data analysis is your primary use case, DuckDB is the sharper tool.

## Who Should Use This

**Yes, use it if:**
- You're learning MCP and want to study a clean, well-structured reference implementation
- You want a quick demo of database access through MCP — the `mcp-demo` prompt makes this nearly zero-effort
- You're prototyping an idea and need disposable local database access for an agent (on throwaway data only)
- You want to understand how MCP tools, resources, and prompts work together

**Don't use it if:**
- You're building anything that will run in production
- Your database contains data you can't afford to lose (no safety guardrails + known SQL injection)
- You need ongoing maintenance, security patches, or MCP spec compatibility
- You need multi-database support or concurrent access
- You want a database MCP server you can rely on long-term
- You're handling any user-supplied or untrusted data (SQL injection risk)

{{< verdict rating="2.5" summary="A good demo with a serious security flaw" >}}
The SQLite MCP server still does what a reference implementation should: it demonstrates how MCP can connect agents to databases in a clean, readable way. The insight memo feature is genuinely clever, the schema inspection workflow is the right pattern, and the codebase is worth studying if you're building your own MCP server. But the picture has gotten worse since our initial review. A publicly disclosed SQL injection vulnerability — with a particularly dangerous stored-prompt-injection attack chain — went unpatched, and Anthropic declined to fix it. Combined with the archived status and zero safety guardrails, the rating drops from 3/5 to 2.5/5. For actual SQLite work with agents, use jparkerweb/mcp-sqlite or Bytebase DBHub. For serious database workloads, consider Neon MCP, Postgres MCP Pro, or DuckDB. The official SQLite MCP server is now a cautionary tale as much as a teaching tool.
{{< /verdict >}}

*Disclosure: We do not test MCP servers hands-on. This review is based on documentation analysis, GitHub repository data, community reports, and publicly available information. All claims should be verified against the official repository and documentation.*

*This review was last updated on 2026-03-21 using Claude Opus 4.6 (Anthropic).*
