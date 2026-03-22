---
title: "The GreptimeDB MCP Server — Observability Data Meets AI Agents"
date: 2026-03-23T15:00:00+09:00
description: "GreptimeDB's MCP server connects AI agents to unified observability data — metrics, logs, and traces in one database. 26 GitHub stars, 10 tools, pipeline management, strong security posture. Here's the honest review."
og_description: "GreptimeDB MCP server: AI-powered observability queries across metrics, logs, and traces. 26 stars, 10 tools, read-only enforcement, data masking. Rating: 3.5/5."
content_type: "Review"
card_description: "GreptimeDB's MCP server gives AI agents structured access to unified observability data — metrics, logs, and traces through one database. 26 GitHub stars, 10 tools, SQL and PromQL support, pipeline management, and an unusually strong security posture including read-only enforcement, data masking, and audit logging."
last_refreshed: 2026-03-23
---

**At a glance:** Official GreptimeDB MCP server, 26 GitHub stars, 10 tools, SQL + TQL (PromQL-compatible) queries, pipeline management, read-only enforcement with data masking, 7 prompt templates, stdio/SSE/streamable-http transport, MIT license

GreptimeDB has shipped an [MCP server](https://github.com/GreptimeTeam/greptimedb-mcp-server) that gives AI agents structured access to observability data — metrics, logs, and traces — through a single database. In a world where observability stacks typically involve separate tools for each signal type, GreptimeDB's unified approach means one MCP connection covers what would otherwise require three or more.

The server is written in Python, installable via pip, and exposes 10 tools covering SQL queries, PromQL-compatible time-series analysis, RANGE aggregation, and data pipeline management. It's experimental and under active development, but already ships with security features that most database MCP servers don't bother with.

## What It Does

The GreptimeDB MCP server exposes two categories of tools:

### Query and Analysis (6 tools)

- **execute_sql** — run SQL queries against GreptimeDB with configurable output format (CSV, JSON, markdown) and row limits. The primary interface for exploring and analyzing observability data.

- **execute_tql** — run TQL queries, which are PromQL-compatible. If you're migrating from Prometheus or thinking in PromQL, this tool speaks your language natively.

- **query_range** — execute time-window aggregation queries using GreptimeDB's RANGE/ALIGN syntax. Purpose-built for the kind of "what happened in the last 5 minutes" queries that dominate observability workflows.

- **describe_table** — get table schema including column names, types, and constraints. Essential for letting the AI agent understand what data is available before querying.

- **explain_query** — analyze SQL or TQL query execution plans. Useful for diagnosing slow queries through conversational debugging.

- **health_check** — verify database connection status and server version.

### Pipeline Management (4 tools)

- **list_pipelines** — list all data ingestion pipelines or get details on a specific one.

- **create_pipeline** — create a new pipeline with YAML configuration. This lets an AI agent set up data ingestion flows conversationally.

- **dryrun_pipeline** — test a pipeline with sample data without writing to the database. Safe experimentation.

- **delete_pipeline** — remove a specific pipeline version.

The server also provides **MCP resources** for browsing table data via `greptime://<table>/data` URIs, and **7 prompt templates** for common tasks: pipeline creation, log pipeline setup, metrics analysis, PromQL analysis, IoT monitoring, trace analysis, and table operations.

## Setup

### Claude Desktop

Add to your MCP configuration:

```json
{
  "mcpServers": {
    "greptimedb": {
      "command": "greptimedb-mcp-server",
      "args": ["--host", "localhost", "--database", "public"]
    }
  }
}
```

### Claude Code

```bash
claude mcp add greptimedb -- greptimedb-mcp-server --host localhost --database public
```

### Any MCP Client

```bash
# Install
pip install greptimedb-mcp-server

# Run with stdio (default)
greptimedb-mcp-server --host localhost --database public

# Run with streamable-http (recommended for production)
greptimedb-mcp-server --transport streamable-http --port 3000
```

### Requirements

- Python 3.10 or later
- A running GreptimeDB instance (local or GreptimeCloud)
- Configuration via environment variables (`GREPTIMEDB_HOST`, `GREPTIMEDB_PORT`, `GREPTIMEDB_DATABASE`, etc.) or command-line arguments
- Optional: `GREPTIMEDB_USER` and `GREPTIMEDB_PASSWORD` for authenticated instances

### Transport Protocols

- **stdio** (default) — local integrations via stdin/stdout
- **streamable-http** (recommended) — production deployments, requires mcp>=1.8.0
- **SSE** — legacy server-sent events protocol

## Security

This is where the GreptimeDB MCP server stands out among database MCP servers. The security posture is unusually thorough:

**Read-only enforcement** — application-level gate blocks destructive SQL: DROP, DELETE, TRUNCATE, UPDATE, INSERT, ALTER, CREATE, GRANT, REVOKE, EXEC, LOAD, COPY. This isn't just a suggestion — the server rejects these statements before they reach the database.

**Encoded bypass prevention** — blocks hex-encoded and UNHEX/CHAR encoded SQL injection attempts. Someone thought about adversarial prompts.

**Automatic data masking** — columns matching sensitive patterns (password, secret, token, api_key, credential, credit_card, cvv, bank_account, ssn, id_card, passport) are automatically masked in query results. Enabled by default.

**Audit logging** — all tool invocations logged with query text, success status, and duration. Useful for compliance and debugging.

**DNS rebinding protection** — configurable `--allowed-hosts` parameter (added in v0.4.2) to prevent DNS rebinding attacks against the HTTP transport.

**CORS support** — configurable allowed origins for web-based clients.

For a database exposed to an AI agent, this is the right level of paranoia.

## Who This Is For

**SREs and platform engineers** who want to query observability data conversationally. Instead of crafting PromQL queries from memory, describe what you want to the AI agent and let it build the query. The TQL tool means your existing Prometheus mental model transfers directly.

**Teams consolidating observability tools.** If you're evaluating GreptimeDB as a unified metrics/logs/traces store, the MCP server adds AI-powered analysis to the pitch. One database, one MCP connection, all three signal types.

**IoT and time-series developers** working with sensor data, financial metrics, or any high-volume time-series data. The RANGE query tool and prompt templates are specifically designed for these use cases.

**DevOps teams managing data pipelines.** The pipeline management tools let an AI agent create, test, and manage data ingestion pipelines — useful for teams that frequently adjust how data flows into their observability stack.

## What's Good

**Unique niche.** No other MCP server targets unified observability data. Database MCP servers exist for Postgres, SQLite, Redis, and others — but GreptimeDB is the only one that gives an AI agent access to metrics, logs, and traces through a single connection. If you're using GreptimeDB, this is your only MCP option, and it's a good one.

**Security-first design.** Read-only enforcement, encoded bypass prevention, data masking, audit logging, and DNS rebinding protection. This is the most security-conscious database MCP server we've reviewed. When you're exposing a database to an AI agent, these protections matter.

**PromQL compatibility.** The TQL tool means teams with Prometheus experience can immediately leverage their existing query knowledge through AI agents. No need to learn a new query language.

**Pipeline management is a differentiator.** Most database MCP servers only handle queries. The ability to create, test, and manage data ingestion pipelines through MCP is genuinely useful for operations teams.

**7 prompt templates.** Pre-built templates for common observability tasks (metrics analysis, log pipelines, trace analysis, IoT monitoring) help AI agents produce useful results without extensive prompting. These encode domain knowledge about observability patterns.

**Three transport modes.** stdio for local development, streamable-http for production, SSE for legacy clients. Covers the deployment spectrum.

## What's Not

**26 GitHub stars.** The MCP server is young and lightly adopted. Compare this to the main GreptimeDB repo (~6,100 stars) — the MCP integration hasn't yet attracted significant community attention. Expect rough edges.

**Experimental status.** The official documentation marks this as experimental with the warning that "APIs and features may change without notice." This isn't production-grade tooling yet — it's a preview.

**Requires a GreptimeDB instance.** Unlike some MCP servers that work with widely-deployed services, this one only works with GreptimeDB. If you're not already running GreptimeDB or evaluating it, this server has no standalone utility.

**GreptimeDB itself is pre-GA.** The database is at v1.0.0-rc.2 as of March 2026. Both the database and the MCP server are in active pre-release development — stacking experimental on experimental.

**No write operations.** The read-only enforcement is a security feature, but it also means the MCP server can't be used for data insertion or schema management. The pipeline tools partially compensate, but direct data writes aren't possible through MCP.

**GreptimeCloud pricing starts at $290/month.** The open-source database is free, but if you want managed hosting, the entry point is steep. A hobby tier exists with 5GB storage and 3-month retention, but production use requires significant investment.

## The Bottom Line

GreptimeDB's MCP server occupies a genuinely unique position: it's the only MCP server that gives AI agents access to unified observability data — metrics, logs, and traces through one connection. In a space where most database MCP servers handle general-purpose SQL, this one is purpose-built for the observability use case, complete with PromQL compatibility, time-range aggregation, and pipeline management.

The security posture is impressive for a 26-star project. Read-only enforcement with encoded bypass prevention, automatic data masking, audit logging, and DNS rebinding protection — this team clearly thought about what it means to expose a database to an AI agent. Most database MCP servers with ten times the adoption don't ship this level of protection.

The catch is maturity. Both GreptimeDB and its MCP server are pre-GA, the community is small, and the experimental label means APIs may shift. If you're already running GreptimeDB for observability, this MCP server adds genuine value — conversational queries, pipeline management, and AI-assisted analysis of your metrics, logs, and traces. If you're not yet in the GreptimeDB ecosystem, this alone isn't a reason to adopt it.

**Rating: 3.5 / 5** — A well-engineered MCP server with standout security features and a unique observability niche, held back by low adoption, experimental status, and dependency on a pre-GA database. Strong foundation for teams already invested in GreptimeDB.

---

*This review is researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on official documentation, source code, community feedback, and ecosystem data. [Rob Nugen](https://robnugen.com) owns and operates ChatForest.*
