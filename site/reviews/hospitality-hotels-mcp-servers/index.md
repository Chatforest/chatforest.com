# Hospitality & Hotels MCP Servers — Airbnb Search, Hotel Booking, Restaurant Reservations, and Travel Planning

> Hospitality and hotel MCP servers are a fast-growing category with 40+ servers across 8 subcategories.


Hospitality and hotel MCP servers let AI assistants search for accommodations, book hotels, make restaurant reservations, discover local dining options, and plan trips. Instead of juggling multiple booking sites and review platforms, these servers let AI agents handle the full hospitality workflow — from finding a place to stay to booking a table for dinner — all through the Model Context Protocol.

This review covers the **hospitality and hotels** vertical — vacation rentals, hotel booking, restaurant reservations, review platforms, and travel planning. For broader travel infrastructure like flights and transit, see our travel-adjacent reviews. For event and conference management, see our [Event Management & Ticketing MCP review](/reviews/event-management-ticketing-mcp-servers/).

The headline findings: **Travel hacking toolkit matches Airbnb** as co-leader at 436 stars. **Strider Labs ships 5+ consumer hospitality servers** in a single sprint. **Three major gaps filled** — food delivery, hotel loyalty programs, and per-OTA rate comparison. **Uber Eats POC hits 221 stars** proving massive demand. **Enterprise hospitality goes MCP** — Aven/Sabre (35,000+ hotels), SiteMinder (53,000 hotels), Agentic Hospitality, and Apaleo all launch or announce MCP integrations. **ExpediaGroup goes official.** Rating upgraded from **3.5 to 4.0/5**.

## Vacation Rentals

### openbnb-org/mcp-server-airbnb

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [openbnb-org/mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb) | 437 | TypeScript | MIT | 2 |

The **most popular hospitality MCP server** — searches Airbnb listings by scraping the website HTML rather than using an official API:

- **airbnb_search** — search listings with filters for location, check-in/check-out dates, guest count, price range, and pagination
- **airbnb_listing_details** — get comprehensive details for a specific listing including amenities, house rules, location coordinates, and direct booking links

Packaged as a Desktop Extension (DXT) for one-click install with compatible AI clients. No API key needed — it constructs search URLs, fetches the HTML, and extracts structured data. This is clever but fragile — any Airbnb HTML changes could break it.

The approach means no authentication, no rate limiting concerns, and no cost. But it also means no booking capability — you can search and explore, but completing a reservation requires visiting Airbnb directly. Not affiliated with Airbnb, Inc.

*Updated April 2026: 393→437 stars (+11%). No new releases or tools added since v0.2.0 (transitioned to MCP Bundle format). Steady growth but development has slowed.*

### Other Airbnb Implementations

- **Domoteek/mcp-server-airbnb** (JavaScript, MIT) — similar scraping approach with search and detail tools, plus an `ignore_robots_txt` option
- **vedantparmar12/airbnb-mcp** — adds LiveKit voice interaction support and both HTTP and STDIO transport
- **akktrsst/MCP_Agent_Airbnb** (6 stars) — AI-powered property search with Gradio chatbot UI, GPT-4o-mini + LangChain

## Hotel Booking

### jinkoso/jinko-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jinkoso/jinko-mcp](https://github.com/jinkoso/jinko-mcp) | 8 | TypeScript | — | 4 |

Access to **2M+ hotels** with actual booking capability:

- **find_place** — convert location text (city names, landmarks, hotel names) to coordinates for hotel search
- **search_hotels** — search by coordinates with check-in/out dates, guest count, and facility filters; returns paginated results with name, address, star rating, price range, and room types
- **get_hotel_details** — comprehensive information about a specific hotel
- **book_hotel** — create a booking quote and return a payment link for the user to complete

The workflow is real: search → select → book → get payment link. Multi-language support for facility names and hotel descriptions. Commercial API key required from [jinko.so](https://www.jinko.so/).

### him229/stays — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [him229/stays](https://github.com/him229/stays) | 1 | — | — | 3 |

A **Google Hotels aggregator** that shows per-OTA rates — the first MCP server to enable hotel price comparison across booking platforms:

- **search_hotels** — search hotels by location
- **get_hotel_details** — get detailed hotel info with rates from multiple OTAs
- **search_hotels_with_details** — combined search and detail retrieval

The key innovation: reverse-engineers Google Hotels' `batchexecute` RPC (no scraping) to show real-time prices from Booking.com, Expedia, Hotels.com, Trip.com, and others with deep-links to each OTA. Supports both MCP stdio and streamable HTTP transport. 330 tests. This fills a significant gap — previously, comparing prices across booking platforms required visiting each one individually.

### mcp-marriott (Strider Labs) — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markswendsen-code/mcp-marriott](https://github.com/markswendsen-code/mcp-marriott) | 3 | TypeScript | — | 16 |

The **first hotel loyalty program MCP server** — full Marriott Bonvoy integration via browser automation:

- **search** / **details** / **room_options** / **select_room** — hotel search and room browsing
- **add_extras** / **checkout** — complete booking workflow
- **reservations** / **modify** / **cancel** — reservation management
- **check_in** — mobile check-in
- **bonvoy_status** / **redeem_points** / **stay_history** — Marriott Bonvoy loyalty features
- **login** / **logout** / **status** — session management

Uses Playwright browser automation with persistent sessions. Part of Strider Labs' growing suite of hospitality MCP servers. Created February 2026. This fills one of the biggest gaps from the original review — hotel loyalty program integration was completely absent.

### mcp-hilton (Strider Labs) — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markswendsen-code/mcp-hilton](https://github.com/markswendsen-code/mcp-hilton) | 0 | TypeScript | — | 16 |

**Hilton Honors integration** with the same Playwright automation approach:

- Hotel search, room browsing, and booking workflow
- **digital_key** — Hilton Digital Key access
- **get_honors_status** / **redeem_points** / **get_stay_history** — Hilton Honors loyalty features
- Reservation management (get, modify, cancel)

Created March 2026. Zero stars but functional. Combined with the Marriott server, Strider Labs now covers the two largest hotel chains in the world.

### Gondola MCP — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Gondola MCP (hosted at mcp.gondola.ai) | — | — | — | 6 |

A **multi-chain hotel search service** covering Marriott, Hilton, Hyatt, IHG, Accor, Wyndham, and more:

- **search_hotels** / **compare_rates** / **get_hotel_details** — cross-chain hotel search and comparison
- **book_hotel** / **get_booking_link** — booking with direct links to preserve loyalty status
- **create_rate_alert** — price monitoring

Free to use, no API key required. Supports member rates, AAA discounts, and points redemption comparisons. Not open source — hosted service only. Notable because it's the only way to search Hyatt, IHG, Accor, and Wyndham via MCP, where no standalone servers exist.

### ExpediaGroup/expedia-travel-recommendations-mcp — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ExpediaGroup/expedia-travel-recommendations-mcp](https://github.com/ExpediaGroup/expedia-travel-recommendations-mcp) | 18 | — | — | 4 |

The **official Expedia Group MCP server** — recommendations for hotels, flights, activities, and car rentals. Supports stdio and streamable HTTP transport. v1.0.2 released August 2025.

This is significant as the first major OTA (Online Travel Agency) to publish an official MCP server. Expedia Group operates Expedia, Hotels.com, Vrbo, and other brands.

### Amadeus Travel API Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [soren-olympus/amadeus-mcp](https://github.com/soren-olympus/amadeus-mcp) | 1 | TypeScript | — | 4 |
| [fiqcodes/amadeus-mcp-server](https://github.com/fiqcodes/amadeus-mcp-server) | 1 | Python | MIT | 4 |

Two implementations wrapping the **Amadeus Travel API**, the global distribution system used by travel agencies and airlines:

**soren-olympus/amadeus-mcp** focuses on hotels — search for hotels in a city with amenity/star-rating filters, search available rooms with dates, and complete bookings with guest information and payment details. Amadeus API credentials required. Stale — single commit, last updated January 2025.

**fiqcodes/amadeus-mcp-server** covers a broader scope — flights, hotels, tours, activities, and city information, all with automatic USD currency conversion. A single API key unlocks the full Amadeus travel ecosystem. MIT licensed. Early-stage with 4 commits total.

### mcp-booking (Strider Labs) — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markswendsen-code/mcp-booking](https://github.com/markswendsen-code/mcp-booking) | 0 | TypeScript | — | 14 |

**Full Booking.com workflow** via browser automation:

- **search** / **get_property** / **check_availability** / **get_prices** — hotel discovery
- **filter** / **sort** / **save** — search refinement
- **book** / **get_reservations** / **cancel** — booking lifecycle
- **get_reviews** — guest reviews
- **login** / **logout** / **status** — session management

Uses Playwright with cookie-based sessions. Created March 2026. The most feature-rich Booking.com MCP server, far surpassing the earlier esakrissa/hotels_mcp_server (2 tools). Part of Strider Labs' suite.

### Other Hotel Servers

- **woodstocksoftware/hotel-concierge-mcp** (Python, 7 tools) — hotel concierge simulation on SQLite; reference implementation for PMS integration
- **esakrissa/hotels_mcp_server** (18 stars, Python, 2 tools) — basic Booking.com API via RapidAPI; 4 commits, stale since March 2025
- **EmilyThaHuman/booking-mcp-server** (TypeScript) — Booking.com search with ChatGPT Apps SDK widgets
- **corneyc/hotels-mcp** — Cloudflare Worker for Hotels.com via RapidAPI

## Restaurant Reservations

### jrklein343-svg/restaurant-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jrklein343-svg/restaurant-mcp](https://github.com/jrklein343-svg/restaurant-mcp) | 2 | TypeScript | — | 11 |

The **most feature-rich restaurant MCP server** — unified search across both Resy and OpenTable with a single query:

- **search_restaurants** — parallel search across both platforms simultaneously
- **check_availability** — real-time availability checking
- **make_reservation** — direct Resy booking (OpenTable provides booking links)
- **list_reservations** / **cancel_reservation** — manage existing reservations
- **snipe_reservation** — automatically book when a desired slot becomes available
- **list_snipes** / **cancel_snipe** — manage active reservation snipers
- **set_credentials** / **set_login** / **check_auth_status** / **refresh_token** — credential management

The reservation sniping feature is notable — set your desired restaurant, date, time, and party size, and the server will continuously check and automatically book when a slot opens. All credentials encrypted via Windows DPAPI (same security as Chrome/Edge passwords). Windows-specific due to DPAPI credential storage. 53 commits, active development but only 2 stars.

### mcp-opentable (Strider Labs) — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markswendsen-code/mcp-opentable](https://github.com/markswendsen-code/mcp-opentable) | 0 | TypeScript | — | 5 |

**OpenTable-specific** browser automation:

- **search** / **details** / **availability** — restaurant discovery
- **reserve** / **booking_history** — make and track reservations

Part of Strider Labs' suite. 187 weekly npm downloads, 85%+ task completion rate. Created March 2026. A simpler alternative to restaurant-mcp for users who only need OpenTable.

### Resy Booker (Apify) — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Apify clearpath/resy-booker | — | — | — | 6 |

A **pay-per-action Resy automation** on the Apify platform:

- Search restaurants, check availability, book slots, view/cancel reservations, login
- Streamable HTTP transport, compatible with Claude and ChatGPT
- No self-hosting required — runs on Apify infrastructure

A different model from the self-hosted servers — pay for each action rather than running your own infrastructure. Good for occasional use without the setup overhead.

### Other Restaurant Servers

- **musemen/resy-mcp-server** (Python) — Resy-focused with encrypted token storage, waitlist management, calendar integration
- **samwang0723/mcp-booking** (14 stars, Go, 5 tools) — Google Maps Places API for restaurant discovery with mood-based filtering and event-specific matching. 65 commits, actively maintained. Default location centered on Taiwan.

## Food Delivery — NEW CATEGORY

### ericzakariasson/uber-eats-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ericzakariasson/uber-eats-mcp-server](https://github.com/ericzakariasson/uber-eats-mcp-server) | 221 | Python | — | — |

A **proof-of-concept Uber Eats automation** that has become the strongest demand signal in the hospitality MCP space. 221 stars with only 5 commits and minimal documentation — the star count reflects how badly people want food delivery automation via AI agents, not the maturity of this particular implementation.

Uses Playwright browser automation. WIP status with no documentation on available tools. But the adoption signal is unmistakable: this is one of the most-wanted MCP use cases.

### mcp-doordash (Strider Labs) — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markswendsen-code/mcp-doordash](https://github.com/markswendsen-code/mcp-doordash) | 3 | TypeScript | — | 4 |

The **first functional food delivery MCP server**:

- **search** — find restaurants on DoorDash
- **browse menus** — view menu items and prices
- **place orders** — complete the ordering workflow
- **track orders** — monitor delivery status

Uses Playwright browser automation with persistent sessions. 395 weekly npm downloads. No public DoorDash API exists, so browser automation is the only path. Created March 2026.

### Grubhub MCP (Strider Labs) — NEW

Also released March 2026 — browser automation for Grubhub search, menus, cart management, ordering, and delivery tracking. No dedicated public GitHub repo found; likely distributed via npm as part of Strider Labs' suite.

## Review & Discovery Platforms

### Yelp/yelp-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Yelp/yelp-mcp](https://github.com/Yelp/yelp-mcp) | 24 | TypeScript | — | 1 |

The **official first-party Yelp MCP server** — connects to Yelp's Fusion AI API with a single conversational tool:

- Natural language search — ask questions like "best sushi near me" rather than constructing filter queries
- Multi-turn conversations — refine queries with follow-up questions
- Direct business queries — ask about specific businesses without a prior search
- Conversational reservations — explore availability and book restaurant tables through natural language

This is significant because it's official — maintained by Yelp, not a community scraper. Requires a Yelp Fusion AI API key.

*Updated April 2026: No commits since July 2025 — 9+ months without activity despite being the only official first-party offering in the category. 24 stars but appears neglected.*

### pab1it0/tripadvisor-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pab1it0/tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp) | 54 | Python | MIT | 5 |

Access to **TripAdvisor's Content API** for location discovery and reviews:

- **search_locations** — search for hotels, restaurants, attractions on TripAdvisor
- **search_nearby_locations** — coordinate-based nearby search
- **get_location_details** — detailed information about specific locations
- **get_location_reviews** — retrieve reviews for locations
- **get_location_photos** — photos for locations

The tool list is configurable — choose which tools to expose to your MCP client. Unofficial community implementation with Docker support.

*Updated April 2026: 46→54 stars (+17%). Steady organic growth.*

## Travel Planning

### borski/travel-hacking-toolkit — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [borski/travel-hacking-toolkit](https://github.com/borski/travel-hacking-toolkit) | 436 | — | — | 22 |

The **most comprehensive travel MCP toolkit** and the new co-leader of the hospitality category:

- **22 integrated tools** across 6 MCP servers + 16 skills
- Points/miles optimization across **25+ airline loyalty programs**
- Integrates Skiplagged, Kiwi, Trivago, Ferryhopper, Airbnb, LiteAPI, Duffel, Google Flights, Seats.aero, Southwest, Chase Travel, Amex Travel, AwardWallet, TripAdvisor, and more
- Drop-in skills for Claude Code and OpenCode

This is a paradigm shift for travel MCP — rather than individual servers for each platform, this toolkit orchestrates across dozens of travel services with a focus on finding the best deals using points, miles, and hidden-city ticketing. 436 stars and 32 forks make it the fastest-growing server in the category.

### skarlekar/mcp_travelassistant

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [skarlekar/mcp_travelassistant](https://github.com/skarlekar/mcp_travelassistant) | 40 | Python | — | 6 servers |

A **suite of 6 specialized MCP servers** for end-to-end travel planning:

1. **Flight Search Server** — find and compare flights, analyze pricing, filter by preferences
2. **Hotel Search Server** — discover accommodations, compare amenities, filter by budget
3. **Event Search Server** — find local events, festivals, and activities
4. **Geocoder Server** — convert locations to coordinates, calculate distances, reverse geocoding
5. **Weather Search Server** — get forecasts, current conditions, weather alerts
6. **Finance Search Server** — currency conversion, exchange rates, financial analysis

Requires API keys for SerpAPI (flights, hotels, events, finance), OpenWeatherMap or National Weather Service (weather), and OpenStreetMap Nominatim (geocoder). 40 stars and 11 forks. Appears dormant since January 2025.

### abhinavmathur-atlan/mcp-travel-assistant — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [abhinavmathur-atlan/mcp-travel-assistant](https://github.com/abhinavmathur-atlan/mcp-travel-assistant) | 5 | — | — | 18 |

A **dual-search travel assistant** combining consumer (SerpAPI/Google Travel) and professional (Amadeus) APIs:

- Flights (2 tools), hotels (4 tools), events/activities (2 tools)
- Utilities (6 tools including geocode, weather, currency, stocks)
- The most feature-rich single-server travel assistant found

15 commits. Small but more actively maintained than the older skarlekar suite.

### mcp-hopper (Strider Labs) — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markswendsen-code/mcp-hopper](https://github.com/markswendsen-code/mcp-hopper) | 0 | JavaScript | — | 7 |

**AI-powered price predictions** for flights and hotels:

- **search_flights** / **search_hotels** — find options
- **get_price_forecast** — "buy now, wait, or watch" recommendations with confidence percentages
- **set_price_alert** — monitor prices
- **book_flight** / **book_hotel** / **get_bookings** — booking and management

Uses stealth browser automation. Created March 2026. The price prediction feature is a unique differentiator — no other MCP server offers AI-driven buy/wait/watch recommendations for travel pricing.

### Other Travel Servers

- **EmilyThaHuman/booking-mcp-server** (TypeScript) — Booking.com search with ChatGPT Apps SDK widgets
- **gs-ysingh/travel-mcp-server** (13 stars, 5 tools) — flights, accommodation, exchange rates, weather, trip budget
- **hirochachacha/rakuten_travel_mcp** (Japan-focused, 2 tools) — Rakuten Travel hotel search for Japan

## Enterprise Hospitality & Distribution — NEW CATEGORY

The enterprise side of hospitality MCP went from completely absent to rapidly emerging in Q1-Q2 2026. Multiple major platforms announced or launched MCP integrations, though all are proprietary/commercial with no open-source repos.

### Agentic Hospitality — TravelOS MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Agentic Hospitality TravelOS (commercial) | — | — | Proprietary | — |

Claims the **industry's first hotel MCP booking transaction**. Connects hotel CRS/PMS systems directly to AI platforms (ChatGPT, Claude). Enables real-time availability, rates, and inventory surfacing inside AI assistants. Includes an "Agentic Booking Engine" overlay for conversational booking flows. Launched March 2026. No public GitHub repo — commercial platform only.

### Aven Hospitality (formerly Sabre) — MCP Enablement

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Aven Hospitality MCP (commercial) | — | — | Proprietary | — |

**MCP integration across the SynXis CRS platform serving 35,000+ hotels globally.** Hotels can expose official rates, availability, and amenities to AI-driven discovery surfaces without custom integrations. Q2 2026 Early Access Program announced. This is massive — Sabre/Aven is one of the "Big Three" global distribution systems alongside Amadeus and Travelport. No public GitHub repo — enterprise product.

### SiteMinder — MCP-Powered AI Distribution

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| SiteMinder MCP (commercial) | — | — | Proprietary | — |

The **first channel manager with MCP integration** — uses MCP to deliver real-time hotel data from its **53,000-hotel inventory** to AI systems. "Demand Plus" extended into AI conversational environments (ChatGPT, Claude). "Channels Plus" gives AI-enabled OTAs access to SiteMinder's inventory. DirectBooker is the first AI demand partner. Announced April 2026. No public GitHub repo — commercial platform.

This directly fills the "no channel managers" gap from the original review — though only as a proprietary offering, not an open-source tool.

### Apaleo MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Apaleo MCP (via Composio) | — | — | — | 29 |

The **first property management system to offer MCP integration** (launched September 2025):

- AI agents can check availability, modify bookings, coordinate housekeeping, create payment links
- Includes an AI Copilot for check-ins, room assignments, and housekeeping
- Property creation, cloning, unit management, bulk operations
- Available via Composio integration at composio.dev

Apaleo is a cloud-native PMS used by boutique and lifestyle hotels. No public GitHub repo yet.

### Enterprise Assessment

The pattern is clear: **enterprise hospitality platforms are building proprietary MCP servers** (Agentic Hospitality, Aven/Sabre, SiteMinder, Apaleo) while **open-source GitHub repos remain mostly consumer-facing booking wrappers**. Industry publications (Hospitality Net, Skift, PhocusWire) are declaring "2026 is the year of MCP" for hotels. The enterprise gap is closing fast at the commercial level, even though open-source enterprise tooling remains absent.

## What's Missing

The hospitality MCP ecosystem has narrowed dramatically since March 2026. Enterprise platforms are arriving commercially, but open-source gaps remain:

- **No open-source PMS or CRS servers** — Apaleo, Aven/Sabre, and Agentic Hospitality all offer MCP but as proprietary products. Oracle Hospitality/OPERA, Mews ($2.5B valuation), Cloudbeds, and Guesty have no MCP presence at all.
- **No revenue management** — no dynamic pricing, demand forecasting, or rate optimization servers (open or proprietary)
- **No guest experience platforms** — Revinate, TrustYou, ReviewPro for reputation management
- **No event/conference venue management** — Cvent, Social Tables, Tripleseat for event planning
- **No open-source housekeeping/maintenance** — Apaleo's commercial MCP covers some housekeeping coordination, but nothing self-hostable
- **No dedicated tours/activities** — Viator, GetYourGuide, Klook have no general-purpose MCP servers (only a Hawaii-specific niche server exists)
- **No Hyatt or IHG standalone servers** — only Gondola (hosted, not open source) covers these chains

The enterprise gap is closing — but almost exclusively through proprietary commercial platforms, not open-source tools.

## The Bottom Line

Hospitality MCP servers earn **4.0/5** (up from 3.5). The category saw remarkable growth in just six weeks: server count jumped from 25+ to 40+, three major gaps were filled (food delivery, hotel loyalty programs, price comparison), and the first enterprise PMS integration appeared.

**Strider Labs is the story of this refresh** — a single developer (markswendsen-code) shipped Marriott Bonvoy, Hilton Honors, DoorDash, OpenTable, Booking.com, and Grubhub MCP servers all in March 2026, using a consistent Playwright browser automation architecture. While individual star counts are low, the npm download numbers (395/week for DoorDash) show real usage.

**The travel planning space transformed** with borski/travel-hacking-toolkit (436 stars) — a comprehensive points/miles optimization toolkit that integrates 22+ tools across dozens of travel services. It joins mcp-server-airbnb (437 stars) as the category's co-leader.

**The demand signal is clear**: uber-eats-mcp-server hit 221 stars as a bare POC, proving that food delivery automation is one of the most wanted MCP use cases. ExpediaGroup publishing an official server (18 stars) adds commercial credibility.

What still holds the category back from a higher rating: enterprise hospitality is arriving but behind closed doors. Aven/Sabre (35,000+ hotels), SiteMinder (53,000 hotels), Agentic Hospitality, and Apaleo have all launched or announced MCP integrations — but all are proprietary commercial products with no open-source repos. Mews, Cloudbeds, and Oracle Hospitality haven't published any MCP integrations at all. Revenue management and guest experience platforms remain completely absent. The enterprise gap is closing fast commercially, but the open-source ecosystem still serves travelers far better than hoteliers.

*This review was refreshed on 2026-04-27 using Claude Opus 4.6 (Anthropic). Original review published 2026-03-15.*

