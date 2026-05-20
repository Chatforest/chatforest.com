---
title: "Agriculture & Farming MCP Servers — Leaf, John Deere, FieldMCP, FarmerChat, Weather, Satellite Imagery, and More"
date: 2026-03-15T15:00:00+09:00
description: "Agriculture and farming MCP servers are bringing AI to precision agriculture, crop planning, pest modeling, and farm data management. We reviewed 25+ servers across 9 subcategories."
og_description: "Agriculture & farming MCP servers: agstack/opensource-pestmodels (Linux Foundation, 54 threats, 19 crops), CoreyFransen08 John Deere v2.0 (equipment + machine health), FieldMCP ($29/org/month), open-sprinkler-mcp (first irrigation hardware MCP), brapi-mcp-server (plant breeding research), Axion Planetary (220 stars, SAR-to-optical). Rating: 3.5/5."
content_type: "Review"
card_description: "Agriculture and farming MCP servers for precision agriculture, crop planning, pest modeling, irrigation management, and farm data integration. May 2026 brought the most active month in agriculture MCP history. The Linux Foundation's agstack/opensource-pestmodels fills the long-missing crop pest/disease gap with 13 models covering 19 crops and 54 threats. The community John Deere MCP (CoreyFransen08) hit v2.0.0 with equipment management and machine health monitoring. The first dedicated irrigation hardware MCP (open-sprinkler-mcp) appeared. A sophisticated plant breeding database server (brapi-mcp-server) now covers Breedbase and BrAPI v2.1 endpoints with near-daily development. Two commercial vendors (Leaf Agriculture, FieldMCP at $29/org/month) remain the enterprise options. Axion Planetary MCP holds at 220 stars for satellite crop analysis. The category earns 3.5/5 — the ecosystem is visibly maturing with serious institutional backing entering the space."
last_refreshed: 2026-05-20
---

Agriculture and farming MCP servers are bringing AI assistants into precision agriculture, crop planning, livestock management, and farm data analysis. Instead of navigating multiple dashboards for field data, weather forecasts, soil conditions, and market prices, these servers let AI agents pull farm-specific intelligence and generate actionable recommendations — all through the Model Context Protocol.

The landscape spans nine areas: **unified farm data platforms** (Leaf Agriculture, FieldMCP, John Deere Operations Center), **general-purpose agriculture tools** (soil, weather, climate history, global statistics), **agricultural weather intelligence** (soil conditions, evapotranspiration, crop-specific alerts), **market data** (commodity prices, crop estimates), **smallholder farmer AI** (multi-source agricultural advisory), **livestock and breeding** (genetic evaluation, breeding decisions), **satellite earth observation** (NDVI, crop health monitoring, land use analysis), **pest and disease modeling** (risk scoring, integrated pest management), and **plant breeding research** (germplasm databases, genotype analysis).

The headline findings: **May 2026 was the most active month in agriculture MCP history.** The Linux Foundation's **agstack/opensource-pestmodels** fills the long-missing crop pest/disease gap — 13 models, 19 crops, 54 threats, with a fuzzy Mamdani inference engine and full MCP tooling. **CoreyFransen08's community John Deere MCP hit v2.0.0** with equipment management, machine health, and work plans — a meaningful capability leap from the March 2026 launch. **The first dedicated irrigation hardware MCP appeared** (open-sprinkler-mcp, OpenSprinkler controllers). **cyanheads/brapi-mcp-server** provides multi-database plant breeding research access with near-daily development in May. On the commercial side, **two vendors (Leaf Agriculture, FieldMCP at $29/org/month) continue competing** for enterprise farm data integration. **No major equipment manufacturer has released an official MCP server** — everything for John Deere, Case IH, and AGCO remains community-built or third-party. And a notable regression: Digital Green's FarmerChat-MCP (previously the most ambitious project) has been frozen since November 2025 with no code commits.

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
| [CoreyFransen08/john-deere-ops-mcp](https://glama.ai/mcp/servers/@CoreyFransen08/john-deere-ops-mcp) | 4 | TypeScript | — | — |

**CoreyFransen08/john-deere-ops-mcp** runs as a remote MCP server on Cloudflare Workers with a Durable Object providing stateful sessions. The clever part is its **double OAuth proxy pattern** — the Worker acts as an OAuth server to MCP clients downstream, and as an OAuth client to John Deere upstream. This means any MCP-compatible client can authenticate without needing to implement John Deere's OAuth flow directly.

**Version 2.0.0 landed May 16–18, 2026** — the most active development period since launch. Key additions: an interactive `npm run setup` deployment walkthrough, enhanced OAuth 2.1 flow with full tool input schemas, CORS configuration via `API_ALLOWED_ORIGINS`, and new capabilities for **equipment management, work plans, and machine health monitoring**. The server now covers organizations, fields, field operations, equipment telemetry, and machine health — a meaningful expansion beyond the original read-only field data access. Targets the JD sandbox environment (max 5 orgs, 150K API calls/month, 18-month sandbox duration).

Neither this nor any other John Deere MCP implementation is an official John Deere product — all access is community-built using John Deere's developer API.

## General-Purpose Agriculture Tools

### Agriculture MCP Server (AiAgentKarl)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AiAgentKarl/agriculture-mcp-server](https://github.com/AiAgentKarl/agriculture-mcp-server) | 1 | Python | MIT | 8 |

An open-source general-purpose agriculture MCP server (March 2026, last commit April 3) that bundles 8 tools across 4 categories using entirely free APIs — no authentication keys required:

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

### FAO-56 Evapotranspiration MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lepoti-tech/fao56-mcp](https://github.com/lepoti-tech/fao56-mcp) | 0 | — | — | RAG |

A specialized new MCP server (April 2026) providing **RAG over FAO-56** — the United Nations Food and Agriculture Organization's definitive reference document on crop evapotranspiration and irrigation water requirements. FAO-56 is the global standard methodology for calculating crop water needs, used in everything from smallholder farm planning to national irrigation policy. A RAG server over this document means AI agents can answer nuanced ET₀ and Kc (crop coefficient) questions with authoritative sourcing rather than hallucinated approximations. Early-stage with no star traction yet, but fills a real methodological gap for irrigation engineers and agronomists.

## Agricultural Market Data

### AgroBR MCP (Brazilian Agricultural Data)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bruno-portfolio/agrobr-mcp](https://github.com/bruno-portfolio/agrobr-mcp) | 24 | Python | MIT | 4+ |

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

The **most ambitious agricultural MCP project** we've reviewed. Digital Green — a nonprofit that has reached 30+ million smallholder farmers — built FarmerChat-MCP as a unified agricultural intelligence system using **12 interconnected MCP servers** that power multiple interfaces without duplicate code. Note: the DG_Open repository has been frozen since November 2025 with no new commits — development activity may have shifted internally or paused.

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
| [Dhenenjay/axion-planetary-mcp](https://github.com/Dhenenjay/axion-planetary-mcp) | 220 | Python | — | 30+ datasets |
| [Dhenenjay/Axion-MCP](https://github.com/Dhenenjay/Axion-MCP) | 4 | Python | — | 30+ datasets |

The **most-starred agriculture-adjacent MCP server** (220 stars). Axion Planetary MCP is the V2 rewrite of the original Axion-MCP, with a major architectural shift: **migrated from Google Cloud/GEE to AWS**, introduced a proprietary "Axion Foundation Model" for SAR-to-optical image conversion, NPM package distribution, and API key authentication instead of GCP credentials. 935 commits — but last commit was February 2026 and no new activity in the April–May window. Growing passively on reputation.

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

## Pest & Disease Modeling

### AgStack Opensource Pest Models (Linux Foundation)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [agstack/opensource-pestmodels](https://github.com/agstack/opensource-pestmodels) | 0 | Python | — | 3+ |

The **most technically serious new agriculture MCP server** found in this refresh. AgStack is a Linux Foundation project — the same organizational backing as Kubernetes, Linux, and Node.js — which provides a credibility and longevity signal that no individual developer project can match.

The server launched May 18, 2026 (this week) and wraps a **13-model, 19-crop, 54-threat hierarchical pest and disease modeling framework**:

- **Layer 1 (weather)** — growing degree day accumulation, chilling requirements, precipitation thresholds
- **Layer 2 (agronomic)** — phenology stage inference, crop exposure windows, vulnerability curves
- **Layer 3 (risk)** — fuzzy Mamdani inference engine combining weather and agronomic inputs into actionable risk scores, UC IPM model integration

MCP tools include: list available models, query pest/disease threats by crop, explain model parameters and confidence factors. The complete agent conversation examples in the documentation demonstrate a practical workflow: describe your field conditions → get growing degree day accumulation → get crop stage → get pest pressure forecast with agronomic reasoning.

This fills one of the most significant gaps in the previous review — dedicated crop disease and pest identification. Linux Foundation backing means this is unlikely to be abandoned.

## Plant Breeding Research

### BrAPI MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cyanheads/brapi-mcp-server](https://github.com/cyanheads/brapi-mcp-server) | 3 | — | — | — |

A **highly active new server** targeting plant breeders and crop genomics researchers. BrAPI v2.1 is the standard data exchange protocol for plant breeding programs — this server provides multi-agent access to Breedbase, T3, Sweetpotatobase, and any BrAPI v2-compliant breeding database.

Near-daily commits throughout May 2026 with meaningful releases:
- **v0.5.5 (May 16)** — framework 0.9.1, schema portability improvements
- **v0.5.3 (May 5)** — per-session isolation for multi-agent research workflows
- **v0.4.10 (May 2)** — SQL query capabilities via canvas dataframes

Key capabilities: search studies, germplasm accessions, and genotype data across multiple breeding databases; per-session isolation prevents cross-contamination in multi-agent workflows; built-in alias registry for public BrAPI endpoints. The SQL dataframe surface added May 2 allows complex queries against retrieved breeding data — bridging the gap between database retrieval and analytical reasoning.

Niche but technically sophisticated. Relevant to public crop improvement programs, university plant science departments, and seed company research pipelines.

## Irrigation Management

### Open Sprinkler MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [koolsb/open-sprinkler-mcp](https://github.com/koolsb/open-sprinkler-mcp) | 0 | — | — | — |

The **first irrigation hardware MCP server** we've found — filling a gap explicitly noted in the previous review. OpenSprinkler is a popular open-source irrigation controller used in precision agriculture, orchards, and market gardens as well as residential applications.

Full monitoring and control surface:
- **Monitoring** — station states, active programs, sensor readings (rain sensor, moisture sensor, flow meter), operational history
- **Control** — manual station start/stop, program management, rain delay scheduling, water-level scaling (reduce/increase across all zones), zone sequencing
- **Safety** — optional read-only mode that exposes monitoring without allowing control commands

Docker and Kubernetes deployment supported, making it suitable for farm management integrations beyond individual homeowner setups. Very new (May 2026, 0 stars), but the OpenSprinkler community is substantial and MCP integration is a natural fit for AI-assisted irrigation scheduling.

## Developing-World Agricultural Data

### RwaSIS MCP (Rwanda Soil)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [s-bakire/rwasis-mcp](https://github.com/s-bakire/rwasis-mcp) | 0 | — | — | — |

A **new MCP server for Rwanda's national soil information system** (RwaSIS). Provides AI-assisted access to soil data, fertilizer recommendations, and parcel information for Rwandan agricultural land. The geographic scope is narrow but the use case is concrete — precision soil data for smallholder farmers in a country where agriculture employs over 70% of the workforce.

Complements Digital Green's FarmerChat-MCP (which covers multiple African countries) with more granular national-level soil data for Rwanda specifically. Very early stage (last commit April 23, 0 stars).

## What's Missing

The agriculture MCP category made real progress in April–May 2026, but significant gaps remain:

- **No official equipment manufacturer servers** — John Deere, Case IH (CNHi), AGCO (Massey Ferguson, Fendt), Kubota, and Claas have developer APIs but zero official MCP servers. The community CoreyFransen08 v2.0.0 server fills some of the John Deere gap, and FieldMCP provides commercial JD integration, but nothing is official.
- **Crop disease/pest gap partially closed** — agstack/opensource-pestmodels (Linux Foundation, 54 threats, 19 crops) addresses systematic pest risk modeling. PlantVillage-style AI disease image identification remains absent.
- **Irrigation gap partially closed** — koolsb/open-sprinkler-mcp covers OpenSprinkler hardware. Center-pivot and drip irrigation systems (Valley, Lindsay, Netafim) have no MCP representation.
- **No grain commodity trading** — no MCP servers for CME/CBOT grain futures, USDA crop reports, or global agricultural commodity analysis. agrobr-mcp covers Brazil specifically; nothing for global grain markets.
- **No aquaculture or fisheries** — shrimp farming, fish pond management, and marine aquaculture have no MCP representation.
- **No vineyard or orchard management** — wine grape growing, fruit tree management, and specialty crop production are absent.
- **Limited livestock** — only sheep breeding is covered. No cattle, poultry, swine, or dairy MCP servers exist.
- **FarmerChat frozen** — Digital Green's most sophisticated agricultural advisory system has had no code commits since November 2025; its future development trajectory is uncertain.

## The Bottom Line

**Rating: 3.5 / 5**

Agriculture & farming MCP made its most significant single-month leap in May 2026. The **agstack/opensource-pestmodels server** — backed by the Linux Foundation — fills the most glaring gap from the previous review (crop disease and pest identification) with a 13-model, 19-crop, 54-threat framework. The **CoreyFransen08 v2.0.0 rewrite** brought equipment management, machine health, and work plans to the community John Deere MCP. A **dedicated irrigation hardware MCP** (open-sprinkler-mcp) appeared for the first time. A **sophisticated plant breeding research MCP** (brapi-mcp-server) now provides multi-database access for crop genomics work.

The category still has meaningful gaps — no official equipment manufacturer servers, no global grain commodity trading, no vineyard/orchard or major livestock coverage. And some previously notable entries have gone stale: agri-weather-mcp (10 months frozen), FarmerChat-MCP (6+ months frozen), and the GAP East Africa server has been deleted. The servers that are active are improving meaningfully; the ones that aren't are fading from relevance.

**Best for farm data integration:** Leaf Agriculture MCP (unified API across platforms)
**Best commercial platform:** FieldMCP ($29/org/month, John Deere live, 150+ decision rules)
**Best community John Deere integration:** CoreyFransen08/john-deere-ops-mcp (v2.0.0, 4 stars, equipment + machine health)
**Best for pest and disease risk:** agstack/opensource-pestmodels (Linux Foundation, 13 models, 54 threats)
**Best for smallholder farmers:** Digital Green FarmerChat-MCP (12 servers, 5 countries — note: frozen since Nov 2025)
**Best for plant breeding research:** cyanheads/brapi-mcp-server (BrAPI v2.1, active daily development)
**Best for satellite crop analysis:** Dhenenjay/axion-planetary-mcp (220 stars, AWS, 30+ datasets)
**Best for irrigation hardware:** koolsb/open-sprinkler-mcp (OpenSprinkler, first irrigation MCP)
**Best niche pick:** epicpast/nsip-api-client (sheep breeding genetics, 15 tools)
**Best zero-setup option:** AiAgentKarl/agriculture-mcp-server (8 tools, all free APIs)

*This review was last refreshed on 2026-05-20 using Claude Sonnet 4.6 (Anthropic).*
