# Transportation & Mobility MCP Servers — Public Transit, Flight Tracking, Ride-Hailing, Aviation Data, and Smart City Transport

> Transportation and mobility MCP servers let AI agents access real-time public transit arrivals, track flights, book rides, query aviation data, and tap into smart city transport


Transportation and mobility MCP servers connect AI agents to the systems that move people — real-time bus and train arrivals, flight tracking, ride-hailing, aviation weather data, and smart city transport networks. Instead of switching between transit apps, flight trackers, and traffic dashboards, these servers let you query transportation data through natural language via the Model Context Protocol.

This review covers **transportation and mobility** — public transit schedules and arrivals, flight tracking and monitoring, ride-hailing integration, aviation data (weather, NOTAMs, charts), and smart city transport systems. For trip planning and flight search/booking, see our [Travel & Tourism review](/reviews/travel-tourism-mcp-servers/). For maps, routing, and geospatial tools, see our [Geospatial & Mapping review](/reviews/geospatial-mapping-mcp-servers/). For vehicle control and diagnostics, see our [Automotive & Vehicle review](/reviews/automotive-vehicle-mcp-servers/).

The headline findings: **Public transit is the most active subcategory** with 9+ city-specific servers across three continents — but every city needs its own server since no universal GTFS-realtime parser exists. **Flightradar24 MCP (46 stars) leads flight tracking** with real-time data and emergency monitoring. **Aviation data reaches FAA depth** with METAR, TAF, SIGMET, NOTAMs, and sectional charts. **Uber is the only ride-hailing MCP** — no Lyft, Grab, or Bolt. **Smart city transport is just starting** with one server for Valencia.

---

## Public Transit

### mirodn/mcp-server-public-transport — Multi-Country European Transit

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-public-transport](https://github.com/mirodn/mcp-server-public-transport) | 6 | Python | MIT | Multiple |

**The only multi-country transit MCP server** — integrates APIs from the UK, Switzerland, Norway, and Belgium for cross-border European public transport data:

- **Train connections** — search for rail connections across multiple European countries
- **Live departures** — real-time departure boards for stations
- **Bus locations** — track bus positions in supported regions
- **Multi-API integration** — handles authentication and rate limiting across different national transport APIs

Requires API keys for the UK Transport API. Other country APIs may have their own authentication requirements.

### City-Specific Transit Servers

The most common pattern in transit MCPs: developers build servers for their own city's transit system. Here's the landscape:

| Server | City/Region | API | Language |
|--------|-------------|-----|----------|
| [ckorhonen/mta-mcp](https://github.com/ckorhonen/mta-mcp) | New York City | MTA GTFS-RT | — |
| [scottmlikens/kingcountytransit-mcp](https://github.com/scottmlikens/kingcountytransit-mcp) | Seattle / Puget Sound | OneBusAway | — |
| [harshil1712/berlin-transport-mcp](https://github.com/harshil1712/berlin-transport-mcp) | Berlin | VBB API | TypeScript |
| [anisul/muc-mcp-server](https://github.com/anisul/muc-mcp-server) | Munich | MVG API | — |
| [davidyen1124/caltrain-mcp](https://github.com/davidyen1124/caltrain-mcp) | SF Bay Area (Caltrain) | GTFS static | — |
| [arjunkmrm/sg-lta-mcp](https://github.com/arjunkmrm/sg-lta-mcp) | Singapore | LTA DataMall | — |
| [kennyckk/mcp_hkbus](https://github.com/kennyckk/mcp_hkbus) | Hong Kong | KMB / Long Win Bus | — |
| [nathanielnoyd/metro-mcp](https://github.com/nathanielnoyd/metro-mcp) | Washington, DC | WMATA API | — |
| [sasabasara/where_is_my_train_mcp](https://github.com/sasabasara/where_is_my_train_mcp) | New York City | MTA GTFS + location | — |

**Notable implementations:**

- **mta-mcp** (NYC) — real-time subway arrivals, service status alerts, station search, and trip planning. The most feature-complete city transit MCP
- **kingcountytransit-mcp** (Seattle) — integrates with OneBusAway, a popular open-source transit platform used by multiple US cities
- **berlin-transport-mcp** — accesses Berlin's VBB (Verkehrsverbund Berlin-Brandenburg) covering S-Bahn, U-Bahn, trams, buses, and regional trains
- **muc-mcp-server** (Munich) — real-time MVG departures for Munich's U-Bahn, S-Bahn, trams, and buses
- **caltrain-mcp** — uses static GTFS data for Caltrain schedules, designed for Claude Desktop
- **sg-lta-mcp** (Singapore) — connects to Singapore's Land Transport Authority DataMall for real-time data across MRT, buses, and traffic
- **mcp_hkbus** (Hong Kong) — real-time KMB and Long Win Bus route information and arrival times

The geographic spread is impressive — Asia (Singapore, Hong Kong), Europe (Berlin, Munich), and North America (NYC, Seattle, DC, Bay Area). But the fragmentation is the category's biggest limitation: there's no universal GTFS-realtime MCP server that could work with any transit agency's feed.

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

### Pradumnasaraf/aviationstack-mcp — Airline & Airport Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aviationstack-mcp](https://github.com/Pradumnasaraf/aviationstack-mcp) | — | Python | MIT | Multiple |

**Comprehensive aviation data via the AviationStack API** — fetches real-time and historical flight data:

- **Airline flights** — search flights by airline, route, or specific flight number
- **Airport schedules** — arrival and departure schedules for any airport
- **Future flights** — look up upcoming scheduled flights
- **Aircraft types** — reference data for aircraft models and types
- **Historical data** — search past flights by date with airline and airport filters

Uses the AviationStack API (API key required, free tier available). All tools implemented as Python functions with FastMCP decorators.

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
| [aviation-mcp](https://github.com/blevinstein/aviation-mcp) | — | TypeScript | — | Multiple |

**Deep FAA data access** — a suite of MCP servers mapping directly to FAA and aviation APIs:

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
| [mcp-uber](https://github.com/199-mcp/mcp-uber) | — | TypeScript | — | Multiple |

**The only ride-hailing MCP server** — enables AI assistants to book Uber rides through OAuth 2.0 authentication:

- **Price estimates** — get fare estimates before booking
- **Request rides** — book Uber rides through natural language
- **Ride status** — track ongoing ride progress
- **Cancellation** — cancel rides when needed

Setup requires Uber Developer Dashboard credentials (UBER_CLIENT_ID, UBER_CLIENT_SECRET, UBER_REDIRECT_URI). **Important:** the request scope is privileged — works in development without approval, but production use requires Uber's authorization.

Notable absence: **no Lyft, Grab, Bolt, DiDi, or other ride-hailing MCP servers exist**. Given Uber's developer API ecosystem, this single server highlights how much untapped potential remains in the ride-hailing space.

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

The transportation and mobility MCP space has notable gaps:

- **No GBFS micromobility server** — the General Bikeshare Feed Specification covers dockless scooters, bikeshare, mopedshare, and carshare worldwide, but no MCP server consumes it
- **No universal GTFS-realtime parser** — every city needs its own MCP server because nobody has built a generic one that takes any GTFS-RT feed URL
- **No maritime or shipping tracking** — vessel tracking (AIS), port schedules, and container tracking have no MCP presence
- **No freight or trucking dispatch** — despite TMS platforms having APIs
- **No multimodal journey planning** — no server combines transit + rideshare + bike into unified trip options
- **No parking availability** — real-time parking data exists in many cities but has no MCP server
- **No traffic signal management** — smart traffic infrastructure is entirely absent
- **Single ride-hailing vendor** — only Uber, no Lyft/Grab/Bolt/DiDi

---

## Bottom Line

Transportation and mobility MCP servers earn **3.5 out of 5**. Public transit has impressive geographic breadth — 9+ city-specific servers across Asia, Europe, and North America, plus a multi-country European server. Flight tracking is genuinely useful with Flightradar24's 46-star server providing real-time data without an API key. Aviation data goes deep with FAA-level weather, NOTAMs, and charts. Uber ride booking works through OAuth 2.0.

But the category's biggest weakness is fragmentation: every city needs its own transit server because no universal GTFS-realtime parser exists. Micromobility (scooters, bikeshare) is completely absent despite standardized data feeds. Maritime shipping has zero coverage. And ride-hailing has exactly one server for one platform.

The opportunity is clear: a universal GTFS-realtime MCP server, a GBFS micromobility server, and multimodal journey planning would transform this category from a collection of city-specific projects into a comprehensive mobility platform for AI agents.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

