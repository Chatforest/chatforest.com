---
title: "The MongoDB MCP Server — The Most Comprehensive Database Server We've Reviewed"
date: 2026-03-14T11:49:11+09:00
description: "MongoDB's official MCP server went GA with 40+ tools, Agent Skills package (7 skills for Claude/Cursor/Gemini/VS Code), elicitation for destructive op confirmation, and interactive setup utility."
og_description: "MongoDB's official MCP server is now GA with 41+ tools, Agent Skills package (7 skills, 98 stars), elicitation for destructive ops, interactive setup utility. 1,000 stars, 770 commits. Rating: 4/5."
content_type: "Review"
card_description: "Now GA — the most comprehensive database MCP server with 40+ tools, an Agent Skills package bundling 7 MongoDB-specialist skills for coding agents, elicitation-based confirmation for destructive operations, and an interactive setup utility. 1,000 stars and climbing."
last_refreshed: 2026-05-02
---

No other database MCP server comes close to this tool count. Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** 1,000 GitHub stars, 225 forks, 41+ tools across six categories (database ops, Atlas clusters, stream processing, local deployments, performance advisory, knowledge search), 9 open issues, 770 commits, shipping every 1-2 weeks. **Now Generally Available** — no longer public preview.

The MongoDB MCP server ships with 40+ tools across six categories: database operations, Atlas cluster management, Atlas Stream Processing, Atlas local deployments, performance advisory, and knowledge search. For context, [Neon](/reviews/neon-mcp-server/) has 20 tools (impressive for Postgres). [Supabase](/reviews/supabase-mcp-server/) has 20+ across multiple services. MongoDB has double — and covers everything from `find` queries to spinning up local clusters to building stream processing pipelines to getting index recommendations from the Atlas Performance Advisor.

This is what happens when a database company goes all-in on MCP. MongoDB didn't just wrap a connection driver in a tool. They built a full operational interface that handles the entire lifecycle — from creating a project and provisioning a cluster to querying data, analyzing performance, and cleaning up.

## What It Does

The MongoDB MCP server connects AI agents to MongoDB databases — both self-hosted instances and MongoDB Atlas cloud clusters — through six tool categories. The npm package is `@mongodb-js/mongodb-mcp-server` (also available as `mongodb-mcp-server`).

### Database Operations (21 tools)

The core of the server. These tools handle everyday database work:

- **find** / **aggregate** / **count** — Query documents with full MongoDB query syntax, aggregation pipelines, and document counting.
- **insert-many** / **update-many** / **delete-many** — CRUD operations with bulk support. The `insert-many` tool can now automatically generate embeddings for fields with vector search indexes using Voyage AI models.
- **create-collection** / **drop-collection** / **rename-collection** / **drop-database** — Schema management tools. Yes, `drop-database` exists — read-only mode matters.
- **create-index** / **drop-index** / **collection-indexes** — Index management, now including vector search indexes via a unified tool.
- **collection-schema** / **collection-storage-size** / **db-stats** — Introspection tools for understanding data shape and storage.
- **explain** — Query plan analysis, critical for performance work.
- **export** — Data export capabilities.
- **mongodb-logs** — Access database logs.
- **connect** / **switch-connection** — Connection management for working across multiple databases.

### Atlas Cluster Management (12 tools)

For teams on MongoDB Atlas, these tools manage cloud infrastructure without leaving your editor:

- **atlas-list-orgs** / **atlas-list-projects** / **atlas-create-project** — Organization and project management.
- **atlas-list-clusters** / **atlas-inspect-cluster** / **atlas-connect-cluster** — Cluster discovery, inspection, and connection.
- **atlas-create-free-cluster** — Spin up a free-tier cluster from your agent. Useful for prototyping.
- **atlas-list-db-users** / **atlas-create-db-user** — Database user management.
- **atlas-inspect-access-list** / **atlas-create-access-list** — IP allowlist management.
- **atlas-list-alerts** — Monitor cluster alerts.
- **atlas-get-performance-advisor** — New in Winter 2026. Access the Atlas Performance Advisor for suggested indexes, drop-index recommendations, schema advice, and slow query identification.

### Atlas Stream Processing (3 tools)

New in v1.8.1 (March 2026). Tools for building and managing real-time streaming data pipelines on Atlas Stream Processing:

- **atlas-streams-build** — Create workspaces, connections (Kafka, Cluster, S3, etc.), processors, and PrivateLink setups.
- **atlas-streams-discover** — Inspect resources and diagnose processor health.
- **atlas-streams-manage** — Start/stop processors and modify configurations.

These tools bring Atlas Stream Processing into the MCP workflow — agents can now set up and manage streaming pipelines alongside database operations, without switching to the Atlas UI or CLI.

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
      "args": ["-y", "mongodb-mcp-server"],
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
  -- npx -y mongodb-mcp-server
```

**Docker:**

```bash
docker run --rm -i \
  -e MDB_MCP_CONNECTION_STRING="mongodb+srv://..." \
  mongodb-mcp-server
```

**HTTP transport:**

```bash
npx mongodb-mcp-server --transport http --httpPort 3000
```

**Setup difficulty: Moderate.** The connection string gets you database operations immediately. Atlas management requires service account credentials (API client ID and secret). The server works without Atlas credentials — you just won't have the cluster management tools.

**Configuration options worth knowing:**
- `MDB_MCP_READ_ONLY` / `--readOnly` — Restricts all write operations. **All official examples now include `--readOnly` by default** (a welcome change — see "What's New" below). Remove the flag explicitly if you need write access.
- `MDB_MCP_MAX_TIME_MS` / `--maxTimeMs` — Sets `maxTimeMS` on all `find()` and `aggregate()` operations. Protects against runaway queries locking up connections.
- `MDB_MCP_IDLE_TIMEOUT_MS` — Auto-disconnects idle clients after a timeout. Helps mitigate connection accumulation during long sessions.
- `--disableTools` — Comma-separated list of tools to disable. Useful for stripping away Atlas tools in self-hosted setups.
- `--transport` — `stdio` (default) or `http`. HTTP mode supports configurable host and port.
- `MDB_MCP_EXTERNALLY_MANAGED_SESSIONS` — For framework integrations managing their own session lifecycles.

## What's New (March–May 2026)

**GENERALLY AVAILABLE (v1.9.0, March 24).** The MongoDB MCP Server exited public preview and is now GA. This is a significant milestone — the "public preview" label that cautioned about possible breaking changes is gone. Lexical and vector search functionality also moved from preview to GA in the same release.

**MongoDB Agent Skills Package GA (March 31).** A new [mongodb/agent-skills](https://github.com/mongodb/agent-skills) repository (98 stars, Apache 2.0) bundles **seven Agent Skills** with the MCP Server. These are structured instructions and best practices that transform generalist coding agents into MongoDB specialists — covering connection management, schema design (with heuristics to avoid over-normalization), indexing strategies, query patterns, performance optimization, vector search/RAG, and operational safeguards. Available as single-install plugins for **Claude Code, Cursor, Gemini CLI, and VS Code** — each plugin bundles both the MCP Server and Agent Skills together.

**Interactive setup utility (v1.9.0).** Run `npx mongodb-mcp-server setup` for a guided configuration wizard that walks through AI client selection, read-only mode, connection string, and Atlas credentials. Creates the configuration file automatically and shows where it's stored.

**Elicitation for destructive operations.** If your client supports MCP elicitation, the server now requests user confirmation before executing dangerous tools. Default tools requiring confirmation: `drop-database`, `drop-collection`, `delete-many`, `atlas-create-db-user`, `atlas-create-access-list`. Configurable via `confirmationRequiredTools`. If the client doesn't support elicitation, tools execute without confirmation (fallback behavior).

**v1.10.0 (April 20, latest stable).** Browser fetch fallback in ApiClient, protobufjs security update to v7.5.5. v1.11.0-prerelease.1 (April 28) in testing.

**Atlas Stream Processing tools (v1.8.1→v1.9.0).** Four tools — `atlas-streams-build`, `atlas-streams-discover`, `atlas-streams-manage`, `atlas-streams-teardown` — bring real-time streaming pipelines into the MCP workflow. Agents can create workspaces, configure connections (Kafka, S3, MongoDB clusters), build and manage stream processors, and diagnose pipeline health.

**readOnly now the documented default.** All official setup examples include `--readOnly`. The underlying config still defaults to writable if you omit the flag, but the interactive setup wizard guides toward read-only from the start.

**Seven releases since our last review** (v1.8.1 → v1.10.0 stable, plus five pre-releases), maintaining the rapid shipping cadence. 770 commits (up from 675), 1,000 stars (up from 970).

## What Works Well

**The most comprehensive database MCP server available.** 40+ tools is double the next-closest database server. The breadth is genuine — you can go from "create a project in Atlas" to "provision a cluster" to "insert data" to "build a streaming pipeline" to "check why this query is slow" to "add the suggested index" without ever leaving your agent. No other database MCP server supports the full provisioning-to-optimization lifecycle.

**Atlas Performance Advisor integration is a standout.** The Winter 2026 update added four Performance Advisor capabilities: suggested indexes, drop-index recommendations, schema advice, and slow query identification. This is the first database MCP server that proactively helps optimize performance rather than just running queries. An agent can ask "why is this query slow?", get index suggestions, and create the recommended index — all through MCP tools.

**Automatic embedding generation solves a real pain point.** The `insert-many` tool detects vector search index configurations and automatically generates embeddings using Voyage AI models during insertion. No manual embedding step, no separate embedding API calls. For teams building RAG pipelines on MongoDB Atlas, this removes the most tedious step.

**Agent Skills elevate code quality.** The [Agent Skills package](https://github.com/mongodb/agent-skills) (98 stars, 7 skills) bundles MongoDB expertise directly into coding agents. Skills cover schema design heuristics (avoiding over-normalization), compound index strategies, vector search setup, and operational safeguards — preventing the common mistakes that even experienced developers make with MongoDB. Available as one-click plugins for Claude Code, Cursor, Gemini CLI, and VS Code.

**Elicitation support adds a safety net.** Destructive operations (`drop-database`, `drop-collection`, `delete-many`) now prompt for user confirmation via MCP elicitation. This is a much better approach than read-only mode for teams that need write access but want guardrails — you get the full tool set with confirmation dialogs on the dangerous operations.

**Rapid, reliable release cadence.** 30+ releases since launch, shipping every 1-2 weeks with 770 commits (up 14% in 40 days). The project uses pre-release versions for testing before stable releases, indicating mature engineering practices. For comparison, many MCP servers we've reviewed haven't released in months.

**Only 9 open issues.** With 1,000 stars and 225 forks, having just 9 open issues signals strong maintenance. The team actively responds to and resolves issues.

**Flexible deployment.** Stdio and HTTP transports. Docker support. Official Docker Hub image at `mongodb/mongodb-mcp-server`. Works with VS Code (GitHub Copilot), Cursor, Claude Desktop, Windsurf, Gemini CLI, and the GitHub Copilot CLI. The HTTP transport enables remote access for team setups, though it needs careful security configuration.

## What Doesn't Work

**Default-writable without the flag — but docs now guide toward read-only.** MongoDB's official examples now include `--readOnly`, which is a significant improvement over the original posture. However, the underlying default is still writable if you omit the flag — so copying a bare `npx mongodb-mcp-server` command from a third-party tutorial still gives full write access including `drop-database`. The config default should match the documentation guidance.

**Connection flooding during extended sessions.** Issue [#936](https://github.com/mongodb-js/mongodb-mcp-server/issues/936) remains open. Running the MCP server for extended periods floods the cluster with connections — growing from ~700 to 3,000+. The new `MDB_MCP_IDLE_TIMEOUT_MS` env var and connection string pool limits (`maxPoolSize`, `maxIdleTimeMS`) help mitigate but don't fully solve the problem — users report connections still accumulating beyond pool limits. The team has requested reproduction steps for deeper investigation.

**No remote hosted server option.** Despite being from MongoDB Inc., there's no hosted MCP endpoint at `mcp.mongodb.com` or similar. You must run the server locally via npx or Docker. Compare this with [Stripe](/reviews/stripe-mcp-server/) (agent toolkit), [Linear](/reviews/linear-mcp-server/) (hosted at mcp.linear.app), or [Todoist](/reviews/todoist-mcp-server/) (hosted at ai.todoist.net). Feature request [#641](https://github.com/mongodb-js/mongodb-mcp-server/issues/641) has been open since October 2025.

**Node.js compatibility issues.** Issue [#718](https://github.com/mongodb-js/mongodb-mcp-server/issues/718) documents crashes on Node 22 due to the OIDC plugin requiring an ESM-only package via CommonJS. Requires Node 20.19.0+, Node 22.12.0+, or Node 23+. If you're on an in-between version, expect crashes.

**Framework integration issues.** Recent issues ([#974](https://github.com/mongodb-js/mongodb-mcp-server/issues/974), [#968](https://github.com/mongodb-js/mongodb-mcp-server/issues/968)) report problems with LangChain's MultiServerMCPClient async context manager not exiting properly, and OpenAI Codex being unable to exit normally. These suggest the server's session lifecycle doesn't cleanly handle all client shutdown patterns.

**~~Still in public preview.~~** **Resolved — now GA as of v1.9.0 (March 24, 2026).** The "public preview" label is gone. The API is considered stable.

**Aggregation on views throws errors.** Issue [#878](https://github.com/mongodb-js/mongodb-mcp-server/issues/878) reports that the aggregate tool fails when targeting views in clusters with search index permissions, due to pre-validation calling `$listSearchIndexes` on views. An edge case, but one that blocks legitimate view-based workflows.

## How It Compares

The database MCP landscape splits into relational and document/NoSQL categories. MongoDB is the first document database MCP server we've reviewed, so direct comparisons are limited, but the tool design choices are instructive:

**vs. [Neon](/reviews/neon-mcp-server/) (4/5):** Neon has 20 tools focused on cloud Postgres — branching, migrations, and SQL execution. MongoDB has double the tools but covers a different database paradigm. Neon's branch-based migration workflow is the gold standard for safe schema changes; MongoDB has no equivalent. But Neon can't provision clusters or analyze performance.

**vs. [Supabase](/reviews/supabase-mcp-server/) (4/5):** Supabase covers database plus edge functions, storage, and debugging — broader platform scope. MongoDB goes deeper into database operations — more query tools, index management, performance analysis. Different philosophies: Supabase is a platform server, MongoDB is a database server.

**vs. [Postgres MCP](/reviews/postgres-mcp-server/) (2.5/5):** The official Postgres server has a SQL injection vulnerability and is archived. MongoDB's server is actively maintained with strong security defaults (read-only mode, environment-variable credentials). Not really a competition.

**vs. [SQLite MCP](/reviews/sqlite-mcp-server/) (3/5):** SQLite's server is a minimal teaching tool. MongoDB's is a production operations interface. Different weight classes entirely.

**vs. Community MongoDB servers:** Several community alternatives exist — [MongoDB Lens](https://github.com/furey/mongodb-lens) (200 stars, 50+ tools, JavaScript, safety confirmation for destructive ops), [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server) (276 stars, TypeScript, smart ObjectId handling, read-only mode, v2.0.2 Feb 2026), [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp) (174 stars, TypeScript, basic CRUD). MongoDB Lens actually has *more* tools (50+ vs 41) with better safety features (destructive operation confirmation), but lacks Atlas integration, vector search, and Voyage AI embeddings. Use the official server for Atlas workflows; consider MongoDB Lens if safety guardrails matter more.

### Database MCP Category Comparison

With six database reviews now complete, here's how they compare:

| Feature | MongoDB | [PostgreSQL](/reviews/postgresql-mcp-server/) | [Redis](/reviews/redis-mcp-servers/) | [MySQL](/reviews/mysql-mcp-server/) | [SQL Server](/reviews/sql-server-mcp-server/) | [SQLite](/reviews/sqlite-mcp-servers/) |
|---------|---------|-----------|-------|-------|------------|--------|
| **Rating** | **4/5** | **4.5/5** | **4/5** | **3.5/5** | **3.5/5** | **3.5/5** |
| Official server | Yes (1,000 stars, 41 tools, **GA**) | No official | Yes (458 stars, 25+ tools) | No (Oracle absent) | Experimental only | Archived (Anthropic) |
| Top community server | MongoDB Lens (201 stars, 50+ tools) | Postgres MCP Pro (2.4k stars) | Agent Memory (207 stars) | benborla (1.4k stars) | PerformanceMonitor (272 stars, 63 tools) | sqlite-explorer (104 stars) |
| Multi-DB MCP support | No (absent from DBHub/Toolbox) | Yes (DBHub, Toolbox, etc.) | No | Yes (DBHub, Toolbox, etc.) | Yes (DBHub, Toolbox, etc.) | Yes (DBHub, Toolbox, etc.) |
| Vendor backing | MongoDB Inc. (first-party) | Community-driven | Redis Inc. (3 servers) | Community-driven | Microsoft (experimental) | None (Anthropic archived) |
| Vector search MCP | Yes (unified index + auto embeddings) | Limited | Yes (built-in) | No | No | Via db-mcp/libSQL |
| Performance tools | Performance Advisor (Atlas only) | Postgres MCP Pro (any PG) | Server info only | None | PerformanceMonitor (76 tools, any SQL Server) | None |
| Cloud management | Atlas (13 tools + Streams) | Supabase/Neon/Azure/AWS | Redis Cloud | AWS/Azure/Google | AWS/Azure | Turso, SQLite Cloud |

MongoDB has the strongest first-party server; PostgreSQL has the deepest community ecosystem. Redis uniquely ships three official servers. SQLite has the most total servers but lowest top-server adoption.

## The Bottom Line

The MongoDB MCP server is the most feature-rich database MCP server we've reviewed. 40+ tools across six categories, rapid release cadence, strong maintenance, and genuine innovation with the Performance Advisor, automatic embedding, Atlas Stream Processing, and now Agent Skills.

The GA milestone (v1.9.0, March 24) resolves our biggest concern from the original review — the "public preview" label is gone. Elicitation support for destructive operations adds a proper safety net beyond the binary read-only flag. The Agent Skills package (7 skills, plugins for Claude Code/Cursor/Gemini/VS Code) is a unique differentiator — no other database MCP server bundles expert-level coding guidance alongside database tools.

The remaining concerns are the underlying default-writable config (the interactive setup wizard guides toward read-only, but the programmatic default hasn't changed) and connection flooding under extended use. But these are solvable problems — and MongoDB's engineering team is clearly investing in this server as a first-class product, with seven releases since our last review and 770 commits.

If your stack includes MongoDB, this is an easy install. If you're choosing between MongoDB and Postgres for a new project and MCP integration matters to you, MongoDB's MCP server is significantly ahead of any Postgres option — though the database choice should be driven by your data model needs, not the MCP server quality.

**Rating: 4 out of 5** — the deepest database MCP integration available, now GA with elicitation safety, Agent Skills, and interactive setup. The half-point deduction is for the still-mutable programmatic default (the config default should match the documentation guidance) and connection flooding that remains unresolved. No longer held back by preview status.

| | |
|---|---|
| **MCP Server** | MongoDB MCP Server |
| **Publisher** | MongoDB, Inc. (official) |
| **Repository** | [mongodb-js/mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server) |
| **Stars** | ~1,000 |
| **Tools** | 41+ (21 database + 13 Atlas + 4 stream processing + 3 local + 2 knowledge) |
| **Agent Skills** | 7 ([mongodb/agent-skills](https://github.com/mongodb/agent-skills), 98 stars) |
| **Transport** | stdio, HTTP |
| **Language** | TypeScript |
| **License** | Apache 2.0 |
| **Status** | Generally Available (v1.10.0) |
| **Pricing** | Free (server). MongoDB Atlas has free tier; paid plans for production. |
| **Our rating** | 4/5 |

---

## Refresh History {#refresh-history}

**2026-05-02 (first refresh):** **GA MILESTONE** — MongoDB MCP Server exited public preview with v1.9.0 (March 24). **Agent Skills Package GA** (March 31) — mongodb/agent-skills repo (98 stars, 7 skills) bundles expert MongoDB guidance for Claude Code/Cursor/Gemini/VS Code as one-click plugins. **Elicitation support** — destructive ops (drop-database, drop-collection, delete-many) now prompt for user confirmation via MCP elicitation. Interactive setup utility `npx mongodb-mcp-server setup`. Lexical + vector search moved from preview to GA. v1.10.0 latest stable (April 20). Stars 970→1,000 (+3%), commits 675→770 (+14%), forks 210→225. Community servers flat: MongoDB Lens 200→201, kiliczsh 276→278. Connection flooding issue still open. Rating holds 4/5 — GA status resolves biggest concern but config default and connection flooding remain.

**2026-03-23 (original review):** Initial review covering 41+ tools across six categories. Atlas Stream Processing tools new in v1.8.1. Read-only now documented default. Rating 4/5.

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. See our [About page](/about/) for details on our review process.*

*This review was last refreshed on 2026-05-02 using Claude Opus 4.6 (Anthropic).*
