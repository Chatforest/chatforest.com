---
title: "Hospitality & Hotels MCP Servers — Airbnb Search, Hotel Booking, Restaurant Reservations, and Travel Planning"
date: 2026-03-15T23:00:00+09:00
description: "Hospitality and hotel MCP servers are a fast-growing category with 40+ servers across 8 subcategories."
og_description: "Hospitality & Hotels MCP servers: mcp-server-airbnb (509 stars), travel-hacking-toolkit (626 stars, 42 skills, points/miles), uber-eats-mcp (235 stars demand signal), ExpediaGroup official (21 stars), Strider Labs ships Marriott/Hilton/DoorDash/Booking.com/OpenTable/Grubhub MCPs, Aven Hospitality (formerly Sabre Hospitality Solutions) MCP for 35K+ hotels, SiteMinder MCP for 53K hotels, Apaleo PMS first enterprise MCP, him229/stays Google Hotels per-OTA rates. 40+ servers reviewed. Rating: 4.0/5."
content_type: "Review"
card_description: "Hospitality and hotel MCP servers for AI-powered accommodation search, hotel booking, restaurant reservations, travel planning, and review platform access. **Refreshed April 2026, re-audited August 2026** — the category saw explosive growth, with server count jumping from 25+ to 40+ in six weeks. **Strider Labs emerges as the dominant player** — shipping DoorDash, OpenTable, Grubhub, Marriott Bonvoy, and Hilton Honors MCP servers in a single March 2026 sprint, all using Playwright browser automation with consistent architecture. **Three former gaps filled**: food delivery (DoorDash + Uber Eats), hotel loyalty programs (Marriott Bonvoy + Hilton Honors + Gondola multi-chain), and hotel price comparison (him229/stays shows per-OTA rates from Booking/Expedia/Hotels.com/Trip.com via reverse-engineered Google Hotels RPC). **Travel planning leaps forward** — borski/travel-hacking-toolkit (626 stars, 42 skills, 6 MCP servers) is the new category co-leader alongside mcp-server-airbnb (509 stars), offering points/miles optimization across 27 mileage programs with Skiplagged, Kiwi, Trivago, Airbnb, Google Flights, and more. **Official vendor presence grows** — ExpediaGroup publishes expedia-travel-recommendations-mcp (21 stars, 4 tools for hotels/flights/activities/cars). **First PMS integration appears** — Apaleo MCP (alpha, 29 tools via Composio) is the first property management system to offer MCP access, cracking open the enterprise hospitality gap. **Uber Eats demand signal is massive** — ericzakariasson/uber-eats-mcp-server has 235 stars despite being a bare proof-of-concept with 5 commits, proving food delivery automation is one of the most wanted MCP use cases. **Restaurant reservation tools expand** — new OpenTable-specific MCP via Strider Labs (5 tools) and Apify's Resy Booker (6 tools, pay-per-action) join the existing Resy+OpenTable unified search server. **Consumer side now excellent** — the full traveler journey from accommodation search through booking, dining, activities, loyalty points, and rate comparison is well-covered. **Enterprise gap narrowing but still wide** — Apaleo is the only PMS vendor with MCP, and Oracle Hospitality, Mews, Cloudbeds, and Guesty remain absent. No revenue management, no channel managers, no housekeeping operations. Rating upgraded to **4.0/5** — three major consumer gaps filled and first enterprise integration arriving moves the category firmly into practical utility territory."
last_refreshed: 2026-08-15
sources_audited: 2026-08-15
category_url: "/categories/lifestyle-personal/"
---

Hospitality and hotel MCP servers let AI assistants search for accommodations, book hotels, make restaurant reservations, discover local dining options, and plan trips. Instead of juggling multiple booking sites and review platforms, these servers let AI agents handle the full hospitality workflow — from finding a place to stay to booking a table for dinner — all through the Model Context Protocol.

This review covers the **hospitality and hotels** vertical — vacation rentals, hotel booking, restaurant reservations, review platforms, and travel planning. For broader travel infrastructure like flights and transit, see our travel-adjacent reviews. For event and conference management, see our [Event Management & Ticketing MCP review](/reviews/event-management-ticketing-mcp-servers/).

The headline findings: **Travel hacking toolkit matches Airbnb** as co-leader at 626 stars. **Strider Labs ships 6 consumer hospitality servers** in a single sprint. **Three major gaps filled** — food delivery, hotel loyalty programs, and per-OTA rate comparison. **Uber Eats POC hits 235 stars** proving massive demand. **Enterprise hospitality goes MCP** — [Aven Hospitality](https://www.avenhospitality.com/insights/aven-hospitality-announces-mcp-enablement) (formerly Sabre Hospitality Solutions, 35,000+ hotels via SynXis), [SiteMinder](https://www.siteminder.com/news/siteminder-ai-hotel-distribution/) (53,000 hotels), [Agentic Hospitality](https://www.hospitalitynet.org/news/4131210/agentic-hospitality-launches-travelos-mcp-server-enabling-agentic-hotel-distribution-inside-ai-platforms), and [Apaleo](https://apaleo.com/blog/apaleo-news/apaleo-launches-mcp-server) all launch or announce MCP integrations. **ExpediaGroup goes official.** Rating upgraded from **3.5 to 4.0/5**.

## Vacation Rentals

### openbnb-org/mcp-server-airbnb

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [openbnb-org/mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb) | 509 | TypeScript | MIT | 2 |

The **most popular hospitality MCP server** — searches Airbnb listings by scraping the website HTML rather than using an official API:

- **airbnb_search** — search listings with filters for location, check-in/check-out dates, guest count, price range, and pagination
- **airbnb_listing_details** — get comprehensive details for a specific listing including amenities, house rules, location coordinates, and direct booking links

Packaged as a Desktop Extension (DXT) for one-click install with compatible AI clients. No API key needed — it constructs search URLs, fetches the HTML, and extracts structured data. This is clever but fragile — any Airbnb HTML changes could break it.

The approach means no authentication, no rate limiting concerns, and no cost. But it also means no booking capability — you can search and explore, but completing a reservation requires visiting Airbnb directly. Not affiliated with Airbnb, Inc.

*Updated April 2026: 393→437 stars (+11%). No new releases or tools added since v0.2.0 (transitioned to MCP Bundle format). Steady growth but development has slowed.* **Update (2026-08-15 audit): 437→[509 stars](https://github.com/openbnb-org/mcp-server-airbnb)** — growth continued through the summer; still MIT-licensed, still 2 tools, no new releases found.

### Other Airbnb Implementations

- **[Domoteek/mcp-server-airbnb](https://github.com/Domoteek/mcp-server-airbnb)** (JavaScript, MIT, 1 star) — a fork of openbnb-org's server with search and detail tools, plus an `ignore_robots_txt` option
- **[vedantparmar12/airbnb-mcp](https://github.com/vedantparmar12/airbnb-mcp)** (1 star) — adds LiveKit voice interaction support and both HTTP and STDIO transport
- **[akktrsst/MCP_Agent_Airbnb](https://github.com/akktrsst/MCP_Agent_Airbnb)** (6 stars, MIT) — AI-powered property search with Gradio chatbot UI, GPT-4o-mini + LangChain

## Hotel Booking

### Jinko (formerly jinkoso/jinko-mcp) — repo taken down

**Correction (2026-08-15 audit):** the original `jinkoso/jinko-mcp` repository this section described now [404s on GitHub](https://github.com/jinkoso/jinko-mcp) — it has been deleted, not just renamed. The `jinkoso` GitHub org still exists but no longer lists this repo among its public projects. A community fork, [dumyCq/jinko-mcp](https://github.com/dumyCq/jinko-mcp) (1 star, no listed license), preserves the original code and its README notes the upstream repo "is no longer available on GitHub." The company itself is alive and has rebranded: it now operates at [gojinko.com](https://gojinko.com/), advertising "MCP & API" access as part of a broader travel-infrastructure platform (flights, trains, activities) rather than a standalone hotel-booking repo, and now claims **2.6M+ hotels** (up from the "2M+" this section originally cited). No public tool count or star count is available for the current MCP offering since it isn't an open GitHub repo.

Previously documented tools (per the surviving fork): **find_place** (location text to coordinates), **search_hotels** (coordinate-based search with dates/guests/facility filters), **get_hotel_details**, and **book_hotel** (creates a booking quote and payment link). Whether these still match Jinko's current commercial MCP offering is unverified — treat this as historical, not current, documentation. Commercial API key required from [gojinko.com](https://gojinko.com/).

### him229/stays — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [him229/stays](https://github.com/him229/stays) | 10 | — | MIT | 3 |

A **Google Hotels aggregator** that shows per-OTA rates — the first MCP server to enable hotel price comparison across booking platforms:

- **search_hotels** — search hotels by location
- **get_hotel_details** — get detailed hotel info with rates from multiple OTAs
- **search_hotels_with_details** — combined search and detail retrieval

The key innovation: reverse-engineers Google Hotels' `batchexecute` RPC (no scraping) to show real-time prices from Booking.com, Expedia, Hotels.com, Trip.com, and others with deep-links to each OTA. Supports both MCP stdio and streamable HTTP transport. 330 tests. This fills a significant gap — previously, comparing prices across booking platforms required visiting each one individually.

### mcp-marriott (Strider Labs) — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markswendsen-code/mcp-marriott](https://github.com/markswendsen-code/mcp-marriott) | 8 | TypeScript | — | 16 |

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
| [Gondola MCP](https://www.gondola.ai/mcp) (hosted at mcp.gondola.ai) | — | — | — | 6 |

A **multi-chain hotel search service** covering Marriott, Hilton, Hyatt, IHG, Accor, Wyndham, and more:

- **search_hotels** / **compare_rates** / **get_hotel_details** — cross-chain hotel search and comparison
- **book_hotel** / **get_booking_link** — booking with direct links to preserve loyalty status
- **create_rate_alert** — price monitoring

Free to use, no API key required for search. Supports member rates, AAA discounts, and points redemption comparisons — surfacing rates other travel APIs don't expose. Not open source — hosted service only. Notable because it's the only way to search Hyatt, IHG, Accor, and Wyndham via MCP, where no standalone servers exist.

### ExpediaGroup/expedia-travel-recommendations-mcp — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ExpediaGroup/expedia-travel-recommendations-mcp](https://github.com/ExpediaGroup/expedia-travel-recommendations-mcp) | 21 | — | Apache-2.0 | 4 |

The **official Expedia Group MCP server** — recommendations for hotels, flights, activities, and car rentals. Supports stdio and streamable HTTP transport. [v1.0.2 released August 28, 2025](https://github.com/ExpediaGroup/expedia-travel-recommendations-mcp/releases).

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
| [markswendsen-code/mcp-booking](https://github.com/markswendsen-code/mcp-booking) | 5 | TypeScript | — | 14 |

**Full Booking.com workflow** via browser automation:

- **search** / **get_property** / **check_availability** / **get_prices** — hotel discovery
- **filter** / **sort** / **save** — search refinement
- **book** / **get_reservations** / **cancel** — booking lifecycle
- **get_reviews** — guest reviews
- **login** / **logout** / **status** — session management

Uses Playwright with cookie-based sessions. Created March 2026. The most feature-rich Booking.com MCP server, far surpassing the earlier esakrissa/hotels_mcp_server (2 tools). Part of Strider Labs' suite.

### Other Hotel Servers

- **woodstocksoftware/hotel-concierge-mcp** (Python, 7 tools) — hotel concierge simulation on SQLite; reference implementation for PMS integration
- **[esakrissa/hotels_mcp_server](https://github.com/esakrissa/hotels_mcp_server)** (28 stars, Python, 2 tools) — basic Booking.com API via RapidAPI; 4 commits, stale since March 2025
- **EmilyThaHuman/booking-mcp-server** (TypeScript) — Booking.com search with ChatGPT Apps SDK widgets
- **corneyc/hotels-mcp** — Cloudflare Worker for Hotels.com via RapidAPI

## Restaurant Reservations

### jrklein343-svg/restaurant-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jrklein343-svg/restaurant-mcp](https://github.com/jrklein343-svg/restaurant-mcp) | 4 | TypeScript | — | 11 |

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
| [markswendsen-code/mcp-opentable](https://github.com/markswendsen-code/mcp-opentable) | 1 | TypeScript | — | 5 |

**OpenTable-specific** browser automation:

- **search** / **details** / **availability** — restaurant discovery
- **reserve** / **booking_history** — make and track reservations

Part of Strider Labs' suite, distributed as [`@striderlabs/mcp-opentable`](https://www.npmjs.com/package/@striderlabs/mcp-opentable) on npm — currently ~39 weekly downloads (down from a vendor-reported 187/week snapshot in April 2026; per-package download counts on npm fluctuate week to week). The vendor's README claims an "85%+ task completion rate," which is a self-reported, unverified figure — no independent benchmark was found. Created March 2026. A simpler alternative to restaurant-mcp for users who only need OpenTable.

### Resy Booker (Apify) — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Apify clearpath/resy-booker](https://apify.com/clearpath/resy-booker) | — | — | — | 6 |

A **pay-per-action Resy automation** on the Apify platform:

- Search restaurants, check availability, book slots, view/cancel reservations, login
- Streamable HTTP transport, compatible with Claude and ChatGPT
- No self-hosting required — runs on Apify infrastructure

A different model from the self-hosted servers — pay for each action rather than running your own infrastructure. Good for occasional use without the setup overhead.

### Other Restaurant Servers

**Correction (2026-08-15 audit):** this section previously listed `musemen/resy-mcp-server` (encrypted token storage, waitlist management, calendar integration). That repository now [404s on GitHub](https://github.com/musemen/resy-mcp-server) — it appears to have been deleted, and no fork or successor could be found (only stale third-party marketplace listings that still point at the dead URL) — so it has been removed rather than corrected.

- **[samwang0723/mcp-booking](https://github.com/samwang0723/mcp-booking)** (16 stars, Go, 5 tools) — Google Maps Places API for restaurant discovery with mood-based filtering and event-specific matching. 65 commits, actively maintained. Default location centered on Taiwan.

## Food Delivery — NEW CATEGORY

### ericzakariasson/uber-eats-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ericzakariasson/uber-eats-mcp-server](https://github.com/ericzakariasson/uber-eats-mcp-server) | 235 | Python | — | — |

A **proof-of-concept Uber Eats automation** that has become the strongest demand signal in the hospitality MCP space. 235 stars with only 5 commits and minimal documentation — the star count reflects how badly people want food delivery automation via AI agents, not the maturity of this particular implementation.

Uses Playwright browser automation. WIP status with no documentation on available tools. But the adoption signal is unmistakable: this is one of the most-wanted MCP use cases.

### mcp-doordash (Strider Labs) — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markswendsen-code/mcp-doordash](https://github.com/markswendsen-code/mcp-doordash) | 6 | TypeScript | — | 4 |

The **first functional food delivery MCP server**:

- **search** — find restaurants on DoorDash
- **browse menus** — view menu items and prices
- **place orders** — complete the ordering workflow
- **track orders** — monitor delivery status

Uses Playwright browser automation with persistent sessions. Distributed as [`@striderlabs/mcp-doordash`](https://www.npmjs.com/package/@striderlabs/mcp-doordash) on npm — currently ~69 weekly downloads (down from a vendor-reported 395/week snapshot in April 2026). No public DoorDash API exists, so browser automation is the only path. Created March 2026.

### Grubhub MCP (Strider Labs) — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markswendsen-code/mcp-grubhub](https://github.com/markswendsen-code/mcp-grubhub) | 1 | TypeScript | MIT | 15 |

**Correction (2026-08-15 audit):** this section previously said no public GitHub repo could be found for the Grubhub server. That was wrong — it's public at [markswendsen-code/mcp-grubhub](https://github.com/markswendsen-code/mcp-grubhub) (1 star, MIT license, 15 tools across authentication, ordering, and order tracking). Released March 10, 2026 — browser automation for Grubhub search, menus, cart management, ordering, and delivery tracking, using the same Playwright approach as the rest of Strider Labs' suite.

## Review & Discovery Platforms

### Yelp/yelp-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Yelp/yelp-mcp](https://github.com/Yelp/yelp-mcp) | 26 | TypeScript | Apache-2.0 | 1 |

The **official first-party Yelp MCP server** — connects to Yelp's Fusion AI API with a single conversational tool:

- Natural language search — ask questions like "best sushi near me" rather than constructing filter queries
- Multi-turn conversations — refine queries with follow-up questions
- Direct business queries — ask about specific businesses without a prior search
- Conversational reservations — explore availability and book restaurant tables through natural language

This is significant because it's official — maintained by Yelp, not a community scraper. Requires a Yelp Fusion AI API key.

*Updated April 2026: No commits since July 2025 — 9+ months without activity despite being the only official first-party offering in the category. 24 stars but appears neglected.* **Correction (2026-08-15 audit):** this was wrong even measured from April 2026, and is more clearly wrong now — [the repo's commit history](https://github.com/Yelp/yelp-mcp/commits/main) shows a commit ("Add security review workflow") on April 2, 2026, after two initial commits in July 2025. It is not neglected; it's a low-commit-volume repo with sparse but real maintenance. 26 stars as of this audit.

### pab1it0/tripadvisor-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pab1it0/tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp) | 62 | Python | MIT | 5 |

Access to **TripAdvisor's Content API** for location discovery and reviews:

- **search_locations** — search for hotels, restaurants, attractions on TripAdvisor
- **search_nearby_locations** — coordinate-based nearby search
- **get_location_details** — detailed information about specific locations
- **get_location_reviews** — retrieve reviews for locations
- **get_location_photos** — photos for locations

The tool list is configurable — choose which tools to expose to your MCP client. Unofficial community implementation with Docker support.

*Updated April 2026: 46→54 stars (+17%). Steady organic growth.* **Update (2026-08-15 audit): 54→[62 stars](https://github.com/pab1it0/tripadvisor-mcp)** — growth continues.

## Travel Planning

### borski/travel-hacking-toolkit — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [borski/travel-hacking-toolkit](https://github.com/borski/travel-hacking-toolkit) | 626 | — | MIT | — |

The **most comprehensive travel MCP toolkit** and the new co-leader of the hospitality category. **Update (2026-08-15 audit):** the [README](https://github.com/borski/travel-hacking-toolkit/blob/main/README.md) now describes a larger toolkit than this section originally documented — 42 skills, not 16, are installed by the plugin command:

- **6 MCP servers** (5 free — Skiplagged, Kiwi, Trivago, Ferryhopper, Airbnb — plus LiteAPI which needs an API key) and **42 skills**
- Points/miles optimization via Seats.aero, which searches award availability across **27 mileage programs**
- Also integrates Duffel, Google Flights, Southwest, Chase Travel, Amex Travel, AwardWallet, TripAdvisor, and more via additional skills
- Drop-in skills/plugins for Claude Code, OpenCode, and Codex

This is a paradigm shift for travel MCP — rather than individual servers for each platform, this toolkit orchestrates across dozens of travel services with a focus on finding the best deals using points, miles, and hidden-city ticketing. 626 stars and 62 forks as of this audit, up from 585 stars and 32 forks in April 2026.

### skarlekar/mcp_travelassistant

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [skarlekar/mcp_travelassistant](https://github.com/skarlekar/mcp_travelassistant) | 56 | Python | — | 6 servers |

A **suite of 6 specialized MCP servers** for end-to-end travel planning:

1. **Flight Search Server** — find and compare flights, analyze pricing, filter by preferences
2. **Hotel Search Server** — discover accommodations, compare amenities, filter by budget
3. **Event Search Server** — find local events, festivals, and activities
4. **Geocoder Server** — convert locations to coordinates, calculate distances, reverse geocoding
5. **Weather Search Server** — get forecasts, current conditions, weather alerts
6. **Finance Search Server** — currency conversion, exchange rates, financial analysis

Requires API keys for SerpAPI (flights, hotels, events, finance), OpenWeatherMap or National Weather Service (weather), and OpenStreetMap Nominatim (geocoder). 56 stars and 12 forks as of this audit. **Correction (2026-08-15 audit):** previously said "appears dormant since January 2025" — the [actual commit history](https://github.com/skarlekar/mcp_travelassistant/commits/main) shows the last commit was June 19, 2025, not January 2025. Still stale (14+ months as of this audit), but the date was wrong.

### abhinavmathur-atlan/mcp-travel-assistant — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [abhinavmathur-atlan/mcp-travel-assistant](https://github.com/abhinavmathur-atlan/mcp-travel-assistant) | 6 | — | MIT | 18 |

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
- **[gs-ysingh/travel-mcp-server](https://github.com/gs-ysingh/travel-mcp-server)** (14 stars, 5 tools) — flights, accommodation, exchange rates, weather, trip budget
- **hirochachacha/rakuten_travel_mcp** (Japan-focused, 2 tools) — Rakuten Travel hotel search for Japan

## Enterprise Hospitality & Distribution — NEW CATEGORY

The enterprise side of hospitality MCP went from completely absent to rapidly emerging in Q1-Q2 2026. Multiple major platforms announced or launched MCP integrations, though all are proprietary/commercial with no open-source repos.

### Agentic Hospitality — TravelOS MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Agentic Hospitality TravelOS (commercial) | — | — | Proprietary | — |

Claims the **industry's first hotel MCP booking transaction** — press coverage (independent of the company) confirms the claim was made and describes the specific booking: a five-unit short-term rental (Rose St. Gardens, Roseau, Dominica) booked via a ChatGPT app request, matched and confirmed through TravelOS MCP. Connects hotel CRS/PMS systems directly to AI platforms (ChatGPT, Claude). Enables real-time availability, rates, and inventory surfacing inside AI assistants. Includes an "Agentic Booking Engine" overlay for conversational booking flows. Launched March 2026. No public GitHub repo — commercial platform only. Sources: [Hospitality Net](https://www.hospitalitynet.org/news/4131210/agentic-hospitality-launches-travelos-mcp-server-enabling-agentic-hotel-distribution-inside-ai-platforms), [Hotel Online](https://www.hotel-online.com/news/agentic-hospitalitys-travelos-mcp-chatgpt-app-is-putting-brands-not-intermediaries-at-the-center-of-ai-bookings).

### Aven Hospitality (formerly Sabre Hospitality Solutions) — MCP Enablement

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Aven Hospitality MCP (commercial) | — | — | Proprietary | — |

**Correction (2026-08-15 audit):** this section previously attributed this MCP integration to "Sabre." That's stale — [TPG closed its acquisition of Sabre's Hospitality Solutions business for $1.1 billion on July 3, 2025](https://www.prnewswire.com/news-releases/aven-hospitality-launches-to-continue-shaping-future-of-hospitality-technology-302669325.html), and the unit rebranded as **Aven Hospitality** on January 27, 2026 — before this MCP announcement. Sabre Corporation no longer owns this business; [sabre.com/hospitality no longer resolves](https://www.sabre.com/hospitality/). It's Aven Hospitality, not Sabre, that is embedding MCP into the [SynXis Central Reservation System and Booking Engine](https://www.avenhospitality.com/insights/aven-hospitality-announces-mcp-enablement), serving **35,000+ hotels globally** (not the "40,000+" this section originally claimed) — the platform still traces to Sabre's original SynXis acquisition, but the operating company is now independent. Hotels can expose official rates, availability, and amenities to AI-driven discovery surfaces without custom integrations. An MCP Early Access Programme with select hotel chains is scheduled for Q2 2026. No public GitHub repo — enterprise product. Sources: [Aven Hospitality](https://www.avenhospitality.com/insights/aven-hospitality-announces-mcp-enablement), [Hotel Management Network](https://www.hotelmanagement-network.com/news/aven-hospitality-enables-mcp-hotel/).

### SiteMinder — MCP-Powered AI Distribution

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| SiteMinder MCP (commercial) | — | — | Proprietary | — |

The **first channel manager with MCP integration** — uses MCP to deliver real-time hotel data from its **53,000-hotel inventory across 150 countries** to AI systems. "Demand Plus" extended beyond metasearch (Google, Trivago, TripAdvisor) into AI conversational environments (ChatGPT, Claude). "Channels Plus" gives AI-enabled OTAs access to SiteMinder's inventory. DirectBooker is the first AI demand partner. Announced April 2026. No public GitHub repo — commercial platform. Sources: [SiteMinder's own announcement](https://www.siteminder.com/news/siteminder-ai-hotel-distribution/), [PhocusWire](https://www.phocuswire.com/news/technology/siteminder-links-hotel-inventory-ai-booking-channels-mcp).

This directly fills the "no channel managers" gap from the original review — though only as a proprietary offering, not an open-source tool.

### Apaleo MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Apaleo MCP (via Composio) | — | — | — | 29 |

The **first property management system to offer MCP integration**, per [Apaleo's own announcement](https://apaleo.com/blog/apaleo-news/apaleo-launches-mcp-server) and corroborating trade coverage from [HFTP](https://www.hftp.org/news/4129031/apaleo-becomes-first-property-management-platform-to-launch-mcp-server-bridging-ai-agents-with-hotel-systems) and [PhocusWire](https://www.phocuswire.com/apaleo-mcp-server-launch-hospitality-property-management):

- AI agents can check availability, modify bookings, coordinate housekeeping, create payment links
- Includes an AI Copilot for check-ins, room assignments, and housekeeping
- Property creation, cloning, unit management, bulk operations
- Available via [Composio integration](https://mcp.composio.dev/apaleo) at composio.dev

Apaleo is a cloud-native PMS used by boutique and lifestyle hotels. The server is currently in alpha. No public GitHub repo yet.

### Enterprise Assessment

The pattern is clear: **enterprise hospitality platforms are building proprietary MCP servers** (Agentic Hospitality, Aven Hospitality/formerly Sabre, SiteMinder, Apaleo) while **open-source GitHub repos remain mostly consumer-facing booking wrappers**. Industry publications ([Hospitality Net](https://www.hospitalitynet.org/), [Skift](https://skift.com/), [PhocusWire](https://www.phocuswire.com/)) are covering multiple such launches in 2026. The enterprise gap is closing fast at the commercial level, even though open-source enterprise tooling remains absent.

## What's Missing

The hospitality MCP ecosystem has narrowed dramatically since March 2026. Enterprise platforms are arriving commercially, but open-source gaps remain:

- **No open-source PMS or CRS servers** — Apaleo, Aven Hospitality (formerly Sabre), and Agentic Hospitality all offer MCP but as proprietary products. Oracle Hospitality/OPERA, Mews, Cloudbeds, and Guesty have no MCP presence at all.
- **No revenue management** — no dynamic pricing, demand forecasting, or rate optimization servers (open or proprietary)
- **No guest experience platforms** — Revinate, TrustYou, ReviewPro for reputation management
- **No event/conference venue management** — Cvent, Social Tables, Tripleseat for event planning
- **No open-source housekeeping/maintenance** — Apaleo's commercial MCP covers some housekeeping coordination, but nothing self-hostable
- **No dedicated tours/activities** — Viator, GetYourGuide, Klook have no general-purpose MCP servers (only a Hawaii-specific niche server exists)
- **No Hyatt or IHG standalone servers** — only Gondola (hosted, not open source) covers these chains

The enterprise gap is closing — but almost exclusively through proprietary commercial platforms, not open-source tools.

## The Bottom Line

Hospitality MCP servers earn **4.0/5** (up from 3.5). The category saw remarkable growth in just six weeks: server count jumped from 25+ to 40+, three major gaps were filled (food delivery, hotel loyalty programs, price comparison), and the first enterprise PMS integration appeared.

**Strider Labs is the story of this refresh** — a single developer (markswendsen-code) shipped Marriott Bonvoy, Hilton Honors, DoorDash, OpenTable, Booking.com, and Grubhub MCP servers all in March 2026, using a consistent Playwright browser automation architecture. Individual star counts are low, and the npm download numbers have come down since an April 2026 peak (69/week for DoorDash as of this audit, down from a vendor-reported 395/week snapshot) — real but modest usage.

**The travel planning space transformed** with borski/travel-hacking-toolkit (626 stars) — a comprehensive points/miles optimization toolkit with 6 MCP servers and 42 skills spanning dozens of travel services. It joins mcp-server-airbnb (509 stars) as the category's co-leader.

**The demand signal is clear**: uber-eats-mcp-server hit 235 stars as a bare POC, proving that food delivery automation is one of the most wanted MCP use cases. ExpediaGroup publishing an official server (21 stars) adds commercial credibility.

What still holds the category back from a higher rating: enterprise hospitality is arriving but behind closed doors. Aven Hospitality (formerly Sabre Hospitality Solutions, 35,000+ hotels), SiteMinder (53,000 hotels), Agentic Hospitality, and Apaleo have all launched or announced MCP integrations — but all are proprietary commercial products with no open-source repos. Mews, Cloudbeds, and Oracle Hospitality haven't published any MCP integrations at all. Revenue management and guest experience platforms remain completely absent. The enterprise gap is closing fast commercially, but the open-source ecosystem still serves travelers far better than hoteliers.

*This review was refreshed on 2026-04-27 using Claude Opus 4.6 (Anthropic); claim-level citation audit completed 2026-08-15. Original review published 2026-03-15.*
