# MotherDuck & DuckDB MCP Server — Analytical SQL for AI Agents, from Local Files to Cloud Warehouse

> MotherDuck's official MCP server connects AI agents to DuckDB databases — local files, S3, or the MotherDuck cloud warehouse. Read-only by default, actively maintained, both hosted and self-hosted options.


Part of our **[Data & Analytics MCP category](/categories/data-analytics/)**.

*At a glance: 468 GitHub stars, 80 forks, 215 commits, MIT license, Python, v1.0.4 (March 30, 2026). 5 tools (local) / expanded toolset (remote). Read-only by default. Supports local DuckDB files, in-memory, S3, MotherDuck cloud. PyPI ~39.5K downloads/week. PulseMCP ~438K all-time visitors (#100 globally, ~15.5K weekly). MotherDuck is a $400M-valued company ($100M raised). Also: ktanaka101/mcp-server-duckdb community server has 174 stars but 2.8M PulseMCP all-time visitors (#18 globally, 1.7M weekly).*

DuckDB has become the default embedded analytical database — 30,000+ GitHub stars, embedded in data pipelines everywhere, and the go-to choice for local SQL analytics. MotherDuck, the company behind DuckDB's cloud offering, provides the official MCP server that connects AI agents to DuckDB's analytical engine across multiple deployment targets: local files, in-memory databases, S3-hosted data, and MotherDuck's managed cloud warehouse.

The server comes in two forms. The **local open-source server** ([motherduckdb/mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck)) runs on your machine and gives you full control over configuration and database connections. The **remote managed server** runs on MotherDuck's infrastructure with zero setup, sandboxed compute, and built-in visualization features. Both speak MCP, but they serve different audiences — the local server is for developers who want DuckDB analytics in their IDE, and the remote server is for teams who want a managed analytics layer their AI agents can query.

## What It Does

**Local server tools:**
- `execute_query` — runs SQL queries using DuckDB dialect, returning results in a structured format
- `list_databases` — enumerates available databases (useful for MotherDuck or multi-database setups)
- `list_tables` — displays tables and views within specified schemas
- `list_columns` — shows column definitions for targeted tables or views
- `switch_database_connection` — changes the active database connection (requires `--allow-switch-databases` flag)

**Remote server additional capabilities:**
- `query` — read-only SQL execution
- `query_rw` — SQL with write access (create tables, save derived data)
- Schema exploration with table relationships and documentation
- **Dives** — AI-generated interactive visualizations from composable SQL
- Catalog search and documentation queries

## Setup

**Local server (open-source):**

```bash
pip install mcp-server-motherduck
```

```json
{
  "mcpServers": {
    "motherduck": {
      "command": "uvx",
      "args": ["mcp-server-motherduck", "--db-path", "my_database.db"]
    }
  }
}
```

For MotherDuck cloud connections, set `--db-path md:` and authenticate via `motherduck_token` environment variable. For S3: `--db-path s3://bucket/path/file.db`.

**Remote server (managed):**

Available through MotherDuck's platform with zero local installation. Connects via Claude, ChatGPT, Gemini, Cursor, and other MCP-compatible clients. Routes automatically based on region.

**Key flags:**
- `--read-write` — enables write operations (default is read-only)
- `--allow-switch-databases` — enables the switch_database_connection tool
- `--init-sql` — execute SQL on startup (note: [only first statement executes](https://github.com/motherduckdb/mcp-server-motherduck/issues/79) when passing a file with multiple statements)

## What's Good

**Read-only by default is the right call.** Unlike many database MCP servers that hand agents full write access, MotherDuck requires an explicit `--read-write` flag to enable mutations. This means a misconfigured agent can't accidentally DROP a table or corrupt data. It's a simple design decision that eliminates an entire class of failure modes.

**Dual deployment model is genuinely flexible.** The local server handles everything from a single Parquet file to a multi-database MotherDuck warehouse. The remote server adds managed compute, sandboxed execution, and visualization. You can start local and move to managed without changing your workflow patterns. Few MCP servers offer this kind of deployment flexibility.

**Active maintenance with clean releases.** Five releases in two months (v1.0.0 through v1.0.4, February to March 2026), each focused and well-scoped. Dependabot PRs are current. Only 1 open issue. 61 closed PRs show consistent community engagement. This is one of the better-maintained database MCP servers in the ecosystem.

**DuckDB's analytical SQL is a genuine advantage.** DuckDB handles Parquet, CSV, JSON, and Arrow files natively. It can query S3 directly. It supports window functions, CTEs, and complex analytical queries that would require loading data into a separate system with most other lightweight databases. Your agent inherits all of this capability through a single `execute_query` tool.

**Strong company backing.** MotherDuck has raised $100M at a $400M valuation, with backing from Andreessen Horowitz, Felicis, and Redpoint. The MCP server is part of their core product strategy — it's on their product page, has dedicated documentation, and ships with their remote managed offering. This isn't a side project.

**SQL traceability on the remote server.** Every answer shows the exact query that was run. This matters for trust and auditability — when an agent says "revenue grew 23%," you can verify the underlying SQL rather than trusting a black box.

## What's Not

**MotherDuck's pricing shifted unfavorably.** The $25/month Lite plan was eliminated in early 2026. The free tier (10GB, limited compute) is functional for prototyping but constrained. The Business plan jumped to $250/month. If you're using the remote managed server, you're on MotherDuck's platform pricing. The local open-source server with plain DuckDB files avoids this entirely, but you lose the managed features.

**The local server has a limited tool count.** Five tools is minimal. There's no schema visualization, no query explanation, no data profiling, no export capabilities. Compare this to [Datadog MCP](/reviews/datadog-mcp-server/) (80+ tools) or [PagerDuty MCP](/reviews/pagerduty-mcp-server/) (67 tools). The argument is that a single `execute_query` tool with DuckDB's capable SQL engine can handle most analytics tasks — and that's true — but richer schema exploration tools would reduce the SQL the agent needs to generate.

**No formal security audit or hardening documentation.** The README doesn't discuss SQL injection prevention, query timeouts, result size limits (configurable at 1,024 rows / 50,000 characters but not audited), or sandboxing. The `--read-write` flag is all-or-nothing — there's no per-table or per-schema permission model. For a database access tool, this is a gap. The remote server's "hypertenancy" with isolated compute is better, but the local server runs with whatever filesystem permissions your MCP client has.

**The `--init-sql` bug is a minor but telling issue.** [Issue #79](https://github.com/motherduckdb/mcp-server-motherduck/issues/79) reports that `--init-sql` only executes the first SQL statement when given a file with multiple statements. This is the only open issue, so it's not a pattern, but initialization scripts are a common DuckDB pattern for loading extensions and setting configurations.

**PyPI downloads are modest relative to DuckDB's popularity.** At ~39.5K downloads/week, the MotherDuck MCP server is well-adopted but represents a tiny fraction of DuckDB's overall user base. DuckDB's Python package gets millions of downloads weekly. The MCP server hasn't yet become a default part of DuckDB-based workflows.

**DuckDB supply chain incident is contextually relevant.** In September 2025, the official DuckDB npm packages (148K weekly downloads) were [compromised via phishing](https://www.aikido.dev/blog/duckdb-npm-packages-compromised) — malicious versions attempted cryptocurrency wallet draining. This didn't affect the MCP server (which is Python/PyPI, not npm), but it's a reminder that supply chain attacks target popular database packages. The MotherDuck MCP server's PyPI package has not been compromised, and dependency updates via Dependabot are current.

## How It Compares

| Feature | MotherDuck MCP | ktanaka101 DuckDB | SQLite MCP | Snowflake MCP | Tinybird MCP |
|---------|---------------|-------------------|------------|---------------|--------------|
| **Type** | Local + Remote | Local only | Local only | Local/Remote | Remote only |
| **Maintained** | Official (MotherDuck) | Community | Archived | Official | Official |
| **Stars** | 468 | 174 | 253 (archived) | N/A | 80 (archived) |
| **PulseMCP weekly** | 15.5K | 1.7M | 7.4K | N/A | 110 |
| **Tools** | 5 (local) / 7+ (remote) | 1 | 6 | 10+ | 6 + dynamic |
| **Read-only default** | Yes | Optional | No | Yes | N/A |
| **Write support** | Flag-gated | Flag-gated | Always | Flag-gated | Via API |
| **Free local use** | Yes | Yes | Yes | No | No |
| **Cloud option** | MotherDuck | No | No | Snowflake | Tinybird |
| **Last release** | Mar 2026 | May 2025 | Archived | N/A | Hosted |

**ktanaka101/mcp-server-duckdb** is the elephant in the room. Despite having only 174 GitHub stars and a single `query` tool, it's the #18 most-visited MCP server on PulseMCP (2.8M all-time, 1.7M weekly — currently #2 this week). This likely reflects DuckDB's massive popularity driving search traffic rather than actual installations (PyPI shows only ~145 downloads/week). The server hasn't been updated since May 2025 (v1.1.0), making it effectively unmaintained. If you want a minimal, single-tool DuckDB MCP server, it works, but the MotherDuck server is the actively maintained choice.

**[SQLite MCP](/reviews/sqlite-mcp-server/)** is the closest local-only comparison. It's simpler but archived, has known SQL injection vulnerabilities, and lacks DuckDB's analytical capabilities (Parquet support, S3 access, window functions). DuckDB is strictly more capable for analytical workloads.

**[Tinybird MCP](/reviews/tinybird-mcp-server/)** offers a similar managed analytics approach but is tightly coupled to Tinybird's ClickHouse platform. MotherDuck's dual local/remote model is more flexible — you can use DuckDB locally for free and only adopt the cloud when you need it.

The **duckdb_mcp** community extension ([teaguesterling/duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp)) takes a different approach — it extends DuckDB itself to act as an MCP resource provider. This is architecturally interesting but early-stage and less practical than a standalone MCP server for most workflows.

## The Bigger Picture

MotherDuck's MCP server sits at an interesting intersection. DuckDB is arguably the most natural database for AI agent workflows — it's embeddable, handles diverse file formats natively, runs analytical SQL without infrastructure, and scales from a laptop to a cloud warehouse. The MCP server makes all of this accessible through a standard protocol.

The dual deployment model (local open-source + remote managed) is the right architecture. It lets individual developers query local Parquet files in their IDE while enterprises connect agents to a managed warehouse with sandboxed compute and audit trails. The read-only default is a simple but important safety decision. The release cadence (five releases in two months) shows genuine investment.

The main gap is depth. Five tools for the local server means the agent is doing most of the work through raw SQL generation. Richer schema exploration, query explanation, and data profiling tools would reduce the burden on the LLM and improve reliability. The remote server is more capable (Dives visualizations, documentation queries, schema relationships) but requires a MotherDuck account.

The ktanaka101 community server's PulseMCP dominance (1.7M weekly visitors, #2 this week) despite being unmaintained since May 2025 tells a clear story: developers want DuckDB MCP access, and the community server got there first. MotherDuck's official server is the better long-term choice — actively maintained, more tools, cloud integration — but it entered the market later and hasn't yet captured the community mindshare that ktanaka101's server holds on discovery platforms.

No MotherDuck MCP-specific CVEs have been reported. The read-only default reduces risk for typical usage. The DuckDB npm compromise of September 2025 did not affect the MCP server (different language/registry), but the incident underscores the importance of supply chain security in the DuckDB ecosystem.

## Rating: 4/5

MotherDuck's DuckDB MCP server earns a 4/5 for being an actively maintained, well-designed database MCP server with a strong safety default (read-only), flexible deployment options (local + remote), and solid company backing ($100M raised, $400M valuation). It loses points for a limited local tool count (5 tools), no granular permission model beyond all-or-nothing write access, minimal security documentation, and MotherDuck's pricing shift that eliminated the affordable paid tier. The dual local/remote architecture is a genuine differentiator — few MCP servers let you start with free local files and scale to a managed cloud warehouse.

**Use this if:** You work with DuckDB for analytics, data engineering, or ad hoc querying and want your AI agents to have safe, read-only SQL access to local files, S3 data, or a MotherDuck warehouse.

**Skip this if:** You need a full-featured database admin MCP (consider [Postgres MCP](/reviews/postgres-mcp-server/) or [Supabase MCP](/reviews/supabase-mcp-server/)), want a lightweight single-tool server (ktanaka101's community server still works), or need write-heavy transactional database access rather than analytical queries.

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic). We did not hands-on test this server — our analysis is based on public documentation, GitHub repositories, PyPI data, PulseMCP metrics, and community reports. Last edited 2026-04-20.*

