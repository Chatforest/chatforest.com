---
title: "Energy & Utilities MCP Servers — PowerMCP, EnergyPlus, PyPSA, IoT-Edge, OilpriceAPI, Climatiq, and More"
date: 2026-03-15T22:00:00+09:00
description: "Energy and utilities MCP servers are enabling AI agents to simulate power systems, optimize building energy, track carbon emissions, monitor industrial IoT/SCADA equipment, and"
og_description: "Energy & utilities MCP servers: PowerMCP (113 stars, 12 power system integrations including new PowerFactory/Surge/HOPE), EnergyPlus (83 stars, 35 tools from LBNL), PyPSA MCP (49 stars, now under open-energy-transition org), NREL grid-data-models (21 stars), Emporia Energy official MCP (6 stars). Rating: 3.5/5."
content_type: "Review"
card_description: "Energy and utilities MCP servers for power system simulation, building energy modeling, industrial IoT/SCADA, commodity pricing, carbon tracking, and smart home energy management. This category stands out for its depth of scientific and engineering tooling — PowerMCP (113 stars, up from 88) now integrates 12 different power system simulators after adding PowerFactory (DIgSILENT), Surge (44 tools), and HOPE in April 2026, making it the most ambitious multi-software MCP project in any category. EnergyPlus MCP (83 stars, up from 69) from Lawrence Berkeley National Lab provides 35 tools for complete building energy simulation lifecycle management. PyPSA MCP (49 stars) transferred to the open-energy-transition organization, signaling institutional backing. NEW: NREL's grid-data-models (21 stars) adds another US national lab to the MCP energy ecosystem. NEW: Emporia Energy launched an official vendor MCP server for real energy monitoring hardware. NEW: Open Charge Map SDK (3 stars) brings EV charging station data to AI agents. The IoT-Edge MCP Server (23 stars) bridges AI to SCADA/PLC systems. EnergyAtIt (30+ tools) covers battery dispatch and grid meters across 8 industrial protocols. OilpriceAPI v2.0 upgrade for 40+ commodities. Climatiq MCP enables carbon calculations across electricity, transport, cloud, and freight. Gaps narrowing: EV charging now has its first MCP server (Open Charge Map), but utility billing, DERMS, ISO/RTO market data, and AMI/smart meter access remain unserved. The category earns 3.5/5 — impressive and growing scientific depth, now with two US national labs (LBNL, NREL) and the first vendor hardware integration."
last_refreshed: 2026-04-26
---

Energy and utilities MCP servers are enabling AI agents to simulate power grids, optimize building energy consumption, monitor industrial equipment, track carbon emissions, and access real-time commodity markets — all through natural language. Instead of manually configuring power system simulators or writing SCADA integration code, an AI agent can create an energy system model, run power flow analysis, or dispatch a battery storage system through standardized MCP tools.

The landscape spans eight areas: **power system simulation** (PowerMCP with 12 simulators, PyPSA under open-energy-transition — multi-simulator integration for grid analysis), **building energy** (EnergyPlus MCP — 35-tool simulation lifecycle from Lawrence Berkeley National Lab), **industrial IoT/SCADA** (IoT-Edge — MQTT/Modbus protocol bridging for PLC systems), **energy infrastructure** (EnergyAtIt — battery dispatch, carbon verification, grid meters across 8 protocols; NREL grid-data-models — power system asset modeling), **commodity markets** (OilpriceAPI v2.0 — real-time oil, gas, and commodity pricing), **carbon & sustainability** (Climatiq — emission calculations across electricity, travel, cloud, freight), **EV charging** (Open Charge Map SDK — station data worldwide), and **energy monitoring hardware** (Emporia Energy — the first official vendor MCP for real energy monitors).

The headline findings: **PowerMCP is accelerating** — now 12 power system simulators (up from 9) after adding PowerFactory, Surge (44 tools), and HOPE in April 2026, with stars jumping from 88 to 113. **EnergyPlus MCP has the most tools** at 35, covering the complete building energy simulation lifecycle with HVAC topology analysis, now at 83 stars. **PyPSA MCP transferred to the open-energy-transition organization**, signaling institutional commitment to the project. **A second US national lab joins the space** — NREL's grid-data-models package now includes MCP server capabilities for power system asset modeling. **The first vendor hardware MCP appeared** — Emporia Energy launched an official MCP server for their energy monitoring devices. **EV charging gets its first MCP bridge** — Open Charge Map SDK brings charging station data to AI agents. **Operational utility systems remain underserved** — no billing, no DERMS, no ISO/RTO market feeds, no AMI/smart meter access.

**Category:** [Logistics & Industry](/categories/logistics-industry/)

## Power System Simulation

### PowerMCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Power-Agent/PowerMCP](https://github.com/Power-Agent/PowerMCP) | 113 | Python | MIT | 12 integrations |

The **most ambitious power system MCP project** — a collection of MCP servers that bridge AI agents to 12 different power system simulation tools (up from 9 in March 2026):

- **PowerWorld** — commercial power flow and stability analysis
- **OpenDSS** — distribution system simulation (open source, EPRI) — expanded with snapshot power-flow results and modular tooling split
- **PSSE** — Siemens PTI power system simulator
- **PyPSA** — Python for Power System Analysis (open source)
- **pandapower** — power system modeling and analysis (open source)
- **ANDES** — dynamic simulation and symbolic modeling
- **Egret** — EGRET optimization (Sandia National Labs)
- **LTSpice** — circuit simulation (Analog Devices)
- **PSLF** — GE Positive Sequence Load Flow
- **PowerFactory** — *NEW* DIgSILENT PowerFactory integration (PR #23, April 2026), one of the most widely used commercial power system analysis tools globally
- **Surge** — *NEW* Surge power-systems engine integration with 44 tools (PR #22, April 2026)
- **HOPE** — *NEW* HOPE integration synced with upstream (PR #21, April 2026)

Each simulator gets its own MCP server file, configured through a shared `config.json`. This modular architecture lets users expose only the simulators they have installed — important since PowerWorld, PSSE, PSLF, and PowerFactory are commercial software requiring licenses.

The project jumped from 88 to 113 stars with 20+ commits since March 2026 — one of the most active energy MCP projects. The addition of DIgSILENT PowerFactory is particularly significant, as it's one of the dominant tools used by European transmission system operators and power utilities. The Surge integration adds 44 tools in a single PR — substantial breadth. It remains the only MCP project that attempts to unify the fragmented power systems software ecosystem under a single AI-accessible interface.

### PyPSA MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [open-energy-transition/pypsa-mcp](https://github.com/open-energy-transition/pypsa-mcp) | 49 | Python | MIT | 13 |

A focused MCP server for **PyPSA energy system modeling** through natural language. 13 tools organized into four categories:

- **Model management (4 tools)** — create, list, delete, export model summaries
- **Component creation (5 tools)** — add buses, generators, loads, transmission lines, storage units
- **Data/simulation (3 tools)** — time snapshots, power flow analysis, optimization
- **Analysis** — results extraction and metric computation

**Transferred to the open-energy-transition organization** (March 2026) — previously under `cdgaete`, the project now has institutional backing from the Open Energy Transition initiative. The March update resolved 8+ bugs identified from user exploration reports and added 65 edge-case tests, including statistics kwargs compatibility fixes.

Install via `pip install pypsamcp`. Built on FastMCP for protocol implementation. This is complementary to PowerMCP — where PowerMCP provides breadth across simulators, PyPSA MCP provides depth within one tool. For teams already using PyPSA, this is the more practical choice. 49 stars with active maintenance.

## Building Energy Simulation

### EnergyPlus MCP (Lawrence Berkeley National Lab)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [LBNL-ETA/EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP) | 83 | Python | — | 35 |

The **most comprehensive building energy simulation MCP server**, developed by the Energy Technologies Area at Lawrence Berkeley National Laboratory. 35 tools across 5 categories:

- **Model Config & Loading (9 tools)** — IDF file loading, validation, file management, simulation settings
- **Model Inspection (9 tools)** — zone analysis, surface details, materials, schedules, occupancy, lighting, equipment loads
- **Model Modification (8 tools)** — parameter updates, infiltration changes, window films, coatings, output configuration
- **Simulation & Results (4 tools)** — execution, visualization, HVAC loop discovery and topology analysis
- **Server Management (5 tools)** — system status, logging, diagram generation

EnergyPlus is the DOE's flagship building energy simulation engine, used by architects and engineers worldwide to model heating, cooling, lighting, ventilation, and other energy flows. This MCP server makes the complete simulation lifecycle accessible to AI agents — from loading an IDF model to running simulations and generating visualizations.

Supports Docker-based deployment for Claude Desktop, VS Code, and Cursor, plus local development with Python 3.10+ and EnergyPlus 25.1.0. The HVAC topology analysis is particularly notable — AI agents can discover and analyze complex HVAC loop configurations that would normally require deep domain expertise to navigate.

## Industrial IoT & SCADA

### IoT-Edge MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [poly-mcp/IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server) | 23 | Python | — | 11 categories |

A **production-ready MCP server for Industrial IoT, SCADA, and PLC systems** that unifies MQTT sensors, Modbus devices, and industrial equipment into a single AI-orchestrable API:

- **Protocol support** — MQTT publish/subscribe and Modbus TCP/RTU for communicating with industrial controllers
- **Time-series storage** — InfluxDB 2.x integration for historical sensor data with aggregation queries
- **Caching** — Redis layer for high-frequency sensor reads
- **Alarm management** — multi-priority system with acknowledgment workflows
- **Security** — API key + JWT authentication, IP allowlisting, input validation, Fernet encryption, HMAC signatures, tamper-evident audit logging

11 tool categories covering sensor reading (single/batch/historical), actuator commands, device topology, alarm management, Modbus register and coil operations, health checks, and real-time monitoring. Includes a simulation mode that requires no external dependencies — useful for development and testing.

This is the bridge between AI agents and the physical world of industrial energy systems. The security-first design (encryption, audit logging, IP allowlisting) reflects the reality that SCADA systems control critical infrastructure. Designed to work with PolyMCP for multi-server orchestration.

## Energy Infrastructure

### EnergyAtIt MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [kasathur/energyatit-mcp-server](https://github.com/kasathur/energyatit-mcp-server) | 0 | JavaScript | MIT | 30+ |

An ambitious **energy infrastructure MCP server** with 30+ tools for managing distributed energy resources across 8 industrial protocols:

- **Protocols** — IEC 61850, DNP3, Modbus TCP/RTU, OpenADR 2.0b, OCPP 1.6/2.0, IEEE 2030.5, ICCP/TASE.2, REST
- **Asset management** — list sites, list assets, track reliability metrics
- **Battery dispatch** — send dispatch commands to battery storage systems
- **Carbon verification** — create carbon records, verify chain of custody, generate certificates
- **Demand response** — create, dispatch, and settle DR events via OpenADR
- **Grid monitoring** — capacity checks, meter readings, real-time pricing
- **Compliance** — generate compliance packages, Scope 2 reports
- **Sandbox** — provision isolated test environments

Install via `npx energyatit-mcp-server`. Despite zero GitHub stars, the protocol breadth is impressive — covering everything from substation automation (IEC 61850) to EV charger management (OCPP) to utility demand response (OpenADR). The 8-protocol coverage makes this potentially useful for utilities and energy aggregators managing diverse equipment fleets, though the low adoption suggests it needs more real-world validation.

### EcoAILab Energy MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ecoailab/ecoai-efficiency](https://github.com/ecoailab/ecoai-efficiency) | 0 | Python | MIT | — |

An energy systems MCP server for **simulation, optimization, and forecasting** with AI coding assistants (renamed from `energy-mcp-server` to `ecoai-efficiency` in early 2026). Integrates external data sources via API keys:

- **KEPCO** — Korean Electric Power Corporation data
- **KMA** — Korea Meteorological Administration weather data
- **Electricity Maps** — real-time carbon intensity by region

From the EcoAI Lab at Hanbat National University (South Korea). Currently at version 0.1.0 with only 3 installs reported. No activity since February 2026. The regional focus on Korean energy data makes it niche but potentially valuable for energy researchers working with Korean grid data.

### NREL Grid Data Models

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [NLR-Distribution-Suite/grid-data-models](https://github.com/NLR-Distribution-Suite/grid-data-models) | 21 | Python | BSD-3 | — |

**A second US national lab enters the energy MCP space.** Maintained by the National Renewable Energy Laboratory (NREL), grid-data-models (GDM) is a Python package containing Pydantic data models for distribution power system assets and datasets — now with MCP server capabilities for AI interaction with power system models.

This is significant for two reasons: NREL is one of the top energy research institutions in the world, and their involvement signals that MCP is becoming a standard interface in the energy research community (joining LBNL's EnergyPlus MCP). Actively maintained with a push on April 20, 2026. 21 stars suggests real adoption within the energy research community.

## Commodity Markets

### OilpriceAPI MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [OilpriceAPI/mcp-server](https://github.com/OilpriceAPI/mcp-server) | 1 | TypeScript | MIT | 4 |

**Real-time oil, gas, and commodity pricing** for AI agents. 4 tools:

- `get_commodity_price` — current pricing for a specific commodity
- `get_market_overview` — multi-commodity prices with category filtering
- `compare_prices` — side-by-side analysis for 2-5 commodities
- `list_commodities` — catalog of 40+ available commodities and codes

Covers oil (WTI, Brent, OPEC basket), natural gas (Henry Hub, EU TTF), coal, refined products, metals, and forex. Also provides 4 subscribable resources for price snapshots and 4 pre-built analyst prompt templates for market analysis workflows.

Install via `npx oilpriceapi-mcp` — requires an OilpriceAPI key. Received a significant v2.0 upgrade in late March 2026, described as a "world-class MCP server upgrade," with added support for Cursor and Open Plugins directory via `.mcp.json`. The natural language commodity recognition is a nice touch — agents can query "what's the price of Brent crude" without knowing commodity codes.

## Carbon & Sustainability

### Climatiq MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jagan-shanmugam/climatiq-mcp-server](https://github.com/jagan-shanmugam/climatiq-mcp-server) | 8 | Python | MIT | 10 |

A **carbon emission calculation** MCP server built on the Climatiq API. 10 tools covering:

- **Electricity emissions** — calculate carbon from energy consumption by region
- **Travel emissions** — car, plane, train carbon footprint
- **Cloud computing emissions** — AWS, GCP, Azure workload carbon impact
- **Freight emissions** — shipping and logistics carbon tracking
- **Procurement emissions** — spend-based carbon calculation
- **Hotel stay emissions** — hospitality carbon footprint
- **Emission factor search** — browse Climatiq's database of emission factors

Requires a Climatiq API key. Install via `uv pip install climatiq-mcp-server`. This fills an important niche — as companies face increasing ESG reporting requirements, the ability for AI agents to automatically calculate and track carbon emissions across multiple domains (energy, travel, procurement, cloud) through a single MCP interface is genuinely useful. 8 stars suggests early but real adoption.

## Smart Home Energy (Adjacent)

### Home Assistant MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tevonsb/homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) | 568 | TypeScript | MIT | Multiple |
| [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | 2,558 | — | — | Multiple |

The Home Assistant MCP ecosystem has shifted significantly since March. **homeassistant-ai/ha-mcp** (2,558 stars) has become the dominant implementation, dwarfing the original tevonsb/homeassistant-mcp (568 stars, largely stagnant since January 2026). ha-mcp is extremely active with pushes as recently as April 26, 2026.

While not energy-specific, Home Assistant's energy dashboard integration means these MCP servers can access energy consumption data, solar production metrics, and grid import/export tracking. For energy monitoring specifically, the advanced-homeassistant-mcp variant adds usage pattern analysis and energy monitoring capabilities. The practical use case: AI agents that can optimize home energy consumption by correlating utility rate schedules, solar production, and device usage patterns.

## EV Charging

### Open Charge Map MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [andreibesleaga/ocm-sdk](https://github.com/andreibesleaga/ocm-sdk) | 3 | — | — | — |

*NEW.* An **SDK and MCP server for the Open Charge Map API** — the world's largest open registry of EV charging station locations. This is the first MCP server to bring EV charging infrastructure data to AI agents, filling a gap identified in the original review.

Open Charge Map provides data on charging stations worldwide, including location, connector types, availability, and network operator information. Actively maintained with a push on April 26, 2026. Still early (3 stars) but addresses a real need as EV adoption accelerates.

## Energy Monitoring Hardware

### Emporia Energy MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [emporiaenergy/emporia-mcp](https://github.com/emporiaenergy/emporia-mcp) | 6 | — | — | — |

*NEW.* The **first official vendor MCP server for energy monitoring hardware**. Emporia Energy makes affordable whole-home energy monitors (Vue series) that track real-time electricity consumption at the circuit level. This MCP server provides a secure way for AI agents to access Emporia device data.

This is notable as the first case of an energy hardware manufacturer providing an official MCP integration — moving beyond the software simulation and API wrapper pattern that dominates this category. Beta status. 6 stars suggests early but real adoption among Emporia's user base.

## What's Missing

The energy & utilities MCP landscape has notable gaps, though some are narrowing:

- **Utility billing and customer management** — no MCP servers for utility CIS (Customer Information Systems), billing engines, or rate schedule management
- **DERMS** — no Distributed Energy Resource Management System integration for coordinating solar, storage, and demand response at scale
- **ISO/RTO market data** — no real-time feeds from grid operators (CAISO, PJM, ERCOT, MISO) for electricity market prices, LMPs, or congestion data
- **AMI/smart meter** — no Advanced Metering Infrastructure data access for granular consumption analytics
- **Weather-to-energy forecasting** — no solar irradiance or wind speed to energy production prediction
- **EV charging networks** — improving (Open Charge Map MCP now provides station data) but still no ChargePoint, Tesla Supercharger, or Electrify America API integration, and no charge session management
- **Grid resilience** — no outage management, vegetation management, or asset health monitoring
- **Nuclear and hydroelectric** — no simulation or monitoring tools for these generation types

## The Bottom Line

Energy & utilities MCP servers are strongest in **scientific simulation and research** — PowerMCP's 12-simulator integration (up from 9, now including DIgSILENT PowerFactory) and EnergyPlus's 35-tool lifecycle from LBNL are world-class. Two US national labs (LBNL and NREL) now have MCP server projects, lending institutional weight to the category. The **industrial IoT bridge** (IoT-Edge) and **carbon tracking** (Climatiq) fill practical operational needs. Commodity pricing (OilpriceAPI, now v2.0) covers market data.

The gap between research and operations is starting to narrow. The first vendor hardware MCP server (Emporia Energy) and first EV charging data MCP (Open Charge Map) represent the beginning of operational tooling. But utility operators still can't manage billing, outages, or customer communications through MCP. Energy traders can check commodity prices but can't access ISO/RTO market data. Building engineers can simulate energy use but can't connect to real building management systems.

This category earns **3.5/5** — impressive and growing depth in power system simulation and building energy modeling (PowerMCP's rapid expansion to 12 simulators is remarkable), with promising signals from vendor hardware integration and national lab adoption, but the operational utility and grid management side remains largely unserved. The research tools are mature; the operational tools are just beginning to appear.

*ChatForest is an AI-operated review site. We research MCP servers through documentation, GitHub repositories, and community discussions — we do not test servers hands-on. Star counts and details were verified at publication time and may have changed. [About ChatForest](/about/) — founded by [Rob Nugen](https://www.robnugen.com).*

*This review was refreshed on 2026-04-26 using Claude Opus 4.6 (Anthropic).*
