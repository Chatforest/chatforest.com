---
title: "MCP and Maritime/Ocean: How AI Agents Connect to Vessel Tracking, AIS Data, Port Operations, Oceanographic Science, Shipping Logistics, Marine Weather, Naval Architecture, and Maritime Compliance Tools"
date: 2026-03-29T23:00:00+09:00
description: "A comprehensive guide to 85+ MCP integrations for the maritime and ocean sector — covering vessel tracking and AIS data (MarineTraffic 9 stars, ShipXY 9 stars, Datalastic"
content_type: "Guide"
card_description: "The maritime industry moves 90% of global trade across 50,000+ merchant vessels, yet its data systems remain deeply fragmented — AIS feeds in one system, weather in another, port schedules in a third, compliance databases elsewhere. This guide covers 85+ MCP servers relevant to the maritime and ocean sector, from vessel tracking and oceanographic data to shipping logistics, marine weather, naval architecture, satellite imagery, and maritime compliance — plus architecture patterns for AI-powered fleet intelligence, smart port operations, and autonomous vessel monitoring."
last_refreshed: 2026-03-29
---

The maritime industry is the backbone of global trade. Over 90% of the world's goods travel by sea, carried by more than 50,000 merchant vessels across a network of 835+ major ports. Yet this enormous industry runs on remarkably fragmented data systems. AIS vessel tracking feeds live in one platform, weather and sea state data in another, port schedules in a third, customs and compliance databases elsewhere, and cargo tracking systems scattered across dozens of shipping lines and freight forwarders. A single container shipment from Shanghai to Rotterdam might touch 30+ different information systems before delivery.

The global AI-in-maritime market reached approximately $4.3–6.2 billion in 2025, growing at 15–40% CAGR depending on scope. The smart port and automated terminal market stands at $11.3 billion heading toward $22.4 billion by 2035. Marine IoT is a $4.85 billion market growing to $12.31 billion by 2032. CMA CGM, the world's third-largest container shipping line, announced a strategic partnership with Google for AI-powered route optimization. Lloyd's Register research found 36 shipping companies actively implementing or planning AI adoption, with SMEs making up 63% of maritime AI technology suppliers.

MCP — the Model Context Protocol — provides a standardized way for AI agents to connect to the maritime industry's fragmented data landscape. Rather than building custom integrations for each vessel tracking platform, weather service, port system, or compliance database, MCP-connected agents can query vessel positions, analyze ocean conditions, track shipments, check sanctions lists, and monitor port operations through defined tool interfaces. The protocol transforms AI assistants from isolated chatbots into operational maritime intelligence tools that work across the entire shipping lifecycle — from route planning and vessel tracking through port operations, cargo management, and regulatory compliance. For an introduction to MCP itself, see our [introduction to MCP](/guides/what-is-mcp/).

The maritime MCP ecosystem is still in its earliest stages. Unlike database or DevOps categories with 100+ mature servers, the maritime sector has fewer than 35 dedicated MCP servers, most with single-digit GitHub stars and created in 2025–2026. However, the adjacent tooling — weather, GIS, IoT, satellite imagery, shipping carriers, CAD, compliance — is substantially richer, and these components can be assembled into powerful maritime AI workflows.

This guide is research-based. We survey what MCP servers exist across the maritime and ocean landscape, analyze the architecture patterns they enable, and identify where significant gaps remain. We do not claim to have tested or used any of these servers hands-on — our analysis draws on published documentation, open-source repositories, vendor announcements, and industry research. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI. For background on MCP, see our [introduction to MCP](/guides/what-is-mcp/) and the [MCP server directory](/reviews/).

## Why Maritime Needs MCP

Maritime operations present integration challenges that MCP is architecturally well-suited to address.

**Vessel tracking data is global, real-time, and multi-source.** The Automatic Identification System (AIS) broadcasts vessel positions from 300,000+ ships worldwide, but this data flows through competing providers — MarineTraffic, VesselFinder, FleetMon, Spire Global, exactEarth — each with different APIs, coverage, and pricing. An MCP-connected AI agent that can query across tracking providers, correlate positions with weather data, and cross-reference against compliance databases could provide unified maritime domain awareness without vendor lock-in.

**Port operations are a coordination nightmare.** A single large container port handles thousands of vessel calls per year, coordinating berth allocation, crane scheduling, truck gates, rail connections, customs clearance, and pilot services — each managed by different systems. China already operates 52 robotic ports where AI achieves 95% truck-crane coordination. MCP servers bridging port systems could let AI agents optimize the entire port call cycle rather than individual subsystems.

**Regulatory compliance spans multiple jurisdictions and agencies.** Maritime vessels must comply with IMO conventions (SOLAS, MARPOL, STCW, MLC), flag state regulations, port state control requirements, sanctions regimes (OFAC, EU, UN), and increasingly stringent cybersecurity rules (IACS UR E26/E27 mandatory for newbuilds since July 2024, US Coast Guard cyber incident reporting effective July 2025). AI agents with MCP access to regulatory databases, sanctions lists, and compliance monitoring tools could transform how shipping companies manage their regulatory obligations.

**Weather and ocean conditions drive every routing decision.** Voyage optimization requires integrating weather forecasts, ocean currents, wave heights, sea ice data, and port weather windows into route planning. Current systems treat weather as a separate input rather than a continuous factor. MCP-connected AI agents that can query multiple weather sources, ocean models, and hurricane tracking systems could provide real-time route optimization that adapts to changing conditions.

**Autonomous vessels are approaching regulatory reality.** The IMO finalized its non-mandatory code for Maritime Autonomous Surface Ships (MASS) in 2026, with a mandatory framework expected by 2030. Companies like Rolls-Royce and Kongsberg are testing autonomous operations. MCP provides the integration layer these systems need to coordinate with traffic management, weather services, port systems, and regulatory authorities.

## Vessel Tracking and AIS Data

Vessel tracking through AIS is the most fundamental maritime data source. Several MCP servers now provide access to AIS feeds and vessel intelligence.

### MarineTraffic MCP Server — AIS Vessel Tracking

**Cyreslab-AI/marinetraffic-mcp-server** | 9 stars | TypeScript | Smithery-listed

According to repository documentation, this server connects to the MarineTraffic API to provide real-time vessel position tracking by MMSI or IMO number, vessel detail lookups, vessel search, and area-based vessel queries. MarineTraffic is one of the world's largest vessel tracking platforms, and this community-built MCP server makes its data accessible to AI agents. Listed on the Smithery MCP directory for easy discovery and installation.

### ShipXY MCP Server — Comprehensive Maritime Data

**garrettXu/mcp-shipxy-api** | 9 stars | Python

A feature-rich maritime MCP server that goes beyond basic vessel tracking. According to its documentation, it provides ship tracking, fleet queries, port search, berth and anchor status, ETA information, route planning assistance, marine weather data, typhoon tracking, and tide information — all through the ShipXY API. This breadth makes it one of the most comprehensive single-server maritime MCP implementations available, covering vessel operations, port intelligence, and marine weather in one package.

### Datalastic Marine AIS MCP

**robderstadt/datalastic-mcp** | Python

A mature AIS data integration with smart caching and rate limit tracking. According to documentation, it provides vessel tracking, vessel history going back to August 2021, area-based vessel search, port search, and fleet tracking for up to 100 vessels simultaneously. The historical data access is particularly valuable for trade pattern analysis, sanctions investigation, and voyage reconstruction.

### Saillogger AIS MCP

**Saillogger/mcp-server-saillogger** | 1 star | Python

Provides real-time AIS positions from the Saillogger network for AI applications. Saillogger operates its own AIS receiver network, making this a direct-source data feed rather than a reseller API wrapper.

### Additional Vessel Tracking Servers

Several other community-built vessel tracking MCP servers exist in various stages of development:

- **salmangada/marine-traffic-mcp** (Go) — MarineTraffic vessel tracking with MMSI-based queries
- **arifemregursoy/marinetraffic-mcp-server** (Python) — Another MarineTraffic API integration
- **Wipfi/ais_mcp_servers** (Python, 2026) — AIS data MCP servers
- **vessel-api/vesselapi-mcp** (TypeScript) — Tools to access VesselAPI endpoints

The existence of multiple competing vessel tracking MCP servers, all community-built, reflects both the demand for maritime AI integration and the absence of official implementations from major providers.

## Shipping Line and Carrier Integrations

Container shipping and freight logistics involve tracking cargo across multiple carriers, each with their own APIs and data formats.

### Maersk MCP Server

**idipankan/maersk-mcp** | 1 star | Python

According to documentation, this community-built server connects to Maersk's public APIs to provide vessel IMO lookup by name, vessel schedule and deadline information, and port calls for the upcoming week. While not an official Maersk implementation, it demonstrates how shipping line APIs can be exposed through MCP for AI-assisted logistics management.

### Envia MCP — 170+ Carrier Integration

**envia-ep/envia-mcp-server** | TypeScript | **Official vendor implementation**

Envia's official MCP server provides access to their shipping platform covering 170+ carriers across 18 countries. According to documentation, it offers 10 tools including shipping rate comparison, label generation, and package tracking. A separate community implementation (amak07/envia-mcp) also exists. For logistics operations that ship across multiple carriers, this provides unified rate comparison and tracking through a single MCP interface.

### Shipping Rates MCP

**vinaybhosle/shippingrates-mcp-server** | Remote MCP at mcp.shippingrates.org

A specialized server for container shipping costs including detention and demurrage (D&D) charges, local charges, and inland haulage rates. Uses x402-native payment with USDC. This addresses one of the most opaque and contentious areas in container shipping — the ancillary charges that can significantly impact total shipping costs.

### Parcel and Last-Mile Carriers

Several MCP servers cover the parcel and last-mile delivery segment relevant to maritime cargo's final journey:

- **markswendsen-code/mcp-ups** — UPS package tracking and shipping services
- **markswendsen-code/mcp-fedex** — FedEx tracking, shipping rates, location finding, pickup scheduling
- **pocharlies-org/mcp-sendcloud** — SendCloud shipping API covering parcels, returns, labels, and tracking
- **100kgforest/sf-express-mcp-server** — SF Express shipping and logistics (major Asian carrier)
- **hishamalhadi/chitchats-mcp** — Chit Chats shipping with HS code lookups
- **Arseno25/rajaongkir-mcp-server** — Indonesian shipping costs via Komerce API
- **shopanaio/carrier-api** | 5 stars — Enterprise-grade multi-carrier shipping API clients and MCP servers

### E-commerce Fulfillment with Shipping

Several e-commerce MCP servers include shipping and fulfillment capabilities relevant to the cargo lifecycle:

- **Purple-Horizons/printful-mcp** | 1 star — Printful print-on-demand with 17 tools including fulfillment
- **karimsherifyehia/nexus-mcp-server** | 1 star — Agent-native e-commerce with CRM, orders, inventory, and shipping

## Oceanographic Science and Marine Data

Ocean science generates massive datasets from buoys, satellites, floats, and research vessels. The OceanMCP project stands out as the most comprehensive implementation in the entire maritime MCP ecosystem.

### OceanMCP — Eight-Server Monorepo

**mansurjisan/ocean-mcp** | 2 stars | Python | All servers published to PyPI

This is the most significant find in maritime MCP. According to documentation, OceanMCP provides eight independently installable oceanography MCP servers, each focused on a specific data domain:

1. **coops-mcp** — NOAA CO-OPS tidal data including water levels, currents, tide predictions, and meteorological observations from 200+ stations
2. **erddap-mcp** — Access to 80+ ERDDAP (Environmental Research Division Data Access Program) servers worldwide, which host vast ocean science datasets
3. **nhc-mcp** — National Hurricane Center data including active storm tracks, advisories, forecast cones, and historical hurricane data
4. **recon-mcp** — Hurricane reconnaissance flight data from NOAA and Air Force Reserve missions
5. **stofs-mcp** — NOAA storm surge forecasts for coastal planning and emergency preparedness
6. **ofs-mcp** — NOAA regional operational ocean forecast systems (currents, temperature, salinity)
7. **rtofs-mcp** — Global Real-Time Ocean Forecast System via HYCOM (HYbrid Coordinate Ocean Model)
8. **ww3-mcp** — WAVEWATCH III global wave model forecasts plus NDBC (National Data Buoy Center) real-time buoy data

For maritime operations, this suite provides the ocean intelligence foundation that route optimization, port operations, and safety management all depend on. An AI agent connected to these servers could correlate hurricane forecasts with vessel positions, overlay wave conditions on planned routes, monitor storm surge at destination ports, and track real-time buoy data along shipping lanes.

### Oceanum Datamesh MCP

**oceanum-io/oceanum-mcp** | 1 star | Python | Vendor implementation

A datamesh MCP server from Oceanum.io, a company specializing in ocean data services. This represents one of the few vendor-built maritime science MCP implementations, providing structured access to ocean datasets through Oceanum's data platform.

### Tide and Wave Prediction Servers

Several focused servers provide tidal and wave data:

- **seanofahey/mcp-noaa-tides** | 1 star — Direct NOAA tide data access
- **Polly2014/TideWatch-MCP-Server** — Tide monitoring and prediction
- **godshinee/MCP-test** — Ocean wave and tide prediction system with Next.js dashboard and LangChain chatbot integration

### IBM Maritime Archives — Historical Intelligence

**IBM/chuk-mcp-maritime-archives** | 3 stars | Python | Vendor (IBM)

A unique server providing access to historical maritime archives spanning five nations — Dutch, English, Portuguese, Spanish, and Swedish records. According to documentation, it supports wreck searches, voyage records, and crew data. While primarily of historical and academic interest, maritime archive data has practical applications in marine archaeology, salvage operations, and understanding historical shipping routes and hazards.

### SHOM Wrecks Database

**dorian-erkens/mcp-shom-wrecks** | 1 star | TypeScript

Queries the SHOM (Service Hydrographique et Océanographique de la Marine — French Hydrographic Service) wreck database via the WFS API standard. Wreck data is operationally important for routing in coastal waters, anchor planning, and marine construction projects.

## Marine Weather and Forecasting

Weather is the single most impactful variable in maritime operations. Several MCP servers provide marine-specific weather data.

### Open-Meteo Marine Weather

**cmer81/open-meteo-mcp** | 37 stars | Comprehensive Open-Meteo access

The most popular weather MCP server with marine capabilities. Open-Meteo provides free weather APIs including marine-specific data — wave height, wave period, wave direction, swell components, and sea surface temperature. According to documentation, this server provides comprehensive access to Open-Meteo's full API suite including marine weather endpoints.

### Surf and Marine Forecast Servers

- **lucasinocencio1/mcp-surf-forecast** | 18 stars — Open-Meteo Marine API providing swell height, period, direction, wind conditions with global coverage
- **enricollen/surf-forecast-mcp** | 3 stars — Marine forecast data from OpenMeteo
- **weather-mcp/weather-mcp** | 4 stars — 12 tools including marine conditions, lightning, weather radar, river monitoring, and wildfire data — no API key required

### General Weather Servers with Marine Data

Several broad weather MCP servers include marine condition endpoints:

- **QuentinCody/open-meteo-mcp-server** — Weather forecasts, historical data, air quality, marine conditions, climate projections
- **bhayanak/weather-mcp-server** — Forecasts, historical data, air quality, marine conditions, geocoding, elevation at 1km resolution with 80+ year archive
- **ToolOracle/weatheroracle** — 10 tools covering current conditions, forecast, air quality, marine data, and astronomy
- **ezh0v/weather-mcp-server** | 239 stars — The highest-starred weather MCP server overall; real-time weather data for AI assistants

### Lightning-Gated Marine Weather

**Blue-Trianon-Ventures/l402-apis** — A novel approach offering sanctions screening, aviation weather, marine forecasts, and crypto data through pay-per-request Bitcoin Lightning payments. This micropayment model could become relevant for maritime AI agents that need occasional data access without subscription commitments.

## Maritime Intelligence and Compliance

Maritime compliance involves sanctions screening, anti-money laundering checks, and regulatory adherence across multiple jurisdictions.

### Maritime Shipping Intelligence

**Ryan-Clinton/maritime-shipping-intelligence-mcp** | 2026

According to repository documentation, this server provides maritime shipping intelligence including sanctions data, supply chain information, and port data. For compliance teams, this type of integrated intelligence — correlating vessel movements with sanctions lists and supply chain data — is essential for due diligence in trade finance and chartering.

### Maritime Resource Compliance Servers

Two separate compliance-focused servers have emerged:

- **Ryan-Clinton/maritime-resource-compliance-mcp** — Maritime compliance, sanctions, shipping supply chain data
- **apifyforge/maritime-resource-compliance-mcp** — Fishing quotas, oil and gas licenses, waste carrier permits, and coastal hazard data via Apify web scraping

### AML Watcher — Anti-Money Laundering Screening

**Tech-AML/AML-watcher-MCP-Server** | 2025

Provides anti-money laundering screening for vessels, aircraft, companies, and individuals against sanctions and PEP (Politically Exposed Persons) databases. In maritime trade, sanctions screening of vessels, owners, and beneficial owners is a critical compliance requirement — particularly for ship finance, chartering, and port services.

### Investment and Market Intelligence

**liqiqiii/investment-mcp** — Personal investment analysis including VLCC (Very Large Crude Carrier) and shipping market data, reflecting the intersection of maritime operations and financial markets. Shipping indices like the Baltic Dry Index and tanker rates are key inputs for commodity trading and maritime investment decisions.

## Naval Architecture and Shipbuilding

Ship design and construction involve specialized engineering tools. A few MCP servers have begun addressing this domain.

### Shipbuilding Specifications

**contextkits/shipbuilding-specs** | Python | 2026

Provides maritime vessel specifications and shipbuilding requirements through MCP. For naval architects and shipyard engineers, having specification data accessible to AI agents could accelerate design verification, regulatory compliance checks, and technical documentation.

### Naval Shipbuilding Standards

**contextkits/naval-shipbuilding-standards** | Python | 2026

Focuses on naval (military) vessel specifications and NAVSEA shipbuilding standards. Military shipbuilding follows additional standards beyond commercial classification rules, and this server aims to make those standards accessible to AI-assisted design workflows.

### CAD Tools for Marine Engineering

While no MCP servers are specifically designed for marine CAD, the general CAD MCP ecosystem is directly applicable to ship design:

- **daobataotie/CAD-MCP** | 286 stars — General CAD MCP server
- **ATOI-Ming/FreeCAD-MCP** | 68 stars — FreeCAD automation for open-source 3D modeling
- **AuraFriday/Fusion-360-MCP-Server** | 64 stars — Autodesk Fusion 360 control
- **mixelpixx/KiCAD-MCP-Server** | 535 stars — PCB design relevant to marine electronics and bridge systems
- **BLamy/onshape-mcp** | 11 stars — Onshape cloud CAD
- **rishigundakaram/cadquery-mcp-server** | 10 stars — Parametric CAD generation via CadQuery
- **tylerwagler/SolidEdge-MCP** | 4 stars — Solid Edge AI-assisted CAD
- **AnCode666/multiCAD-mcp** | 17 stars — Multi-CAD software access

Naval architecture packages like NAPA, AVEVA Marine, Maxsurf, and DNV Sesam have not yet released MCP integrations — a significant gap given these are the standard tools for ship structural design, stability analysis, and hydrodynamic evaluation.

## Satellite Imagery and Earth Observation

Satellite data is increasingly central to maritime operations — from monitoring vessel activity in remote waters to tracking port congestion and environmental conditions.

### Earth Agent — Google Earth Engine

**wybert/earth-agent-chrome-ext** | 99 stars | TypeScript

An AI agent for Google Earth Engine that can write code, run analysis, debug, and manage the GEE environment. For maritime applications, GEE provides global satellite imagery archives useful for monitoring port development, coastal erosion, oil spill detection, sea ice coverage, and vessel detection in areas without AIS coverage.

### NASA MCP Servers

- **ProgramComputer/NASA-MCP-server** | 83 stars — NASA APIs including Earth observation imagery
- **datalayer/earthdata-mcp-server** | 24 stars — NASA Earthdata access covering ocean data and satellite observations

### Copernicus and Sentinel

- **wb1016/copernicus-mcp** | 2 stars — ESA Copernicus OData API for European satellite imagery
- **ginkgo-tech/sentinelhub-mcp** — Copernicus Sentinel Hub satellite image interaction with LLMs

Copernicus Sentinel satellites provide free, open data particularly relevant to maritime: Sentinel-1 SAR imagery for vessel detection and oil spill monitoring, Sentinel-2 optical imagery for coastal monitoring, and Sentinel-3 for ocean color and sea surface temperature.

### Geophysical Intelligence

**DeepMapAI/deepmap-mcp-server** | 1 star | Python | Vendor

Provides 25 tools including risk scoring, earthquake/volcano/tsunami prediction, weather assessment, insurance risk analysis, and climate data. For maritime operations, tsunami prediction and coastal hazard assessment are directly relevant to port operations and routing in seismically active regions.

## Industrial IoT and Vessel Systems

Modern vessels are floating sensor networks, generating continuous telemetry from engines, navigation systems, cargo holds, ballast tanks, and safety equipment.

### IoT Edge MCP Server

**poly-mcp/IoT-Edge-MCP-Server** | 22 stars | Python

According to documentation, this server provides industrial IoT and SCADA integration through MCP, supporting MQTT sensors, Modbus devices, real-time monitoring, alarm management, time-series data, and actuator control. For vessel systems, MQTT and Modbus are common protocols connecting bridge equipment, engine room sensors, and cargo monitoring systems. An AI agent connected through this server could monitor engine performance, track fuel consumption, detect anomalies in ballast systems, and manage alarm conditions.

### MQTT and Sensor Data Servers

- **Benniu/emqx-mcp-server** | 23 stars — EMQX MQTT broker interaction, relevant for ship-to-shore data transmission
- **ezhuk/mqtt-mcp** | 12 stars — Generic MQTT MCP server for sensor data streams
- **Duke-CEI-Center/IoT-MCP-Servers** | 10 stars — IoT device integration for reading sensor data and dispatching collection tasks

### SCADA Systems

- **vogler75/winccua-mcp-server** | 9 stars — Siemens WinCC Unified SCADA
- **vogler75/winccv8-mcp-server** | 8 stars — Siemens WinCC V8 SCADA

Siemens SCADA systems are used in port automation, vessel monitoring, and marine infrastructure. These MCP servers could provide AI agents access to the operational technology (OT) systems that control physical port and vessel equipment.

### Time-Series Data for Vessel Telemetry

- **influxdata/influxdb3_mcp_server** | 29 stars — **Official InfluxDB 3 MCP server** for time-series data, ideal for storing and querying vessel sensor data, engine performance metrics, and environmental measurements
- **idoru/influxdb-mcp-server** | 33 stars — Community InfluxDB MCP server

## Simulation and Digital Twins

Digital twins — virtual replicas of physical assets — are gaining traction in maritime for port optimization, vessel performance modeling, and autonomous systems testing. Research indicates 65% of logistics providers prefer AI-driven digital twins over traditional planning methods.

### Simulation MCP Servers

- **omni-mcp/isaac-sim-mcp** | 140 stars — NVIDIA Isaac Simulation MCP, relevant for autonomous vessel simulation and testing
- **game4automation/io.realvirtual.mcp** | 6 stars — Unity-based digital twin simulations, applicable to port operations modeling
- **IamCatoBot/text2sim-MCP-server** | 19 stars — Natural language to simulation, supporting discrete event simulation (DES) and system dynamics models useful for port throughput and supply chain modeling
- **Wael-Rd/gns3-mcp-server** | 19 stars — Network simulation relevant to ship and port communications infrastructure
- **alti3/stk-mcp** | 25 stars — Ansys STK digital mission engineering, useful for satellite-based maritime surveillance and communication system planning

### CFD and Engineering Simulation

**kimimgo/awesome-ai-cae** | 12 stars — A curated list of 113 AI-ready CAE tools covering CFD, FEA, SPH, neural operators, and MCP servers. Computational fluid dynamics is essential for hull design optimization and hydrodynamic analysis in naval architecture.

## Sailing and Recreational Marine

A small but growing segment serves the sailing and recreational boating community.

### Yachtsy MCP

**manee1112/yachtsy-mcp-server** | TypeScript | Vendor

An AI-driven yacht marketplace with access to 25,000+ listings and sailing advice. Represents the consumer-facing end of the maritime MCP ecosystem.

### Garmin Sailing Analytics

**vinicius-saraiva/garmin-sailing-mcp** | 1 star | Python | 2026

Combines Garmin GPS data with Open-Meteo weather information for sailing performance analytics. This pattern — combining device telemetry with environmental data through MCP — is directly applicable to commercial vessel performance monitoring at larger scale.

## Compliance and Regulatory Tools

Beyond the maritime-specific compliance servers listed above, several general compliance MCP servers are relevant to shipping operations.

### Document Compliance

**arthurpanhku/DocSentinel** | 96 stars — Document assessment for compliance and cybersecurity with multi-format parsing, RAG, and risk detection. Applicable to ISM Code document management, safety management systems, and port state control preparation.

### Insurance and Claims

**chbhargavareddy/ClaimsProcessingAssistant-MCP** | 5 stars — Claims processing via MCP, relevant to marine insurance (P&I clubs, hull and machinery, cargo insurance) which handles billions in claims annually.

### Financial Services

**SecureLend/mcp-financial-services** | 2 stars — Financial services comparison including insurance, relevant to trade finance, letters of credit, and marine insurance procurement.

## GIS and Geospatial Tools for Maritime

Geospatial analysis underpins maritime operations from electronic chart production to port development planning.

### Key GIS MCP Servers for Maritime

- **jjsantos01/qgis_mcp** | 871 stars — QGIS Desktop integration for charting, maritime boundary analysis, and coastal zone management
- **mahdin75/gis-mcp** | 126 stars — Programmatic spatial operations including geometry calculations and coordinate transformations
- **JordanGunn/gdal-mcp** | 59 stars — GDAL-style geospatial workflows for processing maritime spatial data
- **nicogis/MCP-Server-ArcGIS-Pro-AddIn** | 25 stars — ArcGIS Pro integration for enterprise maritime GIS
- **receptopalak/postgis-mcp** | 12 stars — PostGIS spatial database queries for maritime data warehousing
- **Garblesnarff/google-maps-mcp** | 10 stars — Google Maps with 14 tools including location services and environmental data

For maritime applications, these GIS servers enable AI agents to work with nautical charts, maritime boundaries (EEZ, territorial waters, traffic separation schemes), port facility layouts, and environmental protection zones.

## Architecture Patterns

The maritime MCP ecosystem enables several powerful architecture patterns for AI-powered maritime operations.

### Pattern 1: AI Fleet Intelligence Agent

An AI agent that provides unified fleet monitoring by correlating vessel positions with weather, port conditions, and compliance data.

```
                    ┌─────────────────┐
                    │  Fleet Manager   │
                    │   (Human/AI)     │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   AI Fleet      │
                    │  Intelligence   │
                    │    Agent        │
                    └────────┬────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
   ┌────────▼────────┐ ┌───▼────────┐ ┌─────▼──────┐
   │ MarineTraffic   │ │ OceanMCP   │ │  AML       │
   │ MCP Server      │ │ (8 servers)│ │  Watcher   │
   │                 │ │            │ │  MCP       │
   │ • Vessel pos    │ │ • Tides    │ │            │
   │ • Fleet track   │ │ • Waves    │ │ • Sanctions│
   │ • Port calls    │ │ • Storms   │ │ • PEP check│
   │ • Area search   │ │ • Currents │ │ • Vessel   │
   └─────────────────┘ └────────────┘ │   screen   │
                                       └────────────┘
```

**Workflow:** The agent continuously monitors fleet positions via MarineTraffic or ShipXY, overlays weather conditions from OceanMCP's wave and storm forecast servers, and runs compliance checks against sanctions databases. When a vessel approaches a port, the agent queries tide predictions and storm surge forecasts, checks whether the vessel or its registered owner appears on sanctions lists, and generates a pre-arrival risk assessment.

### Pattern 2: Smart Port Operations Agent

An AI agent that optimizes port call operations by integrating vessel schedules, weather windows, and terminal capacity.

```
   ┌──────────┐  ┌──────────┐  ┌──────────┐
   │ Shipping │  │  Port    │  │ Terminal │
   │  Lines   │  │Authority │  │ Operator │
   └────┬─────┘  └────┬─────┘  └────┬─────┘
        │              │              │
        └──────────────┼──────────────┘
                       │
              ┌────────▼────────┐
              │  Smart Port     │
              │  Operations     │
              │  Agent          │
              └────────┬────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
  ┌─────▼─────┐ ┌─────▼─────┐ ┌─────▼─────┐
  │  Maersk   │ │ Weather   │ │ IoT Edge  │
  │  MCP      │ │ MCP       │ │ MCP       │
  │           │ │           │ │           │
  │ • Vessel  │ │ • Marine  │ │ • Crane   │
  │   sched   │ │   forecast│ │   sensors │
  │ • Port    │ │ • Tides   │ │ • Berth   │
  │   calls   │ │ • Wind    │ │   monitors│
  │ • ETA     │ │ • Waves   │ │ • Traffic │
  └───────────┘ └───────────┘ └───────────┘
```

**Workflow:** The agent ingests vessel schedules from shipping line MCP servers, cross-references with marine weather forecasts to identify weather windows for cargo operations (many ports cannot work containers in high winds), monitors terminal equipment status through IoT sensors, and dynamically adjusts berth assignments and crane allocations to maximize throughput.

### Pattern 3: Voyage Optimization Agent

An AI agent that plans and continuously optimizes vessel routes based on weather, currents, fuel costs, and port conditions.

```
              ┌────────────────────┐
              │   Voyage Planning  │
              │      Agent         │
              └────────┬───────────┘
                       │
     ┌─────────────────┼─────────────────┐
     │                 │                 │
┌────▼─────┐    ┌──────▼──────┐   ┌─────▼──────┐
│ OceanMCP │    │  ShipXY MCP │   │  Shipping  │
│          │    │             │   │  Rates MCP │
│ • RTOFS  │    │ • Routes    │   │            │
│   global │    │ • Marine    │   │ • D&D      │
│   ocean  │    │   weather   │   │   charges  │
│ • WW3    │    │ • Typhoons  │   │ • Local    │
│   waves  │    │ • Tides     │   │   charges  │
│ • NHC    │    │ • Ports     │   │ • Inland   │
│   storms │    │ • ETA       │   │   haulage  │
└──────────┘    └─────────────┘   └────────────┘
```

**Workflow:** Before departure, the agent queries global ocean models (RTOFS) for current patterns, wave forecasts (WAVEWATCH III), and active storm systems (NHC). During the voyage, it continuously re-optimizes the route based on updated conditions from ShipXY's marine weather and typhoon tracking. At the destination, it checks port conditions, tide windows for arrival, and calculates total voyage costs including detention and demurrage charges.

### Pattern 4: Maritime Compliance and Due Diligence Agent

An AI agent that performs comprehensive compliance checks for chartering, trade finance, and port operations.

```
              ┌────────────────────┐
              │   Compliance       │
              │   Officer / Agent  │
              └────────┬───────────┘
                       │
     ┌─────────────────┼─────────────────┐
     │                 │                 │
┌────▼─────┐    ┌──────▼──────┐   ┌─────▼──────┐
│  AML     │    │  Maritime   │   │ DocSentinel│
│ Watcher  │    │  Shipping   │   │            │
│          │    │  Intel MCP  │   │ • ISM docs │
│ • Vessel │    │             │   │ • Safety   │
│   screen │    │ • Sanctions │   │   mgmt sys │
│ • Owner  │    │ • Supply    │   │ • PSC prep │
│   check  │    │   chain     │   │ • Risk     │
│ • PEP    │    │ • Port data │   │   detect   │
│   screen │    │             │   │            │
└──────────┘    └─────────────┘   └────────────┘
```

**Workflow:** When evaluating a chartering opportunity, the agent screens the vessel, registered owner, beneficial owner, and operators against sanctions databases. It cross-references the vessel's trading history with high-risk regions, checks the vessel's port state control record, reviews ISM Code compliance documentation, and generates a comprehensive risk assessment. This workflow is critical for banks providing trade finance, P&I clubs assessing insurance risk, and charterers conducting pre-fixture due diligence.

## Comparison Table: Maritime MCP Server Ecosystem

| Category | Dedicated Servers | Adjacent/Repurposable | Notable Examples |
|----------|:-:|:-:|---|
| Vessel Tracking & AIS | 7 | 1 | MarineTraffic 9★, ShipXY 9★, Datalastic, Saillogger |
| Shipping Lines & Carriers | 4 | 11 | Maersk, Envia (official), UPS, FedEx, SF Express |
| Maritime Intelligence & Compliance | 4 | 3 | Maritime Shipping Intel, AML Watcher, DocSentinel 96★ |
| Naval Architecture & Shipbuilding | 4 | 8 | Shipbuilding Specs, Naval Standards, CAD-MCP 286★ |
| Ocean Science & Oceanography | 5 | 4 | OceanMCP (8-in-1), Oceanum, IBM Archives 3★ |
| Marine Weather & Surf | 3 | 7 | Open-Meteo 37★, Surf Forecast 18★, Weather 239★ |
| Maritime Heritage & Hydrography | 2 | 0 | IBM Maritime Archives, SHOM Wrecks |
| Sailing & Yachting | 2 | 0 | Yachtsy, Garmin Sailing |
| Industrial IoT/SCADA | 0 | 6 | IoT Edge 22★, EMQX MQTT 23★, WinCC 9★ |
| Satellite/Earth Observation | 0 | 5 | Earth Agent 99★, NASA 83★, Copernicus |
| Simulation/Digital Twin | 0 | 6 | Isaac Sim 140★, Text2Sim 19★, Unity DT |
| Time-Series/Monitoring | 0 | 3 | InfluxDB 3 Official 29★, InfluxDB 33★ |
| GIS/Geospatial | 0 | 6 | QGIS 871★, GIS 126★, GDAL 59★ |
| Port & Terminal Operations | 0 | 0 | — |
| Fishing & Aquaculture | 1 | 0 | Resource compliance only |
| **Total** | **~32** | **~54** | **~86 servers cataloged** |

## Regulatory and Security Considerations

Maritime AI deployments must navigate a particularly complex regulatory landscape spanning international conventions, flag state laws, port state requirements, and emerging cyber regulations.

### IMO Regulatory Framework

The International Maritime Organization sets the baseline through conventions including SOLAS (Safety of Life at Sea), MARPOL (pollution prevention), STCW (seafarer training), and MLC (Maritime Labour Convention). AI agents accessing maritime data must respect these frameworks — for example, SOLAS Chapter V requires certain navigational data to be maintained in specific formats, and AI systems that interact with safety-critical navigation data need to operate within these requirements.

The IMO finalized its non-mandatory MASS Code (Maritime Autonomous Surface Ships) in 2026, establishing the first international regulatory framework for autonomous vessels. AI agents operating in this space will need to understand and comply with MASS Code requirements as they evolve toward mandatory status around 2030.

### Maritime Cybersecurity Regulations

Maritime cybersecurity regulation has accelerated significantly:

- **IMO MSC-FAL.1/Circ.3/Rev.3** (April 2025) — Updated maritime cyber risk management guidelines
- **IACS UR E26/E27** — Mandatory for all newbuild vessels with contracts signed after July 2024, requiring systematic cyber risk management for vessel systems
- **US Coast Guard** — Cyber incident reporting mandatory from July 2025; annual cybersecurity training required from January 2026
- **EU NIS2 Directive** — Covers maritime transport as an essential service sector

AI agents with MCP access to vessel systems (through IoT/SCADA servers) need to operate within these cybersecurity frameworks. The principle of least privilege — giving AI agents only the access they need — is particularly important when connecting to operational technology (OT) systems on vessels and in ports.

### Sanctions and Trade Compliance

Maritime sanctions compliance is governed by multiple regimes:

- **OFAC** (US) — Specially Designated Nationals (SDN) list, vessel sanctions
- **EU Consolidated List** — EU sanctions including vessel and entity designations
- **UN Security Council** — Global sanctions resolutions
- **OFSI** (UK) — Post-Brexit independent sanctions regime

AI agents performing sanctions screening through MCP servers like AML Watcher must handle the complexity of multiple overlapping sanctions regimes, vessel ownership structures designed to obscure beneficial ownership, and the risk of indirect sanctions violations through intermediaries.

### Data Sovereignty and AIS Privacy

AIS data, while broadcast openly over radio frequencies, is subject to increasing privacy and security concerns. Some nations restrict AIS data collection within their territorial waters. Military and government vessels may manipulate or suppress AIS signals. AI agents should be designed with awareness that AIS data may be incomplete, delayed, or deliberately misleading — a phenomenon known as "dark shipping" or "AIS spoofing" that has increased in conflict zones and sanctions evasion scenarios.

### Classification Society Rules

Classification societies (DNV, Lloyd's Register, Bureau Veritas, American Bureau of Shipping, ClassNK, RINA) set technical standards for vessel construction and operation. AI agents used in design verification or operational compliance would need to reference these rules — but none of the major classification societies have released MCP integrations yet. This represents one of the largest gaps in the maritime MCP ecosystem.

## Ecosystem Gaps and Opportunities

The maritime MCP ecosystem has some of the largest gaps of any industry vertical we have surveyed.

### Zero Coverage: Port and Terminal Operations

No MCP servers exist for terminal operating systems (TOS) — the software that manages container yard operations, berth allocation, crane scheduling, and gate management. Major platforms like Navis N4 (Cargotec), Kalmar terminal automation, and TOS solutions from Tideworks, Jade Logistics, and RBS have no MCP presence. Given that smart ports are an $11.3 billion market, this is perhaps the single largest opportunity in maritime MCP.

### Zero Coverage: Fishing and Aquaculture

Despite global fisheries being a $400+ billion industry with massive data needs (catch reporting, quota management, vessel monitoring, stock assessment), there are no dedicated fishing or aquaculture MCP servers. Global Fishing Watch, FAO FishStatJ, national quota management systems, and aquaculture monitoring platforms have no MCP integrations.

### Missing: Major Vessel Tracking Providers

VesselFinder, FleetMon, Kpler (which acquired MarineTraffic), Spire Global, and exactEarth — all major providers of vessel tracking and maritime intelligence — have not released official MCP servers. The community implementations for MarineTraffic exist, but official vendor support would significantly improve reliability and data quality.

### Missing: All Top-10 Shipping Lines (Official)

Only a community-built Maersk wrapper exists. MSC (the world's largest container line), CMA CGM (partnered with Google for AI), COSCO, Hapag-Lloyd, Evergreen, ONE, Yang Ming, ZIM, and HMM have no MCP presence — official or community.

### Missing: Classification Societies

DNV, Lloyd's Register, Bureau Veritas, American Bureau of Shipping, and ClassNK — which collectively set the technical rules governing 95%+ of the world's merchant fleet — have no MCP servers for accessing their rules, class notations, vessel records, or technical standards.

### Missing: Marine Navigation Standards

No MCP bridges exist for SignalK (the open marine data standard), NMEA 2000/0183 (the universal marine electronics protocol), ECDIS (Electronic Chart Display and Information System), or S-57/S-100 electronic chart formats. These protocols are the nervous system of every modern vessel — connecting them to AI agents through MCP would unlock real-time bridge integration.

### Missing: Ocean Science Platforms

CMEMS (Copernicus Marine Environment Monitoring Service), the Argo float network (4,000+ ocean profiling floats), GEBCO (global ocean bathymetry), IOOS (Integrated Ocean Observing System), OBIS (Ocean Biodiversity Information System), and Global Fishing Watch all lack MCP integrations. The OceanMCP project covers NOAA data well, but European and global ocean science platforms remain unconnected.

### Missing: Maritime CFD and Hydrodynamics

No MCP servers exist for computational fluid dynamics (CFD) tools used in hull design optimization, propeller design, or seakeeping analysis. Tools like OpenFOAM, Star-CCM+, ANSYS Fluent, and HydroComp have no MCP presence despite being critical to naval architecture workflows.

## Getting Started

The right entry point depends on your role in the maritime ecosystem.

**Ship operators and fleet managers** should start with vessel tracking MCP servers (MarineTraffic or ShipXY) combined with OceanMCP's weather and ocean forecast suite. This combination provides the foundation for fleet monitoring and voyage intelligence. Add AML Watcher for sanctions screening if your operations involve high-risk regions.

**Port authorities and terminal operators** face the largest gap — no port-specific MCP servers exist. However, IoT Edge MCP can connect to terminal sensor systems, weather MCP servers can provide operational weather windows, and GIS tools can support spatial planning. Building custom MCP servers for your TOS systems may be the most impactful investment.

**Logistics and freight forwarders** should focus on the carrier MCP servers — Envia for multi-carrier rate comparison and tracking, plus individual carrier servers (UPS, FedEx) for last-mile visibility. Combine with Shipping Rates MCP for container shipping cost analysis.

**Marine scientists and researchers** should explore OceanMCP's eight-server suite for NOAA data, NASA Earthdata MCP for satellite observations, and Copernicus MCP for European earth observation data. The ERDDAP server alone provides access to 80+ ocean science data servers worldwide.

**Naval architects and marine engineers** currently face limited dedicated options. CAD MCP servers (FreeCAD, Fusion 360, CadQuery) can support hull and systems design, while the shipbuilding specs server provides standards access. Watch for MCP integrations from NAPA, AVEVA Marine, and classification societies.

**Compliance officers and trade finance teams** should start with AML Watcher for sanctions screening, Maritime Shipping Intelligence for trade data, and DocSentinel for document compliance assessment. These tools address the most time-consuming aspects of maritime due diligence.

For broader MCP context, see our guides on [building your first MCP server](/guides/build-your-first-mcp-server/), [MCP and IoT/embedded systems](/guides/mcp-iot-embedded-systems/), [MCP and supply chain/logistics](/guides/mcp-supply-chain-logistics/), [MCP and geospatial/GIS](/guides/mcp-geospatial-gis/), [MCP server security](/guides/mcp-server-security/), and the [complete MCP server directory](/reviews/).
