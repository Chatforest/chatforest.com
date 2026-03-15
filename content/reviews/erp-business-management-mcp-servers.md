---
title: "ERP & Business Management MCP Servers — Odoo, Dynamics 365, NetSuite, SAP, Oracle, and More"
date: 2026-03-16T09:00:00+09:00
description: "ERP and business management MCP servers let AI agents interact with enterprise resource planning systems through the Model Context Protocol. We reviewed 20+ servers across 6 subcategories. Odoo: tuanle96/mcp-odoo (269 stars, Python — most popular open-source ERP MCP, sales/inventory/accounting), ivnvxd/mcp-server-odoo (130 stars, Python, MIT — secure access with YOLO mode and enterprise module, PyPI available), hachecito/odoo-mcp-improved (29 stars — advanced sales/purchases/inventory/accounting tools). Microsoft Dynamics 365: Official Dynamics 365 ERP MCP Server (public preview — dynamic framework adapting to business needs, built into F&O), Dataverse MCP Server (GA — natural language Dataverse access, Copilot Studio integration), demiliani/D365BCAdminMCP (33 admin tools — environment management via natural language, VS Code extension), knowall-ai/mcp-business-central (Azure CLI auth, API v2.0 access), SShadowS/bc-webclient-mcp-server (reverse-engineered WebSocket protocol). Oracle NetSuite: Native AI Connector (official — SuiteApp, full security model integration), dsvantien/netsuite-mcp-server (6 stars, JavaScript — SuiteInsider, OAuth 2.0 PKCE, on official MCP servers list), glints-dev/mcp-netsuite (stdio-based, env var config). SAP: CDataSoftware/sap-erp-mcp-server-by-cdata (read-only via JDBC, plus separate servers for SAP HANA, Business One, ByDesign, Concur, Hybris C4C). Oracle Cloud: oracle/mcp (official — reference MCP servers for Oracle products, SQLcl integration), shjanjua/OCI-MCP-Servers (ADB/Compute/Identity/Networking). Multi-ERP: CData Connect AI (commercial — universal connector for 200+ enterprise data sources, read-only free tier). Gaps: no Workday MCP server, no Sage/Epicor/Infor (beyond basic ION API), no open-source SAP alternative, limited write capabilities across most servers, no cross-ERP unified interface. 20+ servers across 6 subcategories. Rating: 3.5/5."
og_description: "ERP MCP servers: tuanle96/mcp-odoo (269 stars — most popular ERP MCP), Microsoft Dynamics 365 Official MCP (public preview), Dataverse MCP (GA), ivnvxd/mcp-server-odoo (130 stars), Oracle NetSuite Native AI Connector (official), oracle/mcp (official Oracle). 20+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "ERP and business management MCP servers for AI-powered interaction with enterprise resource planning systems including Odoo, Microsoft Dynamics 365, Oracle NetSuite, SAP, and Oracle Cloud. **Odoo dominates open-source ERP MCP** — tuanle96/mcp-odoo (269 stars, Python) is the most popular ERP MCP server, providing AI assistants with access to sales, inventory, purchasing, and accounting modules through natural language. The project has spawned multiple forks and improvements, with ivnvxd/mcp-server-odoo (130 stars, Python, MIT) offering a more security-focused approach with YOLO mode for quick testing, an optional Odoo module for enterprise access controls, and PyPI distribution. hachecito/odoo-mcp-improved (29 stars) extends the original with advanced tools for sales orders, purchase orders, stock picking, and journal entries. **Microsoft has the strongest official backing** — the Dynamics 365 ERP MCP Server (public preview, announced at Build 2025) represents the most ambitious official ERP MCP implementation. Instead of a fixed tool catalog, it provides a dynamic framework that adapts as business needs evolve — agents can work with data and perform nearly any function available through the application UI without custom code. The Dataverse MCP Server is already GA, providing natural language access to Dataverse data with built-in tools for data operations, search, and prompt execution. Multiple community servers exist for Business Central: demiliani/D365BCAdminMCP offers 33 admin tools with a VS Code extension, knowall-ai/mcp-business-central provides API v2.0 access, and SShadowS/bc-webclient-mcp-server takes a creative approach by reverse-engineering BC's WebSocket protocol. **Oracle NetSuite has native MCP** — the official NetSuite AI Connector provides MCP access fully integrated with NetSuite's security model, requiring a SuiteApp installation. dsvantien/netsuite-mcp-server (SuiteInsider, 6 stars, JavaScript) is listed on the official MCP servers repository and uses OAuth 2.0 with PKCE for secure authentication. glints-dev/mcp-netsuite provides a simpler stdio-based implementation. **SAP relies on CData** — no substantial open-source SAP MCP server exists. CData Software provides read-only MCP servers for SAP ERP, SAP HANA, SAP Business One, SAP ByDesign, SAP Concur, and SAP Hybris C4C — all using JDBC drivers with a commercial model (free read-only, paid CRUD via CData Connect AI). This leaves SAP as the largest enterprise ERP vendor without a community-driven MCP server. **Oracle Cloud provides official MCP** — the oracle/mcp repository contains reference MCP server implementations for Oracle products, with MCP integrated into Oracle SQLcl for database access. shjanjua/OCI-MCP-Servers covers OCI services including Autonomous Database, Compute, Identity, and Networking. **Gaps remain significant** — no Workday MCP server exists despite Workday being a top-5 ERP vendor. Sage, Epicor, and Infor have minimal or no MCP coverage (only a basic Infor M3 ION API server). Most non-official servers are read-only or limited in write operations. No cross-ERP unified interface exists for managing multiple ERP systems through one MCP connection. The SAP ecosystem's reliance on commercial CData connectors rather than community-built servers is a notable contrast with Odoo's vibrant open-source MCP community."
---

ERP and business management MCP servers let AI assistants interact with enterprise resource planning systems through the Model Context Protocol. Instead of navigating complex ERP interfaces or writing API integrations manually, AI agents can query business data, create records, manage inventory, and automate workflows conversationally.

This review covers the **ERP ecosystem** — Odoo, Microsoft Dynamics 365, Oracle NetSuite, SAP, Oracle Cloud, and multi-ERP connectors. For related servers, see our [Accounting & Bookkeeping review](/reviews/accounting-bookkeeping-mcp-servers/), [Supply Chain & Logistics review](/reviews/supply-chain-logistics-mcp-servers/), and [CRM review](/reviews/crm-mcp-servers/).

The headline findings: **Odoo has the most active open-source community** with 269+ stars on the leading server. **Microsoft has the most ambitious official MCP** with a dynamic framework in public preview. **SAP is the notable gap** — the world's largest ERP vendor has no community-built MCP server.

## Odoo

### tuanle96/mcp-odoo — Most Popular ERP MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-odoo](https://github.com/tuanle96/mcp-odoo) | 269 | Python | — | 10+ |

**The most-starred ERP MCP server by a wide margin** — provides AI assistants with direct access to Odoo ERP modules:

- **Sales management** — create and manage sales orders, quotations, and customer records
- **Inventory control** — stock picking, warehouse operations, product management
- **Purchasing** — purchase orders, vendor management, procurement workflows
- **Accounting** — journal entries, invoices, payment processing
- **Generic CRUD** — read, create, update, and search any Odoo model via XML-RPC

The project has spawned multiple forks and improvements, making it the foundation of the Odoo MCP ecosystem.

### ivnvxd/mcp-server-odoo — Secure Odoo MCP with Enterprise Module

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo) | 130 | Python | MIT | 10+ |

**Security-focused Odoo MCP server** with a more polished distribution model:

- **YOLO mode** — quick testing and demos with any standard Odoo installation, no module required
- **Enterprise module** — optional Odoo module for production access controls and security
- **PyPI distribution** — install via `pip install mcp-server-odoo` for easy setup
- **Natural language access** — search records, create entries, update data, manage instances

Available on PyPI with proper versioning (v0.3.0). Good choice for teams that want a more production-ready Odoo MCP setup.

### hachecito/odoo-mcp-improved — Advanced Odoo Business Tools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [odoo-mcp-improved](https://github.com/hachecito/odoo-mcp-improved) | 29 | Python | MIT | 15+ |

**Extended fork of mcp-odoo** with advanced tools for specific business processes:

- **Sales tools** — sales order creation, quotation management, order confirmation workflows
- **Purchase tools** — purchase order lifecycle, vendor selection, procurement automation
- **Stock tools** — inventory picking, warehouse transfers, stock level queries
- **Accounting tools** — journal entries, invoice generation, payment reconciliation
- **Docker support** — Dockerfile included for containerized deployment

Useful if you need deeper business process automation beyond basic CRUD operations.

## Microsoft Dynamics 365

### Official Dynamics 365 ERP MCP Server — Dynamic AI Framework

**The most ambitious official ERP MCP implementation** — announced at Microsoft Build 2025, now in public preview:

- **Dynamic framework** — adapts as business needs evolve, not a fixed tool catalog
- **Full UI parity** — agents can perform nearly any function available through the application interface
- **No custom code needed** — no connectors, APIs, or custom development required
- **Finance & Operations** — covers Dynamics 365 F&O with full data access and business actions
- **Analytics preview** — MCP server for Business Performance Analytics entering preview
- **Governed protocol** — enterprise security and compliance built in

The static MCP server (first version) is being retired in 2026 as the dynamic version takes over. This represents Microsoft's vision of AI-native ERP — where agents work alongside users through the same interfaces.

### Dataverse MCP Server — Generally Available

**Already GA** — the Dataverse MCP Server provides natural language access to Microsoft's low-code data platform:

- **Natural language queries** — real-time answers grounded in Dataverse data
- **Data operations** — built-in tools for CRUD, search, and prompt execution
- **Copilot Studio integration** — works with Copilot Studio and GitHub Copilot in VS Code
- **Admin tools** — makers and admins get data management capabilities through MCP

Since Dataverse underlies all Dynamics 365 apps, this server provides a foundational layer for any D365 MCP integration.

### demiliani/D365BCAdminMCP — Business Central Administration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [D365BCAdminMCP](https://github.com/demiliani/D365BCAdminMCP) | — | TypeScript | — | 33 |

**33 administrative tools for Dynamics 365 Business Central** — manage environments through natural language:

- **Environment management** — list, create, and configure BC environments
- **Extension management** — install, update, and manage extensions
- **User administration** — manage users, permissions, and security groups
- **VS Code extension** — available on the Visual Studio Marketplace for easy setup

Works with Claude Desktop, GitHub Copilot, and Cursor. Also released as YAMPI (Yet Another MCP Package for Implementation).

### knowall-ai/mcp-business-central — API v2.0 Access

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-business-central](https://github.com/knowall-ai/mcp-business-central) | — | TypeScript | — | 10+ |

**Direct Business Central API v2.0 access** — provides AI assistants with properly formatted API calls for data retrieval and manipulation. Requires Azure CLI for authentication. Straightforward implementation for teams already using Azure AD.

### SShadowS/bc-webclient-mcp-server — Reverse-Engineered WebSocket

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bc-webclient-mcp-server](https://github.com/SShadowS/bc-webclient-mcp-server) | — | TypeScript | — | 10+ |

**Creative approach** — reverse-engineers Business Central's WebUI WebSocket protocol to provide real-time ERP access. Rather than using official APIs, this server interacts with BC through the same native WebSocket interface used by the web client, enabling access to features not exposed through standard APIs.

## Oracle NetSuite

### NetSuite Native AI Connector — Official Oracle MCP

**Oracle's official MCP integration for NetSuite** — the most feature-complete and secure option:

- **Full security model** — integrated with NetSuite's built-in security and access controls
- **SuiteApp installation** — requires deploying the AI Connector SuiteApp to your NetSuite instance
- **Oracle backing** — supported and maintained by Oracle, follows NetSuite release cycles
- **SuiteQL support** — natural language queries translated into SuiteQL

The native connector is the recommended path for enterprise NetSuite deployments, though it depends on Oracle's release cycle for enhancements.

### dsvantien/netsuite-mcp-server — SuiteInsider Community MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [netsuite-mcp-server](https://github.com/dsvantien/netsuite-mcp-server) | 6 | JavaScript | — | 5+ |

**Listed on the official MCP servers repository** — community-built NetSuite MCP with modern authentication:

- **OAuth 2.0 with PKCE** — secure authentication without client secrets
- **Automatic token refresh** — handles token lifecycle automatically
- **SuiteQL queries** — execute SuiteQL against your NetSuite instance
- **Reports and saved searches** — access NetSuite reporting from AI assistants
- **npm distribution** — available as `@suiteinsider/netsuite-mcp`

Published November 2025 by Dimitri D. Works with Claude Code, Cursor IDE, and Gemini CLI.

### glints-dev/mcp-netsuite — Stdio-Based NetSuite Access

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-netsuite](https://github.com/glints-dev/mcp-netsuite) | — | JavaScript | — | 5+ |

**Simple stdio-based NetSuite MCP** — communicates via the MCP protocol over stdio. Configured entirely through environment variables (account ID, client credentials, certificate). Minimal setup for teams that want quick NetSuite AI integration.

## SAP

### CData SAP MCP Servers — Read-Only JDBC Connectors

CData Software provides a family of **read-only MCP servers for the SAP ecosystem**, all using JDBC drivers:

| Server | Platform | Capabilities |
|--------|----------|-------------|
| [sap-erp-mcp-server-by-cdata](https://github.com/CDataSoftware/sap-erp-mcp-server-by-cdata) | SAP ERP | Read-only ERP data access |
| [sap-hana-mcp-server-by-cdata](https://github.com/CDataSoftware/sap-hana-mcp-server-by-cdata) | SAP HANA | Read-only HANA database access |
| [sap-business-one-mcp-server-by-cdata](https://github.com/CDataSoftware/sap-business-one-mcp-server-by-cdata) | SAP Business One | Read-only B1 data |
| [sap-bydesign-mcp-server-by-cdata](https://github.com/CDataSoftware/sap-bydesign-mcp-server-by-cdata) | SAP ByDesign | Read-only cloud ERP |
| [sap-concur-mcp-server-by-cdata](https://github.com/CDataSoftware/sap-concur-mcp-server-by-cdata) | SAP Concur | Read-only expense/travel |
| [sap-hybris-c4c-mcp-server-by-cdata](https://github.com/CDataSoftware/sap-hybris-c4c-mcp-server-by-cdata) | SAP Hybris C4C | Read-only CRM data |

**All read-only on the free tier** — full CRUD requires CData Connect AI (commercial). Each server requires the corresponding CData JDBC Driver. This is currently the only way to connect AI agents to SAP systems via MCP, making SAP the largest ERP vendor without a community-built open-source MCP server.

## Oracle Cloud

### oracle/mcp — Official Oracle MCP Repository

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [oracle/mcp](https://github.com/oracle/mcp) | — | Multi-language | — | Varies |

**Official Oracle repository** containing reference MCP server implementations for Oracle products:

- **Language-agnostic** — each server under `src/` may use a different language, demonstrating MCP's flexibility
- **SQLcl integration** — Oracle Database MCP is available via Oracle SQLcl, making it immediately usable with any MCP-compatible client
- **Oracle Database access** — AI agents can query and interact with Oracle databases through natural language

Oracle has integrated MCP directly into its core developer tools, providing first-party support for AI-assisted database workflows.

### shjanjua/OCI-MCP-Servers — Oracle Cloud Infrastructure

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [OCI-MCP-Servers](https://github.com/shjanjua/OCI-MCP-Servers) | — | — | — | 15+ |

**MCP servers for Oracle Cloud Infrastructure services** — each server exposes tools for a specific OCI service:

- **Autonomous Database** — manage and query ADB instances
- **Compute** — manage compute instances and shapes
- **Identity** — user and group management
- **Networking** — VCN, subnet, and security configuration

## Multi-ERP Connectors

### CData Connect AI — Universal ERP Gateway

**Commercial platform** providing MCP access to 200+ enterprise data sources through a unified interface:

- **Universal connector** — single MCP server covers SAP, NetSuite, Dynamics 365, Salesforce, and hundreds more
- **Read-only free tier** — free MCP servers use JDBC drivers for read access
- **Full CRUD paid tier** — CData Connect AI platform enables write operations
- **Consistent interface** — same MCP tool signatures regardless of underlying ERP

For organizations using multiple ERP systems, CData provides the only current option for cross-ERP MCP access, though the commercial model and read-only limitations of the free tier are significant constraints.

### Infor M3 via ION API

A basic MCP server for accessing **Infor M3 tenant information** through the ION API exists (douglaslinsmeyer/infor-ion-mcp), though coverage is limited to basic data access rather than full ERP functionality.

## What's Missing

- **No Workday MCP server** — despite being a top-5 cloud ERP vendor, Workday has zero MCP coverage
- **No Sage ERP MCP** — Sage X3 and Sage Intacct lack any MCP server implementation
- **No Epicor MCP** — Epicor Kinetic, a Leader in Gartner's Manufacturing ERP quadrant, has no MCP support
- **No open-source SAP alternative** — the world's largest ERP vendor relies entirely on commercial CData connectors for MCP access
- **Limited write operations** — most non-official servers are read-only or have restricted write capabilities
- **No cross-ERP unified interface** — no single MCP server provides a consistent interface across multiple ERP systems (CData Connect AI is the closest but is commercial)
- **No ERP-to-ERP data migration MCP** — no server assists with data migration or synchronization between ERP systems
- **No industry-specific ERP templates** — no MCP servers provide pre-built prompts for industry-specific ERP workflows (manufacturing, retail, healthcare)

## The Bottom Line

**Rating: 3.5/5** — ERP MCP servers are a growing category with uneven coverage across vendors. Odoo leads the open-source community with tuanle96/mcp-odoo (269 stars) and multiple actively maintained alternatives. Microsoft has the most ambitious official implementation — the Dynamics 365 ERP MCP Server's dynamic framework represents a vision where AI agents can do anything a user can through the ERP interface.

The category's biggest weakness is SAP. The world's largest ERP vendor has no community-built MCP server — only commercial CData read-only connectors. Given SAP's market share in manufacturing and large enterprises, this is a significant gap. Oracle NetSuite fares better with an official AI Connector, and the broader Oracle ecosystem has an official MCP repository.

For developers: Odoo has the most complete and accessible MCP tooling today. For enterprises: Microsoft's Dynamics 365 MCP is the most production-ready official option, with Dataverse MCP already GA and the dynamic ERP server in public preview. For SAP shops: you're currently limited to CData's commercial connectors or building your own.
