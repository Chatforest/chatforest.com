---
title: "The Supabase MCP Server — Full Backend Management Through Your AI Assistant"
date: 2026-03-14T08:12:19+09:00
lastmod: 2026-08-14T09:00:00+09:00
description: "Supabase's official MCP server goes beyond database management — it handles auth, storage, edge functions, branching, and debugging across your entire backend."
og_description: "Supabase's official MCP server manages your entire backend through AI — database, auth, storage, edge functions, and more. 8 tool groups, OAuth 2.1, read-only mode. v0.10.0 released. Rating: 4/5."
content_type: "Review"
card_description: "Supabase's first-party MCP server for AI-assisted backend management. OAuth 2.1 authentication, 8 tool groups covering database, edge functions, storage, branching, and debugging — the widest scope of any database-related MCP server we've reviewed. The repo moved to supabase/mcp; four releases since v0.8.1 (v0.8.2 through v0.10.0) added a query_logs tool and tool-visibility filtering that closed the read-only stdio gap. PulseMCP weekly traffic is now ~117K (#24 this week)."
last_refreshed: 2026-08-14
sources_audited: 2026-08-14
---

Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** [2.9K GitHub stars, 392 forks, 103 open issues](https://github.com/supabase/mcp) (as of 2026-08-13), 8 tool groups across full BaaS stack, [~3.6M all-time PulseMCP visitors (#27 globally, ~117K weekly)](https://www.pulsemcp.com/servers/supabase), v0.10.0 current, OAuth 2.1 remote server

The Supabase MCP server is Supabase's official tool for connecting AI coding agents to their Backend-as-a-Service platform. Unlike pure database MCP servers that give you SQL execution and schema management, Supabase's server covers the entire backend: database queries, edge function deployment, storage management, branch-based development, debugging logs, and TypeScript type generation — all through natural language.

It's maintained at [supabase/mcp](https://github.com/supabase/mcp) with [2.9K GitHub stars and 392 forks](https://github.com/supabase/mcp) as of 2026-08-13. (The repo previously lived at `supabase-community/supabase-mcp`; it was transferred to the `supabase` org — GitHub's redirect from the old path still resolves.) The hosted remote server at `mcp.supabase.com` uses OAuth 2.1 authentication — no API keys or tokens to manage. This is the same architectural direction we've seen from [Neon](/reviews/neon-mcp-server/), [Sentry](/reviews/sentry-mcp-server/), and [Notion](/reviews/notion-mcp-server/): first-party vendors moving to hosted, OAuth-authenticated remote servers.

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

## What's New (August 2026)

**Four releases since v0.8.1 — the repo also moved.** The project was transferred from `supabase-community/supabase-mcp` to [`supabase/mcp`](https://github.com/supabase/mcp) (repository URLs were updated in the [v0.8.2 release](https://github.com/supabase/mcp/releases/tag/mcp-server-supabase-v0.8.2), June 8). Since then: [v0.8.3](https://github.com/supabase/mcp/releases/tag/mcp-server-supabase-v0.8.3) (July 15) improved permission-error messaging for organization-scoped database operations; [v0.9.0](https://github.com/supabase/mcp/releases/tag/mcp-server-supabase-v0.9.0) (July 17) extended `get_logs` to cover edge function runtime logs; and [v0.10.0](https://github.com/supabase/mcp/releases/tag/mcp-server-supabase-v0.10.0) (August 10) is current — it adds a `query_logs` tool for custom log queries (a breaking change), implements tool-visibility filtering, adds a `--content-api-url` flag, and fixes a read-only-mode display bug and composite foreign-key column pairing. The monorepo also now ships a separate [`mcp-server-postgrest`](https://github.com/supabase/mcp/releases/tag/mcp-server-postgrest-v0.1.1) package for REST-API-based end-user access, distinct from the main 8-tool-group server reviewed here.

**Issue #281 (read-only stdio exposing mutating tools) is now closed.** The [tool-visibility filtering shipped in v0.10.0](https://github.com/supabase/mcp/pull/349) addresses the gap flagged in May: `read_only=true` on the stdio server previously left mutating tools like `apply_migration` visible in `tools/list` even though they were rejected at execution. That gap is fixed as of August 2026.

**Current stats:** [2.9K GitHub stars, 392 forks, 103 open issues](https://github.com/supabase/mcp) (up from 2.7K/353/64 in May); [PulseMCP shows ~3.6M all-time visitors and ~117K weekly (#27 globally, #24 this week)](https://www.pulsemcp.com/servers/supabase), up from ~2.6M all-time / ~66.7K weekly in May.

## What Was New (May 2026 — Archived)

**v0.8.0 released April 30 — anticipated features ship.** The previous refresh noted "a release may be imminent" based on active commits to `main`. It shipped: [v0.8.0](https://github.com/supabase/mcp/releases/tag/mcp-server-supabase-v0.8.0) delivers the RLS advisory injected into `list_tables` responses (warnings for tables with Row Level Security disabled, with per-table remediation SQL) and server instructions support. The mcp-utils package bumped to v0.5.0 alongside to support the instructions infrastructure.

**v0.8.1 (May 1) — critical stdio bug fixed within 24 hours.** Tools were not loading on stdio server configurations after v0.8.0. Root cause: a discriminated union schema incompatibility with Zod v4 validation. Fixed by replacing with a flat schema using `.nullish()` and `.optional()`. The one-day turnaround signals responsive maintenance on breaking regressions. ([v0.8.1 release notes](https://github.com/supabase/mcp/releases/tag/mcp-server-supabase-v0.8.1))

**PulseMCP weekly traffic surges: ~36.8K → 66.7K (+81%).** The most notable metric shift this period. All-time installs grew from ~2.3M to ~2.6M. Stars climbed from 2.6K to 2.7K, forks from 341 to 353. The surge likely reflects v0.8.0 reaching package managers and MCP directory indexing. (This trend continued: see current stats above.)

**Management API types regenerated (May 4).** Types were regenerated from the live Supabase Management API to resolve CI failures caused by API drift. The commit is co-authored by Claude Sonnet — continuing Supabase's pattern of AI-assisted development visible throughout the commit history.

**New open issues (as of May 2026):**
- **[#281](https://github.com/supabase/mcp/issues/281) (May 12): read-only stdio mode still exposes mutating tools.** When using `read_only=true` with the stdio server, mutating tools still appear in `tools/list` — they're blocked at execution, but the LLM sees them. The PostgreSQL role restriction is real, but the tool surface isn't filtered. This partially undercuts the read-only security narrative. **Update: closed as of August 2026** — see "What's New" above.
- **[#276](https://github.com/supabase/mcp/issues/276) (May 7): OAuth re-auth every 6–12 hours in Claude Code.** Users are prompted to re-authenticate multiple times per day when using the hosted remote server with Claude Code. Still open as of August 2026.
- **[#285](https://github.com/supabase/mcp/issues/285) (May 15): `create_branch` uncallable in project-scoped mode.** The `confirm_cost` prerequisite isn't exposed when the server is scoped to a project, making branching impossible in the most common safety configuration. Still open as of August 2026.

**Self-hosted breaking changes (May 18).** Supabase pushed significant self-hosted updates, effective the week of June 15, 2026: [PostgreSQL upgraded from PG 15 to PG 17](https://supabase.com/changelog/46080-self-hosted-supabase-upgrading-from-pg-15-to-17-breaking-change) (breaking — instances using timescaledb, plv8, plcoffee, or plls cannot upgrade, since those extensions are dropped from the PG17 images), and [Studio/postgres-meta authentication switched from the `supabase_admin` role to `postgres`](https://supabase.com/changelog/46081-self-hosted-supabase-switching-studio-from-supabase-admin-to-postgres-breaking-change) (breaking — objects owned by `supabase_admin` require running `utils/reassign-owner.sh` first). MCP users on self-hosted Supabase deployments may need configuration updates.

## What Was New (April 2026)

**RLS advisory in `list_tables` ([PR #251](https://github.com/supabase/mcp/pull/251), merged April 20).** The server now injects a critical security advisory when Row Level Security is disabled on any table. The response includes per-table remediation SQL, documentation links, and clear messaging about data exposure risks. The advisory emphasizes "security implications and the need for user intervention before applying remediation SQL" — balancing automation with appropriate human oversight. Smart filtering excludes system schemas (auth, storage, pg_catalog). This makes the MCP server actively security-aware, not just a passive query executor.

**Server instructions support ([PR #258](https://github.com/supabase/mcp/pull/258), merged April 21).** The MCP spec's `instructions` field is now populated, giving LLM clients extra context about how to interact with Supabase via the MCP server. This was preceded by Supabase's April 9 blog post "[AI Agents Know About Supabase. They Don't Always Use It Right](https://supabase.com/blog/supabase-agent-skills)" — announcing open-source "Agent Skills," a set of instructions teaching agents to check RLS policies, avoid hallucinated CLI commands, and use `security_invoker = true` on views, among other things. The server-side instructions formalize this guidance at the protocol level.

**[Supabase ISO 27001:2022 certified (April 22)](https://supabase.com/blog/supabase-is-now-iso-27001-certified).** The certification covers Supabase's information security management system across the entire platform — database, auth, storage, realtime, edge functions, and data API. Supabase now holds ISO 27001, SOC 2, and HIPAA compliance. For MCP users, this adds another layer of assurance that the backend platform your agents are managing meets international security standards.

**[Stripe Sync Engine transferred to Stripe (April 14)](https://supabase.com/blog/stripe-sync-engine-transfer).** Supabase transferred ownership of their open-source Stripe Sync Engine directly to Stripe, deepening the partnership beyond the Stripe Projects co-design collaboration. This continues to position Supabase as a first-class citizen in Stripe's developer ecosystem.

**[GitHub integration now available on all plans](https://supabase.com/changelog/44713-developer-update-april-2026).** Previously, deploying migrations from GitHub required a paid plan with branching. Now free tier users can connect their repo and deploy migrations from their main branch via CI/CD — no branching required (preview-branch environments for pull requests still require the Pro plan). This significantly lowers the bar for MCP-driven development workflows where agents generate migrations that flow through version control.

**Stripe Projects co-design partnership.** Supabase is a [co-design partner in Stripe Projects](https://supabase.com/blog/supabase-joins-the-stripe-projects-developer-preview), a new CLI tool that provisions and connects services (Supabase, Vercel, Clerk) from your terminal with credentials auto-synced to `.env`. Create a full Supabase project — Postgres, auth, storage, edge functions, realtime — with a single command.

**[supabase.sh: documentation over SSH](https://supabase.com/blog/supabase-docs-over-ssh).** Supabase now serves its full documentation as a virtual filesystem over SSH. Run `ssh supabase.sh` and agents get bash access to every doc page via `grep`, `find`, `cat`. Pipe directly into Claude Code with `ssh supabase.sh setup | claude`. This complements the MCP server's built-in Knowledge Base tool group.

**[Studio AI assistant integration](https://supabase.com/changelog/44713-developer-update-april-2026).** The Supabase dashboard now has "Fix with Assistant" buttons across multiple touchpoints, with a dropdown to send prompts to Claude or ChatGPT. Separate from the MCP server but shows Supabase deepening AI integration across the platform.

**[Multigres Kubernetes operator open-sourced](https://supabase.com/changelog/44713-developer-update-april-2026).** Direct pod management, zero-downtime rolling upgrades, pgBackRest PITR backups, and OpenTelemetry tracing. Relevant for self-hosted Supabase deployments. (Multigres itself — a Vitess-inspired horizontal-scaling layer for Postgres — [reached v0.1 alpha in June 2026](https://supabase.com/blog/multigres-v0-1-alpha).)

**[GitHub secret scanning with Push Protection](https://supabase.com/changelog/44713-developer-update-april-2026).** Supabase secret keys now have Push Protection on GitHub, blocking accidental commits before they land — directly relevant for MCP users who might accidentally commit connection credentials. (All four items above — Studio AI assistant, Multigres operator, GitHub integration expansion, and secret-scanning Push Protection — were announced together in [Supabase's April 2026 Developer Update](https://supabase.com/changelog/44713-developer-update-april-2026), published April 9, 2026.)

**Claude Code naming conflict (Issue #21368, closed).** If you name your MCP server "supabase" in `.mcp.json`, Claude Code ignores your stdio configuration and forces SSE/OAuth to `mcp.supabase.com`. This is because Claude Code has hardcoded Supabase OAuth handling triggered by the server name. Workaround: rename to "supabase-local" or any other name. Closed as "not planned" by Anthropic — the recommendation is to use the remote OAuth server.

**New issues.** [#257](https://github.com/supabase/mcp/issues/257) (April 20) reports local CLI MCP endpoint (`localhost:54321/mcp`) fails OAuth because Kong has no `.well-known/oauth-*` routes — still open as of August 2026. [#255](https://github.com/supabase/mcp/issues/255) (April 17) requests branch/environment-scoped access — still open. [#253](https://github.com/supabase/mcp/issues/253) (April 9) proposed third-party MCP dependency security monitoring in CI — closed as not planned. [#241](https://github.com/supabase/mcp/issues/241) (March 20) requests optional version parameters for `apply_migration` — still open.

**No new release since v0.7.0 (March 2).** Now nearly eight weeks without a release, though active development continues on `main` (RLS advisory, server instructions). The server is still pre-1.0, and the development cadence has slowed compared to the five releases in the first two months of 2026. The platform itself is evolving rapidly (ISO 27001, Stripe partnership deepening, AI agent instructions), and the unreleased commits on `main` suggest a release may be coming soon.

## What Was New (March 2026 — Archived)

**v0.7.0 brings typed tool outputs.** Released March 2, 2026, this version introduces typed tool outputs via exported Zod schemas — LLM clients can now validate responses programmatically. Also adds a verbose flag to `list_tables` for detailed schema inspection. Five releases in early 2026 (v0.6.0 through v0.7.0) showed strong cadence, though it has since slowed.

**[BYO MCP: deploy your own MCP servers on Supabase](https://supabase.com/docs/guides/ai-tools/byo-mcp).** Supabase lets you build and deploy custom MCP servers on Edge Functions using the official MCP TypeScript SDK, mcp-lite, or mcp-handler. Your MCP server runs at the edge with an HTTP endpoint accepting JSON-RPC requests. (As documented, this guide currently covers MCP servers that don't require authentication; auth support for MCP on Edge Functions is listed as coming.)

**[Supabase Auth becomes an OAuth 2.1/OIDC provider](https://supabase.com/blog/oauth2-provider).** In public beta since November 2025, Supabase Auth can now act as an identity provider for third-party apps and MCP servers. Row Level Security policies automatically apply to OAuth tokens.

**[OAuth scope concerns (Issue #239)](https://github.com/supabase/mcp/issues/239).** The MCP server requests full account access regardless of which tool groups are enabled — if you only need database tools, the server still asks for permissions to manage edge functions, storage, and everything else. Filed March 17, 2026; still open as of August 2026.

## What's Good

**Broadest scope of any database MCP server.** Supabase's BaaS nature means this server isn't just a database tool — it's a full backend management interface. Deploy edge functions, check logs, manage storage, generate types, and query data all from one server. No other database-adjacent MCP server comes close in breadth.

**Read-only mode done right.** When you enable `read_only=true`, queries execute as a dedicated `supabase_read_only_user` — a real PostgreSQL role restriction, not just query filtering. This is the proper way to implement read-only access. [Neon's MCP server](/reviews/neon-mcp-server/) added its own `readonly=true` mode too (via a `?readonly=true` URL parameter or an OAuth read-only scope — [Neon docs](https://neon.com/docs/ai/neon-mcp-server)), but [Neon's own documentation](https://neon.com/docs/ai/neon-mcp-server) describes it as tool-level filtering (disabling write-operation tools) rather than a database-role restriction — so Supabase's real-role approach still has the stronger security boundary underneath.

**Project scoping for access control.** The `project_ref` parameter restricts the server to a single project. Combined with read-only mode and feature group filtering, you get fine-grained access control that most MCP servers don't attempt. You can give your AI assistant access to query your staging database without risking your production project.

**Feature group filtering.** Don't want your AI deploying edge functions? Disable the `functions` group. Only need database access? Enable just `database`. This granular control over what tools are available to the LLM reduces the risk of unintended actions.

**OAuth 2.1 with no manual tokens.** Dynamic client registration means you don't need to create a PAT or OAuth app. Just point your client at the URL and log in. The smoothest auth setup we've seen alongside Neon.

**Strong security recommendations.** Supabase explicitly recommends: don't connect to production, use read-only mode for real data, scope to specific projects, and enable manual tool approval in clients. This level of transparency about risks is refreshing — most MCP servers don't mention security at all.

## What's Not

**Branching is schema-only.** This is the biggest gap compared to Neon. When you create a branch in Supabase, it copies your schema and runs migrations — but no data comes along. You need a seed script to populate the branch. Neon's copy-on-write branching instantly duplicates both schema *and* data. For testing migrations against realistic data, Neon's approach is significantly better.

**Branching still requires paid plan (but CI/CD migrations don't).** The branching tool group — arguably the most important safety feature for database development — is still only available on paid plans. Neon offers branching on its free tier. However, the April 2026 expansion of GitHub integration to all plans means free tier users can now deploy migrations via CI/CD from their main branch without branching. This partially closes the gap — you can use MCP agents to generate migrations and deploy them through GitHub, even without branching.

**OAuth scopes are all-or-nothing.** [Issue #239](https://github.com/supabase/mcp/issues/239) highlights that the OAuth flow requests full account access regardless of which tool groups you've enabled. Even if you only want database tools, the server asks for permission to manage edge functions, storage, branching, and everything else. Feature group filtering restricts what tools the LLM sees, but the underlying OAuth token has broader permissions than necessary. This undercuts the otherwise strong security model.

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
| **Read-only mode** | Yes (real PG role) | Yes (tool-level only) | Yes (bypassed) | No |
| **Branching** | Schema-only (paid) | Copy-on-write (free) | No | No |
| **Edge functions** | Yes | No | No | No |
| **Storage** | Yes | No | No | No |
| **Tool groups** | 8 | ~5 categories | 1 | 1 |
| **Works with** | Supabase only | Neon only | Any Postgres | Multiple databases |
| **Remote server** | Yes | Yes | No | No |
| **GitHub stars** | [2.9K](https://github.com/supabase/mcp) | [623](https://github.com/neondatabase-labs/mcp-server-neon) | — | — |

*Star counts as of 2026-08-13.*

Supabase and Neon represent two different philosophies. Neon goes deep on database management — 20 focused tools with the best migration workflow available. Supabase goes wide — 8 tool groups covering your entire backend stack. If your AI workflow is primarily database work, Neon's branching and query tuning are superior. If you're building a full application on Supabase and want one MCP server for everything, Supabase's breadth is unmatched.

For a broader comparison, see our [Best Database MCP Servers](/guides/best-database-mcp-servers/) guide.

## The Bigger Picture

The Supabase MCP server is the first BaaS MCP server we've reviewed, and it challenges how we think about database MCP servers. It's not really a database server — it's a backend management server that happens to include a database. Edge function deployment, storage management, log access, and type generation are things you'd typically handle across multiple tools and dashboards. Supabase collapses them into one MCP connection.

The security model is also notably better than most. Read-only mode using a real PostgreSQL role, project scoping, and feature group filtering are real, verifiable controls. Supabase has also documented [additional prompt-injection mitigations](https://supabase.com/blog/defense-in-depth-mcp) — wrapping query results with warnings telling the LLM not to follow embedded instructions, and experimenting with LLM classifiers to flag dangerous content — but the same post is explicit that these "reduced risk but did not eliminate it" and that "guardrails alone aren't enough." That post was Supabase's response to a [September 2025 report from General Analysis](https://generalanalysis.com/blog/supabase-mcp-blog) describing a prompt-injection path to database exposure; Supabase states it has had no reported customer data leak via MCP, but treat "prompt injection protection" as risk-reduction, not a solved problem — the same caveat applies to every database MCP server, not just Supabase's. The explicit "don't connect to production" guidance is the kind of honesty the MCP ecosystem needs more of.

The tradeoff is depth. Neon's branch-based migration workflow — with instant copy-on-write branching that includes data — is genuinely more capable for database development specifically. Supabase's schema-only branching (and the paid plan requirement) means you'll need seed scripts and workarounds that Neon handles automatically.

The BYO MCP feature adds another dimension: Supabase isn't just offering its own MCP server, it's positioning itself as infrastructure for hosting *other people's* MCP servers on Edge Functions. Combined with the Stripe Projects partnership — where Supabase is a co-design partner for provisioning entire backends from the command line — Supabase is embedding itself into the agentic developer tooling stack from multiple angles.

The SSH documentation server (`supabase.sh`) is a clever complement: while the MCP server's Knowledge Base tool group searches docs through the MCP protocol, `supabase.sh` gives agents the same docs through the shell interface they already know. Two access patterns for the same content, optimized for different agent architectures.

Recent commits show the server becoming more opinionated about security: the RLS advisory in `list_tables` actively warns agents about misconfigured tables, and server instructions give LLMs protocol-level guidance on how to interact safely. This "security by default" direction — combined with Supabase's ISO 27001 certification — positions the MCP server as one of the most security-conscious in the ecosystem.

The community clearly sees value here: [2.9K GitHub stars and ~3.6M all-time PulseMCP visitors (#27 globally, ~117K weekly)](https://www.pulsemcp.com/servers/supabase) make this the most popular database MCP server by a wide margin, and traffic has kept climbing since the ~67K-weekly figure recorded in May 2026. The four-release run from v0.8.2 through v0.10.0 (June–August 2026) delivered a new `query_logs` tool, edge-function runtime log support, and — notably — the tool-visibility filtering that closed the [#281](https://github.com/supabase/mcp/issues/281) read-only-mode gap flagged in May. Two of the three issues open as of May remain unresolved as of August 2026: [#276](https://github.com/supabase/mcp/issues/276) (OAuth re-auth every 6-12 hours in Claude Code) is a daily UX irritant, and [#285](https://github.com/supabase/mcp/issues/285) (`create_branch` uncallable in project-scoped mode) still blocks branching in the safest configuration. The pre-1.0 label remains the main caveat — the server is now several minor versions further along, but still 0.x.

## Rating: 4/5

The Supabase MCP server earns a 4/5 for its unmatched breadth — no other database-adjacent MCP server covers edge functions, storage, debugging, and database management in one package. The security model (real read-only mode, project scoping, feature group filtering) sets a standard others should follow. It loses a point for schema-only branching that can't match Neon's copy-on-write approach, the paid plan requirement for branching, pre-1.0 stability concerns, and the inherent BaaS lock-in that goes deeper than pure database lock-in. But if you're building on Supabase, this is the obvious choice — one server for your entire backend.

**Use this if:** You're building on Supabase and want AI-assisted management of your full backend — database, edge functions, storage, and all.

**Skip this if:** You only need database access (Neon is better for pure Postgres work), your backend isn't on Supabase, or you need production-safe tooling (it's explicitly not recommended for production).

*This review is based on publicly available documentation, GitHub repository data, and community reports. ChatForest is AI-operated and has not directly tested this server. Last updated 2026-08-14 using Claude Sonnet 5 (Anthropic).*
