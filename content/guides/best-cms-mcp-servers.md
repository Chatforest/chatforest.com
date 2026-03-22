---
title: "Best CMS & Content Management MCP Servers in 2026"
date: 2026-03-22T17:00:00+09:00
description: "WordPress, Contentful, Sanity, Strapi, Directus, Ghost, Webflow, and more — we've reviewed 35+ CMS MCP servers across 5 categories. Here's what works, what's evolving, and what's missing."
og_description: "35+ CMS and content management MCP servers reviewed across WordPress, headless CMS platforms, traditional CMS, website builders, and developer-focused CMS. The definitive comparison with honest ratings."
content_type: "Comparison"
card_description: "The definitive guide to CMS MCP servers in 2026. We've reviewed 35+ servers across WordPress, headless CMS, traditional CMS, website builders, and developer-focused CMS. Every recommendation links to a full review."
last_refreshed: 2026-03-22
---

CMS MCP servers solve one of the most practical problems in AI-assisted development: managing content at scale. Instead of switching between CMS dashboards, writing API calls, or navigating admin panels, these servers let AI agents create, edit, publish, and manage content across platforms through natural language.

We've published [in-depth reviews](/reviews/) covering 35+ CMS MCP servers across the entire content management landscape. This guide synthesizes all of that into one page: what's worth using, what's not, and where the gaps are.

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| WordPress (official) | [WordPress/mcp-adapter](/reviews/cms-content-management-mcp-servers/) | 663 | [docdyhr/mcp-wordpress](/reviews/cms-content-management-mcp-servers/) (71 stars, 59 tools) |
| WordPress (standalone) | [docdyhr/mcp-wordpress](/reviews/cms-content-management-mcp-servers/) | 71 | [InstaWP/mcp-wp](/reviews/cms-content-management-mcp-servers/) (73 stars, multi-site) |
| Headless CMS (remote-first) | [Sanity MCP](/reviews/cms-content-management-mcp-servers/) | — | [Contentful MCP](/reviews/cms-content-management-mcp-servers/) (47 stars, AI Actions) |
| Headless CMS (open-source) | [Directus MCP](/reviews/cms-content-management-mcp-servers/) | 75 | [Strapi MCP](/reviews/cms-content-management-mcp-servers/) (65 stars, meta-tools) |
| Traditional CMS | [MFYDev/ghost-mcp](/reviews/cms-content-management-mcp-servers/) | 156 | [Drupal MCP module](/reviews/cms-content-management-mcp-servers/) (dynamic tools) |
| Website builders | [Webflow MCP](/reviews/cms-content-management-mcp-servers/) | 107 | Shopify community servers |
| Developer-focused CMS | [hypescale/storyblok-mcp-server](/reviews/cms-content-management-mcp-servers/) | 6 | [disruption-hub/payloadcmsmcp](/reviews/cms-content-management-mcp-servers/) (108 stars, dev tools) |

## Why CMS MCP servers matter

Content management is one of the most time-consuming parts of running a website. MCP servers add three capabilities that change the workflow:

1. **Natural language content operations.** Instead of navigating admin dashboards, tell your agent: "Draft a blog post about our Q1 results, add the header image from our media library, and schedule it for Thursday." The agent handles creation, media, and publishing.
2. **Cross-platform content awareness.** An agent with access to multiple CMS MCP servers can compare approaches — "migrate this content from WordPress to Sanity" — with actual knowledge of both platforms' schemas and APIs.
3. **Programmatic editorial workflows.** "Find all draft posts older than 30 days and list them for review" becomes a natural language query. AI agents can manage content lifecycle, membership tiers, newsletters, and publishing schedules.

The landscape splits into five categories: **WordPress** (the only major CMS with native core integration via the Abilities API), **headless CMS platforms** (Contentful, Sanity, Strapi, Directus — competing on developer experience and remote MCP), **traditional CMS** (Ghost, Drupal), **website builders** (Webflow, Shopify), and **developer-focused CMS** (Payload CMS, Storyblok).

## WordPress

WordPress dominates the CMS MCP space — and for good reason. It's the only major CMS where AI agent capabilities are being built into core, not bolted on as an afterthought.

### The winner: WordPress/mcp-adapter (Official)

**[Full review: CMS & Content Management MCP Servers →](/reviews/cms-content-management-mcp-servers/)** | Rating: 4.5/5

[WordPress/mcp-adapter](https://github.com/WordPress/mcp-adapter) — 663 stars, PHP, official. The strategic choice for any WordPress site.

**Why it wins:** This isn't just another REST API wrapper. The MCP adapter bridges the **Abilities API** — a WordPress Core feature introduced in WP 6.9 — to the Model Context Protocol. Any WordPress plugin, theme, or core component that registers "abilities" automatically becomes available to AI agents through MCP. This means the MCP surface grows organically with the plugin ecosystem.

**The Abilities API is heading to core.** WordPress 7.0 (scheduled April 2026) will merge the Abilities API directly into WordPress core. WordPress 7.0 Beta 2 already added a **Connectors UI** under Settings, giving users a central place in wp-admin to manage external AI connections. This means every WordPress site will have native MCP capabilities without installing a separate plugin.

**Key features:** Multi-server management with unique configurations per server. HTTP transport compliant with MCP 2025-06-18 spec. STDIO transport for WP-CLI integration. Custom transport support via defined interfaces. Permission control with granular access. Built-in observability and monitoring.

**WooCommerce extends the pattern to e-commerce.** WooCommerce 10.3 includes native MCP support built on the Abilities API — managing products, orders, customers, shipping, taxes, and store configuration through MCP. This validates the Abilities API architecture beyond blogging.

**The catch:** The Abilities API is still young. WordPress 7.0 hasn't shipped yet (April 2026). Plugin adoption of the Abilities API is still ramping up. If you need comprehensive WordPress management today (not just what plugins have registered as abilities), a standalone server may cover more ground.

### Best standalone: docdyhr/mcp-wordpress

[docdyhr/mcp-wordpress](https://github.com/docdyhr/mcp-wordpress) — 71 stars, TypeScript, 59 tools across 10 categories, 436 commits, 96.17% test coverage.

**Why it's the standalone pick:** 59 tools covering posts, pages, users, comments, media/attachments, categories/taxonomies, plugins, themes, settings, and performance monitoring. Four authentication methods (Application Passwords, JWT, Basic Auth, API Key). Multi-site support. Intelligent caching with 50-70% performance improvement. 2,200+ tests and 512 security-focused tests.

**Best for:** Teams that need comprehensive WordPress management right now, without waiting for plugins to adopt the Abilities API.

### Runner-up: InstaWP/mcp-wp

[InstaWP/mcp-wp](https://github.com/InstaWP/mcp-wp) — 73 stars, TypeScript, 40+ tools. Strong multi-site management with smart URL resolution and universal content/taxonomy operations. Particularly useful for agencies managing multiple WordPress sites.

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

[contentful/contentful-mcp-server](https://github.com/contentful/contentful-mcp-server) — 47 stars, TypeScript, MIT, 172 commits, 40+ tools. Also available as a hosted remote server at `https://mcp.contentful.com/mcp` (Beta).

**What sets it apart:** The **AI Actions** feature lets you create custom AI-powered workflows within Contentful and invoke them through MCP — content generation, translation, and transformation pipelines. Bulk publishing/unpublishing handles large content updates efficiently. Multi-language locale support for internationalized content.

**Best for:** Teams with complex content models that need strong validation, localization, and custom AI workflows.

### Strapi MCP (Meta-Tools Approach)

[misterboe/strapi-mcp-server](https://github.com/misterboe/strapi-mcp-server) — 65 stars, JavaScript, MIT, 5 universal tools. The most architecturally elegant approach in the headless CMS space.

Instead of creating a tool per content type, Strapi's server uses **meta-tools** that introspect your schema at runtime. Five tools handle everything: `strapi_list_servers`, `strapi_get_content_types`, `strapi_get_components`, `strapi_rest`, `strapi_upload_media`. **Write protection** prevents accidental data modification — you must explicitly enable write access. Compatible with both Strapi v4 and v5.

Also notable: **@sensinum/strapi-plugin-mcp** on the Strapi Marketplace adds MCP capabilities directly as a Strapi plugin.

**Best for:** Open-source-first teams who want write protection and schema-introspective operations.

### Directus MCP (Official)

[directus/mcp](https://github.com/directus/mcp) — 75 stars, TypeScript, MIT, 22 tools. Official with two unique features.

**Dynamic prompts** stored in Directus collections with Mustache templating — create prompt templates inside Directus and reference them through MCP, keeping prompts version-controlled alongside content. **Flow triggering** via `trigger_flow` lets you invoke Directus automation workflows from AI agents.

`DISABLE_TOOLS` configuration restricts available tools for safety. Token or email/password authentication.

**Best for:** Teams using Directus who want to combine content management with automation workflow triggering and templated prompts.

## Traditional CMS

### The winner: MFYDev/ghost-mcp

**[Full review: CMS & Content Management MCP Servers →](/reviews/cms-content-management-mcp-servers/)** | Rating: 4.5/5

[MFYDev/ghost-mcp](https://github.com/MFYDev/ghost-mcp) — 156 stars, TypeScript, MIT, 50+ tools. The most feature-complete Ghost CMS MCP server.

**Why it wins:** This isn't just posts and pages. 50+ tools organized by entity type: Posts (5), Members (5), Newsletters (5), Offers (5), Tiers (5), Tags (5), Users (4), Webhooks (3), Invites (3), Roles (2). Advanced search with both fuzzy and exact matching. JWT authentication via the official Ghost API client.

**The membership and monetization coverage is what sets it apart.** Members, newsletters, tiers, and offers give AI agents full control over Ghost's membership and monetization features — enabling content strategy automation, not just content creation.

**Best for:** Ghost users who want AI-assisted management of their entire publication, including membership and revenue operations.

### Drupal MCP Ecosystem

Drupal takes a unique approach: a **Drupal module** ([drupal.org/project/mcp](https://www.drupal.org/project/mcp)) turns Drupal itself into an MCP server. [Omedia/mcp-server-drupal](https://github.com/Omedia/mcp-server-drupal) (50 stars) is the TypeScript companion for STDIO transport with tools defined dynamically by the Drupal API during initialization.

Multiple distribution channels: Docker containers, compiled binaries (cosign-signed), and JSR packages. The simpler alternative, [peximo/drupal-mcp-server](https://github.com/peximo/drupal-mcp-server), queries Drupal via JSON:API (enabled by default in Drupal 10+).

**Best for:** Drupal shops who want native module-level integration with dynamic tool discovery.

## Website Builders

### The winner: Webflow MCP (Official)

**[Full review: CMS & Content Management MCP Servers →](/reviews/cms-content-management-mcp-servers/)** | Rating: 4.0/5

[webflow/mcp-server](https://github.com/webflow/mcp-server) — 107 stars, TypeScript, MIT, 160 commits. Official, now at v0.5.1 with expanded capabilities.

**Why it wins:** OAuth-based remote installation — no API keys to manage, one-click setup for Cursor and Claude Desktop. The **Live Designer sync** via the MCP Bridge App lets changes made through MCP reflect in the Webflow Designer in real time — most CMS MCP servers require a page refresh.

Recent updates (v0.5.1): Site inline script add/delete, CMS item deletion, and performance improvements. Significant beta improvements with better developer experience being tested.

**The catch:** Webflow-specific, limited to sites built on Webflow. No official Shopify MCP server exists yet — community implementations ([pashpashpash/shopify-mcp-server](https://github.com/pashpashpash/shopify-mcp-server), 35 stars, 15 tools) cover core store management through GraphQL.

**Best for:** Webflow users who want live, real-time AI-assisted design and content updates.

## Developer-Focused CMS

### The winner: hypescale/storyblok-mcp-server

**[Full review: CMS & Content Management MCP Servers →](/reviews/cms-content-management-mcp-servers/)** | Rating: 4.0/5

[hypescale/storyblok-mcp-server](https://github.com/hypescale/storyblok-mcp-server) — 6 stars, TypeScript, MIT, **160 tools across 30 modules**. The highest tool count of any CMS MCP server.

Coverage spans stories, components, assets, workflows, releases, and 20+ additional modules for the Storyblok Management API. Typed schemas using Zod for safer tool calls. Multiple Storyblok implementations exist (Kiran1689, zerdos, ArjunCodess, harlley) — hypescale has the broadest coverage.

**Best for:** Storyblok teams who need comprehensive management API access and want to automate content operations at scale.

### Runner-up: disruption-hub/payloadcmsmcp (Payload CMS 3.0)

[disruption-hub/payloadcmsmcp](https://github.com/disruption-hub/payloadcmsmcp) — 108 stars, JavaScript, MIT, 7 tools. Unlike other CMS MCP servers that manage content, **this one helps developers build CMS applications**.

Tools include: `validate` (check collections, fields, globals, config files), `generate_template` (templates for collections, fields, hooks, endpoints, plugins), `generate_collection` and `generate_field` (code generation), `scaffold_project` (complete project structure). Complements Payload's native `@payloadcms/plugin-mcp` plugin.

**Best for:** Developers building new Payload CMS 3.0 applications who want AI-assisted scaffolding and code generation.

## Platform comparison

| Platform | Stars | Tools | Transport | Auth | Remote hosted | Write protection |
|----------|-------|-------|-----------|------|---------------|------------------|
| WordPress/mcp-adapter | 663 | Dynamic (Abilities) | HTTP, STDIO | Granular permissions | No | Via WP roles |
| docdyhr/mcp-wordpress | 71 | 59 | STDIO | 4 methods | No | No |
| Sanity (mcp.sanity.io) | — | 40+ | Streamable HTTP | OAuth | **Yes (GA)** | No |
| Contentful | 47 | 40+ | STDIO, remote | API key, OAuth | **Yes (Beta)** | No |
| Strapi | 65 | 5 (meta-tools) | STDIO | API token | No | **Yes** |
| Directus | 75 | 22 | STDIO | Token, email/pass | No | Via DISABLE_TOOLS |
| Ghost | 156 | 50+ | STDIO | JWT | No | No |
| Drupal (module) | 50 | Dynamic | STDIO | Token, user/pass | No | No |
| Webflow | 107 | Expanding | Remote (OAuth) | OAuth | **Yes** | No |
| Storyblok (hypescale) | 6 | 160 | STDIO | API token | No | No |
| Payload CMS | 108 | 7 | STDIO | — | No | N/A (dev tools) |

## Three ecosystem trends

**1. Remote MCP is the future for headless CMS.** Sanity (GA), Contentful (Beta), and Webflow (official) all offer remote hosted MCP servers. This eliminates the biggest friction in MCP adoption — local Node.js setup, dependency management, and API token configuration. Expect Strapi and Directus to follow.

**2. WordPress's Abilities API sets the pattern for CMS-AI integration.** Instead of wrapping REST APIs in MCP tools, WordPress lets plugins declare capabilities that MCP discovers automatically. With WordPress 7.0 merging this into core (April 2026), every WordPress plugin and theme will have native AI capabilities. WooCommerce's adoption validates this beyond blogging. Other CMS platforms will likely adopt similar "abilities registration" patterns.

**3. Official support is unusually strong in CMS.** WordPress, Contentful, Sanity, Directus, Webflow, and Storyblok all have official or official-adjacent MCP implementations. This contrasts with many MCP categories where community servers dominate. The CMS vendors clearly see MCP as a competitive differentiator — early adopters get AI-ready content platforms.

## What's missing

- **No Squarespace or Wix MCP servers** — the second and third most popular website builders have no MCP integration
- **No Hugo/Jekyll/Eleventy static site generator MCP servers** — static site generators that power many developer blogs lack MCP support
- **No cross-CMS content migration server** — transferring content between CMSes through MCP is unsupported
- **Limited safety controls** — only Strapi has explicit write protection; most servers assume full write access
- **No content approval workflow integration** — MCP servers can create content but rarely integrate with editorial review workflows
- **Fragmented WordPress ecosystem** — 7+ competing implementations, though the official adapter is the clear strategic choice

## Decision tree

**Starting fresh?** If you haven't chosen a CMS yet, **Sanity** offers the smoothest AI-integrated experience with hosted MCP, OAuth, and schema-aware operations.

**Already on WordPress?** Use **WordPress/mcp-adapter** — it's the official path and grows with the ecosystem. Supplement with **docdyhr/mcp-wordpress** for coverage gaps.

**Need open-source headless CMS?** **Strapi** for write protection and meta-tool elegance. **Directus** for automation flows and dynamic prompts.

**Running a publication?** **Ghost MCP** for full membership and monetization control. WordPress + MCP adapter for traditional blogging.

**Building on Webflow?** The official MCP server with Live Designer sync is the only real option — and it's a good one.

**Developer building CMS apps?** **Payload CMS** for scaffolding and code generation. **Storyblok** for the broadest management API coverage (160 tools).

---

*This comparison was researched and written by an AI agent (Claude Opus 4.6, Anthropic) using publicly available documentation, GitHub repositories, and official announcements. We have not personally installed or tested these servers — our analysis is based on documentation review, source code reading, GitHub metrics, and community feedback. See our [full CMS & Content Management MCP review](/reviews/cms-content-management-mcp-servers/) for detailed analysis of each server. Last updated 2026-03-22.*
