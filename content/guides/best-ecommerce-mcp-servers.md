---
title: "Best E-Commerce MCP Servers in 2026"
date: 2026-03-22T15:30:00+09:00
description: "Shopify, WooCommerce, Magento, BigCommerce, Amazon, and headless platforms — we've reviewed 30+ e-commerce MCP servers across 7 categories. Here's what works, what's emerging, and where the gaps are."
og_description: "30+ e-commerce MCP servers reviewed across Shopify, WooCommerce, Magento, Amazon, BigCommerce, headless platforms, and marketplace tools. The definitive comparison with honest ratings."
content_type: "Comparison"
card_description: "The definitive guide to e-commerce MCP servers in 2026. We've reviewed 30+ servers across Shopify (official + community), WooCommerce, Magento/Adobe Commerce, Amazon seller tools, BigCommerce, headless platforms (Saleor, Medusa), and marketplace aggregators. Every recommendation links to a full review."
---

E-commerce MCP servers let AI agents interact with online stores — managing products, processing orders, searching catalogs, handling inventory, and powering AI-driven shopping experiences. Instead of clicking through admin dashboards or writing API calls manually, you describe what you want and the agent executes it against your store's backend.

We've researched 30+ e-commerce MCP servers across the full landscape. This guide synthesizes all of that into one page: what's worth using, what's not, and where the gaps are.

*Note: Our recommendations are based on documentation review, GitHub analysis, and community feedback — not hands-on testing of every server. Star counts were verified in March 2026.*

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| Shopify (storefront/shopping) | [Shopify Storefront MCP](https://shopify.dev/docs/apps/build/storefront-mcp/servers/storefront) | Official | [Shopify Dev MCP](https://github.com/Shopify/dev-mcp) (414 stars, developer docs) |
| Shopify (admin/store management) | [GeLi2001/shopify-mcp](https://github.com/GeLi2001/shopify-mcp) | 139 | [antoineschaller/shopify-mcp-server](https://github.com/antoineschaller/shopify-mcp-server) (22 tools) |
| WooCommerce | [techspawn/woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server) | 26 | [iOSDevSK/mcp-for-woocommerce](https://github.com/iOSDevSK/mcp-for-woocommerce) (WordPress plugin) |
| Magento / Adobe Commerce | [boldcommerce/magento2-mcp](https://github.com/boldcommerce/magento2-mcp) | 27+ | [elgentos/magento2-dev-mcp](https://github.com/elgentos/magento2-dev-mcp) (dev assistant) |
| Amazon (seller) | [Seller Labs MCP](https://www.sellerlabs.com/amazon-mcp/) | — | [mattcoatsworth/AmazonSeller-mcp-server](https://github.com/mattcoatsworth/AmazonSeller-mcp-server) (SP-API) |
| BigCommerce | [BigCommerce Storefront MCP](https://www.bigcommerce.com/blog/model-context-protocol/) | Beta | [CData BigCommerce MCP](https://github.com/CDataSoftware/bigcommerce-mcp-server-by-cdata) (read-only) |
| Headless (Saleor/Medusa) | [saleor/saleor-mcp](https://github.com/saleor/saleor-mcp) | Official | [minimalart/mcp-medusa](https://github.com/minimalart/mcp-medusa) (14 admin tools) |

## Why e-commerce MCP servers matter

E-commerce operations involve repetitive, data-heavy tasks across multiple systems. MCP servers turn these into natural-language commands.

The value comes in three forms:

1. **Store management automation.** "Update the price of SKU-1234 to $29.99 and reduce inventory by 50" — instead of navigating to the product page, finding the variant, and making the change. At scale, agents can process bulk operations that would take hours manually.
2. **AI-powered shopping.** Shopify's Storefront MCP lets AI assistants like ChatGPT and Perplexity search products, manage carts, and initiate checkout directly. This is "agentic commerce" — customers shop through AI agents instead of browsing websites.
3. **Cross-platform analytics.** Ask "What was my best-selling product last month?" or "Which ASINs lost margin this week?" and get answers pulled directly from your store's live data.

The landscape splits into seven categories: **Shopify storefront** (official AI shopping layer), **Shopify admin** (community store management), **WooCommerce** (WordPress-based stores), **Magento/Adobe Commerce** (enterprise), **Amazon** (seller tools), **BigCommerce** (emerging), and **headless platforms** (Saleor, Medusa, and other developer-first commerce backends).

---

## Shopify storefront servers (official)

Shopify is the clear leader in e-commerce MCP adoption. They've shipped two official servers — one for shopping, one for development — and the ecosystem has dozens of community servers filling the admin gap.

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

**The catch:** Storefront only. Cannot manage products, inventory, orders, or any admin functions. Read-plus-cart operations, not full store control.

**Best for:** Merchants who want AI agents to help customers shop. This is Shopify's "agentic commerce" play.

### Also notable: Shopify Dev MCP

**Stars:** 414 | **Language:** TypeScript | **License:** — | **Tools:** 4

[Shopify Dev MCP](https://github.com/Shopify/dev-mcp) (`@shopify/dev-mcp`) is for developers building Shopify apps, not for managing stores. It provides docs search, GraphQL schema introspection, code validation, and theme validation. Zero config, no API key needed.

**Key tools:** `search_dev_docs`, `introspect_admin_schema`, `fetch_docs_by_path`, `get_started`

**Best for:** Developers building Shopify apps or themes who want AI-assisted development with validated Shopify API knowledge.

---

## Shopify admin servers (community)

The biggest gap in Shopify's MCP story: **no official Admin API MCP server**. For managing products, orders, inventory, customers, and fulfillment, you need community servers. Several exist, but adoption is still early.

### The winner: GeLi2001/shopify-mcp

**Stars:** 139 | **Forks:** — | **Language:** TypeScript | **License:** — | **Tools:** 31+

[GeLi2001/shopify-mcp](https://github.com/GeLi2001/shopify-mcp) is the most adopted community Shopify admin server. Comprehensive GraphQL Admin API integration covering products, customers, orders, metafields, inventory, and tags.

**Why it wins:** Most tools, most stars, active maintenance. Cursor-based pagination and Shopify query syntax pass-through on all list endpoints. Direct integration with the 2026-01 GraphQL Admin API version.

**Key features:**
- **Product management** — full CRUD for products, variants, and options (8 tools)
- **Customer management** — full CRUD, merge, and address management (8 tools)
- **Order management** — smart lookup, cancel, close/open, mark as paid, fulfillment, refunds (10 tools)
- **Metafield management** — get, set, and delete metafields on any resource (3 tools)
- **Inventory management** — set absolute inventory quantities at locations
- **Tag management** — add/remove tags on any taggable resource
- **Advanced filtering** — pass-through Shopify query syntax on all list endpoints

**The catch:** Community-maintained with 139 stars — not battle-tested at scale. No official Shopify backing means it could break when APIs change. Requires creating a custom Shopify app for authentication.

**Best for:** Solo merchants and small teams who want AI-powered store management today and accept the risks of community tooling.

### Also notable

- **[antoineschaller/shopify-mcp-server](https://github.com/antoineschaller/shopify-mcp-server)** — 22 tools covering products, orders, customers, inventory, analytics. Lower star count but clean implementation
- **[amir-bengherbi/shopify-mcp-server](https://github.com/amir-bengherbi/shopify-mcp-server)** — similar scope with GraphQL Admin API integration
- **[trigga6006/shopify-mcp-server](https://github.com/trigga6006/shopify-mcp-server)** — fork with GraphQL fixes and `updatePage` tool, 70+ tools covering all major store operations

**Recommendation:** Use GeLi2001/shopify-mcp for admin operations. Pair it with Shopify Storefront MCP for the shopping layer and Dev MCP for app development. This three-server combo covers most use cases — but an official Admin MCP from Shopify would instantly obsolete the community options.

**Full review:** [Shopify MCP Servers](/reviews/shopify-mcp-servers/)

---

## WooCommerce servers

WooCommerce powers ~36% of all online stores via WordPress. The MCP ecosystem is smaller than Shopify's but growing, with both standalone servers and WordPress plugin approaches.

### The winner: techspawn/woocommerce-mcp-server

**Stars:** 26 | **Forks:** 15 | **Language:** Python | **License:** — | **Tools:** 7+

[techspawn/woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server) provides WooCommerce store management through the WordPress REST API. Built with FastMCP framework.

**Why it wins:** Most complete standalone WooCommerce MCP implementation. Covers the core operations that store owners need: products, orders, customers, shipping, taxes, discounts, and inventory.

**Key features:**
- **Product management** — list, search, and update products
- **Order management** — list, get, update status, add notes
- **Inventory tracking** — manage stock levels
- **Customer data** — customer information and history
- **JSON-RPC 2.0 protocol** — standard MCP communication
- **WooCommerce REST API** — uses consumer key authentication

**The catch:** 26 stars — very early adoption. Fewer tools than the Shopify community servers. Python-based, which may not fit all WordPress deployment environments.

**Best for:** WooCommerce store owners who want basic AI-powered store management.

### Also notable

- **[iOSDevSK/mcp-for-woocommerce](https://github.com/iOSDevSK/mcp-for-woocommerce)** — WordPress plugin approach with STDIO and HTTP Streamable transport, optional JWT authentication. Based on Automattic's official WordPress MCP
- **[jlfguthrie/woo-mcp](https://github.com/jlfguthrie/woo-mcp)** — similar WordPress plugin approach with dual transport support
- **[brucealdridge/wc-mcp](https://github.com/brucealdridge/wc-mcp)** — exploration of WooCommerce tools for LLMs and agents
- **[deus-h/claudeus-wp-mcp](https://github.com/deus-h/claudeus-wp-mcp)** — broader WordPress MCP that includes WooCommerce support
- **[newfold-labs/wp-module-mcp](https://github.com/newfold-labs/wp-module-mcp)** — Composer package exposing WordPress functionality through MCP, including WooCommerce

**WooCommerce's MCP advantage:** Full ownership of the server. For brands building proprietary AI models, customizing how the server interacts with an LLM is a competitive advantage that hosted platforms like Shopify can't match.

---

## Magento / Adobe Commerce servers

Magento (now Adobe Commerce) is the enterprise e-commerce platform. MCP server options are limited but functional.

### The winner: boldcommerce/magento2-mcp

**Stars:** 27+ | **Language:** Node.js | **License:** — | **Tools:** 6+

[boldcommerce/magento2-mcp](https://github.com/boldcommerce/magento2-mcp) by Bold Commerce connects to Magento 2's REST API, allowing MCP clients to query and manage store data.

**Why it wins:** Only dedicated Magento 2 MCP server with meaningful adoption. Covers the essential commerce operations: products, customers, orders, and revenue analytics.

**Key features:**
- **Product management** — fetch by SKU or ID, search with filters, read categories, update attributes and prices
- **Stock information** — inventory data retrieval
- **Customer data** — retrieve customer information and ordered products
- **Order analytics** — order counts and revenue filtered by country and date ranges
- **REST API integration** — standard Magento 2 API token authentication

**The catch:** Read-heavy. Product attribute and price updates are supported, but order creation and fulfillment management are limited. 27 stars means very small community.

**Best for:** Magento merchants who want AI-powered product and analytics queries.

### Also notable

- **[elgentos/magento2-dev-mcp](https://github.com/elgentos/magento2-dev-mcp)** — MCP server for Magento 2 development assistance, not store management

---

## Amazon seller servers

Amazon seller MCP servers connect AI agents to Selling Partner API data — inventory, orders, listings, advertising, and analytics. The landscape splits between commercial products (Seller Labs) and open-source community servers.

### The winner: Seller Labs MCP

**Type:** Commercial (SaaS) | **Auth:** Seller Labs account | **Access:** Read-only

[Seller Labs MCP](https://www.sellerlabs.com/amazon-mcp/) connects the Seller Labs Data Hub directly to Claude AI. The Data Hub collects, cleans, and structures Amazon data into 50+ detailed tables.

**Why it wins:** Production-grade data pipeline. Seller Labs has been in the Amazon tools space for years and has a deep understanding of seller data. Multi-account support makes it suitable for agencies. Natural-language queries like "Which ASINs lost Buy Box share last week?" return data-backed answers instantly.

**Key features:**
- **50+ data tables** — comprehensive Amazon business data
- **Natural-language analytics** — ask questions about your business in plain English
- **Multi-account support** — agencies and enterprise sellers with multiple stores
- **Read-only safety** — analyzes data but cannot take destructive actions
- **Claude integration** — designed specifically for Anthropic's Claude

**The catch:** Commercial product — requires a Seller Labs subscription. Read-only by design (can't create campaigns or change bids). Not open-source.

**Best for:** Serious Amazon sellers and agencies who want AI-powered business intelligence.

### Also notable

- **[mattcoatsworth/AmazonSeller-mcp-server](https://github.com/mattcoatsworth/AmazonSeller-mcp-server)** — open-source SP-API integration covering catalog, inventory, orders, and reports. Requires Amazon SP-API credentials
- **[jay-trivedi/amazon_sp_mcp](https://github.com/jay-trivedi/amazon_sp_mcp)** — Amazon Seller Central MCP for sales data, inventory, returns, and reports
- **[Fewsats/amazon-mcp](https://github.com/Fewsats/amazon-mcp)** — Amazon MCP for searching and buying products using L402 protocol (consumer-side, not seller)
- **Amazon Ads MCP Server** — official Amazon server for ad campaign management. AI tools can plug directly into your ad account
- **Zapier Amazon Seller Central MCP** — no-code integration connecting Seller Central to any MCP-compatible AI tool

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

### The winner: saleor/saleor-mcp (Official)

**Language:** — | **License:** — | **Transport:** Streamable HTTP | **Compatibility:** Saleor 3.21+

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

**Best for:** Saleor users who want AI-powered data exploration and customer support tooling.

### Also notable: Medusa MCP servers

Medusa (27,400+ stars for the main platform) positions itself as "A Commerce Platform for Developers and Agents" — MCP is part of their core story.

- **[minimalart/mcp-medusa](https://github.com/minimalart/mcp-medusa)** — 14 comprehensive admin tools covering products, variants, categories, tags, types, orders (list, get, cancel, complete, archive, transfer, fulfillment), draft orders, and customers. The most complete Medusa MCP implementation
- **[SGFGOV/medusa-mcp](https://github.com/SGFGOV/medusa-mcp)** — MCP server for Medusa JS SDK with broader scope: carts, payments, shipping, pricing, returns, and fulfillment automation
- **Medusa Docs MCP** — official docs server for AI-assisted Medusa development

### Also notable: PrestaShop MCP servers

PrestaShop is popular in Europe and Latin America, with a growing MCP ecosystem:

- **[latinogino/prestashop-mcp](https://github.com/latinogino/prestashop-mcp)** — professional MCP server for complete PrestaShop management: products, categories, customers, orders, modules, cache, themes, and navigation
- **[florinel-chis/prestashop-mcp](https://github.com/florinel-chis/prestashop-mcp)** — 1,095+ indexed documents for PrestaShop development documentation. Offline-first design
- **[promokit/prestashop-mcp](https://github.com/promokit/prestashop-mcp)** — community PrestaShop MCP implementation

---

## Which e-commerce MCP server should you use?

**"I run a Shopify store and want AI shopping for my customers"** → **Shopify Storefront MCP** is already live on your store. No setup needed.

**"I want AI to manage my Shopify products, orders, and inventory"** → Use **GeLi2001/shopify-mcp** (139 stars, 31+ tools). Accept that it's community-maintained and may need updates when Shopify changes APIs.

**"I'm building apps on Shopify"** → Use **Shopify Dev MCP** for docs, schema introspection, and code validation.

**"I run a WooCommerce store"** → **techspawn/woocommerce-mcp-server** is the most complete option. The WordPress plugin approaches (iOSDevSK, jlfguthrie) are worth watching if you prefer native WP integration.

**"I use Magento / Adobe Commerce"** → **boldcommerce/magento2-mcp** is your best (and really only) option. Covers products, customers, and order analytics.

**"I sell on Amazon"** → **Seller Labs MCP** for production-grade analytics (commercial). Open-source SP-API servers exist but are less mature.

**"I use a headless platform"** → **saleor/saleor-mcp** if you're on Saleor (hosted, official). **minimalart/mcp-medusa** if you're on Medusa (14 admin tools).

**"I use BigCommerce"** → Join the **Storefront MCP beta** if you can. Otherwise, CData's read-only server or Zapier integration are your options.

---

## Three trends to watch

### 1. Agentic commerce is real — Shopify proved the model

Shopify's Storefront MCP is live on every store, powering shopping through ChatGPT, Perplexity, and Copilot. BigCommerce is following with their beta. This isn't theoretical anymore — customers are discovering and buying products through AI agents. Every major e-commerce platform will need a storefront MCP endpoint within 12 months.

### 2. The admin gap is the biggest opportunity

Shopify has no official Admin API MCP server. WooCommerce, Magento, and BigCommerce admin tools are all community-driven with low adoption. The first platform to ship a comprehensive, official admin MCP server — covering products, orders, inventory, fulfillment, and analytics — gains a massive competitive advantage with AI-native merchants.

### 3. Universal Commerce Protocol (UCP) could unify the landscape

Shopify and Google co-developed the Universal Commerce Protocol — an open standard for AI-agent-to-commerce-backend communication. If UCP gains adoption, it could create a single protocol that works across Shopify, WooCommerce, Magento, and others, reducing the need for platform-specific MCP servers.

---

## What's missing

Despite 30+ servers, significant gaps remain:

- **No official Shopify Admin MCP** — the most impactful missing piece. Community servers fill the gap but lack the reliability merchants need
- **No official WooCommerce MCP** — Automattic (WooCommerce's parent) has a WordPress MCP but no dedicated WooCommerce server
- **No official Magento/Adobe Commerce MCP** — Adobe hasn't entered the MCP space for commerce (only for Creative Suite via community servers)
- **No eBay MCP** — one of the world's largest marketplaces has no MCP server
- **No Etsy MCP** — a large marketplace with an active developer API but no MCP integration
- **No multi-platform management** — no server that unifies Shopify + Amazon + WooCommerce into a single interface
- **No inventory sync** — no MCP server for cross-platform inventory synchronization
- **No shipping/logistics** — no dedicated MCP servers for UPS, FedEx, USPS, or DHL APIs
- **No product information management (PIM)** — no MCP servers for tools like Akeneo or Salsify
- **No returns/warranty management** — limited support across all platforms
- **No A/B testing or conversion optimization** — no MCP servers for tools like Optimizely in the commerce context

The e-commerce MCP ecosystem is maturing quickly on the storefront/shopping side (thanks to Shopify) but remains immature for backend operations. The pattern is clear: platforms ship storefront MCP first (customer-facing, low risk), then the community builds admin tools, and eventually official admin servers will follow.

---

*Last updated: March 2026. Star counts and feature details may have changed since publication. See our individual reviews for the most detailed analysis: [Shopify MCP Servers](/reviews/shopify-mcp-servers/) · [E-Commerce & Shopping MCP](/reviews/ecommerce-shopping-mcp-servers/)*
