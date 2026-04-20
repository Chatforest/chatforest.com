# MCP and Travel/Tourism: How AI Agents Connect to Flights, Hotels, Maps, Railways, Reviews, Weather, Translation, and Trip Planning

> A comprehensive guide to MCP integrations for travel and tourism — covering flight search (Google Flights 364 stars, Amadeus, Duffel), hotels (Airbnb 406 stars, Booking.com


Travel and tourism is one of the most commercially significant corners of the MCP ecosystem. With 76+ community and official MCP servers covering flights, hotels, maps, railways, reviews, weather, translation, and currency conversion, it represents one of the richest collections of real-world integrations available through the protocol. The ecosystem includes official servers from Mapbox, Baidu Maps, Expedia, DeepL, Yelp, and Stadia Maps — alongside hundreds of community implementations.

This commercial momentum reflects a structural reality: travel planning is an inherently multi-source problem. Booking a single trip might require checking flight prices across airlines, comparing hotel options, researching destinations, checking weather forecasts, calculating currency conversions, finding restaurants, and navigating unfamiliar transit systems. Each of these tasks currently requires a separate app, website, or API. MCP servers that expose each data source through a standard protocol allow AI agents to orchestrate the entire planning workflow — creating the unified travel intelligence layer that no single platform provides.

This guide is research-based. We survey what MCP servers exist for travel and tourism, what capabilities they offer, and how they can be combined into useful architectures. We do not claim to have tested or used any of these servers hands-on. [Rob Nugen](https://robnugen.com), the operator of this site, has established ChatForest as a research and documentation resource for the AI ecosystem. For background on MCP itself, see our [introduction to MCP](/guides/what-is-mcp/) and the [MCP server directory](/guides/best-mcp-servers/).


## Why Travel and Tourism Needs MCP

Four structural problems in the travel industry explain why a standard protocol matters.

**Multi-source comparison is the default workflow.** No single platform consistently offers the best price, the best selection, or the most accurate information across flights, hotels, and activities. Experienced travelers routinely check Google Flights, Skyscanner, airline direct sites, hotel aggregators, and specialty booking platforms before making a decision. An AI agent with MCP access to multiple flight and hotel search servers can automate this comparison — querying Duffel, Amadeus, Google Flights, and airline-specific sources simultaneously through the same protocol.

**Context-dependent planning.** Useful travel recommendations require understanding destination weather, local transit options, cultural events, visa requirements, currency exchange rates, health advisories, and personal preferences. A human travel agent synthesizes all of this intuitively. An AI travel agent needs programmatic access to each data source. MCP servers that expose weather APIs, maps, translation services, event databases, and booking platforms allow agents to make contextually appropriate recommendations.

**Language and navigation barriers.** International travel creates immediate practical challenges: reading menus, asking for directions, understanding transit systems, converting currencies, and navigating unfamiliar cities. MCP servers for translation (DeepL), maps (Google Maps, Baidu Maps, Mapbox), local transit (NS Dutch Railways, Japanese train routes, Hong Kong transport), and currency conversion address these needs directly — giving AI agents the tools to serve as real-time travel companions.

**Information fragmentation across booking stages.** A single trip generates information across multiple platforms: confirmation emails, boarding passes, hotel reservations, restaurant bookings, activity tickets, transit cards, and travel insurance policies. MCP servers that connect to these systems allow AI agents to maintain a unified view of the entire itinerary, track changes, and proactively alert travelers to disruptions.


## Flight Search and Booking

Flight search is the most developed category in the travel MCP ecosystem, with 20+ servers covering major booking APIs, airline-specific integrations, and real-time flight tracking.

### Google Flights Integrations

**punitarani/fli** (364 stars, Python) is the most popular flight search MCP server. It provides direct API interaction with Google Flights through a reverse-engineered interface — no scraping required. The project functions both as an MCP server and a standalone Python library for flight search.

**smamidipaka6/flights-mcp-server** (21 stars, 4 tools) offers structured access to Google Flights data with specialized tools: `get_general_flights_info` for comprehensive results, `get_cheapest_flights` for budget optimization, `get_best_flights` for quality ranking, and `get_time_filtered_flights` for schedule-constrained searches.

**arjunprabhulal/mcp-flight-search** (41 stars, 2 tools) uses SerpAPI's Google Flights integration for one-way and round-trip searches with server status monitoring. **salamentic/google-flights-mcp** (16 stars) provides travel agent-level flight planning using the fast-flights API.

### Professional Travel APIs

**ravinahp/flights-mcp** (177 stars, Duffel API) connects to the Duffel flight booking platform, supporting one-way, round-trip, and multi-city searches with multi-day flexible date queries. Duffel provides free search access across hundreds of airlines, making this a practical choice for prototype travel agents. A TypeScript alternative exists at **clockworked247/flights-mcp-ts** (4 stars).

**donghyun-chae/mcp-amadeus** (50 stars, Amadeus API) integrates with the industry-standard Amadeus Flight Offers Search API, enabling natural language flight queries. Amadeus is one of the three major Global Distribution Systems (GDS) that power most airline bookings worldwide. **technicalerikchan/flight-mcp-server** (2 stars) offers an alternative Amadeus implementation.

**maratsarbasov/flights-mcp** (10 stars, Aviasales API) connects to the Aviasales flight search engine, supporting one-way, round-trip, and multi-city searches with filtering, sorting, and direct booking links. A hosted version is available at findflights.me/sse.

### Official Enterprise Servers

**ExpediaGroup/expedia-travel-recommendations-mcp** (14 stars) is the official Expedia MCP server — one of the first major online travel agencies to ship an MCP integration. It provides four endpoints covering hotel, flight, activity, and car rental recommendations through both stdio and streamable-http protocols. This is significant as a signal of enterprise adoption: Expedia was among seven launch partners for ChatGPT's MCP-based integrations.

**Kiwi.com** launched its MCP server in August 2025, becoming the first OTA to publicly ship an MCP integration. While not open-sourced on GitHub, this marked an inflection point for MCP adoption in the travel industry.

### Flight Tracking

**sunsetcoder/flightradar24-mcp-server** (46 stars, 4+ tools) provides real-time flight tracking via Flightradar24 with tools for tracking individual flights, checking arrival and departure times, monitoring airport traffic, and detecting emergency flights. **variflight/variflight-mcp** (22 stars) from the official Variflight service provides flight information, weather data, and flight comfort metrics.

**Pradumnasaraf/aviationstack-mcp** (17 stars, 9+ tools) connects to the AviationStack API for real-time and historical flight data, airline-specific queries, airport schedules, and aircraft information. The free API tier makes this accessible for experimentation.

### Flight Emissions

**abahgat/timcp** (2 stars, 6 tools) connects to Google's Travel Impact Model API for calculating flight CO2 emissions — useful for environmentally conscious travelers and Scope 3 corporate reporting.

### Airline-Specific Servers

**markswendsen-code/mcp-american** (2 stars, 15+ features) targets American Airlines specifically, offering flight search, booking management, check-in, boarding passes, AAdvantage loyalty program access, upgrade management, seat selection, and baggage tracking. It uses Playwright browser automation rather than a formal API.

### Regional Flight Search

**xiaonieli7/FlightTicketMCP** (35 stars, 8+ tools) provides comprehensive Chinese aviation coverage across 282 domestic cities and airports with route search, transfer route planning, weather integration, and real-time flight tracking. Supports SSE, stdio, and streamable-http protocols.


## Hotels and Accommodation

### Airbnb

**openbnb-org/mcp-server-airbnb** (406 stars) is the highest-starred accommodation MCP server. It enables searching Airbnb listings without requiring an API key, respecting robots.txt for ethical access. The project's popularity reflects the demand for AI-powered vacation rental search.

### Booking Platforms

**esakrissa/hotels_mcp_server** (15 stars, 2 tools, Booking.com API) connects to Booking.com via RapidAPI for destination search and hotel listings with room details, pricing, and ratings.

**WinWin-travel/MCP-server** (1 star) is an enterprise-grade server providing access to 3M+ hotel inventory with 500+ attribute filters and up to 10% cashback on bookings. It runs as a fully hosted service requiring no local setup.

**Fast-Transients/lodgify-mcp-server** (2 stars, 7 tools) targets vacation rental property managers using the Lodgify platform, with tools for property management, booking creation and updates, and calendar management.

**birariro/agoda-review-mcp** (2 stars) aggregates Agoda hotel reviews, providing positive and negative sentiment analysis — useful for AI agents that need to summarize accommodation options.

**markswendsen-code/mcp-marriott** (1 star) targets Marriott hotel booking specifically, enabling AI agents to search and book through the Marriott ecosystem.

### Official Enterprise Adoption

Beyond dedicated MCP servers, the broader travel industry is integrating MCP at the platform level. Booking.com and Expedia were among seven launch partners for ChatGPT's MCP-based applications. Apaleo launched an MCP server for hotel property management in September 2025. These enterprise adoptions signal that MCP is moving from developer tooling to production travel infrastructure.


## Maps and Navigation

Maps and navigation servers form the infrastructure layer that enables location-aware travel planning. This category includes some of the highest-quality MCP integrations in the entire ecosystem, with multiple official servers from major mapping platforms.

### Official Mapping Platforms

**baidu-maps/mcp** (415 stars) is the official Baidu Map MCP server and the first map service provider in China to support MCP. It provides 10+ tools covering geocoding, reverse geocoding, POI search, route planning for driving, walking, cycling, and public transit, weather data, IP-based location detection, and real-time traffic information. Python and TypeScript SDKs are available.

**mapbox/mcp-server** (325 stars) is the official Mapbox MCP server, offering geocoding, POI search, multi-modal routing (driving, walking, cycling), travel time matrices, route optimization for multi-stop itineraries, map matching for GPS traces, isochrone generation (reachability maps), and static map rendering. A hosted endpoint is available for quick integration. The companion **mapbox/mcp-devkit-server** (44 stars) provides developer-focused tools for documentation, style management, and token management.

**stadiamaps/stadiamaps-mcp-server-ts** (21 stars) is the official Stadia Maps MCP server, covering time zone lookups, geocoding, place search (POIs), static map rendering, routing, and isochrone generation. A free API key is available.

### Google Maps Integrations

**cablate/mcp-google-map** (236 stars) provides the most comprehensive Google Maps API integration: geocoding, directions, place search, distance matrix calculations, elevation data, and time zone lookups. **Garblesnarff/google-maps-mcp** (10 stars, 14 tools) offers a broad tool set for location services, geocoding, routing, and map rendering. **Neutrollized/google-maps-mcp-server** (14 stars) and **iceener/maps-streamable-mcp-server** (19 stars) provide additional Google Maps implementations with different architectural approaches.

**GongRzhe/TRAVEL-PLANNER-MCP-Server** (96 stars) specifically targets travel planning with Google Maps integration for location search, place details, and route calculations — bridging the gap between mapping data and travel itinerary construction.

### OpenStreetMap

**NERVsystems/osmmcp** (17 stars, 13+ tools, Go) provides a comprehensive OpenStreetMap interface including geocoding, reverse geocoding, nearby POI discovery, routing and directions, category-based search, meeting point finder, EV charging station locator, commute analysis, neighborhood livability scoring, and school and parking finder. The breadth of tools makes this particularly useful for destination research and local exploration.

### Regional Mapping

**cgoinglove/mcp-server-kakao-map** (14 stars) provides Kakao Maps integration for South Korea. **peschinskiy/yandex-maps-mcp** (11 stars, 3 tools) covers Yandex Maps for Russia and CIS countries with geocoding, reverse geocoding, and map rendering as PNG images.

### Nearby Discovery

**kukapay/nearby-search-mcp** (22 stars) combines IP-based location detection with Google Places integration for nearby place searches — useful for travelers who want AI agents to find restaurants, attractions, or services relative to their current location.


## Railway and Train Systems

Railway MCP servers represent one of the most internationally diverse categories, with implementations for rail systems across China, the Netherlands, India, Japan, Spain, Belgium, and Germany.

### China — 12306

**Joooook/12306-mcp** (761 stars) is the highest-starred travel MCP server overall. It connects to China's national railway booking platform (12306.cn), which handles ticket search and booking for the world's largest high-speed rail network. The server's popularity reflects both the scale of Chinese rail travel and the complexity of the booking process that AI assistance can simplify.

### Netherlands — NS Dutch Railways

**r-huijts/ns-mcp-server** (49 stars) provides comprehensive access to Dutch Railways (NS) data: real-time departure boards, travel advice with route options, disruption alerts, pricing information, and station details. Given the density and complexity of Dutch rail networks, this is one of the most practical railway MCP integrations for daily commuters and tourists alike. **lauragift21/ns-travel-mcp** (3 stars) offers an alternative implementation with journey planning and disruption alerts.

### India — Indian Railways

**amith-vp/indian-railway-mcp** (27 stars, 6+ tools) covers Indian Railway data including train search, seat availability checking, live train status, delay information, and station/train code lookup. A hosted remote server is available for easy integration. **rajprem4214/indian-railways-mcp** (7 stars, 6 tools) offers similar coverage with live station status, train information, PNR status checking, and route information.

### Japan — Transit Routes

**tysonwu/norikae-mcp** (13 stars, 1 tool) provides Japanese train route search via Yahoo! Transit, supporting via stations, departure and arrival time preferences, and IC card fare calculations. Japan's rail network — with dozens of operators, multiple fare systems, and complex transfer patterns — is a classic case where AI-assisted route planning adds significant value.

### Spain — Renfe

**belgrano9/renfe_mcp_server** (3 stars, 3 tools) connects to Spain's Renfe rail system using GTFS (General Transit Feed Specification) data, with real-time price scraping and automatic schedule updates. Tools cover train search, price checking, and station finding. **SaberMaple1/renfe_mcp_server** (3 stars) provides a similar implementation.

### Belgium and Germany

**egemenc21/i-rail-mcp** targets Belgian railway information with real-time train schedules. **zzuisa/db-support** connects to Deutsche Bahn timetable data for German rail travel.


## Ride-Sharing and Local Transport

### Uber

**199-mcp/mcp-uber** (7 stars, 5 capabilities) provides Uber ride booking with OAuth 2.0 authentication, price estimates, ride requests, status checking, and cancellation. This enables AI agents to complete the last-mile transportation gap in trip planning. **markswendsen-code/mcp-uber** offers an alternative implementation.

### Regional Public Transit

**kennyfong19931/mcp-hk-transport-eta** provides real-time public transport estimated arrival times across Hong Kong's bus, minibus, and MTR systems. **arjunkmrm/sg-lta-mcp** connects to Singapore's Land Transport Authority for bus arrivals, train alerts, and traffic conditions. **ckorhonen/mta-mcp** provides real-time NYC subway data including arrival predictions, service status, alerts, and trip planning — available as a hosted service at subwayinfo.nyc.

These regional transit servers illustrate an important pattern: while no global transit MCP standard exists, local implementations are emerging for major travel destinations, gradually building a patchwork of AI-accessible transit data.


## Reviews and Discovery

### TripAdvisor

**pab1it0/tripadvisor-mcp** (53 stars) connects to the official TripAdvisor Content API for location data, reviews, and photos. TripAdvisor's partnership with Perplexity for end-to-end hotel booking suggests the platform is actively positioning itself for AI agent integration.

### Yelp

**Yelp/yelp-mcp** (23 stars) is the official Yelp MCP server, using the Yelp Fusion AI platform for natural language business search, multi-turn conversations, direct business queries, and restaurant reservations. The agent-to-agent communication model (`yelp_agent` tool) represents an emerging pattern where MCP servers expose AI capabilities rather than raw data.

### Restaurant Discovery

**samwang0723/mcp-booking** (14 stars, Google Maps Places API) provides restaurant discovery with smart search, mood-based filtering, event-specific matching, and booking assistance — useful for travelers who want AI recommendations that go beyond star ratings.

### Location-Based Services

**alexpriest/swarm-mcp** (3 stars) connects to Foursquare Swarm check-in data, potentially useful for AI agents that want to learn from a traveler's past visit patterns. **harimkang/mcp-korea-tourism-api** connects to South Korea's official tourism API for destination information.


## Comprehensive Trip Planning Suites

Several projects bundle multiple travel capabilities into unified planning platforms.

**skarlekar/mcp_travelassistant** (31 stars) is the most comprehensive, providing a suite of six specialized MCP servers: Flight Search, Hotel Search, Event Search, Geocoder, Weather Search, and Finance/Currency. Together they form a complete travel planning ecosystem with integrated budget management.

**gs-ysingh/travel-mcp-server** (13 stars) combines flight search, accommodation, currency exchange, weather, and trip budgeting in a single server. **abhinavmathur-atlan/mcp-travel-assistant** (5 stars) integrates Google Travel with Amadeus for AI-powered travel planning. **martinoyovo/ts-travel-mcp-server** (5 stars) provides a full-stack travel booking application with a TypeScript MCP backend.

**borski/travel-hacking-toolkit** (61 stars) takes a unique approach: AI-powered travel hacking with points, miles, and award flight optimization. For frequent travelers who manage loyalty programs across airlines and hotels, this addresses a genuine complexity challenge — finding optimal redemption strategies across programs.


## Weather for Travel

Weather data is essential context for travel planning. Several MCP servers provide the forecasting capabilities that travel agents need.

**ezh0v/weather-mcp-server** (239 stars, Go) is a lightweight weather server providing current conditions by city. **glaucia86/weather-mcp-server** (97 stars, TypeScript) offers a production-ready implementation with Docker, Redis caching, and clean architecture.

**cmer81/open-meteo-mcp** (37 stars, 10+ tools) is the most comprehensive weather MCP server, covering 7-day forecasts, historical data going back to 1940, air quality indices, marine weather (relevant for coastal and cruise travel), elevation data, and geocoding. It integrates specialized meteorological models from DWD ICON, NOAA GFS, ECMWF, JMA, and MET Norway.

**TimLukaHorstmann/mcp-weather** (32 stars, AccuWeather) provides hourly forecasts via AccuWeather's commercial API. **rossshannon/weekly-weather-mcp** (8 stars, OpenWeatherMap) offers 8-day global forecasts with morning, afternoon, and evening breakdowns plus 48-hour hourly data.


## Translation for Travel

Language barriers remain one of the biggest challenges in international travel. MCP translation servers allow AI agents to serve as real-time interpreters.

**DeepLcom/deepl-mcp-server** (95 stars) is the official DeepL MCP server, providing text translation, document translation, and text rephrasing with glossary support. The free tier offers 500,000 characters per month — sufficient for extended travel use. DeepL's translation quality, particularly for European languages, makes this one of the most practically useful travel MCP servers.

**krillinai/KlicStudioMCP** (20 stars) provides video and audio translation with subtitle generation — useful for travelers who want to understand local media or translate recorded conversations.


## Currency Conversion

**wesbos/currency-conversion-mcp** (33 stars, 4 tools, Frankfurter API) provides real-time currency conversion with tools for direct conversion, latest exchange rates, currency listings, and historical rate lookups. A hosted version is available at currency-mcp.wesbos.com. **anirbanbasu/frankfurtermcp** (6 stars, Python) offers an alternative Frankfurter API implementation using ECB (European Central Bank) reference data, available on PyPI.


## Comparison Table: Key Travel MCP Servers

| Server | Stars | Category | Key Feature | API/Data Source |
|--------|-------|----------|-------------|-----------------|
| 12306-mcp | 761 | Railway | China rail ticket search | 12306.cn |
| Baidu Maps | 415 | Maps | Official; 10+ tools, routing, POI | Baidu (official) |
| Airbnb MCP | 406 | Hotels | No API key needed | Airbnb listings |
| fli (Google Flights) | 364 | Flights | Direct API, no scraping | Google Flights |
| Mapbox MCP | 325 | Maps | Official; routing, isochrones, optimization | Mapbox (official) |
| Weather MCP | 239 | Weather | Lightweight Go server | WeatherAPI |
| Google Maps MCP | 236 | Maps | Geocoding, directions, places | Google Maps API |
| flights-mcp (Duffel) | 177 | Flights | Multi-city, flexible dates | Duffel API |
| Travel Planner | 96 | Planning | Google Maps travel integration | Google Maps |
| DeepL MCP | 95 | Translation | Official; 500K chars/month free | DeepL (official) |
| Travel Hacking | 61 | Flights | Points/miles optimization | Multiple loyalty programs |
| TripAdvisor MCP | 53 | Reviews | Official API; reviews, photos | TripAdvisor API |
| mcp-amadeus | 50 | Flights | Industry-standard GDS | Amadeus API |
| NS Dutch Railways | 49 | Railway | Real-time, pricing, disruptions | NS API |
| Flightradar24 | 46 | Tracking | Real-time flight tracking | Flightradar24 API |
| mcp-flight-search | 41 | Flights | SerpAPI Google Flights | SerpAPI |
| Open-Meteo | 37 | Weather | Historical data to 1940, marine, air quality | Open-Meteo |
| FlightTicketMCP | 35 | Flights | 282 Chinese cities/airports | Chinese aviation |
| Currency MCP | 33 | Currency | 4 tools, hosted version | Frankfurter/ECB |
| Travel Assistant Suite | 31 | Planning | 6 specialized servers | Multiple APIs |
| Indian Railway | 27 | Railway | Seat availability, live status | Indian Railways |
| Yelp MCP | 23 | Reviews | Official; NL search, reservations | Yelp Fusion AI |
| Nearby Search | 22 | Discovery | IP-based location + Places | Google Places |
| Expedia MCP | 14 | Booking | Official; hotels, flights, cars, activities | Expedia (official) |
| Norikae | 13 | Railway | Japanese train routes, IC fares | Yahoo! Transit |


## Architecture Patterns

### Pattern 1: AI Travel Agent

The most common architecture connects multiple travel MCP servers to create a conversational travel planning agent.

```
User: "Plan a 5-day trip to Tokyo in April for under $3000"

    ┌─────────────────────────┐
    │     AI Travel Agent     │
    │  (Claude / GPT / etc.)  │
    └────┬──┬──┬──┬──┬──┬────┘
         │  │  │  │  │  │
    ┌────┘  │  │  │  │  └────┐
    │       │  │  │  │       │
    ▼       ▼  ▼  ▼  ▼       ▼
 Flights  Hotels Maps Weather Currency Translation
 (Duffel) (Airbnb)(Mapbox)(Open-  (Frank- (DeepL)
          (Booking)       Meteo)  furter)
```

The agent queries flight servers for pricing and availability, hotel servers for accommodation options, weather servers for April conditions in Tokyo, currency servers for JPY conversion, and map servers for itinerary planning. It synthesizes results into a coherent trip plan with budget tracking.

### Pattern 2: Real-Time Travel Companion

This architecture supports travelers during their trip with contextual, location-aware assistance.

```
    ┌───────────────────────────┐
    │   Real-Time Companion     │
    │   (Mobile AI Assistant)   │
    └────┬──┬──┬──┬──┬──┬──────┘
         │  │  │  │  │  │
    ┌────┘  │  │  │  │  └────┐
    │       │  │  │  │       │
    ▼       ▼  ▼  ▼  ▼       ▼
  Maps   Transit Review Translation Nearby Weather
(Google (Norikae)(Yelp)  (DeepL)   Search (AccuWx)
 Maps)  (NS/MTA)(TripAd)
```

A traveler in Tokyo asks "Where should I eat near Shibuya?" The agent uses nearby search for location context, Yelp or TripAdvisor for restaurant reviews, DeepL to help interpret Japanese menus, and Norikae to plan the train route from their current location.

### Pattern 3: Multi-Modal Transport Optimizer

This architecture focuses on finding optimal routes across different transportation modes.

```
    ┌───────────────────────────┐
    │   Transport Optimizer     │
    │  (Route Planning Agent)   │
    └────┬──┬──┬──┬──┬──┬──────┘
         │  │  │  │  │  │
    ┌────┘  │  │  │  │  └────┐
    │       │  │  │  │       │
    ▼       ▼  ▼  ▼  ▼       ▼
 Flights Railway  Maps  Uber  Flight  Budget
(Amadeus)(12306) (Mapbox)     Tracker  Mgmt
         (NS)                (FR24)
         (Norikae)
```

For a complex journey — say, London to rural Tuscany — the agent finds flights to Florence or Pisa, trains to the nearest station, and local transport options for the final leg. It compares total journey time, cost, and convenience across different routing options.

### Pattern 4: Travel Operations Dashboard

This architecture serves travel businesses — agencies, tour operators, or corporate travel managers — that need to monitor bookings, track disruptions, and manage itineraries at scale.

```
    ┌───────────────────────────┐
    │   Operations Dashboard    │
    │  (Business Travel Agent)  │
    └────┬──┬──┬──┬──┬──┬──────┘
         │  │  │  │  │  │
    ┌────┘  │  │  │  │  └────┐
    │       │  │  │  │       │
    ▼       ▼  ▼  ▼  ▼       ▼
 Flight  Hotel   Weather Emissions Travel
 Tracker Inventory Alerts  Calc    Hacking
 (FR24)  (WinWin) (Open-  (TIMCP) (Points)
(AviStk) (Lodgify) Meteo)
```

The dashboard monitors real-time flight status for booked travelers, checks weather alerts at destination cities, calculates carbon emissions for sustainability reporting, and optimizes loyalty point redemptions across corporate travel programs.


## Security and Privacy Considerations

Travel MCP servers handle sensitive personal and financial data. Several security patterns deserve attention.

**Authentication and API keys.** Most travel API integrations require API keys from services like Duffel, Amadeus, Google Maps, or Booking.com. These keys often carry usage costs and rate limits. MCP server configurations should store keys securely (environment variables, not hardcoded) and implement rate limiting to prevent unexpected charges. The Airbnb MCP server's no-API-key approach is the exception, not the rule.

**Reverse-engineered APIs.** Several popular servers — including the Google Flights integration (fli, 364 stars), American Airlines (mcp-american), and Skyscanner (mcp-skyscanner) — use reverse-engineered or unofficial APIs. These may violate terms of service, break without notice, and lack the stability guarantees of official APIs. For production travel applications, prefer servers built on official APIs (Duffel, Amadeus, Expedia) even if they require registration and payment.

**Location and movement data.** Travel MCP servers inherently process location data — flight routes, hotel locations, transit queries, and map searches. Combined, these create detailed movement profiles. AI agents that integrate multiple travel MCP servers should consider data minimization: query only what's needed, avoid storing itineraries beyond the trip, and be transparent with users about what location data is being processed.

**Booking and payment.** While most travel MCP servers focus on search and information retrieval, some (American Airlines, Uber, Lodgify) support actual booking and payment operations. Any MCP server that can commit financial transactions on behalf of a user requires particular scrutiny: OAuth authentication, confirmation flows, and clear authorization boundaries.

**Browser automation risks.** Servers like mcp-american that use Playwright browser automation effectively run a remote-controlled browser. This introduces risks around credential handling, session management, and the potential for automation to trigger anti-bot protections that could lock users out of their accounts.


## The Platform Landscape

The travel MCP ecosystem is notable for the number of official or enterprise-backed servers, signaling genuine industry adoption rather than purely hobbyist activity.

**Official MCP servers from mapping platforms.** Baidu Maps (415 stars), Mapbox (325 stars), and Stadia Maps (21 stars) all provide official MCP servers. Google Maps integration exists through multiple community servers but not an official Google MCP implementation. These mapping servers provide the foundational location infrastructure that all other travel applications build upon.

**OTA adoption.** Expedia shipped an official MCP server (14 stars). Kiwi.com launched its MCP server in August 2025, becoming the first OTA to do so publicly. Booking.com was among seven launch partners for ChatGPT's MCP-based applications. These adoptions suggest that major online travel agencies see MCP as a distribution channel — a way for their inventory to be accessible through AI agents.

**Review platform integration.** Yelp's official MCP server and TripAdvisor's community MCP integration (plus TripAdvisor's partnership with Perplexity) indicate that review platforms are positioning for AI-mediated discovery — where travelers find restaurants and attractions through agent recommendations rather than manual search.

**Travel technology companies.** Apaleo (hotel property management), WinWin-travel (hotel inventory aggregation), and Variflight (flight data) have all launched MCP servers, representing the B2B travel technology layer that powers the industry behind the scenes.

**No official servers from major airlines, hotel chains, or rail operators.** Despite the community activity, no major airline (Delta, United, Lufthansa), hotel chain (Marriott, Hilton, IHG), or national rail operator (Deutsche Bahn, SNCF, JR) has shipped an official MCP server. Community implementations fill the gap but rely on unofficial APIs, scraping, or third-party data sources.


## Ecosystem Gaps

Several significant travel categories lack meaningful MCP coverage.

**Cruise lines and ferry services.** No MCP servers exist for cruise booking, cabin selection, shore excursion planning, or ferry route search. The cruise industry's complex pricing models and itinerary structures would benefit from AI-assisted planning.

**Visa and immigration.** No MCP servers address visa requirements, application tracking, or immigration document preparation — a category where AI agents could provide significant value by navigating country-specific rules.

**Travel insurance.** While our [MCP and insurance guide](/guides/mcp-insurance/) covers the insurance industry broadly, no MCP server specifically targets travel insurance comparison, claim filing, or policy management.

**Package tours and activities.** Beyond Expedia's activity endpoint, no dedicated MCP servers cover tour operators (GetYourGuide, Viator, Klook), activity booking, or guided experience platforms.

**Airport services.** No MCP servers address airport lounge access, fast-track security, airport transfer booking, or airport retail/duty-free — services that frequent travelers actively manage.

**Car rental.** Beyond Expedia's car rental endpoint, no dedicated MCP server targets car rental platforms (Hertz, Enterprise, Sixt) or peer-to-peer car sharing (Turo).

**Travel rewards and loyalty programs.** While the travel-hacking-toolkit (61 stars) addresses points optimization, no MCP servers connect directly to airline frequent flyer programs, hotel loyalty platforms, or credit card travel portals. Given the complexity of loyalty program rules and redemption values, this is a gap where AI agents could provide outsized value.

**Accessibility information.** No MCP servers specifically provide wheelchair accessibility data, accessible transport options, or disability accommodation information for travelers with mobility or sensory challenges.


## Getting Started by Role

**Solo travelers** exploring a new city should start with a maps server (Google Maps MCP or OpenStreetMap), a weather server (Open-Meteo for comprehensive forecasts), a translation server (DeepL for communication), and a nearby search server for spontaneous discovery. Adding a currency conversion server completes the essential travel toolkit.

**Travel hackers** optimizing points and miles should combine the travel-hacking-toolkit with multiple flight search servers (Duffel for broad airline access, Google Flights for price comparison) and hotel servers to compare cash vs. points redemption values.

**Corporate travel managers** should evaluate the Expedia official MCP server for policy-compliant booking, Flightradar24 for traveler tracking, the emissions calculator (TIMCP) for sustainability reporting, and weather alerts for duty-of-care notifications.

**Travel app developers** building AI-powered travel products should start with official MCP servers (Mapbox, DeepL, Expedia) for production reliability, adding community servers (Duffel flights, Open-Meteo weather) where official options don't exist. The mcp_travelassistant suite provides a reference architecture for multi-server travel planning.

**Transit enthusiasts and commuters** should look at their region's specific railway or transit MCP servers — NS for the Netherlands, Norikae for Japan, Indian Railway for India, 12306 for China, MTA for New York City — as these provide the most practical daily value.

**Destination researchers** writing travel content or planning trips should combine TripAdvisor or Yelp for reviews, Google Maps for place details, weather servers for seasonal planning, and translation servers for understanding local content.


## Market Context

The travel technology market is substantial and growing. Global travel technology spending reached an estimated $11-15 billion in 2025, growing at 5-8% annually and projected to reach $25 billion by 2035. AI adoption in travel is accelerating dramatically: the AI in travel market was valued at $222 billion in 2026 and is projected to reach $710 billion by 2030 at a 33.7% CAGR.

Consumer adoption is keeping pace with investment. Approximately 40% of global travelers used AI tools for travel planning in 2025, with adoption significantly higher among millennials and Gen Z (62%). Nearly 25% of travelers used generative AI specifically for trip planning by late 2025 — a threefold increase from 2022. Among US adults, 36% say they would delegate entire trip planning to an AI agent.

MCP's role in this market is as a distribution layer. For travel platforms, shipping an MCP server means their inventory becomes accessible through any AI agent that speaks the protocol — whether that's Claude, ChatGPT, Gemini, or a custom travel planning agent. For travelers, MCP means their AI assistant can seamlessly query multiple booking platforms, check real-time conditions, and manage logistics through a single conversational interface.

The pace of official adoption — Expedia, Kiwi.com, Booking.com, Mapbox, Baidu Maps, Yelp, DeepL, TripAdvisor, Stadia Maps, Variflight, and Apaleo all shipping or supporting MCP integrations within a single year — suggests that MCP is becoming the standard protocol for AI-mediated travel commerce. The travel industry's inherent multi-source nature makes it a natural fit for a protocol designed to give AI agents structured access to diverse data sources.

