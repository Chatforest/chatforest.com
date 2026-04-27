# Travel & Tourism MCP Servers — Fli (2.1K Stars), Skiplagged Official, Airbnb, Amadeus GDS, Mapbox, Expedia, and More

> Travel and tourism MCP servers are turning AI assistants into trip planners. We reviewed 50+ servers across 8 subcategories including Amadeus GDS, Skiplagged, Mapbox, and travel hacking.


Travel and tourism MCP servers are turning AI assistants into capable trip planners — searching flights, finding accommodations, researching destinations, planning routes, and calculating budgets, all through natural language. Instead of tabbing between Google Flights, Booking.com, and Google Maps, you can ask an AI agent to find the cheapest flights to Barcelona next month, compare Airbnb options near the beach, and plan a walking route between your top attractions.

The landscape now spans eight areas: **flight search** (Fli/Google Flights, Skiplagged, Skyscanner, Duffel, Kiwi.com, Amadeus), **accommodation** (Airbnb, Booking.com, Marriott, hotel search), **travel platforms** (Expedia, Tripadvisor, Hopper), **maps and navigation** (Google Maps, Mapbox, route planning, place discovery), **GDS and professional travel** (Amadeus integrations), **travel hacking** (points, miles, award flights, credit card portals), **ground transportation** (car rental, rail), and **multi-service travel assistants** (orchestrated trip planning across multiple data sources).

The headline findings: **Fli has exploded to 2,100 stars** — a Python library with reverse-engineered Google Flights API access, now the most popular flight search MCP server by a wide margin. **Skiplagged launched an official MCP server** — hidden-city deals, flexible dates, hotels, and rental cars with no API key required. **Amadeus GDS now has 6+ MCP implementations** — filling the biggest structural gap from our initial review. **The travel-hacking-toolkit (440 stars) created a new subcategory** — AI-powered points/miles optimization across 25+ award programs. **Mapbox shipped an official MCP server** (335 stars, 18 tools) — a powerful Google Maps alternative. **Four official vendor servers** now exist (Expedia, Kiwi.com, Skiplagged, Mapbox), up from two in March.

*This review was refreshed on April 27, 2026 — 43 days after the initial review on March 15.*

## Flight Search

### Fli — Google Flights MCP and Python Library

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [punitarani/fli](https://github.com/punitarani/fli) | 2,100 | Python | MIT | 2 |

**NEW — The most popular flight search MCP server by a massive margin.** Fli has exploded to 2,100 stars, dwarfing every other flight search implementation. Unlike web scraping approaches, it uses a **reverse-engineered Google Flights API** for direct data access — faster, more reliable, and less prone to breakage.

Two MCP tools cover the core use case:

- **search_flights** — detailed single-date searches with cabin class, stops, airline, and sorting filters
- **search_dates** — find the cheapest travel dates across flexible date ranges

Also ships as a CLI tool (`fli`) and Python library with 11 comprehensive examples. Supports both STDIO and HTTP server modes. Built-in rate limiting and retry mechanisms. Docker support included.

The zero-scraping architecture is the key differentiator — while other Google Flights servers depend on fast-flights or SerpAPI, Fli talks directly to Google's API layer. This makes it significantly more robust for production use.

### Skiplagged (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Skiplagged Official MCP](https://skiplagged.github.io/mcp/) | — | — | — | 5 |

**NEW — Official MCP server from Skiplagged**, the travel search engine famous for **hidden-city ticketing** deals. Five tools with **no API key, no account, no authentication required**:

- **Flight search** — one-way and round-trip with filtering options, including hidden-city routes
- **Flexible date calendars** — explore departure/return dates to find cheaper days
- **Anywhere destinations** — discover low-fare destinations from your origin
- **Hotel search** — accommodations with room-level pricing and amenities
- **Rental car search** — vehicles for specified pickup/drop-off times

Public endpoint at `mcp.skiplagged.com/mcp`. Works with Claude, ChatGPT, Cursor, and VS Code. One-click installation in supported platforms. This is the **third official travel vendor MCP server** (after Expedia and Kiwi.com) and the most frictionless — zero setup required.

### flights-mcp (Duffel API)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ravinahp/flights-mcp](https://github.com/ravinahp/flights-mcp) | 188 | Python | MIT | 3 |

The **most popular Duffel API flight server** (up from 169 stars). Built on Duffel — a modern flight booking API used by travel companies — it provides real-time flight data from multiple airlines through a clean 3-tool interface:

- **search_flights** — one-way, round-trip, and multi-city searches with cabin class and passenger options
- **get_offer_details** — detailed information on specific flight offers
- **search_multi_city_flights** — complex itinerary planning across multiple destinations

The key differentiator is **contextual memory within chat conversations** — the server maintains context so you can search for flights, then ask "what about a day later?" or "compare that with business class" without re-specifying the entire query. Multi-day search helps identify optimal pricing windows.

This is explicitly read-only — it searches for flights but cannot make bookings or charges. Uses Duffel's API which provides access to major airlines without the complexity of traditional GDS integration.

### Google Flights MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [HaroldLeo/google-flights-mcp](https://github.com/HaroldLeo/google-flights-mcp) | 1 | Python | MIT | 10 |
| [tistaharahap/google-flights-mcp](https://github.com/tistaharahap/google-flights-mcp) | — | Python | — | — |
| [msr2903/google-flights-mcp](https://github.com/msr2903/google-flights-mcp) | — | Python | — | — |
| [manohar42/google-flights-mcp-server](https://github.com/manohar42/google-flights-mcp-server) | — | Python | — | — |
| [smamidipaka6/flights-mcp-server](https://github.com/smamidipaka6/flights-mcp-server) | — | Python | — | — |
| [salamentic/google-flights-mcp](https://github.com/salamentic/google-flights-mcp) | — | Python | — | — |

Google Flights implementations have expanded from 3 to 6+ (not counting Fli above, which uses direct API access rather than scraping).

**HaroldLeo/google-flights-mcp** remains the most feature-rich with 10 specialized tools including price context indicators, airline filtering, and token-efficient compact mode. Uses free fast-flights scraping by default with SerpAPI as a fallback.

**tistaharahap/google-flights-mcp** is a new FastMCP server providing Google Flights data with flight search, airport lookup, and pricing tools. **msr2903/google-flights-mcp** uses the bundled fast_flights library. **manohar42/google-flights-mcp-server** combines SerpAPI Google Flights search with Duffel API for bookings — the only implementation bridging search and booking in a single server.

### Skyscanner and Multi-Source

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [shadyvb/mcp-skyscanner](https://github.com/shadyvb/mcp-skyscanner) | 4 | Python | GPL-3.0 | 2 |
| [JamesANZ/flight-finder-mcp](https://github.com/JamesANZ/flight-finder-mcp) | 1 | TypeScript | MIT | 5 |
| [Kiwi.com Official MCP](https://github.com/alpic-ai/kiwi-mcp-server-public) | 11 | — | — | — |

**shadyvb/mcp-skyscanner** exposes Skyscanner's flight search with results organized into **Best, Cheapest, Fastest, and Direct** categories — mirroring Skyscanner's own UI categories. Supports round-trips with up to 8 passengers, configurable locale, currency, and market. Marked experimental/educational only, as it uses a reverse-engineered API.

**JamesANZ/flight-finder-mcp** is the **only multi-source flight search** — it queries both Skyscanner and Google Flights simultaneously, then uses 5 tools to search, compare across date ranges, analyze flight details, recommend best booking dates, and find optimal monthly flights. The month-long analysis with cabin class optimization and weekend/weekday comparison is unique.

**Kiwi.com** has an **official MCP server** (11 stars) supporting one-way and round-trip searches with flexible dates, multiple passengers, and all cabin classes. It works with ChatGPT, Claude, Cursor, and other MCP platforms.

## Accommodation

### Airbnb MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [openbnb-org/mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb) | 437 | JavaScript | MIT | 2 |

The **most popular accommodation MCP server** (up from 394 stars, +11%). v0.2.0 released April 2026. Two tools cover the core use case:

- **airbnb_search** — location-based listing discovery with filters for dates, guests, price range, and Google Maps Place IDs
- **airbnb_listing_details** — comprehensive property information including amenities, policies, coordinates, and photos

The key feature: **no API key required**. It retrieves Airbnb data while respecting robots.txt by default (configurable). Zero setup friction — install, configure your MCP client, and start searching. Now packaged as an MCPB format bundle with client-side geocoding via Photon and Nominatim for improved international support. Available as a Desktop Extension (DXT) for one-click installation in Claude Desktop.

### Marriott Hotels (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markswendsen-code/mcp-marriott](https://github.com/markswendsen-code/mcp-marriott) | 3 | TypeScript | MIT | 16 |

**NEW — The first hotel chain MCP server with loyalty program integration.** 16 tools cover the full hotel workflow plus Bonvoy loyalty:

- **Property search** — find Marriott hotels across global locations
- **Room browsing** — room types and rate comparisons
- **Booking management** — create, view, modify, cancel reservations
- **Mobile check-in** — remote check-in support
- **Bonvoy integration** — points tracking, tier status, award stay redemption, historical stays

Uses Playwright browser automation with cookie-based session persistence. Safety confirmations required for destructive operations (cancellations). This is significant — it's the first MCP server that lets AI agents interact with a major hotel loyalty program.

### Hotels and Booking.com

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markswendsen-code/mcp-booking](https://github.com/markswendsen-code/mcp-booking) | — | TypeScript | MIT | 14 |
| [esakrissa/hotels_mcp_server](https://github.com/esakrissa/hotels_mcp_server) | — | Python | MIT | 2 |
| [EmilyThaHuman/booking-mcp-server](https://github.com/EmilyThaHuman/booking-mcp-server) | — | TypeScript | — | — |
| [prakashsanker/flights-mcp-server](https://github.com/prakashsanker/flights-mcp-server) | 3 | JavaScript | — | 3 |

**markswendsen-code/mcp-booking** is a **NEW** comprehensive Booking.com MCP server with 14 tools covering the full hotel booking workflow — search, availability checks, reservation management, and more — via Playwright browser automation with cookie-based session persistence.

**esakrissa/hotels_mcp_server** connects to Booking.com's API via RapidAPI for hotel searches. Two tools handle destination search (by name) and hotel listing retrieval (with date ranges). Returns comprehensive data: room types, pricing, discounts, ratings, reviews, photos, check-in/out times, and star ratings.

**EmilyThaHuman/booking-mcp-server** integrates Booking.com accommodation search with ChatGPT and provides **interactive UI widgets** for browsing hotels, apartments, hostels, and other accommodation types worldwide.

**prakashsanker/flights-mcp-server** is a generalized travel server — it searches flights via Booking.com's API but also handles hotel discovery and supports Google Maps queries like "15 minutes walk from the Eiffel Tower."

## Travel Platforms

### Expedia (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ExpediaGroup/expedia-travel-recommendations-mcp](https://github.com/ExpediaGroup/expedia-travel-recommendations-mcp) | 14 | Python | Apache-2.0 | 4 |

An **official Expedia server** — maintained by ExpediaGroup on GitHub (up from 11 stars). Four tools cover the major travel verticals:

- **Hotel recommendations** — accommodation discovery and comparison
- **Flight recommendations** — flight search across airlines
- **Activity recommendations** — things to do at destinations
- **Car rental recommendations** — vehicle rental options

Dual protocol support (stdio and streamable-http) means it works both as a local MCP server for desktop clients and as a remote HTTP server for web applications. Docker deployment is supported. API key authentication required.

### Tripadvisor

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pab1it0/tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp) | 54 | Python | MIT | 5 |

Connects AI agents to Tripadvisor's Content API — the world's largest travel guidance platform with reviews for hotels, restaurants, attractions, and experiences (up from 53 stars).

Five tools cover the core research workflow:

- **search_locations** — find hotels, restaurants, and attractions by query
- **search_nearby_locations** — coordinate-based proximity discovery (useful with Google Maps integration)
- **get_location_details** — comprehensive information about a specific location
- **get_location_reviews** — traveler reviews and ratings
- **get_location_photos** — visual content for destinations

Docker containerization is supported, and tool availability is configurable per MCP client. Requires a Tripadvisor API key, which is available through their developer program.

### Hopper (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markswendsen-code/mcp-hopper](https://github.com/markswendsen-code/mcp-hopper) | — | JavaScript | MIT | 7 |

**NEW — AI-powered travel booking with price prediction.** Hopper is known for its AI-driven price forecasting — this MCP server brings that capability to AI agents:

- **search_flights** and **search_hotels** — real-time pricing and availability
- **get_price_forecast** — AI-powered buy/wait/watch recommendations
- **set_price_alert** — automated price monitoring
- **book_flight** and **book_hotel** — booking initiation
- **get_bookings** — booking history access

The price forecasting integration is unique in the travel MCP space — no other server provides AI-driven guidance on whether to buy now or wait for a better price.

## Maps & Navigation

### Mapbox (Official) — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mapbox/mcp-server](https://github.com/mapbox/mcp-server) | 335 | TypeScript | MIT | 18 |

**NEW — Official Mapbox MCP server**, and a major addition to the travel navigation landscape. 18 tools split between online API tools and **offline geospatial calculations** (no API calls needed):

**Online tools (9):** directions, matrix, isochrone, geocoding/search, reverse geocoding, category search (POI across millions of locations), map matching, route optimization (traveling salesman), static images.

**Offline tools (9):** distance, bearing, midpoint, centroid, area, buffer, simplify, bounding box, point-in-polygon.

The **isochrone generation** is unique among travel MCP servers — it calculates reachability areas ("show me everywhere I can reach within 30 minutes of my hotel"). Route optimization solves the traveling salesman problem for multi-stop itineraries. Static map image generation provides visual context. Supports MCP Apps protocol for interactive map previews.

At 335 stars, this is now the **second-most popular mapping MCP server** and provides capabilities Google Maps servers don't offer (isochrones, offline calculations, route optimization).

### Google Maps MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cablate/mcp-google-map](https://github.com/cablate/mcp-google-map) | 224 | TypeScript | MIT | 13 |
| [GongRzhe/TRAVEL-PLANNER-MCP-Server](https://github.com/GongRzhe/TRAVEL-PLANNER-MCP-Server) | 90 | JavaScript | MIT | 4 |
| [vicpeacock/google-maps-comprehensive-mcp](https://github.com/vicpeacock/google-maps-comprehensive-mcp) | — | — | — | 8 |

Google Maps MCP servers remain **the navigation backbone for travel AI agents** — they provide the spatial intelligence that connects flights and hotels to actual trip experiences.

**cablate/mcp-google-map** (224 stars, up from 193, +16%) is the most comprehensive Google Maps server with 13 tools split between atomic and composite operations:

Atomic tools: nearby search, place search, place details, geocode, reverse geocode, distance matrix, directions, elevation, timezone, weather. Composite tools: **explore_area** (discover what's around a location), **plan_route** (multi-stop optimized routing), **compare_places** (side-by-side comparison). All operations are read-only. Now at v0.0.19 with configurable tool limiting to reduce context usage.

**GongRzhe/TRAVEL-PLANNER-MCP-Server** (90 stars) focuses on the core travel planning tools: searchPlaces, getPlaceDetails, calculateRoute (with driving/walking/bicycling/transit modes), and getTimeZone.

## GDS & Professional Travel (NEW)

### Amadeus MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [donghyun-chae/mcp-amadeus](https://github.com/donghyun-chae/mcp-amadeus) | 53 | Python | MIT | 1 |
| [fiqcodes/amadeus-mcp-server](https://github.com/fiqcodes/amadeus-mcp-server) | 1 | Python | — | 4 |
| [lev-corrupted/travel-mcp-server](https://github.com/lev-corrupted/travel-mcp-server) | 2 | Python | MIT | 7 |
| [technicalerikchan/flight-mcp-server](https://github.com/technicalerikchan/flight-mcp-server) | — | — | — | — |
| [soren-olympus/amadeus-mcp](https://github.com/soren-olympus/amadeus-mcp) | — | — | — | — |
| [almogqwinz/mcp-amadeus-api](https://github.com/almogqwinz/mcp-amadeus-api) | — | — | — | — |

**NEW — This fills the biggest structural gap from our initial review.** Amadeus is one of the three major Global Distribution Systems (along with Sabre and Travelport) that power professional travel booking worldwide. Six or more MCP implementations now provide AI agents access to Amadeus inventory.

**donghyun-chae/mcp-amadeus** (53 stars) leads the pack with Docker support and the official amadeus-python SDK. Searches flight offers with cabin class, non-stop preferences, currency, max price, and multi-traveler support. Claude Desktop integration included.

**fiqcodes/amadeus-mcp-server** is the most feature-rich with 4 tools — flight search, city information (IATA codes, coordinates), tours and activities, and hotel search. Automatic USD currency conversion for all prices.

**lev-corrupted/travel-mcp-server** combines Amadeus with AviationStack for 7 tools — flight search, hotel availability, real-time flight tracking, airport information, and cheapest date discovery. The AviationStack integration adds real-time flight status updates that Amadeus alone doesn't provide.

While Sabre and Travelport still lack MCP implementations, Amadeus coverage means AI agents now have access to professional-grade travel industry inventory — a structural shift from the consumer-only landscape of March 2026.

### Visa Intelligent Commerce (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [visa/mcp](https://github.com/visa/mcp) | 25 | TypeScript | MIT | 3 packages |

**NEW — Official Visa MCP integration toolkit.** Enables AI agents to connect to Visa Intelligent Commerce — a platform that allows AI agents to securely browse, shop, and purchase on behalf of consumers. Three npm packages:

- **@visa/token-manager** — JWE token generation and MCP authentication
- **@visa/mcp-client** — MCP client connections with automatic authentication
- **@visa/api-client** — API clients for VIC and VDP with X-Pay authentication and MLE encryption

Includes card tokenization, device binding with FIDO authentication, and Visa Passkey creation. This is significant for travel commerce — it's the first payment network to provide MCP integration, enabling AI agents to potentially complete bookings end-to-end rather than just searching.

## Travel Hacking & Points Optimization (NEW)

### Travel Hacking Toolkit

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [borski/travel-hacking-toolkit](https://github.com/borski/travel-hacking-toolkit) | 440 | Python | MIT | 20+ |

**NEW — The most comprehensive travel optimization project in the MCP ecosystem.** At 440 stars, this is the third-most popular travel MCP project overall. It bundles 5 free MCP servers and 15+ skills covering the entire points/miles travel workflow:

**MCP Servers included:** Skiplagged (flights + hidden-city), Kiwi (flights), Trivago (hotels), Ferryhopper (ferries across 33 countries), Airbnb.

**Key capabilities:**
- **Unified flight comparison** — searches across 25+ award programs and multiple cash booking sources simultaneously
- **Points vs. cash analysis** — automatic cost-per-point calculations with transfer optimization
- **Credit card portal access** — Chase Ultimate Rewards and Amex Membership Rewards travel portals including Points Boost rates
- **Loyalty balance tracking** — AwardWallet integration plus airline-specific scrapers
- **Premium hotel database** — 4,659 Amex Fine Hotels & Resorts and Chase Luxury Hotel Collection properties with stacking detection
- **Award flight search** — Duffel GDS, Ignav, Google Flights, Seats.aero combined

Also includes ferry route planning, Scandinavian transit, aircraft seat map visualization, and destination discovery. This project single-handedly creates a "travel hacking" subcategory that didn't exist in the MCP ecosystem before.

## Ground Transportation (NEW)

### Car Rental

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markswendsen-code/mcp-hertz](https://github.com/markswendsen-code/mcp-hertz) | — | TypeScript | MIT | 10 |

**NEW — First dedicated car rental MCP server**, partially filling a gap noted in our initial review. 10 tools cover the rental workflow:

- **Vehicle search** — availability and detailed rate information
- **Reservation management** — create, view, modify, cancel
- **Location discovery** — nearby Hertz locations by city, airport code, or coordinates
- **Rental policies** — insurance options and terms
- **Optional extras** — GPS, child seats, Wi-Fi, etc.
- **Gold Plus Rewards** — loyalty program integration

Uses Playwright browser automation. Fallback placeholder responses when live data is unavailable. While this is Hertz-specific, it proves the car rental MCP pattern works — Avis, Enterprise, and National servers would follow the same architecture.

### Rail

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lucygoodchild/mcp-national-rail](https://github.com/lucygoodchild/mcp-national-rail) | 4 | TypeScript | — | 4 |

**NEW — First rail MCP server**, partially filling another gap from our initial review. Covers UK National Rail via the Realtime Trains API:

- **get_live_departures** and **get_live_arrivals** — real-time station information
- **get_departures_by_date** and **get_arrivals_by_date** — scheduled/historical queries

UK-specific, but it establishes the pattern. European rail (Eurostar, SNCF, Deutsche Bahn) and Asian rail (JR, KTX) remain uncovered. The travel-hacking-toolkit above includes Scandinavian transit (trains, buses, ferries) and Ferryhopper for ferry routes.

## Multi-Service Travel Assistants

### Travel Assistant Ecosystem

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [skarlekar/mcp_travelassistant](https://github.com/skarlekar/mcp_travelassistant) | 32 | Python | MIT | 6 servers |

The **most architecturally ambitious travel MCP project** — a suite of 6 specialized servers designed to be orchestrated together by Claude for comprehensive trip planning (up from 28 stars):

1. **Flight Search Server** — find and compare flights with pricing analysis
2. **Hotel Search Server** — discover accommodations filtered by budget and amenities
3. **Event Search Server** — locate local events and activities at destinations
4. **Geocoder Server** — location-to-coordinates conversion and distance calculations
5. **Weather Search Server** — forecasts and condition analysis for travel dates
6. **Finance Search Server** — currency conversion and exchange rates

The modular design means each server can be updated independently, and parallel execution queries multiple servers simultaneously. The AI agent synthesizes data across all six to generate complete itineraries with budget tracking and weather-informed activity recommendations.

### Travel Concierge (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [abhinavmathur-atlan/mcp-travel-assistant](https://github.com/abhinavmathur-atlan/mcp-travel-assistant) | 5 | Python | — | — |

**NEW — Combines Google Travel Services (via SerpAPI) with Amadeus GDS** in a single concierge server. Includes geocoding, weather forecasting, and currency conversion. Docker deployment supported. Bridges consumer-friendly Google search with professional Amadeus inventory.

### Comprehensive Travel Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gs-ysingh/travel-mcp-server](https://github.com/gs-ysingh/travel-mcp-server) | 13 | TypeScript | ISC | 5 |

A single-server alternative that packs five travel capabilities into one:

- **search_flights** — flight comparison and search
- **search_accommodation** — hotel and vacation rental discovery
- **get_exchange_rate** — real-time currency conversion
- **get_weather_forecast** — destination weather conditions
- **calculate_trip_budget** — expense estimation for the entire trip

Simpler to set up than multi-server approaches. Good for users who want basic trip planning without managing multiple servers.

## What's Missing

Several gaps from March have been filled (Amadeus GDS, car rental, rail), but important ones remain:

- **No official Google Flights or Booking.com MCP servers** — the two most popular travel search tools still lack vendor-supported MCP integration (though Fli's 2,100-star reverse-engineered approach may reduce the urgency for an official Google Flights server)
- **Sabre and Travelport GDS still absent** — Amadeus is now covered, but the other two major GDS platforms have no public MCP implementations
- **No cruise line servers** — Royal Caribbean, Carnival, Norwegian, and MSC remain completely absent
- **No visa/passport requirement checkers** — Visa's MCP is for payments, not travel documents. No server tells you whether you need a visa for your destination based on your nationality
- **No travel insurance** — no MCP integration with Allianz, World Nomads, or similar providers
- **Rail coverage is minimal** — only UK National Rail and Scandinavian transit (via travel-hacking-toolkit). Eurostar, SNCF, Deutsche Bahn, JR, Amtrak, and KTX are uncovered
- **No airport information** — no lounges, terminal maps, real-time flight status, or airport amenity servers (though AviationStack via lev-corrupted's server provides some flight tracking)
- **No group/corporate travel** — the category remains consumer-focused with no business travel management
- **Booking still limited** — most servers are search-only. Hopper and Marriott attempt booking flows, but end-to-end booking with payment remains rare

## The Bottom Line

Travel and tourism MCP servers earn a **4.5 out of 5**, up from 4.0 in March. This category has matured significantly in 43 days.

**Fli's explosion to 2,100 stars** makes it the most popular flight search MCP server by a massive margin — its reverse-engineered Google Flights API approach has clearly resonated with developers. **Three new official vendor servers** (Skiplagged, Mapbox, Visa) join Expedia and Kiwi.com, bringing the official count to five. **Amadeus GDS integration** fills the biggest structural gap from our initial review — AI agents now have access to professional travel industry inventory through 6+ implementations.

The **travel-hacking-toolkit** (440 stars) created an entirely new subcategory — AI-powered points/miles optimization across 25+ award programs, credit card portals, and loyalty programs. This kind of specialized, high-value use case is where MCP servers deliver outsized impact.

**Mapbox's official server** (335 stars, 18 tools) provides capabilities Google Maps doesn't — isochrone generation, route optimization, and offline geospatial calculations. Car rental (Hertz), hotel chains (Marriott with Bonvoy loyalty), and UK rail fill additional gaps.

What prevents a 5.0 rating: cruise lines remain absent, rail coverage is minimal, most servers are search-only without end-to-end booking, and Sabre/Travelport GDS access is still missing. But the trajectory is clear — travel is becoming one of the most complete and commercially viable MCP categories.

*Last updated: April 2026*

*This review was refreshed on 2026-04-27 using Claude Opus 4.6 (Anthropic).*

