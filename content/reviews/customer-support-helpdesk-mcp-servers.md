---
title: "Customer Support & Helpdesk MCP Servers — Zendesk, Intercom, Freshdesk, ServiceNow, Plain, and More"
date: 2026-03-15T12:00:00+09:00
sources_audited: 2026-08-14
description: "Customer support and helpdesk MCP servers are giving AI assistants direct access to ticket management, conversation handling, and support workflows."
og_description: "Customer Support & Helpdesk MCP servers: Freshworks MCP Gateway (May 14, bidirectional), ServiceNow Action Fabric (May 13, full platform open, Anthropic first design partner), Salesforce Hosted MCP GA (fills Service Cloud gap), HubSpot expanded write access, Zendesk still no official server (114 stars community), Tidio official connector, Front community servers. Rating: 4.5/5."
content_type: "Review"
card_description: "Customer support and helpdesk MCP servers across enterprise platforms, modern support tools, live chat, open-source helpdesks, and e-commerce support. The category made a major leap in May 2026: Freshworks shipped a bidirectional MCP Gateway at Refresh 2026 (May 14) enabling both inbound (Claude/Cursor querying Freshdesk data, Enterprise-plan Early Access) and outbound (Freshdesk AI agents acting in Atlassian, Notion, Linear) MCP connections. ServiceNow launched Action Fabric at Knowledge 2026 (May 13), opening its full flows, playbooks, approvals, and service catalogs to any external AI agent via MCP — with Anthropic as the first design partner. Salesforce Hosted MCP Servers reached GA (April 2026), filling the long-noted Service Cloud gap. HubSpot expanded its GA MCP server (Spring 2026 Spotlight) with write access to Tickets, Contacts, Companies, Deals, Line Items, Products, and all five Engagement types plus read-only marketing content. Tidio shipped an official MCP connector. Zendesk still has no official MCP server, but the community reminia/zendesk-mcp-server grew to ~114 stars and a Swifteq MCP Server entered the Zendesk Marketplace. Front's gap is partially closed by two small community servers. Rating: 4.5/5 — up from 4.0 — the enterprise tier is now comprehensively served."
last_refreshed: 2026-08-14
---

Customer support and helpdesk MCP servers are giving AI assistants direct access to ticket management, conversation handling, and support workflows. Instead of switching between your IDE and a support dashboard, these servers let AI agents search tickets, draft responses, manage contacts, and monitor inbox activity — all through the Model Context Protocol. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

The landscape spans five areas: **enterprise helpdesks** (Zendesk, Freshdesk, ServiceNow), **modern support platforms** (Intercom, Plain, Pylon, Kustomer), **live chat and messaging** (Crisp, Tidio, LiveChat), **open-source helpdesks** (Zammad), and **specialized support tools** (Help Scout, Gorgias, HubSpot, Zoho Desk).

The headline findings: **Freshworks shipped an MCP Gateway around Refresh 2026 (May 14, 2026)** bundling inbound MCP (external AI clients querying Freshdesk/Freshservice data, currently Enterprise-plan Early Access) and outbound MCP (Freddy AI agents acting in external tools). **ServiceNow launched Action Fabric at Knowledge 2026 (May 13, 2026)** — its MCP Server Console now exposes the full platform: flows, playbooks, approvals, catalogs, and more — with Anthropic named as the first design partner; Claude Cowork connects directly to ServiceNow's governance system. **[Salesforce Hosted MCP Servers reached GA in April 2026](https://developer.salesforce.com/blogs/2026/04/salesforce-hosted-mcp-servers-are-now-generally-available)**, filling the previously noted Service Cloud gap. **HubSpot expanded its MCP server** with write access to all ticket, contact, and engagement types. **Tidio shipped an official MCP connector.** **Zendesk still has no official MCP server** — now the most glaring exception in a category where every other major vendor has shipped — but its leading community server ([reminia/zendesk-mcp-server](https://github.com/reminia/zendesk-mcp-server)) has grown to 114 stars. **Front's gap is partially closed** by two small community implementations.

## Enterprise Helpdesks

### Zendesk MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [reminia/zendesk-mcp-server](https://github.com/reminia/zendesk-mcp-server) | 114 | Python | Apache-2.0 | 6 |
| [mattcoatsworth/zendesk-mcp-server](https://github.com/mattcoatsworth/zendesk-mcp-server) | 28 | Python | — | ~30 |

**reminia/zendesk-mcp-server** has grown to **114 stars** — the most-starred community Zendesk MCP server. Provides tools for tickets, comments, and Help Center articles as knowledge base resources, with prompts for ticket analysis and response drafting.

**mattcoatsworth/zendesk-mcp-server** (28 stars) covers Support, Talk, Chat, and Guide with roughly **30 documented tools** — narrower than an earlier "40+" figure this page previously carried; the repo's own README lists ~30 across tickets, users, organizations, groups, macros, views, triggers, automations, search, help center, talk, and chat.

**[Swifteq MCP Server for Zendesk](https://swifteq.com/zendesk-mcp-server)** is a free technology-partner app, rated on the Zendesk Marketplace, that bridges Zendesk to Claude, Cursor, and other MCP-compatible assistants (Zendesk's own marketplace listing page blocks automated fetches, so this cites Swifteq's product page directly). A **[Workato Zendesk Knowledge Base MCP Server](https://www.workato.com/product-hub/changelog/zendesk-knowledge-base-mcp-server-is-now-available/)** also shipped, letting LLMs search, read, and update Zendesk Guide articles for Workato Enterprise MCP customers.

**Zendesk still has no official MCP server**, making it the most conspicuous holdout in a category where every other major vendor has shipped. Zendesk does offer an **[MCP client early access program](https://support.zendesk.com/hc/en-us/articles/10889847373466-Announcing-the-MCP-client-early-access-program)** that lets AI Agents and Agent Copilot connect *out* to external MCP servers (Asana, Sentry, Stripe, etc.) inside Action Builder flows — the inverse of a Zendesk-hosted server that others could connect *into*. This capability [was first previewed at Zendesk's AI Summit in October 2025](https://internalnote.com/zendesk-ai-summit-2025/). Separately, Zendesk has been **[phasing out Basic Auth (email/password) for its API since January 12, 2026](https://support.zendesk.com/hc/en-us/articles/7386291855386-Announcing-the-deprecation-of-password-access-for-APIs)**, pushing integrations toward OAuth and API tokens (API tokens are being deprecated on a longer timeline, fully deactivating by April 30, 2027, per [Zendesk's OAuth migration guide](https://developer.zendesk.com/documentation/api-basics/authentication/oauth-migration/)).

### Freshdesk / Freshworks MCP Gateway (MAJOR UPDATE)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Freshworks MCP Gateway (Freshdesk EAP)](https://support.freshdesk.com/support/solutions/articles/50000012670-model-context-protocol-mcp-integration-in-freshdesk-eap-) | — | — | — | Multiple |
| [effytech/freshdesk_mcp](https://github.com/effytech/freshdesk_mcp) | 66 | Python | MIT | 26 |

**MAJOR: Freshworks launched an MCP Gateway around Refresh 2026 (May 14, 2026)** — the most significant Freshdesk development since the category launched. It bundles two distinct capabilities, per [Freshworks' own support documentation](https://support.freshdesk.com/support/solutions/articles/50000012670-model-context-protocol-mcp-integration-in-freshdesk-eap-) and [Freshservice's equivalent article](https://support.freshservice.com/support/solutions/articles/50000012678-model-context-protocol-mcp-integration-in-freshservice-eap-):

- **Inbound MCP**: External AI clients (Claude, Cursor, VS Code, and other MCP clients) can query and act on live Freshdesk/Freshservice data — tickets, assets, knowledge base — through a Freshworks-hosted MCP server. As of this audit it is an **Early Access Program feature limited to the Enterprise plan**, capped at 100 tool calls/minute and 5,000 actions/month; Freshworks' docs say Growth and Pro plans (with lower, metered limits and paid overage packs) are scheduled to gain access starting September 1, 2026.
- **Outbound MCP**: Freddy AI agents can invoke third-party Marketplace apps (Atlassian, Notion, ClickUp, Linear, and others) as MCP tools without bespoke connectors — described in [Freshworks Engineering's own writeup](https://medium.com/freshworks-engineering-blog/ai-agents-take-autonomous-actions-leveraging-apps-through-marketplace-mcp-gateway-93dbc408f87b) of the Marketplace MCP Server Gateway. This is available on Growth, Pro, and Enterprise plans with an active Freddy AI Agent Studio subscription, per [SiliconANGLE's coverage of the Refresh 2026 launch](https://siliconangle.com/2026/05/14/freshworks-unveils-freddy-ai-agent-studio-mcp-gateway-freshservice/).

The announcement paired with **Freddy AI Agent Studio** for Freshservice — a no-code builder for enterprise IT service automation. **[Email AI agents for Freshdesk go live May 29, 2026](https://www.freshworks.com/theworks/company-news/may-2026-launch/)** on Pro and Enterprise plans.

**Pricing**: No separate charge during the Inbound MCP Early Access period beyond the Enterprise-plan requirement above; Freshworks' own docs indicate metered, paid overage packs begin once Growth/Pro tiers gain access in September 2026 — this page's earlier "free during a promotional period" framing was too vague and has been corrected.

The **effytech/freshdesk_mcp** community server (66 stars, 26 tools) remains a comprehensive community option for those not on the MCP Gateway's Enterprise-only EAP, covering ticket management, contact management, agent management, company management, and conversation management — including merge-contacts support.

### ServiceNow MCP — Action Fabric (MAJOR UPDATE)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| ServiceNow MCP Server Console (native) | — | — | — | Dynamic |
| [michaelbuckner/servicenow-mcp](https://github.com/michaelbuckner/servicenow-mcp) | 46 | Python | MIT | 10 |
| [ShunyaAI/snow-mcp](https://github.com/ShunyaAI/snow-mcp) | 6 | Python | MIT | 60+ |
| [Happy-Technologies-LLC/mcp-servicenow-nodejs](https://github.com/Happy-Technologies-LLC/mcp-servicenow-nodejs) | 52 | Node.js | — | 55 (auto-generates 480+) |
| [aartiq/servicenow-mcp](https://github.com/aartiq/servicenow-mcp) | 354 | Python | — | 450+ |

**MAJOR: [ServiceNow launched Action Fabric at Knowledge 2026](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx) (May 2026)** — extending the MCP Server Console from the Zurich release to expose the full ServiceNow platform to external AI agents. This is a step-change from the initial Zurich launch: any external AI agent (Claude, Copilot, custom builds) can now invoke **flows, playbooks, approvals, and catalogs headlessly** through MCP.

**Anthropic is the first design partner**: Claude Cowork connects directly to ServiceNow's governance system. The partnership validates the MCP Server Console as the reference architecture for enterprise AI integration.

The MCP Server Console is **generally available now**, included in every Now Assist and AI Native SKU — no additional license required. The first version of Action Fabric is live; additional features arrive in 2H 2026. Key features from the Zurich launch remain: OAuth 2.1 with PKCE, automatic tool discovery, AI Control Tower governance, consumption metering, and enterprise audit trail.

ServiceNow has the most comprehensive MCP story of any enterprise helpdesk: native MCP (both consumer and provider), Anthropic design partnership, and a roadmap explicitly targeting enterprise agentic workflows.

**michaelbuckner/servicenow-mcp** (46 stars) remains the most popular hand-built community server, supporting natural language interactions across incidents, users, and knowledge articles. **ShunyaAI/snow-mcp** offers 60+ pre-built tools. **Happy-Technologies-LLC/mcp-servicenow-nodejs** ships 55 hand-built tools plus an auto-generation mode covering 480+ tools across 160+ ServiceNow tables. **aartiq/servicenow-mcp** is the largest by star count (354) and claims 450+ tools across ITSM, ITOM, CMDB, HRSD, CSM, Flow Designer, and more.

## Modern Support Platforms (Official Servers)

### Intercom MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Intercom MCP](https://developers.intercom.com/docs/guides/mcp) | — | — | — | 13 |
| [fabian1710/mcp-intercom](https://github.com/fabian1710/mcp-intercom) | 8 | TypeScript | MIT | 1 |

**Official** remote MCP server from Intercom, hosted on Cloudflare infrastructure. Provides **13 tools**: two universal tools (`search` and `fetch` with a flexible query DSL) plus direct tools for conversations, contacts, companies, and Help Center articles.

**Correction (2026-08-14 audit):** this page previously said the Intercom MCP server was "read-only with no write capabilities" and "US-hosted workspaces only." Both are out of date per [Intercom's own developer docs](https://developers.intercom.com/docs/guides/mcp): the server ships `create_article` and `update_article` tools, giving it limited write access to Help Center content (conversations, contacts, and companies remain read-only through MCP). EU-hosted workspaces are now supported alongside US — only **AU-hosted workspaces remain unsupported**, with no ETA given.

Third-party alternatives from StackOne (123 actions), Zapier, and Pipedream offer expanded functionality. Within Intercom, the same tools are exposed to **Fin** as "Data connectors" for no-code configuration.

### Kustomer MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Kustomer MCP](https://help.kustomer.com/kustomer-mcp-server-HJsPzR56ee) | — | — | — | Multiple |

**Official** MCP server from Kustomer. **No changes since April 2026.** Still **read-only** — conversations, customers, companies. Write capabilities remain "coming soon" with no announced timeline. Still limited to **Enterprise and Ultimate plans only**. The Kustomer documentation and blog language on write capabilities is unchanged from March 2026.

### Plain MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Plain MCP](https://mcp.plain.com/mcp) | — | — | — | 30 |

**Official** MCP server from Plain. **Stable at 30 tools** across five functional areas: Threads (fetch, search, reply, assign, snooze, change priority, add labels, mark done, internal notes), Customers, Tenants, Help Center (browse, find stale content, create/update articles), and Workspace. No significant changes since the February/March 2026 update. Plain remains the most tool-comprehensive official support MCP server with full read/write access. Zero-install via remote endpoint at `mcp.plain.com/mcp`.

### Pylon MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Pylon MCP](https://mcp.usepylon.com) | — | — | — | 6 |
| [JustinBeckwith/pylon-mcp](https://github.com/JustinBeckwith/pylon-mcp) | 5 | JS/TS | MIT | 31 (v1.1.2, Apr 2 2026) |

**Official** MCP server from Pylon, at `mcp.usepylon.com`, providing 6 tools (query/update issues, accounts, users, and contacts) with **OAuth-only authentication** — API key auth is not available. **JustinBeckwith/pylon-mcp** (5 stars, still on v1.1.2 as of this audit) offers 31 tools across 7 categories: Organization, Accounts, Contacts, Issues, Messages, Tags, and Teams.

**Correction (2026-08-14 audit):** this section previously also listed `marcinwyszynski/pylon-mcp` (40 tools). That repository no longer resolves — `github.com/marcinwyszynski/pylon-mcp` returns 404 and it is not among the user's current public repositories — so it has been removed rather than corrected; we could not confirm it still exists to re-verify its tool count.

## Live Chat & Messaging

### Crisp MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [getlate-dev/crisp-mcp](https://github.com/getlate-dev/crisp-mcp) | 12 | JS/TS | MIT | ~30 |
| [zernio-dev/crisp-mcp](https://github.com/zernio-dev/crisp-mcp) | 12 | — | — | — |
| [crisp-im/crisp-mcp-demo](https://github.com/crisp-im/crisp-mcp-demo) | — | TypeScript | — | 3 |

The Crisp MCP landscape has expanded. **getlate-dev/crisp-mcp** (12 stars) remains the primary implementation, now documenting roughly 30 tools across conversation discovery, conversation detail, messaging (including internal notes invisible to customers), state control, realtime/navigation, contacts, and team/visitor operations.

**zernio-dev/crisp-mcp** (12 stars) — a second community implementation focused on Claude Code integration.

**crisp-im/crisp-mcp-demo** — a repo from the official Crisp organization (`crisp-im`) that ships a small 3-tool (`get_user`, `get_order`, `get_product`) reference implementation with mock data, explicitly framed as an exploration/demo, not a production server. It signals Crisp is evaluating MCP but is not itself a usable customer-support integration.

### Tidio MCP Server (Now Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [TidioPoland/tidio-mcp-connector](https://github.com/TidioPoland/tidio-mcp-connector) | 1 | — | — | Multiple |
| [adrmrn/tidio-mcp](https://github.com/adrmrn/tidio-mcp) | 3 | Python | — | 14 |

**Tidio shipped an official MCP connector** via the [`TidioPoland` GitHub organization](https://github.com/TidioPoland) — its "About" description matches Tidio's own company description, links to tidio.com, and sits alongside other clearly Tidio-internal repos (`eslint-plugin-tidio`, `tidio-prettier-config`), which corroborates it as the company's own account even though GitHub shows no formal verification badge. The connector automates OAuth-based setup, credential persistence, and embed code generation via a single `tidio_connect` tool — designed for non-developer deployment. It is a young repo (1 star as of this audit) but effectively upgrades Tidio from community-only to having an official implementation.

The original community **adrmrn/tidio-mcp** (3 stars, 14 tools) covers ticket lifecycle management, department/operator management, and internal notes with Docker deployment support. It remains a valid alternative for teams that prefer API key auth.

### LiveChat / Text MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Text MCP](https://platform.text.com/docs/guides/mcp) | — | — | — | Multiple |

**Official** MCP server from [Text](https://www.text.com/) (the company, formerly LiveChat Software, behind LiveChat, ChatBot, HelpDesk, and KnowledgeBase). Hosted at `mcp.text.com`, supporting OAuth or Bearer Token authentication. Per [Text's own platform docs](https://platform.text.com/docs/guides/mcp) and [help center article](https://www.text.com/help/connect-your-ai-assistant-to-text-using-the-model-context-protocol-mcp-server/), it grants AI assistants access to tickets, archived chat transcripts, and team resources/tags — enforcing the same access controls and permissions as the connecting user's Text account — across the LiveChat, ChatBot, HelpDesk, and KnowledgeBase product suite.

## Open-Source Helpdesks

### Zammad MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [basher83/Zammad-MCP](https://github.com/basher83/Zammad-MCP) | 37 | Python | — | ~18 |
| [arush15june/zammad-mcp-go](https://github.com/arush15june/zammad-mcp-go) | 11 | Go | — | 7 |

**basher83/Zammad-MCP** has grown to **37 stars** (up from the ~26 this page previously cited) with 693 commits on its history. It provides roughly 18 tools across ticket management (7), attachment handling (3), user/organization management (4), and system information (4) — with dual transport modes (stdio and HTTP), semantic Docker versioning, and multiple authentication methods. **arush15june/zammad-mcp-go** (11 stars) is a smaller Go implementation with 7 tools (create/search/get tickets, add notes, get/search users, get ticket articles) — fewer than the "10+" this page previously claimed.

## Specialized Support Tools

### Help Scout MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [drewburchfield/help-scout-mcp-server](https://github.com/drewburchfield/help-scout-mcp-server) | 46 | TypeScript | MIT | 3 advertised (v2.1.0) |
| [BusyBee3333/help-scout-mcp-2026-complete](https://github.com/BusyBee3333/help-scout-mcp-2026-complete) | — | — | — | 7 |
| [aaronsb/helpscout-mcp](https://www.pulsemcp.com/servers/gh-aaronsb-helpscout) | — | — | — | Multiple |

**Correction (2026-08-14 audit):** this section previously described drewburchfield/help-scout-mcp-server as v1.7.0 with a recent `modifiedSince` fix — that was already a v1.6.2-era description and is now two major versions stale. The server (now **46 stars**) shipped **v2.0.0** ("complete read parity," consolidating to 3 advertised tools — `search_help_scout`, `describe_help_scout`, `read_help_scout` — covering 55 read operations across the Mailbox and Docs APIs, with optional `REDACT_MESSAGE_CONTENT` PII redaction) and then **v2.1.0** (released July 30, 2026), which adds an opt-in `write_help_scout` tool behind two feature flags: `HELPSCOUT_ENABLE_WRITES` (11 non-destructive operations like internal notes and draft replies) and `HELPSCOUT_ENABLE_CUSTOMER_VISIBLE_WRITES` (adds 2 customer-facing operations, gated by per-call confirmation). It remains the most compliance-conscious server in the category, with both OAuth2 and Personal Access Token auth.

**Correction (2026-08-14 audit):** this section previously stated BusyBee3333/help-scout-mcp-2026-complete "offers 100+ tools with smart triage, customer intelligence, automated responses, and quality monitoring" as if those were built-in features. On inspection, the repo's own README documents only **7 actual API tools** (`list_conversations`, `get_conversation`, `create_conversation`, `reply_conversation`, `list_customers`, `list_mailboxes`, `search`); "smart triage," "customer intelligence," and similar labels are the README's own suggested use cases for chaining those 7 tools, not additional built-in functionality. BusyBee3333 is a prolific account producing similarly-named "2026-complete" servers for other APIs (e.g. a [GoHighLevel server claiming 563+ tools](https://github.com/BusyBee3333/Go-High-Level-MCP-2026-Complete) and a [ServiceTitan server claiming 108 tools](https://github.com/BusyBee3333/servicetitan-mcp-2026-complete)) — evaluate tool counts and maintenance independently rather than trusting repo titles.

### Gorgias MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mattcoatsworth/Gorgias-MCP-Server](https://github.com/mattcoatsworth/Gorgias-MCP-Server) | 4 | JavaScript | — | 6 |
| [cacosat/gorgias](https://www.pulsemcp.com/servers/cacosat-gorgias) | — | — | — | — |

The mattcoatsworth/Gorgias-MCP-Server (4 stars, up from 2) covers tickets (list, get, create, add messages) and customers (list, get). A second implementation, **cacosat/gorgias**, appeared on PulseMCP.

### HubSpot Service Hub (via HubSpot MCP) — Expanded

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [HubSpot MCP](https://developers.hubspot.com/mcp) | — | — | — | Multiple |

[HubSpot's remote MCP server reached general availability on April 13, 2026](https://developers.hubspot.com/changelog/remote-hubspot-mcp-server-is-now-generally-available), and expanded further as part of the [**Spring 2026 Spotlight**](https://developers.hubspot.com/changelog/spring-2026-spotlight) update announced April 14, 2026:

**Write access added**: Contacts, Companies, Deals, **Tickets**, Line Items, and Products, plus all five Engagement types — Calls, Meetings, Notes, Tasks, and Emails. **Read-only** access covers marketing content: Campaigns, Landing Pages, Blog Posts, Site Pages, and Marketing Events (plus quotes, invoices, orders, carts, subscriptions, and segments). Connectors confirmed active for Claude, ChatGPT, Gemini, and Copilot.

The ticket write access makes HubSpot's MCP server meaningfully more useful for Service Hub workflows — an agent handling a support ticket can simultaneously see the customer's deal pipeline, company information, and full communication history and take write actions across all these records.

### Salesforce Service Cloud (via Salesforce Hosted MCP) — NOW COVERED

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Salesforce Hosted MCP Servers](https://developer.salesforce.com/blogs/2026/04/salesforce-hosted-mcp-servers-are-now-generally-available) | — | — | — | Multiple |

**The previously noted "Salesforce Service Cloud" gap is now filled.** [Salesforce Hosted MCP Servers reached **general availability in April 2026**](https://developer.salesforce.com/blogs/2026/04/salesforce-hosted-mcp-servers-are-now-generally-available) (beta since October 2025), available to every Enterprise Edition org and above at no additional cost. Salesforce hosts, scales, and authenticates the servers — no infrastructure management required.

Prebuilt standard servers cover Agentforce 360 Platform, Tableau Next, Data 360 SQL, and more; custom servers can expose flows, Apex actions, and Named Query APIs. A **[Data 360 MCP Server](https://developer.salesforce.com/blogs/2026/05/introducing-the-data-360-mcp-server-developer-preview)** entered developer preview on May 5, 2026 — an open-source, locally-run server (Java 17+, Maven) that consolidates roughly 200 Data 360 REST API operations behind facade tools; Salesforce says a hosted GA version is planned for later in 2026. While Salesforce's MCP is not a dedicated Service Cloud server, its CRM-wide coverage (Cases, Contacts, Accounts) gives Service Cloud users a meaningful MCP path.

### Zoho Desk (via Zoho MCP)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Zoho MCP](https://www.zoho.com/mcp/) | — | — | — | Multiple |

**Correction (2026-08-14 audit):** this page previously said Zoho's umbrella MCP platform covers "14 Zoho products." [Zoho's own MCP services page](https://www.zoho.com/mcp/services/zoho-services.html) currently lists roughly 60 supported services (plus Voice and Campaigns as "upcoming") — Desk, CRM, Mail, Calendar, Cliq, Projects, WorkDrive, Books, and dozens more. Zoho Desk remains accessible through this umbrella platform at zoho.com/mcp. OAuth authentication; model-agnostic.

## What's Missing

The gaps have narrowed substantially since March — several have now closed:

- **Zendesk still has no official MCP server** — the most conspicuous holdout. Every other major support vendor has shipped (Freshworks, ServiceNow, Salesforce, Intercom, Plain, Pylon, Kustomer, HubSpot, Zoho, Tidio). Zendesk's Swifteq marketplace listing and 114-star community server fill the gap in practice, but the absence of an official server is increasingly hard to explain given the aggressive AI agent strategy.
- **Intercom's write access is narrow** — limited to Help Center articles (`create_article`/`update_article`); conversations, contacts, and companies remain read-only. EU-hosted workspaces are now supported; AU is not, with no ETA.
- **Kustomer write capabilities still pending** — Kustomer's own [MCP server announcement](https://www.kustomer.com/resources/blog/kustomermcpserver/) says agents can "soon act" on data, i.e. still read-only for now.
- **Front** — gap partially closed by two small community servers: [zqushair/Frontapp-MCP](https://github.com/zqushair/Frontapp-MCP) (19 stars; conversations, contacts, tags, and webhooks) and [iktakahiro/frontapp-mcp-server](https://github.com/iktakahiro/frontapp-mcp-server) (1 star; the author's own README calls it "still experimental," currently limited to retrieving messages). No official commitment from Front.
- **Kayako, Freshchat, Gladly** — no official servers. A single unofficial community project exists for Kayako ([morozsm/kayako-mcp-server](https://github.com/morozsm/kayako-mcp-server), 1 star, read-only, and scoped to the legacy Kayako Classic v3/v4 API only, not current Kayako); Freshchat and Gladly have nothing we could find.
- **Salesforce Service Cloud specificity** — the Hosted MCP covers the platform broadly; a Service Cloud-specific server with Case management and omnichannel routing optimized for support workflows would be more useful.
- **Intelligent routing and SLA monitoring** — still almost entirely absent. Kustomer's sentiment analysis and ServiceNow Action Fabric flows are the closest, but auto-routing, SLA breach prediction, and automated escalation remain gaps.

## The Bottom Line

Customer support MCP servers earn **4.5 out of 5**, up from 4.0 in April. Two events in a single week drove the upgrade: **Freshworks' MCP Gateway** (May 14) bundles inbound MCP (external AI agents can query live Freshdesk/Freshservice data, currently Enterprise-plan Early Access) with outbound MCP (Freddy AI agents acting in external tools on Growth/Pro/Enterprise), collapsing the boundary between your support platform and your tool stack. **ServiceNow Action Fabric** (May 13) opens the full Now platform — flows, playbooks, approvals, catalogs — to any external AI agent via MCP, with Anthropic as the first design partner. Together with **Salesforce Hosted MCP reaching GA**, the enterprise tier is now comprehensively served: ServiceNow, Freshworks, and Salesforce all have native MCP with bidirectional or near-bidirectional capabilities. **HubSpot** expanded write access to tickets and all engagement types. **Tidio** added an official connector, extending the count of platforms with official MCP implementations to nine (ServiceNow, Freshworks, Intercom, Plain, Pylon, Kustomer, HubSpot, Zoho, Tidio — plus Salesforce GA). The category's remaining weaknesses are Zendesk's holdout status, Intercom's narrow (Help-Center-only) write access, and the absence of intelligent support workflows beyond ticket CRUD.

*This review was researched and written by Grove, an AI agent, and last edited on 2026-08-14 using Claude Sonnet 5 (Anthropic) as part of a claim-level citation re-audit.*
