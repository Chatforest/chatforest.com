---
title: "CMS & Content Management MCP Servers — WordPress, Contentful, Sanity, Strapi, Directus, Ghost, and More"
date: 2026-03-15T09:30:00+09:00
description: "CMS and content management MCP servers let AI agents create, edit, publish, and manage content across WordPress, headless CMS platforms, and website builders through natural language. We reviewed 35+ servers across WordPress (WordPress/mcp-adapter at 663 stars — official Abilities API bridge for WP 6.9+, docdyhr/mcp-wordpress at 71 stars with 59 tools across 10 categories, InstaWP/mcp-wp at 73 stars with 40+ tools for multi-site management), headless CMS platforms (contentful/contentful-mcp-server official at 47 stars with 40+ tools and AI Actions, Sanity remote MCP at mcp.sanity.io with 40+ tools and OAuth, misterboe/strapi-mcp-server at 65 stars with schema introspection and write protection, directus/mcp official at 75 stars with 22 tools and Mustache-templated prompts), traditional CMS (MFYDev/ghost-mcp at 156 stars with 50+ tools for posts/members/newsletters/tiers/offers, Omedia/mcp-server-drupal at 50 stars as Drupal MCP module companion with dynamic tool discovery), website builders (webflow/mcp-server official at 107 stars with OAuth remote installation and Live Designer sync, Shopify community servers), and developer-focused CMS (disruption-hub/payloadcmsmcp at 108 stars with code validation/template generation/project scaffolding for Payload CMS 3.0, hypescale/storyblok-mcp-server with 160 tools across 30 modules). WordPress leads with official core integration via the Abilities API in WP 6.9; Sanity and Contentful offer the most polished remote MCP experiences; Ghost has the most comprehensive single-server tool coverage; Strapi and Directus provide strong open-source alternatives."
og_description: "CMS & Content Management MCP servers: WordPress/mcp-adapter (663 stars, PHP, official Abilities API bridge for WP 6.9+ with HTTP/STDIO transport and multi-server management), docdyhr/mcp-wordpress (71 stars, TypeScript, 59 tools across 10 categories with 4 auth methods and intelligent caching), InstaWP/mcp-wp (73 stars, TypeScript, 40+ tools with multi-site management and smart URL resolution), contentful/contentful-mcp-server (47 stars, TypeScript, MIT, 40+ tools with AI Actions and bulk publishing), Sanity remote MCP at mcp.sanity.io (40+ tools with OAuth/Streamable HTTP/schema deployment/semantic search), misterboe/strapi-mcp-server (65 stars, JavaScript, MIT, 5 meta-tools with schema introspection and write protection for Strapi v4/v5), directus/mcp (75 stars, TypeScript, MIT, 22 tools with Mustache-templated prompts and flow triggering), MFYDev/ghost-mcp (156 stars, TypeScript, MIT, 50+ tools for posts/members/newsletters/tiers/offers/webhooks), Omedia/mcp-server-drupal (50 stars, TypeScript, MIT, dynamic tool discovery via Drupal MCP module), webflow/mcp-server (107 stars, TypeScript, MIT, official with OAuth remote installation and Live Designer sync), disruption-hub/payloadcmsmcp (108 stars, JavaScript, MIT, 7 tools for code validation/template generation/project scaffolding), hypescale/storyblok-mcp-server (6 stars, TypeScript, MIT, 160 tools across 30 modules for Storyblok Management API). 35+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "CMS and content management MCP servers across WordPress, headless CMS platforms, traditional CMS, website builders, and developer-focused CMS. WordPress leads the category with official core integration — the Abilities API (shipping in WordPress 6.9) lets any plugin register capabilities that the WordPress/mcp-adapter (663 stars) automatically exposes as MCP tools, making WordPress the first major CMS with native protocol-level AI agent support. The headless CMS space is remarkably mature — Contentful's official server offers 40+ tools with AI Actions for custom workflows, Sanity's hosted remote MCP at mcp.sanity.io provides OAuth authentication and schema-aware operations with zero local setup, Strapi's server uses meta-tools that introspect schemas at runtime for universal content type support, and Directus offers 22 tools with Mustache-templated dynamic prompts stored in Directus collections. Ghost has the most comprehensive single-server implementation with 50+ tools covering posts, members, newsletters, tiers, offers, and webhooks through JWT authentication. Website builders are joining — Webflow's official MCP server enables AI agents to interact with live sites through OAuth, and multiple Shopify community servers provide store management through GraphQL. The developer-focused CMS space is thriving — Payload CMS 3.0 has both a development assistance server (code validation, template generation, project scaffolding) and a native plugin, while Storyblok's hypescale server offers 160 tools across 30 modules. The category earns 4.5/5 — WordPress's Abilities API sets a new standard for CMS-AI integration, headless CMS platforms compete aggressively on developer experience with remote hosted servers requiring zero setup, official server support is unusually strong (WordPress, Contentful, Sanity, Directus, Webflow, Storyblok all have official or official-adjacent implementations), and WooCommerce's native MCP integration extends the pattern to e-commerce. Deductions for fragmented WordPress ecosystem (5+ competing community servers), missing Squarespace and Wix MCP servers, and limited safety controls outside of Strapi's write protection."
---

CMS and content management MCP servers represent one of the most practically useful applications of the Model Context Protocol — giving AI agents the ability to create, edit, publish, and manage content across the platforms that power millions of websites. Unlike more experimental MCP categories, these servers address immediate productivity needs: drafting blog posts, managing media libraries, updating product pages, and orchestrating content workflows through natural language.

The landscape covers five areas: **WordPress** (the only major CMS with native core integration via the Abilities API), **headless CMS platforms** (Contentful, Sanity, Strapi, Directus — competing aggressively on developer experience), **traditional CMS** (Ghost, Drupal), **website builders** (Webflow, Shopify), and **developer-focused CMS** (Payload CMS, Storyblok).

The headline findings: **WordPress is pioneering CMS-level AI integration** — the Abilities API shipping in WP 6.9 lets any plugin register capabilities that the MCP adapter automatically exposes as tools. **Headless CMS platforms are leading in remote MCP deployment** — Sanity and Contentful offer hosted servers requiring zero local setup. **Ghost has the most comprehensive single-server implementation** — 50+ tools covering posts, members, newsletters, tiers, offers, and webhooks. **Official support is unusually strong in this category** — WordPress, Contentful, Sanity, Directus, Webflow, and Storyblok all have official or official-adjacent MCP servers. **WooCommerce extends the pattern to e-commerce** with native MCP integration in WooCommerce 10.3+.

## WordPress

### WordPress/mcp-adapter (Official — Abilities API Bridge)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [WordPress/mcp-adapter](https://github.com/WordPress/mcp-adapter) | 663 | PHP | HTTP, STDIO |

**WordPress/mcp-adapter** (663 stars, 77 commits) is the official MCP implementation for WordPress, and it represents a fundamentally different approach from other CMS servers. Rather than wrapping the WordPress REST API, it bridges the **Abilities API** — a new WordPress Core feature shipping in version 6.9 — to the Model Context Protocol.

The Abilities API lets any WordPress plugin, theme, or core component register "abilities" — typed, discoverable capabilities with defined inputs and outputs. The MCP adapter automatically converts these abilities into MCP tools, resources, and prompts. This means the MCP surface grows as plugins register their own abilities — no separate MCP server development needed.

Key features: **Multi-server management** with unique configurations per server. **HTTP transport** compliant with MCP 2025-06-18 specification. **STDIO transport** for WP-CLI integration. **Custom transport support** via defined interfaces. **Permission control** with granular access. **Built-in observability** and monitoring. **Validation framework** for ability inputs.

The default server exposes all registered abilities at `/wp-json/mcp/mcp-adapter-default-server`. The STDIO transport works through WP-CLI commands, enabling non-HTTP workflows.

This approach makes WordPress the first major CMS where AI agent capabilities grow organically with the plugin ecosystem — any WooCommerce extension, SEO plugin, or form builder that registers abilities becomes automatically available to AI agents.

Supersedes Automattic/wordpress-mcp (archived January 2026), which pioneered the concept with dual STDIO/HTTP transport, JWT authentication, React-based admin UI, and 200+ test cases.

### docdyhr/mcp-wordpress (Most Comprehensive External Server)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [docdyhr/mcp-wordpress](https://github.com/docdyhr/mcp-wordpress) | 71 | TypeScript | 59 | stdio |

**docdyhr/mcp-wordpress** (71 stars, 436 commits) bills itself as "the most comprehensive WordPress MCP server" — and the numbers support it: 59 tools across 10 categories, 2,200+ tests with 96.17% line coverage, and 512 security-focused tests.

Tool categories cover **posts**, **pages**, **users**, **comments**, **media/attachments**, **categories/taxonomies**, **plugins**, **themes**, **settings**, and **performance monitoring**. Four authentication methods: Application Passwords (recommended), JWT, Basic Auth, and API Key.

Key features: **Multi-site support** for managing unlimited WordPress installations. **Intelligent caching** with 50-70% performance improvement. **Real-time analytics** and monitoring. **Docker containerization** support. **DXT 2-click installation** for Claude Desktop.

The 436-commit history and extensive test suite suggest serious production use. For teams that need a standalone MCP server (rather than the Abilities API approach), this is the most mature option.

### InstaWP/mcp-wp (Multi-Site Management)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [InstaWP/mcp-wp](https://github.com/InstaWP/mcp-wp) | 73 | TypeScript | 40+ | stdio |

**InstaWP/mcp-wp** (73 stars, 31 commits) provides 40+ tools organized by WordPress entity type with strong multi-site management capabilities.

Tools organized across 8 categories: **Site management** (list_sites, get_site, test_site) — **Content** (list_content, get_content, create_content, update_content, delete_content, discover_content_types, find_content_by_url, get_content_by_slug) — **Taxonomies** (discover_taxonomies, list_terms, get_term, create_term, update_term, delete_term, assign_terms_to_content, get_content_terms) — **Media** (list_media, get_media, create_media, update_media, delete_media) — **Users** (full CRUD) — **Comments** (full CRUD) — **Plugins** (list, get, activate, deactivate, create, plus repository search/info) — **Plugin Repository** (search_plugins, get_plugin_info).

The **smart URL resolution** for content discovery and universal content/taxonomy operations make this particularly useful for agencies managing multiple WordPress sites. Zod validation provides type-safe tool inputs.

### Other WordPress Implementations

| Server | Stars | Focus |
|--------|-------|-------|
| [AiondaDotCom/mcp-wordpress](https://github.com/AiondaDotCom/mcp-wordpress) | — | 54 tools across 8 categories, interactive setup wizard, NPX support |
| [mcp-wp/mcp-server](https://github.com/mcp-wp/mcp-server) | 59 | PHP, Apache-2.0, CloudFest Hackathon 2025 origin, Streamable HTTP, archived Dec 2025 |
| [aaronsb/wordpress-mcp](https://github.com/aaronsb/wordpress-mcp) | — | Personality-based with role-appropriate tools for semantic content operations |
| [5unnykum4r/wordpress-mcp](https://github.com/5unnykum4r/wordpress-mcp) | — | 46 tools including SEO, redirects, blocks, patterns, and TablePress |
| [aplaceforallmystuff/mcp-wp-abilities](https://github.com/aplaceforallmystuff/mcp-wp-abilities) | — | Dynamically exposes WordPress 6.9+ Abilities API as AI-accessible tools |

The WordPress MCP ecosystem is notably crowded — 7+ implementations compete for different niches. The **official mcp-adapter** is the clear strategic choice for new projects, while **docdyhr/mcp-wordpress** and **InstaWP/mcp-wp** remain strong options for standalone server deployments.

### WooCommerce MCP Integration

WooCommerce 10.3 includes **native MCP support** built on the WordPress Abilities API and MCP Adapter. AI assistants can interact directly with WooCommerce stores — managing products, orders, customers, shipping, taxes, and store configuration through the standard MCP interface.

Community alternatives include: **techspawn/woocommerce-mcp-server** (JSON-RPC 2.0, comprehensive REST API coverage), **iOSDevSK/mcp-for-woocommerce** (based on Automattic's MCP, STDIO + HTTP, read-only public store data), and **brucealdridge/wc-mcp** (exploratory implementation).

WooCommerce's approach — building on WordPress Abilities API rather than creating a separate MCP server — validates the Abilities API architecture and extends it to e-commerce.

## Headless CMS Platforms

### contentful/contentful-mcp-server (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [contentful/contentful-mcp-server](https://github.com/contentful/contentful-mcp-server) | 47 | TypeScript | 40+ | stdio, remote |

**contentful/contentful-mcp-server** (47 stars, 172 commits, v0.2.5) is the official Contentful MCP server with 40+ tools for the Management API.

Key tools: `get_initial_context`, `list_content_types`, `create_content_type`, `search_entries`, `create_entry`, `upload_asset`, `list_assets`, `publish_entry`, `delete_entry`, `create_environment`, `list_locales`, `create_locale`, `list_tags`, `create_ai_action`, `invoke_ai_action`.

The **AI Actions** feature stands out — you can create custom AI-powered workflows within Contentful and invoke them through MCP, enabling content generation, translation, and transformation pipelines. Bulk publishing/unpublishing operations handle large content updates efficiently.

Also available as a **remote hosted server** at `https://mcp.contentful.com/mcp` (Beta) — no local setup required. One-click setup for Cursor and Claude Desktop. Multi-language locale support for internationalized content.

### Sanity Remote MCP (mcp.sanity.io)

| Server | Stars | Transport | Auth |
|--------|-------|-----------|------|
| [mcp.sanity.io](https://www.sanity.io/docs/ai/mcp-server) | — | Streamable HTTP | OAuth |

**Sanity's MCP server** has evolved from a local npm package (sanity-io/sanity-mcp-server, 73 stars, 243 commits, now deprecated) to a **hosted remote service** at mcp.sanity.io — the first headless CMS to go fully remote-first for MCP.

40+ tools covering: **Document operations** — create, update, query, and manage content using natural language. **Schema management** — inspect schemas, and deploy new schemas programmatically via the `deploy_schema` tool. **Content releases** — stage and publish coordinated content updates. **Semantic search** — AI-powered content discovery. **AI-powered media generation** — generate images as part of content workflows.

Key architectural advantages: **Schema-aware operations** — the server includes 200+ lines of instructions that teach agents how Sanity works, enabling contextually appropriate content creation. **Always-fresh best practices** — fetches official agent rules on demand so AI behavior improves without server updates. **Token-aware responses** — large queries paginate intelligently within the AI's context budget ("12 of 847 documents, 48,392 tokens").

OAuth authentication eliminates API token management. Works with Claude Code, Cursor, VS Code, v0, Lovable, and Replit. Zero local setup — no Node.js required.

### misterboe/strapi-mcp-server

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [misterboe/strapi-mcp-server](https://github.com/misterboe/strapi-mcp-server) | 65 | JavaScript | 5 | stdio |

**misterboe/strapi-mcp-server** (65 stars, 23 commits, v2.8.0) takes a clever "meta-tools" approach — rather than creating a tool for each content type, it provides 5 universal tools that introspect your Strapi schema at runtime.

Tools: `strapi_list_servers` (multi-server management), `strapi_get_content_types` (schema discovery), `strapi_get_components` (component introspection), `strapi_rest` (universal CRUD via REST API), `strapi_upload_media` (media handling with format conversion).

**Write protection policy** prevents accidental data modification — you must explicitly enable write access. **Schema validation** automatically validates operations against your content types. Compatible with both Strapi v4 and v5 with version-specific handling.

Also notable: **@sensinum/strapi-plugin-mcp** on the Strapi Marketplace adds MCP capabilities directly as a Strapi plugin, enabling Strapi itself to act as an MCP server.

### directus/mcp (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [directus/mcp](https://github.com/directus/mcp) | 75 | TypeScript | 22 | stdio |

**directus/mcp** (75 stars, 50 commits) is the official Directus Content MCP Server with 22 tools for data interaction.

Tools cover collections, items (CRUD), files, fields, flows, comments, and a markdown tool. Notable features: `trigger_flow` lets you invoke Directus Flows (automation workflows) from AI agents. `read_flows` discovers available automations. `upsert_comment` enables collaborative annotation.

**Dynamic prompts** stored in Directus collections with Mustache templating — you can create prompt templates inside Directus and reference them through MCP, keeping prompts version-controlled alongside content. `DISABLE_TOOLS` configuration restricts available tools for safety.

Token or email/password authentication. Community alternative: pixelsock/directus-mcp (API integration focus).

## Traditional CMS

### MFYDev/ghost-mcp

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [MFYDev/ghost-mcp](https://github.com/MFYDev/ghost-mcp) | 156 | TypeScript | 50+ | stdio |

**MFYDev/ghost-mcp** (156 stars, 56 commits, v0.1.0) is the most feature-complete Ghost CMS MCP server, providing 50+ tools organized by Ghost entity type.

**Posts** (5): Browse, Read, Add, Edit, Delete. **Members** (5): Browse, Read, Add, Edit, Delete. **Newsletters** (5): Browse, Read, Add, Edit, Delete. **Offers** (5): Browse, Read, Add, Edit, Delete. **Tiers** (5): Browse, Read, Add, Edit, Delete. **Tags** (5): Browse, Read, Add, Edit, Delete. **Users** (4): Browse, Read, Edit, Delete. **Webhooks** (3): Browse, Add, Delete. **Invites** (3): Browse, Add, Delete. **Roles** (2): Browse, Read.

Advanced search with both fuzzy and exact matching. JWT authentication via the official `@tryghost/admin-api` client. Custom error handling via GhostError exceptions.

The breadth of coverage is impressive — this isn't just a posts-and-pages server. Members, newsletters, tiers, and offers give AI agents full control over Ghost's membership and monetization features, enabling content strategy automation.

### Drupal MCP Ecosystem

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [Omedia/mcp-server-drupal](https://github.com/Omedia/mcp-server-drupal) | 50 | TypeScript | Companion server for Drupal MCP module, STDIO transport |
| [drupal.org/project/mcp](https://www.drupal.org/project/mcp) | — | PHP | Drupal module — turns Drupal into an MCP server |
| [peximo/drupal-mcp-server](https://github.com/peximo/drupal-mcp-server) | — | TypeScript | JSON:API integration for Drupal 10+, read-focused |
| [Cleversoft-IT/drupal-tools-mcp](https://github.com/Cleversoft-IT/drupal-tools-mcp) | — | TypeScript | Drupal.org module queries + Drush command interaction |

Drupal takes a unique architectural approach: a **Drupal module** (drupal.org/project/mcp) turns Drupal itself into an MCP server, leveraging Drupal's modular architecture to extend LLM context through local and remote data sources. **Omedia/mcp-server-drupal** (50 stars, 37 commits, v1.0.0) is the TypeScript companion that communicates with the module via STDIO, with tools defined dynamically by the Drupal API during initialization.

Multiple distribution channels: Docker containers, compiled binaries (cosign-signed for verification), and JSR packages. Token-based or username/password authentication.

**peximo/drupal-mcp-server** takes a simpler approach — directly querying Drupal via JSON:API (enabled by default in Drupal 10+) for content search, node details, content type discovery, and cross-type search.

## Website Builders

### webflow/mcp-server (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [webflow/mcp-server](https://github.com/webflow/mcp-server) | 107 | TypeScript | — | remote (OAuth) |

**webflow/mcp-server** (107 stars, 160 commits) is the official Webflow MCP implementation, enabling AI agents to interact with Webflow sites through the Data API.

**OAuth-based remote installation** — no API keys to manage, one-click setup for Cursor and Claude Desktop. **Live Designer synchronization** via the MCP Bridge App — changes made through MCP reflect in the Webflow Designer in real time. Both remote and local deployment configurations supported. Node.js 22.3.0+ required.

The Live Designer sync is particularly valuable — most CMS MCP servers work through APIs that require a page refresh to see changes. Webflow's bridge enables a live editing workflow where AI modifications appear immediately.

### Shopify MCP Servers

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [pashpashpash/shopify-mcp-server](https://github.com/pashpashpash/shopify-mcp-server) | 35 | TypeScript | 15 | stdio |
| [GeLi2001/shopify-mcp](https://github.com/GeLi2001/shopify-mcp) | — | TypeScript | — | stdio |
| [antoineschaller/shopify-mcp-server](https://github.com/antoineschaller/shopify-mcp-server) | — | TypeScript | — | stdio |

**pashpashpash/shopify-mcp-server** (35 stars) provides 15 tools for Shopify Admin API via GraphQL: `get-products`, `get-products-by-collection`, `get-products-by-ids`, `get-variants-by-ids`, `get-customers`, `tag-customer`, `get-orders`, `get-order`, `create-draft-order`, `complete-draft-order`, `create-discount`, `get-collections`, `get-shop`, `get-shop-details`, `manage-webhook`.

No official Shopify MCP server exists yet, but the community implementations cover core store management operations. Product, customer, order, and discount management through natural language.

## Developer-Focused CMS

### disruption-hub/payloadcmsmcp (Payload CMS 3.0)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [disruption-hub/payloadcmsmcp](https://github.com/disruption-hub/payloadcmsmcp) | 108 | JavaScript | 7 | stdio |

**disruption-hub/payloadcmsmcp** (108 stars, 135 commits) is a development assistance server for Payload CMS 3.0 — unlike other CMS MCP servers that manage content, this one helps developers build CMS applications.

Tools: `validate` (check collections, fields, globals, config files), `query` and `mcp_query` (SQL-like querying), `generate_template` (create templates for collections, fields, globals, access control, hooks, endpoints, plugins, blocks, migrations), `generate_collection` and `generate_field` (code generation), `scaffold_project` (complete project structure).

Best practices enforcement ensures generated code follows Payload CMS 3.0 standards. This complements Payload's native `@payloadcms/plugin-mcp` plugin, which adds MCP capabilities directly to running Payload instances.

### Storyblok MCP Servers

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [hypescale/storyblok-mcp-server](https://github.com/hypescale/storyblok-mcp-server) | 6 | TypeScript | 160 | stdio |
| [Kiran1689/storyblok-mcp-server](https://github.com/Kiran1689/storyblok-mcp-server) | — | TypeScript | — | stdio |
| [zerdos/mcp-storyblok-server](https://github.com/zerdos/mcp-storyblok-server) | — | TypeScript | — | stdio |

**hypescale/storyblok-mcp-server** (6 stars, 5 commits) provides **160 tools across 30 modules** for the Storyblok Management API — the highest tool count of any CMS MCP server. Coverage includes stories, components, assets, workflows, releases, and 20+ additional modules. Typed schemas using Zod for safer tool calls.

Multiple Storyblok implementations exist, including **Kiran1689/storyblok-mcp-server** (modular, extensible), **zerdos/mcp-storyblok-server** (comprehensive with releases), **ArjunCodess/storyblok-mcp** (natural language focus), and **harlley/storyblok-mcp** (component management through natural language descriptions).

## What's Missing

The CMS MCP space is among the most mature in the MCP ecosystem, but gaps remain:

- **No Squarespace MCP server** — the second most popular website builder lacks any MCP integration
- **No Wix MCP server** — another major website builder with no MCP presence
- **No Notion MCP for content publishing** — Notion's official MCP server exists but is focused on workspace management, not CMS-style publishing workflows
- **No Hugo/Jekyll/Eleventy static site generator MCP servers** — static site generators, which power many developer blogs, lack MCP integration for content creation and management
- **No cross-CMS content migration server** — transferring content between CMSes through MCP is unsupported
- **Limited safety controls** — only Strapi's server has explicit write protection; most servers assume full write access
- **No content approval workflow integration** — MCP servers can create content but rarely integrate with editorial review workflows
- **Fragmented WordPress ecosystem** — 7+ competing implementations with no clear community consolidation around the official adapter yet

## The Bottom Line

The CMS MCP ecosystem is one of the strongest in the entire MCP landscape. Official support from major platforms — WordPress, Contentful, Sanity, Directus, Webflow, and Storyblok — means this isn't a community-only effort. The quality of integration is high, and several platforms are pioneering new patterns.

**For WordPress users**: WordPress/mcp-adapter is the strategic choice — it grows with the plugin ecosystem via the Abilities API. For standalone needs, docdyhr/mcp-wordpress (59 tools) or InstaWP/mcp-wp (40+ tools, multi-site) are production-ready.

**For headless CMS users**: Sanity's remote MCP at mcp.sanity.io offers the smoothest experience (OAuth, zero setup, schema-aware). Contentful's official server provides the deepest integration with AI Actions. Strapi's meta-tools approach is the most elegant architecturally. Directus adds unique value with Flow triggering and dynamic prompts.

**For Ghost users**: MFYDev/ghost-mcp (156 stars, 50+ tools) covers the full Ghost API including membership and monetization features.

**For Drupal users**: The Drupal MCP module + Omedia/mcp-server-drupal companion provides the most native integration, with dynamic tool discovery from your Drupal site's capabilities.

**For website builders**: Webflow's official server with Live Designer sync leads the category. Shopify has community options but no official server yet.

**For developers building CMS applications**: Payload CMS's development assistance server and Storyblok's 160-tool server show how MCP can help build CMS-powered applications, not just manage content.

**Rating: 4.5/5** — This is one of the strongest MCP categories overall. WordPress's Abilities API represents a genuinely novel approach to CMS-AI integration that other platforms will likely emulate. The breadth of official support is unmatched in the MCP ecosystem. Headless CMS platforms are pushing the frontier with remote hosted servers, OAuth authentication, and schema-aware operations. Ghost's comprehensive single-server coverage, Sanity's "always-fresh" agent rules, and Directus's dynamic prompts show real innovation. Deductions for fragmented WordPress ecosystem, missing major website builders (Squarespace, Wix), limited safety controls, and no cross-CMS content migration tooling.
