---
title: "Food & Restaurant MCP Servers — Yelp, Instacart, Spoonacular, Uber Eats, Swiggy, Zomato, OpenFoodFacts, and More"
date: 2026-03-15T17:33:00+09:00
description: "Food and restaurant MCP servers are enabling AI agents to search recipes, order food delivery, make restaurant reservations, track nutrition, manage grocery shopping, and explore cocktails and beer."
og_description: "Food & restaurant MCP servers: HowToCook (724 stars, meal planning), OpenNutrition (187 stars, 300K+ foods), Uber Eats (229 stars), official Yelp MCP (agent-to-agent), official Instacart (recipes + shopping), Swiggy Builders Club now open (3 MCP servers 18+ tools invite-led developer platform), official Zomato (168 stars), Spoonacular (official), Edamam (official), Picnic supermarket (72 stars 30+ tools NL/DE/FR), H-E-B grocery (28 stars 20+ tools coupon clipping), Kroger MCP (61 stars +1425%), Toast POS (5 stars 50+ tools), Whole Foods browser automation, HelloFresh meal kit, Mealie recipe manager, NEW iFood MCP (Brazil, OAuth 2.1), Walmart community MCP. Rating: 4.0/5."
content_type: "Review"
card_description: "Food and restaurant MCP servers for recipes, food delivery, restaurant reservations, nutrition tracking, grocery shopping, cocktail discovery, and beer. This category has surprisingly strong official vendor participation — Yelp, Instacart, Swiggy, Zomato, Spoonacular (by the API creator), and Edamam all have official MCP servers, making food one of the most commercially embraced MCP verticals. The June 2026 headline: Swiggy Builders Club is now open with invite-led access — 3 MCP servers and 18+ API tools across Food, Instamart, and Dineout, the first food delivery platform to create a formal developer ecosystem around MCP. The standout for recipes is worryzyy/HowToCook-mcp (724 stars, up from 569 in March), built on the wildly popular programmer's guide to home cooking with smart meal planning. For nutrition data, deadletterq/mcp-opennutrition (187 stars, up 53% from March's 122) runs fully locally with 300,000+ food items. Biggest grocery mover: CupOfOwls/kroger-mcp exploded from 4 to 61 stars (+1,425%) since April. Food delivery added iFood (Brazil's largest platform, OAuth 2.1 login, stdio + HTTP). Remaining gaps: no official DoorDash or GrubHub servers; no dietary condition management; no food safety databases; no wine databases. The category earns 4.0/5 — strong official vendor adoption, mature grocery coverage, and Swiggy's Builders Club pointing toward a developer-ecosystem future for food commerce MCP."
last_refreshed: 2026-06-12
category_url: "/categories/lifestyle-personal/"
---

Food and restaurant MCP servers are enabling AI agents to find recipes, order food delivery, make restaurant reservations, track calories, manage grocery lists, and mix cocktails — all through natural language. Instead of switching between Yelp, DoorDash, MyFitnessPal, and a recipe app, an AI agent can handle the entire food lifecycle: "Find me a chicken tikka masala recipe, check if I have the ingredients, order what's missing from Instacart, and book a table at an Indian restaurant for Saturday in case I don't feel like cooking."

The landscape spans ten areas: **recipes & cooking** (HowToCook, Spoonacular, CookWith, TheMealDB), **recipe managers** (Tandoor with 3 implementations, Mealie), **nutrition & food databases** (OpenNutrition, USDA FoodData Central, Edamam, Nutritionix), **food tracking & calories** (OpenFoodFacts, calorie trackers, meal loggers), **restaurants & reservations** (Yelp, Resy, OpenTable, SevenRooms), **restaurant operations** (Toast POS), **food delivery** (Uber Eats, DoorDash, Swiggy, Zomato), **grocery** (Instacart, Kroger, Picnic, H-E-B, Whole Foods), **meal kits** (HelloFresh), **beverages** (Bar Assistant cocktails, BrewSource beer, Untappd), and **multi-source food data** (barcode scanning, product databases).

The headline findings: **Swiggy Builders Club is now open** (June 2026) — invite-led access to 3 MCP servers and 18+ API tools, the first food delivery platform to create a formal MCP developer ecosystem with real external access. **Official vendor adoption remains exceptionally strong** — Yelp, Instacart, Swiggy, Zomato (168 stars), Spoonacular, and Edamam all have official MCP servers. **HowToCook-mcp grew to 724 stars** (up 27% from 569 in March) with smart meal planning. **OpenNutrition climbed to 187 stars** (up 53% from 122 in March) running fully locally with 300,000+ foods. **Kroger-mcp is the biggest mover** — surging from 4 to 61 stars (+1,425%) in 47 days. **iFood arrives** — Brazil's largest food delivery platform joins the ecosystem with OAuth 2.1 authentication. **Picnic grew to 72 stars** (up 41% from 51) as the most popular grocery MCP. **Toast POS fills the restaurant operations gap** with 50+ tools. **HelloFresh fills the meal kit gap.** **Beer MCP space added two servers but both stalled** — BrewSource has 0 stars and no updates since Nov 2025; Untappd is API-locked.

## Recipes & Cooking

### HowToCook MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [worryzyy/HowToCook-mcp](https://github.com/worryzyy/HowToCook-mcp) | 724 | TypeScript | MIT | 4 |

The **most popular food MCP server** — built on the viral Anduin2017/HowToCook project ("a programmer's guide to home cooking"), which has 70,000+ stars on GitHub. Four tools: query all recipes, query by category, get specific recipe (exact + fuzzy matching), and smart meal planning that generates weekly plans based on dietary restrictions, allergies, and number of diners. Available via npm (`howtocook-mcp`) and now also as a DXT (Desktop Extension) for one-click Claude Desktop installation. Chinese-origin with English README.

The meal planning tool is the differentiator — it doesn't just search recipes but creates coherent weekly meal plans accounting for nutritional balance and dietary constraints. 724 stars (up 27% from 569 in March) makes it the highest-starred food-related MCP server.

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

## Self-Hosted Recipe Managers

### Tandoor Recipe Manager

Three separate MCP implementations for Tandoor Recipes, the popular self-hosted recipe manager:

| Server | Language | Notes |
|--------|----------|-------|
| [starbuck93/tandoor-mcp-server](https://github.com/starbuck93/tandoor-mcp-server) | TypeScript | Most comprehensive — recipes, meal plans, shopping lists CRUD, keyword/food/unit search |
| [ChristopherJMiller/tandoor-mcp](https://github.com/ChristopherJMiller/tandoor-mcp) | Rust | Rare Rust MCP — recipes, shopping, meal planning, inventory tracking |
| [mc-mario/tandoor-mcp](https://github.com/mc-mario/tandoor-mcp) | Python | Auto-creates missing ingredients/units/keywords — smart entity resolution |

Three implementations in three different languages (TypeScript, Rust, Python) for the same platform. mc-mario's Python version differentiates by auto-creating missing entities (ingredients, units, keywords) when adding recipes — a small but practical feature that avoids manual setup. Note: Tandoor limits API auth to 10 requests/day, which constrains all implementations.

### Mealie MCP (New)

| Server | Language | License | Tools |
|--------|----------|---------|-------|
| [eds3028/mealie-mcp](https://github.com/eds3028/mealie-mcp) | Python | MIT | 7 |

A new MCP server for **Mealie**, another popular self-hosted recipe manager. Seven tools: recipe search with tag filtering, full recipe details, view/create meal plans, manage shopping lists, and create blank recipes. Supports both stdio (local) and SSE (remote) transport modes, with Docker support for integration into existing Mealie stacks. Requires Python 3.11+ and a running Mealie instance with API token. A welcome addition to the self-hosted recipe management space alongside Tandoor.

## Nutrition & Food Databases

### OpenNutrition MCP

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [deadletterq/mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition) | 187 | TypeScript | 3 |

The **best nutrition MCP server** — 300,000+ food items running **fully locally** with no external API calls. Three tools: food search, nutritional data lookup, and barcode scanning. Comprehensive nutritional profiles including macros, vitamins, and minerals. 187 stars (up 53% from 122 in March) — second-highest in the food MCP category. The fully-local approach means no API keys, no rate limits, no privacy concerns with dietary data, and offline capability. Data combines authoritative public sources (USDA, CNF, FRIDA, AUSNUT) for transparent, consistent nutritional data.

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

## Restaurant Operations (New)

### Toast POS MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [BusyBee3333/toast-mcp-2026-complete](https://github.com/BusyBee3333/toast-mcp-2026-complete) | 5 | TypeScript | MIT | 50+ |

The **first restaurant POS MCP server** — a community-built integration with Toast, the leading restaurant management platform. 50+ tools across 10 categories: order lifecycle management (12 tools), menu and inventory operations (11 tools), payment and cash management (8 tools), sales reporting and analytics (6 tools), staff and labor analytics (6 tools), and customer relationship management (4 tools). Implements OAuth 2.0 authentication with the Toast API and provides both stdio mode (MCP integration) and HTTP mode (web UI).

This fills a significant gap from the original review — restaurant operations and POS integration. While community-built rather than official, the breadth of 50+ tools covering the full restaurant operations lifecycle (orders, menus, payments, staff, analytics, CRM) makes it a serious entry. No Square POS MCP server has appeared yet.

## Food Delivery

### Uber Eats MCP

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [ericzakariasson/uber-eats-mcp-server](https://github.com/ericzakariasson/uber-eats-mcp-server) | 229 | Python | — |

The **most popular food delivery MCP server** at 229 stars (up from 221 in April). A proof-of-concept using browser automation for restaurant search, menu exploration, and food ordering. While not production-grade, it demonstrates the potential for AI-driven food ordering workflows.

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
| [Zomato MCP](https://github.com/Zomato/mcp-server-manifest) | **Official** — food ordering, order tracking, QR code payment. Production endpoint at mcp-server.zomato.com. Integrates with ChatGPT and Claude. 168 stars (active as of June 2026). |
| [arioliv/ifood-mcp](https://github.com/arioliv/ifood-mcp) | **iFood** — Brazil's largest food delivery platform. Browse, search, cart, and ordering. OAuth 2.1 with real iFood OTP login. stdio + HTTP transports. New June 2026. |
| [GrubHub Scraper MCP](https://apify.com/natanielsantos/grubhub-scraper) | Apify-based scraper, not official |

Swiggy and Zomato — India's two largest food delivery platforms — both have official MCP servers, making India the most MCP-advanced food delivery market. Swiggy's Instamart integration is particularly notable as the **first quick-commerce (instant grocery delivery) MCP** globally, covering 40,000+ SKUs via natural language. Zomato's QR code payment feature shows how MCP can bridge digital ordering with physical restaurant experiences.

**June 2026: Swiggy Builders Club now open** — Swiggy's [Builders Club](https://mcp.swiggy.com/builders/) is now accepting developers under an invite-led model. Built on AWS (Amazon Bedrock and AgentCore), approved builders receive API keys giving access to **3 MCP servers and 18+ API tools** spanning Food, Instamart, and Dineout. Localhost development is allowed without production approval, lowering the barrier to entry. Builders can create AI agents, copilots, and integrations that take real-world actions — ordering food, shopping groceries, booking dining. Includes a "Skills framework" of reusable capabilities for agentic commerce. This makes Swiggy the **first food delivery platform to create a formal developer ecosystem around MCP**, now with live invite-led API access and direct engineering support.

**iFood arrives (June 2026)** — Brazil's largest food delivery platform joins the MCP ecosystem with `arioliv/ifood-mcp`, a community-built server covering browse, search, cart, and ordering. Notably implements **OAuth 2.1 with real iFood OTP login** — one of the most production-grade authentication flows in the community food delivery MCP space. Supports both stdio and HTTP transports. While unofficial, Brazil being represented (alongside India's Swiggy/Zomato) shows MCP food delivery expanding beyond the US and UK markets.

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

### Picnic Supermarket MCP (New)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [ivo-toby/mcp-picnic](https://github.com/ivo-toby/mcp-picnic) | 72 | TypeScript | 30+ |

An impressive MCP server for **Picnic**, the European online supermarket delivery service (Netherlands, Germany, France). 30+ tools covering product search, cart management, order placement, meal planning with automatic shopping list generation, delivery tracking and optimization, budget management with spending analysis, and transaction history. Supports session persistence with 2FA, works with Claude Desktop and other MCP clients. Available via npm (`mcp-picnic`). 72 stars (up 41% from 51 in April) makes it the most popular grocery-specific MCP server.

An alternative exists at [YussufSassi/picnic-mcp](https://github.com/YussufSassi/picnic-mcp).

### H-E-B Grocery MCP (New)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mgwalkerjr95/texas-grocery-mcp](https://github.com/mgwalkerjr95/texas-grocery-mcp) | 28 | Python | MIT | 20+ |

A comprehensive MCP server for **H-E-B**, the beloved Texas grocery chain. 20+ tools across five categories: store location (3 tools), product search with real-time pricing (3 tools), cart management with confirmation requirements (5 tools), **digital coupon discovery and clipping** (4 tools), and session management (4 tools). The coupon clipping feature is unique — no other grocery MCP server offers automated deal discovery. Uses unofficial web APIs and browser automation. Note: unofficial integration. 28 stars (up 40% from 20 in April).

### Whole Foods MCP (New)

| Server | Language | Tools |
|--------|----------|-------|
| [benjiebob/whole-foods-mcp](https://github.com/benjiebob/whole-foods-mcp) | Python | 8 |

The **first Whole Foods MCP server** — enables automated grocery ordering from Amazon Whole Foods via browser automation. Eight tools: login, session saving, product search, product details, add to cart, view cart, remove from cart, and clear cart. Supports weight-based items (produce). Requires Python 3.11+ and an Amazon account with Whole Foods delivery enabled. Fills a significant gap from the original review.

### Dutch Supermarket Price Comparison (New)

| Server | Stars | Language | License |
|--------|-------|----------|---------|
| [Samvox1/nl-supermarkt-mcp](https://github.com/Samvox1/nl-supermarkt-mcp) | 11 | Python | MIT |

Searches and compares prices across **12+ Dutch supermarket chains** (Albert Heijn, Jumbo, Lidl, Aldi, Plus, DekaMarkt, Dirk, and more) plus 7 drugstore chains (Kruidvat, Etos, etc.). Features include shopping list optimization to find the cheapest combinations, weekly promotion tracking, price history alerts, budget management, and weekly menu planning with automatic grocery generation. A creative multi-vendor approach.

### Other Grocery Servers

| Server | Stars | Language | License | Notes |
|--------|-------|----------|---------|-------|
| [CupOfOwls/kroger-mcp](https://github.com/CupOfOwls/kroger-mcp) | 61 | Python | MIT | Product search, store finder, cart management, **shopping path optimization** |
| [jessalva7/grocery-mcp-server](https://github.com/jessalva7/grocery-mcp-server) | — | Python | — | General grocery item and shopping list management |
| [o-b-one/groceries-mcp](https://github.com/o-b-one/groceries-mcp) | 3 | Python | MIT | Multi-vendor grocery API (Rami Levy, Keshet), cart automation |

CupOfOwls/kroger-mcp is the **biggest mover in the grocery category** — jumping from 4 to 61 stars (+1,425%) since April, suggesting Kroger shoppers are actively discovering and adopting this server. Its unique **shopping path optimization tool** — which finds the optimal route through a Kroger store based on your shopping list — may be driving word-of-mouth. Also notable: Walmart partially enters the space with a community server (`DomingosNgongo/walmart-mcp`) for product search, though no official Walmart MCP server exists yet. Separately, LinkedIn reports Walmart is using Anthropic's MCP internally for "super agents" — external API access may follow.

## Meal Kits (New)

### HelloFresh MCP

| Server | Notes |
|--------|-------|
| [striderlabs/mcp-hellofresh](https://lobehub.com/mcp/striderlabs-mcp-hellofresh) | Weekly menu browsing, recipe details (ingredients, instructions, nutrition, allergens), delivery schedule management, subscription plan updates, dietary preference editing |

The **first meal kit MCP server** — enables AI agents to manage HelloFresh accounts end-to-end. Browse current and future weekly menus, access detailed recipe information including allergens and nutrition, view and modify delivery schedules, and update subscription plans and dietary preferences. Install via `claude mcp add hellofresh -- npx -y @striderlabs/mcp-hellofresh`. Requires HelloFresh account credentials.

An alternative by markswendsen-code uses Playwright browser automation for the same functionality. This fills a gap called out in the original review — no Blue Apron or Factor MCP servers yet, but HelloFresh as the market leader is the most impactful entry.

## Beverages

### Bar Assistant MCP

| Server | Language | Tools |
|--------|----------|-------|
| [zhdenny/bar-assistant-mcp-server](https://github.com/zhdenny/bar-assistant-mcp-server) | Python | 7+ |

Smart cocktail search with natural language + similarity matching, complete recipe retrieval, ingredient analysis, batch recipe retrieval, inventory-based recommendations, and advanced filtering by ABV, glassware, and preparation method. The similarity engine is clever — search for "something like a Negroni but less bitter" and it finds cocktails with similar profiles. 70%+ cache hit rate for performance. Integrates with Bar Assistant instances.

### BrewSource Beer MCP

| Server | Language | Tools | Status |
|--------|----------|-------|--------|
| [CharlRitter/brewsource-mcp](https://github.com/CharlRitter/brewsource-mcp) | Go | 3 | **Stalled** (last update Nov 2025) |

Designed as the **first beer-focused MCP server** — three tools covering Beer Judge Certification Program style lookups (`bjcp_lookup`), commercial beer search by name/style/brewery/location (`search_beers`), and brewery discovery with geographic filtering (`find_breweries`). Also exposes 5 MCP resources including complete BJCP style guidelines (beer, mead, cider) and a brewery directory. **Caution:** As of June 2026, this repo has 0 stars and no commits since November 2025, suggesting the project stalled in early development. Phase 1 MVP was announced but appears incomplete.

### Untappd MCP

| Server | Language | License | Tools | Status |
|--------|----------|---------|-------|--------|
| [jtucker/mcp-untappd-server](https://github.com/jtucker/mcp-untappd-server) | JavaScript | GPL-3.0 | 3 | **Limited** (API key closure) |

MCP server for the **Untappd** beer social network — three tools: beer search, detailed beer info, and user checkins. **Important caveat:** Untappd is no longer accepting registrations for new API keys, limiting this to developers with existing access. The `get_user_checkins` tool is noted as non-functional. No updates since December 2025, 0 stars — practically inaccessible to new users.

The beverage space has room to grow — wine remains entirely absent, and both beer-specific servers have significant limitations (one stalled, one API-locked).

## What's Missing

Despite 70+ servers (up from 55+), several gaps have been filled since March while others remain:

**Gaps filled since the April 2026 review:**
- Swiggy Builders Club: moved from announced → **open with invite-led access** (external developers can now build)
- iFood MCP: **Brazil's largest food delivery platform** now represented (community-built, OAuth 2.1)
- Walmart partially enters via **community MCP server** for product search (unofficial)

**Gaps filled since the March 2026 original:**
- ~~No restaurant POS/operations~~ → Toast POS MCP now has 50+ tools (community-built)
- ~~No Whole Foods~~ → benjiebob/whole-foods-mcp provides browser-automated ordering
- ~~No meal kit services~~ → HelloFresh MCP for account management and menu browsing
- ~~No beer databases~~ → BrewSource MCP (BJCP styles, brewery/beer search) and Untappd MCP (both stalled/limited by June 2026)

**Remaining gaps:**
- **No official DoorDash or GrubHub MCP servers** — DoorDash has a developer API but no official MCP server; GrubHub only has third-party scrapers
- **No official Walmart, Amazon Fresh, or Target MCP** — community Walmart server exists; Walmart uses MCP internally but no external API yet
- **No dietary condition management** — no celiac disease, diabetes, IBS, or allergy-aware meal planning with medical-grade data
- **No Square, Clover, or Lightspeed POS** — Toast is covered but the broader restaurant POS market is not
- **No food safety or allergen databases** — no FDA food recalls, no comprehensive allergen cross-reference databases
- **No food photography or plating** — no food styling, plating suggestions, or photo enhancement tools
- **No wine databases** — no Vivino, CellarTracker, or wine-focused servers; beer coverage is also weak (both servers stalled or API-locked)
- **No food waste management** — no servers for tracking expiration dates, suggesting recipes for ingredients about to expire
- **No restaurant review aggregation beyond Yelp** — no Google Maps reviews, TripAdvisor, or The Infatuation
- **No farm-to-table or sourcing** — no farmers market directories, CSA boxes, or local food sourcing
- **No Blue Apron, Factor, or other meal kits** — HelloFresh leads but the broader meal kit market is uncovered

## The Bottom Line

Food & Restaurant MCP servers earn **4.0 out of 5**. The June 2026 headline is Swiggy Builders Club going live — moving from announcement to open invite-led access, letting external developers build on top of 3 MCP servers and 18+ API tools spanning Food, Instamart, and Dineout. This is the clearest sign that food commerce platforms see MCP as infrastructure, not novelty.

Official vendor participation remains the category's strength — Yelp, Instacart, Swiggy, Zomato (168 stars), Spoonacular, and Edamam all have official MCP servers. The recipe space is led by HowToCook-mcp (724 stars, up 27% from March) with Mealie adding self-hosted recipe management. OpenNutrition climbed to 187 stars (up 53% from March) as the best local-first nutrition database.

The biggest mover in this refresh is **kroger-mcp** — from 4 to 61 stars (+1,425%) in 47 days, suggesting real organic adoption among Kroger shoppers. Picnic grew 41% to 72 stars, and iFood brings Brazil's largest food delivery platform into the MCP ecosystem for the first time. **Walmart appears on the horizon**: a community server exists, and Walmart is reportedly using Anthropic's MCP internally for "super agents."

The weaknesses are the continued duplication in nutrition tracking, the absence of official DoorDash/GrubHub servers, and the remaining gaps in wine, dietary condition management, and food safety databases. The beer MCP space added two servers since March but both are stalled or access-limited by June 2026. The Western food delivery market still lags India's production-grade official implementations.

*This review was refreshed on 2026-06-12 using Claude Sonnet 4.6 (Anthropic).*
