---
title: "The Neon MCP Server — Serverless Postgres Management Through Natural Language"
date: 2026-03-14T08:01:47+09:00
description: "Neon's official MCP server brings serverless Postgres management, branch-based migrations, and query tuning directly into your AI coding agent."
og_description: "Neon's official MCP server lets AI agents manage serverless Postgres with branch-based migrations, OAuth auth, and 20 tools. The best cloud database MCP experience available. Rating: 4/5."
content_type: "Review"
card_description: "Neon's first-party MCP server for AI-assisted serverless Postgres management. OAuth authentication, 20 tools covering project management, branch-based migrations, query tuning, and SQL execution — the most thoughtful database MCP server we've reviewed."
last_refreshed: 2026-04-17
---

Part of our **[Databases MCP category](/categories/databases/)**.

*At a glance: 582 GitHub stars, 104 forks, ~194 commits, 12+ contributors, last commit Apr 16 2026, npm v0.6.5 (deprecated — remote server preferred), 20+ tools, MIT license, ~3,284 npm downloads/week, PulseMCP ~115K all-time visitors (#301 globally, ~1,100 weekly). Neon platform: acquired by Databricks for $1B (May 2025), Postgres 14–18 support, storage $0.35/GB-month, Lakebase GA on Azure, Agent Plan for AI platforms.*

The Neon MCP server is Neon's official tool for connecting AI coding agents to their serverless Postgres platform. Instead of clicking through the Neon console or writing CLI commands, your agent can create projects, branch databases, run migrations, tune queries, and execute SQL — all through natural language.

It's first-party and actively maintained at [neondatabase/mcp-server-neon](https://github.com/neondatabase/mcp-server-neon). With 582 GitHub stars and a hosted remote server at `mcp.neon.tech` with OAuth 2.0 authentication, it represents where cloud database MCP servers are heading. The npm package (`@neondatabase/mcp-server-neon`) is now officially deprecated in favor of the remote server — Neon has gone all-in on hosted MCP. The local stdio CLI was removed entirely in February 2026.

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

**Compute & Performance Monitoring**
- `list_branch_computes` — view compute endpoints per branch
- `list_slow_queries` — identify performance bottlenecks

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

**API key authentication (for headless/CI environments):**

The remote server now also supports API key authentication, addressing a major gap for headless environments. No browser-based OAuth flow needed — you can pass a Neon API key directly.

**Local server (removed):**

The local stdio CLI was removed entirely in February 2026 (PR #198). The npm package `@neondatabase/mcp-server-neon` (v0.6.5) is officially deprecated and directs users to the remote server. This is the same trend we saw with [Sentry](/reviews/sentry-mcp-server/) and [Notion](/reviews/notion-mcp-server/): first-party vendors are moving to hosted, OAuth-authenticated remote servers.

**One-command setup:**

```bash
npx neonctl@latest init
```

This automatically configures the MCP server for Claude Code, Cursor, or VS Code, along with Neon's agent skills. It's the smoothest onboarding we've seen for any database MCP server.

## What's Good

**Branch-based safety model.** The migration and query tuning workflows are the most thoughtful approach to database management we've seen in any MCP server. Every dangerous operation happens on a branch first. This is what the archived official Postgres server *should* have been — instead of a read-only wrapper with a [SQL injection vulnerability](/reviews/postgresql-mcp-server/), Neon gives you full write access with structural safety guarantees.

**Remote-first architecture.** OAuth authentication, automatic updates, no local dependencies. The developer experience is genuinely good — one URL in your config and you're connected.

**Comprehensive tooling.** 20 tools covering the full lifecycle: provision → develop → migrate → tune → operate. Most database MCP servers give you query execution and maybe schema inspection. Neon gives you project management, branching, migration workflows, and performance tuning.

**Free tier is generous.** 100 projects, 100 compute-hours per project per month, 0.5 GB storage per branch. Post-Databricks acquisition, storage pricing dropped 80% from $1.75 to $0.35/GB-month, and compute costs dropped 15-25% across all tiers. Unlimited organization members on Free plan. You can meaningfully develop with the MCP server without paying anything.

**Grant-scoped access control.** The remote server supports runtime scoping via URL query parameters (migrated from `X-Neon-*` headers in April 2026 — PR #210) that dynamically filter available tools per authentication grant. This means OAuth integrations can restrict an agent to read-only mode or limit it to a specific project — addressing the "too much power" concern without reducing the overall tool count.

**Evaluation-driven development.** Neon built a formal evaluation framework for LLM tool selection accuracy and published their findings. They improved from 60% to 100% correct tool selection through prompt engineering. This kind of rigor is rare in MCP server development. All 29 tool definitions now include scope fields for permission filtering.

**OpenAI verification and MCP annotations.** As of April 2026 (PR #225), the server supports OpenAI verification tokens and passes tool annotations to MCP responses — expanding compatibility beyond Claude to OpenAI's emerging MCP integrations.

**Supply chain hardening.** PR #215 (April 2026) SHA-pinned all GitHub Action references and added least-privilege permission blocks — the kind of security hygiene that most MCP servers still lack.

## What's Not

**Neon-only.** This server works exclusively with Neon's serverless Postgres. If your database is on RDS, Supabase, or self-hosted Postgres, this server is useless to you. It's a management API wrapper, not a generic Postgres client. Compare this to [Postgres MCP Pro](https://github.com/crystalcreates/postgresql-mcp-pro) which connects to any Postgres instance.

**Development only.** Neon's own documentation states the server is "intended for local development and IDE integrations only" and is "not recommended for production environments." The concern is that LLMs might execute powerful operations (like `delete_project`) without adequate confirmation. This is honest, but it limits the server's utility for operations work.

**OAuth still has rough edges.** While API key authentication now exists for headless environments, the OAuth flow still has some reported issues. The token refresh race condition (#209) was fixed in April 2026 using a SingleFlight pattern with database locking, and the OAuth state/headers regression (#210) was also resolved. But the infinite authorization loop (#186, open since February) and the foundational OAuth design concerns around dynamic client registration (#66, open since May 2025) remain unresolved. The security audit request (#207) was completed and closed in April 2026.

**Tool count can confuse LLMs.** Neon themselves discovered that LLMs struggled to select the right tool from their 20+ tool set, with initial accuracy at only 60%. They fixed this through better tool descriptions and added scope fields to all 29 definitions, but the underlying problem — that more tools means more potential for misrouting — remains a design tension. PR #208 (March 2026) continues refining tool descriptions for better agent selection.

**Read-only mode exists but is maturing.** The grant-scoped access control supports read-only mode via URL query parameters (migrated from headers in April 2026). This only applies to the remote server with OAuth grants. The migration safety model still relies on branches for write operations.

**Dollar-quoted SQL breaks migrations.** Issue #201 (February 2026) reports that `prepare_database_migration` fails on dollar-quoted strings — a common pattern in Postgres stored procedures. This is a real usability gap for teams with non-trivial schemas.

## How It Compares

| Feature | Neon MCP | Supabase MCP | DBHub | MCP Toolbox (Google) |
|---------|----------|-------------|-------|---------------------|
| **Maintained** | Yes (first-party) | Yes (first-party) | Yes (community) | Yes (Google) |
| **Auth** | OAuth 2.0 + API key | OAuth 2.0 | None | Google Auth |
| **Migration safety** | Branch-based | None | None | None |
| **Tools** | 20+ | ~20 | ~10 | Varies |
| **Query tuning** | Yes | No | No | No |
| **Read-only mode** | Yes (grant-scoped) | No | No | No |
| **Works with** | Neon only | Supabase only | Multiple databases | 40+ data sources |
| **Remote server** | Yes | Yes | No | Yes |
| **Free tier** | Yes (100 CU-hrs/mo) | Yes | N/A | GCP credits |

The competitive landscape has shifted since our initial review. Supabase now has OAuth-based MCP with edge function support. Google's MCP Toolbox supports 40+ data sources. But Neon remains the only database MCP server with branch-based migration safety — and that's still the killer differentiator.

If you're already on Neon or starting a new project, this is excellent. If you need multi-database support, [DBHub](https://github.com/bytebase/dbhub) (ultra-efficient at 1.4K tokens vs 19K+ for competitors) or Google's MCP Toolbox are better fits.

For a broader comparison, see our [Best Database MCP Servers](/guides/best-database-mcp-servers/) guide.

## The Bigger Picture

Neon's MCP server represents a clear evolution in what database tooling for AI agents should look like. The archived official servers from Anthropic were minimal reference implementations — they proved the concept but weren't safe or capable enough for real work. Community servers like DBHub and Postgres MCP Pro filled the gap with better multi-database support. Now Neon — backed by Databricks since May 2025 — shows what a well-funded first-party team can build: OAuth authentication, branch-based safety, performance tuning, grant-scoped access control, and an evaluation framework to make sure the LLM actually picks the right tool.

The February 2026 removal of the local CLI marks a clear commitment to the remote-first model. No more `npx` installs, no more API keys on disk (unless you want them for headless use). The server now publishes a `server.json` for the MCP Registry, positioning itself as a first-class entry in the emerging MCP ecosystem infrastructure.

The grant-scoped access control — now migrated from headers to URL query parameters (April 2026) — is a quiet but significant addition. Being able to restrict an agent to read-only mode or a specific project via OAuth scopes is exactly the kind of fine-grained permission model that database MCP servers need. It partially addresses the "development only" concern — if you can scope an agent's access tightly enough, production use becomes more defensible.

April 2026 brought a burst of important fixes: the token refresh race condition (#209) and OAuth state regression (#210) were both resolved, and the security audit (#207) was completed and closed. The OpenAI verification support (PR #225) signals Neon is positioning the MCP server for multi-platform compatibility beyond Claude. Supply chain hardening (SHA-pinned CI actions, least-privilege permissions) shows security maturity.

On the platform side, Neon's Databricks-backed **Agent Plan** — custom resource limits and credits for AI platforms provisioning thousands of databases — suggests Neon sees AI agents as a primary use case, not an afterthought. Lakebase (Neon's technology powering Databricks) is now GA on 14 Azure regions, and snapshot storage billing ($0.09/GB-month) starts May 1, 2026.

The tradeoff is still vendor lock-in. Every improvement Neon makes to this server makes you more dependent on Neon's platform. The branch-based migration workflow — the server's best feature — only works because of Neon's copy-on-write storage architecture. You can't get this on vanilla Postgres. But with storage at $0.35/GB-month and Postgres 14–18 support, the lock-in penalty keeps shrinking.

Open issues worth watching: the dollar-quoted SQL bug (#201) and the infinite auth loop (#186). At 11 open issues and 17 open PRs (mostly Dependabot), the project is actively maintained — the April 2026 fixes addressed the most critical outstanding problems.

## Rating: 4/5

The Neon MCP server earns a 4/5 for being the most capable and thoughtfully designed database MCP server available. The branch-based migration workflow is genuinely innovative, the remote-first architecture with grant-scoped access control sets the right standard, and the 20+ tool coverage is comprehensive without being bloated. It loses a point for Neon-only lock-in, the unresolved infinite auth loop (#186), and the dollar-quoted SQL migration bug (#201). But the trajectory is strong — the April 2026 fixes addressed the token refresh race condition and OAuth state regression, the security audit is complete, and OpenAI verification support shows multi-platform ambition. If you're building on Neon — or willing to start — this is the database MCP server to use.

**Use this if:** You're building on Neon serverless Postgres and want AI-assisted database management with real safety guarantees.

**Skip this if:** Your database is on RDS, Supabase, or self-hosted Postgres — this server literally cannot connect to it. Look at [Supabase MCP](https://supabase.com/features/mcp-server) for Supabase, or [DBHub](https://github.com/bytebase/dbhub) for multi-database support.

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic). We did not hands-on test this server — our analysis is based on public documentation, GitHub repositories, npm data, and community reports. Last edited 2026-04-17.*
