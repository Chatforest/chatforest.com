---
title: "Agriculture & Farming MCP Servers — Leaf, John Deere, FarmerChat, Garmin Weather, Satellite Imagery, and More"
date: 2026-03-15T15:00:00+09:00
description: "Agriculture and farming MCP servers are bringing AI to precision agriculture, crop planning, and farm data management. We reviewed 20+ servers across 6 subcategories. Unified Farm Data: Leaf Agriculture MCP (official vendor, unified API across major ag platforms — the only commercial agriculture MCP server), CoreyFransen08/john-deere-ops-mcp (Cloudflare Workers, double OAuth for John Deere Operations Center), easavin/ag-mcp (John Deere + Auravant + weather in a chat interface). Agricultural Weather: etudelab/agri-weather-mcp (Open-Meteo API, soil conditions at multiple depths, evapotranspiration, crop-specific alerts), eagleisbatman/gap-agriculture-mcp (Kenya/East Africa, TomorrowNow GAP, 14-day ensemble forecasts). Market Data: bruno-portfolio/agrobr-mcp (Brazilian agricultural data from 19 public sources — CEPEA, CONAB, IBGE, INPE, B3, NASA POWER). Smallholder Farmer AI: Digital Green FarmerChat-MCP (12 MCP servers, multi-country, synthesizes soil/weather/elevation data for planting recommendations). Livestock: epicpast/nsip-api-client (15 MCP tools for NSIP sheep breeding genetic evaluation, EBVs, mating plans). Satellite & Earth Observation: Dhenenjay/Axion-MCP (Google Earth Engine, 30+ satellite datasets, NDVI/NDWI/EVI, time series analysis for crop health monitoring). Rating: 3.0/5."
og_description: "Agriculture & farming MCP servers: Leaf Agriculture (official vendor, unified farm API), John Deere Operations Center (2 implementations), agri-weather (Open-Meteo, soil/ET data), Brazilian ag data (19 sources), FarmerChat (12 MCP servers, multi-country), sheep breeding genetics (15 tools), Google Earth Engine for crop monitoring (30+ datasets). Rating: 3.0/5."
content_type: "Review"
card_description: "Agriculture and farming MCP servers for precision agriculture, crop planning, livestock management, and farm data integration. This is an early-stage but genuinely interesting category. Leaf Agriculture stands out as the only commercial vendor with an official MCP server — their unified API connects to major ag platforms (John Deere, Climate FieldView, CNHi, AGCO) through a single integration point. John Deere's Operations Center has two independent MCP implementations, with CoreyFransen08's Cloudflare Workers deployment using a clever double OAuth proxy pattern. Agricultural weather gets specialized treatment with etudelab's agri-weather-mcp offering soil temperature/moisture at multiple depths and evapotranspiration metrics — data points that generic weather MCP servers don't provide. The most ambitious project is Digital Green's FarmerChat-MCP, which runs 12 MCP servers to synthesize soil analysis, weather, elevation, and satellite data for smallholder farmers across India, Ethiopia, Kenya, Nigeria, and Brazil. For livestock, the NSIP sheep breeding MCP server provides 15 tools for genetic evaluation including EBV comparison and mating plans. Satellite imagery gets strong coverage through Axion-MCP's Google Earth Engine integration with 30+ datasets and vegetation indices like NDVI. Major gaps: no official servers from John Deere, Case IH, AGCO, or any equipment manufacturer; no dedicated crop disease/pest identification servers; no irrigation management systems; no commodity trading platforms with grain futures. The category earns 3.0/5 — thin but meaningful, with Leaf's official server and FarmerChat showing that agriculture-specific MCP tools can deliver real value."
last_refreshed: 2026-03-15
---

Agriculture and farming MCP servers are bringing AI assistants into precision agriculture, crop planning, livestock management, and farm data analysis. Instead of navigating multiple dashboards for field data, weather forecasts, soil conditions, and market prices, these servers let AI agents pull farm-specific intelligence and generate actionable recommendations — all through the Model Context Protocol.

The landscape spans six areas: **unified farm data platforms** (Leaf Agriculture, John Deere Operations Center), **agricultural weather intelligence** (soil conditions, evapotranspiration, crop-specific alerts), **market data** (commodity prices, crop estimates), **smallholder farmer AI** (multi-source agricultural advisory), **livestock and breeding** (genetic evaluation, breeding decisions), and **satellite earth observation** (NDVI, crop health monitoring, land use analysis).

The headline findings: **Leaf Agriculture is the only commercial vendor with an official MCP server** — their unified API aggregates data from John Deere, Climate FieldView, CNHi, AGCO, and other platforms through a single integration point. **Digital Green's FarmerChat-MCP is the most ambitious agricultural AI project using MCP** — 12 interconnected servers synthesizing soil, weather, elevation, and satellite data for smallholder farmers across five countries. **Agricultural weather MCP servers provide data that generic weather servers don't** — soil temperature at multiple depths, evapotranspiration metrics, and crop growth stage alerts. **No major equipment manufacturer has an official MCP server** — everything for John Deere, Case IH, and AGCO is community-built.

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

### John Deere Operations Center

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CoreyFransen08/john-deere-ops-mcp](https://glama.ai/mcp/servers/@CoreyFransen08/john-deere-ops-mcp) | — | TypeScript | — | — |
| [easavin/ag-mcp](https://github.com/easavin/ag-mcp) | — | TypeScript | — | — |

Two independent implementations connect AI agents to John Deere's Operations Center API.

**CoreyFransen08/john-deere-ops-mcp** runs as a remote MCP server on Cloudflare Workers with a Durable Object providing stateful sessions. The clever part is its **double OAuth proxy pattern** — the Worker acts as an OAuth server to MCP clients downstream, and as an OAuth client to John Deere upstream. This means any MCP-compatible client can authenticate without needing to implement John Deere's OAuth flow directly. Capabilities include browsing organizations, fields, and field operations data.

**easavin/ag-mcp** takes a different approach — it's a Claude-style chat interface that connects to John Deere Operations Center, Auravant (an Argentine precision agriculture platform), and weather data via MCP. Think of it as a farmer-facing AI assistant where you can ask questions about your fields and equipment in natural language, upload prescription shapefiles, and get multi-source data combined from multiple platforms. The interface is responsive for desktop, tablet, and mobile.

Neither is an official John Deere product — both are community-built integrations using John Deere's developer API.

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
| [bruno-portfolio/agrobr-mcp](https://github.com/bruno-portfolio/agrobr-mcp) | — | Python | — | 4+ |

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

### Axion MCP (Google Earth Engine)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Dhenenjay/Axion-MCP](https://github.com/Dhenenjay/Axion-MCP) | — | Python | — | 30+ datasets |

An **enterprise-grade geospatial analysis platform** that connects AI agents to Google Earth Engine's massive satellite data catalog. While not agriculture-specific, this is the most powerful tool available for farm-level satellite analysis via MCP.

Agricultural capabilities include:

- **Vegetation indices** — NDVI, NDWI, EVI, SAVI, NBR for crop health assessment
- **30+ satellite datasets** — Landsat, Sentinel-2, MODIS at various resolutions and revisit frequencies
- **Cloud-free composites** — automated cloud masking for clean imagery
- **Time series analysis** — track crop growth, stress, and yield trends across seasons
- **Deforestation tracking** — monitor land use change

A farmer or agronomist could ask "show me NDVI trends for my field over the last growing season" and get satellite-derived vegetation health data without touching GIS software. This is the kind of analysis that precision agriculture consultants charge hundreds of dollars per field for.

#### Related Earth Observation Projects

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Dhenenjay/axion-planetary-mcp](https://github.com/Dhenenjay/axion-planetary-mcp) | — | Python | — | — |
| [Dhenenjay/earth-engine-mcp-new](https://github.com/Dhenenjay/earth-engine-mcp-new) | — | Python | — | — |

Dhenenjay maintains multiple Earth Engine MCP implementations at different complexity levels — from basic Sentinel-2 imagery and NDVI calculation to the full Axion platform with 30+ datasets.

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

Agriculture & farming is an early-stage MCP category with a small server count but genuine substance. Leaf Agriculture's official unified farm data server is commercially significant — it's one of the few official vendor MCP servers in any industry vertical that connects to real production data. Digital Green's FarmerChat-MCP demonstrates that MCP can power complex multi-source agricultural advisory at scale across five countries. The agricultural weather servers (agri-weather-mcp, GAP agriculture) provide farming-specific data that generic weather servers don't — soil depth measurements and evapotranspiration are not nice-to-haves in agriculture, they're essential for irrigation decisions.

The ecosystem is thin overall — roughly 20 servers where categories like database tooling or cloud infrastructure have hundreds. But agriculture is a $3 trillion global industry where better information directly translates to higher yields and lower waste. The servers that exist are solving real problems for real farmers, not just wrapping APIs for developer convenience.

**Best for farm data integration:** Leaf Agriculture MCP (unified API across platforms)
**Best for agricultural weather:** etudelab/agri-weather-mcp (soil depth, ET₀, crop alerts)
**Best for smallholder farmers:** Digital Green FarmerChat-MCP (12 servers, 5 countries)
**Best for satellite crop analysis:** Dhenenjay/Axion-MCP (Google Earth Engine, NDVI, 30+ datasets)
**Best niche pick:** epicpast/nsip-api-client (sheep breeding genetics, 15 tools)

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
