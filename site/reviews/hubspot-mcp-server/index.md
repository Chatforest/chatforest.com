# The HubSpot MCP Server — CRM Data at Your AI Agent's Fingertips

> HubSpot's official MCP server connects AI agents directly to your CRM.


**At a glance:** Official GA (April 13, 2026), two server types (remote CRM + local developer), OAuth 2.1/PKCE, 12 tools at GA (16 as of August 2026), full R/W across 12 CRM object types, community server (peakmojo) at ~128 GitHub stars, 1.5M all-time PulseMCP visits (#59 globally)

HubSpot's [official MCP server](https://developers.hubspot.com/mcp) is now [generally available](https://developers.hubspot.com/changelog/remote-hubspot-mcp-server-is-now-generally-available), making one of the world's most popular CRMs directly accessible to AI agents through the Model Context Protocol. The [public beta](https://developers.hubspot.com/changelog/public-beta-self-service-mcp-auth-apps-for-the-hubspot-remote-mcp-server) that preceded it was read-only; it graduated to GA on April 13 with full read/write access across 12 CRM object types and 5 engagement types.

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

**Update, August 2026:** HubSpot has continued shipping new tools since GA — [current documentation](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server) lists 16 tools, adding conversations search, conversation channel metadata, and marketing email analytics/management on top of the 12 listed above.

### Object Coverage

**Full read/write (12 object types):** contacts, companies, deals, tickets, carts, products, orders, line items, invoices, quotes, subscriptions, and segments (lists)

**Full read/write engagements (5 types):** calls, emails, meetings, notes, and tasks

**Read-only:** campaigns, website pages, blog posts, marketing events, and organizational context (users, teams, owners, roles, seats, reporting structures). Landing pages were read-only at GA but [gained write access](https://developers.hubspot.com/changelog/june-2026-rollup) (create, edit, publish) in a June 2026 update.

**Not supported:** Custom objects. Community threads flag this as the biggest remaining gap for advanced teams. HubSpot has pointed users to a Developer Feedback form rather than committing to a timeline.

### Developer MCP Server (Local)

A separate CLI-based server for HubSpot developers, also now GA (February 19, 2026). This one helps you build on the HubSpot platform with AI assistance — scaffolding new projects, adding features like app cards and workflow actions, deploying to HubSpot, and creating test accounts.

Tools include: docs search, project creation, feature addition, project deployment, test account creation, and build validation. Invoked via `hs mcp setup` after installation.

## Setup

### Remote MCP Server

Requires a HubSpot developer platform app with appropriate OAuth scopes. Setup now uses **Self-Service MCP Auth Apps** — a dedicated UI in the Developer Platform for creating and managing OAuth 2.1 connectors. Per HubSpot's [Spring 2026 Spotlight](https://developers.hubspot.com/changelog/spring-2026-spotlight), the Auth Apps *screen* remains in public beta even though the underlying remote MCP server it configures reached GA the same day.

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

Requires [HubSpot CLI version 8.2.0 or later](https://developers.hubspot.com/docs/developer-tooling/local-development/developer-mcp/setup) (up from 7.60.0 during beta):

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

**OAuth 2.1 with PKCE.** [Upgraded from OAuth 2.0 at beta](https://developers.hubspot.com/mcp); [required for all GA connections](https://developers.hubspot.com/changelog/remote-hubspot-mcp-server-is-now-generally-available). Proper modern auth standard with PKCE for added security. The Self-Service MCP Auth Apps UI makes creating and managing connectors straightforward (though, per above, that setup UI itself is still labeled beta).

**Official and well-maintained.** [Spring 2026 Spotlight](https://developers.hubspot.com/changelog/spring-2026-spotlight) featured MCP GA as a flagship developer announcement. HubSpot [reported 299,458 customers as of Q1 2026](https://ir.hubspot.com/news-releases/news-release-details/hubspot-reports-strong-q1-2026-results) and the resources to maintain this long-term.

**Wide app/platform coverage.** HubSpot's [MCP integration docs](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server) confirm the server works with any MCP-compatible client that supports OAuth 2.1/PKCE, including Claude Desktop and Claude Code (per the config example above). This is one of the most widely integrated CRM MCP servers.

**Postman collection available.** HubSpot published an [official Postman collection](https://www.postman.com/hubspot/hubspot-public-api-workspace/collection/682b44c55ac051812a5ee1de) for testing and exploring the server's capabilities — a useful developer resource.

**Community alternative exists.** The [peakmojo/mcp-hubspot](https://github.com/peakmojo/mcp-hubspot) community server (~128 stars as of this audit) adds FAISS vector storage, semantic search, duplicate prevention, and persistent embedding caches. Useful when the official server's caching or custom object gaps matter.

## What's Not

**Custom objects not supported.** This is the most frequently cited limitation post-GA. Teams with heavily customized HubSpot deployments — which is a significant portion of professional accounts — can't expose their custom object data through MCP. No timeline from HubSpot.

**Auth issues in the wild.** Community threads report [401 errors with user-level OAuth tokens](https://community.hubspot.com/t5/APIs-Integrations/401-Error-with-User-Level-OAuth-Token-for-mcp-hubspot-com/m-p/1191357) and [OAuth 500 errors during auth flows](https://community.hubspot.com/t5/Third-Party-Apps/MCP-OAuth-authentication-failed-error-500/m-p/1250875). The standard PKCE flow works with major clients, but edge cases exist.

**Sensitive data mode blocks engagements.** If your HubSpot account has "Sensitive Data" mode enabled, [Activity objects (calls, emails, meetings, notes, tasks) are blocked from MCP access](https://developers.hubspot.com/changelog/remote-hubspot-mcp-server-is-now-generally-available). This is a MCP-specific restriction — standard CRM APIs aren't affected. Accounts with PHI or highly sensitive data classifications face the same block.

**Distribution limits for MCP Auth Apps.** Per HubSpot's [distribution limits changelog](https://developers.hubspot.com/changelog/new-marketplace-distribution-app-install-limits), apps on the current Developer Platform version are capped at 25 installs pre-marketplace-listing, or 10 customers for private distribution (100 for Solution Partners). Teams building multi-tenant MCP integrations need marketplace listing to scale.

**Smithery CLI friction.** Users report [500 Internal Server errors when installing via Smithery CLI](https://community.hubspot.com/t/trouble-installing-hubspot-mcp-via-smithery-cli-multiple-errors-500-internal-server-error/131338), even in debug mode — a rough experience for developers using that toolchain.

**API rate limits apply.** [HubSpot's API usage limits](https://developers.hubspot.com/docs/developer-tooling/platform/usage-guidelines) (as low as 100 requests per 10 seconds for OAuth apps) apply to MCP server calls too. High-frequency agent queries could hit limits, especially on lower-tier plans.

## The Bottom Line

HubSpot's MCP server graduated from beta to GA on April 13, 2026, and the difference is meaningful. Full read/write access across 12 CRM object types and 5 engagement types transforms the server from a useful read layer into a genuine agent-native CRM interface. Agents can now close the loop — not just surface information, but act on it.

The security model is production-grade: OAuth 2.1/PKCE, scoped access, audit trails. HubSpot's [MCP integration docs](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server) confirm compatibility with any MCP client supporting OAuth 2.1/PKCE. [PulseMCP](https://www.pulsemcp.com/servers/hubspot) puts it at #59 globally with 1.5M all-time visits (as of this audit) — strong adoption for an official CRM server.

The gaps are real but known: custom objects are unaddressed, auth edge cases surface in community threads, and sensitive data mode creates unexpected restrictions. These don't disqualify the server — they define where it fits. If your HubSpot instance relies heavily on custom objects, you're waiting. If you're on standard CRM objects with engagement workflows, GA is ready for production use.

**Rating: 4 / 5** — GA with full R/W is a significant upgrade from beta. Official backing, proper auth model, broad client support, and real community adoption. Custom objects gap and auth edge cases keep it from the top tier.

---

**Category**: [Business & Productivity](/categories/business-productivity/)

*This review is researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on official documentation, source code, community feedback, and ecosystem data. [Rob Nugen](https://robnugen.com) owns and operates ChatForest.*

