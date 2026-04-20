# MCP and Food/Restaurant: How AI Agents Connect to Recipes, Nutrition Data, POS Systems, Food Delivery, Reservations, Kitchen Operations, and Grocery Platforms

> A comprehensive guide to MCP integrations for food and restaurants — covering 60+ MCP servers across recipes (HowToCook 702 stars), nutrition tracking (15+ servers), POS systems


Food is one of the most universal human needs, and the industry built around it is massive: restaurant technology alone is a $5.93 billion market in 2025, projected to reach $27 billion by 2035. AI adoption is accelerating — 79% of U.S. restaurants now use some form of AI, and the AI-in-food market is growing at nearly 37% annually. But the tooling is fragmented: POS systems, delivery platforms, reservation systems, recipe databases, nutrition trackers, kitchen display systems, and inventory management all live in separate silos.

MCP is starting to bridge these silos, though unevenly. The consumer side is well-covered — recipe search, nutrition tracking, and restaurant discovery have dozens of MCP servers. The operational side (POS, kitchen ops, food safety) is almost empty. Three official MCP servers exist from food industry companies: Instacart (the landmark first grocery MCP integration with ChatGPT), Yelp (restaurant discovery and reviews), and Square (POS and payments). Major platforms like DoorDash, UberEats, Toast, and every restaurant chain remain absent.

This guide is research-based. We survey what MCP servers exist for food and restaurants, how the industry is approaching AI, and where the gaps remain. We do not claim to have tested or used any of these servers hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI. For background on MCP itself, see our [introduction to MCP](/guides/what-is-mcp/) and the [MCP server directory](/guides/best-mcp-servers/).


## Why the Food Industry Needs MCP

The food industry has characteristics that make standardized AI integration both valuable and overdue.

**Data silos are everywhere.** A single restaurant might use Toast for POS, DoorDash for delivery, OpenTable for reservations, Sysco for supply ordering, 7shifts for labor scheduling, Yelp for reviews, and QuickBooks for accounting. None of these systems talk to each other natively. An AI agent that could read POS data, check delivery orders, and compare against inventory — all through a standard protocol — would unlock cross-system intelligence that restaurant operators currently piece together manually.

**Labor shortages are chronic.** The restaurant industry has a 79.6% annual turnover rate, and 45% of operators report insufficient staffing. AI agents that automate routine tasks — answering phones, taking reservations, managing inventory, generating marketing — aren't a luxury but a survival strategy. MCP provides the standard interface that lets these agents connect to the actual systems restaurants use.

**Food waste is a $200 billion problem.** Restaurants and foodservice generated 12.5 million tons of surplus food in 2024, with more than 85% going to landfill. Predictive demand AI can cut food waste by 40% and labor costs by 25%, but only if it has access to sales data, inventory levels, weather forecasts, and event calendars. MCP can provide that access.

**The consumer experience is already AI-driven.** Chatbots are the most widely deployed AI tool in restaurants (60% daily use). Voice ordering, personalized recommendations, and automated marketing are becoming standard. MCP servers for Yelp, Google Maps, and reservation platforms let AI agents help consumers find, evaluate, and book restaurants through a structured interface rather than screen-scraping.

**Scale varies enormously.** A food truck, a family restaurant, a fast-casual chain with 500 locations, and a global franchise like McDonald's have fundamentally different technology needs. MCP's modular design — where each tool can be adopted independently — fits this spectrum better than monolithic platforms.


## Recipes and Cooking

Recipe management is the most developed area of the food MCP ecosystem, with servers ranging from massive community recipe databases to self-hosted recipe managers and smart kitchen appliance integrations.

### Recipe Search and Discovery

**worryzyy/HowToCook-mcp** (~702 stars) | **Language:** TypeScript | **5 tools** | **License:** MIT

The most popular food MCP server by a wide margin. Built on the Anduin2017/HowToCook Chinese recipe database, it provides five tools: query all recipes, category-based search, specific recipe lookup, weekly meal planning, and daily menu suggestions. Available via npm with stdio, HTTP, and SSE transport options. The high star count reflects both the quality of the underlying recipe database and the strong demand for cooking-related AI assistance.

**ddsky/spoonacular-mcp** (4 stars) | **Language:** JavaScript | **6 tools** | **License:** ISC

Wraps the Spoonacular Food API with six tools: search_recipes, get_recipe_information, search_ingredients, analyze_nutrition, find_recipes_by_ingredients, and get_random_recipes. Spoonacular's free tier allows 150 API requests per day, making this practical for personal use. The find_recipes_by_ingredients tool is particularly useful — tell it what's in your fridge and it suggests what you can make.

Additional recipe search servers include:
- **blaideinc/recipe-mcp** — Uses cookwith.co API for natural language recipe generation and dietary modification (20 requests/hour, no API key needed)
- **blaideinc/cookwith-mcp** — Streamable HTTP version of the same cookwith.co integration
- **suraj-yadav-aiml/recipe-mcp** — TheMealDB API with recipe storage and meal planning via FastMCP
- **D-C2211/mealserver** — TheMealDB-based meal data retrieval
- **Disdjj/mcp-cook** — Another HowToCook-based server with 200+ Chinese food and cocktail recipes
- **ruffood/cn-food-mcp** (4 stars) — Chinese food nutrition data covering ~1,725 foods with 25 nutrients per 100g, bilingual Chinese/English labels

### Self-Hosted Recipe Managers

For users who maintain their own recipe collections, MCP servers exist for the three most popular self-hosted recipe managers.

**starbuck93/tandoor-mcp-server** (10 stars) | **Language:** JavaScript | **13 tools**

Integrates with Tandoor Recipe Manager, a popular self-hosted recipe platform. Provides recipe creation, meal plan management, recipe search, shopping list management (full CRUD operations), and reference data access for meal types, keywords, foods, and units.

**Mealie** has three independent MCP implementations:
- **mdlopresti/mealie-mcp** — Recipe management with search, create, update, import from URLs, meal planning, and shopping lists. Docker deployment available.
- **rldiao/mealie-mcp-server** — Alternative exposing Mealie APIs to Claude Desktop
- **counterbeing/mealie-mcp-ts** — TypeScript implementation

**Paprika** has two MCP servers:
- **soggycactus/paprika-3-mcp** (24 stars) — Go implementation for Paprika 3 with create and update recipe tools. Recipes are also exposed as readable MCP resources. Homebrew install available for macOS.
- **aarons22/paprika-mcp** — Read-only access to list and retrieve recipes, grocery items, and meal plans

### Smart Kitchen Integration

**alexandrepa/mcp-cookidoo** (17 stars) | **Language:** Python | **4 tools** | **License:** MIT

The most notable smart kitchen MCP server — integrates with the Thermomix Cookidoo platform, which combines guided cooking instructions with the Thermomix kitchen appliance. Tools include connect_to_cookidoo, get_recipe_details, generate_recipe_structure, and upload_custom_recipe. This is an unofficial integration but represents an important category: bridging AI agents with smart kitchen hardware.

Additional cooking tools:
- **paulabaal12/kitchen-mcp** (11 tools) — Food/nutrition queries, recipe discovery by ingredients/diet, ingredient substitution, utensil recommendations, mood/season-based food recommendations
- **salindersidhu/food-mcp-server** — Combines TheMealDB (recipes) with USDA Food Data Central (nutrition) in a FastAPI server


## Nutrition Tracking and Diet Management

Nutrition is the second strongest category in food MCP, with 15+ servers connecting to everything from government food databases to commercial diet tracking apps.

### Standalone Nutrition Databases

**deadletterq/mcp-opennutrition** (172 stars) | **Language:** TypeScript | **4 tools** | **License:** MIT

The most popular nutrition MCP server. Contains 300,000+ food items aggregated from four government databases: USDA (United States), CNF (Canada), FRIDA (Denmark), and AUSNUT (Australia). Runs entirely locally with no external API calls required — all data is embedded. Tools include search by name, browse foods, get by ID, and barcode lookup. Docker deployment available.

**nutrition-mcp.com** | **Cloud-hosted** | **Free**

A cloud-hosted nutrition tracker that works with any MCP client supporting OAuth 2.0 PKCE. Offers natural language meal logging, calorie and macro estimation, and daily/weekly summaries. No premium tiers — entirely free. Works with Claude.ai, Claude Desktop, and other MCP clients.

Additional standalone trackers:
- **nagarjun226/food-tracker-mcp** (6 stars) — OpenFoodFacts integration with barcode/keyword search, dietary restriction management, and local JSON persistence
- **neonwatty/food-tracker-mcp** — USDA FoodData Central with SQLite storage
- **VeriTeknik/daily-calorie-tracker** — Natural language meal logging with 100+ built-in food items
- **thitiph0n/calorie-tracker-mcp-server** (3 stars) — Cloudflare Workers + D1 database with BMR/TDEE calculations using Mifflin-St Jeor equation, OAuth 2.1 with PKCE
- **caloriesclub.app** — Commercial AI-powered calorie tracker with photo recognition, barcode scanning, and voice logging, exposed via MCP

### Platform-Connected Trackers

**fliptheweb/yazio-mcp** (25 stars) | **Language:** TypeScript | **11 tools** | **License:** MIT

Unofficial integration with Yazio, a popular diet tracking app. Provides daily summaries, food database search, meal logging, exercise/water intake tracking, and weight history. Uses a reverse-engineered API, so it may break with Yazio updates.

Other platform integrations:
- **pshortino/cronometer-mcp** — Cronometer nutrition data including food logs, macro/micro summaries, CSV exports, fasting tracking, and biometrics. Requires a paid Cronometer account. Uses GWT-RPC protocol.
- **fcoury/fatsecret-mcp** (6 stars, 11 tools) — FatSecret API with full 3-legged OAuth 1.0a authentication. Food and recipe database search, user food diary access, encrypted credential storage.
- **ai-mcp-garage/mcp-myfitnesspal** — MyFitnessPal data retrieval via FastMCP

### Food Data APIs

For applications that need raw nutritional data rather than tracking features, several MCP servers wrap government and open-source food databases.

**JagjeevanAK/OpenFoodFacts-MCP** (14 stars) | **Language:** TypeScript | **20+ tools** | **License:** AGPL-3.0

The most comprehensive Open Food Facts server. Includes search, barcode lookup, Nutri-Score, Eco-Score, allergen detection, additive identification, AI-powered insights from Robotoff, pricing data, and educational resources. Open Food Facts covers 3+ million products globally.

USDA FoodData Central servers:
- **jlfwong/food-data-central-mcp-server** (10 stars) — Search tool plus 3 resources, covering Foundation, SR Legacy, Survey, and Branded datasets
- **FelipeAdachi/mcp-food-data-central** (2 stars) — Python implementation with batch lookup (up to 20 foods)
- **MCP-Forge/nutritionix-mcp-server** (3 stars) — Nutritionix API with natural language meal parsing and exercise calorie estimation

Other Open Food Facts servers:
- **noot-app/openfoodfacts-mcp-server** (2 stars) — Go implementation using DuckDB + Parquet for fast local queries
- **caleb-conner/open-food-facts-mcp** — Product information, nutritional data, and environmental scores


## Food Delivery Platforms

Food delivery is a $74+ billion industry in the US alone, yet no major delivery platform has released an official MCP server. The current landscape is entirely scrapers and proof-of-concept integrations.

### The Official Void

DoorDash (56% US market share), Uber Eats (23%), and Grubhub (16%) have no official MCP servers. This is a significant gap. Restaurants managing orders across multiple delivery platforms — a common pain point — would benefit enormously from a unified MCP interface. Third-party restaurant management platforms like Olo and Ordermark aggregate these already, but none have MCP servers either.

### What Exists

**tas1337/mcp-Im-hungry** (1 star) | **Language:** TypeScript | **4 tools** | **License:** MIT

A multi-platform food delivery proof-of-concept using the A2A (Agent-to-Agent) protocol. Provides search_restaurants, get_menu, search_menu_items, and check_delivery_estimate tools with mock agents for DoorDash, UberEats, and Grubhub. Includes Stripe payment integration with cryptographic mandates. This is a demonstration of what's architecturally possible, not a production integration.

### Scraper-Based Access (Apify MCP)

Multiple Apify actors provide scraper-based access to delivery platform data. These run on Apify's cloud infrastructure and expose MCP endpoints, but rely on web scraping — making them fragile and potentially at odds with platform terms of service.

DoorDash scrapers:
- **sovereigntaylor/doordash-scraper** — Restaurants, menus, prices, ratings, delivery fees, delivery times
- **axlymxp/doordash-store-scraper** — Store search by location with customizable radius
- **consummate_mandala/doordash-menu-scraper** — Menu extraction with pagination and proxy rotation
- **yasmany.casanova/doordash-restaurant-scraper** — Menu and restaurant data

UberEats scrapers:
- **crscrapers/ubereats-menu-scraper** — Full product, price, and modifier data extraction

Regional/specialty:
- **clearpath/thefork-scraper** — TheFork (European restaurant platform) for restaurants, reviews, and menus
- **yasmany.casanova/rappi-restaurant-scraper** — Rappi (Latin American delivery) for menu and restaurant data
- **fortuitous_pirate/weee-scraper** — Weee! Asian grocery delivery for product data


## Grocery and Meal Kit Services

### Instacart: The Landmark Integration

**Instacart Developer Platform MCP** | **Official** | **3 tools**

Instacart's MCP server is arguably the most significant official food industry MCP integration to date. Launched in December 2025, it was the first grocery company to enable full MCP-powered shopping within ChatGPT. The server provides three tools: create recipe pages (with ingredients, instructions, and URLs), create shopping list pages, and get nearby retailers by postal code.

The significance goes beyond the tools themselves. Instacart connects to 1,800+ retailers and 2+ billion products. When an AI agent creates a recipe through this MCP server, the user gets a shoppable list with real prices and real-time availability at nearby stores. This is the model of what food industry MCP integration should look like: official, production-grade, and immediately useful.

Production endpoint: mcp.instacart.com. Development: mcp.dev.instacart.tools.

### Meal Kits and Shopping

**markswendsen-code/mcp-hellofresh** | **Community**

HelloFresh meal kit management via Playwright browser automation (unofficial). Menu browsing, meal selection, delivery schedule management, dietary preferences, order history, and recipe rating. Since it uses browser automation rather than an API, it's fragile but demonstrates the demand for meal kit MCP integration.

Shopping list management:
- **bobby060/anylist-mcp** (7 stars, 5 domain-grouped tools with 18+ actions) — AnyList integration for shopping lists, recipes, meal planning, and recipe collections
- **jessalva7/grocery-mcp-server** — Grocery management with Elasticsearch + Redis, ingesting data from Kaggle datasets


## Restaurant Reservations and Booking

Reservation systems are a mid-tier category in the food MCP ecosystem — not as developed as recipes or nutrition, but with some notable implementations.

**jrklein343-svg/restaurant-mcp** (2 stars) | **Language:** TypeScript | **12 tools**

The most feature-rich reservation server. Unifies Resy and OpenTable search in a single interface with real-time availability checking. Supports direct Resy booking and OpenTable booking links. Its most distinctive feature is a reservation "sniper" — an automated tool that watches for slots to open at hard-to-book restaurants and automatically reserves them. Uses Windows DPAPI for secure credential storage with rate limiting.

**samwang0723/mcp-booking** (14 stars) | **Language:** TypeScript | **5 tools** | **License:** MIT

Google Maps Places API integration focused on restaurant discovery. Finds restaurants by location, cuisine, mood, or event type within a 20km search radius. Includes an AI recommendation engine that returns top 3 picks with booking assistance.

Resy-specific servers:
- **musemen/resy-mcp-server** — Full Resy automation: authentication, search, booking, scheduling, waitlist management, calendar integration. SQLite + encrypted tokens.
- **Jpc54066/resy-mcp** — Resy search functionality

OpenTable access:
- **canadesk/opentable** (Apify) — OpenTable search results and reservation availability via Apify MCP


## Restaurant Reviews and Discovery

### Yelp (Official)

**Yelp/yelp-mcp** (23 stars) | **Language:** Python | **1 tool** | **License:** Apache-2.0

The official Yelp MCP server, backed by the Yelp Fusion AI API. Despite having only one tool (yelp_agent), it handles natural language business search, detailed queries, multi-turn conversations, and restaurant reservation requests. The single-tool design reflects Yelp's approach of letting the AI handle query interpretation rather than exposing multiple specialized endpoints. Docker and local deployment supported. Python 3.10+ required.

### Google Maps

**cablate/mcp-google-map** (236 stars) | **Language:** TypeScript | **18 tools** | **License:** MIT

Not food-specific, but heavily used for restaurant discovery. The 18 tools include search_nearby (filter by type: restaurant, cafe, bakery, etc.), search_places (free text), and place_details (reviews, hours, phone, website, price level). The 14 atomic tools can be composed by AI agents to build restaurant recommendation workflows: search nearby, filter by rating, get details, compare options.

### Review Scrapers

Multiple Apify-based MCP servers provide review data:
- **scraped/yelp-reviews** — Yelp review text and ratings extraction
- **agents/yelp-reviews** — Fast Yelp reviews scraper API
- **tri_angle/hotel-review-aggregator** — Multi-platform review aggregation across Tripadvisor, Yelp, Google Maps, Expedia, Hotels.com, Booking.com, and Airbnb — applicable to restaurants with hotel dining


## POS Systems and Restaurant Operations

### Square (Official)

**square/square-mcp-server** (95 stars) | **Language:** TypeScript | **3 tools** | **License:** Apache-2.0

The official Square MCP server provides access to 40+ Square services through three meta-tools: get_service_info, get_type_info, and make_api_request. This covers payments, orders, customers, inventory, bookings, loyalty, labor, team, and locations. Remote MCP via OAuth at mcp.squareup.com. Sandbox mode available. Read-only option for safety. Currently in beta.

Square is used by many restaurants, cafes, and food trucks, making this server immediately relevant for food service operations. An AI agent with Square MCP access could analyze sales trends, check inventory, manage loyalty programs, and review labor schedules — all through a single protocol.

### The Toast Gap

Toast is the #1 restaurant-specific POS system, used by hundreds of thousands of restaurants. It has no MCP server. A "Toast Notifications MCP Server" exists (by Naru Sensei), but this is for desktop notifications, not the restaurant POS system. Given Toast's dominance in the restaurant POS market, this is perhaps the single most impactful missing MCP integration in the food industry.

### Other POS Gaps

No MCP servers exist for:
- **Clover** — Popular with small-to-medium restaurants
- **Lightspeed** — Used in restaurants and retail
- **TouchBistro** — Restaurant-specific POS
- **SpotOn** — Growing restaurant POS platform
- **Revel Systems** — iPad POS for restaurants

### Order Management

**miyamo2/mcp-restaurant-order** (0 stars) | **Language:** Go | **License:** MIT

An educational implementation of basic restaurant ordering through MCP. Multi-language support (English/Japanese). While not production-ready, it demonstrates the architecture pattern for restaurant order management via MCP.


## Food Safety and Supply Chain

This category has minimal MCP coverage despite its critical importance.

**ryan-clinton/food-safety-supply-chain-mcp** (Apify) | **7 actors** | **Pay-per-use**

The only food safety MCP server found. Covers FDA recalls, adverse events, supplier hygiene ratings, ingredient risk tracing via trade flows, and contamination pathway detection. Hosted on Apify and requires an API token.

### What's Missing

The food safety gap is striking:
- **No HACCP compliance tracking** — HACCP (Hazard Analysis and Critical Control Points) is mandatory for many food businesses, yet no MCP server helps manage it
- **No temperature monitoring** — IoT kitchen sensors that track refrigerator, freezer, and holding temperatures have no MCP integration
- **No allergen management** — With food allergies affecting 32 million Americans, allergen tracking across menus, recipes, and ingredients remains manual
- **No health inspection data** — Restaurant health inspection scores are public data in most jurisdictions but have no MCP interface
- **No food traceability** — Farm-to-table supply chain tracking, increasingly important for food safety and sustainability, has zero MCP coverage


## Comparison of MCP Servers by Category

| Category | Servers | Official | Most Popular | Coverage Level |
|----------|---------|----------|-------------|----------------|
| Recipes & Cooking | 15+ | 0 | HowToCook-mcp (702 stars) | Strong |
| Nutrition Tracking | 15+ | 0 | mcp-opennutrition (172 stars) | Strong |
| Restaurant Discovery | 5+ | 1 (Yelp) | mcp-google-map (236 stars) | Good |
| Reservations | 5+ | 0 | mcp-booking (14 stars) | Moderate |
| Grocery & Shopping | 4+ | 1 (Instacart) | Instacart (official) | Moderate |
| POS Systems | 1 | 1 (Square) | Square (95 stars) | Weak (only Square) |
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
│             │     │ (Instacart)  │     │ (1,800+ stores)  │
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
│  AI Agent   │────▶│ Diet MCP     │────▶│ Yazio/Cronometer│
│             │     │ (yazio-mcp,  │     │ MyFitnessPal     │
│             │     │  cronometer) │     │ (food diary)      │
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

**Personal health information.** Nutrition trackers and diet apps contain sensitive health data. MCP servers for Yazio, Cronometer, MyFitnessPal, and FatSecret access personal food diaries, weight history, and health goals. The FatSecret MCP server uses encrypted credential storage and full OAuth 1.0a — a good pattern. Others store credentials less securely.

**Reservation and personal data.** Restaurant reservation MCP servers handle names, phone numbers, email addresses, and dining preferences. The restaurant-mcp server uses Windows DPAPI for credential encryption. Resy and OpenTable credentials grant access to reservation history and personal profiles.

**Food safety and allergen liability.** AI agents providing food information — recipes, nutrition data, allergen detection — carry implicit liability. If an OpenFoodFacts MCP server returns incorrect allergen data and an AI agent recommends the product, the consequences can be severe. This is not a technical problem MCP can solve, but it's a consideration for anyone building food AI workflows.

**API key management.** Many food MCP servers require API keys for commercial data sources (Spoonacular, Google Maps, Yelp Fusion, Nutritionix). Keys typically go in environment variables or configuration files. The Instacart MCP server uses OAuth for more secure access management. Servers like mcp-opennutrition that run entirely locally with embedded data avoid the API key issue entirely.

**Scraper legal risk.** Food delivery scrapers (DoorDash, UberEats via Apify) operate in a legal gray area. They may violate platform terms of service, and the data they return may not be accurate or current. Building production systems on scraper-based MCP servers is risky.


## Platform Landscape

### Official MCP Servers

Three food industry companies have released official MCP servers:

| Company | Server | Launch | Significance |
|---------|--------|--------|-------------|
| **Instacart** | Instacart Developer Platform MCP | Dec 2025 | First grocery company with MCP + ChatGPT integration. Production-ready. |
| **Yelp** | yelp-mcp (23 stars) | 2025 | Official Yelp Fusion AI integration. Real-time business data. |
| **Square** | square-mcp-server (95 stars) | 2025 | 40+ Square services via MCP. Beta. OAuth. |

### Companies Conspicuously Absent

| Company | Why It Matters | Market Position |
|---------|---------------|----------------|
| **Toast** | #1 restaurant POS | Hundreds of thousands of restaurant locations |
| **DoorDash** | 56% US delivery market share | $74B+ US delivery market |
| **Uber Eats** | 23% US delivery market share | Global presence |
| **Grubhub** | 16% US delivery market share | First mover in US delivery |
| **OpenTable** | Dominant reservation platform | 60,000+ restaurants |
| **Resy** | Premium reservation platform | High-end dining |
| **McDonald's** | Largest restaurant chain globally | 40,000+ locations |
| **Starbucks** | Largest coffee chain globally | 38,000+ locations |

The absence of Toast is particularly notable. Toast is purpose-built for restaurants, has extensive APIs, and serves the exact market segment that would benefit most from AI integration through MCP. An official Toast MCP server would instantly become the most valuable tool in the restaurant MCP ecosystem.


## Ecosystem Gaps

### Critical Gaps

**Restaurant POS systems.** Only Square has an MCP server, and it's in beta. Toast, Clover, Lightspeed, TouchBistro, SpotOn, and Revel — collectively serving the majority of restaurants — have nothing. POS accounts for ~45% of restaurant technology spending. This is the highest-impact gap.

**Kitchen operations.** Zero MCP servers exist for kitchen display systems (KDS), kitchen inventory management, food cost tracking, labor scheduling, or kitchen equipment monitoring. The back-of-house is completely unserved by MCP despite being where restaurants live and die operationally.

**Food delivery APIs.** No official MCP servers from any delivery platform. Restaurants managing orders across DoorDash, UberEats, and Grubhub — a nearly universal pain point — have no structured AI interface. The $74B+ US delivery market is accessible only through scrapers.

### Significant Gaps

**Food safety and compliance.** One Apify-based server for FDA recalls. Nothing for HACCP, temperature monitoring, allergen management, or health inspections. Given that food safety violations can close a restaurant, this gap has outsized consequences.

**Restaurant marketing and loyalty.** No restaurant-specific CRM, email marketing, or loyalty program MCP servers (beyond what Square covers). Restaurant marketing is one of the top AI use cases (53% of operators), but there's no MCP infrastructure for it.

### Complete Gaps

**Beverages.** No MCP servers for wine databases, brewery management, bar operations, coffee/cafe tools, or cocktail recipes (beyond one server with 200+ recipes including some cocktails). The beverage industry — worth hundreds of billions globally — has zero dedicated MCP coverage.

**Major restaurant chains.** No chain (McDonald's, Starbucks, Subway, Chick-fil-A, Domino's, etc.) has published an MCP server. No franchise management tools exist.

**Restaurant accounting.** No restaurant-specific accounting, food cost percentage calculators, or tip management MCP servers.


## Getting Started by Role

### Home Cook / Food Enthusiast
Start with **HowToCook-mcp** or **Spoonacular MCP** for recipe discovery, add **mcp-opennutrition** for nutritional analysis, and connect **Instacart MCP** for direct shopping. These three together create a complete cook-discover-shop pipeline.

### Nutrition-Conscious Individual
Start with **mcp-opennutrition** (300K+ foods, runs locally) for food data, add your preferred tracker (**yazio-mcp**, **fatsecret-mcp**, or **cronometer-mcp**) for daily logging, and add **OpenFoodFacts-MCP** for product scanning with Nutri-Score and allergen data.

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

- **Restaurant technology market:** $5.93B (2025) → $27.05B by 2035 (16.39% CAGR)
- **AI in food & beverages:** $13.39B (2025) → $88.37B by 2031 (36.96% CAGR)
- **US food delivery:** $74B+ industry, dominated by DoorDash (56%), Uber Eats (23%), Grubhub (16%)
- **AI adoption:** 79% of US restaurants use some form of AI; 69% actively adopting in 2026
- **Top AI applications:** Marketing/personalization (53%), predictive analytics (40%), voice ordering (39%)
- **Labor crisis:** 79.6% annual turnover, 45% report insufficient staffing, 92% face rising labor costs
- **Food waste:** 12.5 million tons from restaurants in 2024; 85%+ to landfill
- **ROI:** Tech adopters see 15% lower labor costs, 20% higher monthly sales; predictive demand cuts food waste 40%

The gap between AI adoption rates (79%) and MCP server availability (3 official servers) is enormous. Most restaurants are using AI through proprietary integrations — chatbots from their POS vendor, analytics from their delivery partner, marketing from their CRM. MCP's value proposition is unifying these into a single interface that any AI agent can use, but the infrastructure isn't there yet for most of the operational stack.

For every $1 invested in food waste reduction, restaurants save $7 in operating costs. An AI agent that could connect to POS data (what's selling), inventory systems (what's in stock), weather APIs (tomorrow's demand), and event calendars (is there a concert nearby?) through MCP could make real-time waste-reduction decisions. The recipe and nutrition pieces exist. The operational pieces don't — yet.

