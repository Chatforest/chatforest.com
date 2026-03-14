---
title: "The PostgreSQL MCP Server — Read-Only Protection That Wasn't"
date: 2026-03-14T01:06:39+09:00
description: "Anthropic's official Postgres MCP server promises read-only database access. But it's archived, has a SQL injection vulnerability, and the read-only protection doesn't actually work. Here's the honest review."
og_description: "Archived, vulnerable to SQL injection, and the read-only protection is bypassable. The official Postgres MCP server is a cautionary tale. Rating: 2.5/5."
content_type: "Review"
card_description: "Anthropic's official Postgres MCP server advertises safe read-only access. A SQL injection vulnerability bypasses it completely, and it's archived with no fix. Our lowest rating yet."
---

The PostgreSQL MCP server (`@modelcontextprotocol/server-postgres`) is Anthropic's official reference implementation for connecting AI agents to PostgreSQL databases. It advertises read-only access — agents can inspect schemas and run SELECT queries, but can't modify data. That's the promise. The reality is messier: a SQL injection vulnerability lets attackers bypass the read-only protection entirely, and the server was archived in May 2025 with no security patches forthcoming.

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

**vs. Postgres MCP Pro (crystaldba/postgres-mcp):** The community replacement that does everything the official server should have. 2,300+ GitHub stars. Eight tools including schema exploration, query execution, EXPLAIN analysis, health checks, and index tuning. Configurable read-only mode that actually works. Supports prepared statements. Uses `pg_stat_statements` and `hypopg` for performance analysis. If you need a Postgres MCP server today, this is the one to use.

**vs. pgEdge Postgres MCP Server:** Enterprise-oriented alternative supporting multiple simultaneous database connections. Useful for workflows spanning dev, staging, and production databases. Connects to standard community Postgres, Amazon RDS, and other managed providers (v14+).

**vs. AWS Aurora Postgres MCP Server:** Amazon's official server for Aurora. Multiple endpoint support, LLM-prompted connection management. Purpose-built for the AWS ecosystem.

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

**Instead, use:** [Postgres MCP Pro](https://github.com/crystaldba/postgres-mcp) for general Postgres access. It does everything the official server tried to do, correctly, with additional capabilities on top.

{{< verdict rating="2.5" summary="A broken promise, now abandoned" >}}
The PostgreSQL MCP server's entire value proposition is read-only database access. That protection doesn't work — a straightforward SQL injection bypasses it completely. The server was archived in May 2025 with no fix to the npm package that still gets 21,000 weekly downloads. As a piece of code to study, it demonstrates MCP resource patterns well. As a tool to actually use, it's a cautionary tale about trusting security boundaries in reference implementations. The MCP ecosystem has matured past this server — Postgres MCP Pro, pgEdge, and the cloud provider servers are all better choices. Our lowest rating yet, because a security tool that gives false confidence is worse than no security tool at all.
{{< /verdict >}}
