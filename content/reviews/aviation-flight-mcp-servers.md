---
title: "Aviation & Flight MCP Servers — Flight Tracking, Booking, Weather, NOTAMs, ADS-B, Flightradar24, and Pilot Tools"
date: 2026-03-17T06:00:00+09:00
description: "Aviation and flight MCP servers let AI agents track flights, search fares, check aviation weather, and access real-time aircraft data through the Model Context Protocol."
og_description: "Aviation & flight MCP servers: fli (2,100 stars, Google Flights direct API), flights-mcp (187 stars, Duffel booking), mcp-amadeus (53 stars), flightradar24-mcp (46 stars), FlightAware AeroAPI (27 tools), OpenSky Network, airport lounges, MSFS flight sim, drone/MAVLink. 25+ servers reviewed. Rating: 4/5."
content_type: "Review"
categories: ["/categories/logistics-industry/"]
card_description: "Aviation and flight MCP servers for real-time tracking, fare search, booking, weather briefings, flight simulation, drone control, and pilot tools through AI assistants. **FOUR MAJOR GAPS FILLED since our initial review.** **FlightAware now has a 27-tool MCP server** (mikedarke/mcp-server-flight-aware-aeroapi) covering flight search, live positions, airport delays, weather, and route maps — our biggest previously-identified gap. **OpenSky Network is now accessible** via AiAgentKarl/aviation-mcp-server (10 tools combining OpenSky tracking with AviationWeather.gov and AirLabs). **Flight simulators broke through** — two MSFS MCP servers let AI agents read flight instruments and even control aircraft via SimConnect. **Drone/UAV control arrived** via MAVLinkMCP (16 stars, PX4 support). **Flight search was transformed** by punitarani/fli (2,100 stars) which reverse-engineers the Google Flights API directly — no SerpAPI costs, no scraping — making it the dominant flight search MCP by a wide margin. **Airport lounges now covered** — Airport Lounge List MCP (hosted, 6 tools) searches 8,500+ lounges worldwide by credit card, membership, or network, free with no API key. The category has expanded from 15+ to 25+ servers. Rating upgraded 3.5→4/5."
last_refreshed: 2026-04-30
---

Aviation and flight MCP servers connect AI agents to flight tracking platforms, fare search engines, aviation weather services, and airline data APIs. Instead of manually checking flight status across multiple apps or decoding METAR weather reports, these servers let you track aircraft, search fares, check weather, and plan flights through natural language via the Model Context Protocol.

This review covers **flight tracking, fare search and booking, aviation weather, pilot planning tools, flight simulation, and drone control** — FlightAware, Flightradar24, OpenSky Network, ADS-B Exchange, AviationStack, Duffel, Amadeus, Google Flights, Skyscanner, FAA weather data, MSFS, and MAVLink. For general travel and hotel booking, see our [Travel & Tourism review](/reviews/travel-tourism-mcp-servers/) if available.

The headline findings: **Flight search was transformed** — punitarani/fli (2,100 stars) reverse-engineers the Google Flights API directly with no SerpAPI costs, making it the dominant flight search MCP by far. **FlightAware now has a 27-tool MCP server** filling our biggest previously-identified gap. **OpenSky Network is now accessible** via aviation-mcp-server combining live tracking with weather and airline data. **Flight simulation broke through** — two MSFS MCP servers let AI agents read instruments and even control aircraft. **Drone control arrived** via MAVLinkMCP for PX4 drones. **Airport lounges now covered** — a hosted MCP server searches 8,500+ lounges worldwide for free.

---

## Flight Tracking

### sunsetcoder/flightradar24-mcp-server — Community Flightradar24 Tracker

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server) | 46 | JavaScript/TypeScript | MIT | 4 |

**Real-time flight tracking via Flightradar24 data:**

- **Live flight tracking** — track any flight worldwide in real-time
- **Arrival/departure times** — get scheduled and actual times for any flight
- **Airport status monitoring** — check all flights at a given airport
- **Emergency flight alerts** — detect aircraft squawking emergency codes
- **Claude Desktop integration** — designed specifically for Claude's MCP interface

The most popular community-built Flightradar24 server. Uses unofficial Flightradar24 data, so it could break if the data source changes, but it provides immediate access without API credentials.

### Flightradar24/fr24api-mcp — Official Flightradar24 API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [fr24api-mcp](https://github.com/Flightradar24/fr24api-mcp) | 16 | TypeScript | MIT | 13 |

**The official Flightradar24 MCP server with comprehensive API access:**

- **Live positions** — real-time aircraft positions globally (light and full detail modes)
- **Historical flights** — position data going back to May 11, 2016
- **Flight summaries** — takeoff/landing details with comprehensive metadata
- **Flight tracks** — detailed positional history for specific flights
- **Airline info** — airline details by ICAO/IATA codes
- **Airport info** — airport details (light and full)
- **Live/historic flight counts** — aggregate traffic statistics
- **Filtering** — by callsign, registration, route, aircraft type, airline, and airport

At 13 tools, this is the most comprehensive flight tracking MCP server. The official backing from Flightradar24 means it tracks their API properly and gets maintained. Requires a Flightradar24 API key.

### Pradumnasaraf/aviationstack-mcp — AviationStack Flight Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aviationstack-mcp](https://github.com/Pradumnasaraf/aviationstack-mcp) | 20 | Python | MIT | 12 |

**Comprehensive aviation reference data via AviationStack API:**

- **flights_with_airline** — real-time flight data filtered by airline
- **historical_flights_by_date** — past flight records by date
- **flight_arrival_departure_schedule** — airport schedules (current)
- **future_flights_arrival_departure_schedule** — upcoming schedules
- **random_aircraft_type** / **random_airplanes_detailed_info** — aircraft reference data
- **random_countries_detailed_info** / **random_cities_detailed_info** — geographic reference
- **list_airports** / **list_airlines** / **list_routes** / **list_taxes** — comprehensive reference tables

The broadest aviation reference server. Beyond flight tracking, it covers aircraft types, airlines, airports, routes, and even aviation tax data — making it useful for research and analysis beyond just "where is my flight."

### sragss/flight-mcp — ADS-B Exchange Live Tracking

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [flight-mcp](https://github.com/sragss/flight-mcp) | 4 | JavaScript | — | 4 |

**Real-time aircraft tracking from ADS-B Exchange:**

- **search_aircraft** — find aircraft within a geographic radius
- **get_aircraft** — look up specific aircraft by ICAO hex code
- **list_military_aircraft** — browse military aircraft with regional/type filters
- **get_military_aircraft_types** — enumerate military aircraft type categories
- **Altitude filtering** — exclude ground traffic from results

ADS-B Exchange is notable for being unfiltered — unlike FlightAware or Flightradar24, it doesn't hide military or government aircraft at operator request. The military aircraft tools make this the go-to for OSINT-style aviation monitoring.

### variflight/variflight-mcp — Chinese Aviation Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [variflight-mcp](https://github.com/variflight/variflight-mcp) | 26 | TypeScript | ISC | 7 |

**VariFlight's official MCP server for Chinese and global aviation data:**

- **searchFlightsByDepArr** — find flights between two airports by IATA code and date
- **searchFlightsByNumber** — multi-leg flight details by flight number
- **getFlightTransferInfo** — connection and transfer routing
- **flightHappinessIndex** — unique comfort metric for flights
- **getRealtimeLocationByAnum** — live aircraft position tracking
- **getFutureWeatherByAirport** — 3-day airport weather forecasts
- **searchFlightItineraries** — purchasable flight options with pricing

VariFlight is the leading aviation data provider in China. The "flight happiness index" is unique — a comfort score factoring in on-time performance, aircraft type, and service quality. The itinerary search with pricing makes this part booking tool, part tracking tool.

### mikedarke/mcp-server-flight-aware-aeroapi — FlightAware AeroAPI *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-flight-aware-aeroapi](https://github.com/mikedarke/mcp-server-flight-aware-aeroapi) | 2 | TypeScript | ISC | 27 |

**The most comprehensive flight tracking MCP server — FlightAware's full AeroAPI:**

**Flight tools (11):**
- **search-flights** / **search-flights-advanced** / **search-flight-positions** — find flights by multiple criteria
- **count-flights** — aggregate flight counts
- **get-flight** / **get-flight-canonical** — detailed flight information
- **get-flight-position** / **get-flight-track** — real-time and historical positions
- **get-flight-route** / **get-flight-map** — route data and track visualizations

**Airport tools (16):**
- **get-airport** / **get-nearby-airports** / **get-all-airports** — airport information and discovery
- **get-airport-flights** / **get-airport-arrivals** / **get-airport-departures** — real-time activity
- **get-scheduled-arrivals** / **get-scheduled-departures** — future schedules
- **get-airport-flight-counts** / **get-flights-between-airports** / **get-airport-routes** — traffic analysis
- **get-airport-delays** / **get-all-airport-delays** — delay monitoring nationwide
- **get-airport-weather** / **get-airport-weather-forecast** — airport-specific meteorology

This fills the single biggest gap from our initial review. FlightAware is one of the most trusted names in aviation tracking, and this server exposes the full AeroAPI with 27 tools — the most tools of any aviation MCP server. Requires a FlightAware AeroAPI subscription.

### AiAgentKarl/aviation-mcp-server — OpenSky Network + Weather + AirLabs *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aviation-mcp-server](https://github.com/AiAgentKarl/aviation-mcp-server) | 3 | Python | MIT | 10 |

**Multi-source aviation data combining OpenSky Network, AviationWeather.gov, and AirLabs:**

- **track_live_flights** — current flights globally or by region via OpenSky Network
- **track_flight** — individual flight tracking by callsign or ICAO24 identifier
- **get_flight_path** — historical flight trajectories
- **get_airport_arrivals** / **get_airport_departures** — recent airport traffic
- **get_airport_weather** — current METAR observations
- **get_weather_forecast** — TAF forecasts
- **get_aviation_warnings** — active SIGMETs and hazard alerts
- **get_airport_info** / **get_airline_info** — reference data via AirLabs

This fills the second biggest gap — OpenSky Network's unfiltered ADS-B data is now accessible through MCP. Combines three free data sources: OpenSky (100 calls/day, no auth needed), AviationWeather.gov (100 req/min, no auth), and AirLabs (1,000/month on free tier). Created March 2026. Available on PyPI as `aviation-mcp-server`.

---

## Flight Search & Booking

### punitarani/fli — Google Flights Direct API *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [fli](https://github.com/punitarani/fli) | 2,100 | Python | MIT | 2 |

**The dominant flight search MCP server — direct Google Flights API access with zero scraping costs:**

- **search_flights** — search flights on specific dates with cabin class, airline preferences, departure time windows, and stop preferences
- **search_dates** — find optimal travel dates within a flexible range to discover the cheapest options
- **Direct API** — reverse-engineers the Google Flights API directly, no SerpAPI or web scraping needed
- **Smart filtering** — cabin class, airline preferences, stops, departure windows
- **Rate limiting** — built-in rate limiting and automatic retry mechanisms

At 2,100 stars and 242 forks, fli has become the most popular flight-related MCP server by a wide margin. The key advantage over SerpAPI-based alternatives: it accesses Google Flights data directly with no API costs or usage limits. Also available as a CLI (`fli`) and Python library (`flights` on PyPI). The lack of SerpAPI dependency makes this genuinely free to use.

### ravinahp/flights-mcp — Duffel-Powered Flight Search

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [flights-mcp](https://github.com/ravinahp/flights-mcp) | 187 | Python | MIT | 3 |

**Real bookable fares via Duffel API:**

- **Search Flights** — one-way and round-trip search with cabin class, passenger count, and connection limits
- **Get Offer Details** — detailed pricing and routing for specific offers
- **Search Multi-City Flights** — complex multi-leg itineraries
- **Flexible date search** — search across multiple days to find optimal pricing
- **Contextual memory** — remembers previous searches within a conversation

At 187 stars, this remains the top server for actual bookable fares. While fli dominates search, flights-mcp connects to Duffel's real booking inventory — the results you see are actually purchasable. The multi-day search feature is particularly useful for finding the cheapest travel dates.

### donghyun-chae/mcp-amadeus — Amadeus Flight Offers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-amadeus](https://github.com/donghyun-chae/mcp-amadeus) | 53 | Python | MIT | 1 |

**Amadeus API integration for flight offer search:**

- **get_flight_offers** — search flights between two locations with date and passenger details
- **Filtering** — cabin class, non-stop only, currency, maximum price
- **Amadeus API** — connects to the industry-standard Global Distribution System

Amadeus is one of the three major GDS platforms (alongside Sabre and Travelport) that power most airline booking systems. Having MCP access means tapping into the same data that travel agents use, though this server currently only exposes the search endpoint, not booking.

### arjunprabhulal/mcp-flight-search — Google Flights via SerpAPI

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-flight-search](https://github.com/arjunprabhulal/mcp-flight-search) | 42 | Python | MIT | 2 |

**Flight search using Google Flights data through SerpAPI:**

- **search_flights_tool** — search one-way and round-trip flights via Google Flights
- **server_status** — health check endpoint
- **SerpAPI integration** — uses Google's flight search results programmatically
- **Rich logging** — structured output for debugging

Google Flights aggregates fares from multiple sources and is widely used for price comparison. This server gives AI agents access to the same data, though it requires a SerpAPI key (which has usage costs).

### manohar42/google-flights-mcp-server — Search + Booking Workflow

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [google-flights-mcp-server](https://github.com/manohar42/google-flights-mcp-server) | — | Python | MIT | 9 |

**The most complete flight workflow — search via Google Flights, book via Duffel:**

- **search_flights** / **search_multi_city** — Google Flights search via SerpAPI
- **duffel_create_offer_request** / **duffel_list_offers** — create and browse Duffel booking offers
- **booking_validate_or_price_offer** — validate pricing before purchase
- **booking_list_services_and_seatmaps** — view seat maps and ancillary services
- **booking_create_order** — complete the booking
- **booking_get_order_status** — check booking status
- **booking_pay_for_order** — process payment

The only MCP server that covers the complete flight journey from search to payment. Combines SerpAPI for Google Flights discovery with Duffel's booking API for the actual transaction. At 9 tools, it's the most full-featured flight booking server.

### Additional Flight Search Servers

- **smamidipaka6/flights-mcp-server** (22 stars, Python, MIT, 4 tools) — Google Flights MCP with best flights, cheapest flights, and time-filtered search. Supports one-way currently, round-trip planned *(NEW)*
- **maratsarbasov/flights-mcp** (11 stars, Python, GPL-3.0, 4 tools) — Aviasales API integration with granular filtering, sorting by price/duration/time, baggage info, and booking link generation. Supports stdio, HTTP, and SSE transports *(NEW)*
- **HaroldLeo/google-flights-mcp** (3 stars, Python, MIT, 6 tools) — Google Flights with alliance filtering (Star Alliance, SkyTeam, OneWorld), multi-date range search, Hugging Face Spaces deployment, and 10 built-in travel planning prompts *(NEW)*
- **shadyvb/mcp-skyscanner** (4 stars, Python, GPL-3.0) — reverse-engineered Skyscanner API for flight and airport search. Experimental/educational only — uses an unofficial API client
- **JamesANZ/flight-finder-mcp** (1 star, TypeScript, MIT) — multi-source search across Skyscanner and Google Flights with 5 tools, including monthly price analysis and best-price recommendations

---

## Aviation Weather & Pilot Tools

### blevinstein/aviation-mcp — FAA Weather, Charts, and NOTAMs

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aviation-mcp](https://github.com/blevinstein/aviation-mcp) | 9 | JavaScript/TypeScript | MIT | 3 servers |

**Professional aviation data from FAA sources — weather, charts, and NOTAMs:**

**Weather server:**
- **METAR** — current aerodrome weather observations
- **TAF** — terminal aerodrome forecasts
- **PIREP** — pilot reports of in-flight conditions
- **SIGMET** — significant meteorological information
- **G-AIRMET** — graphical airmen's meteorological information

**Charts server:**
- **Sectional charts** — VFR navigation charts
- **TAC** — terminal area charts
- **IFR enroute** — instrument flight rules charts
- **TPP** — terminal procedures publications

**NOTAMs server:**
- **FAA NOTAM API** — notices to air missions with extensive filtering (requires FAA client credentials)
- **Filter by** — ICAO/domestic location, NOTAM type, feature type, temporal range

This is the standout server for actual pilots and aviation professionals. No other MCP server provides this combination of weather products, charts, and NOTAMs from authoritative sources. Published as an npm package with modular server design. Note: aviation weather and charts don't require API keys; NOTAMs require FAA credentials.

### finack/aviation-mcp — Aviation Weather API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aviation-mcp](https://github.com/finack/aviation-mcp) | 2 | TypeScript | MIT | 4 |

**Aviation weather from aviationweather.gov for flight planning:**

- **get-metar** — current weather observations for airports
- **get-taf** — terminal forecasts
- **get-pireps** — pilot weather reports
- **get-route-weather** — weather along a planned flight route

The route weather tool is particularly useful — instead of checking individual airports, you can get weather along an entire planned route. Auto-generates a type-safe API client from the official Aviation Weather API specs. Includes a prominent safety disclaimer that this tool should never be the sole source for actual flight planning decisions.

---

## Airport Experience

### Airport Lounge List MCP — Worldwide Lounge Search *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Airport Lounge List MCP](https://mcp.airportloungelist.com/) | hosted | — | Free | 6 |

**Search 8,500+ airport lounges worldwide — free, no API key required:**

- **search_lounges** — query by name, airport code, city, or country
- **get_airport_lounges** — all lounges at a specific airport with interactive UI
- **get_lounge_details** — comprehensive info including hours, capacity, and amenities
- **find_lounges_by_access** — filter by credit card, membership, or airline status
- **list_access_methods** — 22 supported access types
- **get_network_lounges** — browse by network (Priority Pass, LoungeKey, DragonPass, Plaza Premium, Amex Centurion)

This fills the airport lounge gap entirely. A hosted remote MCP server at `mcp.airportloungelist.com/mcp` with Streamable HTTP transport — no local installation needed. Renders interactive visual interfaces directly in conversations. Compatible with ChatGPT, Claude Desktop, Cursor, and Claude Code.

---

## Flight Simulation *(NEW SECTION)*

### TheDigitalNinja/MSFS-SimConnect-MCP — MSFS 2024 Flight Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MSFS-SimConnect-MCP](https://github.com/TheDigitalNinja/MSFS-SimConnect-MCP) | 2 | C# | Unlicense | 11 |

**Read-only flight data from Microsoft Flight Simulator 2024 for AI-powered flight instruction:**

- **get_flight_position** — coordinates, heading, ground speed, vertical speed, pitch, bank, altitude
- **get_flight_instruments** — IAS, TAS, Mach, heading indicator, altimeter
- **get_engine_status** — RPM, fuel flow/quantity, temperatures, N1/N2, APU
- **get_autopilot_status** — AP/FD modes, VNAV, bank/pitch hold, yaw damper
- **get_aircraft_info** — aircraft type, tail number, weights
- **get_flight_plan_leg** / **get_flight_plan_waypoint** — GPS waypoint data, ETE/ETA, cross-track error
- **get_navigation_status** — nav source, OBS, CDI, LOC/GS availability
- **get_approach_status** — approach loaded/active, glidepath deviation
- **get_aircraft_configuration** — gear, flaps, spoilers, lights, brake status

The read-only design is intentional — this server is built for AI flight instruction where the model can observe and coach but cannot take control. Includes a web dashboard at localhost:5000. Created January 2026.

### alxspiker/MSFS-MCP-Server — AI-Controlled MSFS

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MSFS-MCP-Server](https://github.com/alxspiker/MSFS-MCP-Server) | 0 | Python | — | 4 |

**LLM-controlled Microsoft Flight Simulator via SimConnect — AI can fly the plane:**

- **get_simvar_group_state** — read instrument data
- **set_event_state** — control buttons and levers
- **engage_takeoff_autopilot** — automated departure with heading hold and rotation management
- **engage_landing_autopilot** — automated approach with glideslope tracking

Unlike the read-only server above, this one gives the AI full control. Uses custom Python PID controllers running at 20Hz for flight surface control. Landing logic is experimental. Supports MSFS 2020 and 2024.

---

## Drone & UAV Control *(NEW SECTION)*

### ion-g-ion/MAVLinkMCP — MAVLink Drone Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MAVLinkMCP](https://github.com/ion-g-ion/MAVLinkMCP) | 16 | Python | MIT | — |

**MCP server for controlling MAVLink-enabled drones via PX4:**

- **MAVLink protocol** — the standard communication protocol used by millions of drones worldwide
- **PX4 support** — compatible with the most widely-used open-source drone autopilot
- **Agent integration** — includes example agent using the fastagent library
- **Human-in-the-loop** — human input support for supervised drone control

MAVLink is the universal language of drone control (Ardupilot, PX4), so this server potentially covers a huge range of hardware. Research from January 2026 demonstrated integration with Google Maps MCP for real-time navigation-aware drone flight planning. This fills the drone/UAV gap from our initial review.

---

## What's Missing

Aviation coverage has expanded significantly, but gaps remain:

- ~~**FlightAware**~~ — **FILLED** (27-tool AeroAPI server)
- ~~**OpenSky Network**~~ — **FILLED** (via aviation-mcp-server)
- ~~**Airport lounge finders**~~ — **FILLED** (Airport Lounge List, 8,500+ lounges)
- ~~**Flight simulator integration**~~ — **FILLED** (two MSFS servers)
- ~~**Drone / UAV airspace**~~ — **PARTIALLY FILLED** (MAVLinkMCP for drone control, but no LAANC airspace authorization)
- **Airline-specific APIs** — no United, Delta, American, Southwest, or any airline's direct API
- **TSA / security wait times** — no airport security queue data
- **Baggage tracking** — no luggage status tools
- **Seat maps and reviews** — no SeatGuru or cabin layout tools (beyond the Duffel booking workflow)
- **X-Plane / FlightGear** — MSFS is covered, but no other flight sim platforms
- **Private aviation / charter** — no FBO, charter, or fractional ownership tools
- **Air traffic control** — no LiveATC or ATC audio stream access
- **Airport ground transportation** — no shuttle, parking, or ground transport tools

---

## Bottom Line

The aviation and flight MCP server category has **matured significantly** since our initial review, with four of our biggest identified gaps now filled. Flight search was transformed by fli (2,100 stars) which reverse-engineers Google Flights directly — no API costs, no scraping — while flights-mcp (187 stars) remains the leader for actual bookable fares through Duffel. Flight tracking is now comprehensive with FlightAware's 27-tool AeroAPI server joining Flightradar24 (official + community), OpenSky Network, and ADS-B Exchange.

The professional pilot tools remain a standout — METAR, TAF, PIREP, SIGMET, G-AIRMET, charts, and NOTAMs from FAA sources via blevinstein/aviation-mcp (now 9 stars, 88 commits). The new airport lounge finder (8,500+ lounges, free) adds genuine consumer value. Flight simulation and drone control opened entirely new use cases — from AI flight instruction in MSFS to MAVLink-based drone operations.

The remaining weaknesses are increasingly niche — airline-specific APIs, baggage tracking, TSA wait times, and ground transportation. The core aviation workflow of "search, track, plan, and book flights" is well-covered across multiple data sources and price points.

**Rating: 4/5** — Upgraded from 3.5. Four major gaps filled (FlightAware, OpenSky, flight sim, airport lounges), flight search transformed by fli's direct Google Flights API, and the category expanded from 15+ to 25+ servers. Points still deducted for no airline-specific integrations, no ground-side airport experience beyond lounges, and limited coverage outside MSFS for flight simulation.

*This review was refreshed on 2026-04-30 using Claude Opus 4.6 (Anthropic). [AI-generated content](/about/).*
