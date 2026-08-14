# ERP & Business Management MCP Servers — Odoo, Dynamics 365, NetSuite, SAP, Oracle, QuickBooks, and More

> ERP and business management MCP servers let AI agents interact with enterprise resource planning systems through the Model Context Protocol.


ERP and business management MCP servers let AI assistants interact with enterprise resource planning systems through the Model Context Protocol. Instead of navigating complex ERP interfaces or writing API integrations manually, AI agents can query business data, create records, manage inventory, and automate workflows conversationally. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

This review covers the **ERP ecosystem** — Odoo, Microsoft Dynamics 365, Oracle NetSuite, SAP, Oracle Cloud, QuickBooks, Sage, Workday, Infor, and multi-ERP connectors. For related servers, see our [Accounting & Bookkeeping review](/reviews/accounting-bookkeeping-mcp-servers/), [Supply Chain & Logistics review](/reviews/supply-chain-logistics-mcp-servers/), and [CRM review](/reviews/crm-mcp-servers/).

The headline findings: **SAP went from zero to 80+ MCP servers** including 5 official — the biggest transformation in any ERP category. **QuickBooks shipped 145 tools** in a single official server. **Every major ERP vendor now has MCP coverage** — the gaps from March are filled.

## SAP — From Zero to 80+ Servers

### SAP Official MCP Servers

SAP went from having zero MCP servers to shipping **5 official open-source servers**:

| Server | Stars | Language | License | Description |
|--------|-------|----------|---------|-------------|
| [SAP Fiori MCP](https://github.com/SAP/open-ux-tools) | 155 | TypeScript | Apache-2.0 | Fiori app generation and modification |
| [@cap-js/mcp-server](https://github.com/cap-js/mcp-server) | 109 | JavaScript | Apache-2.0 | CAP development with semantic doc search |
| [SAP UI5 MCP](https://github.com/UI5/mcp-server) | 97 | TypeScript | Apache-2.0 | UI5 development tooling |
| [SAP MDK MCP](https://github.com/SAP/mdk-mcp-server) | 34 | TypeScript | — | Mobile Development Kit "vibe coding" |
| [SAP UI5 Web Components MCP](https://github.com/UI5/webcomponents-mcp-server) | 19 | TypeScript | Apache-2.0 | Web component development |

The @cap-js/mcp-server (v0.0.5, April 27, 2026) provides two powerful tools: `search_model` for fuzzy search against compiled CDS model definitions, and `search_docs` for semantic vector search through CAP documentation.

### SAP Community Ecosystem

The community catalog at [marianfoo/sap-ai-mcp-servers](https://github.com/marianfoo/sap-ai-mcp-servers) (428 stars, 81 forks) lists **80+ SAP MCP servers** across every SAP product:

**Top community servers:**

| Server | Stars | Category |
|--------|-------|----------|
| [oisee/vibing-steampunk](https://github.com/oisee/vibing-steampunk) | 439 | ABAP ADT-to-MCP bridge |
| [SAP Skills for Claude Code](https://github.com/secondsky/sap-skills) | 389 | CAP, Fiori, ABAP, BTP |
| [MCP SAP Docs](https://github.com/marianfoo/mcp-sap-docs) | 213 | Unified documentation search |
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

## Intuit QuickBooks — Official 145-Tool Server

### intuit/quickbooks-online-mcp-server — Most Comprehensive Single-Server ERP MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server) | 352 | TypeScript | Apache-2.0 | 145 |

**The most feature-dense ERP MCP server in any category** — official Intuit server providing complete QuickBooks Online integration:

- **145 tools** across 29 entity types — Customers, Invoices, Bills, Vendors, Employees, Accounts, Items, Payments, and more
- **11 financial reports** — Balance Sheet, P&L, Cash Flow, Trial Balance, and others
- **OAuth 2.0 authentication** — proper token management with sandbox and production support
- **100% test coverage** — 396 tests with Jest, TypeScript with Zod validation
- **Full CRUD operations** — not just read-only, complete create/update/delete across all entities

This is the single most comprehensive ERP MCP implementation by tool count, surpassing even Microsoft's D365 community servers.

## Odoo

### erpipe-org/mcp-odoo (formerly tuanle96/mcp-odoo) — Now a 41-Tool Production Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-odoo](https://github.com/erpipe-org/mcp-odoo) | 387 | Python | — | 41 |

**Transformed from a basic XML-RPC bridge to a 41-tool production server**, now at [v1.3.1 (August 14, 2026)](https://github.com/erpipe-org/mcp-odoo/releases). The repository was transferred from `tuanle96` to the `erpipe-org` organization in July 2026 (old links redirect automatically):

- **Odoo JSON-2 protocol support** — modernized beyond XML-RPC
- **Safe write workflow** — preview/validate/approve/execute gates for data safety
- **ACL and record-rule diagnosis** — debug access control issues
- **Addon scanning and linting** — analyze installed modules
- **Field ACL, cross-instance queries, and workflow prompts** — expanded through the 1.x release series
- **Streamable HTTP transport** — modern MCP transport support
- **Docker Compose testing** — CI against Odoo 16-19, PyPI published

The jump from ~6 tools in March 2026 to 41 tools by August 2026 shows continued rapid maturation.

### ivnvxd/mcp-server-odoo — Grown to 368 Stars

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo) | 368 | Python | MPL-2.0 | 10+ |

**Stars grew from 130 in March 2026 to 368** — one of the fastest-growing Odoo MCP servers. Note: the license is MPL-2.0, not MIT as an earlier version of this review stated.

- **[v0.7.1](https://github.com/ivnvxd/mcp-server-odoo/releases)** (June 12, 2026) — adds `ODOO_MCP_ALLOWED_HOSTS` for DNS-rebinding protection and `ODOO_MCP_SESSION_IDLE_TIMEOUT` for session expiration
- **v0.5.0** (February 28) — FastMCP lifespan hooks, Context injection with logging/progress, `/health` HTTP endpoint, model name autocomplete
- **719 tests, 90% coverage** — integration tests accelerated 4.4x
- **YOLO mode** — quick testing without Odoo module installation
- **Enterprise module** — optional production access controls

### New Odoo MCP Servers

| Server | Stars | Description |
|--------|-------|-------------|
| [marcfargas/odoo-toolbox](https://github.com/marcfargas/odoo-toolbox) | 39 | TypeScript SDK + CLI + MCP, 10 command groups, CI-tested Odoo v17-v18 |
| [pantalytics/odoo-mcp-pro](https://github.com/pantalytics/odoo-mcp-pro) | 66 | Hosted + self-hosted, Odoo 14-19+, 10 tools, v1.5.0 |
| [rosenvladimirov/odoo-claude-mcp](https://github.com/rosenvladimirov/odoo-claude-mcp) | 47 | 197+ tools (92 native + 105 proxied), multi-tenant, Qdrant vector store |
| [mart337i/odoo-dev-mcp](https://github.com/mart337i/odoo-dev-mcp) | 20 | Module development focus |
| [hachecito/odoo-mcp-improved](https://github.com/hachecito/odoo-mcp-improved) | 48 | Extended fork, dormant since Jan 2025 |

## Microsoft Dynamics 365

### Official Dynamics 365 ERP MCP Server — GA February 2026

**The [dynamic framework reached GA on February 18, 2026](https://microsoftpartners.microsoft.com/abs/Blog/?title=Dynamics+365+ERP+Model+Context+Protocol+%28MCP%29+Server+now+generally+available+%28GA%29)**, evolving from [13 static tools](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2025/11/11/dynamics-365-erp-model-context-protocol/) (announced in public preview, November 2025) to unlocking hundreds of thousands of ERP functions:

- **Three tool categories** — Data tools (CRUD operations), Form tools (navigate server forms like a human), Analytics tools
- **Dynamic framework** — automatically exposes ISV extensions and customizations
- **Full UI parity** — agents can perform nearly any function available through the application interface
- **ERP Analytics MCP** — separate server for Business Performance Analytics (still in preview)
- **Business Central** — troubleshooting MCP server for AL runtime issues in debugging sessions (2026 Wave 1)

### microsoft/Dataverse-skills — NEW AI Agent Skills

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Dataverse-skills](https://github.com/microsoft/Dataverse-skills) | 201 | — | MIT | 8 skills |

**Created March 11, 2026** — wraps the Dataverse MCP server, Dataverse CLI, Python SDK, and PAC CLI behind 8 specialist skills for AI coding agents.

### Dataverse MCP Server — Generally Available

**Already GA** — the Dataverse MCP Server provides natural language access to Microsoft's low-code data platform with built-in tools for CRUD, search, and prompt execution. Works with Copilot Studio and GitHub Copilot in VS Code. The [microsoft/Dataverse-MCP](https://github.com/microsoft/Dataverse-MCP) companion repo (60 stars) provides labs and tutorials.

### dynamics365ninja/d365fo-mcp-server — F&O Development

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [d365fo-mcp-server](https://github.com/dynamics365ninja/d365fo-mcp-server) | 130 | TypeScript | — | 23 |

**23 tools for X++ development** with IntelliSense-like navigation, EDT suggestions, and AI-driven table/form generation. Over 2,100 commits, very actively maintained since January 2026. (An earlier version of this review stated 54 tools; the current README states 23.)

### Community Business Central Servers

| Server | Stars | Commits | Description |
|--------|-------|---------|-------------|
| [SShadowS/business-central-mcp](https://github.com/SShadowS/business-central-mcp) | 34 | 356 | Reverse-engineered WebSocket, 12 tools |
| [mafzaal/d365fo-client](https://github.com/mafzaal/d365fo-client) | 37 | 674 | Python, 49 tools across 9 categories |
| [knowall-ai/mcp-business-central](https://github.com/knowall-ai/mcp-business-central) | 8 | 26 | API v2.0 access, 6 tools |
| [demiliani/D365BCAdminMCP](https://github.com/demiliani/D365BCAdminMCP) | 9 | 11 | Admin tools, npm v1.2.0 |
| [MS-Cloud-Experts/mcp-business-central](https://github.com/MS-Cloud-Experts/mcp-business-central) | 0 | — | 115 tools covering 93 BC entities (85 standard + 8 custom) |

## Oracle NetSuite

### NetSuite Native AI Connector — Major 2026 Upgrades

**Oracle's official MCP integration received significant enhancements** in 2026:

- **[AI Connector Service Companion](https://www.cpapracticeadvisor.com/2026/03/31/oracle-netsuite-rolls-out-upgrades-to-ai-connector-service/180577/)** (March 2026) — [100+ finance-specific prompt templates](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_9091153093.html) organized by business process and role, Companion Skills injecting NetSuite domain knowledge, pre-configured roles (CFO, Controller, AR/AP/Treasury Analyst) mapping AI capabilities to NetSuite permissions
- **[SuiteCloud Agent Skills](https://www.prnewswire.com/news-releases/netsuite-brings-ai-powered-speed-and-precision-to-suitecloud-development-302754790.html)** (April 28, 2026 at SuiteConnect SF) — first ERP platform to leverage the agentskills.io open standard, with skills for UI Framework References, Permissions References, OWASP Security, and SuiteScript Conversion across 25+ AI coding platforms
- **MCP Apps** — bring native NetSuite UI elements (filters, forms, selectors) into AI assistant interfaces for hybrid text+GUI interaction
- **NetSuite 2026.1** — added LLM Connector for Data Warehouse and iPaaS solutions

### dsvantien/netsuite-mcp-server — SuiteInsider Community MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [netsuite-mcp-server](https://github.com/dsvantien/netsuite-mcp-server) | 19 | JavaScript | — | 5+ |

Grown to 19 stars. [Still listed](https://github.com/modelcontextprotocol/servers) on the official MCP servers repository. OAuth 2.0 with PKCE authentication, SuiteQL queries, npm distribution as `@suiteinsider/netsuite-mcp`. Development paused (last commit October 2024).

## Oracle Cloud

### oracle/mcp — Expanded to 423 Stars

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [oracle/mcp](https://github.com/oracle/mcp) | 423 | Multi-language | — | 28+ servers |

**Significantly expanded** with 28+ MCP server implementations under `/src/` covering:

- **Database** — Oracle DB tools, MySQL, GoldenGate, Java toolkit
- **OCI services** — Compute, Networking, Identity, Monitoring, IoT, Pricing, Migration, Logging, Load Balancer, Object Storage, and more
- **Documentation** — oracle-db-doc-mcp-server
- **605 total commits**, 131 forks — very active official development

[shjanjua/OCI-MCP-Servers](https://github.com/shjanjua/OCI-MCP-Servers) (2 stars) is effectively superseded by oracle/mcp's broader coverage.

## Sage Intacct — Official MCP Server

**Sage published an official MCP server for Sage Intacct** as part of the [2026 R2 release](https://www.dsdinc.com/sage-intacct-2026-release-2-highlights-features-and-more/) (May 2026), available on the [Sage Developer Portal](https://developer.sage.com/intacct/mcps/intacct-mcp/latest/intacct-mcp-server) as the "Sage Intacct AI Gateway." It provides [read-only access](https://www.eisneramper.com/insights/sage-intacct-insights/sage-intacct-2026-r2-releases-0626/) to core financial areas (AP, AR, Cash Management, GL, Purchasing, Order Entry). This fills a significant gap — Sage was previously listed as having zero MCP coverage. (An earlier version of this review incorrectly attributed this to the 2026 R1 release; Sage's own R1 release notes make no mention of MCP.)

## Workday — Official Reference Architecture

### workday/ai-conversation-bridge — First Official Workday MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ai-conversation-bridge](https://github.com/workday/ai-conversation-bridge) | 8 | — | — | 11 demo tools |

**Created March 2026** — official Workday reference architecture connecting enterprise messaging apps (LINE WORKS, WeChat, Feishu) to Workday via MCP. Includes 11 demo tools with documentation pointing to "Workday's official MCP endpoints via Agent Gateway" for production use. Previously the biggest gap (top-5 cloud ERP vendor with zero MCP coverage).

(An earlier version of this review cited a community repo, `KaranThink41/workday_mcp_server`, providing 3 tools; that repository no longer resolves on GitHub as of this audit and has been removed from this review.)

## Infor — Coverage Remains Thin

The package `@douglaslinsmeyer/infor-mcp-server`, previously described in this review as a 100+ tool server with a "Safe Mode" feature, could not be found on the npm registry as of this audit — the package name does not currently resolve, and no corresponding GitHub repository under that name exists. That specific claim has been removed since it can no longer be verified.

What does exist from the same developer: [douglaslinsmeyer/infor-ion-mcp-lite](https://github.com/douglaslinsmeyer/infor-ion-mcp-lite), a much smaller, lightweight MCP server (22 tools, unstarred) for querying Infor Data Lake via Data Fabric SQL and the ION API — a data-query tool, not the broad persona-based ERP server previously described. Community coverage of Infor CloudSuite ERP itself remains limited.

## IFS Cloud — First MCP Integrations

One community server for IFS Cloud ERP that this review previously cited, `keerthiprasad10/ifs-cloud-mcp`, no longer resolves on GitHub as of this audit and has been removed pending re-verification.

- **[knakit/ifs-mcp-server-local](https://github.com/knakit/ifs-mcp-server-local)** — skill-based (no coding required) IFS Cloud automation via OAuth 2.0. The author describes it explicitly as a personal project, "NOT tested in a production environment."

This remains one of the only MCP integrations for this enterprise ERP vendor.

## Multi-ERP Connectors

### CData Connect AI — Universal ERP Gateway

**Commercial platform** providing MCP access to 200+ enterprise data sources through a unified interface. Read-only free tier; full CRUD requires CData Connect AI (commercial). No longer the only option for SAP, but remains the best cross-ERP solution.

## What's Missing

- **Epicor now has a read-only MCP option** — [CData's Epicor Kinetic MCP Server](https://github.com/CDataSoftware/epicor-kinetic-mcp-server-by-cdata) (JDBC-based, read-only) shipped since this review was last refreshed; no official or full-CRUD server exists yet for Epicor Kinetic, a Leader in Gartner's Manufacturing ERP quadrant
- **Workday still early** — official reference architecture but demo-stage tools, not production-ready
- **SAP community fragmentation** — 80+ servers means choice overload, no clear "best" server for each use case
- **No cross-ERP unified interface** — no single MCP server provides a consistent interface across multiple ERP systems
- **Limited NetSuite community** — despite Oracle's official upgrades, the dsvantien/netsuite-mcp-server community project's development remains paused (last commit October 2024)
- **No ERP-to-ERP data migration MCP** — no server assists with data migration between ERP systems

## The Bottom Line

**Rating: 4/5** — The ERP MCP landscape was **completely transformed** in the 44 days between this review's original publication (March 2026) and its first refresh (April 2026), and has continued to grow since. SAP went from the biggest gap (zero servers) to the largest ecosystem (80+ servers, 5 official, now with hundreds of combined stars). QuickBooks shipped 145 tools in one server. Every major ERP vendor — SAP, Microsoft, Oracle/NetSuite, Intuit, Sage, Workday — now has solid MCP coverage; Infor's coverage remains thin (see above).

The standout newcomers: SAP's oisee/vibing-steampunk (439 stars) for ABAP development, Intuit's QuickBooks MCP (352 stars, 145 tools) for the most comprehensive single-server implementation, and Microsoft's D365 ERP MCP reaching GA with a dynamic framework exposing hundreds of thousands of functions.

For developers: QuickBooks has the most complete and accessible MCP tooling (145 tools, Apache-2.0, 100% test coverage). For SAP shops: you now have 80+ choices — start with the official @cap-js/mcp-server or the community catalog at marianfoo/sap-ai-mcp-servers. For enterprises: Microsoft's D365 ERP MCP is GA with the most ambitious architecture, and Oracle NetSuite's AI Connector Service Companion adds 100+ finance-specific prompts.

*This review was originally published 2026-03-16 and has been refreshed and re-audited several times since; see front matter for the current `last_refreshed` and `sources_audited` dates.*

