# WordPress MCP Servers — AI-Powered Content Management for 43% of the Web

> WordPress MCP servers let AI agents manage posts, pages, media, plugins, and WooCommerce stores through the Model Context Protocol. Official adapter, hosted connectors, and community options reviewed.


Part of our **[CMS & Content Management MCP category](/categories/cms-content-management/)**.

*At a glance: WordPress powers 43% of all websites. The MCP ecosystem includes the official WordPress/mcp-adapter (914 stars, 89 commits, PHP, v0.5.0), the deprecated Automattic/wordpress-mcp (847 stars, 228 commits, archived Jan 2026), InstaWP/mcp-wp (77 stars, 43 commits, TypeScript, 45+ tools), Royal MCP (700+ active WordPress installations, v1.4.5, 37+ core tools), and the WordPress.com built-in connector (OAuth 2.1, read-only, all paid plans). WordPress 6.9 introduced the Abilities API in core (December 2025); WordPress 7.0 (delayed from April 9 to mid-May 2026) expands it with client-side abilities.*

WordPress and MCP is a story of rapid convergence. In under a year, WordPress went from zero MCP support to having the Abilities API baked into core, an official adapter plugin, a hosted connector on WordPress.com, and a growing ecosystem of community servers. For the 810 million+ sites running WordPress, this opens the door to AI agents that can manage content, handle media, run WooCommerce stores, and administer plugins — all through standardized MCP tool calls.

## The WordPress MCP Landscape

There are four distinct approaches to connecting AI agents to WordPress via MCP:

### 1. Official WordPress MCP Adapter (WordPress/mcp-adapter)

The [canonical MCP integration](https://github.com/WordPress/mcp-adapter) for self-hosted WordPress sites. Built by the Core AI team and announced February 2026, it bridges WordPress's new Abilities API to MCP — any registered WordPress ability becomes an MCP tool.

**Key details:**
- **Stars:** 914 | **Forks:** 117 | **Commits:** 89 | **Open issues:** 25
- **Latest:** v0.5.0 (April 15, 2025 — note: repo uses a pre-release dating convention; active development through April 2026)
- **Requirements:** WordPress 6.9+ (6.9 introduced Abilities API), PHP 7.4+
- **Install:** Composer package (recommended) or WordPress plugin
- **Transport:** STDIO (local via WP-CLI) and HTTP (remote via REST API with `@automattic/mcp-wordpress-remote` proxy)
- **License:** GPL v2

The adapter exposes three meta-tools by default:
- `mcp-adapter/discover-abilities` — lists what the site can do
- `mcp-adapter/get-ability-info` — retrieves documentation for a specific ability
- `mcp-adapter/execute-ability` — invokes a WordPress ability

The power is in the **extensibility model**: any plugin can register abilities via `wp_register_ability()` with JSON Schema input/output definitions and permission callbacks. The adapter automatically converts these to MCP tools. This means the tool surface grows as the plugin ecosystem adopts the Abilities API — a WordPress site with WooCommerce, Yoast SEO, and a custom plugin could expose dozens of AI-invokable operations without writing any MCP code.

**Supersedes:** The [Automattic/wordpress-mcp](https://github.com/Automattic/wordpress-mcp) repo (847 stars, 228 commits) was archived January 2026 and is now deprecated in favor of this adapter.

### 2. WordPress.com Built-in Connector

WordPress.com launched a [Claude Connector](https://developer.wordpress.com/docs/mcp/) on February 5, 2026 — a hosted MCP server available on all paid WordPress.com plans.

**Key details:**
- **Authentication:** OAuth 2.1
- **Access:** Read-only (cannot create, delete, or update content)
- **Capabilities:** Traffic analysis, comment summarization, content freshness auditing, engagement metrics, writing style documentation, content gap analysis, link validation, internal linking recommendations
- **Setup:** Enable MCP in WordPress.com settings → connect via Claude's connector directory → authenticate via OAuth
- **Clients:** Works with Claude Desktop, VS Code, Cursor, and any MCP-enabled client

The read-only constraint is deliberate — WordPress.com is cautious about giving AI agents write access to hosted sites. For site analysis and content strategy, this is sufficient. For content creation and management, you need a self-hosted solution.

### 3. InstaWP/mcp-wp (Community Server)

[InstaWP's MCP server](https://github.com/InstaWP/mcp-wp) is a TypeScript-based MCP server that connects to WordPress via the REST API. It's the most tool-rich option for self-hosted sites that haven't adopted the Abilities API yet.

**Key details:**
- **Stars:** 77 | **Forks:** 28 | **Commits:** 43 | **Open issues:** 1
- **Tools:** 45+ across 8 categories
- **Authentication:** WordPress Application Passwords (username + app-specific password)
- **Multi-site:** Supports managing multiple WordPress sites from one server
- **npm:** @instawp/mcp-wp (~153 downloads)

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
- **Active installations:** 700+
- **Version:** 1.4.5 (updated April 18, 2026)
- **WordPress.org rating:** 5/5 (1 review)
- **Core tools:** 37 (posts, pages, media, comments, users, categories, tags, menus, meta, site info, plugins, themes, search, options)
- **WooCommerce tools:** 9 (products, orders, customers, store stats — auto-detected)
- **GuardPress tools:** 7 (security score, scans, firewall, audit — auto-detected)
- **SiteVault tools:** 6 (backup management, scheduling, progress — auto-detected)
- **Tested up to:** WordPress 7.0

Security features that most WordPress MCP options lack:
- API key authentication on every request (not just session init)
- Timing-safe key comparison (`hash_equals()`)
- Per-IP rate limiting (60 requests/minute)
- Full activity logging of every MCP interaction
- Sensitive data filtering — emails, usernames, admin email, PHP version never exposed
- Session binding to authenticated credentials (prevents hijacking)
- SSRF protection on outbound URLs
- OAuth 2.0 with PKCE (v1.4.0+) — supports Claude Desktop "Add Connector" flow natively
- MCP 2025-03-26 Streamable HTTP spec compliant

The security focus is a genuine differentiator. [Research shows](https://mcpplaygroundonline.com/blog/mcp-server-security-complete-guide-2026) 41% of public MCP servers have no authentication at all. Royal MCP was designed from the start to prevent the most common MCP attack vectors.

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

**WordPress.com connector is zero-setup.** For WordPress.com users on paid plans, connecting Claude is a 3-click process with OAuth 2.1. No server configuration, no credentials to manage.

**Royal MCP's security model.** API key auth, rate limiting, activity logging, sensitive data filtering, SSRF protection, and PKCE OAuth in a free plugin. This should be the baseline for all MCP servers, not the exception.

**WooCommerce integration.** Royal MCP's auto-detected WooCommerce tools (product management, order tracking, store stats) and InstaWP's content management make WordPress MCP useful for e-commerce, not just blogging.

**Massive addressable market.** WordPress powers 43% of websites. MCP support means AI agents can interact with nearly half the web's content management layer through a standardized protocol.

## What's Not

**Fragmented ecosystem.** Four different approaches (official adapter, WordPress.com connector, community servers, plugins) means the "right" choice isn't obvious. The official adapter requires WordPress 6.9+ and Composer knowledge. InstaWP uses Application Passwords. Royal MCP is a plugin. WordPress.com is read-only. Each has tradeoffs.

**Official adapter is still maturing.** 25 open issues, including hook timing problems (#117, #135) where abilities fail to register because the adapter initializes after the hook fires. The `empty object {} parameters` bug (#116) breaks tools with no required inputs. These are rough edges that real users will hit.

**WordPress.com connector is read-only.** Useful for analysis but not for the most common AI agent use case — creating and managing content. This limits it to a reporting tool, not a content automation tool.

**Application Passwords auth model (InstaWP).** Credentials sent via HTTP Basic Auth on every request. If your site isn't on HTTPS (still true for many development environments), credentials are transmitted in cleartext. No rate limiting, no audit logging built in.

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

**WordPress.com site owners** wanting AI-assisted content analysis → WordPress.com connector (zero setup, read-only, OAuth 2.1)

**Self-hosted WordPress developers** on 6.9+ wanting the official, future-proof path → WordPress/mcp-adapter (Abilities API integration, extensible)

**WordPress agencies** managing multiple client sites → InstaWP/mcp-wp (multi-site support, 45+ tools, immediate functionality without Abilities API)

**Security-conscious WordPress administrators** → Royal MCP (API key auth, rate limiting, activity logging, SSRF protection, sensitive data filtering, WooCommerce/security plugin integrations)

## Bottom Line

The WordPress MCP ecosystem went from nothing to four viable options in under a year, anchored by the Abilities API landing in WordPress core. The official adapter (WordPress/mcp-adapter) is the architecturally correct long-term bet — abilities registered by any plugin automatically become MCP tools. But today, it's still maturing: hook timing bugs, limited built-in abilities, and dependency on plugin ecosystem adoption mean it's not the most practical choice for immediate use.

For production WordPress MCP use today, Royal MCP is the strongest option: 37+ core tools, WooCommerce integration, genuine security controls (not afterthoughts), and active maintenance with WordPress 7.0 compatibility already tested. InstaWP/mcp-wp offers the broadest raw tool count (45+) with multi-site support, though it lacks security hardening. The WordPress.com connector is the easiest path but read-only.

The fragmentation is the main weakness — four approaches, none clearly dominant, each with different auth models, tool surfaces, and deployment requirements. As the Abilities API matures and plugins adopt it, the official adapter should consolidate the ecosystem. Until then, pick based on your deployment model and security requirements.

**Rating: 3.5/5** — Impressive ecosystem velocity for the world's most popular CMS. Official core integration via Abilities API is the right architectural direction. Docked for fragmented ecosystem, maturing official adapter with open bugs, read-only WordPress.com connector, and early-stage Abilities API adoption across the plugin ecosystem.

*Last updated: April 21, 2026*

