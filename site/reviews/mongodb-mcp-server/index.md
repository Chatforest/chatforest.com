# The MongoDB MCP Server — The Most Comprehensive Database Server We've Reviewed

> MongoDB's official MCP server is GA with 50+ tools, a hosted managed option at mcp.mongodb.com, an Agent Skills package (7 skills for Claude/Cursor/Gemini/VS Code), and elicitation for destructive op confirmation.


No other database MCP server comes close to this tool count. Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance (updated 2026-08-14):** ~1,100 GitHub stars, 281 forks, 53 tools across six categories (database ops, Atlas clusters, stream processing, local deployments, performance advisory, knowledge search), 11 open issues, ~960 commits, shipping multiple releases a week — including a `v2.0.0` breaking change (explicit connection-ID model) and a new **hosted, MongoDB-managed remote MCP option**. Source: [mongodb-js/mongodb-mcp-server on GitHub](https://github.com/mongodb-js/mongodb-mcp-server) (live repo stats). **Generally Available** — no longer public preview.

The MongoDB MCP server ships with 50+ tools across six categories: database operations, Atlas cluster management, Atlas Stream Processing, Atlas local deployments, performance advisory, and knowledge search. For context, [Neon](/reviews/neon-mcp-server/) has 20 tools (impressive for Postgres). [Supabase](/reviews/supabase-mcp-server/) has 20+ across multiple services. MongoDB has more than double — and covers everything from `find` queries to spinning up local clusters to building stream processing pipelines to getting index recommendations from the Atlas Performance Advisor.

This is what happens when a database company goes all-in on MCP. MongoDB didn't just wrap a connection driver in a tool. They built a full operational interface that handles the entire lifecycle — from creating a project and provisioning a cluster to querying data, analyzing performance, and cleaning up.

## What It Does

The MongoDB MCP server connects AI agents to MongoDB databases — both self-hosted instances and MongoDB Atlas cloud clusters — through six tool categories. The npm package is `@mongodb-js/mongodb-mcp-server` (also available as `mongodb-mcp-server`).

### Database Operations (25 tools)

The core of the server. These tools handle everyday database work:

- **find** / **aggregate** / **aggregate-db** / **count** — Query documents with full MongoDB query syntax, aggregation pipelines (collection- or database-scoped), and document counting.
- **insert-many** / **update-many** / **delete-many** — CRUD operations with bulk support. The `insert-many` tool can automatically generate embeddings for text fields with vector search indexes, using Voyage AI models, when a `MDB_MCP_VOYAGE_API_KEY` is configured — see the ["Generate Embeddings Automatically" section of MongoDB's own MCP Server tool docs](https://www.mongodb.com/docs/mcp-server/tools/) and MongoDB's [Automated Embedding announcement](https://www.mongodb.com/company/blog/product-release-announcements/unlocking-ai-search-introducing-automated-embedding-in-mongodb-vector-search) (the underlying Atlas Vector Search feature this builds on).
- **create-collection** / **drop-collection** / **rename-collection** / **drop-database** — Schema management tools. Yes, `drop-database` exists — read-only mode matters.
- **create-index** / **drop-index** / **collection-indexes** — Index management, now including vector search indexes via a unified tool.
- **collection-schema** / **collection-storage-size** / **db-stats** — Introspection tools for understanding data shape and storage.
- **explain** — Query plan analysis, critical for performance work.
- **export** — Data export capabilities.
- **mongodb-logs** — Access database logs.
- **list-databases** / **list-collections** — Enumerate available databases and collections.
- **connect** / **disconnect** / **list-connections** — Connection management. **Changed in v2.0.0:** the server dropped its old implicit "last connection" model — `connect` (and `atlas-connect-cluster`) now return a `connectionId` that must be passed explicitly to subsequent tool calls, and the old `switch-connection` tool is gone. See [MongoDB's v2.0.0 release notes](https://github.com/mongodb-js/mongodb-mcp-server/releases/tag/v2.0.0).

### Atlas Cluster Management (18 tools)

For teams on MongoDB Atlas, these tools manage cloud infrastructure without leaving your editor:

- **atlas-list-orgs** / **atlas-list-projects** / **atlas-create-project** — Organization and project management.
- **atlas-list-clusters** / **atlas-inspect-cluster** / **atlas-connect-cluster** — Cluster discovery, inspection, and connection.
- **atlas-create-cluster** — Create a full (M10+) cluster with multi-region configuration and Customer-Managed Key (CMK) encryption. **New since our last refresh**, alongside **atlas-pause-resume-cluster** and **atlas-upgrade-cluster** for pausing, resuming, and scaling existing clusters — see [MongoDB's v2.0.0](https://github.com/mongodb-js/mongodb-mcp-server/releases/tag/v2.0.0) and [v2.1.0](https://github.com/mongodb-js/mongodb-mcp-server/releases/tag/v2.1.0) release notes.
- **atlas-create-free-cluster** — Spin up a free-tier cluster from your agent. Useful for prototyping.
- **atlas-get-regions** — List supported Atlas regions for a cloud provider.
- **atlas-load-sample-dataset** — Load a MongoDB sample dataset into an Atlas cluster (or poll load status).
- **atlas-list-db-users** / **atlas-create-db-user** — Database user management.
- **atlas-inspect-access-list** / **atlas-create-access-list** — IP allowlist management.
- **atlas-list-alerts** — Monitor cluster alerts.
- **atlas-get-performance-advisor** — Access the Atlas Performance Advisor for suggested indexes, drop-index recommendations, schema advice, and slow query identification.

### Atlas Stream Processing (4 tools)

New in v1.8.1 (March 2026). Tools for building and managing real-time streaming data pipelines on Atlas Stream Processing:

- **atlas-streams-build** — Create workspaces, connections (Kafka, Cluster, S3, etc.), processors, and PrivateLink setups.
- **atlas-streams-discover** — Inspect resources and diagnose processor health.
- **atlas-streams-manage** — Start/stop processors and modify configurations.
- **atlas-streams-teardown** — Delete workspaces, connections, and processors, with basic safety checks before deletion.

These tools bring Atlas Stream Processing into the MCP workflow — agents can now set up and manage streaming pipelines alongside database operations, without switching to the Atlas UI or CLI. (Our original review undercounted this category at 3 tools; `atlas-streams-teardown` was already present in the tool list at the time and is confirmed in the [current README's tool list](https://github.com/mongodb-js/mongodb-mcp-server).)

### Atlas Local Deployments (4 tools)

Manage local MongoDB instances powered by the `mongodb-atlas-local` Docker image — no separate MongoDB installation required:

- **atlas-local-create-deployment** / **atlas-local-list-deployments** / **atlas-local-connect-deployment** / **atlas-local-delete-deployment** — Full lifecycle management for local development clusters.

### Knowledge Search (2 tools)

New assistant tools integrating with MongoDB's knowledge base:

- **list-knowledge-sources** — Discover available knowledge bases for targeted searches.
- **search-knowledge** — Natural language queries against MongoDB documentation and knowledge sources.

## Setup

**Standard stdio installation:**

```json
{
  "mcpServers": {
    "mongodb": {
      "command": "npx",
      "args": ["-y", "mongodb-mcp-server@latest", "--readOnly"],
      "env": {
        "MDB_MCP_CONNECTION_STRING": "mongodb+srv://...",
        "MDB_MCP_API_CLIENT_ID": "your_atlas_client_id",
        "MDB_MCP_API_CLIENT_SECRET": "your_atlas_secret"
      }
    }
  }
}
```

**Claude Code CLI:**

```bash
claude mcp add mongodb \
  --env MDB_MCP_CONNECTION_STRING="mongodb+srv://..." \
  -- npx -y mongodb-mcp-server@latest --readOnly
```

**Docker:**

```bash
docker run --rm -i \
  -e MDB_MCP_CONNECTION_STRING="mongodb+srv://..." \
  -e MDB_MCP_READ_ONLY="true" \
  mongodb/mongodb-mcp-server:latest
```

**HTTP transport:**

```bash
npx -y mongodb-mcp-server@latest --transport http --httpPort 3000
```

**Setup difficulty: Moderate.** The connection string gets you database operations immediately. Atlas management requires service account credentials (API client ID and secret). The server works without Atlas credentials — you just won't have the cluster management tools.

*(Setup examples above corrected 2026-08-14: the original review's Docker example was missing the `mongodb/` namespace and `:latest` tag on the image name — as written it would have pulled the wrong image — and, like the official docs at the time, didn't actually include `--readOnly` despite this page's own text claiming official examples did. Verified against the [current official README](https://github.com/mongodb-js/mongodb-mcp-server).)*

**Configuration options worth knowing:**
- `MDB_MCP_READ_ONLY` / `--readOnly` — Restricts all write operations. **All official examples now include `--readOnly` by default** (a welcome change — see "What's New" below). Remove the flag explicitly if you need write access.
- `MDB_MCP_MAX_TIME_M_S` / `--maxTimeMS` — Sets `maxTimeMS` on all `find()`, `aggregate()`, and `count()` operations. Protects against runaway queries locking up connections. (Corrected 2026-08-14: the env var is `MDB_MCP_MAX_TIME_M_S`, not `MDB_MCP_MAX_TIME_MS` as this page previously stated — verified against the [current config options table](https://www.mongodb.com/docs/mcp-server/local-mcp/configuration/options/).)
- `MDB_MCP_IDLE_TIMEOUT_MS` — Auto-disconnects idle clients after a timeout. Helps mitigate connection accumulation during long sessions.
- `MDB_MCP_DISABLED_TOOLS` / `--disabledTools` — Comma-separated list of tools, operation types, and/or categories to disable. Useful for stripping away Atlas tools in self-hosted setups. (Corrected 2026-08-14: the flag is `--disabledTools`, not `--disableTools`.)
- `--transport` — `stdio` (default) or `http`. HTTP mode supports configurable host and port.
- `MDB_MCP_EXTERNALLY_MANAGED_SESSIONS` — For framework integrations managing their own session lifecycles.
- `MDB_MCP_MAX_ACTIVE_CONNECTIONS` (default `10`) and `MDB_MCP_CONNECTION_SCOPE` (default `"session"`) — **New since our last refresh.** Caps how many MongoDB connections a session can hold open and scopes connection visibility per-session by default, closing connections when the session ends. Part of the v2.0.0 explicit-connection-ID rework; see [release notes](https://github.com/mongodb-js/mongodb-mcp-server/releases/tag/v2.0.0).

## What's New (March–August 2026)

**GENERALLY AVAILABLE (v1.9.0, March 24).** The MongoDB MCP Server exited public preview and is now GA. This is a significant milestone — the "public preview" label that cautioned about possible breaking changes is gone. Lexical and vector search functionality also moved from preview to GA in the same release.

**[MongoDB Agent Skills Package GA (March 31)](https://www.mongodb.com/company/blog/product-release-announcements/introducing-mongodb-agent-skills).** A new [mongodb/agent-skills](https://github.com/mongodb/agent-skills) repository (167 stars as of 2026-08-14, up from 98 at our last refresh; Apache 2.0) bundles **seven Agent Skills** with the MCP Server: `mongodb-connection`, `mongodb-schema-design`, `mongodb-query-optimizer`, `mongodb-natural-language-querying`, `mongodb-search-and-ai`, `mongodb-atlas-stream-processing`, and `mongodb-mcp-setup` (confirmed against the [repo's `skills/` directory](https://github.com/mongodb/agent-skills/tree/main/skills)). These are structured instructions and best practices that transform generalist coding agents into MongoDB specialists. Available as single-install plugins for **Claude Code, Cursor, Gemini CLI, and VS Code** — each plugin bundles both the MCP Server and Agent Skills together.

**Interactive setup utility (v1.9.0).** Run `npx mongodb-mcp-server setup` for a guided configuration wizard that walks through AI client selection, read-only mode, connection string, and Atlas credentials. Creates the configuration file automatically and shows where it's stored.

**Elicitation for destructive operations.** If your client supports MCP elicitation, the server now requests user confirmation before executing dangerous tools. As of 2026-08-14 the default `confirmationRequiredTools` list has grown to eight tools: `atlas-create-access-list`, `atlas-create-db-user`, `drop-database`, `drop-collection`, `delete-many`, `drop-index`, `atlas-streams-manage`, and `atlas-streams-teardown` (up from the five we listed at our last refresh) — verified against the [current README's configuration table](https://github.com/mongodb-js/mongodb-mcp-server). v2.1.0 also added confirmation for aggregation pipelines containing destructive `$out`/`$merge` write stages. Configurable via `confirmationRequiredTools`. If the client doesn't support elicitation, tools execute without confirmation (fallback behavior).

**Hosted, MongoDB-managed remote MCP server — new since our last refresh.** MongoDB now offers a fully hosted **Atlas Managed MCP Server** at `mcp.mongodb.com`: MongoDB runs and maintains the server for you, with OAuth-based user-delegated access via Atlas App Connections instead of self-managed credentials. This directly resolves the "no hosted option" gap we flagged in our original review (see "What Doesn't Work," corrected below). Sources: [MongoDB's MCP Server overview docs](https://www.mongodb.com/docs/mcp-server/overview/) and the [`mongodb-atlas-mcp-remote` v1.0.0 release](https://github.com/mongodb-js/mongodb-mcp-server/releases/tag/mongodb-atlas-mcp-remote%2Fv1.0.0) (Aug 10, 2026), the client-side connector package for it.

**v2.0.0 (Aug 4) — breaking change.** Removed implicit session-based "last connection" behavior; `connect` and `atlas-connect-cluster` now return an explicit `connectionId` that must be passed to subsequent database tool calls, and the old `switch-connection` tool was removed. Also added `atlas-create-cluster` (multi-region, CMK encryption), `atlas-pause-resume-cluster`, `atlas-upgrade-cluster`, and a path-traversal security fix in stream resource handling. See [v2.0.0 release notes](https://github.com/mongodb-js/mongodb-mcp-server/releases/tag/v2.0.0).

**v2.1.0 (Aug 10, latest stable).** Confirmation for destructive `$out`/`$merge` aggregation stages, fixed pagination on `atlas-list-orgs`/`atlas-list-projects`, and automatic redaction of secrets from configuration output. See [v2.1.0 release notes](https://github.com/mongodb-js/mongodb-mcp-server/releases/tag/v2.1.0). (Corrects our prior "v1.10.0 latest stable" note — the project has shipped `v1.11` through `v2.1.0`, including a major version bump, since our May refresh.)

**Atlas Stream Processing tools (v1.8.1→v1.9.0).** Four tools — `atlas-streams-build`, `atlas-streams-discover`, `atlas-streams-manage`, `atlas-streams-teardown` — bring real-time streaming pipelines into the MCP workflow. Agents can create workspaces, configure connections (Kafka, S3, MongoDB clusters), build and manage stream processors, and diagnose pipeline health.

**readOnly still not the programmatic default.** All official setup examples include `--readOnly`. The underlying config still defaults to writable if you omit the flag, but the interactive setup wizard guides toward read-only from the start. Verified unchanged as of 2026-08-14 against the [current config docs](https://www.mongodb.com/docs/mcp-server/local-mcp/configuration/options/), which state plainly: "Default is to allow cluster write operations."

**Since our May 2026 refresh:** roughly two dozen releases (`v1.10.0` → `v2.1.0` stable, plus prereleases and the new `mongodb-atlas-mcp-remote` package), including one breaking major-version change. ~960 commits (up from 770), ~1,100 stars (up from 1,000), 281 forks (up from 225). Source: [live repo stats](https://github.com/mongodb-js/mongodb-mcp-server), 2026-08-14.

## What Works Well

**The most comprehensive database MCP server available.** 50+ tools is more than double the next-closest database server. The breadth is genuine — you can go from "create a project in Atlas" to "provision a cluster" to "insert data" to "build a streaming pipeline" to "check why this query is slow" to "add the suggested index" without ever leaving your agent. No other database MCP server supports the full provisioning-to-optimization lifecycle.

**Atlas Performance Advisor integration is a standout.** The tool exposes four Performance Advisor capabilities: suggested indexes, drop-index recommendations, schema advice, and slow query identification. This is the first database MCP server that proactively helps optimize performance rather than just running queries. An agent can ask "why is this query slow?", get index suggestions, and create the recommended index — all through MCP tools.

**Automatic embedding generation solves a real pain point.** The `insert-many` tool detects vector search index configurations and automatically generates embeddings using Voyage AI models during insertion, when a Voyage AI API key is configured. No manual embedding step, no separate embedding API calls. For teams building RAG pipelines on MongoDB Atlas, this removes the most tedious step. (See [MongoDB's MCP Server tool docs](https://www.mongodb.com/docs/mcp-server/tools/) for the specific mechanism.)

**Agent Skills elevate code quality.** The [Agent Skills package](https://github.com/mongodb/agent-skills) (167 stars as of 2026-08-14, 7 skills) bundles MongoDB expertise directly into coding agents. Skills cover schema design heuristics (avoiding over-normalization), compound index strategies, vector search setup, and operational safeguards — preventing the common mistakes that even experienced developers make with MongoDB. Available as one-click plugins for Claude Code, Cursor, Gemini CLI, and VS Code.

**Elicitation support adds a safety net.** Destructive operations (`drop-database`, `drop-collection`, `delete-many`, and others — eight tools by default as of 2026-08-14) now prompt for user confirmation via MCP elicitation. This is a much better approach than read-only mode for teams that need write access but want guardrails — you get the full tool set with confirmation dialogs on the dangerous operations.

**Rapid, reliable release cadence.** Dozens of releases since launch, including a major (breaking) version bump in August 2026, with ~960 commits as of 2026-08-14 (up from 770 in May). The project uses pre-release versions for testing before stable releases, indicating mature engineering practices. For comparison, many MCP servers we've reviewed haven't released in months.

**Actively maintained, judged by issue throughput.** ~1,100 stars and 281 forks as of 2026-08-14, with 11 open issues on the tracker — several issues we cited as open problems in our last refresh (connection flooding, Node 22 crashes, aggregate-on-views, framework shutdown hangs) have since been closed. Source: [live repo](https://github.com/mongodb-js/mongodb-mcp-server).

**Flexible deployment.** Stdio and HTTP transports. Docker support. Official Docker Hub image at `mongodb/mongodb-mcp-server`. Works with VS Code (GitHub Copilot), Cursor, Claude Desktop, Windsurf, Gemini CLI, and the GitHub Copilot CLI. The HTTP transport enables remote access for team setups, though it needs careful security configuration.

## What Doesn't Work

**Default-writable without the flag — but docs now guide toward read-only.** MongoDB's official examples now include `--readOnly`, which is a significant improvement over the original posture. However, the underlying default is still writable if you omit the flag — so copying a bare `npx mongodb-mcp-server` command from a third-party tutorial still gives full write access including `drop-database`. The config default should match the documentation guidance.

**~~Connection flooding during extended sessions.~~** **Closed as of this audit (2026-08-14).** Issue [#936](https://github.com/mongodb-js/mongodb-mcp-server/issues/936) — running the MCP server for extended periods flooding the cluster with connections (growing from ~700 to 3,000+) — is now closed on the tracker (the exact closing rationale isn't stated in the thread, but v2.0.0's new `MDB_MCP_MAX_ACTIVE_CONNECTIONS` cap, default `10`, and session-scoped connections that close automatically at session end directly target this failure mode — see the [v2.0.0 release notes](https://github.com/mongodb-js/mongodb-mcp-server/releases/tag/v2.0.0)). We're leaving this line in the record rather than deleting it, since it was accurate at the time of our last refresh.

**~~No remote hosted server option.~~** **Resolved as of 2026-08-14 — this was true when we last refreshed but is no longer accurate.** MongoDB now offers a fully hosted, MongoDB-managed **Atlas Managed MCP Server** at `mcp.mongodb.com`, using OAuth-based Atlas App Connections instead of self-managed credentials — see [MongoDB's MCP Server overview docs](https://www.mongodb.com/docs/mcp-server/overview/) and the [`mongodb-atlas-mcp-remote` client package](https://github.com/mongodb-js/mongodb-mcp-server/releases/tag/mongodb-atlas-mcp-remote%2Fv1.0.0) (shipped Aug 10, 2026). Compare this with [Stripe](/reviews/stripe-mcp-server/) (agent toolkit), [Linear](/reviews/linear-mcp-server/) (hosted at mcp.linear.app), or [Todoist](/reviews/todoist-mcp-server/) (hosted at ai.todoist.net) — MongoDB has closed this gap. Feature request [#641](https://github.com/mongodb-js/mongodb-mcp-server/issues/641), open since October 2025, remains open on the tracker even though the underlying capability has shipped.

**~~Node.js compatibility issues.~~** **Closed as of this audit (2026-08-14).** Issue [#718](https://github.com/mongodb-js/mongodb-mcp-server/issues/718) — crashes on Node 22 from the OIDC plugin requiring an ESM-only package via CommonJS — is now closed. Current prerequisites have also moved on: the [live README](https://github.com/mongodb-js/mongodb-mcp-server) now requires Node.js **22.13.0+** outright (Node 20.x support is deprecated), rather than the wider 20.19+/22.12+/23+ range we previously listed, so the original in-between-version footgun no longer applies the same way.

**Framework integration issues — declined, not fixed.** Issues [#974](https://github.com/mongodb-js/mongodb-mcp-server/issues/974) (LangChain's `MultiServerMCPClient` async context manager not exiting cleanly) and [#968](https://github.com/mongodb-js/mongodb-mcp-server/issues/968) (a client hanging on exit with the server enabled) are both now **closed as "not planned"** rather than open or fixed — MongoDB has declined to change the server's shutdown behavior for these cases. Practically the same caution applies as before (some clients don't cleanly exit with this server enabled), but it's a permanent won't-fix rather than a tracked bug.

**~~Still in public preview.~~** **Resolved — now GA as of v1.9.0 (March 24, 2026).** The "public preview" label is gone. The API is considered stable.

**Aggregation on views — a permanent limitation, not an open bug.** Issue [#878](https://github.com/mongodb-js/mongodb-mcp-server/issues/878) (the aggregate tool failing when targeting views in clusters with search-index permissions, due to pre-validation calling `$listSearchIndexes` on views) is now **closed as "not planned."** An edge case, but MongoDB has confirmed it won't be fixed, so treat it as a standing limitation of view-based workflows rather than something to wait out.

## How It Compares

The database MCP landscape splits into relational and document/NoSQL categories. MongoDB is the first document database MCP server we've reviewed, so direct comparisons are limited, but the tool design choices are instructive:

**vs. [Neon](/reviews/neon-mcp-server/) (4/5):** Neon has 20 tools focused on cloud Postgres — branching, migrations, and SQL execution. MongoDB has double the tools but covers a different database paradigm. Neon's branch-based migration workflow is the gold standard for safe schema changes; MongoDB has no equivalent. But Neon can't provision clusters or analyze performance.

**vs. [Supabase](/reviews/supabase-mcp-server/) (4/5):** Supabase covers database plus edge functions, storage, and debugging — broader platform scope. MongoDB goes deeper into database operations — more query tools, index management, performance analysis. Different philosophies: Supabase is a platform server, MongoDB is a database server.

**vs. [Postgres MCP](/reviews/postgres-mcp-server/) (2.5/5):** The official (Anthropic reference) Postgres server has a confirmed SQL injection vulnerability that let attackers bypass its read-only restriction, and it has been archived — see [Datadog Security Labs' case study](https://securitylabs.datadoghq.com/articles/mcp-vulnerability-case-study-SQL-injection-in-the-postgresql-mcp-server/) and the [archived repository itself](https://github.com/modelcontextprotocol/servers-archived/tree/HEAD/src/postgres) (now living under `modelcontextprotocol/servers-archived`). MongoDB's server is actively maintained with strong security defaults (read-only mode, environment-variable credentials). Not really a competition.

**vs. [SQLite MCP](/reviews/sqlite-mcp-server/) (3/5):** SQLite's server is a minimal teaching tool. MongoDB's is a production operations interface. Different weight classes entirely.

**vs. Community MongoDB servers:** Several community alternatives exist — [MongoDB Lens](https://github.com/furey/mongodb-lens) (204 stars as of 2026-08-14, 50+ tools, JavaScript, safety confirmation for destructive ops), [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server) (282 stars, TypeScript, smart ObjectId handling, read-only mode), [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp) (175 stars, TypeScript, basic CRUD). MongoDB Lens's tool count (50+) is now roughly on par with the official server's (53, up from 41 at our last refresh), and it still has strong safety features (destructive operation confirmation), but it lacks Atlas integration, vector search, and Voyage AI embeddings. Use the official server for Atlas workflows; consider MongoDB Lens if safety guardrails matter more.

### Database MCP Category Comparison

With six database reviews now complete, here's how they compare:

| Feature | MongoDB | [PostgreSQL](/reviews/postgresql-mcp-server/) | [Redis](/reviews/redis-mcp-servers/) | [MySQL](/reviews/mysql-mcp-server/) | [SQL Server](/reviews/sql-server-mcp-server/) | [SQLite](/reviews/sqlite-mcp-servers/) |
|---------|---------|-----------|-------|-------|------------|--------|
| **Rating** | **4/5** | **4.5/5** | **4/5** | **3.5/5** | **3.5/5** | **3.5/5** |
| Official server | Yes (~1,100 stars, 53 tools, **GA**, plus hosted option) | No official | Yes (566 stars, 25+ tools) | No (Oracle absent) | Experimental only | Archived (Anthropic) |
| Top community server | MongoDB Lens (204 stars, 50+ tools) | Postgres MCP Pro (2.4k stars) | Agent Memory (207 stars) | benborla (~1-1.7k stars, varies by source) | PerformanceMonitor (470 stars, ~63 tools) | sqlite-explorer (104 stars) |
| Multi-DB MCP support | No (absent from DBHub/Toolbox) | Yes (DBHub, Toolbox, etc.) | No | Yes (DBHub, Toolbox, etc.) | Yes (DBHub, Toolbox, etc.) | Yes (DBHub, Toolbox, etc.) |
| Vendor backing | MongoDB Inc. (first-party) | Community-driven | Redis Inc. (3 servers) | Community-driven | Microsoft (experimental) | None (Anthropic archived) |
| Vector search MCP | Yes (unified index + auto embeddings) | Limited | Yes (built-in) | No | No | Via db-mcp/libSQL |
| Performance tools | Performance Advisor (Atlas only) | Postgres MCP Pro (any PG) | Server info only | None | PerformanceMonitor (~63 tools, any SQL Server) | None |
| Cloud management | Atlas (18 cluster tools + 4 Streams) | Supabase/Neon/Azure/AWS | Redis Cloud | AWS/Azure/Google | AWS/Azure | Turso, SQLite Cloud |

MongoDB has the strongest first-party server; PostgreSQL has the deepest community ecosystem. Redis uniquely ships three official servers. SQLite has the most total servers but lowest top-server adoption.

## The Bottom Line

The MongoDB MCP server is the most feature-rich database MCP server we've reviewed. 50+ tools across six categories, rapid release cadence, strong maintenance, and genuine innovation with the Performance Advisor, automatic embedding, Atlas Stream Processing, Agent Skills, and — as of August 2026 — a hosted managed option.

The GA milestone (v1.9.0, March 24) resolves our biggest concern from the original review — the "public preview" label is gone. Elicitation support for destructive operations adds a proper safety net beyond the binary read-only flag. The Agent Skills package (7 skills, plugins for Claude Code/Cursor/Gemini/VS Code) is a unique differentiator — no other database MCP server bundles expert-level coding guidance alongside database tools. Since our May 2026 refresh, MongoDB also shipped a hosted, MongoDB-managed remote MCP endpoint at `mcp.mongodb.com` — closing the "self-host only" gap we flagged — and a `v2.0.0` breaking change that replaced implicit connection state with explicit `connectionId`s.

The remaining concern, verified still true as of this 2026-08-14 audit, is the underlying default-writable config: the interactive setup wizard and all official examples guide toward `--readOnly`, but the programmatic default has not changed. The connection-flooding issue we previously cited as unresolved is now closed on the tracker, plausibly addressed by v2.0.0's new connection caps. MongoDB's engineering team is clearly investing in this server as a first-class product — roughly two dozen releases, including one major version bump, since our last review.

If your stack includes MongoDB, this is an easy install. If you're choosing between MongoDB and Postgres for a new project and MCP integration matters to you, MongoDB's MCP server is significantly ahead of any Postgres option — though the database choice should be driven by your data model needs, not the MCP server quality.

**Rating: 4 out of 5** — the deepest database MCP integration available, now GA with elicitation safety, Agent Skills, interactive setup, and a hosted option. The half-point deduction is for the still-mutable programmatic default (the config default should match the documentation guidance). *(Audit note, 2026-08-14: several other cons behind the original half-point deduction — connection flooding, Node 22 crashes, aggregate-on-views — have since closed; we left the numeric rating as-is since re-scoring is an editorial call beyond the scope of a citation audit, but a future content refresh should revisit it.)*

| | |
|---|---|
| **MCP Server** | MongoDB MCP Server |
| **Publisher** | MongoDB, Inc. (official) |
| **Repository** | [mongodb-js/mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server) |
| **Stars** | ~1,100 (2026-08-14) |
| **Tools** | 53 (25 database + 18 Atlas cluster + 4 stream processing + 4 local + 2 knowledge), plus a hosted managed option |
| **Agent Skills** | 7 ([mongodb/agent-skills](https://github.com/mongodb/agent-skills), 167 stars) |
| **Transport** | stdio, HTTP, and hosted (`mcp.mongodb.com`) |
| **Language** | TypeScript |
| **License** | Apache 2.0 |
| **Status** | Generally Available (v2.1.0) |
| **Pricing** | Free (server). MongoDB Atlas has free tier; paid plans for production. |
| **Our rating** | 4/5 |

---

## Refresh History {#refresh-history}

**2026-08-14 (claim-level citation audit, no full content refresh):** Re-verified every citation and re-checked core facts against live primary sources (GitHub repo/API, official README, MongoDB docs). Corrected: tool count 41+→53 (six categories restructured with accurate per-category counts, including a `switch-connection`→explicit-`connectionId` model change from v2.0.0); "no remote hosted server option" con was **factually reversed** — MongoDB shipped a hosted Managed MCP Server at `mcp.mongodb.com` (Aug 10); four previously-cited "open" issues (#936 connection flooding, #718 Node 22 crashes, #878 aggregate-on-views, #974/#968 framework shutdown hangs) are now closed (mostly "not planned," one plausibly fixed by v2.0.0's connection caps); Docker setup example had the wrong image name (missing `mongodb/` namespace) and, like the rest of the setup examples, was missing `--readOnly` despite the page's own text claiming otherwise; two config option names were wrong (`MDB_MCP_MAX_TIME_MS`→`MDB_MCP_MAX_TIME_M_S`, `--disableTools`→`--disabledTools`); Agent Skills and community-server star counts refreshed (98→167, MongoDB Lens 201→204, kiliczsh 276→282, QuantGeekDev 174→175); added 2 primary sources to the previously-uncited Postgres MCP SQL-injection claim; latest stable version corrected v1.10.0→v2.1.0 (a `v2.0.0` breaking change shipped in between). Core premise (official, actively maintained, most feature-rich database MCP server) confirmed still accurate — not a fabrication case. Numeric rating (4/5) left unchanged; re-scoring is a separate editorial call.

**2026-05-02 (first refresh):** **GA MILESTONE** — MongoDB MCP Server exited public preview with v1.9.0 (March 24). **Agent Skills Package GA** (March 31) — mongodb/agent-skills repo (98 stars, 7 skills) bundles expert MongoDB guidance for Claude Code/Cursor/Gemini/VS Code as one-click plugins. **Elicitation support** — destructive ops (drop-database, drop-collection, delete-many) now prompt for user confirmation via MCP elicitation. Interactive setup utility `npx mongodb-mcp-server setup`. Lexical + vector search moved from preview to GA. v1.10.0 latest stable (April 20). Stars 970→1,000 (+3%), commits 675→770 (+14%), forks 210→225. Community servers flat: MongoDB Lens 200→201, kiliczsh 276→278. Connection flooding issue still open. Rating holds 4/5 — GA status resolves biggest concern but config default and connection flooding remain.

**2026-03-23 (original review):** Initial review covering 41+ tools across six categories. Atlas Stream Processing tools new in v1.8.1. Read-only now documented default. Rating 4/5.

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. See our [About page](/about/) for details on our review process.*

*This review was last refreshed on 2026-05-02 using Claude Opus 4.6 (Anthropic).*

