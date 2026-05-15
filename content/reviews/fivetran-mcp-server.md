---
title: "Fivetran MCP Server — 161 Auto-Generated Tools for Managed ELT Pipeline Control, Write-Protected by Default"
date: 2026-05-16T18:00:00+09:00
description: "Fivetran's official MCP server auto-generates 161 tools from the Fivetran REST API OpenAPI spec — covering connections, destinations, groups, hybrid deployment agents, and external logging. Many tools are commented out by default to protect context windows. Writes are disabled unless you explicitly enable them. Free tier API access included. Claude Desktop and Claude Code compatible; no claude.ai browser support. Rating 3/5."
og_description: "Fivetran MCP: 161 tools auto-generated from OpenAPI spec, writes disabled by default, Python-only, STDIO mode, 15 GitHub stars, free tier API access. Claude Desktop and Claude Code compatible. Rating: 3/5."
content_type: "Review"
card_description: "Fivetran's official MCP server generates 161 tools from the Fivetran REST API — connections, destinations, groups, sync controls, and more. Writes are disabled unless opted in. Many tools commented out by default. Python-only, STDIO mode, low community signal (15 stars). Free tier API access included. Part of the ETL & Data Integration category alongside Airbyte."
last_refreshed: 2026-05-16
---

**At a glance:** Fivetran's official MCP server (`fivetran/fivetran-mcp`) auto-generates **161 tools** from Fivetran's REST API OpenAPI specification — covering connections, destinations, groups, external logging, and hybrid deployment agents. A large portion of those tools are **commented out by default** to keep context windows manageable; write operations (62 of the 161) are **disabled unless you explicitly set `FIVETRAN_ALLOW_WRITES=true`**. Installation requires cloning the repo or using `uvx` — there is no official npm or PyPI package. The server runs STDIO-only (no cloud-hosted remote HTTP mode) and requires an API key pair from the Fivetran dashboard. Free tier users can access the REST API. Part of our **[ETL & Data Integration category](/categories/etl-data-integration/)**.

[Fivetran](https://fivetran.com/) is one of the most established **managed ELT (Extract, Load, Transform)** services in data engineering, competing directly with Airbyte, Stitch, and Matillion. Unlike open-source Airbyte, Fivetran is a **fully managed, paid SaaS** platform — customers pay for the connectors and sync frequency they need, and Fivetran handles all infrastructure. With over **700+ managed connectors**, Fivetran targets enterprise data teams that want reliability and support SLAs over self-hosted flexibility.

The MCP integration gives AI agents natural-language control over existing Fivetran pipelines — listing connectors, triggering syncs, managing destinations, and modifying schemas — without requiring users to navigate the Fivetran UI.

## What Fivetran Is

Fivetran is a **fully managed ELT data pipeline service**. It connects source systems (SaaS APIs, databases, files) to destination data warehouses (Snowflake, BigQuery, Redshift, Databricks) and keeps them synchronized on a schedule. Key characteristics:

- **700+ managed connectors** — databases (MySQL, PostgreSQL, MongoDB), SaaS apps (Salesforce, HubSpot, Zendesk, Google Analytics, Shopify), files (S3, SFTP), and events (Kafka)
- **Fully managed** — no infrastructure to deploy; Fivetran runs all extraction, schema management, and load scheduling
- **Schema normalization** — Fivetran automatically handles schema drift, type changes, and column additions
- **Sync frequencies** — 5-minute sync intervals on paid plans; 1-minute on Enterprise; scheduled syncs on Free
- **Monthly Active Rows (MAR) pricing** — cost is based on rows synced; the Free plan includes 500,000 MAR/month, access to 5,000 monthly model runs (Fivetran Transformations), and REST API access

**Pricing implications for MCP users:** As of 2026, the Fivetran Free Plan explicitly includes REST API access. This means users can authenticate the MCP server and use its read tools without a paid subscription. Write operations (creating connections, triggering syncs) will consume MAR against whatever plan you're on — on the Free tier, heavy sync triggering could exhaust the monthly allowance.

## The MCP Server — Overview

The official Fivetran MCP server lives at `github.com/fivetran/fivetran-mcp`. It was published by the Fivetran organization, though an official November 2025 Fivetran blog post (by Lead Solution Architect Elijah Davis) stated at the time that "Fivetran does not currently have an officially supported MCP Server" — the org-level repo appears to have arrived after that post. As of May 2026, the repo exists and is functional, but its **official support status is somewhat ambiguous**: the repo has only 28 commits and 0 open issues, suggesting it may be more "published but experimental" than "officially supported."

**Key technical facts:**

| Attribute | Detail |
|-----------|--------|
| GitHub | `fivetran/fivetran-mcp` |
| Stars | 15 |
| Forks | 6 |
| Commits | 28 |
| Language | Python 100% |
| License | Not explicitly stated (community forks use MIT) |
| Python requirement | 3.10+ |
| Deployment mode | STDIO only |
| Package | No official PyPI/npm — clone or use `uvx` |
| Write operations | Disabled by default (`FIVETRAN_ALLOW_WRITES=false`) |

The server auto-generates its tool list from Fivetran's OpenAPI specification, which is why it has 161 tools — it reflects the Fivetran REST API surface, not a curated selection. This is efficient from a maintenance standpoint (tools update when the API spec updates) but creates a UX challenge: 161 tool descriptions consume substantial context window space in AI clients.

## Available Tools

The 161 tools break into these functional groups:

**Read operations (75 tools):** List, get, and search operations across all Fivetran resources. These are safe — they cannot modify anything.

**Write operations (62 tools):** Create, modify, and delete operations. **These are disabled unless `FIVETRAN_ALLOW_WRITES=true` is set in the environment.** Includes connection creation, destination provisioning, group management, user administration, and deletion operations.

**Operational tools (24 tools):** Sync triggering, schema reloads, setup tests, transform runs, and webhook management. Some of these (sync triggers) are operational rather than destructive, but they still require `FIVETRAN_ALLOW_WRITES=true`.

**Enabled by default (curated subset):**

The server's `server.py` file comments out the majority of tools to limit context consumption. The default-enabled set focuses on the most common workflows:

- **Account:** `get_account_info`
- **Connections (18 tools):** `list_connections`, `create_connection`, `get_connection_details`, `modify_connection`, `delete_connection`, `get_connection_state`, `modify_connection_state`, `sync_connection`, `resync_connection`, `resync_tables`, `get_connection_schema_config`, `modify_connection_schema_config`, `modify_connection_table_config`, `modify_connection_column_config`, `delete_connection_column_config`, `run_connection_setup_tests`, `create_connect_card`, `reload_connection_schema_config`
- **Destinations (6 tools):** `list_destinations`, `create_destination`, `get_destination_details`, `modify_destination`, `delete_destination`, `run_destination_setup_tests`
- **Groups (9 tools):** `list_groups`, `create_group`, `modify_group`, `delete_group`, `list_users_in_group`, `add_user_to_group`, `delete_user_from_group`, `get_group_ssh_public_key`, `get_group_service_account`
- **External Logging (6 tools):** `list_log_services`, `create_log_service`, `get_log_service_details`, `update_log_service`, `delete_log_service`, `run_log_service_setup_tests`
- **Hybrid Deployment Agents (3 tools):** `list_hybrid_deployment_agents`, `create_hybrid_deployment_agent`, `get_hybrid_deployment_agent`

**Disabled by default (must uncomment in `server.py`):** Certificates and fingerprints management, full user and team administration, system keys, private links, proxy agents, and HVR (high-volume replication) functionality.

**Practical scope:** The enabled default set covers the most common daily use cases — managing connections and destinations, triggering syncs, and organizing resources into groups. Users with specific needs (e.g., managing private links or HVR configs) must edit the server code directly.

## Installation and Configuration

There is no official PyPI or npm package for the official `fivetran/fivetran-mcp` repo. The recommended installation paths are:

**Option 1 — uvx (recommended, no clone needed):**
```bash
uvx --from git+https://github.com/fivetran/fivetran-mcp fivetran-mcp
```

**Option 2 — Local clone:**
```bash
git clone https://github.com/fivetran/fivetran-mcp
cd fivetran-mcp
python3 -m venv .venv
source .venv/bin/activate
pip install .
```

**Claude Desktop configuration (`claude_desktop_config.json`):**
```json
{
  "mcpServers": {
    "fivetran": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/fivetran/fivetran-mcp", "fivetran-mcp"],
      "env": {
        "FIVETRAN_API_KEY": "your_api_key",
        "FIVETRAN_API_SECRET": "your_api_secret",
        "FIVETRAN_ALLOW_WRITES": "false"
      }
    }
  }
}
```

**Note on write mode:** The server defaults to read-only behavior (`FIVETRAN_ALLOW_WRITES=false`). To enable sync triggering, connection creation, and other write operations, set `FIVETRAN_ALLOW_WRITES=true`. This is a deliberate design choice — accidental writes against a production Fivetran account could trigger unintended data syncs and MAR consumption.

**Community alternatives:**

Two community implementations offer alternative installation paths:

- **`mcp-fivetran` (PyPI):** `pip install mcp-fivetran` — published by andrewkkchan/davidetodorov; v0.1.0, May 2025. Provides only 3 tools (invite user, list connections, trigger sync). Requires Python ≥3.12.8. Useful for very targeted workflows; not a replacement for the full official server.
- **`YimingYAN/fivetran-mcp`:** Installable via `uvx fivetran-mcp@latest`. 14 tools. Adds Cloudflare Workers deployment support for a cloud-hosted HTTP endpoint — a feature absent from the official repo. Last updated January 2026.

## Authentication

The server uses Fivetran's HTTP Basic Auth scheme. No OAuth flow. Configuration is via environment variables:

- **`FIVETRAN_API_KEY`** — Required. Your Fivetran API key.
- **`FIVETRAN_API_SECRET`** — Required. Your Fivetran API secret.
- **`FIVETRAN_ALLOW_WRITES`** — Optional, default `false`. Set to `true` to enable create/modify/delete/sync operations.

**Where to get credentials:** Fivetran Dashboard → Account Settings → API Config → Generate API Key.

**Security concern:** Credentials live in plain text inside the MCP configuration file (typically `~/.claude.json` or `claude_desktop_config.json`). There is no built-in credential vault integration or secrets management. If you use a shared machine or check configuration files into version control, take care to exclude these credentials.

The API calls all route directly to `api.fivetran.com` — no data passes through any third-party relay.

## Claude.ai Compatibility

| Client | Compatible | Notes |
|--------|-----------|-------|
| Claude Desktop (macOS/Windows) | Yes | Documented and tested by community |
| Claude Code (CLI) | Yes | Configure via `~/.claude.json` |
| claude.ai browser | No | MCP requires local client; browser interface not supported |
| Cursor | Yes | Standard MCP STDIO config |
| Windsurf | Yes | Standard MCP STDIO config |
| VS Code + Copilot | Yes | With MCP extension |

The server runs STDIO-only, which means it requires a local client application that manages the MCP subprocess. Claude Desktop (the free downloadable app for macOS and Windows) works well for interactive use. Claude Code works well for developer workflows. The browser-based `claude.ai` interface — including claude.ai Personal and claude.ai Pro — does not support external MCP servers.

## Fivetran vs. Airbyte MCP

Both Fivetran and Airbyte are ELT platforms with MCP integrations, but they serve different audiences:

| Dimension | Fivetran MCP | Airbyte MCP |
|-----------|-------------|-------------|
| Platform model | Managed SaaS (paid) | Open-source + Cloud (free self-host) |
| MCP tools | 161 (official); 25 (community toolkit) | Multiple implementations; various tool counts |
| Deployment mode | STDIO only | Remote HTTP (Agent MCP) + STDIO |
| claude.ai browser | No | No (Agent MCP requires Claude Desktop) |
| Architecture | REST API proxy (live calls) | Context Store (pre-indexed ELT layer) |
| Token efficiency | Standard (live API responses) | High (pre-indexed; 40–90% reduction claimed) |
| Community signal | 15 stars on MCP repo | 21,300+ stars on main Airbyte repo |
| Connector count | 700+ managed | 600+ (ELT); 50 agent-optimized |
| Free tier | Yes (500K MAR, API access included) | Yes (Airbyte Cloud free trial; self-hosted free) |
| License | Official repo unclear; community MIT | Apache-2.0 (Airbyte core) |
| Writes | Disabled by default, explicit opt-in | Available (connector-dependent) |

**The core distinction:** Fivetran MCP is a natural-language control plane for an **existing Fivetran account** — it manages connectors and triggers syncs, but data flows through the standard Fivetran pipeline. Airbyte's Agent MCP (launched May 2026) is an entirely different architecture: it pre-indexes business data into a Context Store and serves AI queries from there, reducing token usage. If you already use Fivetran, the MCP integration adds AI-native control at no additional cost. If you're starting fresh and want an agentic data layer with token efficiency, Airbyte's approach is more sophisticated.

## Limitations and Gotchas

1. **Many tools disabled by default** — 161 tools total, but the majority are commented out in `server.py`. Users who need the full API surface must manually edit the server code.

2. **Writes disabled by default** — All 62 write and operational tools silently refuse unless `FIVETRAN_ALLOW_WRITES=true` is explicitly set. This is good for safety but can confuse new users who expect sync triggers to work immediately.

3. **STDIO only** — No cloud-hosted remote HTTP mode in the official repo. Every user must run the server locally. The community YimingYAN fork adds Cloudflare Workers support, but that's an unofficial, unmaintained fork.

4. **API keys in plain text** — Standard MCP config files are unencrypted JSON on disk. Exercise caution on shared machines.

5. **Pagination not automatic** — Large Fivetran accounts with many connections (700+) will require manual pagination; large result sets also consume substantial context window.

6. **License unclear** — The official `fivetran/fivetran-mcp` repo does not appear to have an explicit LICENSE file, creating ambiguity for enterprise users with open-source license requirements. Community forks are MIT.

7. **Low community activity** — 15 stars, 6 forks, 28 commits, 0 open issues. This either means the server works perfectly (unlikely for a young project) or engagement is very low. There is little community feedback to gauge real-world reliability.

8. **Ambiguous official status** — Fivetran's own blog said no official server existed (November 2025); the org repo appeared later. Whether the repo represents a supported product or an experimental project is unclear from the repo signals alone.

9. **No Docker image** — Unlike some MCP servers (Zoho Analytics, dbt Labs), there is no Docker deployment option.

10. **Context window pressure** — Even the default-enabled subset of tools is large. Users with smaller context window budgets may need to further trim the enabled tool list.

## Who Should Use Fivetran MCP

**Good fit if:**
- You already have an active Fivetran account and want AI-native control over existing pipelines
- You need to manage connections and destinations via natural language without navigating the UI
- Your use case is read-heavy (auditing connector states, listing schemas, reviewing sync histories)
- You use Claude Desktop or Claude Code as your primary AI client
- Write operations are acceptable with explicit opt-in (`FIVETRAN_ALLOW_WRITES=true`)

**Poor fit if:**
- You want claude.ai browser compatibility — the STDIO-only architecture requires a local client
- You need an agent-optimized data access layer with token efficiency — Airbyte's Context Store approach is architecturally better suited
- You need a cloud-hosted remote MCP endpoint without running anything locally
- You need Docker deployment
- You are cost-sensitive and not already paying for Fivetran — Airbyte's self-hosted option is free

## Verdict

The Fivetran MCP server does exactly what it says: it wraps the Fivetran REST API in an MCP interface, giving AI agents natural-language control over existing Fivetran pipelines. The 161-tool count sounds impressive, but the reality is more cautious — many are commented out, writes require explicit enablement, and the server is STDIO-only. For users already paying for Fivetran, the integration is a useful addition that requires no extra cost (free tier API access included) and works with Claude Desktop and Claude Code.

The reservations are about ecosystem maturity and architectural approach. Fifteen stars and 28 commits on the official repo is a thin signal for a platform with 700+ connectors and enterprise-grade positioning. The write-protection default is sensible safety design, but the manual code-editing required to unlock the full tool set is a friction point. And compared to Airbyte's Context Store model — which pre-indexes data for token efficiency rather than proxying live API calls — the Fivetran MCP is architecturally simpler in a way that matters for agentic workflows at scale.

For Fivetran customers who want AI-native pipeline management, this is a workable integration. For teams choosing between ELT platforms and evaluating MCP maturity, Airbyte's agent ecosystem is further along.

**Rating: 3/5** — Covers the core use case for existing Fivetran customers; free tier API access is a genuine plus; write-protection default shows safety awareness. Held back by low community signal (15 stars, 28 commits), many tools disabled by default requiring code edits, STDIO-only deployment, unclear license, ambiguous official support status, and no architectural advantages over a simple API proxy.

---

*Researched May 2026. Community implementations vary; see the [fivetran/fivetran-mcp GitHub repo](https://github.com/fivetran/fivetran-mcp) for current status. For a comparison in the ETL space, see our [Airbyte MCP review](/reviews/airbyte-mcp-server/).*
