---
title: "Airtable MCP Server — Full Database CRUD for Your AI Agent"
date: 2026-03-23T21:00:00+09:00
description: "The most popular Airtable MCP server gives AI agents full CRUD access to bases, tables, records, fields, and comments."
og_description: "Airtable MCP: 15 tools for full database CRUD — records, tables, fields, comments, attachments. Community-built, TypeScript, MIT. Rating: 4/5."
content_type: "Review"
card_description: "Community-built MCP server exposing 15 tools for Airtable database operations including record CRUD, table/field schema management, comments, and file attachments. TypeScript, MIT license, stdio and HTTP transport, personal access token authentication. 438 GitHub stars, actively maintained. Airtable also launched an official MCP server in February 2026."
last_refreshed: 2026-04-21
---

**At a glance:** [GitHub](https://github.com/domdomegg/airtable-mcp-server) — 438 stars, TypeScript, MIT license, 120 commits, 15 tools, stdio + HTTP transport, personal access token auth. Community-built by [domdomegg](https://github.com/domdomegg) (Adam Jones).

The Airtable MCP server is the **most popular community-built MCP integration** for [Airtable](https://airtable.com/), Howie Liu's no-code database platform used by 500,000+ organizations. It gives AI agents full CRUD access to bases, tables, records, fields, and comments — everything you need to read, write, and manage Airtable data programmatically through natural language.

[Airtable Inc.](https://airtable.com/) was founded in 2012 by Howie Liu, Andrew Ofstad, and Emmett Nicholas in San Francisco. The company has raised $1.4B in funding, peaked at an $11.7B valuation (Series F, December 2021), and currently sits around ~$4B on secondary markets. As of early 2026: ~929 employees, ~$478M ARR (up ~27% year-over-year from $375M in 2023), cash flow positive since late 2024 with roughly half of the $1.4B raised still in the bank. In September 2025, CEO Howie Liu announced a "refounding" of Airtable as an AI-native platform. In October 2025, Airtable hired CTO David Azose from OpenAI and acquired AI startup DeepSky. In January 2026, Airtable launched **Superagent** — its first standalone product in 13 years — a multi-agent research platform that coordinates specialized agents working in parallel, powered by Claude and pulling from FactSet, Crunchbase, and SEC filings. An IPO may be on the horizon for 2026.

**In February 2026, Airtable launched an [official MCP server](https://support.airtable.com/docs/using-the-airtable-mcp-server)** — resolving the gap this review previously noted. The official server uses OAuth authentication, supports Claude, ChatGPT, and Cursor, and enables searching/analyzing data, creating records, updating records, and accessing Airtable Interface data. It respects existing Airtable permissions and is subject to standard API rate limits (creating records is limited to 10 per request). This means domdomegg's community server now competes with — and in some ways still exceeds — the official offering.

## What It Does

The server exposes **15 MCP tools** across four categories:

### Database Navigation

| Tool | What It Does |
|------|-------------|
| `list_bases` | Lists all accessible bases with IDs, names, and permission levels |
| `list_tables` | Retrieves tables from a base with configurable detail levels |
| `describe_table` | Gets comprehensive info about a table's structure, fields, and views |

### Record Operations

| Tool | What It Does |
|------|-------------|
| `list_records` | Query records with optional filtering and record limits |
| `search_records` | Text-based search across specified or all text fields |
| `get_record` | Retrieve an individual record by ID |
| `create_record` | Add new records with specified field values |
| `update_records` | Modify multiple records simultaneously |
| `delete_records` | Remove records from tables |

### Schema Management

| Tool | What It Does |
|------|-------------|
| `create_table` | Create new tables with field definitions |
| `update_table` | Modify table names or descriptions |
| `create_field` | Add fields with type specifications |
| `update_field` | Change field metadata |

### Collaboration & Attachments

| Tool | What It Does |
|------|-------------|
| `create_comment` | Add record comments with optional threading |
| `list_comments` | Retrieve comments sorted newest-to-oldest with pagination |
| `upload_attachment` | Direct file uploads to attachment fields (added v1.11.0) |

The server covers Airtable's core data layer — bases, tables, records, fields, comments, and attachments. It does **not** support Airtable Automations, Interfaces, Extensions, or Webhooks.

## Setup & Configuration

### Quick Start (npx)

```json
{
  "mcpServers": {
    "airtable": {
      "command": "npx",
      "args": ["-y", "airtable-mcp-server"],
      "env": {
        "AIRTABLE_API_KEY": "pat..."
      }
    }
  }
}
```

### Other Installation Methods

- **Homebrew:** `brew install airtable-mcp-server`
- **Docker:** Container support available
- **DXT:** Claude Desktop Extension format
- **Cursor:** One-click install from Cursor marketplace
- **Cline:** Available in Cline marketplace

### HTTP Transport

Set environment variables to run as a stateless HTTP server:

```
MCP_TRANSPORT=http
PORT=3000
```

The HTTP transport has no built-in authentication — a reverse proxy with auth is recommended for production use.

## Authentication

Uses an Airtable **Personal Access Token** passed via the `AIRTABLE_API_KEY` environment variable. You create the token in [Airtable's developer hub](https://airtable.com/create/tokens) with specific scopes:

- **Required:** `schema.bases:read`, `data.records:read`
- **For writes:** `data.records:write`
- **For comments:** `data.recordComments:read`, `data.recordComments:write`

The granular scope system means you can create a read-only token for agents that should only query data, or a full-access token for agents that need to create and modify records.

## Development History

| Date | Version | What Changed |
|------|---------|-------------|
| Dec 12, 2024 | — | Repository created |
| Dec 22, 2024 | v1.1.0–v1.2.0 | Added `search_records`, improved tool guidance |
| May 11, 2025 | v1.5.x | View support, sorting, validation fixes |
| Sep–Oct 2025 | v1.7.0–v1.9.0 | Rapid iteration, HTTP transport |
| Nov–Dec 2025 | v1.9.5–v1.9.6 | Server metadata, stability fixes |
| Jan 16, 2026 | v1.10.0 | `destructiveHint` annotations for dangerous tools |
| Feb 16, 2026 | v1.11.0 | `upload_attachment` tool |
| Feb 27, 2026 | v1.12.0 | Typecast support for create/update operations |
| Mar 7, 2026 | v1.13.0 | Fixed body size limit for large payloads |

**15 releases** over 15 months, though no new release since v1.13.0 (March 7, 2026) — a 45-day gap, the longest since the project's early days. The primary author (domdomegg) has contributed the bulk of 120 commits, with Dependabot handling dependency updates and 7 community contributors. PulseMCP: 102K all-time visitors, 2.2K weekly, #351 globally.

## Airtable Pricing

The MCP server is free and open-source. You pay for Airtable's platform, which determines your API limits:

| Tier | Price | Records/Base | API Calls/Month | Rate Limit |
|------|-------|-------------|-----------------|------------|
| **Free** | $0 | 1,000 | 1,000 | 5 req/sec/base |
| **Team** | $20/seat/mo | 50,000 | 100,000 | 5 req/sec/base |
| **Business** | $45/seat/mo | 125,000 | 500,000 | 5 req/sec/base |
| **Enterprise** | Custom | 500,000+ | Unlimited | 5 req/sec/base |

**The Free tier is almost unusable for MCP.** A single AI conversation — listing tables, searching records, updating a few — can consume dozens of API calls. At 1,000 calls/month, even moderate use would exhaust the allowance in a few sessions. The Team tier (100,000 calls) is the realistic minimum for regular MCP usage.

The hard **5 requests per second per base** rate limit applies to all tiers and cannot be increased. There's also a 50 requests/second limit across all traffic from a given user's personal access tokens. Exceeding limits returns a 429 status code with a mandatory 30-second backoff.

## How It Compares

| Feature | Airtable MCP (domdomegg) | Airtable MCP (official) | Notion MCP (official) | Monday.com MCP (official) |
|---------|------------------------|------------------------|---------------------|--------------------------|
| **Official** | No (community) | Yes | Yes | Yes |
| **Stars** | 438 | N/A (hosted) | 4,080 | 383 |
| **Tools** | 15 | ~4 (search, create, update, interfaces) | ~20 | ~15 |
| **Transport** | stdio + HTTP | Hosted (OAuth) | stdio | stdio + HTTP |
| **License** | MIT | Proprietary | MIT | MIT |
| **Auth** | Personal access token | OAuth 2.1 | OAuth | OAuth |
| **CRUD** | Full | Create + update + search | Full | Full |
| **Schema management** | Yes | No | Limited | Yes |
| **Comments** | Yes | No | Yes | No |
| **Attachments** | Yes | No | No | No |
| **Free tier API limit** | 1,000/mo | 1,000/mo | Varies | Varies |
| **Rate limit** | 5 req/sec/base | 5 req/sec/base | 3 req/sec | — |

With the **official Airtable MCP server launching in February 2026**, Airtable has joined Notion and Monday.com in offering first-party MCP support. However, the official server is notably limited compared to domdomegg's community version — it lacks schema management, comments, attachments, delete operations, and is restricted to 10 records per create request. The community server remains the more capable option for power users who need full database control.

### Other Airtable MCP Servers

| Server | Stars | Notes |
|--------|-------|-------|
| **Airtable official** | N/A | Hosted OAuth server, launched Feb 2026, limited tools (~4), no schema/delete/comments |
| domdomegg/airtable-mcp-server | 438 | Dominant community option, reviewed here |
| rashidazarang/airtable-ai-agent | 4 | Python, 33 tools, broader Airtable coverage |
| onimsha/airtable-mcp-server-oauth | 3 | Python, adds OAuth 2.1 support |
| CDataSoftware/airtable-mcp-server-by-cdata | 1 | Java, read-only, via CData JDBC |
| glassBead-tc/effect-airtable-mcp | 1 | TypeScript, Effect-based with type-safe validation |

## Known Issues

1. **Community project alongside official server** — Airtable launched its own official MCP server in February 2026, which means this community project is no longer the only option. The official server uses OAuth and respects Airtable permissions natively, but is significantly more limited in capabilities (no schema management, no delete, no comments, no attachments). If domdomegg stops maintaining this server, users would fall back to the official server but lose substantial functionality.

2. **Free tier API exhaustion** — Airtable's Free tier allows only 1,000 API calls/month. MCP interactions are API-call-intensive — users report hitting limits quickly even with moderate usage. The Team tier ($20/seat/mo) is realistically required.

3. **Context window consumption** — No field filtering on record retrieval. [Issue #75](https://github.com/domdomegg/airtable-mcp-server/issues/75) requests support for Airtable's `fields` API parameter to limit returned data and conserve LLM context, but this hasn't been implemented yet.

4. **5 req/sec hard rate limit** — Airtable enforces a 5 requests/second/base limit on all tiers with a mandatory 30-second backoff on 429 responses. An agent doing rapid sequential operations can easily hit this.

5. **No OAuth support** — Uses personal access tokens only. A separate fork (onimsha/airtable-mcp-server-oauth) adds OAuth 2.1 support, but the main server requires token management.

6. **HTTP transport lacks auth** — Running in HTTP mode exposes the server without built-in authentication. A reverse proxy with auth must be configured separately for any non-local deployment.

7. **Destructive operations** — While v1.10.0 added `destructiveHint` annotations for delete/update tools, the server doesn't enforce any confirmation flow. An agent can delete records or tables without a safety net beyond the LLM's judgment.

8. **Limited collaboration features** — Comments and attachments are supported, but no access to Airtable Automations, Interfaces, Extensions, Webhooks, or revision history. The server covers data operations, not workflow management.

9. **Release cadence slowing** — No new release since v1.13.0 (March 7, 2026), a 45-day gap. With the official Airtable MCP server now available, the question of long-term community maintenance becomes more pointed. 5 open issues remain, including the longstanding #75 (field filtering) from December 2025.

## Bottom Line

The Airtable MCP server is a **well-maintained, community-driven integration** that covers the essential data operations most users need — listing bases, querying records, creating and updating data, managing schema, and handling comments and attachments. With 438 stars, 15 releases, and 120 commits, it remains the most feature-complete Airtable MCP option available.

The landscape shifted significantly in February 2026 when **Airtable launched its own official MCP server**. This resolves the gap this review previously highlighted — Airtable now joins Notion and Monday.com with first-party MCP support. However, the official server is surprisingly limited: it covers basic search, create, and update operations with OAuth auth and Airtable Interface access, but lacks schema management, delete operations, comments, attachments, and the granular control that domdomegg's server provides. For power users who need full database control, the community server remains the better choice.

For practical use: if you want simple data queries and record creation with OAuth convenience, the official server may be sufficient. If you need full CRUD, schema management, comments, attachments, or HTTP transport, domdomegg's server delivers more. Both are subject to Airtable's API rate limits, and the Free tier's 1,000 calls/month remains impractical for regular MCP usage.

The 45-day release gap since v1.13.0 and the arrival of an official competitor raise questions about long-term maintenance. Airtable's broader AI strategy — Superagent, the DeepSky acquisition, a potential 2026 IPO — suggests the official server will mature over time, potentially narrowing the feature gap.

**Rating: 4 / 5** — Still the most complete Airtable MCP server available, with 15 tools covering full CRUD, schema management, comments, and attachments. MIT license, multiple installation methods (npx, Homebrew, Docker, DXT), dual transport support. The arrival of Airtable's official MCP server (February 2026) reduces the "no official backing" risk, but the official server's limited feature set means this community server retains its practical edge. Loses points for slowing release cadence, no field filtering on record retrieval (#75), Free tier API limits, and no support for Airtable's automation and workflow features.

**Category**: [Business & Productivity](/categories/business-productivity/)
