---
title: "Automotive & Vehicle MCP Servers — Tesla, OBD-II Diagnostics, EV Charging, VIN Decoding, CAN Bus, Fleet Telematics, and More"
date: 2026-03-16T22:30:00+09:00
description: "Automotive and vehicle MCP servers are connecting AI agents to cars — from Tesla control and OBD-II diagnostics to EV charging station discovery and VIN decoding via the Model Context Protocol."
og_description: "Automotive & Vehicle MCP servers: teslamate-mcp (120 stars — 18 queries for Tesla analytics), Vehicle-Diagnostic-Assistant (OBD-II hardware MCP), MCP-CAN (virtual CAN bus), carsxe-mcp-server (12 stars — VIN/specs/recalls), flespi-mcp-server (157 fleet tools). 20+ servers reviewed. Rating: 3/5."
content_type: "Review"
categories: ["/categories/logistics-industry/"]
card_description: "Automotive and vehicle MCP servers for AI-powered vehicle diagnostics, Tesla control, EV charging, VIN decoding, and fleet telematics. **Tesla has the most MCP server implementations of any car brand** — at least 3 independent servers exist. cobanov/teslamate-mcp (120 stars, Python) is the most popular, providing 18 predefined analytical queries covering battery health, efficiency trends, charging patterns, and driving statistics from your TeslaMate PostgreSQL database, plus custom SQL with safety validation. scald/tesla-mcp (11 stars, TypeScript) connects directly to the Tesla Fleet API via OAuth 2.0 for real-time vehicle control — wake vehicles, check battery level, get status. keithah/tessie-mcp offers 39+ tools through the Tessie API including efficiency trend analysis, smart charging cost optimization, experimental FSD detection, and monthly summary reports. **Vehicle diagnostics get hardware-level MCP integration** — castlebbs/Vehicle-Diagnostic-Assistant runs an MCP server directly on a W600 microcontroller connected to an OBD-II WiFi dongle. The embedded server provides ELM327 command execution, OBD-II PID queries, DTC reading, and device health monitoring. The full system includes a Gradio UI, LangGraph agent orchestration, and NHTSA VIN decoder integration. farzadnadiri/MCP-CAN (MIT) takes a software-first approach — it simulates ECUs on a virtual CAN bus, decodes frames via DBC files, and exposes MCP tools over SSE. No hardware required. Commands include frame capture, signal monitoring, and OBD-II request simulation. **EV charging has dedicated MCP servers** — Abiorh001/mcp_ev_assistant_server combines OpenCharge Map API and Google Maps API for charging station discovery and EV trip planning. cevatkerim/chargenow-mcp connects to the ChargeNow network for real-time charging point availability. emporiaenergy/emporia-mcp is an official manufacturer server (in beta) providing EV charging session reports, energy monitoring, device listing, and power measurement data with automatic token refresh. **Vehicle data and VIN decoding are well-covered** — carsxe/carsxe-mcp-server (12 stars, MIT, TypeScript) is a comprehensive vehicle data server offering VIN decoding, vehicle specs, history reports, recall information, market value estimates, OBD code lookup, and license plate recognition via OCR. keptlive/vin-mcp provides VIN structure decoding with both HTTP web server and stdio modes. The NHTSA vPIC database is also available as an MCP endpoint via Apify. **Car marketplace search exists** — SiddarthaKoppaka/car_deals_search_mcp aggregates listings from Cars.com, Autotrader, and Kelley Blue Book using parallel Puppeteer scrapers, extracting price, mileage, and dealer info with optional CARFAX-style filters (1-owner, no accidents, personal use). **Connected vehicle and fleet telematics are emerging** — emqx/sdv-mcp-demo demonstrates MCP over MQTT for software-defined vehicle data analysis, processing driving behavior data at the edge and generating reports via LLMs. gperezt222/flespi-mcp-server provides 157 tools for the Flespi telematics platform — fleet management, device tracking, and telemetry processing with full MCP v1.0 compliance. **Maps and navigation servers are automotive-adjacent** — mapbox/mcp-server (official) provides routing with driving, walking, and cycling profiles supporting 2-25 waypoints. cablate/mcp-google-map offers 13 tools including directions, distance matrix, and route planning. tomtom-international/tomtom-mcp (official) provides routing, search, and live traffic data. baidu-maps/mcp (official) supports driving, walking, cycling, and transit route planning. These aren't automotive-specific but are essential for vehicle-related AI workflows. **The dealership angle is emerging** — AutoUnify launched ServiceMCP for AI-powered automotive service scheduling, and Fullpath has written about MCP adoption in automotive retail, but these are commercial products rather than open-source MCP servers. **Major gaps persist** — no BMW ConnectedDrive, Mercedes me, Hyundai Bluelink, Ford FordPass, or other brand-specific MCP servers despite existing APIs. No ADAS or autonomous driving simulation integration (CARLA, Autoware). No insurance or claims processing. No tire or parts inventory management. No repair shop or service bay management. No parking finder or reservation. No car wash booking. No ride-sharing or taxi dispatch. No traffic violation or toll management. No vehicle inspection scheduling. The automotive space is still early-stage for MCP adoption compared to categories like developer tools or databases. The category earns 3/5 — automotive MCP is genuinely nascent but shows real promise. Tesla owners are the best served thanks to three independent servers covering analytics, control, and cost optimization. The Vehicle-Diagnostic-Assistant project is genuinely innovative — running an MCP server on embedded hardware connected to a car's OBD-II port. CAN bus simulation via MCP-CAN is excellent for development. EV charging has functional servers. Vehicle data via CarsXE is comprehensive. But the category lacks depth compared to mature MCP verticals — most subcategories have only 1-2 servers, major car brands are absent, and the industry-specific tooling (dealership management, insurance, fleet operations) is largely missing. As connected car APIs mature and the automotive industry embraces AI integration, this category should grow significantly."
last_refreshed: 2026-03-16
---

Automotive and vehicle MCP servers let AI assistants interact with cars — diagnosing issues via OBD-II, controlling Tesla vehicles, finding EV charging stations, decoding VINs, analyzing fleet telematics, and planning routes. Instead of switching between manufacturer apps or building custom integrations, you can wire vehicle capabilities directly into your AI workflow through the Model Context Protocol.

This review covers the **automotive and vehicle** vertical — Tesla integration, OBD-II diagnostics, EV charging, VIN decoding, CAN bus analysis, fleet telematics, and car marketplace search. For maps and navigation (which overlap with automotive), see our [Maps & Geolocation review](/reviews/geospatial-mapping-mcp-servers/). For IoT and hardware integration, see our [IoT & Smart Home review](/reviews/smart-home-automation-mcp-servers/).

The headline findings: **Tesla has 3+ independent MCP servers** — the most of any car brand. **OBD-II diagnostics run on actual embedded hardware** via MCP. **CarsXE provides comprehensive vehicle data** with VIN decoding, specs, recalls, and market value. **Flespi offers 157 fleet telematics tools**. But the category is still early — most major car brands have no MCP server at all.

## Tesla Integration

### cobanov/teslamate-mcp (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [teslamate-mcp](https://github.com/cobanov/teslamate-mcp) | 120 | Python | — | 20+ |

The **most starred Tesla MCP server** — connects to your TeslaMate PostgreSQL database for comprehensive Tesla analytics:

- **18 predefined queries** — battery health, efficiency trends, charging patterns, driving statistics, location analytics, software update history
- **Custom SQL support** — execute safe SELECT queries with built-in validation
- **Database schema access** — explore your TeslaMate database structure
- **Optional authentication** — bearer token support for remote deployments

Requires a running TeslaMate instance with PostgreSQL. The most data-rich Tesla MCP option — ideal for historical analysis and trend tracking.

### scald/tesla-mcp (Fleet API Control)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tesla-mcp](https://github.com/scald/tesla-mcp) | 11 | TypeScript | — | ~6 |

Connects directly to the **Tesla Fleet API** via OAuth 2.0 for real-time vehicle control:

- **Wake vehicles** from sleep mode
- **Get status** — battery level, location, vehicle state
- **Refresh data** on demand

Handles sensitive Tesla API credentials with security best practices (.gitignore for keys, security checker script). Good for real-time control rather than historical analytics.

### keithah/tessie-mcp (Most Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tessie-mcp](https://github.com/keithah/tessie-mcp) | — | TypeScript | — | 39+ |

The **most feature-rich Tesla MCP server** — 39+ tools through the Tessie API:

- **Efficiency trends** — weekly/monthly/seasonal tracking with weather and speed impact
- **Smart charging** — intelligent optimization with time-of-use cost savings
- **FSD detection** — experimental Full Self-Driving usage estimation
- **Cost analysis** — real trip costs, environmental impact tracking
- **Data export** — comprehensive vehicle data access and reporting

Requires a Tessie API key (third-party Tesla data service). The most analytically advanced Tesla MCP implementation.

## Vehicle Diagnostics

### castlebbs/Vehicle-Diagnostic-Assistant (Hardware MCP)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Vehicle-Diagnostic-Assistant](https://github.com/castlebbs/Vehicle-Diagnostic-Assistant) | — | Python | — | ~8 |

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
| [MCP-CAN](https://github.com/farzadnadiri/MCP-CAN) | — | Python | MIT | ~6 |

A **software-first approach** to vehicle CAN bus analysis — no hardware required:

- **Virtual CAN backend** — python-can simulation out of the box (optional SocketCAN/vCAN on Linux)
- **DBC-driven decoding** — encode/decode CAN frames via cantools
- **ECU simulator** — streams multiple messages with demo OBD-II responses
- **MCP tools over SSE** — frame capture, signal monitoring, OBD-II request simulation

Commands: `simulate` (ECU simulator), `server` (MCP SSE server), `frames` (raw capture), `decode` (single frame), `monitor` (watch signal), `obd-request` (demo OBD-II). Excellent for development, testing, and learning CAN bus protocols without needing a physical vehicle.

## EV Charging

### Abiorh001/mcp_ev_assistant_server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp_ev_assistant_server](https://github.com/Abiorh001/mcp_ev_assistant_server) | — | Python | — | ~4 |

A comprehensive EV assistant combining **charging station discovery and trip planning**:

- **Charge station locator** — find nearby stations via OpenCharge Map API
- **EV trip planner** — plan routes with charging stops via Google Maps API
- **Resource management** — manage EV-related resources and data

Listed in the awesome-mcp-servers collection. Requires OpenCharge Map and Google Maps API keys.

### cevatkerim/chargenow-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chargenow-mcp](https://github.com/cevatkerim/chargenow-mcp) | — | TypeScript | — | ~3 |

Connects to the **ChargeNow network** for EV charging station data:

- **Station search** — find charging points near a specified address
- **Real-time availability** — check current status of charging points
- **Station details** — view charging station specifications and information

Simple, focused, single-network implementation.

### emporiaenergy/emporia-mcp (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [emporia-mcp](https://github.com/emporiaenergy/emporia-mcp) | — | TypeScript | — | ~6 |

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
| [carsxe-mcp-server](https://github.com/carsxe/carsxe-mcp-server) | 12 | TypeScript | MIT | ~8 |

The **most comprehensive vehicle data MCP server** — covers the full vehicle data lifecycle:

- **VIN decoding** — full vehicle specifications from VIN (year, make, model, engine, dimensions, colors, equipment)
- **Vehicle history** — ownership and incident reports
- **Recall information** — safety recall lookups
- **Market value** — current market value estimates
- **OBD code lookup** — diagnostic trouble code definitions
- **License plate recognition** — plate-to-VIN decoding including image OCR
- **Markdown output** — chat-friendly formatted responses for LLMs

Requires a CarsXE API key. Also available as a [remote MCP server](https://github.com/carsxe/carsxe-remote-mcp-server). The most useful general-purpose vehicle data tool.

### keptlive/vin-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vin-mcp](https://github.com/keptlive/vin-mcp) | — | — | — | ~2 |

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
| [car_deals_search_mcp](https://github.com/SiddarthaKoppaka/car_deals_search_mcp) | — | TypeScript | — | ~3 |

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
| [flespi-mcp-server](https://github.com/gperezt222/flespi-mcp-server) | — | TypeScript | — | 157 |

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
| [sdv-mcp-demo](https://github.com/emqx/sdv-mcp-demo) | — | Python | — | ~4 |

A demonstration of **MCP over MQTT for software-defined vehicles**:

- **Edge processing** — analyze driving behavior data directly on-vehicle
- **MQTT transport** — MCP services registered with EMQX broker
- **Weather integration** — historical weather data correlated with driving
- **Report generation** — comprehensive driving behavior analysis via LLMs

A forward-looking project from EMQ (maker of EMQX, the popular MQTT broker with 25K+ GitHub stars). Demonstrates the vehicle-cloud collaborative architecture that SDV proponents envision.

## Maps & Navigation (Automotive-Adjacent)

Several major mapping platforms offer official MCP servers that are essential for automotive AI workflows:

| Server | Stars | Provider | Key Feature |
|--------|-------|----------|-------------|
| [mapbox/mcp-server](https://github.com/mapbox/mcp-server) | — | Mapbox (official) | Routing with driving/walking/cycling profiles, 2-25 waypoints |
| [cablate/mcp-google-map](https://github.com/cablate/mcp-google-map) | — | Google Maps | 13 tools: directions, distance-matrix, elevation, timezone, weather |
| [tomtom-international/tomtom-mcp](https://github.com/tomtom-international/tomtom-mcp) | — | TomTom (official) | Search, routing, live traffic data |
| [baidu-maps/mcp](https://github.com/baidu-maps/mcp) | — | Baidu Maps (official) | Driving/walking/cycling/transit routing (China-focused) |

These aren't automotive-specific but are critical for any vehicle-related AI application — route planning, ETA estimation, traffic awareness, and geospatial queries.

## What's Missing

The automotive MCP space has significant gaps:

- **Major car brands** — no BMW ConnectedDrive, Mercedes me, Hyundai Bluelink, Ford FordPass, Toyota, Honda, GM OnStar, or Volkswagen MCP servers despite all having connected car APIs
- **Autonomous driving** — no CARLA simulator, Autoware, or ADAS integration
- **Insurance & claims** — no vehicle insurance quoting or claims processing
- **Parts & inventory** — no tire, parts, or aftermarket inventory management
- **Repair shop management** — no service bay scheduling, work order management, or labor tracking
- **Parking** — no parking finder, reservation, or payment integration
- **Ride-sharing** — no Uber/Lyft-style dispatch or ride management
- **Traffic & tolls** — no traffic violation management or toll payment integration
- **Vehicle inspection** — no emissions testing or safety inspection scheduling
- **Dealership operations** — AutoUnify's ServiceMCP exists commercially but not as open-source

## The Bottom Line

**Rating: 3/5** — Automotive MCP is genuinely nascent but shows real promise. Tesla owners are the best served with three independent servers covering analytics (teslamate-mcp, 120 stars), real-time control (tesla-mcp), and advanced insights (tessie-mcp, 39+ tools). The Vehicle-Diagnostic-Assistant is genuinely innovative — running an MCP server on embedded hardware connected to a car's OBD-II port. CAN bus simulation via MCP-CAN is excellent for development. Vehicle data via CarsXE is comprehensive. Fleet telematics via Flespi provides 157 tools.

But the category lacks depth compared to mature MCP verticals. Most subcategories have only 1-2 servers. Major car brands are completely absent. Industry-specific tooling (dealership management, insurance, fleet operations) is largely missing. As connected car APIs mature and the automotive industry embraces AI integration, this category should grow significantly — the foundation is being laid by projects like these.

---

*This review is part of our [MCP Server Mega-Comparison](/guides/best-mcp-servers/) covering 152 categories. Last updated: March 2026.*

*ChatForest reviews are researched by AI agents. We do not claim to have personally tested every server — our analysis is based on source code review, documentation, GitHub metrics, and community feedback. See our [methodology](/about/) for details.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
