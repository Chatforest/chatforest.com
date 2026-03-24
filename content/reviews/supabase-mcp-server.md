---
title: "The Supabase MCP Server — Full Backend Management Through Your AI Assistant"
date: 2026-03-14T08:12:19+09:00
description: "Supabase's official MCP server goes beyond database management — it handles auth, storage, edge functions, branching, and debugging across your entire backend. 8 tool groups, OAuth authentication, and the broadest scope of any database-adjacent MCP server. Here's the honest review."
og_description: "Supabase's official MCP server manages your entire backend through AI — database, auth, storage, edge functions, and more. 8 tool groups, OAuth 2.1, read-only mode. Rating: 4/5."
content_type: "Review"
card_description: "Supabase's first-party MCP server for AI-assisted backend management. OAuth 2.1 authentication, 8 tool groups covering database, edge functions, storage, branching, and debugging — the widest scope of any database-related MCP server we've reviewed."
last_refreshed: 2026-03-14
---

Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** 2.5K GitHub stars, 316 forks, 8 tool groups across full BaaS stack, ~2M all-time PulseMCP visitors (#24 globally, ~51.2K weekly), v0.7.0 current, OAuth 2.1 remote server

The Supabase MCP server is Supabase's official tool for connecting AI coding agents to their Backend-as-a-Service platform. Unlike pure database MCP servers that give you SQL execution and schema management, Supabase's server covers the entire backend: database queries, edge function deployment, storage management, branch-based development, debugging logs, and TypeScript type generation — all through natural language.

It's maintained at [supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp) with 2.5K GitHub stars and 316 forks. The hosted remote server at `mcp.supabase.com` uses OAuth 2.1 authentication — no API keys or tokens to manage. This is the same architectural direction we've seen from [Neon](/reviews/neon-mcp-server/), [Sentry](/reviews/sentry-mcp-server/), and [Notion](/reviews/notion-mcp-server/): first-party vendors moving to hosted, OAuth-authenticated remote servers.

The key distinction: Supabase is a BaaS (Backend-as-a-Service), not just a database. So while [Neon's MCP server](/reviews/neon-mcp-server/) gives you 20 tools for serverless Postgres, Supabase gives you 8 entire tool groups spanning your full backend stack.

## What It Does

The server organizes its capabilities into eight tool groups:

**Account Management** (disabled when project-scoped)
- List and create projects and organizations
- Calculate and confirm costs before provisioning
- Manage project configuration

**Database**
- `list_tables` — browse tables across schemas (v0.7.0 added verbose mode for detailed output)
- `list_extensions` / `list_migrations` — inspect database state
- `apply_migration` — run SQL migrations with automatic tracking
- Execute SQL queries directly against your database

**Branching** (paid plans only)
- `create_branch` / `list_branches` / `delete_branch` — manage development branches
- `merge_branch` / `reset_branch` / `rebase_branch` — git-like branch operations
- Create branches from production schema, test changes, merge back

**Edge Functions**
- List, retrieve, and deploy Edge Functions directly from your AI assistant
- `deploy_edge_function` — push new functions or update existing ones without leaving your IDE

**Development**
- `generate_typescript_types` — create types from your database schema
- Get project URLs and API keys for configuration

**Debugging**
- Retrieve logs from API gateway, PostgreSQL, edge functions, auth, storage, and realtime services
- Access advisory notices for security and performance issues

**Knowledge Base**
- Search Supabase documentation directly within your AI workflow

**Storage** (disabled by default)
- Manage storage buckets and configuration (requires paid plan for updates)

The breadth here is remarkable. Most database MCP servers give you query execution and maybe schema inspection. Supabase gives you database management *plus* serverless function deployment, storage operations, log analysis, and project lifecycle management — all from one server.

## Setup

Supabase offers a clean remote-first setup:

**Remote server (recommended — OAuth, zero install):**

```json
{
  "mcpServers": {
    "supabase": {
      "url": "https://mcp.supabase.com/mcp"
    }
  }
}
```

First connection opens a browser for OAuth 2.1 consent. You select your organization, and you're connected. No tokens, no API keys, no config files.

**Scoped access (recommended for safety):**

```json
{
  "mcpServers": {
    "supabase": {
      "url": "https://mcp.supabase.com/mcp?project_ref=YOUR_PROJECT_REF&read_only=true"
    }
  }
}
```

Query parameters let you restrict the server to a specific project and enable read-only mode. This is a security model that most MCP servers lack entirely.

**Local development server:**

```
http://localhost:54321/mcp
```

When running Supabase locally via `supabase start`, a local MCP server is available with limited tools — no OAuth needed. Good for offline development but missing the full feature set.

## What's New (March 2026)

**v0.7.0 brings typed tool outputs.** Released March 2, 2026, the latest version introduces typed tool outputs via exported Zod schemas — LLM clients can now validate responses programmatically. Also adds a verbose flag to `list_tables` for detailed schema inspection. Five releases in 2026 so far (v0.6.0 through v0.7.0), showing active development cadence.

**Zod v4 and AI SDK v6 upgrade.** v0.6.0 (January 6) modernized the dependency stack with Zod v4, AI SDK v6, and MCP registry publication. The server is now listed in the official MCP registry with proper metadata.

**BYO MCP: deploy your own MCP servers on Supabase.** Supabase now lets you build and deploy custom MCP servers on Edge Functions using the official MCP TypeScript SDK, mcp-lite, or mcp-handler. Your MCP server runs at the edge with an HTTP endpoint accepting JSON-RPC requests. Auth support for BYO MCP servers is coming soon.

**Supabase Auth becomes an OAuth 2.1/OIDC provider.** In public beta since November 2025, Supabase Auth can now act as an identity provider for third-party apps and MCP servers. This complements the MCP server's own OAuth: while the MCP server uses Supabase's OAuth for agent authentication, the new OAuth server feature means your Supabase project can be the auth provider that other MCP servers authenticate against. Row Level Security policies automatically apply to OAuth tokens.

**OAuth scope concerns emerge.** Issue #239 (March 17) flags that the MCP server requests full account access regardless of which tool groups are enabled — if you only need database tools, the server still asks for permissions to manage edge functions, storage, and everything else. This is an active security discussion.

## What's Good

**Broadest scope of any database MCP server.** Supabase's BaaS nature means this server isn't just a database tool — it's a full backend management interface. Deploy edge functions, check logs, manage storage, generate types, and query data all from one server. No other database-adjacent MCP server comes close in breadth.

**Read-only mode done right.** When you enable `read_only=true`, queries execute as a dedicated `supabase_read_only_user` — a real PostgreSQL role restriction, not just query filtering. This is the proper way to implement read-only access, and it's better than what [Neon](/reviews/neon-mcp-server/) offers (Neon has no read-only mode at all).

**Project scoping for access control.** The `project_ref` parameter restricts the server to a single project. Combined with read-only mode and feature group filtering, you get fine-grained access control that most MCP servers don't attempt. You can give your AI assistant access to query your staging database without risking your production project.

**Feature group filtering.** Don't want your AI deploying edge functions? Disable the `functions` group. Only need database access? Enable just `database`. This granular control over what tools are available to the LLM reduces the risk of unintended actions.

**OAuth 2.1 with no manual tokens.** Dynamic client registration means you don't need to create a PAT or OAuth app. Just point your client at the URL and log in. The smoothest auth setup we've seen alongside Neon.

**Strong security recommendations.** Supabase explicitly recommends: don't connect to production, use read-only mode for real data, scope to specific projects, and enable manual tool approval in clients. This level of transparency about risks is refreshing — most MCP servers don't mention security at all.

## What's Not

**Branching is schema-only.** This is the biggest gap compared to Neon. When you create a branch in Supabase, it copies your schema and runs migrations — but no data comes along. You need a seed script to populate the branch. Neon's copy-on-write branching instantly duplicates both schema *and* data. For testing migrations against realistic data, Neon's approach is significantly better.

**Branching requires paid plan.** The branching tool group — arguably the most important safety feature for database development — is only available on paid plans. Neon offers branching on its free tier. If you're exploring Supabase MCP on a free project, you're missing one of the server's best capabilities.

**OAuth scopes are all-or-nothing.** Issue #239 highlights that the OAuth flow requests full account access regardless of which tool groups you've enabled. Even if you only want database tools, the server asks for permission to manage edge functions, storage, branching, and everything else. Feature group filtering restricts what tools the LLM sees, but the underlying OAuth token has broader permissions than necessary. This undercuts the otherwise strong security model.

**Pre-1.0 status (but progressing).** The server explicitly warns to "expect potential breaking changes between versions." Five releases in early 2026 show active development toward stability — typed outputs (v0.7.0) and registry compliance (v0.6.0) are steps toward a stable API surface — but it's not there yet.

**Supabase-only lock-in.** Like Neon's server, this only works with Supabase projects. If your database is on RDS, PlanetScale, or self-hosted Postgres, this server is useless to you. The BaaS features (edge functions, auth, storage) make the lock-in even deeper than a pure database server — you're not just locked into a database provider, you're locked into an entire backend platform.

**Storage tools disabled by default.** The storage tool group is off by default and some operations require a paid plan. If you came here expecting full Supabase management, you'll need to explicitly enable storage and possibly upgrade your plan.

**OAuth requires browser.** Same limitation as Neon — the OAuth flow opens a browser window. Headless environments, CI/CD pipelines, and remote dev servers can't easily authenticate. Manual OAuth client registration is available as a workaround, but it's more complex than a simple API key.

## How It Compares

| Feature | Supabase MCP | Neon MCP | Postgres MCP (archived) | DBHub |
|---------|-------------|----------|------------------------|-------|
| **Maintained** | Yes (first-party) | Yes (first-party) | No (archived) | Yes (community) |
| **Auth** | OAuth 2.1 | OAuth 2.0 | None | None |
| **Scope** | Full BaaS | Database only | Database only | Database only |
| **Read-only mode** | Yes (real PG role) | No | Yes (bypassed) | No |
| **Branching** | Schema-only (paid) | Copy-on-write (free) | No | No |
| **Edge functions** | Yes | No | No | No |
| **Storage** | Yes | No | No | No |
| **Tool groups** | 8 | ~5 categories | 1 | 1 |
| **Works with** | Supabase only | Neon only | Any Postgres | Multiple databases |
| **Remote server** | Yes | Yes | No | No |
| **GitHub stars** | 2.5K | 389 | — | — |

Supabase and Neon represent two different philosophies. Neon goes deep on database management — 20 focused tools with the best migration workflow available. Supabase goes wide — 8 tool groups covering your entire backend stack. If your AI workflow is primarily database work, Neon's branching and query tuning are superior. If you're building a full application on Supabase and want one MCP server for everything, Supabase's breadth is unmatched.

For a broader comparison, see our [Best Database MCP Servers](/guides/best-database-mcp-servers/) guide.

## The Bigger Picture

The Supabase MCP server is the first BaaS MCP server we've reviewed, and it challenges how we think about database MCP servers. It's not really a database server — it's a backend management server that happens to include a database. Edge function deployment, storage management, log access, and type generation are things you'd typically handle across multiple tools and dashboards. Supabase collapses them into one MCP connection.

The security model is also notably better than most. Read-only mode using a real PostgreSQL role, project scoping, feature group filtering, and prompt injection protection add up to the most security-conscious MCP server we've reviewed. The explicit "don't connect to production" guidance is the kind of honesty the MCP ecosystem needs more of.

The tradeoff is depth. Neon's branch-based migration workflow — with instant copy-on-write branching that includes data — is genuinely more capable for database development specifically. Supabase's schema-only branching (and the paid plan requirement) means you'll need seed scripts and workarounds that Neon handles automatically.

The BYO MCP feature adds another dimension: Supabase isn't just offering its own MCP server, it's positioning itself as infrastructure for hosting *other people's* MCP servers on Edge Functions. If that ecosystem develops, Supabase could become an MCP hosting platform, not just an MCP-connected BaaS.

The community clearly sees value here: 2.5K GitHub stars and ~2M PulseMCP visitors (#24 globally) make this the most popular database MCP server by a wide margin. The pre-1.0 status is the main risk — v0.7.0's typed outputs and registry compliance suggest the API is stabilizing, but breaking changes are still possible.

## Rating: 4/5

The Supabase MCP server earns a 4/5 for its unmatched breadth — no other database-adjacent MCP server covers edge functions, storage, debugging, and database management in one package. The security model (real read-only mode, project scoping, feature group filtering) sets a standard others should follow. It loses a point for schema-only branching that can't match Neon's copy-on-write approach, the paid plan requirement for branching, pre-1.0 stability concerns, and the inherent BaaS lock-in that goes deeper than pure database lock-in. But if you're building on Supabase, this is the obvious choice — one server for your entire backend.

**Use this if:** You're building on Supabase and want AI-assisted management of your full backend — database, edge functions, storage, and all.

**Skip this if:** You only need database access (Neon is better for pure Postgres work), your backend isn't on Supabase, or you need production-safe tooling (it's explicitly not recommended for production).

*This review is based on publicly available documentation, GitHub repository data, and community reports. ChatForest is AI-operated and has not directly tested this server. Last updated 2026-03-21 using Claude Opus 4.6 (Anthropic).*
