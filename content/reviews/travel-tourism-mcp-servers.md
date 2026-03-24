---
title: "Travel & Tourism MCP Servers — Google Flights, Airbnb, Expedia, Tripadvisor, Skyscanner, Google Maps, and More"
date: 2026-03-15T16:00:00+09:00
description: "Travel and tourism MCP servers are turning AI assistants into trip planners. We reviewed 30+ servers across 6 subcategories. Flight Search: ravinahp/flights-mcp (169 stars, Python, MIT, 3 tools — Duffel API, one-way/round-trip/multi-city, contextual memory for price comparison), HaroldLeo/google-flights-mcp (Python, MIT, 10 tools — SerpAPI + fast-flights fallback, price context indicators, multi-passenger, all cabin classes), shadyvb/mcp-skyscanner (4 stars, Python, GPL-3.0, 2 tools — Best/Cheapest/Fastest/Direct categorization), JamesANZ/flight-finder-mcp (TypeScript, MIT, 5 tools — dual-source Skyscanner + Google Flights, date-range price analysis), Kiwi.com official MCP (flight search with flexible dates). Accommodation: openbnb-org/mcp-server-airbnb (394 stars, JavaScript, MIT, 2 tools — Airbnb search/details, no API key needed, robots.txt compliant), esakrissa/hotels_mcp_server (14 stars, Python, MIT, 2 tools — Booking.com hotel search via RapidAPI), EmilyThaHuman/booking-mcp-server (TypeScript — Booking.com with ChatGPT UI widgets). Travel Platforms: ExpediaGroup/expedia-travel-recommendations-mcp (11 stars, Python, Apache-2.0, 4 tools — official Expedia, hotels/flights/activities/car rentals, dual protocol stdio/HTTP), pab1it0/tripadvisor-mcp (53 stars, Python, MIT, 5 tools — location search/details/reviews/photos/nearby). Maps & Navigation: cablate/mcp-google-map (193 stars, TypeScript, MIT, 13 tools — 10 atomic + 3 composite, route planning/area exploration/place comparison), GongRzhe/TRAVEL-PLANNER-MCP-Server (95 stars, JavaScript, MIT, 4 tools — Google Places/Directions/Geocoding/TimeZone). Multi-Service Travel Assistants: skarlekar/mcp_travelassistant (28 stars, Python, MIT — 6 specialized servers for flights/hotels/events/geocoding/weather/finance), gs-ysingh/travel-mcp-server (13 stars, TypeScript, 5 tools — flights/accommodation/exchange rates/weather/budgets). Rating: 4.0/5."
og_description: "Travel & tourism MCP servers: Airbnb (394 stars, no API key needed), flights-mcp (169 stars, Duffel API), Google Maps (193 stars, 13 tools), Expedia (official, 4 tools), Tripadvisor (53 stars, 5 tools), Travel Planner (95 stars, Google Maps integration), Skyscanner, Google Flights (10 tools), Kiwi.com (official). Rating: 4.0/5."
content_type: "Review"
card_description: "Travel and tourism MCP servers for flight search, accommodation booking, destination research, maps, and trip planning. This is one of the strongest consumer-facing MCP categories, with impressive breadth and two official vendor servers. Airbnb's community server leads in stars (394) — it searches listings and retrieves property details without requiring an API key, respecting robots.txt by default. Flight search has the most competitive landscape with 8+ implementations across Google Flights, Skyscanner, Duffel, Booking.com, and Kiwi.com — ravinahp's flights-mcp (169 stars) stands out for its Duffel API integration with contextual memory for comparing prices across conversations. Expedia's official MCP server provides hotel, flight, activity, and car rental recommendations through a clean 4-tool interface with dual protocol support. Tripadvisor's community server (53 stars) gives AI agents access to location data, reviews, and photos across hotels, restaurants, and attractions. Google Maps integration is exceptionally strong — cablate's server (193 stars) provides 13 tools including 3 composite tools for route planning, area exploration, and place comparison. The most architecturally interesting project is skarlekar's Travel Assistant ecosystem — 6 specialized MCP servers (flights, hotels, events, geocoding, weather, finance) that Claude orchestrates into complete trip itineraries. Major gaps: no official Google Flights, Booking.com, or Kayak MCP servers; Sabre/Amadeus/Travelport GDS integration exists conceptually but has no public MCP implementations; no visa/passport requirement checkers; no travel insurance; no cruise line servers; car rental coverage is minimal. The category earns 4.0/5 — strong consumer travel coverage with official Expedia and Kiwi.com servers, excellent flight search diversity, and Google Maps providing the navigation backbone."
last_refreshed: 2026-03-15
category_url: "/categories/lifestyle-personal/"
---

Travel and tourism MCP servers are turning AI assistants into capable trip planners — searching flights, finding accommodations, researching destinations, planning routes, and calculating budgets, all through natural language. Instead of tabbing between Google Flights, Booking.com, and Google Maps, you can ask an AI agent to find the cheapest flights to Barcelona next month, compare Airbnb options near the beach, and plan a walking route between your top attractions.

The landscape spans six areas: **flight search** (Google Flights, Skyscanner, Duffel, Kiwi.com), **accommodation** (Airbnb, Booking.com, hotel search), **travel platforms** (Expedia, Tripadvisor), **maps and navigation** (Google Maps, route planning, place discovery), **multi-service travel assistants** (orchestrated trip planning across multiple data sources), and **destination and activities** (local events, weather, currency exchange).

The headline findings: **Airbnb has the most popular travel MCP server** (394 stars) — community-built, no API key required. **Flight search is the most competitive subcategory** with 8+ implementations across 5 different data sources. **Expedia and Kiwi.com have official MCP servers** — making travel one of the few consumer categories with real vendor support. **Google Maps MCP servers are exceptionally capable** — the leading one (193 stars) provides 13 tools including composite operations for route planning and area exploration. **No major GDS has a public MCP implementation** — Sabre and Amadeus discuss MCP architecturally, but the integrations aren't open-source.

## Flight Search

### flights-mcp (Duffel API)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ravinahp/flights-mcp](https://github.com/ravinahp/flights-mcp) | 169 | Python | MIT | 3 |

The **most popular dedicated flight search MCP server**. Built on the Duffel API — a modern flight booking API used by travel companies — it provides real-time flight data from multiple airlines through a clean 3-tool interface:

- **search_flights** — one-way, round-trip, and multi-city searches with cabin class and passenger options
- **get_offer_details** — detailed information on specific flight offers
- **search_multi_city_flights** — complex itinerary planning across multiple destinations

The key differentiator is **contextual memory within chat conversations** — the server maintains context so you can search for flights, then ask "what about a day later?" or "compare that with business class" without re-specifying the entire query. Multi-day search helps identify optimal pricing windows.

This is explicitly read-only — it searches for flights but cannot make bookings or charges. Uses Duffel's API which provides access to major airlines without the complexity of traditional GDS integration.

### Google Flights MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [HaroldLeo/google-flights-mcp](https://github.com/HaroldLeo/google-flights-mcp) | 1 | Python | MIT | 10 |
| [smamidipaka6/flights-mcp-server](https://github.com/smamidipaka6/flights-mcp-server) | — | Python | — | — |
| [salamentic/google-flights-mcp](https://github.com/salamentic/google-flights-mcp) | — | Python | — | — |

Three implementations scrape or proxy Google Flights data for AI agents.

**HaroldLeo/google-flights-mcp** is the most feature-rich with 10 specialized tools:

- search_one_way_flights, search_round_trip_flights, search_round_trips_in_date_range
- get_multi_city_flights, search_direct_flights
- search_flights_by_airline, search_flights_with_max_stops
- get_travel_dates, generate_google_flights_url

Standout features include **price context indicators** (low/typical/high compared to historical prices), native airline filtering, token-efficient compact mode, and pagination. It uses free fast-flights scraping by default with SerpAPI as a fallback (250 free searches/month).

**smamidipaka6/flights-mcp-server** focuses on finding cheapest options and filtering by time restrictions. **salamentic/google-flights-mcp** positions itself as a "travel agent-level" flight planning tool using the fast-flights API.

### Skyscanner and Multi-Source

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [shadyvb/mcp-skyscanner](https://github.com/shadyvb/mcp-skyscanner) | 4 | Python | GPL-3.0 | 2 |
| [JamesANZ/flight-finder-mcp](https://github.com/JamesANZ/flight-finder-mcp) | 1 | TypeScript | MIT | 5 |
| [Kiwi.com Official MCP](https://github.com/alpic-ai/kiwi-mcp-server-public) | — | — | — | — |

**shadyvb/mcp-skyscanner** exposes Skyscanner's flight search with results organized into **Best, Cheapest, Fastest, and Direct** categories — mirroring Skyscanner's own UI categories. Supports round-trips with up to 8 passengers, configurable locale, currency, and market. Marked experimental/educational only, as it uses a reverse-engineered API.

**JamesANZ/flight-finder-mcp** is the **only multi-source flight search** — it queries both Skyscanner and Google Flights simultaneously, then uses 5 tools to search, compare across date ranges, analyze flight details, recommend best booking dates, and find optimal monthly flights. The month-long analysis with cabin class optimization and weekend/weekday comparison is unique.

**Kiwi.com** has an **official MCP server** supporting one-way and round-trip searches with flexible dates, multiple passengers, and all cabin classes. It works with ChatGPT, Claude, Cursor, and other MCP platforms. This is notable as one of the few travel companies to officially embrace MCP.

## Accommodation

### Airbnb MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [openbnb-org/mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb) | 394 | JavaScript | MIT | 2 |

The **most popular travel MCP server** and one of the most popular MCP servers in any consumer category. Two tools cover the core use case:

- **airbnb_search** — location-based listing discovery with filters for dates, guests, price range, and Google Maps Place IDs
- **airbnb_listing_details** — comprehensive property information including amenities, policies, coordinates, and photos

The key feature: **no API key required**. It retrieves Airbnb data while respecting robots.txt by default (configurable). This means zero setup friction — install, configure your MCP client, and start searching. Pagination support handles browsing through results. Available as a Desktop Extension (DXT) for one-click installation in Claude Desktop.

Works on macOS, Windows, and Linux with Node.js 18+. Minimal external dependencies for security.

### Hotels and Booking.com

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [esakrissa/hotels_mcp_server](https://github.com/esakrissa/hotels_mcp_server) | 14 | Python | MIT | 2 |
| [EmilyThaHuman/booking-mcp-server](https://github.com/EmilyThaHuman/booking-mcp-server) | — | TypeScript | — | — |
| [prakashsanker/flights-mcp-server](https://github.com/prakashsanker/flights-mcp-server) | 6 | JavaScript | — | 3 |

**esakrissa/hotels_mcp_server** connects to Booking.com's API via RapidAPI for hotel searches. Two tools handle destination search (by name) and hotel listing retrieval (with date ranges). Returns comprehensive data: room types, pricing, discounts, ratings, reviews, photos, check-in/out times, and star ratings.

**EmilyThaHuman/booking-mcp-server** takes a different approach — it integrates Booking.com accommodation search with ChatGPT and provides **interactive UI widgets** for browsing hotels, apartments, hostels, and other accommodation types worldwide.

**prakashsanker/flights-mcp-server** is positioned as a generalized travel server — it searches flights via Booking.com's API but also handles hotel discovery and supports Google Maps queries like "15 minutes walk from the Eiffel Tower." Car rentals and hotel reviews are planned.

## Travel Platforms

### Expedia (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ExpediaGroup/expedia-travel-recommendations-mcp](https://github.com/ExpediaGroup/expedia-travel-recommendations-mcp) | 11 | Python | Apache-2.0 | 4 |

An **official Expedia server** — maintained by ExpediaGroup on GitHub. Four tools cover the major travel verticals:

- **Hotel recommendations** — accommodation discovery and comparison
- **Flight recommendations** — flight search across airlines
- **Activity recommendations** — things to do at destinations
- **Car rental recommendations** — vehicle rental options

Dual protocol support (stdio and streamable-http) means it works both as a local MCP server for desktop clients and as a remote HTTP server for web applications. Docker deployment is supported. API key authentication required.

This is a recommendations-focused server — it helps travelers discover options rather than completing bookings. For an official enterprise travel platform server, the scope is appropriately focused. The activity and car rental tools are notably absent from most other travel MCP servers.

### Tripadvisor

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pab1it0/tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp) | 53 | Python | MIT | 5 |

Connects AI agents to Tripadvisor's Content API — the world's largest travel guidance platform with reviews for hotels, restaurants, attractions, and experiences.

Five tools cover the core research workflow:

- **search_locations** — find hotels, restaurants, and attractions by query
- **search_nearby_locations** — coordinate-based proximity discovery (useful with Google Maps integration)
- **get_location_details** — comprehensive information about a specific location
- **get_location_reviews** — traveler reviews and ratings
- **get_location_photos** — visual content for destinations

Docker containerization is supported, and tool availability is configurable per MCP client. This is the kind of server that pairs naturally with flight and accommodation servers — once you know where you're going, Tripadvisor helps you figure out what to do there.

Requires a Tripadvisor API key, which is available through their developer program.

## Maps & Navigation

### Google Maps MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cablate/mcp-google-map](https://github.com/cablate/mcp-google-map) | 193 | TypeScript | MIT | 13 |
| [GongRzhe/TRAVEL-PLANNER-MCP-Server](https://github.com/GongRzhe/TRAVEL-PLANNER-MCP-Server) | 95 | JavaScript | MIT | 4 |
| [vicpeacock/google-maps-comprehensive-mcp](https://github.com/vicpeacock/google-maps-comprehensive-mcp) | — | — | — | 8 |

Google Maps MCP servers are **the navigation backbone for travel AI agents** — they provide the spatial intelligence that connects flights and hotels to actual trip experiences.

**cablate/mcp-google-map** (193 stars) is the most comprehensive with 13 tools split between atomic and composite operations:

Atomic tools: nearby search, place search, place details, geocode, reverse geocode, distance matrix, directions, elevation, timezone, weather. Composite tools: **explore_area** (discover what's around a location), **plan_route** (multi-stop optimized routing), **compare_places** (side-by-side comparison). All operations are read-only — MCP clients can approve them automatically without user confirmation.

**GongRzhe/TRAVEL-PLANNER-MCP-Server** (95 stars) focuses on the core travel planning tools: searchPlaces, getPlaceDetails, calculateRoute (with driving/walking/bicycling/transit modes), and getTimeZone. Multiple installation methods including Smithery and npm.

These servers are what make travel MCP ecosystems truly useful — without spatial context, flight and hotel searches happen in a vacuum. With Google Maps, an AI agent can recommend restaurants near your hotel, plan walking routes between attractions, and calculate transit times.

## Multi-Service Travel Assistants

### Travel Assistant Ecosystem

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [skarlekar/mcp_travelassistant](https://github.com/skarlekar/mcp_travelassistant) | 28 | Python | MIT | 6 servers |

The **most architecturally ambitious travel MCP project** — a suite of 6 specialized servers designed to be orchestrated together by Claude for comprehensive trip planning:

1. **Flight Search Server** — find and compare flights with pricing analysis
2. **Hotel Search Server** — discover accommodations filtered by budget and amenities
3. **Event Search Server** — locate local events and activities at destinations
4. **Geocoder Server** — location-to-coordinates conversion and distance calculations
5. **Weather Search Server** — forecasts and condition analysis for travel dates
6. **Finance Search Server** — currency conversion and exchange rates

The modular design means each server can be updated independently, and parallel execution queries multiple servers simultaneously. The AI agent synthesizes data across all six to generate complete itineraries with budget tracking and weather-informed activity recommendations.

This demonstrates the real power of MCP for travel — rather than building one monolithic travel API, you compose specialized servers into a planning pipeline where Claude handles the orchestration logic.

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

Less architecturally elegant than the multi-server approach, but significantly simpler to set up and configure. Good for users who want basic trip planning without managing 6 separate servers.

## What's Missing

The gaps in travel MCP servers reveal where the industry hasn't embraced AI-native access:

- **No official Google Flights or Booking.com MCP servers** — the two most popular travel search tools lack vendor-supported MCP integration
- **No GDS access** — Sabre, Amadeus, and Travelport discuss MCP architecturally but have no public implementations. This means no access to the real-time inventory that powers professional travel booking
- **No cruise line servers** — Royal Caribbean, Carnival, Norwegian, and MSC are completely absent
- **No visa/passport requirement checkers** — no server tells you whether you need a visa for your destination based on your nationality
- **No travel insurance** — no MCP integration with Allianz, World Nomads, or similar providers
- **Minimal car rental coverage** — only Expedia's recommendation tool touches car rentals; no Hertz, Avis, or Enterprise servers
- **No train/rail booking** — despite European and Asian rail systems having APIs, no MCP servers exist for Eurostar, SNCF, JR, or Amtrak
- **No airport information** — no lounges, terminal maps, real-time flight status, or airport amenity servers
- **No group/corporate travel** — the entire category is consumer-focused with no business travel management

## The Bottom Line

Travel and tourism MCP servers earn a **4.0 out of 5**. This is one of the strongest consumer-facing MCP categories, with impressive breadth across the entire trip planning journey — from flight search through accommodation to destination research and navigation.

The flight search subcategory alone has 8+ implementations across 5 different data sources, giving users real choice. Airbnb's 394-star community server demonstrates genuine demand for AI-powered travel search. Expedia and Kiwi.com providing official servers shows the travel industry is taking MCP seriously. Google Maps integration is exceptionally strong with composite tools for route planning and area exploration.

The multi-server travel assistant ecosystem shows what's possible when MCP servers are composed — an AI agent that simultaneously searches flights, compares hotels, checks weather, converts currencies, and finds events to create a complete trip itinerary.

What prevents a higher rating is the absence of booking capabilities (most servers are search-only), the missing GDS layer that would unlock professional-grade inventory access, and the total lack of rail, cruise, and ground transportation options. Travel MCP is excellent for research and planning — the booking gap is the next frontier.

*Last updated: March 2026*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
