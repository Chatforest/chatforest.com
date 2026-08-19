---
title: "Turso MCP Server — The 23.9K-Star SQLite Database With Built-In AI Agent Access"
date: 2026-03-23T23:00:00+09:00
sources_audited: 2026-08-19
description: "Turso's built-in MCP server gives AI agents direct SQL access to SQLite-compatible databases. 23.9K GitHub stars, 9 tools, MIT license, one-flag setup."
og_description: "Turso MCP Server: 23.9K stars, MIT license, 9 MCP tools built into the database CLI. SQLite-compatible, Rust-powered, one-flag setup. Free tier: 5GB storage, 100 databases. Rating: 3.5/5."
content_type: "Review"
card_description: "SQLite-compatible database with built-in MCP server. 9 tools for schema inspection, querying, and data modification — activated with a single --mcp flag. Rust-powered, MIT license, works with Claude Desktop, Claude Code, and Cursor."
last_refreshed: 2026-08-19
---

Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** [23,900+ stars, 1,271 forks](https://github.com/tursodatabase/turso), MIT license, beta status, Rust, [9 MCP tools built in](https://turso.tech/blog/introducing-the-turso-database-mcp-server), local + cloud deployment, free tier (5GB storage, 100 databases).

## What's New (August 2026 Update)

**Active release cadence continues — v0.7.2 stable, v0.8.0 in pre-release.** Since the original March 23 review, Turso has shipped a steady stream of releases: [v0.5.2 (April 1, 2026)](https://github.com/tursodatabase/turso/releases/tag/v0.5.2), v0.6.0 (May 14), v0.6.1 (May 22), v0.7.0 (July 13), v0.7.1 (July 22), and [v0.7.2 (July 30, 2026)](https://github.com/tursodatabase/turso/releases/tag/v0.7.2), with v0.8.0 pre-releases actively shipping as of mid-August. The project remains far more active than typical beta projects.

**MVCC concurrent writes promoted from tech preview to beta (v0.5.0, March 4).** Per [Turso's own release announcement](https://turso.tech/blog/turso-0.5.0), concurrent writes moved from tech preview to beta in v0.5.0, enabled with `PRAGMA journal_mode = 'mvcc'` — tested against the Hermitage test suite, the Elle transactional consistency checker, and Antithesis fault injection. A lock-free monotonic rowid allocator eliminates the contention bottleneck that previously slowed concurrent transactions, and ATTACHed databases now each get independent MVCC transaction state.

**Full-text search via Tantivy shipped in v0.5, now a default feature.** Full-text search [powered by the Tantivy search engine](https://turso.tech/blog/turso-0.5.0) (Rust) stores inverted index segments directly inside the SQLite B-tree — no external index file, no separate process. It's listed as an experimental feature in the [project's current feature list](https://github.com/tursodatabase/turso). Combined with the existing built-in vector search, Turso now has both structured-text search and semantic (embedding) search in a single embedded database engine.

**Multi-process database access has shipped as an experimental feature.** The GitHub issue this review previously cited (#769) [closed in July 2026](https://github.com/tursodatabase/turso/issues/769); multi-process access itself shipped in the meantime as "multi-process WAL coordination via the `.tshm` sidecar for cross-process WAL readers and writers," listed among Turso's [current experimental features](https://github.com/tursodatabase/turso). It's still rough — a newer tracking issue, [#1853 "Multi-process support"](https://github.com/tursodatabase/turso/issues/1853), remains open for further work, and related bugs (e.g. reader connections missing cross-process writes) are still being filed. So this is shipped-but-experimental, not merely "in development."

**AgentFS: Turso expands into agent storage.** [tursodatabase/agentfs](https://github.com/tursodatabase/agentfs) is a separate repository providing a filesystem built for AI agents: file/directory access, a key-value store for agent state, and a tool-call audit trail, all backed by a single SQLite database file (powered by Turso). TypeScript, Python, and Rust SDKs are available, and it can be mounted via FUSE (Linux) or NFS (macOS). Correction from the original May update: AgentFS did not launch with a "v0.6.4" release — no such Turso version exists. Per [Turso's own announcement post](https://turso.tech/blog/agentfs), AgentFS launched **November 13, 2025** as its own project, not tied to a specific Turso database release. It nonetheless signals Turso positioning itself as a storage layer for the agentic AI stack, not just a database.

**Turso Cloud's next-generation engine is in private beta.** Per [Turso's announcement](https://turso.tech/blog/turso-cloud-new-generation-private-beta), Turso Cloud — which currently runs on libSQL, the original SQLite fork — is beginning a migration to the new Rust-rewritten Turso engine, starting with a private beta aimed at teams running AI-agent, distributed-systems, and edge-first workloads. Existing Turso Cloud users are unaffected for now; this is the clearest signal yet of a path from beta to GA.

**Stars: 18.4K → 23.9K.** [Roughly 5,500 stars](https://github.com/tursodatabase/turso) since the May update — meaningfully faster growth than the modest pace reported in that update, consistent with an active infrastructure project gaining real mindshare.

**MCP tool surface unchanged.** The [9 built-in MCP tools](https://turso.tech/blog/introducing-the-turso-database-mcp-server) (open_database, current_database, list_tables, describe_table, execute_query, insert_data, update_data, delete_data, schema_change) remain the same. No new tools, no deprecated tools.

**Rating holds 3.5/5.** Active development, meaningful technical progress (MVCC to beta, Tantivy FTS, experimental multi-process WAL, AgentFS, cloud-gen private beta), and a clear trajectory toward production readiness — but beta is still beta. The MCP tool surface remains basic CRUD, and the multi-process/remote transport story, while further along than the May update suggested, is still experimental.

[Turso](https://github.com/tursodatabase/turso) takes a different approach to database MCP integration: instead of building a separate MCP server that wraps database calls, the MCP server is built directly into the database itself. Run `tursodb your_database.db --mcp` and your SQLite-compatible database becomes an MCP tool that AI agents can query, modify, and inspect through natural language.

This is part of the [SQLite renaissance](https://dev.to/pockit_tools/the-sqlite-renaissance-why-the-worlds-most-deployed-database-is-taking-over-production-in-2026-3jcc) happening in 2026 — a convergence of Turso, Cloudflare D1, Litestream, and the embedded database movement making SQLite viable for production workloads that were previously PostgreSQL-or-nothing territory. Note on naming: the [`tursodatabase/turso`](https://github.com/tursodatabase/turso) engine reviewed here is a ground-up rewrite of SQLite in Rust — it is a separate codebase from [libSQL](https://github.com/tursodatabase/libsql), the older open-source SQLite fork that still powers Turso Cloud's production hosting today. [Turso Cloud's next-generation engine](https://turso.tech/blog/turso-cloud-new-generation-private-beta), currently in private beta, is what migrates Turso Cloud onto this Rust engine. This `tursodatabase/turso` engine adds distributed replication, vector search, concurrent writes via MVCC, and now native MCP support.

The key question: is a beta database with built-in MCP more practical than a production-ready database paired with a standalone MCP adapter?

## What It Does

Turso's MCP server [exposes 9 tools](https://turso.tech/blog/introducing-the-turso-database-mcp-server) through the `--mcp` CLI flag:

### Database Operations

| Tool | Purpose |
|------|---------|
| **open_database** | Open a SQLite database file or create an in-memory instance |
| **current_database** | Show which database is currently active |

### Schema Inspection

| Tool | Purpose |
|------|---------|
| **list_tables** | List all tables in the current database |
| **describe_table** | Show column names, types, constraints, and indexes for a table |

### Data Access

| Tool | Purpose |
|------|---------|
| **execute_query** | Run read-only SELECT statements — returns results as structured data |

### Data Modification

| Tool | Purpose |
|------|---------|
| **insert_data** | Insert rows into tables |
| **update_data** | Update existing rows with conditions |
| **delete_data** | Remove rows matching conditions |

### Schema Management

| Tool | Purpose |
|------|---------|
| **schema_change** | Run CREATE TABLE, ALTER TABLE, and DROP TABLE operations |

The tool design enforces a clear separation: `execute_query` is strictly read-only (SELECT only), while write operations go through dedicated tools with explicit intent. This is a safety pattern — an agent can't accidentally DROP a table through the query tool.

## Setup

### One-Flag Activation

```bash
# Open a database file with MCP enabled
tursodb your_database.db --mcp

# Or use an in-memory database
tursodb --mcp
```

That's it. No separate server to install, no Docker container, no npm package. The MCP server runs as part of the database process itself.

### Claude Desktop

```json
{
  "mcpServers": {
    "turso": {
      "command": "tursodb",
      "args": ["path/to/database.db", "--mcp"]
    }
  }
}
```

### Claude Code

```bash
claude mcp add my-database -- tursodb ./path/to/your/database.db --mcp
```

### Cursor

Add to your MCP configuration with the same command/args pattern.

### Installation

Install via the [official script](https://github.com/tursodatabase/turso#-command-line):

```bash
curl -sSfL https://get.tur.so/install.sh | bash
```

(Correction: the `get.turso.tech` install URL previously listed here no longer resolves. The current official installer domain is `get.tur.so`.)

Or via Rust:

```bash
cargo add turso
```

SDKs available for JavaScript (`@tursodatabase/database`), Python (`pyturso`), Go, Java, Rust, .NET, and WebAssembly, per the [project's language bindings](https://github.com/tursodatabase/turso).

**Setup difficulty: Low.** One install command, one flag. No Docker, no API keys for local use, no separate MCP server process. The simplest database MCP setup we've reviewed.

## Key Capabilities

### SQLite Compatibility With Extras

Turso isn't just another database — it's a SQLite-compatible engine that extends SQLite with features the original lacks:

- **Vector search** — store and query embeddings natively, useful for RAG pipelines
- **BEGIN CONCURRENT** — MVCC-based concurrent writes (experimental), solving SQLite's single-writer limitation
- **Distributed replication** — sync local databases to edge replicas globally via Turso Cloud
- **Change data capture** — stream real-time database modifications
- **Encryption at rest** — protect data on disk (experimental)
- **Full-text search** — powered by the tantivy search engine (experimental)
- **Asynchronous I/O** — io_uring support on Linux for better performance

### Multi-Language Bindings

The database itself (not just the MCP server) runs in-process across Go, JavaScript, Java, Python, Rust, and WebAssembly. An AI agent could help you build an application using Turso, then directly query the development database through MCP — no context switching between the code editor and a database client.

### Cloud Integration

For production use, [Turso Cloud](https://turso.tech/pricing) offers hosted databases with global edge replication:

| Plan | Price | Storage | Databases | Row Reads/Month |
|------|-------|---------|-----------|-----------------|
| **Free** | $0 | 5GB | 100 | 500M |
| **Developer** | $4.99/mo | 9GB | Unlimited | Included |
| **Scaler** | $24.92/mo | 24GB | Unlimited | Included |
| **Pro** | $416.58/mo | 50GB | Unlimited | Included |
| **Enterprise** | Custom | Custom | Custom | Custom |

(Pricing verified against [turso.tech/pricing](https://turso.tech/pricing) as of August 2026; the Pro tier's database limit was corrected from a previous "10,000 active" figure — the live pricing page lists Unlimited databases for Developer, Scaler, and Pro tiers alike.)

The free tier is generous — 5GB storage, 100 databases, and 500 million row reads per month with no credit card required. Enough for development and small production workloads.

## Compared to Other Database MCP Servers

| Feature | Turso | [Neon](/reviews/neon-mcp-server/) | [Supabase](/reviews/supabase-mcp-server/) | [MongoDB](/reviews/mongodb-mcp-server/) |
|---------|-------|------|----------|---------|
| **GitHub stars** | [23.9K](https://github.com/tursodatabase/turso) | [~22.9K](https://github.com/neondatabase/neon) (platform) | [~108K](https://github.com/supabase/supabase) (platform) | [~1.1K](https://github.com/mongodb-js/mongodb-mcp-server) (MCP) |
| **Database type** | SQLite (Rust rewrite) | PostgreSQL | PostgreSQL | Document (NoSQL) |
| **MCP integration** | Built into database | Separate server | Separate server | Separate server |
| **MCP tools** | 9 | 6+ | 10+ | 8+ |
| **Setup** | `--mcp` flag | npx / Docker | npx / Docker | npx |
| **Local-first** | Yes (file-based) | Cloud-first | Cloud-first | Cloud or local |
| **Vector search** | Built-in | pgvector extension | pgvector extension | Atlas Vector Search |
| **Free tier** | 5GB, 100 DBs | 0.5GB, 1 project | 500MB, 2 projects | 512MB |
| **License** | MIT | Apache 2.0 | Apache 2.0 | SSPL |
| **Production-ready** | Beta | Yes | Yes | Yes |

### vs. Neon

[Neon](/reviews/neon-mcp-server/) is the serverless PostgreSQL platform with branching, autoscaling, and a mature MCP server. If you need PostgreSQL compatibility — complex queries, advanced indexing, stored procedures, ecosystem tooling — Neon is the better choice. Turso wins on simplicity (one binary, file-based, no Docker) and SQLite compatibility (your existing SQLite databases just work).

### vs. Supabase

[Supabase](/reviews/supabase-mcp-server/) offers PostgreSQL plus auth, storage, edge functions, and realtime subscriptions — a full backend platform. Its MCP server exposes all of this. Turso is narrower: just the database layer with MCP access. Choose Supabase for a complete backend; choose Turso for a lightweight, embeddable database.

### vs. Standalone SQLite MCP Servers

Several community MCP servers wrap raw SQLite (e.g., the reference `sqlite` MCP server). Turso's advantage: the database engine itself is enhanced (vector search, concurrent writes, replication, full-text search) while maintaining SQLite file format compatibility. You get more than SQLite without leaving the SQLite ecosystem.

## Limitations

- **Beta status.** The project explicitly warns against production use. The database engine is under active development with experimental features (BEGIN CONCURRENT, encryption, full-text search). For production workloads, Neon and Supabase are safer choices today.
- **9 tools is thin.** Compared to Supabase's 10+ tools covering auth, storage, and edge functions, or even Neon's database branching capabilities, Turso's MCP surface is basic CRUD operations plus schema management. No migration tools, no backup/restore, no replication management through MCP.
- **No advanced query tools.** The `execute_query` tool only handles SELECT statements. There's no EXPLAIN/ANALYZE for query optimization, no transaction management across multiple operations, no prepared statement support. Agents can read and write data but can't tune performance.
- **Local-only MCP for now.** The `--mcp` flag works with local database files. Connecting the MCP server to Turso Cloud databases requires the CLI authentication flow (`turso db shell <dbname> --mcp` or manual URL/token configuration). The seamless "cloud database + MCP" story is still developing.
- **Ecosystem maturity.** [23.9K stars and 1,271 forks](https://github.com/tursodatabase/turso) indicate strong interest, but the contributor and tooling ecosystem is smaller than PostgreSQL-based alternatives. SQLite tooling (migrations, ORMs, admin UIs) is less mature than the PostgreSQL ecosystem, though [Drizzle ORM](https://orm.drizzle.team/) and others are closing the gap.
- **MCP transport details are sparse.** The documentation focuses on stdio transport (via the CLI `--mcp` flag). SSE and WebSocket support — important for remote and multi-agent setups — aren't documented. This limits use to local, single-agent configurations.

## Who Should Use This

**Good fit:**
- Developers building AI-assisted applications who want their development database directly accessible to their coding agent
- Projects already using SQLite that want MCP access without adding infrastructure
- Prototyping and local development where simplicity matters more than production guarantees
- Teams exploring the edge database / embedded database paradigm
- Applications that need vector search alongside traditional SQL in a single embedded engine

**Not the right fit:**
- Production workloads that need a battle-tested database (use Neon or Supabase)
- PostgreSQL-dependent projects (Turso is SQLite-compatible, not PostgreSQL-compatible)
- Multi-agent setups that need remote MCP access (stdio transport only)
- Teams that need comprehensive MCP tooling beyond basic CRUD (migrations, backups, replication management)

## The Bottom Line

Turso's built-in MCP server represents what database-native AI integration should look like: no separate server, no Docker container, no npm package — just a `--mcp` flag on the database itself. The 9 tools cover the essentials (schema inspection, querying, data modification), and the one-command setup is the simplest of any database MCP server we've reviewed.

The underlying database is compelling too. SQLite compatibility means your existing `.db` files just work, while Turso adds vector search, concurrent writes, distributed replication, and full-text search that vanilla SQLite can't match. At [23,900+ stars](https://github.com/tursodatabase/turso) with MIT licensing, the project has serious momentum.

But beta is beta. The production-readiness gap between Turso and established alternatives like [Neon](/reviews/neon-mcp-server/) and [Supabase](/reviews/supabase-mcp-server/) is real. The MCP tool surface is basic CRUD without the advanced operations (migrations, transactions, performance analysis) that would make it a complete database management interface. And the stdio-only MCP transport limits it to local, single-agent use.

**Rating: 3.5 out of 5** — The simplest database MCP setup available, backed by an ambitious SQLite-compatible engine with genuine technical innovations. The picture has continued to improve since the original review: MVCC concurrent writes promoted to beta, Tantivy full-text search shipped, multi-process database access now shipped experimentally (via a WAL sidecar), AgentFS established as a separate agent-native storage project, and Turso Cloud's next-generation engine entering private beta. Star count has grown substantially too — 18.4K in May to 23.9K in August. The trajectory toward production readiness is clearer than it was in March. But beta is still beta. The MCP tool surface remains basic CRUD (9 tools), multi-process access and remote MCP transport are both still experimental rather than production-grade, and the gap with production-ready alternatives like [Neon](/reviews/neon-mcp-server/) and [Supabase](/reviews/supabase-mcp-server/) remains.

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Originally published March 2026; refreshed May 2026, August 2026. See our [About page](/about/) for details on our review process.*
