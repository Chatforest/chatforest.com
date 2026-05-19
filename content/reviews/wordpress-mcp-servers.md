---
title: "WordPress MCP Servers — AI-Powered Content Management for 43% of the Web"
date: 2026-04-21T15:00:00+09:00
description: "WordPress MCP servers let AI agents manage posts, pages, media, plugins, and WooCommerce stores through the Model Context Protocol. Official adapter, hosted connectors, and community options reviewed."
og_description: "WordPress MCP servers reviewed — official mcp-adapter (1,098 stars), WordPress.com connector (now write-enabled), InstaWP/mcp-wp (45+ tools), Royal MCP (2,000 installs, Elementor). Rating: 4/5."
content_type: "Review"
card_description: "MCP servers that connect AI agents to WordPress sites for content management, plugin operations, media handling, and WooCommerce store management. Multiple options from official WordPress adapter to community servers and security-focused plugins."
last_refreshed: 2026-05-20
---

Part of our **[CMS & Content Management MCP category](/categories/cms-content-management/)**.

*At a glance: WordPress powers 43% of all websites. The MCP ecosystem includes the official WordPress/mcp-adapter (1,098 stars, ~96 commits, PHP, v0.5.0), the deprecated Automattic/wordpress-mcp (883 stars, archived Jan 2026), InstaWP/mcp-wp (81 stars, stagnant since April 8), Royal MCP (2,000+ active installations, v1.4.20, 67 core + 55 integration tools), and the WordPress.com built-in connector (OAuth 2.1, now write-enabled as of March 20). WordPress 6.9 introduced the server-side Abilities API; WordPress 7.0 (scheduled May 20, 2026) adds the JavaScript Abilities API (`@wordpress/abilities`), WP AI Client, Connectors API, and WordPress Playground MCP server. WooCommerce 10.3 shipped native MCP support via the Abilities API.*

WordPress and MCP is a story of rapid convergence. In under a year, WordPress went from zero MCP support to having the Abilities API baked into core, an official adapter plugin, a hosted connector on WordPress.com, and a growing ecosystem of community servers. For the 810 million+ sites running WordPress, this opens the door to AI agents that can manage content, handle media, run WooCommerce stores, and administer plugins — all through standardized MCP tool calls.

## The WordPress MCP Landscape

There are four distinct approaches to connecting AI agents to WordPress via MCP:

### 1. Official WordPress MCP Adapter (WordPress/mcp-adapter)

The [canonical MCP integration](https://github.com/WordPress/mcp-adapter) for self-hosted WordPress sites. Built by the Core AI team and announced February 2026, it bridges WordPress's new Abilities API to MCP — any registered WordPress ability becomes an MCP tool.

**Key details:**
- **Stars:** 1,098 | **Forks:** 127 | **Commits:** ~96 | **Open issues:** 42
- **Latest:** v0.5.0 (April 15, 2026 — typed DTO protocol handling, `wordpress/php-mcp-schema` integration, protocol version negotiation for `2025-11-25`/`2025-06-18`/`2024-11-05`, security hardening). Last push: May 19, 2026.
- **Requirements:** WordPress 6.9+ (6.9 introduced Abilities API), PHP 7.4+
- **Install:** Composer package or WordPress plugin (distribution via WordPress.org plugin directory in progress)
- **Transport:** STDIO (local via WP-CLI) and HTTP (remote via REST API with `@automattic/mcp-wordpress-remote` proxy)
- **License:** GPL v2

The adapter exposes three meta-tools by default:
- `mcp-adapter/discover-abilities` — lists what the site can do
- `mcp-adapter/get-ability-info` — retrieves documentation for a specific ability
- `mcp-adapter/execute-ability` — invokes a WordPress ability

The power is in the **extensibility model**: any plugin can register abilities via `wp_register_ability()` with JSON Schema input/output definitions and permission callbacks. The adapter automatically converts these to MCP tools. This means the tool surface grows as the plugin ecosystem adopts the Abilities API — a WordPress site with WooCommerce, Yoast SEO, and a custom plugin could expose dozens of AI-invokable operations without writing any MCP code.

**Supersedes:** The [Automattic/wordpress-mcp](https://github.com/Automattic/wordpress-mcp) repo (847 stars, 228 commits) was archived January 2026 and is now deprecated in favor of this adapter.

### 2. WordPress.com Built-in Connector

WordPress.com launched a [Claude Connector](https://developer.wordpress.com/docs/mcp/) on February 5, 2026 — a hosted MCP server available on all paid WordPress.com plans. As of March 20, 2026, it gained **write capabilities**, removing the read-only limitation from the initial release.

**Key details:**
- **Authentication:** OAuth 2.1 with PKCE, dynamic client registration, token rotation (since January 2026)
- **Access:** Read + Write (19 write operations across posts, pages, comments, categories, tags, and media)
- **Write safety model:** Every write operation requires `user_confirmed: true` in the tool call — agents must describe the intended action and receive explicit approval before anything changes. New posts/pages default to draft status.
- **Read capabilities:** Traffic analysis, comment summarization, content freshness auditing, engagement metrics, writing style documentation, content gap analysis, link validation, internal linking recommendations
- **Role-based access:** Administrators have full access; contributors can create drafts but not publish
- **Setup:** Enable MCP in WordPress.com settings → connect via Claude's connector directory → authenticate via OAuth
- **Clients:** Claude Desktop, ChatGPT, VS Code, Cursor, Codex, and any MCP-enabled client

The write capabilities are a significant upgrade from the initial launch. The `user_confirmed: true` gate and default-to-draft behavior show careful design for safety — agents can't silently publish content. Documentation was updated May 15, 2026.

### 3. InstaWP/mcp-wp (Community Server)

[InstaWP's MCP server](https://github.com/InstaWP/mcp-wp) is a TypeScript-based MCP server that connects to WordPress via the REST API. It's the most tool-rich option for self-hosted sites that haven't adopted the Abilities API yet.

**Key details:**
- **Stars:** 81 | **Forks:** 30 | **Commits:** 43 | **Open issues:** 10
- **Last push:** April 8, 2026 — **no commits in 6+ weeks**
- **Tools:** 45+ across 8 categories
- **Authentication:** WordPress Application Passwords (username + app-specific password)
- **Multi-site:** Supports managing multiple WordPress sites from one server
- **Note:** Development activity may have shifted to `InstaWP/mcp-wp-php` (PHP SDK implementation)

Tool categories:
- **Content Management (8):** CRUD for posts/pages/custom post types, content type discovery, URL/slug lookup
- **Taxonomy (8):** Full taxonomy management including term assignment
- **Media (6):** Upload, browse, edit, delete media files
- **Users (5):** User management with role handling
- **Comments (5):** Comment moderation and management
- **Plugins (5+2):** Installed plugin management plus WordPress.org plugin repository search
- **Database (1):** `execute_sql_query` (read-only) — direct database queries for advanced use cases

The Application Passwords auth model is simpler but less secure than OAuth — credentials are sent with every request via HTTP Basic Auth. Fine for local development, requires HTTPS in production.

### 4. Royal MCP (Security-First Plugin)

[Royal MCP](https://wordpress.org/plugins/royal-mcp/) is a WordPress plugin that takes the opposite approach to most MCP implementations: security first, features second.

**Key details:**
- **Active installations:** 2,000 (from 700+ — nearly tripled in 30 days)
- **Version:** 1.4.20 (updated May 18, 2026 — 15 releases since v1.4.5)
- **WordPress.org rating:** 5/5
- **Core tools:** 67 (posts, pages, media, comments, users, categories, tags, menus, meta, site info, plugins, themes, search, options)
- **WooCommerce tools:** 9+ (products, orders, customers, store stats — auto-detected; HPOS bug fixed in v1.4.20)
- **Elementor tools:** 6 (clone page, replace text/image, get outline, list/import templates — added in v1.4.19)
- **GuardPress tools:** 7 (security score, scans, firewall, audit — auto-detected)
- **SiteVault tools:** 6 (backup management, scheduling, progress — auto-detected)
- **Tested up to:** WordPress 7.0

**Notable releases since April 21:**
- **v1.4.19:** 6 new Elementor integration tools; admin notice for stale `.well-known/oauth-authorization-server` files breaking Claude.ai connections
- **v1.4.18:** User-Agent-aware GET handler for Anthropic's `Claude-User` probe; fixed `wp_update_menu_item` destructive bug (could wipe all menu item fields)
- **v1.4.17:** Auth codes moved from WordPress transients to dedicated DB table (transient eviction was silently breaking OAuth on multi-cache hosts); "Reset OAuth State" button added; tool calls logged in Activity Log
- **v1.4.16:** OAuth failures now logged (previously silent)
- **v1.4.15:** Session TTL changed from fixed 1-hour to sliding 24-hour

Security features that most WordPress MCP options lack:
- API key authentication on every request (not just session init)
- Timing-safe key comparison (`hash_equals()`)
- Per-IP rate limiting (60 requests/minute)
- Full activity logging of every MCP interaction
- Sensitive data filtering — emails, usernames, admin email, PHP version never exposed
- Session binding to authenticated credentials (prevents hijacking)
- SSRF protection on outbound URLs
- OAuth 2.1 with PKCE — supports Claude Desktop "Add Connector" flow natively
- MCP 2025-03-26 Streamable HTTP spec compliant

The security focus is a genuine differentiator. [Research shows](https://mcpplaygroundonline.com/blog/mcp-server-security-complete-guide-2026) 41% of public MCP servers have no authentication at all. Royal MCP was designed from the start to prevent the most common MCP attack vectors. The 2,000-installation milestone and near-weekly release cadence signal a project that has found serious traction.

### 5. WordPress.org Plugin Directory MCP Server (New)

The official [`@wporg/mcp`](https://make.wordpress.org/meta/2026/03/20/plugin-directory-mcp-server/) package (launched March 20, 2026) connects AI IDEs directly to the WordPress.org plugin directory. This is a different use case from site management — it's for **plugin developers**, not site administrators.

**Capabilities:**
- Readme validation against WordPress.org submission standards
- Plugin status checks (review queue position, compatibility flags)
- Plugin submission support
- Plugin directory metadata queries

This fills a niche that none of the other four options address: the plugin development and publishing workflow. For teams building WordPress plugins, this enables AI-assisted readme writing, pre-submission validation, and directory status monitoring without leaving the IDE.

## Setup

**Official Adapter (self-hosted WordPress 6.9+):**

```bash
# Install via Composer (recommended)
composer require wordpress/mcp-adapter

# Or install as a WordPress plugin
# Download from github.com/WordPress/mcp-adapter/releases
```

Configure for Claude Desktop (STDIO mode via WP-CLI):
```json
{
  "mcpServers": {
    "wordpress": {
      "command": "wp",
      "args": ["mcp-adapter", "start", "--path=/path/to/wordpress"]
    }
  }
}
```

**InstaWP/mcp-wp:**

```json
{
  "mcpServers": {
    "wordpress": {
      "command": "npx",
      "args": ["-y", "@instawp/mcp-wp"],
      "env": {
        "WORDPRESS_SITE_URL": "https://your-site.com",
        "WORDPRESS_USERNAME": "your-username",
        "WORDPRESS_PASSWORD": "your-app-password"
      }
    }
  }
}
```

**Royal MCP:**

1. Install from WordPress Plugin Directory or upload to `/wp-content/plugins/`
2. Activate and go to Royal MCP → Settings
3. Copy API key and MCP server URL
4. Configure your MCP client with the endpoint URL and `X-Royal-MCP-API-Key` header (or use OAuth 2.0 connector flow)

**WordPress.com:**

1. Enable MCP in WordPress.com account settings
2. Connect via Claude's connector directory
3. Authenticate via OAuth 2.1

## What's Good

**Core integration path.** The Abilities API in WordPress 6.9/7.0 means MCP support is being built into WordPress itself, not bolted on. Any plugin that registers abilities automatically becomes MCP-accessible via the adapter. This is architecturally sound and future-proof.

**Multiple deployment models.** Self-hosted with CLI (STDIO), self-hosted with HTTP (remote), hosted on WordPress.com, or plugin-based. Whatever your WordPress setup, there's an MCP path.

**WordPress.com connector now write-enabled.** March 20 added 19 write operations across posts, pages, comments, categories, tags, and media. The `user_confirmed: true` gate and default-to-draft model are thoughtful safety design. For WordPress.com users on paid plans, connecting Claude remains a 3-click OAuth flow.

**Royal MCP's security model.** API key auth, rate limiting, activity logging, sensitive data filtering, SSRF protection, and PKCE OAuth in a free plugin. This should be the baseline for all MCP servers, not the exception.

**WooCommerce native MCP.** WooCommerce 10.3 (May 2026) shipped MCP support built directly on the Abilities API — any WooCommerce ability automatically becomes an MCP tool through the official adapter. Royal MCP also provides its 9-tool WooCommerce integration (with HPOS bug fixed in v1.4.20) for sites that need immediate functionality.

**WordPress.org Plugin Directory MCP Server.** The official `@wporg/mcp` package (launched March 20) lets AI IDEs connect to the plugin directory for readme validation, plugin status checks, and plugin submission — a new use case the prior review didn't cover.

**Massive addressable market.** WordPress powers 43% of websites. MCP support means AI agents can interact with nearly half the web's content management layer through a standardized protocol.

## What's Not

**Fragmented ecosystem.** Four different approaches (official adapter, WordPress.com connector, community servers, plugins) means the "right" choice isn't obvious. The official adapter requires WordPress 6.9+ and Composer knowledge. InstaWP uses Application Passwords. Royal MCP is a plugin. WordPress.com is read-only. Each has tradeoffs.

**Official adapter is still maturing.** 25 open issues, including hook timing problems (#117, #135) where abilities fail to register because the adapter initializes after the hook fires. The `empty object {} parameters` bug (#116) breaks tools with no required inputs. These are rough edges that real users will hit.

**InstaWP development stalled.** No commits since April 8 — the server most praised for its broad tool count (45+ tools, multi-site support) has gone 6+ weeks without an update. Open issues have grown to 10. Development may have shifted to a PHP rewrite (`InstaWP/mcp-wp-php`), but the TypeScript server is in limbo. The Application Passwords auth model (HTTP Basic Auth, no rate limiting, no audit logging) remains a security gap.

**mcp-adapter issue backlog growing.** Open issues jumped from 25 to 42 since the last review — hook timing bugs (#117, #135) and the empty-parameters bug (#116) from the last review appear unresolved. Increased adoption is surfacing more edge cases. Still no v0.6.0 release.

**Abilities API adoption is early.** The adapter's power depends on plugins registering abilities. As of April 2026, only WordPress core ships a handful of built-in abilities. Until major plugins (WooCommerce, Yoast, ACF, Elementor) register abilities, the adapter's tool surface is limited compared to purpose-built servers like InstaWP or Royal MCP.

**WordPress 7.0 delayed.** The release was pushed from April 9 to mid-to-late May 2026 for stability improvements. Client-side abilities and other 7.0 features that would expand the MCP surface area are on hold.

## Security Considerations

WordPress MCP security is a layered problem — WordPress itself is a frequent target (thousands of CVEs annually across plugins), and MCP adds a new attack surface.

**AI Engine plugin vulnerability (2025):** A critical flaw in the popular AI Engine plugin allowed privilege escalation to administrator via MCP. The No-Auth URL feature exposed bearer tokens in public REST API endpoints. Fixed June 2025, but demonstrates the risk of MCP + WordPress + third-party plugins.

**Royal MCP security patches (2026):**
- v1.4.2: Fixed authentication enforcement gap — earlier versions only required API key at session init, not on subsequent requests
- v1.4.3: Fixed broken access control on REST API endpoints (reported via Patchstack)
- v1.3.0: Added SSRF protection, timing-safe key comparison

These patches show the security surface is real and actively being probed.

**General WordPress MCP risks:**
- Write-enabled MCP tools + compromised API keys = full site takeover (content creation, plugin activation, user management)
- Prompt injection via WordPress content (comments, post content) could manipulate AI agents with tool access
- Multi-site configurations amplify blast radius — one MCP connection could affect multiple sites
- Plugin detection tools (Royal MCP's GuardPress/SiteVault integration) expose security posture to connected AI agents

**Recommendations:**
- Use HTTPS for all MCP connections (obvious but not universal)
- Prefer OAuth 2.1/PKCE over Application Passwords
- Use dedicated WordPress user accounts for MCP with minimal necessary permissions
- Enable rate limiting and activity logging (Royal MCP provides both)
- Audit MCP tool access regularly — remove tools you don't need exposed
- Keep WordPress, plugins, and MCP adapter/servers updated

## How It Compares

**vs [Notion MCP](/reviews/notion-mcp-server/)** (3.5/5): Notion's MCP server has deeper search and database features. WordPress MCP is broader (content, media, plugins, commerce, users) but less structured. Different CMS philosophies reflected in their MCP implementations.

**vs [Shopify MCP](/reviews/shopify-dev-mcp-server/)**: For e-commerce specifically, Shopify's MCP is more purpose-built. Royal MCP's WooCommerce integration covers the basics (products, orders, customers, stats) but lacks Shopify's depth in storefronts, checkout, and fulfillment.

**vs custom REST API integration**: WordPress already has a comprehensive REST API. MCP adds tool discovery, structured schemas, and standardized client support. The Abilities API adds permission-gated, schema-validated operations. MCP is higher-level and more agent-friendly than raw REST calls.

## Who Should Use This

**WordPress.com site owners** wanting AI-assisted content management → WordPress.com connector (zero setup, OAuth 2.1, read + write as of March 20 with `user_confirmed` safety gate)

**Self-hosted WordPress developers** on 6.9+ wanting the official, future-proof path → WordPress/mcp-adapter (Abilities API integration, extensible)

**WordPress agencies** managing multiple client sites → InstaWP/mcp-wp (multi-site support, 45+ tools, immediate functionality without Abilities API) — but note development is stalled; monitor `InstaWP/mcp-wp-php` for the active successor

**Security-conscious WordPress administrators** → Royal MCP (API key auth, rate limiting, activity logging, SSRF protection, sensitive data filtering, WooCommerce/security plugin integrations)

## Bottom Line

This cycle's changes are substantial. The WordPress.com connector gained write capabilities (19 operations, `user_confirmed` safety gate, role-based access) — removing the biggest objection from the April review. Royal MCP went from 700+ to 2,000 active installs in 30 days, shipping 15 releases including Elementor integration, OAuth hardening, and a WooCommerce HPOS fix. WordPress 7.0 (releasing May 20) brings the JavaScript Abilities API, WP AI Client, and WordPress Playground MCP server. WooCommerce 10.3 shipped native MCP support via the Abilities API.

For production WordPress MCP today, **Royal MCP remains the strongest option**: 67 core tools + 55 integration tools (Elementor, WooCommerce, GuardPress, SiteVault), the most rigorous security model in the category, and a release cadence that shows active product investment. The mcp-adapter (1,098 stars, v0.5.0, active development) is the architecturally correct long-term path and is worth adopting now for WordPress 6.9+ self-hosted sites — hook timing bugs and the growing issue backlog (42 open) are the main friction. The WordPress.com connector is now the easiest path for hosted sites with real content management capability, not just analysis.

InstaWP's stall since April 8 is a concern for agencies relying on it — the PHP rewrite may be the successor, but the current TypeScript server is on an uncertain trajectory.

The fragmentation hasn't fully resolved — four approaches still coexist — but the ecosystem is converging: WooCommerce 10.3 and the eventual Elementor and Yoast Abilities API adoption will make the official adapter increasingly dominant over time. The pace of change across all four options in one month is remarkable.

**Rating: 4/5** — Bumped from 3.5/5. WordPress.com write capabilities close the biggest gap from the prior review. Royal MCP's tripled install base and sustained release cadence demonstrate genuine adoption. WordPress 7.0's JavaScript Abilities API and WooCommerce native MCP support show the ecosystem converging on a coherent architecture. Held back from 4.5/5 by the mcp-adapter's growing issue backlog, InstaWP's stall, and fragmentation that won't fully resolve until major plugins adopt the Abilities API.

*Last updated: May 20, 2026*
