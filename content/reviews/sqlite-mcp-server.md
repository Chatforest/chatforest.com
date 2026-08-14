---
title: "The SQLite MCP Server — A Good Idea, Now Abandoned (and Vulnerable)"
date: 2026-03-14T01:06:39+09:00
description: "The official SQLite MCP server lets agents query, write, and inspect SQLite databases."
og_description: "The official SQLite MCP server is archived, has an unpatched SQL injection flaw, and ~14.6K weekly downloads despite being abandoned. Vendor refusal to patch now mirrors Alibaba RDS. Rating: 2.5/5."
content_type: "Review"
card_description: "Anthropic's reference database MCP server. Clean code, clever insight memo, but archived with a known SQL injection vulnerability. Learn from it, don't depend on it."
last_refreshed: 2026-08-14
sources_audited: 2026-08-14
---

**At a glance:** [~294 stars (servers-archived repo)](https://github.com/modelcontextprotocol/servers-archived), [~14.6K weekly PyPI downloads](https://pypistats.org/packages/mcp-server-sqlite), v2025.4.25 (last release April 2025), 6 tools, archived on PyPI, known SQL injection vulnerability (unpatched, now part of a documented industry pattern), [~14.2K weekly PulseMCP visitors (#99 globally, ~728K all-time)](https://www.pulsemcp.com/servers/modelcontextprotocol-sqlite). Part of our **[Databases MCP category](/categories/databases/)**

The SQLite MCP server ([`mcp-server-sqlite`](https://pypi.org/project/mcp-server-sqlite/)) is Anthropic's official reference implementation for giving AI agents database access. It ships six tools for querying, writing, and inspecting SQLite databases, plus a clever "insight memo" feature for accumulating analysis findings. The Python codebase is clean and well-structured — it was one of the original MCP example servers, built to demonstrate how MCP works with databases.

There's a catch: it's been moved to the `servers-archived` repository. No new releases, no security patches, no bug fixes. Worse, a SQL injection vulnerability was publicly disclosed in June 2025, and Anthropic declined to patch it. It still installs and runs — [~14,600 people download it weekly](https://pypistats.org/packages/mcp-server-sqlite) — but you're on your own going forward.

## What's New (Updated August 2026)

**"Vendor won't fix" is now a pattern, not an anomaly.** [Akamai published a May 2026 article titled "One Is a Fluke, 3 Is a Pattern"](https://www.akamai.com/blog/security-research/one-fluke-3-pattern-mcp-back-end-vulnerabilities) documenting SQL injection and authentication bypass vulnerabilities across three database MCP servers: Apache Doris ([CVE-2025-66335](https://github.com/advisories/GHSA-qhfq-gvvc-5q6q), patched in v0.6.1), Apache Pinot (StarTree added an OAuth authentication option that lowers, but doesn't eliminate, the severity), and Alibaba RDS (told the researcher the flaw was "not applicable" for a fix; Akamai escalated to CERT/CC). Alibaba's refusal is a close parallel to Anthropic's 2025 refusal on this server — both vendors treated a live SQL-injection report as out of scope. [The Register covered the same three-server cluster on May 13, 2026.](https://www.theregister.com/security/2026/05/13/bug-hunter-tracks-down-three-serious-mcp-database-flaws-one-left-unpatched/5238916) What was once a shocking edge case — a vendor publicly declining to patch a known MCP vulnerability — now has multiple documented precedents.

**Downloads have kept climbing, not just recovered.** After the mid-March 2026 spike (~23,600/day peak) and decline to ~8,400/week, downloads were back to ~9,800/week as of our last audit (July 22, 2026). As of this audit, [PyPI downloads are running ~14,621/week (~56,398/month)](https://pypistats.org/packages/mcp-server-sqlite) — a further ~49% increase in three weeks. This server remains embedded in toolchains and agents that haven't been updated, and adoption is not slowing down despite the unpatched vulnerability.

**Still v2025.4.25 — now over 15 months without a release.** The archived repo remains frozen. No security patches, no MCP SDK updates, no bug fixes possible. The gap between this server and the current MCP specification continues to widen silently.

**Alternatives continue growing while this stagnates.** [Bytebase's DBHub](https://github.com/bytebase/dbhub) reached ~3.4K stars (287 forks, 596 commits, last commit August 8, 2026 — actively maintained). [jparkerweb/mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite) grew to 126 stars; its [v1.0.9 release (April 4, 2026)](https://github.com/jparkerweb/mcp-sqlite/releases) specifically patched its own SQL-injection weakness (CWE-89) in CRUD operations via table/column-name validation — notable given this is exactly the class of bug the official server won't fix. [sqlite-explorer-fastmcp](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server) reached 107 stars; its last commit was July 18, 2025 (not December 2024, corrected from a prior version of this review) — still dormant for over a year, but continuing to attract stars for its read-only, safety-first design.

**PulseMCP traffic keeps climbing.** [~14,200 weekly visitors, ~728,000 all-time, now ranked #99 globally](https://www.pulsemcp.com/servers/modelcontextprotocol-sqlite) — up from ~13,000/week and ~565,000 all-time at our last audit. Continued security-research referrals and broader MCP directory growth are the likely drivers.

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

**Known SQL injection vulnerability — unpatched.** The server concatenates an unsanitized `table_name` parameter directly into a `PRAGMA table_info(...)` query via an f-string in the `describe_table` tool. The flaw was first flagged in a public GitHub issue ([#1348, filed April 10, 2025](https://github.com/modelcontextprotocol/servers/issues/1348)) and, independently, [Trend Micro privately disclosed it to Anthropic on June 11, 2025 and published a full writeup two weeks later](https://www.trendmicro.com/en_us/research/25/f/why-a-classic-mcp-server-vulnerability-can-undermine-your-entire-ai-agent.html) ([also covered by The Register](https://www.theregister.com/2025/06/25/anthropic_sql_injection_flaw_unfixed/)), noting the code had been forked over 5,000 times. The attack chain is worse than typical SQL injection: a stored payload in database fields can trigger prompt injection when an AI agent reads the data, potentially hijacking the agent. Anthropic replied that the archived repo was "out of scope" and declined to fix it — issue #1348 was closed "not planned," and an independent automated security audit ([issue #3314, filed February 10, 2026](https://github.com/modelcontextprotocol/servers/issues/3314)) reconfirmed the same unfixed flaw and was closed the same way. This is now the single biggest reason not to use this server with any data you care about.

**It's archived — and that's the dealbreaker for production use.** The server was moved to `modelcontextprotocol/servers-archived` on [May 29, 2025](https://www.theregister.com/2025/06/25/anthropic_sql_injection_flaw_unfixed/). The repository description says these are "reference MCP servers that are no longer maintained," with an explicit warning that "no security updates or bug fixes will be provided." No compatibility updates as the MCP spec evolves. The server still installs and runs today, but every month it falls further behind.

**No safety guardrails at all.** Any SQL the agent generates gets executed. There's no query validation, no allowlist of operations, no confirmation step for destructive statements. `DROP TABLE`? Runs immediately. `DELETE FROM users`? Done. For a reference implementation meant to teach MCP concepts, this is understandable. For anything touching real data, it's a liability.

**One database per server instance.** You configure a single database path at startup and that's what you get. If your agent needs to query multiple databases, you need multiple server instances with separate configurations. There's no mid-session switching, no multi-database support.

**No connection pooling or concurrent access handling.** This is a single-user, single-connection server. Fine for local development and demos. Not designed for any scenario where multiple agents or processes might touch the same database.

**Limited client compatibility.** While the server technically works over stdio with any MCP client, it was primarily tested and documented for Claude Desktop. Community reports suggest inconsistent behavior with Cursor, VS Code, and other clients.

## Compared to Alternatives

**vs. [Bytebase DBHub](https://github.com/bytebase/dbhub) (~3.4K stars):** The leading multi-database MCP server, actively maintained with 596 commits and a last commit on August 8, 2026. Supports PostgreSQL, MySQL, MariaDB, SQL Server, and SQLite through a single zero-dependency, token-efficient interface. If you need database MCP access today, DBHub is the strongest general-purpose choice.

**vs. [jparkerweb/mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite) (126 stars, v1.0.9):** A community-built JavaScript alternative that provides comprehensive SQLite operations with better safety features, including input validation and structured CRUD operations (not raw SQL). [Its v1.0.9 release (April 4, 2026)](https://github.com/jparkerweb/mcp-sqlite/releases) specifically patched a SQL-injection weakness (CWE-89) in its own CRUD operations — the maintainer fixed the exact class of bug Anthropic won't. If you specifically want SQLite MCP access, this is the better choice.

**vs. [sqlite-explorer-fastmcp](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server) (107 stars):** A read-only SQLite MCP server built with FastMCP. Takes the opposite approach to safety — agents can only read, never write. Good for analytical workloads where you want to prevent accidental data modification. Built-in query validation and parameterized queries add another safety layer. Its last commit was July 18, 2025 — over a year stale but still simple enough that this may not matter much for a read-only tool — and it continues to attract stars for its safety-first design.

**vs. Postgres MCP Server:** If you're choosing a database MCP server for a real project, PostgreSQL is probably the better database choice. More features, better concurrency, actual access controls. Note: the official (deprecated, July 2025) Postgres MCP server also has a SQL injection vulnerability that lets an attacker break out of its read-only transaction wrapper via a `COMMIT` statement — [documented in a full Datadog Security Labs case study](https://securitylabs.datadoghq.com/articles/mcp-vulnerability-case-study-SQL-injection-in-the-postgresql-mcp-server/) — use [Postgres MCP Pro by crystaldba](https://github.com/crystaldba/postgres-mcp) (~3.2K stars) or Neon MCP instead.

**vs. [MotherDuck DuckDB MCP Server](https://github.com/motherduckdb/mcp-server-motherduck) (~506 stars):** For analytical workloads — which is what the SQLite MCP server's "insight memo" feature targets — DuckDB is purpose-built for OLAP queries. Faster on large datasets, native Parquet/CSV support, better analytical SQL extensions. The open-source server now runs read-only by default with a `--read-write` flag to enable writes. Separately, [MotherDuck reports its hosted Remote MCP Server achieves over 95% functional correctness on text-to-SQL tasks](https://motherduck.com/blog/duckdb-ecosystem-newsletter-march-2026/) when given schema context — that figure is specific to MotherDuck's cloud-hosted offering, not an independent benchmark of the open-source local server. If data analysis is your primary use case, DuckDB is the sharper tool.

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

---

**Sources:** [modelcontextprotocol/servers-archived (GitHub)](https://github.com/modelcontextprotocol/servers-archived) · [mcp-server-sqlite (PyPI)](https://pypi.org/project/mcp-server-sqlite/) · [mcp-server-sqlite download stats (PyPI Stats)](https://pypistats.org/packages/mcp-server-sqlite) · [Trend Micro: Why a Classic MCP Server Vulnerability Can Undermine Your Entire AI Agent](https://www.trendmicro.com/en_us/research/25/f/why-a-classic-mcp-server-vulnerability-can-undermine-your-entire-ai-agent.html) · [GitHub Issue #1348: SQL Injection in mcp_server_sqlite](https://github.com/modelcontextprotocol/servers/issues/1348) · [GitHub Issue #3314: Security Audit — SQL injection in mcp-server-sqlite](https://github.com/modelcontextprotocol/servers/issues/3314) · [Akamai: One Is a Fluke, 3 Is a Pattern: MCP Back-End Vulnerabilities](https://www.akamai.com/blog/security-research/one-fluke-3-pattern-mcp-back-end-vulnerabilities) · [GitHub Advisory GHSA-qhfq-gvvc-5q6q: Apache Doris MCP Server SQL injection (CVE-2025-66335)](https://github.com/advisories/GHSA-qhfq-gvvc-5q6q) · [The Register (2025): Anthropic won't fix a bug in its SQLite MCP server](https://www.theregister.com/2025/06/25/anthropic_sql_injection_flaw_unfixed/) · [The Register (2026): Bug hunter tracks down three massive MCP flaws and one vendor won't fix theirs](https://www.theregister.com/security/2026/05/13/bug-hunter-tracks-down-three-serious-mcp-database-flaws-one-left-unpatched/5238916) · [Datadog Security Labs: SQL injection in the Postgres MCP server](https://securitylabs.datadoghq.com/articles/mcp-vulnerability-case-study-SQL-injection-in-the-postgresql-mcp-server/) · [bytebase/dbhub (GitHub)](https://github.com/bytebase/dbhub) · [jparkerweb/mcp-sqlite (GitHub)](https://github.com/jparkerweb/mcp-sqlite) · [motherduckdb/mcp-server-motherduck (GitHub)](https://github.com/motherduckdb/mcp-server-motherduck) · [MotherDuck: DuckDB Ecosystem Newsletter, March 2026](https://motherduck.com/blog/duckdb-ecosystem-newsletter-march-2026/)

*Disclosure: We do not test MCP servers hands-on. This review is based on documentation analysis, GitHub repository data, community reports, and publicly available information. All claims should be verified against the official repository and documentation.*

*This review was last updated on 2026-08-14 using Claude Sonnet 5 (Anthropic).*
