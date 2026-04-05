---
title: "Best CRM MCP Servers in 2026"
date: 2026-03-22T22:00:00+09:00
description: "Salesforce, HubSpot, Pipedrive, Attio, Dynamics 365, Zoho, Monday.com, Close, and more — we've reviewed 40+ CRM MCP servers across 10 platforms. Here's what works, what's emerging, and where the gaps are."
og_description: "40+ CRM MCP servers reviewed across Salesforce, HubSpot, Pipedrive, Attio, Dynamics 365, Zoho, Monday.com, Close, and open-source CRMs. The definitive comparison with honest ratings."
content_type: "Comparison"
card_description: "The definitive guide to CRM MCP servers in 2026. We've reviewed 40+ servers across Salesforce (official + community), HubSpot (official + community), Pipedrive, Attio, Dynamics 365 (now with official servers), Zoho, Monday.com, Close, and open-source CRMs like Twenty. Every recommendation links to a full review."
last_refreshed: 2026-04-05
---

CRM data is some of the most valuable information a business owns — contacts, deals, pipeline stages, revenue forecasts, customer histories. Giving an AI agent access to that data changes how sales teams, customer success managers, and operations work. Instead of clicking through dashboards, you ask.

We've researched 40+ CRM MCP servers across the full landscape. This guide synthesizes all of that into one page: what's worth using, what's not, and where the gaps are.

> **🔒 Security note (April 2026):** The MCP ecosystem has seen 30+ CVEs filed in the past 60 days, including critical authentication flaws in Azure MCP infrastructure (CVE-2026-32211, CVSS 9.1) and a command injection RCE in a Salesforce community MCP server (CVE-2026-26029). Always pin versions, audit tool permissions, and prefer official servers with enterprise auth. See our [MCP security coverage](/guides/mcp-security/) for the full picture.

*Note: Our recommendations are based on documentation review, GitHub analysis, and community feedback — not hands-on testing of every server. Star counts were verified in April 2026.*

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| Salesforce (official) | [salesforcecli/mcp](https://github.com/salesforcecli/mcp) | 342 | [forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted) (39 stars, hosted) |
| Salesforce (community) | [smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce) | 170 | [tsmztech/mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce) (149 stars) |
| HubSpot (official) | [HubSpot Remote MCP](https://developers.hubspot.com/mcp) | Official | [HubSpot Developer MCP](https://developers.hubspot.com/docs/developer-tooling/local-development/mcp-server) (GA, app/CMS dev) |
| HubSpot (community) | [peakmojo/mcp-hubspot](https://github.com/peakmojo/mcp-hubspot) | 118 | [adeel0x01/hubspot-mcp-tools](https://github.com/adeel0x01/hubspot-mcp-tools) (87+ tools) |
| Pipedrive | [iamsamuelfraga/mcp-pipedrive](https://github.com/iamsamuelfraga/mcp-pipedrive) | 4 | [WillDent/pipedrive-mcp-server](https://github.com/WillDent/pipedrive-mcp-server) (53 stars, read-only) |
| Attio (official) | [Attio MCP Server](https://docs.attio.com/mcp/overview) | Official | [kesslerio/attio-mcp-server](https://github.com/kesslerio/attio-mcp-server) (60 stars, community) |
| Dynamics 365 (official) | [D365 Sales MCP](https://learn.microsoft.com/en-us/dynamics365/sales/connect-to-model-context-protocol-sales) | Official | [D365 ERP MCP](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/mcp-server) (GA, Finance & SCM) |
| Monday.com (official) | [mondaycom/mcp](https://github.com/mondaycom/mcp) | 390 | — |
| Close (official) | [Close MCP Server](https://mcp.close.com/mcp) | Official | [bcharleson/close-crm-cli](https://github.com/bcharleson/close-crm-cli) (160+ commands) |
| Zoho | [Zoho MCP Platform](https://www.zoho.com/mcp/) | Official | [CData Zoho CRM MCP](https://github.com/CDataSoftware/zoho-crm-mcp-server-by-cdata) (read-only) |
| Open-source CRM | [mhenry3164/twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server) | 47 | [Descomplicar/mcp-perfex-crm](https://github.com/Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm) (186 tools) |

## Why CRM MCP servers matter

CRM operations involve constant context-switching between apps, dashboards, and spreadsheets. MCP servers turn these into natural-language commands.

The value comes in three forms:

1. **Pipeline management automation.** "Show me all deals closing this month with value over $50K" or "Update the deal stage for Acme Corp to Negotiation" — instead of navigating multiple screens and filters. At scale, agents can process bulk operations across hundreds of records.
2. **Data enrichment and hygiene.** Agents can find duplicate contacts, fill missing fields from web research, and maintain data quality across your entire CRM — tasks that would take hours manually.
3. **Cross-platform insights.** Ask "Which sales rep has the highest win rate this quarter?" or "What's our average deal cycle time?" and get answers pulled directly from your CRM's live data.

The landscape splits into ten categories: **Salesforce** (official + deep community ecosystem), **HubSpot** (newly official + community), **Pipedrive** (community-driven), **Attio** (now with official server), **Dynamics 365** (newly official from Microsoft), **Monday.com** (official, 390 stars), **Close** (official hosted, 57 tools), **Zoho** (official platform), **open-source CRMs** (Twenty, Perfex), and **niche platforms** (Clay, Bitrix24, Gainsight, Method CRM).

---

## Salesforce servers

Salesforce dominates the CRM MCP space with 140+ repositories on GitHub, an officially-maintained server with 60+ tools, and a hosted deployment option for enterprise use.

### The winner: salesforcecli/mcp (Official)

**Stars:** 342 | **Language:** TypeScript | **License:** Apache 2.0 | **Status:** Beta

[salesforcecli/mcp](https://github.com/salesforcecli/mcp) is officially maintained by Salesforce as part of their CLI toolchain. It's by far the most comprehensive CRM MCP server in any ecosystem. Rapid development continues — v0.30.5 shipped April 3, 2026, with the code-analysis toolset reaching GA and auto-approval for read-only tools (no more confirmation prompts for safe actions).

**Why it wins:** 60+ tools organized into dynamic toolsets that keep agent context focused. Instead of loading all tools at once, you specify which toolset(s) to enable — SOQL for queries, Metadata for deployments, Apex for testing. This is a design pattern more MCP servers should adopt.

**Key toolsets:**
- **SOQL** — query Salesforce data using SOQL
- **Metadata** — deploy, retrieve, list, describe metadata components
- **Apex** — run tests, execute anonymous Apex, view test results
- **LWC** — Lightning Web Component development
- **Code Analysis** — static analysis and quality checks
- **DevOps Center** — deployment and pipeline management

**Auth:** Requires Salesforce CLI installed and authenticated via `sf org login web` or VS Code SFDX extension.

**The catch:** Developer-focused, not user-focused. The toolsets target Salesforce developers, not sales reps who want "show me my open deals." You'll need SOQL fluency. Also still in beta — breaking changes possible.

**Best for:** Salesforce developers who want official, comprehensive MCP access with dynamic tool loading.

### Also notable: forcedotcom/mcp-hosted

**Stars:** 39 | **License:** Apache 2.0 | **Status:** Open Beta

[forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted) is the enterprise deployment model. Salesforce runs the MCP server — your agent connects remotely via External Client Apps. Admin-governed endpoints with enterprise-grade auth. Toolsets include sobject operations (14 tools), Tableau Next (21 tools), Data Cloud queries, and Revenue Cloud (15 tools). Originally targeted for GA in Spring '26, it remains in open beta — watch TDX 2026 (April 15-16) for a possible GA announcement.

**Best for:** Enterprise teams that need centrally-managed, admin-governed MCP access to Salesforce.

### Community Salesforce servers

**[smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce)** (170 stars, Python, MIT) — The leading community alternative. SOQL queries, SOSL search, record CRUD, metadata retrieval, Tooling API, and direct REST API calls. Three auth modes (OAuth, CLI, username/password). New v0.1.13 (March 31, 2026) added token-optimized output formats and a test suite. Best Python-based Salesforce MCP server.

**[tsmztech/mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce)** (149 stars, TypeScript) — Strong feature set including aggregate queries, field-level security management, anonymous Apex execution, debug logging, and multi-org support. Ships as a Claude Desktop extension (`.dxt`). One of the few servers that handles field-level security explicitly.

**[advancedcommunities/salesforce-mcp-server](https://github.com/advancedcommunities/salesforce-mcp-server)** (25 stars, TypeScript, MIT) — 40 tools with a standout safety feature: **read-only mode** and **org restriction** to prevent accidental changes to production orgs.

> **⚠️ Salesforce ecosystem security note:** CVE-2026-26029 (CVSS 7.5 HIGH) affects [akutishevsky/sf-mcp-server](https://github.com/akutishevsky/sf-mcp-server), a smaller tutorial/demo Salesforce MCP server — command injection RCE via unsafe `child_process.exec`. None of the servers recommended above are affected, but it underscores the need to vet community servers carefully before granting them Salesforce credentials.

---

## HubSpot servers

HubSpot's MCP story has transformed since late 2025. The once-empty official repo has been replaced by two production servers — a remote CRM server and a developer tools server — while the community ecosystem continues to fill specialized gaps.

### The winner: HubSpot Remote MCP Server (Official)

**Status:** Public Beta | **Transport:** Remote (mcp.hubspot.com) | **Auth:** OAuth 2.0

[HubSpot's Remote MCP Server](https://developers.hubspot.com/mcp) is the official CRM MCP server, available as a remote endpoint at `mcp.hubspot.com`. It provides read-only access to core CRM objects through natural language.

**Why it wins:** Official backing, hosted infrastructure (no local setup), and OAuth-based auth that respects existing HubSpot permissions. Available to all HubSpot customers at no extra cost.

**Key features:**
- **Read-only CRM access** — contacts, companies, deals, tickets, invoices, products, line items, quotes, subscriptions, orders, carts, and users
- **9 tools at launch** — covering the core CRM objects and engagement management
- **OAuth 2.0 auth** — uses self-service MCP Auth Apps (Public Beta since January 2026)
- **Sensitive data filtering** — excludes personal health information and other sensitive fields by default
- **Remote hosted** — no local server installation required

**The catch:** Read-only. You can pull summaries, trends, associations, and pipeline snapshots, but you can't update CRM data. For write operations, you need the community servers. Also still in beta.

**Best for:** HubSpot users who want safe, official, read-only CRM access for AI agents — great for reporting, analysis, and pipeline visibility.

### Also notable: HubSpot Developer MCP Server (Official, GA)

[HubSpot Developer MCP Server](https://developers.hubspot.com/docs/developer-tooling/local-development/mcp-server) reached GA in February 2026. This is for developers building HubSpot apps and CMS assets — not for CRM data access. Available as `@hubspot/mcp-server` on NPM. Works with VS Code, Claude Code, Cursor, and other MCP-compatible IDEs.

**Best for:** Developers building HubSpot apps, themes, and CMS content — not for sales teams querying CRM data.

### Community HubSpot servers

**[peakmojo/mcp-hubspot](https://github.com/peakmojo/mcp-hubspot)** (118 stars, Python, MIT) — The most popular community HubSpot MCP server, and it offers something no official server does: **FAISS semantic search** across contacts and companies. Builds a local vector index of your HubSpot data for "find companies similar to X" queries. 7 tools covering contacts, companies, and engagement history with built-in duplicate prevention. Docker, Smithery, or local install. Note: last commit was November 2025 — development has slowed.

**[adeel0x01/hubspot-mcp-tools](https://github.com/adeel0x01/hubspot-mcp-tools)** (4 stars, TypeScript, MIT) — Now **87+ tools** across 9 categories including deals, tickets, pipelines, and custom objects. Much broader coverage than peakmojo, but very low adoption. If you need HubSpot write access and deal/ticket management, this is currently the only option.

**[scopiousdigital/hubspot-mcp](https://github.com/scopiousdigital/hubspot-mcp)** (10 stars, JavaScript, MIT) — 6+ tools with Private App auth (14 scopes). Lighter-weight alternative. Last commit March 2025 — appears dormant.

---

## Pipedrive servers

Pipedrive's MCP ecosystem is community-driven with no official server. The landscape has expanded significantly — multiple write-capable options now exist alongside the popular read-only server.

### The winner: iamsamuelfraga/mcp-pipedrive

**Stars:** 4 | **Language:** TypeScript | **Tools:** 100+

[iamsamuelfraga/mcp-pipedrive](https://github.com/iamsamuelfraga/mcp-pipedrive) is the most comprehensive Pipedrive MCP server, claiming 100+ tools across 10 categories. Full CRUD across deals, persons, organizations, activities, notes, leads, products, and pipelines.

**Why it wins:** Broadest tool coverage by far. If you need deep Pipedrive automation, this is the most feature-complete option available.

**The catch:** 4 stars — very new, very low adoption. Less community validation than WillDent's read-only server.

**Best for:** Pipedrive power users who need full read/write automation with broad entity coverage.

### Also notable: WillDent/pipedrive-mcp-server

**Stars:** 53 | **Language:** TypeScript | **License:** MIT | **Tools:** 16

[WillDent/pipedrive-mcp-server](https://github.com/WillDent/pipedrive-mcp-server) is the most popular Pipedrive server by adoption. 16 tools and 8 predefined prompts for deals, persons, organizations, and pipelines. **Read-only** — no creating or modifying records. Added Docker support, SSE transport, JWT auth, and rate limiting. If you only need to query your pipeline and pull reports, this is the safer, more validated choice.

### Also notable: Teapot-Agency/mcp_pipedrive

**Stars:** 5 | **Language:** TypeScript | **License:** MIT | **Tools:** 40

[Teapot-Agency/mcp_pipedrive](https://github.com/Teapot-Agency/mcp_pipedrive) — 20 read + 20 write operations covering deals, persons, organizations, activities, notes, and leads. Fuzzy person search and soft delete recovery. A solid middle ground between WillDent's read-only approach and iamsamuelfraga's 100+ tool breadth.

---

## Attio — Now with an official server

Attio's MCP story has leveled up. The platform now has its own first-party hosted MCP server alongside the excellent community server — giving Attio users two strong options depending on their needs.

### The winner: Attio MCP Server (Official)

**Status:** GA | **Transport:** Remote (mcp.attio.com) | **Auth:** OAuth | **Tools:** 20+

[Attio's official MCP Server](https://docs.attio.com/mcp/overview) is hosted at `mcp.attio.com/mcp` and provides 20+ tools across 6 categories: Records & Objects (5), Notes (4), Tasks (2), Meetings & Calls (4), Emails (3), and Workspace (3).

**Why it wins:** Official backing, hosted infrastructure (no local setup), and OAuth authentication. Read operations are auto-approved; write operations require confirmation. This is the zero-friction path to Attio + AI.

**Best for:** Attio users who want official, hosted MCP access with sensible safety defaults.

### Also excellent: kesslerio/attio-mcp-server (Community)

**Stars:** 60 | **Language:** TypeScript | **License:** Apache 2.0 | **Commits:** 1,326+

[kesslerio/attio-mcp-server](https://github.com/kesslerio/attio-mcp-server) remains one of the most actively maintained CRM MCP servers by commit count. For a CRM with a fraction of Salesforce's market share, the MCP server quality is disproportionately high.

**Why it's excellent:** Architectural elegance. The server consolidates 70+ resource-specific operations into 35 tools (21 universal + 11 list + 3 workspace member) through parameter-based routing — a 68% tool reduction while maintaining complete CRM surface coverage. This is the design pattern every CRM MCP server should study.

**Key features:**
- **Complete CRUD** for Companies, People, Deals, Tasks, Lists, and Notes
- **Advanced AND/OR filtering** and batch operations
- **Content search** across all objects
- **10 MCP prompts** and **3 Claude Skills**
- **OAuth support** for Cloudflare Workers deployment
- **Safety annotations** for OpenAI compatibility
- **Custom object display names** fetched from Attio API
- **Levenshtein distance suggestions** for attribute name typos

**Best for:** Attio power users who want deeper tool coverage, self-hosted control, or the architectural elegance of parameter-based routing.

---

## Dynamics 365 — Microsoft finally arrives

Microsoft has closed the Dynamics 365 MCP gap with two official servers — one for Sales and one for Finance & Supply Chain Management (ERP). The landscape has transformed from "minimal" to "officially supported."

### The winner: Dynamics 365 Sales MCP Server (Official)

**Status:** GA | **Tools:** 20 | **Auth:** Microsoft Entra ID

[Dynamics 365 Sales MCP Server](https://learn.microsoft.com/en-us/dynamics365/sales/connect-to-model-context-protocol-sales) provides 20 tools covering lead research, account research, competitor research, opportunity insights, outreach email drafting, and sales record summaries. Integrates with Copilot's Sales Qualification Agent and Sales Close Agent capabilities.

**Why it wins:** Official Microsoft backing, deep integration with Copilot for Sales features, and comprehensive coverage of the sales workflow — from lead research to close. This is exactly what the guide previously said was missing.

**Key tools include:** `get_lead_research`, `get_account_research`, `get_competitor_research`, `draft_outreach_email`, `get_sales_record_summary`, `get_key_opportunity_insights`.

**Best for:** Dynamics 365 Sales users who want official, enterprise-grade MCP access integrated with Microsoft's AI sales stack.

### Also notable: Dynamics 365 ERP MCP Server (Official)

**Status:** GA (February 2026) | **Auth:** Microsoft Entra ID

Microsoft's D365 Finance & Supply Chain Management MCP server reached general availability in February 2026. Provides Form Tools, Data Tools, and Action Tools for ERP operations. The earlier "static" MCP server is being retired in 2026, replaced by this dynamic version. Microsoft recommends Claude Sonnet as the model for best results — a notable endorsement.

**Best for:** D365 Finance & Operations teams who need AI agent access to ERP data and workflows.

### Community Dynamics 365 servers

**[dynamics365ninja/d365fo-mcp-server](https://github.com/dynamics365ninja/d365fo-mcp-server)** (38 stars, TypeScript) — 54 AI tools for X++ code navigation in D365 Finance & Operations. Created January 2026. Developer-focused, not CRM-focused.

**[demiliani/D365BCAdminMCP](https://github.com/demiliani/D365BCAdminMCP)** (6 stars) — 34 tools for Business Central administration.

**[srikanth-paladugula/mcp-dynamics365-server](https://github.com/srikanth-paladugula/mcp-dynamics365-server)** (18 stars, TypeScript, MIT) — The original community server. Just 5 tools. Superseded by the official servers for most use cases.

---

## Monday.com — The biggest surprise

### The winner: mondaycom/mcp (Official)

**Stars:** 390 | **Language:** TypeScript | **Transport:** Remote (monday.com/w/mcp) + stdio

[mondaycom/mcp](https://github.com/mondaycom/mcp) is Monday.com's official MCP server — and at 390 stars, it's one of the most popular CRM MCP servers in the entire ecosystem. Available on all Monday.com plans at no additional cost.

**Why it wins:** Official backing, high community adoption, and broad coverage across Monday.com's work management and CRM features. Supports both hosted remote (monday.com/w/mcp) and local stdio transports. OAuth and API token authentication.

**Key features:**
- **Item and Board operations** — full CRUD across Monday.com boards
- **Account management** — user and team operations
- **WorkForms** integration
- **Dynamic API Tools** (beta) — auto-generated tools from Monday.com's API
- **Apps Framework Tools** — for building Monday.com apps
- **Available on all plans** — no premium tier required

**The catch:** Monday.com's CRM is built on their work management platform, so the MCP server is oriented toward boards and items rather than traditional CRM objects (contacts, deals, pipelines). If you think in CRM terms, there's a mental model translation.

**Best for:** Monday.com CRM users. The official server is strong enough that community alternatives aren't needed.

---

## Close — Official and impressive

### The winner: Close MCP Server (Official)

**Status:** GA | **Transport:** Remote (mcp.close.com) | **Auth:** OAuth 2.0 | **Tools:** 57

[Close's official MCP Server](https://help.close.com/docs/mcp-server) is hosted at `mcp.close.com/mcp` and provides 57 tools — one of the most comprehensive official CRM MCP servers in the ecosystem. HTTP Streamable transport with OAuth 2.0 and Dynamic Client Registration.

**Why it wins:** 57 tools is serious coverage. Three permission scopes (`mcp.read`, `mcp.write_safe`, `mcp.write_destructive`) give fine-grained control over what an AI agent can do. The read/safe-write/destructive-write separation is a thoughtful security model that more CRM vendors should adopt.

**Best for:** Close CRM users. The official server is comprehensive enough for most use cases.

### Also notable: bcharleson/close-crm-cli

**Stars:** 1 | **Tools:** 160+ commands across 30 resource groups

[bcharleson/close-crm-cli](https://github.com/bcharleson/close-crm-cli) — Community CLI + MCP server created March 2026. Much broader command coverage than the official server, but extremely new and low adoption.

---

## Zoho — The platform play

### The winner: Zoho MCP Platform (Official)

**Status:** GA | **Transport:** Remote (mcp.zoho.com) | **Auth:** OAuth

[Zoho MCP](https://www.zoho.com/mcp/) is Zoho's official MCP platform — not just a CRM server, but a platform that exposes tools from across the Zoho suite (CRM, Mail, Calendar, Desk, Cliq, Projects, WorkDrive) plus 500+ third-party apps.

**Why it wins:** Official backing from Zoho, model-agnostic design, and cross-app workflows. Instead of building separate MCP servers for each Zoho product, the platform provides a unified interface with a configuration UI, security controls, and pre-built integrations.

**Key features:**
- **Multi-app coverage** — CRM, Mail, Calendar, Desk, Cliq, Projects, WorkDrive
- **500+ third-party integrations** — Asana, Twilio, OneDrive, Notion, and more
- **Configuration UI** — visual setup at mcp.zoho.com
- **Model-agnostic** — works with any LLM through standard MCP clients
- **Security controls** — admin-managed permissions and access policies

**The catch:** Platform approach means CRM-specific depth may lag behind dedicated CRM MCP servers. Early documentation suggests broad but shallow tool coverage compared to Salesforce's 60+ developer-focused tools.

**Best for:** Zoho ecosystem users who want unified MCP access across all their Zoho apps — especially teams using multiple Zoho products together.

### Also notable: CData Zoho CRM MCP Server

[CDataSoftware/zoho-crm-mcp-server-by-cdata](https://github.com/CDataSoftware/zoho-crm-mcp-server-by-cdata) provides read-only access to Zoho CRM through CData JDBC Drivers. Natural language queries over relational SQL models. For full CRUD, CData points to their commercial Connect AI platform.

---

## Open-source and niche CRMs

### Twenty CRM

**[mhenry3164/twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** (47 stars, JavaScript, MIT) — For [Twenty](https://twenty.com), the open-source CRM. Dynamic schema discovery, advanced search, full CRUD across people, companies, tasks, and notes. If you've chosen Twenty as your CRM, this is a solid integration.

### Clay

**[clay-inc/clay-mcp](https://github.com/clay-inc/clay-mcp)** (30 stars) — First-party from Clay (the contact enrichment and outbound platform). Contact search, interaction retrieval, analytics, calendar integration. Also available as a hosted endpoint at `mcp.clay.earth/mcp`. Guided login flow for auth.

### Gainsight (NEW)

**[Gainsight MCP](https://www.gainsight.com)** — Announced April 2, 2026. Official MCP support across Gainsight CS and Staircase AI. Enables AI agents to access customer health scores, renewal timelines, sentiment trends, manage CTAs, log activities, and build success plans. The first customer success platform with MCP support — significant for post-sale CRM workflows.

### Bitrix24

**[gunnit/bitrix24-mcp-server](https://github.com/gunnit/bitrix24-mcp-server)** (25 stars, TypeScript, MIT) — Contact, deal, task, and lead management for Bitrix24. Rate limiting (2 req/sec) built in. Auth via webhook URL.

### Perfex CRM

**[Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm](https://github.com/Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm)** (18 stars, TypeScript, MIT) — 186 tools across 14 modules. Uses direct MySQL access for 10-100x faster queries than REST. Read-only by default. Enormous tool count, but Perfex is a niche platform.

### Method CRM

**[avisangle/method-crm-mcp](https://github.com/avisangle/method-crm-mcp)** — 20 tools for tables, files, users, events, and API key management. Rate limiting, retry logic, dual transport (stdio/HTTP). Also has a [Cloudflare Workers variant](https://github.com/avisangle/method-crm-mcp-workers) with 22 tools and OAuth 2.1 support.

---

## CRM platform comparison

| Feature | Salesforce | HubSpot | Pipedrive | Attio | Dynamics 365 | Monday.com | Close | Zoho |
|---------|-----------|---------|-----------|-------|--------------|-----------|-------|------|
| Official server | Yes (beta) | Yes (beta) | No | Yes (GA) | Yes (GA) | Yes (GA) | Yes (GA) | Yes (GA) |
| Top server stars | 342 | 118 (community) | 53 | 60 (community) | 38 (community) | 390 | — | — |
| Tool count (best) | 60+ | 9 (official) / 87+ (community) | 100+ | 20+ (official) / 35 (community) | 20 (official) | Board/Item ops | 57 | Platform (multi-app) |
| Read/Write | Both | Read-only (official) | Both | Both | Both | Both | Both (scoped) | Both |
| Hosted option | Yes (mcp-hosted) | Yes (mcp.hubspot.com) | No | Yes (mcp.attio.com) | Yes (Microsoft) | Yes (monday.com/w/mcp) | Yes (mcp.close.com) | Yes (mcp.zoho.com) |
| Auth model | SF CLI | OAuth 2.0 | API token | OAuth | Entra ID | OAuth / API token | OAuth 2.0 | OAuth |
| Active maintenance | High | High (official) | Low | High | High (official) | High | High | High |
| Ecosystem repos | 140+ | 20+ | 8+ | 2 | 5+ | 1 (but excellent) | 2 | Growing |
| Maturity | Strong | Growing fast | Early | Mature | Transformed | Strong | Strong | Early |
| Security issues | CVE on community server | None known | None known | None known | Azure MCP CVEs | None known | None known | None known |

---

## Which CRM server should you use?

**"I use Salesforce"** → **[salesforcecli/mcp](https://github.com/salesforcecli/mcp)** for official, comprehensive access with dynamic toolsets. If you need Python, **[smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce)** is the community standard. For enterprise hosted deployment, look at **[forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted)**.

**"I use HubSpot"** → Start with the **[official Remote MCP Server](https://developers.hubspot.com/mcp)** for safe, read-only CRM access. For semantic search and vector-based queries, add **[peakmojo/mcp-hubspot](https://github.com/peakmojo/mcp-hubspot)**. For write access and broader coverage (deals, tickets, pipelines), try **[adeel0x01/hubspot-mcp-tools](https://github.com/adeel0x01/hubspot-mcp-tools)** (87+ tools despite low star count).

**"I use Pipedrive"** → **[iamsamuelfraga/mcp-pipedrive](https://github.com/iamsamuelfraga/mcp-pipedrive)** for the broadest coverage (100+ tools). **[WillDent/pipedrive-mcp-server](https://github.com/WillDent/pipedrive-mcp-server)** if read-only is sufficient and you want higher community validation. **[Teapot-Agency/mcp_pipedrive](https://github.com/Teapot-Agency/mcp_pipedrive)** for a balanced 40-tool read/write middle ground.

**"I use Attio"** → Start with the **[official Attio MCP Server](https://docs.attio.com/mcp/overview)** for hosted, OAuth-based access. For power users who want deeper tool coverage and self-hosted control, **[kesslerio/attio-mcp-server](https://github.com/kesslerio/attio-mcp-server)** remains excellent.

**"I use Dynamics 365"** → **[D365 Sales MCP Server](https://learn.microsoft.com/en-us/dynamics365/sales/connect-to-model-context-protocol-sales)** for sales workflows (20 tools). **[D365 ERP MCP Server](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/mcp-server)** for Finance & Supply Chain Management. Both officially backed by Microsoft. The landscape has transformed since early 2026.

**"I use Monday.com"** → **[mondaycom/mcp](https://github.com/mondaycom/mcp)** — official, 390 stars, available on all plans. No need to look further.

**"I use Close"** → **[Close MCP Server](https://help.close.com/docs/mcp-server)** — official, hosted at mcp.close.com, 57 tools with granular permission scopes. Excellent.

**"I use Zoho"** → **[Zoho MCP Platform](https://www.zoho.com/mcp/)** for official, multi-app access. Still early but officially backed and actively expanding.

**"I use an open-source CRM"** → **[twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** for Twenty. **[mcp-perfex-crm](https://github.com/Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm)** for Perfex (186 tools, read-only by default).

**"I need customer success, not just sales"** → **[Gainsight MCP](https://www.gainsight.com)** for customer health scores, renewal tracking, and success plans.

---

## Four trends to watch

### 1. The official server wave crested — and it's bigger than expected

In late 2025, only Salesforce had an official MCP server. By April 2026: HubSpot, Zoho, Attio, Microsoft Dynamics 365 (Sales + ERP), Monday.com, Close, and Gainsight all have official MCP support. The holdouts (Pipedrive, Freshsales) are now the exception, not the rule. The pace exceeded our March predictions — Monday.com (390 stars) and Close (57 tools) both launched strong.

### 2. Granular permission scopes are emerging

Close's three-tier permission model (`mcp.read`, `mcp.write_safe`, `mcp.write_destructive`) and Attio's auto-approved reads with confirmation-based writes represent a maturing security pattern. This is more nuanced than the binary read-only/read-write split that dominated early CRM MCP servers. Expect more vendors to adopt tiered permission scopes.

### 3. Platform MCP vs. dedicated CRM MCP

Zoho's approach — a single MCP platform spanning CRM, email, calendar, helpdesk, and 500+ apps — represents a different model from Salesforce's dedicated CRM server. The platform approach enables cross-app workflows ("when a deal closes, send an email and create a project") but may sacrifice depth. Monday.com's approach is similar — their MCP server covers their entire work management platform, not just CRM.

### 4. CRM MCP security is lagging behind adoption

CVE-2026-26029 (command injection in a Salesforce community MCP server) and CVE-2026-32211 (critical Azure MCP auth flaw, CVSS 9.1) highlight that CRM MCP servers are not immune to the security issues plaguing the broader MCP ecosystem. CRM data is among the most sensitive data AI agents access — but security auditing of CRM MCP servers has not kept pace with their proliferation.

---

## What's missing

Despite 40+ servers, some gaps remain — though the list has shrunk dramatically since our last update:

- **No official Pipedrive MCP** — the third-largest sales CRM by market share still has no official MCP support. Community options are expanding (100+ tools from iamsamuelfraga), but official backing remains absent.
- **No Freshsales/Freshworks CRM MCP** — Freshworks has MCP servers for Freshservice and Freshdesk, but not for their CRM product. Available only through platform integrations (Zapier MCP, viaSocket MCP, CData MCP).
- **No multi-CRM server** — no server that unifies Salesforce + HubSpot + Pipedrive data into a single interface for companies running multiple CRMs.
- **HubSpot write access still unofficial** — the official HubSpot server remains read-only. Write operations require community servers with low adoption.

**Gaps closed since our last update:** Microsoft Dynamics 365 (now has official Sales + ERP servers), Monday.com (official, 390 stars), Close (official, 57 tools), Attio (now has official hosted server alongside community server).
- **No CRM migration tool** — no MCP server for moving data between CRM platforms
- **No sales engagement integration** — limited MCP coverage for tools like Outreach, Salesloft, or Apollo.io that sit alongside CRMs
- **No revenue intelligence** — no MCP servers for Gong, Chorus, or similar conversation intelligence platforms
- **HubSpot write gap** — the official server is read-only; write operations require community servers with low adoption

The CRM MCP ecosystem is bifurcated: Salesforce and Attio users are well-served with deep, actively-maintained servers. HubSpot and Zoho now have official backing but are still maturing. Everyone else is waiting for either official support or a community to form around their platform.

---

*Last updated: March 2026. Star counts and feature details may have changed since publication. See our full review for detailed analysis: [CRM MCP Servers](/reviews/crm-mcp-servers/)*
