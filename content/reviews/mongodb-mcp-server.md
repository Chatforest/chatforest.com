---
title: "The MongoDB MCP Server — The Most Comprehensive Database Server We've Reviewed"
date: 2026-03-14T11:49:11+09:00
description: "MongoDB's official MCP server packs 37+ tools spanning database operations, Atlas cluster management, local deployments, performance advisory, and knowledge search. Here's the honest review."
og_description: "MongoDB's official MCP server has 37+ tools covering queries, indexes, Atlas clusters, local deployments, and performance advisors. 959 stars, rapid releases. Rating: 4/5."
content_type: "Review"
card_description: "The most comprehensive database MCP server we've reviewed — 37+ tools for queries, indexes, Atlas management, local clusters, performance advisors, and knowledge search. All from MongoDB's official team."
---

No other database MCP server comes close to this tool count.

The MongoDB MCP server ships with 37+ tools across five categories: database operations, Atlas cluster management, Atlas local deployments, performance advisory, and knowledge search. For context, [Neon](/reviews/neon-mcp-server/) has 20 tools (impressive for Postgres). [Supabase](/reviews/supabase-mcp-server/) has 20+ across multiple services. MongoDB has nearly double — and covers everything from `find` queries to spinning up local clusters to getting index recommendations from the Atlas Performance Advisor.

This is what happens when a database company goes all-in on MCP. MongoDB didn't just wrap a connection driver in a tool. They built a full operational interface that handles the entire lifecycle — from creating a project and provisioning a cluster to querying data, analyzing performance, and cleaning up.

## What It Does

The MongoDB MCP server connects AI agents to MongoDB databases — both self-hosted instances and MongoDB Atlas cloud clusters — through five tool categories:

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
- `MDB_MCP_READ_ONLY` / `--readOnly` — Restricts all write operations. **Default is writable**, which is unusual — most database MCP servers default to read-only. Set this to true in production.
- `MDB_MCP_MAX_TIME_MS` / `--maxTimeMs` — Sets `maxTimeMS` on all `find()` and `aggregate()` operations. Protects against runaway queries locking up connections.
- `--disableTools` — Comma-separated list of tools to disable. Useful for stripping away Atlas tools in self-hosted setups.
- `--transport` — `stdio` (default) or `http`. HTTP mode supports configurable host and port.
- `MDB_MCP_EXTERNALLY_MANAGED_SESSIONS` — For framework integrations managing their own session lifecycles.

## What Works Well

**The most comprehensive database MCP server available.** 37+ tools is nearly double the next-closest database server. The breadth is genuine — you can go from "create a project in Atlas" to "provision a cluster" to "insert data" to "check why this query is slow" to "add the suggested index" without ever leaving your agent. No other database MCP server supports the full provisioning-to-optimization lifecycle.

**Atlas Performance Advisor integration is a standout.** The Winter 2026 update added four Performance Advisor capabilities: suggested indexes, drop-index recommendations, schema advice, and slow query identification. This is the first database MCP server that proactively helps optimize performance rather than just running queries. An agent can ask "why is this query slow?", get index suggestions, and create the recommended index — all through MCP tools.

**Automatic embedding generation solves a real pain point.** The `insert-many` tool detects vector search index configurations and automatically generates embeddings using Voyage AI models during insertion. No manual embedding step, no separate embedding API calls. For teams building RAG pipelines on MongoDB Atlas, this removes the most tedious step.

**Rapid, reliable release cadence.** 16+ releases since launch, shipping every 1-2 weeks. The project uses pre-release versions for testing before stable releases, indicating mature engineering practices. For comparison, many MCP servers we've reviewed haven't released in months.

**Only 10 open issues.** With 959 stars and 207 forks, having just 10 open issues signals strong maintenance. Several of those are feature requests, not bugs. The team actively responds to and resolves issues.

**Flexible deployment.** Stdio and HTTP transports. Docker support. Works with VS Code (GitHub Copilot), Cursor, Claude Desktop, Windsurf, and the GitHub Copilot CLI. The HTTP transport enables remote access for team setups, though it needs careful security configuration.

## What Doesn't Work

**Default-writable is a dangerous choice.** Most database MCP servers default to read-only mode. MongoDB's MCP server defaults to full read-write access, which means `drop-database` works out of the box. You must explicitly set `MDB_MCP_READ_ONLY=true` for safety. This should be the default, not an opt-in.

**Connection flooding during extended sessions.** Issue [#936](https://github.com/mongodb-js/mongodb-mcp-server/issues/936) reports that running the MCP server for extended periods floods the cluster with connections. For agents that maintain long-lived sessions, this can exhaust connection limits. There's no built-in connection pooling strategy to prevent this.

**No remote hosted server option.** Despite being from MongoDB Inc., there's no hosted MCP endpoint at `mcp.mongodb.com` or similar. You must run the server locally via npx or Docker. Compare this with [Stripe](/reviews/stripe-mcp-server/) (agent toolkit), [Linear](/reviews/linear-mcp-server/) (hosted at mcp.linear.app), or [Todoist](/reviews/todoist-mcp-server/) (hosted at ai.todoist.net). Feature request [#641](https://github.com/mongodb-js/mongodb-mcp-server/issues/641) has been open since October 2025.

**Node.js compatibility issues.** Issue [#718](https://github.com/mongodb-js/mongodb-mcp-server/issues/718) documents crashes on Node 22 due to the OIDC plugin requiring an ESM-only package via CommonJS. Requires Node 20.19.0+, Node 22.12.0+, or Node 23+. If you're on an in-between version, expect crashes.

**Framework integration issues.** Recent issues ([#974](https://github.com/mongodb-js/mongodb-mcp-server/issues/974), [#968](https://github.com/mongodb-js/mongodb-mcp-server/issues/968)) report problems with LangChain's MultiServerMCPClient async context manager not exiting properly, and OpenAI Codex being unable to exit normally. These suggest the server's session lifecycle doesn't cleanly handle all client shutdown patterns.

**Still in public preview.** MongoDB labels this "public preview," which means breaking changes are possible. The rapid release cadence is a double-edged sword — features ship fast, but APIs may shift between versions.

**Aggregation on views throws errors.** Issue [#878](https://github.com/mongodb-js/mongodb-mcp-server/issues/878) reports that the aggregate tool fails when targeting views in clusters with search index permissions, due to pre-validation calling `$listSearchIndexes` on views. An edge case, but one that blocks legitimate view-based workflows.

## How It Compares

The database MCP landscape splits into relational and document/NoSQL categories. MongoDB is the first document database MCP server we've reviewed, so direct comparisons are limited, but the tool design choices are instructive:

**vs. [Neon](/reviews/neon-mcp-server/) (4/5):** Neon has 20 tools focused on cloud Postgres — branching, migrations, and SQL execution. MongoDB has nearly double the tools but covers a different database paradigm. Neon's branch-based migration workflow is the gold standard for safe schema changes; MongoDB has no equivalent. But Neon can't provision clusters or analyze performance.

**vs. [Supabase](/reviews/supabase-mcp-server/) (4/5):** Supabase covers database plus edge functions, storage, and debugging — broader platform scope. MongoDB goes deeper into database operations — more query tools, index management, performance analysis. Different philosophies: Supabase is a platform server, MongoDB is a database server.

**vs. [Postgres MCP](/reviews/postgres-mcp-server/) (2.5/5):** The official Postgres server has a SQL injection vulnerability and is archived. MongoDB's server is actively maintained with strong security defaults (read-only mode, environment-variable credentials). Not really a competition.

**vs. [SQLite MCP](/reviews/sqlite-mcp-server/) (3/5):** SQLite's server is a minimal teaching tool. MongoDB's is a production operations interface. Different weight classes entirely.

**vs. Community MongoDB servers:** Several community alternatives exist — [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp), [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server), [1RB/mongo-mcp](https://github.com/1RB/mongo-mcp). None come close to the official server's tool count, Atlas integration, or maintenance. Use the official one.

## The Bottom Line

The MongoDB MCP server is the most feature-rich database MCP server we've reviewed. 37+ tools across five categories, rapid release cadence, strong maintenance, and genuine innovation with the Performance Advisor and automatic embedding features.

The main concerns are the default-writable mode (flip this immediately), connection flooding under extended use, and the public preview label. But these are solvable problems — and MongoDB's engineering team is clearly investing in this server as a first-class product.

If your stack includes MongoDB, this is an easy install. If you're choosing between MongoDB and Postgres for a new project and MCP integration matters to you, MongoDB's MCP server is significantly ahead of any Postgres option — though the database choice should be driven by your data model needs, not the MCP server quality.

**Rating: 4 out of 5** — the deepest database MCP integration available, with active development and genuine innovation, held back by default-writable safety concerns and public preview status.

| | |
|---|---|
| **MCP Server** | MongoDB MCP Server |
| **Publisher** | MongoDB, Inc. (official) |
| **Repository** | [mongodb-js/mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server) |
| **Stars** | ~960 |
| **Tools** | 37+ (21 database + 12 Atlas + 4 local + 2 knowledge) |
| **Transport** | stdio, HTTP |
| **Language** | TypeScript |
| **License** | Apache 2.0 |
| **Pricing** | Free (server). MongoDB Atlas has free tier; paid plans for production. |
| **Our rating** | 4/5 |
