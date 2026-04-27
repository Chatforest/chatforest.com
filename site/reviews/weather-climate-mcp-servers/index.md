# Weather & Climate MCP Servers — Open-Meteo, OpenWeatherMap, NOAA/NWS, AccuWeather, Aviation METAR/TAF, Climatiq, Stormglass, and More

> Weather and climate MCP servers are enabling AI agents to retrieve forecasts, current conditions, historical weather data, air quality readings, severe weather alerts, marine


Weather and climate MCP servers are enabling AI agents to check forecasts, monitor severe weather, analyze historical climate data, track air quality, calculate carbon emissions, and access marine conditions — all through natural language. Instead of manually calling weather APIs or parsing JSON responses, an AI agent can simply ask "What's the weather in Tokyo this week?" or "Show me air quality in Beijing" and get structured, actionable data back.

The landscape spans eight areas: **comprehensive multi-source platforms** (weather-mcp, Open-Meteo MCP — unified access to multiple weather APIs and models), **Open-Meteo implementations** (free, no API key, global coverage), **OpenWeatherMap integrations** (commercial API with free tier), **NOAA/NWS servers** (free US government weather data), **NOAA oceanographic data** (tides, currents, sea level trends, flood analysis), **AccuWeather servers** (commercial forecasting), **aviation weather** (METAR, TAF, PIREP, SIGMET — NEW), **marine & surf** (ocean conditions, tides, wave forecasts), and **air quality, carbon & climate** (pollution monitoring, emission calculations, earthquake data).

The headline findings: **Weather is one of the most duplicated MCP categories** — at least 30 implementations exist, many doing nearly the same thing. **Open-Meteo dominates the free tier** with comprehensive coverage and no API key requirement. **cmer81/open-meteo-mcp has the most tools** at 19, spanning 7 national weather models and CMIP6 climate projections (now 41 stars, up from 36). **weather-mcp/weather-mcp is the most feature-diverse** with 16 tools pulling from 5 free API sources covering forecasts through wildfire tracking (doubled to 6 stars). **NEW: NOAA Tides & Currents** (RyanCardin15, 25+ tools) provides the most comprehensive oceanographic MCP server with water levels, tide predictions, currents, sea level trends, flood analysis, and astronomy data. **NEW: Aviation weather emerged as a subcategory** — blevinstein/aviation-mcp (9 stars) provides METAR, TAF, PIREP, SIGMET, and G-AIRMET data plus aeronautical charts and NOTAMs. **The gap between basic and advanced is wide** — most servers offer simple current conditions and forecasts, while only a few tackle historical data, marine conditions, or climate projections.

**Category:** [Lifestyle & Personal](/categories/lifestyle-personal/)

## Comprehensive Multi-Source Platforms

### weather-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [weather-mcp/weather-mcp](https://github.com/weather-mcp/weather-mcp) | 6 | TypeScript | MIT | 16 |

The **most feature-diverse weather MCP server** — 16 tools pulling from 5 free API sources with **zero API keys required**:

- **NOAA** — US weather forecasts, current conditions, severe weather alerts, fire weather indices
- **Open-Meteo** — international forecasts, historical data (1940–present), climate normals
- **RainViewer** — weather radar and precipitation imagery
- **Blitzortung.org** — real-time lightning strike detection
- **NIFC WFIGS** — wildfire tracking and perimeters

Tools span current conditions, forecasts (up to 16 days), historical weather, air quality, marine conditions, lightning activity, weather radar imagery, river monitoring, wildfire proximity alerts, and saved location management. Automatic source selection picks the best data provider based on location (NOAA for US, Open-Meteo for international).

Performance features include built-in in-memory cache (50–80% API call reduction, <10ms cached response vs 200–1000ms for API calls) with intelligent TTL-based expiration and LRU eviction. Tool selection presets (basic/standard/full/all) let users optimize context window usage. Available in the Official MCP Registry as `io.github.dgahagan/weather-mcp`. Star count doubled from 3 to 6 since initial review — the most ambitious scope of any weather MCP server is gaining traction.

### Open-Meteo MCP (cmer81)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cmer81/open-meteo-mcp](https://github.com/cmer81/open-meteo-mcp) | 41 | TypeScript | — | 19 |

The **most comprehensive weather MCP server by tool count** — 19 tools spanning Open-Meteo's complete API suite:

- **Core weather (6)** — forecast, archive (1940–present), air quality, marine weather, elevation, geocoding
- **National weather models (7)** — DWD ICON (Germany), NOAA GFS (US), Météo-France, ECMWF (European), JMA (Japan), MET Norway, Environment Canada GEM
- **Advanced forecasting (4)** — flood forecast, seasonal forecast, climate projections (CMIP6), ensemble forecast
- **Plus** geocoding and elevation lookups

The national weather model tools are notable — they let you query specific numerical weather prediction models rather than just blended forecasts, which is valuable for meteorological research or comparing model accuracy. CMIP6 climate projections extend the scope to multi-decade climate change analysis.

Requires Node.js ≥22.0.0. Dual transport (stdio and HTTP via Express). Docker support with pre-built GHCR images. 41 stars and 16 forks (up from 36 stars/14 forks) — the most popular weather MCP server by star count. Released v1.3.1 with Zod validation fixes. No API key required for any endpoint.

## Open-Meteo Implementations

Open-Meteo is the most popular weather API in the MCP ecosystem due to its free tier, no API key requirement, and comprehensive data. Multiple implementations exist:

### OpenMeteo MCP (gbrigandi — Rust)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gbrigandi/mcp-server-openmeteo](https://github.com/gbrigandi/mcp-server-openmeteo) | 1 | Rust | MIT | 4 |

A **Rust implementation** of Open-Meteo access — 4 tools: current weather, forecast (up to 16 days with daily highs/lows, UV index, sunrise/sunset), historical weather (date range analysis with min/max/mean statistics), and location search. Human-readable weather reports with emojis. Notable for being one of the few Rust-based MCP servers in any category. 30-second request timeouts with input validation for coordinate ranges.

### Other Open-Meteo Implementations

| Server | Stars | Language | Tools | Notes |
|--------|-------|----------|-------|-------|
| [JeremyMorgan/Weather-MCP-Server](https://github.com/JeremyMorgan/Weather-MCP-Server) | — | Python | 2 | Current conditions and forecasts |
| [isdaniel/mcp_weather_server](https://github.com/isdaniel/mcp_weather_server) | — | Python | 2 | Basic Open-Meteo wrapper |
| [microagents/mcp-weather-free](https://github.com/microagents/mcp-weather-free) | — | Python | 2 | Get weather by coordinates or city name |
| [lucasinocencio1/mcp-surf-forecast](https://github.com/lucasinocencio1/mcp-surf-forecast) | — | Python | — | Open-Meteo Marine API for surf/swell data |

The duplication here illustrates a common pattern in the MCP ecosystem: weather is a popular beginner project, so many minimal implementations exist. For production use, cmer81/open-meteo-mcp (above) covers the same API with far more completeness.

## OpenWeatherMap Servers

### jezweb/weather-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jezweb/weather-mcp-server](https://github.com/jezweb/weather-mcp-server) | 11 | Python | MIT | 5 |

The **best OpenWeatherMap MCP integration** — 5 tools: current weather, 5-day forecast (3-hour intervals), location search, weather by ZIP code, and air quality (AQI with pollutant breakdown). Smart caching with configurable TTL (default 10 minutes) is important here because OpenWeatherMap's free tier limits you to 1,000 API calls/day and 60 calls/minute. Supports metric, imperial, and standard temperature units. Dual transport (HTTP/stdio) via FastMCP.

### robertn702/mcp-openweathermap

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [robertn702/mcp-openweathermap](https://github.com/robertn702/mcp-openweathermap) | 3 | JS/TS | MIT | 10+ |

The **most tool-rich OpenWeatherMap MCP server** — 10+ tools including current weather, 5-day forecast, hourly forecast (48 hours), daily forecast (8 days), **minutely precipitation** (minute-by-minute rain/snow), weather alerts with severity classification, current and historical air pollution, reverse geocoding, and forward geocoding. Built with Bun runtime. The minutely precipitation feature is unusual — most weather MCP servers don't expose this granular data.

### rossshannon/weekly-weather-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rossshannon/weekly-weather-mcp](https://github.com/rossshannon/weekly-weather-mcp) | 8 | Python | MIT | 2 |

A **weekly forecast specialist** using OpenWeatherMap's One Call API 3.0 — 2 tools: `get_weather` (8-day forecasts with morning, afternoon, and evening data points for each day) and `get_current_weather` (present conditions). The time-of-day granularity is unique — most weather MCP servers return a single daily forecast, while this one breaks each day into three periods with separate temperature, precipitation, and wind data. Built on Zippland's earlier work with extended functionality. Tested with Claude Desktop, Cursor, and other MCP clients. 8 stars — the third-most popular OpenWeatherMap MCP server.

### Other OpenWeatherMap Implementations

| Server | Stars | Language | Tools | Notes |
|--------|-------|----------|-------|-------|
| [Zippland/weather-mcp](https://github.com/Zippland/weather-mcp) | 7 | Python | 2 | get_weather and get_current_weather, multi-timezone support |
| [mschneider82/mcp-openweather](https://github.com/mschneider82/mcp-openweather) | — | Go | — | Free API tier wrapper |

## NOAA / National Weather Service Servers

Free US government weather data with no API key required — the most cost-effective option for US-focused applications.

### dangahagan/weather-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| dangahagan/weather-mcp | — | TypeScript | — | — |

A **dual-source weather server** — automatically selects NOAA for US locations and Open-Meteo for international forecasts. Available via npx (`npx -y @dangahagan/weather-mcp@latest`). This hybrid approach is smart: NOAA provides the most authoritative US weather data (it's the source data that AccuWeather and others build on), while Open-Meteo fills the international gap.

### benziela/weather-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| benziela/weather-mcp | — | — | — | 2 |

A **NWS-only server** — weather forecasts and severe weather alerts for US locations via latitude/longitude. No API key needed. Simple and focused: if you only need US weather, this avoids any commercial API dependency.

### NWS Reference Implementation

The official Anthropic MCP documentation uses a National Weather Service weather server as its tutorial example, making NWS-based weather servers the most commonly reproduced MCP implementation. Many of the "basic" weather servers on GitHub are variations of this tutorial. Microsoft's Azure-Samples organization now provides NWS MCP reference implementations in both Node.js/TypeScript and Python, with Azure App Service deployment support — adding enterprise-grade deployment patterns to the tutorial ecosystem.

## NOAA Tides, Currents & Oceanographic Data

### RyanCardin15/NOAA-TidesAndCurrents-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [RyanCardin15/NOAA-TidesAndCurrents-MCP](https://github.com/RyanCardin15/NOAA-TidesAndCurrents-MCP) | 4 | TypeScript | MIT | 25+ |

The **most comprehensive oceanographic MCP server** — 25+ tools spanning four domains from the NOAA Tides and Currents API:

- **Water Data (6 tools)** — real-time water levels, tide predictions, current measurements and forecasts, meteorological data (wind, temperature, pressure), station search and details
- **Climate & Research (9 tools)** — sea level trend analysis, high tide flooding projections and daily counts, extreme water level statistics, historical top-ten water levels
- **Astronomy (7 tools)** — moon phase calculations and ranges, solar times (sunrise, sunset, dawn, dusk), sun position tracking, next lunar/solar event predictions
- **Configuration (1 tool)** — parameter definitions and valid API values

Built on FastMCP with zero-config setup. Multiple transport modes: STDIO for Claude Desktop and HTTP with Server-Sent Events for web integration. Available via `npx @ryancardin/noaa-tides-currents-mcp-server` or the shorter alias `npx noaa-mcp`. Also published on npm and Smithery. The sea level trend and flood analysis tools are particularly notable — they provide the kind of long-term climate impact data that the weather category previously lacked entirely.

## Aviation Weather (NEW)

A new subcategory that emerged since the initial review — aviation-specific weather data (METAR observations, TAF forecasts, pilot reports, and hazard advisories) is now accessible through several MCP servers.

### blevinstein/aviation-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [blevinstein/aviation-mcp](https://github.com/blevinstein/aviation-mcp) | 9 | TS/JS | MIT | 3 servers |

The **most comprehensive aviation MCP project** — a suite of three MCP servers mapping to FAA and other aviation APIs:

- **Weather server** — METAR (current observations), TAF (terminal forecasts), PIREP (pilot reports), SIGMET (significant meteorological information), G-AIRMET (graphical area forecasts)
- **Charts server** — Sectional charts, TAC, IFR enroute charts, Terminal Procedures Publications (TPP)
- **NOTAMs server** — FAA NOTAM API integration

Additional servers in development for aircraft data, airport information, and precipitation APIs. 9 stars and 88 commits indicate active development. The SIGMET and G-AIRMET tools are unique in the weather MCP ecosystem — no other server exposes hazardous weather advisories for aviation.

### finack/aviation-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [finack/aviation-mcp](https://github.com/finack/aviation-mcp) | 2 | TypeScript | MIT | 4 |

A **focused aviation weather server** — 4 tools: `get-metar` (current observations), `get-taf` (terminal forecasts), `get-pireps` (pilot reports near an airport), and `get-route-weather` (comprehensive weather for routes between two airports). The route weather tool is unique — it provides end-to-end weather briefing for planned flights. Built by a retired corporate pilot. Includes explicit disclaimer: "DO NOT USE THIS TOOL FOR FLIGHT PLANNING OR IN-FLIGHT DECISION MAKING."

### Other Aviation Weather Implementations

| Server | Stars | Language | Tools | Notes |
|--------|-------|----------|-------|-------|
| daedalus/mcp-metar | — | — | 2 | METAR/TAF by ICAO code, released March 2026 |
| mangobanaani/metarmcp | — | Python | 2 | METAR parsing with SQLite caching (30-min TTL) from NOAA Aviation Weather Center |

## AccuWeather Servers

### adhikasp/mcp-weather

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [adhikasp/mcp-weather](https://github.com/adhikasp/mcp-weather) | 32 | Python | Unlicense | 1 |

The **most popular single-API weather MCP server** by star count — 32 stars (up from 29) with a single `mcp-weather` tool providing hourly forecasts (12-hour outlook) using AccuWeather's API. Returns current conditions with temperature, humidity, and precipitation probability. Minimal but well-executed — one of the earlier weather MCP servers that people actually discovered and used, with 29 forks indicating it's frequently used as a starting template.

### TimLukaHorstmann/mcp-weather

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [TimLukaHorstmann/mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather) | — | Python | — | — |

Another AccuWeather-based implementation with hourly and daily forecasts. Similar scope to adhikasp's version.

## Marine & Surf Forecasting

### surf-mcp (Stormglass)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ravinahp/surf-mcp](https://github.com/ravinahp/surf-mcp) | 19 | Python | MIT | 1 |

A **Stormglass API wrapper for tide data** — the `get_tides` tool retrieves high/low tide information with heights and timing for any latitude/longitude coordinates. Designed for surfers (optimal waves arrive about 2 hours before high tide). 19 stars. The same developer also built the popular flights-mcp server (169 stars) for the travel category — a consistent pattern of building practical lifestyle MCP tools.

### Marine Weather in Multi-Source Servers

Both weather-mcp/weather-mcp and cmer81/open-meteo-mcp include marine weather tools (wave height, swell, ocean currents, sea surface temperature) as part of their broader toolsets. For marine-focused use, lucasinocencio1/mcp-surf-forecast provides dedicated surf and swell data from Open-Meteo's Marine API, converting city names to coordinates for surf spot lookups.

## Air Quality, Carbon & Climate

### AQICN MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mattmarcin/aqicn-mcp](https://github.com/mattmarcin/aqicn-mcp) | 1 | Python | MIT | 3 |

A **World Air Quality Index (AQICN.org) integration** — 3 tools: city AQI lookup, coordinate-based AQI lookup, and station search. Returns AQI values, dominant pollutants, station identification, and geographic coordinates. Requires API key. Docker support included.

### Climatiq MCP (Carbon Emissions)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jagan-shanmugam/climatiq-mcp-server](https://github.com/jagan-shanmugam/climatiq-mcp-server) | 8 | Python | MIT | 10 |

The **most comprehensive carbon emission calculation MCP server** — 10 tools across multiple emission domains:

- **Electricity** — carbon output from power consumption
- **Travel** — vehicle, plane, or rail journey emissions
- **Cloud computing** — digital infrastructure carbon footprint
- **Freight** — cargo transportation emissions
- **Procurement** — purchasing-related emissions
- **Hotel** — lodging carbon footprint
- **Travel spend** — expense-based emission estimates
- **Search emission factors** — query Climatiq's factor database
- **Custom calculation** — use specific emission factors

Includes a `climate-impact-explanation` prompt for generating natural language summaries. Resources use `climatiq://calculation/{id}` URI scheme. Requires Climatiq API key. 8 stars. This server is equally relevant to the [Energy & Utilities](/reviews/energy-utilities-mcp-servers/) category, where we also cover it.

### MeasureSpace MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MeasureSpace/measure-space-mcp-server](https://github.com/MeasureSpace/measure-space-mcp-server) | 3 | TS/Python | Apache-2.0 | 7 |

A **multi-service weather and environmental platform** — 7 tools covering hourly weather (5 days), daily weather (15 days), 9-month climate forecast, air quality (4 days), **agriculture** (growing degree days, crop growth stage, heat/frost stress), **pollen** (5-day daily forecast), and geocoding with astronomy data (sunrise/sunset). The agriculture and pollen tools are unique in the weather MCP ecosystem — no other server provides crop growth modeling or pollen forecasting. Requires separate API keys per service.

### Visual Crossing MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [peterjohnbeck/visual_crossing_mcp](https://github.com/peterjohnbeck/visual_crossing_mcp) | 1 | Python | GPL-3.0 | 1 |

A **historical weather data server** using Visual Crossing's Timeline Weather API — retrieves temperature, precipitation, solar radiation, cloud cover, snow depth, heat index, and wind chill. Minimal adoption (1 star, 3 commits) but fills the historical weather niche for users who need a different data source than Open-Meteo's archive.

## Natural Disaster Monitoring

### USGS Earthquake MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [blake365/usgs-quakes-mcp](https://github.com/blake365/usgs-quakes-mcp) | 1 | JS/TS | MIT | 2 |

A **USGS Earthquake API integration** — 2 tools: `find-earthquakes` (search by magnitude, location bounds, time range) and `find-earthquake-details` (comprehensive metadata for specific events). Supports natural language queries like "find earthquakes over 2 magnitude in Florida over the last 20 years." Docker support. Low adoption but accesses authoritative USGS data.

### ClimateTriage MCP

Available via PulseMCP — connects to the ClimateTriage API for searching open-source climate change and sustainability projects across GitHub. More of a developer tool than a weather data tool, but notable for bridging AI agents to the climate tech open-source community.

## What's Missing

Weather is one of the most populated MCP categories, but significant gaps remain:

- **No official government weather service MCP servers** — neither NOAA, Met Office, DWD, JMA, nor any other national meteorological agency has released an official MCP server (though NOAA data is well-served by community implementations like RyanCardin15's Tides & Currents server and weather-mcp's NWS integration)
- **No severe weather model output** — HRRR (High-Resolution Rapid Refresh), NAM, RAP, and other numerical weather prediction model grids are not accessible via MCP
- **No historical reanalysis** — ERA5 (ECMWF's reanalysis dataset, the gold standard for historical climate research) has no MCP server
- **No tropical cyclone tracking** — no dedicated hurricane/typhoon tracking or forecast cone data
- **No avalanche or snow forecasting** — no integration with avalanche centers or snowpack models
- **No wildfire smoke forecasting** — HRRR-Smoke and BlueSky models are not exposed
- **No weather station hardware** — no integration with personal weather stations (Davis, Ecowitt, Ambient Weather) or WeatherUnderground's personal station network
- **No insurance/actuarial weather risk** — no cat modeling (RMS, AIR, CoreLogic) or parametric weather insurance data
- **No agricultural weather beyond MeasureSpace** — no evapotranspiration models, irrigation scheduling, or crop-specific degree-day calculations (though these exist in the [Agriculture & Farming](/reviews/agriculture-farming-mcp-servers/) category)
- **Heavy duplication of basic implementations** — at least 15 servers provide near-identical "current weather + 5-day forecast" functionality
- ~~No aviation weather~~ — **FILLED**: blevinstein/aviation-mcp now provides METAR, TAF, PIREP, SIGMET, and G-AIRMET data
- ~~No NOAA tides/oceanographic data~~ — **FILLED**: RyanCardin15/NOAA-TidesAndCurrents-MCP provides 25+ tools for water levels, tides, currents, sea level trends, and flood analysis

## The Bottom Line

Weather & Climate MCP servers hold at **3.5 out of 5**. The category has impressive breadth — cmer81/open-meteo-mcp's 19 tools spanning 7 national weather models and CMIP6 climate projections are genuinely useful for meteorological research (now 41 stars, up 14%), while weather-mcp/weather-mcp's multi-source approach covering forecasts through wildfire tracking demonstrates the potential for comprehensive environmental monitoring (doubled to 6 stars). The free and open nature of the ecosystem is a strength: multiple servers require zero API keys, making weather one of the most accessible MCP categories for getting started.

Since the initial review, two notable gaps have been filled. **RyanCardin15/NOAA-TidesAndCurrents-MCP** (25+ tools) brings comprehensive oceanographic data — water levels, tide predictions, currents, sea level trends, flood analysis, and astronomy — providing the kind of long-term climate impact data the category previously lacked. **Aviation weather emerged as a new subcategory** with blevinstein/aviation-mcp (9 stars) delivering METAR, TAF, PIREP, SIGMET, and G-AIRMET data plus aeronautical charts and NOTAMs — professional-grade aviation weather that no other weather MCP server provides.

But the fundamental challenges persist: significant duplication (dozens of near-identical basic weather servers), a wide gap between simple forecast tools and serious meteorological or climate science needs, no numerical weather prediction model grids, no reanalysis datasets, no tropical cyclone tracking, and no official government agency servers. For most users, cmer81/open-meteo-mcp or weather-mcp/weather-mcp will cover their needs completely — the challenge is knowing which of the 30+ servers to choose, since most of the others offer strictly less functionality.

*This review was refreshed on 2026-04-27 using Claude Opus 4.6 (Anthropic). Initial review published 2026-03-15.*

