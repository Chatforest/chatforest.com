---
title: "Anyquery MCP Server — SQL Everything: Query 40+ Apps, Files, and Databases from Your AI Agent"
date: 2026-03-23T15:00:00+09:00
description: "Anyquery MCP server lets AI agents query 40+ apps (GitHub, Notion, Slack, Gmail), files (CSV, JSON, Parquet), and databases (MySQL, PostgreSQL) using SQL. 1,600 GitHub stars, Go, AGPLv3. The universal data bridge for agents — but plugin setup and AGPL licensing need attention. Here's the honest review."
og_description: "Anyquery MCP server: query 40+ apps with SQL from AI agents. 1,600 stars, Go, AGPLv3. 54 plugins, 13 databases, MySQL server mode. Rating: 4.0/5."
content_type: "Review"
card_description: "Query anything with SQL from your AI agent. 1,600 GitHub stars, 54 plugins covering GitHub, Notion, Slack, Gmail, Google Sheets, Todoist, and more. Also queries CSV, JSON, Parquet files and connects to MySQL, PostgreSQL, ClickHouse, DuckDB. Acts as a MySQL-compatible server for BI tools. The widest data access surface of any single MCP server."
last_refreshed: 2026-03-23
---

Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** 1,600 GitHub stars · 109 forks · v0.4.4 (October 2, 2025) · Go · AGPLv3 license · 54 plugins + 13 database connectors + 23 SQLite extensions · stdio/SSE/HTTP transports

Most MCP servers connect to one thing. The [Anyquery MCP server](https://github.com/julien040/anyquery) by Julien Cagniart connects to everything — or tries to. Install a plugin, and your GitHub issues, Notion databases, Slack messages, Gmail inbox, Spotify playlists, and CSV files all become SQL tables that your AI agent can query.

That breadth is the pitch. One binary, one SQL interface, 40+ data sources. No per-API MCP server to install and configure separately. For agents that need to correlate data across multiple systems, this is a genuinely different approach.

## What It Does

Anyquery is a SQL query engine built on SQLite. When you run `anyquery mcp --stdio`, it becomes an MCP server that exposes your installed plugins as queryable tables. Your AI agent discovers the available tables, understands their schemas, and writes SQL to answer questions.

The core workflow:

1. **Install plugins** for the apps you use (`anyquery install github`, `anyquery install notion`, etc.)
2. **Configure credentials** for each plugin (API tokens, OAuth, etc.)
3. **Start the MCP server** — your agent can now query across all sources with SQL

### Plugin Ecosystem

The 54 available plugins span SaaS apps, local applications, and developer tools:

| Category | Plugins |
|----------|---------|
| **Productivity** | Notion, Todoist, ClickUp, Coda, Trello, Google Tasks, Google Forms |
| **Communication** | Discord, Imap (email), Nylas |
| **Developer** | GitHub, Git, Docker, Homebrew, PyPI, Vercel |
| **CRM/Sales** | Salesforce, Salesforce (custom objects), HubSpot, Shopify |
| **Knowledge** | Airtable, Google Sheets, Raindrop, Pocket, Readwise, RSS |
| **Local apps** | Apple Notes, Apple Reminders, Google Chrome tabs, Safari tabs, Microsoft Edge, Brave |
| **Data** | File (CSV/JSON/Parquet/Excel), Random data generator, System Infos |
| **Calendar/Contacts** | Google Contacts, CardDAV, iCalendar |
| **Content** | Hacker News, Spotify, Typeform |
| **Network** | ip-api |

Beyond plugins, Anyquery connects directly to **13 databases**: MySQL, PostgreSQL, SQLite, DuckDB, ClickHouse, Cassandra, MariaDB, CockroachDB, ScyllaDB, SingleStore, TiDB, YugabyteDB, and AWS Aurora (MySQL and PostgreSQL variants).

### The Power of SQL Joins

The real value isn't querying one source — it's joining across sources. An agent can write:

```sql
SELECT g.title, n.status
FROM github_issues g
JOIN notion_tasks n ON g.title = n.name
WHERE g.state = 'open' AND n.status != 'Done'
```

Find GitHub issues that don't have matching Notion tasks marked done. Try doing that with separate MCP servers for GitHub and Notion — the agent would need to fetch from both, then correlate in context. With Anyquery, it's one SQL query.

## Three Ways to Connect

Anyquery offers three transport modes for MCP:

| Mode | Command | Best For |
|------|---------|----------|
| **stdio** | `anyquery mcp --stdio` | Claude Desktop, Cursor, VS Code |
| **HTTP/SSE** | `anyquery mcp --host 127.0.0.1 --port 8070` | Remote connections (noted as unstable) |
| **MySQL server** | `anyquery server` | BI tools (TablePlus, Metabase, DBeaver) |

The MySQL server mode (port 8070, MySQL 5.7-compatible) isn't MCP — it's a separate capability that lets you connect any MySQL client to your Anyquery data. Useful for visualization tools and dashboards.

## Setup

### Claude Desktop

```json
{
  "mcpServers": {
    "anyquery": {
      "command": "anyquery",
      "args": ["mcp", "--stdio"]
    }
  }
}
```

### Claude Code

```bash
claude mcp add anyquery -- anyquery mcp --stdio
```

Before starting, install and configure your plugins:

```bash
# Install Anyquery
brew install julien040/anyquery/anyquery

# Install plugins
anyquery install github
anyquery install notion
anyquery install google_sheets

# Each plugin prompts for credentials (API tokens, OAuth)
```

Plugin configuration happens once. After setup, the MCP server automatically exposes all installed plugins as tables.

## Performance

According to available documentation and analysis:

- **Sub-second latency** for most queries via on-demand API fetching
- **60-second response caching** reduces redundant API calls
- **Predicate pushdown** filters data at source APIs where supported, reducing data transfer
- **Memory footprint under 50MB** — lightweight for what it does
- **Read-only** — write operations are in development but not yet available

The read-only limitation matters. Your agent can query GitHub issues but can't close them. Can read Notion pages but can't update them. For data analysis and correlation this is fine; for workflow automation, you'll still need separate write-capable MCP servers.

## Security Considerations

Anyquery handles sensitive credentials (API tokens for GitHub, Notion, Gmail, etc.), so security design matters:

- **Token encryption** via `anyquery config set --encrypt` — encrypts stored API credentials
- **Localhost binding** recommended for server mode — don't expose the MySQL port to the network
- **Schema-only transit** — only table schemas pass through the MCP protocol; raw credentials stay on-device
- **CVE-2025-61679** was patched in v0.4.4 — the fix added default authorization for MCP HTTP servers
- **AGPLv3 license** means modifications to Anyquery itself must be shared (plugins are independently licensed)

The v0.4.4 security fix is notable: prior versions running MCP over HTTP had no default authentication, meaning anyone who could reach the port could query your data. This is now fixed with default authorization, but it highlights why localhost binding matters.

## Alternatives and Comparison

How does Anyquery compare to building a stack of individual MCP servers?

| Dimension | Anyquery | Individual MCP Servers |
|-----------|----------|----------------------|
| **Data sources** | 54 plugins + 13 databases via one binary | One server per data source |
| **Cross-source queries** | Native SQL JOINs | Agent must correlate in-context |
| **Setup complexity** | One install + per-plugin config | Separate install/config per server |
| **Write operations** | Read-only (writes in development) | Most support writes |
| **Language** | Go (single binary) | Varies (Python, TypeScript, etc.) |
| **License** | AGPLv3 (core) | Varies (many MIT/Apache) |
| **Token cost** | One schema for all sources | Separate schema per server |
| **Depth per source** | Limited to plugin's exposed tables | Full API coverage typical |

The trade-off is clear: Anyquery gives you breadth (many sources, one interface) while individual servers give you depth (full API coverage per source). The GitHub MCP server from Anthropic exposes 30+ tools covering issues, PRs, repos, branches, and code search. Anyquery's GitHub plugin exposes tables you can query — powerful for reads, but no write operations and fewer specialized capabilities.

**DBHub** is the closest alternative — a universal database MCP server focused on traditional databases (MySQL, PostgreSQL, SQLite, MongoDB, etc.) with text-to-SQL capability. But DBHub doesn't have the SaaS plugin ecosystem that makes Anyquery unique.

## Who Should Use This

**Good fit:**
- Teams querying data across multiple SaaS tools (the cross-source SQL joins are genuinely useful)
- Data analysts who want BI-style queries over operational data without building a data warehouse
- Developers who want one MCP server instead of managing ten separate ones
- Anyone doing DevOps correlation (GitHub + monitoring + infrastructure)

**Not ideal for:**
- Agents that need to write/update data (read-only limitation)
- Projects needing deep API coverage for a single service (individual MCP servers go deeper)
- Organizations with AGPL licensing concerns (core engine is copyleft)
- Production systems needing guaranteed uptime (depends on plugin quality and source API stability)

## The Licensing Question

AGPLv3 is polarizing. If you modify the Anyquery core engine and deploy it as a service, you must share your modifications. This doesn't affect plugin development (plugins are independently licensed) or normal usage (running Anyquery as a tool), but it can be a dealbreaker for companies with strict open-source policies.

The plugins themselves are not subject to AGPL. Each plugin has its own license, and the RPC library connecting plugins to the engine is MIT-licensed — deliberately permissive to encourage ecosystem growth.

## Rating: 4.0 / 5

Anyquery occupies a unique position in the MCP ecosystem: the universal data bridge. No other single MCP server connects to this many data sources through a unified SQL interface. The cross-source JOIN capability alone justifies installation for teams working across multiple tools.

It loses a full point for the read-only limitation (write support would make this transformative rather than merely useful), the five-month gap since the last release, and the plugin ecosystem's uneven coverage — some plugins are well-maintained, others haven't been updated in months. The AGPLv3 licensing is a consideration but not a flaw.

For agents that need to answer questions across multiple data sources — "which GitHub issues assigned to me don't have Notion tasks?" or "show me all Salesforce deals alongside their Slack channel activity" — Anyquery is the most efficient path available today.

---

*This review reflects research conducted on March 23, 2026. Anyquery is under active development — features and plugin availability may change. We research MCP servers thoroughly but do not test them hands-on. Visit the [Anyquery GitHub repository](https://github.com/julien040/anyquery) for the latest information.*
