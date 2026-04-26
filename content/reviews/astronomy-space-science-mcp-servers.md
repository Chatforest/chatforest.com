---
title: "Astronomy & Space Science MCP Servers — NASA APIs, Telescope Control, Satellite Tracking, SpaceX, Astronomical Surveys, and Research Tools"
date: 2026-03-17T06:00:00+09:00
description: "Astronomy and space science MCP servers let AI agents access NASA data, control telescopes, track satellites, query astronomical surveys, and compute celestial positions through the Model Context Protocol."
og_description: "Astronomy & space science MCP servers: NASA-MCP-server (83 stars, 20+ APIs), nasa/earthdata-mcp (official NASA), astro_mcp (40+ astronomical surveys), ASCOM telescope control, AiBridge ESP32 telescope automation, SpaceX MCP (launches+rockets+Starlink), CelestialMCP (117k stars catalog), nasa-ads-mcp (paper search+citations+BibTeX), satellitetracking-mcp (N2YO 31 categories). 18+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Astronomy and space science MCP servers for accessing NASA data, controlling telescopes, tracking satellites, exploring SpaceX launches, querying astronomical surveys, and computing celestial positions through AI assistants. This is a **maturing category** where scientific data access meets AI tooling — and several gaps identified in our original review have now been filled. **NASA API servers dominate** — ProgramComputer/NASA-MCP-server (83 stars) leads with access to 20+ NASA and JPL data sources through a single TypeScript server. **NASA has released an official MCP server** — nasa/earthdata-mcp provides semantic search across NASA Earthdata with embedding-powered discovery, deployed on AWS Lambda. **Telescope control has arrived** — stellarpunk/mcp-server-ascom brings MCP 2025-06-18 compliant ASCOM Alpaca control (natural language telescope commands, auto-discovery, async operations), and OnStepNinja/AiBridge (6 stars, MIT) runs an MCP server on an ESP32 microcontroller bridging AI agents directly to OnStep telescope mounts. **SpaceX data is now accessible** — pipeworx-io/mcp-spacex provides launch history, rocket specs, crew data, and Starlink tracking via the SpaceX API v4 with no API key required. **The astronomical research tooling is genuinely impressive** — SandyYuan/astro_mcp provides unified access to 40+ astronomical services (SIMBAD, VizieR, SDSS, Gaia, DESI, MAST) through astroquery. **The astro-orchestra project takes it further** with a multi-agent system where specialized agents collaborate on research tasks. **NASA ADS integration is strong** — prtc/nasa-ads-mcp (3 stars, 10 tools) gives access to astrophysics literature search, citation metrics, and BibTeX export, with a second implementation from ivan-katkov offering Solr syntax queries. **CelestialMCP fills the observational gap** with positioning data for 117,000+ stars and 14,000 deep-sky objects plus star-hopping pathfinding. **Satellite tracking covers 31 categories** via N2YO API with visual and radio pass predictions. **Remaining gaps** — no Stellarium integration, no JWST dedicated pipeline, no aurora alerting, no radio astronomy/LIGO data, no ESA/JAXA/ISRO official servers. The category earns 3.5/5 — NASA coverage is comprehensive (including an official server now), telescope control and SpaceX data fill major previous gaps, but consumer-facing polish and international space agency participation remain thin."
last_refreshed: 2026-04-26
---

Astronomy and space science MCP servers connect AI agents to NASA data, telescope hardware, astronomical survey databases, satellite tracking systems, launch schedules, and celestial positioning tools. Instead of manually querying APIs, learning specialized astronomy software, or writing telescope control scripts, these servers let you explore space data and control observatory equipment through natural language via the Model Context Protocol. Part of our **[Science & Research MCP category](/categories/science-research/)**.

This review covers **NASA APIs, telescope control, astronomical data and research tools, celestial positioning, satellite tracking, and rocket launch data** — APOD, Mars rovers, near-Earth objects, space weather, exoplanets, DESI, SIMBAD, Gaia, ASCOM telescope automation, SpaceX launches, and more. For weather and climate data on Earth, see our [Weather & Climate review](/reviews/weather-climate-mcp-servers/).

The headline findings: **NASA has gone official** — nasa/earthdata-mcp is NASA's own MCP server for Earthdata semantic search, joining the comprehensive community NASA-MCP-server (83 stars, 20+ APIs). **Telescope control has arrived** — ASCOM MCP server and AiBridge now let AI agents point telescopes, control cameras, and manage observatory equipment via natural language. **SpaceX data is accessible** — launches, rockets, crew, and Starlink tracking with no API key needed. **Astronomical research tools are genuinely innovative** — astro_mcp connects to 40+ survey services through astroquery. **CelestialMCP provides observational data** for 117,000+ stars and 14,000 deep-sky objects. **Remaining gaps: no Stellarium integration, no JWST dedicated pipeline, no ESA/JAXA official servers.**

---

## NASA API Servers

### ProgramComputer/NASA-MCP-server — Comprehensive NASA & JPL Data Access

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server) | 83 | TypeScript | ISC | 17+ |

**The most comprehensive NASA data server with 20+ API integrations:**

- **APOD** — Astronomy Picture of the Day with scientific explanations and high-resolution imagery
- **Mars Rover Photos** — imagery from Curiosity, Perseverance, Opportunity, and Spirit
- **NEO (Near Earth Objects)** — asteroid tracking, hazardous object identification, orbital data
- **DONKI** — Space Weather Database with solar flare and geomagnetic storm data
- **Exoplanet Archive** — queries against NASA's exoplanet database
- **EPIC** — Earth Polychromatic Imaging Camera full-disk Earth imagery
- **TLE** — Two-Line Element satellite orbital data
- **NASA Image and Video Library** — searchable media archive
- **EONET** — Earth Observatory natural event tracking
- **NASA Sounds API** — audio from missions and space
- **POWER** — Prediction of Worldwide Energy Resources
- **JPL Small-Body Database** — asteroid and comet orbital parameters
- **JPL Close-Approach Data** — upcoming near-Earth encounters
- **JPL Fireball Data** — atmospheric impact events
- **JPL Scout** — newly discovered object analysis
- **GIBS** — Global Imagery Browse Services satellite imagery
- **CMR** — Common Metadata Repository for Earth science data
- **FIRMS** — Fire Information for Resource Management System

The standout NASA MCP server. At 83 stars and 17+ API integrations spanning both api.nasa.gov and JPL Solar System Dynamics, this is the most complete gateway to NASA's public data. TypeScript with automatic parameter validation, rate limiting, and standardized output formats optimized for AI consumption. Works with Claude Desktop, Cursor, and SSE via SuperGateway.

### nasa/earthdata-mcp — Official NASA Earthdata MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [earthdata-mcp](https://github.com/nasa/earthdata-mcp) | — | Python | Government | Semantic search |

**NASA's official MCP server for Earthdata** — under the [nasa GitHub org](https://github.com/nasa). This is significant: it's an official NASA-maintained MCP server, joining GovInfo and Census Bureau as U.S. federal agencies directly supporting the protocol.

The server uses **semantic search powered by embeddings** to help AI agents discover and access NASA's Earth science data holdings. The architecture includes MCP tool implementations, centralized data models, AWS Lambda handlers for processing and enrichment, and infrastructure-as-code via Terraform.

While primarily focused on Earth observation data rather than deep-space astronomy, this is the authoritative pipeline for NASA's satellite-based Earth science datasets — climate, weather, land use, ocean, and atmospheric data. The official status means guaranteed API stability and long-term support that community servers can't promise.

A community alternative, [datalayer/earthdata-mcp-server](https://github.com/datalayer/earthdata-mcp-server), provides similar Earthdata access with a different approach.

### jezweb/nasa-mcp-server — NASA Open APIs with Smart Caching

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nasa-mcp-server](https://github.com/jezweb/nasa-mcp-server) | 8 | Python | — | 8+ |

**Focused NASA API access with multi-tier caching:**

- **APOD** — daily astronomy imagery with date lookup and random discovery
- **Mars Rover Operations** — photos from all four rovers, search by sol or Earth date, multiple cameras
- **Asteroid Tracking** — real-time approach monitoring, hazardous object identification
- **NASA Media Library** — searchable image and video collection
- **Smart caching** — 30-minute image cache, 10-minute dynamic data cache
- **Built-in prompts** — space_exploration, mars_mission_report, asteroid_watch, daily_space_brief

A more focused alternative to the TypeScript server above. Includes pre-built prompts for common space exploration queries and multi-tier caching to manage API rate limits. Good for users who want curated NASA data without the full 20+ API surface.

### AnCode666/nasa-mcp — DONKI Space Weather & Exoplanets

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nasa-mcp](https://github.com/AnCode666/nasa-mcp) | 6 | Python | MIT | 6 |

**NASA API access with space weather and exoplanet focus:**

- **APOD** — Astronomy Picture of the Day
- **Asteroids NeoWs** — near-Earth object data
- **DONKI** — solar flares, geomagnetic storms, coronal mass ejections
- **Earth imagery** — Landsat 8 satellite photos for specific coordinates
- **EPIC** — full-disk Earth images
- **Exoplanet Archive** — database queries for confirmed exoplanets

Lighter-weight NASA server with MIT license and Docker support. Integrates with Claude Desktop, Cursor, CODEGPT, and Roo Code. The DONKI (space weather) and Exoplanet Archive tools make it useful for researchers tracking solar activity or studying planetary systems.

---

## Astronomical Data & Research

### SandyYuan/astro_mcp — 40+ Astronomical Survey Services

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [astro_mcp](https://github.com/SandyYuan/astro_mcp) | 3 | Python | — | 7+ |

**Unified access to the major astronomical survey databases:**

- **DESI** — Dark Energy Spectroscopic Instrument data (1.8M EDR, 18M+ DR1 spectra via SPARCL and Data Lab)
- **Astroquery universal access** — automatic discovery of 40+ services including SIMBAD, VizieR, SDSS, Gaia, MAST, IRSA, ESASky, and many more
- **search_objects** — cross-survey object lookup
- **astroquery_query** — flexible queries against any supported service
- **get_spectrum_by_id** — spectral data retrieval
- **list_astroquery_services / search_astroquery_services** — service discovery and exploration
- **file management** — preview data, convert to FITS format, file statistics

The most ambitious astronomy MCP server. The vision is to transform big-data astronomy from a software engineering problem into natural language conversation — a student with little programming experience should be able to perform multi-survey analysis like an expert astronomer. Access to SIMBAD, Gaia, SDSS, MAST, and 30+ other services through a single interface is genuinely powerful for researchers.

### SandyYuan/astro-orchestra — Multi-Agent Astronomy Research System

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [astro-orchestra](https://github.com/SandyYuan/astro-orchestra) | 1 | Python | MIT | Multi-agent |

**Orchestrated research system with specialized AI agents:**

- **Orchestrator Agent** — coordinates tasks across the research pipeline
- **Planning Agent** — structures research methodologies
- **Data Gathering Agent** — retrieves datasets via MCP tool servers
- **Analysis Agent** — statistical computations and data analysis
- **Theorist/Simulation Agent** — cosmological simulations (N-body, etc.)
- **Literature Reviewer Agent** — aggregates scientific papers from ArXiv
- **Human-in-the-loop** — researchers review and provide feedback during the process
- **MCP integration** — connects to DESI, LSST, CMB databases, statistics processors, and literature tools

An early but fascinating project that goes beyond simple data access. Instead of one server wrapping one API, astro-orchestra orchestrates multiple specialized agents that collaborate on research tasks — planning studies, gathering data, running simulations, and reviewing literature. Still in active development but represents what AI-native scientific research could look like.

### prtc/nasa-ads-mcp — Astrophysics Literature Search

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nasa-ads-mcp](https://github.com/prtc/nasa-ads-mcp) | 3 | Python | MIT | 10 |

**Direct access to NASA's Astrophysics Data System:**

- **search_papers** — search the ADS database by keywords, authors, dates
- **get_paper_details** — retrieve full metadata for specific papers
- **get_author_papers** — find all papers by a given author
- **get_paper_metrics** — citation counts and impact metrics
- **get_author_metrics** — author-level bibliometric data
- **export_bibtex** — export references in BibTeX format
- **list_libraries / get_library_papers** — browse personal ADS libraries
- **create_library / add_to_library** — manage reference collections

A focused tool for astronomers and astrophysicists who live in NASA ADS. Having paper search, citation metrics, and BibTeX export directly in your AI assistant is genuinely useful for literature reviews and writing papers. Requires a NASA ADS API key.

**Alternative implementation:** [ivan-katkov/nasa-ads-mcp](https://github.com/ivan-katkov/nasa-ads-mcp) (0 stars, Python) provides 5 tools (search, get_record, get_bibtex, get_citations, get_references) with full Solr query syntax support and multiple output formats (short, detailed, bibtex). A lighter alternative if you don't need library management features.

---

## Celestial Positioning

### Rkm1999/CelestialMCP — Star Catalog & Object Positioning

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CelestialMCP](https://github.com/Rkm1999/CelestialMCP) | 1 | TypeScript | MIT | 3 |

**Real-time celestial positioning with extensive star and deep-sky catalogs:**

- **getCelestialDetails** — equatorial and horizontal coordinates, visibility status, rise/transit/set times, distance (solar system), phase illumination (Moon/planets), upcoming lunar phases
- **listCelestialObjects** — browse by category: planets, stars, Messier, NGC, IC, and other deep-sky objects
- **getStarHoppingPath** — calculate navigation paths from bright stars to target objects using specified field-of-view parameters
- **117,000+ stars** from the HYG star database
- **14,000+ deep-sky objects** from the OpenNGC catalog
- **astronomy-engine library** for precise calculations

The observational astronomy server. The star-hopping pathfinding tool is a standout — it calculates step-by-step navigation routes from bright reference stars to fainter targets, adjusting for your telescope's field of view. Useful for amateur astronomers planning observation sessions or anyone curious about what's visible in tonight's sky.

---

## Satellite Tracking

### Cyreslab-AI/satellitetracking-mcp-server — N2YO Satellite Tracking

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [satellitetracking-mcp-server](https://github.com/Cyreslab-AI/satellitetracking-mcp-server) | 4 | TypeScript | MIT | 6 |

**Real-time satellite tracking via N2YO API:**

- **get_satellite_position** — real-time positioning by NORAD ID
- **get_satellite_tle** — Two-Line Element orbital data
- **predict_visual_passes** — when a satellite will be visible from your location
- **predict_radio_passes** — radio signal windows for amateur radio operators
- **get_satellites_above** — find all satellites currently overhead at given coordinates
- **search_satellites** — browse 31 categories including ISS, Starlink, OneWeb, weather, navigation, and amateur radio satellites
- **Free tier** — 1,000 requests per hour

The go-to server for satellite tracking. Covers ISS, Starlink, GPS, weather satellites, and more across 31 categories. Visual and radio pass predictions make it useful for both casual ISS spotters and amateur radio operators tracking signal windows. The free N2YO API tier is generous enough for personal use.

---

## Telescope Control & Observatory Automation

### stellarpunk/mcp-server-ascom — ASCOM Alpaca Telescope Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-ascom](https://github.com/stellarpunk/mcp-server-ascom) | — | Python | — | Multi-device |

**MCP 2025-06-18 compliant server for controlling astronomy equipment** via the ASCOM Alpaca protocol. This fills one of the biggest gaps identified in our original review — amateur telescope control through AI agents.

- **Natural language commands** — "Point at M31" just works, with automatic coordinate resolution
- **Auto-discovery** — finds ASCOM Alpaca devices on the network with no manual configuration
- **Multi-device support** — telescopes, cameras, focusers, filter wheels, domes
- **Async operations** — non-blocking I/O so long exposures don't stall your AI session

ASCOM Alpaca is the network-based successor to the Windows-only ASCOM COM driver standard. By bridging MCP to Alpaca, this server lets any MCP-compatible AI assistant control a modern observatory setup. Install via pip, point it at your Alpaca devices, and your AI agent becomes a telescope operator.

### OnStepNinja/AiBridge — ESP32 AI-to-Telescope Bridge

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AiBridge](https://github.com/OnStepNinja/AiBridge) | 6 | C++ | MIT | Hardware control |

**An MCP server running on a $5 ESP32 microcontroller** that bridges AI agents directly to OnStep telescope mounts and ASCOM Alpaca devices. This is a remarkable piece of engineering — a full Model Context Protocol implementation running on embedded hardware.

- **GOTO commands** — slew to celestial coordinates
- **Park/unpark** — automated telescope storage and deployment
- **Tracking control** — sidereal, lunar, solar tracking modes
- **Relay control** — toggle observatory power, dew heaters, flat panel lights
- **Environmental sensing** — temperature, humidity, sky quality (with appropriate sensors)
- **SSE transport** — communicates with Claude and other AI agents over Server-Sent Events

The AiBridge approach is different from the ASCOM MCP server above — instead of running on a PC, it runs directly on the microcontroller that controls the telescope hardware. This means you can have AI-driven observatory automation without a full computer in the loop. Active development (last commit February 2026).

---

## Rocket Launch & SpaceX Data

### pipeworx-io/mcp-spacex — SpaceX Launch Intelligence

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-spacex](https://github.com/pipeworx-io/mcp-spacex) | — | — | — | Multi-tool |

**SpaceX launch, rocket, crew, and Starlink data** via the community-maintained SpaceX API v4. No API key required — completely free access.

- **Launch data** — historical and upcoming launches, mission details, success/failure outcomes
- **Rocket specifications** — Falcon 9, Falcon Heavy, Starship technical details
- **Crew information** — astronaut profiles, crew assignments, mission roles
- **Starlink tracking** — satellite constellation status and deployment data
- **Company information** — SpaceX corporate data and milestones

This fills another gap from our original review — rocket launch tracking. The SpaceX API v4 is community-maintained (the [r-spacex/SpaceX-API](https://github.com/r-spacex/SpaceX-API) project) and is the de facto standard for SpaceX data access. Compatible with Claude Desktop, ChatGPT, and other MCP clients.

**Also available:** SpaceX Launch Intelligence on [Apify](https://apify.com/benthepythondev/spacex-launch-intelligence/api/mcp) provides a hosted MCP endpoint with similar capabilities.

---

## What's Missing

The astronomy and space science MCP ecosystem has narrowed its gaps since our March 2026 review — telescope control and SpaceX data have arrived — but notable holes remain:

- **No Stellarium integration** — the most popular open-source planetarium has no MCP bridge
- **No James Webb Space Telescope** — no dedicated JWST data pipeline server (some data is accessible through MAST via astro_mcp)
- **No ESA, JAXA, or ISRO official MCP servers** — NASA leads with earthdata-mcp, but no other space agency has followed
- **No aurora/space weather alerting** — DONKI raw data exists in NASA servers, but no dedicated aurora prediction or geomagnetic storm alert server
- **No radio astronomy** — no servers for accessing radio telescope data, pulsar catalogs, or SETI datasets
- **No gravitational wave data** — no LIGO/Virgo event catalog access
- **No light pollution mapping** — no Bortle scale or sky quality data
- **No astrophotography workflows** — camera control exists via ASCOM MCP, but no image stacking, plate solving, or processing pipeline
- **No INDI protocol support** — only ASCOM Alpaca; Linux-native INDI users have no MCP option
- **No non-SpaceX launch data** — no aggregated launch schedule covering all providers (ULA, Rocket Lab, Arianespace, etc.)

---

## The Bottom Line

The astronomy and space science MCP ecosystem earns a **3.5 out of 5**.

**What works:** NASA API coverage is now the strongest it's been — ProgramComputer's server gives you 17+ data sources, and NASA's own earthdata-mcp adds official federal backing. Telescope control has arrived via ASCOM MCP and the AiBridge ESP32 project, turning AI agents into observatory operators. SpaceX data fills the launch tracking gap. The astronomical research tools from SandyYuan remain genuinely innovative. NASA ADS integration is a practical win for researchers.

**What's improved since March 2026:** Two of the biggest gaps — telescope control and rocket launch data — have been filled. NASA has joined the handful of federal agencies with official MCP servers. A second NASA ADS implementation adds choice for literature access. Star counts are growing modestly across the ecosystem.

**What doesn't:** The category still lacks international space agency participation — no ESA, JAXA, or ISRO servers. No dedicated JWST data pipeline. Aurora/space weather alerting remains raw DONKI data without user-friendly predictions. INDI protocol users (Linux-native telescope control) have no MCP option. Launch data is SpaceX-only — no aggregated multi-provider schedule.

**Who benefits most:** Astronomy researchers wanting natural language access to survey databases. Amateur astronomers with ASCOM-compatible equipment who want AI-driven observation sessions. Science communicators who need quick NASA imagery and data. Students exploring astronomy without learning complex APIs. Space enthusiasts tracking SpaceX launches.

**Who should wait:** Anyone wanting polished aurora alerts, JWST data analysis, or non-SpaceX launch schedules. INDI users without ASCOM Alpaca compatibility. Anyone needing radio astronomy, gravitational wave, or SETI data access.

| Subcategory | Server Count | Top Server | Rating |
|-------------|-------------|------------|--------|
| NASA APIs | 4 | ProgramComputer/NASA-MCP-server (83 stars) | ★★★★ |
| Astronomical research | 3 | SandyYuan/astro_mcp (40+ services) | ★★★★ |
| Telescope control | 2 | stellarpunk/mcp-server-ascom (ASCOM Alpaca) | ★★★½ |
| Rocket launches | 1 | pipeworx-io/mcp-spacex (SpaceX API v4) | ★★★ |
| Celestial positioning | 1 | Rkm1999/CelestialMCP (117k stars, 14k DSOs) | ★★★ |
| Satellite tracking | 1 | Cyreslab-AI/satellitetracking-mcp-server (6 tools) | ★★★ |

**Overall: 3.5/5** — Significantly improved since our March 2026 review. NASA official participation, telescope control, and SpaceX data fill major gaps. The research tooling remains innovative. But international space agency participation, JWST, aurora alerting, and multi-provider launch schedules keep this from a higher rating.

*This review was refreshed on 2026-04-26 using Claude Opus 4.6 (Anthropic). Originally published 2026-03-17.*
