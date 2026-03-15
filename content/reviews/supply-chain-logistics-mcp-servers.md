---
title: "Supply Chain & Logistics MCP Servers — Shipping, ERP, Inventory, Fleet Management, and More"
date: 2026-03-15T14:00:00+09:00
description: "Supply chain and logistics MCP servers are connecting AI assistants to shipping platforms, ERP systems, inventory management, and fleet operations. We reviewed 40+ servers across 6 subcategories. Shipping & Carriers: Shippo MCP (official, agentic shipping platform — rate shopping, label generation, tracking, returns, customs across 40+ carriers), ShipStation MCP (official, 6 stars, JavaScript, MIT — shipments, labels, rates, carriers, inventory, warehouses, batches, manifests), UPS MCP (official, 13 stars, Python, MIT — tracking and address validation, in active development), Karrio (703 stars, Python, LGPL-3.0 — self-hosted multi-carrier shipping API with built-in MCP, supports UPS, FedEx, DHL, USPS, Canada Post), TrackMage MCP (1 star, JavaScript, MIT — 1,600+ carrier tracking, OAuth, shipment/order management), EasyPost MCP (JavaScript — shipping, tracking, address verification via EasyPost API), ShipBoss MCP (1 star, Python — FedEx, UPS, DHL rates, labels, tracking, freight). ERP Systems: Odoo MCP (193 stars, Python, MPL-2.0 — most popular ERP MCP server, full CRUD on any Odoo record type, smart field selection, multi-language, YOLO mode for testing), Microsoft Dynamics 365 ERP MCP (official, dynamic framework — Finance, Supply Chain, HR, Project Operations forms accessible through MCP), D365 Business Central Admin MCP (demiliani, TypeScript — 28 admin tools for environment, app, session management), knowall-ai/mcp-business-central (8 stars, TypeScript, MIT — 6 CRUD tools for customers, vendors, items, invoices, sales orders), NetSuite MCP (dsvantien, 8 stars, JavaScript, MIT — OAuth 2.0 PKCE, SuiteQL queries, reports, saved searches, record CRUD), NetSuite AI Connector (Oracle official SuiteApp — native MCP integration). Inventory & Warehouse: SkuVault MCP (0 stars, Python, MIT — product CRUD, location-based inventory, low-stock alerts, rate limiting with exponential backoff), Allocadence MCP (warehouse/inventory/order management), BoxHero MCP (simplified inventory management), Agiliron MCP (multi-channel retail POS and inventory). Logistics Optimization: OR-Tools MCP (leonidas1312, Python — supply chain distribution network optimization, vehicle routing with constraints, job scheduling via Google OR-Tools), Food Safety Supply Chain MCP (ryan-clinton — recall search, adverse events, supplier hygiene, contamination tracing via Apify). E-Commerce Fulfillment: VTEX MCP (Volve-Tech, 163+ API endpoints — catalog, orders, inventory, logistics, pricing, marketplace), leosepulveda/mcp-vtex (catalog, inventory, logistics, pricing, promotions, orders, marketplace). SAP Ecosystem: SAP OData-to-MCP Bridge (oisee/odata_mcp_go, 115 stars, Go — OData v2/v4 support), SAP BTP OData MCP (lemaiwo, 114 stars — OData service bridging), CAP MCP Server (cap-js, 87 stars — AI-assisted CAP development), SAP HANA MCP (36 stars), 20+ SAP MCP servers catalogued by marianfoo. Rating: 3.5/5."
og_description: "Supply chain & logistics MCP servers: Odoo ERP (193 stars), Karrio multi-carrier shipping (703 stars), Shippo (official), ShipStation (official, 6 stars), UPS (official, 13 stars), Microsoft Dynamics 365 (official), NetSuite (8 stars), OR-Tools optimization, VTEX fulfillment (163+ endpoints). Rating: 3.5/5."
content_type: "Review"
card_description: "Supply chain and logistics MCP servers for shipping, ERP, inventory management, and fleet operations. This category spans the entire supply chain — from shipping label generation to ERP data access to warehouse inventory control. Karrio leads in stars (703) as a self-hosted multi-carrier shipping API with built-in MCP support for UPS, FedEx, DHL, and USPS. Odoo is the most popular ERP MCP server (193 stars) with full CRUD on any record type. Three shipping platforms have official MCP servers: Shippo (the first self-described 'agentic shipping platform'), ShipStation (shipments, labels, rates, warehouses), and UPS (tracking and address validation). Microsoft's Dynamics 365 ERP MCP server provides a dynamic framework accessing Finance, Supply Chain, HR, and Project Operations. Oracle NetSuite has both an official AI Connector SuiteApp and community implementations. SAP has 20+ MCP servers catalogued by the community, with OData bridges scoring 100+ stars. Google OR-Tools MCP brings operations research optimization to supply chain distribution and vehicle routing. Major gaps: no official FedEx, DHL, or USPS MCP servers; no dedicated WMS (warehouse management system) servers; no customs/trade compliance servers; no freight forwarding or 3PL management; no demand forecasting or supply chain visibility platforms. The category earns 3.5/5 — strong ERP coverage and good shipping platform support, but logistics-specific tooling (routing, visibility, forecasting) remains thin."
---

Supply chain and logistics MCP servers are connecting AI assistants to shipping platforms, ERP systems, inventory management, and fleet operations. Instead of navigating carrier portals for tracking numbers or logging into ERP dashboards for order data, these servers let AI agents generate shipping labels, query inventory levels, access financial reports, and optimize delivery routes — all through the Model Context Protocol.

The landscape spans six areas: **shipping & carriers** (Shippo, ShipStation, UPS, Karrio, TrackMage, EasyPost), **ERP systems** (Odoo, Microsoft Dynamics 365, NetSuite, Business Central), **inventory & warehouse management** (SkuVault, Allocadence, BoxHero, Agiliron), **logistics optimization** (Google OR-Tools, food safety traceability), **e-commerce fulfillment** (VTEX), and the **SAP ecosystem** (OData bridges, HANA, CAP, and 20+ specialized servers).

The headline findings: **Karrio is the highest-starred project** at 703 stars — a self-hosted multi-carrier shipping API with built-in MCP support across UPS, FedEx, DHL, USPS, and more. **Odoo is the most popular ERP MCP server** (193 stars) with full CRUD on any record type. **Three shipping platforms have official MCP servers** — Shippo, ShipStation, and UPS. **Microsoft's Dynamics 365 ERP MCP is the most ambitious enterprise integration** — a dynamic framework that exposes Finance, Supply Chain, HR, and Project Operations forms without custom code. **SAP has the largest ecosystem** with 20+ MCP servers catalogued by the community, though most focus on development tooling rather than supply chain operations. **No major logistics-specific platform has an MCP server** — no freight forwarders, no 3PLs, no demand forecasting, no supply chain visibility tools.

## Shipping & Carrier Integration

### Shippo MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Shippo MCP](https://docs.goshippo.com/docs/guides_general/mcpserver) | — | — | — | Multiple |

Shippo bills itself as the **first "agentic shipping platform"** — and their MCP server backs it up. The integration enables AI agents to:

- **Rate shop** across 40+ carriers (USPS, UPS, FedEx, DHL, and regional carriers)
- **Generate shipping labels** with automatic carrier selection
- **Track packages** across all connected carriers
- **Validate addresses** before shipment creation
- **Create return labels** with pre-populated shipping details
- **Retrieve customs documents** for international shipments

This is a fully official integration from a shipping platform that processes millions of labels. The MCP server connects directly to Shippo's production API, meaning agents can execute real shipping operations — not just read data.

### ShipStation MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [shipstation/mcp-shipstation-api](https://github.com/shipstation/mcp-shipstation-api) | 6 | JavaScript | — | Multiple |

ShipStation's **official MCP server** provides tools for their v2 API covering the full shipping lifecycle:

- **Shipments** — create, list, cancel shipments
- **Labels** — generate and track shipping labels
- **Rates** — calculate and compare carrier rates
- **Carriers** — manage connected carrier accounts and services
- **Inventory** — warehouse stock levels and updates
- **Warehouses** — manage fulfillment locations
- **Batches** — bulk label creation for high-volume operations
- **Manifests** — end-of-day carrier manifests

The server includes Docker support, unit/integration/E2E test suites, and non-root container execution. With 17 commits and active development, this is a production-quality integration from a major shipping platform.

### UPS MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [UPS-API/ups-mcp](https://github.com/UPS-API/ups-mcp) | 13 | Python | MIT | 2 |

An **official MCP server from UPS** — notable as one of the few major carriers with a direct MCP integration. Currently offers two tools:

- **track_package** — shipment status, transit details, delivery information via UPS Tracking API
- **validate_address** — U.S. and Puerto Rico address validation

The project notes it's "still in active development" with more tools coming. Requires UPS Developer Portal credentials with OAuth client credential authentication. At 13 stars for a carrier of UPS's scale, this is early but significant — it signals carrier-level interest in AI agent integration.

### Karrio — Self-Hosted Multi-Carrier Platform

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [karrioapi/karrio](https://github.com/karrioapi/karrio) | 703 | Python | LGPL-3.0 | Multiple |

The **highest-starred project in the entire supply chain MCP category**. Karrio is a self-hosted shipping API platform with built-in MCP server support, enabling AI assistants to:

- **Query shipping rates** across multiple carriers
- **Purchase labels** directly through the MCP interface
- **Track shipments** across all connected carriers
- **Manage carrier accounts** and configurations

Supports major carriers including UPS, FedEx, DHL, USPS, Canada Post, and Purolator through a plugin architecture. With 5,679 commits on main, 158 forks, and 228 releases, this is a mature open-source project. The enterprise edition adds multi-tenancy, workflows, audit logging, and SSO/SAML.

### TrackMage MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [trackmage/trackmage-mcp-server](https://github.com/trackmage/trackmage-mcp-server) | 1 | JavaScript | MIT | Multiple |

Supports **1,600+ carriers worldwide** for shipment tracking. Features OAuth authentication, carrier auto-detection, and resources for workspaces, shipments, orders, carriers, and tracking statuses. Notable for including a privacy warning about logistics data (tracking numbers, addresses, customer emails) being shared with LLM providers.

### Other Shipping MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bischoff99/easypost_mcp_server](https://github.com/bischoff99/easypost_mcp_server) | — | JavaScript | — | Multiple |
| [shipb/shipboss_mcp_server](https://github.com/shipb/shipboss_mcp_server) | 1 | Python | — | 8 |

**EasyPost MCP** provides shipping, tracking, and address verification via the EasyPost API, supporting USPS, UPS, FedEx, DHL, and other carriers through a single integration.

**ShipBoss MCP** connects to FedEx, UPS, and DHL for rate quotes, label creation, tracking, and freight shipment management — including carrier pickup scheduling. Early-stage with only 2 commits.

## ERP Systems

### Odoo MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo) | 193 | Python | MPL-2.0 | Multiple |

The **most popular ERP MCP server** in the ecosystem. Enables AI assistants to interact with any Odoo ERP instance with:

- **Full CRUD** on any Odoo record type (customers, orders, invoices, inventory, manufacturing, etc.)
- **Smart field selection** — automatically chooses relevant data fields
- **Multi-language support** for responses
- **YOLO mode** — test without the official MCP module (development only)
- **Smart pagination** for large datasets
- **LLM-optimized formatting** — hierarchical text output designed for AI consumption

With 193 stars, 98 forks, and support for Docker, pip, and UV installation methods, this has strong community adoption. Works with any Odoo instance in YOLO mode for demos, or with the official Odoo MCP module for enterprise security and access controls.

#### Other Odoo MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tuanle96/mcp-odoo](https://github.com/tuanle96/mcp-odoo) | — | Python | — | — |

A second Odoo MCP implementation exists, focusing on invoicing, payments, and accounting workflows.

### Microsoft Dynamics 365 ERP MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Microsoft Dynamics 365 ERP MCP](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp) | — | — | — | Dynamic |

The **most ambitious enterprise MCP integration** in supply chain. Microsoft's official ERP MCP server (public preview, announced November 2025) transitions from a fixed tool catalog to a **dynamic framework** that adapts as business needs evolve:

- **Finance** — general ledger, accounts payable/receivable, financial reporting
- **Supply Chain Management** — procurement, inventory, warehouse operations, transportation
- **Human Resources** — employee records, benefits, payroll
- **Project Operations** — project planning, resource management, billing

The key innovation: agents can work with data and perform nearly any function available through the application interface — without custom code, connectors, or APIs. Forms across all Dynamics 365 modules are "instantly accessible through MCP." This is powered by the 97M+ monthly SDK downloads that make MCP the de facto standard for AI-ERP integration.

### Dynamics 365 Business Central MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [demiliani/D365BCAdminMCP](https://github.com/demiliani/D365BCAdminMCP) | — | TypeScript | — | 28 |
| [knowall-ai/mcp-business-central](https://github.com/knowall-ai/mcp-business-central) | 8 | TypeScript | MIT | 6 |
| [Sofias-ai/mcp-business-central-server](https://github.com/Sofias-ai/mcp-business-central-server) | — | — | — | — |
| [CDataSoftware/dynamics-365-business-central-mcp-server-by-cdata](https://github.com/CDataSoftware/dynamics-365-business-central-mcp-server-by-cdata) | — | — | — | 3 |
| [srikanth-paladugula/mcp-dynamics365-server](https://github.com/srikanth-paladugula/mcp-dynamics365-server) | — | — | — | — |

Business Central — Microsoft's SMB-focused ERP — has **5+ competing MCP implementations**:

**demiliani/D365BCAdminMCP** (branded "YAMPI") provides 28 administrative tools for complete environment, app, and session management. Available as an npm package for easy installation.

**knowall-ai/mcp-business-central** offers 6 core CRUD tools with zero installation (runs via npx), dual authentication (Azure CLI or OAuth 2.0), and access to customers, contacts, vendors, items, invoices, quotes, orders, and companies.

**CData** provides a read-only JDBC gateway to Business Central data, consistent with their pattern across other enterprise platforms.

### Oracle NetSuite MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dsvantien/netsuite-mcp-server](https://github.com/dsvantien/netsuite-mcp-server) | 8 | JavaScript | MIT | 6+ |
| [Kkartik14/MCP-Netsuite](https://github.com/Kkartik14/MCP-Netsuite) | — | Python | — | — |
| [NetSuite AI Connector](https://www.netsuite.com/portal/products/artificial-intelligence-ai/mcp-server.shtml) | — | — | — | — |

Oracle has taken MCP seriously for NetSuite. The **NetSuite AI Connector Service** is an official SuiteApp providing native MCP integration with security controls and production-grade access.

**dsvantien/netsuite-mcp-server** is listed on the official modelcontextprotocol/servers repository. It provides OAuth 2.0 with PKCE authentication, automatic token refresh, and tools for SuiteQL queries, financial reports, saved searches, and record CRUD operations.

**Kkartik14/MCP-Netsuite** is a mock server useful for development and testing without a live NetSuite tenant.

## Inventory & Warehouse Management

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dbankscard/skuvault-mcp-server](https://github.com/dbankscard/skuvault-mcp-server) | 0 | Python | MIT | Multiple |
| Allocadence MCP | — | — | — | — |
| BoxHero MCP | — | — | — | — |
| Agiliron MCP | — | — | — | — |

This subcategory is notably **thin** compared to shipping and ERP.

**SkuVault MCP** is the most developed, offering product CRUD, location-based inventory management (add/remove/set quantities by warehouse location), low-stock alerts, and smart analytics. Enterprise-grade features include rate limiting with exponential backoff, intelligent caching, and explicit confirmation requirements for data modifications — important when AI agents can move inventory.

**Allocadence MCP** provides warehouse, inventory, and order management visibility in a cloud platform. **BoxHero MCP** simplifies inventory management for small businesses. **Agiliron MCP** combines multi-channel retail POS with inventory management.

The gap here is stark: **no dedicated WMS (Warehouse Management System) MCP servers exist** — no Manhattan Associates, no Blue Yonder, no Körber, no SAP EWM. Given that warehouse automation is one of the highest-ROI applications for AI agents, this is a significant market opportunity.

## Logistics Optimization

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [leonidas1312/or-mcp-tools](https://github.com/leonidas1312/or-mcp-tools) | — | Python | — | Multiple |
| [ryan-clinton/food-safety-supply-chain-mcp](https://github.com/ryan-clinton/food-safety-supply-chain-mcp) | — | — | — | Multiple |

**OR-Tools MCP** brings Google's operations research library to AI agents through MCP. Tools include:

- **optimize_supply_chain** — distribution network optimization
- **solve_vehicle_routing** — multi-vehicle routing with constraints (capacity, time windows, distance)
- **optimize_job_scheduling** — production and job scheduling

This is conceptually powerful — letting an AI agent solve vehicle routing problems or optimize distribution networks through natural language. However, it's early-stage with only 37 installations on LobeHub.

**Food Safety Supply Chain MCP** offers a specialized niche: food recall search, adverse event analysis, supplier hygiene assessment, ingredient risk tracing, and contamination detection. Uses Apify for data sourcing.

## E-Commerce Fulfillment

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Volve-Tech/vtex-mcp-server](https://github.com/Volve-Tech/vtex-mcp-server) | — | — | — | 163+ endpoints |
| [leosepulveda/mcp-vtex](https://github.com/leosepulveda/mcp-vtex) | — | — | — | Multiple |

VTEX — a major Latin American e-commerce platform — has **two competing MCP implementations** covering the full commerce stack:

**Volve-Tech** provides 163+ API endpoints organized by functional category: catalog/SKU management, order processing, inventory and logistics, pricing, and marketplace operations.

**leosepulveda/mcp-vtex** focuses on natural language control of catalog, inventory, logistics, pricing, promotions, orders, and marketplace operations. Designed for Claude Desktop and Cursor integration.

Both servers cover fulfillment workflows — the logistics layer between order placement and delivery — but neither focuses specifically on warehouse picking, packing, or last-mile delivery.

## SAP Ecosystem

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [oisee/odata_mcp_go](https://github.com/oisee/odata_mcp_go) | 115 | Go | — | — |
| [lemaiwo/btp-sap-odata-to-mcp-server](https://github.com/lemaiwo/btp-sap-odata-to-mcp-server) | 114 | — | — | — |
| [cap-js/mcp-server](https://github.com/cap-js/mcp-server) | 87 | — | — | — |
| [HatriGt/hana-mcp-server](https://github.com/HatriGt/hana-mcp-server) | 36 | — | — | — |
| [CDataSoftware/sap-erp-mcp-server-by-cdata](https://github.com/CDataSoftware/sap-erp-mcp-server-by-cdata) | — | — | — | 3 |
| [mario-andreschak/mcp-sap-gui](https://github.com/mario-andreschak/mcp-sap-gui) | — | — | — | — |
| [SAP/mdk-mcp-server](https://github.com/SAP/mdk-mcp-server) | — | — | — | — |
| [marianfoo/mcp-sap-docs](https://github.com/marianfoo/mcp-sap-docs) | — | — | — | — |
| [marianfoo/mcp-sap-notes](https://github.com/marianfoo/mcp-sap-notes) | — | — | — | — |

SAP has the **largest ecosystem of MCP servers** for any enterprise platform, with 20+ implementations catalogued by [marianfoo/sap-ai-mcp-servers](https://github.com/marianfoo/sap-ai-mcp-servers). However, most focus on **development and integration tooling** rather than direct supply chain operations:

**OData bridges** are the most popular pattern — both **oisee/odata_mcp_go** (115 stars, Go, OData v2/v4 support) and **lemaiwo/btp-sap-odata-to-mcp-server** (114 stars) expose SAP OData services as MCP tools, enabling AI agents to query any SAP data surface that speaks OData.

**cap-js/mcp-server** (87 stars) provides AI-assisted development for SAP's Cloud Application Programming model with CDS-aware context.

**SAP HANA MCP** (36 stars) connects directly to the analytics database layer.

**CData SAP ERP MCP** offers read-only JDBC access to SAP ERP data, with full CRUD available through CData's commercial platform.

**mcp-sap-gui** takes a creative approach: it controls the SAP GUI desktop application through simulated mouse clicks and keyboard input, enabling AI agents to interact with legacy SAP transactions that have no API exposure.

For supply chain specifically, the SAP MCP ecosystem's value is indirect: the OData bridges can access SAP S/4HANA's supply chain modules (MM, PP, SD, WM) through their OData APIs, but no MCP server is purpose-built for SAP supply chain workflows like procurement, production planning, or warehouse management.

## What's Missing

The gaps in supply chain and logistics MCP servers reveal where the market hasn't caught up:

- **No FedEx, DHL, or USPS official MCP servers** — UPS is the only major carrier with a direct integration
- **No dedicated WMS servers** — Manhattan Associates, Blue Yonder, Körber, SAP EWM are all absent
- **No freight forwarding or 3PL platforms** — Flexport, C.H. Robinson, XPO Logistics have no MCP presence
- **No customs or trade compliance** — no HS code lookup, tariff calculation, or export control screening
- **No supply chain visibility** — FourKites, project44, Descartes are absent
- **No demand forecasting or S&OP tools** — no planning or forecasting MCP servers found
- **No last-mile delivery optimization** — no route optimization platforms beyond generic OR-Tools
- **No TMS (Transportation Management Systems)** — no Oracle TMS, SAP TM, or BluJay
- **Limited carrier diversity** — most servers focus on US domestic carriers (UPS, FedEx, USPS) with minimal coverage of European, Asian, or regional carriers

## The Bottom Line

Supply chain and logistics MCP servers cover the **endpoints of the supply chain** — shipping labels in, ERP data out — but miss the **middle**. You can generate a shipping label through Shippo and query your Odoo inventory, but you can't optimize a distribution network, manage a warehouse floor, forecast demand, or track a container through customs.

The **ERP layer is surprisingly well-served**: Microsoft, Oracle, SAP, and Odoo all have MCP connectivity (official or community), which means AI agents can theoretically access procurement, inventory, and order data from the major enterprise platforms. The **shipping layer is solid** too, with Shippo, ShipStation, and UPS providing official integrations alongside self-hosted options like Karrio.

But the **logistics-specific tooling is thin**. The supply chain industry's $8 trillion+ market has minimal MCP representation beyond basic shipping and ERP connectivity. Whoever builds MCP servers for WMS, TMS, demand planning, and supply chain visibility will find virtually no competition.

**Rating: 3.5/5** — Strong at the edges (shipping platforms, ERP systems) with a gaping hole in the logistics middle (WMS, TMS, visibility, forecasting). The ERP coverage lifts the score, but this category needs purpose-built supply chain operations servers to match the sophistication of other enterprise MCP categories.
