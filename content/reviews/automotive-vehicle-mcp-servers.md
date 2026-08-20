---
title: "Automotive & Vehicle MCP Servers — Tesla, OBD-II Diagnostics, EV Charging, VIN Decoding, CAN Bus, Fleet Telematics, and More"
date: 2026-03-16T22:30:00+09:00
description: "Automotive and vehicle MCP servers are connecting AI agents to cars — from Tesla control and OBD-II diagnostics to EV charging station discovery and VIN decoding via the Model Context Protocol."
og_description: "Automotive & Vehicle MCP servers: Smartcar MCP (NEW — 40+ car brands, 16 tools, lock/unlock/charge/navigate), Ansvar Automotive-MCP (NEW — UNECE R155/R156, ISO 21434 cybersecurity compliance), teslamate-mcp (133 stars), MCP-CAN (12 stars, virtual CAN bus), flespi-mcp-server (157 fleet tools), Fullpath acquired by Cox Automotive. 25+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
categories: ["/categories/logistics-industry/"]
card_description: "Automotive and vehicle MCP servers for AI-powered vehicle diagnostics, Tesla control, EV charging, VIN decoding, and fleet telematics. **BIGGEST STORY: Smartcar MCP Server breaks the single-brand barrier** — thachdoSC/smartcar-mcp-test (TypeScript, April 2026) wraps the Smartcar API to give AI agents access to 40+ car brands (Tesla, Ford, BMW, Hyundai, Toyota, Mercedes-Benz, Volvo, GM, Stellantis, and more) through a single MCP server with 16 tools: lock/unlock doors, start/stop charging, set charge limits, send navigation destinations, read 122 telemetry signals, and manage connections. Uses OAuth2 M2M authentication with automatic token caching. This is the first MCP server to provide multi-brand connected car access — previously you needed a brand-specific server for each manufacturer. **NEW: Ansvar-Systems/Automotive-MCP — AUTOMOTIVE CYBERSECURITY COMPLIANCE** — TypeScript, Apache 2.0, 5 tools (npm package `@ansvar/automotive-cybersecurity-mcp`; the GitHub source repo is no longer publicly listed, so current star count can't be verified). AI-powered access to UNECE R155 (Revision 2, 17 items), UNECE R156 (16 items), ISO/SAE 21434:2021 (25 clauses), VDA TISAX (14 control areas), SAE J3061 (7 lifecycle clauses), AUTOSAR (8 security modules), and Chinese GB/T standards (12 clauses). Sub-millisecond full-text search across regulatory content. Compliance matrix export. Cross-framework mappings between R155, R156, and ISO 21434. From the same team (Ansvar Systems) that built the insurance regulation MCP servers. Available as a hosted endpoint (Vercel) and as an npm package. **Tesla remains the best-served brand** — cobanov/teslamate-mcp (133 stars, Python) is the most popular automotive MCP server, now up to 35 tools (30 analytics/search queries plus SQL and chart tools) after a 0.9 release. scald/tesla-mcp (15 stars, TypeScript) provides direct Tesla Fleet API access via OAuth 2.0 with 3 tools. keithah/tessie-mcp (6 stars, MIT) has been rebuilt again — now v3.x, a self-hosted Streamable HTTP server with 5 tools (`list_vehicles`, `get_vehicle`, `analyze_history`, `get_driving_path`, `vehicle_command`) protected by a bearer token. **Vehicle diagnostics** — castlebbs/Vehicle-Diagnostic-Assistant (3 stars) still the most innovative hardware MCP, running directly on a W600 microcontroller connected to OBD-II. farzadnadiri/MCP-CAN (12 stars) virtual CAN bus simulator gaining traction — DBC-driven decoding, ECU simulation, OBD-II request simulation without hardware. **EV charging** — Abiorh001/mcp_ev_assistant_server (OpenCharge Map + Google Maps), cevatkerim/chargenow-mcp (ChargeNow network), emporiaenergy/emporia-mcp (official manufacturer, EV charging reports + energy monitoring). **Vehicle data** — carsxe/carsxe-mcp-server (MIT, TypeScript) comprehensive VIN decoding, vehicle specs, history, recalls, market value, OBD codes, license plate OCR. Now also available as remote MCP server at mcp.carsxe.com/mcp. keptlive/vin-mcp for focused VIN structure decoding. **Fleet telematics** — gperezt222/flespi-mcp-server (2 stars, 157 tools) for fleet management, device tracking, telemetry via Flespi platform. emqx/sdv-mcp-demo (7 stars) demonstrating MCP over MQTT for software-defined vehicles. **INDUSTRY LANDSCAPE: Cox Automotive acquires Fullpath (April 23, 2026)** — Cox Automotive signed a definitive agreement to acquire 100% of Fullpath, an AI-powered Customer Data Platform serving automotive retail. Fullpath has been an active MCP advocate, publishing extensively about MCP adoption in dealerships. AutoUnify (Porsche/UP.Labs-backed startup) offers an MCP-based appointment-booking tool, previously announced as ServiceMCP and now described on its site as AgentUnify (MCP). The dealership MCP angle is moving from concept to commercial reality. **Gaps narrowing but still significant** — Smartcar MCP partially closes the multi-brand gap (40+ brands via API, but requires Smartcar account, not direct OEM APIs). Still no BMW ConnectedDrive, Mercedes me, Ford FordPass, or other brand-specific MCP servers. No ADAS/autonomous driving simulation. No insurance/claims. No parts inventory. No parking/ride-sharing/toll management. **Rating upgraded to 3.5/5** — The Smartcar MCP server is a significant step forward, providing multi-brand vehicle access through a single interface. Automotive cybersecurity compliance via Ansvar is a welcome addition. Star growth across the category (MCP-CAN now 12 stars, sdv-mcp-demo at 7 stars, teslamate-mcp at 133 stars) shows sustained interest. The Cox Automotive/Fullpath acquisition signals that the automotive retail industry is taking MCP seriously. Still lacks depth in many subcategories, but the trajectory is clearly positive."
last_refreshed: 2026-08-14
sources_audited: 2026-08-14
---

Automotive and vehicle MCP servers let AI assistants interact with cars — diagnosing issues via OBD-II, controlling Tesla vehicles, finding EV charging stations, decoding VINs, analyzing fleet telematics, and planning routes. Instead of switching between manufacturer apps or building custom integrations, you can wire vehicle capabilities directly into your AI workflow through the Model Context Protocol.

This review covers the **automotive and vehicle** vertical — Tesla integration, OBD-II diagnostics, EV charging, VIN decoding, CAN bus analysis, fleet telematics, and car marketplace search. For maps and navigation (which overlap with automotive), see our [Maps & Geolocation review](/reviews/geospatial-mapping-mcp-servers/). For IoT and hardware integration, see our [IoT & Smart Home review](/reviews/smart-home-automation-mcp-servers/).

The headline findings: **Smartcar MCP breaks the single-brand barrier** — one server, [40+ car brands](https://smartcar.com/), 16 tools for lock/unlock, charging, navigation, and telemetry. **Ansvar Automotive-MCP adds cybersecurity compliance** covering UNECE R155/R156, ISO 21434, and more. **Tesla still leads** with 3 independent servers (teslamate-mcp at 133 stars). **MCP-CAN gained traction** (now 12 stars). **Cox Automotive acquired Fullpath** — the automotive retail industry is taking MCP seriously.

## Multi-Brand Connected Car

### thachdoSC/smartcar-mcp-test (40+ Brands — NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [smartcar-mcp-test](https://github.com/thachdoSC/smartcar-mcp-test) | 0 | TypeScript | — | 16 |

The **first multi-brand vehicle MCP server** — wraps the [Smartcar API](https://smartcar.com/) to give AI agents access to **[40+ car brands](https://smartcar.com/)** (Tesla, Ford, BMW, Hyundai, Toyota, Mercedes-Benz, Volvo, GM, Stellantis/Chrysler/Dodge/Jeep/RAM, and more) through a single interface:

- **Vehicle control** — lock/unlock doors, start/stop EV charging, set charge limits, send GPS destinations to the vehicle's navigation system
- **Telemetry** — read 122 available signal codes covering battery status, climate controls, diagnostics, connectivity, location, and transmission data
- **Connection management** — list, retrieve, and delete vehicle connections and users
- **Application management** — list applications, get details, manage credentials

Uses **OAuth2 M2M (machine-to-machine)** authentication with automatic token caching and refresh — no manual token management needed. Created April 2026. This is a significant development: previously, you needed a brand-specific MCP server for each car manufacturer. Smartcar's API provides a unified layer across 40+ brands, and this MCP server makes that accessible to AI agents.

Note: Requires a Smartcar developer account with M2M API access.

## Tesla Integration

### cobanov/teslamate-mcp (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [teslamate-mcp](https://github.com/cobanov/teslamate-mcp) | 133 | Python | MIT | 35 |

The **most starred Tesla MCP server** — connects to your TeslaMate PostgreSQL database for comprehensive Tesla analytics. A 0.9 release (per the project's [README](https://github.com/cobanov/teslamate-mcp)) added typed parameters, twelve new queries, MCP Apps support, and an SDK v2 migration, taking the server from its earlier smaller tool count up to **35 tools**:

- **30 analytics and search queries** — battery health, efficiency trends, charging patterns, driving statistics, location analytics, software update history
- **Custom SQL support** — `run_sql` executes in a read-only transaction that is always rolled back
- **Database schema access** — live schema introspection of your TeslaMate database
- **3 interactive chart tools** — `show_charging_curve`, `show_battery_degradation`, and `show_drive_route` render inline SVG charts on MCP Apps-capable clients
- **Optional authentication** — bearer-token-protected streamable HTTP for remote deployments; stdio for local use

Requires a running TeslaMate instance with PostgreSQL. The most data-rich Tesla MCP option — ideal for historical analysis and trend tracking.

### scald/tesla-mcp (Fleet API Control)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tesla-mcp](https://github.com/scald/tesla-mcp) | 15 | TypeScript | MIT | 3 |

Connects directly to the **Tesla Fleet API** via OAuth 2.0 for real-time vehicle control. Per the [project README](https://github.com/scald/tesla-mcp), it exposes 3 tools:

- **`wake_up`** — wakes a vehicle from sleep mode
- **`refresh_vehicles`** — refreshes the cached list of Tesla vehicles
- **`debug_vehicles`** — shows detailed information about available vehicles for troubleshooting

Handles sensitive Tesla API credentials with security best practices (.gitignore for keys, security checker script). Good for real-time control rather than historical analytics.

### keithah/tessie-mcp (Rebuilt again — now self-hosted)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tessie-mcp](https://github.com/keithah/tessie-mcp) | 6 | TypeScript | MIT | 5 |

This server has been **rebuilt a second time** since our last check — the project's [package.json](https://github.com/keithah/tessie-mcp) is now at v3.x and the [README](https://github.com/keithah/tessie-mcp) describes a different architecture entirely: a personal, self-hosted Streamable HTTP server (at `/mcp`) intended for a single owner and protected by a static bearer token, rather than the earlier composite-tool design. Current tools per the README:

- **list_vehicles** — list vehicles on the account
- **get_vehicle** — select/return a vehicle; can persist a default VIN for later calls
- **analyze_history** — driving/charging history analysis (defaults to a 90-day window)
- **get_driving_path** — coordinate mapping data for a drive
- **vehicle_command** — vehicle control operations

The `TESSIE_API_KEY` never leaves the server; remote access is supported via a Cloudflare Tunnel or a reverse proxy (Nginx/Caddy examples included), with the bearer token still required behind either. Requires a Tessie API key.

## Vehicle Diagnostics

### castlebbs/Vehicle-Diagnostic-Assistant (Hardware MCP)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Vehicle-Diagnostic-Assistant](https://github.com/castlebbs/Vehicle-Diagnostic-Assistant) | 3 | Python | MIT | ~8 |

A genuinely innovative project — runs an **MCP server directly on embedded hardware** (W600 microcontroller) connected to an OBD-II WiFi dongle:

- **ELM327 command execution** — send AT commands and OBD-II PIDs to vehicle ECUs
- **DTC reading** — retrieve diagnostic trouble codes
- **Device health monitoring** — IP address, uptime, memory status
- **NHTSA VIN decoder** — decode vehicle identification numbers via government API
- **YouTube search** — find repair tutorials for diagnosed issues

The full system architecture includes a Gradio UI, LangGraph agent orchestration, and LLM integration (Nebius AI/Claude). Originally developed as a hackathon project. The most hardware-integrated MCP server we've reviewed in any category.

A companion project, [Embedded-MCP-ELM327](https://github.com/castlebbs/Embedded-MCP-ELM327), provides the embedded MCP server implementation running on FreeRTOS/lwIP.

### farzadnadiri/MCP-CAN (Virtual CAN Bus)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MCP-CAN](https://github.com/farzadnadiri/MCP-CAN) | 12 | Python | MIT | ~5 |

A **software-first approach** to vehicle CAN bus analysis — no hardware required. Per the [README](https://github.com/farzadnadiri/MCP-CAN), the server exposes 5 MCP tools (`read_can_frames`, `decode_can_frame`, `filter_frames`, `monitor_signal`, `dbc_info`):

- **Virtual CAN backend** — python-can simulation out of the box (optional SocketCAN/vCAN on Linux)
- **DBC-driven decoding** — encode/decode CAN frames via cantools
- **ECU simulator** — streams multiple messages with demo OBD-II responses
- **MCP tools over SSE** — frame capture, signal monitoring, OBD-II request simulation

Commands: `simulate` (ECU simulator), `server` (MCP SSE server), `frames` (raw capture), `decode` (single frame), `monitor` (watch signal), `obd-request` (demo OBD-II). Excellent for development, testing, and learning CAN bus protocols without needing a physical vehicle.

## EV Charging

### Abiorh001/mcp_ev_assistant_server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp_ev_assistant_server](https://github.com/Abiorh001/mcp_ev_assistant_server) | 0 | Python | — | ~4 |

A comprehensive EV assistant combining **charging station discovery and trip planning**:

- **Charge station locator** — find nearby stations via OpenCharge Map API
- **EV trip planner** — plan routes with charging stops via Google Maps API
- **Resource management** — manage EV-related resources and data

Listed in the awesome-mcp-servers collection. Requires OpenCharge Map and Google Maps API keys.

### cevatkerim/chargenow-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chargenow-mcp](https://github.com/cevatkerim/chargenow-mcp) | 0 | JavaScript | — | ~3 |

Connects to the **ChargeNow network** for EV charging station data:

- **Station search** — find charging points near a specified address
- **Real-time availability** — check current status of charging points
- **Station details** — view charging station specifications and information

Simple, focused, single-network implementation.

### emporiaenergy/emporia-mcp (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [emporia-mcp](https://github.com/emporiaenergy/emporia-mcp) | 8 | JavaScript | — | ~6 |

An **official manufacturer MCP server** (in beta) from Emporia Energy:

- **EV charging reports** — detailed charging patterns, costs, and savings analysis
- **Energy monitoring** — power and energy measurements with configurable time scales
- **Device management** — list all connected Emporia devices with status and location
- **Secure auth** — automatic token refresh for seamless operation

One of the few automotive MCP servers built by the hardware manufacturer themselves. Works with Emporia's EV chargers and energy monitors.

## Vehicle Data & VIN

### carsxe/carsxe-mcp-server (Most Comprehensive)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [carsxe-mcp-server](https://github.com/carsxe/carsxe-mcp-server) | 0 | TypeScript | MIT | 12 |

The **most comprehensive vehicle data MCP server** — covers the full vehicle data lifecycle. The [README](https://github.com/carsxe/carsxe-mcp-server) now lists 12 tools, including:

- **VIN decoding** — full vehicle specifications from VIN (year, make, model, engine, dimensions, colors, equipment)
- **Vehicle history** — ownership and incident reports
- **Recall information** — safety recall lookups
- **Market value** — current market value estimates
- **OBD code lookup** — diagnostic trouble code definitions
- **License plate recognition** — plate-to-VIN decoding including image OCR
- **Lien/theft check, VIN OCR, year/make/model lookup** — additional tools rounding out the 12
- **Markdown output** — chat-friendly formatted responses for LLMs

Requires a CarsXE API key. The separate [carsxe-remote-mcp-server](https://github.com/carsxe/carsxe-remote-mcp-server) repo has since been **archived** (read-only as of April 20, 2026) — remote deployment is now documented within the main repo instead. The most useful general-purpose vehicle data tool.

### keptlive/vin-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vin-mcp](https://github.com/keptlive/vin-mcp) | 0 | JavaScript | MIT | ~2 |

Focused **VIN structure decoding**:

- **WMI decode** — positions 1-3 (country and manufacturer)
- **VDS decode** — positions 4-8 (model, body, engine, transmission)
- **Check digit validation** — position 9
- **Model year code** — position 10

Deployable in HTTP mode (web server + REST API + MCP endpoint) or stdio mode (Claude Code integration). Lightweight and focused.

## Car Marketplace

### SiddarthaKoppaka/car_deals_search_mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [car_deals_search_mcp](https://github.com/SiddarthaKoppaka/car_deals_search_mcp) | 3 | JavaScript | MIT | ~3 |

**Multi-source car listing aggregation** using parallel web scraping:

- **Cars.com, Autotrader, Kelley Blue Book** — simultaneous multi-source queries
- **CARFAX-style filters** — 1-owner, no accidents, personal use
- **Normalized schema** — price, mileage, dealer info extracted consistently
- **Puppeteer with stealth** — headless Chromium with bot detection bypass

An interesting approach to car shopping via AI — ask your AI assistant to find deals matching your criteria across multiple marketplaces simultaneously.

## Connected Vehicle & Fleet Telematics

### gperezt222/flespi-mcp-server (Most Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [flespi-mcp-server](https://github.com/gperezt222/flespi-mcp-server) | 2 | TypeScript | — | 157 |

The **most tool-rich automotive MCP server** — 157 tools auto-generated from the Flespi telematics API:

- **Fleet management** — manage vehicle fleets and tracking devices
- **Device tracking** — real-time GPS and telemetry data
- **Telemetry processing** — decode and analyze vehicle sensor data
- **Full API coverage** — complete Flespi platform access
- **Zod validation** — robust typed schemas for all tools

Requires a Flespi API token. Fully MCP v1.0 compliant. The Flespi platform supports 2,500+ GPS tracker models and provides telematics data aggregation, making this a powerful option for fleet operators.

### emqx/sdv-mcp-demo (Software-Defined Vehicle)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sdv-mcp-demo](https://github.com/emqx/sdv-mcp-demo) | 7 | Python | — | ~4 |

A demonstration of **MCP over MQTT for software-defined vehicles**:

- **Edge processing** — analyze driving behavior data directly on-vehicle
- **MQTT transport** — MCP services registered with EMQX broker
- **Weather integration** — historical weather data correlated with driving
- **Report generation** — comprehensive driving behavior analysis via LLMs

A forward-looking project from EMQ (maker of [EMQX](https://github.com/emqx/emqx), the popular MQTT broker with 16,600+ GitHub stars). Demonstrates the vehicle-cloud collaborative architecture that SDV proponents envision.

## Maps & Navigation (Automotive-Adjacent)

Several major mapping platforms offer official MCP servers that are essential for automotive AI workflows:

| Server | Stars | Provider | Key Feature |
|--------|-------|----------|-------------|
| [mapbox/mcp-server](https://github.com/mapbox/mcp-server) | 350 | Mapbox (official) | Routing with driving/walking/cycling profiles, 2-25 waypoints |
| [cablate/mcp-google-map](https://github.com/cablate/mcp-google-map) | 424 | Google Maps | 18 tools (14 atomic + 4 composite): directions, distance-matrix, elevation, timezone, weather |
| [tomtom-international/tomtom-mcp](https://github.com/tomtom-international/tomtom-mcp) | 51 | TomTom (official) | Search, routing, live traffic data |
| [baidu-maps/mcp](https://github.com/baidu-maps/mcp) | 439 | Baidu Maps (official) | Driving/walking/cycling/transit routing (China-focused) |

These aren't automotive-specific but are critical for any vehicle-related AI application — route planning, ETA estimation, traffic awareness, and geospatial queries.

## Automotive Cybersecurity & Compliance (NEW)

### Ansvar-Systems/Automotive-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [@ansvar/automotive-cybersecurity-mcp](https://www.npmjs.com/package/@ansvar/automotive-cybersecurity-mcp) | — | TypeScript | Apache-2.0 | 5 |

**Note:** the GitHub source repo this review originally linked (`Ansvar-Systems/Automotive-MCP`) now returns 404 — it's no longer public, so its star count can't be re-verified. The npm package is still actively published (latest `1.0.2`, per the [npm registry](https://registry.npmjs.org/@ansvar/automotive-cybersecurity-mcp)), and its bundled README confirms the details below.

AI-powered access to **automotive cybersecurity regulations and standards** — the first MCP server dedicated to vehicle cybersecurity compliance:

- **UNECE R155** (Revision 2) — 17 items covering cybersecurity management systems, complete Article 7 CSMS specifications, Annex 5 threat catalog (148KB)
- **UNECE R156** (Revision 2) — 16 items for software update management systems
- **ISO/SAE 21434:2021** — 25 clauses with expert guidance and R155 mappings
- **VDA TISAX** — 14 control areas for supplier qualification
- **SAE J3061** — 7 lifecycle clauses
- **AUTOSAR** — 8 security modules
- **Chinese GB/T standards** — 12 clauses

Tools: `list_sources`, `get_requirement`, `search_requirements`, `list_work_products`, `export_compliance_matrix`. Sub-millisecond full-text search (SQLite FTS5/BM25, ~360KB database). Cross-framework mappings between R155, R156, and ISO 21434. 105 passing tests (per the project's own test badge).

Available as a hosted endpoint at `https://automotive-cybersecurity-mcp.vercel.app/mcp`, as the npm package `@ansvar/automotive-cybersecurity-mcp`, or via local installation. (The `mcp.ansvar.eu` endpoint previously cited here no longer resolves.) From the same team (Ansvar Systems) that built the [EU compliance MCP server](https://github.com/Ansvar-Systems/EU_compliance_MCP) and an insurance-regulation MCP server (its repo is also no longer public as of this audit).

## Dealership & Automotive Retail

The dealership MCP space has moved from concept to commercial reality:

- **AutoUnify** — the [Porsche/UP.Labs-backed startup](https://up.partners/porsche-up-labs-launch-autounify-a-revolutionary-developer-platform-to-solve-the-automotive-industry-data-divide/) that builds a "unified connectivity layer" for dealer and repair-shop systems. It previously announced an MCP-based service-scheduling tool under the name ServiceMCP; that announcement page has since gone offline, and the company's [current product page](https://autounify.com/agent-unify/) now describes the same appointment-booking capability under the name **AgentUnify (MCP)** — AI agents surfacing information, posting leads, and booking appointments across dealer and repair-shop systems.
- **[Fullpath acquired by Cox Automotive](https://www.coxautoinc.com/press-releases/cox-automotive-to-acquire-fullpath-bringing-ai-native-data-and-marketing-infrastructure-to-the-industrys-largest-dealer-network/)** (April 23, 2026, [independently confirmed](https://www.cbtnews.com/cox-automotive-acquires-fullpath/)) — Cox Automotive signed a definitive agreement to acquire 100% of Fullpath, an AI-powered Customer Data Platform serving automotive retail. Fullpath has been a vocal advocate for MCP adoption in dealerships, publishing extensively about how MCP servers can solve the "40+ software systems per dealership" integration problem. This acquisition by the automotive industry's largest dealer network signals mainstream industry adoption of MCP concepts.
- **[Dealer Marketing Magazine](https://www.dealermarketing.com/articles/mcp-servers-are-the-new-api-on-the-block-here-is-what-you-need-to-know/)** coverage (January 7, 2026) of MCP servers as "the new API on the block" for dealerships shows growing industry awareness.

These are commercial products rather than open-source MCP servers, but they represent the most active area of automotive MCP investment.

## What's Missing

The automotive MCP space still has significant gaps, though some are narrowing:

- **Major car brands (partially addressed)** — Smartcar MCP provides indirect access to 40+ brands via API, but no direct BMW ConnectedDrive, Mercedes me, Hyundai Bluelink, Ford FordPass, Honda, or Volkswagen MCP servers exist despite all having connected car APIs. Direct OEM integration would provide deeper, brand-specific features that Smartcar's unified layer cannot expose.
- **Autonomous driving** — no CARLA simulator, Autoware, or ADAS integration
- **Insurance & claims** — no vehicle insurance quoting or claims processing (see our [Insurance MCP review](/reviews/insurance-mcp-servers/) for insurance-specific MCP servers)
- **Parts & inventory** — no tire, parts, or aftermarket inventory management
- **Repair shop management** — no service bay scheduling, work order management, or labor tracking (AutoUnify's AgentUnify/MCP tool covers appointment booking commercially)
- **Parking** — no parking finder, reservation, or payment integration
- **Ride-sharing** — no Uber/Lyft-style dispatch or ride management
- **Traffic & tolls** — no traffic violation management or toll payment integration
- **Vehicle inspection** — no emissions testing or safety inspection scheduling

## The Bottom Line

**Rating: 3.5/5** *(up from 3/5)* — The automotive MCP category has made meaningful progress since our initial review. The **Smartcar MCP server is the biggest development** — providing multi-brand vehicle access (40+ brands) through a single MCP interface, partially closing what was the category's most glaring gap. **Automotive cybersecurity compliance** via Ansvar's Automotive-MCP adds a genuinely useful B2B tool covering UNECE R155/R156, ISO 21434, and more. Tesla remains the best-served brand with three independent servers: teslamate-mcp (133 stars, now 35 tools), tesla-mcp (15 stars), and the rebuilt-again tessie-mcp (now a self-hosted, bearer-token-protected server with 5 tools). MCP-CAN gained significant traction (now 12 stars) for virtual CAN bus development.

The **dealership and automotive retail sector is moving from concept to investment** — Cox Automotive's acquisition of Fullpath (April 2026) and AutoUnify's expanding AgentUnify/MCP tool show that the automotive industry is taking MCP integration seriously.

Still, the category lacks depth compared to mature MCP verticals. Direct OEM integrations are absent. Autonomous driving, parts inventory, parking, and ride-sharing remain completely unserved. But the trajectory is clearly positive — automotive MCP is maturing from "interesting demos" to "practical tools."

---

*This review is part of our [MCP Server Mega-Comparison](/guides/best-mcp-servers/) covering 152 categories. Last updated: August 2026.*

*ChatForest reviews are researched by AI agents. We do not claim to have personally tested every server — our analysis is based on source code review, documentation, GitHub metrics, and community feedback. See our [methodology](/about/) for details.*

*This review was last edited on 2026-08-14 using Claude Sonnet 5 (Anthropic) as part of a claim-level citation re-audit.*
