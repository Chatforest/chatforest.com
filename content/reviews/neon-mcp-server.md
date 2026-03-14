---
title: "The Neon MCP Server — Serverless Postgres Management Through Natural Language"
date: 2026-03-14T08:01:47+09:00
description: "Neon's official MCP server brings serverless Postgres management, branch-based migrations, and query tuning directly into your AI coding agent. 20 tools, OAuth authentication, and the best migration workflow in any database MCP server. Here's the honest review."
og_description: "Neon's official MCP server lets AI agents manage serverless Postgres with branch-based migrations, OAuth auth, and 20 tools. The best cloud database MCP experience available. Rating: 4/5."
content_type: "Review"
card_description: "Neon's first-party MCP server for AI-assisted serverless Postgres management. OAuth authentication, 20 tools covering project management, branch-based migrations, query tuning, and SQL execution — the most thoughtful database MCP server we've reviewed."
---

The Neon MCP server is Neon's official tool for connecting AI coding agents to their serverless Postgres platform. Instead of clicking through the Neon console or writing CLI commands, your agent can create projects, branch databases, run migrations, tune queries, and execute SQL — all through natural language.

It's first-party and actively maintained at [neondatabase/mcp-server-neon](https://github.com/neondatabase/mcp-server-neon). With 389 GitHub stars and a hosted remote server at `mcp.neon.tech` with OAuth 2.0 authentication, it represents where cloud database MCP servers are heading. The npm package (`@neondatabase/mcp-server-neon`) is now deprecated in favor of the remote server — Neon is going all-in on hosted MCP.

This is the first cloud-native database MCP server we've reviewed, and it makes the archived official Postgres and SQLite servers look like proof-of-concepts. Which, to be fair, they were.

## What It Does

The server exposes 20 tools organized across five categories:

**Project & Database Management**
- `list_projects` / `list_shared_projects` — browse your Neon projects
- `describe_project` — detailed project info including branches, databases, and configuration
- `create_project` — provision a new serverless Postgres instance
- `delete_project` — tear down a project and all associated resources

**Branch-Based Migrations** (the killer feature)
- `prepare_database_migration` — creates a temporary branch, applies the migration there
- `complete_database_migration` — merges the migration to the main branch after verification
- `get_database_tables` — list all tables in a database
- `describe_table_schema` — retrieve column definitions, types, and constraints

**SQL Execution**
- `run_sql` — execute queries directly against your Neon databases
- `run_sql_transaction` — execute multi-statement transactions

**Query Tuning**
- `list_slow_queries` — identify performance bottlenecks
- `explain_sql_statement` — get EXPLAIN output for query analysis
- `prepare_query_tuning` — create a branch for testing optimizations
- `complete_query_tuning` — apply or discard tuning changes

**Authentication & Data API**
- `provision_neon_auth` — set up authentication for your database
- `get_connection_string` — retrieve connection details for a database

**Documentation**
- `list_docs_resources` — discover available Neon documentation pages
- `get_doc_resource` — fetch documentation as markdown

The standout is the **branch-based migration workflow**. When your agent runs `prepare_database_migration`, Neon creates an instant copy-on-write branch from your production data. The migration runs on this branch first. Your agent can verify the results — check that tables look right, run test queries, confirm the schema — before calling `complete_database_migration` to merge it to the main branch. If something goes wrong, just discard the branch. No rollback scripts, no downtime risk.

This is genuinely clever. Neon's branching is near-instant because of their copy-on-write storage architecture. What would be a risky operation on a traditional database (running DDL on production) becomes a safe, reviewable workflow. Neon even published a [blog post](https://www.zenml.io/llmops-database/implementing-evaluation-framework-for-mcp-server-tool-selection) about building an evaluation framework to ensure LLMs select the right migration tools — they improved tool selection from 60% to 100% through prompt engineering alone.

The **query tuning tools** follow the same pattern: branch, optimize, verify, merge or discard. It's a consistent "safe experimentation" philosophy throughout the server.

## Setup

Neon offers two paths, but strongly recommends the remote server:

**Remote server (recommended — zero install, OAuth):**

```json
{
  "mcpServers": {
    "neon": {
      "url": "https://mcp.neon.tech/mcp"
    }
  }
}
```

First connection triggers an OAuth flow in your browser. No API keys to manage, no tokens on disk. The server uses Streamable HTTP transport by default — if your client doesn't support that yet, use `https://mcp.neon.tech/sse` for Server-Sent Events fallback.

**Local server (deprecated):**

```json
{
  "mcpServers": {
    "neon": {
      "command": "npx",
      "args": ["-y", "@neondatabase/mcp-server-neon", "start", "<YOUR_NEON_API_KEY>"]
    }
  }
}
```

The npm package still works but is officially deprecated. Neon wants everyone on the remote server — you get automatic updates and don't need to manage API keys. This is the same trend we saw with [Sentry](/reviews/sentry-mcp-server/) and [Notion](/reviews/notion-mcp-server/): first-party vendors are moving to hosted, OAuth-authenticated remote servers.

**One-command setup:**

```bash
npx neonctl@latest init
```

This automatically configures the MCP server for Claude Code, Cursor, or VS Code, along with Neon's agent skills. It's the smoothest onboarding we've seen for any database MCP server.

## What's Good

**Branch-based safety model.** The migration and query tuning workflows are the most thoughtful approach to database management we've seen in any MCP server. Every dangerous operation happens on a branch first. This is what the archived official Postgres server *should* have been — instead of a read-only wrapper with a [SQL injection vulnerability](/reviews/postgresql-mcp-server/), Neon gives you full write access with structural safety guarantees.

**Remote-first architecture.** OAuth authentication, automatic updates, no local dependencies. The developer experience is genuinely good — one URL in your config and you're connected.

**Comprehensive tooling.** 20 tools covering the full lifecycle: provision → develop → migrate → tune → operate. Most database MCP servers give you query execution and maybe schema inspection. Neon gives you project management, branching, migration workflows, and performance tuning.

**Free tier is generous.** 100 projects, 100 compute-hours per project per month, 0.5 GB storage per branch. Post-Databricks acquisition, storage pricing dropped from $1.75 to $0.35/GB-month. You can meaningfully develop with the MCP server without paying anything.

**Evaluation-driven development.** Neon built a formal evaluation framework for LLM tool selection accuracy and published their findings. They improved from 60% to 100% correct tool selection through prompt engineering. This kind of rigor is rare in MCP server development.

## What's Not

**Neon-only.** This server works exclusively with Neon's serverless Postgres. If your database is on RDS, Supabase, or self-hosted Postgres, this server is useless to you. It's a management API wrapper, not a generic Postgres client. Compare this to [Postgres MCP Pro](https://github.com/crystalcreates/postgresql-mcp-pro) which connects to any Postgres instance.

**Development only.** Neon's own documentation states the server is "intended for local development and IDE integrations only" and is "not recommended for production environments." The concern is that LLMs might execute powerful operations (like `delete_project`) without adequate confirmation. This is honest, but it limits the server's utility for operations work.

**OAuth requires a browser.** The remote server's OAuth flow opens a browser for consent. This works great in desktop IDEs but is problematic for headless environments, CI/CD pipelines, or remote development servers. The deprecated API key approach actually works better for automated workflows — and it's being phased out.

**Tool count can confuse LLMs.** Neon themselves discovered that LLMs struggled to select the right tool from their 20-tool set, with initial accuracy at only 60%. They fixed this through better tool descriptions, but the underlying problem — that more tools means more potential for misrouting — remains a design tension. Each tool has a scope category for permission filtering, which helps, but it's still a lot of tools for an agent to reason about.

**No read-only mode.** Unlike the (flawed) official Postgres server that at least *attempted* read-only access, Neon's server is full read-write from the start. The branch-based safety model mitigates this for migrations, but `run_sql` executes directly on your database. There's no "explore without risk" mode for ad-hoc queries.

## How It Compares

| Feature | Neon MCP | Postgres MCP (archived) | SQLite MCP (archived) | DBHub |
|---------|----------|------------------------|----------------------|-------|
| **Maintained** | Yes (first-party) | No (archived) | No (archived) | Yes (community) |
| **Auth** | OAuth 2.0 | None | None | None |
| **Migration safety** | Branch-based | Read-only (bypassed) | None | None |
| **Tools** | 20 | 5 | 6 | ~10 |
| **Query tuning** | Yes | No | No | No |
| **Project management** | Yes | No | No | No |
| **Works with** | Neon only | Any Postgres | Local SQLite | Multiple databases |
| **Remote server** | Yes | No | No | No |
| **Free tier** | Yes (100 CU-hrs/mo) | N/A | N/A | N/A |

Neon is clearly the most capable database MCP server available — but it's also the most locked-in. If you're already on Neon or starting a new project, this is excellent. If you need to connect to an existing non-Neon database, look at [DBHub](https://github.com/bytebase/dbhub) or Postgres MCP Pro instead.

For a broader comparison, see our [Best Database MCP Servers](/guides/best-database-mcp-servers/) guide.

## The Bigger Picture

Neon's MCP server represents a clear evolution in what database tooling for AI agents should look like. The archived official servers from Anthropic were minimal reference implementations — they proved the concept but weren't safe or capable enough for real work. Community servers like DBHub and Postgres MCP Pro filled the gap with better multi-database support. Now Neon shows what a well-funded first-party team can build: OAuth authentication, branch-based safety, performance tuning, and an evaluation framework to make sure the LLM actually picks the right tool.

The tradeoff is vendor lock-in. Every improvement Neon makes to this server makes you more dependent on Neon's platform. The branch-based migration workflow — the server's best feature — only works because of Neon's copy-on-write storage architecture. You can't get this on vanilla Postgres.

Whether that tradeoff is worth it depends on where you are. For new projects, Neon's free tier + MCP server is arguably the best way to start a database-backed AI workflow. For existing projects on other platforms, this server offers nothing.

## Rating: 4/5

The Neon MCP server earns a 4/5 for being the most capable and thoughtfully designed database MCP server available. The branch-based migration workflow is genuinely innovative, the OAuth-first remote architecture sets the right standard, and the 20-tool coverage is comprehensive without being bloated. It loses a point for being Neon-only (vendor lock-in is real), the development-only limitation, and the OAuth flow that doesn't work well in headless environments. But if you're building on Neon — or willing to start — this is the database MCP server to use.

**Use this if:** You're building on Neon serverless Postgres and want AI-assisted database management with real safety guarantees.

**Skip this if:** Your database is on RDS, Supabase, or self-hosted Postgres — this server literally cannot connect to it.
