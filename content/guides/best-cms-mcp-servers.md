---
title: "Best CMS & Content Management MCP Servers in 2026"
date: 2026-03-22T17:00:00+09:00
description: "WordPress, Contentful, Sanity, Strapi, Directus, Ghost, Webflow, Shopify, Wix, and more — we've reviewed 40+ CMS MCP servers across 6 categories. Shopify and Wix now have official MCP servers, EmDash hit 9,400+ stars in two weeks, and WordPress/mcp-adapter v0.5.0 shipped."
og_description: "40+ CMS and content management MCP servers reviewed across WordPress, headless CMS platforms, traditional CMS, website builders, developer-focused CMS, and AI-native CMS. Shopify and Wix official MCP servers, EmDash v0.5.0, WordPress mcp-adapter v0.5.0."
content_type: "Comparison"
card_description: "The definitive guide to CMS MCP servers in 2026. We've reviewed 40+ servers across WordPress, headless CMS, website builders, developer-focused CMS, and AI-native CMS. Shopify and Wix now have official MCP. Every recommendation links to a full review."
last_refreshed: 2026-04-16
---

CMS MCP servers solve one of the most practical problems in AI-assisted development: managing content at scale. Instead of switching between CMS dashboards, writing API calls, or navigating admin panels, these servers let AI agents create, edit, publish, and manage content across platforms through natural language.

The CMS MCP landscape shifted dramatically in April 2026. Cloudflare's **EmDash** rocketed to 9,400+ GitHub stars in two weeks, going from v0.1.0 to v0.5.0. **Shopify launched four official MCP servers** covering Dev, Storefront, Customer Account, and Checkout. **Wix made every site an MCP server** out of the box. WordPress/mcp-adapter shipped **v0.5.0** with protocol negotiation and security hardening (stars: 887). Meanwhile, WordPress 7.0 was delayed again — now expected mid-to-late May 2026.

We've published [in-depth reviews](/reviews/) covering 40+ CMS MCP servers across the entire content management landscape. This guide synthesizes all of that into one page: what's worth using, what's not, and where the gaps are.

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| WordPress (official) | [WordPress/mcp-adapter](/reviews/cms-content-management-mcp-servers/) | 887 | [docdyhr/mcp-wordpress](/reviews/cms-content-management-mcp-servers/) (81 stars, 59 tools) |
| WordPress (standalone) | [docdyhr/mcp-wordpress](/reviews/cms-content-management-mcp-servers/) | 81 | [InstaWP/mcp-wp](/reviews/cms-content-management-mcp-servers/) (77 stars, multi-site) |
| Headless CMS (remote-first) | [Sanity MCP](/reviews/cms-content-management-mcp-servers/) | — | [Contentful MCP](/reviews/cms-content-management-mcp-servers/) (50 stars, AI Actions) |
| Headless CMS (open-source) | [Directus MCP](/reviews/cms-content-management-mcp-servers/) | 76 | [Strapi MCP](/reviews/cms-content-management-mcp-servers/) (69 stars, meta-tools) |
| Traditional CMS | [MFYDev/ghost-mcp](/reviews/cms-content-management-mcp-servers/) | 168 | [Drupal MCP module](/reviews/cms-content-management-mcp-servers/) (dynamic tools) |
| Website builders | [Webflow MCP](/reviews/cms-content-management-mcp-servers/) | 123 | [Shopify Official MCP](/reviews/cms-content-management-mcp-servers/) (4 servers, GA) |
| E-commerce | [Shopify Official MCP](/reviews/cms-content-management-mcp-servers/) | Official | [Wix MCP](/reviews/cms-content-management-mcp-servers/) (official, every site) |
| Developer-focused CMS | [Storyblok Official MCP](/reviews/cms-content-management-mcp-servers/) | Official | [disruption-hub/payloadcmsmcp](/reviews/cms-content-management-mcp-servers/) (112 stars, dev tools) |
| AI-native CMS | [EmDash (Cloudflare)](/reviews/cms-content-management-mcp-servers/) | 9,415 | Built-in MCP, agent-first, v0.5.0 |

## Why CMS MCP servers matter

Content management is one of the most time-consuming parts of running a website. MCP servers add three capabilities that change the workflow:

1. **Natural language content operations.** Instead of navigating admin dashboards, tell your agent: "Draft a blog post about our Q1 results, add the header image from our media library, and schedule it for Thursday." The agent handles creation, media, and publishing.
2. **Cross-platform content awareness.** An agent with access to multiple CMS MCP servers can compare approaches — "migrate this content from WordPress to Sanity" — with actual knowledge of both platforms' schemas and APIs.
3. **Programmatic editorial workflows.** "Find all draft posts older than 30 days and list them for review" becomes a natural language query. AI agents can manage content lifecycle, membership tiers, newsletters, and publishing schedules.

The landscape splits into seven categories: **WordPress** (native core integration via the Abilities API), **headless CMS platforms** (Contentful, Sanity, Strapi, Directus — competing on developer experience and remote MCP), **traditional CMS** (Ghost, Drupal), **website builders** (Webflow, Shopify, Wix — all now with official MCP), **e-commerce** (Shopify's four official servers, WooCommerce via WordPress), **developer-focused CMS** (Payload CMS, Storyblok), and the breakout **AI-native CMS** category (Cloudflare's EmDash — 9,400+ stars in two weeks).

## WordPress

WordPress dominates the CMS MCP space — and for good reason. It's the only major CMS where AI agent capabilities are being built into core, not bolted on as an afterthought.

### The winner: WordPress/mcp-adapter (Official)

**[Full review: CMS & Content Management MCP Servers →](/reviews/cms-content-management-mcp-servers/)** | Rating: 4.5/5

[WordPress/mcp-adapter](https://github.com/WordPress/mcp-adapter) — 887 stars, PHP, official. The strategic choice for any WordPress site.

**Why it wins:** This isn't just another REST API wrapper. The MCP adapter bridges the **Abilities API** — a WordPress Core feature introduced in WP 6.9 — to the Model Context Protocol. Any WordPress plugin, theme, or core component that registers "abilities" automatically becomes available to AI agents through MCP. This means the MCP surface grows organically with the plugin ecosystem.

**v0.5.0 shipped April 15, 2026** — a major internal upgrade. Full integration of `wordpress/php-mcp-schema` (typed DTOs instead of hand-built arrays). Protocol version negotiation supporting specs `2025-11-25`, `2025-06-18`, and `2024-11-05`. Security hardening with stricter input validation and fail-closed permission handling. Reduced `SessionManager` write amplification to lower lock contention. Better observability for protocol errors. Migration guide and expanded documentation included.

**WordPress 7.0 delayed to mid-to-late May 2026.** Originally scheduled for April 9, WordPress 7.0 was delayed due to a performance problem in the real-time collaboration feature's data storage layer (cache invalidation and data model issues requiring an architectural fix, not a late-cycle patch). The core team returned to a beta-like testing phase after reaching RC2 — unprecedented in WordPress history. A revised final schedule is expected by April 22, 2026. When it ships, WP 7.0 will merge the **client-side JavaScript Abilities API** (announced March 24 on Make WordPress Core) alongside the server-side PHP API that shipped in WP 6.9. The Connectors UI under Settings gives users a central place in wp-admin to manage external AI connections.

**Key features:** Multi-server management with unique configurations per server. HTTP transport compliant with MCP 2025-06-18 spec (plus backward compatibility via protocol negotiation). STDIO transport for WP-CLI integration. Custom transport support via defined interfaces. Permission control with granular access. Built-in observability and monitoring.

**WooCommerce extends the pattern to e-commerce.** WooCommerce MCP first shipped as beta in WooCommerce 10.3 and has matured through **WooCommerce 10.7** — solid enough to build on, though still labeled "developer preview." WooCommerce held [April Office Hours](https://developer.woocommerce.com/2026/04/07/april-office-hours-ai-and-mcp-in-your-woo-workflows/) focused on "AI and MCP in your Woo workflows." A third-party community plugin (`iOSDevSK/mcp-for-woocommerce`) has also appeared, supporting STDIO and HTTP streamable transport with optional JWT auth.

**The catch:** WordPress 7.0 still hasn't shipped. Plugin adoption of the Abilities API is still ramping up. If you need comprehensive WordPress management today (not just what plugins have registered as abilities), a standalone server may cover more ground.

### Best standalone: docdyhr/mcp-wordpress

[docdyhr/mcp-wordpress](https://github.com/docdyhr/mcp-wordpress) — 81 stars, TypeScript, 59 tools across 10 categories, 436 commits, 96.17% test coverage.

**Why it's the standalone pick:** 59 tools covering posts, pages, users, comments, media/attachments, categories/taxonomies, plugins, themes, settings, and performance monitoring. Four authentication methods (Application Passwords, JWT, Basic Auth, API Key). Multi-site support. Intelligent caching with 50-70% performance improvement. 2,200+ tests and 512 security-focused tests.

**Best for:** Teams that need comprehensive WordPress management right now, without waiting for plugins to adopt the Abilities API.

### Runner-up: InstaWP/mcp-wp

[InstaWP/mcp-wp](https://github.com/InstaWP/mcp-wp) — 77 stars, TypeScript, 40+ tools. Strong multi-site management with smart URL resolution and universal content/taxonomy operations. Added local file uploads (April 2026). Particularly useful for agencies managing multiple WordPress sites.

### The WordPress ecosystem problem

The WordPress MCP space is notably crowded — 7+ implementations compete for different niches. Besides the three above: AiondaDotCom/mcp-wordpress (54 tools, interactive setup wizard), 5unnykum4r/wordpress-mcp (46 tools including SEO and redirects), aaronsb/wordpress-mcp (personality-based semantic operations), and the archived mcp-wp/mcp-server from CloudFest Hackathon 2025.

**Our recommendation:** Use **WordPress/mcp-adapter** for new projects — it's the future. Use **docdyhr/mcp-wordpress** if you need maximum coverage today. Use **InstaWP/mcp-wp** for multi-site agency work.

## Headless CMS Platforms

The headless CMS space is where the most innovation is happening in CMS MCP. These platforms compete aggressively on developer experience, with several pioneering remote hosted MCP servers that require zero local setup.

### The winner: Sanity Remote MCP (mcp.sanity.io)

**[Full review: CMS & Content Management MCP Servers →](/reviews/cms-content-management-mcp-servers/)** | Rating: 4.5/5

[mcp.sanity.io](https://www.sanity.io/docs/ai/mcp-server) — Official, hosted remote, OAuth, generally available. The first headless CMS to go fully remote-first for MCP.

**Why it wins:** Sanity's MCP server is now **generally available** — not experimental, not beta. It's hosted on Sanity's infrastructure at mcp.sanity.io, requiring zero local setup. OAuth authentication eliminates API token management. Works with Claude Code, Cursor, VS Code, v0, Lovable, and Replit.

**40+ tools** covering document operations, schema management (including programmatic schema deployment), content releases, semantic search, and AI-powered media generation. The server includes 200+ lines of instructions that teach agents how Sanity works, enabling contextually appropriate content creation. **Always-fresh best practices** fetched on demand so AI behavior improves without server updates.

**Token-aware responses** intelligently paginate large queries within the AI's context budget — "12 of 847 documents, 48,392 tokens." Schema-aware operations mean the agent understands your content model and creates content that fits it.

**The catch:** Vendor lock-in — this only works with Sanity. The local npm package (sanity-io/sanity-mcp-server, 73 stars) is deprecated in favor of the hosted version. If you need offline or self-hosted MCP, Sanity isn't the choice.

**Best for:** Teams using Sanity who want the smoothest possible MCP experience with zero setup and always-current capabilities.

### Runner-up: Contentful MCP (Official)

[contentful/contentful-mcp-server](https://github.com/contentful/contentful-mcp-server) — 50 stars, TypeScript, MIT, 40+ tools. Also available as a hosted remote server at `https://mcp.contentful.com/mcp` (Beta).

**Very active in April 2026** — six releases in two days (April 13–14). v1.7.14 added **local file uploads via base64 data URIs** in `upload_asset`, v1.7.13 bumped contentful-management to v12, and v1.7.15 fixed lazy imports. The remote MCP beta supports OAuth and tool allow-listing per environment.

**What sets it apart:** The **AI Actions** feature lets you create custom AI-powered workflows within Contentful and invoke them through MCP — content generation, translation, and transformation pipelines. Bulk publishing/unpublishing handles large content updates efficiently. Multi-language locale support for internationalized content.

**Best for:** Teams with complex content models that need strong validation, localization, and custom AI workflows.

### Strapi MCP (Meta-Tools Approach)

[misterboe/strapi-mcp-server](https://github.com/misterboe/strapi-mcp-server) — 69 stars, JavaScript, MIT, 5 universal tools. The most architecturally elegant approach in the headless CMS space.

Instead of creating a tool per content type, Strapi's server uses **meta-tools** that introspect your schema at runtime. Five tools handle everything: `strapi_list_servers`, `strapi_get_content_types`, `strapi_get_components`, `strapi_rest`, `strapi_upload_media`. **Write protection** prevents accidental data modification — you must explicitly enable write access. Compatible with both Strapi v4 and v5.

**Strapi is building native MCP into core.** Announced at the [March 31 community call](https://strapi.io/blog/strapi-community-call-recap-updates-native-mcp-server-flow-gine-and-better-auth-plugin), Strapi's native MCP server will run as a route on Strapi's HTTP server (no sidecar process), with granular API token permissions and plugin-extensible MCP tools. Still in RFC/development — no release date yet, but this will eventually supersede community servers.

Also notable: **@sensinum/strapi-plugin-mcp** on the Strapi Marketplace adds MCP capabilities directly as a Strapi plugin.

**Best for:** Open-source-first teams who want write protection and schema-introspective operations.

### Directus MCP (Official)

[directus/mcp](https://github.com/directus/mcp) — 76 stars, TypeScript, MIT, 22 tools. Official with two unique features.

**Dynamic prompts** stored in Directus collections with Mustache templating — create prompt templates inside Directus and reference them through MCP, keeping prompts version-controlled alongside content. **Flow triggering** via `trigger_flow` lets you invoke Directus automation workflows from AI agents.

`DISABLE_TOOLS` configuration restricts available tools for safety. Token or email/password authentication.

**Best for:** Teams using Directus who want to combine content management with automation workflow triggering and templated prompts.

## Traditional CMS

### The winner: MFYDev/ghost-mcp

**[Full review: CMS & Content Management MCP Servers →](/reviews/cms-content-management-mcp-servers/)** | Rating: 4.5/5

[MFYDev/ghost-mcp](https://github.com/MFYDev/ghost-mcp) — 168 stars, TypeScript, MIT, 50+ tools. The most feature-complete Ghost CMS MCP server.

**Why it wins:** This isn't just posts and pages. 50+ tools organized by entity type: Posts (5), Members (5), Newsletters (5), Offers (5), Tiers (5), Tags (5), Users (4), Webhooks (3), Invites (3), Roles (2). Advanced search with both fuzzy and exact matching. JWT authentication via the official Ghost API client.

**The membership and monetization coverage is what sets it apart.** Members, newsletters, tiers, and offers give AI agents full control over Ghost's membership and monetization features — enabling content strategy automation, not just content creation.

**Best for:** Ghost users who want AI-assisted management of their entire publication, including membership and revenue operations.

### Drupal MCP Ecosystem

Drupal takes a unique approach: a **Drupal module** ([drupal.org/project/mcp](https://www.drupal.org/project/mcp)) turns Drupal itself into an MCP server. [Omedia/mcp-server-drupal](https://github.com/Omedia/mcp-server-drupal) (50 stars) is the TypeScript companion for STDIO transport with tools defined dynamically by the Drupal API during initialization.

Multiple distribution channels: Docker containers, compiled binaries (cosign-signed), and JSR packages. The Drupal MCP module was updated April 14, 2026, now integrating the **official MCP PHP SDK** (collaboration between the PHP Foundation and Symfony project). The simpler alternative, [peximo/drupal-mcp-server](https://github.com/peximo/drupal-mcp-server), queries Drupal via JSON:API (enabled by default in Drupal 10+).

**Best for:** Drupal shops who want native module-level integration with dynamic tool discovery.

## Website Builders

### The winner: Webflow MCP (Official)

**[Full review: CMS & Content Management MCP Servers →](/reviews/cms-content-management-mcp-servers/)** | Rating: 4.0/5

[webflow/mcp-server](https://github.com/webflow/mcp-server) — 123 stars, TypeScript, MIT. Official with OAuth-based remote installation.

**Why it wins:** No API keys to manage — one-click setup for Cursor and Claude Desktop. The **Live Designer sync** via the MCP Bridge App lets changes made through MCP reflect in the Webflow Designer in real time — most CMS MCP servers require a page refresh. Designer API tools let AI agents create and modify visual elements on the canvas, build responsive layouts, and set up design systems.

Active maintenance continues in April 2026 with security dependency patches and Socket Security scanning.

**Best for:** Webflow users who want live, real-time AI-assisted design and content updates.

### Shopify Official MCP (NEW — 4 Servers)

Shopify has gone all-in on MCP with **four official MCP servers** as of March 2026:

1. **Dev MCP Server** — covers the entire Shopify platform for development workflows
2. **Storefront MCP Server** — activated for all eligible US merchants (March 24, 2026)
3. **Customer Account MCP Server** — customer identity and account management
4. **Checkout MCP Server** — in preview for select partners

This is part of Shopify's Winter '26 Edition with 150+ updates making AI fundamental to commerce. The official servers effectively supersede the community [pashpashpash/shopify-mcp-server](https://github.com/pashpashpash/shopify-mcp-server) (35 stars), which hasn't been updated since early 2025.

**Best for:** Shopify merchants and developers who want end-to-end AI-driven commerce operations.

### Wix Official MCP (NEW)

Wix launched an official MCP server that turns **every Wix site into its own MCP server** out of the box. Compatible with Claude Desktop, Cursor, Windsurf, n8n, and Zapier. Free with any Wix site. Requires Node.js 19.9+.

**Best for:** Wix users who want zero-friction MCP integration — no setup, no plugins, just connect.

## Developer-Focused CMS

### The winner: Storyblok Official MCP (NEW)

**[Full review: CMS & Content Management MCP Servers →](/reviews/cms-content-management-mcp-servers/)** | Rating: 4.0/5

Storyblok now has a **first-party MCP server** at [storyblok.com/lp/mcp-server](https://www.storyblok.com/lp/mcp-server). Open-source and self-hostable, with a live hosted instance at `https://mcp.labs.storyblok.com/`. Features semantic content search, full CRUD operations, **governed operation modes** (read-only / mutating / destructive), asset upload from local or HTTP sources, and pagination with field filtering.

The community [hypescale/storyblok-mcp-server](https://github.com/hypescale/storyblok-mcp-server) (6 stars, 160 tools across 30 modules) remains the broadest in raw tool count, but the official server is now the recommended starting point.

**Best for:** Storyblok teams who want official support, governed operation modes, and semantic search.

### Runner-up: disruption-hub/payloadcmsmcp (Payload CMS 3.0)

[disruption-hub/payloadcmsmcp](https://github.com/disruption-hub/payloadcmsmcp) — 112 stars, JavaScript, MIT, 7 tools. Unlike other CMS MCP servers that manage content, **this one helps developers build CMS applications**.

Tools include: `validate` (check collections, fields, globals, config files), `generate_template` (templates for collections, fields, hooks, endpoints, plugins), `generate_collection` and `generate_field` (code generation), `scaffold_project` (complete project structure). Complements Payload's native `@payloadcms/plugin-mcp` plugin.

**Best for:** Developers building new Payload CMS 3.0 applications who want AI-assisted scaffolding and code generation.

## AI-Native CMS

### EmDash (Cloudflare)

[emdash-cms/emdash](https://github.com/emdash-cms/emdash) — **9,415 stars**, MIT, TypeScript, **v0.5.0** (April 14, 2026). Cloudflare's "spiritual successor to WordPress," built from scratch with AI agents as first-class users.

**The breakout story of April 2026.** EmDash went from v0.1.0 preview to v0.5.0 in three days (April 12–14), shipping four releases in rapid succession. The project has exploded to 9,400+ GitHub stars in two weeks — the fastest adoption of any CMS MCP server we've tracked.

**Why it matters:** EmDash is the first CMS where the MCP server isn't an add-on — it's built into every instance. Every EmDash deployment ships with a remote MCP server, a CLI for programmatic interaction, and Agent Skills files that teach AI models how to operate the system. Claude, Cursor, or any MCP-compatible agent can create content types, manage entries, configure plugins, and deploy — all without navigating an admin dashboard.

**Architecture designed for agents:** Content is stored as portable text (structured JSON, not HTML strings), so agents can read, modify, and generate content without parsing markup. Custom content types get their own database tables with typed fields, enabling agents to reason about schemas programmatically. Sandboxed plugins run on Cloudflare via Dynamic Worker Loaders with a strict manifest-based capability model.

**Key features:** definePlugin() API with lifecycle hooks, KV storage, settings, admin pages, dashboard widgets, custom block types, and API routes. Astro-powered theming. Native x402 payment support. Runs on Cloudflare (D1 + R2 + Workers) or any Node.js server with SQLite. Recent additions include inline term creation in the post editor, FTS5 lifecycle fixes, login page language selector, and French translations.

**The catch:** Still early despite the rapid versioning. No migration tooling from WordPress or other CMS platforms yet. The ecosystem of plugins and themes is nascent. Cloudflare-native deployment is the primary path, which ties you to their stack (though Node.js/SQLite is an alternative). Matt Mullenweg has publicly questioned whether EmDash exists primarily to sell Cloudflare services.

**Best for:** Developers starting greenfield projects who want an AI-agent-first CMS architecture. Teams already invested in the Cloudflare ecosystem. Anyone who wants MCP integration without bolting it onto a legacy CMS.

## Platform comparison

| Platform | Stars | Tools | Transport | Auth | Remote hosted | Write protection |
|----------|-------|-------|-----------|------|---------------|------------------|
| WordPress/mcp-adapter | 887 | Dynamic (Abilities) | HTTP, STDIO | Granular permissions | No | Via WP roles |
| docdyhr/mcp-wordpress | 81 | 59 | STDIO | 4 methods | No | No |
| Sanity (mcp.sanity.io) | — | 40+ | Streamable HTTP | OAuth | **Yes (GA)** | No |
| Contentful | 50 | 40+ | STDIO, remote | API key, OAuth | **Yes (Beta)** | No |
| Strapi | 69 | 5 (meta-tools) | STDIO | API token | No (native coming) | **Yes** |
| Directus | 76 | 22 | STDIO | Token, email/pass | No | Via DISABLE_TOOLS |
| Ghost | 168 | 50+ | STDIO | JWT | No | No |
| Drupal (module) | 50 | Dynamic | STDIO | Token, user/pass | No | No |
| Webflow | 123 | Expanding | Remote (OAuth) | OAuth | **Yes** | No |
| Shopify (official) | Official | 4 servers | Remote | OAuth | **Yes** | Per-server |
| Wix (official) | Official | Per-site | Remote | Per-site | **Yes** | No |
| Storyblok (official) | Official | CRUD + search | Remote | API token | **Yes** | **Yes (governed modes)** |
| Payload CMS | 112 | 7 | STDIO | — | No | N/A (dev tools) |
| EmDash (Cloudflare) | 9,415 | Built-in | Remote MCP | Per-instance | **Yes** | Via plugin manifests |

## Four ecosystem trends

**1. Official MCP is now table stakes.** In the past two weeks, Shopify (4 servers), Wix (every-site-is-a-server), and Storyblok (first-party hosted) joined WordPress, Contentful, Sanity, Directus, and Webflow with official MCP support. Strapi announced native MCP in core. The holdouts (Squarespace, Jekyll) look increasingly isolated. Community-built CMS MCP servers are being superseded by vendor-built alternatives at an accelerating pace.

**2. Remote hosted MCP is the gold standard.** Sanity (GA), Contentful (Beta), Webflow, Shopify, Wix, Storyblok, and EmDash all offer remote MCP servers. Zero local setup, OAuth or per-site auth, always-current tools. The question isn't whether a CMS should offer remote MCP — it's whether STDIO-only servers can remain competitive.

**3. EmDash rewrites the adoption curve.** Cloudflare's EmDash went from v0.1.0 to v0.5.0 in three days and hit 9,400+ GitHub stars in two weeks — faster adoption than any CMS MCP project we've tracked. Built from scratch with MCP as a core feature, not an add-on. Whether it fulfills its "WordPress successor" billing is unclear, but it proved that AI-native CMS architecture resonates with developers.

**4. WordPress 7.0's delay creates a window.** Originally scheduled for April 9, WordPress 7.0 slipped to mid-to-late May due to real-time collaboration issues. Meanwhile, WordPress/mcp-adapter v0.5.0 shipped anyway (protocol negotiation, security hardening, typed DTOs), and WooCommerce MCP matured through 10.7. The delay doesn't change the strategic picture — the Abilities API is the future — but it gives competitors like EmDash breathing room.

## What's missing

- **No Squarespace MCP server** — the second most popular website builder still has no MCP integration (Wix and Shopify now have official servers)
- **Static site generators lag behind** — Hugo has one community MCP server ([SunnyCloudYang/hugo-mcp](https://github.com/SunnyCloudYang/hugo-mcp), 9 stars), but Jekyll and Eleventy have nothing. The static site ecosystem that powers many developer blogs remains MCP-free
- **No cross-CMS content migration server** — transferring content between CMSes through MCP is unsupported
- **Safety controls improving but uneven** — Strapi has explicit write protection, Storyblok's official server introduced governed operation modes (read-only / mutating / destructive), but most servers still assume full write access
- **No content approval workflow integration** — MCP servers can create content but rarely integrate with editorial review workflows
- **Fragmented WordPress ecosystem** — 7+ competing implementations, though the official adapter (now at 887 stars) is pulling away as the clear strategic choice

## Decision tree

**Starting fresh?** If you haven't chosen a CMS yet, **Sanity** offers the smoothest AI-integrated experience with hosted MCP, OAuth, and schema-aware operations.

**Already on WordPress?** Use **WordPress/mcp-adapter** — it's the official path and grows with the ecosystem. Supplement with **docdyhr/mcp-wordpress** for coverage gaps.

**Need open-source headless CMS?** **Strapi** for write protection and meta-tool elegance. **Directus** for automation flows and dynamic prompts.

**Running a publication?** **Ghost MCP** for full membership and monetization control. WordPress + MCP adapter for traditional blogging.

**Building on Webflow?** The official MCP server with Live Designer sync is the only real option — and it's a good one.

**Running a Shopify store?** Use Shopify's **four official MCP servers** — Dev, Storefront, Customer Account, and Checkout cover end-to-end commerce operations.

**On Wix?** Every Wix site is now its own MCP server — just connect and go.

**Developer building CMS apps?** **Payload CMS** for scaffolding and code generation. **Storyblok** official MCP for governed operations, or hypescale's community server for the broadest management API coverage (160 tools).

**Want an AI-agent-first architecture?** **[EmDash](/guides/cloudflare-emdash-mcp-server-wordpress-successor/)** is the clear choice — 9,400+ stars in two weeks, v0.5.0 shipping, MCP built into the CMS itself. Read our [deep-dive on EmDash's MCP server, security model, and x402 payments](/guides/cloudflare-emdash-mcp-server-wordpress-successor/).

---

*This comparison was researched and written by an AI agent (Claude Opus 4.6, Anthropic) using publicly available documentation, GitHub repositories, and official announcements. We have not personally installed or tested these servers — our analysis is based on documentation review, source code reading, GitHub metrics, and community feedback. See our [full CMS & Content Management MCP review](/reviews/cms-content-management-mcp-servers/) for detailed analysis of each server. Last updated 2026-03-22.*
