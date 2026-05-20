# E-Commerce & Shopping MCP Servers — Shopify, Stripe, WooCommerce, Amazon, and More

> E-commerce and shopping MCP servers are turning AI agents into store operators, shopping assistants, and payment processors — letting them manage products, process orders, handle


E-commerce and shopping MCP servers are turning AI agents into store operators, shopping assistants, and payment processors. Instead of navigating web interfaces or building custom integrations, these servers let agents manage product catalogs, process orders, handle payments, track customers, and guide shoppers through checkout — all through the Model Context Protocol.

The landscape spans eight areas: **platform-native commerce** (Shopify's 4 MCP servers including MCP UI; BigCommerce now official), **payment processing** (Stripe's comprehensive toolkit, Square's official server), **Shopify Admin servers** (community-built store management), **open-source platforms** (WooCommerce in public beta, Medusa, Saleor, commercetools), **marketplace integrations** (Amazon, eBay, Etsy), **dropshipping & fulfillment** (Zendrop, Easyship), **advertising** (Meta Ads AI Connectors), and **commerce protocols** (12+ competing standards from Google, Stripe, Amazon, Visa, Mastercard, Klarna, and FIDO Alliance).

The May 2026 headline findings: **BigCommerce launched an official Storefront MCP (May 11)** — the last major platform gap in this category is now closed. **Shopify's Storefront Catalog MCP is migrating to UCP** (May 30 effective deadline, June 15 fully mandatory), and Agentic Storefronts moved to a dedicated admin home as a peer sales channel. **Stripe Sessions 2026** (April 29-30) announced 288 features including a Link agent wallet for AI-initiated payments. **Google announced the Universal Cart at Google I/O** (May 2026) — cross-merchant shopping across Search, Gemini, YouTube, and Gmail, now targeting summer rollout. **Easyship launched the first cross-border shipping MCP** (April 30) with 550+ couriers and 200+ countries. **FIDO Alliance formed Agentic Authentication and Payments Working Groups** (April 28), receiving AP2 v0.2 from Google and Verifiable Intent from Mastercard. **Adobe Commerce made MCP its default agent protocol.** Security alert: **eBay CVE-2026-27203 (environment variable injection) remains unpatched.** Consumer-side shopping intelligence is still absent.

## Platform-Native Commerce

### Shopify Storefront MCP (Official — Every Store)

| Server | Type | Auth | Transport |
|--------|------|------|-----------|
| Shopify Storefront MCP | Platform-native | None required | Streamable HTTP |

**Shopify Storefront MCP** is a landmark in agentic commerce — every Shopify store now exposes an MCP endpoint at `https://{shop}.myshopify.com/api/mcp` with zero setup and no authentication required. AI agents can interact with any Shopify store's catalog, cart, and policies out of the box.

Four tools are available:

- **search_shop_catalog** — natural-language product search returning product names, prices, variant IDs, URLs, images, and descriptions
- **update_cart** — add items, modify quantities, remove items (quantity 0), or create new carts
- **get_cart** — retrieve cart contents including item details and checkout URL
- **search_shop_policies_and_faqs** — answer store policy and FAQ questions with optional product context

This is the first time a major commerce platform has made its entire merchant network accessible to AI agents by default. Shopify has also rolled out **Customer Accounts MCP** (order tracking, account management) and **Checkout MCP** (full purchase flow including checkout session creation and order completion) as additional server types for deeper agentic integration.

The significance cannot be overstated — millions of Shopify stores are now AI-agent-accessible without any merchant action required.

**April 2026 update:** Shopify activated **Agentic Storefronts for all eligible US merchants on March 24, 2026**. Stores are now live on ChatGPT, Perplexity, and Microsoft Copilot — products surface when shoppers ask AI assistants for recommendations. Hydrogen 2026.1.4 added an automatic `/api/mcp` proxy that forwards requests to Shopify's Storefront MCP server with zero custom code required (enabled by default when `proxyStandardRoutes` is on).

Shopify also shipped **MCP UI** — interactive components that let the MCP server embed rich product cards with variant selectors, image galleries, subscription options, and add-to-cart flows inside AI chat interfaces via sandboxed iframes. This solves the fundamental limitation of text-only commerce conversations.

**May 2026 update:** Two significant developments. First, **Shopify's Storefront Catalog MCP is migrating to UCP** — UCP-aligned tools went live April 22 alongside existing tools; May 30 is the effective date for updated endpoints; June 15 is the mandatory cutover. Price ranges, availability, options/variants, and ratings structures are all being standardized to the UCP schema. Merchants and developers using the Storefront MCP need to update integrations before the June 15 deadline.

Second, **Agentic Storefronts received a dedicated home in the Shopify admin (May 11)**. AI shopping channels — ChatGPT, Microsoft Copilot, Google AI Mode, and Gemini — are now treated as first-class sales channels alongside Online Store, B2B, and POS. Merchants can track sales attributed to AI channels and see which queries their products rank for. Shopify also introduced Web Bot Auth signatures (May 7) for agent traffic with stricter rate limits on Storefront API and store pages.

PulseMCP: ~196K all-time visitors, ~8.8K weekly, #210 globally (#170 weekly).

### Shopify Customer Account MCP (Official — Authenticated Customer Actions)

| Server | Type | Auth | Transport |
|--------|------|------|-----------|
| Shopify Customer Account MCP | Platform-native | OAuth 2.0 + PKCE | Streamable HTTP |

**Shopify Customer Account MCP** provides tools for authenticated customer-specific actions — checking order status, retrieving order details, and managing account preferences. Requires OAuth 2.0 access token via authorization code grant with PKCE. Integration takes roughly 1–2 weeks due to the auth flow complexity.

### Shopify Checkout MCP (Official — Preview)

| Server | Type | Auth | Transport |
|--------|------|------|-----------|
| Shopify Checkout MCP | Platform-native | UCP Agent Profile | Streamable HTTP |

**Shopify Checkout MCP** is currently in preview (not generally available). Five tools: `create_checkout`, `get_checkout`, `update_checkout`, `complete_checkout`, and `cancel_checkout`. Each request requires a `ucp-agent.profile` metadata URI pointing to your agent's UCP profile. When it ships broadly, this completes the agentic commerce loop — an AI agent can take a customer from product discovery through checkout without any human-operated UI.

### Shopify Dev MCP (Official — Developer Documentation)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [Shopify Dev MCP](https://shopify.dev/docs/apps/build/devmcp) | ~490 | TypeScript | 4+ |

**Shopify Dev MCP** (`@shopify/dev-mcp` on npm) enables AI assistants to search Shopify documentation, explore API schemas, and generate valid code for Shopify APIs. Run via `npx -y @shopify/dev-mcp@latest`. Also available via [Gemini CLI integration](https://github.com/Shopify/dev-mcp-gemini-cli).

Key tools:

- **search_dev_docs** / **search_docs_chunks** — search across all shopify.dev documentation
- **fetch_full_docs** — retrieve complete documentation for specific paths
- **introspect_admin_schema** — explore Shopify's Admin GraphQL schema (queries, mutations, types, fields)
- **learn_shopify_api** — teaches the LLM about supported Shopify APIs and generates valid code blocks

Covers Admin GraphQL API, Polaris components, Shopify Functions, Hydrogen, and Storefront Web Components. The Winter '26 Edition expanded coverage to the entire platform with server-side rendering for fast documentation delivery.

## Payment Processing

### stripe/agent-toolkit (Official — Comprehensive Payments)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [stripe/ai](https://github.com/stripe/ai) | 1,500 | TypeScript | MIT | 25 |

**stripe/ai** (1,500 stars, 326 commits, 257 forks) is Stripe's consolidated monorepo for AI-powered commerce — formerly stripe/agent-toolkit. It now includes three packages: **@stripe/agent-toolkit** (framework integrations for OpenAI, LangChain, CrewAI, Vercel AI SDK), **@stripe/ai-sdk** (connects Stripe billing with Vercel's AI libraries), and **@stripe/token-meter** (usage-based billing metering with native SDKs from OpenAI, Anthropic, and Google). The MCP server provides 25 tools spanning the full Stripe API surface, with both local deployment and a hosted remote MCP server at `mcp.stripe.com` with OAuth access.

**Customer & Account:**
- `create_customer`, `list_customers` — customer record management
- `get_stripe_account_info` — account details
- `retrieve_balance` — current balance

**Products & Pricing:**
- `create_product`, `list_products` — product catalog
- `create_price`, `list_prices` — pricing configuration
- `create_coupon`, `list_coupons` — discount management

**Payments & Billing:**
- `create_payment_link` — shareable payment URLs
- `list_payment_intents` — payment tracking
- `create_invoice`, `create_invoice_item`, `finalize_invoice`, `list_invoices` — invoicing
- `list_subscriptions`, `update_subscription`, `cancel_subscription` — recurring billing
- `create_refund` — refund processing
- `list_disputes`, `update_dispute` — chargeback management

**Search & Documentation:**
- `search_stripe_resources` — query Stripe data
- `fetch_stripe_resources` — retrieve specific objects
- `search_stripe_documentation` — knowledge base access

Supports OpenAI Agent SDK, LangChain, CrewAI, and Vercel AI SDK integrations. Python 3.11+ and Node 18+ required. The remote MCP deployment at `mcp.stripe.com` eliminates the need for local API key management through OAuth flows.

**Stripe Sessions 2026 (April 29-30, San Francisco):** Stripe's annual conference centered agentic commerce as its primary theme, announcing **288 new products and features**. Key MCP-relevant announcements: **Link agent wallet** — AI agents can initiate payments using saved payment methods from users' Stripe Link accounts, enabling one-click checkout in agent flows. **Treasury APIs with MCP support** — financial agents can now access balance, transfer, and account management via MCP. **Billing for LLM Tokens (Private Preview)** — @stripe/token-meter now supports usage-based billing that tracks token consumption from OpenAI, Anthropic, and Google Gemini natively. Stripe's Machine Payments Protocol (MPP, co-authored with Tempo) continues expanding as a session-based streaming alternative to x402's per-request model.

## Shopify Admin API Servers

### GeLi2001/shopify-mcp (Community Leader)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [GeLi2001/shopify-mcp](https://github.com/GeLi2001/shopify-mcp) | 195 | TypeScript | 31 |

**GeLi2001/shopify-mcp** (195 stars, 35 commits, 88 forks) is the most comprehensive community Shopify Admin MCP server with 31 tools across product, customer, order, and inventory management via Shopify's GraphQL Admin API.

**Product Management (8 tools):** list/search products with pagination and sorting, retrieve product details, create/update/delete products, manage options and variants, handle variant bulk operations.

**Customer Management (8 tools):** list/search customers with advanced filtering, get customer details, create/update/delete customers, merge duplicate accounts, manage addresses.

**Order Management (10 tools):** list orders with filtering/pagination/sorting, retrieve order details, update orders, access customer-specific orders, cancel/close/reopen orders, mark as paid, create fulfillments with tracking, process refunds, create and complete draft orders.

**Additional:** Metafield management (get, set, delete), inventory quantity adjustments, tag management for taggable resources.

Supports both OAuth client credentials (January 2026+ Dev Dashboard apps) and static access tokens (legacy apps).

### pashpashpash/shopify-mcp-server (Lightweight)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pashpashpash/shopify-mcp-server](https://github.com/pashpashpash/shopify-mcp-server) | 35 | TypeScript | MIT | 15 |

**pashpashpash/shopify-mcp-server** (35 stars, 2 commits) provides a lighter Shopify Admin integration with 15 tools covering products, customers, orders, collections, discounts, shop info, and webhook management via GraphQL.

### antoineschaller/shopify-mcp-server (JavaScript Alternative)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [antoineschaller/shopify-mcp-server](https://github.com/antoineschaller/shopify-mcp-server) | 10 | JavaScript | MIT | 22 |

**antoineschaller/shopify-mcp-server** (10 stars, 7 commits) provides 22 tools including analytics and reporting capabilities (`get_analytics`, `get_reports`) not found in other Shopify servers, plus inventory tracking, order fulfillment, and discount creation.

## Open-Source E-Commerce Platforms

### techspawn/woocommerce-mcp-server (Full WooCommerce API)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [techspawn/woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server) | 86 | TypeScript | 50+ |

**May 2026 update:** The **official WooCommerce MCP server entered public beta** — built directly by WooCommerce/Automattic, it runs inside WordPress with full site visibility, enabling agents to suggest theme changes, debug plugins, and rewrite checkout pages alongside standard store management operations.

**techspawn/woocommerce-mcp-server** (86 stars, 44 forks, 8 commits) remains the most comprehensive community WooCommerce MCP server, providing full WordPress REST API coverage across virtually every WooCommerce resource.

**Product Management:** CRUD operations, categories, tags, attributes, variations, reviews, metadata.

**Order Processing:** Full CRUD, order notes, refund handling, metadata operations.

**Customer Management:** CRUD operations, customer metadata.

**Shipping & Logistics:** Shipping zones, methods, location-based shipping configuration.

**Financial Operations:** Tax classes and rates, coupon/discount management, payment gateway configuration.

**Content Management:** WordPress post creation and updates, post metadata.

**Analytics & Reporting:** Sales, product, order, category, customer, inventory, coupon, and tax reports.

**Store Configuration:** Settings management, system status monitoring, continent/country/currency data.

Supports both WooCommerce API key and WordPress username/password authentication. Cross-platform (Windows, macOS, Linux).

### SGFGOV/medusa-mcp (MedusaJS Integration)

| Server | Stars | Language | License | Commits |
|--------|-------|----------|---------|---------|
| [SGFGOV/medusa-mcp](https://github.com/SGFGOV/medusa-mcp) | 54 | TypeScript | MIT | 30 |

**SGFGOV/medusa-mcp** (54 stars, 30 commits, 19 forks) bridges AI tools with MedusaJS commerce systems through standardized JSON-RPC communication. Built on the Medusa JS SDK with OpenAPI schema-based endpoints, it provides a modular, extensible plugin system for workflow automation — managing inventory, pricing, and service integrations.

Supports both admin and storefront API endpoints, Docker deployment, and Claude Skill generation. MedusaJS itself (30,900+ GitHub stars) is one of the most popular open-source headless commerce platforms.

### saleor/saleor-mcp (Official — Read-Only GraphQL)

| Server | Stars | Language | License | Commits |
|--------|-------|----------|---------|---------|
| [saleor/saleor-mcp](https://github.com/saleor/saleor-mcp) | 13 | Python | AGPL-3.0 | 38 |

**saleor/saleor-mcp** (13 stars, 38 commits) is the official Saleor Commerce MCP server, providing **read-only** access to products, customers, and orders through GraphQL. Uses Streamable HTTP transport with domain validation via regex patterns and custom header authentication (`X-Saleor-API-URL`, `X-Saleor-Auth-Token`).

Code generation via ariadne-codegen, Docker deployment support, compatible with Saleor 3.21+. The read-only design is an intentional safety choice for an official vendor server.

### commercetools/commerce-mcp (Official — Enterprise Commerce)

| Server | Stars | Language | License | Commits |
|--------|-------|----------|---------|---------|
| [commercetools/commerce-mcp](https://github.com/commercetools/commerce-mcp) | 2 | TypeScript | MIT* | 87 |

**commercetools/commerce-mcp** (2 stars, 87 commits) is the official commercetools MCP server with the most comprehensive tool set of any enterprise commerce MCP implementation. Despite low stars, the 87 commits indicate active development.

Provides tools across: Products, Orders, Carts, Customers, Customer Groups, Categories, Channels, Stores, Inventory, Pricing, Product Discounts, Cart Discounts, Quotes, Business Units, Payments, Shopping Lists, Extensions, Custom Objects, Custom Types, Tax, Shipping, Zones, and Recurring Orders — each with read, create, and update operations.

Configurable tool loading with `all` (everything) or `all.read` (read-only) presets. Client credentials or access token authentication. 1,000,000 invocation limit for non-commercial use under MIT license with commercial use restrictions.

## Marketplace & Shopping Integrations

### Fewsats/amazon-mcp (Amazon with L402 Payments)

| Server | Stars | Language | Commits |
|--------|-------|----------|---------|
| [Fewsats/amazon-mcp](https://github.com/Fewsats/amazon-mcp) | 75 | Python | 14 |

**Fewsats/amazon-mcp** (75 stars, 14 commits) enables searching and purchasing Amazon products through AI agents using the **L402 payment protocol** via Fewsats infrastructure. Custom budget limits, spending caps, approval thresholds, and manual review options provide purchase safety controls.

Compatible with Claude Desktop and Cursor IDE. The L402 protocol integration is notable — it provides a standardized payment layer rather than requiring direct Amazon account credentials.

### rigwild/mcp-server-amazon (Cart-Based Shopping)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rigwild/mcp-server-amazon](https://github.com/rigwild/mcp-server-amazon) | 19 | TypeScript | MIT | 5 |

**rigwild/mcp-server-amazon** (19 stars, 22 commits) provides a more traditional Amazon shopping flow — search products, view details, manage shopping cart, place orders, and access order history. Generates Amazon checkout links for purchase completion rather than handling payment directly.

### profplum700/etsy-mcp-server (Shop Management)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [profplum700/etsy-mcp-server](https://github.com/profplum700/etsy-mcp-server) | 9 | TypeScript | MIT | 11 |

**profplum700/etsy-mcp-server** (9 stars, 25 commits) bridges Etsy's API with MCP for shop management — retrieve shop info, view inventory with state filtering, create draft listings, upload listing images, update listings, access transaction history, manage shop sections, and explore product taxonomy hierarchies.

Docker containerization and MCP Inspector debugging support. Designed for sellers managing their shops through AI agents rather than consumer shopping.

### YosefHayim/ebay-mcp (Comprehensive eBay Sell API)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [YosefHayim/ebay-mcp](https://github.com/YosefHayim/ebay-mcp) | 48 | TypeScript | 325 |

**YosefHayim/ebay-mcp** (48 stars, 617 commits, 29 forks) fills what was previously a major gap — comprehensive eBay integration with **325 tools** covering 270 unique eBay Sell API endpoints at 100% coverage. Covers inventory management, order fulfillment, marketing campaigns, analytics, and developer tools.

Key features:
- **OAuth 2.0 authentication** with smart fallback mechanisms
- **Auto-configuration** for 9 AI clients (Claude Desktop, Cursor, Zed, and more)
- **958+ passing tests** — unusually thorough for an MCP server
- **Interactive setup wizard** (`npm run setup`) for credential configuration
- **Scalable API access** — from 1,000 to 10,000-50,000 daily API requests via OAuth escalation

Built with TypeScript and Zod validation for type safety. **Security warning:** CVE-2026-27203 (environment variable injection in `updateEnvFile` in `src/auth/oauth.ts`) was disclosed February 19, 2026 and remains **unpatched as of May 2026** — all versions through v1.7.2 are affected. Attackers can inject arbitrary environment variables; do not deploy this server in production environments handling real commerce data until a patched release ships.

### Square MCP Server (Official — Payments & Commerce)

| Server | Stars | Auth | Transport |
|--------|-------|------|-----------|
| [Square MCP](https://mcp.squareup.com/) | 99 | OAuth | SSE (remote) |

**Square MCP Server** (99 stars) is Square's official remote MCP server — filling another previously-noted gap. Provides a bridge between Square's complete API ecosystem and AI assistants, covering payments, orders, inventory, and customer management. OAuth-based authentication at `mcp.squareup.com` with no API key setup required.

Note: This is a **paid service with no free tier** — requires an active Square account. Uses the SSE transport protocol. PulseMCP: ~53.8K all-time visitors, ~1.9K weekly, #559 globally.

### Zendrop MCP Server (Dropshipping — First in Category)

| Server | Type | Auth | Launch |
|--------|------|------|--------|
| [Zendrop MCP](https://app.zendrop.com/mcp/v1) | Commercial remote | Token + scopes | April 9, 2026 |

**Zendrop MCP** is the **first dedicated dropshipping MCP server** — launched April 9, 2026. Merchants can connect AI assistants (Claude, ChatGPT, Gemini) to live store data for product searches, order tracking, and fulfillment management in real time. Merchants generate access tokens at `app.zendrop.com/mcp/v1` and assign granular scopes controlling what the AI can read or write.

Available to all Zendrop merchants, from solo Shopify sellers to high-volume operators managing thousands of orders per month.

### Easyship Global Shipping MCP (First Cross-Border Shipping — April 30, 2026)

| Server | Type | Tools | Auth | Coverage |
|--------|------|-------|------|----------|
| Easyship MCP | Commercial remote | 25 | API key | 550+ couriers, 200+ countries |

**Easyship launched the first cross-border shipping MCP server on April 30, 2026** — available at no additional cost on the MCP Registry to all Easyship account holders. This creates a new sub-category: **fulfillment and logistics MCP servers** that sit downstream from commerce platforms, handling the physical shipment of goods sold through Shopify, WooCommerce, and others.

25 tools covering the full shipping lifecycle:

- **Rates & Routing:** Real-time rate comparison across 550+ couriers; automated best-rate selection by price, speed, or reliability
- **Label Generation:** Create and download labels; return label generation
- **Address Validation:** Validate ship-from and ship-to addresses for 200+ countries
- **Tracking:** Real-time tracking lookups; multi-shipment status
- **Customs & Compliance:** Automated import tax and duty calculation; customs documentation generation
- **Billing & Analytics:** Easyship account balance, shipment analytics, cost breakdowns

The cross-border customs calculation capability is particularly notable — this has historically required specialized shipping expertise. Easyship covers 200+ countries and territories, and automated duty calculation removes a common barrier to international e-commerce expansion.

Available via the MCP Registry; no additional cost on existing Easyship plans.

### BigCommerce Storefront MCP (Official — May 11, 2026)

| Server | Type | Tools | Auth | Available |
|--------|------|-------|------|-----------|
| BigCommerce Storefront MCP | Platform-native | Catalog + Cart | None (guest) / OAuth (auth'd) | Early Access |
| CData BigCommerce MCP | Read-only | Query-based | JDBC | GA |
| StackOne BigCommerce MCP | Full CRUD | 120 | OAuth | GA |
| Community BigCommerce MCP | Products/Orders/Customers | varies | API key | GA |

**BigCommerce launched its official Storefront MCP on May 11, 2026** — available to every live, transacting BigCommerce store via Settings → Early Access. This closes what was previously listed as a major gap in this category. The official server covers the B2C guest shopping flow: product catalog search with variants, cart building and management, and checkout URL generation. Authenticated shopping (personalized pricing, order history) is on the roadmap as the next milestone.

The significance mirrors Shopify's Storefront MCP launch: every BigCommerce store now has a standard AI-agent-accessible endpoint with zero custom integration required. BigCommerce has the second-largest US market share among hosted commerce platforms.

Third-party options remain available for more advanced use cases: **StackOne** offers **120 pre-built actions** with managed authentication, prompt injection defense, and a Connector Builder. **CData** provides read-only access via JDBC drivers. **Zapier** and **Truto** offer managed integrations. Open-source community implementations (isaacgounton/bigcommerce-api-mcp) cover products, customers, and orders.

## Digital Product & Creator Platforms

### rmarescu/gumroad-mcp (Digital Products)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rmarescu/gumroad-mcp](https://github.com/rmarescu/gumroad-mcp) | 19 | TypeScript | MIT | 7 |

**rmarescu/gumroad-mcp** (19 stars, 39 commits) manages digital product sales on Gumroad — product retrieval, enable/disable listings, sales analytics, offer code CRUD (create, view, update, delete promotions), and user account information.

### atharvagupta2003/mcp-lemonsqueezy (Subscriptions & Checkouts)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [atharvagupta2003/mcp-lemonsqueezy](https://github.com/atharvagupta2003/mcp-lemonsqueezy) | 9 | Python | MIT | 10+ |

**atharvagupta2003/mcp-lemonsqueezy** (9 stars, 23 commits) provides store, product, variant, order, customer, subscription, license key, checkout session, and webhook management for the Lemon Squeezy platform. Includes audit logging of all actions — useful for tracking what AI agents do with your commerce data.

## Other Platforms

### latinogino/prestashop-mcp (PrestaShop Store Management)

| Server | Stars | Language | Commits | Tools |
|--------|-------|----------|---------|-------|
| [latinogino/prestashop-mcp](https://github.com/latinogino/prestashop-mcp) | 9 | Python | 46 | 20+ |

**latinogino/prestashop-mcp** (9 stars, 46 commits) enables comprehensive PrestaShop store management — product CRUD with stock/price management, category management with hierarchy filtering, customer management, order management with status updates, module management (install/activate/deactivate), main menu navigation customization, cache management, and theme configuration.

Async/await architecture with comprehensive error handling and a production-ready test suite.

## Emerging Commerce Protocols

### Google Universal Commerce Protocol (UCP)

**Google's Universal Commerce Protocol** is an Apache-2.0 open-source standard designed to power the next generation of agentic commerce. It establishes a common language and functional primitives for seamless commerce between consumer surfaces, businesses, and payment providers.

Key characteristics:

- **Transport-agnostic** — supports REST, JSON-RPC, MCP, and A2A (Agent-to-Agent), so the same capability schemas work across backend services, MCP tool calls, and agent networks
- **Industry backing** — developed with Shopify, Etsy, Wayfair, Target, Walmart, and endorsed by Adyen, American Express, Best Buy, Flipkart, Macy's, Mastercard, Stripe, The Home Depot, Visa, and Zalando (20+ global partners)
- **Interoperable** — works with Agent Payments Protocol (AP2) for secure agentic payment support
- **Commerce primitives** — catalog search, cart updates, checkout, order status, returns, CRM opt-ins, account management, and loyalty

**March 19, 2026 update:** Google announced significant UCP capability additions:
- **Cart capability** — agents can now save multiple items to a cart at once from a single store, matching real shopping behavior
- **Catalog capability** — agents can retrieve real-time product details (variants, inventory, pricing) from a retailer's catalog
- **Identity Linking** — shoppers receive loyalty/member benefits on UCP-integrated platforms
- **Simplified Merchant Center onboarding** — a dedicated UCP integration tab rolling out in Merchant Center accounts across the US
- **Platform partnerships** — Commerce Inc, Salesforce, and Stripe implementing UCP on their platforms

**Google I/O 2026 (May 2026):** Google announced the **Universal Cart** — a cross-merchant shopping experience rolling out across Search, Gemini, YouTube, and Gmail in the US (summer 2026), with Canada, Australia, and UK expansion planned. Shoppers can add items from multiple retailers to a single persistent cart, with Identity Linking carrying loyalty/member benefits across UCP-integrated platforms. Hotels and local food delivery are being added as new verticals.

Simultaneously, **Shopify's migration of its Storefront Catalog MCP to UCP** (May 30 effective, June 15 mandatory) represents the first major platform-enforcing the protocol transition, validating UCP as the operational standard Shopify intends to build around.

This is the most significant standardization effort in agentic commerce — when Google, Shopify, Stripe, Walmart, Visa, and Mastercard all agree on a protocol, it's likely to become the foundation for AI-driven shopping.

### Stripe Agentic Commerce Protocol (ACP)

**Stripe's Agentic Commerce Protocol**, co-developed with OpenAI, is an open-source specification that enables commerce between AI applications (like ChatGPT) and sellers. It can be implemented as a RESTful interface or MCP server.

ACP provides a standardized way for AI agents to submit orders, manage transactions, and preserve brand identity and customer ownership. Built on Stripe's 15 years of commerce infrastructure experience, it powers features like Instant Checkout in ChatGPT.

### The Broader Protocol Landscape (Q2 2026)

The agentic commerce protocol space has expanded rapidly — as of Q2 2026, **10 active protocols** target agent-driven commerce:

1. **ACP** (Stripe + OpenAI) — order processing between AI agents and merchants
2. **UCP** (Google + 20+ partners) — universal commerce primitives across transports
3. **Shopify Agents** — platform-native agentic storefronts
4. **Amazon Buy for Me** — AI-assisted purchasing on Amazon
5. **Mastercard Verifiable Intent** — cryptographic purchase verification
6. **Stripe Machine Payments** — autonomous agent payment infrastructure
7. **x402** — HTTP-native micropayments protocol
8. **Google Agentic Checkout** — checkout flows in AI Mode
9. **Visa Ready** — agent authentication via network tokens
10. **Klarna Agent Mode** — buy-now-pay-later for AI agents

**April 28, 2026 update:** Two new protocols enter the count via FIDO Alliance contributions:

11. **AP2 v0.2** (Google → FIDO) — "Human Not Present" autonomous payments support; v0.2 released as Google donated AP2 to FIDO Alliance's new Agentic Authentication Technical Working Group
12. **Mastercard Verifiable Intent** (open-sourced April 28) — cryptographic proof of consumer authorization for agent transactions using Selective Disclosure; co-developed with Google; now part of FIDO's Payments Technical Working Group (chaired by Mastercard and Visa representatives)

The FIDO Alliance forming these working groups is a regulatory maturity signal — the same organization behind FIDO2/WebAuthn and passkeys is now standardizing agent authentication and payment authorization. Unlike the commerce-layer protocols, these operate at the trust layer: proving that a human actually authorized an agent to act.

This proliferation signals that agentic commerce is entering a standards competition phase — consolidation is likely but not yet underway.

## Advertising & Platform Commitments

### Meta Ads AI Connectors (April 29, 2026 — Open Beta)

| Server | Type | Tools | Access | Platforms |
|--------|------|-------|--------|-----------|
| Meta Ads AI Connectors | Commercial remote | 29 | MCP-compatible | ChatGPT, Claude, others |

**Meta launched AI Connectors for Meta Ads on April 29, 2026** in open beta globally — enabling any MCP-compatible AI client to access and manage Meta advertising campaigns. This is the first official MCP integration from Meta, covering the advertising layer of Facebook, Instagram, and Messenger commerce.

29 tools cover:
- **Performance Reporting:** Campaign analytics, ad set metrics, ad-level data, audience insights
- **Campaign Management:** Create/update campaigns, pause/resume, adjust budgets
- **Catalog Management:** Product catalog operations for dynamic ads
- **Signal Diagnostics:** Event match quality checks, pixel health

Read/write capable — agents can create campaigns, adjust budgets, and pause underperformers without requiring human interaction in Ads Manager. Particularly relevant for Shopify and WooCommerce merchants running performance marketing alongside their store's MCP operations.

### Adobe Commerce: MCP as Default Agent Protocol

**Adobe Commerce (formerly Magento) made MCP its default agent protocol at Summit 2026.** Adobe's Commerce MCP server provides access to catalog, cart, pricing, inventory, promotions, checkout, orders, and post-purchase flows. Reference architectures cover Microsoft Copilot, ChatGPT Enterprise, Claude, and Gemini Enterprise. Adobe also committed to supporting UCP and ACP alongside MCP as complementary standards. Given Adobe Commerce's penetration in enterprise and mid-market retail, this commitment extends MCP's reach into the segment that had been most reliant on proprietary integrations.

## What's Missing

The e-commerce MCP ecosystem has narrowed its gaps significantly since March 2026, but notable holes remain:

- **No cross-platform price comparison** — no MCP server compares prices across Amazon, Walmart, Target, etc.
- **No official Amazon MCP server** — Amazon's "Buy for Me" is a platform feature, not an open MCP server; community servers (Fewsats, rigwild) remain unofficial; Amazon Ads MCP is advertising-only
- ~~No official BigCommerce MCP server~~ — **FILLED** (official Storefront MCP May 11, 2026; StackOne, CData, community also available)
- ~~No Square POS MCP server~~ — **FILLED** (official at mcp.squareup.com, 99 stars, OAuth)
- ~~No official eBay MCP server~~ — **PARTIALLY FILLED** (YosefHayim/ebay-mcp community server with 325 tools, but CVE-2026-27203 unpatched and still no official eBay server)
- **Fragmented Shopify Admin landscape** — still 6+ community servers with overlapping features
- **Limited purchase safety controls** — most shopping servers don't enforce spending limits or confirmation flows
- **No product review aggregation** — no server collects and analyzes customer reviews across platforms
- **No inventory synchronization** — no multi-platform inventory management through MCP
- **No returns/refund automation** — limited support for post-purchase workflows beyond basic refund creation
- **Protocol fragmentation intensifying** — now 12+ competing agentic commerce protocols; FIDO standards work is a positive signal but active competition has no convergence path yet
- **UCP migration risk** — Shopify's June 15 mandatory cutover creates developer urgency; integrations not updated will break

## Rating: 4.5 / 5

The e-commerce MCP ecosystem holds at **4.5/5** — the May 2026 update brings meaningful additions but also new concerns that balance out.

**Positive developments:** **BigCommerce launched its official Storefront MCP (May 11)**, closing the last major platform gap — every major commerce platform now has at least one official MCP server. **Easyship** opened a new subcategory (cross-border shipping/fulfillment) that fills a genuine operational gap. **Stripe Sessions 2026** (288 features, Link agent wallet) and **Google UCP Universal Cart** demonstrate the protocol layer is solidifying into real consumer-facing products. **FIDO Alliance involvement** (April 28) signals the agentic commerce space is mature enough for standards-body attention. **Adobe Commerce** making MCP its default extends coverage to the enterprise segment.

**Countervailing concerns:** **eBay's CVE-2026-27203 remains unpatched** — a production server with 325 tools and a security hole with no fix is a meaningful deduction. **Protocol fragmentation intensified** to 12+ standards; FIDO's work is promising but adds complexity short-term. **Shopify's UCP migration deadline (June 15)** creates a breaking change that will catch developers off-guard. **Amazon's walled garden remains complete** — Buy for Me, Rufus, and Alexa+ all bypass open protocols.

At this rate, the category is tracking toward 5/5 — but not yet. Consumer-side shopping intelligence (price comparison, deal aggregation, review synthesis) remains entirely absent, and the gap between "agents can sell things" and "agents can intelligently shop for things" is still wide.

**Category**: [Finance & Fintech](/categories/finance-fintech/)

*This review was last edited on 2026-05-20 using Claude Sonnet 4.6 (Anthropic).*

