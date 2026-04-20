# Food & Restaurant MCP Servers — Yelp, Instacart, Spoonacular, Uber Eats, Swiggy, Zomato, OpenFoodFacts, and More

> Food and restaurant MCP servers are enabling AI agents to search recipes, order food delivery, make restaurant reservations, track nutrition, manage grocery shopping, and explore cocktails.


Food and restaurant MCP servers are enabling AI agents to find recipes, order food delivery, make restaurant reservations, track calories, manage grocery lists, and mix cocktails — all through natural language. Instead of switching between Yelp, DoorDash, MyFitnessPal, and a recipe app, an AI agent can handle the entire food lifecycle: "Find me a chicken tikka masala recipe, check if I have the ingredients, order what's missing from Instacart, and book a table at an Indian restaurant for Saturday in case I don't feel like cooking."

The landscape spans nine areas: **recipes & cooking** (HowToCook, Spoonacular, CookWith, TheMealDB), **recipe managers** (Tandoor with 3 implementations), **nutrition & food databases** (OpenNutrition, USDA FoodData Central, Edamam, Nutritionix), **food tracking & calories** (OpenFoodFacts, calorie trackers, meal loggers), **restaurants & reservations** (Yelp, Resy, OpenTable, SevenRooms), **food delivery** (Uber Eats, DoorDash, Swiggy, Zomato), **grocery** (Instacart, Kroger), **beverages** (Bar Assistant cocktail search), and **multi-source food data** (barcode scanning, product databases).

The headline findings: **Official vendor adoption is exceptionally strong** — Yelp, Instacart, Swiggy, Zomato, Spoonacular, and Edamam all have official MCP servers. **Swiggy launched the first quick-commerce MCP globally** with Instamart covering 40,000+ SKUs. **HowToCook-mcp leads recipe servers** at 569 stars with smart meal planning. **OpenNutrition runs fully locally** with 300,000+ foods and no external API calls. **The restaurant reservation space has a unified Resy + OpenTable searcher** with a reservation sniper feature. **Nutrition tracking is heavily duplicated** — 6+ USDA wrappers doing essentially the same thing.

## Recipes & Cooking

### HowToCook MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [worryzyy/HowToCook-mcp](https://github.com/worryzyy/HowToCook-mcp) | 569 | TypeScript | MIT | 4 |

The **most popular food MCP server** — built on the viral Anduin2017/HowToCook project ("a programmer's guide to home cooking"), which has 70,000+ stars on GitHub. Four tools: query all recipes, query by category, get specific recipe (exact + fuzzy matching), and smart meal planning that generates weekly plans based on dietary restrictions, allergies, and number of diners. Available via npm (`howtocook-mcp`). Chinese-origin with English README.

The meal planning tool is the differentiator — it doesn't just search recipes but creates coherent weekly meal plans accounting for nutritional balance and dietary constraints. 569 stars makes it the highest-starred food-related MCP server.

### Spoonacular MCP (Official)

| Server | Language | Tools |
|--------|----------|-------|
| [ddsky/spoonacular-mcp](https://github.com/ddsky/spoonacular-mcp) | TypeScript | 6 |

Built by David Urbansky, the creator of the Spoonacular API itself — making this effectively an **official** server. Six tools: search recipes with filters, get recipe details, search ingredients by name, analyze nutrition for ingredients, find recipes by available ingredients ("what can I make with chicken and rice?"), and get random recipes. Requires a Spoonacular API key (free tier available).

A community alternative exists at [zym9863/spoonacular-server](https://github.com/zym9863/spoonacular-server) in TypeScript.

### CookWith MCP

| Server | Language | Tools | Notes |
|--------|----------|-------|-------|
| [blaideinc/recipe-mcp](https://github.com/blaideinc/recipe-mcp) | TypeScript | 4 | stdio transport, no API key (rate limited) |
| [blaideinc/cookwith-mcp](https://github.com/blaideinc/cookwith-mcp) | TypeScript | 4 | Streamable HTTP, production endpoint |

Two implementations of the CookWith.co recipe AI — one via stdio, one via streamable HTTP (production endpoint at cookwith.co/api/mcp). Tools: generate recipes from natural language, transform/remix recipes (make it vegan, adjust calories, change serving size), dietary support, and smart nutritional adaptations. No API key required for the stdio version (rate limited). The recipe transformation capability is unique — "take this lasagna recipe and make it dairy-free with 500 calories per serving."

### Other Recipe Servers

| Server | Language | Notes |
|--------|----------|-------|
| [suraj-yadav-aiml/recipe-mcp](https://github.com/suraj-yadav-aiml/recipe-mcp) | Python | TheMealDB API — recipe search, storage, meal plan creation |
| [salindersidhu/food-mcp-server](https://github.com/salindersidhu/food-mcp-server) | Python | TheMealDB + USDA FoodData Central — recipes with nutritional data |
| [disdjj/mcp-cook](https://github.com/disdjj/mcp-cook) | Python | Another HowToCook dataset implementation |
| [paulabaal12/kitchen-mcp](https://github.com/paulabaal12/kitchen-mcp) | Python | Ingredient-based recipe discovery with nutrition focus |
| [dmorrill/cooking-with-claude](https://github.com/dmorrill/cooking-with-claude) | JavaScript | Full cooking workflow — meal planning, prep, shopping, execution |
| [idjohnson/recipeMakerMCP](https://github.com/idjohnson/recipeMakerMCP) | — | Recipe creation with image generation via nanobanana |

salindersidhu/food-mcp-server stands out for combining TheMealDB recipes with USDA FoodData Central nutrition data — giving you both how to cook something and its nutritional breakdown. dmorrill/cooking-with-claude takes the most holistic approach with a full cooking workflow covering meal planning, prep, shopping, and execution.

## Tandoor Recipe Manager

Three separate MCP implementations for Tandoor Recipes, the popular self-hosted recipe manager:

| Server | Language | Notes |
|--------|----------|-------|
| [starbuck93/tandoor-mcp-server](https://github.com/starbuck93/tandoor-mcp-server) | TypeScript | Most comprehensive — recipes, meal plans, shopping lists CRUD, keyword/food/unit search |
| [ChristopherJMiller/tandoor-mcp](https://github.com/ChristopherJMiller/tandoor-mcp) | Rust | Rare Rust MCP — recipes, shopping, meal planning, inventory tracking |
| [mc-mario/tandoor-mcp](https://github.com/mc-mario/tandoor-mcp) | Python | Auto-creates missing ingredients/units/keywords — smart entity resolution |

Three implementations in three different languages (TypeScript, Rust, Python) for the same platform. mc-mario's Python version differentiates by auto-creating missing entities (ingredients, units, keywords) when adding recipes — a small but practical feature that avoids manual setup. Note: Tandoor limits API auth to 10 requests/day, which constrains all implementations.

## Nutrition & Food Databases

### OpenNutrition MCP

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [deadletterq/mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition) | 122 | TypeScript | 3 |

The **best nutrition MCP server** — 300,000+ food items running **fully locally** with no external API calls. Three tools: food search, nutritional data lookup, and barcode scanning. Comprehensive nutritional profiles including macros, vitamins, and minerals. 122 stars — second-highest in the food MCP category. The fully-local approach means no API keys, no rate limits, no privacy concerns with dietary data, and offline capability.

### USDA FoodData Central Servers

Six implementations of the USDA FoodData Central API — the US government's comprehensive food composition database:

| Server | Language | Notes |
|--------|----------|-------|
| [i-am-neon/nutrition-mcp-server-python](https://github.com/i-am-neon/nutrition-mcp-server-python) | Python | USDA lookup + automated meal planner with diet-specific prompts |
| [asachs01/nutrition-mcp](https://github.com/asachs01/nutrition-mcp) | JavaScript | 24-hour API cache, local meal log, nutrition goal targets |
| [zen-apps/mcp-nutrition-tools](https://github.com/zen-apps/mcp-nutrition-tools) | Python | Dual architecture (MCP + HTTP API), Docker/Cloud Run ready |
| [jlfwong/food-data-central-mcp-server](https://github.com/jlfwong/food-data-central-mcp-server) | TypeScript | Direct USDA API integration |
| [HemantaPatil/mcp_postgres](https://github.com/HemantaPatil/mcp_postgres) | Python | USDA data in local PostgreSQL, MCP Inspector web interface |
| [MCP-Forge/nutritionix-mcp-server](https://github.com/MCP-Forge/nutritionix-mcp-server) | Python | Nutritionix API — natural language exercise calorie estimates |

This is the most duplicated subcategory — 6 servers wrapping the same government API. i-am-neon's version adds an automated meal planner. asachs01's adds meal logging with goals. zen-apps' has a dual MCP + HTTP architecture for cloud deployment. For most users, mcp-opennutrition (above) is a better choice since it runs locally with a larger database.

### Official Food Data APIs

| Server | Notes |
|--------|-------|
| [Edamam MCP](https://developer.edamam.com/mcp-edamam-food/) | **Official** — food search by name or barcode (UPC/EAN/PLU), nutrient analysis, food image analysis via AI, REST + JSON-RPC + Inspector UI |
| [GuptaPurujit/nutritionix_mcp](https://github.com/GuptaPurujit/nutritionix_mcp) | Nutritionix API v2 — natural language meal logging, calorie/macro breakdowns |
| [fcoury/fatsecret-mcp](https://github.com/fcoury/fatsecret-mcp) | FatSecret — OAuth 1.0a, food diary logging |

Edamam's official MCP is notable for **food image analysis** — photograph your plate and get nutritional estimates. This is a genuinely useful AI-native feature that goes beyond simple database lookups.

## Food Tracking & Calories

### Calorie & Meal Trackers

| Server | Language | Notes |
|--------|----------|-------|
| [nagarjun226/food-tracker-mcp](https://github.com/nagarjun226/food-tracker-mcp) | Python | OpenFoodFacts — barcode scanning, dietary restriction management, consumption logging |
| [neonwatty/food-tracker-mcp](https://github.com/neonwatty/food-tracker-mcp) | Python | USDA — food logging, daily totals vs goals, local SQLite |
| [thitiph0n/calorie-tracker-mcp-server](https://github.com/thitiph0n/calorie-tracker-mcp-server) | TypeScript | Cloudflare Workers + D1 — BMR/TDEE via Mifflin-St Jeor, body composition tracking, OAuth 2.1 with PKCE |
| [VeriTeknik/daily-calorie-tracker](https://github.com/VeriTeknik/daily-calorie-tracker) | TypeScript | Built-in database of 100+ common foods, natural language entry, weekly reports |
| [ajaykallepalli/MCP_Food_Search](https://github.com/ajaykallepalli/MCP_Food_Search) | Python | Grocery price search + nutritional info + cross-store price comparison |
| [evangstav/personal-mcp](https://github.com/evangstav/personal-mcp) | Python | Multi-purpose server — nutrition module logs meals with hunger/satisfaction levels |

thitiph0n/calorie-tracker-mcp-server is the most production-ready — built on Cloudflare Workers with D1 database, OAuth 2.1 with PKCE authentication, BMR/TDEE calculations using the Mifflin-St Jeor equation, and historical body composition tracking. ajaykallepalli/MCP_Food_Search stands out for combining nutrition data with grocery pricing and cross-store price comparison.

### OpenFoodFacts Servers

Four implementations of the OpenFoodFacts database — the Wikipedia of food products:

| Server | Language | Notes |
|--------|----------|-------|
| [JagjeevanAK/OpenFoodFacts-MCP](https://github.com/JagjeevanAK/OpenFoodFacts-MCP) | Python | 7 tools — AI-powered analysis, product comparison, recipe suggestions |
| [noot-app/openfoodfacts-mcp-server](https://github.com/noot-app/openfoodfacts-mcp-server) | TypeScript | Parquet database with DuckDB — local, automatic dataset updates, file locking |
| [caleb-conner/open-food-facts-mcp](https://github.com/caleb-conner/open-food-facts-mcp) | Python | Nutri-Score, NOVA, Eco-Score analysis — Docker-ready |

noot-app's TypeScript version is architecturally interesting — it uses Parquet files with DuckDB for local querying rather than hitting the OpenFoodFacts API, with automatic dataset updates and file locking for concurrent safety. caleb-conner's version includes Nutri-Score, NOVA food processing classification, and Eco-Score environmental impact ratings.

## Restaurants & Reservations

### Yelp MCP (Official)

| Server | Language | Tools |
|--------|----------|-------|
| [Yelp/yelp-mcp](https://github.com/Yelp/yelp-mcp) | Python | 1 (agent-to-agent) |

**Official Yelp product** — a single `yelp_agent` tool with a unique agent-to-agent communication design. Instead of exposing multiple search/filter tools, you send natural language queries and the Yelp agent handles parsing, search, comparison, and itinerary planning. Supports follow-up via chat_id for multi-turn conversations. Uses the Yelp Fusion AI API.

The agent-to-agent design is architecturally significant — rather than an MCP server being a thin API wrapper, Yelp's server is itself an AI agent that understands context and maintains conversation state. This points toward a future where MCP servers are increasingly agentic.

### Restaurant Reservation Servers

| Server | Language | Notes |
|--------|----------|-------|
| [jrklein343-svg/restaurant-mcp](https://github.com/jrklein343-svg/restaurant-mcp) | TypeScript | **Unified Resy + OpenTable** — parallel search, reservation sniper, DPAPI-encrypted credentials |
| [samwang0723/mcp-booking](https://github.com/samwang0723/mcp-booking) | Go | Google Maps integration — AI recommendations, mood-based filtering |
| [OpenTable MCP (Apify)](https://apify.com/canadesk/opentable/api/mcp) | — | Scraper-based OpenTable search and availability |
| [SevenRooms MCP](https://mcpmarket.com) | — | Enterprise restaurant reservation management |
| Resy MCP (LobeHub) | — | Search, availability, reservations, waitlists |

jrklein343-svg/restaurant-mcp is the standout — it **searches both Resy and OpenTable simultaneously**, comparing results in parallel. The reservation sniper feature continuously monitors for table availability and books instantly when a slot opens. DPAPI-encrypted credential storage shows security awareness — the server never handles payment information. samwang0723/mcp-booking takes a mood-based approach: describe the occasion ("anniversary dinner" or "casual Friday with friends") and it recommends restaurants from Google Maps.

## Food Delivery

### Uber Eats MCP

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [ericzakariasson/uber-eats-mcp-server](https://github.com/ericzakariasson/uber-eats-mcp-server) | 217 | Python | — |

The **most popular food delivery MCP server** at 217 stars. A proof-of-concept using browser automation for restaurant search, menu exploration, and food ordering. While not production-grade, it demonstrates the potential for AI-driven food ordering workflows.

### DoorDash Servers

| Server | Language | Notes |
|--------|----------|-------|
| [JordanDalton/DoorDash-MCP-Server](https://github.com/JordanDalton/DoorDash-MCP-Server) | TypeScript | DoorDash API integration, requires DOORDASH_API_KEY |
| [amannm/doordash-mcp](https://github.com/amannm/doordash-mcp) | TypeScript | Minimal MCP-to-DoorDash-SDK — delivery quotes, creation, status, cancellation |
| [Doriandarko/webmcp-starter](https://github.com/Doriandarko/webmcp-starter) | — | Educational demo — DoorDash-style delivery workflow with 9 AI tools |

amannm/doordash-mcp is the most focused — a minimal transformation layer between MCP and the DoorDash SDK with delivery quotes, creation, status checking, and cancellation. Unlike Uber Eats, DoorDash has a developer API, so these servers use official SDK endpoints rather than browser automation.

### Official Food Delivery Platforms

| Server | Notes |
|--------|-------|
| [Swiggy MCP](https://github.com/Swiggy/swiggy-mcp-server-manifest) | **Official** — three services: swiggy-food (restaurant ordering), swiggy-instamart (grocery/quick-commerce, 40,000+ SKUs), swiggy-dineout (restaurant discovery). Launched January 2026. **First quick-commerce platform globally to adopt MCP.** |
| [Zomato MCP](https://github.com/Zomato/mcp-server-manifest) | **Official** — food ordering, order tracking, QR code payment. Production endpoint at mcp-server.zomato.com. Integrates with ChatGPT and Claude. |
| [GrubHub Scraper MCP](https://apify.com/natanielsantos/grubhub-scraper) | Apify-based scraper, not official |

Swiggy and Zomato — India's two largest food delivery platforms — both have official MCP servers, making India the most MCP-advanced food delivery market. Swiggy's Instamart integration is particularly notable as the **first quick-commerce (instant grocery delivery) MCP** globally, covering 40,000+ SKUs via natural language. Zomato's QR code payment feature shows how MCP can bridge digital ordering with physical restaurant experiences.

### Multi-Platform Delivery

| Server | Notes |
|--------|-------|
| MCP A2A AP2 "I'm Hungry" (Glama) | Multi-delivery service discovery across DoorDash, UberEats, and GrubHub with Stripe payment processing and cryptographically signed user authorization |

## Grocery Shopping

### Instacart MCP (Official)

| Server | Notes |
|--------|-------|
| [Instacart MCP](https://docs.instacart.com/developer_platform_api/guide/tutorials/mcp/) | **Official** — create recipes (with ingredients, instructions, measurements), create shopping lists, discover retailers by postal code. Shareable URLs for recipes and lists. |
| [sjufan84/instacart-cli](https://github.com/sjufan84/instacart-cli) | Go CLI + library for Instacart recipe and shopping list creation |

Instacart's official MCP creates a compelling workflow: describe a meal, get a recipe page with ingredients and instructions, then convert it to a shopping list with one-click ordering. The shareable URL feature means an AI agent can create a recipe, generate a link, and hand it to you for review before placing an order.

### Other Grocery Servers

| Server | Stars | Language | License | Notes |
|--------|-------|----------|---------|-------|
| [CupOfOwls/kroger-mcp](https://github.com/CupOfOwls/kroger-mcp) | 4 | Python | MIT | Product search, store finder, cart management, **shopping path optimization** |
| [jessalva7/grocery-mcp-server](https://github.com/jessalva7/grocery-mcp-server) | — | Python | — | General grocery item and shopping list management |

CupOfOwls/kroger-mcp has a unique **shopping path optimization tool** — it finds the optimal route through a Kroger store based on your shopping list. While a niche feature, it demonstrates how MCP servers can provide utility beyond simple API wrappers.

## Beverages

### Bar Assistant MCP

| Server | Language | Tools |
|--------|----------|-------|
| [zhdenny/bar-assistant-mcp-server](https://github.com/zhdenny/bar-assistant-mcp-server) | Python | 7+ |

Smart cocktail search with natural language + similarity matching, complete recipe retrieval, ingredient analysis, batch recipe retrieval, inventory-based recommendations, and advanced filtering by ABV, glassware, and preparation method. The similarity engine is clever — search for "something like a Negroni but less bitter" and it finds cocktails with similar profiles. 70%+ cache hit rate for performance. Integrates with Bar Assistant instances.

The only beverage-focused MCP server found — a gap given the popularity of wine, beer, and cocktail culture.

## What's Missing

Despite 55+ servers, significant gaps remain:

- **No official DoorDash or GrubHub MCP servers** — DoorDash has a developer API but no official MCP server; GrubHub only has third-party scrapers
- **No Whole Foods, Walmart Grocery, Amazon Fresh, or Target** — major US grocery platforms absent from MCP
- **No dietary condition management** — no celiac disease, diabetes, IBS, or allergy-aware meal planning with medical-grade data
- **No restaurant POS/operations** — no Toast, Square, Clover, or other point-of-sale system integrations
- **No food safety or allergen databases** — no FDA food recalls, no comprehensive allergen cross-reference databases
- **No meal kit services** — no HelloFresh, Blue Apron, Factor, or other subscription meal kit integrations
- **No food photography or plating** — no food styling, plating suggestions, or photo enhancement tools
- **No wine/beer databases** — no Vivino, Untappd, CellarTracker, or comprehensive beverage databases beyond cocktails
- **No food waste management** — no servers for tracking expiration dates, suggesting recipes for ingredients about to expire
- **No restaurant review aggregation** — Yelp is available but no Google Maps reviews, TripAdvisor, or The Infatuation
- **No farm-to-table or sourcing** — no farmers market directories, CSA boxes, or local food sourcing

## The Bottom Line

Food & Restaurant MCP servers earn **4.0 out of 5**. The official vendor participation is the headline story — Yelp, Instacart, Swiggy, Zomato, Spoonacular, and Edamam all have official MCP servers, making food one of the most commercially embraced MCP categories. India leads in food delivery MCP adoption with both major platforms (Swiggy and Zomato) offering production servers, and Swiggy's Instamart becoming the first quick-commerce MCP globally.

The recipe space is well-served by HowToCook-mcp (569 stars) with its smart meal planning and Spoonacular's official API access. Nutrition tracking has strong local-first options — OpenNutrition's 300,000+ food database runs entirely offline. The restaurant reservation space has a standout in the unified Resy + OpenTable searcher with its reservation sniper feature. Grocery shopping gets Instacart's official workflow and Kroger's creative shopping path optimization.

The weaknesses are the heavy duplication in nutrition tracking (6+ near-identical USDA wrappers), the absence of major US grocery chains beyond Kroger, and the lack of food delivery MCP servers from Western platforms — DoorDash, GrubHub, and UberEats only have community-built or proof-of-concept implementations while Indian platforms have production-grade official servers. The beverage space is notably underdeveloped with only one cocktail server and no wine or beer databases.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

