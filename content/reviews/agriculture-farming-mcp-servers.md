---
title: "Agriculture & Farming MCP Servers — Leaf, John Deere, FieldMCP, FarmerChat, Weather, Satellite Imagery, and More"
date: 2026-03-15T15:00:00+09:00
description: "Agriculture and farming MCP servers are bringing AI to precision agriculture, crop planning, pest modeling, and farm data management. We reviewed 25+ servers across 9 subcategories."
og_description: "Agriculture & farming MCP servers: agstack/opensource-pestmodels (Linux Foundation, 54 threats, 19 crops), CoreyFransen08 John Deere MCP (equipment + machine health), FieldMCP ($29/org/month), open-sprinkler-mcp (first irrigation hardware MCP), brapi-mcp-server (plant breeding research), Axion Planetary (221 stars, SAR-to-optical). Rating: 3.5/5."
content_type: "Review"
card_description: "Agriculture and farming MCP servers for precision agriculture, crop planning, pest modeling, irrigation management, and farm data integration. May 2026 brought the most active month in agriculture MCP history. The Linux Foundation's agstack/opensource-pestmodels fills the long-missing crop pest/disease gap with 13 models covering 19 crops and 54 threats. The community John Deere MCP (CoreyFransen08) added equipment management and machine health monitoring. The first dedicated irrigation hardware MCP (open-sprinkler-mcp) appeared. A sophisticated plant breeding database server (brapi-mcp-server) now covers Breedbase and BrAPI v2.1 endpoints with near-daily development. Two commercial vendors (Leaf Agriculture, FieldMCP at $29/org/month) remain the enterprise options. Axion Planetary MCP holds at 221 stars for satellite crop analysis. The category earns 3.5/5 — the ecosystem is visibly maturing with serious institutional backing entering the space."
last_refreshed: 2026-08-14
sources_audited: 2026-08-14
---

Agriculture and farming MCP servers are bringing AI assistants into precision agriculture, crop planning, livestock management, and farm data analysis. Instead of navigating multiple dashboards for field data, weather forecasts, soil conditions, and market prices, these servers let AI agents pull farm-specific intelligence and generate actionable recommendations — all through the Model Context Protocol.

The landscape spans nine areas: **unified farm data platforms** (Leaf Agriculture, FieldMCP, John Deere Operations Center), **general-purpose agriculture tools** (soil, weather, climate history, global statistics), **agricultural weather intelligence** (soil conditions, evapotranspiration, crop-specific alerts), **market data** (commodity prices, crop estimates), **smallholder farmer AI** (multi-source agricultural advisory), **livestock and breeding** (genetic evaluation, breeding decisions), **satellite earth observation** (NDVI, crop health monitoring, land use analysis), **pest and disease modeling** (risk scoring, integrated pest management), and **plant breeding research** (germplasm databases, genotype analysis).

The headline findings: **May 2026 was the most active month in agriculture MCP history.** The Linux Foundation's **agstack/opensource-pestmodels** fills the long-missing crop pest/disease gap — 13 models, 19 crops, 54 threats, with a fuzzy Mamdani inference engine and full MCP tooling. **CoreyFransen08's community John Deere MCP added** equipment management, machine health, and work plans — a meaningful capability leap from the March 2026 launch (note: an earlier version of this page attached a "v2.0.0" version label and release date to this that we could not verify against the repo — see the corrected section below). **The first dedicated irrigation hardware MCP appeared** (open-sprinkler-mcp, OpenSprinkler controllers). **cyanheads/brapi-mcp-server** provides multi-database plant breeding research access with near-daily development in May. On the commercial side, **two vendors (Leaf Agriculture, FieldMCP at $29/org/month) continue competing** for enterprise farm data integration. **No major equipment manufacturer has released an official MCP server** — everything for John Deere, Case IH, and AGCO remains community-built or third-party. One correction from an earlier version of this page: Digital Green's FarmerChat-MCP was previously described as "frozen since November 2025," but that claim was sourced to the wrong GitHub repository (an unrelated Digital Green chatbot codebase with no MCP code). Digital Green hasn't published FarmerChat-MCP's code publicly as far as we can find, so its development status can't actually be verified — see the corrected section below.

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
| [CoreyFransen08/john-deere-ops-mcp](https://github.com/CoreyFransen08/john-deere-ops-mcp) | 8 | TypeScript | — | — |

**CoreyFransen08/john-deere-ops-mcp** runs as a remote MCP server on Cloudflare Workers with a Durable Object providing stateful sessions. The clever part is its **double OAuth proxy pattern** — the Worker acts as an OAuth server to MCP clients downstream, and as an OAuth client to John Deere upstream. This means any MCP-compatible client can authenticate without needing to implement John Deere's OAuth flow directly.

Correction: an earlier version of this page described a "Version 2.0.0" release dated May 16–18, 2026, with specifics like an OAuth 2.1 flow and CORS configuration via `API_ALLOWED_ORIGINS`. Re-checking the repo, none of that holds up — there is no v2.0.0 tag, no GitHub release, no CHANGELOG, and the current `package.json` still reports version `1.0.0`; "OAuth 2.1" and `API_ALLOWED_ORIGINS` don't appear anywhere in the current README. What the [README](https://github.com/CoreyFransen08/john-deere-ops-mcp) does confirm: an interactive `npm run setup` deployment walkthrough and capabilities for **equipment management, work plans, and machine health monitoring** alongside the original organizations/fields/field-operations coverage. It targets the JD developer sandbox environment specifically — max 5 connected organizations, max 150,000 API calls/month, 18-month maximum sandbox duration.

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
| [bruno-portfolio/agrobr-mcp](https://github.com/bruno-portfolio/agrobr-mcp) | 26 | Python | MIT | 4+ |

Connects LLMs to **19 public Brazilian agricultural data sources** — the most comprehensive agricultural market data MCP server we've found in any country. Data sources include:

- **CEPEA/ESALQ** — daily spot prices for agricultural commodities
- **B3** — daily adjustments for agricultural futures contracts
- **CONAB** — current crop estimates by state
- **IBGE PAM** — historical production data by state
- **INPE** — deforestation monitoring data
- **NASA POWER** — climate data for agricultural applications

Available tools include `preco_diario` (spot prices), `futuros_b3` (futures adjustments), `estimativa_safra` (crop estimates), and `producao_anual` (historical production). All data logic lives in the separate `agrobr` Python library, which handles collection, parsing, and caching — the MCP server is a thin wrapper for text formatting.

Brazil is [one of the world's largest agricultural producers](https://www.ers.usda.gov/topics/international-markets-us-trade/countries-regions/brazil/) — including soybeans, coffee, sugar, and orange juice — so having comprehensive MCP access to Brazilian agricultural data is globally significant, not just locally useful.

## Smallholder Farmer AI

### FarmerChat-MCP (Digital Green)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Digital Green: "Bridging Fields and Futures" (FarmerChat-MCP technical write-up)](https://medium.com/digitalgreen-techblog/bridging-fields-and-futures-agricultural-intelligence-with-farmerchat-mcp-5a38ed72b537) | N/A | N/A | N/A | 12 servers |

**Correction (2026-08-14 audit):** an earlier version of this page cited `digitalgreenorg/DG_Open` as FarmerChat-MCP's source repo and claimed it had been "frozen since November 2025 with no new commits." That repo is real and its last commit is indeed from November 23, 2025 — but it's a *different* Digital Green project (a Django/OpenAI-based Farmer.Chat chatbot + FarmStack monorepo). Its README never mentions MCP, iSDA, NASA GRACE, OpenElevation, or iNaturalist. We could not find a public GitHub repository for FarmerChat-MCP itself; the only primary source we could locate is Digital Green's own January 2026 technical blog post, linked above.

The **most ambitious agricultural MCP project** we've reviewed, per that write-up. Digital Green — [a nonprofit](https://en.wikipedia.org/wiki/Digital_Green) focused on smallholder agricultural advisory — describes FarmerChat-MCP as a unified agricultural intelligence system using **twelve interconnected MCP servers** that power multiple interfaces without duplicate code. Because there's no public repo to check, we can't independently verify whether development is active, paused, or anything in between — we're not repeating the "frozen since November 2025" claim, since that was sourced to the wrong project entirely.

The architecture, per the write-up, synthesizes data from multiple sources in parallel:

- **Soil analysis** — via iSDA (Africa-specific data) and Google Earth Engine/OpenLandMap
- **Weather conditions** — via Open-Meteo
- **Groundwater data** — via NASA GRACE satellite
- **Elevation data** — via OpenElevation
- **Species/pest identification** — via iNaturalist
- **Satellite and crop intelligence** — via Google DeepMind's AnthroKrishi API

The write-up's detailed walkthrough example is drawn from a real deployment in **Bihar, India** (Araria district, Bhaisalotan village), where the assistant synthesizes soil type, weather forecast, elevation, and groundwater data into crop and planting recommendations.

The write-up documents this system operating in **India**; it doesn't establish that this specific MCP architecture is live in other countries, so we've dropped the "India, Ethiopia, Kenya, Nigeria, and Nepal" claim that appeared in an earlier version of this page — we couldn't verify it, and Nepal in particular doesn't show up in any Digital Green source we could find (their broader, separate, non-MCP FarmerChat product's own materials mention Ethiopia, Kenya, and Nigeria, not Nepal). This is not a hobbyist project — it's described as production infrastructure for agricultural extension.

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
| [Dhenenjay/axion-planetary-mcp](https://github.com/Dhenenjay/axion-planetary-mcp) | 221 | Python | — | 30+ datasets |
| [Dhenenjay/Axion-MCP](https://github.com/Dhenenjay/Axion-MCP) | 4 | Python | — | 30+ datasets |

The **most-starred agriculture-adjacent MCP server** (221 stars as of this audit, up from 220). Axion Planetary MCP is the V2 rewrite of the original Axion-MCP, with a major architectural shift: **migrated from Google Cloud/GEE to AWS**, introduced a proprietary "Axion Foundation Model" for SAR-to-optical image conversion, NPM package distribution, and API key authentication instead of GCP credentials. 935 commits — but the last commit was February 19, 2026, and there's been no new activity since (confirmed still true as of this August 2026 audit). Growing passively on reputation.

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
| [agstack/opensource-pestmodels](https://github.com/agstack/opensource-pestmodels) | 1 | Python | Apache-2.0 | 3+ |

The **most technically serious new agriculture MCP server** found in this refresh. [AgStack is a Linux Foundation project](https://www.linuxfoundation.org/press/agstack-first-dataset-field-boundaries) building open-source digital infrastructure for agriculture, which provides a credibility and longevity signal that no individual developer project can match.

The underlying pest-and-disease-model codebase in this repo dates back to 2020, but the **MCP server layer specifically was added May 18, 2026** — the commit history shows the MCP mount and quick-start docs landing that day. It wraps a **13-model, 19-crop, 54-threat hierarchical pest and disease modeling framework**:

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

A **new MCP server for Rwanda's national soil information system** (RwaSIS). Provides AI-assisted access to soil data, fertilizer recommendations, and parcel information for Rwandan agricultural land. The geographic scope is narrow but the use case is concrete — precision soil data for smallholder farmers in a country where, [per the World Bank](https://www.worldbank.org/en/news/press-release/2025/04/01/rwandas-afe-economy-registers-robust-growth-in-2024-despite-global-challenges), "agriculture remains the cornerstone of Rwanda's economy, employing 40% of the workforce and contributing 27% to GDP." (An earlier version of this page cited a stale 55% figure from the World Bank's modeled ILO employment indicator, which has since been revised down — that indicator now shows the estimate falling toward 35% by 2025, illustrating just how volatile these modeled estimates are; the April 2025 World Bank press release above is a more stable, directly quotable figure.)

Complements Digital Green's iSDA-based soil layer in FarmerChat-MCP (see above) with more granular national-level soil data for Rwanda specifically. Very early stage (last commit April 23, 0 stars).

## What's Missing

The agriculture MCP category made real progress in April–May 2026, but significant gaps remain:

- **No official equipment manufacturer servers** — John Deere, Case IH (CNHi), AGCO (Massey Ferguson, Fendt), Kubota, and Claas have developer APIs but zero official MCP servers. The community CoreyFransen08/john-deere-ops-mcp server (equipment management, work plans, machine health) fills some of the John Deere gap, and FieldMCP provides commercial JD integration, but nothing is official.
- **Crop disease/pest gap partially closed** — agstack/opensource-pestmodels (Linux Foundation, 54 threats, 19 crops) addresses systematic pest risk modeling. PlantVillage-style AI disease image identification remains absent.
- **Irrigation gap partially closed** — koolsb/open-sprinkler-mcp covers OpenSprinkler hardware. Center-pivot and drip irrigation systems (Valley, Lindsay, Netafim) have no MCP representation.
- **No grain commodity trading** — no MCP servers for CME/CBOT grain futures, USDA crop reports, or global agricultural commodity analysis. agrobr-mcp covers Brazil specifically; nothing for global grain markets.
- **No aquaculture or fisheries** — shrimp farming, fish pond management, and marine aquaculture have no MCP representation.
- **No vineyard or orchard management** — wine grape growing, fruit tree management, and specialty crop production are absent.
- **Limited livestock** — only sheep breeding is covered. No cattle, poultry, swine, or dairy MCP servers exist.
- **FarmerChat-MCP has no public repository** — Digital Green's most sophisticated agricultural advisory system, per its January 2026 technical write-up, doesn't appear to have published code we can find, so its development trajectory can't be independently verified.

## The Bottom Line

**Rating: 3.5 / 5**

Agriculture & farming MCP made its most significant single-month leap in May 2026. The **agstack/opensource-pestmodels server** — backed by the [Linux Foundation](https://www.linuxfoundation.org/press/agstack-first-dataset-field-boundaries) — fills the most glaring gap from the previous review (crop disease and pest identification) with a 13-model, 19-crop, 54-threat framework. **CoreyFransen08/john-deere-ops-mcp** added equipment management, machine health, and work plans to the community John Deere MCP. A **dedicated irrigation hardware MCP** (open-sprinkler-mcp) appeared for the first time. A **sophisticated plant breeding research MCP** (brapi-mcp-server) now provides multi-database access for crop genomics work.

The category still has meaningful gaps — no official equipment manufacturer servers, no global grain commodity trading, no vineyard/orchard or major livestock coverage. And some previously notable entries have gone stale: agri-weather-mcp (no commits since July 2025) and the GAP East Africa server ([eagleisbatman/gap-agriculture-mcp](https://github.com/eagleisbatman/gap-agriculture-mcp), now 404 — deleted or made private). The servers that are active are improving meaningfully; the ones that aren't are fading from relevance.

**Best for farm data integration:** Leaf Agriculture MCP (unified API across platforms)
**Best commercial platform:** FieldMCP ($29/org/month, John Deere live, 150+ decision rules)
**Best community John Deere integration:** CoreyFransen08/john-deere-ops-mcp (8 stars, equipment + machine health)
**Best for pest and disease risk:** agstack/opensource-pestmodels (Linux Foundation, 13 models, 54 threats)
**Best for smallholder farmers:** Digital Green FarmerChat-MCP (12 servers, per its Jan 2026 technical write-up — no public code repo we could find)
**Best for plant breeding research:** cyanheads/brapi-mcp-server (BrAPI v2.1, active daily development)
**Best for satellite crop analysis:** Dhenenjay/axion-planetary-mcp (221 stars, AWS, 30+ datasets)
**Best for irrigation hardware:** koolsb/open-sprinkler-mcp (OpenSprinkler, first irrigation MCP)
**Best niche pick:** epicpast/nsip-api-client (sheep breeding genetics, 15 tools)
**Best zero-setup option:** AiAgentKarl/agriculture-mcp-server (8 tools, all free APIs)

*This review was last refreshed on 2026-05-20 and citation-audited on 2026-08-14 using Claude Sonnet 5 (Anthropic).*
