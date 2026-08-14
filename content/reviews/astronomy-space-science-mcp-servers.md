---
title: "Astronomy & Space Science MCP Servers — NASA APIs, Telescope Control, Satellite Tracking, SpaceX, Astronomical Surveys, and Research Tools"
date: 2026-03-17T06:00:00+09:00
description: "Astronomy and space science MCP servers let AI agents access NASA data, control telescopes, track satellites, query astronomical surveys, and compute celestial positions through the Model Context Protocol."
og_description: "Astronomy & space science MCP servers: NASA-MCP-server (92 stars, 20+ APIs), nasa/earthdata-mcp (v1.0, 20 stars, new get_variables/get_citations tools), noaa-spaceweather-mcp (aurora alerting fills a gap), astro_mcp (40+ surveys), ASCOM telescope control, SpaceX MCP (Starship V3), CelestialMCP (120k-star catalog, 1 GitHub star), spacetrack-mcp (collision risk), overview-mcp/earthdeck (26 Earth-system tools). 25+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Astronomy and space science MCP servers for accessing NASA data, controlling telescopes, tracking satellites, exploring SpaceX launches, querying astronomical surveys, and computing celestial positions through AI assistants. This is a **maturing category** where the ecosystem has expanded significantly since our April refresh. **NASA API servers dominate** — ProgramComputer/NASA-MCP-server (92 stars) leads with access to 20+ NASA and JPL data sources. **NASA Earthdata hits v1.0** — nasa/earthdata-mcp (20 stars) released its first major version in late May, adding get_variables, get_citations, and get_keywords tools. **Aurora alerting is now covered** — cyanheads/noaa-spaceweather-mcp-server (June 2026) fills the previously identified gap with 6 NOAA SWPC tools including Kp index, aurora latitude guidance, and OVATION probability. **Satellite tracking has expanded dramatically** — kaushik701/spacetrack-mcp adds Space-Track collision risk queries, pipeworx-io/mcp-n2yo provides another N2YO option, and cstahly/satellites-overhead adds RTL-SDR capture scheduling and METEOR LRPT decoding. **Earth observation joins the mix** — marcoloco23/overview-mcp (now rebranded earthdeck) brings Sentinel-2 imagery, NASA GIBS overlays, wildfire/forest-alert monitoring, and climate time series across 26 tools. **SpaceX milestone** — Starship Version 3 successfully launched May 22, 2026; SpaceX's Pacific drone ship 'Of Course I Still Love You' logged its 200th booster landing June 3. **Remaining gaps** — no Stellarium integration, no JWST dedicated pipeline, no ESA/JAXA/ISRO official servers, no multi-provider launch schedule, no INDI protocol support. The category holds at 3.5/5 — the aurora gap is filled and satellite tracking has deepened, but international space agency participation and JWST data access remain absent."
last_refreshed: 2026-08-14
sources_audited: 2026-08-14
---

Astronomy and space science MCP servers connect AI agents to NASA data, telescope hardware, astronomical survey databases, satellite tracking systems, launch schedules, and celestial positioning tools. Instead of manually querying APIs, learning specialized astronomy software, or writing telescope control scripts, these servers let you explore space data and control observatory equipment through natural language via the Model Context Protocol. Part of our **[Science & Research MCP category](/categories/science-research/)**.

This review covers **NASA APIs, telescope control, astronomical data and research tools, celestial positioning, satellite tracking, rocket launch data, space weather, and Earth observation** — APOD, Mars rovers, near-Earth objects, space weather, exoplanets, DESI, SIMBAD, Gaia, ASCOM telescope automation, SpaceX launches, aurora alerting, Sentinel-2 imagery, and more. For weather and climate data on Earth, see our [Weather & Climate review](/reviews/weather-climate-mcp-servers/).

The headline findings: **NASA Earthdata hits v1.0** — nasa/earthdata-mcp reached its first major version in late May 2026 with new tools for variable discovery, citation lookup, and keyword browsing. **Aurora alerting fills a long-identified gap** — cyanheads/noaa-spaceweather-mcp-server launched June 5 with 6 NOAA SWPC tools covering aurora probability, Kp index, solar wind, and flare forecasts. **Satellite tracking has expanded** — spacetrack-mcp adds conjunction/collision risk queries, pipeworx-io launched mcp-n2yo and mcp-celestrak, and cstahly/satellites-overhead adds RTL-SDR automation. **Earth observation arrives** — marcoloco23/overview-mcp (rebranded earthdeck) provides Sentinel-2 imagery, NASA GIBS overlays, and a broader Earth-system tool set. **SpaceX milestone** — [Starship V3 debuted successfully May 22](https://www.space.com/news/live/spacex-starship-flight-12-launch-updates-may-22-2026). **Remaining gaps: no Stellarium integration, no JWST dedicated pipeline, no ESA/JAXA official servers.**

---

## NASA API Servers

### ProgramComputer/NASA-MCP-server — Comprehensive NASA & JPL Data Access

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server) | 92 | TypeScript | ISC | 17+ |

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

The standout NASA MCP server. At [92 stars](https://github.com/ProgramComputer/NASA-MCP-server) and 17+ API integrations spanning both api.nasa.gov and JPL Solar System Dynamics, this is the most complete gateway to NASA's public data. TypeScript with automatic parameter validation, rate limiting, and standardized output formats optimized for AI consumption. Works with Claude Desktop, Cursor, and SSE via SuperGateway. Maintenance has slowed — commit activity is sparse and mostly README updates — but organic discovery continues to push star count upward, and it remains the top-starred astronomy MCP server covered in this review.

### nasa/earthdata-mcp — Official NASA Earthdata MCP Server (v1.0)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [earthdata-mcp](https://github.com/nasa/earthdata-mcp) | 20 | Python | Government | Semantic search + 8+ tools |

**NASA's official MCP server for Earthdata** — under the [nasa GitHub org](https://github.com/nasa). This server reached its **v1.0 milestone in late May 2026** with a major cleanup and feature expansion (see the [commit history](https://github.com/nasa/earthdata-mcp/commits/main), which confirms the dates below via commit messages CMRNLP-99/100/103).

**New tools added since April 2026:**
- **get_variables** — discover variables within NASA Earthdata collections (added May 11)
- **get_citations** — DOI and collection citation discovery with reverse lookups (added April 24)
- **get_keywords** — KMS keyword discovery for navigating NASA's keyword taxonomy (added April 24)
- **Pagination** — full pagination implementation across all tools (v1.0 May 19)

The server uses **semantic search powered by embeddings** to help AI agents discover and access NASA's Earth science data holdings. The architecture includes MCP tool implementations, centralized data models, AWS Lambda handlers, and infrastructure-as-code via Terraform. The v1.0 release cleaned up legacy infrastructure and added pagination. With [20 stars and 12 forks](https://github.com/nasa/earthdata-mcp) as of August 2026, this is one of the more actively-starred astronomy MCPs on GitHub — backed by NASA's institutional commitment for long-term API stability.

While primarily focused on Earth observation rather than deep-space astronomy, this is the authoritative pipeline for NASA's satellite-based Earth science datasets — climate, weather, land use, ocean, and atmospheric data.

A community alternative, [datalayer/earthdata-mcp-server](https://github.com/datalayer/earthdata-mcp-server), provides similar Earthdata access with a different approach.

### jezweb/nasa-mcp-server — NASA Open APIs with Smart Caching

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nasa-mcp-server](https://github.com/jezweb/nasa-mcp-server) | 9 | Python | — | 8+ |

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
| [astro_mcp](https://github.com/SandyYuan/astro_mcp) | 5 | Python | — | 7+ |

**Unified access to the major astronomical survey databases:**

- **DESI** — Dark Energy Spectroscopic Instrument data (~1.8M EDR, 18M+ DR1 spectra via [SPARCL and Data Lab](https://datalab.noirlab.edu/data/desi))
- **Astroquery universal access** — automatic discovery of 40+ services including SIMBAD, VizieR, SDSS, Gaia, MAST, IRSA, ESASky, and many more
- **search_objects** — cross-survey object lookup
- **astroquery_query** — flexible queries against any supported service
- **get_spectrum_by_id** — spectral data retrieval
- **list_astroquery_services / search_astroquery_services** — service discovery and exploration
- **file management** — preview data, convert to FITS format, file statistics

The most ambitious astronomy MCP server. The vision is to transform big-data astronomy from a software engineering problem into natural language conversation — a student with little programming experience should be able to perform multi-survey analysis like an expert astronomer. Access to SIMBAD, Gaia, SDSS, MAST, and 30+ other services through a single interface is genuinely powerful for researchers. Active development continued in May 2026.

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

An early but fascinating project that goes beyond simple data access. Instead of one server wrapping one API, astro-orchestra orchestrates multiple specialized agents that collaborate on research tasks — planning studies, gathering data, running simulations, and reviewing literature. **Note: [no commits since July 2025](https://github.com/SandyYuan/astro-orchestra/commits/main); essentially dormant.** Still represents what AI-native scientific research could look like, and the companion astro_mcp server remains actively developed.

### prtc/nasa-ads-mcp — Astrophysics Literature Search

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nasa-ads-mcp](https://github.com/prtc/nasa-ads-mcp) | 7 | Python | MIT | 10 |

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
- **~120,000 stars** cataloged from the [HYG star database](https://www.astronexus.com/projects/hyg) (not to be confused with GitHub stars — this repo itself has [1 GitHub star](https://github.com/Rkm1999/CelestialMCP))
- **14,000+ deep-sky objects** from the OpenNGC catalog
- **astronomy-engine library** for precise calculations

The observational astronomy server. The star-hopping pathfinding tool is a standout — it calculates step-by-step navigation routes from bright reference stars to fainter targets, adjusting for your telescope's field of view. Useful for amateur astronomers planning observation sessions or anyone curious about what's visible in tonight's sky.

---

## Satellite Tracking & Orbital Intelligence

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
- **search_satellites** — browse 30 categories including ISS, Starlink, OneWeb, weather, navigation, and amateur radio satellites
- **Free tier** — [1,000 requests per hour](https://github.com/Cyreslab-AI/satellitetracking-mcp-server)

The established N2YO satellite tracking server. Covers ISS, Starlink, GPS, weather satellites, and more across 30 categories. Visual and radio pass predictions make it useful for both casual ISS spotters and amateur radio operators tracking signal windows. The free N2YO API tier is generous enough for personal use.

### pipeworx-io/mcp-n2yo — Pipeworx N2YO Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-n2yo](https://github.com/pipeworx-io/mcp-n2yo) | 0 | — | — | Multi-tool |

A second N2YO MCP wrapper from the pipeworx-io organization, launched June 7, 2026 as part of the [Pipeworx gateway](https://github.com/pipeworx-io/mcp-n2yo), which as of this refresh connects to [1,394+ live data sources](https://github.com/pipeworx-io/mcp-n2yo). The pipeworx-io family also includes **mcp-celestrak** (June 8) for CelesTrak satellite orbital elements and TLE/GP data, and **mcp-tle** for generic TLE tracking. No star count yet but the organization has demonstrated active maintenance across their MCP portfolio.

### kaushik701/spacetrack-mcp — Space-Track Conjunction & Catalog

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [spacetrack-mcp](https://github.com/kaushik701/spacetrack-mcp) | 0 | Python | — | 3 |

**Collision risk intelligence via the NASA/USSTRATCOM Space-Track API:**

- **TLE lookup** — orbital elements by NORAD ID
- **conjunction/CDM queries** — Conjunction Data Messages for satellite collision risk assessment
- **satellite catalog search** — query the official Space-Track catalog

Requires a free Space-Track.org account. Installs via `uvx spacetrack-mcp`. Uses diskcache for rate-limit compliance (30 requests/minute, 300/hour). This fills a niche that standard N2YO trackers don't cover — official conjunction data for orbital debris monitoring and active collision avoidance. Useful for mission operations professionals and researchers studying orbital congestion.

### cstahly/satellites-overhead — Pass Prediction & RTL-SDR Capture

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [satellites-overhead](https://github.com/cstahly/satellites-overhead) | 0 | — | — | Multi-tool |

**Integrated satellite tracking, capture scheduling, and signal decoding:**

- **Real-time overhead pass prediction** — when satellites pass over your location
- **RTL-SDR capture rules** — autonomous scheduling of software-defined radio recordings
- **METEOR LRPT decoding** — process imagery from Russian METEOR weather satellites
- **SatNOGS lookup** — frequency, modulation, and telemetry mode data per satellite
- **Autonomous campaign management** — run hands-off satellite observation sequences

Created June 3, 2026 (last updated June 10). Goes beyond pure tracking into the signal reception layer — relevant for amateur radio enthusiasts who want AI-driven satellite observation campaigns. The METEOR LRPT decoder is a rare capability: most satellite MCP tools stop at position prediction; this one can actually capture and decode the imagery.

---

## Telescope Control & Observatory Automation

### stellarpunk/mcp-server-ascom — ASCOM Alpaca Telescope Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-ascom](https://github.com/stellarpunk/mcp-server-ascom) | 0 | Python | — | Multi-device |

**MCP 2025-06-18 compliant server for controlling astronomy equipment** via the ASCOM Alpaca protocol. This fills one of the biggest gaps identified in our original review — amateur telescope control through AI agents.

- **Natural language commands** — "Point at M31" just works, with automatic coordinate resolution
- **Auto-discovery** — finds ASCOM Alpaca devices on the network with no manual configuration
- **Multi-device support** — telescopes, cameras, focusers, filter wheels, domes
- **Async operations** — non-blocking I/O so long exposures don't stall your AI session

ASCOM Alpaca is the network-based successor to the Windows-only ASCOM COM driver standard. By bridging MCP to Alpaca, this server lets any MCP-compatible AI assistant control a modern observatory setup. Install via pip, point it at your Alpaca devices, and your AI agent becomes a telescope operator.

### OnStepNinja/AiBridge — ESP32 AI-to-Telescope Bridge

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AiBridge](https://github.com/OnStepNinja/AiBridge) | 7 | C++ | MIT | Hardware control |

**An MCP server running on a $5 ESP32 microcontroller** that bridges AI agents directly to OnStep telescope mounts and ASCOM Alpaca devices. This is a remarkable piece of engineering — a full Model Context Protocol implementation running on embedded hardware.

- **GOTO commands** — slew to celestial coordinates
- **Park/unpark** — automated telescope storage and deployment
- **Tracking control** — sidereal, lunar, solar tracking modes
- **Relay control** — toggle observatory power, dew heaters, flat panel lights
- **Environmental sensing** — temperature, humidity, sky quality (with appropriate sensors)
- **SSE transport** — communicates with Claude and other AI agents over Server-Sent Events

The AiBridge approach is different from the ASCOM MCP server above — instead of running on a PC, it runs directly on the microcontroller that controls the telescope hardware. This means you can have AI-driven observatory automation without a full computer in the loop. [Repository activity continues into June 2026](https://github.com/OnStepNinja/AiBridge/commits/main).

---

## Rocket Launch & SpaceX Data

### pipeworx-io/mcp-spacex — SpaceX Launch Intelligence

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-spacex](https://github.com/pipeworx-io/mcp-spacex) | 0 | — | — | Multi-tool |

**SpaceX launch, rocket, crew, and Starlink data** via the community-maintained SpaceX API v4. No API key required — completely free access.

- **Launch data** — historical and upcoming launches, mission details, success/failure outcomes
- **Rocket specifications** — Falcon 9, Falcon Heavy, Starship technical details
- **Crew information** — astronaut profiles, crew assignments, mission roles
- **Starlink tracking** — satellite constellation status and deployment data
- **Company information** — SpaceX corporate data and milestones

**SpaceX milestones (May–June 2026):** [Starship Version 3 successfully launched May 22, 2026](https://www.space.com/news/live/spacex-starship-flight-12-launch-updates-may-22-2026) (Starship Flight Test 12) — the first flight of the new design. SpaceX also achieved its [50th Starlink mission of 2026 on May 30](https://spaceflightnow.com/2026/05/30/live-coverage-spacex-to-launch-50th-starlink-mission-of-2026/), and on June 3 its Pacific drone ship "Of Course I Still Love You" logged its [200th booster landing](https://spaceflightnow.com/2026/06/03/live-coverage-spacex-to-launch-24-starlink-satellites-on-falcon-9-rocket-from-vandenberg-3/) (that vessel's 200th, not SpaceX's all-time drone-ship total, which passed that mark years earlier). The SpaceX API v4 data covers historical milestones but real-time mission data typically reflects completed missions. Compatible with Claude Desktop, ChatGPT, and other MCP clients.

**Also available:** SpaceX Launch Intelligence on [Apify](https://apify.com/benthepythondev/spacex-launch-intelligence/api/mcp) provides a hosted MCP endpoint with similar capabilities.

---

## Space Weather & Aurora Alerting

*This section is new as of June 2026, addressing a gap identified in previous reviews.*

### cyanheads/noaa-spaceweather-mcp-server — NOAA SWPC Space Weather

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [noaa-spaceweather-mcp-server](https://github.com/cyanheads/noaa-spaceweather-mcp-server) | 1 | — | — | 6 |

**Direct access to NOAA Space Weather Prediction Center feeds** — launched June 5, 2026. This fills the aurora alerting and space weather gap identified in every previous version of this review.

- **Geomagnetic storm scales** — R/S/G scale classifications and current status
- **Kp index** — with aurora-latitude guidance (tells you how far south aurora may be visible)
- **OVATION aurora probability** — Aurora Borealis/Australis probability by coordinates
- **DSCOVR real-time solar wind** — speed, density, and Bz component (the key aurora trigger variable)
- **GOES X-ray flux** — solar flare monitoring and flare probabilities
- **SWPC alerts/watches/warnings** — official NOAA space weather advisories

All feeds are keyless/public from NOAA SWPC. [Data refresh rates](https://github.com/cyanheads/noaa-spaceweather-mcp-server): solar wind updates roughly every minute, the aurora probability map roughly every 5 minutes, and Kp index at 3-hour intervals. Supports both STDIO and Streamable HTTP transports. Only 1 star as of this refresh (launched in June 2026), but the capability is real and the source data is authoritative.

### lysechko1/space-intelligence-mcp — Asteroid & Space Weather Aggregator

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [space-intelligence-mcp](https://github.com/lysechko1/space-intelligence-mcp) | 0 | — | — | 11 |

**Multi-source space intelligence with a provenance-first design** — launched June 1, 2026.

- **Asteroid search** — JPL Small-Body Database object search
- **Full object profile** — comprehensive asteroid/comet data
- **Ephemeris** — orbital position over time
- **Close approaches** — upcoming near-Earth encounters
- **Space weather snapshot** — aggregated view from NASA JPL, NOAA SWPC, and DSCOVR

The ["disclaimers array on every response"](https://github.com/lysechko1/space-intelligence-mcp) design philosophy makes it useful in contexts where data attribution matters. The [roadmap](https://github.com/lysechko1/space-intelligence-mcp) targets DONKI flare events for v0.2, with CelesTrak/Space-Track satellite data pushed out to v0.4. Zero stars at launch; an early project but with a clear multi-source vision.

---

## Earth Observation

*This section is new as of June 2026.*

### marcoloco23/overview-mcp — Satellite Earth Observation, now rebranded "earthdeck"

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [overview-mcp](https://github.com/marcoloco23/overview-mcp) | 3 | — | — | 26 |

**Earth observation imagery and change detection via NASA and ESA Copernicus feeds** — launched June 5, 2026. Since our last refresh the project has [expanded well beyond its original Sentinel-2/GIBS scope and rebranded itself "earthdeck"](https://github.com/marcoloco23/overview-mcp), now shipping **26 tools** in total.

**Keyless tools (no account required) — 17 of the 26**, including:
- **eo_snapshot** — NASA GIBS true-color, false-color, and fire overlay imagery
- **events** — live natural events (wildfires, storms, volcanoes) via NASA EONET
- **geo_resolve** — place name to coordinates via OpenStreetMap
- **stac_search / narrate / eo_similar** — imagery discovery and AI-generated summaries
- **planet_pulse, enso, ocean_temp, co2, global_temp, sea_ice, quakes, climate_history, air_quality, river_discharge** — global climate and environmental time series (global_temp draws on records back to 1880)
- **earthdata_search** — NASA Earthdata catalog search

**Credentialed tools (free API keys required) — 9 of the 26:**
- **fires_in (NASA FIRMS)** — wildfire detection points with satellite source
- **eo_render, eo_index, eo_search, eo_compare, sar_render, sar_water, sar_flood** — Sentinel-2/Landsat/MODIS imagery, NDVI/NDWI/NBR indices, and SAR-based flood/water analysis via ESA Copernicus (CDSE)
- **forest_alerts (Global Forest Watch)** — deforestation alerts

Sentinel-2-based imagery is a significant addition to the MCP ecosystem — this is the data source professional remote sensing workflows rely on. The broadened scope (fire, forest, ocean, and climate time series alongside imagery) makes this one of the more ambitious Earth-observation MCP servers, though the "earthdeck" rename means the project is now closer to a general environmental-data server than the narrower "overview" imagery tool this review originally covered.

---

## What's Missing

The astronomy and space science MCP ecosystem has addressed several gaps identified in earlier reviews — aurora/space weather alerting is now covered, satellite tracking has expanded, and Earth observation with Sentinel-2 has arrived — but notable gaps remain:

- **No Stellarium integration** — the most popular open-source planetarium has no MCP bridge
- **No James Webb Space Telescope** — no dedicated JWST data pipeline server (JWST has produced landmark discoveries in May–June 2026: [the first chemical fingerprint — methane detection — from an interstellar object, comet 3I/ATLAS](https://science.nasa.gov/missions/webb/nasas-webb-finds-clues-to-ancient-distant-origin-of-comet-3i-atlas/), [the strongest spectral evidence yet for "black hole stars"](https://science.nasa.gov/missions/webb/nasa-webb-finds-strongest-evidence-yet-for-black-hole-stars/), and [a supermassive black hole (Abell 2744-QSO1) that appears to predate its host galaxy](https://science.nasa.gov/missions/webb/nasas-webb-reveals-black-hole-that-formed-before-its-galaxy/); none yet accessible via dedicated MCP tooling)
- **No ESA, JAXA, or ISRO official MCP servers** — NASA leads with earthdata-mcp (now at v1.0), but no other space agency has followed. [JAXA launched an H3 rocket (its new low-cost "H3-30" configuration) on June 12, 2026](https://global.jaxa.jp/press/2026/06/20260612-1_e.html) but has no MCP presence.
- **No INDI protocol support** — only ASCOM Alpaca; Linux-native INDI users (the majority of Linux observatory operators) have no MCP option
- **No non-SpaceX launch data** — no aggregated multi-provider launch schedule covering ULA, Rocket Lab, Arianespace, Blue Origin, JAXA, ISRO, etc.
- **No radio astronomy** — no servers for accessing radio telescope data, pulsar catalogs, or SETI datasets
- **No gravitational wave data** — no LIGO/Virgo event catalog access
- **No light pollution mapping** — no Bortle scale or sky quality data
- **No astrophotography workflows** — camera control exists via ASCOM MCP, but no image stacking, plate solving, or processing pipeline

---

## The Bottom Line

The astronomy and space science MCP ecosystem earns a **3.5 out of 5**.

**What works:** NASA API coverage remains the strongest it's been — ProgramComputer's server (92 stars, 17+ APIs) leads, and NASA's own earthdata-mcp (v1.0, 20 stars) adds official federal backing with new variable, citation, and keyword discovery tools. Telescope control via ASCOM MCP and AiBridge continues. SpaceX data covers the world's most active launch program, now with Starship V3 milestones in the data. The astronomical research tools from SandyYuan remain innovative. The satellite tracking ecosystem has expanded notably with space-track collision risk (spacetrack-mcp) and RTL-SDR automation (satellites-overhead).

**What's improved since April 2026:** Aurora alerting and space weather — the most consistently identified gap — is now covered by noaa-spaceweather-mcp-server with full NOAA SWPC integration. Earth observation via Sentinel-2 and NASA GIBS is now available through overview-mcp. Satellite orbital intelligence has deepened with Space-Track CDM data and CelesTrak TLE access. NASA earthdata-mcp reached v1.0 with expanded tooling.

**What doesn't:** The category still lacks international space agency participation — no ESA, JAXA, or ISRO servers despite active programs. No dedicated JWST data pipeline, despite JWST producing major discoveries regularly. INDI protocol users (Linux-native telescope control) have no MCP option. Launch data remains SpaceX-only. Radio astronomy and gravitational wave data remain inaccessible.

**Who benefits most:** Astronomy researchers wanting natural language access to survey databases. Amateur astronomers with ASCOM-compatible equipment who want AI-driven observation sessions. Aurora chasers tracking Kp index and solar wind conditions. Environmental researchers using Sentinel-2 change detection. Science communicators who need quick NASA imagery and data.

**Who should wait:** Anyone wanting JWST data analysis, multi-provider launch schedules, or INDI telescope support. Radio astronomy, gravitational wave, or SETI data users. Astrophotographers wanting image processing pipelines.

| Subcategory | Server Count | Top Server | Rating |
|-------------|-------------|------------|--------|
| NASA APIs | 4 | ProgramComputer/NASA-MCP-server (92 stars) | ★★★★ |
| Astronomical research | 3 | SandyYuan/astro_mcp (40+ services) | ★★★★ |
| Telescope control | 2 | stellarpunk/mcp-server-ascom (ASCOM Alpaca) | ★★★½ |
| Satellite tracking | 5 | Cyreslab-AI + spacetrack-mcp + pipeworx-io family | ★★★½ |
| Space weather | 2 | cyanheads/noaa-spaceweather-mcp-server (NOAA SWPC) | ★★★ |
| Earth observation | 1 | marcoloco23/overview-mcp / earthdeck (26 tools) | ★★★ |
| Rocket launches | 1 | pipeworx-io/mcp-spacex (SpaceX API v4) | ★★★ |
| Celestial positioning | 1 | Rkm1999/CelestialMCP (120k-star catalog, 14k DSOs) | ★★★ |

**Overall: 3.5/5** — A meaningfully expanded ecosystem since our April 2026 review. Aurora alerting fills a long-identified gap. NASA Earthdata reaches v1.0. Satellite tracking deepens with collision risk and SDR automation. Earth observation joins the category via Sentinel-2. But JWST data, international space agency participation, and multi-provider launch schedules remain absent.

*This review was refreshed on 2026-06-12 using Claude Sonnet 4.6 (Anthropic); citations and figures re-verified 2026-08-14. Originally published 2026-03-17.*
