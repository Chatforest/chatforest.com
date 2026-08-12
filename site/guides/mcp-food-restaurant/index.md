# MCP and Food/Restaurant: How AI Agents Connect to Recipes, Nutrition Data, POS Systems, Food Delivery, Reservations, Kitchen Operations, and Grocery Platforms

> A comprehensive guide to MCP integrations for food and restaurants — covering 60+ MCP servers across recipes (HowToCook ~750 stars), nutrition tracking (15+ servers), POS systems


Food is one of the most universal human needs, and the industry built around it is massive: [restaurant technology alone is a $5.93 billion market in 2025, projected to reach $27 billion by 2035](https://www.globalgrowthinsights.com/market-reports/restaurant-technology-market-116768). AI adoption is accelerating — in Toast's [2025 survey of 712 restaurant decision-makers](https://pos.toasttab.com/blog/data/ai-in-restaurants), 86% of operators said they were comfortable using AI and 81% said they planned to increase their AI use — and the [AI-in-food market is growing at roughly 37% annually](https://www.globenewswire.com/news-release/2025/12/12/3204534/0/en/ai-in-food-innovation-market-to-surge-at-a-cagr-of-37-3-reaching-usd-39-76-billion-by-2034.html). But the tooling is fragmented: POS systems, delivery platforms, reservation systems, recipe databases, nutrition trackers, kitchen display systems, and inventory management all live in separate silos.

MCP is starting to bridge these silos, though unevenly. The consumer side is well-covered — recipe search, nutrition tracking, and restaurant discovery have dozens of MCP servers. The operational side (POS, kitchen ops, food safety) is almost empty. Three official MCP servers exist from food industry companies: Instacart (the first grocery partner with an app inside ChatGPT, built on OpenAI's MCP-based Apps SDK), Yelp (restaurant discovery and reviews), and Square (POS and payments). Major platforms like DoorDash, UberEats, Toast, and every restaurant chain remain absent.

This guide is research-based. We survey what MCP servers exist for food and restaurants, how the industry is approaching AI, and where the gaps remain. We do not claim to have tested or used any of these servers hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI. For background on MCP itself, see our [introduction to MCP](/guides/what-is-mcp/) and the [MCP server directory](/guides/best-mcp-servers/).


## Why the Food Industry Needs MCP

The food industry has characteristics that make standardized AI integration both valuable and overdue.

**Data silos are everywhere.** A single restaurant might use Toast for POS, DoorDash for delivery, OpenTable for reservations, Sysco for supply ordering, 7shifts for labor scheduling, Yelp for reviews, and QuickBooks for accounting. None of these systems talk to each other natively. An AI agent that could read POS data, check delivery orders, and compare against inventory — all through a standard protocol — would unlock cross-system intelligence that restaurant operators currently piece together manually.

**Labor shortages are chronic.** [The restaurant industry's average annual turnover rate has been 79.6% over the past decade](https://turnozo.com/blog/restaurant-staffing-statistics). AI agents that automate routine tasks — answering phones, taking reservations, managing inventory, generating marketing — aren't a luxury but a survival strategy. MCP provides the standard interface that lets these agents connect to the actual systems restaurants use.

**Food waste is a massive problem.** [Restaurants and foodservice generated 12.5 million tons of surplus food in 2024, with more than 85% going to landfill](https://refed.org/downloads/2024-refed-food-waste-report-updated-4-18-2025.pdf). Demand-forecasting AI needs access to sales data, inventory levels, weather forecasts, and event calendars to help reduce that waste. MCP can provide that access.

**The consumer experience is already AI-driven.** [Chatbots are the most widely deployed AI tool in restaurants, with 60% of operators using them daily](https://www.deloitte.com/us/en/insights/industry/retail-distribution/ai-in-restaurants.html). Voice ordering, personalized recommendations, and automated marketing are becoming standard. MCP servers for Yelp, Google Maps, and reservation platforms let AI agents help consumers find, evaluate, and book restaurants through a structured interface rather than screen-scraping.

**Scale varies enormously.** A food truck, a family restaurant, a fast-casual chain with 500 locations, and a global franchise like McDonald's have fundamentally different technology needs. MCP's modular design — where each tool can be adopted independently — fits this spectrum better than monolithic platforms.


## Recipes and Cooking

Recipe management is the most developed area of the food MCP ecosystem, with servers ranging from massive community recipe databases to self-hosted recipe managers and smart kitchen appliance integrations.

### Recipe Search and Discovery

**[worryzyy/HowToCook-mcp](https://github.com/worryzyy/HowToCook-mcp)** (~750 stars) | **Language:** TypeScript | **5 tools** | **License:** MIT

The most popular food MCP server by a wide margin. Built on the [Anduin2017/HowToCook](https://github.com/Anduin2017/HowToCook) Chinese recipe database, it provides five tools: query all recipes, category-based search, specific recipe lookup, weekly meal planning, and daily menu suggestions. Available via npm with stdio, HTTP, and SSE transport options. The high star count reflects both the quality of the underlying recipe database and the strong demand for cooking-related AI assistance.

**[ddsky/spoonacular-mcp](https://github.com/ddsky/spoonacular-mcp)** (5 stars) | **Language:** JavaScript | **6 tools** | **License:** ISC

Wraps the Spoonacular Food API with six tools: search_recipes, get_recipe_information, search_ingredients, analyze_nutrition, find_recipes_by_ingredients, and get_random_recipes. [Spoonacular's free tier allows 50 points per day](https://spoonacular.com/food-api/pricing), making this practical for light personal use (different endpoints consume different numbers of points). The find_recipes_by_ingredients tool is particularly useful — tell it what's in your fridge and it suggests what you can make.

Additional recipe search servers include:
- **[valetdotdev/recipe-mcp](https://github.com/valetdotdev/recipe-mcp)** (formerly published under the blaideinc org) — Uses cookwith.co API for natural language recipe generation and dietary modification (20 requests/hour, no API key needed)
- **[valetdotdev/cookwith-mcp](https://github.com/valetdotdev/cookwith-mcp)** (formerly blaideinc) — Streamable HTTP version of the same cookwith.co integration
- **[suraj-yadav-aiml/recipe-mcp](https://github.com/suraj-yadav-aiml/recipe-mcp)** — TheMealDB API with recipe storage and meal planning via FastMCP
- **[D-C2211/mealserver](https://github.com/D-C2211/mealserver)** — TheMealDB-based meal data retrieval
- **[Disdjj/mcp-cook](https://github.com/Disdjj/mcp-cook)** — Another HowToCook-based server with 200+ Chinese food and cocktail recipes
- **[ruffood/cn-food-mcp](https://github.com/ruffood/cn-food-mcp)** (8 stars) — Chinese food nutrition data covering ~1,725 foods with 25 nutrients per 100g, bilingual Chinese/English labels

### Self-Hosted Recipe Managers

For users who maintain their own recipe collections, MCP servers exist for the three most popular self-hosted recipe managers.

**[starbuck93/tandoor-mcp-server](https://github.com/starbuck93/tandoor-mcp-server)** (15 stars) | **Language:** JavaScript | **13 tools**

Integrates with Tandoor Recipe Manager, a popular self-hosted recipe platform. Provides recipe creation, meal plan management, recipe search, shopping list management (full CRUD operations), and reference data access for meal types, keywords, foods, and units.

**Mealie** has three independent MCP implementations:
- **[mdlopresti/mealie-mcp](https://github.com/mdlopresti/mealie-mcp)** — Recipe management with search, create, update, import from URLs, meal planning, and shopping lists. Docker deployment available.
- **[rldiao/mealie-mcp-server](https://github.com/rldiao/mealie-mcp-server)** — Alternative exposing Mealie APIs to Claude Desktop
- **[counterbeing/mealie-mcp-ts](https://github.com/counterbeing/mealie-mcp-ts)** — TypeScript implementation

**Paprika** has two MCP servers:
- **[soggycactus/paprika-3-mcp](https://github.com/soggycactus/paprika-3-mcp)** (34 stars) — Go implementation for Paprika 3 with create and update recipe tools. Recipes are also exposed as readable MCP resources. Homebrew install available for macOS.
- **[aarons22/paprika-tools](https://github.com/aarons22/paprika-tools)** (formerly paprika-mcp) — Read-only access to list and retrieve recipes, grocery items, and meal plans

### Smart Kitchen Integration

**[alexandrepa/mcp-cookidoo](https://github.com/alexandrepa/mcp-cookidoo)** (38 stars) | **Language:** Python | **4 tools** | **License:** MIT

The most notable smart kitchen MCP server — integrates with the Thermomix Cookidoo platform, which combines guided cooking instructions with the Thermomix kitchen appliance. Tools include connect_to_cookidoo, get_recipe_details, generate_recipe_structure, and upload_custom_recipe. This is an unofficial integration but represents an important category: bridging AI agents with smart kitchen hardware.

Additional cooking tools:
- **[paulabaal12/kitchen-mcp](https://github.com/paulabaal12/kitchen-mcp)** (11 tools) — Food/nutrition queries, recipe discovery by ingredients/diet, ingredient substitution, utensil recommendations, mood/season-based food recommendations
- **[salindersidhu/food-mcp-server](https://github.com/salindersidhu/food-mcp-server)** — Combines TheMealDB (recipes) with USDA Food Data Central (nutrition) in a FastAPI server


## Nutrition Tracking and Diet Management

Nutrition is the second strongest category in food MCP, with 15+ servers connecting to everything from government food databases to commercial diet tracking apps.

### Standalone Nutrition Databases

**[deadletterq/mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition)** (~200 stars) | **Language:** TypeScript | **4 tools** | **License:** MIT

The most popular nutrition MCP server. Contains 300,000+ food items aggregated from four government databases: USDA (United States), CNF (Canada), FRIDA (Denmark), and AUSNUT (Australia). Runs entirely locally with no external API calls required — all data is embedded. Tools include search by name, browse foods, get by ID, and barcode lookup. Docker deployment available.

**[nutrition-mcp.com](https://nutrition-mcp.com)** | **Cloud-hosted** | **Free**

A cloud-hosted nutrition tracker that works with any MCP client supporting OAuth 2.0 PKCE. Offers natural language meal logging, calorie and macro estimation, and daily/weekly summaries. No premium tiers — entirely free. Works with Claude.ai, Claude Desktop, and other MCP clients.

Additional standalone trackers:
- **[nagarjun226/food-tracker-mcp](https://github.com/nagarjun226/food-tracker-mcp)** (6 stars) — OpenFoodFacts integration with barcode/keyword search, dietary restriction management, and local JSON persistence
- **[neonwatty/food-tracker-mcp](https://github.com/neonwatty/food-tracker-mcp)** — USDA FoodData Central with SQLite storage
- **[VeriTeknik/daily-calorie-tracker](https://github.com/VeriTeknik/daily-calorie-tracker)** — Natural language meal logging with 100+ built-in food items
- **[thitiph0n/calorie-tracker-mcp-server](https://github.com/thitiph0n/calorie-tracker-mcp-server)** (4 stars) — Cloudflare Workers + D1 database with BMR/TDEE calculations using Mifflin-St Jeor equation, OAuth 2.1 with PKCE
- **[caloriesclub.app](https://caloriesclub.app)** — Commercial AI-powered calorie tracker with photo recognition, barcode scanning, and voice logging, exposed via MCP

### Platform-Connected Trackers

**[fliptheweb/yazio-mcp](https://github.com/fliptheweb/yazio-mcp)** (54 stars) | **Language:** TypeScript | **11 tools** | **License:** MIT

Unofficial integration with Yazio, a popular diet tracking app. Provides daily summaries, food database search, meal logging, exercise/water intake tracking, and weight history. Uses a reverse-engineered API, so it may break with Yazio updates.

Other platform integrations:
- **[fcoury/fatsecret-mcp](https://github.com/fcoury/fatsecret-mcp)** (8 stars, 11 tools) — FatSecret API with full 3-legged OAuth 1.0a authentication. Food and recipe database search, user food diary access, encrypted credential storage.
- **[ai-mcp-garage/mcp-myfitnesspal](https://github.com/ai-mcp-garage/mcp-myfitnesspal)** — MyFitnessPal data retrieval via FastMCP

A previously listed Cronometer integration (attributed to "pshortino/cronometer-mcp") could not be re-verified — the GitHub account no longer resolves — so it has been removed from this guide pending a working, sourceable link.

### Food Data APIs

For applications that need raw nutritional data rather than tracking features, several MCP servers wrap government and open-source food databases.

**[JagjeevanAK/OpenFoodFacts-MCP](https://github.com/JagjeevanAK/OpenFoodFacts-MCP)** (17 stars) | **Language:** TypeScript | **20+ tools** | **License:** AGPL-3.0

The most comprehensive Open Food Facts server. Includes search, barcode lookup, Nutri-Score, Eco-Score, allergen detection, additive identification, AI-powered insights from Robotoff, pricing data, and educational resources. Open Food Facts covers 3+ million products globally.

USDA FoodData Central servers:
- **[jlfwong/food-data-central-mcp-server](https://github.com/jlfwong/food-data-central-mcp-server)** (11 stars) — Search tool plus 3 resources, covering Foundation, SR Legacy, Survey, and Branded datasets
- **[FelipeAdachi/mcp-food-data-central](https://github.com/FelipeAdachi/mcp-food-data-central)** (3 stars) — Python implementation with batch lookup (up to 20 foods)
- **[MCP-Forge/nutritionix-mcp-server](https://github.com/MCP-Forge/nutritionix-mcp-server)** (3 stars) — Nutritionix API with natural language meal parsing and exercise calorie estimation

Other Open Food Facts servers:
- **[noot-app/openfoodfacts-mcp-server](https://github.com/noot-app/openfoodfacts-mcp-server)** (2 stars) — Go implementation using DuckDB + Parquet for fast local queries
- **[caleb-conner/open-food-facts-mcp](https://github.com/caleb-conner/open-food-facts-mcp)** — Product information, nutritional data, and environmental scores


## Food Delivery Platforms

The [US online food delivery market was valued at $31.91 billion in 2024 and is projected to reach $74+ billion by 2033](https://finance.yahoo.com/news/united-states-online-food-delivery-135000318.html), yet no major delivery platform has released an official MCP server. The current landscape is entirely scrapers and proof-of-concept integrations.

### The Official Void

[DoorDash (~67% US market share), Uber Eats (~23%), and Grubhub (~6%)](https://www.imarcgroup.com/united-states-online-food-delivery-market) have no official MCP servers. This is a significant gap. Restaurants managing orders across multiple delivery platforms — a common pain point — would benefit enormously from a unified MCP interface. Third-party restaurant management platforms like Olo and Ordermark aggregate these already, but none have MCP servers either.

### What Exists

**[tas1337/mcp-Im-hungry](https://github.com/tas1337/mcp-Im-hungry)** (1 star) | **Language:** TypeScript | **4 tools** | **License:** MIT

A multi-platform food delivery proof-of-concept using the A2A (Agent-to-Agent) protocol. Provides search_restaurants, get_menu, search_menu_items, and check_delivery_estimate tools with mock agents for DoorDash, UberEats, and Grubhub. Includes Stripe payment integration with cryptographic mandates. This is a demonstration of what's architecturally possible, not a production integration.

### Scraper-Based Access (Apify MCP)

Multiple Apify actors provide scraper-based access to delivery platform data. These run on Apify's cloud infrastructure and expose MCP endpoints, but rely on web scraping — making them fragile and potentially at odds with platform terms of service.

DoorDash scrapers (two entries previously listed here, "sovereigntaylor/doordash-scraper" and "consummate_mandala/doordash-menu-scraper", could not be re-verified on Apify and have been dropped):
- **[axlymxp/doordash-store-scraper](https://apify.com/axlymxp/doordash-store-scraper)** — Store search by location with customizable radius
- **[yasmany.casanova/doordash-restaurant-scraper](https://apify.com/yasmany.casanova/doordash-restaurant-scraper)** — Menu and restaurant data

UberEats scrapers (a previously listed "crscrapers/ubereats-menu-scraper" entry could not be re-verified on Apify and has been dropped):
- **[crawlerbros/ubereats-menu-scraper](https://apify.com/crawlerbros/ubereats-menu-scraper)** — Full product, price, and modifier data extraction

Regional/specialty:
- **[clearpath/thefork-scraper](https://apify.com/clearpath/thefork-scraper)** — TheFork (European restaurant platform) for restaurants, reviews, and menus
- **[yasmany.casanova/rappi-restaurant-scraper](https://apify.com/yasmany.casanova/rappi-restaurant-scraper)** — Rappi (Latin American delivery) for menu and restaurant data
- **[fortuitous_pirate/weee-scraper](https://apify.com/fortuitous_pirate/weee-scraper)** — Weee! Asian grocery delivery for product data


## Grocery and Meal Kit Services

### Instacart: The Landmark Integration

**Instacart Developer Platform MCP** | **Official** | **3 tools**

Instacart's MCP server is arguably the most significant official food industry MCP integration to date. [Instacart announced in December 2025 that it was the first grocery partner to launch an app within ChatGPT](https://company.instacart.com/pressreleases/instacart-app-launches-in-openai-chatgpt), letting consumers shop from 1,800+ retailers there, with end-to-end Instant Checkout built in. [OpenAI's Apps SDK — the framework this integration runs on — is built on the Model Context Protocol](https://openai.com/index/introducing-apps-in-chatgpt/); Instacart's own announcement credits the checkout flow specifically to the separate Agentic Commerce Protocol (ACP), so the MCP and ACP pieces of the integration are distinct and shouldn't be conflated. The server provides three tools: create recipe pages (with ingredients, instructions, and URLs), create shopping list pages, and get nearby retailers by postal code.

The significance goes beyond the tools themselves. [Instacart's own company page cites 2,200+ retail banners across 100,000+ stores](https://company.instacart.com/) in its broader network (a larger figure than the 1,800 retailers available specifically inside the ChatGPT app). When an AI agent creates a recipe through this MCP server, the user gets a shoppable list with real prices and real-time availability at nearby stores. This is the model of what food industry MCP integration should look like: official, production-grade, and immediately useful.

Production endpoint: mcp.instacart.com. Development: mcp.dev.instacart.tools.

### Meal Kits and Shopping

**[markswendsen-code/mcp-hellofresh](https://github.com/markswendsen-code/mcp-hellofresh)** | **Community**

HelloFresh meal kit management via Playwright browser automation (unofficial). Menu browsing, meal selection, delivery schedule management, dietary preferences, order history, and recipe rating. Since it uses browser automation rather than an API, it's fragile but demonstrates the demand for meal kit MCP integration.

Shopping list management:
- **[bobby060/anylist-mcp](https://github.com/bobby060/anylist-mcp)** (25 stars, 5 domain-grouped tools with 18+ actions) — AnyList integration for shopping lists, recipes, meal planning, and recipe collections
- **[jessalva7/grocery-mcp-server](https://github.com/jessalva7/grocery-mcp-server)** — Grocery management with Elasticsearch + Redis, ingesting data from Kaggle datasets


## Restaurant Reservations and Booking

Reservation systems are a mid-tier category in the food MCP ecosystem — not as developed as recipes or nutrition, but with some notable implementations.

**[jrklein343-svg/restaurant-mcp](https://github.com/jrklein343-svg/restaurant-mcp)** (4 stars) | **Language:** TypeScript | **12 tools**

The most feature-rich reservation server. Unifies Resy and OpenTable search in a single interface with real-time availability checking. Supports direct Resy booking and OpenTable booking links. Its most distinctive feature is a reservation "sniper" — an automated tool that watches for slots to open at hard-to-book restaurants and automatically reserves them. Uses Windows DPAPI for secure credential storage with rate limiting.

**[samwang0723/mcp-booking](https://github.com/samwang0723/mcp-booking)** (16 stars) | **Language:** TypeScript | **5 tools** | **License:** MIT

Google Maps Places API integration focused on restaurant discovery. Finds restaurants by location, cuisine, mood, or event type within a 20km search radius. Includes an AI recommendation engine that returns top 3 picks with booking assistance.

Two previously listed Resy-specific servers ("musemen/resy-mcp-server" and "Jpc54066/resy-mcp") could not be re-verified — neither GitHub path resolves — and have been removed pending a working, sourceable link.

OpenTable access:
- **[canadesk/opentable](https://apify.com/canadesk/opentable)** (Apify) — OpenTable search results and reservation availability via Apify MCP


## Restaurant Reviews and Discovery

### Yelp (Official)

**[Yelp/yelp-mcp](https://github.com/Yelp/yelp-mcp)** (26 stars) | **Language:** Python | **1 tool** | **License:** Apache-2.0

The official Yelp MCP server, backed by the Yelp Fusion AI API. Despite having only one tool (yelp_agent), it handles natural language business search, detailed queries, multi-turn conversations, and restaurant reservation requests. The single-tool design reflects Yelp's approach of letting the AI handle query interpretation rather than exposing multiple specialized endpoints. Docker and local deployment supported. Python 3.10+ required.

### Google Maps

**[cablate/mcp-google-map](https://github.com/cablate/mcp-google-map)** (421 stars) | **Language:** TypeScript | **18 tools** | **License:** MIT

Not food-specific, but heavily used for restaurant discovery. Per the project's own README, the 18 tools break down as 14 atomic tools plus 4 composite tools. The atomic set includes search_nearby (filter by type: restaurant, cafe, bakery, etc.), search_places (free text), and place_details (reviews, hours, phone, website, price level). The 14 atomic tools can be composed by AI agents to build restaurant recommendation workflows: search nearby, filter by rating, get details, compare options.

### Review Scrapers

Multiple Apify-based MCP servers provide review data:
- **[scraped/yelp-reviews](https://apify.com/scraped/yelp-reviews)** — Yelp review text and ratings extraction
- **[agents/yelp-reviews](https://apify.com/agents/yelp-reviews)** — Fast Yelp reviews scraper API
- **[tri_angle/hotel-review-aggregator](https://apify.com/tri_angle/hotel-review-aggregator)** — Multi-platform review aggregation across Tripadvisor, Yelp, Google Maps, Expedia, Hotels.com, Booking.com, and Airbnb — applicable to restaurants with hotel dining


## POS Systems and Restaurant Operations

### Square (Official)

**[square/square-mcp-server](https://github.com/square/square-mcp-server)** (106 stars) | **Language:** TypeScript | **3 tools** | **License:** Apache-2.0

The official Square MCP server provides access to Square's API ecosystem through three meta-tools: get_service_info, get_type_info, and make_api_request. [Its README lists a service catalog of roughly 38 named services](https://github.com/square/square-mcp-server/blob/main/README.md), covering payments, orders, customers, inventory, bookings, loyalty, labor, team, and locations. Remote MCP via OAuth at mcp.squareup.com. Sandbox mode available. Read-only option for safety. Currently in beta.

Square is used by many restaurants, cafes, and food trucks, making this server immediately relevant for food service operations. An AI agent with Square MCP access could analyze sales trends, check inventory, manage loyalty programs, and review labor schedules — all through a single protocol.

### The Toast Gap

Toast is a leading restaurant-specific POS system, with [approximately 180,000 restaurant locations as of Q2 2026 per its own quarterly results](https://www.nasdaq.com/press-release/toast-announces-second-quarter-2026-financial-results-2026-08-04). It has no MCP server. A "Toast Notifications MCP Server" exists (by Naru Sensei), but this is for desktop notifications, not the restaurant POS system. Given Toast's scale in the restaurant POS market, this is perhaps the single most impactful missing MCP integration in the food industry.

### Other POS Gaps

No MCP servers exist for:
- **Clover** — Popular with small-to-medium restaurants
- **Lightspeed** — Used in restaurants and retail
- **TouchBistro** — Restaurant-specific POS
- **SpotOn** — Growing restaurant POS platform
- **Revel Systems** — iPad POS for restaurants

### Order Management

**[miyamo2/mcp-restaurant-order](https://github.com/miyamo2/mcp-restaurant-order)** (0 stars) | **Language:** Go | **License:** MIT

An educational implementation of basic restaurant ordering through MCP. Multi-language support (English/Japanese). While not production-ready, it demonstrates the architecture pattern for restaurant order management via MCP.


## Food Safety and Supply Chain

This category has minimal MCP coverage despite its critical importance.

**[ryanclinton/food-safety-supply-chain-mcp](https://apify.com/ryanclinton/food-safety-supply-chain-mcp)** (Apify) | **Pay-per-use**

The only food safety MCP server found. Covers FDA recalls, adverse events, supplier hygiene ratings, ingredient risk tracing via trade flows, and contamination pathway detection. Hosted on Apify and requires an API token.

### What's Missing

The food safety gap is striking:
- **No HACCP compliance tracking** — HACCP (Hazard Analysis and Critical Control Points) is mandatory for many food businesses, yet no MCP server helps manage it
- **No temperature monitoring** — IoT kitchen sensors that track refrigerator, freezer, and holding temperatures have no MCP integration
- **No allergen management** — [With food allergies affecting an estimated 33 million Americans](https://www.foodallergy.org/resources/facts-and-statistics), allergen tracking across menus, recipes, and ingredients remains manual
- **No health inspection data** — Restaurant health inspection scores are public data in most jurisdictions but have no MCP interface
- **No food traceability** — Farm-to-table supply chain tracking, increasingly important for food safety and sustainability, has zero MCP coverage


## Comparison of MCP Servers by Category

| Category | Servers | Official | Most Popular | Coverage Level |
|----------|---------|----------|-------------|----------------|
| Recipes & Cooking | 15+ | 0 | HowToCook-mcp (~750 stars) | Strong |
| Nutrition Tracking | 15+ | 0 | mcp-opennutrition (~200 stars) | Strong |
| Restaurant Discovery | 5+ | 1 (Yelp) | mcp-google-map (421 stars) | Good |
| Reservations | 5+ | 0 | mcp-booking (16 stars) | Moderate |
| Grocery & Shopping | 4+ | 1 (Instacart) | Instacart (official) | Moderate |
| POS Systems | 1 | 1 (Square) | Square (106 stars) | Weak (only Square) |
| Food Delivery | 10+ scrapers | 0 | DoorDash scrapers | Weak (no official) |
| Food Safety | 1 | 0 | FDA recalls (Apify) | Minimal |
| Kitchen Operations | 0 | 0 | — | None |
| Beverages | 0 | 0 | — | None |


## Architecture Patterns

Four architecture patterns emerge from how MCP servers connect AI agents to food industry systems.

### Pattern 1: Recipe Discovery and Meal Planning

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  AI Agent   │────▶│ Recipe MCP   │────▶│ Recipe Database  │
│  (Claude)   │     │ (HowToCook,  │     │ (TheMealDB,      │
│             │     │  Spoonacular) │     │  Spoonacular API)│
│             │     └──────────────┘     └─────────────────┘
│             │     ┌──────────────┐     ┌─────────────────┐
│             │────▶│ Nutrition MCP│────▶│ USDA / OpenFood │
│             │     │ (opennutri-  │     │ Facts / Nutri-   │
│             │     │  tion)       │     │ tionix API       │
│             │     └──────────────┘     └─────────────────┘
│             │     ┌──────────────┐     ┌─────────────────┐
│             │────▶│ Grocery MCP  │────▶│ Instacart API   │
│             │     │ (Instacart)  │     │ (1,800+ retailers)│
└─────────────┘     └──────────────┘     └─────────────────┘
```

This is the most mature pattern. An AI agent can search for recipes based on dietary requirements or available ingredients, analyze nutritional content, and create a shopping list with real products at real prices — all through MCP. Instacart's official integration makes the last step production-ready.

### Pattern 2: Restaurant Discovery and Booking

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  AI Agent   │────▶│ Yelp MCP     │────▶│ Yelp Fusion AI  │
│             │     │ (official)   │     │ (reviews, hours,  │
│             │     └──────────────┘     │  ratings)         │
│             │     ┌──────────────┐     └─────────────────┘
│             │────▶│ Maps MCP     │────▶│ Google Places API│
│             │     │ (google-map) │     │ (location, type)  │
│             │     └──────────────┘     └─────────────────┘
│             │     ┌──────────────┐     ┌─────────────────┐
│             │────▶│ Booking MCP  │────▶│ Resy / OpenTable│
│             │     │ (restaurant- │     │ (availability,   │
│             │     │  mcp)        │     │  booking)         │
└─────────────┘     └──────────────┘     └─────────────────┘
```

An AI agent can find restaurants matching criteria (cuisine, location, budget, dietary needs), check reviews and ratings across platforms, verify real-time availability, and make a reservation. The unified Resy + OpenTable search in restaurant-mcp is notable for bridging two competing platforms.

### Pattern 3: Restaurant Operations Dashboard

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  AI Agent   │────▶│ Square MCP   │────▶│ Square POS      │
│             │     │ (official)   │     │ (sales, orders,   │
│             │     └──────────────┘     │  inventory, labor) │
│             │     ┌──────────────┐     └─────────────────┘
│             │────▶│ Yelp MCP     │────▶│ Customer Reviews │
│             │     │ (official)   │     │ (sentiment,       │
│             │     └──────────────┘     │  ratings trends)   │
│             │     ┌──────────────┐     └─────────────────┘
│             │────▶│ Safety MCP   │────▶│ FDA Recalls /    │
│             │     │ (Apify)      │     │ Supply Chain Data │
└─────────────┘     └──────────────┘     └─────────────────┘
```

A restaurant operator's AI assistant that can check today's sales, review customer feedback, manage inventory, and monitor food safety alerts. Currently limited by Square being the only POS with MCP support and the food safety server being scraper-based.

### Pattern 4: Personal Food Intelligence

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  AI Agent   │────▶│ Diet MCP     │────▶│ Yazio/FatSecret │
│             │     │ (yazio-mcp,  │     │ MyFitnessPal     │
│             │     │  fatsecret)  │     │ (food diary)      │
│             │     └──────────────┘     └─────────────────┘
│             │     ┌──────────────┐     ┌─────────────────┐
│             │────▶│ Recipe MCP   │────▶│ Recipes matching │
│             │     │ (Spoonacular)│     │ dietary goals     │
│             │     └──────────────┘     └─────────────────┘
│             │     ┌──────────────┐     ┌─────────────────┐
│             │────▶│ Food Data MCP│────▶│ Product scans /  │
│             │     │ (OpenFood-   │     │ Nutri-Score /     │
│             │     │  Facts)      │     │ allergen data     │
└─────────────┘     └──────────────┘     └─────────────────┘
```

An AI nutritionist that tracks what you eat, understands your dietary goals and restrictions, suggests recipes that match your macros, and can scan product barcodes to check ingredients and scores. The combination of tracking apps + recipe databases + food product data creates a comprehensive personal food intelligence system.


## Security, Privacy, and Compliance

Food industry MCP integrations involve several specific security and compliance considerations.

**POS and payment data.** Square's MCP server provides access to payment processing, customer data, and financial records. The read-only mode option is critical — an AI agent that can view sales data but not process refunds or modify orders is much safer than one with full write access. OAuth authentication and sandbox mode provide additional safety layers.

**Personal health information.** Nutrition trackers and diet apps contain sensitive health data. MCP servers for Yazio, MyFitnessPal, and FatSecret access personal food diaries, weight history, and health goals. The FatSecret MCP server uses encrypted credential storage and full OAuth 1.0a — a good pattern. Others store credentials less securely.

**Reservation and personal data.** Restaurant reservation MCP servers handle names, phone numbers, email addresses, and dining preferences. The restaurant-mcp server uses Windows DPAPI for credential encryption. Resy and OpenTable credentials grant access to reservation history and personal profiles.

**Food safety and allergen liability.** AI agents providing food information — recipes, nutrition data, allergen detection — carry implicit liability. If an OpenFoodFacts MCP server returns incorrect allergen data and an AI agent recommends the product, the consequences can be severe. This is not a technical problem MCP can solve, but it's a consideration for anyone building food AI workflows.

**API key management.** Many food MCP servers require API keys for commercial data sources (Spoonacular, Google Maps, Yelp Fusion, Nutritionix). Keys typically go in environment variables or configuration files. The Instacart MCP server uses OAuth for more secure access management. Servers like mcp-opennutrition that run entirely locally with embedded data avoid the API key issue entirely.

**Scraper legal risk.** Food delivery scrapers (DoorDash, UberEats via Apify) operate in a legal gray area. They may violate platform terms of service, and the data they return may not be accurate or current. Building production systems on scraper-based MCP servers is risky.


## Platform Landscape

### Official MCP Servers

Three food industry companies have released official MCP servers:

| Company | Server | Launch | Significance |
|---------|--------|--------|-------------|
| **Instacart** | Instacart Developer Platform MCP | Dec 2025 | [First grocery partner with an app inside ChatGPT](https://company.instacart.com/pressreleases/instacart-app-launches-in-openai-chatgpt), built on OpenAI's MCP-based Apps SDK. Production-ready. |
| **Yelp** | yelp-mcp (26 stars) | 2025 | Official Yelp Fusion AI integration. Real-time business data. |
| **Square** | square-mcp-server (106 stars) | 2025 | ~38 Square services via MCP. Beta. OAuth. |

### Companies Conspicuously Absent

| Company | Why It Matters | Market Position |
|---------|---------------|----------------|
| **Toast** | Leading restaurant-specific POS | [~180,000 restaurant locations as of Q2 2026](https://www.nasdaq.com/press-release/toast-announces-second-quarter-2026-financial-results-2026-08-04) |
| **DoorDash** | [~67% US delivery market share](https://www.imarcgroup.com/united-states-online-food-delivery-market) | [US delivery market: $31.91B (2024), projected $74B+ by 2033](https://finance.yahoo.com/news/united-states-online-food-delivery-135000318.html) |
| **Uber Eats** | [~23% US delivery market share](https://www.imarcgroup.com/united-states-online-food-delivery-market) | Global presence |
| **Grubhub** | [~6% US delivery market share](https://www.imarcgroup.com/united-states-online-food-delivery-market) | Early mover in US delivery |
| **OpenTable** | Dominant reservation platform | [65,000+ restaurants worldwide](https://www.prnewswire.com/news-releases/book-the-restaurant-then-the-room-opentable-reveals-the-2026-top-100-hotel-restaurants-in-america-302825007.html) |
| **Resy** | Premium reservation platform | High-end dining |
| **McDonald's** | Largest restaurant chain globally | [45,000+ locations at year-end 2025](https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm) |
| **Starbucks** | Largest coffee chain globally | [41,000+ locations as of Q1 FY2026](https://s203.q4cdn.com/326826266/files/doc_financials/2026/q1/SBUX-12-28-2025-Earnings-Release-Exhibit-99-1-6pm.pdf) |

The absence of Toast is particularly notable. Toast is purpose-built for restaurants, has extensive APIs, and serves the exact market segment that would benefit most from AI integration through MCP. An official Toast MCP server would instantly become one of the most valuable tools in the restaurant MCP ecosystem.


## Ecosystem Gaps

### Critical Gaps

**Restaurant POS systems.** Only Square has an MCP server, and it's in beta. Toast, Clover, Lightspeed, TouchBistro, SpotOn, and Revel — collectively serving the majority of restaurants — have nothing. This is arguably the highest-impact gap, since POS is the system of record for sales, orders, and inventory that most other operational AI use cases depend on.

**Kitchen operations.** Zero MCP servers exist for kitchen display systems (KDS), kitchen inventory management, food cost tracking, labor scheduling, or kitchen equipment monitoring. The back-of-house is completely unserved by MCP despite being where restaurants live and die operationally.

**Food delivery APIs.** No official MCP servers from any delivery platform. Restaurants managing orders across DoorDash, UberEats, and Grubhub — a nearly universal pain point — have no structured AI interface. The US delivery market (projected to reach $74B+ by 2033) is accessible only through scrapers.

### Significant Gaps

**Food safety and compliance.** One Apify-based server for FDA recalls. Nothing for HACCP, temperature monitoring, allergen management, or health inspections. Given that food safety violations can close a restaurant, this gap has outsized consequences.

**Restaurant marketing and loyalty.** No restaurant-specific CRM, email marketing, or loyalty program MCP servers (beyond what Square covers). Restaurant marketing is a widely cited top AI use case in industry surveys, but there's no MCP infrastructure for it.

### Complete Gaps

**Beverages.** No MCP servers for wine databases, brewery management, bar operations, coffee/cafe tools, or cocktail recipes (beyond one server with 200+ recipes including some cocktails). The beverage industry — worth hundreds of billions globally — has zero dedicated MCP coverage.

**Major restaurant chains.** No chain (McDonald's, Starbucks, Subway, Chick-fil-A, Domino's, etc.) has published an MCP server. No franchise management tools exist.

**Restaurant accounting.** No restaurant-specific accounting, food cost percentage calculators, or tip management MCP servers.


## Getting Started by Role

### Home Cook / Food Enthusiast
Start with **HowToCook-mcp** or **Spoonacular MCP** for recipe discovery, add **mcp-opennutrition** for nutritional analysis, and connect **Instacart MCP** for direct shopping. These three together create a complete cook-discover-shop pipeline.

### Nutrition-Conscious Individual
Start with **mcp-opennutrition** (300K+ foods, runs locally) for food data, add your preferred tracker (**yazio-mcp** or **fatsecret-mcp**) for daily logging, and add **OpenFoodFacts-MCP** for product scanning with Nutri-Score and allergen data.

### Restaurant Owner (Using Square)
Start with **Square MCP** (official) for sales data, inventory, and customer management. Add **Yelp MCP** (official) for monitoring reviews and customer sentiment. Currently, this is the extent of what's available through official channels. The kitchen operations and food safety gaps mean most operational tasks still require manual tools.

### Restaurant Discoverer
Start with **Yelp MCP** (official) for reviews and ratings, add **mcp-google-map** for location-based search, and connect **restaurant-mcp** for unified Resy + OpenTable reservation search and booking.

### Self-Hosted Recipe Manager
If you use **Tandoor**, **Mealie**, or **Paprika** for recipe management, MCP servers exist for all three. These let AI agents search your personal recipe collection, suggest meals from what you already know how to cook, and manage shopping lists.

### Food Developer / Startup
Look at **Instacart MCP** as the gold standard for official food industry MCP integration. Use **Spoonacular MCP** for recipe APIs, **USDA FoodData Central MCP** servers for nutritional data, and **OpenFoodFacts-MCP** for product data. The scraper-based servers (Apify) are useful for prototyping but unreliable for production.


## Market Context

The food industry's AI transformation is well underway, and the numbers underscore why MCP integration matters:

- **Restaurant technology market:** [$5.93B (2025) → $27.05B by 2035 (16.39% CAGR)](https://www.globalgrowthinsights.com/market-reports/restaurant-technology-market-116768)
- **AI in food & beverages:** [$13.39B (2025) → $88.37B by 2031 (36.96% CAGR)](https://www.mordorintelligence.com/industry-reports/artificial-intelligence-in-food-and-beverages-market)
- **US food delivery:** [$31.91B (2024), projected $74B+ by 2033](https://finance.yahoo.com/news/united-states-online-food-delivery-135000318.html), dominated by [DoorDash (~67%), Uber Eats (~23%), Grubhub (~6%)](https://www.imarcgroup.com/united-states-online-food-delivery-market)
- **AI comfort/adoption:** [86% of restaurant operators say they're comfortable using AI; 81% plan to increase their use of it](https://pos.toasttab.com/blog/data/ai-in-restaurants)
- **Labor churn:** [79.6% average annual turnover over the past decade](https://turnozo.com/blog/restaurant-staffing-statistics)
- **Food waste:** [12.5 million tons from restaurants in 2024; 85%+ to landfill](https://refed.org/downloads/2024-refed-food-waste-report-updated-4-18-2025.pdf)

The gap between AI comfort/adoption (86% of operators comfortable using AI) and MCP server availability (3 official servers) is enormous. Most restaurants are using AI through proprietary integrations — chatbots from their POS vendor, analytics from their delivery partner, marketing from their CRM. MCP's value proposition is unifying these into a single interface that any AI agent can use, but the infrastructure isn't there yet for most of the operational stack.

[For every $1 invested in food waste reduction, restaurants save $7 in operating costs](https://www.restaurantdive.com/news/restaurants-save-7-for-each-1-invested-in-cutting-food-waste-report-show/548996/). An AI agent that could connect to POS data (what's selling), inventory systems (what's in stock), weather APIs (tomorrow's demand), and event calendars (is there a concert nearby?) through MCP could make real-time waste-reduction decisions. The recipe and nutrition pieces exist. The operational pieces don't — yet.

