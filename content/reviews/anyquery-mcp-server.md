---
title: "Anyquery MCP Server — SQL Everything: Query 40+ Apps, Files, and Databases from Your AI Agent"
date: 2026-03-23T15:00:00+09:00
description: "Anyquery MCP server lets AI agents query 40+ apps (GitHub, Notion, Discord, Google Sheets), files (CSV, JSON, Parquet), and databases (MySQL, PostgreSQL) using SQL."
og_description: "Anyquery MCP server: query 40+ apps with SQL from AI agents. ~1,750 stars, Go, AGPLv3. 44 plugins, 13 databases, MySQL server mode. Rating: 4.0/5."
content_type: "Review"
card_description: "Query anything with SQL from your AI agent. ~1,750 GitHub stars, 44 plugins covering GitHub, Notion, Discord, Google Sheets, Todoist, and more. Also queries CSV, JSON, Parquet files and connects to MySQL, PostgreSQL, ClickHouse, DuckDB. Acts as a MySQL-compatible server for BI tools. Development resumed mid-2026 after a quiet stretch, with three releases (mostly security patches) between June and August."
last_refreshed: 2026-05-03
sources_audited: 2026-08-16
---

Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** [~1,750 GitHub stars](https://github.com/julien040/anyquery) · [v0.5.0](https://github.com/julien040/anyquery/releases/tag/0.5.0) (August 5, 2026) · Go · AGPLv3 license · 44 plugins + 13 database connectors + 22 SQLite extensions · stdio/SSE/HTTP transports

Most MCP servers connect to one thing. The [Anyquery MCP server](https://github.com/julien040/anyquery) by Julien Cagniart connects to everything — or tries to. Install a plugin, and your GitHub issues, Notion databases, Discord messages, Google Sheets rows, Spotify playlists, and CSV files all become SQL tables that your AI agent can query.

That breadth is the pitch. One binary, one SQL interface, 40+ data sources. No per-API MCP server to install and configure separately. For agents that need to correlate data across multiple systems, this is a genuinely different approach.

## What It Does

Anyquery is a SQL query engine built on SQLite. When you run `anyquery mcp --stdio`, it becomes an MCP server that exposes your installed plugins as queryable tables. Your AI agent discovers the available tables, understands their schemas, and writes SQL to answer questions.

The core workflow:

1. **Install plugins** for the apps you use (`anyquery install github`, `anyquery install notion`, etc.)
2. **Configure credentials** for each plugin (API tokens, OAuth, etc.)
3. **Start the MCP server** — your agent can now query across all sources with SQL

### Plugin Ecosystem

As of this audit (August 2026), [Anyquery's plugin registry](https://registry.anyquery.dev/v0/registry/) lists **44 plugins** spanning SaaS apps, local applications, and developer tools — down from 54 at the March 2026 launch and 47 at the May 2026 refresh, with two new additions (Asana, Atlas Cloud) since then offsetting further removals elsewhere:

| Category | Plugins |
|----------|---------|
| **Productivity** | Notion, Todoist, ClickUp, Coda, Trello, Google Tasks, Google Forms, Asana |
| **Communication** | Discord, Imap (email), Nylas |
| **Developer** | GitHub, Git, Docker, Homebrew, PyPI, Vercel, Atlas Cloud |
| **CRM/Sales** | Salesforce, Salesforce (custom objects), HubSpot, Shopify |
| **Knowledge** | Airtable, Google Sheets, Raindrop, Pocket, Readwise, RSS |
| **Local apps** | Apple Notes, Apple Reminders, Google Chrome tabs, Safari tabs, Microsoft Edge, Brave |
| **Data** | File (CSV/JSON/Parquet/Excel), Random data generator, System Infos |
| **Calendar/Contacts** | Google Contacts, CardDAV, iCalendar |
| **Content** | Hacker News, Spotify, Typeform |
| **Network** | ip-api |

There is no dedicated Slack or Gmail plugin — Gmail access goes through the generic Imap plugin instead, per [Anyquery's own Gmail guide](https://anyquery.dev/integrations/).

Beyond plugins, Anyquery connects directly to [**13 databases**](https://anyquery.dev/docs/database): MySQL, PostgreSQL, SQLite, DuckDB, ClickHouse, Cassandra, MariaDB, CockroachDB, ScyllaDB, SingleStore, TiDB, YugabyteDB, and AWS Aurora (MySQL and PostgreSQL variants).

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

The [MySQL server mode](https://anyquery.dev/docs/usage/mysql-server/) (port 8070 by default) isn't MCP — it's a separate capability that lets you connect any MySQL-protocol client to your Anyquery data. Useful for visualization tools and dashboards.

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

- **Write support is plugin-specific, not universal** — this review's earlier claim that Anyquery is blanket read-only was wrong as of this audit

Coverage varies a lot by plugin. [Notion](https://anyquery.dev/integrations/notion) and [Google Sheets](https://anyquery.dev/integrations/google_sheets) support full `INSERT`/`UPDATE`/`DELETE`. [Todoist](https://anyquery.dev/integrations/todoist) supports `INSERT` and `DELETE` (creating and closing tasks) but not `UPDATE`. [GitHub](https://anyquery.dev/integrations/github) remains explicitly read-only — you can query issues but not close or comment on them. There's no single answer to "can Anyquery write to X" — you have to check each plugin's own docs page before relying on it for workflow automation.

## Security Considerations

Anyquery handles sensitive credentials (API tokens for GitHub, Notion, Gmail, etc.), so security design matters:

- **Token encryption** via `anyquery config set --encrypt` — encrypts stored API credentials
- **Localhost binding** recommended for server mode — don't expose the MySQL port to the network
- **Schema-only transit** — only table schemas pass through the MCP protocol; raw credentials stay on-device
- [v0.4.4](https://github.com/julien040/anyquery/releases/tag/0.4.4) added default authorization for MCP HTTP servers (security fix)
- **AGPLv3 license** means modifications to Anyquery itself must be shared (plugins are independently licensed)

The v0.4.4 fix addressed a real gap: prior versions running MCP over HTTP had no default authentication, meaning anyone who could reach the port could query your data. But that wasn't the last security issue. Since then, [v0.4.5](https://github.com/julien040/anyquery/releases/tag/0.4.5) (June 2026) patched two CVEs ([CVE-2026-50006](https://www.cve.org/CVERecord?id=CVE-2026-50006), [CVE-2026-47253](https://www.cve.org/CVERecord?id=CVE-2026-47253)) by adding server-side sandboxing, [v0.4.6](https://github.com/julien040/anyquery/releases/tag/0.4.6) (July 2026) fixed another advisory ([GHSA-j4wj-p47h-f9cc](https://github.com/julien040/anyquery/security/advisories/GHSA-j4wj-p47h-f9cc)), and [v0.5.0](https://github.com/julien040/anyquery/releases/tag/0.5.0) (August 2026) closed five more advisories, including a sandbox bypass where a crafted `ATTACH DATABASE`/`VACUUM INTO` target could get read-write disk access despite looking like an in-memory database. Read that history as a mixed signal: the maintainer has been responsive, but a single-developer project running with credentials for GitHub, Notion, Gmail-via-IMAP, and more has had a real string of exploitable bugs in 2026. Keep it updated and keep the port off the network.

## Alternatives and Comparison

How does Anyquery compare to building a stack of individual MCP servers?

| Dimension | Anyquery | Individual MCP Servers |
|-----------|----------|----------------------|
| **Data sources** | 44 plugins + 13 databases via one binary | One server per data source |
| **Cross-source queries** | Native SQL JOINs | Agent must correlate in-context |
| **Setup complexity** | One install + per-plugin config | Separate install/config per server |
| **Write operations** | Plugin-dependent (some full read-write, some read-only) | Most support writes |
| **Language** | Go (single binary) | Varies (Python, TypeScript, etc.) |
| **License** | AGPLv3 (core) | Varies (many MIT/Apache) |
| **Token cost** | One schema for all sources | Separate schema per server |
| **Depth per source** | Limited to plugin's exposed tables | Full API coverage typical |

The trade-off is clear: Anyquery gives you breadth (many sources, one interface) while individual servers give you depth (full API coverage per source). [GitHub's own official MCP server](https://github.com/github/github-mcp-server) — not an Anthropic product, contrary to what an earlier version of this review said — exposes well over 100 tools across toolsets like issues, PRs, repos, branches, code security, and code search. Anyquery's GitHub plugin exposes tables you can query — powerful for reads, but read-only and far narrower than the dedicated server.

**[DBHub](https://github.com/bytebase/dbhub)** is the closest alternative — a universal database MCP server (MIT-licensed, ~3,400 stars) focused on traditional databases: MySQL, PostgreSQL, SQL Server, MariaDB, and SQLite. It does not support MongoDB and does not advertise a text-to-SQL feature, contrary to what an earlier version of this review claimed — it exposes typed tools (`execute_sql`, `search_objects`) that still require you to write the SQL yourself. DBHub doesn't have the SaaS plugin ecosystem that makes Anyquery unique.

## Who Should Use This

**Good fit:**
- Teams querying data across multiple SaaS tools (the cross-source SQL joins are genuinely useful)
- Data analysts who want BI-style queries over operational data without building a data warehouse
- Developers who want one MCP server instead of managing ten separate ones
- Anyone doing DevOps correlation (GitHub + monitoring + infrastructure)

**Not ideal for:**
- Agents that need guaranteed write access to a specific source — write support is per-plugin (GitHub is read-only; Notion and Google Sheets are read-write; Todoist is insert/delete only), not a blanket capability, so verify the target plugin first
- Projects needing deep API coverage for a single service (individual MCP servers go deeper)
- Organizations with AGPL licensing concerns (core engine is copyleft)
- Production systems needing guaranteed uptime (depends on plugin quality and source API stability)
- Teams uneasy with a single-maintainer security track record — three releases since June 2026 fixed multiple CVEs and GHSA advisories in a row

## The Licensing Question

AGPLv3 is polarizing. If you modify the Anyquery core engine and deploy it as a service, you must share your modifications. This doesn't affect plugin development (plugins are independently licensed) or normal usage (running Anyquery as a tool), but it can be a dealbreaker for companies with strict open-source policies.

The plugins themselves are not subject to AGPL. Each plugin has its own license, and the RPC library connecting plugins to the engine is MIT-licensed — deliberately permissive to encourage ecosystem growth.

## Rating: 4.0 / 5

*(Corrected back up from the 3.5/5 assigned in the May 2026 refresh — that downgrade's central premise, "no releases since October 2025 / project appears dormant," turned out to be wrong. See below.)*

Anyquery occupies a unique position in the MCP ecosystem: the universal data bridge. No other single MCP server connects to this many data sources through a unified SQL interface. The cross-source JOIN capability alone justifies installation for teams working across multiple tools.

**What this August 2026 audit found:** the "dormant" call in the May 2026 refresh does not hold up. [v0.4.5](https://github.com/julien040/anyquery/releases/tag/0.4.5) shipped June 9, 2026 (two CVEs patched via server sandboxing), [v0.4.6](https://github.com/julien040/anyquery/releases/tag/0.4.6) shipped July 3, 2026 (another security advisory, plus update notifications and faster CLI table streaming), and [v0.5.0](https://github.com/julien040/anyquery/releases/tag/0.5.0) shipped August 5, 2026 (five more advisories closed, new file-format auto-detection, and share-link rewriting for GitHub/GitLab/Hugging Face/Dropbox links). That's three releases in three months — the opposite of dormant. Stars have grown from ~1,600 to ~1,750 over the same window.

The write-operations picture was also mischaracterized: it isn't "read-only, writes in development" — write support already exists and is simply plugin-specific (full read-write for Notion and Google Sheets, insert/delete for Todoist, read-only for GitHub). And the earlier comparison table wrongly credited Anthropic for GitHub's own official MCP server.

None of that means the project is risk-free. The pace of security advisories (two CVEs plus six further GHSA advisories across three releases) says a solo-maintained project handling credentials for a few dozen SaaS APIs has had real, exploitable bugs this year — evaluate that alongside the renewed activity, not instead of it. Net effect on the rating: the dormancy-driven downgrade is reversed, restoring 4.0/5, while the security history and plugin-by-plugin write support (rather than a clean "read-only" story) are now called out explicitly rather than glossed over.

For agents that need to answer questions across multiple data sources — "which GitHub issues assigned to me don't have Notion tasks?" or "show me all Salesforce deals alongside recent Discord activity" — Anyquery remains one of the more efficient paths available today, with real (if uneven) write support layered on top for a growing number of plugins.

---

*This review was originally published March 23, 2026, refreshed May 3, 2026, and corrected August 16, 2026 after a claim-by-claim citation audit. That audit found the May 2026 "project appears dormant" call was outdated (three releases shipped June–August 2026), the blanket "read-only" write-support claim was wrong (write support is plugin-specific), the plugin count needed updating to 44, the GitHub MCP server was wrongly attributed to Anthropic instead of GitHub, DBHub's database list and "text-to-SQL" claim were wrong, and the article named Slack and Gmail as example integrations that don't exist as dedicated plugins. We research MCP servers thoroughly but do not test them hands-on. Visit the [Anyquery GitHub repository](https://github.com/julien040/anyquery) for the latest information.*
