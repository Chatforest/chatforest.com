# Best E-Commerce MCP Servers in 2026

> Shopify, WooCommerce, Magento, BigCommerce, Amazon, eBay, Etsy, Square, and headless platforms — we've reviewed 40+ e-commerce MCP servers across 10 categories. Here's what works, what's emerging, and where the gaps are.


E-commerce MCP servers let AI agents interact with online stores — managing products, processing orders, searching catalogs, handling inventory, and powering AI-driven shopping experiences. Instead of clicking through admin dashboards or writing API calls manually, you describe what you want and the agent executes it against your store's backend.

We've researched 40+ e-commerce MCP servers across the full landscape. This guide synthesizes all of that into one page: what's worth using, what's not, and where the gaps are.

> **⚠ Security note:** The MCP ecosystem saw 30+ CVEs filed in 60 days in early 2026. E-commerce-adjacent vulnerabilities include CVE-2026-27203 (environment variable injection in a community eBay MCP server) and CVE-2026-1926 (WooCommerce Subscriptions auth bypass). Always vet community servers before connecting them to production stores.

*Note: Our recommendations are based on documentation review, GitHub analysis, and community feedback — not hands-on testing of every server. Star counts were verified in April 2026.*

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| Shopify (storefront/shopping) | [Shopify Storefront MCP](https://shopify.dev/docs/apps/build/storefront-mcp/servers/storefront) | Official | [Shopify Catalog MCP](https://shopify.dev/docs/agents/catalog/mcp) (cross-merchant discovery) |
| Shopify (developer) | [Shopify Dev MCP](https://www.npmjs.com/package/@shopify/dev-mcp) | ~488 | v1.7.0, 8 tools, full platform coverage |
| Shopify (admin/store management) | [GeLi2001/shopify-mcp](https://github.com/GeLi2001/shopify-mcp) | 181 | [trigga6006/shopify-mcp-server](https://github.com/trigga6006/shopify-mcp-server) (70+ tools) |
| WooCommerce | [WooCommerce Native MCP](https://developer.woocommerce.com/docs/features/mcp/) | Official (beta) | [techspawn/woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server) (84 stars) |
| Magento / Adobe Commerce | [boldcommerce/magento2-mcp](https://github.com/boldcommerce/magento2-mcp) | 54 | [Freento MCP](https://commercemarketplace.adobe.com/freento-module-mcp.html) (Adobe Marketplace) |
| Amazon (seller analytics) | [Seller Labs MCP](https://www.sellerlabs.com/amazon-mcp/) | — | [Amazon Ads MCP](https://advertising.amazon.com/) (official, 50+ tools) |
| Amazon (advertising) | [Amazon Ads MCP Server](https://advertising.amazon.com/) | Official | 50+ tools, open beta since Feb 2026 |
| eBay | [eBay/npm-public-api-mcp](https://github.com/eBay/npm-public-api-mcp) | Official | [YosefHayim/ebay-mcp](https://github.com/YosefHayim/ebay-mcp) (40 stars, 325 tools) |
| Etsy | [aserper/etsy-mcp](https://github.com/aserper/etsy-mcp) | 1 | [profplum700/etsy-mcp-server](https://github.com/profplum700/etsy-mcp-server) (9 stars) |
| Square | [square/square-mcp-server](https://github.com/square/square-mcp-server) | 95 | Official beta |
| BigCommerce | [BigCommerce Storefront MCP](https://www.bigcommerce.com/blog/model-context-protocol/) | Beta | [CData BigCommerce MCP](https://github.com/CDataSoftware/bigcommerce-mcp-server-by-cdata) (read-only) |
| Headless (Saleor) | [saleor/saleor-mcp](https://github.com/saleor/saleor-mcp) | Official | v0.1.4, hosted at mcp.saleor.app |
| Headless (Medusa) | [SGFGOV/medusa-mcp](https://github.com/SGFGOV/medusa-mcp) | 54 | [minimalart/mcp-medusa](https://github.com/minimalart/mcp-medusa) (14 admin tools) |
| Shipping | [Shippo MCP](https://docs.goshippo.com/docs/guides_general/mcpserver/) | Official | Multi-carrier: USPS, UPS, FedEx, DHL |

## Why e-commerce MCP servers matter

E-commerce operations involve repetitive, data-heavy tasks across multiple systems. MCP servers turn these into natural-language commands.

The value comes in three forms:

1. **Store management automation.** "Update the price of SKU-1234 to $29.99 and reduce inventory by 50" — instead of navigating to the product page, finding the variant, and making the change. At scale, agents can process bulk operations that would take hours manually.
2. **AI-powered shopping.** Shopify's Storefront MCP lets AI assistants like ChatGPT and Perplexity search products, manage carts, and initiate checkout directly. This is "agentic commerce" — customers shop through AI agents instead of browsing websites.
3. **Cross-platform analytics.** Ask "What was my best-selling product last month?" or "Which ASINs lost margin this week?" and get answers pulled directly from your store's live data.

The landscape now spans ten categories: **Shopify** (5 official servers plus community admin tools), **WooCommerce** (now with official MCP beta), **Magento/Adobe Commerce** (enterprise), **Amazon** (seller analytics + official Ads MCP), **eBay** (official MCP launched), **Etsy** (community servers), **Square** (official beta), **BigCommerce** (still in beta), **headless platforms** (Saleor, Medusa, PrestaShop), and **shipping** (Shippo as first dedicated logistics MCP).

---

## Shopify storefront servers (official)

Shopify is the clear leader in e-commerce MCP adoption. They've now shipped **five official MCP servers** — Storefront (shopping), Dev (developer docs), Catalog (cross-merchant product discovery), Customer Account, and Checkout (preview) — plus the community fills the admin gap. Agentic Storefronts went live on March 24, 2026, making millions of merchants discoverable and shoppable inside ChatGPT with no separate integration.

### The winner: Shopify Storefront MCP (Official)

**Status:** GA, live on all Shopify stores | **Auth:** None required | **Transport:** Streamable HTTP

[Shopify Storefront MCP](https://shopify.dev/docs/apps/build/storefront-mcp/servers/storefront) is built into every Shopify store. Each store gets its own MCP endpoint that exposes storefront features to AI agents — product search, cart operations, policy Q&A, and checkout initiation.

**Why it wins:** Zero configuration. Every Shopify store automatically has an MCP endpoint. AI assistants like ChatGPT, Perplexity, and Copilot can connect to any Shopify store and help customers browse and buy. No API keys, no custom apps, no setup.

**Key features:**
- **Semantic product search** — natural-language product discovery using vector embeddings
- **Cart operations** — create carts, add/remove items, apply discounts
- **Policy Q&A** — answers questions about return policies, shipping, FAQs
- **Checkout initiation** — starts the checkout flow from within the AI agent
- **MCP UI components** — interactive product cards and cart UI within the agent interface
- **Available on every Shopify store** — part of Hydrogen Winter '26 Edition
- **Agentic Storefronts live (March 24, 2026)** — millions of merchants now discoverable in ChatGPT
- **AI client integrations** — ChatGPT, Perplexity, Microsoft Copilot live; Google AI Mode and Gemini rolling out
- **MCP UI components** — remote resource URIs for interactive product cards, variant selection, bundles, subscriptions in sandboxed iframes

**The catch:** Storefront only. Cannot manage products, inventory, orders, or any admin functions. Read-plus-cart operations, not full store control.

**Best for:** Merchants who want AI agents to help customers shop. This is Shopify's "agentic commerce" play — and it's now live at scale.

### Also notable: Shopify Dev MCP

**Stars:** ~488 | **Language:** TypeScript | **License:** — | **Tools:** 8 | **Latest:** v1.7.0 (April 2026)

[Shopify Dev MCP](https://www.npmjs.com/package/@shopify/dev-mcp) (`@shopify/dev-mcp`) is for developers building Shopify apps, not for managing stores. Winter '26 Edition expanded it to cover the **entire platform** — Admin, UI Extensions, Liquid, and Hydrogen. Infrastructure moved to server-side rendering. Also available via Gemini CLI and as an AI Agent Plugin.

**Key tools:** `learn_shopify_api`, `search_docs_chunks`, `fetch_full_docs`, `introspect_graphql_schema`, `validate_graphql_codeblocks`, `validate_theme_codeblocks`, `validate_theme`, plus Shopify Functions tools

**Best for:** Developers building Shopify apps or themes who want AI-assisted development with validated Shopify API knowledge.

### Also notable: Shopify Catalog MCP (NEW)

[Shopify Catalog MCP](https://shopify.dev/docs/agents/catalog/mcp) enables cross-merchant product discovery — AI agents can search products across multiple Shopify stores. Two tools: `search_global_products` and `get_global_product_details`. This is distinct from the per-store Storefront MCP.

### Also notable: Shopify Checkout MCP (Preview)

Checkout MCP is in preview with select partners. Five tools: `create_checkout`, `get_checkout`, `update_checkout`, `complete_checkout`, `cancel_checkout`. Enables end-to-end purchase flows entirely within AI agent conversations.

---

## Shopify admin servers (community)

The biggest gap in Shopify's MCP story: **no official Admin API MCP server**. For managing products, orders, inventory, customers, and fulfillment, you need community servers. Several exist, but adoption is still early.

### The winner: GeLi2001/shopify-mcp

**Stars:** 181 | **Forks:** 62 | **Language:** TypeScript | **License:** — | **Tools:** 31+ | **Last pushed:** April 5, 2026

[GeLi2001/shopify-mcp](https://github.com/GeLi2001/shopify-mcp) is the most adopted community Shopify admin server. Comprehensive GraphQL Admin API integration covering products, customers, orders, metafields, inventory, and tags. Actively maintained with consistent commits.

**Why it wins:** Most tools, most stars, active maintenance. Cursor-based pagination and Shopify query syntax pass-through on all list endpoints. Direct integration with the 2026-01 GraphQL Admin API version.

**Key features:**
- **Product management** — full CRUD for products, variants, and options (8 tools)
- **Customer management** — full CRUD, merge, and address management (8 tools)
- **Order management** — smart lookup, cancel, close/open, mark as paid, fulfillment, refunds (10 tools)
- **Metafield management** — get, set, and delete metafields on any resource (3 tools)
- **Inventory management** — set absolute inventory quantities at locations
- **Tag management** — add/remove tags on any taggable resource
- **Advanced filtering** — pass-through Shopify query syntax on all list endpoints

**The catch:** Community-maintained with 181 stars — growing but not battle-tested at scale. No official Shopify backing means it could break when APIs change. Requires creating a custom Shopify app for authentication.

**Best for:** Solo merchants and small teams who want AI-powered store management today and accept the risks of community tooling.

### Also notable

- **[trigga6006/shopify-mcp-server](https://github.com/trigga6006/shopify-mcp-server)** — fork with GraphQL fixes and `updatePage` tool, 70+ tools covering all major store operations
- **[antoineschaller/shopify-mcp-server](https://github.com/antoineschaller/shopify-mcp-server)** — 22 tools covering products, orders, customers, inventory, analytics. ⚠ Dormant since August 2025
- **[amir-bengherbi/shopify-mcp-server](https://github.com/amir-bengherbi/shopify-mcp-server)** — similar scope with GraphQL Admin API integration

**Recommendation:** Use GeLi2001/shopify-mcp for admin operations. Pair it with Shopify Storefront MCP for the shopping layer, Catalog MCP for cross-merchant discovery, and Dev MCP for app development. Shopify now has five official servers — but none cover admin operations, so community tools remain essential for store management.

**Full review:** [Shopify MCP Servers](/reviews/shopify-mcp-servers/)

---

## WooCommerce servers

WooCommerce powers ~36% of all online stores via WordPress. **The biggest news since our last update: WooCommerce now has native MCP support in beta.** The ecosystem has matured significantly with both the official integration and the WordPress MCP Adapter as a foundation.

### The winner: WooCommerce Native MCP (Official Beta — NEW)

**Status:** Beta (WooCommerce 10.3+) | **Auth:** WooCommerce REST API keys | **Transport:** Via WordPress MCP Adapter

[WooCommerce Native MCP](https://developer.woocommerce.com/docs/features/mcp/) is built into WooCommerce itself, starting with version 10.3. It bridges to existing REST API endpoints through the WordPress Abilities API and the [WordPress/mcp-adapter](https://github.com/WordPress/mcp-adapter) plugin (805 stars, v0.4.1).

**Why it wins:** Official support from the WooCommerce team. Respects the existing permission system and REST API key authentication. Built on the WordPress Abilities API, which is moving into WordPress Core in version 6.9. No separate server to install — it's part of WooCommerce.

**Key features:**
- **Native integration** — built into WooCommerce, not a separate server
- **WordPress Abilities API** — standardized capability exposure for AI agents
- **Existing permission model** — uses WooCommerce's REST API key auth
- **REST API bridge** — exposes existing endpoints through MCP protocol

**The catch:** Still in beta. Feature coverage may be limited compared to mature community servers. Requires WooCommerce 10.3+ and the WordPress MCP Adapter plugin.

**Best for:** WooCommerce store owners who want official, supported MCP integration.

**Note:** The previous WordPress MCP server (Automattic/wordpress-mcp) was **archived on January 19, 2026** — all users should migrate to [WordPress/mcp-adapter](https://github.com/WordPress/mcp-adapter).

### Also notable

- **[techspawn/woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server)** (84 stars, 45 forks) — standalone Python MCP server via WooCommerce REST API. The most popular community option before the official integration. ⚠ No code updates since November 2025
- **[iOSDevSK/mcp-for-woocommerce](https://github.com/iOSDevSK/mcp-for-woocommerce)** — WordPress plugin approach with STDIO and HTTP Streamable transport, optional JWT authentication
- **[jlfguthrie/woo-mcp](https://github.com/jlfguthrie/woo-mcp)** — similar WordPress plugin approach with dual transport support
- **[deus-h/claudeus-wp-mcp](https://github.com/deus-h/claudeus-wp-mcp)** — broader WordPress MCP that includes WooCommerce support
- **[newfold-labs/wp-module-mcp](https://github.com/newfold-labs/wp-module-mcp)** — Composer package exposing WordPress functionality through MCP, including WooCommerce
- **[CDataSoftware/woocommerce-mcp-server-by-cdata](https://github.com/CDataSoftware/woocommerce-mcp-server-by-cdata)** — read-only MCP via CData JDBC Drivers

**WooCommerce's MCP advantage:** Full ownership of the server and now official backing. The native integration means WooCommerce is closing the gap with Shopify's official MCP strategy.

---

## Magento / Adobe Commerce servers

Magento (now Adobe Commerce) is the enterprise e-commerce platform. MCP server options have expanded, with a third-party server now on the official Adobe Commerce Marketplace.

### The winner: boldcommerce/magento2-mcp

**Stars:** 54 | **Forks:** 20 | **Language:** Node.js | **License:** — | **Tools:** 6+

[boldcommerce/magento2-mcp](https://github.com/boldcommerce/magento2-mcp) by Bold Commerce connects to Magento 2's REST API, allowing MCP clients to query and manage store data.

**Why it wins:** Most adopted dedicated Magento 2 MCP server. Covers the essential commerce operations: products, customers, orders, and revenue analytics. Stars doubled since our last update (27→54).

**Key features:**
- **Product management** — fetch by SKU or ID, search with filters, read categories, update attributes and prices
- **Stock information** — inventory data retrieval
- **Customer data** — retrieve customer information and ordered products
- **Order analytics** — order counts and revenue filtered by country and date ranges
- **REST API integration** — standard Magento 2 API token authentication

**The catch:** Read-heavy. Product attribute and price updates are supported, but order creation and fulfillment management are limited. ⚠ No code updates since April 2025 — approaching one year dormant.

**Best for:** Magento merchants who want AI-powered product and analytics queries.

### Also notable

- **[Freento MCP Server](https://commercemarketplace.adobe.com/freento-module-mcp.html)** (NEW) — available on the **Adobe Commerce Marketplace** since February 2026. Compatible with Adobe Commerce (cloud/on-prem) 2.4 and Magento Open Source 2.4. MIT license. Read-only tools for sales, catalog, customers with filtering, sorting, and aggregation. While not Adobe-built, marketplace listing signals ecosystem legitimacy
- **[elgentos/magento2-dev-mcp](https://github.com/elgentos/magento2-dev-mcp)** (36 stars, v1.0.2) — MCP server for Magento 2 development assistance, not store management. Actively maintained (last push March 2026)
- **[rafaelstz/adobe-commerce-dev-mcp](https://github.com/rafaelstz/adobe-commerce-dev-mcp)** (NEW, 25 stars) — dev-focused, helps with GraphQL schema understanding for Adobe Commerce

**Note:** Adobe has NOT shipped a first-party MCP server. Freento on the Marketplace is the closest thing to official backing.

---

## Amazon seller servers

Amazon seller MCP servers connect AI agents to Selling Partner API data — inventory, orders, listings, advertising, and analytics. The landscape splits between commercial products (Seller Labs), the **official Amazon Ads MCP** (now a major player with 50+ tools), and open-source community servers.

### The winner (analytics): Seller Labs MCP

**Type:** Commercial (SaaS) | **Auth:** Seller Labs account | **Access:** Read-only

[Seller Labs MCP](https://www.sellerlabs.com/amazon-mcp/) connects the Seller Labs Data Hub directly to Claude AI. The Data Hub collects, cleans, and structures Amazon data into 50+ detailed tables. Now included with Profit Genius and Genius Bundle plans (while in beta).

**Why it wins:** Production-grade data pipeline. Seller Labs has been in the Amazon tools space for years and has a deep understanding of seller data. Multi-account support makes it suitable for agencies. Natural-language queries like "Which ASINs lost Buy Box share last week?" return data-backed answers instantly.

**Key features:**
- **50+ data tables** — comprehensive Amazon business data
- **Natural-language analytics** — ask questions about your business in plain English
- **Multi-account support** — agencies and enterprise sellers with multiple stores
- **Read-only safety** — analyzes data but cannot take destructive actions
- **Claude integration** — designed specifically for Anthropic's Claude
- **Profit margin, FBA fees, inventory forecasts, review trends** — full business intelligence

**The catch:** Commercial product — requires a Seller Labs subscription. Read-only by design (can't create campaigns or change bids). Not open-source.

**Best for:** Serious Amazon sellers and agencies who want AI-powered business intelligence.

### The winner (advertising): Amazon Ads MCP Server (Official — MAJOR UPDATE)

**Status:** Open beta (since February 2, 2026) | **Auth:** Amazon Ads API credentials | **Tools:** 50+

[Amazon Ads MCP Server](https://advertising.amazon.com/) is Amazon's official MCP server for advertising campaign management. This was previously a brief mention in our guide — it has since launched into open beta as a major product with extensive coverage.

**Why it matters:** 50+ tools spanning **Sponsored Products, Sponsored Brands, Sponsored Display, DSP, and Amazon Marketing Cloud**. End-to-end campaign creation in a single prompt (normally 3+ operations). Geographic campaign expansion with one prompt. Works with Claude, ChatGPT, Gemini, and any MCP-compatible client. Available globally to Amazon Ads partners with active API credentials.

**Key capabilities:**
- **Campaign management** — create, modify, pause/resume campaigns across all ad types
- **Keyword and targeting** — bid optimization, keyword research, audience targeting
- **Reporting** — performance analytics, ACOS, ROAS, impression share
- **Amazon Marketing Cloud** — advanced audience analytics and attribution
- **DSP** — programmatic display and video ad management

**The catch:** Advertising only — no inventory, order, or catalog management. Requires active Amazon Ads API credentials. Still in beta.

**Best for:** Advertisers and agencies managing Amazon ad campaigns at scale.

### Also notable

- **[mattcoatsworth/AmazonSeller-mcp-server](https://github.com/mattcoatsworth/AmazonSeller-mcp-server)** (37 stars) — open-source SP-API integration covering catalog, inventory, orders, and reports. ⚠ No updates since April 2025
- **[jay-trivedi/amazon_sp_mcp](https://github.com/jay-trivedi/amazon_sp_mcp)** (7 stars) — Amazon Seller Central MCP for sales data, inventory, returns, and reports. Added Google Sheets integration for SKU-level cost data
- **[Fewsats/amazon-mcp](https://github.com/Fewsats/amazon-mcp)** — Amazon MCP for searching and buying products using L402 protocol (consumer-side, not seller)
- **[CDataSoftware/amazon-marketplace-mcp-server-by-cdata](https://github.com/CDataSoftware/amazon-marketplace-mcp-server-by-cdata)** (NEW) — read-only Amazon Marketplace data via CData JDBC
- **AWS Marketplace MCP Server** (NEW) — official AWS docs for marketplace integration
- **Zapier Amazon Seller Central MCP** — no-code integration connecting Seller Central to any MCP-compatible AI tool

**Note:** Amazon's new **Agent Policy** (effective March 4, 2026) governs how AI agents interact with Seller Central. Review compliance requirements before deploying any Amazon MCP integration.

---

## BigCommerce servers

BigCommerce is developing its own Storefront MCP, currently in closed beta. Third-party options exist but are limited.

### The winner: BigCommerce Storefront MCP (Beta)

**Status:** Closed beta | **Type:** Official

[BigCommerce Storefront MCP](https://www.bigcommerce.com/blog/model-context-protocol/) enables AI-powered commerce experiences, following Shopify's model. Combined with Google's Agent Development Kit (ADK), developers can build commerce-aware merchant agents.

**Why it wins:** Official platform support signals long-term commitment. Following the same storefront-first approach as Shopify suggests interoperability across the agentic commerce ecosystem.

**The catch:** Closed beta — not generally available yet. Limited documentation. Feature set not fully disclosed.

**Best for:** BigCommerce merchants who want to be early adopters of agentic commerce.

### Also notable

- **[CDataSoftware/bigcommerce-mcp-server-by-cdata](https://github.com/CDataSoftware/bigcommerce-mcp-server-by-cdata)** — read-only MCP server that lets LLMs query live BigCommerce data using natural language through CData JDBC Drivers
- **[isaacgounton/bigcommerce-api-mcp](https://github.com/isaacgounton/bigcommerce-api-mcp)** — community BigCommerce MCP server with products, customers, and orders management
- **Zapier BigCommerce MCP** — no-code integration for connecting BigCommerce to MCP-compatible AI tools

---

## Headless platform servers (Saleor, Medusa, PrestaShop)

Developer-first headless commerce platforms are shipping MCP servers that give AI agents direct access to their APIs. These are particularly interesting because the platforms themselves are designed for programmatic control.

### The winner (Saleor): saleor/saleor-mcp (Official)

**Stars:** 13 | **Language:** Python | **License:** — | **Transport:** Streamable HTTP | **Compatibility:** Saleor 3.21+ | **Latest:** v0.1.4 (Feb 2026)

[saleor/saleor-mcp](https://github.com/saleor/saleor-mcp) is the official MCP server for Saleor Commerce (21,800+ stars for the main platform). Production instance deployed at `mcp.saleor.app/mcp`.

**Why it wins:** Official, hosted, production-ready. The Saleor team maintains it alongside their platform. Streamable HTTP transport means remote access without local installation. Compatible with Saleor Cloud instances.

**Key features:**
- **Product browsing** — query and browse products with rich formatting
- **Order data** — retrieve order information and history
- **Customer data** — access customer records
- **Remote hosted** — production instance at `mcp.saleor.app/mcp`
- **Streamable HTTP** — modern transport protocol
- **Token-based auth** — requires MANAGE_PRODUCTS and MANAGE_ORDERS permissions

**The catch:** Read-only — no mutations. Cannot create products, process orders, or modify inventory. Limited to data retrieval and browsing.

**Security note:** Recent security patches for CVE-2026-32597 (PyJWT, March 16) and CVE-2026-28802 (authlib, March 5). The Saleor team is actively maintaining security.

**Best for:** Saleor users who want AI-powered data exploration and customer support tooling.

### The winner (Medusa): SGFGOV/medusa-mcp (PROMOTED)

**Stars:** 54 | **Forks:** 18 | **Language:** TypeScript | **Last pushed:** March 2026

[SGFGOV/medusa-mcp](https://github.com/SGFGOV/medusa-mcp) is now the dominant Medusa MCP server, surpassing minimalart/mcp-medusa in both stars and activity. Medusa (27,400+ stars for the main platform) positions itself as "A Commerce Platform for Developers and Agents."

**Why it wins:** Active development (Claude skills added March 12, 2026), broader scope than alternatives, and growing community (54 stars). Covers carts, payments, shipping, pricing, returns, and fulfillment automation via the Medusa JS SDK.

**Also notable (Medusa):**
- **[minimalart/mcp-medusa](https://github.com/minimalart/mcp-medusa)** — 14 comprehensive admin tools covering products, variants, categories, tags, orders, draft orders, and customers. ⚠ Dormant since December 2025 (1 star)
- **Medusa Docs MCP** — official docs server for AI-assisted Medusa development

### Also notable: PrestaShop MCP servers

PrestaShop is popular in Europe and Latin America, with a growing MCP ecosystem:

- **[GeorgesAdSim/prestashop-mcp-server](https://github.com/GeorgesAdSim/prestashop-mcp-server)** (NEW, created March 30, 2026) — manages products, categories, orders, customers, stock, CMS, and SEO. The newest and most comprehensive PrestaShop MCP
- **[latinogino/prestashop-mcp](https://github.com/latinogino/prestashop-mcp)** (9 stars) — professional MCP server for complete PrestaShop management. ⚠ Dormant since June 2025
- **[florinel-chis/prestashop-mcp](https://github.com/florinel-chis/prestashop-mcp)** (8 stars) — 1,095+ indexed documents for PrestaShop development documentation. Offline-first design
- **[belvg-public/belvg_mcp_extended](https://github.com/belvg-public/belvg_mcp_extended)** (NEW) — extends MCP server with Morning Briefing and Low Stock features

---

## Marketplace servers (eBay, Etsy) — NEW

Two of the biggest gaps from our March guide have been filled: both eBay and Etsy now have MCP servers.

### eBay: eBay/npm-public-api-mcp (Official)

**Stars:** 4 | **Created:** January 2026 | **Last pushed:** March 28, 2026

[eBay/npm-public-api-mcp](https://github.com/eBay/npm-public-api-mcp) is eBay's official MCP server. Integrates eBay APIs into AI assistant workflows; supports Claude Desktop, Cursor, and Cline.

**Why it matters:** eBay is one of the world's largest marketplaces, and this is the first official MCP integration. Low star count reflects early awareness, not quality.

**Also notable (eBay):**
- **[YosefHayim/ebay-mcp](https://github.com/YosefHayim/ebay-mcp)** (40 stars, 325 tools) — comprehensive community server covering Sell APIs (inventory, fulfillment, marketing, analytics). ⚠ **CVE-2026-27203** — environment variable injection vulnerability. Vet carefully before use
- **[CDataSoftware/ebay-mcp-server-by-cdata](https://github.com/CDataSoftware/ebay-mcp-server-by-cdata)** — read-only CData variant

### Etsy: Community servers emerging

No official Etsy MCP server yet, but multiple community options:

- **[aserper/etsy-mcp](https://github.com/aserper/etsy-mcp)** (NEW, created April 2, 2026) — 37 tools, ~70 API endpoints, OAuth 2.0 + PKCE, buyer + seller workflows. The most comprehensive option
- **[profplum700/etsy-mcp-server](https://github.com/profplum700/etsy-mcp-server)** (9 stars) — subset of Etsy API for shop data and listings
- **[administrativetrick/etsy-mcp-server](https://github.com/administrativetrick/etsy-mcp-server)** (3 stars) — Etsy API v3 integration

---

## Other platform servers (Square, Wix) — NEW

### Square: square/square-mcp-server (Official Beta)

**Stars:** 95 | **Forks:** 22 | **Last pushed:** February 2026

[square/square-mcp-server](https://github.com/square/square-mcp-server) is Square's official MCP server, currently in beta. Documented at developer.squareup.com/docs/mcp. Significant traction for a beta product (95 stars).

**Best for:** Square merchants who want AI-powered commerce operations.

### Wix: wix/wix-mcp (Official)

**Stars:** 10 | **Forks:** 9 | **Hosted:** mcp.wix.com/mcp

[wix/wix-mcp](https://github.com/wix/wix-mcp) is Wix's official MCP server. Search Wix docs, write code for Wix platform, and make API calls on Wix sites. Requires Node.js 19.9+.

**Best for:** Developers building on the Wix platform.

---

## Shipping and logistics servers — NEW

The first dedicated shipping MCP server has arrived, closing one of the biggest functional gaps in the e-commerce MCP ecosystem.

### The winner: Shippo MCP (Official)

**Package:** `@shippo/shippo-mcp` on npm | **Auth:** Shippo API key

[Shippo MCP](https://docs.goshippo.com/docs/guides_general/mcpserver/) is from GoShippo, self-described as "The First Agentic Shipping Platform." Multi-carrier support across USPS, UPS, FedEx, DHL, and more.

**Key features:**
- **Address validation** — verify shipping addresses before label creation
- **Rate shopping** — compare rates across carriers in real-time
- **Label generation** — create shipping labels programmatically
- **Returns management** — generate return labels
- **Customs documents** — international shipping documentation
- **Tracking** — real-time package tracking across carriers

**Also notable:**
- **[Shipi MCP](https://myshipi.com/mcp)** — commercial service with live rates, labels, tracking, and split shipping with DHL, FedEx, UPS, DPD, and Aramex

No standalone UPS-only, FedEx-only, or USPS-only MCP servers exist yet. Shippo and Shipi are the multi-carrier aggregators filling this space.

---

## Which e-commerce MCP server should you use?

**"I run a Shopify store and want AI shopping for my customers"** → **Shopify Storefront MCP** is already live on your store. No setup needed. Agentic Storefronts went live March 24 — your store is already discoverable in ChatGPT.

**"I want AI to manage my Shopify products, orders, and inventory"** → Use **GeLi2001/shopify-mcp** (181 stars, 31+ tools). Accept that it's community-maintained and may need updates when Shopify changes APIs.

**"I'm building apps on Shopify"** → Use **Shopify Dev MCP** (v1.7.0, 8 tools covering the full platform).

**"I run a WooCommerce store"** → Start with the **WooCommerce Native MCP** (beta in WooCommerce 10.3+) for official support. Alternatively, **techspawn/woocommerce-mcp-server** (84 stars) is the most popular community option.

**"I use Magento / Adobe Commerce"** → **boldcommerce/magento2-mcp** (54 stars) for store management. Check **Freento MCP** on the Adobe Commerce Marketplace for a read-only alternative.

**"I sell on Amazon"** → **Seller Labs MCP** for business analytics (commercial). **Amazon Ads MCP** for advertising (official, 50+ tools, open beta).

**"I sell on eBay"** → **eBay/npm-public-api-mcp** (official). For extensive seller tools, **YosefHayim/ebay-mcp** (325 tools) — but review CVE-2026-27203 first.

**"I sell on Etsy"** → **aserper/etsy-mcp** (37 tools, OAuth 2.0 + PKCE). Still very early — no official Etsy MCP yet.

**"I use Square"** → **square/square-mcp-server** (official beta, 95 stars).

**"I need shipping integration"** → **Shippo MCP** for multi-carrier rates, labels, and tracking.

**"I use a headless platform"** → **saleor/saleor-mcp** if you're on Saleor (hosted, official). **SGFGOV/medusa-mcp** (54 stars) if you're on Medusa.

**"I use BigCommerce"** → Join the **Storefront MCP beta** if you can. Otherwise, CData's read-only server or Zapier integration are your options.

---

## Four trends to watch

### 1. Agentic commerce is live at scale

Shopify's Agentic Storefronts went live March 24, 2026 — millions of merchants are now discoverable and shoppable inside ChatGPT with no integration work. Google AI Mode and Gemini are rolling out support. BigCommerce is still in beta. This is no longer a trend to watch; it's a shipping feature.

### 2. Official MCP servers are proliferating fast

Since our March update, the number of **official** e-commerce MCP servers has expanded dramatically: Shopify (5 servers), WooCommerce (native beta), eBay (official), Square (official beta), Wix (official), Amazon Ads (50+ tools in open beta), Shippo (shipping). The community-only era is ending — platforms are owning their MCP strategy.

### 3. The admin gap persists but is narrowing

Shopify still has no official Admin API MCP server. But WooCommerce now has native MCP (closing a major gap), and Shopify's Checkout MCP preview signals movement toward transactional operations. The first platform to ship comprehensive admin MCP — covering products, orders, inventory, fulfillment, and analytics in one official server — still gains a massive competitive advantage.

### 4. Universal Commerce Protocol (UCP) + security are shaping the ecosystem

Shopify and Google's UCP (endorsed by Etsy, Target, Walmart, Stripe, PayPal, and 20+ others) launched at NRF in January 2026. It standardizes checkout, identity linking (OAuth 2.0), and order management across platforms. Meanwhile, 30+ MCP CVEs in 60 days and e-commerce-adjacent vulnerabilities (CVE-2026-27203, CVE-2026-1926, Magento PolyShell) are forcing the ecosystem to take security seriously. Always vet community servers before connecting them to stores with real money.

---

## What's missing

The landscape has improved significantly since March 2026 — four of our previous "missing" items are now partially or fully addressed. But gaps remain:

**Gaps closed or closing:**
- ~~No official WooCommerce MCP~~ → **Native MCP beta in WooCommerce 10.3** (via WordPress Abilities API)
- ~~No eBay MCP~~ → **eBay/npm-public-api-mcp** (official) + community servers
- ~~No Etsy MCP~~ → Multiple community servers now available (aserper/etsy-mcp with 37 tools)
- ~~No shipping/logistics~~ → **Shippo MCP** (multi-carrier: USPS, UPS, FedEx, DHL) + Shipi

**Still missing:**
- **No official Shopify Admin MCP** — still the most impactful missing piece. Shopify has 5 official servers but none cover admin operations. Community servers (GeLi2001 at 181 stars) fill the gap
- **No official Magento/Adobe Commerce MCP** — Adobe hasn't shipped a first-party server. Freento on the Marketplace is the closest
- **No official Etsy MCP** — community servers exist but no official backing
- **No multi-platform management** — no server that unifies Shopify + Amazon + WooCommerce into a single interface. UCP could eventually enable this
- **No inventory sync** — no MCP server for cross-platform inventory synchronization
- **No product information management (PIM)** — Plytix MCP (47 tools for Plytix PIM) is the first entry, but no servers for Akeneo or Salsify
- **No returns/warranty management** — limited support across all platforms
- **No A/B testing or conversion optimization** — no MCP servers for tools like Optimizely in the commerce context
- **No Squarespace MCP** — still no official server from one of the largest site builders

The pattern is accelerating: platforms are now shipping official MCP servers faster than we can track them. The storefront-first approach (Shopify pioneered, others followed) is giving way to full-stack commerce MCP — advertising (Amazon), shipping (Shippo), payments (Stripe), and store management (WooCommerce) are all coming online.

---

*Last updated: April 2026. Star counts and feature details may have changed since publication. See our individual reviews for the most detailed analysis: [Shopify MCP Servers](/reviews/shopify-mcp-servers/) · [E-Commerce & Shopping MCP](/reviews/ecommerce-shopping-mcp-servers/)*

