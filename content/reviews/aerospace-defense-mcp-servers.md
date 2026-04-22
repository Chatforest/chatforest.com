---
title: "Aerospace & Defense MCP Servers — NASA Official Earthdata, Flightradar24 Official, STK, MAVLink, Axion V2.0, Satellite Imagery, Drones, and More"
date: 2026-03-15T18:30:00+09:00
lastmod: 2026-04-22T18:30:00+09:00
description: "Aerospace and defense MCP servers are enabling AI agents to query NASA data, simulate orbital mechanics, control drones, track flights via Flightradar24's official API, order satellite imagery, and plan space missions."
og_description: "Aerospace & defense MCP servers: NASA official earthdata-mcp (8 stars, first official NASA MCP), NASA community (83 stars, 20+ APIs), Flightradar24 official (16 stars, 15 tools), Axion V2.0 (218 stars, AWS rebuild, SAR-to-optical), IO-Aerospace (SPICE astrodynamics, hosted), STK MCP (26 stars, Ansys bridge), aerospace-mcp (62 commits, 44+ tools), MAVLinkMCP (16 stars, drone control), SkyFi (commercial satellite imagery), Planetary Computer MCP, OpenSky Network MCP. Rating: 3.5/5."
content_type: "Review"
card_description: "Aerospace and defense MCP servers across NASA data access, orbital mechanics, aviation operations, drone control, satellite tracking, and earth observation. Two watershed developments since March 2026: NASA published its first official MCP server (nasa/earthdata-mcp, 8 stars, 139 commits) providing semantic search over the Common Metadata Repository, and Flightradar24 released an official MCP server (16 stars, 15 tools) — the first major flight tracking platform to ship MCP support, filling a gap we flagged in March. The community space data landscape is anchored by ProgramComputer/NASA-MCP-server (83 stars, TypeScript, npm v1.0.11) providing AI access to 20+ NASA APIs. Earth observation saw the biggest leap: Dhenenjay's Axion MCP (218 stars, +15%) completed a V2.0 rebuild on AWS with 935 commits and introduced an exclusive SAR-to-optical foundation model for cloud-free Earth observation. Commercial satellite imagery ordering arrived via SkyFi MCP (150+ satellite providers) and Microsoft Planetary Computer MCP for STAC data. For orbital mechanics, IO-Aerospace's MCP server (16 stars, 31 commits) remains the production-grade SPICE-powered endpoint at mcp.io-aerospace.org. alti3/stk-mcp grew to 26 stars bridging LLMs to Ansys STK. Aviation expanded with Flightradar24 official (live positions, historical data back to 2016, airline/airport reference) plus community alternatives (sunsetcoder, 46 stars) and an OpenSky Network MCP for open ADS-B data. cheesejaguar/aerospace-mcp continues as the most comprehensive server with 44+ tools and 62 commits spanning aviation and space. Drone control matured with MAVLinkMCP (16 stars) and a January 2026 academic paper demonstrating real UAV flight control via LLM-MCP. Astronomical data access expanded with astro_mcp (60 commits, DESI/SIMBAD/Gaia/40+ services). Defense remains completely absent — no contractors, no C2 systems, no military logistics. The category holds at 3.5/5 — NASA going official and Flightradar24 entering are significant milestones, and earth observation is thriving, but defense is still entirely absent and several subcategories remain thin."
last_refreshed: 2026-04-22
---

Aerospace and defense MCP servers are enabling AI agents to query NASA's vast data archives, simulate orbital mechanics with SPICE-level accuracy, control drones via natural language, track flights through Flightradar24's official API, order commercial satellite imagery, and analyze earth observation data — all through natural language. Instead of writing Python scripts to query the APOD API or manually running STK scenarios, an AI agent can handle it conversationally: "Show me near-earth asteroids approaching within 5 lunar distances this week, then calculate an observation window from my location."

This review covers the **aerospace and defense** vertical — space data access, orbital mechanics, aviation operations, drone/UAV control, satellite tracking, and earth observation. For weather data more broadly, see our [Weather & Climate MCP review](/reviews/weather-climate-mcp-servers/). For geospatial mapping platforms (Mapbox, Google Maps), see our [Geospatial & Mapping MCP review](/reviews/geospatial-mapping-mcp-servers/). For cybersecurity tools, see our [Code Security MCP review](/reviews/code-security-mcp-servers/). For dedicated flight tracking and aviation operations, see our [Aviation & Flight MCP review](/reviews/aviation-flight-mcp-servers/).

The landscape spans seven areas: **NASA & space data** (APOD, Mars rovers, NEO, space weather, Earthdata), **orbital mechanics & astrodynamics** (SPICE, STK, orbital propagation), **aviation** (Flightradar24 official, FAA APIs, airport databases, flight tracking, weather), **drones & UAV** (MAVLink, DJI Tello), **satellite tracking & imagery** (TLE data, pass predictions, SkyFi commercial imagery, Planetary Computer), **earth observation** (Axion V2.0 on AWS, Google Earth Engine, SAR-to-optical AI), and **GIS & spatial analysis** (geocoding, routing, coordinate transforms).

The headline findings: **NASA published its first official MCP server** — nasa/earthdata-mcp provides semantic search over the Common Metadata Repository. **Flightradar24 shipped an official MCP server** with 15 tools for live and historical flight data — the first major flight tracking platform to enter the MCP ecosystem. **Axion V2.0 rebuilt on AWS** with 935 commits and an exclusive SAR-to-optical foundation model. **Commercial satellite imagery** arrived via SkyFi MCP. **IO-Aerospace provides production-grade astrodynamics** with a hosted endpoint. **MAVLink MCP bridges AI to millions of real drones**, now backed by academic research. **Defense is still completely absent** — no defense contractors or military-adjacent tools exist in the MCP ecosystem.

**Category:** [Logistics & Industry](/categories/logistics-industry/)

## NASA & Space Data

### NASA Earthdata MCP (Official)

| Server | Stars | Language | License | Commits |
|--------|-------|----------|---------|---------|
| [nasa/earthdata-mcp](https://github.com/nasa/earthdata-mcp) | 8 | Python | — | 139 |

**NASA's first official MCP server**, providing semantic search over the Common Metadata Repository (CMR) — the central catalog for all NASA Earth science data. Created November 2025, actively developed with 139 commits:

- **get_collections** — search for datasets using scientific keywords, instruments, or spatial/temporal parameters
- **get_granules** — locate specific data files within collections to verify availability
- **get_services** — find data access endpoints (OPeNDAP, Harmony) and visualization layers
- **get_tools** — discover web portals and downloadable software associated with datasets

Follows a structured "Discover → Verify → Access" workflow, guiding LLM clients through systematic data discovery and authentication using the earthaccess Python library. Uses embeddings for semantic search. AWS Lambda-based architecture with Terraform infrastructure-as-code. This is a significant milestone — the first time a space agency has published an official MCP server.

A community alternative, [datalayer/earthdata-mcp-server](https://github.com/datalayer/earthdata-mcp-server) (23 stars), provides a separate implementation focused on dataset search and granule downloading.

### NASA MCP Server (Community)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ProgramComputer/NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server) | 83 | TypeScript | MIT | 20+ |

The **most comprehensive NASA data gateway** for AI agents, providing standardized access to 20+ NASA APIs through a single MCP server. Now at npm v1.0.11 with 31 commits:

- **Astronomy Picture of the Day (APOD)** — daily curated images with professional astronomical explanations
- **Mars Rover Photos** — imagery from Curiosity, Opportunity, and Spirit, filterable by sol, camera, and Earth date
- **Near Earth Objects (NEO)** — asteroid tracking with close-approach data from the Center for Near Earth Object Studies
- **Space Weather (DONKI)** — coronal mass ejections, solar flares, geomagnetic storms, radiation belt enhancement, and interplanetary shock events
- **Earth Polychromatic Imaging Camera (EPIC)** — full-disk Earth images from the DSCOVR satellite at L1
- **Earth Observatory Natural Event Tracker (EONET)** — wildfires, severe storms, volcanic eruptions, and other events
- **TLE (Two-Line Element)** — satellite orbital data
- **JPL Solar System Dynamics** — small body lookups, orbit visualizations
- **POWER** — NASA's Prediction of Worldwide Energy Resources for solar/wind energy and agricultural data
- **NASA Image and Video Library** — searchable archive of NASA imagery

Security features include Zod-based input validation and sanitization. Available as an npm package for easy integration with Claude Desktop and other MCP clients. PulseMCP shows 4,700 all-time visitors, ranking #3,250 globally.

### Other NASA & Space Science Implementations

| Server | Language | Notes |
|--------|----------|-------|
| [AnCode666/nasa-mcp](https://github.com/AnCode666/nasa-mcp) | Python | Community alternative, curated API set |
| [jezweb/nasa-mcp-server](https://github.com/jezweb/nasa-mcp-server) | — | APOD, Mars rovers, asteroids, Earth imagery |
| [adithya1012/NASA-MCP-Server](https://github.com/adithya1012/NASA-MCP-Server) | — | Additional NASA API implementation |
| [SandyYuan/astro_mcp](https://github.com/SandyYuan/astro_mcp) | Python | **NEW** — 60 commits, DESI + 40+ astroquery services |

Multiple community implementations exist alongside the primary server. The n8n workflow platform also offers a [NASA Tool MCP Server template](https://n8n.io/workflows/5118-nasa-tool-mcp-server-all-15-operations/) covering 15 operations for workflow automation.

**NEW: astro_mcp** is a modular MCP server providing unified access to multiple astronomical datasets — DESI spectroscopic data and 40+ astroquery services (SIMBAD, VizieR, SDSS, Gaia, and more). Features coordinate-based searches, object type filtering, redshift selection, SQL queries across surveys, spectral retrieval, and FITS format conversion. Aims to transform big-data astronomy from a software engineering problem into a natural language conversation.

## Orbital Mechanics & Astrodynamics

### IO Aerospace MCP Server

| Server | Stars | Language | License | Transport | Commits |
|--------|-------|----------|---------|-----------|---------|
| [IO-Aerospace-software-engineering/mcp-server](https://github.com/IO-Aerospace-software-engineering/mcp-server) | 16 | .NET (C#) | — | Streamable HTTP, SSE | 31 |

The **most technically sophisticated astrodynamics MCP server**, powered by the IO Astrodynamics framework which provides a .NET wrapper around CSPICE — the same astrodynamics library used by NASA, ESA, and JAXA for mission planning:

- **Celestial Body Ephemeris** — precise positions of planets, moons, and other solar system bodies
- **Orbital Conversions** — transform between Keplerian elements, state vectors, and other orbital representations
- **Deep Space Station (DSS) Tools** — ground station visibility and communication window calculations
- **Time Conversions** — UTC, TDB, TT, TAI, and other time systems used in astrodynamics
- **Unit & Math Utilities** — coordinate frame transformations and unit conversions

The key differentiator: **production-hosted endpoint** at `mcp.io-aerospace.org` with streamable HTTP transport. No local installation needed — connect any MCP client to the hosted instance and start computing orbits immediately. Also supports SSE for legacy clients and Docker-based self-hosting with SPICE kernel configuration.

### Ansys STK MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [alti3/stk-mcp](https://github.com/alti3/stk-mcp) | 26 | Python | — | 5+ |

Bridges LLMs to **Ansys/AGI Systems Tool Kit (STK)**, the industry-standard digital mission engineering software used by NASA, ESA, Boeing, and defense agencies worldwide:

- **Scenario Setup** — create and configure STK scenarios with start/stop times and epoch
- **Facility Creation** — create ground stations at specific latitude/longitude/altitude
- **Satellite Configuration** — create satellites from apogee/perigee, RAAN, and inclination with TwoBody propagation
- **Access Computation** — calculate line-of-sight access intervals between objects (satellite-to-ground, satellite-to-satellite)
- **Ephemeris Export** — return satellite LLA (latitude, longitude, altitude) over the scenario interval

Requires STK Desktop (Windows) or STK Engine (Windows/Linux) with Python 3.12+. The modular architecture separates CLI, MCP server, STK logic, and tool definitions. This is the only MCP bridge to commercial mission engineering software — significant for organizations already using STK for satellite constellation design, sensor coverage analysis, and mission planning.

### Orbit MCP (BuildASpacePro)

| Server | Language | Notes |
|--------|----------|-------|
| [BuildASpacePro/Orbit-MCP](https://github.com/BuildASpacePro/Orbit-MCP) | — | Satellite orbital mechanics |

A specialized orbital mechanics MCP server with practical mission planning features:

- **Satellite Access Windows** — calculate when satellites are visible from ground locations
- **TLE Generation** — create Two-Line Element sets for various orbit types (LEO, MEO, GEO, SSO, Molniya, Polar)
- **Lighting Analysis** — ground and satellite illumination conditions
- **World Cities Database** — 200+ cities built in for easy location lookup
- **Natural Language Parsing** — extract orbital parameters from conversational text
- **Bulk Processing** — CSV import for multiple satellites and locations

Communicates via JSON-RPC 2.0 over stdio with Docker support.

## Aviation

### Aerospace MCP (cheesejaguar)

| Server | Language | Tools | Notes |
|--------|----------|-------|-------|
| [cheesejaguar/aerospace-mcp](https://github.com/cheesejaguar/aerospace-mcp) | Python | 44+ | Aviation + space, FastMCP, 62 commits |

The **most comprehensive aerospace MCP server**, spanning both aviation and space domains with 44+ tools:

**Aviation capabilities:**
- **Airport Resolution** — intelligent search across 28,000+ airports worldwide
- **Route Calculation** — great-circle distance and bearing between airports
- **Aircraft Performance** — performance estimation and flight envelope analysis
- **Atmospheric Modeling** — ISA and non-standard atmosphere calculations

**Space capabilities:**
- **Orbital Mechanics** — propagation, rendezvous planning, trajectory optimization
- **Spacecraft Trajectory** — interplanetary mission planning
- **Coordinate Transforms** — between reference frames used in aerospace

**Aerodynamics & propulsion:**
- **Aerodynamic Analysis** — lift, drag, moment coefficient calculations
- **Propeller Performance** — efficiency and thrust modeling
- **Rocket Trajectory Optimization** — launch vehicle ascent planning

Available via Docker or UV package manager. The website at aeroastro.org provides API documentation. **Important disclaimer:** for educational and research purposes only — not certified by any aviation authority.

### Flightradar24 Official MCP (NEW)

| Server | Stars | Language | Tools | Notes |
|--------|-------|----------|-------|-------|
| [Flightradar24/fr24api-mcp](https://github.com/Flightradar24/fr24api-mcp) | 16 | Node.js | 15 | **Official**, 16 commits |

**The first major flight tracking platform to ship an MCP server.** Flightradar24 — the world's most popular flight tracking service — released an official MCP server providing comprehensive aviation data access:

- **Live flight data** (3 tools) — real-time aircraft positions globally, basic/full position data, flight counts
- **Historical flight data** (3 tools) — past positions and historical counts going back to May 2016
- **Flight summaries** (3 tools) — takeoff/landing information with flexible filtering
- **Specific flight tracking** (1 tool) — detailed trajectory data for individual flights
- **Reference data** (5 tools) — airline and airport information in basic/comprehensive formats

Supports filtering by geographic bounds, flight numbers, callsigns, registrations, altitude ranges, routes, and aircraft categories. Requires a Flightradar24 API key. This fills a major gap we flagged in our March review.

A popular community alternative, [sunsetcoder/flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server) (46 stars), provides a simpler Claude Desktop integration for real-time flight tracking, arrival/departure times, airport status, and emergency flight monitoring.

### OpenSky Network MCP (NEW)

An MCP server for real-time aircraft tracking via the OpenSky Network API — an open, crowd-sourced ADS-B data network. Track flights by ICAO code or search aircraft near any location. This fills another gap from our March review where we noted no open ADS-B data sources had MCP support.

### Aviation Weather & Data Servers

| Server | Language | Notes |
|--------|----------|-------|
| [blevinstein/aviation-mcp](https://github.com/blevinstein/aviation-mcp) | — | FAA APIs, weather + charts |
| [finack/aviation-mcp](https://github.com/finack/aviation-mcp) | — | Flight planning weather |
| [Pradumnasaraf/aviationstack-mcp](https://github.com/Pradumnasaraf/aviationstack-mcp) | Python | AviationStack API, real-time flights |

**blevinstein/aviation-mcp** provides modular MCP servers mapping directly to FAA and other aviation APIs:
- **Aviation Weather** — METAR, TAF, PIREP, SIGMET, G-AIRMET reports (no API key required)
- **Charts** — sectional, TAC, IFR enroute, and terminal procedure charts
- **NOTAMs** — Notice to Air Missions (requires FAA client ID/secret)
- **Airspace Data** — machine-readable airspace boundaries

**finack/aviation-mcp** focuses specifically on aviation weather for flight planning — query METARs, TAFs, PIREPs, and full route weather profiles between two airports. Sources from aviationweather.gov. Includes explicit disclaimer: not FAA-approved, not a replacement for certified weather services.

**Pradumnasaraf/aviationstack-mcp** connects to the AviationStack API for real-time and historical flight data:
- Airline flight tracking and airport schedules
- Future flight schedules
- Aircraft types and airline reference data

Built with FastMCP, each endpoint exposed as a decorated `@mcp.tool()` function.

## Drones & UAV

### MAVLink MCP

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [ion-g-ion/MAVLinkMCP](https://github.com/ion-g-ion/MAVLinkMCP) | 16 | Python | MAVLink protocol, PX4/ArduPilot |

The **most significant drone MCP server**, enabling natural language control of drones via the MAVLink protocol — the standard communication protocol used by PX4 and ArduPilot, the two largest drone software platforms running on millions of drones worldwide. Now backed by academic research — a [January 2026 paper on arXiv](https://arxiv.org/html/2601.15486v1) demonstrated real UAV flight control via LLM-MCP with 15,000 lines of code, 45 tools, and integration with Google Maps MCP for real-time navigation:

- **Natural Language Commands** — the LLM interprets intent and translates to MAVLink commands
- **Telemetry Access** — real-time sensor data, GPS position, battery status, flight mode
- **Flight Control** — takeoff, landing, waypoint navigation, mode switching
- **Protocol Breadth** — MAVLink supports hundreds of commands for diverse drone types

The MCP server handles all drone communication, providing the LLM with capability descriptions for context-aware command generation. Compatible with any MAVLink-enabled vehicle — quadcopters, fixed-wing, VTOL, rovers, and submarines. Works with both physical hardware and simulators (SITL/HITL).

### DJI Tello MCP

| Server | Language | Notes |
|--------|----------|-------|
| [0xKoda/drone-mcp](https://github.com/0xKoda/drone-mcp) | — | DJI Tello, consumer drone |

A simpler MCP server for the **DJI Tello** educational drone:
- **Basic Flight** — takeoff, land, move, rotate
- **Real-time Control** — SSE-based communication
- **Consumer Friendly** — designed for the $100 Tello drone, popular in education

Good for getting started with drone MCP development, but limited to the Tello platform and basic flight commands compared to MAVLinkMCP's universal protocol support.

## Satellite Tracking

### N2YO MCP

| Server | Language | License | Notes |
|--------|----------|---------|-------|
| [MaxwellCalkin/N2YO-MCP](https://github.com/MaxwellCalkin/N2YO-MCP) | — | MIT | N2YO space catalog |

A satellite tracking MCP server integrating with the N2YO.com API for comprehensive space object monitoring:

- **TLE Data Access** — Two-Line Element sets by NORAD ID for orbit determination
- **Real-time Positioning** — current satellite latitude, longitude, altitude
- **Pass Predictions** — when satellites will be visible from a given observer location
- **Radio Pass Optimization** — optimized passes for amateur radio operators
- **Space Debris Tracking** — collision avoidance monitoring
- **Category Search** — filter by military, weather, GPS, amateur, Starlink, space stations
- **Country Filtering** — find satellites by launching country
- **Natural Language Queries** — the `query_satellites_natural` tool parses countries and cities
- **Trajectory Visualization** — orbital path rendering for planning

Particularly useful for amateur radio operators, space enthusiasts, and satellite collision avoidance research.

## Earth Observation

### Axion Planetary MCP V2.0

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [Dhenenjay/axion-planetary-mcp](https://github.com/Dhenenjay/axion-planetary-mcp) | 218 | TypeScript | Google Earth Engine, AWS |

Billed as the **"world's first Virtual Satellite"** you can connect via MCP, Axion provides enterprise-grade earth observation analysis. **V2.0 completely rebuilt on AWS infrastructure** for better performance, reliability, and global accessibility. Now at 935 commits and 7,458 npm downloads/month:

- **Satellite Imagery Filtering** — search by date, location, and collection (Sentinel-2, Landsat, MODIS)
- **Vegetation Indices** — NDVI (Normalized Difference Vegetation Index) and NDWI (Normalized Difference Water Index) calculations
- **Crop Classification** — agricultural monitoring and analysis
- **Wildfire Risk Assessment** — environmental monitoring
- **Map Visualization** — interactive map generation with satellite overlays
- **Image Statistics** — region-based calculations for selected areas
- **Cloud Storage Export** — export processed imagery to cloud storage
- **SAR-to-Optical AI** (NEW) — exclusive proprietary "Axion Foundation Model" that converts SAR radar imagery to optical-like images for **cloud-free Earth observation** — available only through the hosted server

The highest-starred server in this review at 218 stars (+15% from March). Hosted on Render at `axion-mcp-sse.onrender.com`. Also available as [Axion-MCP](https://github.com/Dhenenjay/Axion-MCP) for a more focused integration.

### Commercial Satellite Imagery (NEW)

| Server | Platform | Notes |
|--------|----------|-------|
| SkyFi MCP | SkyFi | 150+ satellites, 12+ providers, commercial imagery ordering |
| [isaaccorley/planetary-computer-mcp](https://github.com/isaaccorley/planetary-computer-mcp) | Microsoft | 3 stars, 27 commits, STAC data access |

**SkyFi MCP** brings commercial satellite imagery ordering to the MCP ecosystem for the first time. Search, price, order, and monitor satellite imagery from 150+ satellites across 12+ providers including Planet, ICEYE, Umbra, and Satellogic. Features natural language date parsing, cost controls with spending limits, order management, multi-location search, satellite tasking, and area monitoring with webhooks. Available on PulseMCP (488 visitors, released March 2026). Multiple implementations exist from different developers.

**Planetary Computer MCP** provides unified access to Microsoft's Planetary Computer STAC (SpatioTemporal Asset Catalog) API — satellite and geospatial data through natural language queries. Handles raster (GeoTIFF), vector (GeoParquet), and Zarr formats with automatic visualization and natural language geocoding. Licensed Apache 2.0.

### GIS & Spatial Analysis

| Server | Language | Notes |
|--------|----------|-------|
| [matbel91765/gis-mcp-server](https://github.com/matbel91765/gis-mcp-server) | — | Geocoding, routing, spatial analysis |
| [mahdin75/gis-mcp](https://github.com/mahdin75/gis-mcp) | — | GIS operations via GIS libraries |
| [NodeGIS/geo-mcp-server](https://github.com/nodegis/geo-mcp-server) | — | Coordinate conversion, distance, area |

**matbel91765/gis-mcp-server** is the most feature-rich, offering geocoding, batch geocoding, elevation data, routing, spatial analysis, file I/O, and CRS (Coordinate Reference System) transformation.

**mahdin75/gis-mcp** focuses on connecting LLMs to GIS operations using standard geospatial libraries — geometry operations, coordinate transformations, measurements, and spatial validation.

**NodeGIS/geo-mcp-server** provides focused tools for coordinate system conversion, distance calculation, and area measurement.

These complement the earth observation servers by providing ground-level geospatial analysis — useful for combining satellite imagery with local geographic data.

## Defense & Military

### The Missing Category

As of March 2026, **no dedicated defense MCP servers exist in the public ecosystem**. This is the most notable gap:

- **No defense contractors** — Lockheed Martin, Boeing Defense, Northrop Grumman, Raytheon, General Dynamics, and BAE Systems have no public MCP servers
- **No radar or electronic warfare** tools
- **No command and control (C2)** systems integration
- **No missile defense** or weapons systems modeling
- **No military logistics** or force deployment planning
- **No classified/controlled data access** — unsurprising given security requirements
- **No NATO or military standard** protocol bridges (STANAG, MIL-STD)

This absence is understandable: defense systems operate in classified environments with strict access controls, and the MCP protocol's open nature doesn't align with military security requirements. However, some adjacent tools serve dual-use purposes:

- **Cybersecurity MCP servers** (covered in our [Code Security review](/reviews/code-security-mcp-servers/)) — offensive and defensive security tooling
- **STK MCP** (above) — used by defense agencies for mission engineering
- **Satellite tracking** — space domain awareness has both civilian and military applications
- **MAVLink MCP** — the same protocol used for both commercial and military drones

## What's missing

Beyond the defense gap, several aerospace areas lack MCP coverage. Note that several gaps flagged in March 2026 have now been filled:

- ~~No official NASA MCP servers~~ — **FILLED:** nasa/earthdata-mcp is now the first official NASA MCP server
- ~~No FlightRadar24~~ — **FILLED:** Flightradar24 shipped an official MCP server with 15 tools
- ~~No OpenSky Network~~ — **PARTIALLY FILLED:** an OpenSky Network MCP server now exists for ADS-B data
- **No ESA or JAXA official MCP servers** — still community-built only for non-NASA agencies
- **No FlightAware** — the other major flight tracking platform still has no MCP server
- **No ADS-B Exchange** MCP server (OpenSky is available, but ADSBX is not)
- **No air traffic control** simulation or data
- **No GNSS/GPS** precision tools or RTK correction services
- **No CFD (Computational Fluid Dynamics)** integration (OpenFOAM, ANSYS Fluent)
- **No FEA (Finite Element Analysis)** tools beyond MATLAB
- **No spacecraft bus design** or mission lifecycle management
- **No launch vehicle operations** — no SpaceX, Rocket Lab, or ULA integration
- **No space weather forecasting** beyond NASA DONKI's historical data
- **No aircraft maintenance** (EASA/FAA Part 145) or airworthiness management
- **No UAS traffic management (UTM)** for drone operations in controlled airspace
- **No propulsion simulation** or engine performance modeling
- **No materials science** databases for aerospace-grade materials (MMPDS, CMH-17)

## The bottom line

Aerospace and defense MCP servers hold at **3.5 out of 5**. The rating reflects significant progress since March 2026 — NASA publishing its first official MCP server, Flightradar24 entering with 15 tools, Axion's V2.0 AWS rebuild with SAR-to-optical AI, and commercial satellite imagery arriving via SkyFi — but the complete absence of defense applications, the still-thin drone ecosystem, and missing coverage in key areas (ESA/JAXA official servers, FlightAware, ATC, propulsion, materials science) prevent an upgrade. The gap between the civilian aerospace side (actively growing) and the defense side (completely empty) remains the defining characteristic of this category.

**Best for space science:** nasa/earthdata-mcp (official) for Earth science data discovery, ProgramComputer/NASA-MCP-server for broad NASA API access, IO-Aerospace for orbital calculations, STK MCP for mission engineering, astro_mcp for astronomical surveys

**Best for aviation:** Flightradar24 official for live and historical flight data, cheesejaguar/aerospace-mcp for comprehensive flight planning, blevinstein/aviation-mcp for FAA weather data

**Best for drones:** MAVLinkMCP for serious drone development, drone-mcp for educational Tello projects

**Best for earth observation:** Axion V2.0 for Google Earth Engine + SAR-to-optical AI, SkyFi MCP for commercial satellite imagery ordering, Planetary Computer MCP for Microsoft STAC data

The category will likely grow significantly as space becomes more commercialized and as drone delivery and urban air mobility create demand for AI-integrated aerospace operations. The pace of official vendor entry (NASA, Flightradar24) suggests more aviation and space platforms will follow.

*This review was last edited on 2026-04-22 using Claude Opus 4.6 (Anthropic).*
