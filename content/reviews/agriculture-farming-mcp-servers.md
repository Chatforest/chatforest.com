---
title: "Agriculture & Farming MCP Servers — Leaf, John Deere, FieldMCP, FarmerChat, Weather, Satellite Imagery, and More"
date: 2026-03-15T15:00:00+09:00
description: "Agriculture and farming MCP servers are bringing AI to precision agriculture, crop planning, and farm data management. We reviewed 20+ servers across 7 subcategories."
og_description: "Agriculture & farming MCP servers: Leaf Agriculture (official vendor, unified farm API), FieldMCP (commercial SaaS, $29/org/month, John Deere live), John Deere Operations Center, agri-weather (Open-Meteo, soil/ET data), Brazilian ag data (23 stars), FarmerChat (12 MCP servers, multi-country), sheep breeding genetics (15 tools), Axion Planetary MCP (218 stars, AWS, SAR-to-optical). Rating: 3.0/5."
content_type: "Review"
card_description: "Agriculture and farming MCP servers for precision agriculture, crop planning, livestock management, and farm data integration. This is an early-stage but genuinely interesting category. Two commercial vendors now offer MCP servers — Leaf Agriculture's unified API connects to major ag platforms through a single integration point, and the new FieldMCP ($29/org/month) provides John Deere integration with 150+ agronomic decision rules. John Deere's Operations Center has one active community MCP implementation (CoreyFransen08's Cloudflare Workers with double OAuth proxy). Agricultural weather gets specialized treatment with agri-weather-mcp offering soil temperature/moisture at multiple depths and evapotranspiration metrics. A new general-purpose agriculture MCP server (AiAgentKarl) provides 8 tools across soil, weather, climate history, and global statistics using free APIs. The most ambitious project remains Digital Green's FarmerChat-MCP with 12 servers across five countries. Axion Planetary MCP has grown to 218 stars with a V2 rewrite migrating to AWS and introducing a SAR-to-optical foundation model. Major gaps persist: no official equipment manufacturer servers, no crop disease identification, no irrigation management. The category earns 3.0/5 — thin but meaningful, with commercial entrants signaling that agricultural MCP is becoming a real market."
last_refreshed: 2026-04-24
---

Agriculture and farming MCP servers are bringing AI assistants into precision agriculture, crop planning, livestock management, and farm data analysis. Instead of navigating multiple dashboards for field data, weather forecasts, soil conditions, and market prices, these servers let AI agents pull farm-specific intelligence and generate actionable recommendations — all through the Model Context Protocol.

The landscape spans seven areas: **unified farm data platforms** (Leaf Agriculture, FieldMCP, John Deere Operations Center), **general-purpose agriculture tools** (soil, weather, climate history, global statistics), **agricultural weather intelligence** (soil conditions, evapotranspiration, crop-specific alerts), **market data** (commodity prices, crop estimates), **smallholder farmer AI** (multi-source agricultural advisory), **livestock and breeding** (genetic evaluation, breeding decisions), and **satellite earth observation** (NDVI, crop health monitoring, land use analysis).

The headline findings: **Two commercial vendors now offer agriculture MCP servers** — Leaf Agriculture's unified API aggregates data from major platforms through a single integration point, and the new FieldMCP ($29/org/month) provides John Deere integration with 150+ agronomic decision rules and OAuth 2.1 authentication. **Digital Green's FarmerChat-MCP remains the most ambitious agricultural AI project using MCP** — 12 interconnected servers synthesizing soil, weather, elevation, and satellite data for smallholder farmers across five countries. **Agricultural weather MCP servers provide data that generic weather servers don't** — soil temperature at multiple depths, evapotranspiration metrics, and crop growth stage alerts. **No major equipment manufacturer has an official MCP server** — everything for John Deere, Case IH, and AGCO is community-built or third-party.

**Category:** [Logistics & Industry](/categories/logistics-industry/)

## Unified Farm Data Platforms

### Leaf Agriculture MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Leaf Agriculture MCP](https://withleaf.io/en/whats-new/leaf-mcp-launch/) | — | — | Commercial | — |

The **only commercial vendor with an official agriculture MCP server**. Leaf's unified API is the standard integration layer for agricultural software — it aggregates field boundaries, machine operations, satellite imagery, and weather data from major platforms including John Deere, Climate FieldView, CNHi, AGCO, and Trimble into a single normalized API.

Their MCP server wraps this unified API for AI agent access. Developers can connect Claude Desktop, Cursor, VS Code, or any MCP-compatible client to live farm data with a single configuration. Key capabilities include:

- **Field operations data** — planting, application, harvest records across equipment brands
- **Machine data** — standardized telemetry from mixed fleets
- **Satellite imagery** — field-level imagery with vegetation indices
- **Weather data** — historical and forecast data tied to specific fields
- **Integrated documentation** — API docs accessible within the chat context

All tool calls use your Leaf API key and hit existing API endpoints, so security is handled through standard API authentication. This is a commercial product with paid tiers, but it's the closest thing to a "universal farm data MCP" that exists.

### FieldMCP (Commercial SaaS)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [FieldMCP](https://www.fieldmcp.com) | — | — | Commercial | 150+ rules |

A **new commercial SaaS platform** that provides MCP servers for agricultural APIs. FieldMCP connects AI assistants to farm data through standard MCP protocol with OAuth 2.1 authentication — your AI can access field boundaries, equipment data, harvest records, and agronomic recommendations through natural language.

Key capabilities:

- **John Deere Operations Center integration** — live and production-ready
- **150+ agronomic decision rules** across 12 analysis domains
- **Climate FieldView, CNHi, AGCO** — listed as "coming soon"
- **Two-step setup** — sign up, connect your John Deere account, MCP clients discover and connect natively
- **Transparency focus** — every recommendation traces to documented rules

**Pricing: $29/org/month** with a 14-day free trial and 17K API requests/month included. This is the first dedicated commercial MCP platform targeting agriculture (Leaf is a broader ag-data platform that also offers MCP access).

### John Deere Operations Center (Community)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CoreyFransen08/john-deere-ops-mcp](https://glama.ai/mcp/servers/@CoreyFransen08/john-deere-ops-mcp) | 0 | TypeScript | — | — |

**CoreyFransen08/john-deere-ops-mcp** runs as a remote MCP server on Cloudflare Workers with a Durable Object providing stateful sessions. The clever part is its **double OAuth proxy pattern** — the Worker acts as an OAuth server to MCP clients downstream, and as an OAuth client to John Deere upstream. This means any MCP-compatible client can authenticate without needing to implement John Deere's OAuth flow directly. Capabilities include browsing organizations, fields, and field operations data. Targets the JD sandbox environment (max 5 orgs, 150K API calls/month, 18-month sandbox duration). No activity since its initial commit in March 2026.

A second implementation (easavin/ag-mcp) that previously provided a Claude-style chat interface combining John Deere, Auravant, and weather data appears to have been removed — the repository now returns 404.

Neither existing implementation is an official John Deere product — both are community-built integrations using John Deere's developer API.

## General-Purpose Agriculture Tools

### Agriculture MCP Server (AiAgentKarl)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AiAgentKarl/agriculture-mcp-server](https://github.com/AiAgentKarl/agriculture-mcp-server) | 1 | Python | MIT | 8 |

A **new open-source general-purpose agriculture MCP server** (March 2026) that bundles 8 tools across 4 categories using entirely free APIs — no authentication keys required:

- **Soil conditions** — soil temperature, moisture, evapotranspiration forecasts via Open-Meteo
- **Crop weather** — agricultural weather metrics, historical climate data since 1981 (NASA POWER), long-term monthly climate patterns
- **Global statistics** — country-specific agriculture profiles and cross-country comparisons via World Bank (20+ indicators)
- **Food products** — barcode-based product lookups and searches across 3M+ products via Open Food Facts

The breadth is appealing — a single server that covers soil, weather, climate history, and global agriculture statistics. The trade-off is depth: each tool wraps a public API without much agricultural domain logic on top. Still, for quick agricultural data access with zero setup cost, this fills a gap between the specialized servers above and generic weather/data tools.

## Agricultural Weather Intelligence

### Agri-Weather MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [etudelab/agri-weather-mcp](https://github.com/etudelab/agri-weather-mcp) | — | Python | — | 5+ |

A weather MCP server **designed specifically for agriculture**, not just generic weather data repurposed for farming. Built on the free Open-Meteo API, it provides data points that matter for crop management:

- **Current weather** — temperature, humidity, precipitation, wind, and soil data at the location level
- **5-day forecasts** — hourly granularity for planning field operations around weather windows
- **Soil conditions** — temperature and moisture at **multiple depths** — critical for planting decisions and root zone management
- **Evapotranspiration** — ET and reference ET₀ data for calculating irrigation requirements
- **Agricultural alerts** — crop-specific recommendations keyed to growth stages (planting, vegetative, flowering, harvest)

The soil depth data and evapotranspiration metrics are what set this apart from general-purpose weather MCP servers. A generic weather server might tell you it's 25°C with 60% humidity — this one tells you that soil moisture at 10cm is adequate but at 30cm it's dropping, and your ET₀ suggests irrigation within 48 hours.

### GAP Agriculture MCP (East Africa)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [eagleisbatman/gap-agriculture-mcp](https://github.com/eagleisbatman/gap-agriculture-mcp) | — | TypeScript | — | — |

Provides **satellite weather forecasts for agricultural planning in Kenya and East Africa** via TomorrowNow's Global Access Platform (GAP). Coverage includes Kenya, Tanzania, Uganda, Ethiopia, and Somalia.

Key technical detail: the server processes **50-member ensemble forecasts** into single actionable values — temperature, rainfall, humidity, and wind — with up to 14 days of forecast data. The AI agent can then analyze this data and generate planting recommendations, irrigation schedules, and farming advice.

The server accepts default coordinates via HTTP headers, allowing farmers to ask weather questions without specifying their location every time. This is a small but thoughtful UX detail for agricultural users who always care about the same fields.

Requires Node.js >= 18.0.0 and a GAP API Token from TomorrowNow. Coverage is limited to regions where TomorrowNow operates — primarily East Africa.

## Agricultural Market Data

### AgroBR MCP (Brazilian Agricultural Data)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bruno-portfolio/agrobr-mcp](https://github.com/bruno-portfolio/agrobr-mcp) | 23 | Python | MIT | 4+ |

Connects LLMs to **19 public Brazilian agricultural data sources** — the most comprehensive agricultural market data MCP server we've found in any country. Data sources include:

- **CEPEA/ESALQ** — daily spot prices for agricultural commodities
- **B3** — daily adjustments for agricultural futures contracts
- **CONAB** — current crop estimates by state
- **IBGE PAM** — historical production data by state
- **INPE** — deforestation monitoring data
- **NASA POWER** — climate data for agricultural applications

Available tools include `preco_diario` (spot prices), `futuros_b3` (futures adjustments), `estimativa_safra` (crop estimates), and `producao_anual` (historical production). All data logic lives in the separate `agrobr` Python library, which handles collection, parsing, and caching — the MCP server is a thin wrapper for text formatting.

Brazil is the world's largest producer of soybeans, coffee, sugar, and orange juice, and a top-5 producer of corn, cotton, and beef — so having comprehensive MCP access to Brazilian agricultural data is globally significant, not just locally useful.

## Smallholder Farmer AI

### FarmerChat-MCP (Digital Green)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [digitalgreenorg/DG_Open](https://github.com/digitalgreenorg/DG_Open) | — | Python | — | 12 servers |

The **most ambitious agricultural MCP project** we've reviewed. Digital Green — a nonprofit that has reached 30+ million smallholder farmers — built FarmerChat-MCP as a unified agricultural intelligence system using **12 interconnected MCP servers** that power multiple interfaces without duplicate code.

The architecture synthesizes data from multiple sources in parallel:

- **Soil analysis** — via iSDA (Africa-specific) and OpenLandMap
- **Weather conditions** — via Open-Meteo
- **Groundwater data** — via NASA GRACE satellite
- **Elevation data** — via OpenElevation
- **Species identification** — via iNaturalist
- **Satellite imagery** — for crop monitoring

A farmer can describe their situation ("I have 2 acres of clay soil at 1,200m elevation, dry season coming") and FarmerChat synthesizes soil type, weather forecast, elevation, and groundwater data to recommend specific crops ("plant wheat and drought-tolerant lentils"), planting schedules, and management practices.

The system operates across **India, Ethiopia, Kenya, Nigeria, and Brazil** — regions where the difference between good and bad agricultural advice can mean the difference between food security and hunger. This is not a hobbyist project — it's production infrastructure for agricultural extension at scale.

## Livestock & Breeding

### NSIP Sheep Breeding MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [epicpast/nsip-api-client](https://github.com/epicpast/nsip-api-client) | — | Python | — | 15 |

A surprisingly deep MCP server for the **National Sheep Improvement Program (NSIP)** — the U.S. genetic evaluation system for sheep. Provides 15 MCP tools split between API access and breeding decision support:

- **10 NSIP API tools** — search animals, query flocks, retrieve breeding values
- **5 Shepherd consultation tools** — compare EBVs (Estimated Breeding Values), plan matings, rank flocks, evaluate genetic improvement decisions

The server includes **intelligent context management** with automatic response summarization to prevent LLM context window overflow when dealing with large breeding datasets — a thoughtful technical detail. Smart caching with 1-hour TTL keeps repeated queries fast. Supports multiple transports: stdio (CLI), HTTP SSE (web), and WebSocket.

This is a niche tool, but it automates complex genetic calculations that would otherwise require specialized software or extensive spreadsheet work. For commercial sheep operations making breeding decisions worth thousands of dollars per ram selection, having AI-assisted genetic analysis through natural language is genuinely useful.

## Satellite & Earth Observation for Agriculture

### Axion Planetary MCP (V2)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Dhenenjay/axion-planetary-mcp](https://github.com/Dhenenjay/axion-planetary-mcp) | 218 | Python | — | 30+ datasets |
| [Dhenenjay/Axion-MCP](https://github.com/Dhenenjay/Axion-MCP) | 4 | Python | — | 30+ datasets |

The **most-starred agriculture-adjacent MCP server** (218 stars). Axion Planetary MCP is the V2 rewrite of the original Axion-MCP, with a major architectural shift: **migrated from Google Cloud/GEE to AWS**, introduced a proprietary "Axion Foundation Model" for SAR-to-optical image conversion, NPM package distribution, and API key authentication instead of GCP credentials. 935 commits demonstrate active development, though the last commit was February 2026.

Agricultural capabilities include:

- **Vegetation indices** — NDVI, NDWI, EVI, SAVI, NBR for crop health assessment
- **30+ satellite datasets** — Landsat, Sentinel-2, MODIS at various resolutions and revisit frequencies
- **Cloud-free composites** — automated cloud masking for clean imagery
- **Time series analysis** — track crop growth, stress, and yield trends across seasons
- **Deforestation tracking** — monitor land use change
- **SAR-to-optical conversion** — the new foundation model generates optical-like imagery from radar data, useful when cloud cover blocks optical satellites

The original Axion-MCP (4 stars) connected directly to Google Earth Engine and remains functional for users with GCP credentials, but development has shifted to the V2 platform.

#### Related Earth Observation Project

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Dhenenjay/earth-engine-mcp-new](https://github.com/Dhenenjay/earth-engine-mcp-new) | — | Python | — | — |

A simpler Earth Engine MCP implementation for basic Sentinel-2 imagery and NDVI calculation.

## Adjacent: Biodiversity & Species Identification

### iNaturalist MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cvsouth/inaturalist-mcp](https://github.com/cvsouth/inaturalist-mcp) | — | Python | — | 5+ |

While not strictly an agriculture server, **iNaturalist's biodiversity data is directly useful for farming** — pest identification, beneficial insect recognition, weed species lookup, and crop disease diagnosis all benefit from access to one of the world's largest community-contributed species databases.

Tools include searching for taxa, places, and community projects (bioblitzes, biodiversity surveys), finding species commonly confused with a given taxon (useful for distinguishing crop pests from beneficial look-alikes), and searching across all of iNaturalist for taxa, places, projects, and users.

Digital Green's FarmerChat-MCP already integrates iNaturalist data for species identification — showing that the connection between biodiversity data and agricultural advisory is not theoretical.

## What's Missing

Despite interesting depth in a few areas, the agriculture MCP ecosystem has significant gaps:

- **No official equipment manufacturer servers** — John Deere, Case IH (CNHi), AGCO (Massey Ferguson, Fendt), Kubota, and Claas have developer APIs but zero official MCP servers. All John Deere MCP access is community-built.
- **No crop disease or pest identification** — no dedicated MCP servers for plant pathology, pest scouting, or integrated pest management. FarmerChat uses iNaturalist, but a PlantVillage-style disease detection MCP would fill a real gap.
- **No irrigation management** — despite multiple weather and soil moisture MCP servers, there's no dedicated irrigation scheduling or pivot/drip control MCP server.
- **No grain commodity trading** — no MCP servers for CME/CBOT grain futures, USDA crop reports, or agricultural commodity market analysis (agrobr-mcp covers Brazil specifically, but nothing for global grain markets).
- **No aquaculture or fisheries** — shrimp farming, fish pond management, and marine aquaculture have no MCP representation.
- **No vineyard or orchard management** — wine grape growing, fruit tree management, and specialty crop production are absent.
- **Limited livestock** — only sheep breeding is covered. No cattle, poultry, swine, or dairy MCP servers exist.

## The Bottom Line

**Rating: 3.0 / 5**

Agriculture & farming remains an early-stage MCP category with a small server count but genuine substance. The arrival of **FieldMCP as a dedicated commercial SaaS platform** ($29/org/month) is the most significant development since our initial review — it signals that agricultural MCP is transitioning from hobbyist projects to a real market. Combined with Leaf Agriculture's unified API, there are now two commercial vendors competing in this space.

Digital Green's FarmerChat-MCP continues to demonstrate that MCP can power complex multi-source agricultural advisory at scale across five countries. The agricultural weather servers provide farming-specific data that generic weather servers don't — soil depth measurements and evapotranspiration remain essential for irrigation decisions. Axion Planetary MCP's growth to 218 stars and its V2 rewrite with SAR-to-optical conversion shows the satellite/earth observation side of agricultural MCP gaining traction.

The ecosystem is still thin — roughly 20-25 servers where categories like database tooling or cloud infrastructure have hundreds. But agriculture is a $3 trillion global industry where better information directly translates to higher yields and lower waste. The servers that exist are solving real problems for real farmers, not just wrapping APIs for developer convenience.

**Best for farm data integration:** Leaf Agriculture MCP (unified API across platforms)
**Best commercial platform:** FieldMCP ($29/org/month, John Deere live, 150+ decision rules)
**Best for agricultural weather:** etudelab/agri-weather-mcp (soil depth, ET₀, crop alerts)
**Best for smallholder farmers:** Digital Green FarmerChat-MCP (12 servers, 5 countries)
**Best for satellite crop analysis:** Dhenenjay/axion-planetary-mcp (218 stars, AWS, 30+ datasets)
**Best niche pick:** epicpast/nsip-api-client (sheep breeding genetics, 15 tools)
**Best zero-setup option:** AiAgentKarl/agriculture-mcp-server (8 tools, all free APIs)

*This review was last refreshed on 2026-04-24 using Claude Opus 4.6 (Anthropic).*
