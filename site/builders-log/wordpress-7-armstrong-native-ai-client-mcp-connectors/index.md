# WordPress 7.0 Armstrong: Native AI Is Now Core, Not a Plugin

> WordPress 7.0 Armstrong ships a built-in AI Client, a Connectors hub for managing OpenAI/Anthropic/Google API keys, and an MCP Adapter that makes any registered WordPress capability discoverable by Claude Code, Cursor, or any MCP client. AI is no longer a plugin layer — it's in core.


On May 20, 2026, WordPress 7.0 "Armstrong" shipped. For the first time in WordPress's 23-year history, AI is not a plugin — it's in core.

The release includes a built-in AI Client, a Connectors hub for managing provider API keys, and an MCP Adapter that bridges WordPress capabilities to any MCP client. The implications for builders who work with WordPress at scale, or who want to operate WordPress sites through AI agents, are material.

---

## What's Actually New

Three components shipped together in 7.0:

**WP AI Client** — A provider-agnostic interface in WordPress core for communicating with external AI models. Three providers are registered out of the box: OpenAI, Anthropic (Claude), and Google (Gemini). Any plugin built against the AI Client can use whichever provider the site owner has configured.

**Connectors hub** — A new screen in the WordPress admin dashboard where site owners enter API keys once. That entry propagates to every plugin using the AI Client. There's no longer a per-plugin credential management problem, and developers building AI features don't have to ship their own key management UX.

**MCP Adapter** — A package that bridges the WordPress Abilities API to the Model Context Protocol. Any capability registered through the Abilities API becomes discoverable and callable as an MCP tool by compatible MCP clients — including Claude Code, Cursor, Windsurf, and GitHub Copilot.

WordPress also ships its own MCP server for plugin developers, providing tools for plugin submission, readme validation, and submission status checks.

---

## The Abilities API: The Piece That Connects Everything

The Abilities API is the programmable surface that makes the MCP integration meaningful rather than ceremonial.

A WordPress "Ability" is a declared capability — publish a post, query posts, update site settings, manage media — that follows a defined schema: what the action does, what parameters it takes, what it returns, and what permissions it requires. When you register an Ability, the MCP Adapter automatically surfaces it as a tool in any connected MCP client.

What this means in practice: if a plugin developer registers an Ability called `ecommerce/create_order`, that action becomes available to Claude Code or Cursor without any additional integration work. The developer writes the Ability once; the MCP surface comes for free.

This is a fundamentally different model from how WordPress has handled integrations historically. The REST API exposed WordPress data. Abilities expose WordPress actions — with permissions and schemas baked in.

---

## For Builders: What Changed

**If you're running a WordPress site**, you can now connect Claude Code or any other MCP client and give it the ability to draft posts, manage media, or query content — without building any custom tooling. The connection goes through the Connectors hub and the built-in MCP server.

**If you're building WordPress plugins**, the Abilities API gives you a standard way to make your plugin's functionality accessible to AI agents. Previously, making a plugin AI-accessible meant building a custom API surface or hoping someone else built an MCP wrapper. Now there's a first-party path.

**If you're building workflows** that involve WordPress as a content layer, the provider-agnostic AI Client means you can use Claude on one site, OpenAI on another, and Gemini on a third — all from the same plugin codebase, with configuration at the site level.

---

## The MCP Angle

The MCP Adapter is the part of this release with the broadest implications for the agent ecosystem.

WordPress powers [roughly 43% of the web](https://w3techs.com/technologies/details/cm-wordpress). Most of that isn't developer-run Gatsby setups — it's content sites, editorial workflows, WooCommerce stores, and multi-site networks. These are environments where AI agents could take meaningful action (publishing, scheduling, updating product inventory, managing subscriptions) but where building bespoke integrations has been expensive and fragile.

The Abilities API + MCP Adapter changes the unit of work. Instead of building a WordPress-to-Claude integration from scratch, developers now build Abilities that work across the entire MCP ecosystem.

The practical constraint is adoption. The Abilities API is new; existing plugins don't have Abilities registered yet. The out-of-the-box MCP surface covers WordPress core operations. Third-party plugin coverage will grow over the next release cycle as developers adopt the API. For the most popular ecosystems — WooCommerce, Elementor, ACF — there will likely be Abilities packages appearing over the next few months.

---

## What the Connectors Hub Solves

Before 7.0, AI in WordPress was a plugin-layer problem. You might have one plugin using the OpenAI API, another using a different key from the same provider, a third hardcoding a model, and no unified view of what was being called or at what cost. Managing that across a multi-site network was particularly painful.

The Connectors hub moves provider credentials to the site (or network) level. You enter your Anthropic API key once. Every plugin using the AI Client inherits it. Budget control, key rotation, and provider switching are now sysadmin-level operations rather than plugin-by-plugin decisions.

This is the kind of infrastructure that makes AI features appropriate for managed hosting environments — where site owners don't want to think about AI plumbing, just AI features.

---

## Limitations Worth Knowing

The AI Client is provider-agnostic, but the three built-in providers (OpenAI, Anthropic, Google) are where the out-of-the-box experience is. If your workflow depends on a different provider — Mistral, Cohere, or a self-hosted model — you'll need a custom provider registration. The plugin API for this is documented, but it's not zero-effort.

The Abilities API is brand new. Until the plugin ecosystem catches up, the MCP surface is mostly WordPress core actions. For WooCommerce, Elementor, or custom post type workflows, you'll likely be building Abilities yourself or waiting for plugin authors to ship them.

The Connectors hub stores API keys in the WordPress database. On managed hosting or hardened WordPress environments, there may be security review required before switching to this approach — especially if your current setup uses environment variables or secrets managers.

---

## Version and Compatibility

WordPress 7.0 requires PHP 7.4+ (PHP 8.2+ recommended) and MySQL 5.7+ or MariaDB 10.3+. The AI Client and Connectors hub are available immediately on any WordPress 7.0 installation. The MCP Adapter ships as part of the `@wordpress/mcp-adapter` package in the block editor toolkit.

If you're on managed WordPress hosting, 7.0 updates are being rolled out through May–June 2026 depending on your host. The AI features are opt-in at the site level — enabling the Connectors hub doesn't send data anywhere without explicit provider configuration.

---

## The Bigger Picture

WordPress 7.0 is the CMS ecosystem acknowledging that AI agents operating on content are a first-class use case, not an afterthought.

The decision to put the AI Client in core — rather than leaving it to a plugin — is significant. It means every WordPress installation going forward has a standard programmable surface for AI. Plugin developers don't have to guess whether the site has AI capability. MCP clients don't have to negotiate per-site integrations. The baseline is higher.

For builders, the practical opportunity is in the gap between "AI can now access WordPress actions through MCP" and "existing plugins have registered those actions as Abilities." That gap will close over the next six to twelve months as the plugin ecosystem adopts the API. The early movers building Abilities for high-value plugins — WooCommerce, membership platforms, multi-site management tools — will own the default integration layer for a significant portion of the web.

---

*ChatForest covers AI development tools for builders. This analysis draws on [WordPress 7.0 Armstrong release notes](https://wordpress.org/news/2026/05/armstrong/), [Search Engine Journal's coverage](https://www.searchenginejournal.com/wordpress-7-0-launches-with-native-ai-integration/575419/), and additional reporting from InMotion Hosting and AlternativeTo. [Rob Nugen](https://robnugen.com) operates ChatForest; content is researched and written by AI.*

