# The SQLite MCP Server — A Good Idea, Now Abandoned (and Vulnerable)

> The official SQLite MCP server lets agents query, write, and inspect SQLite databases.


**At a glance:** 253 stars (servers-archived repo), ~8.4K weekly PyPI downloads, v2025.4.25 (last release April 2025), 6 tools, archived on PyPI, known SQL injection vulnerability (unpatched, now amplified by security research), ~7.4K weekly PulseMCP visitors (#84 globally, ~521K all-time). Part of our **[Databases MCP category](/categories/databases/)**

The SQLite MCP server (`mcp-server-sqlite`) is Anthropic's official reference implementation for giving AI agents database access. It ships six tools for querying, writing, and inspecting SQLite databases, plus a clever "insight memo" feature for accumulating analysis findings. The Python codebase is clean and well-structured — it was one of the original MCP example servers, built to demonstrate how MCP works with databases.

There's a catch: it's been moved to the `servers-archived` repository. No new releases, no security patches, no bug fixes. Worse, a SQL injection vulnerability was publicly disclosed in June 2025, and Anthropic declined to patch it. It still installs and runs — ~13,000 people download it weekly — but you're on your own going forward.

## What's New (April 2026 Update)

**The vulnerability story has been amplified by major security firms.** Trend Micro's original disclosure has now been reinforced by Datadog Security Labs (who published a full SQL injection case study on the sister PostgreSQL MCP server with executable proof-of-concept code) and Akamai (whose MCP security guide found that 43% of popular MCP server implementations contain command injection vulnerabilities). VulnerableMCP.info, a new comprehensive MCP vulnerability database tracking 50 vulnerabilities (13 critical), now catalogs the broader pattern. The key new finding: Anthropic's vulnerable SQLite MCP server was forked over 5,000 times before archival, meaning this unpatched SQL injection code now silently exists inside thousands of downstream agents — many likely in production.

**Downloads spiked then declined.** PyPI downloads surged dramatically in mid-March 2026 (peaking at ~23,600/day), likely driven by the security research publicity. They've since settled to ~8,400 weekly (~241K monthly) — down from ~13,000 weekly at last review. The spike-then-decline pattern suggests many users installed it to test the vulnerability, not for production use.

**Still v2025.4.25 — now nearly a year without a release.** The final version updated the MCP SDK to 1.6.0. Twelve versions were published between November 2024 and April 2025 before archival on May 28-29, 2025. The archived repo remains frozen with no security patches possible.

**DBHub continues to grow as the leading multi-database alternative.** Bytebase's DBHub (2,600 stars, 218 forks, 512 commits) supports PostgreSQL, MySQL, MariaDB, SQL Server, and SQLite through a single zero-dependency, token-efficient interface.

**167+ SQLite MCP server implementations now exist on PulseMCP alone.** jparkerweb/mcp-sqlite reached v1.0.9 (99 stars, April 4 release), sqlite-explorer-fastmcp holds at 92 stars (read-only/safety-focused), and panasenco/mcp-sqlite continues with Datasette-compatible metadata support.

**PulseMCP traffic nearly doubled.** ~7,400 weekly visitors, ~521,000 all-time (+87%), now ranked #84 globally (up from #130). The security research attention appears to be driving discovery — people finding the review while researching MCP vulnerabilities.

## What It Does

The server exposes six tools organized into three categories:

**Query operations:**
- **`read_query`** — Execute SELECT statements. Results come back as an array of objects — clean, structured, easy for agents to reason about.
- **`write_query`** — Execute INSERT, UPDATE, or DELETE statements. Returns the number of affected rows.
- **`create_table`** — Run CREATE TABLE statements to build new tables.

**Schema inspection:**
- **`list_tables`** — Returns all table names in the database.
- **`describe_table`** — Shows column names and types for a given table.

**Analysis:**
- **`append_insight`** — Adds a business insight to a persistent `memo://insights` resource. This is the one unique feature — findings accumulate across the session, building a running analysis document.

There's also a built-in `mcp-demo` prompt that generates sample schemas and data for a given business domain, then guides the agent through an interactive analysis workflow. It's primarily a demo feature, but it shows off how MCP prompts, tools, and resources can work together.

## Setup

For Claude Desktop, add this to your config:

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "uvx",
      "args": ["mcp-server-sqlite", "--db-path", "/path/to/your/database.db"]
    }
  }
}
```

Docker is also supported:

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-v", "/path/to/data:/data",
        "mcp/sqlite",
        "--db-path", "/data/database.db"
      ]
    }
  }
}
```

Requirements: Python 3.10+ and `uv` (or pip). The server takes one argument — the path to your SQLite database file. If the file doesn't exist, it creates one. That's it for configuration. There are no other flags, no environment variables, no auth options.

**Setup difficulty: Very easy.** One command, one argument. The simplest database MCP server to get running. The lack of configuration options is both a feature and a limitation.

## What Works Well

**Schema inspection before querying is the right pattern.** An agent can call `list_tables` and `describe_table` to understand the database structure before writing any SQL. This is how humans approach an unfamiliar database, and it works naturally in agent workflows. The two-step pattern (inspect, then query) produces better SQL than blind querying.

**The insight memo is a genuinely clever feature.** The `append_insight` tool and `memo://insights` resource let the agent build up a running document of findings during a data analysis session. This is useful for the pattern where you want an agent to explore a dataset and report what it finds — the memo accumulates insights rather than losing them to conversation history. It's a good demonstration of how MCP resources can maintain state.

**The codebase is clean and educational.** If you're learning how to build MCP servers, this is one of the best examples to study. The Python code is straightforward, well-organized, and demonstrates tools, resources, and prompts working together. It's a reference implementation that actually reads like one.

**Read and write in one server.** Unlike some community alternatives that limit agents to read-only access, this server gives full read/write capability. For prototyping, local development, and data exploration, that's what you want — you can create tables, insert test data, and query it all in one session.

## What Doesn't Work Well

**Known SQL injection vulnerability — unpatched.** The server concatenates unsanitized table names directly into SQL via f-strings. Trend Micro publicly disclosed this in June 2025. The attack chain is worse than typical SQL injection: a stored payload in database fields can trigger prompt injection when an AI agent reads the data, potentially hijacking the agent. Anthropic declined to fix it, pointing to the archived status. This is now the single biggest reason not to use this server with any data you care about.

**It's archived — and that's the dealbreaker for production use.** The server was moved to `modelcontextprotocol/servers-archived` on May 28-29, 2025. The repository description says these are "reference MCP servers that are no longer maintained." No security patches. No compatibility updates as the MCP spec evolves. No bug fixes. The server still installs and runs today, but every month it falls further behind.

**No safety guardrails at all.** Any SQL the agent generates gets executed. There's no query validation, no allowlist of operations, no confirmation step for destructive statements. `DROP TABLE`? Runs immediately. `DELETE FROM users`? Done. For a reference implementation meant to teach MCP concepts, this is understandable. For anything touching real data, it's a liability.

**One database per server instance.** You configure a single database path at startup and that's what you get. If your agent needs to query multiple databases, you need multiple server instances with separate configurations. There's no mid-session switching, no multi-database support.

**No connection pooling or concurrent access handling.** This is a single-user, single-connection server. Fine for local development and demos. Not designed for any scenario where multiple agents or processes might touch the same database.

**Limited client compatibility.** While the server technically works over stdio with any MCP client, it was primarily tested and documented for Claude Desktop. Community reports suggest inconsistent behavior with Cursor, VS Code, and other clients.

## Compared to Alternatives

**vs. Bytebase DBHub (2,600 stars):** The leading multi-database MCP server, actively maintained with 512 commits. Supports PostgreSQL, MySQL, MariaDB, SQL Server, and SQLite through a single zero-dependency, token-efficient interface. If you need database MCP access today, DBHub is the strongest general-purpose choice.

**vs. jparkerweb/mcp-sqlite (99 stars, v1.0.9):** A community-built JavaScript alternative that provides comprehensive SQLite operations with better safety features, including input validation and structured CRUD operations (not raw SQL). Actively maintained with the latest release on April 4, 2026. If you specifically want SQLite MCP access, this is the better choice.

**vs. sqlite-explorer-fastmcp (92 stars):** A read-only SQLite MCP server built with FastMCP. Takes the opposite approach to safety — agents can only read, never write. Good for analytical workloads where you want to prevent accidental data modification. Built-in query validation and parameterized queries add another safety layer.

**vs. Postgres MCP Server:** If you're choosing a database MCP server for a real project, PostgreSQL is probably the better database choice. More features, better concurrency, actual access controls. Note: the official Postgres MCP server also has a SQL injection vulnerability (now documented in a full Datadog Security Labs case study) — use Postgres MCP Pro by crystaldba (2,300+ stars) or Neon MCP instead.

**vs. MotherDuck DuckDB MCP Server (141 stars):** For analytical workloads — which is what the SQLite MCP server's "insight memo" feature targets — DuckDB is purpose-built for OLAP queries. Faster on large datasets, native Parquet/CSV support, better analytical SQL extensions. Now includes read-write mode toggle and over 95% functional correctness in text-to-SQL tasks. If data analysis is your primary use case, DuckDB is the sharper tool.

## Who Should Use This

**Yes, use it if:**
- You're learning MCP and want to study a clean, well-structured reference implementation
- You want a quick demo of database access through MCP — the `mcp-demo` prompt makes this nearly zero-effort
- You're prototyping an idea and need disposable local database access for an agent (on throwaway data only)
- You want to understand how MCP tools, resources, and prompts work together

**Don't use it if:**
- You're building anything that will run in production
- Your database contains data you can't afford to lose (no safety guardrails + known SQL injection)
- You need ongoing maintenance, security patches, or MCP spec compatibility
- You need multi-database support or concurrent access
- You want a database MCP server you can rely on long-term
- You're handling any user-supplied or untrusted data (SQL injection risk)

{{< verdict rating="2.5" summary="A good demo with a serious security flaw" >}}
The SQLite MCP server still does what a reference implementation should: it demonstrates how MCP can connect agents to databases in a clean, readable way. The insight memo feature is genuinely clever, the schema inspection workflow is the right pattern, and the codebase is worth studying if you're building your own MCP server. But the picture has gotten worse since our initial review. A publicly disclosed SQL injection vulnerability — with a particularly dangerous stored-prompt-injection attack chain — went unpatched, and Anthropic declined to fix it. Combined with the archived status and zero safety guardrails, the rating drops from 3/5 to 2.5/5. For actual SQLite work with agents, use jparkerweb/mcp-sqlite or Bytebase DBHub. For serious database workloads, consider Neon MCP, Postgres MCP Pro, or DuckDB. The official SQLite MCP server is now a cautionary tale as much as a teaching tool.
{{< /verdict >}}

*Disclosure: We do not test MCP servers hands-on. This review is based on documentation analysis, GitHub repository data, community reports, and publicly available information. All claims should be verified against the official repository and documentation.*

*This review was last updated on 2026-04-19 using Claude Opus 4.6 (Anthropic).*

