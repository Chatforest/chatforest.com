---
title: "Transportation & Mobility MCP Servers — Public Transit, Flight Tracking, Ride-Hailing, Aviation Data, and Smart City Transport"
date: 2026-03-16T11:00:00+09:00
description: "Transportation and mobility MCP servers let AI agents access real-time public transit arrivals, track flights, book rides, query aviation data, and tap into smart city transport"
og_description: "Transportation & mobility MCP servers: 12306-mcp (799 stars, Chinese rail), ns-mcp-server (53 stars, Dutch Railways), Flightradar24 (46 stars), indian-railway-mcp (28 stars), variflight-mcp (26 stars), aviationstack-mcp (20 stars). Universal GTFS MCP (any transit system). Maritime vessel tracking via MarineTraffic. 15+ city/country transit servers across 5 continents. 30+ servers reviewed. Rating: 4/5."
content_type: "Review"
categories: ["/categories/logistics-industry/"]
card_description: "Transportation and mobility MCP servers for real-time public transit, flight tracking, ride-hailing, aviation data, maritime tracking, and smart city transport. This category covers the infrastructure that moves people — not trip planning (see [Travel & Tourism](/reviews/travel-tourism-mcp-servers/)), not maps/routing (see [Geospatial & Mapping](/reviews/geospatial-mapping-mcp-servers/)), not vehicle control (see [Automotive & Vehicle](/reviews/automotive-vehicle-mcp-servers/)). **Rail went global with 12306-mcp leading at 799 stars** — Joooook/12306-mcp is the most popular transport MCP server by far, providing Chinese rail ticket search via the 12306 platform (82 commits, MIT). Indian Railway MCP (28 stars, 8 tools including live train status and seat availability), Dutch Railways ns-mcp-server (53 stars, real-time schedules + pricing + disruptions), and Swiss Railways sbb-mcp (ticket prices with Half-Fare/GA support) bring rail coverage to four continents. **A universal GTFS MCP server finally exists** — jdamcd/gtfs-mcp (TypeScript, MIT) works with ANY GTFS-compatible transit system, combining GTFS static schedules with GTFS-RT realtime feeds. It has 10+ tools including stop search, arrivals, routes, alerts, and vehicle positions. Pre-configured for NYC Subway but extensible to any agency via the Mobility Database. This fills the biggest gap from the previous review. **City-specific transit spans five continents** — 15+ servers cover NYC (metro-mcp unified with DC, 13 tools on Cloudflare Workers), Berlin (VBB API), Munich (MVG), Seattle (OneBusAway), Singapore (LTA DataMall), Hong Kong (KMB bus + transport ETA), DC (WMATA), Caltrain, Sydney/NSW (real-time alerts across 8 transport modes), and Vilnius. mirodn/mcp-server-public-transport (7 stars, 66 commits) expanded to 5 European regions adding Berlin/Brandenburg. **Flight tracking added Variflight (26 stars)** — variflight/variflight-mcp provides 8 tools including comfort index, real-time aircraft tracking, pricing data, and itinerary planning. Flightradar24 (46 stars) remains the most popular pure tracker. aviationstack-mcp grew to 20 stars with v1.6.0. aviation-mcp reached 9 stars and 88 commits with FAA-level weather/charts/NOTAMs. **Maritime tracking gap partially filled** — Cyreslab-AI/marinetraffic-mcp-server (9 stars) provides vessel position tracking, vessel search, and area monitoring via MarineTraffic API. Previously zero maritime coverage existed. **Ride-hailing still only Uber** — mcp-uber (11 stars) remains the sole ride-hailing MCP server. **Remaining gaps** — no GBFS micromobility (scooters/bikeshare), no freight/trucking, no multimodal journey planning, no parking availability. The category earns **4/5** — up from 3.5 — thanks to the universal GTFS server, rail going global (China 799 stars, India, Netherlands, Switzerland), maritime tracking appearing, and Australia joining the transit coverage. 30+ servers now span five continents."
last_refreshed: 2026-04-30
---

Transportation and mobility MCP servers connect AI agents to the systems that move people — real-time bus and train arrivals, flight tracking, ride-hailing, aviation weather data, and smart city transport networks. Instead of switching between transit apps, flight trackers, and traffic dashboards, these servers let you query transportation data through natural language via the Model Context Protocol.

This review covers **transportation and mobility** — public transit schedules and arrivals, flight tracking and monitoring, ride-hailing integration, aviation data (weather, NOTAMs, charts), and smart city transport systems. For trip planning and flight search/booking, see our [Travel & Tourism review](/reviews/travel-tourism-mcp-servers/). For maps, routing, and geospatial tools, see our [Geospatial & Mapping review](/reviews/geospatial-mapping-mcp-servers/). For vehicle control and diagnostics, see our [Automotive & Vehicle review](/reviews/automotive-vehicle-mcp-servers/).

The headline findings: **12306-mcp (799 stars) for Chinese rail is the most popular transport MCP by far** — rail went global with servers for China, India, Netherlands, and Switzerland. **A universal GTFS MCP server finally exists** — jdamcd/gtfs-mcp works with any GTFS-compatible transit system, combining static schedules and real-time feeds. **City-specific transit now spans five continents** with 15+ servers including new entries for Australia (NSW) and Lithuania. **Maritime vessel tracking appeared** via Cyreslab-AI/marinetraffic-mcp-server (9 stars). **Variflight (26 stars) joined flight tracking** with 8 tools including comfort index and pricing. **Uber remains the only ride-hailing MCP** (now 11 stars).

---

## Universal Transit

### jdamcd/gtfs-mcp — Universal GTFS Transit Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gtfs-mcp](https://github.com/jdamcd/gtfs-mcp) | 0 | TypeScript | MIT | 10+ |

**The universal GTFS MCP server the category has been waiting for** — works with ANY GTFS-compatible transit system by combining GTFS static schedules with GTFS-RT realtime feeds:

- **list_systems, search_stops, find_nearby_stops, get_stop** — discover and query transit stops for any configured system
- **get_arrivals** — real-time arrival predictions overlaid on scheduled times with delay information
- **list_routes, get_route** — route details and patterns
- **get_alerts** — service alert filtering by route or stop
- **get_vehicles** — live vehicle position tracking
- **get_trip, get_system_status** — trip details and overall system health

GTFS static data is downloaded as a ZIP and imported into a local SQLite database (auto-refreshes). GTFS-RT feeds are fetched on demand with 30-second caching. Pre-configured for NYC Subway (MTA), but extensible to any agency via the [Mobility Database](https://mobilitydatabase.org/) — including MBTA Boston, VBB Berlin, and hundreds more. Requires Node.js 22+.

This fills the single biggest gap identified in the previous review: every city no longer needs its own MCP server.

---

## National Rail Systems

### Joooook/12306-mcp — Chinese Rail (12306)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [12306-mcp](https://github.com/Joooook/12306-mcp) | 799 | JavaScript | MIT | 4 |

**The most popular transport MCP server by far** — provides Chinese railway ticket search through the 12306 platform (China's national rail booking system):

- **Ticket search** — query available trains between stations on specific dates
- **Train data filtering** — filter by train type, departure time, duration
- **Station passage search** — find trains passing through specific stations
- **Transfer route queries** — discover multi-leg routing options

799 stars and 82 commits make this the dominant transport MCP. Supports CLI via stdio or HTTP modes, Docker deployment, and direct MCP server configuration. Marked as "for learning purposes only" (仅用于学习).

### r-huijts/ns-mcp-server — Dutch Railways (NS)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ns-mcp-server](https://github.com/r-huijts/ns-mcp-server) | 53 | TypeScript | MIT | Multiple |

**Comprehensive Dutch Railways integration** — connects to the official NS API for real-time train travel information:

- **Real-time schedules** — departures and arrivals with platform and delay information
- **Journey planning** — route planning with alternatives
- **Pricing** — fare information across travel classes and passenger groups
- **Station details** — accessibility features and facility information
- **Disruption alerts** — service disruptions and engineering works
- **Multi-language** — Dutch and English support

53 stars and 46 commits make this one of the highest-starred transit MCP servers. Requires NS API key. Available via NPM or Smithery.

### amith-vp/indian-railway-mcp — Indian Railway

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [indian-railway-mcp](https://github.com/amith-vp/indian-railway-mcp) | 28 | TypeScript | — | 8 |

**Comprehensive Indian Railways data** with eight tools:

- **search-trains** — find available trains between stations on specific dates
- **get-seat-availability** — occupancy status across classes and dates
- **get-train-info** — comprehensive train details, routes, and schedules
- **get-train-live-status** — real-time position and delay information
- **get-train-delay-info** — historical average delays by station
- **get-live-station-info** — current train movements at stations
- **get-station-code / get-train-code** — lookup tools

Connects via remote endpoint. 28 stars and growing. A second Indian Railways server (rajprem4214/indian-railways-mcp) also exists with real-time station status.

### Fabsbags/sbb-mcp — Swiss Federal Railways (SBB/CFF/FFS)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sbb-mcp](https://github.com/Fabsbags/sbb-mcp) | 0 | JavaScript | Proprietary | 8 |

**Swiss Railways with ticket pricing** — 8 tools covering station search, train schedules, detailed trip info, and price lookups with Half-Fare (Halbtax) and GA travelcard support. Includes direct ticket purchase links to SBB.ch. Rebranded to swisstrip-mcp (hosted at mcp.swisstrip.app). Family pricing calculations for multi-traveler groups.

---

## Public Transit

### mirodn/mcp-server-public-transport — Multi-Country European Transit

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-public-transport](https://github.com/mirodn/mcp-server-public-transport) | 7 | Python | MIT | Multiple |

**Multi-country transit MCP server** — now covers **five European regions**: UK, Switzerland, Norway, Belgium, and Berlin/Brandenburg (new). 66 commits show steady development:

- **Train connections** — search for rail connections across multiple European countries
- **Live departures** — real-time departure boards for stations
- **Bus locations** — track bus positions in supported regions
- **Berlin/Brandenburg** — location searches, live departures/arrivals, journey planning, and nearby station finding via VBB API (new)
- **Multi-API integration** — handles authentication and rate limiting across different national transport APIs

Requires API keys for the UK Transport API. Other country APIs may have their own authentication requirements.

### aarekaz/metro-mcp — Unified US Metro (NYC + DC)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [metro-mcp](https://github.com/aarekaz/metro-mcp) | 3 | TypeScript | MIT | 13 |

**First multi-city US transit server** — combines Washington DC Metro (WMATA) and NYC Subway (MTA) in one server with 13 tools:

- **Universal tools** — real-time station predictions, station search, line info, service alerts, station listings
- **DC Metro exclusive** — elevator/escalator outages, bus predictions/routes, live bus and train positions
- **NYC Subway exclusive** — station transfer connections with walk times (87 transfer stations), express/local patterns, platform directional guidance

Deployed on Cloudflare Workers with OAuth 2.1 + PKCE authentication. Public instance available. 49 commits.

### City-Specific Transit Servers

| Server | City/Region | API | Language |
|--------|-------------|-----|----------|
| [scottmlikens/kingcountytransit-mcp](https://github.com/scottmlikens/kingcountytransit-mcp) | Seattle / Puget Sound | OneBusAway | — |
| [harshil1712/berlin-transport-mcp](https://github.com/harshil1712/berlin-transport-mcp) | Berlin | VBB API | TypeScript |
| [anisul/muc-mcp-server](https://github.com/anisul/muc-mcp-server) | Munich | MVG API | — |
| [davidyen1124/caltrain-mcp](https://github.com/davidyen1124/caltrain-mcp) | SF Bay Area (Caltrain) | GTFS static | — |
| [arjunkmrm/sg-lta-mcp](https://github.com/arjunkmrm/sg-lta-mcp) | Singapore | LTA DataMall | — |
| [kennyckk/mcp_hkbus](https://github.com/kennyckk/mcp_hkbus) | Hong Kong | KMB / Long Win Bus | — |
| [kennyfong19931/mcp-hk-transport-eta](https://github.com/kennyfong19931/mcp-hk-transport-eta) | Hong Kong | Multi-transport ETA | JavaScript |
| [nathanielnoyd/metro-mcp](https://github.com/nathanielnoyd/metro-mcp) | Washington, DC | WMATA API | — |
| [sasabasara/where_is_my_train_mcp](https://github.com/sasabasara/where_is_my_train_mcp) | New York City | MTA GTFS + location | — |
| [piddlingtuna/tfnsw-realtime-alerts-mcp-server](https://github.com/piddlingtuna/tfnsw-realtime-alerts-mcp-server) | Sydney / NSW, Australia | TfNSW API | JavaScript |
| [sarunasdaujotis/vilnius-transport-mcp-server](https://github.com/sarunasdaujotis/vilnius-transport-mcp-server) | Vilnius, Lithuania | City API | Python |

**Notable implementations:**

- **tfnsw-realtime-alerts-mcp-server** (Sydney/NSW) — **Australia's first transit MCP**, providing real-time transport alerts across 8 modes: buses, ferries, light rail, metro, NSW trains, regional buses, and Sydney trains. 7 stars
- **metro-mcp** (DC) — WMATA API for DC Metro schedules and alerts
- **kingcountytransit-mcp** (Seattle) — integrates with OneBusAway, a popular open-source transit platform used by multiple US cities
- **berlin-transport-mcp** — accesses Berlin's VBB (Verkehrsverbund Berlin-Brandenburg) covering S-Bahn, U-Bahn, trams, buses, and regional trains
- **muc-mcp-server** (Munich) — real-time MVG departures for Munich's U-Bahn, S-Bahn, trams, and buses
- **sg-lta-mcp** (Singapore) — connects to Singapore's Land Transport Authority DataMall for real-time data across MRT, buses, and traffic
- **mcp_hkbus** (Hong Kong) — real-time KMB and Long Win Bus route information and arrival times
- **mcp-hk-transport-eta** (Hong Kong) — second HK server focusing on ETA across multiple transport modes
- **vilnius-transport-mcp-server** (Lithuania) — stop search and nearest stop by coordinates

The geographic spread now covers **five continents** — Asia (Singapore, Hong Kong, India, China), Europe (Berlin, Munich, UK, Switzerland, Norway, Belgium, Netherlands, Lithuania), North America (NYC, Seattle, DC, Bay Area), Oceania (Sydney/NSW), and the universal GTFS server can reach any remaining agency.

---

## Flight Tracking

### sunsetcoder/flightradar24-mcp-server — Real-Time Flight Tracking

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server) | 46 | Python | — | Multiple |

**The most popular flight tracking MCP server** — provides real-time flight data using Flightradar24 as the data source:

- **Track any flight** in real-time by flight number or aircraft registration
- **Airport activity** — view arrivals and departures for any airport
- **Emergency monitoring** — track flights squawking emergency codes
- **Arrival/departure times** — get scheduled and actual times for specific flights

Lightweight and easy to set up — ideal for aviation enthusiasts, travel planners, or monitoring flights overhead. No API key required (uses the Flightradar24 data layer).

### variflight/variflight-mcp — Flight Info, Weather & Comfort Metrics

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [variflight-mcp](https://github.com/variflight/variflight-mcp) | 26 | JavaScript | ISC | 8 |

**Feature-rich flight data from Variflight** — 8 tools covering flight search, tracking, comfort, and pricing:

- **Flight search by route** — query direct flights using city or airport codes
- **Flight number lookup** — find specific flights by number and date
- **Transfer/connecting flights** — discover multi-leg routing options
- **Comfort index** — punctuality, aircraft type, cabin configuration, meals, and entertainment
- **Real-time aircraft tracking** — locate aircraft by registration number
- **Weather forecasting** — three-day airport forecasts
- **Itinerary planning** — natural-language summary with recommended options, lowest price, shortest duration
- **Pricing data** — cabin-level prices between two cities

Requires API key from mcp.variflight.com. 26 stars. The comfort index is unique — no other flight MCP rates the passenger experience.

### Pradumnasaraf/aviationstack-mcp — Airline & Airport Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aviationstack-mcp](https://github.com/Pradumnasaraf/aviationstack-mcp) | 20 | Python | MIT | Multiple |

**Comprehensive aviation data via the AviationStack API** — now at 20 stars and 38 commits with v1.6.0:

- **Airline flights** — search flights by airline, route, or specific flight number
- **Airport schedules** — arrival and departure schedules for any airport
- **Future flights** — look up upcoming scheduled flights
- **Aircraft types** — reference data for aircraft models and types
- **Historical data** — search past flights by date with airline and airport filters

Uses the AviationStack API (API key required, free tier available). Steady growth from unlisted to 20 stars.

### mikedarke/mcp-server-flight-aware-aeroapi — FlightAware Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-flight-aware-aeroapi](https://github.com/mikedarke/mcp-server-flight-aware-aeroapi) | — | — | — | Multiple |

**Professional-grade flight data via FlightAware's AeroAPI** — the aviation industry's most trusted tracking service:

- **Real-time flight positions** — GPS-accurate tracking data
- **Flight status and delays** — departure, en-route, arrival, and diversion information
- **Airport information** — delays, weather, and runway conditions
- **Search capabilities** — find flights by airline, aircraft, or route

FlightAware AeroAPI is a paid service used by airlines and aviation professionals. This MCP server brings that data to AI agents.

### Cyreslab-AI/flightradar-mcp-server — Alternative FR24 Implementation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [flightradar-mcp-server](https://github.com/Cyreslab-AI/flightradar-mcp-server) | — | — | — | Multiple |

An alternative Flightradar24 MCP implementation. Provides similar real-time flight tracking capabilities to sunsetcoder's version.

---

## Aviation Data

### blevinstein/aviation-mcp — FAA Weather, NOTAMs, and Charts

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aviation-mcp](https://github.com/blevinstein/aviation-mcp) | 9 | TypeScript | — | Multiple |

**Deep FAA data access** — now at 9 stars and 88 commits. A suite of MCP servers mapping directly to FAA and aviation APIs:

- **Aviation weather** — METAR (current conditions), TAF (forecasts), PIREP (pilot reports), SIGMET (significant meteorological info), G-AIRMET (graphical AIRMETs). Includes geo-referenced data. **No API key needed**
- **Charts** — sectional charts, TAC (Terminal Area Charts), IFR enroute charts, and TPP (Terminal Procedures Publication). **No API key needed**
- **NOTAMs** (Notices to Air Missions) — requires FAA client ID and secret for authentication
- **Planned: Airspace data** — machine-readable airspace boundaries

This is the most specialized aviation MCP server — built for pilots, flight planners, and aviation weather enthusiasts rather than casual flight trackers. The no-API-key requirement for weather and charts makes it immediately accessible.

---

## Ride-Hailing

### 199-mcp/mcp-uber — Uber Ride Booking

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-uber](https://github.com/199-mcp/mcp-uber) | 11 | TypeScript | — | Multiple |

**The only ride-hailing MCP server** — enables AI assistants to book Uber rides through OAuth 2.0 authentication:

- **Price estimates** — get fare estimates before booking
- **Request rides** — book Uber rides through natural language
- **Ride status** — track ongoing ride progress
- **Cancellation** — cancel rides when needed

Setup requires Uber Developer Dashboard credentials (UBER_CLIENT_ID, UBER_CLIENT_SECRET, UBER_REDIRECT_URI). **Important:** the request scope is privileged — works in development without approval, but production use requires Uber's authorization.

Notable absence: **no Lyft, Grab, Bolt, DiDi, or other ride-hailing MCP servers exist**. Given Uber's developer API ecosystem, this single server highlights how much untapped potential remains in the ride-hailing space.

---

## Maritime & Vessel Tracking

### Cyreslab-AI/marinetraffic-mcp-server — MarineTraffic Vessel Tracking

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [marinetraffic-mcp-server](https://github.com/Cyreslab-AI/marinetraffic-mcp-server) | 9 | TypeScript | ISC | 4 |

**The first maritime MCP server** — fills the previously empty maritime tracking gap with MarineTraffic API integration:

- **get_vessel_position** — real-time vessel location via MMSI or IMO number
- **get_vessel_details** — comprehensive vessel information
- **search_vessels** — query by name, MMSI, IMO, or vessel type
- **get_vessels_in_area** — find all vessels in a specified geographic area

Requires MarineTraffic API key. Available via Smithery for Claude Desktop. 9 stars and 4 forks show real interest. Resource URIs (`vessel://`, `vessels://area/`) provide direct data access.

---

## Smart City Transport

### sosanzma/SmartCityMCP — Valencia Real-Time Transport Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SmartCityMCP](https://github.com/sosanzma/SmartCityMCP) | — | Python | — | Multiple |

**The first smart city transport MCP server** — provides real-time urban mobility data from Valencia, Spain:

- **Traffic status** — real-time traffic conditions and incidents
- **Bike-sharing** — station availability and bike counts (Valencia's Valenbisi system)
- **Air quality** — pollution monitoring data
- **Weather** — current conditions and forecasts

Demonstrates the concept of city-as-a-platform for AI agents — combining multiple urban data sources into one MCP interface. Currently Valencia-only, but the architecture could be replicated for any city with open data APIs.

---

## What's Missing

The transportation and mobility MCP space has shrunk its gap list significantly but notable holes remain:

- **No GBFS micromobility server** — the General Bikeshare Feed Specification covers dockless scooters, bikeshare, mopedshare, and carshare worldwide, but no MCP server consumes it
- ~~**No universal GTFS-realtime parser**~~ — **FILLED**: jdamcd/gtfs-mcp now works with any GTFS-compatible transit system
- ~~**No maritime or shipping tracking**~~ — **PARTIALLY FILLED**: marinetraffic-mcp-server provides vessel tracking, but port schedules and container tracking still missing
- **No freight or trucking dispatch** — despite TMS platforms having APIs
- **No multimodal journey planning** — no server combines transit + rideshare + bike into unified trip options
- **No parking availability** — real-time parking data exists in many cities but has no MCP server
- **No traffic signal management** — smart traffic infrastructure is entirely absent
- **Single ride-hailing vendor** — still only Uber, no Lyft/Grab/Bolt/DiDi

---

## Bottom Line

Transportation and mobility MCP servers earn **4 out of 5** — up from 3.5 in the previous review. The category has transformed in 45 days with three major developments:

**Rail went global.** 12306-mcp (799 stars) for Chinese rail is now the most popular transport MCP by far. Dutch Railways (53 stars), Indian Railway (28 stars), and Swiss Federal Railways bring national rail coverage to four continents. Rail is now the deepest subcategory.

**The universal GTFS server arrived.** jdamcd/gtfs-mcp works with any GTFS-compatible transit system, combining static schedules and realtime feeds. This was the single biggest gap in the previous review — the "every city needs its own server" problem now has a solution.

**Maritime tracking appeared.** Cyreslab-AI/marinetraffic-mcp-server (9 stars) fills another previously empty gap with vessel position tracking, search, and area monitoring.

City-specific transit now spans five continents with 15+ servers. Flight tracking added Variflight (26 stars, 8 tools including a unique comfort index) alongside the established Flightradar24 (46 stars) and growing aviationstack-mcp (20 stars). Aviation data goes deep with FAA-level weather, NOTAMs, and charts (9 stars, 88 commits).

The remaining weaknesses: micromobility (GBFS scooters/bikeshare) is still completely absent, ride-hailing still has only Uber, and multimodal journey planning doesn't exist. But the trajectory is clear — this category went from fragmented city projects to a genuinely global transportation intelligence layer for AI agents.

*This review was refreshed on 2026-04-30 using Claude Opus 4.6 (Anthropic).*
