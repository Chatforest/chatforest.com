# MCP Food & Restaurant Industry Research Data
## Compiled: 2026-03-29
## Status: Research only — nothing has been tested or tried hands-on

---

## CATEGORY 1: RECIPE MANAGEMENT & COOKING

### Recipe Search & Generation

| Server | Stars | Lang | Tools | Status | License | Key Features |
|--------|-------|------|-------|--------|---------|-------------|
| [worryzyy/HowToCook-mcp](https://github.com/worryzyy/HowToCook-mcp) | ~702 | TypeScript | 5 | Community | MIT | Most popular food MCP server. Based on Anduin2017/HowToCook Chinese recipe database. Query all recipes, category-based search, specific recipe lookup, weekly meal planning, daily menu suggestions. Available via npm, supports stdio/HTTP/SSE. DXT for Claude Desktop. |
| [ddsky/spoonacular-mcp](https://github.com/ddsky/spoonacular-mcp) | 4 | JavaScript | 6 | Community | ISC | Wraps Spoonacular Food API. search_recipes, get_recipe_information, search_ingredients, analyze_nutrition, find_recipes_by_ingredients, get_random_recipes. Free tier: 150 API requests/day. |
| [blaideinc/recipe-mcp](https://github.com/blaideinc/recipe-mcp) | 0 | TypeScript | 2 | Community | MIT | Uses cookwith.co API. generate_recipe (natural language), transform_recipe (dietary modifications). Supports allergies, restrictions, caloric targeting. Rate limit: 20 req/hour. No API key needed. |
| [blaideinc/cookwith-mcp](https://github.com/blaideinc/cookwith-mcp) | 0 | JavaScript | 2 | Community | MIT | Streamable HTTP version of the cookwith.co MCP server. Same generate_recipe and transform_recipe tools. |
| [suraj-yadav-aiml/recipe-mcp](https://github.com/suraj-yadav-aiml/recipe-mcp) | N/A | Python | Multiple | Community | N/A | Comprehensive recipe search, storage, and meal planning using TheMealDB API. Built with FastMCP. |
| [D-C2211/mealserver](https://github.com/D-C2211/mealserver) | N/A | N/A | Multiple | Community | N/A | TheMealDB-based meal data server. Retrieves/manipulates meal data via API. |
| [Disdjj/mcp-cook](https://github.com/disdjj/mcp-cook) | N/A | N/A | 2 | Community | N/A | Based on HowToCook repository. Dish-name lookups and recipe retrieval. 200+ Chinese food and cocktail recipes. Lightweight stdio server. |
| [ruffood/cn-food-mcp](https://github.com/ruffood/cn-food-mcp) | 4 | TypeScript | 5 | Community | MIT | Chinese food nutrition data. ~1,725 foods with 25 nutrients per 100g. list_nutrients, search_food, get_nutrition, compare_foods, filter_by_nutrient. Bilingual Chinese/English labels. |

### Self-Hosted Recipe Managers

| Server | Stars | Lang | Tools | Status | License | Key Features |
|--------|-------|------|-------|--------|---------|-------------|
| [starbuck93/tandoor-mcp-server](https://github.com/starbuck93/tandoor-mcp-server) | 10 | JavaScript | 13 | Community | N/A | Integrates with Tandoor Recipe Manager (self-hosted). Recipe creation, meal plan management, recipe search, shopping list management (CRUD), reference data access (meal types, keywords, foods, units). |
| [mdlopresti/mealie-mcp](https://github.com/mdlopresti/mealie-mcp) | N/A | N/A | Multiple | Community | N/A | Integrates with Mealie (self-hosted recipe manager). Recipe management (search, create, update, import from URLs), meal planning, shopping list operations. Docker deployment available. |
| [rldiao/mealie-mcp-server](https://github.com/rldiao/mealie-mcp-server) | N/A | N/A | Multiple | Community | N/A | Alternative Mealie MCP server exposing Mealie APIs to Claude Desktop. |
| [counterbeing/mealie-mcp-ts](https://github.com/counterbeing/mealie-mcp-ts) | N/A | TypeScript | Multiple | Community | N/A | TypeScript implementation of Mealie MCP server. |
| [soggycactus/paprika-3-mcp](https://github.com/soggycactus/paprika-3-mcp) | 24 | Go | 2 | Community | MIT | MCP Server for Paprika 3 recipe manager. create_paprika_recipe, update_paprika_recipe. Recipes exposed as readable MCP resources. Homebrew install for macOS. |
| [aarons22/paprika-mcp](https://github.com/aarons22/paprika-mcp) | N/A | N/A | Multiple | Community | N/A | Read-only access to Paprika Recipe Manager. List/retrieve recipes, grocery items, meal plans. |

### Kitchen & Cooking Tools

| Server | Stars | Lang | Tools | Status | License | Key Features |
|--------|-------|------|-------|--------|---------|-------------|
| [paulabaal12/kitchen-mcp](https://github.com/paulabaal12/kitchen-mcp) | 0 | JS/Python | 11 | Community | N/A | Food/nutrition queries, recipe discovery by ingredients/diet, ingredient substitution suggestions, kitchen utensil recommendations, mood/season-based food recommendations. |
| [salindersidhu/food-mcp-server](https://github.com/salindersidhu/food-mcp-server) | 1 | Python | Multiple | Community | Apache 2.0 | FastAPI-based. Combines TheMealDB (recipes) + USDA Food Data Central (nutrition). Meal search, detail retrieval, category browsing, regional dish exploration. |
| [alexandrepa/mcp-cookidoo](https://github.com/alexandrepa/mcp-cookidoo) | 17 | Python | 4 | Community | MIT | Thermomix Cookidoo platform integration. connect_to_cookidoo, get_recipe_details, generate_recipe_structure, upload_custom_recipe. Unofficial. Smart kitchen appliance MCP bridge. |

---

## CATEGORY 2: NUTRITION TRACKING & DIET MANAGEMENT

### Standalone Nutrition Trackers

| Server | Stars | Lang | Tools | Status | License | Key Features |
|--------|-------|------|-------|--------|---------|-------------|
| [deadletterq/mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition) | 172 | TypeScript | 4 | Community | MIT | Most popular nutrition MCP. 300,000+ food items from USDA, CNF, FRIDA, AUSNUT. Search by name, browse foods, get by ID, barcode lookup. Runs entirely locally — no external API calls. Docker available. |
| [nutrition-mcp.com](https://nutrition-mcp.com) | N/A | N/A | Multiple | Commercial (Free) | N/A | Cloud-hosted nutrition tracker for Claude. Natural language meal logging, calorie/macro estimation, daily/weekly summaries. Free, no premium tiers. Works with Claude.ai, desktop, mobile, and any MCP client with OAuth 2.0 PKCE. |
| [nagarjun226/food-tracker-mcp](https://github.com/nagarjun226/food-tracker-mcp) | 6 | Python | 7 | Community | N/A | OpenFoodFacts integration. Barcode/keyword search, nutrition analysis, dietary restriction management, food consumption logging, meal categorization. Local JSON persistence. |
| [neonwatty/food-tracker-mcp](https://github.com/neonwatty/food-tracker-mcp) | 0 | JS/TS | 6 | Community | MIT | USDA FoodData Central. search_food, log_food, get_daily_log, set_goals, get_summary, delete_entry. SQLite storage. |
| [VeriTeknik/daily-calorie-tracker](https://github.com/VeriTeknik/daily-calorie-tracker) | 0 | JS/TS | 4 | Community | MIT | Natural language meal logging. add_meal, get_daily_summary, get_weekly_report, search_food. SQLite persistence. 100+ built-in food items. |
| [thitiph0n/calorie-tracker-mcp-server](https://github.com/thitiph0n/calorie-tracker-mcp-server) | 3 | TypeScript | 8 | Community | N/A | Cloudflare Workers + D1 database. BMR/TDEE calculations (Mifflin-St Jeor). OAuth 2.1 with PKCE. Food tracking, profile management, admin tools. |
| [caloriesclub.app](https://www.caloriesclub.app/en/mcp) | N/A | N/A | Multiple | Commercial | N/A | AI-powered calorie tracking with photo recognition, barcode scanning, voice logging. MCP server for ChatGPT, Claude, or any MCP-compatible client. |

### Platform-Connected Nutrition Trackers

| Server | Stars | Lang | Tools | Status | License | Key Features |
|--------|-------|------|-------|--------|---------|-------------|
| [fliptheweb/yazio-mcp](https://github.com/fliptheweb/yazio-mcp) | 25 | JS/TS | 11 | Community | MIT | Unofficial Yazio integration. Daily summaries, food database search, meal logging, exercise/water intake tracking, weight history. Uses reverse-engineered API — may break. |
| [pshortino/cronometer-mcp](https://libraries.io/pypi/cronometer-mcp) | N/A | Python | Multiple | Community | N/A | Cronometer nutrition data. Food logs, daily macro/micro summaries, CSV exports, diary management, fasting tracking, biometrics, recurring foods. Requires paid Cronometer account. Uses GWT-RPC protocol. |
| [fcoury/fatsecret-mcp](https://github.com/fcoury/fatsecret-mcp) | 6 | TypeScript | 11 | Community | N/A | FatSecret API integration. Full 3-legged OAuth 1.0a. Food/recipe database search, user food diary access, food entry addition. Encrypted credential storage. |
| [ai-mcp-garage/mcp-myfitnesspal](https://github.com/ai-mcp-garage/mcp-myfitnesspal) | N/A | Python | Multiple | Community | N/A | MyFitnessPal data retrieval via MCP. FastMCP server. |

### Food Data APIs (USDA, Open Food Facts)

| Server | Stars | Lang | Tools | Status | License | Key Features |
|--------|-------|------|-------|--------|---------|-------------|
| [jlfwong/food-data-central-mcp-server](https://github.com/jlfwong/food-data-central-mcp-server) | 10 | TypeScript | 1 tool + 3 resources | Community | N/A | USDA FoodData Central API. search-foods tool, food://details, food://foods, food://list resources. Pagination, multiple dataset types (Foundation, SR Legacy, Survey, Branded). |
| [FelipeAdachi/mcp-food-data-central](https://github.com/FelipeAdachi/mcp-food-data-central) | 2 | Python | 3 | Community | MIT | USDA FoodData Central. search_foods, get_food_details, get_multiple_foods (batch up to 20). Docker + Python deployment. SSE/stdio transport. |
| [JagjeevanAK/OpenFoodFacts-MCP](https://github.com/JagjeevanAK/OpenFoodFacts-MCP) | 14 | TypeScript | 20+ | Community | AGPL-3.0 | Most comprehensive Open Food Facts server. Search, barcode lookup, Nutri-Score, Eco-Score, allergen detection, additive identification, AI-powered insights from Robotoff, pricing data, educational resources. |
| [noot-app/openfoodfacts-mcp-server](https://github.com/noot-app/openfoodfacts-mcp-server) | 2 | Go | 3 | Community | MIT | Open Food Facts via DuckDB + Parquet. Brand/name search, barcode search, simplified search. Dual mode: STDIO (local) + HTTP (remote with auth). |
| [caleb-conner/open-food-facts-mcp](https://github.com/caleb-conner/open-food-facts-mcp) | N/A | N/A | Multiple | Community | N/A | Open Food Facts access for product information, nutritional data, environmental scores. |
| [MCP-Forge/nutritionix-mcp-server](https://github.com/MCP-Forge/nutritionix-mcp-server) | 3 | Python | 3 | Community | N/A | Nutritionix API integration. Food search, natural language meal parsing, exercise calorie estimation. |

---

## CATEGORY 3: FOOD DELIVERY PLATFORMS

### Multi-Platform Ordering

| Server | Stars | Lang | Tools | Status | License | Key Features |
|--------|-------|------|-------|--------|---------|-------------|
| [tas1337/mcp-Im-hungry](https://github.com/tas1337/mcp-Im-hungry) | 1 | TypeScript | 4 | Community | MIT | Multi-platform food delivery via A2A protocol. search_restaurants, get_menu, search_menu_items, check_delivery_estimate. Mock agents for DoorDash/UberEats/Grubhub. Stripe AP2 payment integration with cryptographic mandates. Demonstration/proof-of-concept. |

### DoorDash Scrapers (Apify MCP)

| Server | Platform | Key Features |
|--------|----------|-------------|
| [sovereigntaylor/doordash-scraper](https://apify.com/sovereigntaylor/doordash-scraper/api/mcp) | Apify | Restaurants, menus, prices, ratings, delivery fees, delivery times. JSON/CSV/Excel export. |
| [axlymxp/doordash-store-scraper](https://apify.com/axlymxp/doordash-store-scraper/api/mcp) | Apify | Store search by location with customizable radius. Detailed store information. |
| [consummate_mandala/doordash-menu-scraper](https://apify.com/consummate_mandala/doordash-menu-scraper/api/mcp) | Apify | Menu extraction with automatic pagination and proxy rotation. |
| [yasmany.casanova/doordash-restaurant-scraper](https://apify.com/yasmany.casanova/doordash-restaurant-scraper/api/mcp) | Apify | Menu and restaurant data extraction API. |

### UberEats Scrapers (Apify MCP)

| Server | Platform | Key Features |
|--------|----------|-------------|
| [crscrapers/ubereats-menu-scraper](https://apify.com/crscrapers/ubereats-menu-scraper---v2/api/mcp) | Apify | Full product, price, and modifier data extraction. |

### Other Food Delivery Scrapers (Apify MCP)

| Server | Platform | Key Features |
|--------|----------|-------------|
| [clearpath/thefork-scraper](https://apify.com/clearpath/thefork-scraper/api/mcp) | Apify | TheFork (European restaurant platform) — restaurants, reviews, menus. |
| [yasmany.casanova/rappi-restaurant-scraper](https://apify.com/yasmany.casanova/rappi-restaurant-scraper/api/mcp) | Apify | Rappi (Latin American delivery) — menu and restaurant data. |
| [fortuitous_pirate/weee-scraper](https://apify.com/fortuitous_pirate/weee-scraper/api/mcp) | Apify | Weee! Asian grocery delivery — product data extraction. |

**Note:** No official MCP servers exist from DoorDash, UberEats, or Grubhub. All current integrations are community-built scrapers or mock APIs.

---

## CATEGORY 4: GROCERY & MEAL KIT SERVICES

### Instacart (Official)

| Server | Stars | Lang | Tools | Status | License | Key Features |
|--------|-------|------|-------|--------|---------|-------------|
| [Instacart Developer Platform MCP](https://docs.instacart.com/developer_platform_api/guide/tutorials/mcp/) | N/A | N/A | 3 | **Official** | N/A | **The most significant official food industry MCP server.** Create recipe pages (with ingredients, instructions, URL), create shopping list pages, get nearby retailers by postal code. Production endpoint: mcp.instacart.com. Dev: mcp.dev.instacart.tools. First grocery company to integrate MCP with ChatGPT (Dec 2025). 1,800+ retailers, 2B+ products. |

### HelloFresh

| Server | Stars | Lang | Tools | Status | License | Key Features |
|--------|-------|------|-------|--------|---------|-------------|
| [markswendsen-code/mcp-hellofresh](https://github.com/markswendsen-code/mcp-hellofresh) | N/A | N/A | Multiple | Community | N/A | HelloFresh meal kit management. Menu browsing, meal selection, delivery schedule management, dietary preferences, order history, recipe rating. Uses Playwright browser automation (unofficial). |

### Shopping List Management

| Server | Stars | Lang | Tools | Status | License | Key Features |
|--------|-------|------|-------|--------|---------|-------------|
| [bobby060/anylist-mcp](https://github.com/bobby060/anylist-mcp) | 7 | JavaScript | 5 (18+ actions) | Community | N/A | AnyList integration. Shopping lists, recipes, meal planning, recipe collections. 5 domain-grouped tools. Unofficial. |
| [jessalva7/grocery-mcp-server](https://github.com/jessalva7/grocery-mcp-server) | 0 | Python | Multiple | Community | N/A | Grocery management with Elasticsearch + Redis. Data ingestion from Kaggle datasets. Store inventory management. |

---

## CATEGORY 5: RESTAURANT RESERVATION & BOOKING

| Server | Stars | Lang | Tools | Status | License | Key Features |
|--------|-------|------|-------|--------|---------|-------------|
| [samwang0723/mcp-booking](https://github.com/samwang0723/mcp-booking) | 14 | TypeScript | 5 | Community | MIT | Google Maps Places API integration. Restaurant discovery by location/cuisine/mood/event type. AI recommendation engine (top 3 picks). Booking assistance. 20km search radius. |
| [jrklein343-svg/restaurant-mcp](https://github.com/jrklein343-svg/restaurant-mcp) | 2 | TypeScript | 12 | Community | N/A | **Most feature-rich reservation server.** Unified Resy + OpenTable search. Real-time availability. Direct Resy booking; OpenTable booking links. Reservation "sniper" (auto-book when slots open). Secure credential storage (Windows DPAPI). Rate limiting. |
| [musemen/resy-mcp-server](https://github.com/musemen/resy-mcp-server) | N/A | Python | Multiple | Community | N/A | Resy-only reservation automation. Authentication, restaurant search, booking, automated scheduling, waitlist management, calendar integration. SQLite + encrypted tokens. |
| [Jpc54066/resy-mcp](https://github.com/Jpc54066/resy-mcp) | N/A | N/A | Multiple | Community | N/A | Resy search functionality testing. |
| [canadesk/opentable](https://apify.com/canadesk/opentable/api/mcp) | N/A | Apify | Multiple | Community | N/A | OpenTable search results, restaurants, and reservation availability via Apify MCP. |

---

## CATEGORY 6: RESTAURANT REVIEWS & DISCOVERY

| Server | Stars | Lang | Tools | Status | License | Key Features |
|--------|-------|------|-------|--------|---------|-------------|
| [Yelp/yelp-mcp](https://github.com/Yelp/yelp-mcp) | 23 | Python | 1 | **Official** | Apache-2.0 | **Official Yelp MCP server.** Single yelp_agent tool handles natural language business search, detailed queries, multi-turn conversations, restaurant reservations. Yelp Fusion AI API. Real-time data. Docker + local deployment. Python 3.10+. |
| [cablate/mcp-google-map](https://github.com/cablate/mcp-google-map) | 236 | TypeScript | 18 | Community | MIT | Google Maps integration with strong restaurant discovery. search_nearby (by type: restaurant, cafe, etc.), search_places (free text), place_details (reviews, hours, phone, website). 18 tools total (14 atomic + 4 composite). |
| [scraped/yelp-reviews](https://apify.com/scraped/yelp-reviews/api/mcp) | N/A | Apify | Multiple | Community | N/A | Yelp reviews scraper via Apify MCP. Review text, ratings extraction. |
| [agents/yelp-reviews](https://apify.com/agents/yelp-reviews/api/mcp) | N/A | Apify | Multiple | Community | N/A | Fast Yelp reviews scraper API via Apify MCP. |
| [tri_angle/hotel-review-aggregator](https://apify.com/tri_angle/hotel-review-aggregator/api/mcp) | N/A | Apify | Multiple | Community | N/A | Multi-platform review aggregation: Tripadvisor, Yelp, Google Maps, Expedia, Hotels.com, Booking.com, Airbnb. Applicable to restaurants with hotel dining. |

---

## CATEGORY 7: POS SYSTEMS & RESTAURANT OPERATIONS

### Point-of-Sale Systems

| Server | Stars | Lang | Tools | Status | License | Key Features |
|--------|-------|------|-------|--------|---------|-------------|
| [square/square-mcp-server](https://github.com/square/square-mcp-server) | 95 | TypeScript | 3 | **Official** | Apache-2.0 | **Official Square MCP server.** get_service_info, get_type_info, make_api_request. Access to 40+ Square services: payments, orders, customers, inventory, bookings, loyalty, labor, team, locations. Remote MCP with OAuth (mcp.squareup.com). Sandbox mode. Read-only option. Beta. |

**Gap Analysis — POS Systems:**
- **Toast POS**: No MCP server. Toast has a "Toast Notifications MCP Server" (by Naru Sensei) but this is for desktop notifications, NOT the restaurant POS system.
- **Clover POS**: No MCP server found.
- **Lightspeed**: No MCP server found.
- **Revel Systems**: No MCP server found.
- **TouchBistro**: No MCP server found.
- **SpotOn**: No MCP server found.

### Restaurant Order Management

| Server | Stars | Lang | Tools | Status | License | Key Features |
|--------|-------|------|-------|--------|---------|-------------|
| [miyamo2/mcp-restaurant-order](https://github.com/miyamo2/mcp-restaurant-order) | 0 | Go | Few | Community | MIT | Educational/toy project. Basic MCP restaurant order implementation. Multi-language (EN/JP). |

---

## CATEGORY 8: FOOD SAFETY & SUPPLY CHAIN

| Server | Stars | Lang | Tools | Status | License | Key Features |
|--------|-------|------|-------|--------|---------|-------------|
| [ryan-clinton/food-safety-supply-chain-mcp](https://apify.com/ryanclinton/food-safety-supply-chain-mcp) | N/A | Apify | 7 actors | Community | Pay-per-use | FDA recalls, adverse events, supplier hygiene ratings, ingredient risk tracing via trade flows, contamination pathway detection. Hosted on Apify. Requires Apify API token. |

**Gap Analysis — Food Safety:**
- No MCP servers for HACCP compliance tracking
- No MCP servers for temperature monitoring / IoT kitchen sensors
- No MCP servers for food allergen management systems
- No MCP servers for health department inspection data
- No dedicated food traceability / farm-to-table MCP servers

---

## CATEGORY 9: BEVERAGES & SPECIALTY

**No dedicated MCP servers found for:**
- Wine databases/sommeliers
- Beer/brewery management
- Coffee/cafe operations
- Cocktail/bartending
- Starbucks, McDonald's, or other major food chain APIs

**Note:** The [Disdjj/mcp-cook](https://github.com/disdjj/mcp-cook) server includes some cocktail recipes within its 200+ recipe database.

---

## OFFICIAL vs. COMMUNITY SERVERS SUMMARY

### Official MCP Servers (from the company)

| Company | Server | Status | Notes |
|---------|--------|--------|-------|
| **Instacart** | [Instacart Developer Platform MCP](https://docs.instacart.com/developer_platform_api/guide/tutorials/mcp/) | Production | First grocery company with ChatGPT MCP integration (Dec 2025). 1,800+ retailers. |
| **Yelp** | [Yelp/yelp-mcp](https://github.com/Yelp/yelp-mcp) | Production | Official Yelp Fusion AI integration. Real-time business data. |
| **Square** | [square/square-mcp-server](https://github.com/square/square-mcp-server) | Beta | 40+ Square service APIs. OAuth authentication. |

### Notable Community Servers (by adoption/stars)

| Server | Stars | Category |
|--------|-------|----------|
| HowToCook-mcp | ~702 | Recipe/Cooking |
| mcp-google-map | 236 | Restaurant Discovery |
| mcp-opennutrition | 172 | Nutrition Data |
| square-mcp-server | 95 | POS/Business |
| yazio-mcp | 25 | Diet Tracking |
| paprika-3-mcp | 24 | Recipe Management |
| Yelp MCP | 23 | Reviews/Discovery |
| mcp-cookidoo | 17 | Smart Kitchen |
| OpenFoodFacts-MCP | 14 | Food Product Data |
| mcp-booking | 14 | Restaurant Booking |

---

## MARKET DATA & INDUSTRY STATISTICS

### Restaurant Technology Market
- Global restaurant technology market: **USD 5.93B** (2025), projected **USD 6.9B** (2026), reaching **USD 27.05B** by 2035 (16.39% CAGR)
- POS systems account for ~45% of total restaurant technology adoption
- ~65% of restaurants use integrated POS and payment systems

### AI in Food & Beverages Market
- **USD 13.39B** (2025) growing to **USD 18.34B** (2026), forecast to reach **USD 88.37B** by 2031 (36.96% CAGR)
- Alternative estimate: projected to reach **$79.38B** by 2030 at 42.3% CAGR

### Online Food Delivery Market
- Global: **$1.40 trillion** revenue (2025), growing to **$715.89B** online-only by 2034 (9.5% CAGR)
- US market: **$74+ billion** industry
- DoorDash: **56%** US market share
- Uber Eats: **23%** US market share
- Grubhub: **16%** US market share
- 2,656 million online food delivery users forecast by 2026

### AI Adoption in Restaurants
- **79%** of U.S. restaurants now utilize some form of AI
- **69%** of restaurants adopting AI (2026 data)
- **73%** of restaurant operators planning AI investment
- **81%** of operators plan to increase AI use in the future
- **51%** of brands currently investing in AI, 22% plan to start this year
- Most common AI applications: marketing/personalization (53%), predictive analytics (40%), voice ordering (39%)
- Chatbots are the most widely deployed AI tool (60% daily use)

### Restaurant Industry Pain Points
- Average annual turnover rate: **79.6%**
- **45%** of operators report insufficient staffing
- **92%** experienced rising labor costs in last 12 months
- **89%** expect labor costs to increase
- **70%** of QSR operators cite unfilled positions
- 41% of consumers prefer minimal AI interaction in dining

### ROI & Efficiency Data
- Kitchen automation adopters: **69%** report improved efficiency and productivity
- Restaurants using predictive demand: **40%** less food waste, **25%** lower labor costs
- Tech adopters: labor costs drop **15%**, monthly sales rise **20%**
- Analytics platform users: **15%** lower food costs, **22%** improved forecast accuracy
- For every **$1** invested in food waste reduction, restaurants save **$7** in operating costs

### Food Waste Statistics
- Restaurants/foodservice generated **12.5 million tons** of surplus food in 2024
- More than **85%** went to landfill or incineration
- **30-40%** of US food supply is wasted

---

## ECOSYSTEM GAP ANALYSIS

### Major Gaps in Current MCP Food Ecosystem

**1. Restaurant POS Systems (CRITICAL GAP)**
- Only Square has an official MCP server
- No Toast POS MCP server (despite Toast being the #1 restaurant POS)
- No Clover, Lightspeed, TouchBistro, SpotOn, or Revel MCP servers
- This is the single largest gap given POS is 45% of restaurant tech spend

**2. Food Delivery Platform APIs (SIGNIFICANT GAP)**
- No official MCP servers from DoorDash, UberEats, or Grubhub
- Only scrapers and mock/demo servers exist
- Instacart is the sole grocery delivery platform with an official MCP server
- No official DoorDash Drive (white-label delivery) MCP integration

**3. Kitchen Operations & Back-of-House (SIGNIFICANT GAP)**
- No kitchen display system (KDS) MCP servers
- No inventory management MCP servers
- No labor scheduling MCP servers
- No food cost management MCP servers
- No kitchen IoT / smart equipment MCP servers (beyond Thermomix Cookidoo)

**4. Food Safety & Compliance (SIGNIFICANT GAP)**
- Only one Apify-based food safety server (FDA recalls)
- No HACCP compliance tracking
- No temperature monitoring integration
- No food allergen management
- No health inspection data access

**5. Restaurant Marketing & Loyalty (MODERATE GAP)**
- No restaurant loyalty program MCP servers
- No restaurant-specific CRM MCP servers
- No restaurant email/SMS marketing MCP servers
- Square MCP covers loyalty partially through Square Loyalty

**6. Beverage Industry (COMPLETE GAP)**
- No wine database/sommelier MCP servers
- No beer/brewery MCP servers
- No bar/nightclub operations MCP servers
- No beverage inventory MCP servers

**7. Major Restaurant Chains (COMPLETE GAP)**
- No McDonald's, Starbucks, Subway, Chick-fil-A, or any major chain MCP servers
- No franchise management MCP servers

**8. Accounting & Financial (MODERATE GAP)**
- No restaurant-specific accounting MCP servers
- No food cost percentage calculators
- No tip management / payroll MCP servers
- Square MCP partially covers payment processing

### Areas with Good Coverage

**1. Recipe Search & Discovery** — Well-covered with 10+ servers, multiple APIs (Spoonacular, TheMealDB, HowToCook)

**2. Nutrition Tracking** — Strong coverage with 15+ servers spanning USDA, Open Food Facts, Nutritionix, FatSecret, Yazio, Cronometer, MyFitnessPal

**3. Restaurant Discovery & Reviews** — Good coverage via Yelp (official), Google Maps, and various scraper-based MCP servers

**4. Reservation Booking** — Moderate coverage via Resy and OpenTable community servers

**5. Grocery Shopping** — Instacart's official MCP server provides excellent coverage

---

## NOTABLE PATTERNS & OBSERVATIONS

1. **Consumer-facing tools dominate**: Most food MCP servers target consumers (recipes, nutrition tracking, restaurant discovery) rather than restaurant operators (POS, inventory, kitchen ops).

2. **Instacart leads in official adoption**: Instacart's December 2025 ChatGPT integration was a landmark moment — first grocery company to enable full MCP-powered checkout within an AI assistant.

3. **Chinese food/recipe ecosystem is strong**: HowToCook-mcp (702 stars) is the most popular food MCP server, and multiple Chinese-language food/nutrition servers exist (cn-food-mcp, mcp-cook).

4. **Nutrition data is fragmented**: 15+ servers cover nutrition, but they connect to different databases (USDA, Open Food Facts, Nutritionix, FatSecret) with varying completeness and accuracy.

5. **Self-hosted recipe managers are well-served**: Tandoor, Mealie, and Paprika all have MCP integrations, reflecting the MCP community's developer-oriented user base.

6. **Scraper-based approach dominates food delivery**: Without official APIs from DoorDash/UberEats/Grubhub, the community relies on Apify scrapers, which are fragile and TOS-questionable.

7. **B2B restaurant operations is wide open**: The back-of-house / operations side of restaurants has almost zero MCP coverage despite being a multi-billion-dollar market segment.

8. **Smart kitchen appliance integration is nascent**: Only Thermomix/Cookidoo has an MCP server. No integrations for smart ovens, sous vide devices, coffee machines, or other IoT kitchen appliances.

---

## SOURCES

### GitHub Repositories
- https://github.com/worryzyy/HowToCook-mcp
- https://github.com/ddsky/spoonacular-mcp
- https://github.com/starbuck93/tandoor-mcp-server
- https://github.com/blaideinc/recipe-mcp
- https://github.com/blaideinc/cookwith-mcp
- https://github.com/paulabaal12/kitchen-mcp
- https://github.com/salindersidhu/food-mcp-server
- https://github.com/JagjeevanAK/OpenFoodFacts-MCP
- https://github.com/alexandrepa/mcp-cookidoo
- https://github.com/deadletterq/mcp-opennutrition
- https://github.com/nagarjun226/food-tracker-mcp
- https://github.com/neonwatty/food-tracker-mcp
- https://github.com/VeriTeknik/daily-calorie-tracker
- https://github.com/thitiph0n/calorie-tracker-mcp-server
- https://github.com/fliptheweb/yazio-mcp
- https://github.com/fcoury/fatsecret-mcp
- https://github.com/ai-mcp-garage/mcp-myfitnesspal
- https://github.com/jlfwong/food-data-central-mcp-server
- https://github.com/FelipeAdachi/mcp-food-data-central
- https://github.com/noot-app/openfoodfacts-mcp-server
- https://github.com/MCP-Forge/nutritionix-mcp-server
- https://github.com/ruffood/cn-food-mcp
- https://github.com/tas1337/mcp-Im-hungry
- https://github.com/samwang0723/mcp-booking
- https://github.com/jrklein343-svg/restaurant-mcp
- https://github.com/Yelp/yelp-mcp
- https://github.com/square/square-mcp-server
- https://github.com/cablate/mcp-google-map
- https://github.com/soggycactus/paprika-3-mcp
- https://github.com/bobby060/anylist-mcp
- https://github.com/disdjj/mcp-cook
- https://github.com/miyamo2/mcp-restaurant-order
- https://github.com/jessalva7/grocery-mcp-server
- https://github.com/suraj-yadav-aiml/recipe-mcp
- https://github.com/D-C2211/mealserver
- https://github.com/caleb-conner/open-food-facts-mcp

### Official Documentation
- https://docs.instacart.com/developer_platform_api/guide/tutorials/mcp/
- https://business.yelp.com/data/solutions/ai-agents/
- https://nutrition-mcp.com
- https://www.caloriesclub.app/en/mcp

### MCP Directories
- https://www.pulsemcp.com
- https://mcpmarket.com
- https://glama.ai/mcp/servers
- https://lobehub.com/mcp

### Apify MCP Servers
- https://apify.com/sovereigntaylor/doordash-scraper/api/mcp
- https://apify.com/axlymxp/doordash-store-scraper/api/mcp
- https://apify.com/consummate_mandala/doordash-menu-scraper/api/mcp
- https://apify.com/crscrapers/ubereats-menu-scraper---v2/api/mcp
- https://apify.com/clearpath/thefork-scraper/api/mcp
- https://apify.com/yasmany.casanova/rappi-restaurant-scraper/api/mcp
- https://apify.com/fortuitous_pirate/weee-scraper/api/mcp
- https://apify.com/canadesk/opentable/api/mcp
- https://apify.com/scraped/yelp-reviews/api/mcp

### Market Research Sources
- https://www.businessresearchinsights.com/market-reports/restaurant-technology-market-118085
- https://www.thebusinessresearchcompany.com/report/ai-in-food-and-beverages-global-market-report
- https://www.mordorintelligence.com/industry-reports/artificial-intelligence-in-food-and-beverages-market
- https://finance.yahoo.com/news/united-states-online-food-delivery-135000318.html
- https://oysterlink.com/spotlight/food-delivery-market-share-statistics/
- https://pos.toasttab.com/blog/data/ai-in-restaurants
- https://foodinstitute.com/focus/6-ways-ai-will-impact-restaurants-in-2026/
- https://www.deloitte.com/us/en/insights/industry/retail-distribution/ai-in-restaurants.html
- https://restauranttechnologynews.com/2026/02/research-69-of-restaurants-are-adopting-ai-while-81-increase-digital-marketing-investment/
- https://www.restolabs.com/blog/restaurant-technology-trends
- https://www.incentivio.com/blog-news-restaurant-industry/2026-restaurant-technology-trends-what-forward-thinking-operators-need-to-know
