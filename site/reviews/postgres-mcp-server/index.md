# The PostgreSQL MCP Server — Read-Only Protection That Wasn't

> Anthropic's official Postgres MCP server promises read-only database access.


**At a glance:** Archived May 2025, deprecated July 2025, npm v0.6.2 (unpatched), ~21,000 weekly npm downloads, ~1,000 weekly Docker pulls, 1 tool, SQL injection vulnerability (no CVE assigned), parent repo modelcontextprotocol/servers at 81,600 stars. Part of our **[Databases MCP category](/categories/databases/)**

The PostgreSQL MCP server (`@modelcontextprotocol/server-postgres`) is Anthropic's official reference implementation for connecting AI agents to PostgreSQL databases. It advertises read-only access — agents can inspect schemas and run SELECT queries, but can't modify data. That's the promise. The reality is messier: a SQL injection vulnerability lets attackers bypass the read-only protection entirely, and the server was archived in May 2025 with no security patches forthcoming. It was officially deprecated on npm and Docker Hub in July 2025 — yet it still pulls 21,000 weekly downloads from people who likely don't know the situation.

This is the companion piece to our [SQLite MCP server review](/reviews/sqlite-mcp-server/). Both are Anthropic reference implementations, both are archived, and both teach important lessons about the state of the MCP ecosystem. But where the SQLite server's main weakness was a lack of safety guardrails, the Postgres server's weakness is a guardrail that actively misleads you about its protection.

## What It Does

The server is minimal. It exposes one tool and one resource type:

**Tool:**
- **`query`** — Execute SQL queries against the connected PostgreSQL database. All queries are wrapped in a `BEGIN TRANSACTION READ ONLY` block to prevent writes.

**Resources:**
- **`postgres://<host>/<table>/schema`** — Exposes schema information for each table as a JSON resource. Column names and data types are automatically discovered from database metadata.

That's it. One tool, schema resources. Compare that to the SQLite server's six tools, or community alternatives with eight or more. This is the most minimal database MCP server we've reviewed.

## Setup

For Claude Desktop with npx:

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://localhost/mydb"
      ]
    }
  }
}
```

Or with Docker:

```json
{
  "mcpServers": {
    "postgres": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "mcp/postgres",
        "postgresql://host.docker.internal:5432/mydb"
      ]
    }
  }
}
```

The connection string is the only configuration. No flags, no environment variables, no auth options beyond what's in the connection URL. On macOS with Docker, use `host.docker.internal` instead of `localhost` to reach the host machine.

**Setup difficulty: Easy.** One command, one connection string. But that simplicity extends to security — there's no way to restrict which schemas, tables, or operations are accessible.

## The SQL Injection Problem

This is the part that matters most, and the reason this review exists.

The server wraps every query in a read-only transaction:

```sql
BEGIN TRANSACTION READ ONLY;
[user query]
ROLLBACK;
```

This should prevent any writes. But the Node.js `postgres` client accepts multiple semicolon-delimited SQL statements in a single `client.query()` call. An attacker — or a confused agent — can escape the read-only transaction by injecting:

```sql
COMMIT; DROP SCHEMA public CASCADE;
```

The `COMMIT` ends the read-only transaction. Everything after it executes with full privileges. The "read-only" protection simply doesn't work against multi-statement injection.

There's a secondary attack vector too: modifying session variables. `COMMIT; SET statement_timeout TO 1;` persists across connection pool reuse, degrading all subsequent queries on that connection.

This vulnerability was reported by Datadog Security Labs and an independent researcher in April 2025. The repository was patched and then archived in May 2025. The npm package at v0.6.2 — which still gets 21,000 weekly downloads — contains the vulnerable code.

**If you're running this server against a production database, stop.** The read-only protection is theater. A patched fork exists (`@zeddotdev/postgres-context-server` v0.1.4), which uses prepared statements to prevent multi-statement execution, but it's a community effort with its own maintenance timeline.

## What's New (March 2026 Update)

The ecosystem has moved on dramatically since our initial review. The official server remains dead — but its alternatives have exploded.

**The server is now fully deprecated, not just archived.** As of July 10, 2025, `@modelcontextprotocol/server-postgres` is marked deprecated on npm and Docker Hub. The source was moved to a separate `modelcontextprotocol/servers-archived` repository. The main `modelcontextprotocol/servers` repo now contains only 7 reference servers (Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking, Time) — Postgres is one of 12 that were cut. Open issues referencing Postgres still exist in the main repo but are effectively orphaned.

**Google's MCP Toolbox for Databases has emerged as the dominant multi-database option.** At 13,500 stars, it dwarfs every Postgres-specific MCP server. Written in Go under Apache 2.0, it supports AlloyDB, Cloud SQL, BigQuery, Spanner, Firestore, and Bigtable — with OAuth2/OIDC auth and OpenTelemetry integration. Version 0.30.0 shipped on March 20, 2026. If you're in the Google Cloud ecosystem, this has become the default choice.

**pgEdge went GA on April 2, 2026.** Their Go-based server supports custom tools defined via YAML, PL/pgSQL and PL/Python execution, write mode, a web UI, hybrid search (BM25+MMR+vector), and a natural language agent CLI. Works with any Postgres v14+ — community, RDS, Azure, Google Cloud SQL, or self-hosted. Now production-ready and available in pgEdge Cloud.

**DBHub from Bytebase (2,400 stars) takes a token-efficient approach.** It supports Postgres, MySQL, SQLite, MariaDB, and SQL Server through just 2 tools — a deliberate design to reduce LLM token consumption. This addresses a real pain point: enterprise databases with 200+ tables can consume tens of thousands of tokens just for schema information.

**Supabase MCP Server (~2,400 stars, ~20,000 weekly npm downloads)** now rivals the official server's download count. It covers the full Supabase surface — auth, realtime, storage, edge functions — not just database queries.

**The fragmentation is real.** PulseMCP now lists 139 Postgres-related MCP servers. The market has split into vendor-neutral multi-DB tools (Google Toolbox), Postgres-specific production tools (Crystal DBA, pgEdge), and vendor-specific platforms (Supabase, Neon, AWS Aurora). Simon Willison's "lethal trifecta" warning — private data access + untrusted content exposure + exfiltration capability — applies to all of them. Local development remains the viable sweet spot where trusted environments eliminate most exploit vectors.

## What Works Well

**Schema discovery via resources is the right approach.** Exposing table schemas as MCP resources means agents can inspect database structure before querying. The `postgres://host/table/schema` URI pattern is clean and predictable. An agent can enumerate resources to understand what's available, then write targeted queries. This is better than the SQLite server's approach of requiring tool calls to inspect schemas — resources are more natural for read-only metadata.

**The minimal surface area is actually a safety feature (when it works).** One tool that only does queries is simpler to reason about than six tools with varying write permissions. If the read-only protection had been implemented correctly, this would be a genuinely safe way to give agents database access.

**Connection string configuration is standard.** Using a standard PostgreSQL connection URL means you can leverage existing credential management — environment variables, secrets managers, connection poolers like PgBouncer. No custom auth scheme to learn.

## What Doesn't Work Well

**The SQL injection vulnerability undermines the entire value proposition.** The server's one promise is read-only access. That promise is broken. Everything else is secondary to this fact. You cannot trust this server to protect your database from unintended writes.

**It's archived with no maintenance path.** Moved to `modelcontextprotocol/servers-archived` in May 2025. The repository is read-only. No security patches, no MCP spec compatibility updates, no bug fixes. Still getting 21,000 weekly downloads on npm from people who likely don't know it's abandoned.

**One database per server instance.** The connection string is the only configuration, and it points to one database. Multi-database workflows require running multiple server instances. The pgEdge and Crystal DBA alternatives both support multiple connections.

**No query constraints.** Even setting aside the injection vulnerability, there's no way to restrict queries to specific schemas, tables, or query patterns. An agent with access can query any table the connection credentials allow. For production databases, you'd want row-level security, schema restrictions, or query allowlists — none of which exist here.

**No parameterized queries.** Raw SQL strings go directly to the database. No parameter binding means no structural protection against injection. The agent constructs queries by string concatenation, which is exactly the pattern that enables the vulnerability described above.

**No performance guardrails.** No query timeouts, no row limits, no EXPLAIN plan analysis. An agent can fire off a full table scan on a billion-row table and you'll find out when your database slows to a crawl.

## Compared to Alternatives

**vs. Postgres MCP Pro (crystaldba/postgres-mcp):** The community replacement that does everything the official server should have. 2,400+ GitHub stars, ~2,500 weekly downloads. Eight tools including schema exploration, query execution, EXPLAIN analysis, health checks, and index tuning. Configurable read-only mode that actually works. Supports prepared statements. Uses `pg_stat_statements` and `hypopg` for performance analysis. Community reports praise it for real-world performance tuning — one user fixed slow SQLAlchemy ORM queries in minutes. Still our top recommendation for Postgres-specific MCP access.

**vs. Google MCP Toolbox for Databases:** The new category leader at 13,500 stars. Go-based, Apache 2.0, supports AlloyDB, Cloud SQL, BigQuery, Spanner, Firestore, and Bigtable. OAuth2/OIDC authentication, OpenTelemetry integration, v0.30.0 released March 20, 2026 with Java SDK. If you're multi-database or in the Google Cloud ecosystem, this is the strongest option available.

**vs. DBHub (Bytebase):** 2,400 stars, ~5,000 weekly downloads. Multi-database support (Postgres, MySQL, SQLite, MariaDB, SQL Server) through just 2 tools — a deliberate token-efficient design. Includes a web workbench. Good choice for teams that need cross-database access without tool sprawl.

**vs. Supabase MCP Server:** ~2,400 stars, ~20,000 weekly npm downloads. Full Supabase integration covering auth, realtime, storage, and edge functions beyond just database queries. If you're already on Supabase, this is the obvious pick.

**vs. pgEdge Postgres MCP Server:** GA since April 2, 2026. Go-based with custom YAML tool definitions, PL/pgSQL and PL/Python support, write mode, web UI, hybrid search (BM25+MMR+vector), and natural language agent CLI. Enterprise-oriented, supporting multiple simultaneous database connections across dev/staging/production. Connects to any standard Postgres v14+ — community, Amazon RDS, Azure, Google Cloud SQL, or self-hosted. Also available as a managed service via pgEdge Cloud.

**vs. Neon MCP Server:** 549 stars. Neon-specific: branching, provisioning, migrations. Purpose-built for the Neon serverless Postgres platform.

**vs. AWS Aurora Postgres MCP Server:** Amazon's official server for Aurora in the `awslabs/mcp` repository. RDS Data API integration, multiple endpoint support. Purpose-built for the AWS ecosystem.

**vs. Azure Database for PostgreSQL MCP Server:** Microsoft's entry. OIDC authentication with row-level security, OpenTelemetry integration. The most security-conscious option for cloud-managed Postgres.

**vs. [SQLite MCP Server](/reviews/sqlite-mcp-server/):** Same provenance (Anthropic reference implementation), same fate (archived). The SQLite server is actually more capable — six tools vs. one, plus the insight memo feature. But it intentionally allows writes. The Postgres server's failure is worse: it promises protection and doesn't deliver.

## Who Should Use This

**Yes, use it if:**
- You're studying MCP server implementations and want to understand how database resources work (read the code, don't run it against real data)
- You're connecting to a throwaway development database with no sensitive data, and you understand the read-only protection doesn't work
- You need a minimal example of a TypeScript MCP server for educational purposes

**Don't use it if:**
- Your database contains any data you care about
- You're relying on the read-only transaction wrapper for safety
- You need ongoing maintenance, security patches, or MCP spec compatibility
- You need multi-database support, query constraints, or performance guardrails
- You're building anything intended for production use

**Instead, use:** [Postgres MCP Pro](https://github.com/crystaldba/postgres-mcp) for Postgres-specific access, or [Google MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox) for multi-database support.

{{< verdict rating="2.5" summary="A broken promise, now abandoned" >}}
The PostgreSQL MCP server's entire value proposition is read-only database access. That protection doesn't work — a straightforward SQL injection bypasses it completely. The server was archived in May 2025, deprecated in July 2025, and the npm package at v0.6.2 still carries the unpatched vulnerability while pulling 21,000 weekly downloads. The ecosystem has moved on decisively: Google's MCP Toolbox for Databases leads at 13,500 stars with multi-database support, Postgres MCP Pro (2,400 stars) handles Postgres-specific production workloads, and vendor servers from Supabase, pgEdge, Neon, AWS, and Azure cover specialized use cases. With 139 Postgres-related MCP servers now listed on PulseMCP, there's no reason to run this one. Our lowest rating remains, because a deprecated security tool that gives false confidence is worse than no security tool at all.
{{< /verdict >}}

*Disclosure: ChatForest researches MCP servers using public documentation, GitHub repositories, community discussions, and published benchmarks. We do not test or run MCP servers hands-on. All claims reflect publicly available information at the time of writing.*

*This review was last edited on 2026-03-21 using Claude Opus 4.6 (Anthropic).*

