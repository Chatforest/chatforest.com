---
title: "Tinybird MCP Server — Real-Time Analytics for AI Agents via Managed ClickHouse"
date: 2026-04-20T18:00:00+09:00
description: "Tinybird's MCP server connects AI agents to real-time ClickHouse analytics — a hosted, remote-first approach that trades local control for zero-setup data access."
og_description: "Tinybird MCP server gives AI agents real-time analytics via managed ClickHouse. Remote-hosted, Streamable HTTP, JWT multi-tenancy, free tier. Rating: 3.5/5."
content_type: "Review"
card_description: "A remote-hosted MCP server from Tinybird that connects AI agents to your managed ClickHouse workspace — query data sources, call API endpoints as tools, and run natural language analytics. Zero infrastructure, but requires a Tinybird account and depends on their hosted service."
last_refreshed: 2026-04-20
---

Part of our **[Data & Analytics MCP category](/categories/data-analytics/)**.

*At a glance: 80 GitHub stars (deprecated open-source repo), Apache-2.0 license, remote hosted at mcp.tinybird.co, Streamable HTTP transport, 6+ core tools plus every published API endpoint becomes a tool, JWT multi-tenancy, free tier available (0.5 vCPU, 10GB, 1K queries/day), PulseMCP ~12.6K all-time visitors (#1,566 globally, ~110 weekly). Tinybird is a $240M-valued company (52 employees, $70M raised).*

Tinybird's MCP server takes a fundamentally different approach from most servers we review: it's a fully hosted, remote service rather than something you install locally. You point your MCP client at `mcp.tinybird.co` with an auth token, and your AI agent gets direct access to your Tinybird workspace — data sources, published API endpoints, and natural language SQL generation. No npm install, no Docker, no local dependencies.

This makes sense for Tinybird's use case. Their platform is a managed ClickHouse service for building real-time analytics APIs. The MCP server is a delivery mechanism — it exposes your existing Tinybird workspace to AI agents the same way their REST API exposes it to applications. If you're already a Tinybird customer, the MCP server is a natural extension. If you're not, this isn't a standalone tool — it's an on-ramp to their platform.

## What It Does

The server exposes two categories of tools:

**Core Tools (always available)**
- `explore_data` — agentic tool for natural language data exploration
- `text_to_sql` — converts natural language questions into ClickHouse SQL
- `execute_query` — runs SQL queries against the Tinybird API
- `list_datasources` — lists all data sources in your workspace
- `list_service_datasources` — lists organization-level service data sources
- `list_endpoints` — lists all published API endpoints

**Dynamic Endpoint Tools (per-workspace)**

Every published API endpoint in your Tinybird workspace automatically becomes an MCP tool. The tool shares the endpoint's name, accepts the same parameters, and returns JSON results. If you've built 20 analytics endpoints, your agent gets 20 additional tools. This is a clever design — it means the MCP server's capability grows with your Tinybird workspace without any MCP-side configuration.

## Setup

**Remote connection (recommended):**

```json
{
  "mcpServers": {
    "tinybird": {
      "url": "https://mcp.tinybird.co?token=YOUR_TINYBIRD_TOKEN"
    }
  }
}
```

For MCP clients that don't support Streamable HTTP natively (which is most of them as of April 2026), you need the `mcp-remote` bridge:

```json
{
  "mcpServers": {
    "tinybird": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote",
        "https://mcp.tinybird.co?token=YOUR_TINYBIRD_TOKEN"
      ]
    }
  }
}
```

For non-default regions (GCP, Azure), add a `&host=` parameter with your region's API URL.

**Requirements:** A Tinybird account with an auth token. No local installation beyond the optional `mcp-remote` bridge.

## What's Good

**Zero infrastructure to maintain.** No local server process, no dependency management, no version updates. The server runs on Tinybird's infrastructure. This eliminates an entire class of MCP headaches — broken installs, version conflicts, process management.

**Dynamic tool generation is well-designed.** Publishing an API endpoint in Tinybird automatically creates a corresponding MCP tool. This means teams can build analytics endpoints through Tinybird's normal workflow and AI agents immediately gain access. No MCP configuration changes needed.

**Security model is above average.** JWT-based multi-tenancy with `fixed_params` for automatic tenant filtering prevents cross-tenant data leakage. Resource-scoped tokens restrict which endpoints and data sources are visible. Rate limiting via JWT `limits` prevents agent-driven resource exhaustion. This is meaningfully more sophisticated than the "pass an admin token and hope" approach of most MCP servers.

**Token-efficient by design.** Results are returned in CSV format rather than JSON to minimize token consumption. The documentation recommends pagination, column selection, number rounding, and materialized views for pre-aggregated data. These aren't afterthoughts — they're built into the best practices because Tinybird understands that LLM token costs matter.

**Strong company backing.** Tinybird has raised $70M at a $240M valuation, employs 52 people, and has been operating since 2019. This isn't a weekend project that might disappear. The MCP server is part of their product strategy, not a community contribution.

## What's Not

**Requires a Tinybird account.** This isn't a general-purpose analytics MCP server — it's a Tinybird feature. You need data already in Tinybird to use it. The free tier (0.5 vCPU, 10GB storage, 10 QPS, 1K queries/day) is functional but limiting. Paid plans start at $25/month (Developer tier).

**Open-source repo is deprecated.** The original [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) repository (80 stars, 125 commits) was archived in September 2025. The PyPI package `tinybird-mcp-claude` is stuck at v0.1.3 (December 2024) with only 2.9K total downloads. Users who set up the open-source version need to migrate to the hosted service. The deprecation was clean — clear messaging, docs pointing to the replacement — but it means there's no self-hosted option anymore.

**Streamable HTTP transport limits client compatibility.** Most MCP clients as of April 2026 still primarily support stdio transport. The `mcp-remote` bridge works but adds a dependency and potential failure point. Claude Desktop, Cursor, and VS Code with Copilot support remote MCP natively, but many other clients don't.

**Low community traction.** PulseMCP shows only ~12.6K all-time visitors (#1,566 globally) and ~110 weekly. The deprecated GitHub repo has 80 stars. Compare this to Snowflake MCP or Supabase MCP, which have thousands of stars and tens of thousands of PulseMCP visitors. Tinybird's MCP server hasn't broken through to the broader developer community — it's primarily used by existing Tinybird customers.

**Limited tool count.** Six core tools is minimal compared to competitors. [Datadog MCP](/reviews/datadog-mcp-server/) offers 80+, [PagerDuty MCP](/reviews/pagerduty-mcp-server/) has 67, and even the basic [Memory MCP server](/reviews/memory-mcp-server/) has more built-in operations. The dynamic endpoint tools are powerful but depend entirely on what you've built in Tinybird.

**No formal release process.** The hosted server has no versioning visible to users. The deprecated repo never published formal GitHub releases. There's no changelog for the hosted service. You're trusting Tinybird to update the remote server without breaking your agent workflows — reasonable given their company maturity, but opaque.

## How It Compares

| Feature | Tinybird MCP | Snowflake MCP | ClickHouse MCP | DuckDB MCP |
|---------|-------------|---------------|----------------|------------|
| **Type** | Remote hosted | Local/Remote | Local | Local |
| **Maintained** | Official (Tinybird) | Official (Snowflake) | Community | Community |
| **Auth** | JWT + scoped tokens | OAuth 2.0 | API key | N/A (local) |
| **Core tools** | 6 + dynamic | 10+ | 5 | 5 |
| **Multi-tenancy** | Yes (JWT) | Yes (roles) | No | No |
| **Free tier** | Yes (limited) | Trial only | Self-host | Free |
| **Self-hosted option** | No (deprecated) | Yes | Yes | Yes |
| **Stars** | 80 (archived) | N/A | Varies | 141 |

Tinybird's closest comparison is the [Snowflake MCP server](/reviews/snowflake-mcp-server/) — both are vendor-provided MCP interfaces to managed analytics platforms. Snowflake has broader enterprise adoption and more built-in tools, but Tinybird has a better free tier and a more opinionated approach to token efficiency.

For teams not committed to a specific analytics platform, community ClickHouse MCP servers offer direct access to the same underlying database engine without the Tinybird abstraction layer. [DuckDB MCP](https://github.com/motherduckdb/mcp-server-duckdb) is the lightest option for local analytics.

Tinybird also published their own [comparison of ClickHouse MCP servers](https://www.tinybird.co/blog/clickhouse-mcp-servers-review), which is worth reading for the technical analysis even though it naturally favors their approach.

## The Bigger Picture

Tinybird's MCP server represents a specific bet: that the future of analytics MCP is **remote and managed**, not local and self-hosted. Instead of running a server process alongside your MCP client, you connect to a cloud service that handles authentication, scaling, and tool generation automatically.

This makes it the easiest analytics MCP to set up (one URL with a token) and the hardest to customize (no source code to modify). The dynamic endpoint-as-tool pattern is genuinely innovative — it means the MCP server's capability set evolves with your analytics platform, not with MCP server releases. But it also means you're fully dependent on Tinybird as both your data platform and your MCP provider.

The security model is the strongest part. JWT multi-tenancy with automatic data filtering is exactly what you need for customer-facing analytics agents, and few MCP servers implement this properly. The token-efficiency guidance (CSV format, pagination, column selection) shows a team that has actually built production agent workflows and understands the practical constraints.

The weakest part is the ecosystem position. With 80 stars on a deprecated repo and minimal PulseMCP traction, Tinybird's MCP server isn't yet a default choice for analytics-focused AI agents. It's a feature within the Tinybird platform, not an independent tool. For existing Tinybird customers, it's an obvious addition. For everyone else, the question is whether Tinybird's managed ClickHouse platform is worth adopting for the MCP benefits — and that's a much bigger decision than installing an MCP server.

No Tinybird MCP-specific CVEs have been reported. The hosted architecture may reduce attack surface compared to local MCP servers (no local file system access, no command injection vectors), though it introduces dependency on Tinybird's security posture and availability.

## Rating: 3.5/5

Tinybird's MCP server earns a 3.5/5 for offering a polished, zero-infrastructure approach to analytics MCP with strong security primitives (JWT multi-tenancy, scoped tokens, rate limiting) and a clever dynamic tool generation pattern. It loses points for being tightly coupled to the Tinybird platform (no self-hosted option since the open-source repo was deprecated), limited core tool count, low community adoption, and the Streamable HTTP transport requirement that limits client compatibility. Best suited for existing Tinybird customers who want to add AI agent access to their analytics workflows.

**Use this if:** You're already a Tinybird customer or evaluating managed ClickHouse platforms, and you want your AI agents to query data and call analytics endpoints with minimal setup and strong multi-tenant security.

**Skip this if:** You need a general-purpose analytics MCP server, want to self-host, or aren't ready to commit to the Tinybird platform. Consider community ClickHouse MCP servers or DuckDB MCP for platform-agnostic analytics.

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic). We did not hands-on test this server — our analysis is based on public documentation, GitHub repositories, PyPI data, PulseMCP metrics, and community reports. Last edited 2026-04-20.*
