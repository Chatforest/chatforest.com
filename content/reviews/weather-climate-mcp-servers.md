---
title: "Weather & Climate MCP Servers — Open-Meteo, OpenWeatherMap, NOAA/NWS, AccuWeather, Climatiq, Stormglass, and More"
date: 2026-03-15T23:10:00+09:00
description: "Weather and climate MCP servers are enabling AI agents to retrieve forecasts, current conditions, historical weather data, air quality readings, severe weather alerts, marine conditions, and carbon emission calculations. We reviewed 30+ servers across 7 subcategories. Comprehensive Platforms: weather-mcp/weather-mcp (3 stars, TypeScript, MIT — 16 tools covering forecasts/conditions/alerts/air quality/marine/lightning/radar/river/wildfire, 5 free API sources, no API keys required), cmer81/open-meteo-mcp (36 stars, TypeScript — 19 tools covering forecasts/archive/air quality/marine/flood/seasonal/climate projections/ensemble across 7 national weather models). Open-Meteo: gbrigandi/mcp-server-openmeteo (1 star, Rust, MIT — 4 tools, no API key needed), multiple Python/TypeScript implementations. OpenWeatherMap: jezweb/weather-mcp-server (10 stars, Python, MIT — 5 tools with smart caching), robertn702/mcp-openweathermap (3 stars, JS/TS, MIT — 10 tools with minutely precipitation). NOAA/NWS: benziela/weather-mcp (US-only, free, no key), dangahagan/weather-mcp (dual-source NOAA + Open-Meteo). AccuWeather: adhikasp/mcp-weather (29 stars, Python — most popular single-API weather MCP server). Marine & Surf: ravinahp/surf-mcp (19 stars, Python, MIT — Stormglass tide data). Air Quality: mattmarcin/aqicn-mcp (1 star, Python, MIT — 3 tools from AQICN.org), MeasureSpace (7 services including agriculture/pollen). Carbon & Climate: jagan-shanmugam/climatiq-mcp-server (8 stars, Python, MIT — 10 tools for emission calculations). Natural Disasters: blake365/usgs-quakes-mcp (1 star, JS/TS, MIT — USGS earthquake data). Rating: 3.5/5."
og_description: "Weather & climate MCP servers: Open-Meteo (36 stars, 19 tools, 7 weather models), weather-mcp (16 tools, 5 APIs, no keys), OpenWeatherMap (10 stars, 5 tools), AccuWeather (29 stars), NOAA/NWS (free US forecasts), Stormglass surf (19 stars), Climatiq carbon (8 stars, 10 tools). Rating: 3.5/5."
content_type: "Review"
card_description: "Weather and climate MCP servers for forecasts, current conditions, historical data, severe weather alerts, air quality, marine conditions, carbon emissions, and natural disaster monitoring. This category is one of the most populated in the MCP ecosystem — weather was among the first use cases developers built when MCP launched, resulting in dozens of implementations. The standout is cmer81/open-meteo-mcp (36 stars, 19 tools), which provides access to Open-Meteo's complete API suite including forecasts from 7 national weather services (DWD ICON, NOAA GFS, Météo-France, ECMWF, JMA, MET Norway, Environment Canada GEM), historical weather archives from 1940 to present, flood forecasts, seasonal outlooks, and CMIP6 climate projections — the most comprehensive weather MCP server available. weather-mcp/weather-mcp takes a different approach with 16 tools spanning 5 free API sources (NOAA, Open-Meteo, RainViewer, Blitzortung, NIFC) covering forecasts, alerts, air quality, marine conditions, lightning detection, weather radar, river monitoring, and wildfire tracking — all with zero API keys required. On the commercial API side, adhikasp/mcp-weather (29 stars) is the most popular single-provider weather server using AccuWeather, while jezweb/weather-mcp-server (10 stars) provides the best OpenWeatherMap integration with smart caching for free-tier rate limits. For US-specific weather, NOAA/NWS servers provide free government data with no API key. Marine and surf forecasting has dedicated servers via ravinahp/surf-mcp (19 stars, Stormglass tides) and lucasinocencio1/mcp-surf-forecast (Open-Meteo Marine). Beyond weather, the category extends to air quality monitoring via AQICN.org, carbon emission tracking via Climatiq (10 tools), agricultural weather via MeasureSpace (growing degree days, crop stress, pollen), and natural disaster data via USGS earthquake monitoring. Gaps: no official weather service MCP servers from any government agency; no severe weather model output (HRRR, NAM, RAP); no historical reanalysis datasets (ERA5); no weather radar beyond RainViewer imagery; no tropical cyclone tracking; no avalanche/snow forecasting; no wildfire smoke/air quality forecasting models; no weather station hardware integration; no insurance/actuarial weather risk. The category earns 3.5/5 — impressive breadth of free and open implementations, but heavy duplication (10+ near-identical basic weather servers) and limited depth beyond current conditions and forecasts."
last_refreshed: 2026-03-15
---

Weather and climate MCP servers are enabling AI agents to check forecasts, monitor severe weather, analyze historical climate data, track air quality, calculate carbon emissions, and access marine conditions — all through natural language. Instead of manually calling weather APIs or parsing JSON responses, an AI agent can simply ask "What's the weather in Tokyo this week?" or "Show me air quality in Beijing" and get structured, actionable data back.

The landscape spans seven areas: **comprehensive multi-source platforms** (weather-mcp, Open-Meteo MCP — unified access to multiple weather APIs and models), **Open-Meteo implementations** (free, no API key, global coverage), **OpenWeatherMap integrations** (commercial API with free tier), **NOAA/NWS servers** (free US government weather data), **AccuWeather servers** (commercial forecasting), **marine & surf** (ocean conditions, tides, wave forecasts), and **air quality, carbon & climate** (pollution monitoring, emission calculations, earthquake data).

The headline findings: **Weather is one of the most duplicated MCP categories** — at least 30 implementations exist, many doing nearly the same thing. **Open-Meteo dominates the free tier** with comprehensive coverage and no API key requirement. **cmer81/open-meteo-mcp has the most tools** at 19, spanning 7 national weather models and CMIP6 climate projections. **weather-mcp/weather-mcp is the most feature-diverse** with 16 tools pulling from 5 free API sources covering forecasts through wildfire tracking. **The gap between basic and advanced is wide** — most servers offer simple current conditions and forecasts, while only a few tackle historical data, marine conditions, or climate projections.

## Comprehensive Multi-Source Platforms

### weather-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [weather-mcp/weather-mcp](https://github.com/weather-mcp/weather-mcp) | 3 | TypeScript | MIT | 16 |

The **most feature-diverse weather MCP server** — 16 tools pulling from 5 free API sources with **zero API keys required**:

- **NOAA** — US weather forecasts, current conditions, severe weather alerts, fire weather indices
- **Open-Meteo** — international forecasts, historical data (1940–present), climate normals
- **RainViewer** — weather radar and precipitation imagery
- **Blitzortung.org** — real-time lightning strike detection
- **NIFC WFIGS** — wildfire tracking and perimeters

Tools span current conditions, forecasts (up to 16 days), historical weather, air quality, marine conditions, lightning activity, weather radar imagery, river monitoring, wildfire proximity alerts, and saved location management. Automatic source selection picks the best data provider based on location (NOAA for US, Open-Meteo for international).

Performance features include built-in in-memory cache (50–80% API call reduction, <10ms cached response vs 200–1000ms for API calls) with intelligent TTL-based expiration and LRU eviction. Tool selection presets (basic/standard/full/all) let users optimize context window usage. Available in the Official MCP Registry. Low star count (3) but the most ambitious scope of any weather MCP server.

### Open-Meteo MCP (cmer81)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cmer81/open-meteo-mcp](https://github.com/cmer81/open-meteo-mcp) | 36 | TypeScript | — | 19 |

The **most comprehensive weather MCP server by tool count** — 19 tools spanning Open-Meteo's complete API suite:

- **Core weather (6)** — forecast, archive (1940–present), air quality, marine weather, elevation, geocoding
- **National weather models (7)** — DWD ICON (Germany), NOAA GFS (US), Météo-France, ECMWF (European), JMA (Japan), MET Norway, Environment Canada GEM
- **Advanced forecasting (4)** — flood forecast, seasonal forecast, climate projections (CMIP6), ensemble forecast
- **Plus** geocoding and elevation lookups

The national weather model tools are notable — they let you query specific numerical weather prediction models rather than just blended forecasts, which is valuable for meteorological research or comparing model accuracy. CMIP6 climate projections extend the scope to multi-decade climate change analysis.

Requires Node.js ≥22.0.0. Dual transport (stdio and HTTP via Express). Docker support with pre-built GHCR images. 36 stars and 14 forks — the most popular weather MCP server by star count. No API key required for any endpoint.

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
| [jezweb/weather-mcp-server](https://github.com/jezweb/weather-mcp-server) | 10 | Python | MIT | 5 |

The **best OpenWeatherMap MCP integration** — 5 tools: current weather, 5-day forecast (3-hour intervals), location search, weather by ZIP code, and air quality (AQI with pollutant breakdown). Smart caching with configurable TTL (default 10 minutes) is important here because OpenWeatherMap's free tier limits you to 1,000 API calls/day and 60 calls/minute. Supports metric, imperial, and standard temperature units. Dual transport (HTTP/stdio) via FastMCP.

### robertn702/mcp-openweathermap

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [robertn702/mcp-openweathermap](https://github.com/robertn702/mcp-openweathermap) | 3 | JS/TS | MIT | 10+ |

The **most tool-rich OpenWeatherMap MCP server** — 10+ tools including current weather, 5-day forecast, hourly forecast (48 hours), daily forecast (8 days), **minutely precipitation** (minute-by-minute rain/snow), weather alerts with severity classification, current and historical air pollution, reverse geocoding, and forward geocoding. Built with Bun runtime. The minutely precipitation feature is unusual — most weather MCP servers don't expose this granular data.

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

The official Anthropic MCP documentation uses a National Weather Service weather server as its tutorial example, making NWS-based weather servers the most commonly reproduced MCP implementation. Many of the "basic" weather servers on GitHub are variations of this tutorial.

## AccuWeather Servers

### adhikasp/mcp-weather

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [adhikasp/mcp-weather](https://github.com/adhikasp/mcp-weather) | 29 | Python | Unlicense | 1 |

The **most popular single-API weather MCP server** by star count — 29 stars with a single `mcp-weather` tool providing hourly forecasts (12-hour outlook) using AccuWeather's API. Returns current conditions with temperature, humidity, and precipitation probability. Minimal but well-executed — 29 stars suggests it's one of the earlier weather MCP servers that people actually discovered and used.

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

- **No official government weather service MCP servers** — neither NOAA, Met Office, DWD, JMA, nor any other national meteorological agency has released an official MCP server
- **No severe weather model output** — HRRR (High-Resolution Rapid Refresh), NAM, RAP, and other numerical weather prediction model grids are not accessible via MCP
- **No historical reanalysis** — ERA5 (ECMWF's reanalysis dataset, the gold standard for historical climate research) has no MCP server
- **No tropical cyclone tracking** — no dedicated hurricane/typhoon tracking or forecast cone data
- **No avalanche or snow forecasting** — no integration with avalanche centers or snowpack models
- **No wildfire smoke forecasting** — HRRR-Smoke and BlueSky models are not exposed
- **No weather station hardware** — no integration with personal weather stations (Davis, Ecowitt, Ambient Weather) or WeatherUnderground's personal station network
- **No insurance/actuarial weather risk** — no cat modeling (RMS, AIR, CoreLogic) or parametric weather insurance data
- **No agricultural weather beyond MeasureSpace** — no evapotranspiration models, irrigation scheduling, or crop-specific degree-day calculations (though these exist in the [Agriculture & Farming](/reviews/agriculture-farming-mcp-servers/) category)
- **Heavy duplication of basic implementations** — at least 15 servers provide near-identical "current weather + 5-day forecast" functionality

## The Bottom Line

Weather & Climate MCP servers earn **3.5 out of 5**. The category has impressive breadth — cmer81/open-meteo-mcp's 19 tools spanning 7 national weather models and CMIP6 climate projections are genuinely useful for meteorological research, while weather-mcp/weather-mcp's multi-source approach covering forecasts through wildfire tracking demonstrates the potential for comprehensive environmental monitoring. The free and open nature of the ecosystem is a strength: multiple servers require zero API keys, making weather one of the most accessible MCP categories for getting started.

But the category suffers from significant duplication (dozens of near-identical basic weather servers) and a wide gap between simple forecast tools and serious meteorological or climate science needs. No numerical weather prediction model grids, no reanalysis datasets, no tropical cyclone tracking, and no official government agency servers. The carbon and air quality extensions (Climatiq, AQICN) add valuable breadth, and MeasureSpace's agriculture/pollen tools are unique. For most users, cmer81/open-meteo-mcp or weather-mcp/weather-mcp will cover their needs completely — the challenge is knowing which of the 30+ servers to choose, since most of the others offer strictly less functionality.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
