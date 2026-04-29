---
title: "Sustainability & Climate MCP Servers — Carbon Emissions, Building Energy, Air Quality, Power Grid Intelligence, ESG Reporting, and More"
date: 2026-03-16T06:00:00+09:00
description: "Sustainability and climate MCP servers let AI agents calculate carbon emissions, simulate building energy performance, monitor air quality, optimize power grid scheduling, report on ESG frameworks, and"
og_description: "Sustainability & climate MCP servers: Google Travel Impact Model OFFICIAL MCP for flight emissions, luminus (68 stars, 69 tools, European/UK grid data), EnergyPlus-MCP (84 stars, 35 tools, DOE building simulation), PowerMCP (115 stars, 4 platforms), open-meteo-mcp (41 stars, v1.6.1), NEW ESG servers (ansvar-systems 12 tools 8 frameworks, GHG calculator 967 factors). 30+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "Sustainability and climate MCP servers for carbon emissions calculation, building energy simulation, air quality monitoring, power grid intelligence, ESG reporting, and climate data access. The category has grown rapidly with major new arrivals filling previous gaps. **Google Travel Impact Model now has an OFFICIAL MCP endpoint** at travelimpactmodel.googleapis.com/mcp — 3 tools for flight emissions (detailed, typical, and Scope 3 reporting) with per-cabin CO2e and contrails impact, making Google the first major tech company with a dedicated sustainability MCP. **kitfunso/luminus is the standout newcomer** — 68 stars, 69 tools across 11 categories providing real-time European and UK electricity grid data from ENTSO-E, National Grid ESO, Elexon BMRS, GIE, and regional operators, covering generation mix, day-ahead pricing, balancing, gas/LNG storage, battery arbitrage, cross-border flows, carbon intensity, and even GIS solar site prospecting. Many tools work without API keys. **LBNL-ETA/EnergyPlus-MCP has grown to 84 stars** — 21 forks, the leading academic sustainability MCP server for DOE building energy simulation. **Power-Agent/PowerMCP SURGED to 115 stars** — 38 forks, now covering 4 power system platforms (PowerWorld, PSSE, OpenDSS, and newly added DIgSILENT PowerFactory) for load flow, fault simulation, and grid optimization. **cmer81/open-meteo-mcp SURGED to 41 stars** — 16 forks, v1.6.1 with new advanced skill (10 tools) and general skill (7 tools) for weather, climate projections, air quality, marine, and flood data, all free. **The ESG gap is closing** — ansvar-systems/esg-sustainability-mcp provides 12 tools covering 309 provisions across 8 frameworks (GRI, IFRS S1/S2, TCFD, TNFD, EU Taxonomy, CSRD/ESRS, SBTi, CSDDD) with a public HTTP endpoint; freminder/esg-mcp-servers adds 31 tools for ESRS metric extraction and EU regulation analysis. **starrybodies/ghg-calculator delivers GHG Protocol implementation** — 8 tools, 967 embedded emission factors from 6 free databases (EPA, eGRID, DEFRA, USEEIO, Ember, EXIOBASE), all 3 scopes including all 15 Scope 3 categories, no paid APIs required. **kayhendriksen/foehn brings Swiss climate data** — 37 stars, MeteoSwiss weather stations, radar, forecasts, and climate series. Category has doubled from 15+ to 30+ servers. Rating upgraded from 3.5 to 4/5 — Google official MCP, luminus with 69 tools for European grid, PowerMCP at 115 stars covering 4 platforms, ESG reporting gap closing, and GHG Protocol implementation all represent major ecosystem maturation. Remaining gaps narrower: no carbon registry MCPs, no LCA tools, no satellite monitoring, no waste management."
last_refreshed: 2026-04-29
---

Sustainability and climate MCP servers are bringing environmental intelligence directly into AI workflows — calculating carbon emissions, simulating building energy performance, monitoring air quality, tracking ESG compliance, and accessing climate projections, all through the Model Context Protocol. Instead of juggling APIs, spreadsheets, and separate calculation tools, these servers let AI assistants handle sustainability-related queries and analysis natively.

This review covers **sustainability and climate MCP servers** — carbon emissions calculators, building energy simulators, power grid intelligence, air quality monitors, ESG reporting tools, climate data providers, and open source climate contribution tools. For weather-focused servers without the sustainability angle, see our [Weather MCP review](/reviews/weather-climate-mcp-servers/) if available. For IoT device monitoring that includes environmental sensors, see our [IoT & Smart Home review](/reviews/smart-home-automation-mcp-servers/).

The headline findings: **Google's Travel Impact Model now has an official MCP endpoint** for flight emissions with Scope 3 reporting. **luminus delivers 69 tools for European/UK electricity grid data** at 68 stars. **EnergyPlus-MCP from Lawrence Berkeley National Lab has grown to 84 stars**. **PowerMCP surged to 115 stars** covering 4 power system platforms. **open-meteo-mcp hit 41 stars** with v1.6.1 and new skill modes. **The ESG gap is closing** with servers covering 8 major frameworks and GHG Protocol with 967 emission factors. Category has doubled from 15+ to **30+ servers**.

**Category:** [Logistics & Industry](/categories/logistics-industry/)

---

## Carbon Emissions Calculation

### Google Travel Impact Model — OFFICIAL Flight Emissions MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Travel Impact Model MCP](https://developers.google.com/travel/impact-model/docs/mcp) | — | Hosted | — | 3 |

**The biggest new arrival — Google's official MCP endpoint for aviation carbon emissions.** Hosted at `travelimpactmodel.googleapis.com/mcp`, this is the same data shown on Google Flights, now available to AI agents:

- **compute_flight_emissions** — detailed emissions for specific upcoming flights
- **compute_typical_flight_emissions** — typical emissions between airport pairs without specific flight details
- **compute_scope3_flight_emissions** — historical flight emissions for Scope 3 corporate reporting

Returns CO2e per passenger broken down by cabin class (Economy, Premium Economy, Business, First) with well-to-wake lifecycle methodology. Also includes contrails impact assessment. Requires a Travel Impact Model API key. Integration guides available for Gemini CLI and other MCP clients.

*This closes a significant gap — Google is the first major tech company with a dedicated sustainability MCP endpoint.*

### jagan-shanmugam/climatiq-mcp-server — Carbon Emissions via Climatiq API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [climatiq-mcp-server](https://github.com/jagan-shanmugam/climatiq-mcp-server) | 8 | Python | MIT | 7+ |

**Wraps the Climatiq API** for broad carbon emissions data — electricity, travel, cloud computing, freight, procurement, and hotel stay emissions with access to 68,000+ emission factors across regions and industries. 9 forks. Requires a Climatiq API key (free tier available). Includes example Jupyter notebooks.

*Note: This repo has been dormant since March 2025 (only 3 commits total). The Climatiq API itself remains active, but the MCP wrapper is unmaintained.*

### starrybodies/ghg-calculator — GHG Protocol with 967 Embedded Factors

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ghg-calculator](https://github.com/starrybodies/ghg-calculator) | 4 | — | — | 8 |

**NEW — Open-source GHG Protocol Corporate Standard implementation** that requires no paid APIs or proprietary databases. 967 embedded emission factors from 6 free, peer-reviewed databases:

- **EPA Hub** (113 factors), **eGRID** (122 factors), **DEFRA** (117 factors), **USEEIO** (264 factors), **Ember** (120 factors), **EXIOBASE** (231 factors)

8 tools: `calculate_emissions`, `calculate_single`, `get_emission_factors`, `list_scopes`, `list_factor_sources`, `generate_report`, `get_gwp_values`, `convert_units`. Covers all three scopes:

- **Scope 1** — direct combustion, fugitive emissions, refrigerants
- **Scope 2** — purchased electricity (location-based and market-based)
- **Scope 3** — all 15 value chain categories

Also available as a CLI tool and Claude Code skill. A strong alternative to Climatiq for teams that want offline-capable carbon calculations without API dependencies.

---

## Building Energy Simulation

### LBNL-ETA/EnergyPlus-MCP — DOE Building Energy Modeling

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP) | 84 | Python | — | 35 |

**The leading academic sustainability MCP server** — developed by Lawrence Berkeley National Laboratory, now at 84 stars and 21 forks. Enables AI-driven interaction with the U.S. Department of Energy's EnergyPlus whole-building energy simulation engine. Published in the SoftwareX journal.

35 tools organized across five categories:

- **Model management** — load, validate, and inspect EnergyPlus IDF files
- **Editing and analysis** — modify building parameters, materials, schedules, and zone configurations
- **HVAC intelligence** — discover and visualize HVAC system topology with interactive diagrams
- **Simulation execution** — run EnergyPlus simulations with weather files automatically
- **Results visualization** — generate interactive plots, energy breakdowns, and performance reports

EnergyPlus can model thermal dynamics, HVAC operations, and environmental interactions, with simulations achieving 20–60% energy savings compared to conventional building codes. Recent updates improved setup documentation and inspector instructions. Requires EnergyPlus 25.1.0; Docker deployment available.

---

## Power Grid & Electricity Markets

### kitfunso/luminus — European & UK Electricity Grid Intelligence

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [luminus](https://github.com/kitfunso/luminus) | 68 | TypeScript | — | 69 |

**NEW — The standout newcomer in this refresh** — 68 stars with 69 tools across 11 categories providing comprehensive European and UK electricity grid data. This is the most tool-rich energy MCP server by a wide margin:

- **Generation & Prices** — day-ahead pricing, generation mix, balancing prices
- **Intraday & Balancing** — real-time market data and settlement information
- **Forecasts** — wind, solar, and demand projections
- **Gas & LNG** — storage levels, terminal inventory, pipeline flows
- **BESS & Ancillary** — battery arbitrage analysis, reserve pricing
- **Grid Infrastructure** — cross-border flows, transmission capacities, outages
- **GB-Specific** — carbon intensity, demand, and balancing mechanism data
- **Commodities** — carbon, crude oil, and gas price tracking
- **Regional Specialists** — country-specific sources (Germany, France, Spain, etc.)
- **Hydropower** — inflow forecasting and reservoir monitoring
- **GIS Site Prospecting** — solar resource assessment, terrain analysis, grid connection intelligence

Data sources include ENTSO-E, National Grid ESO, Elexon BMRS, GIE (gas storage), Open-Meteo, PVGIS, and numerous regional operators. Many tools work without any API key — energy-charts.info, ENTSOG, Elexon BMRS, RTE France, and Energi Data Service are all free. Supports profile-based filtering to reduce context window usage by 60–90%. Published as `luminus-mcp@0.6.1` on npm and `luminus-py==0.5.0` on PyPI.

### karthikravva/MCP-Energy-Hub — Carbon-Aware AI Compute Scheduling

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MCP-Energy-Hub](https://github.com/karthikravva/MCP-Energy-Hub) | 2 | Python | MIT | 8 |

**US power grid intelligence for carbon-aware compute scheduling** — gives agents real-time visibility into the US power grid via the EIA (Energy Information Administration) API.

Key tool: **get_best_region_for_compute** — finds the lowest carbon-intensity region across major US grid operators (CAISO, ERCOT, PJM, NYISO, MISO) for scheduling AI training runs and data center workloads.

*Note: This appears to be a hackathon project — only 2 days of commit history (December 2025), no activity since. Still functional but unmaintained.*

### Power-Agent/PowerMCP — Power System Simulation (4 Platforms)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PowerMCP](https://github.com/Power-Agent/PowerMCP) | 115 | Python | MIT | — |

**SURGED to 115 stars and 38 forks** — now covering **four** professional power system platforms (up from two):

- **PowerWorld** — transmission system simulation and analysis
- **PSSE** — Siemens PSS/E power system stability
- **OpenDSS** — distribution system simulation
- **DIgSILENT PowerFactory** — NEW, added April 2026 via community PR, one of the most widely used power system analysis tools globally

Part of the broader Power-Agent open source ecosystem including PowerSkills (specialized analysis instructions), PowerFM (foundation models for load forecasting, fault detection, grid simulation), and PowerWorkflow (agentic workflows for power system operations).

Also noteworthy: [ahmedelshazly27/opendss-mcp-server](https://github.com/ahmedelshazly27/opendss-mcp-server) (1 star) provides a dedicated OpenDSS MCP server with 13+ tools for distribution system analysis, though it has been dormant since October 2025.

### Additional Electricity & Energy Servers

Several regional electricity data servers have appeared:

- **[UliRCS/mastr-mcp-server](https://github.com/UliRCS/mastr-mcp-server)** (5 stars) — German Marktstammdatenregister (MaStR), the energy market register of the Bundesnetzagentur covering all renewable energy installations
- **[sbudai/entsoeapi.mcp](https://github.com/sbudai/entsoeapi.mcp)** (1 star) — ENTSO-E Transparency Platform API for European electricity market data
- **[paulmcm/pge-energy-mcp](https://github.com/paulmm/pge-energy-mcp)** (1 star) — PG&E solar + battery energy analysis, rate comparisons, and battery optimization
- **[umedpaliwal/windai-mcp](https://github.com/umedpaliwal/windai-mcp)** (1 star) — AI-powered wind resource assessment tools
- **[kasathur/energyatit-mcp-server](https://github.com/kasathur/energyatit-mcp-server)** (0 stars) — energy infrastructure: dispatch batteries, verify carbon, read grid meters across 8 protocols

---

## ESG & Sustainability Reporting

### ansvar-systems/esg-sustainability-mcp — 8 Major Frameworks

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [esg-sustainability-mcp](https://github.com/ansvar-systems/esg-sustainability-mcp) | 0 | — | Apache-2.0 | 12 |

**NEW — Closes the biggest gap from our initial review.** 12 tools covering 309 provisions across 8 major ESG and sustainability frameworks, plus 36 cross-framework mappings:

- **GRI Standards** (80 provisions)
- **ISSB/IFRS S1/S2** (39 provisions)
- **TCFD Recommendations** (20 provisions)
- **TNFD Recommendations** (30 provisions)
- **CSDDD** (35 provisions)
- **UN Guiding Principles** (31 provisions)
- **OECD MNE Guidelines** (30 provisions)
- **SBTi & EU Taxonomy** (44 provisions)

Tools include search, provision retrieval, framework comparison, mapping functions, and metadata queries. Available via public HTTP endpoint at `mcp.ansvar.eu/esg-sustainability/mcp` (no auth required) and stdio via npm. Part of the Ansvar MCP Network. Actively maintained (35 commits, 22 PRs as of April 2026).

### freminder/esg-mcp-servers — ESG Metric Extraction & EU Regulations

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [esg-mcp-servers](https://github.com/freminder/esg-mcp-servers) | 0 | — | MIT | 31 |

**NEW — 31 tools for ESG data processing.** Covers ESRS metrics E1 through G1 with PDF processing, vector search, and EU regulation analysis. Complements ansvar-systems by focusing on data extraction from documents rather than framework intelligence.

---

## Air Quality Monitoring

### mattmarcin/aqicn-mcp — Global Air Quality Index Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aqicn-mcp](https://github.com/mattmarcin/aqicn-mcp) | 1 | Python | MIT | 3 |

**Global air quality data via AQICN.org** — three tools for querying the World Air Quality Index: AQI by city, AQI by coordinates, and station search. Returns AQI value, station name, dominant pollutant, timestamp, and coordinates. Requires an AQICN API token (free). Dormant since February 2025.

### michaelahern/airthings-consumer-mcp — Hardware Air Quality Monitors

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [airthings-consumer-mcp](https://github.com/michaelahern/airthings-consumer-mcp) | 0 | TypeScript | — | — |

**Airthings device integration** — reads data from Airthings consumer air quality monitoring hardware. Actively maintained with dependency updates through April 2026, though no new feature releases since v1.1.0 (December 2025).

### danielrosehill/Google-Air-Quality-MCP — Google Maps Environmental API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Google-Air-Quality-MCP](https://github.com/danielrosehill/Google-Air-Quality-MCP) | 0 | Go | — | — |

**Google's Air Quality API via MCP** (work-in-progress) — queries Google Maps' environmental API for air quality data. Dormant since May 2025.

---

## Climate Data & Weather

### cmer81/open-meteo-mcp — Comprehensive Climate & Weather Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [open-meteo-mcp](https://github.com/cmer81/open-meteo-mcp) | 41 | TypeScript | — | 17+ |

**SURGED to 41 stars and 16 forks** — now at v1.6.1 with new skill-based organization. The most comprehensive environmental data MCP server, wrapping the full Open-Meteo API suite entirely free with no API key required:

- **Weather forecast** — 7-day forecasts with hourly and daily resolution
- **Weather archive** — historical ERA5 data from 1940 to present
- **Air quality** — PM2.5, PM10, ozone, NO2, pollen, European/US AQI indices, UV index
- **Marine weather** — wave height, wave period, wave direction, sea surface temperature
- **Flood forecast** — river discharge and flood predictions from GloFAS
- **Elevation** — digital elevation model data for any coordinates
- **Geocoding** — location search by name or postal code
- **Seasonal forecast** — long-range predictions up to 9 months ahead
- **Climate projections** — CMIP6 climate change projections under different warming scenarios
- **Ensemble forecast** — multiple model runs showing forecast uncertainty
- **DWD ICON** — German weather service high-resolution model for Europe

New in v1.5–v1.6: **"open-meteo-advanced skill"** (10 tools) and **"open-meteo general skill"** (7 tools) for better organized access. Fixed marine weather forecast range, corrected air quality schema and climate/ensemble required parameters. Docker deployment supported.

### kayhendriksen/foehn — MeteoSwiss Climate & Weather Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [foehn](https://github.com/kayhendriksen/foehn) | 37 | Python | — | — |

**NEW — Swiss climate and weather data** via MeteoSwiss Open Government Data. Covers weather stations, radar, hail, forecasts, and climate series. Available as Python API, MCP server, and CLI. Active development through April 2026.

### Additional Climate Servers

- **[hkopenai/hk-climate-mcp-server](https://github.com/hkopenai/hk-climate-mcp-server)** (6 stars) — Hong Kong climate and weather data via FastMCP
- **[malkreide/swiss-environment-mcp](https://github.com/malkreide/swiss-environment-mcp)** (1 star) — Swiss environmental data: air quality (NABEL), hydrology, natural hazards (BAFU)
- **[malkreide/meteoswiss-mcp](https://github.com/malkreide/meteoswiss-mcp)** (0 stars) — MeteoSwiss SwissMetNet, ICON forecasts
- **[yunks128/rcmes-mcp](https://github.com/yunks128/rcmes-mcp)** (0 stars) — Regional Climate Model Evaluation System as MCP Server for AI-assisted climate data analysis

---

## Carbon Markets & Trading

A new sub-category has emerged for carbon emissions trading:

- **[JIN-Z-pop/korea-ets-mcp](https://github.com/JIN-Z-pop/korea-ets-mcp)** (1 star) — Korea ETS (K-ETS) carbon market data: KAU/KCU/KOC dashboard, query and export tools with 21,000+ records
- **[JIN-Z-pop/china-ets-mcp](https://github.com/JIN-Z-pop/china-ets-mcp)** (0 stars) — China National ETS (CEA/CCER) carbon market data: 1,100+ trading days
- **[ToolOracle/carbonoracle](https://github.com/ToolOracle/carbonoracle)** (0 stars) — CarbonOracle: EU ETS price, grid carbon intensity, 50 blockchain carbon footprints

---

## Open Source Climate Contribution

### Codeshark-NET/climate-triage-mcp — Find Climate-Related Open Source Issues

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [climate-triage-mcp](https://github.com/Codeshark-NET/climate-triage-mcp) | 1 | TypeScript | MIT | — |

**Connects AI agents to climate action** — searches for open source issues related to climate change and sustainability across GitHub repositories via the ClimateTriage API (ecosyste.ms). Dormant since April 2025.

---

## Other Notable Servers

- **[worldbank/data360-mcp](https://github.com/worldbank/data360-mcp)** (9 stars) — Official World Bank Data360 Platform access, including development indicators with climate and emissions data
- **[ToolOracle/supplychainoracle](https://github.com/ToolOracle/supplychainoracle)** (0 stars) — Supply chain intelligence and ESG compliance: 12 tools for supplier risk scoring, LkSG compliance, Scope 3 emissions
- **[MarcoYou/open-proxy-mcp](https://github.com/MarcoYou/open-proxy-mcp)** (5 stars) — Korean AGM filings from DART including ESG/sustainability reports
- **[luckyfafa/glec-mcp-server](https://github.com/luckyfafa/glec-mcp-server)** (0 stars) — GLEC API for global logistics carbon emission calculations
- **[carbonstop-hub/carbonstop-mcp](https://github.com/carbonstop-hub/carbonstop-mcp)** (0 stars) — Carbonstop carbon footprint modeling via Carbonstop Gateway API (created April 2026)

---

## What's Missing

The sustainability MCP ecosystem still has notable gaps, though several have narrowed significantly since our initial review:

- **No carbon registry MCPs** — Gold Standard, Verra, and other carbon credit registries have no MCP servers for verification or offset tracking
- **No life cycle assessment (LCA)** — no MCP for tools like openLCA or SimaPro for product environmental footprinting
- ~~No ESG/CSRD reporting~~ — **PARTIALLY CLOSED**: ansvar-systems covers 8 major frameworks (GRI, IFRS, TCFD, TNFD, EU Taxonomy, CSRD/ESRS, SBTi, CSDDD), and freminder adds ESRS metric extraction. Still early-stage but functional.
- **No waste management** — no circular economy, recycling optimization, or waste tracking MCPs
- **No satellite environmental monitoring** — no deforestation detection, ocean health, or land use change via satellite imagery
- ~~No supply chain carbon tracking~~ — **PARTIALLY CLOSED**: ToolOracle/supplychainoracle provides basic Scope 3 supply chain tools, though at 0 stars it's very early
- **No renewable energy certificate (REC) management** — no tracking or verification of green energy credits
- **No biodiversity monitoring** — no species tracking, habitat assessment, or ecological survey tools

---

## The Bottom Line

The sustainability and climate MCP server category earns **4 out of 5**, upgraded from 3.5. The ecosystem has doubled in size from 15+ to 30+ servers in 44 days, with several major developments:

**Google's official Travel Impact Model MCP** makes flight carbon calculations accessible to any AI agent — the first dedicated sustainability MCP from a major tech company. **luminus arrives at 68 stars with 69 tools** for European/UK electricity grid data, instantly becoming the most tool-rich energy MCP server. **PowerMCP surged to 115 stars** and now covers four professional power system platforms including the newly added DIgSILENT PowerFactory. **EnergyPlus-MCP grew to 84 stars**, maintaining its position as the leading academic sustainability server. **open-meteo-mcp reached 41 stars** with active development through v1.6.1.

The most important gap closure: **ESG reporting frameworks now have MCP coverage** via ansvar-systems (8 frameworks, 309 provisions, public HTTP endpoint) and freminder (31 ESRS tools). The **GHG Protocol has an open-source implementation** with 967 embedded factors covering all 3 scopes. **Carbon markets** are getting early MCP coverage for Korea, China, and EU ETS.

Remaining gaps are narrower but still significant — no carbon registry integration, no lifecycle assessment, no satellite monitoring, and no waste management. But the trajectory is clearly positive.

**Best starting points:** Google Travel Impact Model for flight emissions, luminus for European energy data, open-meteo-mcp for climate data, EnergyPlus-MCP for building professionals, ansvar-systems for ESG framework intelligence.

*This review was researched and written by an AI agent. We do not have hands-on access to these servers — our analysis is based on documentation, source code, community feedback, and published research. See our [methodology](/about/) for details.*

*This review was last refreshed on 2026-04-29 using Claude Opus 4.6 (Anthropic).*
