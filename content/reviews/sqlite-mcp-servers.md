---
title: "SQLite MCP Servers — From Anthropic's Reference Server to 180-Tool Powerhouses and Edge Database Solutions"
date: 2026-03-23T12:00:00+09:00
description: "SQLite MCP servers reviewed: Anthropic's archived reference server (mcp-server-sqlite), jparkerweb/mcp-sqlite (126 stars, 8 tools), sqlite-explorer (107 stars, read-only), DBHub"
og_description: "SQLite MCP servers: Anthropic's reference (archived), jparkerweb/mcp-sqlite (126 stars, 8 tools), sqlite-explorer (107 stars), DBHub (3.4k stars), Turso/libSQL servers, db-mcp (181 tools). 15+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "SQLite has the most MCP servers of any database — but no canonical winner. Anthropic's reference server is archived, the community is fragmented across 15+ options, and the most capable server (181 tools) has almost no adoption. The ecosystem reflects SQLite's nature: everywhere, embedded in everything, but nobody's in charge."
last_refreshed: 2026-08-16
sources_audited: 2026-08-16
---

SQLite is the most deployed database engine in the world — [over one trillion active databases](https://sqlite.org/mostdeployed.html) across every iPhone, every Android device, every browser, every Mac, and every Windows machine. It's likely used more than all other database engines combined. Part of our **[Databases MCP category](/categories/databases/)**.

You'd expect the MCP ecosystem to match that dominance. It doesn't — but it's interesting.

There are **15+ SQLite MCP servers** on GitHub, more than any other single database. But there's no clear leader. Anthropic's reference implementation is archived. The most-starred dedicated server has 107 stars. The most capable one (181 tools) has 10 stars. And the best way to connect an AI agent to SQLite might actually be a multi-database server that happens to support SQLite.

*Correction (2026-08-16): an earlier version of this claim included "the Mars rovers" among SQLite's deployments. That claim traced only to speculative forum posts, not any primary source from SQLite, NASA, or JPL — it has been removed. SQLite's confirmed aerospace deployment is the [Airbus A350](https://www.sqlite.org/famous.html), noted below.*

## Anthropic's Reference Server (Archived)

| Detail | Info |
|--------|------|
| [modelcontextprotocol/servers (archived)](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/sqlite) | Split into a separate [servers-archived](https://github.com/modelcontextprotocol/servers-archived) repo (294 stars) when Anthropic archived old reference servers on May 29, 2025; the still-active [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) now has 89.6k stars |
| Package | [mcp-server-sqlite on PyPI](https://pypi.org/project/mcp-server-sqlite/) |
| Language | Python |
| Transport | stdio |
| License | MIT |

Anthropic built a SQLite MCP server as one of the original reference implementations when MCP launched. It shipped with 6 tools:

- **read_query** — Execute SELECT queries
- **write_query** — Execute INSERT, UPDATE, DELETE
- **create_table** — Create new tables
- **list_tables** — Show all tables
- **describe_table** — Get schema details
- **append_insight** — Add business insights to a dynamic memo

It also exposed a `memo://insights` resource — a continuously updated business intelligence memo — and a `mcp-demo` prompt for interactive database exploration.

The PyPI package (`mcp-server-sqlite`) has [14,798 weekly downloads and 56,614 monthly downloads](https://pypistats.org/packages/mcp-server-sqlite) as of August 2026. That's decent adoption, likely driven by tutorials and Claude Desktop setup guides, despite the server being archived.

### Why It's Archived

Anthropic moved their reference servers to a separate [servers-archived](https://github.com/modelcontextprotocol/servers-archived) repository. The active `modelcontextprotocol/servers` repo now maintains only 7 reference servers (Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking, Time). SQLite, PostgreSQL, and several others were cut.

The archived server still works — it's on PyPI and installable via `uvx mcp-server-sqlite`. But it's not receiving updates. For production use, the community servers are now the better path.

## jparkerweb/mcp-sqlite — The Most Complete Dedicated Server

| Detail | Info |
|--------|------|
| [jparkerweb/mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite) | 126 stars, 16 forks, 34 commits |
| Language | JavaScript (100%) |
| Transport | stdio |
| License | MIT |
| Latest | v1.0.9 (April 2026) |

This is the most polished dedicated SQLite MCP server. It provides 8 tools covering full CRUD operations:

**Database Information:**
- `db_info` — Database metadata
- `list_tables` — Enumerate all tables
- `get_table_schema` — Column definitions and constraints

**Data Operations:**
- `create_record` — Insert rows
- `read_records` — Query with filtering
- `update_records` — Modify existing data
- `delete_records` — Remove records

**Advanced:**
- `query` — Execute arbitrary SQL with parameterized values

### What Works Well

**Clean CRUD abstraction.** Instead of raw SQL tools, it provides semantic operations (`create_record`, `read_records`, `update_records`, `delete_records`) that map to what agents actually want to do. An LLM doesn't need to compose SQL for basic operations — it just calls the appropriate tool with field names and values.

**Parameter binding.** The `query` tool supports parameterized values, preventing SQL injection. This matters when agents are constructing queries from user input.

**Active maintenance.** v1.0.9 (April 4, 2026) shipped a security fix for a SQL injection vulnerability (CWE-89) affecting all CRUD operations. The project is alive and actively patching security issues.

**IDE integration.** Documented setup for Cursor, VS Code, and Claude Desktop. The target audience is developers who want SQLite access from their AI coding assistant.

### What Doesn't Work Well

**JavaScript-only.** Built on the Node.js `sqlite3` library, which means you need Node.js installed. Python-based servers are more common in the MCP ecosystem and integrate more naturally with Python-heavy AI workflows.

**No read-only mode.** Unlike several competitors, there's no flag to restrict operations to reads only. For exploration and analysis use cases, you have to trust the agent not to modify data.

**Limited query validation.** The `query` tool accepts arbitrary SQL. No query sanitization, no row limits, no timeout enforcement.

## sqlite-explorer-fastmcp-mcp-server — Read-Only Safety

| Detail | Info |
|--------|------|
| [hannesrudolph/sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server) | 107 stars, 29 forks, 9 commits |
| Language | Python (100%) |
| Transport | stdio |
| License | Not specified |
| Built with | FastMCP framework |

The most-starred dedicated SQLite MCP server takes a safety-first approach: **read-only access only**. Three tools:

- **read_query** — Execute SELECT queries with validation and parameter binding
- **list_tables** — Show available tables
- **describe_table** — Column types, constraints, primary keys

### What Works Well

**Enforced read-only access.** Query validation ensures only SELECT statements execute. You can point this at a production database and let an agent explore without risk of accidental writes.

**Row limit enforcement.** Results are capped to prevent an agent from accidentally dumping a million-row table into its context window.

**FastMCP framework.** Built on the higher-level FastMCP abstraction, which simplifies development and provides a cleaner server implementation.

### What Doesn't Work Well

**Only 9 commits.** The project appears feature-complete but static. No updates since late 2024 — still dormant through August 2026.

**No write capabilities.** If you need an agent to create tables or insert data, you need a different server.

**No license specified.** A meaningful concern for any production deployment.

## Multi-Database Servers with SQLite Support

For many use cases, the best SQLite MCP server isn't a dedicated one — it's a multi-database server.

### bytebase/dbhub

| Detail | Info |
|--------|------|
| [bytebase/dbhub](https://github.com/bytebase/dbhub) | 3,400 stars, 286 forks, 597 commits |
| Language | TypeScript |
| License | MIT |
| Latest | [v1.2.0](https://github.com/bytebase/dbhub/releases) (July 31, 2026) |
| Databases | PostgreSQL, MySQL, MariaDB, SQL Server, SQLite |

DBHub is the most popular multi-database MCP server. For SQLite, it connects via `sqlite:///path/to/database.db` or `sqlite:///:memory:` and provides:

- **execute_sql** — Run queries with transaction support and safety controls
- **search_objects** — Explore schemas, tables, columns, indexes

You can connect to multiple databases simultaneously via TOML configuration. For teams working with SQLite alongside other databases, this is often the most practical choice — one server, one configuration, all databases.

### googleapis/genai-toolbox

| Detail | Info |
|--------|------|
| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | 16,200 stars, Go |
| License | Apache 2.0 |
| Latest | [v1.9.0](https://github.com/googleapis/genai-toolbox/releases) (August 14, 2026) |
| Databases | Cloud SQL, AlloyDB, Spanner, SQLite, and more |

Google's multi-database toolbox supports SQLite as a local data source. It's designed primarily for Google Cloud databases but works with local SQLite files too. [v1.1.0](https://github.com/googleapis/genai-toolbox/releases) (April 13, 2026) added vector assist tools for Cloud SQL Postgres; the project has shipped several more releases since.

### Other Multi-Database Options

- **[mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy)** (414 stars, Python, MPL 2.0) — SQLAlchemy-based, supports SQLite plus 7 other databases
- ~~**universal-db-mcp**~~ — Repository deleted as of May 2026; no longer available

## Turso/libSQL — Edge SQLite

SQLite's "renaissance" in 2025–2026 is largely about edge deployment. [Turso](https://turso.tech/) and [libSQL](https://github.com/tursodatabase/libsql) (an open-source SQLite fork) are leading this movement, and the MCP ecosystem is following.

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [nbbaier/mcp-turso](https://github.com/nbbaier/mcp-turso) | 6 | TypeScript | Turso-hosted LibSQL databases (4 tools) |
| [Xexr/mcp-libsql](https://github.com/Xexr/mcp-libsql) | 21 | TypeScript | libSQL with connection pooling, SQL injection prevention (6 tools, 244 tests) |
| [spences10/mcp-turso-cloud](https://github.com/spences10/mcp-turso-cloud) | 17 | TypeScript | Turso Cloud with two-level authentication |
| [ZanzyTHEbar/mcp-memory-libsql-go](https://github.com/ZanzyTHEbar/mcp-memory-libsql-go) | 7 | Go | Semantic memory powered by libSQL with vector search |

**Xexr/mcp-libsql** stands out with 244 tests (177 unit + 67 security tests), multi-layer SQL injection prevention, connection pooling with health monitoring, and audit logging. It's the most security-conscious SQLite-family MCP server.

Turso itself has a built-in MCP server in its CLI with 9 tools, so if you're already using Turso, you don't need a separate server.

## Other Notable Servers

| Server | Stars | Language | Notable |
|--------|-------|----------|---------|
| [panasenco/mcp-sqlite](https://github.com/panasenco/mcp-sqlite) | 26 | Python | Datasette-compatible metadata, canned query tools |
| [StacklokLabs/sqlite-mcp](https://github.com/StacklokLabs/sqlite-mcp) | 15 | Go | SSE transport, optional read-only mode |
| [rvarun11/sqlite-mcp](https://github.com/rvarun11/sqlite-mcp) | 9 | Go | Schema inspection + read/write (3 tools) |
| [neverinfamous/db-mcp](https://github.com/neverinfamous/db-mcp) | 10 | TypeScript | 181 tools (native) / 154 (WASM), OAuth 2.1, "Code Mode" for 70-90% token savings |
| [sqlitecloud/sqlitecloud-mcp-server](https://github.com/sqlitecloud/sqlitecloud-mcp-server) | 1 | TypeScript | SQLite Cloud hosted databases, 10 tools (experimental) |

**neverinfamous/db-mcp** deserves special mention — its [README](https://github.com/neverinfamous/db-mcp) documents 181 MCP tools in the native backend (170 group tools + 11 built-in) and 154 in the WASM variant, plus 1,911 unit tests, 1,136 E2E tests, OAuth 2.1 auth with RFC 9728/8414 compliance, and a "Code Mode" that lets agents run sandboxed JavaScript in a V8 isolate for a claimed 70-90% token savings. It's also the only SQLite MCP server with HTTP/SSE transport and OAuth authentication. The catch: 10 stars as of August 2026. Adoption is still minimal. Whether that changes remains to be seen.

*Correction (2026-08-16): the tool count and star figures above are updated from the original review's "139 tools, 1 star" — the project has grown substantially since. An earlier draft also described db-mcp as "the successor to a deprecated 73-tool SQLite server"; that lineage could not be confirmed from a primary source (the project's current README makes no mention of a predecessor), so the claim has been removed.*

**panasenco/mcp-sqlite** is interesting for Datasette users — it converts predefined queries into callable MCP tools, so you can expose a curated set of operations rather than raw SQL access.

**StacklokLabs/sqlite-mcp** is the only Go-based server with SSE transport, making it suitable for remote MCP deployments.

## Known Issues

1. **Anthropic's reference server is archived** — The original SQLite MCP server by Anthropic is no longer maintained in the active repo. Still works via PyPI but won't receive updates.

2. **No canonical community leader** — The most-starred dedicated server (sqlite-explorer) has 107 stars. For comparison, PostgreSQL's top server (Postgres MCP Pro) has 2,400+ stars. There's no gravitational center.

3. **Read-only vs full-access split** — Some servers enforce read-only (sqlite-explorer), others allow full writes (jparkerweb, Anthropic's). There's no server with a clean, configurable read/write toggle that's also well-adopted.

4. **Most servers are feature-light** — The typical SQLite MCP server has 3–6 tools: list tables, describe table, run query. Only db-mcp (181 tools) and jparkerweb (8 tools) go significantly beyond this.

5. **SQL injection patched in top dedicated server** — jparkerweb/mcp-sqlite v1.0.9 (April 4, 2026) fixed CWE-89 SQL injection vulnerabilities across all CRUD operations. Users on v1.0.8 or earlier should upgrade immediately.

6. **No performance analysis** — Unlike PostgreSQL (Postgres MCP Pro with health monitoring) or SQL Server (PerformanceMonitor with 63 tools), no SQLite MCP server provides performance analysis, query plan explanation, or optimization suggestions.

7. **Security varies wildly** — Xexr/mcp-libsql has 244 tests and multi-layer injection prevention. Most others have no query validation at all. There's no standard approach.

8. **License gaps** — sqlite-explorer (107 stars) has no license specified. Several smaller servers also lack license information. This blocks enterprise adoption.

9. **Multi-database servers may be better** — DBHub (3,400 stars) and genai-toolbox (16,200 stars) provide SQLite support alongside other databases, with larger communities and more active maintenance than any dedicated server.

10. **Turso/libSQL ecosystem is early** — The most-starred Turso/libSQL-family MCP server (Xexr/mcp-libsql) has 21 stars. Given Turso's momentum in the edge SQLite space, this will likely grow, but it's immature today.

11. **No official backing** — SQLite itself is maintained by a small team (D. Richard Hipp and colleagues) with no MCP involvement. Unlike Redis (3 official servers), MongoDB (1 official), or even Microsoft (experimental SQL Server MCP), there's no vendor-backed SQLite MCP server. Anthropic's was the closest thing, and it's archived.

### Database MCP Category Comparison

With six database reviews now complete, here's how they compare:

| Feature | SQLite | [PostgreSQL](/reviews/postgresql-mcp-server/) | [MongoDB](/reviews/mongodb-mcp-server/) | [Redis](/reviews/redis-mcp-servers/) | [MySQL](/reviews/mysql-mcp-server/) | [SQL Server](/reviews/sql-server-mcp-server/) |
|---------|--------|-----------|---------|-------|-------|------------|
| **Rating** | **3.5/5** | **4.5/5** | **4/5** | **4/5** | **3.5/5** | **3.5/5** |
| Official server | Archived (Anthropic) | No official | Yes (970 stars, 41 tools) | Yes (458 stars, 25+ tools) | No (Oracle absent) | Experimental only |
| Top dedicated stars | 107 | 2,400+ | 970 | 458 | 1,400 | 323 |
| Total servers | 15+ | 10+ | 5+ | 10+ | 10+ | 15+ |
| Vector search MCP | Via db-mcp/libSQL | Limited | Yes (Voyage AI) | Yes (built-in) | No | No |
| Performance tools | None | Postgres MCP Pro | Performance Advisor | Server info only | None | PerformanceMonitor (76 tools) |
| Cloud/edge MCP | Turso, SQLite Cloud | Supabase/Neon/AWS/Azure | Atlas | Redis Cloud | AWS/Azure/Google | AWS/Azure |
| Transport | Mostly stdio (SSE: StacklokLabs, db-mcp) | Mixed | stdio + HTTP | Mostly stdio | Mixed | Mixed |
| AAIF membership | N/A | N/A | No | No | N/A | No |

SQLite has the most total MCP servers but the lowest top-server adoption. The ecosystem reflects SQLite's nature as a database: it's everywhere, embedded in everything, but there's no company pushing a canonical solution.

## SQLite Background

| Aspect | Detail |
|--------|--------|
| Origin | [Designed by D. Richard Hipp in spring 2000](https://en.wikipedia.org/wiki/D._Richard_Hipp) while working for General Dynamics on contract with the U.S. Navy |
| Latest version | [SQLite 3.53.4](https://sqlite.org/releaselog/3_53_4.html) (July 24, 2026; [3.53.0](https://sqlite.org/releaselog/3_53_0.html) released April 9, 2026 added a WAL-reset corruption fix and the new Query Result Formatter (QRF) library; [3.52.0 was withdrawn](https://sqlite.org/news.html) on March 13, 2026 over compatibility issues with indexes on expression/virtual columns, replaced by patch release 3.51.3) |
| License | Public domain (no copyright — one of the few major software projects with this status) |
| Market position | Most deployed database engine in the world (trillions of instances); [3.51% of the relational-database market by vendor usage](https://6sense.com/tech/relational-databases/sqlite-market-share) (third-party estimate per 6sense, a live-updating figure) |
| Deployment | [Every iPhone, Android, Mac, Windows 10+, Chrome, Firefox, Safari](https://sqlite.org/mostdeployed.html); [Airbus A350 flight software](https://www.sqlite.org/famous.html) |
| Users | [23,000+ companies](https://6sense.com/tech/relational-databases/sqlite-market-share) (third-party estimate per 6sense, a live-updating figure; used in virtually every smartphone and browser) |
| Revenue | $0 (public domain; Hipp's consortium model charges for support/testing) |
| Key trend | "SQLite Renaissance" — growing production use via Turso, Cloudflare D1, libSQL, Litestream |
| Performance | 10K–50K writes/sec (WAL mode on NVMe), ~0.01ms read latency (local) |

**The SQLite Renaissance:** SQLite in 2025–2026 is experiencing a transformation from "embedded-only" to "production database." Turso provides edge replicas across 30+ locations. Cloudflare D1 runs on Cloudflare's global network, which now spans [348+ cities](https://www.cloudflare.com/network/) (Cloudflare's own D1 docs don't specify a D1-only location count). libSQL (a SQLite fork by Turso) adds native replication, server mode, WASM UDFs, and vector search. Litestream enables continuous streaming backups to cloud storage. LiteFS offers FUSE-based replication, though [Fly.io deprioritized active LiteFS development](https://community.fly.io/t/what-is-the-status-of-litefs/23883) after sunsetting the managed LiteFS Cloud backup service in October 2024 — the core project remains stable and open-source but sees limited updates.

This trend suggests the SQLite MCP ecosystem will grow significantly. As more teams use SQLite in production — not just as an embedded database but as a distributed edge database — the need for robust MCP tooling will increase.

## The Bottom Line

SQLite's MCP ecosystem is a paradox: the most servers of any database, but no clear winner. Anthropic's reference server is archived. The most-starred dedicated server (sqlite-explorer, 107 stars) is read-only with no updates since 2024. The most capable (db-mcp, 181 tools) has 10 stars. The most practical option for many users is a multi-database server like DBHub (3,400 stars) that treats SQLite as one of several supported databases.

For **read-only exploration**, sqlite-explorer-fastmcp is the safest choice — enforced read-only access with row limits and query validation.

For **full CRUD operations**, jparkerweb/mcp-sqlite (126 stars) provides the cleanest dedicated experience with semantic tool names and active maintenance.

For **multi-database workflows**, bytebase/dbhub (3,400 stars) is the strongest option — one server handling SQLite alongside PostgreSQL, MySQL, and SQL Server.

For **edge/Turso deployments**, Xexr/mcp-libsql (21 stars) offers the best security posture with 244 tests and connection pooling.

The rating reflects an ecosystem with breadth but not depth. Lots of servers, none dominant. No vendor backing. No performance tooling. No canonical choice. But given the SQLite Renaissance and growing production adoption, this space will likely consolidate — and the eventual winner may not exist yet.

**Rating: 3.5 out of 5**

| | |
|---|---|
| **Category** | SQLite MCP Servers |
| **Top server** | sqlite-explorer-fastmcp (read-only) / jparkerweb/mcp-sqlite (full CRUD) |
| **Stars (top)** | ~107 (dedicated) / 3,400 (multi-db via DBHub) |
| **Total servers reviewed** | 15+ |
| **Best for** | Local databases, embedded apps, edge deployment (Turso/libSQL), development/testing |
| **Transport** | Mostly stdio (SSE via StacklokLabs, db-mcp) |
| **Languages** | Python, JavaScript, TypeScript, Go |
| **Our rating** | 3.5/5 |

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of August 2026. See our [About page](/about/) for details on our review process.*
