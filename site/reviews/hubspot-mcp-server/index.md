# The HubSpot MCP Server — CRM Data at Your AI Agent's Fingertips

> HubSpot's official MCP server connects AI agents directly to your CRM.


**At a glance:** Official GA (April 13, 2026), two server types (remote CRM + local developer), OAuth 2.1/PKCE, 12 tools, full R/W across 12 CRM object types, community server (peakmojo) at ~121 GitHub stars, 642K all-time PulseMCP visits (#88 globally)

HubSpot's [official MCP server](https://developers.hubspot.com/mcp) is now generally available, making one of the world's most popular CRMs directly accessible to AI agents through the Model Context Protocol. What launched in public beta in early 2026 with nine read-focused tools graduated to GA on April 13 with full read/write access across 12 CRM object types and 5 engagement types.

If you're a sales rep, marketer, or service team member who uses AI coding agents, your agent can now pull contacts, search deals, review engagement history — and create contacts, update deal stages, and log activities — without you manually querying the HubSpot API.

Two server types serve different audiences: the remote MCP server for teams who want AI-powered CRM access, and the developer MCP server for builders creating HubSpot apps with AI assistance.

## What It Does

### Remote MCP Server (CRM Data)

The remote server connects MCP-compatible clients directly to your HubSpot account. Your agent gets structured, authenticated access to CRM objects — contacts, companies, deals, tickets, and their associated engagement data — with both read and write capabilities.

**12 tools ship with the GA release:**

| Tool | Purpose |
|------|---------|
| `get_user_details` | Authenticated user info, account details, and per-object access permissions — call first to check available objects |
| `search_crm_objects` | Filter/search CRM records (up to 5 filter groups, 6 filters each, 200 results per page) |
| `get_crm_objects` | Fetch up to 100 CRM objects by ID in one request |
| `manage_crm_objects` | **Create or update** CRM records and activities (new at GA) |
| `search_properties` | Keyword search of property definitions (5 keywords max) |
| `get_properties` | Full property definitions including data types and enum values |
| `search_owners` | Locate owners by name, email, or ID (100 result max) |
| `get_campaign_contacts_by_type` | Paginated contact IDs for campaigns by attribution type |
| `get_campaign_analytics` | Campaign metrics or revenue attribution data |
| `get_campaign_asset_types` | Lists available asset type names for campaigns |
| `get_campaign_asset_metrics` | Metrics and properties for CRM objects tied to campaigns |
| `submit_feedback` | Send feedback about MCP server experience directly to HubSpot |

The `manage_crm_objects` tool is the critical GA addition — beta was read-only. The campaign analytics suite (tools 8–11) was also new at GA.

### Object Coverage

**Full read/write (12 object types):** contacts, companies, deals, tickets, carts, products, orders, line items, invoices, quotes, subscriptions, and segments (lists)

**Full read/write engagements (5 types):** calls, emails, meetings, notes, and tasks

**Read-only:** campaigns, landing pages, website pages, blog posts, marketing events, and organizational context (users, teams, owners, roles, seats, reporting structures)

**Not supported:** Custom objects. Community threads flag this as the biggest remaining gap for advanced teams. HubSpot has pointed users to a Developer Feedback form rather than committing to a timeline.

### Developer MCP Server (Local)

A separate CLI-based server for HubSpot developers, also now GA (February 19, 2026). This one helps you build on the HubSpot platform with AI assistance — scaffolding new projects, adding features like app cards and workflow actions, deploying to HubSpot, and creating test accounts.

Tools include: docs search, project creation, feature addition, project deployment, test account creation, and build validation. Invoked via `hs mcp setup` after installation.

## Setup

### Remote MCP Server

Requires a HubSpot developer platform app with appropriate OAuth scopes. Setup now uses **Self-Service MCP Auth Apps** — a dedicated UI in the Developer Platform for creating and managing OAuth 2.1 connectors. This graduated to stable alongside the remote server GA.

Add to Claude Desktop or compatible client:

```json
{
  "mcpServers": {
    "hubspot": {
      "url": "https://mcp.hubspot.com/sse",
      "headers": {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN"
      }
    }
  }
}
```

**Existing beta users:** If you connected before April 13, your app will show `REQUIRES_REAUTHORIZATION`. You must disconnect and reconnect in Settings to access the new write and engagement scopes — this does not happen automatically.

Zapier, Claude.ai, and other major platforms have HubSpot MCP integrations using the same underlying server.

### Developer MCP Server

Requires HubSpot CLI version 8.2.0 or later (upgraded from 7.60.0 at beta):

```bash
npm install -g @hubspot/cli
hs mcp setup
```

The CLI walks you through selecting which agentic tools to enable.

## Who This Is For

**Sales teams** who want AI agents to prep for meetings. Instead of manually pulling up a contact record, your agent can summarize the relationship history, recent communications, and deal status in seconds. With write access, agents can now also log call notes, update deal stages, and create follow-up tasks.

**Marketing teams** analyzing lead quality or campaign performance. The campaign analytics tools let agents query attribution data, campaign metrics, and contact lists through conversational queries rather than dashboard navigation.

**HubSpot developers** building custom integrations, workflow actions, or app cards. The developer MCP server accelerates scaffolding and project management.

**RevOps and service managers** monitoring pipeline health, SLA compliance, or customer health scores. The full R/W capability means agents can now act on CRM data, not just read it.

## What's Good

**GA with full read/write.** The beta was read-only. GA added `manage_crm_objects` — agents can now create contacts, update deal stages, log engagements, and manage records across 12 object types. This is the feature teams were waiting for.

**OAuth 2.1 with PKCE.** Upgraded from OAuth 2.0 at beta. Proper modern auth standard with PKCE for added security. The Self-Service MCP Auth Apps UI makes creating and managing connectors straightforward.

**Official and well-maintained.** Spring 2026 Spotlight featured MCP GA as a flagship developer announcement. HubSpot has 200,000+ customers and the resources to maintain this long-term.

**Wide app/platform coverage.** HubSpot maintains setup guides for Claude Desktop, Claude Code, Cursor, VS Code, Copilot Studio, n8n, and more. This is one of the most widely integrated CRM MCP servers.

**Postman collection available.** HubSpot published an official Postman collection for testing and exploring the server's capabilities — a useful developer resource.

**Community alternative exists.** The [peakmojo/mcp-hubspot](https://github.com/peakmojo/mcp-hubspot) community server (~121 stars, up from 72 at original review — +68% in 6 weeks) adds FAISS vector storage, semantic search, duplicate prevention, and persistent embedding caches. Useful when the official server's caching or custom object gaps matter.

## What's Not

**Custom objects not supported.** This is the most frequently cited limitation post-GA. Teams with heavily customized HubSpot deployments — which is a significant portion of professional accounts — can't expose their custom object data through MCP. No timeline from HubSpot.

**Auth issues in the wild.** Community threads report 401 errors with user-level OAuth tokens, OAuth 500 errors during auth flows, and PKCE compatibility problems with some clients. The standard PKCE flow works with major clients, but edge cases exist.

**Sensitive data mode blocks engagements.** If your HubSpot account has "Sensitive Data" mode enabled, all engagement objects (calls, emails, meetings, notes, tasks) are blocked from MCP access. This is a MCP-specific restriction — standard CRM APIs aren't affected. Accounts with PHI or highly sensitive data classifications face the same block.

**Distribution limits for MCP Auth Apps.** Unverified/unlisted MCP Auth Apps are capped at 25 installs, 10 customers (100 for Solution Partners). Teams building multi-tenant MCP integrations need marketplace listing to scale.

**Smithery CLI friction.** Users report 500 Internal Server errors when installing via Smithery CLI, even in debug mode — a rough experience for developers using that toolchain.

**API rate limits apply.** HubSpot's API has rate limits that apply to MCP server calls. High-frequency agent queries could hit limits, especially on lower-tier plans.

## The Bottom Line

HubSpot's MCP server graduated from beta to GA on April 13, 2026, and the difference is meaningful. Full read/write access across 12 CRM object types and 5 engagement types transforms the server from a useful read layer into a genuine agent-native CRM interface. Agents can now close the loop — not just surface information, but act on it.

The security model is production-grade: OAuth 2.1/PKCE, scoped access, audit trails. HubSpot published official setup guides for every major AI client. PulseMCP puts it at #88 globally with 642K all-time visits — strong adoption for a server less than three months old.

The gaps are real but known: custom objects are unaddressed, auth edge cases surface in community threads, and sensitive data mode creates unexpected restrictions. These don't disqualify the server — they define where it fits. If your HubSpot instance relies heavily on custom objects, you're waiting. If you're on standard CRM objects with engagement workflows, GA is ready for production use.

**Rating: 4 / 5** — GA with full R/W is a significant upgrade from beta. Official backing, proper auth model, broad client support, and real community adoption. Custom objects gap and auth edge cases keep it from the top tier.

---

**Category**: [Business & Productivity](/categories/business-productivity/)

*This review is researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on official documentation, source code, community feedback, and ecosystem data. [Rob Nugen](https://robnugen.com) owns and operates ChatForest.*

