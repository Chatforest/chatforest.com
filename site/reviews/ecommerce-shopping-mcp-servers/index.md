# E-Commerce & Shopping MCP Servers — Shopify, Stripe, WooCommerce, Amazon, and More

> E-commerce and shopping MCP servers are turning AI agents into store operators, shopping assistants, and payment processors — letting them manage products, process orders, handle


E-commerce and shopping MCP servers are turning AI agents into store operators, shopping assistants, and payment processors. Instead of navigating web interfaces or building custom integrations, these servers let agents manage product catalogs, process orders, handle payments, track customers, and guide shoppers through checkout — all through the Model Context Protocol.

The landscape spans six areas: **platform-native commerce** (Shopify's built-in MCP endpoints), **payment processing** (Stripe's comprehensive toolkit), **Shopify Admin servers** (community-built store management), **open-source platforms** (WooCommerce, Medusa, Saleor, commercetools), **marketplace integrations** (Amazon, Etsy), and **emerging protocols** (Google UCP, Stripe ACP).

The headline findings: **Shopify is the first major commerce platform with native MCP integration** — every store gets a free Storefront MCP endpoint at `/api/mcp` with no authentication required. **Stripe dominates payment processing** with 25 tools and both local and hosted remote MCP deployment. **WooCommerce has the most comprehensive open-source store management server** covering products, orders, shipping, taxes, and analytics. **Google's Universal Commerce Protocol signals industry-wide standardization** with backing from Shopify, Stripe, Walmart, Target, Visa, and Mastercard. **Consumer-side shopping intelligence is notably absent** — no MCP server yet offers cross-platform price comparison or deal-finding capabilities.

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

### Shopify Dev MCP (Official — Developer Documentation)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [Shopify Dev MCP](https://shopify.dev/docs/apps/build/devmcp) | 488 | TypeScript | 4+ |

**Shopify Dev MCP** (`@shopify/dev-mcp` on npm) enables AI assistants to search Shopify documentation, explore API schemas, and generate valid code for Shopify APIs. Run via `npx -y @shopify/dev-mcp@latest`.

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
| [stripe/agent-toolkit](https://github.com/stripe/agent-toolkit) | 1,400 | TypeScript | MIT | 25 |

**stripe/agent-toolkit** (1,400 stars, 296 commits, 34+ contributors) is Stripe's official one-stop shop for building AI-powered commerce. It provides 25 tools spanning the full Stripe API surface, with both local deployment and a hosted remote MCP server at `mcp.stripe.com` with OAuth access.

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

## Shopify Admin API Servers

### GeLi2001/shopify-mcp (Community Leader)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [GeLi2001/shopify-mcp](https://github.com/GeLi2001/shopify-mcp) | 147 | TypeScript | 31 |

**GeLi2001/shopify-mcp** (147 stars, 32 commits) is the most comprehensive community Shopify Admin MCP server with 31 tools across product, customer, order, and inventory management via Shopify's GraphQL Admin API.

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
| [techspawn/woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server) | 82 | TypeScript | 50+ |

**techspawn/woocommerce-mcp-server** (82 stars, 8 commits) is the most comprehensive WooCommerce MCP server, providing full WordPress REST API coverage across virtually every WooCommerce resource.

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
| [SGFGOV/medusa-mcp](https://github.com/SGFGOV/medusa-mcp) | 51 | TypeScript | MIT | 28 |

**SGFGOV/medusa-mcp** (51 stars, 28 commits) bridges AI tools with MedusaJS commerce systems through standardized JSON-RPC communication. Built on the Medusa JS SDK with OpenAPI schema-based endpoints, it provides a modular, extensible plugin system for workflow automation — managing inventory, pricing, and service integrations.

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
| [commercetools/commerce-mcp](https://github.com/commercetools/commerce-mcp) | 1 | TypeScript | MIT* | 86 |

**commercetools/commerce-mcp** (1 star, 86 commits) is the official commercetools MCP server with the most comprehensive tool set of any enterprise commerce MCP implementation. Despite low stars, the 86 commits indicate active development.

Provides tools across: Products, Orders, Carts, Customers, Customer Groups, Categories, Channels, Stores, Inventory, Pricing, Product Discounts, Cart Discounts, Quotes, Business Units, Payments, Shopping Lists, Extensions, Custom Objects, Custom Types, Tax, Shipping, Zones, and Recurring Orders — each with read, create, and update operations.

Configurable tool loading with `all` (everything) or `all.read` (read-only) presets. Client credentials or access token authentication. 1,000,000 invocation limit for non-commercial use under MIT license with commercial use restrictions.

## Marketplace & Shopping Integrations

### Fewsats/amazon-mcp (Amazon with L402 Payments)

| Server | Stars | Language | Commits |
|--------|-------|----------|---------|
| [Fewsats/amazon-mcp](https://github.com/Fewsats/amazon-mcp) | 68 | Python | 14 |

**Fewsats/amazon-mcp** (68 stars, 14 commits) enables searching and purchasing Amazon products through AI agents using the **L402 payment protocol** via Fewsats infrastructure. Custom budget limits, spending caps, approval thresholds, and manual review options provide purchase safety controls.

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

This is the most significant standardization effort in agentic commerce — when Google, Shopify, Stripe, Walmart, Visa, and Mastercard all agree on a protocol, it's likely to become the foundation for AI-driven shopping.

### Stripe Agentic Commerce Protocol (ACP)

**Stripe's Agentic Commerce Protocol**, co-developed with OpenAI, is an open-source specification that enables commerce between AI applications (like ChatGPT) and sellers. It can be implemented as a RESTful interface or MCP server.

ACP provides a standardized way for AI agents to submit orders, manage transactions, and preserve brand identity and customer ownership. Built on Stripe's 15 years of commerce infrastructure experience, it powers features like Instant Checkout in ChatGPT.

## What's Missing

The e-commerce MCP ecosystem has notable gaps:

- **No cross-platform price comparison** — no MCP server compares prices across Amazon, Walmart, Target, etc.
- **No official BigCommerce MCP server** — despite being a major platform
- **No Square POS MCP server** — the leading point-of-sale platform has no MCP integration
- **No official eBay MCP server** — one of the largest marketplaces has no agent interface
- **Fragmented Shopify Admin landscape** — 6+ community servers with overlapping features, no consolidation
- **Limited purchase safety controls** — most Amazon shopping servers don't enforce spending limits or confirmation flows
- **No product review aggregation** — no server collects and analyzes customer reviews across platforms
- **No inventory synchronization** — no multi-platform inventory management through MCP
- **No returns/refund automation** — limited support for post-purchase workflows beyond basic refund creation

## Rating: 4.0 / 5

The e-commerce MCP ecosystem earns **4.0/5** — Shopify's platform-native MCP is a genuine industry first (making millions of stores AI-accessible by default), Stripe's toolkit is the gold standard for payment processing integration, WooCommerce gets comprehensive coverage, and the commercetools server demonstrates enterprise-grade commerce tooling. The Google UCP and Stripe ACP protocols signal that agentic commerce standardization is a priority for the world's largest commerce companies.

Deductions for: fragmented Shopify Admin server landscape with 6+ overlapping community implementations, no consumer-facing shopping intelligence (price comparison, deal-finding, review aggregation), missing major platforms (BigCommerce, Square, eBay), limited safety controls for AI-driven purchases, and the Amazon servers being unofficial with potential reliability concerns. The gap between Shopify's visionary platform-native approach and other platforms' absence is striking — this is a category where first-mover advantage matters enormously.

**Category**: [Finance & Fintech](/categories/finance-fintech/)

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

