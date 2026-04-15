---
title: "MCP and Mining: How AI Agents Connect to Geological Modeling, Mine Planning, Resource Estimation, Environmental Monitoring, Oil & Gas, and Commodity Trading Tools"
date: 2026-03-29T21:00:00+09:00
description: "A comprehensive guide to 100+ MCP integrations for mining and natural resources — covering geospatial/GIS tools (QGIS 901 stars, ArcGIS, GDAL 64 stars), geological survey data"
content_type: "Guide"
card_description: "Mining operations generate massive datasets across geological modeling, drill-hole databases, fleet telemetry, environmental sensors, and commodity markets — yet most of this data lives in disconnected systems. This guide covers 100+ MCP servers relevant to the mining and natural resources sector, from GIS platforms and geological databases to critical minerals data, satellite imagery, industrial IoT, oil & gas pricing, and environmental compliance — plus architecture patterns for AI-powered exploration, autonomous operations, and ESG reporting."
last_refreshed: 2026-04-15
---

Mining is one of the most data-intensive industries on earth. A single mine generates terabytes of geological survey data, drill-hole logs, grade control models, fleet telemetry, environmental sensor readings, commodity price feeds, and regulatory compliance reports — each stored in specialized software that rarely talks to the others. The global AI-in-mining market reached approximately $35.47 billion in 2025, growing at 41.92% annually toward a projected $828.33 billion by 2034. Asia-Pacific leads with a 40% market share, driven by China's smart coal mine investments and Australia's autonomous extraction leadership, while North America is the fastest-growing region as critical mineral demand surges.

MCP — the Model Context Protocol — provides a standardized way for AI agents to connect to mining's fragmented data ecosystem. Rather than building custom integrations for each geological database, fleet management system, or environmental sensor network, MCP-connected agents can query spatial data, analyze drill-hole results, monitor equipment telemetry, track commodity prices, and generate compliance reports through defined tool interfaces. The protocol transforms AI assistants from isolated chatbots into operational mining intelligence tools that work across the entire mine lifecycle — from exploration and resource estimation through extraction, processing, and environmental remediation. For an introduction to MCP itself, see our [introduction to MCP](/guides/what-is-mcp/).

The mining MCP ecosystem is maturing. As of April 2026, Seequent — the company behind Leapfrog Geo and Oasis montaj — has released the first MCP server from a major mining software vendor (Evo MCP, early development). Other mining software vendors (Deswik, Maptek, Hexagon, Datamine) have not yet released dedicated MCP servers, but the adjacent tooling — geospatial analysis (including Microsoft's Earth Copilot with 130+ satellite collections), industrial IoT, environmental monitoring, commodity pricing, and scientific databases — is increasingly rich, and these components can be assembled into powerful mining AI workflows.

This guide is research-based. We survey what MCP servers exist across the mining and natural resources landscape, analyze the architecture patterns they enable, and identify where significant gaps remain. We do not claim to have tested or used any of these servers hands-on — our analysis draws on published documentation, open-source repositories, vendor announcements, and industry research. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI. For background on MCP, see our [introduction to MCP](/guides/what-is-mcp/) and the [MCP server directory](/reviews/).

## Why Mining Needs MCP

Mining workflows present integration challenges that MCP is architecturally well-suited to address.

**Geological data is inherently spatial and multi-dimensional.** Drill-hole databases, block models, geological surfaces, and grade estimates all live in specialized formats (CSV, OMF, GOCAD, Vulcan block models) across different software platforms. An MCP-connected AI agent that can read across GIS platforms, geological databases, and spatial analysis tools could automate the tedious process of correlating data across these systems.

**Mine operations generate continuous telemetry.** Autonomous haul trucks, conveyors, crushers, processing plants, and environmental sensors produce real-time data streams. SCADA systems and IoT platforms capture this data but rarely expose it in formats accessible to AI agents. MCP servers bridging industrial IoT platforms let AI agents monitor operations, detect anomalies, and recommend optimizations.

**Commodity markets drive every mining decision.** Whether to develop a deposit, expand production, or shut down operations depends on metal and energy prices that fluctuate continuously. AI agents with MCP access to commodity price feeds can integrate market intelligence into operational decisions — adjusting cut-off grades, blending strategies, or production schedules based on real-time prices.

**Environmental compliance is non-negotiable and growing.** The global ESG compliance market for mining reached $4.53 billion in 2024, growing at 8.9% CAGR to $9.55 billion by 2033. IFRS S1/S2 mandatory climate disclosures started in 2025, CSRD is live in the EU, and GRI 14: Mining Sector 2024 takes effect globally from 2026. AI agents that can pull environmental monitoring data, generate compliance reports, and track regulatory requirements across jurisdictions could transform how mines manage their ESG obligations.

**Autonomous operations are already reality.** Rio Tinto's AutoHaul runs the world's first fully autonomous long-distance heavy-haul rail network across 1,700 kilometers of track. BHP and Rio Tinto have expanded fleets of AI-driven autonomous haul trucks using LiDAR-based path planning. Digital twins like Anglo American's Quellaveco mine in Peru optimize water usage and predict operational bottlenecks. MCP provides the integration layer these autonomous systems need to coordinate with planning, scheduling, and compliance workflows.

## Geospatial and GIS MCP Servers

Geospatial analysis is the foundation of mining — from satellite-based exploration to pit design and environmental monitoring. The GIS MCP ecosystem is the most mature category relevant to mining.

### QGIS MCP Server — Leading Open Source GIS

**jjsantos01/qgis_mcp** | 901 stars | Connects Claude to QGIS Desktop

According to repository documentation, this server connects QGIS Desktop to AI through MCP, allowing agents to create and manage GIS projects, load and manipulate vector and raster layers, execute processing algorithms from the QGIS Processing Toolbox, and run arbitrary Python code within the QGIS environment. For mining applications, this means AI agents could automate geological mapping workflows, overlay drill-hole data on topographic surfaces, calculate volumes for pit design, and run spatial analysis on environmental monitoring data — all through natural language commands.

### GIS MCP Server — Programmatic Spatial Operations

**mahdin75/gis-mcp** | 134 stars | GIS operations via Python libraries

Now at v0.14.0 Beta with support for PySAL spatial analytics alongside Shapely, PyProj, GeoPandas, and Rasterio. Exposes comprehensive geometry operations (intersection, union, buffer, difference), advanced coordinate transformations between reference systems, accurate distance/area/length measurements, and spatial analysis including validation, proximity checks, and spatial overlays. Supports both HTTP and stdio transport modes with Docker deployment. Mining applications include automated boundary calculations, lease area analysis, and spatial correlation of geological and environmental datasets.

### ArcGIS Pro MCP Integration

**nicogis/MCP-Server-ArcGIS-Pro-AddIn** | 25 stars | ArcGIS Pro as MCP tools

Integrates ArcGIS Pro functionality as MCP tools, allowing AI agents to interact with Esri's enterprise GIS environment. For mining companies that standardize on ArcGIS (common in large operations), this provides a bridge between AI workflows and their existing spatial data infrastructure — mine plans, environmental boundaries, tenement data, and geological maps stored in ArcGIS geodatabases.

### GIS Data Conversion MCP

**ronantakizawa/gis-dataconversion-mcp** | 15 stars | 1,000+ downloads | Format conversion

Converts between GIS file formats, coordinate systems, and spatial references. Mining data flows between many formats — shapefiles from surveyors, GeoJSON from web platforms, KML from GPS units, GeoTIFF from satellite imagery. This server automates the format wrangling that consumes significant time in mining data workflows.

### PostGIS MCP Server

**receptopalak/postgis-mcp** | 12 stars | Spatial database queries

Provides direct PostgreSQL database integration with PostGIS spatial extension support. Mining companies using PostGIS for spatial data warehousing can expose their geological databases, tenement boundaries, drill-hole locations, and environmental monitoring stations to AI agents for SQL-based spatial queries.

### GIS-MCP-Server — Multi-Capability

**matbel91765/GIS-MCP-Server** | Community | Geocoding, routing, spatial analysis

A geospatial tools server for AI agents providing geocoding, routing, spatial analysis, and file operations. Useful for logistics-heavy mining operations that need to optimize haul routes, plan infrastructure access, and analyze spatial relationships between mining tenements and environmental features.

### GDAL MCP Server — Geospatial Data Processing

**JordanGunn/gdal-mcp** | 64 stars | GDAL-style geospatial workflows

Now at v1.1.3, this server provides GDAL-style geospatial workflows via Rasterio, GeoPandas, and PyProj, including catalog discovery, raster and vector processing, and format conversion. Features an "epistemic reasoning" reflection middleware that requires AI agents to justify their methodological choices before executing operations — a useful guardrail for mining applications where incorrect coordinate transformations or raster processing can propagate costly errors. For mining, AI agents can process elevation models (DEMs) for pit design, convert between coordinate systems used in different mining jurisdictions, and process satellite-derived raster data for geological interpretation.

### Google Earth Engine MCP

**Dhenenjay/Axion-MCP** | 4 stars | Google Earth Engine geospatial analysis

Provides access to Google Earth Engine's planetary-scale geospatial analysis platform. For mining, GEE offers decades of satellite imagery for change detection, vegetation monitoring, and environmental baseline studies — capabilities particularly valuable for exploration-stage projects and environmental compliance monitoring across large tenement areas.

### Satellite Imagery MCP Servers

**microsoft/Earth-Copilot** | 149 stars | **Official by Microsoft** | AI-powered geospatial analysis

Microsoft's Earth Copilot exposes an MCP server for AI-powered satellite imagery search and GEOINT analysis. According to repository documentation, it provides access to 130+ satellite data collections through Microsoft Planetary Computer and NASA VEDA, with extensible analysis modules for terrain, timeseries comparison, building damage assessment, extreme weather, and mobility analysis. For mining, this is a significant capability — AI agents can search decades of satellite imagery for mineral exploration signatures, monitor pit progression, assess environmental baselines, and detect land-use changes across large tenement areas, all through natural language queries in Claude Desktop, VS Code, or other MCP-compatible tools.

**PSkinnerTech/SkyFi-MCP-server** | 3 stars | SkyFi satellite imagery platform

Enables ordering satellite imagery, searching archives, and tasking new captures through the SkyFi platform. For mining, on-demand high-resolution imagery supports pit progression monitoring, tailings dam surveillance, and environmental impact assessment.

**isaaccorley/planetary-computer-mcp** | 2 stars | Microsoft Planetary Computer STAC API

Query and download satellite imagery from Microsoft's Planetary Computer STAC catalog, which includes Sentinel-2, Landsat, and numerous other Earth observation datasets. The STAC (SpatioTemporal Asset Catalog) standard is increasingly used in mining for organizing and accessing remote sensing data.

## Geological and Earth Science Data

Mining depends on geological data — from regional surveys that identify exploration targets to detailed drill-hole databases that define ore bodies.

### Macrostrat MCP Server — Geological Data

**blake365/macrostrat-mcp** | 6 stars | Macrostrat geological database API

Provides access to the Macrostrat API for querying geological data including stratigraphic columns, lithological descriptions, and geological map data. Macrostrat covers geological information across North America and globally, making it valuable for regional geological context during exploration — understanding the broader geological setting, stratigraphic relationships, and lithological patterns surrounding a mining tenement.

### USGS Earthquake and Volcano Data

**blake365/usgs-quakes-mcp** | ~5 stars | USGS Earthquake API

Query USGS earthquake data with natural language. Seismic data is directly relevant to mining — both for assessing geotechnical risk at mine sites and for monitoring induced seismicity from underground mining or hydraulic fracturing operations.

**blake365/volcanoes-mcp** | Community | Smithsonian Global Volcanism Program

Access volcanic activity data from the Smithsonian's Global Volcanism Program. Relevant for mining operations near volcanic regions — common in Pacific Rim mineral provinces — where volcanic hazard assessment is part of mine planning.

### Seequent Evo MCP Server — First Major Mining Vendor MCP

**SeequentEvo/evo-mcp** | 5 stars | **Official by Seequent** | Geoscience data platform

Seequent — the company behind Leapfrog Geo, Oasis montaj, and MX Deposit — has released an official MCP server for their Evo cloud-based geoscience data platform. This is the first MCP server from a major mining software vendor, marking a significant milestone for the mining MCP ecosystem.

According to repository documentation, the Evo MCP server provides workspace management (create, summarize, snapshot, duplicate workspaces, copy objects between workspaces), geoscience object creation from CSV files with automated data validation and schema mapping (pointsets, line segments, downhole collections, and downhole intervals), and data import/download/query operations. Tools are organized into admin, data, filesystem, and general categories, with support for both STDIO and Streamable HTTP transport modes.

The server is in early development with limited functionality, but it establishes a bridge between AI tools and Seequent's geoscience data infrastructure. For mining companies using Leapfrog Geo for geological modeling, this means AI agents can begin to interact with geological data stored in Evo — querying block models, managing workspace objects, and automating data preparation workflows. Seequent also announced partnerships with Orica Digital Solutions (connecting drilling data with Leapfrog workflows) and Deswik (improving data flow between geological models and mine planning), suggesting a broader push toward integrated AI-accessible mining data pipelines.

### Geological Survey MCP Servers

Several country-specific geological survey MCP servers have emerged:

**pouliens/MCP---AGS-Boreholes-OGC-API** | Community | British Geological Survey borehole data

Access British Geological Survey (BGS) borehole data through the OGC API standard. BGS maintains one of the world's oldest and most comprehensive geological databases, with borehole records spanning centuries.

**furrytailapps/mcp-sgu** | Community | Swedish Geological Survey (SGU)

Access geological data from Sweden's Geological Survey — relevant for the Nordic mining sector, which includes major iron ore (LKAB), base metal, and rare earth element operations.

**MackinHung/mcp-taiwan-geology** | Community | Taiwan geological hazard data

Geological hazard data for Taiwan, demonstrating the pattern of national geological surveys becoming accessible through MCP.

**pouliens/mcp---bgs-mineral-stats** | Community | BGS mineral production, import, and export data

Provides access to global mineral production, import, and export statistics from the British Geological Survey spanning 1970 to present. Covers 18 minerals including copper, lithium, gold, nickel, and rare earth elements. Built on the BGS Open Government License data via OGC WFS 2.0.0 protocol. For mining, this server enables AI agents to analyze historical production trends, import/export flows, and supply chain patterns for critical minerals — useful for market analysis, feasibility studies, and strategic planning.

### Mining-Specific Data Servers

**Redliana/critical-minerals-data-tools** | Community | Critical minerals data (CLAIMM + BGS)

MCP servers and REST APIs specifically for critical minerals data, connecting to the CLAIMM database and British Geological Survey. Critical minerals (lithium, cobalt, rare earths, nickel) are at the center of the energy transition — this server addresses a specific and growing need for AI-powered analysis of critical mineral supply chains.

**Ryan-Clinton/critical-minerals-dependency-mcp** | Community | Critical minerals dependency analysis

A dedicated MCP server for analyzing critical mineral dependencies — useful for understanding supply chain risks, geopolitical exposure, and sourcing alternatives for strategic minerals.

**KatLabPuss/minemarket-mcp** | Community | Search mining projects via Claude

Search mining projects through Claude, providing market intelligence on active mining projects, development-stage properties, and exploration prospects.

### NASA Earthdata MCP Server — Official

**nasa/earthdata-mcp** | 8 stars | **Official by NASA** | NASA Common Metadata Repository

NASA's official MCP server for searching Earth science data collections through the Common Metadata Repository (CMR). The project is currently transitioning its architecture — deprecating its earlier ingestion and embedding pipelines in favor of direct, real-time CMR API integrations. For mining, this means AI agents can search NASA's extensive Earth science archive for satellite-derived geological data — multispectral imagery for mineral mapping, InSAR data for ground subsidence monitoring, elevation models for site planning, and vegetation indices for environmental baseline studies. NASA's Earthdata archive contains petabytes of freely available data relevant to mineral exploration and environmental monitoring.

### NASA Open APIs MCP Server

**jezweb/nasa-mcp-server** | 8 stars | APOD, Mars rovers, asteroids, Earth imagery

A comprehensive server accessing NASA's open APIs including Earth observation imagery. While primarily designed for general NASA data access, the Earth imagery endpoints provide satellite views useful for mine site monitoring, land-use change detection, and environmental impact assessment.

### USGS Data Resources

The U.S. Geological Survey maintains the National Geochemical Database with data for over 1.5 million rock, sediment, soil, and mineral samples analyzed from 1962 through 2023. Their Mineral Resources Data System (MRDS) covers metallic and nonmetallic mineral deposits worldwide. The USMIN database provides authoritative U.S. mineral deposit data. Their Mineral Resources Online Spatial Data portal provides interactive maps and downloadable data for regional and global geology, geochemistry, geophysics, and mineral resources. While no dedicated USGS MCP server exists yet, USGS maintains data repositories through their GitHub organization (github.com/DOI-USGS) that could serve as foundations for future MCP integrations.

### Open Geoscience Ecosystem

The **softwareunderground/awesome-open-geoscience** repository catalogs open-source tools for geoscientists including geological modeling libraries, well log analysis tools, seismic processing software, and geospatial utilities. Many of these tools expose Python APIs that could be wrapped as MCP servers — libraries like GemPy (3D geological modeling), PyGMT (mapping), Welly (well log analysis), and SimPEG (geophysical simulation) represent untapped potential for MCP integration in mining workflows.

## Oil, Gas, and Commodity Pricing

Real-time commodity prices drive mining economics. The MCP ecosystem has direct coverage for energy commodities and precious metals.

### OilPriceAPI MCP Server

**OilpriceAPI/mcp-server** | 1 star | Real-time oil, gas, and commodity prices

Provides 4 tools for getting real-time prices, market overviews, price comparisons, and commodity listings across 40+ commodities including oil, gas, coal, refined products, metals, and forex. Also includes 4 resources for subscribable price snapshots and 4 pre-built analyst prompt templates. For mining companies, this provides real-time energy cost data (diesel for haul trucks, electricity for processing) and metal price feeds that drive cut-off grade decisions.

### Metal Price MCP Server

**isdaniel/mcp-metal-price** | 1 star | Gold, silver, platinum, palladium

Provides current and historical prices for gold (XAU), silver (XAG), platinum (XPT), and palladium (XPD) via GoldAPI.io. For precious metal mining operations, this enables AI agents to integrate real-time metal prices into grade control decisions, production scheduling, and financial modeling.

### Financial Data Integration

The broader MCP finance ecosystem (covered in our [finance and fintech guide](/guides/mcp-finance-fintech/)) includes servers for Bloomberg-style market data, stock trading, and financial analysis. Mining companies listed on stock exchanges can use these servers to correlate operational data with share price movements, analyst expectations, and peer company performance.

## Industrial IoT, SCADA, and Sensor Networks

Mining operations run on industrial control systems. The IoT MCP ecosystem provides the bridge between sensor networks and AI agents.

### IoT-Edge-MCP-Server — Industrial Grade

**poly-mcp/IoT-Edge-MCP-Server** | 22 stars | MQTT + Modbus + InfluxDB

A production-ready MCP server for industrial IoT, edge computing, and SCADA/PLC systems. According to repository documentation, it provides a unified tool interface over HTTP (FastAPI) integrating MQTT sensors and Modbus devices with InfluxDB time-series storage and Redis caching. Features include real-time monitoring, alarm management, time-series data storage, and actuator control.

For mining, this server could bridge AI agents to: haul truck telemetry (engine temperature, fuel consumption, payload weight), conveyor belt sensors (speed, belt tension, material flow), crusher and mill instrumentation (throughput, power draw, vibration), tailings dam monitoring (piezometers, inclinometers, seepage sensors), ventilation systems in underground mines (gas detectors, airflow sensors), and water treatment plant instrumentation.

### AWS IoT SiteWise MCP Server — Official by AWS

**awslabs/mcp** (aws-iot-sitewise-mcp-server) | Part of 8,800-star AWS MCP collection | **Official**

AWS's official IoT SiteWise MCP server, now at v11.0.11, provides comprehensive industrial IoT asset management including asset creation/management, hierarchies, models, properties, data ingestion, historical retrieval with aggregations, bulk export, gateway management, and SQL-like queries. A standout feature is ML-powered anomaly detection — most IoT MCP servers only read data, but SiteWise actively identifies problems using machine learning. The server includes built-in industrial domain knowledge, automatically applying proper units, data types, and quality indicators. For mining, this means AI agents can model processing plants, conveyor systems, and fleet assets while receiving automated alerts when equipment behavior deviates from normal patterns.

### Litmus MCP Server — Official

**Litmus Edge MCP Server** | **Official by Litmus** | Industrial edge computing

Litmus provides an official MCP server implementation that serves as a bridge between LLMs and industrial systems. Litmus Edge is used in manufacturing and mining for edge data collection from PLCs, SCADA systems, and industrial equipment. The MCP server enables AI agents to access real-time production data from industrial edge nodes.

### General IoT MCP Server

**jordy33/iot_mcp_server** | 2 stars | Smart devices and sensors

A general-purpose MCP server for controlling and monitoring IoT devices including sensors, providing standardized interfaces for device control and state management. While designed for consumer IoT, the architecture patterns apply to mining sensor networks.

## Weather and Environmental Monitoring

Environmental conditions directly impact mining operations — from weather affecting open-pit mining to water quality monitoring required for compliance.

### Weather MCP Server — Comprehensive

**weather-mcp/weather-mcp** | 4 stars | 12 weather tools, global coverage, no API keys

Provides forecasts, current conditions, historical weather data (1940–present), weather alerts, air quality monitoring, marine conditions, lightning detection, weather radar imagery, river monitoring, and wildfire tracking. For mining, this covers operational weather planning (blast timing, dust suppression, flooding risk), historical climate analysis for mine planning, air quality monitoring for compliance, and wildfire risk assessment for remote operations.

### Open-Meteo MCP Servers

Multiple implementations provide weather data through the Open-Meteo API, including historical weather data essential for hydrological modeling in mine design — calculating probable maximum precipitation, designing water management infrastructure, and planning for extreme weather events.

### Air Quality and Chemical Data

**mattmarcin/aqicn-mcp** | ~5 stars | Air quality data from AQICN.org

Provides real-time air quality index data globally. Mining operations face strict air quality regulations — particulate matter from blasting, dust from haul roads, and emissions from processing plants all require continuous monitoring. This server helps contextualize site-specific air quality readings against regional baselines.

**ToxMCP/comptox-mcp** | ~1 star | EPA CompTox chemical and hazard data

Access EPA's CompTox Dashboard for chemical, bioactivity, exposure, and hazard data. Relevant for mining operations handling hazardous chemicals in processing (cyanide in gold extraction, sulfuric acid in copper leaching) and for environmental impact assessment of mine discharge on surrounding ecosystems.

### Regulatory and Maritime Compliance

**apifyforge/maritime-resource-compliance-mcp** | Community | Maritime resource compliance

Covers fishing quotas, oil & gas licenses, waste carriers, and coastal hazards. Relevant for offshore mining operations, seabed mineral exploration, and port-based bulk commodity shipping.

**apifyforge/uk-regulatory-ecosystem-mcp** | Community | UK regulatory intelligence

Access to UK regulatory databases including NSTA (North Sea Transition Authority) oil and gas licensing data. Useful for oil & gas operations in UK waters and onshore mining operations navigating British regulatory frameworks.

## Mining Software Landscape — Where MCP Gaps Exist

The mining industry's specialized software platforms represent the largest gap in the MCP ecosystem. None of the major mining software vendors have released official MCP implementations.

### Mine Planning and Scheduling

| Platform | Vendor | AI Status | MCP Server |
|----------|--------|-----------|------------|
| Deswik.Suite | Sandvik (Deswik) | AI scheduling with AutoMine integration | No MCP server |
| MinePlan | Hexagon Mining | Geotechnical forecasting, slope stability | No MCP server |
| Datamine Studio | Datamine | Block modeling, resource estimation | No MCP server |
| Surpac/GEOVIA | Dassault Systemes | Geological modeling, mine design | No MCP server |
| Vulcan | Maptek | ML-powered grade control | No MCP server |
| Micromine | Micromine | Exploration to production workflow | No MCP server |

### Geological Modeling

| Platform | Vendor | AI Status | MCP Server |
|----------|--------|-----------|------------|
| Leapfrog Geo | Seequent | AI-driven implicit modeling, 30% more accuracy | **Evo MCP (early)** |
| GOCAD/SKUA | Emerson/AspenTech | Geological modeling, reservoir simulation | No MCP server |
| GemPy | Open source | 3D geological modeling in Python | Wrappable as MCP |
| Oasis montaj | Seequent | Geophysical data processing | **Evo MCP (early)** |

### Fleet Management and Autonomous Systems

| Platform | Vendor | AI Status | MCP Server |
|----------|--------|-----------|------------|
| AutoHaul | Rio Tinto | Fully autonomous rail (1,700 km) | No MCP server |
| FrontRunner AHS | Komatsu | Autonomous haul trucks | No MCP server |
| Command for Hauling | Caterpillar | Autonomous trucks | No MCP server |
| MineStar | Caterpillar | Fleet management, terrain guidance | No MCP server |
| Wenco FMS | Hitachi | Fleet management, dispatch optimization | No MCP server |

### Environmental and ESG Platforms

| Platform | Use Case | MCP Server |
|----------|----------|------------|
| Envirosuite | Environmental monitoring, air quality | No MCP server |
| Intelex | EHS/ESG management | No MCP server |
| Enablon (Wolters Kluwer) | Sustainability reporting | No MCP server |
| Benchmark ESG | Mining-specific ESG | No MCP server |

## Architecture Patterns for Mining AI

Despite the vendor gap, existing MCP servers can be assembled into powerful mining AI architectures.

### Pattern 1: AI-Powered Exploration Assistant

```
┌─────────────────────────────────────────────────────┐
│                AI Exploration Agent                   │
│         (Geological Target Identification)            │
├─────────────────────────────────────────────────────┤
│                                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────┐   │
│  │ NASA     │  │ QGIS MCP  │  │ PostGIS MCP      │   │
│  │ Earthdata│  │ (901★)   │  │ (Drill-hole DB)  │   │
│  │ MCP      │  │          │  │                   │   │
│  └────┬─────┘  └────┬─────┘  └────┬──────────────┘   │
│       │              │              │                  │
│  Satellite      Geological     Historical             │
│  imagery &      mapping &      drill-hole             │
│  mineral        spatial        & assay                │
│  signatures     analysis       data                   │
│       │              │              │                  │
│       └──────────────┼──────────────┘                  │
│                      │                                 │
│              ┌───────▼────────┐                        │
│              │ GIS MCP (134★) │                        │
│              │ Spatial overlay │                        │
│              │ & correlation   │                        │
│              └───────┬────────┘                        │
│                      │                                 │
│              ┌───────▼────────┐                        │
│              │ Metal Price MCP │                        │
│              │ Economic filter │                        │
│              └────────────────┘                        │
└─────────────────────────────────────────────────────┘

Agent workflow:
1. Query NASA Earthdata for multispectral satellite imagery
2. Load geological maps and known mineralization in QGIS
3. Pull historical drill-hole data from PostGIS database
4. Run spatial correlation analysis via GIS MCP
5. Filter targets by current metal prices for economic viability
6. Generate ranked exploration target report
```

### Pattern 2: Autonomous Operations Monitor

```
┌─────────────────────────────────────────────────────┐
│              AI Operations Monitor                    │
│         (Real-time Mine Performance)                  │
├─────────────────────────────────────────────────────┤
│                                                       │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────┐  │
│  │ IoT-Edge MCP │  │ AWS IoT      │  │ Weather   │  │
│  │ (22★)        │  │ SiteWise MCP │  │ MCP (4★)  │  │
│  │ MQTT/Modbus  │  │ (Official)   │  │           │  │
│  └──────┬───────┘  └──────┬───────┘  └─────┬─────┘  │
│         │                  │                │         │
│    Equipment           Asset             Weather      │
│    telemetry:          hierarchy:        conditions:   │
│    - Truck GPS         - Plant models    - Wind/rain   │
│    - Crusher loads     - Conveyor KPIs   - Dust risk   │
│    - Pump pressures    - Energy usage    - Flood risk   │
│         │                  │                │         │
│         └──────────────────┼────────────────┘         │
│                            │                          │
│                   ┌────────▼────────┐                 │
│                   │ Anomaly detect  │                 │
│                   │ & alert triage  │                 │
│                   └────────┬────────┘                 │
│                            │                          │
│                   ┌────────▼────────┐                 │
│                   │ Operations      │                 │
│                   │ dashboard &     │                 │
│                   │ shift reports   │                 │
│                   └─────────────────┘                 │
└─────────────────────────────────────────────────────┘

Agent workflow:
1. Poll equipment sensors via IoT-Edge MCP (MQTT/Modbus)
2. Query asset performance from AWS IoT SiteWise
3. Check weather conditions for operational impact
4. Detect anomalies (unusual vibration, temperature spikes, flow drops)
5. Correlate equipment alerts with weather events
6. Generate shift handover reports with key metrics and alerts
```

### Pattern 3: ESG and Environmental Compliance Engine

```
┌─────────────────────────────────────────────────────┐
│            AI Compliance & ESG Agent                  │
│      (Environmental Monitoring & Reporting)           │
├─────────────────────────────────────────────────────┤
│                                                       │
│  ┌──────────────┐  ┌──────────┐  ┌───────────────┐  │
│  │ IoT-Edge MCP │  │ Weather  │  │ QGIS MCP      │  │
│  │ Environmental│  │ MCP      │  │ (901★)        │  │
│  │ sensors      │  │ Air qual │  │ Spatial report │  │
│  └──────┬───────┘  └────┬─────┘  └──────┬────────┘  │
│         │               │                │            │
│    Water quality     Air quality      Spatial          │
│    Dust levels       Historical       boundaries:      │
│    Noise monitors    weather data     - Lease areas    │
│    Seepage sensors   Wind patterns    - Buffer zones   │
│         │               │             - Habitats       │
│         └───────────────┼────────────┘                │
│                         │                             │
│                ┌────────▼────────┐                    │
│                │ Compliance check │                    │
│                │ vs permit limits │                    │
│                └────────┬────────┘                    │
│                         │                             │
│                ┌────────▼────────┐                    │
│                │ Generate IFRS   │                    │
│                │ S2 / GRI 14 /   │                    │
│                │ CSRD reports    │                    │
│                └─────────────────┘                    │
└─────────────────────────────────────────────────────┘

Agent workflow:
1. Collect environmental sensor data (water pH, turbidity, dust PM10)
2. Pull air quality and weather data for dispersion modeling
3. Map monitoring points against lease boundaries and sensitive areas
4. Compare readings against permit conditions and regulatory limits
5. Flag exceedances and generate incident reports
6. Produce ESG disclosures for IFRS S2, GRI 14, and CSRD frameworks
```

### Pattern 4: Commodity-Driven Production Optimizer

```
┌─────────────────────────────────────────────────────┐
│           AI Production Optimizer                     │
│     (Market-Responsive Mining Operations)             │
├─────────────────────────────────────────────────────┤
│                                                       │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────┐  │
│  │ OilPrice MCP │  │ Metal Price  │  │ PostGIS   │  │
│  │ (40+ commod) │  │ MCP (Au/Ag/  │  │ MCP       │  │
│  │              │  │ Pt/Pd)       │  │ (Block    │  │
│  │              │  │              │  │  model DB) │  │
│  └──────┬───────┘  └──────┬───────┘  └─────┬─────┘  │
│         │                  │                │         │
│    Energy costs:       Revenue per      Grade &       │
│    - Diesel            ounce/tonne:     tonnage by    │
│    - Electricity       - Current spot   block:         │
│    - Gas               - Trends         - Au g/t       │
│         │              - Forecasts      - Cu %         │
│         └──────────────────┼────────────┘              │
│                            │                           │
│                   ┌────────▼────────┐                  │
│                   │ Cut-off grade   │                  │
│                   │ optimization    │                  │
│                   └────────┬────────┘                  │
│                            │                           │
│                   ┌────────▼────────┐                  │
│                   │ Production      │                  │
│                   │ schedule &      │                  │
│                   │ blend plan      │                  │
│                   └─────────────────┘                  │
└─────────────────────────────────────────────────────┘

Agent workflow:
1. Fetch current metal prices and energy costs
2. Query block model for available ore by grade and location
3. Calculate break-even cut-off grade based on current economics
4. Optimize extraction sequence for maximum NPV
5. Generate daily blend plan and truck dispatch recommendations
6. Alert when price movements trigger schedule changes
```

## Regulatory and Safety Considerations

Mining AI deployments face unique regulatory requirements that differ significantly from other industries.

**Mining-specific safety regulations.** Most jurisdictions require that safety-critical decisions in mining be made or approved by qualified mining engineers or geotechnical engineers. AI agents should assist with analysis and recommendations but should not autonomously make decisions about blast patterns, ground support, ventilation design, or dam stability without human expert review. MSHA (US), WHS (Australia), and equivalent regulators in other jurisdictions mandate human accountability for safety decisions.

**Resource estimation standards.** JORC (Australasia), NI 43-101 (Canada), SAMREC (South Africa), and CIM (Canada) codes define how mineral resources and reserves must be estimated and reported. AI agents can assist with data analysis and modeling, but a Competent Person (JORC) or Qualified Person (NI 43-101) must sign off on resource estimates. GRI 14: Mining Sector 2024, which takes effect globally from 2026, adds further disclosure requirements around mineral resources and reserves.

**Environmental permit conditions.** Mining permits typically specify exact monitoring parameters, sampling frequencies, reporting formats, and exceedance thresholds. AI agents processing environmental data must be configured to match these precise requirements — a reading that's 0.01 mg/L over a discharge limit can trigger regulatory action, so approximate analysis is insufficient.

**ESG reporting frameworks.** IFRS S1/S2 mandatory climate disclosures (from 2025), CSRD with ESRS reporting (live in EU), and Task Force on Climate-related Financial Disclosures (TCFD) all require specific data collection, analysis, and reporting formats. AI agents can automate data collection and report drafting, but disclosures must be reviewed by qualified personnel and may require limited assurance from auditors.

**Data sovereignty and Indigenous rights.** Mining often occurs on or near Indigenous lands. Cultural heritage data, sacred site locations, and traditional knowledge may be subject to data sovereignty requirements that restrict how information can be stored, processed, and shared. AI agents must be configured to respect these boundaries — some geological or cultural data should never leave specific jurisdictions or systems.

**Autonomous equipment regulations.** While autonomous haul trucks and trains are operational, most jurisdictions require safety management plans, risk assessments, and defined exclusion zones. AI agents coordinating with autonomous equipment must operate within these regulatory frameworks and maintain audit trails of all decisions that affect equipment movement or safety zones.

## Current Ecosystem Gaps

The mining MCP ecosystem has significant gaps, though Seequent's Evo MCP server (see above) marks the first major vendor entry. Many opportunities remain for developers.

**Mine planning software integration.** No MCP servers exist for any major mine planning platform. Deswik, Hexagon MinePlan, Datamine, Maptek Vulcan, and Micromine all have APIs or scripting interfaces that could be exposed through MCP. This is the highest-value gap in the ecosystem — mine planning is where the most consequential decisions are made, and AI assistance could significantly improve scheduling optimization, grade control, and production forecasting. Seequent's announced partnership with Deswik for data flow between geological models and mine planning may eventually bring MCP connectivity to this space.

**Geological modeling tools.** Seequent's Evo MCP server provides early access to workspace and data management features, but does not yet expose Leapfrog Geo's core implicit modeling capabilities (surface generation, block modeling, grade estimation) through MCP. The gap has narrowed — AI agents can now interact with Seequent's geoscience data platform — but direct AI-driven geological modeling via MCP remains out of reach. GemPy (open-source 3D geological modeling in Python) remains the most MCP-ready option for actual modeling operations — its Python API could be wrapped as an MCP server relatively easily.

**Drill-hole database management.** acQuire and Fusion (Seequent) are the primary drill-hole data management systems in mining. Seequent's Evo MCP server provides some access to downhole collections and intervals, but purpose-built drill-hole database MCP servers with support for full assay querying, QAQC workflows, and compositing do not yet exist. These databases are the foundation of mineral exploration and resource estimation — deeper MCP access would enable AI agents to analyze assay results, correlate geological units, and identify exploration targets.

**Fleet management systems.** Caterpillar MineStar, Wenco FMS, Modular Mining DISPATCH, and Hexagon MineOperate all manage haul truck fleets but lack MCP servers. Fleet optimization is a high-value use case where AI agents could improve truck dispatch, reduce fuel consumption, and minimize equipment idle time.

**Tailings dam monitoring.** Given the catastrophic consequences of tailings dam failures (Brumadinho, Samarco, Mount Polley), real-time monitoring of tailings facilities is critical. While IoT MCP servers can bridge sensor data, no mining-specific tailings monitoring MCP server exists that understands piezometer readings, inclinometer data, seepage flow rates, and dam stability calculations.

**Mineral processing and metallurgy.** Concentrator plants, heap leach operations, and smelters generate extensive process data but have no MCP coverage. Digital twin platforms like Metso's Geminex (used at Newmont's Lihir mine) could benefit from MCP interfaces for AI-driven process optimization.

**Mine closure and rehabilitation.** Mine closure planning, progressive rehabilitation, and post-closure monitoring represent a growing regulatory focus but have no dedicated MCP tooling. AI agents could help track rehabilitation progress against closure plans, estimate closure liabilities, and monitor post-closure environmental performance.

## Getting Started by Role

### Exploration Geologist
Start with the **QGIS MCP server** (901 stars) and **NASA Earthdata MCP** for satellite-based mineral mapping. Use **PostGIS MCP** to query drill-hole databases spatially. Add **GIS MCP** for spatial correlation analysis between geological, geochemical, and geophysical datasets.

### Mine Engineer
Focus on **IoT-Edge MCP Server** for equipment telemetry and **AWS IoT SiteWise MCP** for asset monitoring. Use **Weather MCP** for operational weather planning. The gap you'll feel most is the lack of mine planning software MCP servers — for now, consider wrapping your planning tool's Python API as a custom MCP server.

### Environmental Manager
Combine **IoT-Edge MCP** for environmental sensor data with **Weather MCP** for meteorological context and **QGIS MCP** for spatial compliance mapping. Use these to automate monitoring report generation and exceedance alerting. The ESG reporting gap is significant — you'll likely need custom tooling to map sensor data to IFRS S2 and GRI 14 disclosure formats.

### Commodity Analyst
Use **OilPriceAPI MCP** for energy commodities and **Metal Price MCP** for precious metals. Combine with financial MCP servers from the broader ecosystem for market analysis. The gap is in base metals pricing (copper, iron ore, lithium, nickel) — no MCP server yet covers these directly, though OilPriceAPI covers 40+ commodities.

### Mine Manager
You need the full stack: **IoT-Edge MCP** for operations, **Weather MCP** for planning, **commodity price servers** for economics, and **QGIS/PostGIS** for spatial context. Start with the operations monitor pattern — getting real-time equipment and environmental data into AI workflows provides the fastest operational value.

### Mining Software Developer
The biggest opportunity is building MCP servers for mining-specific platforms. Start with whichever platform your organization uses — Deswik, Maptek, Hexagon, or open-source alternatives. Wrap existing APIs or scripting interfaces as MCP tools. Even a read-only MCP server for a block model database would be valuable to the community.

## Related Guides

- [What is MCP?](/guides/what-is-mcp/) — Introduction to the Model Context Protocol
- [MCP Server Directory](/reviews/) — Browse all MCP servers by category
- [Best IoT MCP Servers](/guides/best-iot-mcp-servers/) — Comprehensive IoT server coverage
- [MCP and Energy & Utilities](/guides/mcp-energy-utilities/) — Power, oil, gas, and utility MCP servers
- [MCP and Environmental Monitoring](/guides/mcp-environmental-monitoring/) — Environmental sensor networks and compliance
- [MCP and Supply Chain & Logistics](/guides/mcp-supply-chain-logistics/) — Fleet management and logistics
- [MCP and Agriculture & Farming](/guides/mcp-agriculture-farming/) — Related natural resources sector
- [MCP and GIS/Geospatial](/guides/mcp-geospatial-gis/) — Detailed geospatial server coverage
