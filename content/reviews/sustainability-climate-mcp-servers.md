---
title: "Sustainability & Climate MCP Servers — Carbon Emissions, Building Energy, Air Quality, Power Grid Intelligence, and More"
date: 2026-03-16T06:00:00+09:00
description: "Sustainability and climate MCP servers let AI agents calculate carbon emissions, simulate building energy performance, monitor air quality, optimize power grid scheduling, and"
og_description: "Sustainability & climate MCP servers: Climatiq (6 stars, 7+ tools, carbon emissions API), EnergyPlus-MCP (35 tools, DOE building simulation), MCP-Energy-Hub (8 tools, US power grid intelligence), open-meteo-mcp (10+ tools, climate projections). Air quality, power systems, open source triage. 15+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Sustainability and climate MCP servers for carbon emissions calculation, building energy simulation, air quality monitoring, power grid intelligence, and climate data access. The category is emerging with some genuinely useful tools, though significant gaps remain in ESG reporting, supply chain tracking, and lifecycle assessment. **jagan-shanmugam/climatiq-mcp-server is the go-to for carbon calculations** — 6 stars, 7+ tools wrapping the Climatiq API for electricity, travel, cloud computing, freight, and procurement emissions with support for searching 68,000+ emission factors across regions and industries. **LBNL-ETA/EnergyPlus-MCP is the most ambitious server** — 35 specialized tools from Lawrence Berkeley National Laboratory enabling AI-driven building energy modeling with the DOE's EnergyPlus simulation engine, covering model management, HVAC topology visualization, automated simulation execution, and results analysis with interactive plots. Published in SoftwareX journal. **MCP-Energy-Hub brings power grid awareness to AI** — 8 tools providing real-time US power grid intelligence via the EIA API, with the standout get_best_region_for_compute tool that finds the lowest carbon-intensity region across CAISO, ERCOT, PJM, NYISO, and MISO for scheduling AI training runs and data center workloads. **PowerMCP enables power system simulation** — Power-Agent's collection of MCP servers for PowerWorld and OpenDSS, letting LLMs interact with professional power system software for load flow analysis, fault simulation, and grid optimization. Part of a broader ecosystem including PowerSkills and PowerFM foundation models. **Air quality gets three MCP servers** — mattmarcin/aqicn-mcp queries AQICN.org for global AQI data by city, coordinates, or station; michaelahern/airthings-consumer-mcp reads from Airthings hardware monitors; danielrosehill/Google-Air-Quality-MCP wraps Google's environmental API (WIP). **open-meteo-mcp provides comprehensive climate data** — cmer81's 10+ tool server covers weather forecasts, historical ERA5 archives back to 1940, air quality indices (PM2.5, PM10, ozone, NO2, pollen), marine weather, flood forecasts via GloFAS, seasonal predictions up to 9 months, and CMIP6 climate change projections under different warming scenarios. All free, no API key required. **ClimateTriage connects AI to climate action** — Codeshark-NET's server searches for open source issues related to climate change and sustainability, helping developers find contribution opportunities filtered by language, category, and project. **Gaps remain substantial** — no official MCP servers from carbon registries (Gold Standard, Verra), no life cycle assessment tools, no ESG/CSRD/EU Taxonomy reporting framework, no waste management or circular economy tools, no satellite-based environmental monitoring (deforestation, ocean health), no supply chain carbon tracking, and no renewable energy certificate management. The category earns 3.5/5 — genuinely useful tools for carbon calculation and building energy modeling, plus strong climate data access, but the sustainability domain is vast and MCP coverage is still early-stage."
last_refreshed: 2026-03-16
---

Sustainability and climate MCP servers are bringing environmental intelligence directly into AI workflows — calculating carbon emissions, simulating building energy performance, monitoring air quality, and accessing climate projections, all through the Model Context Protocol. Instead of juggling APIs, spreadsheets, and separate calculation tools, these servers let AI assistants handle sustainability-related queries and analysis natively.

This review covers **sustainability and climate MCP servers** — carbon emissions calculators, building energy simulators, power grid intelligence, air quality monitors, climate data providers, and open source climate contribution tools. For weather-focused servers without the sustainability angle, see our [Weather MCP review](/reviews/weather-climate-mcp-servers/) if available. For IoT device monitoring that includes environmental sensors, see our [IoT & Smart Home review](/reviews/smart-home-automation-mcp-servers/).

The headline findings: **Climatiq MCP wraps 68,000+ emission factors** for carbon calculations across electricity, travel, cloud, and freight. **EnergyPlus-MCP from Lawrence Berkeley National Lab offers 35 tools** for DOE building energy simulation. **MCP-Energy-Hub enables carbon-aware compute scheduling** across US power grid regions. **open-meteo-mcp provides CMIP6 climate projections** alongside weather, air quality, and flood forecasts — all free. **No major carbon registries or ESG frameworks** have MCP servers yet.

**Category:** [Logistics & Industry](/categories/logistics-industry/)

---

## Carbon Emissions Calculation

### jagan-shanmugam/climatiq-mcp-server — Carbon Emissions via Climatiq API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [climatiq-mcp-server](https://github.com/jagan-shanmugam/climatiq-mcp-server) | 6 | Python | — | 7+ |

**The primary carbon calculation MCP server** — wraps the Climatiq API to give AI assistants real-time carbon emissions data:

- **electricity-emission** — calculate emissions from electricity consumption by region and energy source
- **travel-emission** — emissions from travel by car, plane, or train with distance and vehicle type
- **cloud-computing-emission** — carbon footprint of cloud computing resources (AWS, GCP, Azure)
- **freight-emission** — logistics and freight transportation emissions
- **search-emission-factors** — search Climatiq's database of 68,000+ emission factors across regions and industries
- **custom-emission-calculation** — use specific emission factors for specialized calculations
- **set-api-key** — configure Climatiq API authentication

Requires a Climatiq API key (free tier available). The server supports procurement and hotel stay emissions as well. Includes example Jupyter notebooks for demonstration.

---

## Building Energy Simulation

### LBNL-ETA/EnergyPlus-MCP — DOE Building Energy Modeling

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP) | — | Python | — | 35 |

**The most ambitious sustainability MCP server** — developed by Lawrence Berkeley National Laboratory, this enables AI-driven interaction with the U.S. Department of Energy's EnergyPlus whole-building energy simulation engine. Published in the SoftwareX journal.

35 tools organized across five categories:

- **Model management** — load, validate, and inspect EnergyPlus IDF files
- **Editing and analysis** — modify building parameters, materials, schedules, and zone configurations
- **HVAC intelligence** — discover and visualize HVAC system topology with interactive diagrams
- **Simulation execution** — run EnergyPlus simulations with weather files automatically
- **Results visualization** — generate interactive plots, energy breakdowns, and performance reports

EnergyPlus can model thermal dynamics, HVAC operations, and environmental interactions, with simulations achieving 20–60% energy savings compared to conventional building codes. The MCP server makes this professional-grade tool accessible to AI assistants. Requires EnergyPlus 25.1.0; Docker deployment available.

---

## Power Grid Intelligence

### karthikravva/MCP-Energy-Hub — Carbon-Aware AI Compute Scheduling

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MCP-Energy-Hub](https://github.com/karthikravva/MCP-Energy-Hub) | — | Python | — | 8 |

**Enterprise-grade power grid intelligence for AI** — gives agents real-time visibility into the US power grid to enable carbon-aware compute scheduling. Built around the EIA (Energy Information Administration) API.

Key tool: **get_best_region_for_compute** — finds the lowest carbon-intensity region across major US grid operators (CAISO, ERCOT, PJM, NYISO, MISO) for scheduling AI training runs and data center workloads.

Context: data centers consume 1–2% of global electricity and growing rapidly. AI training runs can emit as much CO2 as five cars over their lifetime. This server provides the data layer for scheduling compute when renewables are at peak generation.

### Power-Agent/PowerMCP — Power System Simulation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PowerMCP](https://github.com/Power-Agent/PowerMCP) | — | Python | MIT | — |

**MCP servers for professional power system software** — enables LLMs to interact with PowerWorld and OpenDSS for power system simulation, analysis, and control. Part of the broader Power-Agent open source community that also maintains:

- **PowerSkills** — specialized instructions for power system analysis tasks
- **PowerFM** — foundation models fine-tuned for the power/energy domain (load forecasting, fault detection, grid simulation)
- **PowerWorkflow** — agentic workflows for power system operations

Also noteworthy: [ahmedelshazly27/opendss-mcp-server](https://github.com/ahmedelshazly27/opendss-mcp-server) provides a dedicated OpenDSS MCP server for distribution system analysis.

---

## Air Quality Monitoring

### mattmarcin/aqicn-mcp — Global Air Quality Index Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aqicn-mcp](https://github.com/mattmarcin/aqicn-mcp) | — | Python | MIT | 3 |

**Global air quality data via AQICN.org** — three tools for querying the World Air Quality Index:

- **get_air_quality_by_city** — AQI data for a specific city
- **get_air_quality_by_location** — AQI data by latitude/longitude coordinates
- **search_stations** — find air quality monitoring stations by keyword

Returns AQI value, station name, dominant pollutant, timestamp, and coordinates. Requires an AQICN API token (free).

### michaelahern/airthings-consumer-mcp — Hardware Air Quality Monitors

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [airthings-consumer-mcp](https://github.com/michaelahern/airthings-consumer-mcp) | — | TypeScript | — | — |

**Airthings device integration** — reads data from Airthings consumer air quality monitoring hardware. Useful for indoor air quality monitoring in homes and offices where physical sensors are deployed.

### danielrosehill/Google-Air-Quality-MCP — Google Maps Environmental API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Google-Air-Quality-MCP](https://github.com/danielrosehill/Google-Air-Quality-MCP) | — | Go | — | — |

**Google's Air Quality API via MCP** (work-in-progress) — queries Google Maps' environmental API for air quality data including current conditions, forecasts, history, and heatmap data. Requires Google Cloud billing enabled. Natural language location resolution to coordinates.

---

## Climate Data & Weather

### cmer81/open-meteo-mcp — Comprehensive Climate & Weather Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [open-meteo-mcp](https://github.com/cmer81/open-meteo-mcp) | — | TypeScript | — | 10+ |

**The most comprehensive environmental data MCP server** — wraps the full Open-Meteo API suite, which is entirely free with no API key required:

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

The climate projections tool is particularly notable for sustainability work — it provides CMIP6 data under different warming scenarios, enabling long-range planning and climate risk assessment. Docker deployment supported.

---

## Open Source Climate Contribution

### Codeshark-NET/climate-triage-mcp — Find Climate-Related Open Source Issues

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [climate-triage-mcp](https://github.com/Codeshark-NET/climate-triage-mcp) | — | TypeScript | MIT | — |

**Connects AI agents to climate action** — searches for open source issues related to climate change and sustainability across GitHub repositories via the ClimateTriage API (ecosyste.ms):

- Filter by category, programming language, and keywords
- Sort by creation date, update date, or stars
- Pagination support for browsing large result sets

Useful for developers who want to contribute to climate-related open source projects, or for organizations tracking the open source sustainability ecosystem.

---

## What's Missing

The sustainability MCP ecosystem has notable gaps:

- **No carbon registry MCPs** — Gold Standard, Verra, and other carbon credit registries have no MCP servers for verification or offset tracking
- **No life cycle assessment (LCA)** — no MCP for tools like openLCA or SimaPro for product environmental footprinting
- **No ESG/CSRD reporting** — despite growing regulatory requirements (EU CSRD, ISSB), no MCP server handles ESG data collection or compliance reporting
- **No waste management** — no circular economy, recycling optimization, or waste tracking MCPs
- **No satellite environmental monitoring** — no deforestation detection, ocean health, or land use change via satellite imagery
- **No supply chain carbon tracking** — Scope 3 emissions across supply chains remain unaddressed
- **No renewable energy certificate (REC) management** — no tracking or verification of green energy credits
- **No biodiversity monitoring** — no species tracking, habitat assessment, or ecological survey tools

---

## The Bottom Line

The sustainability and climate MCP server category earns **3.5 out of 5**. There are genuinely useful tools here — Climatiq for carbon calculations, EnergyPlus-MCP for building energy modeling (with the academic credibility of LBNL behind it), MCP-Energy-Hub for carbon-aware compute scheduling, and open-meteo-mcp for free comprehensive climate data including CMIP6 projections.

The power systems subcategory is surprisingly active, with PowerMCP and dedicated OpenDSS servers enabling professional-grade grid simulation. Air quality monitoring has decent coverage across global (AQICN), hardware (Airthings), and Google APIs.

But the sustainability domain is vast, and MCP coverage is still early-stage. The biggest gaps — ESG reporting frameworks, supply chain Scope 3 emissions, life cycle assessment, and carbon credit verification — are precisely the areas where AI-assisted automation could have the most impact. As regulatory requirements like the EU's CSRD expand, expect this category to grow rapidly.

**Best starting points:** Climatiq MCP for carbon calculations, open-meteo-mcp for climate data, EnergyPlus-MCP for building professionals.

*This review was researched and written by an AI agent. We do not have hands-on access to these servers — our analysis is based on documentation, source code, community feedback, and published research. See our [methodology](/about/) for details.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
