# Apify MCP Server — 59,000+ Scrapers at Your AI Agent's Fingertips

> The Apify MCP Server connects AI agents to 59,000+ ready-made web scrapers (Actors) via the Model Context Protocol.


Most MCP servers give your agent one capability — search, or database access, or browser automation. The [Apify MCP Server](https://github.com/apify/apify-mcp-server) takes a different approach: it gives your agent access to an entire marketplace of [59,000+ pre-built scrapers](https://apify.com/store/categories), crawlers, and automation tools (called "Actors" in Apify's terminology), and lets the agent discover and use new ones on the fly.

Need Amazon product data? There's an Actor for that. Google Maps leads? Actor. LinkedIn profiles, Instagram posts, TikTok videos, real estate listings? Actors for all of them. The MCP server is the bridge that lets your AI agent search this marketplace, understand what each tool expects, run it, and get structured results back.

## What It Does

As of the current [README](https://github.com/apify/apify-mcp-server#readme), the Apify MCP Server exposes 19 tools organized around four capabilities: **discovering** Actors, **running** them, **accessing** stored results, and **browsing** Apify's documentation.

### Actor Discovery & Execution

| Tool | Purpose |
|------|---------|
| **search-actors** | Search Apify Store for scrapers matching a description |
| **fetch-actor-details** | Get an Actor's input schema, README, pricing, and output schema |
| **call-actor** | Run an Actor with specified inputs and get results |

Note: the earlier **add-actor** tool (which dynamically registered an Actor as a discrete new tool) was [retired in v0.13.0](https://github.com/apify/apify-mcp-server/blob/master/CHANGELOG.md) (July 2026) as part of a stateless-architecture migration. Clients that pass `tools=add-actor` now get it silently ignored; the server's own docs say to use `call-actor` directly instead.

### Run Management

| Tool | Purpose |
|------|---------|
| **get-actor-run** | Get detailed info about a specific Actor run |
| **abort-actor-run** | Abort a running Actor run, optionally gracefully |
| **get-actor-run-list** | List an Actor's runs, filterable by status |
| **get-actor-log** | Retrieve logs for a specific run |

### Storage Access

| Tool | Purpose |
|------|---------|
| **get-dataset** / **get-dataset-items** | Access structured scraping results |
| **get-dataset-schema** / **get-dataset-list** | Inspect dataset structure and list available datasets |
| **get-key-value-store** / **get-key-value-store-keys** | Access key-value storage for files, screenshots, etc. |
| **get-key-value-store-record** / **get-key-value-store-list** | Retrieve specific records and list stores |

### Documentation & Dev

| Tool | Purpose |
|------|---------|
| **search-apify-docs** | Search Apify documentation |
| **fetch-apify-docs** | Fetch full documentation pages |
| **apify--rag-web-browser** | Built-in RAG web browsing Actor (pre-configured) |
| **report-problem** | Report a problem with an Apify tool or Actor to the Apify team |

The **dynamic tool discovery** workflow is still the standout feature, though the exact mechanics changed with the July 2026 stateless migration. Rather than pre-configuring specific scrapers, your agent now:

1. Searches the Apify Store for relevant Actors using `search-actors`
2. Inspects Actor details to understand required inputs via `fetch-actor-details`
3. Calls the Actor directly with `call-actor`, passing the Actor ID and input — no separate "add as a tool" step

This is a simpler flow than the earlier `add-actor` model, per the [current README](https://github.com/apify/apify-mcp-server#readme): "It allows an AI agent to find new tools (Actors) as needed and incorporate them." Your agent's capabilities still grow dynamically based on what it needs, without manual reconfiguration — it just doesn't register each discovered Actor as its own named tool anymore.

## Hosted vs Local

Apify offers two ways to run the MCP server, and the differences matter:

| Aspect | Hosted (`mcp.apify.com`) | Local (stdio via npx) |
|--------|--------------------------|----------------------|
| **Setup** | One-click OAuth or Bearer token | `npx @apify/actors-mcp-server` + API token |
| **Output Schemas** | Inferred automatically — agents understand result structure | Not supported |
| **Transport** | Streamable HTTP | stdio |
| **Node.js Required** | No | [v22+](https://github.com/apify/apify-mcp-server/blob/master/package.json) |
| **Telemetry** | Opt-out via URL param | Opt-out via CLI flag or env var |

The hosted mode at `https://mcp.apify.com` is the recommended path. It supports OAuth (no token exposure), infers output schemas so agents better understand what they'll get back, and requires zero local setup. The [Apify UI configurator](https://mcp.apify.com/) even offers one-click install buttons for supported clients.

**SSE deprecated:** Server-Sent Events transport was removed on April 1, 2026 as planned, replaced by Streamable HTTP per the MCP specification. If you configured the SSE endpoint (`/sse`), update to the Streamable HTTP endpoint (`/mcp`).

## Setup

**Claude Desktop (hosted with OAuth):**

Use the one-click install at [mcp.apify.com](https://mcp.apify.com/), or add manually:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

*(Note: The SSE endpoint `/sse` was removed April 1, 2026. Use `/mcp` for Streamable HTTP.)*

**Claude Desktop (local):**

```json
{
  "mcpServers": {
    "actors-mcp-server": {
      "command": "npx",
      "args": ["-y", "@apify/actors-mcp-server"],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

**Claude Code:**

```bash
claude mcp add apify -- npx -y @apify/actors-mcp-server
```

Set `APIFY_TOKEN` in your environment.

**Cursor:**

Create `.cursor/mcp.json` pointing to the hosted URL with Bearer token authentication.

## Pricing Reality

The MCP server itself is free and open source ([MIT license](https://github.com/apify/apify-mcp-server/blob/master/LICENSE.md) — not Apache 2.0, correcting an earlier version of this review). But using it costs money because running Actors consumes Apify platform credits. Per [Apify's pricing page](https://apify.com/pricing):

- **Free tier:** $5/month in credits (no credit card required). Enough for hundreds of small scraping tasks — testing, learning, small projects.
- **Starter:** $29/month
- **Scale:** $199/month
- **Business:** $999/month
- **Enterprise:** Custom pricing

Individual Actor pricing varies widely. Some community Actors are free; premium ones charge per result or per compute unit. Always use `fetch-actor-details` to check pricing before running an Actor.

The [**Skyfire** integration](https://docs.apify.com/platform/integrations/skyfire) enables autonomous agent payments via PAY tokens (minimum $5 USD), letting agents pay for Actor runs without pre-configured Apify tokens — interesting for fully autonomous agent workflows.

## How It Compares

The Apify MCP Server competes in the web data extraction space. Here's how it stacks up:

| Dimension | [Apify MCP](https://github.com/apify/apify-mcp-server) | [Firecrawl MCP](https://github.com/firecrawl/firecrawl-mcp-server) | [Bright Data MCP](https://github.com/brightdata/brightdata-mcp) | [Crawl4AI](https://github.com/unclecode/crawl4ai) |
|-----------|-----------|---------------|-----------------|--------------|
| **Approach** | Marketplace of 59,000+ specialized scrapers | General-purpose web crawler | Enterprise proxy + scraper infrastructure | Open-source crawler |
| **GitHub Stars** | 3,700+ | 7,200+ | 2,600+ | 78,000+ |
| **Pricing** | Free tier ($5/mo credits) + paid plans | Free tier + paid plans | Free tier (5,000 req/mo) + [$499+/mo plans](https://brightdata.com/pricing/mcp-server) | Free (open source) |
| **Unique Strength** | Pre-built scrapers for specific sites | Clean markdown extraction | Enterprise reliability, officially maintained scrapers | Zero cost, self-hosted |
| **Dynamic Discovery** | Yes — agents find and call new tools at runtime | No | No | No |
| **License** | MIT | MIT | MIT | Apache 2.0 |
| **Actor/Scraper Quality** | Variable (community-created) | Consistent (single tool) | Consistent (officially maintained) | Consistent (single tool) |

Star counts and licenses checked directly against each project's GitHub repository on 2026-08-15; Firecrawl's MCP server has moved to the `firecrawl/firecrawl-mcp-server` repo (previously under the `mendableai` org).

The key differentiator is **breadth through marketplace**: instead of one general-purpose scraper, you get thousands of purpose-built ones. The tradeoff is quality variance — community-created Actors range from excellent to abandoned, and you need to evaluate each one. Bright Data's [scraper library](https://docs.brightdata.com/datasets/scrapers/scrapers-library/overview) lists 1,000+ pre-built, officially maintained scrapers, while Apify's 59,000+ Actors are community-curated and vary widely in quality.

Bright Data's officially maintained scraper library offers higher consistency for enterprise deployments, while Apify's marketplace model means there's likely a specialized Actor for niche sites that general-purpose crawlers can't handle.

## What's Good

- **Unmatched breadth** — [59,000+ Actors](https://apify.com/store/categories) covering social media, search engines, e-commerce, maps, real estate, and more
- **Dynamic tool discovery** — agents find and call new scrapers at runtime without configuration changes
- **Hosted mode is smooth** — OAuth login, no tokens to manage, output schema inference
- **Free tier** — $5/month in credits with no credit card required, enough for testing and small projects
- **Active development** — [v0.14.3 released August 12, 2026](https://github.com/apify/apify-mcp-server/releases); the server shipped a breaking stateless-architecture migration across v0.12.0–v0.14.0 (July 2026), added `abort-actor-run` and `report-problem` tools, and retired the older `add-actor` tool
- **MIT license** — permissive open-source license for the server itself (corrected from an earlier version of this review, which stated Apache 2.0)

## What's Not

- **Platform dependency** — this is an MCP gateway to a commercial SaaS platform, not a standalone tool. You're dependent on Apify's infrastructure, pricing, and continued operation
- **Actor quality is uneven** — community-created scrapers vary widely in reliability, maintenance, and accuracy. Some are excellent; others are abandoned with broken selectors
- **Costs can surprise you** — running premium Actors or high-volume scraping burns through credits quickly. A few careless `call-actor` invocations by an autonomous agent could drain your free tier. The paid tiers above [Starter](https://apify.com/pricing) also jump quickly (Scale is $199/month, not the $39/month this review previously stated)
- **Rate limiting** — [30 requests/second per user](https://docs.apify.com/platform/integrations/mcp). Heavy autonomous agent loops can hit this
- **Telemetry on by default** — both Sentry error tracking and usage telemetry are enabled unless you opt out
- **Workflow churn** — the July 2026 stateless migration removed the `add-actor` tool with no deprecation window beyond one minor version, meaning integrations built around registering Actors as named tools broke and had to be rewritten around `call-actor`

## The Bottom Line

The Apify MCP Server is the most capable web data extraction gateway available through MCP. Its dynamic tool discovery model — where agents can search a marketplace of 59,000+ scrapers and call them as tools at runtime — is unique and genuinely powerful. No other MCP server offers this level of adaptive capability.

But it's a gateway to a commercial platform, not a self-contained tool. You're paying Apify for every Actor run, quality varies across community-created scrapers, and the server's rapid breaking-change pace (four minor versions in July 2026 alone, including a tool removal) is worth planning around. For small-to-medium scraping needs with the free tier, it's an excellent way to give agents structured web data. For enterprise-scale extraction, Bright Data's officially maintained scraper library and higher reliability may justify the premium.

**Rating: 3.5 / 5** — Unique marketplace model with dynamic discovery, held back by platform dependency, uneven Actor quality, and a fast-moving API surface that has already broken at least one advertised workflow (`add-actor`). The free tier makes it worth trying; just watch your credit consumption with autonomous agents.

---

*This review was originally published March 23, 2026, refreshed May 3, 2026, and claim-level audited August 15, 2026. Audit findings: latest release is [v0.14.3](https://github.com/apify/apify-mcp-server/releases) (August 12, 2026), not v0.9.16 — the server went through a breaking stateless-architecture migration (v0.12.0–v0.14.0, July 2026) that retired the `add-actor` tool and added `abort-actor-run`/`report-problem`. License is MIT, not Apache 2.0. Stars grew to ~3,700+. The Apify Store now lists [59,000+ Actors](https://apify.com/store/categories), not 3,000+. Apify's paid "Scale" plan is $199/month, not $39/month. Node.js requirement is now v22+. Competitor star counts and licenses (Firecrawl, Bright Data, Crawl4AI) were re-verified directly against their GitHub repos. The previous "18.8% stress-test success rate" claim was removed — its sole source is a benchmark that discloses a sponsorship relationship with Apify, and no independent second source could be found. We research MCP servers thoroughly but do not test them hands-on. Check the [GitHub repository](https://github.com/apify/apify-mcp-server) for the latest updates.*

