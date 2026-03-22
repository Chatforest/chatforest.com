---
title: "Astronomy & Space Science MCP Servers — NASA APIs, Celestial Positioning, Satellite Tracking, Astronomical Surveys, and Research Tools"
date: 2026-03-17T06:00:00+09:00
description: "Astronomy and space science MCP servers let AI agents access NASA data, track satellites, query astronomical surveys, and compute celestial positions through the Model Context Protocol. We reviewed 12+ servers across 4 subcategories. NASA APIs (4 servers): ProgramComputer/NASA-MCP-server (81 stars, TypeScript, ISC — 20+ data sources including APOD, Mars Rover, NEO, DONKI, Exoplanet Archive, JPL Small-Body Database, GIBS, FIRMS), jezweb/nasa-mcp-server (8 stars, Python — APOD, Mars rovers, asteroids, media library, smart caching), AnCode666/nasa-mcp (6 stars, Python, MIT — APOD, NEO, DONKI space weather, Earth imagery, EPIC, Exoplanet Archive). Astronomical data & research (3 servers): SandyYuan/astro_mcp (3 stars, Python — 40+ astronomical services via astroquery, DESI survey, SIMBAD, VizieR, SDSS, Gaia, MAST), SandyYuan/astro-orchestra (1 star, Python, MIT — multi-agent research system with 5 specialized agents, MCP tool orchestration), prtc/nasa-ads-mcp (2 stars, Python, MIT — 10 tools, NASA ADS paper search, citations, BibTeX export, library management). Celestial positioning (1 server): Rkm1999/CelestialMCP (1 star, TypeScript, MIT — 3 tools, 117,000+ stars, 14,000 deep-sky objects, rise/set times, star-hopping paths). Satellite tracking (1 server): Cyreslab-AI/satellitetracking-mcp-server (3 stars, TypeScript, MIT — 6 tools, N2YO API, 31 satellite categories, visual/radio pass prediction). Gaps: no Stellarium integration, no James Webb Space Telescope data, no amateur telescope control (ASCOM/INDI), no aurora/space weather alerts, no planetarium tools, no SpaceX/launch schedule APIs, no radio astronomy, no gravitational wave data (LIGO). Rating: 3.5/5."
og_description: "Astronomy & space science MCP servers: NASA-MCP-server (81 stars, 20+ APIs), astro_mcp (40+ astronomical surveys), CelestialMCP (117k stars catalog), nasa-ads-mcp (paper search), satellitetracking-mcp (N2YO). 12+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Astronomy and space science MCP servers for accessing NASA data, tracking satellites, querying astronomical surveys, and computing celestial positions through AI assistants. This is a **fascinating emerging category** where scientific data access meets AI tooling. **NASA API servers dominate** — ProgramComputer/NASA-MCP-server (81 stars) leads with access to 20+ NASA and JPL data sources through a single TypeScript server, covering everything from the Astronomy Picture of the Day to exoplanet archives and near-Earth object tracking. **The astronomical research tooling is genuinely impressive** — SandyYuan/astro_mcp provides unified access to 40+ astronomical services (SIMBAD, VizieR, SDSS, Gaia, DESI, MAST, and more) through astroquery, effectively democratizing big-data astronomy by turning complex API choreography into natural language queries. **The astro-orchestra project takes it further** with a multi-agent system where specialized agents (planning, data gathering, analysis, simulation, literature review) collaborate on research tasks — a glimpse of AI-native scientific workflows. **NASA ADS integration is a standout niche** — prtc/nasa-ads-mcp gives AI assistants direct access to astrophysics literature search, citation metrics, and BibTeX export. **CelestialMCP fills the observational astronomy gap** with positioning data for 117,000+ stars and 14,000 deep-sky objects plus a star-hopping pathfinding tool. **Satellite tracking exists but is basic** — one server wraps the N2YO API for position tracking and pass predictions across 31 categories. **The biggest gaps are conspicuous** — no Stellarium or planetarium integration, no James Webb Space Telescope data pipeline, no amateur telescope control (ASCOM/INDI), no SpaceX or launch schedule APIs, no aurora/space weather alerting beyond raw DONKI data, no radio astronomy or gravitational wave tools. The category earns 3.5/5 — the NASA API coverage is solid and the astronomical research tools are genuinely innovative, but consumer-facing space experiences (launch tracking, aurora alerts, telescope control) are largely absent."
last_refreshed: 2026-03-17
---

Astronomy and space science MCP servers connect AI agents to NASA data, astronomical survey databases, satellite tracking systems, and celestial positioning tools. Instead of manually querying APIs or learning specialized astronomy software, these servers let you explore space data through natural language via the Model Context Protocol.

This review covers **NASA APIs, astronomical data and research tools, celestial positioning, and satellite tracking** — APOD, Mars rovers, near-Earth objects, space weather, exoplanets, DESI, SIMBAD, Gaia, and more. For weather and climate data on Earth, see our [Weather & Climate review](/reviews/weather-climate-mcp-servers/).

The headline findings: **NASA API servers are the strongest segment** — NASA-MCP-server (81 stars) gives access to 20+ data sources from api.nasa.gov and JPL. **Astronomical research tools are genuinely innovative** — astro_mcp connects to 40+ survey services through astroquery, while astro-orchestra orchestrates multi-agent research workflows. **CelestialMCP provides observational data** for 117,000+ stars and 14,000 deep-sky objects. **The biggest gap: no amateur telescope control, no launch schedule APIs, and no aurora alerting.**

---

## NASA API Servers

### ProgramComputer/NASA-MCP-server — Comprehensive NASA & JPL Data Access

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server) | 81 | TypeScript | ISC | 20+ |

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

The standout NASA MCP server. At 81 stars and 20+ API integrations spanning both api.nasa.gov and JPL Solar System Dynamics, this is the most complete gateway to NASA's public data. TypeScript with automatic parameter validation, rate limiting, and standardized output formats optimized for AI consumption. Works with Claude Desktop, Cursor, and SSE via SuperGateway.

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
| [nasa-ads-mcp](https://github.com/prtc/nasa-ads-mcp) | 2 | Python | MIT | 10 |

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
| [satellitetracking-mcp-server](https://github.com/Cyreslab-AI/satellitetracking-mcp-server) | 3 | TypeScript | MIT | 6 |

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

## What's Missing

The astronomy and space science MCP ecosystem has notable gaps:

- **No telescope control** — no ASCOM or INDI protocol servers for controlling amateur telescopes, mounts, or cameras remotely
- **No Stellarium integration** — the most popular open-source planetarium has no MCP bridge
- **No James Webb Space Telescope** — no dedicated JWST data pipeline server (some data is accessible through MAST via astro_mcp)
- **No SpaceX or launch schedule APIs** — no rocket launch tracking, countdown, or mission data
- **No aurora/space weather alerting** — DONKI raw data exists in NASA servers, but no dedicated aurora prediction or geomagnetic storm alert server
- **No radio astronomy** — no servers for accessing radio telescope data, pulsar catalogs, or SETI datasets
- **No gravitational wave data** — no LIGO/Virgo event catalog access
- **No light pollution mapping** — no Bortle scale or sky quality data
- **No astrophotography tools** — no image stacking, plate solving, or camera control
- **No planetary simulation** — no Kerbal-style orbital mechanics or mission planning

---

## The Bottom Line

The astronomy and space science MCP ecosystem earns a **3.5 out of 5**.

**What works:** NASA API coverage is solid — ProgramComputer's server gives you 20+ data sources in one package. The astronomical research tools from SandyYuan are genuinely innovative, turning complex multi-survey data access into natural language. NASA ADS integration is a practical win for researchers. CelestialMCP's star-hopping feature is a clever niche tool for amateur astronomers.

**What doesn't:** The category is heavily skewed toward professional/research use. Consumer-facing space experiences — launch tracking, aurora alerts, "what's in the sky tonight" — are largely absent or buried in raw API outputs. Satellite tracking exists but is limited to one server wrapping one API. The total server count is modest compared to more established categories.

**Who benefits most:** Astronomy researchers and data scientists who want natural language access to survey databases. Science communicators who need quick access to NASA imagery and data. Amateur astronomers who want celestial positioning data. Students exploring astronomy data without learning complex APIs.

**Who should wait:** Anyone wanting telescope automation, launch tracking, or polished consumer space experiences. The tools for casual space enthusiasts are still thin — you'll get more from dedicated apps than from MCP servers right now.

| Subcategory | Server Count | Top Server | Rating |
|-------------|-------------|------------|--------|
| NASA APIs | 3 | ProgramComputer/NASA-MCP-server (81 stars) | ★★★★ |
| Astronomical research | 3 | SandyYuan/astro_mcp (40+ services) | ★★★★ |
| Celestial positioning | 1 | Rkm1999/CelestialMCP (117k stars, 14k DSOs) | ★★★ |
| Satellite tracking | 1 | Cyreslab-AI/satellitetracking-mcp-server (6 tools) | ★★★ |

**Overall: 3.5/5** — Strong scientific data access and innovative research tools, but thin on consumer-facing space experiences and missing major data sources like JWST, launch schedules, and telescope control.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
