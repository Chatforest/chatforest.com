---
title: "Logistics & Supply Chain MCP Servers — Shipping, Fleet Tracking, Inventory Management, and Maritime Intelligence"
date: 2026-03-15T23:30:00+09:00
description: "Logistics and supply chain MCP servers are an emerging category with 20+ servers across 5 subcategories."
og_description: "Logistics & Supply Chain MCP servers: Shippo MCP (official, multi-carrier shipping), UPS-API/ups-mcp (4 stars, official UPS), skuvault-mcp-server (production-ready inventory), flespi-mcp-server (157 telematics tools), ShipXY (9 stars, maritime tracking), ebay-mcp (325 tools). 20+ servers reviewed. Rating: 3/5."
content_type: "Review"
categories: ["/categories/logistics-industry/"]
card_description: "Logistics and supply chain MCP servers for AI-powered shipping, fleet management, inventory control, and maritime tracking. This is an emerging category with strong shipping coverage but significant enterprise gaps. **Shippo leads as the first agentic shipping platform** — the official Shippo MCP server (TypeScript) is the standout, providing multi-carrier shipping via USPS, UPS, FedEx, DHL, and dozens of others through a single MCP integration. Create shipments, generate labels, compare rates, track packages, validate addresses, and manage customs declarations — all through natural language prompts. This is one of the few MCP servers backed by a well-funded shipping infrastructure company. Requires a Shippo API key. **UPS goes official with MCP** — UPS-API/ups-mcp (4 stars, Python, MIT) is UPS's own MCP server, enabling AI agents to track shipments, get shipping rates, and manage UPS logistics. Still in active development but significant as a first-party offering from one of the world's largest carriers. **Indian e-commerce shipping gets MCP coverage** — bfrs/shiprocket-mcp (TypeScript) connects to Shiprocket for courier partner comparison, shipping rate checks, order creation/update/cancellation, direct shipping, and AWB tracking. Connects via email/password authentication to your Shiprocket account. **EasyPost brings multi-carrier abstraction** — bischoff99/easypost_mcp_server wraps the EasyPost API for rate comparison, label purchase, package tracking, and address verification across USPS, UPS, FedEx, DHL, and many other carriers. **Inventory management reaches production quality** — dbankscard/skuvault-mcp-server (Python) provides enterprise-grade SkuVault integration with product management, inventory control across multiple warehouses, low stock alerts, and analytics. Features smart rate limiting with exponential backoff, intelligent caching, and confirmation requirements for all mutations — designed for real production use, not demos. **eBay sellers get 325 tools** — YosefHayim/ebay-mcp (TypeScript) is a massive MCP server covering eBay's entire Sell API surface: inventory management, order fulfillment, marketing campaigns, analytics, and developer tools. The breadth is extraordinary — 325 tools in a single server. **Fleet telematics gets 157 tools** — gperezt222/flespi-mcp-server (TypeScript) auto-generates 157 MCP tools from the Flespi telematics API, covering fleet management, device tracking, and telemetry data processing for 1,000+ IoT device types. Fully MCP v1.0 compliant with Zod validation. **Maritime intelligence goes real-time** — garrettXu/mcp-shipxy-api (9 stars, Python, MIT) integrates with ShipXY for real-time vessel tracking, ship position queries, port and berth data, route planning, weather forecasts, typhoon tracking, and tide station data. A comprehensive maritime logistics toolkit. **Major gaps in enterprise supply chain** — no ERP integration (SAP S/4HANA, Oracle SCM, Microsoft Dynamics), no warehouse management systems (Manhattan Associates, Blue Yonder, SAP EWM), no transportation management systems (Oracle Transportation, MercuryGate, BluJay), no demand planning or forecasting, no customs/trade compliance (Descartes, Amber Road), no cold chain monitoring, no last-mile delivery optimization (Route4Me, OptimoRoute), no procurement platforms (Coupa, Ariba, Jaggaer), no freight marketplaces (Convoy, Uber Freight, DAT). The category earns 3/5 — shipping and parcel management is well-served with official backing from Shippo and UPS, inventory has a production-ready option in SkuVault, and fleet telematics and maritime tracking offer impressive tool counts. But the enterprise supply chain stack — ERP, WMS, TMS, demand planning, procurement — is completely absent, leaving a massive opportunity for MCP servers that connect AI agents to the operational backbone of global commerce."
last_refreshed: 2026-03-15
---

Logistics and supply chain MCP servers let AI assistants manage shipping operations, track fleets, control inventory, and monitor maritime vessel movements. Instead of logging into separate carrier portals, warehouse systems, and tracking platforms, these servers let AI agents handle logistics workflows through the Model Context Protocol.

This review covers the **logistics and supply chain** vertical — shipping and parcel management, inventory and warehouse operations, fleet telematics, and maritime tracking. For e-commerce platforms that include some shipping features, see our [E-Commerce MCP review](/reviews/ecommerce-shopping-mcp-servers/). For general business operations, see our [Business & Productivity MCP review](/reviews/erp-business-management-mcp-servers/).

The headline findings: **Shippo launches the first agentic shipping platform** with multi-carrier support. **UPS goes official** with its own MCP server. **SkuVault inventory reaches production quality** with enterprise-grade rate limiting and safety confirmations. **Flespi delivers 157 telematics tools** for fleet management. **Enterprise supply chain (ERP, WMS, TMS, procurement) is completely missing.**

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

## Maritime & Vessel Tracking

### garrettXu/mcp-shipxy-api

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [garrettXu/mcp-shipxy-api](https://github.com/garrettXu/mcp-shipxy-api) | 9 | Python | MIT | Multiple |

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

## What's Missing

The logistics MCP ecosystem covers shipping and parcel operations well but has critical gaps in enterprise supply chain management:

- **No ERP integration** — SAP S/4HANA, Oracle SCM Cloud, Microsoft Dynamics 365 have no MCP servers
- **No warehouse management systems** — Manhattan Associates, Blue Yonder, SAP EWM, Körber remain unconnected
- **No transportation management** — Oracle Transportation Management, MercuryGate, BluJay Solutions, project44
- **No demand planning or forecasting** — no AI-powered demand sensing, S&OP planning, or inventory optimization servers
- **No customs & trade compliance** — Descartes, Amber Road, Integration Point for cross-border logistics
- **No cold chain monitoring** — no temperature tracking, pharmaceutical logistics, or food safety compliance
- **No last-mile delivery optimization** — Route4Me, OptimoRoute, Onfleet for delivery route planning
- **No procurement platforms** — Coupa, SAP Ariba, Jaggaer for supplier management and purchasing
- **No freight marketplaces** — Convoy, Uber Freight, DAT, Loadsmart for freight matching and booking
- **No 3PL/fulfillment** — ShipBob, Deliverr, Flexport API integration for outsourced logistics
- **No returns management** — Loop Returns, Happy Returns, Returnly for reverse logistics

The gap between "ship a parcel" (well-served) and "manage a supply chain" (completely absent) mirrors what we see in many MCP verticals — consumer-facing workflows arrive first, enterprise operations lag behind.

## The Bottom Line

Logistics & Supply Chain MCP servers earn **3/5**. The shipping and parcel management segment is the clear strength — Shippo's official agentic shipping platform provides multi-carrier shipping through a single MCP integration, UPS offers first-party AI agent support, and EasyPost and Shiprocket add carrier breadth and regional coverage. Inventory management has a genuinely production-ready option in the SkuVault server with enterprise-grade safety features, and eBay sellers get an extraordinary 325-tool server. Fleet telematics via Flespi (157 tools) and maritime intelligence via ShipXY round out specialized verticals.

What holds the category back is the complete absence of enterprise supply chain infrastructure. Organizations managing global supply chains — with ERP systems, warehouse management, transportation management, demand planning, and procurement workflows — will find nothing here. The category serves shippers and sellers well but supply chain managers not at all. As supply chain digitization accelerates and platforms like SAP and Oracle invest in AI agent ecosystems, expect MCP servers for enterprise logistics to emerge — but the physical supply chain's MCP moment hasn't arrived yet.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
