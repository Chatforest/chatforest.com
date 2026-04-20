# Best Database MCP Servers in 2026

> MongoDB vs PostgreSQL vs SQLite vs DuckDB — which database MCP server should you use? We compare official servers, community alternatives, and the new MongoDB MCP that changes the game.


The official Anthropic database MCP servers — both SQLite and PostgreSQL — are archived. No security patches, no updates, and in Postgres's case, a [SQL injection vulnerability that bypasses read-only protection](/reviews/postgres-mcp-server/). If you're still using them, it's time to switch.

The good news: the community has built better alternatives. Here's how they compare, and which one you should use.

## The Contenders

| Server | Database | Rating | Best For |
|--------|----------|--------|----------|
| [MongoDB MCP](/reviews/mongodb-mcp-server/) | MongoDB | 4/5 | MongoDB + Atlas management |
| [Supabase MCP](/reviews/supabase-mcp-server/) | Supabase (BaaS) | 4/5 | Full backend management |
| [Neon MCP](/reviews/neon-mcp-server/) | Neon Postgres | 4/5 | Cloud Postgres with AI workflows |
| Oracle Autonomous AI Database MCP | Oracle (19c, 26ai) | — | Enterprise Oracle with managed MCP |
| MariaDB MCP | MariaDB | — | MariaDB + vector search |
| [Official SQLite MCP](/reviews/sqlite-mcp-server/) | SQLite | 3/5 | Learning MCP only |
| [Official Postgres MCP](/reviews/postgres-mcp-server/) | PostgreSQL | 2.5/5 | Nothing (vulnerable) |
| Postgres MCP Pro (crystaldba) | PostgreSQL | — | Self-hosted production Postgres |
| pgEdge MCP | PostgreSQL (any v14+) | — | Enterprise Postgres with hybrid search |
| MotherDuck DuckDB MCP | DuckDB | — | Analytics & data pipelines |
| DBHub (Bytebase) | Multi-database | — | Multi-database workflows |
| jparkerweb/mcp-sqlite | SQLite | — | SQLite in production |

## Why the Official Servers Failed

Both official database MCP servers share the same story: built as reference implementations, archived when the MCP ecosystem matured past them.

**The SQLite server** is clean, educational code with a clever insight memo feature. But it has zero safety guardrails — `DROP TABLE` executes without hesitation. It was never meant for production, and now it never will be. [Read our full review](/reviews/sqlite-mcp-server/).

**The PostgreSQL server** is worse. Its entire value proposition — read-only database access — is broken by a SQL injection vulnerability. `COMMIT; DROP SCHEMA public CASCADE;` escapes the read-only transaction. The npm package at v0.6.2 still gets 21,000 weekly downloads. [Read our full review](/reviews/postgres-mcp-server/).

If you're using either of these, stop. Not eventually — now.

## The Replacements

### For Cloud Postgres: Neon MCP

**[Neon MCP](/reviews/neon-mcp-server/)** (4/5) is Neon's first-party MCP server for their serverless Postgres platform. With 20 tools, OAuth authentication, and a hosted remote server at `mcp.neon.tech`, it's the most capable database MCP server we've reviewed.

**The killer feature:** branch-based migrations. When your agent runs a migration, Neon creates an instant copy-on-write branch from your production data. The migration runs on this branch first. Your agent verifies the results, then merges to the main branch — or discards the branch if something went wrong. No rollback scripts, no downtime risk.

**What it offers:**
- Project management (create, list, describe, delete projects)
- Branch-based migration workflows (prepare → verify → complete)
- SQL execution and transactions
- Query tuning with EXPLAIN analysis and branch-based optimization
- Schema inspection (tables, columns, constraints)
- OAuth 2.0 authentication (no API keys on disk)
- Built-in documentation access

**Setup (remote, recommended):**
```json
{
  "mcpServers": {
    "neon": {
      "url": "https://mcp.neon.tech/mcp"
    }
  }
}
```

**The catch:** Neon-only. This server works exclusively with Neon's serverless Postgres. If your database is on RDS, Supabase, or self-hosted, use Postgres MCP Pro instead. [Read our full review](/reviews/neon-mcp-server/).

### For Supabase Users: Supabase MCP

**[Supabase MCP](/reviews/supabase-mcp-server/)** (4/5) is the only BaaS MCP server we've reviewed — it manages your entire backend, not just the database. 8 tool groups cover database queries, edge function deployment, storage management, branch-based development, debugging logs, and TypeScript type generation.

**What it offers beyond database:**
- Edge function deployment directly from your AI assistant
- Storage bucket management
- Service logs (API, Postgres, edge functions, auth, storage, realtime)
- TypeScript type generation from database schema
- OAuth 2.1 authentication with project scoping
- Read-only mode using a real PostgreSQL role (not query filtering)

**Setup (remote, recommended):**
```json
{
  "mcpServers": {
    "supabase": {
      "url": "https://mcp.supabase.com/mcp?project_ref=YOUR_PROJECT_REF&read_only=true"
    }
  }
}
```

**How it compares to Neon:** Supabase goes wide (full backend), Neon goes deep (database). Neon's copy-on-write branching includes data; Supabase's is schema-only and requires a paid plan. For pure database work, Neon is better. For managing your entire Supabase stack from one server, Supabase wins. [Read our full review](/reviews/supabase-mcp-server/).

### For MongoDB: MongoDB MCP Server

**[MongoDB MCP](/reviews/mongodb-mcp-server/)** (4/5) is the most comprehensive database MCP server we've reviewed — 40+ tools across five categories: database operations, Atlas cluster management, Atlas local deployments, performance advisory, and knowledge search.

**What it offers:**
- 21 database tools: find, aggregate, count, insert/update/delete, index management, schema inspection, explain, export, logs
- 13 Atlas management tools: create projects, provision clusters, manage users, inspect access lists, monitor alerts, Atlas Stream Processing
- 4 local deployment tools: create and manage local MongoDB clusters via Docker
- Performance Advisor: suggested indexes, drop recommendations, schema advice, slow query analysis
- Knowledge search: natural language queries against MongoDB documentation
- Automatic embedding generation for vector search indexes during insert operations

**Setup:**
```json
{
  "mcpServers": {
    "mongodb": {
      "command": "npx",
      "args": ["-y", "mongodb-mcp-server"],
      "env": {
        "MDB_MCP_CONNECTION_STRING": "mongodb+srv://...",
        "MDB_MCP_READ_ONLY": "true"
      }
    }
  }
}
```

**Why it wins:** No other database MCP server covers the full lifecycle — from provisioning infrastructure to querying data to optimizing performance. The v1.8 series added Atlas Stream Processing tools and process metrics. The Performance Advisor integration is unique: your agent can ask why a query is slow, get index suggestions, and create the index, all through MCP. The 1-2 week release cadence shows serious investment. Set `MDB_MCP_READ_ONLY=true` — the default-writable mode is the main safety concern. [Read our full review](/reviews/mongodb-mcp-server/).

### For Self-Hosted PostgreSQL: Postgres MCP Pro

**[Postgres MCP Pro](https://github.com/crystaldba/postgres-mcp)** (crystaldba) is the community server that does everything the official one should have done. 2,400+ GitHub stars, actively maintained, and designed for real-world use.

**What it offers:**
- Schema exploration (list schemas, objects, table details)
- SQL execution with configurable read-only mode that actually works
- EXPLAIN plan analysis — see how PostgreSQL will execute your query before running it
- Index tuning based on an industrial-strength algorithm (originally developed for Microsoft SQL Server)
- Database health checks: unused indexes, duplicate indexes, bloated indexes, buffer cache hit rates, connection issues
- Hypothetical index simulation — test whether an index would help without creating it

**Setup:**
```json
{
  "mcpServers": {
    "postgres": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "crystaldba/postgres-mcp",
        "--access-mode=unrestricted",
        "--connection-string=postgresql://user:pass@host/db"
      ]
    }
  }
}
```

**Why it wins:** It's not just a query tool — it's a database advisor. The EXPLAIN analysis and index tuning tools mean your agent can diagnose slow queries, not just run them. The health check alone justifies switching from the official server.

### For Any PostgreSQL: pgEdge MCP

**[pgEdge MCP Server](https://github.com/pgEdge/pgedge-postgres-mcp)** went GA on April 2, 2026, making it the most deployment-flexible PostgreSQL MCP server available. Unlike Neon (Neon-only) or Supabase (Supabase-only), pgEdge works with *any* standard Postgres v14+ — community Postgres, Amazon RDS, Azure Database, Google Cloud SQL, or self-hosted.

**What it offers:**
- Schema introspection — primary keys, foreign keys, indexes, column types, constraints
- SQL query execution — read-only transactions by default, preventing accidental data modification
- Hybrid search — combines vector similarity with BM25 and MMR for advanced retrieval
- Embedding generation — generate vector embeddings from text using AI models
- Natural language agent CLI — query your database in plain English without writing SQL
- Web UI — React-based interface with AI-powered chat for database interaction
- Custom tools via YAML — define your own MCP tools backed by PL/pgSQL or PL/Python
- Docker support — complete containerized deployment
- TLS, token authentication, and connection pooling for production use

**Setup:**
```json
{
  "mcpServers": {
    "pgedge-postgres": {
      "command": "pgedge-postgres-mcp",
      "args": ["--config", "/path/to/config.yaml"]
    }
  }
}
```

pgEdge uses a YAML configuration file for database connections, authentication, and custom tool definitions. Docker deployment is also available via `docker compose up`.

**Why it wins:** Three things set pgEdge apart. First, it works with any Postgres — not just one vendor's managed service. If you're on RDS, self-hosted, or any other Postgres provider, pgEdge connects without requiring a specific platform. Second, the hybrid search (BM25 + MMR + vector similarity) is unique among database MCP servers — useful for RAG applications where you want both keyword and semantic matching. Third, custom YAML tool definitions let you expose stored procedures and complex queries as named MCP tools without writing Go or Python.

**The catch:** The GitHub repo had 91 stars at last count — far less community validation than Postgres MCP Pro (2,400 stars). The GA announcement came April 2, 2026, so production track record is minimal. The Go-based server requires building from source or using Docker (no simple `npx` or `pip install`). Enterprise features like distributed Postgres and multi-region failover require pgEdge Cloud.

**Best for:** Teams running PostgreSQL on any provider who want hybrid search, natural language querying, and custom tool definitions. Especially useful for organizations that need to connect to multiple Postgres databases across different environments (dev/staging/production).

### For Analytics: MotherDuck DuckDB MCP

**[MotherDuck DuckDB MCP](https://github.com/motherduckdb/mcp-server-motherduck)** is the official DuckDB server, backed by MotherDuck. If your workload is analytical — aggregations, joins across large datasets, Parquet/CSV ingestion — DuckDB is purpose-built for it.

**What it offers:**
- SQL execution against local DuckDB files, in-memory databases, S3-hosted databases, or MotherDuck cloud
- Read-only by default, `--read-write` flag for write access
- Results limited to 1,024 rows / 50,000 chars by default (configurable)
- Native support for Parquet, CSV, and JSON file formats
- DuckDB's analytical SQL extensions (window functions, QUALIFY, LIST aggregates)

**Setup:**
```json
{
  "mcpServers": {
    "duckdb": {
      "command": "uvx",
      "args": ["mcp-server-motherduck"]
    }
  }
}
```

Set the `MOTHERDUCK_TOKEN` environment variable for MotherDuck cloud access, or use a local `.duckdb` file path.

**Why it wins:** DuckDB handles analytical queries that would bring SQLite to its knees. SUM over a million rows, GROUP BY across ten columns, joins between Parquet files on S3 — these are DuckDB's bread and butter. The MCP server inherits all of this with sensible defaults (read-only, row limits).

### For Multiple Databases: DBHub

**[DBHub](https://github.com/bytebase/dbhub)** (Bytebase) takes a different approach: one MCP server for all your databases. PostgreSQL, MySQL, MariaDB, SQL Server, SQLite — all through a single interface.

**What it offers:**
- Two tools: `execute_sql` and `search_objects` — deliberately minimal for token efficiency
- Multi-connection support via TOML configuration — connect to dev, staging, and production simultaneously
- Zero external dependencies
- Built-in web interface for debugging and query inspection
- Works with Claude Desktop, Claude Code, Cursor, VS Code, Copilot CLI

**Setup:**
```json
{
  "mcpServers": {
    "dbhub": {
      "command": "npx",
      "args": ["-y", "@bytebase/dbhub", "--dsn", "postgresql://user:pass@host/db"]
    }
  }
}
```

For multiple databases, use a TOML config file:
```toml
[[database]]
name = "production"
dsn = "postgresql://user:pass@prod-host/mydb"

[[database]]
name = "staging"
dsn = "postgresql://user:pass@staging-host/mydb"

[[database]]
name = "local-sqlite"
dsn = "sqlite:///path/to/local.db"
```

**Why it wins:** If your agent needs to touch more than one database — cross-reference production and staging, migrate data between MySQL and Postgres, query a local SQLite cache alongside a remote Postgres instance — DBHub handles all of it without running five separate MCP servers.

### For Enterprise Oracle: Oracle Autonomous AI Database MCP

**[Oracle Autonomous AI Database MCP Server](https://www.oracle.com/autonomous-database/mcp-server/)** is the first enterprise database vendor to ship MCP as a built-in, managed feature of its cloud database. Announced March 2026, it supports Oracle Database 19c and 26ai on Autonomous Database Serverless — no separate MCP infrastructure to deploy or maintain.

**What it offers:**
- Schema discovery — agents discover permitted schemas and objects through MCP endpoints
- SQL execution — run queries enforced by Oracle's existing database security policies (VPD, Database Vault, Data Redaction)
- Select AI Agent integration — define custom tools that the MCP server exposes to AI agents and clients
- Multi-tenant architecture — each database instance runs its own MCP endpoint
- Enterprise auditing — all MCP interactions are logged through Oracle's unified audit trail
- Compatible with Claude Desktop, OCI AI Agent, and other MCP clients

**Why it matters:** This is the first time a major enterprise database vendor has embedded MCP directly into the database engine. There's no separate server to deploy, no Docker container to manage, no npm package to keep updated. The MCP endpoint is part of the database instance itself. Oracle's security policies apply automatically — if a user can't see a column through SQL, they can't see it through MCP either.

**The catch:** Oracle-only. This requires Oracle Autonomous Database Serverless on OCI — it doesn't work with on-premises Oracle, Oracle on AWS/Azure RDS, or any other database. Oracle licensing costs are substantially higher than alternatives. Documentation is still early (GA announced March 2026).

**Best for:** Organizations already running Oracle Autonomous Database that want AI agent access governed by their existing security policies. The zero-deployment model is genuinely attractive for enterprises where spinning up additional infrastructure requires procurement cycles.

### For MariaDB: MariaDB MCP (Official)

**[MariaDB MCP](https://github.com/MariaDB/mcp)** is MariaDB's official MCP server, shipped as part of the MariaDB Enterprise Platform 2026 release. It covers standard SQL operations and — unusually for a relational database MCP server — native vector search.

**What it offers:**
- Database and table discovery with metadata
- Schema inspection (detailed column info, indexes, constraints)
- SQL query execution with parameterized queries
- EXPLAIN plan analysis for performance tuning
- Vector store management — create vector tables, batch insert embeddings, semantic similarity search
- Built-in security: SQL injection prevention, read-only mode, connection pooling, query timeouts, result size limits

**Setup:**
```json
{
  "mcpServers": {
    "mariadb": {
      "command": "npx",
      "args": ["-y", "@mariadb/mcp"],
      "env": {
        "MARIADB_HOST": "localhost",
        "MARIADB_USER": "your_user",
        "MARIADB_PASSWORD": "your_password",
        "MARIADB_DATABASE": "your_database"
      }
    }
  }
}
```

**Why it wins:** The vector search integration is the standout. No other official relational database MCP server combines SQL operations with native embedding storage and similarity search in one server. If you're building RAG applications on MariaDB, this eliminates the need for a separate vector database MCP server. The security defaults (parameterized queries, timeouts, size limits) are sensible out of the box.

**The catch:** MariaDB-specific — won't work with MySQL despite protocol compatibility (the vector features depend on MariaDB's vector implementation). The GitHub repo is relatively new with limited community adoption compared to alternatives like DBHub or Postgres MCP Pro. Enterprise Platform licensing is required for production vector features.

**Best for:** Teams running MariaDB who want a first-party MCP server, especially those building AI applications that need both SQL queries and vector similarity search in the same database.

### For SQLite Specifically: jparkerweb/mcp-sqlite

**[jparkerweb/mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite)** is the community replacement for the official SQLite server. TypeScript, actively maintained, with structured CRUD operations instead of raw SQL.

**What it offers:**
- Input validation and structured operations (not raw SQL strings)
- Table creation, reading, updating, deleting with proper safeguards
- Schema inspection
- Actively maintained with regular updates

**Why it wins over the official server:** It actually validates inputs. The official server runs whatever SQL you hand it. This one provides structured operations that prevent the "oops, the agent ran DROP TABLE" scenario.

## Feature Comparison

| Feature | [MongoDB MCP](/reviews/mongodb-mcp-server/) | Postgres MCP Pro | pgEdge MCP | Oracle ADB MCP | MariaDB MCP | DuckDB (MotherDuck) | DBHub | jparkerweb/mcp-sqlite |
|---------|------------|-----------------|------------|----------------|-------------|---------------------|-------|----------------------|
| Actively maintained | Yes (1-2 week releases) | Yes | Yes (GA April 2026) | Yes (GA March 2026) | Yes | Yes | Yes | Yes |
| Read-only mode | Yes (opt-in) | Yes (works) | Yes (default) | Yes (policy-based) | Yes | Yes (default) | Yes | N/A |
| Schema inspection | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Query execution | MongoDB queries | SQL | SQL | SQL | SQL | SQL | SQL | Structured CRUD |
| Performance analysis | Performance Advisor, explain | EXPLAIN, index tuning | No | No | EXPLAIN | No | No | No |
| Health checks | Atlas alerts | Yes | No | No | No | No | No | No |
| Cloud management | Atlas (full) | No | pgEdge Cloud | OCI (built-in) | No | MotherDuck | No | No |
| Multi-database | No (MongoDB only) | No | Yes (YAML config) | No | No | No | Yes | No |
| Vector/hybrid search | Yes (with embeddings) | No | Yes (BM25+MMR+vector) | No | Yes (native) | No | No | No |
| Safety guardrails | Read-only mode, maxTimeMS | Yes | Read-only default, TLS, token auth | Database policies, audit | Parameterized queries, timeouts | Row/char limits | Yes | Input validation |
| Managed/hosted | No (local) | No (local) | Optional (pgEdge Cloud) | Yes (built-in to ADB) | No (local) | No (local) | No (local) | No (local) |
| Tool count | 40+ | ~10 | 5+ custom YAML tools | Custom (Select AI Agent) | ~8 | ~3 | 2 | ~5 |

## Our Recommendations

### You have a PostgreSQL database → Postgres MCP Pro

No contest. It's the most capable database MCP server available — query execution, EXPLAIN analysis, index tuning, health checks. The configurable access modes (restricted vs. unrestricted) give you actual safety controls. If you're doing anything with PostgreSQL, this is the one to install.

### You have PostgreSQL on any provider → pgEdge MCP

If your Postgres is on RDS, Azure, Google Cloud SQL, or self-hosted and you want more than just SQL queries — hybrid search, natural language querying, custom YAML-defined tools — pgEdge is the most feature-rich option that isn't tied to a specific platform. The April 2026 GA release makes it production-ready, though community adoption is still early.

### You're doing data analysis → DuckDB (MotherDuck)

If your agent is analyzing data — running aggregations, processing CSVs or Parquet files, building reports — DuckDB is the right engine. It's an order of magnitude faster than SQLite or Postgres for analytical workloads, and the MCP server has sensible defaults (read-only, output limits) that prevent runaway queries.

### You work across multiple databases → DBHub

If your workflow spans databases — maybe you're comparing staging vs. production, or your data lives in both MySQL and Postgres — DBHub's single-server-multiple-connections approach saves you from managing five separate MCP configurations. The trade-off is fewer specialized features (no EXPLAIN, no health checks), but the convenience is real.

### You need local SQLite → jparkerweb/mcp-sqlite

For quick local database work — prototyping, caching, small datasets — this is the SQLite MCP server to use. Input validation keeps agents from accidentally destroying data, and it's actively maintained.

### You use Oracle Autonomous Database → Oracle ADB MCP

The zero-deployment model is the differentiator. MCP is built into the database instance — no servers to manage, no packages to update, and Oracle's security policies (VPD, Database Vault, Data Redaction) apply automatically to all MCP interactions. The trade-off is Oracle lock-in and licensing costs.

### You use MariaDB → MariaDB MCP

The official first-party server with a unique feature: native vector search alongside standard SQL. If you're building RAG or similarity search on MariaDB, this consolidates what would otherwise require two separate MCP servers (one for SQL, one for vectors) into one.

### You're learning MCP → Official SQLite (read the code, don't run it)

The official SQLite server is still worth reading as a learning resource. The insight memo pattern, the schema-first workflow, the clean Python code — it's a good example of MCP server architecture. Just don't use it for anything real.

## Decision Flowchart

**What database engine are you using?**

- **MongoDB** → [MongoDB MCP](/reviews/mongodb-mcp-server/) (4/5, 40+ tools)
- **PostgreSQL (Neon)** → [Neon MCP](/reviews/neon-mcp-server/)
- **Supabase (full backend)** → [Supabase MCP](/reviews/supabase-mcp-server/)
- **PostgreSQL (self-hosted/RDS/other, needs hybrid search/NLP)** → pgEdge MCP
- **PostgreSQL (self-hosted/RDS/other, needs performance tuning)** → Postgres MCP Pro
- **Oracle (Autonomous Database)** → Oracle Autonomous AI Database MCP (managed, zero-deploy)
- **MariaDB** → MariaDB MCP (official, with vector search)
- **SQLite** → jparkerweb/mcp-sqlite
- **DuckDB** → MotherDuck DuckDB MCP
- **MySQL / SQL Server** → DBHub
- **Multiple databases** → DBHub

**What's your primary use case?**

- **Cloud Postgres with AI workflows** → [Neon MCP](/reviews/neon-mcp-server/) (branch-based migrations)
- **Full Supabase backend management** → [Supabase MCP](/reviews/supabase-mcp-server/) (database + edge functions + storage)
- **Querying a production database** → Postgres MCP Pro (restricted mode)
- **Data analysis / reporting** → DuckDB (MotherDuck)
- **Development / prototyping** → DBHub or jparkerweb/mcp-sqlite
- **MongoDB + Atlas management** → [MongoDB MCP](/reviews/mongodb-mcp-server/) (provisioning, queries, performance optimization)
- **Database performance tuning** → Postgres MCP Pro or Neon MCP (both have EXPLAIN + tuning)
- **Vector search / RAG** → [Chroma MCP](/reviews/chroma-mcp-server/) (3.5/5, 13 tools, four deployment modes) or [Qdrant MCP](/reviews/qdrant-mcp-server/) (3/5, if you need remote MCP transport). See our [full vector database comparison](/guides/best-vector-database-mcp-servers/) for Pinecone, Milvus, and more.
- **Learning MCP** → Read the official SQLite server's source code

## The Bottom Line

The official database MCP servers served their purpose as reference implementations — they showed what was possible. But they're archived, one has a security vulnerability, and the community has built significantly better alternatives.

For most developers in 2026, the answer depends on your database. **MongoDB MCP** (4/5) leads in raw capability with 40+ tools covering the full provisioning-to-optimization lifecycle — the most comprehensive database MCP server available. **Neon MCP** (4/5) is the best Postgres experience — branch-based migrations, OAuth, 20 tools. **Supabase MCP** (4/5) is the choice if you want one server for your entire backend — database, edge functions, storage, and debugging. **Postgres MCP Pro** is the pick for PostgreSQL performance tuning (EXPLAIN, index analysis, health checks). **pgEdge MCP** (GA April 2026) is the most deployment-flexible PostgreSQL option — works with any Postgres v14+, adds hybrid search (BM25+MMR+vector), natural language querying, and custom YAML tool definitions. **Oracle Autonomous AI Database MCP** is the enterprise play — managed MCP built into the database instance with zero deployment. **MariaDB MCP** is notable for combining SQL and vector search in one official server. **DuckDB** for analytics. **DBHub** for multi-database support. The ecosystem has matured past reference implementations, and enterprise vendors (Oracle, MariaDB, pgEdge) are now shipping first-party MCP as a standard database feature — a sign that MCP is becoming table stakes for database platforms.

For the full details on the reviewed servers:
- [MongoDB MCP Server Review](/reviews/mongodb-mcp-server/) (4/5)
- [Supabase MCP Server Review](/reviews/supabase-mcp-server/) (4/5)
- [Neon MCP Server Review](/reviews/neon-mcp-server/) (4/5)
- [SQLite MCP Server Review](/reviews/sqlite-mcp-server/) (3/5)
- [PostgreSQL MCP Server Review](/reviews/postgres-mcp-server/) (2.5/5)

