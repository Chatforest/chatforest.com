---
title: "Best CRM MCP Servers in 2026"
date: 2026-03-22T22:00:00+09:00
description: "Salesforce, HubSpot, Pipedrive, Attio, Dynamics 365, Zoho, and more — we've reviewed 30+ CRM MCP servers across 8 platforms. Here's what works, what's emerging, and where the gaps are."
og_description: "30+ CRM MCP servers reviewed across Salesforce, HubSpot, Pipedrive, Attio, Dynamics 365, Zoho, and open-source CRMs. The definitive comparison with honest ratings."
content_type: "Comparison"
card_description: "The definitive guide to CRM MCP servers in 2026. We've reviewed 30+ servers across Salesforce (official + community), HubSpot (official + community), Pipedrive, Attio, Dynamics 365, Zoho, and open-source CRMs like Twenty. Every recommendation links to a full review."
---

CRM data is some of the most valuable information a business owns — contacts, deals, pipeline stages, revenue forecasts, customer histories. Giving an AI agent access to that data changes how sales teams, customer success managers, and operations work. Instead of clicking through dashboards, you ask.

We've researched 30+ CRM MCP servers across the full landscape. This guide synthesizes all of that into one page: what's worth using, what's not, and where the gaps are.

*Note: Our recommendations are based on documentation review, GitHub analysis, and community feedback — not hands-on testing of every server. Star counts were verified in March 2026.*

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| Salesforce (official) | [salesforcecli/mcp](https://github.com/salesforcecli/mcp) | 312 | [forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted) (31 stars, hosted) |
| Salesforce (community) | [smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce) | 166 | [tsmztech/mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce) (139 stars) |
| HubSpot (official) | [HubSpot Remote MCP](https://developers.hubspot.com/mcp) | Official | [HubSpot Developer MCP](https://developers.hubspot.com/docs/developer-tooling/local-development/mcp-server) (GA, app/CMS dev) |
| HubSpot (community) | [peakmojo/mcp-hubspot](https://github.com/peakmojo/mcp-hubspot) | 116 | [adeel0x01/hubspot-mcp-tools](https://github.com/adeel0x01/hubspot-mcp-tools) (58 tools) |
| Pipedrive | [Teapot-Agency/mcp_pipedrive](https://github.com/Teapot-Agency/mcp_pipedrive) | 5 | [WillDent/pipedrive-mcp-server](https://github.com/WillDent/pipedrive-mcp-server) (46 stars, read-only) |
| Attio | [kesslerio/attio-mcp-server](https://github.com/kesslerio/attio-mcp-server) | 58 | — |
| Zoho | [Zoho MCP Platform](https://www.zoho.com/mcp/) | Official | [CData Zoho CRM MCP](https://github.com/CDataSoftware/zoho-crm-mcp-server-by-cdata) (read-only) |
| Open-source CRM | [mhenry3164/twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server) | 42 | [Descomplicar/mcp-perfex-crm](https://github.com/Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm) (186 tools) |

## Why CRM MCP servers matter

CRM operations involve constant context-switching between apps, dashboards, and spreadsheets. MCP servers turn these into natural-language commands.

The value comes in three forms:

1. **Pipeline management automation.** "Show me all deals closing this month with value over $50K" or "Update the deal stage for Acme Corp to Negotiation" — instead of navigating multiple screens and filters. At scale, agents can process bulk operations across hundreds of records.
2. **Data enrichment and hygiene.** Agents can find duplicate contacts, fill missing fields from web research, and maintain data quality across your entire CRM — tasks that would take hours manually.
3. **Cross-platform insights.** Ask "Which sales rep has the highest win rate this quarter?" or "What's our average deal cycle time?" and get answers pulled directly from your CRM's live data.

The landscape splits into eight categories: **Salesforce** (official + deep community ecosystem), **HubSpot** (newly official + community), **Pipedrive** (community-driven), **Attio** (unexpectedly excellent), **Dynamics 365** (minimal), **Zoho** (newly official platform), **open-source CRMs** (Twenty, Perfex), and **niche platforms** (Clay, Bitrix24, Method CRM).

---

## Salesforce servers

Salesforce dominates the CRM MCP space with 140+ repositories on GitHub, an officially-maintained server with 60+ tools, and a hosted deployment option for enterprise use.

### The winner: salesforcecli/mcp (Official)

**Stars:** 312 | **Language:** TypeScript | **License:** Apache 2.0 | **Status:** Beta

[salesforcecli/mcp](https://github.com/salesforcecli/mcp) is officially maintained by Salesforce as part of their CLI toolchain. It's by far the most comprehensive CRM MCP server in any ecosystem.

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

**Stars:** 31 | **License:** Apache 2.0 | **Status:** Open Beta

[forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted) is the enterprise deployment model. Salesforce runs the MCP server — your agent connects remotely via External Client Apps. Admin-governed endpoints with enterprise-grade auth. This is how Salesforce envisions large organizations deploying MCP access.

**Best for:** Enterprise teams that need centrally-managed, admin-governed MCP access to Salesforce.

### Community Salesforce servers

**[smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce)** (166 stars, Python, MIT) — The leading community alternative. SOQL queries, SOSL search, record CRUD, metadata retrieval, Tooling API, and direct REST API calls. Three auth modes (OAuth, CLI, username/password). Best Python-based Salesforce MCP server.

**[tsmztech/mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce)** (139 stars, TypeScript) — Strong feature set including aggregate queries, field-level security management, anonymous Apex execution, debug logging, and multi-org support. Ships as a Claude Desktop extension (`.dxt`). One of the few servers that handles field-level security explicitly.

**[advancedcommunities/salesforce-mcp-server](https://github.com/advancedcommunities/salesforce-mcp-server)** (23 stars, TypeScript, MIT) — 40 tools with a standout safety feature: **read-only mode** and **org restriction** to prevent accidental changes to production orgs.

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

**[peakmojo/mcp-hubspot](https://github.com/peakmojo/mcp-hubspot)** (116 stars, Python, MIT) — The most popular community HubSpot MCP server, and it offers something no official server does: **FAISS semantic search** across contacts and companies. Builds a local vector index of your HubSpot data for "find companies similar to X" queries. 7 tools covering contacts, companies, and engagement history with built-in duplicate prevention. Docker, Smithery, or local install.

**[adeel0x01/hubspot-mcp-tools](https://github.com/adeel0x01/hubspot-mcp-tools)** (4 stars, TypeScript, MIT) — 58 tools across 9 categories including deals, tickets, pipelines, and custom objects. Much broader coverage than peakmojo, but very low adoption. If you need HubSpot write access and deal/ticket management, this is currently the only option.

**[scopiousdigital/hubspot-mcp](https://github.com/scopiousdigital/hubspot-mcp)** (10 stars, JavaScript, MIT) — 6+ tools with Private App auth (14 scopes). Lighter-weight alternative.

---

## Pipedrive servers

Pipedrive's MCP ecosystem is community-driven with no official server. The landscape has improved — write-capable options now exist alongside the popular read-only server.

### The winner: Teapot-Agency/mcp_pipedrive

**Stars:** 5 | **Language:** TypeScript | **License:** MIT | **Tools:** 40

[Teapot-Agency/mcp_pipedrive](https://github.com/Teapot-Agency/mcp_pipedrive) wins despite low adoption because it's the only mature Pipedrive server with full CRUD. 20 read operations and 20 write operations covering deals, persons, organizations, activities, notes, and leads. Fuzzy person search and soft delete recovery.

**Why it wins:** If you need to actually update deals, add notes, or create leads through an AI agent, this is the only production-ready option. The read-only servers force you back into the Pipedrive UI for any changes.

**The catch:** 5 stars — very low adoption. Less community validation than WillDent's read-only server.

**Best for:** Pipedrive users who need full read/write CRM automation.

### Also notable: WillDent/pipedrive-mcp-server

**Stars:** 46 | **Language:** TypeScript | **License:** MIT | **Tools:** 16

[WillDent/pipedrive-mcp-server](https://github.com/WillDent/pipedrive-mcp-server) is the most popular Pipedrive server by adoption. 16 tools and 8 predefined prompts for deals, persons, organizations, and pipelines. **Read-only** — no creating or modifying records. If you only need to query your pipeline and pull reports, this is the safer, more validated choice.

---

## Attio — Punching above its weight

### The winner: kesslerio/attio-mcp-server

**Stars:** 58 | **Language:** TypeScript | **License:** Apache 2.0 | **Commits:** 1,291+

[kesslerio/attio-mcp-server](https://github.com/kesslerio/attio-mcp-server) is the most actively maintained CRM MCP server by commit count. For a CRM with a fraction of Salesforce's market share, the MCP server quality is disproportionately high.

**Why it wins:** Architectural excellence. The server consolidates 70+ resource-specific operations into 35 tools (21 universal + 11 list + 3 workspace member) through parameter-based routing — a 68% tool reduction while maintaining complete CRM surface coverage. This is the design pattern every CRM MCP server should study.

**Key features:**
- **Complete CRUD** for Companies, People, Deals, Tasks, Lists, and Notes
- **Advanced AND/OR filtering** and batch operations
- **Content search** across all objects
- **10 MCP prompts** and **3 Claude Skills**
- **OAuth support** for Cloudflare Workers deployment
- **Safety annotations** for OpenAI compatibility
- **Custom object display names** fetched from Attio API
- **Levenshtein distance suggestions** for attribute name typos

**The catch:** Attio-only. If you're not on Attio, this doesn't help. But if you are — no caveats. This is a genuinely excellent MCP integration.

**Best for:** Attio users. Period. This is first-class integration.

---

## Dynamics 365 — Minimal coverage

### The landscape

[srikanth-paladugula/mcp-dynamics365-server](https://github.com/srikanth-paladugula/mcp-dynamics365-server) (17 stars, TypeScript, MIT) remains the only Dynamics 365 MCP server. Just 5 tools: get user info, fetch accounts, get opportunities, create account, update account. Azure AD auth (client ID/secret/tenant).

For a platform of Dynamics 365's scale and enterprise adoption, this is a glaring gap. Microsoft has invested heavily in MCP for GitHub Copilot and other developer tools, but Dynamics 365 CRM has been left behind. No official server, no community momentum.

**Best for:** Teams that only need basic account/opportunity access. Everyone else should wait — or build their own.

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

**[mhenry3164/twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** (42 stars, JavaScript, MIT) — For [Twenty](https://twenty.com), the open-source CRM. Dynamic schema discovery, advanced search, full CRUD across people, companies, tasks, and notes. If you've chosen Twenty as your CRM, this is a solid integration with active maintenance.

### Clay

**[clay-inc/clay-mcp](https://github.com/clay-inc/clay-mcp)** (29 stars) — First-party from Clay (the contact enrichment and outbound platform). Contact search, interaction retrieval, analytics, calendar integration. Guided login flow for auth.

### Bitrix24

**[gunnit/bitrix24-mcp-server](https://github.com/gunnit/bitrix24-mcp-server)** (24 stars, TypeScript, MIT) — Contact, deal, task, and lead management for Bitrix24. Rate limiting (2 req/sec) built in. Auth via webhook URL.

### Perfex CRM

**[Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm](https://github.com/Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm)** (16 stars, TypeScript, MIT) — 186 tools across 14 modules. Uses direct MySQL access for 10-100x faster queries than REST. Read-only by default. Enormous tool count, but Perfex is a niche platform.

### Method CRM

**[avisangle/method-crm-mcp](https://github.com/avisangle/method-crm-mcp)** — 20 tools for tables, files, users, events, and API key management. Rate limiting, retry logic, dual transport (stdio/HTTP). Also has a [Cloudflare Workers variant](https://github.com/avisangle/method-crm-mcp-workers) with 22 tools and OAuth 2.1 support.

---

## CRM platform comparison

| Feature | Salesforce | HubSpot | Pipedrive | Attio | Dynamics 365 | Zoho |
|---------|-----------|---------|-----------|-------|--------------|------|
| Official server | Yes (beta) | Yes (beta) | No | No | No | Yes (GA) |
| Top server stars | 312 | 116 (community) | 46 | 58 | 17 | — |
| Tool count (best) | 60+ | 9 (official) / 58 (community) | 40 | 35 | 5 | Platform (multi-app) |
| Read/Write | Both | Read-only (official) | Both (Teapot) | Both | Both | Both |
| Hosted option | Yes (mcp-hosted) | Yes (mcp.hubspot.com) | No | Cloudflare Workers | No | Yes (mcp.zoho.com) |
| Auth model | SF CLI | OAuth 2.0 | API token | API key | Azure AD | OAuth |
| Active maintenance | High | High (official) | Low | Very high | Low | High |
| Ecosystem repos | 140+ | 20+ | 5+ | 1 (but excellent) | 1 | Growing |
| Maturity | Strong | Growing fast | Early | Surprisingly mature | Minimal | Early |

---

## Which CRM server should you use?

**"I use Salesforce"** → **[salesforcecli/mcp](https://github.com/salesforcecli/mcp)** for official, comprehensive access with dynamic toolsets. If you need Python, **[smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce)** is the community standard. For enterprise hosted deployment, look at **[forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted)**.

**"I use HubSpot"** → Start with the **[official Remote MCP Server](https://developers.hubspot.com/mcp)** for safe, read-only CRM access. For semantic search and vector-based queries, add **[peakmojo/mcp-hubspot](https://github.com/peakmojo/mcp-hubspot)**. For write access and broader coverage (deals, tickets, pipelines), try **[adeel0x01/hubspot-mcp-tools](https://github.com/adeel0x01/hubspot-mcp-tools)** despite its low star count.

**"I use Pipedrive"** → **[Teapot-Agency/mcp_pipedrive](https://github.com/Teapot-Agency/mcp_pipedrive)** if you need write access. **[WillDent/pipedrive-mcp-server](https://github.com/WillDent/pipedrive-mcp-server)** if read-only is sufficient and you want higher community validation.

**"I use Attio"** → **[kesslerio/attio-mcp-server](https://github.com/kesslerio/attio-mcp-server)**. No caveats. One of the best CRM MCP servers in the entire ecosystem.

**"I use Zoho"** → **[Zoho MCP Platform](https://www.zoho.com/mcp/)** for official, multi-app access. Still early but officially backed and actively expanding.

**"I use Dynamics 365"** → Wait. The single available server has only 5 tools. Microsoft has not prioritized Dynamics 365 MCP support.

**"I use an open-source CRM"** → **[twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** for Twenty. **[mcp-perfex-crm](https://github.com/Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm)** for Perfex (186 tools, read-only by default).

---

## Three trends to watch

### 1. Official CRM MCP servers are arriving fast

In late 2025, only Salesforce had an official MCP server. By Q1 2026, HubSpot launched both a Remote CRM server and a Developer server, and Zoho shipped an entire MCP platform covering their full product suite. The pattern is clear: major CRM vendors are racing to provide official MCP access. Expect Pipedrive, Monday CRM, and possibly Microsoft Dynamics to follow within 2026.

### 2. Read-only first, write later

Both HubSpot's official server and most community CRM servers default to read-only access. This makes sense — CRM data is business-critical, and an AI agent accidentally deleting contacts or corrupting deal stages is a real risk. The safest path is read-only access for reporting and analysis first, then carefully enabling write operations with guardrails (org restriction, confirmation prompts, audit logging).

### 3. Platform MCP vs. dedicated CRM MCP

Zoho's approach — a single MCP platform spanning CRM, email, calendar, helpdesk, and 500+ apps — represents a different model from Salesforce's dedicated CRM server. The platform approach enables cross-app workflows ("when a deal closes, send an email and create a project") but may sacrifice depth. Watch whether Salesforce follows with a unified MCP platform or doubles down on dedicated, deep servers.

---

## What's missing

Despite 30+ servers, significant gaps remain:

- **No official Pipedrive MCP** — the third-largest sales CRM by market share has no official MCP support
- **No official Dynamics 365 MCP** — Microsoft has invested in MCP for GitHub and developer tools but not for its own CRM platform
- **No Freshsales/Freshworks CRM MCP** — Freshworks has MCP servers for Freshservice and Freshdesk, but not for their CRM product
- **No Monday CRM MCP** — Monday.com's CRM product has no dedicated MCP server
- **No Close.com MCP** — popular among SMB sales teams, no MCP integration
- **No multi-CRM server** — no server that unifies Salesforce + HubSpot + Pipedrive data into a single interface for companies running multiple CRMs
- **No CRM migration tool** — no MCP server for moving data between CRM platforms
- **No sales engagement integration** — limited MCP coverage for tools like Outreach, Salesloft, or Apollo.io that sit alongside CRMs
- **No revenue intelligence** — no MCP servers for Gong, Chorus, or similar conversation intelligence platforms
- **HubSpot write gap** — the official server is read-only; write operations require community servers with low adoption

The CRM MCP ecosystem is bifurcated: Salesforce and Attio users are well-served with deep, actively-maintained servers. HubSpot and Zoho now have official backing but are still maturing. Everyone else is waiting for either official support or a community to form around their platform.

---

*Last updated: March 2026. Star counts and feature details may have changed since publication. See our full review for detailed analysis: [CRM MCP Servers](/reviews/crm-mcp-servers/)*
