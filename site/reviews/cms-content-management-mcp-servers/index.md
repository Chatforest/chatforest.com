# CMS & Content Management MCP Servers — WordPress, Contentful, Sanity, Strapi, Directus, Ghost, and More

> CMS and content management MCP servers let AI agents create, edit, publish, and manage content across WordPress, headless CMS platforms, and website builders through natural language.


CMS and content management MCP servers represent one of the most practically useful applications of the Model Context Protocol — giving AI agents the ability to create, edit, publish, and manage content across the platforms that power millions of websites. Unlike more experimental MCP categories, these servers address immediate productivity needs: drafting blog posts, managing media libraries, updating product pages, and orchestrating content workflows through natural language.

The landscape covers six areas: **WordPress** (the only major CMS with native core integration via the Abilities API), **headless CMS platforms** (Contentful, Sanity, Strapi, Directus — competing aggressively on developer experience), **traditional CMS** (Ghost, Drupal), **website builders** (Webflow, Shopify), **developer-focused CMS** (Payload CMS, Storyblok), and the emerging **AI-native CMS** category (Cloudflare's EmDash — built from scratch with MCP as a core feature).

The headline findings: **WordPress is pioneering CMS-level AI integration** — the Abilities API shipping in WP 6.9 lets any plugin register capabilities that the MCP adapter automatically exposes as tools. **Headless CMS platforms are leading in remote MCP deployment** — Sanity and Contentful offer hosted servers requiring zero local setup. **Ghost has the most comprehensive single-server implementation** — 42 tools covering posts, members, newsletters, tiers, offers, and webhooks. **Official support is unusually strong in this category** — WordPress, Contentful, Sanity, Directus, Webflow, and Storyblok all have official or official-adjacent MCP servers. **WooCommerce extends the pattern to e-commerce** with native MCP integration (developer preview) in WooCommerce 10.3+, currently covering products and orders.

**Category:** [Business & Productivity](/categories/business-productivity/)

## WordPress

### WordPress/mcp-adapter (Official — Abilities API Bridge)

| Server | Stars | Language | Transport |
|--------|-------|----------|-----------|
| [WordPress/mcp-adapter](https://github.com/WordPress/mcp-adapter) | 1,575 | PHP | HTTP, STDIO |

**WordPress/mcp-adapter** (1,575 stars, 141 commits) is the official MCP implementation for WordPress, and it represents a fundamentally different approach from other CMS servers. Rather than wrapping the WordPress REST API, it bridges the **[Abilities API](https://make.wordpress.org/core/2025/11/10/abilities-api-in-wordpress-6-9/)** — a WordPress Core feature that shipped with [WordPress 6.9](https://make.wordpress.org/core/2025/07/28/roadmap-to-6-9/) (released December 2, 2025) — to the Model Context Protocol.

The Abilities API lets any WordPress plugin, theme, or core component register "abilities" — typed, discoverable capabilities with defined inputs and outputs. The MCP adapter automatically converts these abilities into MCP tools, resources, and prompts. This means the MCP surface grows as plugins register their own abilities — no separate MCP server development needed.

Key features: **Multi-server management** with unique configurations per server. **HTTP transport** compliant with MCP 2025-06-18 specification. **STDIO transport** for WP-CLI integration. **Custom transport support** via defined interfaces. **Permission control** with granular access. **Built-in observability** and monitoring. **Validation framework** for ability inputs.

The default server exposes all registered abilities at `/wp-json/mcp/mcp-adapter-default-server`. The STDIO transport works through WP-CLI commands, enabling non-HTTP workflows.

This approach makes WordPress the first major CMS where AI agent capabilities grow organically with the plugin ecosystem — any WooCommerce extension, SEO plugin, or form builder that registers abilities becomes automatically available to AI agents.

Supersedes Automattic/wordpress-mcp (archived January 2026), which pioneered the concept with dual STDIO/HTTP transport, JWT authentication, React-based admin UI, and 200+ test cases.

### docdyhr/mcp-wordpress (Most Comprehensive External Server)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [docdyhr/mcp-wordpress](https://github.com/docdyhr/mcp-wordpress) | 102 | TypeScript | 71 | stdio |

**docdyhr/mcp-wordpress** (102 stars, 595 commits) bills itself as "the most comprehensive WordPress MCP server" — and the numbers support it: [71 tools across 12 categories, 2,750+ tests with ~76% line coverage, and 371 security-focused tests](https://github.com/docdyhr/mcp-wordpress).

Tool categories cover **posts**, **pages**, **media**, **SEO**, **users**, **comments**, **taxonomies**, **site settings**, **authentication**, **cache management**, **performance monitoring**, and **system**. Four authentication methods: Application Passwords (recommended), JWT, Basic Auth, and API Key.

Key features: **Multi-site support** for managing unlimited WordPress installations. **Intelligent caching** with 50-70% performance improvement. **Real-time analytics** and monitoring. **Docker containerization** support. **DXT 2-click installation** for Claude Desktop.

The 595-commit history and extensive test suite suggest serious production use. For teams that need a standalone MCP server (rather than the Abilities API approach), this is the most mature option.

### InstaWP/mcp-wp (Multi-Site Management)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [InstaWP/mcp-wp](https://github.com/InstaWP/mcp-wp) | 91 | TypeScript | 40+ | stdio |

**InstaWP/mcp-wp** (91 stars, 68 commits) provides 40+ tools organized by WordPress entity type with strong multi-site management capabilities.

Tools organized across 8 categories: **Site management** (list_sites, get_site, test_site) — **Content** (list_content, get_content, create_content, update_content, delete_content, discover_content_types, find_content_by_url, get_content_by_slug) — **Taxonomies** (discover_taxonomies, list_terms, get_term, create_term, update_term, delete_term, assign_terms_to_content, get_content_terms) — **Media** (list_media, get_media, create_media, update_media, delete_media) — **Users** (full CRUD) — **Comments** (full CRUD) — **Plugins** (list, get, activate, deactivate, create, plus repository search/info) — **Plugin Repository** (search_plugins, get_plugin_info).

The **smart URL resolution** for content discovery and universal content/taxonomy operations make this particularly useful for agencies managing multiple WordPress sites. Zod validation provides type-safe tool inputs.

### Other WordPress Implementations

| Server | Stars | Focus |
|--------|-------|-------|
| [AiondaDotCom/mcp-wordpress](https://github.com/AiondaDotCom/mcp-wordpress) | — | 54 tools across 8 categories, interactive setup wizard, NPX support |
| [mcp-wp/mcp-server](https://github.com/mcp-wp/mcp-server) | 61 | PHP, Apache-2.0, CloudFest Hackathon 2025 origin, Streamable HTTP, archived Dec 2025 |
| [aaronsb/wordpress-mcp](https://github.com/aaronsb/wordpress-mcp) | — | Personality-based with role-appropriate tools for semantic content operations |
| [5unnykum4r/wordpress-mcp](https://github.com/5unnykum4r/wordpress-mcp) | — | 46 tools including SEO, redirects, blocks, patterns, and TablePress |
| [aplaceforallmystuff/mcp-wp-abilities](https://github.com/aplaceforallmystuff/mcp-wp-abilities) | — | Dynamically exposes WordPress 6.9+ Abilities API as AI-accessible tools |

The WordPress MCP ecosystem is notably crowded — 7+ implementations compete for different niches. The **official mcp-adapter** is the clear strategic choice for new projects, while **docdyhr/mcp-wordpress** and **InstaWP/mcp-wp** remain strong options for standalone server deployments.

### WooCommerce MCP Integration

[WooCommerce 10.3](https://developer.woocommerce.com/2025/11/03/call-for-testing-woocommerce-mcp-beta/) shipped **native MCP support in beta**, built on the WordPress Abilities API and MCP Adapter. As of WooCommerce 10.7, the [official developer docs](https://developer.woocommerce.com/docs/features/mcp/) and [WooCommerce's own MCP writeup](https://woocommerce.com/posts/woocommerce-mcp/) describe the built-in abilities as still limited to **products** (list, get, create, update, delete) and **orders** (list, get, create, update) — MCP is explicitly still in developer preview, so customer, shipping, tax, and store-configuration abilities are not yet built in.

Community alternatives include: **techspawn/woocommerce-mcp-server** (JSON-RPC 2.0, comprehensive REST API coverage), **iOSDevSK/mcp-for-woocommerce** (based on Automattic's MCP, STDIO + HTTP, read-only public store data), and **brucealdridge/wc-mcp** (exploratory implementation).

WooCommerce's approach — building on WordPress Abilities API rather than creating a separate MCP server — validates the Abilities API architecture and extends it to e-commerce.

## Headless CMS Platforms

### contentful/contentful-mcp-server (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [contentful/contentful-mcp-server](https://github.com/contentful/contentful-mcp-server) | 58 | TypeScript | 40+ | stdio, remote |

**contentful/contentful-mcp-server** (58 stars, 240 commits, [v1.15.0](https://github.com/contentful/contentful-mcp-server/releases)) is the official Contentful MCP server with 40+ tools for the Management API.

Key tools: `get_initial_context`, `list_content_types`, `create_content_type`, `search_entries`, `create_entry`, `upload_asset`, `list_assets`, `publish_entry`, `delete_entry`, `create_environment`, `list_locales`, `create_locale`, `list_tags`, `create_ai_action`, `invoke_ai_action`.

The **AI Actions** feature stands out — you can create custom AI-powered workflows within Contentful and invoke them through MCP, enabling content generation, translation, and transformation pipelines. Bulk publishing/unpublishing operations handle large content updates efficiently.

Also available as a **remote hosted server** at `https://mcp.contentful.com/mcp` (Beta) — no local setup required. One-click setup for Cursor and Claude Desktop. Multi-language locale support for internationalized content.

### Sanity Remote MCP (mcp.sanity.io)

| Server | Stars | Transport | Auth |
|--------|-------|-----------|------|
| [mcp.sanity.io](https://www.sanity.io/docs/ai/mcp-server) | — | Streamable HTTP | OAuth |

**Sanity's MCP server** has evolved from a local npm package ([sanity-io/sanity-mcp-server](https://github.com/sanity-io/sanity-mcp-server), 72 stars, 243 commits, archived July 2026) to a **hosted remote service** at mcp.sanity.io — the first headless CMS to go fully remote-first for MCP.

40+ tools covering: **Document operations** — create, update, query, and manage content using natural language. **Schema management** — inspect schemas, and deploy new schemas programmatically via the `deploy_schema` tool. **Content releases** — stage and publish coordinated content updates. **Semantic search** — AI-powered content discovery. **AI-powered media generation** — generate images as part of content workflows.

Key architectural advantages: **Schema-aware operations** — the server includes 200+ lines of instructions that teach agents how Sanity works, enabling contextually appropriate content creation. **Always-fresh best practices** — fetches official agent rules on demand so AI behavior improves without server updates. **Token-aware responses** — large queries paginate intelligently within the AI's context budget ("12 of 847 documents, 48,392 tokens").

OAuth authentication eliminates API token management. Works with Claude Code, Cursor, VS Code, v0, Lovable, and Replit. Zero local setup — no Node.js required.

### misterboe/strapi-mcp-server

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [misterboe/strapi-mcp-server](https://github.com/misterboe/strapi-mcp-server) | 76 | JavaScript | 5 | stdio |

**misterboe/strapi-mcp-server** (76 stars, 23 commits, [v2.8.0 on npm](https://www.npmjs.com/package/@bschauer/strapi-mcp-server)) takes a clever "meta-tools" approach — rather than creating a tool for each content type, it provides 5 universal tools that introspect your Strapi schema at runtime.

Tools: `strapi_list_servers` (multi-server management), `strapi_get_content_types` (schema discovery), `strapi_get_components` (component introspection), `strapi_rest` (universal CRUD via REST API), `strapi_upload_media` (media handling with format conversion).

**Write protection policy** prevents accidental data modification — you must explicitly enable write access. **Schema validation** automatically validates operations against your content types. Compatible with both Strapi v4 and v5 with version-specific handling.

Also notable: **@sensinum/strapi-plugin-mcp** on the Strapi Marketplace adds MCP capabilities directly as a Strapi plugin, enabling Strapi itself to act as an MCP server.

### directus/mcp (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [directus/mcp](https://github.com/directus/mcp) | 83 | TypeScript | ~21 | stdio |

**directus/mcp** (83 stars, 50 commits) is the official Directus Content MCP Server with ~21 tools for data interaction.

Tools cover collections, items (CRUD), files, fields, flows, comments, and a markdown tool. Notable features: `trigger_flow` lets you invoke Directus Flows (automation workflows) from AI agents. `read_flows` discovers available automations. `upsert_comment` enables collaborative annotation.

**Dynamic prompts** stored in Directus collections with Mustache templating — you can create prompt templates inside Directus and reference them through MCP, keeping prompts version-controlled alongside content. `DISABLE_TOOLS` configuration restricts available tools for safety.

Token or email/password authentication. Community alternative: pixelsock/directus-mcp (API integration focus).

## Traditional CMS

### MFYDev/ghost-mcp

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [MFYDev/ghost-mcp](https://github.com/MFYDev/ghost-mcp) | 220 | TypeScript | 42 | stdio |

**MFYDev/ghost-mcp** (220 stars, 62 commits, [v0.2.0](https://github.com/MFYDev/ghost-mcp/releases)) is the most feature-complete Ghost CMS MCP server, providing 42 tools organized by Ghost entity type.

**Posts** (5): Browse, Read, Add, Edit, Delete. **Members** (5): Browse, Read, Add, Edit, Delete. **Newsletters** (5): Browse, Read, Add, Edit, Delete. **Offers** (5): Browse, Read, Add, Edit, Delete. **Tiers** (5): Browse, Read, Add, Edit, Delete. **Tags** (5): Browse, Read, Add, Edit, Delete. **Users** (4): Browse, Read, Edit, Delete. **Webhooks** (3): Browse, Add, Delete. **Invites** (3): Browse, Add, Delete. **Roles** (2): Browse, Read.

Advanced search with both fuzzy and exact matching. JWT authentication via the official `@tryghost/admin-api` client. Custom error handling via GhostError exceptions.

The breadth of coverage is impressive — this isn't just a posts-and-pages server. Members, newsletters, tiers, and offers give AI agents full control over Ghost's membership and monetization features, enabling content strategy automation.

### Drupal MCP Ecosystem

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [Omedia/mcp-server-drupal](https://github.com/Omedia/mcp-server-drupal) | 51 | TypeScript | Companion server for Drupal MCP module, STDIO transport |
| [drupal.org/project/mcp](https://www.drupal.org/project/mcp) | — | PHP | Drupal module — turns Drupal into an MCP server |
| [peximo/drupal-mcp-server](https://github.com/peximo/drupal-mcp-server) | — | TypeScript | JSON:API integration for Drupal 10+, read-focused |
| [Cleversoft-IT/drupal-tools-mcp](https://github.com/Cleversoft-IT/drupal-tools-mcp) | — | TypeScript | Drupal.org module queries + Drush command interaction |

Drupal takes a unique architectural approach: a **Drupal module** (drupal.org/project/mcp) turns Drupal itself into an MCP server, leveraging Drupal's modular architecture to extend LLM context through local and remote data sources. **Omedia/mcp-server-drupal** (51 stars, 37 commits, v1.0.0) is the TypeScript companion that communicates with the module via STDIO, with tools defined dynamically by the Drupal API during initialization.

Multiple distribution channels: Docker containers, compiled binaries (cosign-signed for verification), and JSR packages. Token-based or username/password authentication.

**peximo/drupal-mcp-server** takes a simpler approach — directly querying Drupal via JSON:API (enabled by default in Drupal 10+) for content search, node details, content type discovery, and cross-type search.

## Website Builders

### webflow/mcp-server (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [webflow/mcp-server](https://github.com/webflow/mcp-server) | 137 | TypeScript | — | remote (OAuth) |

**webflow/mcp-server** (137 stars, 163 commits) is the official Webflow MCP implementation, enabling AI agents to interact with Webflow sites through the Data API.

**OAuth-based remote installation** — no API keys to manage, one-click setup for Cursor and Claude Desktop. **Live Designer synchronization** via the MCP Bridge App — changes made through MCP reflect in the Webflow Designer in real time. Both remote and local deployment configurations supported. Node.js 22.3.0+ required.

The Live Designer sync is particularly valuable — most CMS MCP servers work through APIs that require a page refresh to see changes. Webflow's bridge enables a live editing workflow where AI modifications appear immediately.

### Shopify MCP Servers

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [pashpashpash/shopify-mcp-server](https://github.com/pashpashpash/shopify-mcp-server) | 36 | TypeScript | 15 | stdio |
| [GeLi2001/shopify-mcp](https://github.com/GeLi2001/shopify-mcp) | 235 | TypeScript | — | stdio |
| [antoineschaller/shopify-mcp-server](https://github.com/antoineschaller/shopify-mcp-server) | 18 | TypeScript | — | stdio |

**pashpashpash/shopify-mcp-server** (36 stars) provides 15 tools for Shopify Admin API via GraphQL: `get-products`, `get-products-by-collection`, `get-products-by-ids`, `get-variants-by-ids`, `get-customers`, `tag-customer`, `get-orders`, `get-order`, `create-draft-order`, `complete-draft-order`, `create-discount`, `get-collections`, `get-shop`, `get-shop-details`, `manage-webhook`.

No official Shopify MCP server exists yet, but the community implementations cover core store management operations. Product, customer, order, and discount management through natural language. Note that by star count, [GeLi2001/shopify-mcp](https://github.com/GeLi2001/shopify-mcp) (235 stars) now has considerably more community traction than pashpashpash's server — worth evaluating alongside it if you're choosing a Shopify server.

## Developer-Focused CMS

### disruption-hub/payloadcmsmcp (Payload CMS 3.0)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [disruption-hub/payloadcmsmcp](https://github.com/disruption-hub/payloadcmsmcp) | 117 | JavaScript | 7 | stdio |

**disruption-hub/payloadcmsmcp** (117 stars, 135 commits) is a development assistance server for Payload CMS 3.0 — unlike other CMS MCP servers that manage content, this one helps developers build CMS applications.

Tools: `validate` (check collections, fields, globals, config files), `query` and `mcp_query` (SQL-like querying), `generate_template` (create templates for collections, fields, globals, access control, hooks, endpoints, plugins, blocks, migrations), `generate_collection` and `generate_field` (code generation), `scaffold_project` (complete project structure).

Best practices enforcement ensures generated code follows Payload CMS 3.0 standards. This complements Payload's native `@payloadcms/plugin-mcp` plugin, which adds MCP capabilities directly to running Payload instances.

### Storyblok MCP Servers

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [hypescale/storyblok-mcp-server](https://github.com/hypescale/storyblok-mcp-server) | 8 | TypeScript | 160 | stdio |
| [Kiran1689/storyblok-mcp-server](https://github.com/Kiran1689/storyblok-mcp-server) | 40 | TypeScript | — | stdio |
| [zerdos/mcp-storyblok-server](https://github.com/zerdos/mcp-storyblok-server) | 1 | TypeScript | — | stdio |

**hypescale/storyblok-mcp-server** (8 stars, 5 commits) provides **160 tools across 30 modules** for the Storyblok Management API — the highest tool count of any CMS MCP server. Coverage includes stories, components, assets, workflows, releases, and 20+ additional modules. Typed schemas using Zod for safer tool calls.

Multiple Storyblok implementations exist, including **[Kiran1689/storyblok-mcp-server](https://github.com/Kiran1689/storyblok-mcp-server)** (40 stars — modular, extensible), **zerdos/mcp-storyblok-server** (1 star — comprehensive with releases), **ArjunCodess/storyblok-mcp** (natural language focus), and **harlley/storyblok-mcp** (component management through natural language descriptions).

## AI-Native CMS

### EmDash (Cloudflare)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | 11,613 | TypeScript | Built-in | Remote MCP |

**EmDash** (launched as a preview in April 2026, now at [v0.33.0](https://github.com/emdash-cms/emdash/releases) as of August 2026, still labeled "beta preview" by the project) is Cloudflare's "spiritual successor to WordPress" — and the first CMS designed from the ground up with AI agents as first-class users. It has grown quickly since launch, passing 11,600 GitHub stars by mid-August 2026. Unlike every other CMS on this page where MCP is an integration layer, EmDash ships with a built-in remote MCP server in every instance.

Every deployment includes: a **remote MCP server** (Claude, Cursor, or any MCP-compatible agent can create content types, manage entries, configure plugins, and deploy), a **CLI** for programmatic interaction, and **Agent Skills files** that teach AI models how to operate the system without step-by-step instruction.

Architecture choices favor agents: content stored as **portable text** (structured JSON, not HTML) so agents can read and modify content without parsing markup. Custom content types get **typed database tables**, enabling agents to reason about schemas programmatically. Sandboxed plugins run on Cloudflare via **Dynamic Worker Loaders** with strict manifest-based capability controls — a plugin can only perform actions declared in its manifest.

**Key features:** definePlugin() API with lifecycle hooks, KV storage, settings, admin pages, dashboard widgets, custom block types, and API routes. Astro-powered theming. Native x402 payment support. Runs on Cloudflare (D1 + R2 + Workers) or any Node.js server with SQLite. MIT licensed, open source.

**Limitations:** Still labeled beta preview by the project, though it has matured and grown its star count substantially since the April 2026 launch. [WordPress migration tooling now exists](https://github.com/emdash-cms/emdash) — the project supports importing posts, pages, media, and taxonomies from WXR exports, the WordPress REST API, or WordPress.com, with AI agent skills to help port plugins and themes — but the third-party plugin and theme ecosystem is still nascent (mostly first-party plugins and three starter themes as of this writing). Cloudflare-native deployment (D1 + R2 + Workers) is the primary/recommended path, with a Node.js + SQLite option available.

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

**For WordPress users**: WordPress/mcp-adapter is the strategic choice — it grows with the plugin ecosystem via the Abilities API. For standalone needs, docdyhr/mcp-wordpress (71 tools) or InstaWP/mcp-wp (40+ tools, multi-site) are production-ready.

**For headless CMS users**: Sanity's remote MCP at mcp.sanity.io offers the smoothest experience (OAuth, zero setup, schema-aware). Contentful's official server provides the deepest integration with AI Actions. Strapi's meta-tools approach is the most elegant architecturally. Directus adds unique value with Flow triggering and dynamic prompts.

**For Ghost users**: MFYDev/ghost-mcp (220 stars, 42 tools) covers the full Ghost API including membership and monetization features.

**For Drupal users**: The Drupal MCP module + Omedia/mcp-server-drupal companion provides the most native integration, with dynamic tool discovery from your Drupal site's capabilities.

**For website builders**: Webflow's official server with Live Designer sync leads the category. Shopify has community options but no official server yet.

**For developers building CMS applications**: Payload CMS's development assistance server and Storyblok's 160-tool server show how MCP can help build CMS-powered applications, not just manage content.

**For greenfield AI-agent-first projects**: Cloudflare's EmDash is the first CMS where MCP is built in rather than bolted on. Still labeled beta preview, but growing fast (11,600+ GitHub stars by mid-August 2026) and architecturally compelling if you want agents to be first-class citizens from day one.

## What's New (May 2026)

**Optimizely JavaScript SDK v2 and AI-agent markdown (April 2026).** [Optimizely's 2026 CMS 12 release notes](https://support.optimizely.com/hc/en-us/articles/33309043090189-2026-Optimizely-CMS-12-release-notes) include two agent-relevant updates: the JavaScript SDK v2 ships stronger validation, expanded content type support, and improved handling of Content and ContentReference properties. More interesting is the beta "Markdown for AI agents" feature — CMS 12 and CMS 13 can now deliver clean markdown versions of pages to AI agents at the edge rather than full HTML, reducing ingestion cost and improving AI response accuracy. This positions Optimizely as one of the first enterprise CMSes to optimize its output format for LLM consumption rather than browser rendering.

**EmDash accelerates (v0.1.x to v0.2.x window).** Cloudflare's EmDash has continued shipping rapidly since its April 2026 preview launch. The "built-in MCP from day one" architecture has attracted attention from headless-CMS-adjacent teams looking for simpler deployment paths. Still early-stage, but now with community momentum building.

**Rating: 4.5/5** — This is one of the strongest MCP categories overall. WordPress's Abilities API represents a genuinely novel approach to CMS-AI integration that other platforms will likely emulate. The breadth of official support is unmatched in the MCP ecosystem. Headless CMS platforms are pushing the frontier with remote hosted servers, OAuth authentication, and schema-aware operations. Ghost's comprehensive single-server coverage, Sanity's "always-fresh" agent rules, and Directus's dynamic prompts show real innovation. Deductions for fragmented WordPress ecosystem, missing major website builders (Squarespace, Wix), limited safety controls, and no cross-CMS content migration tooling.

*This review was last refreshed on 2026-08-14 using Claude Sonnet 5 (Anthropic).*

