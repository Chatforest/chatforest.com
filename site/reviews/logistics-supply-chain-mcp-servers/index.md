# Logistics & Supply Chain MCP Servers — Shipping, Fleet Tracking, Inventory Management, and Maritime Intelligence

> Logistics and supply chain MCP servers are a maturing category with 30+ servers across 6 subcategories.


Logistics and supply chain MCP servers let AI assistants manage shipping operations, track fleets, control inventory, and monitor maritime vessel movements. Instead of logging into separate carrier portals, warehouse systems, and tracking platforms, these servers let AI agents handle logistics workflows through the Model Context Protocol.

This review covers the **logistics and supply chain** vertical — shipping and parcel management, inventory and warehouse operations, fleet telematics, and maritime tracking. For e-commerce platforms that include some shipping features, see our [E-Commerce MCP review](/reviews/ecommerce-shopping-mcp-servers/). For general business operations, see our [Business & Productivity MCP review](/reviews/erp-business-management-mcp-servers/).

The headline findings: **Karrio emerges as the open-source shipping leader** with 720 stars, 50+ carriers, and built-in MCP. **Shippo expands into full agentic operations** with returns, WISMO, analytics, and batch processing. **TrackMage scales tracking to 1,600+ carriers.** **ReplenishRadar brings AI-native inventory intelligence** with stockout risk and demand forecasting for Shopify/Amazon. **Enterprise procurement gets its first MCP bridge** via SAP Ariba through CData. **Oracle Integration becomes an MCP tools provider**, opening enterprise SCM workflows to AI agents. **eBay MCP hit by CVE-2026-27203** (CVSS 8.3, unpatched).

## Shipping & Parcel Management

### Shippo MCP (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Shippo MCP](https://goshippo.com/mcp) | — | TypeScript | — | Multiple |

The **first agentic shipping platform** — Shippo's official MCP server exposes their full shipping API through the Model Context Protocol:

- **Rate shopping** — compare shipping rates across USPS, UPS, FedEx, DHL, and dozens of other carriers
- **Label generation** — purchase and generate shipping labels programmatically
- **Package tracking** — monitor shipment status and location across carriers
- **Address validation** — verify shipping addresses before label creation
- **Customs declarations** — handle international shipping documentation
- **Carrier management** — manage multiple carrier accounts through a single integration

Install via `npx -y @shippo/shippo-mcp start` with your Shippo API key. This is significant because Shippo is a well-funded shipping infrastructure company (valued at $1B+) — this isn't a hobbyist wrapper but a commercially-backed agentic interface to real shipping operations. Natural language prompts translate directly into shipping actions.

**April 2026 update:** Shippo has expanded well beyond label generation into a full agentic shipping operations platform. New capabilities include **automated returns** (prepaid labels, validated addresses, customer updates without manual work), **WISMO inquiry handling** (AI agents answer "where is my order" questions), **proactive tracking updates**, **batch processing** for multiple shipments, **pickup scheduling**, **end-of-day manifest generation**, and **shipping analytics** (delivery trends, spend distribution across carriers). Both retailers and platform customers are actively experimenting with conversational rate shopping and automated returns workflows.

### karrioapi/karrio

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [karrioapi/karrio](https://github.com/karrioapi/karrio) | 720 | Python | LGPL-3.0 | Multiple |

The **open-source multi-carrier shipping leader** — Karrio is a self-hosted programmable shipping API with a built-in MCP server supporting **50+ carriers** worldwide:

- **Rate shopping** — query and compare shipping rates across FedEx, UPS, DHL, USPS, Canada Post, and dozens of regional carriers
- **Label generation** — purchase shipping labels programmatically
- **Shipment tracking** — real-time tracking across all connected carriers
- **Carrier management** — manage carrier accounts and connections through a single platform
- **Self-hosted** — deploy on your own infrastructure with full data control

What makes Karrio significant is the combination of scale and openness. With 720 stars, 235 releases, and active development (v2026.1.29 as of April 2026), this is the most mature open-source shipping platform with MCP support. The dual license (LGPL-3.0 for open-source, enterprise license for commercial features) means organizations can start free and upgrade as needed.

Install via `npx karrio-mcp` with your Karrio API key and URL. Works with Claude, Cursor, and Windsurf.

### trackmage/trackmage-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [trackmage/trackmage-mcp-server](https://github.com/trackmage/trackmage-mcp-server) | 2 | JavaScript | MIT | 10 |

A **universal shipment tracking server** supporting **1,600+ carriers worldwide** through the TrackMage API:

- **Shipment management** — create, update, list shipments, get checkpoints, retrack
- **Order management** — create, update, list orders
- **Carrier detection** — auto-detect carrier from tracking number, list available carriers
- **OAuth authentication** — client credentials flow

The 1,600+ carrier coverage is the broadest of any logistics MCP server — useful for businesses shipping internationally across many regional carriers. Docker deployment available.

### markswendsen-code/mcp-fedex

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markswendsen-code/mcp-fedex](https://github.com/markswendsen-code/mcp-fedex) | — | TypeScript | MIT | 4 |

A community **FedEx MCP server** using Playwright browser automation:

- Track packages with full event history
- Get shipping rate estimates between zip codes with transit times
- Find nearby FedEx Office stores and drop-off points
- Schedule pickups at residential or business addresses

Note: uses browser automation rather than official FedEx APIs, which may be less reliable but doesn't require FedEx developer credentials.

### theYahia/correios-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [theYahia/correios-mcp](https://github.com/theYahia/correios-mcp) | — | TypeScript | MIT | 8 |

An MCP server for **Brazil's Correios** postal service — the first dedicated Latin American shipping MCP:

- Package tracking, shipping cost calculations, delivery time estimates
- Service listings, ZIP code lookups
- Shipment creation, label generation, cancellation

Valuable for businesses with Brazilian e-commerce operations needing AI-powered access to Correios logistics.

### UPS-API/ups-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [UPS-API/ups-mcp](https://github.com/UPS-API/ups-mcp) | 4 | Python | MIT | Multiple |

**UPS's official MCP server** — one of the world's largest carriers providing first-party AI agent integration:

- Track shipment status, transit events, and expected delivery dates
- Get shipping rates and service options
- Access UPS logistics capabilities through AI agents

Still in active development — the tool count and feature set are evolving. The significance is the official backing: this comes from UPS-API, UPS's own GitHub organization, not a community scraper. Requires UPS API credentials.

### bfrs/shiprocket-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bfrs/shiprocket-mcp](https://github.com/bfrs/shiprocket-mcp) | — | TypeScript | — | Multiple |

An MCP server for **Shiprocket**, India's leading e-commerce shipping platform:

- Check best and fastest serviceable courier partners based on city or pincodes
- Compare shipping rates across courier partners
- Create, update (single or bulk), and cancel orders
- Ship orders directly through the platform
- Track orders using AWB number, Shiprocket Order ID, or Source Order ID

Connects to your personal Shiprocket account via email and password. Particularly valuable for Indian e-commerce businesses that rely on Shiprocket for domestic and international shipping across India's fragmented courier landscape.

### bischoff99/easypost_mcp_server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bischoff99/easypost_mcp_server](https://github.com/bischoff99/easypost_mcp_server) | — | TypeScript | — | Multiple |

Wraps the **EasyPost API** for multi-carrier shipping abstraction:

- Rate comparison across USPS, UPS, FedEx, DHL, and many other carriers
- Label purchase and generation
- Package tracking across carriers
- Address verification

EasyPost's value proposition is a single API for dozens of carriers — the MCP server inherits that advantage. EasyPost API key required.

## Inventory & Warehouse Management

### dbankscard/skuvault-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dbankscard/skuvault-mcp-server](https://github.com/dbankscard/skuvault-mcp-server) | — | Python | — | Multiple |

A **production-ready MCP server** for SkuVault inventory management — the most enterprise-grade logistics MCP server we've reviewed:

- **Product management** — create, read, update products individually or in batches
- **Inventory control** — add, remove, and set inventory quantities across warehouses
- **Warehouse operations** — list warehouses and manage inventory by location
- **Smart analytics** — active/inactive products, low stock alerts, inventory summaries

What sets this apart is the engineering: dynamic rate limit learning with exponential backoff, intelligent response caching to minimize API calls, confirmation requirements for all mutating operations (no accidental inventory adjustments), comprehensive input validation, and connection pooling with request queuing. This is designed for real warehouse operations where a bad API call could mean shipping the wrong products.

Built for Claude Desktop. Requires SkuVault tenant and user tokens.

### YosefHayim/ebay-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [YosefHayim/ebay-mcp](https://github.com/YosefHayim/ebay-mcp) | — | TypeScript | — | 325 |

The **largest MCP server by tool count** in the logistics space — 325 tools covering eBay's entire Sell API:

- Inventory management — product listings, stock levels, variants
- Order fulfillment — order processing, shipping, returns
- Marketing campaigns — promotions, ads, deals
- Analytics — sales data, traffic, performance metrics
- Developer tools — API diagnostics, webhook management

The sheer breadth is extraordinary. For eBay sellers who manage significant inventory, this provides AI-powered access to virtually every seller operation. The trade-off is complexity — 325 tools means the AI agent needs good context to pick the right one.

**⚠️ Security advisory (April 2026):** [CVE-2026-27203](https://www.cvedetails.com/cve/CVE-2026-27203/) (CVSS 8.3 High) affects all versions up to 1.7.2. The `ebay_set_user_tokens` tool allows environment variable injection via the `updateEnvFile` function in `src/auth/oauth.ts`, which doesn't validate inputs for newlines or quotes. Attackers can inject arbitrary environment variables, potentially hijacking OAuth flows, causing denial of service, or achieving remote code execution via `NODE_OPTIONS` injection. **No patch is available yet.** Use with caution in production environments.

### ReplenishRadar/MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ReplenishRadar/MCP](https://github.com/ReplenishRadar/MCP) | — | JavaScript | Proprietary | 28 |

**AI-native inventory intelligence** for Shopify and Amazon sellers — 28 tools split across 18 read and 10 write operations:

- **Stockout risk analysis** — identify products at risk of going out of stock
- **Demand forecasting** — AI-powered demand predictions
- **Purchase order management** — create, update, approve, send, cancel POs
- **Sales analytics** — top sellers, slow movers, lost sales, inventory value
- **SKU health scoring** — comprehensive product health assessment
- **Supplier management** — list suppliers, manage vendor relationships

The safety design is noteworthy: all write operations create **drafts only** — no AI agent can send purchase orders without human approval. This is the kind of guardrail that makes inventory automation production-safe. Commercial product with API key required.

### bigl34/inflow-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bigl34/inflow-mcp-server](https://github.com/bigl34/inflow-mcp-server) | 1 | TypeScript | MIT | 50+ |

A comprehensive MCP server for **inFlow Inventory** — 50+ tools across multiple categories:

- **Product management** — listing, searching, creating, updating products
- **Sales and purchase orders** — full order lifecycle management
- **Customer and vendor records** — CRM-like capabilities within inventory context
- **Inventory operations** — adjustments, transfers, counts, manufacturing orders
- **Reference data** — locations, categories, pricing, tax information
- **Webhooks** — subscription support for real-time event notifications

Features token bucket rate limiting, automatic retry with exponential backoff, and filtering/pagination/sorting across list operations. Requires Node.js 18+ and an active inFlow subscription with API access.

### Other Inventory Servers

- **Agiliron MCP Server** — connects to Agiliron's inventory management and multi-channel retail POS system
- **BoxHero MCP Server** — simpler inventory management with an "inventory reinvented" approach
- **git-laks/inventorymanagement** — full-stack inventory tracking with Python FastAPI backend and React frontend, MCP server for AI agent interaction

## Fleet Management & Telematics

### gperezt222/flespi-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gperezt222/flespi-mcp-server](https://github.com/gperezt222/flespi-mcp-server) | — | TypeScript | — | 157 |

A massive **157-tool MCP server** for the Flespi telematics platform — auto-generated from the complete Flespi API:

- Fleet management and vehicle tracking
- IoT device management for 1,000+ device types
- Telemetry data processing and analysis
- Channel and stream management
- Plugin and calculator configuration

Fully MCP v1.0 compliant with Zod validation for all inputs. The Flespi platform supports GPS trackers from Teltonika, Queclink, Concox, and hundreds of other manufacturers — this server gives AI agents access to that entire ecosystem. Requires a Flespi API token.

The auto-generation approach means comprehensive coverage but potentially overwhelming tool selection. Best suited for organizations already using Flespi for fleet management who want to add AI agent capabilities.

**April 2026 update:** Flespi has expanded its AI ecosystem significantly. The platform now offers **Codi AI** with real-time processing transparency (animated popups showing data gathering in progress), **REST API tools and MCP servers** for Claude Code, Cursor, and other AI-powered IDEs, and **Agent Skills** following the machine-readable SKILL.md specification for token-efficient platform bootstrapping. Codi's intelligence now scales with subscription tier, from basic assistance (Free) to frontier models (Pro/Enterprise/Ultimate). API methods are being migrated from POST to GET, with the MCP tool `get-api-schema` receiving a new canonical name `api-method-schema`.

## Maritime & Vessel Tracking

### garrettXu/mcp-shipxy-api

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [garrettXu/mcp-shipxy-api](https://github.com/garrettXu/mcp-shipxy-api) | 10 | Python | MIT | Multiple |

A comprehensive **maritime intelligence server** integrating with ShipXY's vessel tracking platform:

- **Ship tracking** — real-time vessel positions, static ship information, fleet queries, area-based vessel searches
- **Port data** — global port search, berth and anchor queries, ETA predictions, port call records
- **Route planning** — point-to-point and port-to-port maritime route planning
- **Weather & tides** — marine weather forecasts, typhoon tracking, tide station data

This fills a unique niche — maritime logistics is a specialized domain where real-time vessel tracking, port operations data, and marine weather are critical for supply chain planning. Shipping companies, freight forwarders, and commodity traders who need to track cargo vessels would find this particularly valuable.

Requires a ShipXY API key from the ShipXY Open Platform. MIT licensed and extensible.

## Software Supply Chain Security

### securechaindev/securechain-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [securechaindev/securechain-mcp-server](https://github.com/securechaindev/securechain-mcp-server) | — | TypeScript | — | Multiple |

A different kind of supply chain — **software supply chain security** via MCP:

- Query packages from PyPI, NPM, Maven, Cargo, RubyGems, and NuGet ecosystems
- Vulnerability intelligence and security analysis
- Supply chain risk assessment for software dependencies

While not physical logistics, software supply chain security is an increasingly important domain. This server lets AI agents analyze dependency risks and vulnerability exposure across multiple package ecosystems. Included here for completeness — it addresses "supply chain" in the software sense rather than the physical goods sense.

## Enterprise Supply Chain (Emerging)

### CDataSoftware/sap-ariba-procurement-mcp-server-by-cdata

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CDataSoftware/sap-ariba-procurement-mcp-server-by-cdata](https://github.com/CDataSoftware/sap-ariba-procurement-mcp-server-by-cdata) | 2 | Java | MIT | 3 |

The **first enterprise procurement platform accessible through MCP** — CData's read-only server connects Claude Desktop to SAP Ariba Procurement data via JDBC drivers:

- **get_tables** — discover available data tables
- **get_columns** — explore table schemas
- **run_query** — natural language querying of procurement data (no SQL required)

This is read-only — you can query procurement data but not create purchase orders or modify workflows. Still, it represents the first crack in the enterprise procurement MCP wall. CData offers free (beta) read/write servers for additional functionality.

### Oracle Integration as MCP Tools Provider

Oracle Integration Cloud (OIC) now functions as an **MCP tools provider**, turning any existing integration flow into agent-callable MCP tools. This is significant for supply chain because:

- Any OIC integration with SAP, Oracle SCM, or other enterprise systems becomes an MCP tool
- OAuth2 authentication, session management, and audit logging handled by OIC
- Oracle AI Agent Studio can use OIC as an MCP server directly
- Infosys is already using this to scale enterprise agentic AI systems

This isn't a standalone MCP server you install — it's a platform capability that bridges the enterprise supply chain gap by exposing existing enterprise integrations to AI agents. Organizations with Oracle Fusion Cloud SCM, for example, can now expose their supply chain workflows (procurement, planning, manufacturing, logistics) as MCP tools without building custom servers.

Oracle also announced **29 prebuilt AI agents for SCM** in Fusion Cloud Applications (February 2026), including a Planning Cycle Agent for automated task coordination and a Component Replacement Agent for minimizing disruptions. These operate within the Fusion Applications security framework.

## What's Missing

The logistics MCP ecosystem has matured in shipping and is beginning to bridge the enterprise gap, but significant holes remain:

- **No dedicated ERP MCP servers** — SAP S/4HANA, Oracle SCM Cloud, Microsoft Dynamics 365 lack standalone MCP servers (though Oracle Integration's MCP capability and CData's SAP Ariba bridge provide indirect access)
- **No warehouse management systems** — Manhattan Associates, Blue Yonder, SAP EWM, Körber remain unconnected
- **No transportation management** — Oracle Transportation Management, MercuryGate, BluJay Solutions, project44
- **No demand planning or forecasting** — no AI-powered demand sensing, S&OP planning, or inventory optimization servers (ReplenishRadar's forecasting is e-commerce-focused, not enterprise S&OP)
- **No customs & trade compliance** — Descartes, Amber Road, Integration Point for cross-border logistics
- **No cold chain monitoring** — no temperature tracking, pharmaceutical logistics, or food safety compliance
- **No last-mile delivery optimization** — Route4Me, OptimoRoute, Onfleet for delivery route planning (despite the $178B last-mile market)
- **No Coupa procurement** — SAP Ariba has a read-only MCP bridge via CData, but Coupa and Jaggaer remain absent
- **No freight marketplaces** — Convoy, Uber Freight, DAT, Loadsmart for freight matching and booking
- **No 3PL/fulfillment** — ShipBob, Deliverr, Flexport API integration for outsourced logistics
- **No DHL official MCP** — despite DHL's heavy AI investment (Greenplan routing, 95% volume prediction accuracy), no official MCP server exists
- **No returns management** — Loop Returns, Happy Returns, Returnly for reverse logistics (though Shippo now handles returns automation)

The gap between "ship a parcel" and "manage a supply chain" is narrowing — Oracle Integration's MCP capability and CData's SAP Ariba bridge show enterprise platforms are beginning to expose supply chain data to AI agents. But dedicated, purpose-built MCP servers for enterprise logistics remain absent.

## The Bottom Line

Logistics & Supply Chain MCP servers earn **3.5/5**, up from 3/5 in our initial review. The shipping segment has strengthened considerably — Karrio (720 stars, 50+ carriers, self-hosted) emerges as the open-source leader alongside Shippo's expanded agentic platform (now covering returns, WISMO, analytics, and batch operations). TrackMage scales tracking to 1,600+ carriers, FedEx gets community coverage, and Correios adds Latin American reach. Inventory management has diversified from SkuVault alone to include ReplenishRadar's AI-native intelligence (28 tools with demand forecasting and safety guardrails) and inFlow's 50+ tool comprehensive suite. Fleet telematics via Flespi (157 tools, now with Codi AI and Agent Skills) and maritime intelligence via ShipXY continue to serve specialized verticals.

The most significant development is the **emergence of enterprise supply chain bridges**. Oracle Integration Cloud functioning as an MCP tools provider means any existing enterprise integration (SAP, Oracle SCM, procurement workflows) can become an agent-callable tool. CData's SAP Ariba MCP server — though read-only — is the first direct procurement platform MCP bridge. These aren't the dedicated, feature-rich MCP servers that enterprise logistics needs, but they're the first signs of the enterprise supply chain's MCP moment arriving.

What still holds the category back: no dedicated ERP, WMS, TMS, or procurement MCP servers. No last-mile optimization despite the $178B market. No DHL official MCP despite their AI leadership. And the eBay MCP's unpatched CVE-2026-27203 (CVSS 8.3) is a reminder that security must scale alongside tooling. The gap is narrowing, but enterprise supply chain management through AI agents remains more promise than reality.

*This review was refreshed on 2026-04-28 using Claude Opus 4.6 (Anthropic). First published 2026-03-15.*

