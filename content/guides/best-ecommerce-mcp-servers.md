---
title: "Best E-Commerce MCP Servers in 2026"
date: 2026-04-05T18:00:00+09:00
description: "Shopify, WooCommerce, Magento, BigCommerce, Amazon, eBay, Etsy, Square, and headless platforms — we've reviewed 40+ e-commerce MCP servers across 10 categories. Here's what works, what's emerging, and where the gaps are."
og_description: "40+ e-commerce MCP servers reviewed across Shopify, WooCommerce, Magento, Amazon, eBay, Etsy, Square, BigCommerce, headless platforms, and marketplace tools. The definitive comparison with honest ratings."
content_type: "Comparison"
card_description: "The definitive guide to e-commerce MCP servers in 2026. We've reviewed 40+ servers across Shopify (5 official servers + community), WooCommerce (official, canonical abilities since 10.9), Magento/Adobe Commerce, Amazon (50+ tool Ads MCP), eBay (official), Etsy, Square (official), BigCommerce (official, GA), headless platforms (Saleor, Medusa), and shipping (Shippo). Every recommendation links to a full review."
last_refreshed: 2026-08-25
sources_audited: 2026-08-25
---

E-commerce MCP servers let AI agents interact with online stores — managing products, processing orders, searching catalogs, handling inventory, and powering AI-driven shopping experiences. Instead of clicking through admin dashboards or writing API calls manually, you describe what you want and the agent executes it against your store's backend.

We've researched 40+ e-commerce MCP servers across the full landscape. This guide synthesizes all of that into one page: what's worth using, what's not, and where the gaps are.

> **⚠ Security note:** The MCP ecosystem saw [30+ CVEs filed in 60 days in early 2026](https://www.heyuan110.com/posts/ai/2026-03-10-mcp-security-2026/). E-commerce-adjacent vulnerabilities include [CVE-2026-27203](https://nvd.nist.gov/vuln/detail/CVE-2026-27203) (environment variable injection in the community [YosefHayim/ebay-mcp](https://github.com/YosefHayim/ebay-mcp) server) and [CVE-2026-1926](https://nvd.nist.gov/vuln/detail/CVE-2026-1926) (auth bypass in the third-party "Subscriptions for WooCommerce" plugin, patched in v1.9.3). Always vet community servers before connecting them to production stores.

*Note: Our recommendations are based on documentation review, GitHub analysis, and community feedback — not hands-on testing of every server. Star counts were verified in August 2026.*

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| Shopify (storefront/shopping) | [Shopify Storefront MCP](https://shopify.dev/docs/apps/build/storefront-mcp/servers/storefront) | Official | [Shopify Catalog MCP](https://shopify.dev/docs/agents/catalog/mcp) (cross-merchant discovery) |
| Shopify (developer) | [Shopify Dev MCP](https://www.npmjs.com/package/@shopify/dev-mcp) | — | v1.14.5 on npm, full platform coverage |
| Shopify (admin/store management) | [GeLi2001/shopify-mcp](https://github.com/GeLi2001/shopify-mcp) | 236 | [trigga6006/shopify-mcp-server](https://github.com/trigga6006/shopify-mcp-server) (70+ tools) |
| WooCommerce | [WooCommerce Native MCP](https://developer.woocommerce.com/docs/features/mcp/) | Official (10.9+) | [techspawn/woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server) (101 stars) |
| Magento / Adobe Commerce | [boldcommerce/magento2-mcp](https://github.com/boldcommerce/magento2-mcp) | 59 | [Freento MCP](https://commercemarketplace.adobe.com/freento-module-mcp.html) (Adobe Marketplace) |
| Amazon (seller analytics) | [Seller Labs MCP](https://www.sellerlabs.com/amazon-mcp/) | — | [Amazon Ads MCP](https://advertising.amazon.com/) (official, 50+ tools) |
| Amazon (advertising) | [Amazon Ads MCP Server](https://advertising.amazon.com/) | Official | 50+ tools, still in open beta as of Aug 2026 |
| eBay | [eBay/npm-public-api-mcp](https://github.com/eBay/npm-public-api-mcp) | Official | [YosefHayim/ebay-mcp](https://github.com/YosefHayim/ebay-mcp) (131 stars, 325 tools) |
| Etsy | [aserper/etsy-mcp](https://github.com/aserper/etsy-mcp) | 3 | [profplum700/etsy-mcp-server](https://github.com/profplum700/etsy-mcp-server) (9 stars) |
| Square | [square/square-mcp-server](https://github.com/square/square-mcp-server) | 106 | Official beta |
| BigCommerce | [BigCommerce Storefront MCP](https://www.bigcommerce.com/blog/storefront-mcp/) | Official, GA | [CData BigCommerce MCP](https://github.com/CDataSoftware/bigcommerce-mcp-server-by-cdata) (read-only) |
| Headless (Saleor) | [saleor/saleor-mcp](https://github.com/saleor/saleor-mcp) | 16 | Official, hosted at mcp.saleor.app |
| Headless (Medusa) | [SGFGOV/medusa-mcp](https://github.com/SGFGOV/medusa-mcp) | 69 | [minimalart/mcp-medusa](https://github.com/minimalart/mcp-medusa) (14 admin tools) |
| Shipping | [Shippo MCP](https://docs.goshippo.com/docs/guides_general/mcpserver/) | Official | Multi-carrier: USPS, UPS, FedEx, DHL |

## Why e-commerce MCP servers matter

E-commerce operations involve repetitive, data-heavy tasks across multiple systems. MCP servers turn these into natural-language commands.

The value comes in three forms:

1. **Store management automation.** "Update the price of SKU-1234 to $29.99 and reduce inventory by 50" — instead of navigating to the product page, finding the variant, and making the change. At scale, agents can process bulk operations that would take hours manually.
2. **AI-powered shopping.** Shopify's Storefront MCP lets AI assistants like ChatGPT and Perplexity search products, manage carts, and initiate checkout directly. This is "agentic commerce" — customers shop through AI agents instead of browsing websites.
3. **Cross-platform analytics.** Ask "What was my best-selling product last month?" or "Which ASINs lost margin this week?" and get answers pulled directly from your store's live data.

The landscape now spans ten categories: **Shopify** (5 official servers plus community admin tools), **WooCommerce** (official, now on canonical MCP abilities since 10.9), **Magento/Adobe Commerce** (enterprise), **Amazon** (seller analytics + official Ads MCP), **eBay** (official MCP launched), **Etsy** (community servers), **Square** (official beta), **BigCommerce** (official, GA since May 2026), **headless platforms** (Saleor, Medusa, PrestaShop), and **shipping** (Shippo as first dedicated logistics MCP).

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
- **[Agentic Storefronts live (March 24, 2026)](https://shopify.com/news/agentic-commerce-momentum)** — millions of merchants now discoverable in ChatGPT
- **AI client integrations** — ChatGPT, Perplexity, Microsoft Copilot live; Google AI Mode and Gemini rolling out
- **MCP UI components** — remote resource URIs for interactive product cards, variant selection, bundles, subscriptions in sandboxed iframes

**The catch:** Storefront only. Cannot manage products, inventory, orders, or any admin functions. Read-plus-cart operations, not full store control.

**Best for:** Merchants who want AI agents to help customers shop. This is Shopify's "agentic commerce" play — and it's now live at scale.

### Also notable: Shopify Dev MCP

**Language:** TypeScript | **Tools:** 8 | **Latest:** [v1.14.5](https://www.npmjs.com/package/@shopify/dev-mcp) (published Aug 19, 2026)

[Shopify Dev MCP](https://www.npmjs.com/package/@shopify/dev-mcp) (`@shopify/dev-mcp`) is for developers building Shopify apps, not for managing stores. Winter '26 Edition expanded it to cover the **entire platform** — Admin, UI Extensions, Liquid, and Hydrogen. Infrastructure moved to server-side rendering. Also available via Gemini CLI and as an AI Agent Plugin. **Note:** the `Shopify/dev-mcp` GitHub repo now returns a 404 (source appears to have moved under Shopify's broader plugin tooling); the npm package itself remains actively published, so we've dropped the stale GitHub star count rather than repeat an unverifiable figure.

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

**Stars:** 236 | **Forks:** 117 | **Language:** TypeScript | **License:** — | **Tools:** 31+ | **Last pushed:** April 5, 2026

[GeLi2001/shopify-mcp](https://github.com/GeLi2001/shopify-mcp) is the most adopted community Shopify admin server. Comprehensive GraphQL Admin API integration covering products, customers, orders, metafields, inventory, and tags.

**Why it wins:** Most tools, most stars among community Shopify admin servers. Cursor-based pagination and Shopify query syntax pass-through on all list endpoints. Direct integration with the 2026-01 GraphQL Admin API version. **Update:** stars and forks kept growing through April 2026, but the repo has had no new commits since April 5, 2026 — over four months as of this audit — so "actively maintained" no longer holds; treat it as stable-but-unmaintained rather than under active development.

**Key features:**
- **Product management** — full CRUD for products, variants, and options (8 tools)
- **Customer management** — full CRUD, merge, and address management (8 tools)
- **Order management** — smart lookup, cancel, close/open, mark as paid, fulfillment, refunds (10 tools)
- **Metafield management** — get, set, and delete metafields on any resource (3 tools)
- **Inventory management** — set absolute inventory quantities at locations
- **Tag management** — add/remove tags on any taggable resource
- **Advanced filtering** — pass-through Shopify query syntax on all list endpoints

**The catch:** Community-maintained with 236 stars — the largest community Shopify admin server, but not battle-tested at scale, and now dormant since April 2026. No official Shopify backing means it could break when APIs change with no guarantee of a fix. Requires creating a custom Shopify app for authentication.

**Best for:** Solo merchants and small teams who want AI-powered store management today and accept the risks of community tooling.

### Also notable

- **[trigga6006/shopify-mcp-server](https://github.com/trigga6006/shopify-mcp-server)** — fork with GraphQL fixes and `updatePage` tool, 70+ tools covering all major store operations
- **[antoineschaller/shopify-mcp-server](https://github.com/antoineschaller/shopify-mcp-server)** — 22 tools covering products, orders, customers, inventory, analytics. ⚠ Dormant since August 2025
- **[amir-bengherbi/shopify-mcp-server](https://github.com/amir-bengherbi/shopify-mcp-server)** — similar scope with GraphQL Admin API integration

**Recommendation:** Use GeLi2001/shopify-mcp for admin operations. Pair it with Shopify Storefront MCP for the shopping layer, Catalog MCP for cross-merchant discovery, and Dev MCP for app development. Shopify now has five official servers — but none cover admin operations, so community tools remain essential for store management.

**Full review:** [Shopify MCP Servers](/reviews/shopify-mcp-servers/)

---

## WooCommerce servers

[WooCommerce powers roughly one-third of all online stores](https://barn2.com/blog/woocommerce-stats/) (estimates range from 32–38% depending on the measurement methodology). **The biggest news since our last audit: the original WooCommerce MCP beta is already being superseded.** [WooCommerce 10.9 (released June 23, 2026)](https://developer.woocommerce.com/2026/05/12/mcp-abilities-api-10-9/) replaced the REST-derived MCP bridge introduced in 10.3 with **canonical domain abilities** — a purpose-built semantic layer, not a wrapper around existing REST endpoints.

### The winner: WooCommerce Native MCP (Official — canonical abilities in 10.9+)

**Status:** Shipping in WooCommerce 10.9+ | **Auth:** WooCommerce REST API keys | **Transport:** Via WordPress MCP Adapter

[WooCommerce Native MCP](https://developer.woocommerce.com/docs/features/mcp/) is built into WooCommerce itself. The original 10.3 beta bridged MCP to existing REST endpoints; [WooCommerce 10.9](https://developer.woocommerce.com/2026/05/12/mcp-abilities-api-10-9/) replaced that with seven canonical abilities shipped in core — product query/create/update/delete plus order query, order-status update, and order note — exposed through the [WordPress/mcp-adapter](https://github.com/WordPress/mcp-adapter) plugin (now 1,614 stars). WooCommerce's own developer blog states plainly: "the WooCommerce-specific MCP endpoint and REST-derived WooCommerce abilities are deprecated transition surfaces," kept at `/wp-json/woocommerce/mcp` only for backward compatibility during the migration.

**Why it wins:** Official support from the WooCommerce team, now on a more durable architecture than the initial REST-shaped beta. Respects the existing permission system and REST API key authentication. Built on the WordPress Abilities API, which [shipped in WordPress Core with version 6.9](https://make.wordpress.org/core/2025/11/10/abilities-api-in-wordpress-6-9/) (not merely "moving into" it, as we said in our last update). No separate server to install — it's part of WooCommerce.

**Key features:**
- **Canonical domain abilities** — purpose-built product and order actions, not a REST-endpoint wrapper
- **WordPress Abilities API** — standardized capability exposure for AI agents, live in WP Core since 6.9
- **Existing permission model** — uses WooCommerce's REST API key auth
- **Extension abilities** — third-party plugins can register their own via the `woocommerce_ability_definition_classes` filter

**The catch:** The architecture changed twice in five months (10.3 → 10.9), so anything built against the original REST-derived beta needs migrating. Feature coverage (7 canonical abilities) is still narrower than mature community servers. Requires WooCommerce 10.9+ for the canonical abilities.

**Best for:** WooCommerce store owners who want official, supported MCP integration — build against the 10.9 canonical abilities, not the deprecated 10.3 bridge.

**Note:** The previous WordPress MCP server (Automattic/wordpress-mcp) was **archived on January 19, 2026** — all users should migrate to [WordPress/mcp-adapter](https://github.com/WordPress/mcp-adapter).

### Also notable

- **[techspawn/woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server)** (101 stars, 50 forks) — standalone Python MCP server via WooCommerce REST API. The most popular community option before the official integration. ⚠ No code updates since November 2025
- **[iOSDevSK/mcp-for-woocommerce](https://github.com/iOSDevSK/mcp-for-woocommerce)** — WordPress plugin approach with STDIO and HTTP Streamable transport, optional JWT authentication
- **[jlfguthrie/woo-mcp](https://github.com/jlfguthrie/woo-mcp)** — similar WordPress plugin approach with dual transport support. ⚠ Repo is now archived
- **[deus-h/claudeus-wp-mcp](https://github.com/deus-h/claudeus-wp-mcp)** — broader WordPress MCP that includes WooCommerce support
- **[newfold-labs/wp-module-mcp](https://github.com/newfold-labs/wp-module-mcp)** — Composer package exposing WordPress functionality through MCP, including WooCommerce
- **[CDataSoftware/woocommerce-mcp-server-by-cdata](https://github.com/CDataSoftware/woocommerce-mcp-server-by-cdata)** — read-only MCP via CData JDBC Drivers

**WooCommerce's MCP advantage:** Full ownership of the server and now official backing, on a purpose-built abilities architecture rather than a REST wrapper. The native integration means WooCommerce is closing the gap with Shopify's official MCP strategy.

---

## Magento / Adobe Commerce servers

Magento (now Adobe Commerce) is the enterprise e-commerce platform. MCP server options have expanded, with a third-party server now on the official Adobe Commerce Marketplace.

### The winner: boldcommerce/magento2-mcp

**Stars:** 59 | **Forks:** 24 | **Language:** Node.js | **License:** — | **Tools:** 6+

[boldcommerce/magento2-mcp](https://github.com/boldcommerce/magento2-mcp) by Bold Commerce connects to Magento 2's REST API, allowing MCP clients to query and manage store data.

**Why it wins:** Most adopted dedicated Magento 2 MCP server. Covers the essential commerce operations: products, customers, orders, and revenue analytics. Stars have more than doubled since our original count (27→59), though nearly all of that growth predates the repo going dormant — see below.

**Key features:**
- **Product management** — fetch by SKU or ID, search with filters, read categories, update attributes and prices
- **Stock information** — inventory data retrieval
- **Customer data** — retrieve customer information and ordered products
- **Order analytics** — order counts and revenue filtered by country and date ranges
- **REST API integration** — standard Magento 2 API token authentication

**The catch:** Read-heavy. Product attribute and price updates are supported, but order creation and fulfillment management are limited. ⚠ No code updates since April 2025 — now over a year and four months dormant.

**Best for:** Magento merchants who want AI-powered product and analytics queries.

### Also notable

- **[Freento MCP Server](https://commercemarketplace.adobe.com/freento-module-mcp.html)** (NEW) — available on the **Adobe Commerce Marketplace** since February 2026. Compatible with Adobe Commerce (cloud/on-prem) 2.4 and Magento Open Source 2.4. MIT license. Read-only tools for sales, catalog, customers with filtering, sorting, and aggregation. While not Adobe-built, marketplace listing signals ecosystem legitimacy
- **[elgentos/magento2-dev-mcp](https://github.com/elgentos/magento2-dev-mcp)** (40 stars, v1.0.2) — MCP server for Magento 2 development assistance, not store management. Actively maintained (last push April 2026)
- **[rafaelstz/adobe-commerce-dev-mcp](https://github.com/rafaelstz/adobe-commerce-dev-mcp)** (27 stars) — dev-focused, helps with GraphQL schema understanding for Adobe Commerce

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

**Status:** [Open beta (since February 2, 2026, still open beta as of this Aug 2026 audit)](https://advertising.amazon.com/library/news/amazon-ads-mcp-server-open-beta) | **Auth:** Amazon Ads API credentials | **Tools:** 50+

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

- **[mattcoatsworth/AmazonSeller-mcp-server](https://github.com/mattcoatsworth/AmazonSeller-mcp-server)** (43 stars) — open-source SP-API integration covering catalog, inventory, orders, and reports. ⚠ No updates since April 2025
- **[jay-trivedi/amazon_sp_mcp](https://github.com/jay-trivedi/amazon_sp_mcp)** (31 stars) — Amazon Seller Central MCP for sales data, inventory, returns, and reports. Added Google Sheets integration for SKU-level cost data
- **[Fewsats/amazon-mcp](https://github.com/Fewsats/amazon-mcp)** — Amazon MCP for searching and buying products using L402 protocol (consumer-side, not seller). ⚠ **Repo is now archived**
- **[CDataSoftware/amazon-marketplace-mcp-server-by-cdata](https://github.com/CDataSoftware/amazon-marketplace-mcp-server-by-cdata)** (NEW) — read-only Amazon Marketplace data via CData JDBC
- **AWS Marketplace MCP Server** (NEW) — official AWS docs for marketplace integration
- **Zapier Amazon Seller Central MCP** — no-code integration connecting Seller Central to any MCP-compatible AI tool

**Note:** Amazon's new [**Agent Policy**](https://ppc.land/amazons-new-ai-agent-rules-shake-up-sellers-before-march-4-deadline/) (part of the Business Solutions Agreement, effective March 4, 2026) requires AI seller agents to identify themselves as automated and to operate through a registered SP-API application tied to a verified developer account. Review compliance requirements before deploying any Amazon MCP integration.

---

## BigCommerce servers

**Update since our last audit: BigCommerce Storefront MCP moved from closed beta to general availability.** [As of May 11, 2026](https://www.bigcommerce.com/blog/storefront-mcp/), "BigCommerce Storefront MCP is now available to every store on the platform. Any live, transacting store can opt in starting now" — enabled via Settings → Early Access in the control panel.

### The winner: BigCommerce Storefront MCP (Official, GA)

**Status:** Generally available to all live, transacting stores (since May 11, 2026) | **Type:** Official

[BigCommerce Storefront MCP](https://www.bigcommerce.com/blog/storefront-mcp/) enables AI-powered commerce experiences, following Shopify's model. It supports catalog search, product/variant details, cart building, and generating checkout URLs for guest shopping flows; authenticated shopping (personalized pricing, order history) is a listed forthcoming enhancement, not yet available. Combined with Google's Agent Development Kit (ADK), developers can build commerce-aware merchant agents.

**Why it wins:** Official platform support, now shipped to every store rather than a limited beta cohort. Following the same storefront-first approach as Shopify suggests interoperability across the agentic commerce ecosystem.

**The catch:** Guest checkout only for now — authenticated/personalized shopping isn't live yet. No admin/store-management coverage (storefront only, same limitation as Shopify's equivalent).

**Best for:** BigCommerce merchants who want AI agents to help customers browse, build carts, and check out as guests.

### Also notable

- **[CDataSoftware/bigcommerce-mcp-server-by-cdata](https://github.com/CDataSoftware/bigcommerce-mcp-server-by-cdata)** — read-only MCP server that lets LLMs query live BigCommerce data using natural language through CData JDBC Drivers
- **[etugrand/bigcommerce-api-mcp](https://github.com/etugrand/bigcommerce-api-mcp)** — community BigCommerce MCP server with products, customers, and orders management (repo moved from isaacgounton/bigcommerce-api-mcp; 5 stars)
- **Zapier BigCommerce MCP** — no-code integration for connecting BigCommerce to MCP-compatible AI tools

---

## Headless platform servers (Saleor, Medusa, PrestaShop)

Developer-first headless commerce platforms are shipping MCP servers that give AI agents direct access to their APIs. These are particularly interesting because the platforms themselves are designed for programmatic control.

### The winner (Saleor): saleor/saleor-mcp (Official)

**Stars:** 16 | **Language:** Python | **License:** — | **Transport:** Streamable HTTP | **Compatibility:** Saleor 3.21+

[saleor/saleor-mcp](https://github.com/saleor/saleor-mcp) is the official MCP server for [Saleor Commerce (23,000+ stars)](https://github.com/saleor/saleor) for the main platform. Production instance deployed at `mcp.saleor.app/mcp`. Actively maintained — last pushed July 22, 2026.

**Why it wins:** Official, hosted, production-ready. The Saleor team maintains it alongside their platform. Streamable HTTP transport means remote access without local installation. Compatible with Saleor Cloud instances.

**Key features:**
- **Product browsing** — query and browse products with rich formatting
- **Order data** — retrieve order information and history
- **Customer data** — access customer records
- **Remote hosted** — production instance at `mcp.saleor.app/mcp`
- **Streamable HTTP** — modern transport protocol
- **Token-based auth** — requires MANAGE_PRODUCTS and MANAGE_ORDERS permissions

**The catch:** Read-only — no mutations. Cannot create products, process orders, or modify inventory. Limited to data retrieval and browsing.

**Security note:** Saleor shipped upgrades addressing [CVE-2026-32597](https://nvd.nist.gov/vuln/detail/CVE-2026-32597) (a PyJWT flaw where unrecognized `crit` header extensions were incorrectly accepted) and [CVE-2026-28802](https://nvd.nist.gov/vuln/detail/CVE-2026-28802) (an Authlib JWT signature-verification bypass via `alg:none`, affecting Authlib 1.6.5–1.6.6). Both are upstream dependency CVEs, not Saleor-specific flaws, and the Saleor team patched by upgrading the affected libraries.

**Best for:** Saleor users who want AI-powered data exploration and customer support tooling.

### The winner (Medusa): SGFGOV/medusa-mcp (PROMOTED)

**Stars:** 69 | **Forks:** 21 | **Language:** TypeScript | **Last pushed:** April 2026

[SGFGOV/medusa-mcp](https://github.com/SGFGOV/medusa-mcp) is now the dominant Medusa MCP server by star count. [Medusa (35,000+ stars for the main platform)](https://github.com/medusajs/medusa) positions itself as "A Commerce Platform for Developers and Agents."

**Why it wins:** Broader scope than alternatives (carts, payments, shipping, pricing, returns, and fulfillment automation via the Medusa JS SDK) and the larger community of the two options (69 stars vs. 4).

**Also notable (Medusa):**
- **[minimalart/mcp-medusa](https://github.com/minimalart/mcp-medusa)** — 14 comprehensive admin tools covering products, variants, categories, tags, orders, draft orders, and customers. **Correction:** our previous audit called this "dormant since December 2025," but the repo was pushed as recently as July 17, 2026 — it's smaller (4 stars) but still active, not dormant
- **Medusa Docs MCP** — official docs server for AI-assisted Medusa development

### Also notable: PrestaShop MCP servers

PrestaShop is popular in Europe and Latin America, with a growing MCP ecosystem:

- **[GeorgesAdSim/prestashop-mcp-server](https://github.com/GeorgesAdSim/prestashop-mcp-server)** (NEW, created March 30, 2026) — manages products, categories, orders, customers, stock, CMS, and SEO. The newest and most comprehensive PrestaShop MCP
- **[latinogino/prestashop-mcp](https://github.com/latinogino/prestashop-mcp)** (8 stars) — professional MCP server for complete PrestaShop management. ⚠ Dormant since June 2025
- **[florinel-chis/prestashop-mcp](https://github.com/florinel-chis/prestashop-mcp)** (8 stars) — 1,095+ indexed documents for PrestaShop development documentation. Offline-first design
- **[belvg-public/belvg_mcp_extended](https://github.com/belvg-public/belvg_mcp_extended)** (NEW) — extends MCP server with Morning Briefing and Low Stock features

---

## Marketplace servers (eBay, Etsy) — NEW

Two of the biggest gaps from our March guide have been filled: both eBay and Etsy now have MCP servers.

### eBay: eBay/npm-public-api-mcp (Official)

**Stars:** 15 | **Created:** January 2026 | **Last pushed:** August 14, 2026

[eBay/npm-public-api-mcp](https://github.com/eBay/npm-public-api-mcp) is eBay's official MCP server. Integrates eBay APIs into AI assistant workflows; supports Claude Desktop, Cursor, and Cline.

**Why it matters:** eBay is one of the world's largest marketplaces, and this is the first official MCP integration. Stars nearly quadrupled since our last audit (4→15), and it's still being actively pushed as recently as mid-August 2026.

**Also notable (eBay):**
- **[YosefHayim/ebay-mcp](https://github.com/YosefHayim/ebay-mcp)** (131 stars, 57 forks) — comprehensive community server covering Sell APIs (inventory, fulfillment, marketing, analytics). Stars more than tripled since our last audit. ⚠ **[CVE-2026-27203](https://nvd.nist.gov/vuln/detail/CVE-2026-27203)** — environment variable injection vulnerability in the `ebay_set_user_tokens` tool, disclosed Feb 21, 2026, affecting versions through 1.7.2 ([details](https://www.miggo.io/vulnerability-database/cve/CVE-2026-27203)). Confirm you're on a patched release before use
- **[CDataSoftware/ebay-mcp-server-by-cdata](https://github.com/CDataSoftware/ebay-mcp-server-by-cdata)** — read-only CData variant

### Etsy: Community servers emerging

No official Etsy MCP server yet, but multiple community options:

- **[aserper/etsy-mcp](https://github.com/aserper/etsy-mcp)** (3 stars, created April 2, 2026) — 37 tools, ~70 API endpoints, OAuth 2.0 + PKCE, buyer + seller workflows. The most comprehensive option
- **[profplum700/etsy-mcp-server](https://github.com/profplum700/etsy-mcp-server)** (9 stars) — subset of Etsy API for shop data and listings
- **[administrativetrick/etsy-mcp-server](https://github.com/administrativetrick/etsy-mcp-server)** (13 stars) — Etsy API v3 integration

---

## Other platform servers (Square, Wix) — NEW

### Square: square/square-mcp-server (Official Beta)

**Stars:** 106 | **Forks:** 26 | **Last pushed:** April 2026

[square/square-mcp-server](https://github.com/square/square-mcp-server) is Square's official MCP server, currently in beta, also hosted as a remote server at `mcp.squareup.com/sse`. Documented at developer.squareup.com/docs/mcp. Significant traction for a beta product (106 stars).

**Best for:** Square merchants who want AI-powered commerce operations.

### Wix: wix/wix-mcp (Official)

**Stars:** 16 | **Forks:** 12 | **Hosted:** mcp.wix.com/mcp

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

**"I want AI to manage my Shopify products, orders, and inventory"** → Use **GeLi2001/shopify-mcp** (236 stars, 31+ tools). Accept that it's community-maintained, now dormant since April 2026, and may need updates when Shopify changes APIs.

**"I'm building apps on Shopify"** → Use **Shopify Dev MCP** (v1.14.5, 8 tools covering the full platform).

**"I run a WooCommerce store"** → Start with the **WooCommerce Native MCP** — build against the canonical abilities shipped in **WooCommerce 10.9+**, not the deprecated 10.3 REST bridge. Alternatively, **techspawn/woocommerce-mcp-server** (101 stars) is the most popular community option.

**"I use Magento / Adobe Commerce"** → **boldcommerce/magento2-mcp** (59 stars, dormant since April 2025) for store management. Check **Freento MCP** on the Adobe Commerce Marketplace for a read-only alternative.

**"I sell on Amazon"** → **Seller Labs MCP** for business analytics (commercial). **Amazon Ads MCP** for advertising (official, 50+ tools, still open beta as of Aug 2026).

**"I sell on eBay"** → **eBay/npm-public-api-mcp** (official). For extensive seller tools, **YosefHayim/ebay-mcp** (325 tools) — but review CVE-2026-27203 first.

**"I sell on Etsy"** → **aserper/etsy-mcp** (37 tools, OAuth 2.0 + PKCE). Still very early — no official Etsy MCP yet.

**"I use Square"** → **square/square-mcp-server** (official beta, 106 stars).

**"I need shipping integration"** → **Shippo MCP** for multi-carrier rates, labels, and tracking.

**"I use a headless platform"** → **saleor/saleor-mcp** if you're on Saleor (hosted, official). **SGFGOV/medusa-mcp** (69 stars) if you're on Medusa.

**"I use BigCommerce"** → **Storefront MCP is now GA** — enable it from Settings → Early Access. Otherwise, CData's read-only server or Zapier integration are your options for admin-side data.

---

## Four trends to watch

### 1. Agentic commerce is live at scale

[Shopify's Agentic Storefronts went live March 24, 2026](https://shopify.com/news/agentic-commerce-momentum) — millions of merchants are now discoverable and shoppable inside ChatGPT with no integration work. Google AI Mode and Gemini are rolling out support. [BigCommerce's Storefront MCP reached general availability on May 11, 2026](https://www.bigcommerce.com/blog/storefront-mcp/). This is no longer a trend to watch; it's a shipping feature.

### 2. Official MCP servers are proliferating fast

Since our original guide, the number of **official** e-commerce MCP servers has expanded dramatically: Shopify (5 servers), WooCommerce (native, now on canonical abilities in 10.9+), BigCommerce (GA since May 2026), eBay (official), Square (official beta), Wix (official), Amazon Ads (50+ tools in open beta), Shippo (shipping). The community-only era is ending — platforms are owning their MCP strategy.

### 3. The admin gap persists but is narrowing

Shopify still has no official Admin API MCP server. But WooCommerce now has native MCP (closing a major gap), and Shopify's Checkout MCP is [still in preview with select partner agents as of mid-2026, with general availability expected in H2 2026](https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp) as part of the UCP rollout. The first platform to ship comprehensive admin MCP — covering products, orders, inventory, fulfillment, and analytics in one official server — still gains a massive competitive advantage.

### 4. Universal Commerce Protocol (UCP) + security are shaping the ecosystem

[Google's UCP, co-developed with Shopify, Etsy, Wayfair, Target, and Walmart and backed by 20+ additional retailers/payment processors (including Stripe), launched January 11, 2026 at NRF](https://shopify.com/news/agentic-commerce-momentum). It standardizes checkout, identity linking (OAuth 2.0), and order management across platforms. Meanwhile, [30+ MCP CVEs in 60 days](https://www.heyuan110.com/posts/ai/2026-03-10-mcp-security-2026/) and e-commerce-adjacent vulnerabilities ([CVE-2026-27203](https://nvd.nist.gov/vuln/detail/CVE-2026-27203), [CVE-2026-1926](https://nvd.nist.gov/vuln/detail/CVE-2026-1926), and the [Magento "PolyShell" unauthenticated file-upload flaw](https://thehackernews.com/2026/03/magento-polyshell-flaw-enables.html) affecting every production Magento/Adobe Commerce version through 2.4.9-alpha2) are forcing the ecosystem to take security seriously. Always vet community servers before connecting them to stores with real money.

---

## What's missing

The landscape has improved significantly since our original guide — five of our previous "missing" items are now partially or fully addressed. But gaps remain:

**Gaps closed or closing:**
- ~~No official WooCommerce MCP~~ → **Native MCP, now on canonical abilities in WooCommerce 10.9+** (via WordPress Abilities API, which shipped in WP Core 6.9)
- ~~BigCommerce Storefront MCP in closed beta~~ → **GA to all stores since May 11, 2026**
- ~~No eBay MCP~~ → **eBay/npm-public-api-mcp** (official) + community servers
- ~~No Etsy MCP~~ → Multiple community servers now available (aserper/etsy-mcp with 37 tools)
- ~~No shipping/logistics~~ → **Shippo MCP** (multi-carrier: USPS, UPS, FedEx, DHL) + Shipi

**Still missing:**
- **No official Shopify Admin MCP** — still the most impactful missing piece. Shopify has 5 official servers but none cover admin operations. Community servers (GeLi2001 at 236 stars) fill the gap
- **No official Magento/Adobe Commerce MCP** — Adobe hasn't shipped a first-party server. Freento on the Marketplace is the closest
- **No official Etsy MCP** — community servers exist but no official backing
- **No multi-platform management** — no server that unifies Shopify + Amazon + WooCommerce into a single interface. UCP could eventually enable this
- **No inventory sync** — no MCP server for cross-platform inventory synchronization
- **No product information management (PIM)** — [Supplyline/plytix-mcp](https://github.com/Supplyline/plytix-mcp) (46-51 tools depending on transport, for Plytix PIM) is the first entry, but no servers for Akeneo or Salsify
- **No returns/warranty management** — limited support across all platforms
- **No A/B testing or conversion optimization** — no MCP servers for tools like Optimizely in the commerce context
- **No Squarespace MCP** — still no official server from one of the largest site builders

The pattern is accelerating: platforms are now shipping official MCP servers faster than we can track them. The storefront-first approach (Shopify pioneered, others followed) is giving way to full-stack commerce MCP — advertising (Amazon), shipping (Shippo), payments (Stripe), and store management (WooCommerce) are all coming online.

---

*Last fact-checked: August 2026. Star counts and feature details may have changed since publication. See our individual reviews for the most detailed analysis: [Shopify MCP Servers](/reviews/shopify-mcp-servers/) · [E-Commerce & Shopping MCP](/reviews/ecommerce-shopping-mcp-servers/)*
