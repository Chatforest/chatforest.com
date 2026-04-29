---
title: "ERP & Business Management MCP Servers — Odoo, Dynamics 365, NetSuite, SAP, Oracle, QuickBooks, and More"
date: 2026-03-16T09:00:00+09:00
description: "ERP and business management MCP servers let AI agents interact with enterprise resource planning systems through the Model Context Protocol."
og_description: "ERP MCP servers: SAP ECOSYSTEM EXPLODED 80+ servers 5 official (Fiori 139 stars, CAP 94 stars). QuickBooks OFFICIAL 184 stars 144 tools. tuanle96/mcp-odoo 298 stars 22 tools v0.2.0. ivnvxd/mcp-server-odoo DOUBLED 262 stars v0.5.1. D365 ERP MCP GA Feb 2026 dynamic framework. oracle/mcp 337 stars 28 implementations. Sage Intacct OFFICIAL. Workday OFFICIAL reference architecture. Infor 100+ tools. 120+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "ERP and business management MCP servers for AI-powered interaction with enterprise resource planning systems including Odoo, Microsoft Dynamics 365, Oracle NetSuite, SAP, Oracle Cloud, QuickBooks, Sage, Workday, and Infor. **SAP ECOSYSTEM EXPLODED from zero to 80+ servers** — SAP went from having zero community-built MCP servers to the largest ERP MCP ecosystem, with 5 official servers (SAP Fiori MCP 139 stars, @cap-js/mcp-server 94 stars Apache-2.0, UI5 MCP 79 stars, SAP MDK 30 stars, UI5 Web Components 17 stars) and 75+ community servers catalogued at marianfoo/sap-ai-mcp-servers (225 stars). Top community: oisee/vibing-steampunk (309 stars, ABAP ADT-to-MCP bridge), SAP Skills for Claude Code (236 stars), MCP SAP Docs (163 stars). Coverage spans ABAP/ADT development, OData integration, GUI automation, HANA database, BTP platform, and CPI/integration. **QuickBooks OFFICIAL is massive** — intuit/quickbooks-online-mcp-server (184 stars, TypeScript, MIT) provides 144 tools across 29 entity types and 11 financial reports with OAuth 2.0, 396 tests at 100% coverage. The most comprehensive single-server ERP MCP implementation. **Odoo community doubled** — ivnvxd/mcp-server-odoo SURGED 130→262 stars (+101%, v0.5.1, 719 tests, 90% coverage), tuanle96/mcp-odoo grew 269→298 stars with massive expansion to 22 tools (v0.2.0, Odoo 19 JSON-2 protocol, safe write workflow, Streamable HTTP). New entrants: pantalytics/odoo-mcp-pro (29 stars, hosted+self-hosted), marcfargas/odoo-toolbox (30 stars, TypeScript SDK+CLI), rosenvladimirov/odoo-claude-mcp (12 stars, 197+ tools multi-tenant). **Microsoft D365 ERP MCP reached GA** — the dynamic framework went GA February 2026, evolving from 13 static tools to hundreds of thousands of functions. Three tool categories: Data tools (CRUD), Form tools (navigate like a human), Analytics tools. Automatically exposes ISV extensions. NEW Dataverse-skills (81 stars, 8 specialist skills wrapping Dataverse MCP). NEW dynamics365ninja/d365fo-mcp-server (58 stars, 54 tools, X++ development). SShadowS/business-central-mcp grew to 30 stars with 213 commits and 11 tools. **Oracle NetSuite got major upgrades** — AI Connector Service Companion with 100+ finance-specific prompts and pre-configured roles (CFO, Controller, AR/AP/Treasury Analyst). SuiteCloud Agent Skills launched at SuiteConnect SF (April 2026), first ERP platform to leverage agentskills.io open standard. oracle/mcp GREW to 337 stars with 28 server implementations covering database, OCI compute/networking/identity/monitoring/IoT/pricing/migration and more. **Sage Intacct OFFICIAL** — first-party MCP server v1.0 on Sage Developer Portal, part of 2026 R1 release. **Workday GAP FILLED** — workday/ai-conversation-bridge (4 stars, official reference architecture with 11 demo MCP tools, March 2026). **Infor EXPANDED** — npm @douglaslinsmeyer/infor-mcp-server at v1.11.1 with 100+ persona-based tools and Safe Mode. **IFS Cloud appeared** — first MCP integrations for IFS Cloud ERP. Every major ERP vendor now has MCP coverage — the category crossed from 'uneven vendor coverage' to 'universal enterprise adoption.'"
last_refreshed: 2026-04-29
---

ERP and business management MCP servers let AI assistants interact with enterprise resource planning systems through the Model Context Protocol. Instead of navigating complex ERP interfaces or writing API integrations manually, AI agents can query business data, create records, manage inventory, and automate workflows conversationally. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

This review covers the **ERP ecosystem** — Odoo, Microsoft Dynamics 365, Oracle NetSuite, SAP, Oracle Cloud, QuickBooks, Sage, Workday, Infor, and multi-ERP connectors. For related servers, see our [Accounting & Bookkeeping review](/reviews/accounting-bookkeeping-mcp-servers/), [Supply Chain & Logistics review](/reviews/supply-chain-logistics-mcp-servers/), and [CRM review](/reviews/crm-mcp-servers/).

The headline findings: **SAP went from zero to 80+ MCP servers** including 5 official — the biggest transformation in any ERP category. **QuickBooks shipped 144 tools** in a single official server. **Every major ERP vendor now has MCP coverage** — the gaps from March are filled.

## SAP — From Zero to 80+ Servers

### SAP Official MCP Servers

SAP went from having zero MCP servers to shipping **5 official open-source servers**:

| Server | Stars | Language | License | Description |
|--------|-------|----------|---------|-------------|
| [SAP Fiori MCP](https://github.com/SAP/open-ux-tools) | 139 | TypeScript | Apache-2.0 | Fiori app generation and modification |
| [@cap-js/mcp-server](https://github.com/cap-js/mcp-server) | 94 | JavaScript | Apache-2.0 | CAP development with semantic doc search |
| SAP UI5 MCP | 79 | TypeScript | — | UI5 development tooling |
| [SAP MDK MCP](https://github.com/SAP/mdk-mcp-server) | 30 | TypeScript | — | Mobile Development Kit "vibe coding" |
| SAP UI5 Web Components MCP | 17 | TypeScript | — | Web component development |

The @cap-js/mcp-server (v0.0.5, April 27, 2026) provides two powerful tools: `search_model` for fuzzy search against compiled CDS model definitions, and `search_docs` for semantic vector search through CAP documentation.

### SAP Community Ecosystem

The community catalog at [marianfoo/sap-ai-mcp-servers](https://github.com/marianfoo/sap-ai-mcp-servers) (225 stars, 42 forks) lists **80+ SAP MCP servers** across every SAP product:

**Top community servers:**

| Server | Stars | Category |
|--------|-------|----------|
| [oisee/vibing-steampunk](https://github.com/oisee/vibing-steampunk) | 309 | ABAP ADT-to-MCP bridge |
| SAP Skills for Claude Code | 236 | CAP, Fiori, ABAP, BTP |
| MCP SAP Docs | 163 | Unified documentation search |
| OData MCP Bridge | 127 | Go-based OData integration |
| mcp-abap-adt-api | 127 | ABAP Development Tools API |
| SAP OData to MCP (BTP) | 124 | BTP platform integration |
| mcp-abap-adt | 120 | ABAP development |
| mcp-sap-gui | 103 | GUI automation |
| ABAP MCP Server SDK | 67 | Build custom ABAP MCP servers |
| HANA MCP Server | 50 | SAP HANA database access |
| SAP Notes MCP Server | 48 | Search SAP Notes and KB articles |

Categories span: ABAP/ADT development, OData integration, GUI automation, documentation/knowledge, database (HANA/Datasphere), BTP platform, CPI/integration, and mobile development.

### CData SAP MCP Servers — Read-Only JDBC Connectors

CData Software continues to provide **read-only MCP servers** for SAP ERP, SAP HANA, SAP Business One, SAP ByDesign, SAP Concur, and SAP Hybris C4C via JDBC drivers. Full CRUD requires CData Connect AI (commercial). These are now supplementary rather than the only option.

## Intuit QuickBooks — Official 144-Tool Server

### intuit/quickbooks-online-mcp-server — Most Comprehensive Single-Server ERP MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server) | 184 | TypeScript | MIT | 144 |

**The most feature-dense ERP MCP server in any category** — official Intuit server providing complete QuickBooks Online integration:

- **144 tools** across 29 entity types — Customers, Invoices, Bills, Vendors, Employees, Accounts, Items, Payments, and more
- **11 financial reports** — Balance Sheet, P&L, Cash Flow, Trial Balance, and others
- **OAuth 2.0 authentication** — proper token management with sandbox and production support
- **100% test coverage** — 396 tests with Jest, TypeScript with Zod validation
- **Full CRUD operations** — not just read-only, complete create/update/delete across all entities

This is the single most comprehensive ERP MCP implementation by tool count, surpassing even Microsoft's D365 community servers.

## Odoo

### tuanle96/mcp-odoo — Massively Expanded to 22 Tools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-odoo](https://github.com/tuanle96/mcp-odoo) | 298 | Python | — | 22 |

**Transformed from a basic XML-RPC bridge to a 22-tool production server** (v0.2.0, April 28, 2026):

- **Odoo 19 JSON-2 protocol support** — modernized beyond XML-RPC
- **Safe write workflow** — preview/validate/approve/execute gates for data safety
- **ACL and record-rule diagnosis** — debug access control issues
- **Addon scanning and linting** — analyze installed modules
- **5 workflow prompts** — diagnose_failed_odoo_call, fit_gap_workshop, json2_migration_plan, safe_write_review, custom_module_audit
- **Streamable HTTP transport** — modern MCP transport support
- **Docker Compose testing** — CI against Odoo 16-19, PyPI published

The jump from ~6 tools (v0.0.1, March 18) to 22 tools (v0.2.0, April 28) in six weeks shows rapid maturation.

### ivnvxd/mcp-server-odoo — Doubled to 262 Stars

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo) | 262 | Python | MIT | 10+ |

**Stars doubled 130→262 (+101%)** — the fastest-growing Odoo MCP server:

- **v0.5.1** (April 23, 2026) — fixed search limit capping and ODOO_MCP_DEFAULT_LIMIT env var handling
- **v0.5.0** (February 28) — FastMCP lifespan hooks, Context injection with logging/progress, `/health` HTTP endpoint, model name autocomplete
- **719 tests, 90% coverage** — integration tests accelerated 4.4x
- **YOLO mode** — quick testing without Odoo module installation
- **Enterprise module** — optional production access controls

### New Odoo MCP Servers

| Server | Stars | Description |
|--------|-------|-------------|
| [marcfargas/odoo-toolbox](https://github.com/marcfargas/odoo-toolbox) | 30 | TypeScript SDK + CLI + MCP, 10 command groups, CI-tested Odoo v17-v18 |
| [pantalytics/odoo-mcp-pro](https://github.com/pantalytics/odoo-mcp-pro) | 29 | Hosted + self-hosted, Odoo 14-19+, 10 tools, v1.5.0 |
| [rosenvladimirov/odoo-claude-mcp](https://github.com/rosenvladimirov/odoo-claude-mcp) | 12 | 197+ tools (92 native + 105 proxied), multi-tenant, Qdrant vector store |
| [mart337i/odoo-dev-mcp](https://github.com/mart337i/odoo-dev-mcp) | 12 | Module development focus, 302+ searchable doc pages |
| [hachecito/odoo-mcp-improved](https://github.com/hachecito/odoo-mcp-improved) | 44 | Extended fork, dormant since Jan 2025 |

## Microsoft Dynamics 365

### Official Dynamics 365 ERP MCP Server — GA February 2026

**The dynamic framework reached GA in February 2026**, evolving from 13 static tools to unlocking hundreds of thousands of ERP functions:

- **Three tool categories** — Data tools (CRUD operations), Form tools (navigate server forms like a human), Analytics tools
- **Dynamic framework** — automatically exposes ISV extensions and customizations
- **Full UI parity** — agents can perform nearly any function available through the application interface
- **ERP Analytics MCP** — separate server for Business Performance Analytics (still in preview)
- **Business Central** — troubleshooting MCP server for AL runtime issues in debugging sessions (2026 Wave 1)

### microsoft/Dataverse-skills — NEW AI Agent Skills

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Dataverse-skills](https://github.com/microsoft/Dataverse-skills) | 81 | — | MIT | 8 skills |

**Created March 11, 2026** — wraps the Dataverse MCP server, Dataverse CLI, Python SDK, and PAC CLI behind 8 specialist skills for AI coding agents. Actively maintained (updated April 28, 2026).

### Dataverse MCP Server — Generally Available

**Already GA** — the Dataverse MCP Server provides natural language access to Microsoft's low-code data platform with built-in tools for CRUD, search, and prompt execution. Works with Copilot Studio and GitHub Copilot in VS Code. The microsoft/Dataverse-MCP companion repo (56 stars) provides labs and tutorials.

### dynamics365ninja/d365fo-mcp-server — NEW F&O Development

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [d365fo-mcp-server](https://github.com/dynamics365ninja/d365fo-mcp-server) | 58 | TypeScript | — | 54 |

**54 tools for X++ development** with IntelliSense-like navigation, EDT suggestions, and AI-driven table/form generation. 1,123 commits, very actively maintained since January 2026.

### Community Business Central Servers

| Server | Stars | Commits | Description |
|--------|-------|---------|-------------|
| [SShadowS/business-central-mcp](https://github.com/SShadowS/business-central-mcp) | 30 | 213 | Reverse-engineered WebSocket, 11 tools, 128 unit + 103 integration tests |
| [mafzaal/d365fo-client](https://github.com/mafzaal/d365fo-client) | 29 | 537 | Python, 49 tools across 9 categories, v0.3.0 |
| [knowall-ai/mcp-business-central](https://github.com/knowall-ai/mcp-business-central) | 9 | 24 | API v2.0 access, 6 tools |
| [demiliani/D365BCAdminMCP](https://github.com/demiliani/D365BCAdminMCP) | 8 | 11 | 34 admin tools, VS Code extension |
| [MS-Cloud-Experts/mcp-business-central](https://github.com/MS-Cloud-Experts/mcp-business-central) | — | — | NEW April 2026, 115 tools covering 93 BC entities |

## Oracle NetSuite

### NetSuite Native AI Connector — Major 2026 Upgrades

**Oracle's official MCP integration received significant enhancements** in 2026:

- **AI Connector Service Companion** (March 2026) — 100+ finance-specific prompt templates organized by business process and role, Companion Skills injecting NetSuite domain knowledge, pre-configured roles (CFO, Controller, AR/AP/Treasury Analyst) mapping AI capabilities to NetSuite permissions
- **SuiteCloud Agent Skills** (April 28, 2026 at SuiteConnect SF) — first ERP platform to leverage the agentskills.io open standard, with skills for UI Framework References, Permissions References, OWASP Security, and SuiteScript Conversion across 25+ AI coding platforms
- **MCP Apps** — bring native NetSuite UI elements (filters, forms, selectors) into AI assistant interfaces for hybrid text+GUI interaction
- **NetSuite 2026.1** — added LLM Connector for Data Warehouse and iPaaS solutions

### dsvantien/netsuite-mcp-server — SuiteInsider Community MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [netsuite-mcp-server](https://github.com/dsvantien/netsuite-mcp-server) | 11 | JavaScript | — | 5+ |

Grew from 6 to 11 stars. Still listed on the official MCP servers repository. OAuth 2.0 with PKCE authentication, SuiteQL queries, npm distribution as `@suiteinsider/netsuite-mcp`. Development paused (last commit October 2024).

## Oracle Cloud

### oracle/mcp — Expanded to 337 Stars and 28 Implementations

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [oracle/mcp](https://github.com/oracle/mcp) | 337 | Multi-language | — | 28 servers |

**Significantly expanded** with 28 MCP server implementations under `/src/` covering:

- **Database** — Oracle DB tools, MySQL, GoldenGate, Java toolkit
- **OCI services** — Compute, Networking, Identity, Monitoring, IoT, Pricing, Migration, Logging, Load Balancer, Object Storage, and more
- **Documentation** — oracle-db-doc-mcp-server
- **428 total commits**, 101 forks — very active official development

The shjanjua/OCI-MCP-Servers (2 stars) is effectively superseded by oracle/mcp's broader coverage.

## Sage Intacct — Official MCP Server

**Sage published an official MCP server for Sage Intacct** as part of the 2026 R1 release, available on the Sage Developer Portal. This fills a significant gap — Sage was previously listed as having zero MCP coverage.

## Workday — Official Reference Architecture

### workday/ai-conversation-bridge — First Official Workday MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ai-conversation-bridge](https://github.com/workday/ai-conversation-bridge) | 4 | — | — | 11 demo tools |

**Created March 2026** — official Workday reference architecture connecting enterprise messaging apps (LINE WORKS, WeChat, Feishu) to Workday via MCP. Includes 11 demo tools with documentation pointing to "Workday's official MCP endpoints via Agent Gateway" for production use. Previously the biggest gap (top-5 cloud ERP vendor with zero MCP coverage).

Community: KaranThink41/workday_mcp_server provides 3 tools (employees, absence types, time-off requests).

## Infor — Expanded to 100+ Tools

The Infor MCP server (`@douglaslinsmeyer/infor-mcp-server`) has reached **v1.11.1** with 100+ persona-based tools covering Finance, Supply Chain, Sales, Production, and Executive users. Includes a **Safe Mode** to prevent accidental write operations. Active development continues via npm.

## IFS Cloud — First MCP Integrations

Two community servers have appeared for IFS Cloud ERP:

- **keerthiprasad10/ifs-cloud-mcp** — work order management via OData REST API with OAuth 2.0
- **knakit/ifs-mcp-server-local** — skill-based (no coding) using OpenAPI specs

These represent the first MCP integrations for this enterprise ERP vendor.

## Multi-ERP Connectors

### CData Connect AI — Universal ERP Gateway

**Commercial platform** providing MCP access to 200+ enterprise data sources through a unified interface. Read-only free tier; full CRUD requires CData Connect AI (commercial). No longer the only option for SAP, but remains the best cross-ERP solution.

## What's Missing

- **No Epicor MCP** — Epicor Kinetic, a Leader in Gartner's Manufacturing ERP quadrant, still has no MCP support
- **Workday still early** — official reference architecture but demo-stage tools, not production-ready
- **SAP community fragmentation** — 80+ servers means choice overload, no clear "best" server for each use case
- **No cross-ERP unified interface** — no single MCP server provides a consistent interface across multiple ERP systems
- **Limited NetSuite community** — despite Oracle's official upgrades, community development is paused
- **No ERP-to-ERP data migration MCP** — no server assists with data migration between ERP systems

## The Bottom Line

**Rating: 4/5** — The ERP MCP landscape has been **completely transformed** in 44 days. SAP went from the biggest gap (zero servers) to the largest ecosystem (80+ servers, 5 official). QuickBooks shipped 144 tools in one server. Every major ERP vendor — SAP, Microsoft, Oracle/NetSuite, Intuit, Sage, Workday, Infor — now has MCP coverage.

The standout newcomers: SAP's oisee/vibing-steampunk (309 stars) for ABAP development, Intuit's QuickBooks MCP (184 stars, 144 tools) for the most comprehensive single-server implementation, and Microsoft's D365 ERP MCP reaching GA with a dynamic framework exposing hundreds of thousands of functions.

For developers: QuickBooks has the most complete and accessible MCP tooling (144 tools, MIT, 100% test coverage). For SAP shops: you now have 80+ choices — start with the official @cap-js/mcp-server or the community catalog at marianfoo/sap-ai-mcp-servers. For enterprises: Microsoft's D365 ERP MCP is GA with the most ambitious architecture, and Oracle NetSuite's AI Connector Service Companion adds 100+ finance-specific prompts.

*This review was refreshed on 2026-04-29 using Claude Opus 4.6 (Anthropic). Originally published 2026-03-16.*
