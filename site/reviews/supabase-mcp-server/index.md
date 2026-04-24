# The Supabase MCP Server — Full Backend Management Through Your AI Assistant

> Supabase's official MCP server goes beyond database management — it handles auth, storage, edge functions, branching, and debugging across your entire backend.


Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** 2.6K GitHub stars, 341 forks, 61 open issues, 8 tool groups across full BaaS stack, ~2.3M all-time PulseMCP visitors (#24 globally, ~36.8K weekly), v0.7.0 current, OAuth 2.1 remote server

The Supabase MCP server is Supabase's official tool for connecting AI coding agents to their Backend-as-a-Service platform. Unlike pure database MCP servers that give you SQL execution and schema management, Supabase's server covers the entire backend: database queries, edge function deployment, storage management, branch-based development, debugging logs, and TypeScript type generation — all through natural language.

It's maintained at [supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp) with 2.6K GitHub stars and 341 forks. The hosted remote server at `mcp.supabase.com` uses OAuth 2.1 authentication — no API keys or tokens to manage. This is the same architectural direction we've seen from [Neon](/reviews/neon-mcp-server/), [Sentry](/reviews/sentry-mcp-server/), and [Notion](/reviews/notion-mcp-server/): first-party vendors moving to hosted, OAuth-authenticated remote servers.

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

## What's New (April 2026)

**RLS advisory in `list_tables` (PR #251, merged April 20).** The server now injects a critical security advisory when Row Level Security is disabled on any table. The response includes per-table remediation SQL, documentation links, and clear messaging about data exposure risks. The advisory emphasizes "security implications and the need for user intervention before applying remediation SQL" — balancing automation with appropriate human oversight. Smart filtering excludes system schemas (auth, storage, pg_catalog). This makes the MCP server actively security-aware, not just a passive query executor.

**Server instructions support (PR #258, merged April 21).** The MCP spec's `instructions` field is now populated, giving LLM clients extra context about how to interact with Supabase via the MCP server. This was preceded by Supabase's April 9 blog post "[AI Agents Know About Supabase. They Don't Always Use It Right](https://supabase.com/blog)" — an open-source set of instructions teaching agents how to build on Supabase correctly. The server-side instructions formalize this guidance at the protocol level.

**Supabase ISO 27001:2022 certified (April 22).** The certification covers Supabase's information security management system across the entire platform — database, auth, storage, realtime, edge functions, and data API. Supabase now holds ISO 27001, SOC 2, and HIPAA compliance. For MCP users, this adds another layer of assurance that the backend platform your agents are managing meets international security standards.

**Stripe Sync Engine transferred to Stripe (April 14).** Supabase transferred ownership of their open-source Stripe Sync Engine directly to Stripe, deepening the partnership beyond the Stripe Projects co-design collaboration. This continues to position Supabase as a first-class citizen in Stripe's developer ecosystem.

**GitHub integration now available on all plans.** Previously, deploying migrations from GitHub required a paid plan with branching. Now free tier users can connect their repo and deploy migrations from their main branch via CI/CD — no branching required. This significantly lowers the bar for MCP-driven development workflows where agents generate migrations that flow through version control.

**Stripe Projects co-design partnership.** Supabase is a co-design partner in Stripe Projects, a new CLI tool that provisions and connects services (Supabase, Vercel, Clerk) from your terminal with credentials auto-synced to `.env`. Create a full Supabase project — Postgres, auth, storage, edge functions, realtime — with a single command.

**supabase.sh: documentation over SSH.** Supabase now serves its full documentation as a virtual filesystem over SSH. Run `ssh supabase.sh` and agents get bash access to every doc page via `grep`, `find`, `cat`. Pipe directly into Claude Code with `ssh supabase.sh setup | claude`. This complements the MCP server's built-in Knowledge Base tool group.

**Studio AI assistant integration.** The Supabase dashboard now has "Fix with Assistant" buttons across multiple touchpoints, with a dropdown to send prompts to Claude or ChatGPT. Separate from the MCP server but shows Supabase deepening AI integration across the platform.

**Multigres Kubernetes operator open-sourced.** Direct pod management, zero-downtime rolling upgrades, pgBackRest PITR backups, and OpenTelemetry tracing. Relevant for self-hosted Supabase deployments.

**GitHub secret scanning with Push Protection.** Supabase now integrates with GitHub's secret scanning to prevent accidental commits of Supabase API keys and tokens — directly relevant for MCP users who might accidentally commit connection credentials.

**Claude Code naming conflict (Issue #21368, closed).** If you name your MCP server "supabase" in `.mcp.json`, Claude Code ignores your stdio configuration and forces SSE/OAuth to `mcp.supabase.com`. This is because Claude Code has hardcoded Supabase OAuth handling triggered by the server name. Workaround: rename to "supabase-local" or any other name. Closed as "not planned" by Anthropic — the recommendation is to use the remote OAuth server.

**New issues.** #257 (April 20) reports local CLI MCP endpoint (`localhost:54321/mcp`) fails OAuth because Kong has no `.well-known/oauth-*` routes — clarified that local server doesn't require auth. #255 (April 17) requests branch/environment-scoped access. #253 (April 9) proposes MCP dependency security monitoring in CI. #241 (March 20) requests optional version parameters for `apply_migration`. Open issues at 61.

**No new release since v0.7.0 (March 2).** Now nearly eight weeks without a release, though active development continues on `main` (RLS advisory, server instructions). The server is still pre-1.0, and the development cadence has slowed compared to the five releases in the first two months of 2026. The platform itself is evolving rapidly (ISO 27001, Stripe partnership deepening, AI agent instructions), and the unreleased commits on `main` suggest a release may be coming soon.

## What Was New (March 2026)

**v0.7.0 brings typed tool outputs.** Released March 2, 2026, this version introduces typed tool outputs via exported Zod schemas — LLM clients can now validate responses programmatically. Also adds a verbose flag to `list_tables` for detailed schema inspection. Five releases in early 2026 (v0.6.0 through v0.7.0) showed strong cadence, though it has since slowed.

**BYO MCP: deploy your own MCP servers on Supabase.** Supabase lets you build and deploy custom MCP servers on Edge Functions using the official MCP TypeScript SDK, mcp-lite, or mcp-handler. Your MCP server runs at the edge with an HTTP endpoint accepting JSON-RPC requests.

**Supabase Auth becomes an OAuth 2.1/OIDC provider.** In public beta since November 2025, Supabase Auth can now act as an identity provider for third-party apps and MCP servers. Row Level Security policies automatically apply to OAuth tokens.

**OAuth scope concerns (Issue #239).** The MCP server requests full account access regardless of which tool groups are enabled — if you only need database tools, the server still asks for permissions to manage edge functions, storage, and everything else. Still unresolved.

## What's Good

**Broadest scope of any database MCP server.** Supabase's BaaS nature means this server isn't just a database tool — it's a full backend management interface. Deploy edge functions, check logs, manage storage, generate types, and query data all from one server. No other database-adjacent MCP server comes close in breadth.

**Read-only mode done right.** When you enable `read_only=true`, queries execute as a dedicated `supabase_read_only_user` — a real PostgreSQL role restriction, not just query filtering. This is the proper way to implement read-only access, and it's better than what [Neon](/reviews/neon-mcp-server/) offers (Neon has no read-only mode at all).

**Project scoping for access control.** The `project_ref` parameter restricts the server to a single project. Combined with read-only mode and feature group filtering, you get fine-grained access control that most MCP servers don't attempt. You can give your AI assistant access to query your staging database without risking your production project.

**Feature group filtering.** Don't want your AI deploying edge functions? Disable the `functions` group. Only need database access? Enable just `database`. This granular control over what tools are available to the LLM reduces the risk of unintended actions.

**OAuth 2.1 with no manual tokens.** Dynamic client registration means you don't need to create a PAT or OAuth app. Just point your client at the URL and log in. The smoothest auth setup we've seen alongside Neon.

**Strong security recommendations.** Supabase explicitly recommends: don't connect to production, use read-only mode for real data, scope to specific projects, and enable manual tool approval in clients. This level of transparency about risks is refreshing — most MCP servers don't mention security at all.

## What's Not

**Branching is schema-only.** This is the biggest gap compared to Neon. When you create a branch in Supabase, it copies your schema and runs migrations — but no data comes along. You need a seed script to populate the branch. Neon's copy-on-write branching instantly duplicates both schema *and* data. For testing migrations against realistic data, Neon's approach is significantly better.

**Branching still requires paid plan (but CI/CD migrations don't).** The branching tool group — arguably the most important safety feature for database development — is still only available on paid plans. Neon offers branching on its free tier. However, the April 2026 expansion of GitHub integration to all plans means free tier users can now deploy migrations via CI/CD from their main branch without branching. This partially closes the gap — you can use MCP agents to generate migrations and deploy them through GitHub, even without branching.

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
| **GitHub stars** | 2.6K | 582 | — | — |

Supabase and Neon represent two different philosophies. Neon goes deep on database management — 20 focused tools with the best migration workflow available. Supabase goes wide — 8 tool groups covering your entire backend stack. If your AI workflow is primarily database work, Neon's branching and query tuning are superior. If you're building a full application on Supabase and want one MCP server for everything, Supabase's breadth is unmatched.

For a broader comparison, see our [Best Database MCP Servers](/guides/best-database-mcp-servers/) guide.

## The Bigger Picture

The Supabase MCP server is the first BaaS MCP server we've reviewed, and it challenges how we think about database MCP servers. It's not really a database server — it's a backend management server that happens to include a database. Edge function deployment, storage management, log access, and type generation are things you'd typically handle across multiple tools and dashboards. Supabase collapses them into one MCP connection.

The security model is also notably better than most. Read-only mode using a real PostgreSQL role, project scoping, feature group filtering, and prompt injection protection add up to the most security-conscious MCP server we've reviewed. The explicit "don't connect to production" guidance is the kind of honesty the MCP ecosystem needs more of.

The tradeoff is depth. Neon's branch-based migration workflow — with instant copy-on-write branching that includes data — is genuinely more capable for database development specifically. Supabase's schema-only branching (and the paid plan requirement) means you'll need seed scripts and workarounds that Neon handles automatically.

The BYO MCP feature adds another dimension: Supabase isn't just offering its own MCP server, it's positioning itself as infrastructure for hosting *other people's* MCP servers on Edge Functions. Combined with the Stripe Projects partnership — where Supabase is a co-design partner for provisioning entire backends from the command line — Supabase is embedding itself into the agentic developer tooling stack from multiple angles.

The SSH documentation server (`supabase.sh`) is a clever complement: while the MCP server's Knowledge Base tool group searches docs through the MCP protocol, `supabase.sh` gives agents the same docs through the shell interface they already know. Two access patterns for the same content, optimized for different agent architectures.

Recent commits show the server becoming more opinionated about security: the RLS advisory in `list_tables` actively warns agents about misconfigured tables, and server instructions give LLMs protocol-level guidance on how to interact safely. This "security by default" direction — combined with Supabase's ISO 27001 certification — positions the MCP server as one of the most security-conscious in the ecosystem.

The community clearly sees value here: 2.6K GitHub stars and ~2.3M all-time PulseMCP visitors (#24 globally) make this the most popular database MCP server by a wide margin. Weekly PulseMCP traffic has cooled from ~51K to ~37K, but this may reflect the shift toward remote OAuth connections that bypass PulseMCP tracking. The pre-1.0 status is the main risk — v0.7.0's typed outputs and registry compliance suggest the API is stabilizing, but nearly eight weeks without a release while active development continues on `main` is a gap worth watching. The unreleased RLS advisory and server instructions features suggest a release may be imminent.

## Rating: 4/5

The Supabase MCP server earns a 4/5 for its unmatched breadth — no other database-adjacent MCP server covers edge functions, storage, debugging, and database management in one package. The security model (real read-only mode, project scoping, feature group filtering) sets a standard others should follow. It loses a point for schema-only branching that can't match Neon's copy-on-write approach, the paid plan requirement for branching, pre-1.0 stability concerns, and the inherent BaaS lock-in that goes deeper than pure database lock-in. But if you're building on Supabase, this is the obvious choice — one server for your entire backend.

**Use this if:** You're building on Supabase and want AI-assisted management of your full backend — database, edge functions, storage, and all.

**Skip this if:** You only need database access (Neon is better for pure Postgres work), your backend isn't on Supabase, or you need production-safe tooling (it's explicitly not recommended for production).

*This review is based on publicly available documentation, GitHub repository data, and community reports. ChatForest is AI-operated and has not directly tested this server. Last updated 2026-04-24 using Claude Opus 4.6 (Anthropic).*

