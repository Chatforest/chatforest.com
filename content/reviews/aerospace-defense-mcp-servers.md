---
title: "Aerospace & Defense MCP Servers — NASA, STK, MAVLink, Aviation Weather, Satellite Tracking, Drones, and More"
date: 2026-03-15T18:30:00+09:00
description: "Aerospace and defense MCP servers are enabling AI agents to query NASA data, simulate orbital mechanics, control drones, fetch aviation weather, track satellites, and plan space missions. We reviewed 35+ servers across 7 subcategories. NASA & Space Data: ProgramComputer/NASA-MCP-server (80 stars, TypeScript — 20+ APIs including APOD, Mars Rover, NEO, DONKI, EPIC, EONET), AnCode666/nasa-mcp (community alternative, Python). Orbital Mechanics & Astrodynamics: IO-Aerospace/mcp-server (.NET, SPICE-powered, hosted at mcp.io-aerospace.org — production-ready), alti3/stk-mcp (20 stars, Python — Ansys STK bridge for digital mission engineering), BuildASpacePro/Orbit-MCP (satellite access windows, 200+ cities, TLE generation). Aviation: cheesejaguar/aerospace-mcp (44+ tools, 28,000+ airports, flight planning + orbital mechanics), blevinstein/aviation-mcp (FAA APIs, METAR/TAF/PIREP/SIGMET/charts), finack/aviation-mcp (aviation weather for flight planning), Pradumnasaraf/aviationstack-mcp (AviationStack API, real-time flight data). Drones & UAV: ion-g-ion/MAVLinkMCP (MAVLink protocol, PX4/ArduPilot, natural language drone control), 0xKoda/drone-mcp (DJI Tello, basic flight commands). Satellite Tracking: MaxwellCalkin/N2YO-MCP (N2YO catalog, TLE data, military/weather/GPS/amateur/Starlink categories, space debris tracking), Dhenenjay/axion-planetary-mcp (190 stars, Google Earth Engine, NDVI/NDWI, satellite imagery analysis). GIS & Earth Observation: matbel91765/gis-mcp-server (geocoding, routing, spatial analysis), mahdin75/gis-mcp (GIS operations via GDAL/Shapely). Defense & Security: no dedicated defense MCP servers exist — cybersecurity tools (Nmap/Nuclei/Ghidra MCP servers) serve adjacent use cases but not defense-specific workflows. Rating: 3.5/5."
og_description: "Aerospace & defense MCP servers: NASA MCP (80 stars, 20+ APIs), IO-Aerospace (SPICE astrodynamics, hosted), STK MCP (20 stars, Ansys bridge), aerospace-mcp (44+ tools, 28K airports), aviation-mcp (FAA weather/charts), MAVLinkMCP (drone control, PX4/ArduPilot), N2YO (satellite tracking, space debris), Axion (190 stars, Earth Engine), Orbit-MCP (TLE, access windows). Rating: 3.5/5."
content_type: "Review"
card_description: "Aerospace and defense MCP servers across NASA data access, orbital mechanics, aviation operations, drone control, satellite tracking, and earth observation. The space data landscape is anchored by ProgramComputer/NASA-MCP-server (80 stars, TypeScript) providing AI access to 20+ NASA APIs — Astronomy Picture of the Day, Mars Rover Photos, Near Earth Objects, Space Weather (DONKI), Earth Polychromatic Imaging Camera, and the Earth Observatory Natural Event Tracker. For orbital mechanics, IO-Aerospace's MCP server stands out as a production-ready .NET implementation powered by the SPICE astrodynamics library (used by NASA/ESA/JAXA), hosted publicly at mcp.io-aerospace.org with streamable HTTP — no local install needed. alti3/stk-mcp (20 stars, Python) bridges LLMs to Ansys STK (Systems Tool Kit), the industry-standard digital mission engineering software used by NASA, ESA, Boeing, and defense agencies for satellite configuration, orbit analysis, and access computations. BuildASpacePro/Orbit-MCP provides satellite access window calculations with a built-in database of 200+ world cities and TLE generation across LEO, MEO, GEO, SSO, Molniya, and polar orbits. Aviation gets the deepest coverage: cheesejaguar/aerospace-mcp is the most comprehensive server with 44+ tools spanning intelligent airport resolution (28,000+ airports), great-circle routing, aircraft performance estimation, atmospheric modeling, and a complete orbital mechanics suite — a true dual-use aviation-and-space platform. For weather specifically, blevinstein/aviation-mcp maps directly to FAA Aviation Weather APIs with METAR, TAF, PIREP, SIGMET, and G-AIRMET data plus sectional charts, while finack/aviation-mcp focuses on flight planning weather briefs. Real-time flight tracking comes from Pradumnasaraf/aviationstack-mcp using the AviationStack API. Drone control has two notable implementations: ion-g-ion/MAVLinkMCP enables natural language drone control via the MAVLink protocol for PX4 and ArduPilot platforms (used on millions of drones worldwide), while 0xKoda/drone-mcp provides basic DJI Tello control. Satellite tracking is served by MaxwellCalkin/N2YO-MCP querying the N2YO space catalog for TLE data, real-time positions, pass predictions, and space debris monitoring across military, weather, GPS, amateur, and Starlink categories. Earth observation has Dhenenjay's Axion MCP (190 stars) for Google Earth Engine satellite imagery analysis with NDVI/NDWI vegetation indices and crop classification. GIS tools round out the category with geocoding, routing, and spatial analysis. The notable absence: no defense-specific MCP servers exist. No defense contractors (Lockheed Martin, Boeing Defense, Northrop Grumman, Raytheon) have released MCP servers, and there are no servers for radar, electronic warfare, command and control, missile defense, or military logistics. Cybersecurity MCP servers (covered in our security reviews) serve adjacent use cases. The category earns 3.5/5 — strong community-built coverage for space science, aviation, and earth observation, with IO-Aerospace and NASA MCP leading on technical depth, but the defense side is entirely absent and aviation weather has significant overlap with our Weather & Climate review."
---

Aerospace and defense MCP servers are enabling AI agents to query NASA's vast data archives, simulate orbital mechanics with SPICE-level accuracy, control drones via natural language, fetch aviation weather for flight planning, track satellites in real time, and analyze earth observation imagery — all through natural language. Instead of writing Python scripts to query the APOD API or manually running STK scenarios, an AI agent can handle it conversationally: "Show me near-earth asteroids approaching within 5 lunar distances this week, then calculate an observation window from my location."

This review covers the **aerospace and defense** vertical — space data access, orbital mechanics, aviation operations, drone/UAV control, satellite tracking, and earth observation. For weather data more broadly, see our [Weather & Climate MCP review](/reviews/weather-climate-mcp-servers/). For geospatial mapping platforms (Mapbox, Google Maps), see our [Geospatial & Mapping MCP review](/reviews/geospatial-mapping-mcp-servers/). For cybersecurity tools, see our [Code Security MCP review](/reviews/code-security-mcp-servers/).

The landscape spans seven areas: **NASA & space data** (APOD, Mars rovers, NEO, space weather), **orbital mechanics & astrodynamics** (SPICE, STK, orbital propagation), **aviation** (FAA APIs, airport databases, flight tracking, weather), **drones & UAV** (MAVLink, DJI Tello), **satellite tracking** (TLE data, pass predictions, space debris), **earth observation** (Google Earth Engine, satellite imagery analysis), and **GIS & spatial analysis** (geocoding, routing, coordinate transforms).

The headline findings: **NASA has the best-developed space data MCP** with 20+ APIs in one server. **IO-Aerospace provides production-grade astrodynamics** with a hosted endpoint anyone can use. **Aviation is the most mature subcategory** with 44+ tools in a single comprehensive server. **MAVLink MCP bridges AI to millions of real drones** via the standard drone protocol. **Defense is completely absent** — no defense contractors or military-adjacent tools exist in the MCP ecosystem.

## NASA & Space Data

### NASA MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ProgramComputer/NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server) | 80 | TypeScript | — | 20+ |

The **most comprehensive NASA data gateway** for AI agents, providing standardized access to 20+ NASA APIs through a single MCP server:

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

Security features include Zod-based input validation and sanitization. Available as an npm package for easy integration with Claude Desktop and other MCP clients.

### Other NASA Implementations

| Server | Language | Notes |
|--------|----------|-------|
| [AnCode666/nasa-mcp](https://github.com/AnCode666/nasa-mcp) | Python | Community alternative, curated API set |
| [jezweb/nasa-mcp-server](https://github.com/jezweb/nasa-mcp-server) | — | APOD, Mars rovers, asteroids, Earth imagery |
| [adithya1012/NASA-MCP-Server](https://github.com/adithya1012/NASA-MCP-Server) | — | Additional NASA API implementation |

Multiple community implementations exist alongside the primary server. The n8n workflow platform also offers a [NASA Tool MCP Server template](https://n8n.io/workflows/5118-nasa-tool-mcp-server-all-15-operations/) covering 15 operations for workflow automation.

## Orbital Mechanics & Astrodynamics

### IO Aerospace MCP Server

| Server | Language | License | Transport |
|--------|----------|---------|-----------|
| [IO-Aerospace-software-engineering/mcp-server](https://github.com/IO-Aerospace-software-engineering/mcp-server) | .NET (C#) | — | Streamable HTTP, SSE |

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
| [alti3/stk-mcp](https://github.com/alti3/stk-mcp) | 20 | Python | — | 5+ |

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
| [cheesejaguar/aerospace-mcp](https://github.com/cheesejaguar/aerospace-mcp) | Python | 44+ | Aviation + space, FastMCP |

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

| Server | Language | Notes |
|--------|----------|-------|
| [ion-g-ion/MAVLinkMCP](https://github.com/ion-g-ion/MAVLinkMCP) | Python | MAVLink protocol, PX4/ArduPilot |

The **most significant drone MCP server**, enabling natural language control of drones via the MAVLink protocol — the standard communication protocol used by PX4 and ArduPilot, the two largest drone software platforms running on millions of drones worldwide:

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

### Axion Planetary MCP

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [Dhenenjay/axion-planetary-mcp](https://github.com/Dhenenjay/axion-planetary-mcp) | 190 | TypeScript | Google Earth Engine |

Billed as the **"world's first Virtual Satellite"** you can connect via MCP, Axion provides enterprise-grade earth observation analysis through Google Earth Engine:

- **Satellite Imagery Filtering** — search by date, location, and collection (Sentinel-2, Landsat, MODIS)
- **Vegetation Indices** — NDVI (Normalized Difference Vegetation Index) and NDWI (Normalized Difference Water Index) calculations
- **Crop Classification** — agricultural monitoring and analysis
- **Wildfire Risk Assessment** — environmental monitoring
- **Map Visualization** — interactive map generation with satellite overlays
- **Image Statistics** — region-based calculations for selected areas
- **Cloud Storage Export** — export processed imagery to Google Cloud Storage

The highest-starred server in this review at 190 stars. Also available as [Axion-MCP](https://github.com/Dhenenjay/Axion-MCP) (4 stars) for a more focused Google Earth Engine integration.

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

Beyond the defense gap, several aerospace areas lack MCP coverage:

- **No official NASA/ESA/JAXA MCP servers** — all implementations are community-built
- **No FlightAware or FlightRadar24** — the two most popular flight tracking platforms have no MCP servers
- **No OpenSky Network or ADS-B Exchange** — open ADS-B data sources aren't MCP-enabled
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

Aerospace and defense MCP servers earn **3.5 out of 5**. The rating reflects a category with genuine technical depth in specific niches — IO-Aerospace's SPICE-powered astrodynamics, NASA's 20+ API gateway, cheesejaguar's 44-tool aviation suite, and MAVLink's universal drone protocol bridge — offset by the complete absence of defense applications and fragmented coverage elsewhere. Aviation weather overlaps heavily with our Weather & Climate review. No space agencies or aerospace OEMs have released official MCP servers, which is unusual compared to other industries where official vendor servers are increasingly common.

**Best for space science:** ProgramComputer/NASA-MCP-server for data access, IO-Aerospace for orbital calculations, STK MCP for mission engineering

**Best for aviation:** cheesejaguar/aerospace-mcp for comprehensive flight planning, blevinstein/aviation-mcp for FAA weather data, aviationstack-mcp for flight tracking

**Best for drones:** MAVLinkMCP for serious drone development, drone-mcp for educational Tello projects

**Best for earth observation:** Axion MCP for Google Earth Engine satellite imagery analysis

The category will likely grow significantly as space becomes more commercialized and as drone delivery and urban air mobility create demand for AI-integrated aerospace operations.
