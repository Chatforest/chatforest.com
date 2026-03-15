---
title: "Hospitality & Hotels MCP Servers — Airbnb Search, Hotel Booking, Restaurant Reservations, and Travel Planning"
date: 2026-03-15T23:00:00+09:00
description: "Hospitality and hotel MCP servers are a growing category with 25+ servers across 6 subcategories. Vacation Rentals: openbnb-org/mcp-server-airbnb (393 stars, TypeScript, MIT — 2 tools, Airbnb listing search and detail retrieval via HTML scraping, DXT format, advanced filtering by location/dates/guests/price). Hotel Booking: jinkoso/jinko-mcp (TypeScript — 5 tools, 2M+ hotels worldwide, real booking with payment links, facility filtering, multi-language), soren-olympus/amadeus-mcp (TypeScript — Amadeus Travel API, hotel list/search/booking with payment details), fiqcodes/amadeus-mcp-server (Python, MIT — flights/hotels/tours/activities with auto USD conversion). Hotel Concierge: woodstocksoftware/hotel-concierge-mcp (Python — 7 tools, SQLite demo, check availability/make reservations/room types/service requests). Restaurant Reservations: jrklein343-svg/restaurant-mcp (TypeScript — 12+ tools, unified Resy + OpenTable search, direct Resy booking, reservation sniping, Windows Credential Manager), musemen/resy-mcp-server (Python — Resy automation with encrypted token storage, waitlist management, calendar integration), samwang0723/mcp-booking (Go — Google Maps Places API, restaurant discovery with mood/event matching, mock booking). Review Platforms: Yelp/yelp-mcp (official Yelp, TypeScript — Fusion AI API, natural language search, conversational reservations, multi-turn conversations), pab1it0/tripadvisor-mcp (46 stars, Python, MIT — location search, reviews, photos, nearby locations via TripAdvisor Content API). Travel Planning: skarlekar/mcp_travelassistant (Python — 6 specialized servers: flights/hotels/events/geocoder/weather/finance, multi-API orchestration). Gaps: no property management systems (Oracle Hospitality, Mews, Cloudbeds), no revenue management, no guest experience platforms, no event/conference venue management, no food delivery integration, no hotel loyalty program APIs, no housekeeping/operations. Rating: 3.5/5."
og_description: "Hospitality & Hotels MCP servers: mcp-server-airbnb (393 stars, TypeScript, MIT — Airbnb search), jinko-mcp (5 tools, 2M+ hotels), restaurant-mcp (Resy + OpenTable unified booking), Yelp/yelp-mcp (official, Fusion AI API), tripadvisor-mcp (46 stars, reviews/photos), amadeus-mcp (Amadeus Travel API). 25+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Hospitality and hotel MCP servers for AI-powered accommodation search, hotel booking, restaurant reservations, travel planning, and review platform access. This is a solid mid-tier category with strong coverage of consumer-facing booking workflows but limited enterprise/operations tooling. **Airbnb search leads the category in adoption** — openbnb-org/mcp-server-airbnb (393 stars, TypeScript, MIT) is the standout with 2 tools for searching and inspecting Airbnb listings by scraping HTML with advanced filtering (location, dates, guests, price range). Packaged as a Desktop Extension (DXT) for one-click install. No API key needed — it mimics browser requests to extract structured data. The most popular hospitality MCP server by a wide margin. **Hotel booking reaches production scale** — jinkoso/jinko-mcp (TypeScript, 5 tools) provides access to 2M+ hotels worldwide with actual booking capability that returns payment links. Search by coordinates, filter by amenities via a built-in facility database, get hotel details, and complete bookings — the closest thing to a full hotel booking API via MCP. Requires a Jinko API key (commercial). For Amadeus Travel API users, soren-olympus/amadeus-mcp wraps hotel list/search/booking, while fiqcodes/amadeus-mcp-server adds flights, tours, and activities with automatic USD conversion. **Restaurant reservations get unified search** — jrklein343-svg/restaurant-mcp (TypeScript, 12+ tools) is the most ambitious dining server, searching both Resy and OpenTable simultaneously with a single query, making direct Resy bookings, and even offering reservation 'sniping' — automatically booking when slots become available. Credentials are encrypted via Windows Credential Manager (DPAPI). musemen/resy-mcp-server focuses on Resy automation with encrypted token storage, waitlist management, and calendar integration. samwang0723/mcp-booking takes a different approach — using Google Maps Places API for restaurant discovery with mood and event-type matching (dating, business, family), though booking is currently mock-only. **Official platform servers add credibility** — Yelp/yelp-mcp is an official first-party server connecting to Yelp's Fusion AI API for natural language business search, detailed information retrieval, and conversational restaurant reservations. pab1it0/tripadvisor-mcp (46 stars, Python, MIT) provides TripAdvisor Content API access for location search across hotels/restaurants/attractions, reviews, photos, and nearby location discovery. **Travel planning gets a full ecosystem** — skarlekar/mcp_travelassistant is a suite of 6 specialized MCP servers (flights, hotels, events, geocoder, weather, finance) designed for Claude to orchestrate end-to-end travel planning including accommodation search, flight comparison, weather analysis, and budget management across currencies. **Hotel concierge is demo-ready** — woodstocksoftware/hotel-concierge-mcp (Python, 7 tools) provides a complete hotel concierge simulation with availability checking, reservation management, room type browsing, service requests, and hotel info — running on auto-created SQLite. Designed as a reference implementation that can be swapped for real PMS/API integration. **Major gaps in enterprise hospitality** — no property management system servers (Oracle Hospitality/OPERA, Mews, Cloudbeds, Guesty), no revenue management or dynamic pricing, no guest experience platforms (Revinate, TrustYou), no event/conference venue management (Cvent, Social Tables), no food delivery integration (DoorDash, Uber Eats), no hotel loyalty program APIs (Marriott Bonvoy, Hilton Honors, IHG), no housekeeping/maintenance operations, no channel managers (SiteMinder, RateGain). The category earns 3.5/5 — consumer-facing booking and search workflows are well-covered with multiple production-ready options for accommodation search, hotel booking, and restaurant reservations, plus official backing from Yelp and Amadeus. But the enterprise hospitality stack (PMS, revenue management, operations) is completely absent, leaving a significant gap for hotel operators as opposed to travelers."
---

Hospitality and hotel MCP servers let AI assistants search for accommodations, book hotels, make restaurant reservations, discover local dining options, and plan trips. Instead of juggling multiple booking sites and review platforms, these servers let AI agents handle the full hospitality workflow — from finding a place to stay to booking a table for dinner — all through the Model Context Protocol.

This review covers the **hospitality and hotels** vertical — vacation rentals, hotel booking, restaurant reservations, review platforms, and travel planning. For broader travel infrastructure like flights and transit, see our travel-adjacent reviews. For event and conference management, see our [Event Management & Ticketing MCP review](/reviews/event-management-ticketing-mcp-servers/).

The headline findings: **Airbnb search dominates adoption** with 393 stars. **Hotel booking reaches 2M+ properties** via Jinko. **Restaurant reservations get unified Resy + OpenTable search** with auto-booking. **Official Yelp server adds credibility** to the category. **Enterprise hospitality (PMS, revenue management, operations) is completely missing.**

## Vacation Rentals

### openbnb-org/mcp-server-airbnb

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [openbnb-org/mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb) | 393 | TypeScript | MIT | 2 |

The **most popular hospitality MCP server** — searches Airbnb listings by scraping the website HTML rather than using an official API:

- **airbnb_search** — search listings with filters for location, check-in/check-out dates, guest count, price range, and pagination
- **airbnb_listing_details** — get comprehensive details for a specific listing including amenities, house rules, location coordinates, and direct booking links

Packaged as a Desktop Extension (DXT) for one-click install with compatible AI clients. No API key needed — it constructs search URLs, fetches the HTML, and extracts structured data. This is clever but fragile — any Airbnb HTML changes could break it.

The approach means no authentication, no rate limiting concerns, and no cost. But it also means no booking capability — you can search and explore, but completing a reservation requires visiting Airbnb directly. Not affiliated with Airbnb, Inc.

### Other Airbnb Implementations

- **Domoteek/mcp-server-airbnb** (JavaScript, MIT) — similar scraping approach with search and detail tools, plus an `ignore_robots_txt` option
- **vedantparmar12/airbnb-mcp** — adds LiveKit voice interaction support and both HTTP and STDIO transport
- **akktrsst/MCP_Agent_Airbnb** — AI-powered property search with a visual UI

## Hotel Booking

### jinkoso/jinko-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jinkoso/jinko-mcp](https://github.com/jinkoso/jinko-mcp) | — | TypeScript | — | 5 |

The **first MCP server with access to 2M+ hotels** and actual booking capability:

- **find_place** — convert location text (city names, landmarks, hotel names) to coordinates for hotel search
- **get_facilities** — retrieve the facility database in your language for filtering searches by amenities
- **search_hotels** — search by coordinates with check-in/out dates, guest count, and facility filters; returns paginated results with name, address, star rating, price range, and room types
- **get_hotel_details** — comprehensive information about a specific hotel
- **book_hotel** — create a booking quote and return a payment link for the user to complete

This is the closest thing to a full hotel booking API via MCP. The workflow is real: search → select → book → get payment link. Multi-language support for facility names and hotel descriptions. Commercial API key required from [jinko.so](https://www.jinko.so/).

### Amadeus Travel API Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [soren-olympus/amadeus-mcp](https://github.com/soren-olympus/amadeus-mcp) | — | TypeScript | — | 3+ |
| [fiqcodes/amadeus-mcp-server](https://github.com/fiqcodes/amadeus-mcp-server) | — | Python | MIT | 5 |

Two implementations wrapping the **Amadeus Travel API**, the global distribution system used by travel agencies and airlines:

**soren-olympus/amadeus-mcp** focuses on hotels — search for hotels in a city with amenity/star-rating filters, search available rooms with dates, and complete bookings with guest information and payment details. Amadeus API credentials required.

**fiqcodes/amadeus-mcp-server** covers a broader scope — flights, hotels, tours, activities, and city information, all with automatic USD currency conversion. A single API key unlocks the full Amadeus travel ecosystem. MIT licensed with Claude Desktop configuration examples.

### woodstocksoftware/hotel-concierge-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [woodstocksoftware/hotel-concierge-mcp](https://github.com/woodstocksoftware/hotel-concierge-mcp) | 0 | Python | — | 7 |

A **hotel concierge simulation** designed as a reference implementation:

- **check_availability** — check room availability for dates
- **make_reservation** / **get_reservation** / **cancel_reservation** — full reservation lifecycle
- **submit_service_request** — handle guest service requests
- **get_hotel_info** — hotel details and information
- **get_room_types** — browse available room categories

Runs on an auto-created SQLite database. The value is as a starting point — swap the SQLite backend for a real Property Management System (PMS) API and you have a production concierge bot. Python 3.12, pip installable.

### esakrissa/hotels_mcp_server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [esakrissa/hotels_mcp_server](https://github.com/esakrissa/hotels_mcp_server) | 0 | Python | — | — |

A minimal MCP server wrapping the **Booking.com API** for hotel searches. Created March 2025 with no subsequent updates. Requires a Booking.com API key. Too early to evaluate — single-commit project with no documentation on available tools or features.

## Restaurant Reservations

### jrklein343-svg/restaurant-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jrklein343-svg/restaurant-mcp](https://github.com/jrklein343-svg/restaurant-mcp) | — | TypeScript | — | 12+ |

The **most feature-rich restaurant MCP server** — unified search across both Resy and OpenTable with a single query:

- **search_restaurants** — parallel search across both platforms simultaneously
- **check_availability** — real-time availability checking
- **make_reservation** — direct Resy booking (OpenTable provides booking links)
- **list_reservations** / **cancel_reservation** — manage existing reservations
- **snipe_reservation** — automatically book when a desired slot becomes available
- **list_snipes** / **cancel_snipe** — manage active reservation snipers
- **set_credentials** / **set_login** / **check_auth_status** / **refresh_token** — credential management

The reservation sniping feature is notable — set your desired restaurant, date, time, and party size, and the server will continuously check and automatically book when a slot opens. All credentials encrypted via Windows DPAPI (same security as Chrome/Edge passwords). The MCP server never handles payment information.

Windows-specific due to DPAPI credential storage — cross-platform would require a different secrets backend.

### musemen/resy-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [musemen/resy-mcp-server](https://github.com/musemen/resy-mcp-server) | — | Python | — | — |

A **Resy-focused automation server** with encrypted token storage at `~/.resy-mcp/`:

- Authentication management with encrypted tokens and encryption keys
- Restaurant search and reservation operations
- Automated scheduling and waitlist management
- Calendar integration

Includes an automated setup script. The Resy-only focus means deeper integration with that platform compared to the multi-platform restaurant-mcp server.

### samwang0723/mcp-booking

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [samwang0723/mcp-booking](https://github.com/samwang0723/mcp-booking) | — | Go | — | 4+ |

An **AI-powered restaurant discovery server** using Google Maps Places API:

- Smart restaurant search within 20km radius with advanced filtering
- Mood-based filtering — find restaurants matching atmosphere (romantic, casual, upscale)
- Event-specific matching — optimized for dating, family gatherings, business meetings, celebrations
- AI-powered top-3 recommendations with detailed reasoning
- Booking assistance (currently mock implementation)

Default location centered on Taiwan. Google Maps API key required. The mood/event matching is a clever differentiation — "find a romantic Italian restaurant for a date night" is a more natural query than specifying cuisine + price range + rating filters.

Booking is mock-only. Real booking would require integration with restaurant-specific systems or services like OpenTable/Resy.

## Review & Discovery Platforms

### Yelp/yelp-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Yelp/yelp-mcp](https://github.com/Yelp/yelp-mcp) | — | TypeScript | — | — |

The **official first-party Yelp MCP server** — connects to Yelp's Fusion AI API:

- Natural language search — ask questions like "best sushi near me" rather than constructing filter queries
- Multi-turn conversations — refine queries with follow-up questions
- Direct business queries — ask about specific businesses without a prior search
- Conversational reservations — explore availability and book restaurant tables through natural language

This is significant because it's official — maintained by Yelp, not a community scraper. Requires a Yelp Fusion AI API key. The conversational reservation feature means an AI agent can handle the full flow from discovery to booking without the user leaving their chat interface.

### pab1it0/tripadvisor-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pab1it0/tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp) | 46 | Python | MIT | 4+ |

Access to **TripAdvisor's Content API** for location discovery and reviews:

- Search for locations (hotels, restaurants, attractions) on TripAdvisor
- Get detailed information about specific locations
- Retrieve reviews and photos for locations
- Search for nearby locations based on coordinates

The tool list is configurable — choose which tools to expose to your MCP client. Unofficial community implementation, but well-maintained with 46 stars. Requires a TripAdvisor Content API key.

## Travel Planning

### skarlekar/mcp_travelassistant

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [skarlekar/mcp_travelassistant](https://github.com/skarlekar/mcp_travelassistant) | — | Python | — | 6 servers |

A **suite of 6 specialized MCP servers** for end-to-end travel planning:

1. **Flight Search Server** — find and compare flights, analyze pricing, filter by preferences
2. **Hotel Search Server** — discover accommodations, compare amenities, filter by budget
3. **Event Search Server** — find local events, festivals, and activities
4. **Geocoder Server** — convert locations to coordinates, calculate distances, reverse geocoding
5. **Weather Search Server** — get forecasts, current conditions, weather alerts
6. **Finance Search Server** — currency conversion, exchange rates, financial analysis

Requires API keys for SerpAPI (flights, hotels, events, finance), OpenWeatherMap or National Weather Service (weather), and OpenStreetMap Nominatim (geocoder). The orchestration concept is powerful — a single travel query triggers multiple specialized servers working together.

## EmilyThaHuman/booking-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [EmilyThaHuman/booking-mcp-server](https://github.com/EmilyThaHuman/booking-mcp-server) | — | TypeScript | — | — |

Integrates **Booking.com accommodation search** with ChatGPT using the OpenAI Apps SDK, providing interactive UI widgets for searching hotels, apartments, hostels, and other accommodations worldwide. A different approach — designed for ChatGPT plugins rather than Claude Desktop, but built on MCP infrastructure.

## What's Missing

The hospitality MCP ecosystem covers the traveler/consumer side well but has major gaps on the operator/enterprise side:

- **No Property Management Systems** — Oracle Hospitality/OPERA, Mews, Cloudbeds, Guesty, Hostaway have no MCP integrations
- **No revenue management** — no dynamic pricing, demand forecasting, or rate optimization servers
- **No guest experience platforms** — Revinate, TrustYou, ReviewPro for reputation management
- **No event/conference venue management** — Cvent, Social Tables, Tripleseat for event planning
- **No food delivery** — DoorDash, Uber Eats, Grubhub APIs remain unconnected
- **No hotel loyalty programs** — Marriott Bonvoy, Hilton Honors, IHG Rewards, World of Hyatt
- **No housekeeping/maintenance** — no operations management servers
- **No channel managers** — SiteMinder, RateGain, Cloudbeds channel management
- **No dedicated concierge/activities** — Viator, GetYourGuide, Klook for tours and activities

The gap between "search and book as a traveler" (well-served) and "manage operations as a hotelier" (completely absent) is one of the starkest divides in any MCP category.

## The Bottom Line

Hospitality MCP servers earn **3.5/5**. The consumer booking journey is well-covered: you can search Airbnb (393 stars, no API key needed), book from 2M+ hotels via Jinko, search both Resy and OpenTable for restaurant reservations with auto-sniping, discover businesses through official Yelp and TripAdvisor servers, and orchestrate full trip planning across 6 specialized servers. The official Yelp server and Amadeus Travel API integrations add commercial credibility.

What holds the category back from a higher rating is the complete absence of enterprise hospitality tooling. A hotel general manager, revenue analyst, or operations director would find nothing useful here — no PMS integration, no revenue management, no guest communication, no housekeeping workflows. The category serves travelers excellently but hoteliers not at all. As PMS providers like Mews and Cloudbeds embrace AI, expect MCP servers for hotel operations to emerge — but they aren't here yet.
