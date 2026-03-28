# MCP Servers for Retail & Hospitality — Research Data
## Compiled 2026-03-29

---

## 1. POINT OF SALE (POS) MCP SERVERS

### Square MCP Server (Official)
- **GitHub**: https://github.com/square/square-mcp-server
- **Stars**: 95 | **Forks**: 20
- **Language**: TypeScript
- **Status**: Beta
- **Tools**: 3 core tools (get_service_info, get_type_info, make_api_request) providing access to 40+ Square API services
- **Key Features**: Payments, orders, customers, catalog management, bookings, loyalty programs, inventory. Remote MCP via OAuth at `https://mcp.squareup.com/sse`. Local deployment option with access tokens. Read-only mode available.
- **Official docs**: https://developer.squareup.com/docs/mcp
- **License**: Apache-2.0

### Lightspeed Retail POS MCP Servers
- **Zapier MCP**: https://zapier.com/mcp/lightspeed-retail-pos-x-series — connects Lightspeed X-Series actions with AI tools via MCP
- **viaSocket MCP**: https://viasocket.com/mcp/Lightspeed_Retail_POS
- **LobeHub (busybee3333)**: https://lobehub.com/mcp/busybee3333-lightspeed-mcp-2026-complete — "2026 Complete Version"
- **SyncHub Connector**: https://www.synchub.io/connectors/lightspeed/mcp — R-Series connector
- **Tools**: list_sales, get_sale, list_items, get_item, update_inventory, create/update customers, create register sales, product creation
- **Note**: Also has Lightspeed Restaurant POS (O-Series/Kounta) MCP connector via SyncHub

### Toast POS
- **Status**: No dedicated MCP server found for Toast POS restaurant system. Toast has an integration partner directory but no public MCP implementation yet.

### Clover POS
- **Status**: No dedicated MCP server found. Gap in the market.

---

## 2. E-COMMERCE MCP SERVERS

### Shopify (Official — Built-in)
- **Storefront MCP**: Built into every Shopify store at `/api/mcp` since Summer 2025 Edition — no setup required
- **Docs**: https://shopify.dev/docs/apps/build/storefront-mcp
- **Tools**: Product search, customer support/FAQ, cart management, checkout initiation
- **Also**: Customer Accounts MCP server (order tracking, returns, account management)
- **Also**: Shopify Dev MCP server (https://shopify.dev/docs/apps/build/devmcp) for development
- **MCP-UI**: Open-source extension allowing rich interactive UI components in MCP responses (published August 2025)
- **Significance**: Every Shopify store is MCP-enabled by default — massive ecosystem reach

### Shopify Community MCP Servers (GitHub)

#### GeLi2001/shopify-mcp (Most Popular Community)
- **GitHub**: https://github.com/GeLi2001/shopify-mcp
- **Stars**: 174 | **Forks**: 55
- **Language**: TypeScript
- **Tools**: 31 tools across products (8), customers (8), orders (10), draft orders (1), metafields (3), inventory (1), tags (1)
- **Key Features**: Full GraphQL Admin API integration, cursor-based pagination, sorting, advanced filtering

#### pashpashpash/shopify-mcp-server
- **GitHub**: https://github.com/pashpashpash/shopify-mcp-server
- **Stars**: 10
- **Tools**: Product management, customer management, order management via GraphQL Admin API

#### antoineschaller/shopify-mcp-server
- **GitHub**: https://github.com/antoineschaller/shopify-mcp-server
- **Tools**: 22 tools for products, orders, customers, inventory, analytics

#### QuentinCody/shopify-storefront-mcp-server
- **GitHub**: https://github.com/QuentinCody/shopify-storefront-mcp-server
- **Tools**: shopify_discover, shopify_storefront_graphql, customer_data

### WooCommerce MCP Servers

#### techspawn/woocommerce-mcp-server
- **GitHub**: https://github.com/techspawn/woocommerce-mcp-server
- **Stars**: 83 | **Forks**: 48
- **Language**: TypeScript
- **Tools**: Product CRUD, order lifecycle management, customer operations, shipping/taxes, discounts/coupons, payment gateways, reporting (sales, products, orders, categories, customers, stock, coupons, taxes), WordPress integration, store configuration
- **Key Features**: Full WooCommerce REST API integration, JSON-RPC 2.0, cross-platform

#### iOSDevSK/mcp-for-woocommerce (WordPress Plugin)
- **GitHub**: https://github.com/iOSDevSK/mcp-for-woocommerce
- **Type**: WordPress community plugin
- **Features**: STDIO and HTTP streamable transport, optional JWT auth, read-only tools with permalink fields, product search, category/attribute exploration, reviews, WordPress content
- **Based on**: Automattic's official WordPress MCP

#### WordPress/mcp-adapter (Official)
- **GitHub**: https://github.com/WordPress/mcp-adapter
- **Description**: Official MCP adapter bridging WordPress Abilities API to MCP
- **WooCommerce integration**: Exposes WooCommerce operations as MCP tools, respects WooCommerce permission system, uses REST API keys for auth

### Magento 2 MCP Servers

#### boldcommerce/magento2-mcp
- **GitHub**: https://github.com/boldcommerce/magento2-mcp
- **Stars**: 53 | **Forks**: 19
- **Language**: JavaScript
- **Tools**: Product queries (by SKU/ID), advanced search with filtering, categories, related items, stock data, product attributes, customer ordered products, order count tracking, revenue analysis by timeframe/country, product sales statistics, top performers
- **Key Features**: Supports relative dates ("today", "YTD"), analytics capabilities

#### elgentos/magento2-dev-mcp
- **GitHub**: https://github.com/elgentos/magento2-dev-mcp
- **Stars**: 36
- **Language**: TypeScript (npm: @elgentos/magento2-dev-mcp)
- **Tools**: config-show, db-query, DI preference inspection, module management, theme enumeration, module creation, system diagnostics
- **Key Features**: Development-focused, Docker auto-detection (Warden, DDEV, docker-magento)

### BigCommerce MCP Servers

#### isaacgounton/bigcommerce-api-mcp
- **GitHub**: https://github.com/isaacgounton/bigcommerce-api-mcp
- **Stars**: 3 | **Forks**: 1
- **Language**: JavaScript
- **Tools**: Products management, customer management, order management with customer-product relationship data
- **Key Features**: Built-in tool discovery, Docker support, multiple server modes (stdio, SSE, streamable HTTP)

#### CDataSoftware/bigcommerce-mcp-server-by-cdata
- **GitHub**: https://github.com/CDataSoftware/bigcommerce-mcp-server-by-cdata
- **Type**: Read-only MCP server via CData JDBC Drivers

### Saleor Commerce MCP Server (Official — Headless)
- **GitHub**: https://github.com/saleor/saleor-mcp
- **Stars**: 13 | **Forks**: 6
- **Language**: Python (94.7%)
- **Tools**: Read-only API integration for products, customers, orders
- **Key Features**: Streamable HTTP at `https://mcp.saleor.app/mcp`, domain validation, GraphQL-based
- **Note**: Saleor is a popular open-source headless e-commerce platform (used by Breitling, Lush)

### Salesforce B2C Commerce MCP Service (Official)
- **Docs**: https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/agentic-mcp-shopper-tools-quick-start.html
- **Status**: Pilot
- **Type**: Fully-hosted service
- **Tools**: Product catalog, customer management, shopping cart, order management, promotions, content management, search & navigation
- **Key Features**: Supports MCP /tools, HTTP SSE, Google A2A, SLAS token auth, guest and registered user support
- **Significance**: Major enterprise commerce platform with official MCP

### Google Universal Commerce Protocol (UCP)
- **URL**: https://ucp.dev/
- **Docs**: https://developers.google.com/merchant/ucp
- **Description**: Open-source standard for agentic commerce, works across discovery, buying, and post-purchase
- **MCP Integration**: Supports REST API and MCP binding, Agent Payments Protocol (AP2), Agent2Agent (A2A)
- **Partners**: Shopify, Etsy, Wayfair, Target, Walmart — 20+ global partners
- **Features**: Multi-item cart, real-time product details, identity linking for loyalty, agentic checkout
- **Status**: US merchants only as of March 2026, expanding globally
- **Significance**: Google-backed standard with massive retail partner buy-in

### Octogen AI — Retail MCP (rMCP)
- **URL**: https://medium.com/@octogenai/introducing-retail-mcp-ecc5dc859427
- **Description**: Proposed MCP standard specifically for e-commerce
- **Tools**: Catalog search, cart updates, checkout, order status, returns, CRM opt-ins, account management, loyalty
- **Key Features**: Standardized contract so any compliant agent can plug in without bespoke integration

---

## 3. INVENTORY & WAREHOUSE MANAGEMENT MCP SERVERS

### Picqer MCP Server
- **URL**: https://www.mcpbundles.com/providers/picqer
- **Description**: Cloud-based warehouse management for e-commerce
- **Tools**: Task management with filtering, packaging advice for picklists, order resumption, storage location management, warehouse inventory snapshots, order creation/updates, order processing (concept to processing), picklist management with PDF generation, manual closure
- **Key Features**: Optimized picking paths, stock organization, complete WMS functionality via conversation

### Pipe17 MCP Server
- **URL**: https://pipe17.com/ai/mcp/
- **Description**: First MCP server designed specifically for post-purchase order operations
- **Tools**: Orders (query by status, date, external ID), products (search/retrieve with variants), inventory (real-time across locations), fulfillments (status/details), shipments (progress/carriers), customers (records/history), locations (warehouse/fulfillment), exceptions (system exceptions)
- **Key Features**: Business intelligence (exceptions, events, automations, routing, jobs), setup in under 10 minutes, works with Gemini/CoPilot/Claude/ChatGPT/Perplexity
- **Company**: 163% order volume growth in 2025

### Microsoft Dynamics 365 ERP MCP Server
- **URL**: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp
- **Description**: Dynamic framework for Finance and Supply Chain Management
- **Initial Launch**: Build 2025 with 13 curated tools
- **Current**: Dynamic ERP MCP server (public preview) — adapts as business needs evolve
- **Capabilities**: Journal entries, transaction validation, KPI retrieval across Finance, Supply Chain, HR, and Project Operations
- **Use Cases**: Shop-floor agents, payment inquiry automation, inbound load creation, recall impact analysis, supplier performance insight, service chain coordination, production recovery planning
- **Significance**: Major enterprise ERP with official MCP support

---

## 4. CRM & CUSTOMER LOYALTY MCP SERVERS

### HubSpot MCP Servers

#### Official HubSpot MCP Server
- **URL**: https://developers.hubspot.com/mcp
- **Tools**: 100+ tools across contacts, companies, deals, and other data types

#### peakmojo/mcp-hubspot
- **GitHub**: https://github.com/peakmojo/mcp-hubspot
- **Stars**: 116
- **Key Features**: FAISS semantic search, vector storage, caching to overcome HubSpot API limitations

#### calypsoCodex/hubspot-mcp-extended
- **GitHub**: https://github.com/calypsoCodex/hubspot-mcp-extended
- **Tools**: 106 comprehensive tools for CRM automation including invoices and line items
- **License**: Source Available — Free for non-commercial use

### Salesforce MCP Server
- **GitHub**: https://github.com/tsmztech/mcp-server-salesforce
- **Stars**: 312
- **Tools**: 60+ tools
- **Key Features**: Dynamic toolset loading, SOQL queries, Apex test execution, metadata deployment
- **Significance**: Most-starred CRM MCP server

### Retail-Specific CRM/Loyalty via MCP
- Loyalty programs can be connected through MCP frameworks to inventory, order history, and loyalty databases
- Microsoft Dynamics 365 Customer Insights + Commerce MCP Server enables Retail Clienteling agents
- Google UCP supports identity linking for loyalty benefits across AI platforms
- Shopify's built-in MCP preserves loyalty hooks for automatic enrollment/credits

---

## 5. RESTAURANT & FOOD SERVICE MCP SERVERS

### Restaurant Reservation MCP Server
- **GitHub**: https://github.com/jrklein343-svg/restaurant-mcp
- **Stars**: 2
- **Language**: TypeScript
- **Tools**: 12 tools — search_restaurants, check_availability, make_reservation, list_reservations, cancel_reservation, set_credentials, set_login, check_auth_status, refresh_token, snipe_reservation, list_snipes, cancel_snipe
- **Key Features**: Unified Resy + OpenTable search, real-time availability, direct Resy booking, automated reservation "sniper" for high-demand slots, Windows Credential Manager with DPAPI encryption

### Restaurant Booking MCP Server (Google Maps)
- **GitHub**: https://github.com/samwang0723/mcp-booking
- **Description**: AI-powered restaurant discovery via Google Maps Places API
- **Key Features**: Location, cuisine, mood, and event-based search; intelligent recommendations

### Uber Eats MCP Server
- **GitHub**: https://github.com/ericzakariasson/uber-eats-mcp-server
- **Stars**: 216 | **Forks**: 38
- **Language**: Python
- **Key Features**: Playwright browser automation, restaurant search, menu exploration, food ordering
- **Type**: Proof-of-concept

### DoorDash MCP Server
- **GitHub**: https://github.com/JordanDalton/DoorDash-MCP-Server
- **Stars**: 22 | **Forks**: 7
- **Language**: TypeScript
- **Key Features**: Restaurant search, menu browsing, cart management, order placement, delivery tracking via DoorDash Drive API

### OpenTable MCP Servers
- **Apify**: https://apify.com/canadesk/opentable/api/mcp — data extraction for restaurant listings, availability, menus, reviews
- **Bright Data**: https://brightdata.com/ai/mcp-server/opentable — public data extraction at scale

### DoorDash Scraper MCP
- **Apify**: https://apify.com/sovereigntaylor/doordash-scraper/api/mcp — restaurants, menus, prices, fees

### Kitchen Display / Menu Management
- **Status**: No dedicated KDS MCP servers found. CloudKitchens has multi-channel menu management tech but no public MCP. Gap in the market.

---

## 6. HOTEL & PROPERTY MANAGEMENT MCP SERVERS

### Apaleo MCP Server (Official — First Hotel PMS with MCP)
- **URL**: https://apaleo.com/blog/apaleo-news/apaleo-launches-mcp-server
- **Description**: First property management platform to launch MCP server
- **Tools**: 29+ tools for scheduling & booking automation
- **Capabilities**: Check availability, modify bookings, update rates, amend loyalty records, notify housekeeping, trigger billing, cross-system operations
- **Scale**: 2,000+ properties in 30+ countries
- **Key Features**: API-first platform, every function accessible via API, Apaleo Store with hundreds of hospitality app integrations
- **Significance**: Industry first-mover in hotel MCP

### Agentic Hospitality — TravelOS MCP Server
- **URL**: https://www.agentichospitality.com
- **Description**: AI-native hotel distribution infrastructure
- **Products**: TravelOS MCP Server, Agentic Booking Engine, Schema Adapter, Channel Manager, AgentSite AI CMS
- **Capabilities**: Real-time availability/rates/inventory inside AI assistants, conversational booking, loyalty-aware rate personalization, policy transparency
- **Milestone**: Achieved industry's first MCP hotel booking (Rose St. Gardens, Dominica)
- **Proprietary**: MCP Intent Matrix (MIM), Signal-to-Action Ratio (SAR)
- **Significance**: First-ever hotel booking made via MCP

### Hotels MCP Server (Booking.com API)
- **GitHub**: https://github.com/esakrissa/hotels_mcp_server
- **Stars**: 15 | **Forks**: 5
- **Language**: Python
- **Tools**: 2 — search_destinations, get_hotels
- **Key Features**: Room configs, pricing with discounts, guest ratings, image galleries, arrival/departure times, star classifications
- **API**: Booking.com via RapidAPI

### Airbnb MCP Server
- **GitHub**: https://github.com/openbnb-org/mcp-server-airbnb
- **Stars**: 406 | **Forks**: 101
- **Language**: JavaScript
- **Tools**: 2 — airbnb_search, airbnb_listing_details
- **Key Features**: Location-based search, Google Maps Place ID integration, date/guest/price filtering, detailed property info including amenities and house rules, DXT format for Claude Desktop
- **Note**: No API key required; robots.txt compliant by default

### Mirai (Hotel Distribution Perspective)
- **URL**: https://www.mirai.com/blog/mcp-the-bridge-that-will-allow-hotels-to-compete-in-the-era-of-ai-assistants-and-llms/
- **Perspective**: MCP gives hotels a chance to reclaim direct guest relationships from OTAs in the AI era

---

## 7. PAYMENT PROCESSING MCP SERVERS

### Stripe MCP Server (Official)
- **GitHub**: https://github.com/stripe/ai (monorepo)
- **Stars**: 1,400 | **Forks**: 239
- **Package**: `@stripe/mcp` via npm
- **Remote**: https://mcp.stripe.com (OAuth)
- **Local**: `npx -y @stripe/mcp --api-key=YOUR_KEY`
- **Tools**: 25 tools across 13 categories — customers, products, invoices, subscriptions, refunds, payment links, documentation access
- **Key Features**: Part of Stripe's Agentic Commerce Suite (March 2026), OAuth remote access, RAK-controlled permissions
- **Also includes**: @stripe/agent-toolkit (OpenAI, LangChain, CrewAI, Vercel AI SDK integrations)
- **License**: MIT
- **Significance**: Most-starred payment MCP server, official enterprise support

### PayPal MCP Server (Official)
- **GitHub**: https://github.com/paypal/paypal-mcp-server
- **Stars**: 8 | **Forks**: 4
- **Language**: JavaScript/TypeScript
- **Run**: `npx -y @paypal/mcp --tools=all`
- **Tools**: Invoicing (create, list, send, reminders, QR codes), payments (orders, processing, refunds), disputes (list, retrieve, claim acceptance), shipment tracking, catalog management (products CRUD), subscriptions (plans, management, cancellation), reporting (transactions with filtering/pagination)
- **Key Features**: Comprehensive PayPal API coverage

### Adyen MCP Server (Official)
- **GitHub**: https://github.com/Adyen/adyen-mcp
- **Stars**: 20 | **Forks**: 13
- **Language**: TypeScript
- **Tools**: 6 categories — Checkout sessions (create, retrieve, payment methods), payment links (generate, status, expiry), modifications (cancel, refunds), merchant accounts (list), terminals (manage, reassign, apps, certificates, actions, settings), webhooks (list, retrieve)
- **Key Features**: TEST and LIVE environments, selective tool configuration
- **Version**: 0.4.0

### Paddle MCP Server
- **Glama listing**: 63 stars, 172 forks
- **Tools**: Products, prices, customers, transactions, subscriptions management via Paddle Billing API

### Community Stripe Implementations
- **atharvagupta2003/mcp-stripe**: https://github.com/atharvagupta2003/mcp-stripe — customer CRUD, payment intents, charges, refunds
- **jsyapps/stripe-mcp**: https://github.com/jsyapps/stripe-mcp — payment links, products, customers for Claude Desktop
- **wrsmith108/stripe-mcp-skill**: https://github.com/wrsmith108/stripe-mcp-skill — Claude Code skill for Stripe

### PortOne MCP Server
- **Stars**: 13 | **Forks**: 57
- **Features**: Payment documentation access, payment history lookup, sub-merchant queries

---

## 8. ANALYTICS & BI FOR RETAIL

### Google Analytics MCP Server (Official)
- **URL**: https://developers.google.com/analytics/devguides/MCP
- **Description**: Connects Analytics data to LLMs like Gemini
- **Significance**: Official Google product

### Google BigQuery + ADK for Retail Forecasting
- **URL**: https://cloud.google.com/blog/products/data-analytics/ai-based-forecasting-and-analytics-in-bigquery-via-mcp-and-adk
- **Key Features**: Revenue forecasting from sales data, Google Maps cross-referencing for location intelligence, delivery route validation — all via managed MCP servers

### Microsoft Dynamics 365 ERP MCP Server
- **Features**: KPI retrieval, analytics across Finance, Supply Chain, HR, and Project Operations
- **See Section 3 for full details**

### Retail-Specific Analytics Gaps
- No dedicated retail foot traffic MCP server found
- No dedicated demand forecasting MCP server found
- These capabilities are typically embedded within larger platforms (Google, Microsoft) rather than standalone servers

---

## 9. MARKET DATA & STATISTICS

### Retail AI Market Size
- **2025**: USD 12.40 billion (Fortune Business Insights) / USD 14.03 billion (Precedence Research) / USD 31.12 billion in 2024 (MarketsandMarkets)
- **2026 Projection**: USD 16.54 billion (Fortune Business Insights)
- **2034 Projection**: USD 105.88 billion at 26.10% CAGR (Fortune) / USD 62.64 billion at 18.14% CAGR (Precedence)
- **2030 Projection**: USD 164.74 billion at 32.0% CAGR (MarketsandMarkets)
- **North America share**: 36.90% in 2025

### Hospitality AI Market Size
- **2023**: USD 16.33 billion (Kings Research)
- **2031 Projection**: USD 70.32 billion at 20.36% CAGR
- **2026-2035 Testing Market**: 16.6% CAGR

### AI Adoption in Retail
- 89% of retailers actively using or assessing AI projects
- 80% of online retailers have integrated AI
- 78% of organizations use AI in at least one business function (up from 55% in 2023)
- Pure-play e-commerce: 74% adoption
- Omnichannel retailers with physical stores: 41% adoption
- Grocery and discount retailers: 28% adoption
- Only 7% have fully scaled AI deployments; 62% stuck in piloting phases
- 92% of retail marketers using AI as of 2025

### MCP Ecosystem Scale
- 97+ million monthly SDK downloads
- 10,000+ public MCP servers
- Native support from OpenAI, Google, Microsoft, Shopify
- Originally developed by Anthropic (late 2024)

### Global AI-enabled E-commerce Market
- **2025**: USD 8.65 billion
- **2032 Projection**: USD 22.60 billion at 14.60% CAGR

---

## 10. NOTABLE PLATFORMS & OFFICIAL MCP INTEGRATIONS

### Tier 1 — Major Platforms with Official MCP Support
| Platform | Type | MCP Status |
|----------|------|-----------|
| **Shopify** | E-commerce | Built-in on every store (`/api/mcp`), Storefront MCP, Dev MCP, Customer Accounts MCP |
| **Square** | POS/Payments | Official MCP server (Beta), remote OAuth at mcp.squareup.com |
| **Stripe** | Payments | Official MCP (1.4K stars), remote at mcp.stripe.com, part of Agentic Commerce Suite |
| **Salesforce** | CRM/Commerce | B2C Commerce MCP Service (Pilot), Salesforce CRM MCP (312 stars) |
| **PayPal** | Payments | Official MCP server via npm |
| **Adyen** | Payments | Official MCP server (20 stars) |
| **Google** | Commerce Protocol | Universal Commerce Protocol (UCP) with MCP binding |
| **Microsoft** | ERP | Dynamics 365 ERP MCP Server (13+ tools, dynamic framework) |
| **Apaleo** | Hotel PMS | First hotel PMS with MCP server |
| **HubSpot** | CRM | Official MCP server (100+ tools) |
| **WordPress/WooCommerce** | E-commerce/CMS | Official MCP adapter via WordPress Abilities API |
| **Saleor** | Headless Commerce | Official MCP server |

### Tier 2 — Emerging/Specialized
| Platform | Type | MCP Status |
|----------|------|-----------|
| **Agentic Hospitality** | Hotel Distribution | TravelOS MCP Server, first MCP hotel booking achieved |
| **Pipe17** | Order Management | First post-purchase order operations MCP |
| **Picqer** | Warehouse Management | MCP server for warehouse operations |
| **Lightspeed** | POS | Multiple third-party MCP integrations (Zapier, SyncHub, viaSocket) |
| **Octogen AI** | Retail Infrastructure | Retail MCP (rMCP) standard proposal |

### Tier 3 — Community/Third-Party
| Platform | Type | MCP Status |
|----------|------|-----------|
| **Magento 2** | E-commerce | Community MCP servers (53 stars, 36 stars) |
| **BigCommerce** | E-commerce | Community MCP server (3 stars) |
| **Airbnb** | Vacation Rental | Community search MCP (406 stars) |
| **Uber Eats** | Food Delivery | Community POC MCP (216 stars) |
| **DoorDash** | Food Delivery | Community MCP (22 stars) |
| **OpenTable/Resy** | Reservations | Community MCP servers |
| **Booking.com** | Hotel Search | Community MCP via RapidAPI (15 stars) |

---

## GAPS & OPPORTUNITIES

Key areas with no or minimal MCP server coverage:
1. **Toast POS** — Major restaurant POS with no MCP server
2. **Clover POS** — Popular POS with no MCP server
3. **Kitchen Display Systems** — No dedicated MCP servers
4. **Dedicated Retail Analytics/Foot Traffic** — No standalone MCP servers
5. **Demand Forecasting** — Embedded in platforms but no standalone MCP
6. **Hotel Channel Managers** — Traditional tools, no standalone MCP
7. **Restaurant Management Suites** — No comprehensive restaurant operations MCP
8. **Grocery/Food Retail** — Underserved despite large market

---

## SOURCES

### POS Systems
- https://github.com/square/square-mcp-server
- https://developer.squareup.com/docs/mcp
- https://zapier.com/mcp/lightspeed-retail-pos-x-series
- https://viasocket.com/mcp/Lightspeed_Retail_POS

### E-commerce
- https://shopify.dev/docs/apps/build/storefront-mcp
- https://shopify.dev/docs/apps/build/devmcp
- https://shopify.engineering/mcp-ui-breaking-the-text-wall
- https://github.com/GeLi2001/shopify-mcp
- https://github.com/techspawn/woocommerce-mcp-server
- https://github.com/iOSDevSK/mcp-for-woocommerce
- https://github.com/WordPress/mcp-adapter
- https://github.com/boldcommerce/magento2-mcp
- https://github.com/elgentos/magento2-dev-mcp
- https://github.com/isaacgounton/bigcommerce-api-mcp
- https://github.com/saleor/saleor-mcp
- https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/agentic-mcp-shopper-tools-quick-start.html
- https://ucp.dev/
- https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/
- https://medium.com/@octogenai/introducing-retail-mcp-ecc5dc859427
- https://glama.ai/mcp/servers/categories/ecommerce-and-retail

### Inventory & Warehouse
- https://www.mcpbundles.com/providers/picqer
- https://pipe17.com/ai/mcp/
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp

### CRM & Loyalty
- https://developers.hubspot.com/mcp
- https://github.com/peakmojo/mcp-hubspot
- https://github.com/calypsoCodex/hubspot-mcp-extended
- https://github.com/tsmztech/mcp-server-salesforce
- https://www.merge.dev/blog/crm-mcp-server

### Restaurant & Food Service
- https://github.com/jrklein343-svg/restaurant-mcp
- https://github.com/samwang0723/mcp-booking
- https://github.com/ericzakariasson/uber-eats-mcp-server
- https://github.com/JordanDalton/DoorDash-MCP-Server
- https://apify.com/canadesk/opentable/api/mcp

### Hotel & Property Management
- https://apaleo.com/blog/apaleo-news/apaleo-launches-mcp-server
- https://www.agentichospitality.com
- https://www.hospitalityupgrade.com/news/agentic-hospitality-announces-industrys-first-hotel-mcp-booking-a-daniel-vs-goliath-story
- https://github.com/esakrissa/hotels_mcp_server
- https://github.com/openbnb-org/mcp-server-airbnb
- https://www.mirai.com/blog/mcp-the-bridge-that-will-allow-hotels-to-compete-in-the-era-of-ai-assistants-and-llms/

### Payments
- https://github.com/stripe/ai
- https://docs.stripe.com/mcp
- https://github.com/paypal/paypal-mcp-server
- https://github.com/Adyen/adyen-mcp
- https://docs.adyen.com/development-resources/mcp-server

### Analytics
- https://developers.google.com/analytics/devguides/MCP
- https://cloud.google.com/blog/products/data-analytics/ai-based-forecasting-and-analytics-in-bigquery-via-mcp-and-adk

### Market Data
- https://www.fortunebusinessinsights.com/artificial-intelligence-ai-in-retail-market-101968
- https://www.precedenceresearch.com/artificial-intelligence-in-retail-market
- https://www.marketsandmarkets.com/Market-Reports/artificial-intelligence-ai-retail-market-36255973.html
- https://www.kingsresearch.com/ai-in-hospitality-market-671
- https://www.thebusinessresearchcompany.com/report/artificial-intelligence-ai-in-hospitality-global-market-report
- https://www.envive.ai/post/generative-ai-commerce-adoption-statistics

### Industry Analysis
- https://www.arcade.dev/blog/enterprise-mcp-guide-for-retail-ecommerce
- https://www.bluecore.com/blog/what-is-mcp-server-ai-retail/
- https://www.hitec.org/news/4131275/your-hotels-new-front-door-what-the-new-mcp-means-for-hospitality
- https://www.cybage.com/blog/mcp-servers-in-hospitality-scaling-ai-agents-across-multi-property-hotel-systems
