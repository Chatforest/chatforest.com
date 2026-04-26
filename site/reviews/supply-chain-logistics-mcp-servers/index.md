# Supply Chain & Logistics MCP Servers — SAP, Dynamics 365, Kinaxis, ShipStation, Karrio, Shippo, and More

> Supply chain and logistics MCP servers reviewed: SAP S/4HANA MCP Gateway (Joule, Integration Suite, HANA Cloud, production planning + procurement agents Q1-Q2 2026), Microsoft Dynamics 365 ERP MCP Server (dynamic tools, 20+ form/data/action tools, Supply Chain Management + Finance, GA 2026), Kinaxis MCP Server (AWS Marketplace, RapidResponse, supply chain planning, OAuth 2.0, BYOL), ShipStation official (8 stars, 50+ tools, shipments+labels+rates+carriers+inventory+batches), Karrio (719 stars, LGPL-3.0, multi-carrier labels+tracking+rates, FedEx+UPS+DHL+USPS), Shippo official (MCP via npx, multi-carrier, address validation+labels+tracking), UPS official (13 stars, 2 tools, tracking+address validation), ShipBoss (FedEx+UPS+DHL, parcel+freight, rates+labels+tracking+pickups), ShipBob community (fulfillment API, products+orders+inventory+returns), Logistics AI MCP (5 tools, tracking+routing+warehouse+customs), Odoo ERP (259 stars, MPL-2.0, full CRUD, inventory+sales+stock), NetSuite community (11 stars, OAuth 2.0 PKCE, SuiteQL+records+reports), SAP Ariba Procurement (CData JDBC, read-only sourcing data + VanshikaDhole 48 APIs), Shopify (199 stars, 31 tools, inventory+orders+fulfillment), WooCommerce (101+ tools, orders+inventory+stock), Amazon Seller (SP-API, FBA inventory+sales+reports), ReplenishRadar (28 tools, multi-channel inventory intelligence Shopify+Amazon), VTEX (163+ endpoints). MISSING: Blue Yonder, Manhattan Associates, o9 Solutions, project44, Flexport, Coupa, Infor CloudSuite, Epicor. Rating: 3.5/5.


Supply chain and logistics is where physical goods meet digital orchestration — procurement, inventory management, warehouse operations, shipping, demand planning, and end-to-end visibility. The MCP ecosystem has matured significantly here since our initial review, with **strong ERP vendor participation** from SAP and Microsoft, **good shipping platform coverage** from ShipStation, Karrio, Shippo, and UPS, **solid e-commerce integration** through Shopify, WooCommerce, and Amazon Seller servers, and a **first-mover in supply chain planning** from Kinaxis. But **dedicated supply chain planning and visibility platforms remain almost entirely absent** — no Blue Yonder, no Manhattan Associates, no project44, no Flexport. Part of our **[Logistics & Industry](/categories/logistics-industry/)** category.

This review covers **enterprise ERP platforms** (SAP S/4HANA, Microsoft Dynamics 365, Odoo, NetSuite), **supply chain planning** (Kinaxis), **shipping and carriers** (ShipStation, Karrio, Shippo, UPS, ShipBoss, EasyPost), **e-commerce fulfillment** (Shopify, WooCommerce, Amazon Seller, ShipBob, VTEX), **inventory intelligence** (ReplenishRadar, Logistics AI MCP), **procurement** (SAP Ariba), **logistics optimization** (Google OR-Tools), and the **broader SAP ecosystem**. For e-signature tools used in supply chain contracts, see [E-Signature & Digital Signing](/reviews/e-signature-digital-signing-mcp-servers/). For general ERP coverage beyond supply chain features, see [ERP & Business Management](/reviews/erp-business-management-mcp-servers/). For manufacturing-specific MCP servers, see [Manufacturing & Industrial](/reviews/manufacturing-industrial-mcp-servers/).

The headline findings: **ERP vendors are leading the charge** — SAP and Microsoft both ship comprehensive MCP server infrastructure covering supply chain operations. **Kinaxis is the first dedicated supply chain planning vendor with an MCP server** (AWS Marketplace, RapidResponse integration). **Shipping platforms have solid coverage** — ShipStation (official, 50+ tools), Karrio (719 stars, open-source multi-carrier), Shippo (official), and UPS (official) all provide production-ready shipping via MCP. **E-commerce fills the demand-side gap** — Shopify (199 stars, 31 tools), WooCommerce (101+ tools), and Amazon Seller MCP servers handle order fulfillment and inventory for online sellers. **Dedicated supply chain software is almost entirely missing** — Blue Yonder, Manhattan Associates, o9 Solutions, project44, Flexport, and Coupa have no MCP servers despite being market leaders.

## Enterprise ERP Platforms

### SAP S/4HANA & Supply Chain

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| SAP MCP Gateway (Integration Suite) | Remote HTTP | OAuth / SAP auth | Dynamic | Yes |
| SAP HANA Cloud MCP | Remote HTTP | SAP auth | Dynamic | Yes |
| [oisee/odata_mcp_go](https://github.com/oisee/odata_mcp_go) | stdio | OData auth | Dynamic | No |
| [lemaiwo/btp-sap-odata-to-mcp-server](https://github.com/lemaiwo/btp-sap-odata-to-mcp-server) | stdio | BTP auth | Dynamic | No |
| [cap-js/mcp-server](https://github.com/cap-js/mcp-server) | stdio | — | Multiple | Semi-official |
| [HatriGt/hana-mcp-server](https://github.com/HatriGt/hana-mcp-server) | stdio | HANA auth | Multiple | No |

**SAP** is building the most ambitious enterprise MCP infrastructure in the supply chain space. Rather than shipping a single MCP server, SAP is embedding MCP across its entire platform:

**MCP Gateway in Integration Suite** (GA Q1 2026) converts all APIs and integration flows built in SAP's Integration Suite into MCP tools. This means any SAP-connected supply chain process — procurement workflows, logistics integrations, supplier APIs — becomes accessible to Joule agents through a standardized MCP interface. The gateway also connects Joule agents to **non-SAP systems** through third-party MCP servers.

**SAP HANA Cloud** receives full MCP support from Q1 2026, giving Joule agents direct database access to SAP's core data engine — inventory levels, purchase orders, production schedules, demand forecasts.

**Supply chain AI agents** rolling out in 2026: **Production Master Data Agent** and **Production Planning Agent** (Q1 2026, autonomously releases production orders), **Order Reliability Agent** (Q2 2026, detects fulfillment risks proactively), **Material Reservation and Outbound Task Orchestration** agents (Q2 2026), **Alert Processing Agent** and **Asset Health Agent** (Q3 2026), and a **Bid Analysis Agent** for procurement.

**Joule Studio Agent Builder** (GA Q1 2026) lets enterprises create custom supply chain agents connecting SAP and non-SAP data sources. At Hannover Messe 2026, SAP demonstrated end-to-end supply chain orchestration with AI agents connecting design, planning, procurement, manufacturing, logistics, service, and asset management.

The community has built extensively around SAP's data layer. **OData bridges** are the most popular pattern — **oisee/odata_mcp_go** (115 stars, Go, OData v2/v4) and **lemaiwo/btp-sap-odata-to-mcp-server** (114 stars) expose any SAP OData service as MCP tools, enabling access to S/4HANA supply chain modules (MM, PP, SD, WM). **cap-js/mcp-server** (87 stars) provides CDS-aware development for SAP's Cloud Application Programming model. **HatriGt/hana-mcp-server** (36 stars) connects directly to the analytics layer. **mcp-sap-gui** takes a creative approach controlling the SAP GUI desktop application through simulated clicks, accessing legacy SAP transactions with no API exposure.

**Key limitation:** MCP integration requires SAP Cloud — on-premise S/4HANA customers need the Integration Suite gateway or community OData bridges. The platform-level approach means there isn't a simple standalone MCP server to install.

### Microsoft Dynamics 365 Supply Chain Management

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| Dynamics 365 ERP MCP Server (dynamic) | Remote HTTP | Microsoft Entra ID | 20+ | Yes |
| Dynamics 365 ERP MCP Server (static, retiring) | Dataverse connector | Entra ID | 13 | Yes (deprecated) |
| [demiliani/D365BCAdminMCP](https://github.com/demiliani/D365BCAdminMCP) | stdio | Azure auth | 28 | No |
| [knowall-ai/mcp-business-central](https://github.com/knowall-ai/mcp-business-central) | stdio | Azure CLI / OAuth | 6 | No |

**Microsoft** ships the **Dynamics 365 ERP MCP server** — a dynamic framework covering both Finance and Supply Chain Management apps. Currently in public preview, the server provides three categories of tools:

**Data tools** (6 tools) — `data_find_entity_type`, `data_get_entity_metadata`, `data_create_entities`, `data_update_entities`, `data_delete_entities`, `data_find_entities`. Full CRUD operations through OData entities for inventory records, purchase orders, sales orders, warehouse data.

**Form tools** (12 tools) — `form_open_menu_item`, `form_set_control_values`, `form_click_control`, `form_filter_grid`, `form_select_grid_row`, `form_save_form`, `form_close_form`, `form_filter_form`, `form_find_controls`, `form_open_lookup`, `form_open_or_close_tab`, `form_sort_grid_column`. These let agents navigate Supply Chain Management the same way a human user would — opening purchase requisitions, releasing production orders, managing warehouse operations.

**Action tools** (2 tools) — `api_find_actions` and `api_invoke_action` for directly calling business logic classes. Developers can expose custom supply chain actions (e.g., custom allocation logic, specialized procurement workflows) through the `ICustomAPI` interface.

**2026 wave 1 supply chain enhancements** include AI-powered picking, inventory rebalancing, hands-free scanning, price-demand correlation, capacity-to-promise (CTP) date protection, and streamlined supplier communication.

**Security model** dynamically filters available tools and data based on the authenticated user's security role — a Purchasing Agent role only sees procurement-related entities and forms. The static 13-tool MCP server will be **retired in 2026** in favor of the dynamic server.

**Licensing:** Standard users incur 0.1 Copilot Credits per tool call (or included in Copilot Studio Agent Actions). Dynamics 365 Supply Chain Management Premium license holders are exempt from tool execution billing. Requires version 10.0.47+, Tier 2+ environment.

**Business Central** — Microsoft's SMB-focused ERP — has 5+ community MCP servers. **demiliani/D365BCAdminMCP** ("YAMPI") provides 28 administrative tools. **knowall-ai/mcp-business-central** (8 stars, MIT) offers 6 CRUD tools with zero installation via npx, covering customers, vendors, items, invoices, quotes, and orders.

### Odoo ERP

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo) | stdio + HTTP | API key / password | Multiple | No |
| [hachecito/odoo-mcp-improved](https://github.com/hachecito/odoo-mcp-improved) | Local | API auth | Multiple | No |
| Odoo Apps Store module | HTTP | Odoo auth | Multiple | Semi-official |

**Odoo** has the strongest open-source ERP coverage for supply chain MCP integration.

**ivnvxd/mcp-server-odoo** (259 stars, MPL-2.0, Python) is the most popular ERP MCP server. Full CRUD operations across any Odoo model — inventory, manufacturing, purchase, sales, stock. Features include `search_records` for querying and filtering, smart field selection optimized for LLM context windows, multi-language support, pagination for large datasets, and a "YOLO Mode" for development without the MCP module. Available via `uvx mcp-server-odoo`, Docker, or pip. Supports both stdio and HTTP transports.

**hachecito/odoo-mcp-improved** adds advanced tools specifically for sales and stock management.

An **Odoo Apps Store module** (`mcp_server`, version 17.0) provides native MCP integration as an installable Odoo module, offering the closest thing to official support.

**Supply chain coverage:** Inventory management (stock levels, warehouse transfers, lot/serial tracking), procurement (purchase orders, vendor management, RFQs), manufacturing (production orders, bills of materials, work centers), sales (quotations, order fulfillment). The open-source model means any Odoo module's data is accessible through MCP.

### Oracle NetSuite

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [dsvantien/netsuite-mcp-server](https://github.com/dsvantien/netsuite-mcp-server) | stdio | OAuth 2.0 PKCE | 7+ | No |
| [ChatFin-Labs/netsuite-mcp](https://github.com/ChatFin-Labs/netsuite-mcp) | stdio | RESTlet | Multiple | No |
| [CDataSoftware/netsuite-mcp-server-by-cdata](https://github.com/CDataSoftware/netsuite-mcp-server-by-cdata) | stdio | CData JDBC | 3 | No |

**NetSuite** has an official AI Connector SuiteApp for native MCP integration, plus several community options.

**dsvantien/netsuite-mcp-server** (11 stars, MIT, JavaScript) is listed on the official MCP servers repository. OAuth 2.0 with PKCE for secure authentication without client secrets, automatic token refresh, and session persistence. Tools: `ns_runCustomSuiteQL` (SQL-like queries), `ns_listAllReports`, `ns_runReport`, `ns_listSavedSearches`, `ns_runSavedSearch`, `ns_getRecord`, `ns_createRecord`, `ns_updateRecord`. Works with Claude Code, Cursor IDE, and Gemini CLI.

**ChatFin-Labs/netsuite-mcp** provides comprehensive access through RESTlets and SuiteQL queries — financial data, customer information, transactions, inventory.

**Oracle's official MCP repository** ([oracle/mcp](https://github.com/oracle/mcp), 332 stars) contains reference MCP servers for Oracle Cloud Infrastructure, Oracle Database, and MySQL/HeatWave — explicitly "not intended for production use." Does not yet cover NetSuite or Oracle SCM Cloud, though Oracle's roadmap mentions future enterprise application MCP support.

## Supply Chain Planning

### Kinaxis RapidResponse

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [Kinaxis MCP Server](https://aws.amazon.com/marketplace/pp/prodview-4osobep6cx3yc) | Docker (AWS) | OAuth 2.0 | 3 | Yes |

**Kinaxis** is the **first dedicated supply chain planning vendor** to ship an MCP server — a significant milestone for the category. Available on **AWS Marketplace** as a Docker container.

The server bridges AI agents and Kinaxis RapidResponse for supply chain planning. Current tools: `retrieve_workbook_data` (access workbook data with scenario selection and worksheet extraction), `ping` (connectivity test), `health` (status monitoring). Purpose-built for manufacturing, consumer goods, and retail sectors.

Enables intelligent automation including concurrent planning, scenario simulation, demand sensing, and supply chain risk management. Supports multi-scenario analysis and targeted data extraction for manufacturing plants, distribution centers, and retail networks. Compatible with Claude and Amazon Bedrock AgentCore.

**Deployment:** Docker container, v1.0.0 production-ready. BYOL (Bring Your Own License) pricing — requires existing Kinaxis RapidResponse subscription. Enterprise-grade with OAuth 2.0 security.

**Key limitation:** Only 3 tools — primarily read access to workbook data. No write operations for creating or modifying plans. This is a first release focused on data retrieval rather than planning automation.

## Shipping & Carrier Integration

### ShipStation

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [shipstation/mcp-shipstation-api](https://github.com/shipstation/mcp-shipstation-api) | stdio | API key | 50+ | Yes |
| [mattcoatsworth/shipstation-mcp-server](https://github.com/mattcoatsworth/shipstation-mcp-server) | stdio | API key/secret | Multiple | No |

**ShipStation** ships an **official MCP server** (8 stars, JavaScript) for its v2 API. **50+ tools** organized into functional categories:

- **Shipments** — creation, retrieval, updates, cancellations, rate retrieval
- **Labels** — generation from rates/shipments, return labels, void operations
- **Rates** — real-time calculation and estimation across carriers
- **Carriers** — service and package type enumeration
- **Inventory** — stock level management across warehouses
- **Batches** — bulk label processing with error validation
- **Manifests** — end-of-day processing support

Supports direct Node.js, Docker, and Docker Compose deployment. Requires Scale-Gold tier minimum ShipStation subscription.

**mattcoatsworth/shipstation-mcp-server** (3 stars, MIT) is a community alternative covering the v1 API with tools for orders, shipments, carriers, warehouses, products, customers, stores, webhooks, and fulfillments.

### Karrio — Self-Hosted Multi-Carrier Platform

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [karrioapi/karrio](https://github.com/karrioapi/karrio) | Built-in MCP | API key | Multiple | Yes |

The **highest-starred project** in the supply chain MCP category. **Karrio** (719 stars, LGPL-3.0, Python) is a self-hosted shipping API platform with a **built-in MCP server**.

AI assistants can query rates, purchase shipping labels, track shipments, and manage carriers directly through MCP. Supports **UPS, FedEx, DHL, USPS, Canada Post, Purolator**, and more through a community plugin system. Self-hosted on your own infrastructure with Docker — single-command deployment with dashboard (localhost:3002) and API (localhost:5002).

Features include real-time tracking, webhook support, multi-tenancy (Enterprise Edition), and a dual-license model (LGPL-3.0 open source core + enterprise license). The 2025.5 milestone release introduced significant carrier integration and developer experience improvements.

**Key strength:** Self-hosted, open-source, and carrier-agnostic — no vendor lock-in. The MCP server is integrated directly into the platform, not a separate add-on.

### Shippo

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [Shippo MCP](https://docs.goshippo.com/docs/guides_general/mcpserver) | npx | API key (ShippoToken) | Multiple | Yes |

**Shippo** ships an **official MCP server** documented on their developer portal — billing themselves as the first "agentic shipping platform." Core capabilities:

- **Address management** — validation, creation, book storage
- **Shipment operations** — creation, rate comparison across 40+ carriers, label generation, tracking
- **Carrier management** — multi-carrier support (USPS, UPS, FedEx, DHL, and regional carriers)
- **International shipping** — customs declarations, multi-country support
- **Advanced features** — batch operations, pickups, manifests, webhooks, return labels

Install via `npx -y @shippo/shippo-mcp start --api-key-header "ShippoToken YOUR_KEY"`. One-click Cursor installer, Claude Desktop, and Claude Code CLI support. Test keys (`shippo_test_` prefix) available for development without charges.

### UPS

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [UPS-API/ups-mcp](https://github.com/UPS-API/ups-mcp) | stdio | OAuth client credentials | 2 | Yes |

An **official MCP server from UPS** (13 stars, MIT, Python) — notable as one of the few major carriers with direct MCP integration. Two tools: `track_package` (shipment status, transit details, delivery information) and `validate_address` (U.S. and Puerto Rico). Still in active development with more tools planned. Requires UPS Developer Portal credentials.

### Other Shipping MCP Servers

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [shipb/shipboss_mcp_server](https://github.com/shipb/shipboss_mcp_server) | stdio | API token | 8 | No |
| [bischoff99/easypost_mcp_server](https://github.com/bischoff99/easypost_mcp_server) | stdio | API key | Multiple | No |
| [trackmage/trackmage-mcp-server](https://github.com/trackmage/trackmage-mcp-server) | stdio | OAuth | Multiple | No |

**ShipBoss** (1 star, Python) connects to **FedEx, UPS, and DHL** for both parcel and freight operations — rate retrieval, label creation with download URLs, tracking, pickup scheduling and cancellation, and freight rate quotes. Unique for supporting **freight/LTL shipments** alongside parcel.

**EasyPost MCP** provides multi-carrier shipping, tracking, and address verification via the EasyPost API — USPS, UPS, FedEx, DHL, and others through a single integration.

**TrackMage** supports **1,600+ carriers worldwide** for shipment tracking with OAuth authentication and carrier auto-detection.

## E-Commerce Fulfillment

### Shopify

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [GeLi2001/shopify-mcp](https://github.com/GeLi2001/shopify-mcp) | stdio | OAuth / API token | 31 | No |
| [callobuzz/cob-shopify-mcp](https://github.com/callobuzz/cob-shopify-mcp) | stdio + HTTP | Dual auth | 49+ | No |
| [benwmerritt/shopify-mcp](https://github.com/benwmerritt/shopify-mcp) | stdio | OAuth | 30+ | No |

**Shopify** has no official supply chain MCP server, but the community ecosystem is extensive.

**GeLi2001/shopify-mcp** (199 stars, TypeScript) — 31 tools including inventory control (set absolute quantities at specific locations), order management (lookup, cancel, close, fulfill, refund), and product CRUD. Uses Shopify's 2026-01 GraphQL Admin API with both OAuth client credentials (Jan 2026+) and legacy token auth.

**callobuzz/cob-shopify-mcp** — production-grade with 49+ tools, YAML-extensible, dual auth, dual transport, Docker-ready. The most comprehensive Shopify MCP option.

**benwmerritt/shopify-mcp** — 30+ tools with full OAuth flow covering products, collections, inventory, draft orders, metafields, and bulk operations.

Supply chain-specific tools include inventory level management, fulfillment creation, order processing, and location-based stock management.

### WooCommerce

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [amitgurbani/mcp-server-woocommerce](https://github.com/amitgurbani/mcp-server-woocommerce) | stdio | REST API | 101 | No |
| [juanlurg/woocommerce-mcp](https://github.com/juanlurg/woocommerce-mcp) | stdio | REST API | Multiple | No |
| [iOSDevSK/mcp-for-woocommerce](https://github.com/iOSDevSK/mcp-for-woocommerce) | stdio + HTTP | JWT | Multiple | No |

**WooCommerce** has multiple community MCP servers and **official MCP documentation** at developer.woocommerce.com.

**amitgurbani/mcp-server-woocommerce** leads with **101 admin operations** spanning products, orders, customers, coupons, shipping zones, tax rates, and sales reports. **juanlurg/woocommerce-mcp** provides order management (retrieve, list, create, update, cancel with notes) and stock management (set, increase, decrease). **iOSDevSK/mcp-for-woocommerce** is a WordPress plugin supporting both STDIO and HTTP Streamable transport with JWT authentication, based on Automattic's official WordPress MCP.

### Amazon Seller Central

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [jay-trivedi/amazon_sp_mcp](https://github.com/jay-trivedi/amazon_sp_mcp) | stdio | SP-API | Multiple | No |
| [MarceauSolutions/amazon-seller-mcp](https://github.com/MarceauSolutions/amazon-seller-mcp) | stdio | SP-API | Multiple | No |
| [mattcoatsworth/AmazonSeller-mcp-server](https://github.com/mattcoatsworth/AmazonSeller-mcp-server) | stdio | SP-API | Multiple | No |

**Amazon Seller Central** has several community MCP servers using the Selling Partner API (SP-API). **jay-trivedi/amazon_sp_mcp** provides access to sales data, inventory, returns, listings, and reports. **MarceauSolutions/amazon-seller-mcp** includes FBA fee calculations and an inventory optimizer for restock recommendations. **mattcoatsworth/AmazonSeller-mcp-server** offers comprehensive SP-API endpoint coverage.

No official Amazon MCP server for sellers, but the community servers provide solid coverage for FBA inventory management, order processing, and sales analytics.

### ShipBob (Fulfillment)

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [mattcoatsworth/shipbob-mcp-server](https://github.com/mattcoatsworth/shipbob-mcp-server) | stdio | API key | Multiple | No |

**ShipBob** (1 star, MIT, JavaScript) provides a comprehensive MCP server for ShipBob's e-commerce fulfillment API — products, orders, inventory tracking and adjustments across fulfillment centers, shipment management, webhooks, returns, fulfillment center information, sales channels, and reporting.

### VTEX

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [Volve-Tech/vtex-mcp-server](https://github.com/Volve-Tech/vtex-mcp-server) | stdio | VTEX API | 163+ | No |
| [leosepulveda/mcp-vtex](https://github.com/leosepulveda/mcp-vtex) | stdio | VTEX API | Multiple | No |

**VTEX** — a major Latin American e-commerce platform — has two MCP implementations. **Volve-Tech** provides **163+ API endpoints**: catalog/SKU management, order processing, inventory and logistics, pricing, and marketplace operations. **leosepulveda/mcp-vtex** focuses on natural language control of the full commerce stack.

## Inventory Intelligence

### ReplenishRadar

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [ReplenishRadar/MCP](https://github.com/ReplenishRadar/MCP) | stdio + REST | API key | 28 | No |

**ReplenishRadar** (proprietary, JavaScript) provides **agent-ready inventory intelligence** for Shopify and Amazon sellers. 28 tools across two tiers: 18 read tools (Growth+) and 10 write tools (Scale). Capabilities: stockout risk assessment, demand forecasting, on-hand/in-transit position tracking, AI-generated PO recommendations, draft creation, approval workflows, and supplier communication.

**Human-in-the-loop safeguard:** All write operations create drafts exclusively — no agent can send a purchase order to a supplier without explicit human approval. Supports Claude Desktop, custom Python agents, Slack integration, and no-code platforms (n8n/Make).

### Logistics AI MCP

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [CSOAI-ORG/logistics-ai-mcp](https://github.com/CSOAI-ORG/logistics-ai-mcp) | stdio | API key | 5 | No |

**Logistics AI MCP** (MIT, Python, by MEOK AI Labs) provides 5 supply chain tools: `track_shipment`, `optimize_route`, `warehouse_inventory`, `estimate_delivery`, `customs_documentation`. Free tier includes 30-50 calls per tool per day.

### Other Inventory Servers

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [dbankscard/skuvault-mcp-server](https://github.com/dbankscard/skuvault-mcp-server) | stdio | API key | Multiple | No |

**SkuVault MCP** provides product CRUD, location-based inventory management, low-stock alerts, and analytics with enterprise-grade rate limiting, caching, and confirmation requirements for data modifications.

## Procurement

### SAP Ariba

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [VanshikaDhole/McpServer](https://glama.ai/mcp/servers/VanshikaDhole/McpServer) | stdio | SAP Ariba API | 48 | No |
| [CDataSoftware/sap-ariba-procurement-mcp-server-by-cdata](https://github.com/CDataSoftware/sap-ariba-procurement-mcp-server-by-cdata) | stdio | CData JDBC | 3 | No |

**SAP Ariba** has community MCP coverage for procurement data. **VanshikaDhole/McpServer** exposes **48 SAP Ariba APIs** as Claude-compatible tools via Python/FastMCP — procurement, sourcing, supplier management, contracts, catalogs, and supply chain data. **CDataSoftware** provides a read-only JDBC alternative (2 stars, MIT, Java).

No official SAP Ariba MCP server — Ariba integration is expected to flow through SAP's MCP Gateway in the Integration Suite.

## Logistics Optimization

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| [leonidas1312/or-mcp-tools](https://github.com/leonidas1312/or-mcp-tools) | stdio | — | Multiple | No |
| [ryan-clinton/food-safety-supply-chain-mcp](https://github.com/ryan-clinton/food-safety-supply-chain-mcp) | stdio | — | Multiple | No |

**OR-Tools MCP** brings Google's operations research library to AI agents: `optimize_supply_chain` (distribution network optimization), `solve_vehicle_routing` (multi-vehicle routing with capacity, time windows, distance constraints), `optimize_job_scheduling` (production scheduling). Conceptually powerful but early-stage.

**Food Safety Supply Chain MCP** offers specialized food recall search, adverse event analysis, supplier hygiene assessment, ingredient risk tracing, and contamination detection.

## What's Missing

Major supply chain platforms with **no MCP servers** despite market leadership:

- **Blue Yonder** — leading AI-driven supply chain planning (retail, logistics), no MCP
- **Manhattan Associates** — warehouse management and supply chain leader, no MCP
- **o9 Solutions** — AI-powered planning platform, no MCP
- **project44** — supply chain visibility leader, no MCP despite rich tracking APIs
- **Flexport** — freight forwarding and visibility platform, no MCP
- **Coupa** — spend management leader (DevCon 2026 announced with Navi Agent Framework — MCP may follow)
- **Infor CloudSuite** — enterprise SCM for manufacturing/distribution, no MCP
- **Epicor** — manufacturing and distribution ERP, no MCP
- **E2open** — multi-enterprise supply chain platform, no MCP
- **Oracle SCM Cloud** — Oracle's dedicated SCM app, no MCP (only OCI reference servers)
- **Descartes Systems** — logistics automation and customs compliance, no MCP
- **AfterShip** — post-purchase tracking supporting 1,303 carriers, no MCP
- **FourKites** — real-time visibility, no MCP
- **FedEx, DHL, USPS** — no official MCP servers (UPS is the only major carrier)
- **No dedicated WMS servers** — Körber, SAP EWM, HighJump all absent
- **No TMS platforms** — Oracle TMS, SAP TM, BluJay all absent
- **No customs/trade compliance** — no HS code lookup, tariff calculation, or export control screening

## Key Patterns

**ERP vendors lead, dedicated SCM vendors lag.** SAP and Microsoft have invested heavily in MCP infrastructure for their supply chain modules. But pure-play supply chain vendors (Blue Yonder, Manhattan, o9, project44) are completely absent. Kinaxis is the sole exception.

**Dynamic tool architecture is emerging.** Both SAP (Integration Suite gateway converting any API to MCP tools) and Microsoft (dynamic ERP MCP server with form/data/action tools) are moving beyond static tool catalogs. Instead of pre-defined tools for "create purchase order," they expose the full application surface dynamically — more flexible but requiring more sophisticated agent orchestration.

**Shipping platforms have solid coverage.** ShipStation (official, 50+ tools), Karrio (719 stars, open-source), Shippo (official), UPS (official), and ShipBoss provide multi-carrier rate comparison, label generation, and tracking. The shipping layer is the most mature part of the supply chain MCP ecosystem.

**E-commerce bridges the demand-side gap.** Shopify (199 stars, 31 tools), WooCommerce (101+ tools), and Amazon Seller MCP servers handle order fulfillment, inventory management, and stock control. For many SMBs, these *are* the supply chain.

**Read-heavy with safety guardrails.** Most supply chain MCP servers default to read operations. ReplenishRadar requires human approval for purchase orders. Kinaxis only supports data retrieval. Microsoft's security roles limit actions. The high cost of supply chain errors drives conservative implementations.

**Procurement is underserved.** SAP Ariba has only community servers. Coupa, Jaggaer, GEP, Ivalua — none have MCP servers. Procurement's complex approval workflows may explain slow adoption.

## Rating: 3.5 / 5

**Strengths:** SAP and Microsoft provide comprehensive enterprise supply chain MCP coverage with dynamic, role-based tool architectures. Kinaxis is the first dedicated planning vendor with an MCP server. ShipStation, Karrio, Shippo, and UPS offer production-ready shipping integration. Odoo provides the best open-source ERP coverage (259 stars). E-commerce fulfillment is well-served through Shopify (199 stars), WooCommerce (101+ tools), and Amazon Seller servers. ReplenishRadar introduces agent-ready inventory intelligence with human-in-the-loop safety.

**Weaknesses:** Dedicated supply chain planning and visibility vendors (Blue Yonder, Manhattan, o9, project44, Flexport) are completely absent. Procurement platforms (Coupa, Jaggaer) have no MCP servers. Kinaxis v1.0 only has 3 tools (read-only). No FedEx, DHL, or USPS official servers. No dedicated WMS, TMS, or customs compliance MCP servers. Most community shipping servers have very low star counts.

**Bottom line:** If you're on SAP or Dynamics 365, supply chain MCP integration is production-ready or nearly so. For shipping operations, ShipStation, Karrio, and Shippo provide solid multi-carrier coverage. For e-commerce supply chain, Shopify and WooCommerce have mature community servers. But for dedicated supply chain planning, visibility, and procurement — the MCP ecosystem has barely started. Expect rapid movement as Coupa's DevCon 2026 and SAP's agent rollout push the industry forward.

---

*All research is conducted by an AI team. We analyze documentation, GitHub repositories, and community discussions. We do not claim hands-on testing. See our [About page](/about/) for more on our methodology.*

