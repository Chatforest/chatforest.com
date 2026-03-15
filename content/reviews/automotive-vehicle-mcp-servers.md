---
title: "Automotive & Vehicle MCP Servers — Tesla, OBD-II Diagnostics, VIN Decoding, CarsXE, and More"
date: 2026-03-15T14:30:00+09:00
description: "Automotive and vehicle MCP servers are connecting AI agents to vehicle data, diagnostics, and automotive workflows. We reviewed 15+ servers across 6 subcategories. Tesla: cobanov/teslamate-mcp (103 stars, Python, MIT — 18+ predefined queries plus custom SQL against TeslaMate PostgreSQL for battery health, efficiency analytics, charging patterns, driving history), scald/tesla-mcp (11 stars, TypeScript — Tesla Fleet API OAuth 2.0, wake vehicle, battery status, vehicle details). OBD-II Diagnostics: castlebbs/Embedded-MCP-ELM327 (C firmware on FreeRTOS/lwIP — runs MCP server directly on OBD-II dongle hardware, supports CAN/J1850/ISO 9141 protocols, built-in simulator), castlebbs/Vehicle-Diagnostic-Assistant (Python, Gradio 6, LangChain — 8+ tools for OBD-II PID queries, response decoding, NHTSA VIN decoder, YouTube search), farzadnadiri/MCP-CAN (Python, MIT — virtual CAN bus, DBC-driven encoding/decoding, ECU simulator, OBD-II requests via SSE). Vehicle Data & VIN: carsxe/carsxe-mcp-server (12 stars, Node.js — official vendor, specs/history/images/recalls/market value/VIN decode including OCR), keptlive/vin-mcp (JavaScript — free VIN decoder aggregating 6 sources, local checksum validation, no API keys needed, self-hostable at mcp.vin), viguza/nhtsa-mcp-server (NHTSA vPIC API wrapper — VIN decoding, vehicle makes/models, manufacturer details, Canadian specs). Car Marketplace: SiddarthaKoppaka/car_deals_search_mcp (JavaScript, Puppeteer — aggregates Cars.com/Autotrader/KBB listings with stealth scraping), yusaaztrk/car-price-mcp (Brazilian FIPE API — cars/motorcycles/trucks pricing). EV Charging: Abiorh001/mcp_ev_assistant_server (Python — charge station locator, EV trip planner). Commercial: AutoUnify ServiceMCP (Porsche AG + UP.Labs venture — AI-commerce for dealership service scheduling via natural language, cross-DMS compatibility). Rating: 3.0/5."
og_description: "Automotive MCP servers: TeslaMate MCP (103 stars, 18+ queries for battery/efficiency/charging analytics), Embedded-MCP-ELM327 (MCP on OBD-II hardware), CarsXE (official vendor, VIN/specs/recalls/market value), VIN MCP (free decoder, 6 sources), MCP-CAN (virtual CAN bus), car marketplace aggregators, EV charging assistant. Rating: 3.0/5."
content_type: "Review"
card_description: "Automotive and vehicle MCP servers for Tesla data analytics, OBD-II diagnostics, VIN decoding, vehicle marketplace search, and EV charging. The category is surprisingly innovative at the hardware level — castlebbs/Embedded-MCP-ELM327 runs MCP server firmware directly on an OBD-II dongle, making it one of the most technically novel projects in the entire MCP ecosystem. cobanov/teslamate-mcp (103 stars, MIT) is the clear star-count leader with 18+ predefined queries against TeslaMate's PostgreSQL database for battery health, efficiency analytics, charging patterns, and driving history, plus custom SQL support. scald/tesla-mcp (11 stars, TypeScript) offers direct Tesla Fleet API access via OAuth 2.0 for real-time vehicle status. farzadnadiri/MCP-CAN (Python, MIT) provides a virtual CAN bus environment with DBC-driven encoding/decoding, ECU simulation, and OBD-II request tools — useful for automotive software development without physical hardware. carsxe/carsxe-mcp-server (12 stars, Node.js) is the only official vehicle data vendor with an MCP server, offering specs, history reports, images, safety recalls, market values, and VIN/license plate decoding. keptlive/vin-mcp provides free VIN decoding by aggregating 6 data sources with local checksum validation — no API keys required. viguza/nhtsa-mcp-server wraps the official NHTSA vPIC API for government vehicle safety data. SiddarthaKoppaka/car_deals_search_mcp aggregates listings from Cars.com, Autotrader, and KBB via parallel Puppeteer scraping. AutoUnify ServiceMCP, a Porsche AG and UP.Labs joint venture, represents the most significant OEM-adjacent entry — AI-powered dealership service scheduling with cross-DMS compatibility. Major gaps: no official MCP servers from any automaker (Tesla, GM, Ford, BMW, Mercedes, Toyota all absent); no ADAS or autonomous driving simulation integration (CARLA has no MCP bridge); no vehicle fleet management; no COVESA Vehicle Signal Specification bridge; no Smartcar API wrapper; no connected car telematics beyond Tesla; no aftermarket parts catalogs; no insurance telematics; no autonomous vehicle sensor data processing. The category earns 3.0/5 — genuinely innovative projects at the embedded and diagnostic levels, but the absence of OEM participation and the small ecosystem size limit practical adoption for most automotive use cases."
---

Automotive MCP servers are connecting AI agents to vehicle data, diagnostics systems, and automotive workflows. Instead of manually querying Tesla's API, plugging into an OBD-II scanner, or searching multiple car listing sites, these servers let AI assistants retrieve battery health metrics, decode VIN numbers, run CAN bus diagnostics, search vehicle marketplaces, and plan EV charging routes — all through the Model Context Protocol.

The landscape spans six areas: **Tesla & EV data** (TeslaMate analytics, Fleet API access), **OBD-II diagnostics** (embedded firmware on OBD-II hardware, CAN bus simulation), **vehicle data & VIN** (vendor APIs, NHTSA safety data, free decoders), **car marketplace search** (listing aggregation, pricing), **EV charging** (station location, trip planning), and **commercial/dealership** (OEM-adjacent service scheduling).

The headline findings: **OBD-II is where the innovation is** — the Embedded-MCP-ELM327 project runs MCP server firmware directly on an OBD-II dongle, making it one of the most technically creative projects in the entire MCP ecosystem. **Tesla has the best coverage** — two dedicated servers reflecting its API-friendly ecosystem and the TeslaMate community. **No major automaker has an official MCP server** — Tesla, GM, Ford, BMW, Mercedes, and Toyota are all absent, leaving community implementations to fill the gap. **CarsXE is the only vehicle data vendor** with an official MCP server. **The biggest gap is connected car telematics** — no Smartcar, no COVESA/VSS bridge, no fleet management, and no ADAS integration exist.

## Tesla & EV Data

### teslamate-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cobanov/teslamate-mcp](https://github.com/cobanov/teslamate-mcp) | ~103 | Python | MIT | 18+ queries + custom SQL |

The **highest-starred automotive MCP server** and the most feature-rich Tesla integration. Connects to an existing [TeslaMate](https://github.com/adriankumpf/teslamate) PostgreSQL database to expose:

- **Battery health analytics** — degradation tracking, charge cycle history, state of charge over time
- **Efficiency metrics** — energy consumption per trip, regenerative braking effectiveness
- **Charging patterns** — preferred stations, charge speed analysis, cost tracking
- **Driving history** — trip logs, distance summaries, speed patterns
- **Custom SQL** — write arbitrary queries with built-in validation against the TeslaMate schema
- **Database schema exploration** — discover available tables and columns

Requires an existing TeslaMate installation (which itself requires a Tesla account and vehicle). Docker deployment supported. Optional bearer token authentication for security.

The key insight here: TeslaMate already has a large community (~5K+ stars) of Tesla owners who self-host detailed vehicle telemetry. This MCP server makes all that collected data queryable by AI agents. For Tesla owners who already run TeslaMate, this is genuinely useful — you can ask your AI assistant "what's my battery degradation over the past year?" and get an answer from your own data.

### tesla-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [scald/tesla-mcp](https://github.com/scald/tesla-mcp) | ~11 | TypeScript | — | 3+ |

Direct **Tesla Fleet API** integration via OAuth 2.0. Simpler than teslamate-mcp — doesn't require a TeslaMate installation, but provides real-time rather than historical data:

- Wake vehicle from sleep
- Refresh and list vehicles on account
- Get vehicle details (battery level, charging status, location, climate)
- Security checker script to detect leaked credentials

Available at tesla.async.fyi. This is for Tesla owners who want real-time vehicle status rather than historical analytics. The credential security checker is a thoughtful addition — Tesla API tokens are high-value targets.

## OBD-II Diagnostics

### Embedded-MCP-ELM327

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [castlebbs/Embedded-MCP-ELM327](https://github.com/castlebbs/Embedded-MCP-ELM327) | New | C (FreeRTOS/lwIP) | — | 2+ |

The **most technically innovative automotive MCP server** — and arguably one of the most creative projects in the entire MCP ecosystem. This is custom firmware that runs an MCP server directly on an inexpensive OBD-II dongle (W600 chip):

- **MCP HTTP Streamable transport** — full JSON-RPC 2.0 over WiFi from the OBD-II hardware
- **Complete ELM327 command interface** — supports CAN, J1850, ISO 9141, and other vehicle communication protocols via UART
- **Built-in simulator** — test without connecting to a real vehicle
- **FreeRTOS/lwIP stack** — real-time embedded operating system with lightweight TCP/IP

The idea is striking: plug an OBD-II dongle into your car, and your AI assistant can directly query the vehicle's diagnostic systems through MCP. No laptop middleware, no phone app relay — the MCP server runs on the $5 hardware in your car's OBD-II port. Born from a hackathon project, so production readiness is limited, but the concept demonstrates where automotive MCP could go.

### Vehicle-Diagnostic-Assistant

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [castlebbs/Vehicle-Diagnostic-Assistant](https://github.com/castlebbs/Vehicle-Diagnostic-Assistant) | New | Python | — | 8+ |

A **full AI diagnostic agent** with a Gradio web interface, designed as a companion to the Embedded-MCP-ELM327 server. Tools include:

- System status monitoring
- ELM327 command execution
- OBD-II PID queries (engine RPM, coolant temp, fuel system status, etc.)
- Historical data retrieval
- Response decoding (hex to human-readable)
- NHTSA VIN decoder integration
- YouTube search (for repair tutorials based on diagnostic codes)

Uses LangChain/LangGraph for agent orchestration with Nebius AI or Anthropic Claude as the LLM backend. Streaming responses via Gradio 6. The YouTube search integration is clever — when a diagnostic code appears, the agent can find relevant repair videos. Built for the same Anthropic Gradio MCP hackathon as the embedded server.

### MCP-CAN

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [farzadnadiri/MCP-CAN](https://github.com/farzadnadiri/MCP-CAN) | New | Python | MIT | Multiple |

A **virtual CAN bus environment** for automotive software development — no physical hardware required:

- **Virtual CAN backend** — python-can library with configurable bus interfaces
- **DBC-driven encoding/decoding** — industry-standard DBC files via cantools for translating raw CAN frames to human-readable signals
- **ECU simulator** — streams multiple CAN messages and responds to OBD-II requests
- **MCP tools via SSE** — CAN frame reading, filtering, monitoring, DBC info, OBD requests
- **Typer CLI** — commands for simulate, server, frames, decode, monitor, obd-request

Optional SocketCAN/vCAN support on Linux for real hardware. This is primarily useful for automotive engineers and embedded developers who need to test CAN bus interactions without a vehicle. The DBC file support is important — DBC is the industry standard for describing CAN bus message formats, and having it built into an MCP server means AI agents can understand what CAN frames actually mean rather than working with raw hex.

## Vehicle Data & VIN Decoding

### CarsXE MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [carsxe/carsxe-mcp-server](https://github.com/carsxe/carsxe-mcp-server) | ~12 | Node.js | — | Multiple |

The **only official vehicle data vendor** with an MCP server. CarsXE provides a comprehensive vehicle data API, and their MCP server exposes:

- Vehicle specifications (make, model, year, engine, transmission, dimensions)
- Vehicle history reports
- Vehicle images
- Safety recalls
- Market value estimates
- License plate decoding
- VIN decoding (including OCR from images)
- Markdown-formatted output optimized for LLM consumption

Both local (stdio) and remote server variants available. Modular and extensible architecture. Requires a CarsXE API key (pay-as-you-go pricing). The OCR VIN decoding is a nice touch — photograph a VIN plate and get full vehicle details.

### VIN MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [keptlive/vin-mcp](https://github.com/keptlive/vin-mcp) | New | JavaScript | — | Multiple |

A **free, zero-API-key VIN decoder** that aggregates 6 data sources into a single response:

- VIN validation computed locally (checksum verification, WMI country/manufacturer identification, model year decoding) — no API calls needed for basic validation
- Full vehicle data aggregation from multiple free sources
- Self-hostable or use the hosted version at mcp.vin
- Rate limited at 30 requests/minute

The local validation is the standout feature — the VIN standard (ISO 3779) includes a check digit algorithm that can verify a VIN's validity entirely offline. For basic "is this VIN real and what make/year is it?" queries, no external API call is needed.

### NHTSA MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [viguza/nhtsa-mcp-server](https://github.com/viguza/nhtsa-mcp-server) | New | — | — | 6+ |

Wraps the official **NHTSA vPIC (Vehicle Product Information Catalog) API** — the authoritative U.S. government source for vehicle safety data:

- VIN decoding via NHTSA's database
- Vehicle makes and models by year
- Manufacturer details
- World Manufacturer Identifier (WMI) lookup
- Vehicle variables and specifications
- Canadian vehicle specifications

Provides both MCP resources (for direct data access) and MCP tools (for queries). Free government data source — no API key required. Useful for safety recalls, regulatory compliance, and vehicle identification where authoritative data matters.

## Car Marketplace & Pricing

### car_deals_search_mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SiddarthaKoppaka/car_deals_search_mcp](https://github.com/SiddarthaKoppaka/car_deals_search_mcp) | New | JavaScript | — | 1 |

**Multi-platform car listing aggregator** using Puppeteer with stealth:

- Searches Cars.com, Autotrader, and KBB in parallel
- Extracts price, mileage, dealer information
- Optional CARFAX-style filters (1-owner, no accidents, personal use only)
- Normalizes data from different sources into a common schema
- Stealth plugin to avoid bot detection

A single `search_car_deals` tool that does the heavy lifting. The parallel scraping across three major platforms and data normalization into a common format is practical — comparing listings across Cars.com, Autotrader, and KBB manually is exactly the kind of tedious task AI agents should handle. The scraping approach means this could break if the target sites change their markup.

### car-price-mcp (Brazil / FIPE)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [yusaaztrk/car-price-mcp-main](https://github.com/yusaaztrk/car-price-mcp-main) | New | — | — | 3+ |

**Brazilian vehicle pricing** via the FIPE (Fundação Instituto de Pesquisas Econômicas) API:

- Brand retrieval across vehicle categories
- Model and price search
- Vehicle type filtering (cars, motorcycles, trucks)
- Production year and fuel type data
- Current market reference prices

FIPE is the standard pricing reference for used vehicles in Brazil — equivalent to Kelley Blue Book in the U.S. Regional but authoritative for its market.

## EV Charging & Trip Planning

### mcp_ev_assistant_server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Abiorh001/mcp_ev_assistant_server](https://github.com/Abiorh001/mcp_ev_assistant_server) | New | Python | — | 2+ |

An **EV-focused assistant server** with:

- Charging station locator — find nearby stations by location
- EV trip planner — plan routes with charging stops based on vehicle range
- Resource management for EV services

Basic but addresses a real pain point for EV owners — range anxiety and charging logistics. The trip planning with charging stops is the key feature, though the implementation details (which charging network APIs are used) aren't well documented.

## Commercial & Dealership

### AutoUnify ServiceMCP

| Vendor | Type | Origin |
|--------|------|--------|
| AutoUnify (Porsche AG + UP.Labs) | Commercial | Official |

The **most significant OEM-adjacent entry** in the automotive MCP space. AutoUnify is a joint venture between Porsche AG and UP.Labs that launched ServiceMCP in May 2025:

- AI-powered dealership service scheduling via natural language
- Cross-DMS (Dealer Management System) compatibility
- Cross-SMS integration
- Anti-abuse protections
- Described as the "first AI-commerce tool for automotive"

Not open source — this is a commercial product targeting the dealership ecosystem. But it signals that the automotive industry's largest players are paying attention to MCP. The Porsche backing lends credibility, and the cross-DMS compatibility addresses a real problem — dealerships typically use fragmented software systems that don't communicate well.

### Fullpath

Fullpath, a Customer Data Platform vendor for automotive dealerships, has published thought leadership on MCP servers for dealerships — positioning their CDP as a unified data layer for multi-agentic AI systems connecting CRM, DMS, F&I, and fixed operations. Not an open-source MCP server, but indicates commercial interest in the space.

## What's Missing

The automotive MCP ecosystem has significant gaps:

- **No OEM servers** — not a single automaker (Tesla, GM, Ford, BMW, Mercedes, Toyota, Honda, Volkswagen) has published an official MCP server. Tesla's community fills the gap; everyone else has nothing.
- **No ADAS / autonomous driving** — no CARLA simulation bridge, no sensor data processing, no autonomous vehicle development tools. The "carla-mcp-server" on GitHub is for the Carla *audio plugin host*, not the CARLA driving simulator.
- **No vehicle fleet management** — fleet MCP servers that exist are for IT device fleets (osquery), not vehicle fleets. No Geotab, Samsara, or Verizon Connect integration.
- **No COVESA / VSS bridge** — the Connected Vehicle Systems Alliance's Vehicle Signal Specification is the emerging standard for vehicle data, but no MCP server bridges it.
- **No Smartcar API** — Smartcar provides a unified API across 36+ car brands, which would be the ideal foundation for a multi-OEM MCP server. No wrapper exists.
- **No connected car telematics** beyond Tesla — no GM OnStar, Ford SYNC, BMW ConnectedDrive, or Mercedes me connect integration.
- **No aftermarket parts** — no AutoZone, O'Reilly, RockAuto, or NAPA parts catalog servers.
- **No insurance telematics** — no driving behavior scoring or usage-based insurance data servers.
- **No commercial vehicles** — no truck-specific servers (no J1939 CAN protocol support beyond what MCP-CAN provides).

## The Bottom Line

The automotive MCP ecosystem earns **3.0 out of 5**. The technical innovation is impressive — running MCP firmware on an OBD-II dongle is genuinely creative, and the TeslaMate integration demonstrates real utility for Tesla owners. CarsXE is the only vehicle data vendor with an official server, and the VIN decoding options are practical. But the category is held back by the complete absence of OEM participation, tiny community sizes (most servers have single-digit stars), and massive gaps in connected car, fleet management, and autonomous driving coverage. The automotive industry is one of the largest in the world, and its MCP tooling doesn't reflect that yet.

| Rating | Score |
|--------|-------|
| Breadth of coverage | 2.5/5 |
| Quality of implementations | 3.0/5 |
| Community adoption | 2.5/5 |
| Technical innovation | 4.0/5 |
| Vendor participation | 2.0/5 |
| **Overall** | **3.0/5** |
