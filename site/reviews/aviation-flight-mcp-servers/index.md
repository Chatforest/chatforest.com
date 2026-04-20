# Aviation & Flight MCP Servers — Flight Tracking, Booking, Weather, NOTAMs, ADS-B, Flightradar24, and Pilot Tools

> Aviation and flight MCP servers let AI agents track flights, search fares, check aviation weather, and access real-time aircraft data through the Model Context Protocol.


Aviation and flight MCP servers connect AI agents to flight tracking platforms, fare search engines, aviation weather services, and airline data APIs. Instead of manually checking flight status across multiple apps or decoding METAR weather reports, these servers let you track aircraft, search fares, check weather, and plan flights through natural language via the Model Context Protocol.

This review covers **flight tracking, fare search and booking, aviation weather, and pilot planning tools** — Flightradar24, ADS-B Exchange, AviationStack, Duffel, Amadeus, Google Flights, Skyscanner, and FAA weather data. For general travel and hotel booking, see our [Travel & Tourism review](/reviews/travel-tourism-mcp-servers/) if available.

The headline findings: **Flight search is the strongest segment** — flights-mcp (169 stars) leads with Duffel API integration for bookable fares across airlines. **Flightradar24 has both official and community MCP servers**, with the official version offering 13 tools and historical data back to 2016. **Professional pilot tools exist** — aviation-mcp provides METAR, TAF, PIREP, SIGMET, and NOTAM access from FAA sources. **VariFlight uniquely covers Chinese aviation** with comfort metrics and airport weather. **The biggest gap: no FlightAware or OpenSky Network MCP servers**, and no airline-specific integrations.

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
| [fr24api-mcp](https://github.com/Flightradar24/fr24api-mcp) | 14 | TypeScript | MIT | 13 |

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
| [aviationstack-mcp](https://github.com/Pradumnasaraf/aviationstack-mcp) | 17 | Python | MIT | 12 |

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
| [variflight-mcp](https://github.com/variflight/variflight-mcp) | 22 | TypeScript | ISC | 7 |

**VariFlight's official MCP server for Chinese and global aviation data:**

- **searchFlightsByDepArr** — find flights between two airports by IATA code and date
- **searchFlightsByNumber** — multi-leg flight details by flight number
- **getFlightTransferInfo** — connection and transfer routing
- **flightHappinessIndex** — unique comfort metric for flights
- **getRealtimeLocationByAnum** — live aircraft position tracking
- **getFutureWeatherByAirport** — 3-day airport weather forecasts
- **searchFlightItineraries** — purchasable flight options with pricing

VariFlight is the leading aviation data provider in China. The "flight happiness index" is unique — a comfort score factoring in on-time performance, aircraft type, and service quality. The itinerary search with pricing makes this part booking tool, part tracking tool.

---

## Flight Search & Booking

### ravinahp/flights-mcp — Duffel-Powered Flight Search

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [flights-mcp](https://github.com/ravinahp/flights-mcp) | 169 | Python | MIT | 3 |

**The most popular flight search MCP server — real bookable fares via Duffel:**

- **Search Flights** — one-way and round-trip search with cabin class, passenger count, and connection limits
- **Get Offer Details** — detailed pricing and routing for specific offers
- **Search Multi-City Flights** — complex multi-leg itineraries
- **Flexible date search** — search across multiple days to find optimal pricing
- **Contextual memory** — remembers previous searches within a conversation

At 169 stars, this is the most popular aviation MCP server overall. Duffel provides access to real, bookable airline fares (not scraped prices), so the results you see are actually purchasable. The multi-day search feature is particularly useful for finding the cheapest travel dates.

### donghyun-chae/mcp-amadeus — Amadeus Flight Offers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-amadeus](https://github.com/donghyun-chae/mcp-amadeus) | 50 | Python | MIT | 1 |

**Amadeus API integration for flight offer search:**

- **get_flight_offers** — search flights between two locations with date and passenger details
- **Filtering** — cabin class, non-stop only, currency, maximum price
- **Amadeus API** — connects to the industry-standard Global Distribution System

Amadeus is one of the three major GDS platforms (alongside Sabre and Travelport) that power most airline booking systems. Having MCP access means tapping into the same data that travel agents use, though this server currently only exposes the search endpoint, not booking.

### arjunprabhulal/mcp-flight-search — Google Flights via SerpAPI

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-flight-search](https://github.com/arjunprabhulal/mcp-flight-search) | 40 | Python | MIT | 2 |

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

- **shadyvb/mcp-skyscanner** (4 stars, Python, GPL-3.0) — reverse-engineered Skyscanner API for flight and airport search. Experimental/educational only — uses an unofficial API client
- **JamesANZ/flight-finder-mcp** (1 star, TypeScript, MIT) — multi-source search across Skyscanner and Google Flights with 5 tools, including monthly price analysis and best-price recommendations

---

## Aviation Weather & Pilot Tools

### blevinstein/aviation-mcp — FAA Weather, Charts, and NOTAMs

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aviation-mcp](https://github.com/blevinstein/aviation-mcp) | 6 | JavaScript/TypeScript | MIT | 3 servers |

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

## What's Missing

Aviation is a massive industry but MCP coverage has clear gaps:

- **FlightAware** — one of the most popular flight tracking platforms has no MCP server
- **OpenSky Network** — the largest open ADS-B data source has no dedicated MCP server
- **Airline-specific APIs** — no United, Delta, American, Southwest, or any airline's direct API
- **TSA / security wait times** — no airport security queue data
- **Baggage tracking** — no luggage status tools
- **Airport lounge finders** — no Priority Pass, LoungeBuddy, or lounge access tools
- **Seat maps and reviews** — no SeatGuru or cabin layout tools (beyond the Duffel booking workflow)
- **Carbon offset calculation** — no flight emissions calculators
- **Flight simulator integration** — no MSFS, X-Plane, or FlightGear MCP servers
- **Drone / UAV airspace** — no LAANC authorization, drone airspace, or Part 107 tools
- **Private aviation / charter** — no FBO, charter, or fractional ownership tools
- **Air traffic control** — no LiveATC or ATC audio stream access
- **Airport ground transportation** — no shuttle, parking, or ground transport tools

---

## Bottom Line

The aviation and flight MCP server category is **well-balanced across consumer and professional use cases**. Flight search is genuinely useful — flights-mcp at 169 stars provides real bookable fares through Duffel, and you can combine Google Flights search with Duffel booking for a complete search-to-purchase workflow. Flight tracking is strong with Flightradar24 having both an official 13-tool server and a popular community version, plus ADS-B Exchange for unfiltered tracking including military aircraft.

The professional pilot tools set this category apart from typical consumer travel — METAR, TAF, PIREP, SIGMET, G-AIRMET, charts, and NOTAMs from FAA sources is a genuinely useful combination for flight planning support. VariFlight fills the Chinese market gap with unique features like the flight happiness index.

The main weakness is breadth — FlightAware and OpenSky Network are notably absent, no individual airlines have MCP servers, and the entire ground-side airport experience (security, lounges, baggage, ground transport) is missing. But for the core use cases of "track a flight" and "search for fares," the tools available are solid.

**Rating: 3.5/5** — Strong flight tracking and fare search with genuine professional aviation tools. The Duffel-powered booking workflow and FAA weather/NOTAM access are standout features. Points deducted for missing major platforms (FlightAware, OpenSky), no airline-specific integrations, and no coverage of the ground-side airport experience.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

