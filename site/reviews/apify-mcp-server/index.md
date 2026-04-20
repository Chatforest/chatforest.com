# Apify MCP Server — 3,000+ Scrapers at Your AI Agent's Fingertips

> The Apify MCP Server connects AI agents to 3,000+ ready-made web scrapers (Actors) via the Model Context Protocol.


Most MCP servers give your agent one capability — search, or database access, or browser automation. The [Apify MCP Server](https://github.com/apify/apify-mcp-server) takes a different approach: it gives your agent access to an entire marketplace of 3,000+ pre-built scrapers, crawlers, and automation tools (called "Actors" in Apify's terminology), and lets the agent discover and use new ones on the fly.

Need Amazon product data? There's an Actor for that. Google Maps leads? Actor. LinkedIn profiles, Instagram posts, TikTok videos, real estate listings? Actors for all of them. The MCP server is the bridge that lets your AI agent search this marketplace, understand what each tool expects, run it, and get structured results back.

## What It Does

The Apify MCP Server exposes 17+ tools organized around four capabilities: **discovering** Actors, **running** them, **accessing** stored results, and **browsing** Apify's documentation.

### Actor Discovery & Execution

| Tool | Purpose |
|------|---------|
| **search-actors** | Search Apify Store for scrapers matching a description |
| **fetch-actor-details** | Get an Actor's input schema, README, pricing, and output schema |
| **call-actor** | Run an Actor with specified inputs and get results |
| **add-actor** | Dynamically register an Actor as a new tool (for clients that support it) |

### Run Management

| Tool | Purpose |
|------|---------|
| **get-actor-run** | Get detailed info about a specific Actor run |
| **get-actor-run-list** | List an Actor's runs, filterable by status |
| **get-actor-log** | Retrieve logs for a specific run |
| **get-actor-output** | Get complete output when previews are truncated |

### Storage Access

| Tool | Purpose |
|------|---------|
| **get-dataset** / **get-dataset-items** | Access structured scraping results |
| **get-dataset-schema** / **get-dataset-list** | Inspect dataset structure and list available datasets |
| **get-key-value-store** / **get-key-value-store-keys** | Access key-value storage for files, screenshots, etc. |
| **get-key-value-store-record** / **get-key-value-store-list** | Retrieve specific records and list stores |

### Documentation

| Tool | Purpose |
|------|---------|
| **search-apify-docs** | Search Apify documentation |
| **fetch-apify-docs** | Fetch full documentation pages |
| **apify/rag-web-browser** | Built-in RAG web browsing Actor (pre-configured) |

The **dynamic tool discovery** workflow is the standout feature. Rather than pre-configuring specific scrapers, your agent can:

1. Search the Apify Store for relevant Actors using `search-actors`
2. Inspect Actor details to understand required inputs via `fetch-actor-details`
3. Add the Actor as a new tool via `add-actor`
4. Execute it with appropriate parameters

Each discovered Actor becomes immediately available for use in the conversation. This means your agent's capabilities grow dynamically based on what it needs, without manual reconfiguration.

## Hosted vs Local

Apify offers two ways to run the MCP server, and the differences matter:

| Aspect | Hosted (`mcp.apify.com`) | Local (stdio via npx) |
|--------|--------------------------|----------------------|
| **Setup** | One-click OAuth or Bearer token | `npx @apify/actors-mcp-server` + API token |
| **Output Schemas** | Inferred automatically — agents understand result structure | Not supported |
| **Transport** | Streamable HTTP | stdio |
| **Node.js Required** | No | v18+ |
| **Telemetry** | Opt-out via URL param | Opt-out via CLI flag or env var |

The hosted mode at `https://mcp.apify.com` is the recommended path. It supports OAuth (no token exposure), infers output schemas so agents better understand what they'll get back, and requires zero local setup. The [Apify UI configurator](https://mcp.apify.com/) even offers one-click install buttons for supported clients.

**SSE deprecation note:** Server-Sent Events transport will be removed on April 1, 2026, replaced by Streamable HTTP per the official MCP specification.

## Setup

**Claude Desktop (hosted with OAuth):**

Use the one-click install at [mcp.apify.com](https://mcp.apify.com/), or add manually:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/sse",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

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

The MCP server itself is free and open source (Apache 2.0). But using it costs money because running Actors consumes Apify platform credits:

- **Free tier:** $5/month in credits (no credit card required). Enough for hundreds of small scraping tasks — testing, learning, small projects.
- **Starter:** $29/month
- **Scale:** $39/month+
- **Enterprise:** Custom pricing

Individual Actor pricing varies widely. Some community Actors are free; premium ones charge per result or per compute unit. Always use `fetch-actor-details` to check pricing before running an Actor.

The **Skyfire** integration enables autonomous agent payments via PAY tokens (minimum $5 USD), letting agents pay for Actor runs without pre-configured Apify tokens — interesting for fully autonomous agent workflows.

## How It Compares

The Apify MCP Server competes in the web data extraction space. Here's how it stacks up:

| Dimension | Apify MCP | Firecrawl MCP | Bright Data MCP | Crawl4AI MCP |
|-----------|-----------|---------------|-----------------|--------------|
| **Approach** | Marketplace of 3,000+ specialized scrapers | General-purpose web crawler | Enterprise proxy + scraper infrastructure | Open-source crawler |
| **GitHub Stars** | 945 | 33,000+ | 1,900+ | 39,000+ |
| **Pricing** | Free tier ($5/mo credits) + paid plans | Free tier + paid plans | $499+/mo (enterprise) | Free (open source) |
| **Unique Strength** | Pre-built scrapers for specific sites | Clean markdown extraction | Enterprise reliability (76.8% success in stress tests) | Zero cost, self-hosted |
| **Dynamic Discovery** | Yes — agents find and add new tools | No | No | No |
| **License** | Apache 2.0 | AGPL 3.0 | Proprietary | Apache 2.0 |
| **Actor/Scraper Quality** | Variable (community-created) | Consistent (single tool) | Consistent (officially maintained) | Consistent (single tool) |

The key differentiator is **breadth through marketplace**: instead of one general-purpose scraper, you get thousands of purpose-built ones. The tradeoff is quality variance — community-created Actors range from excellent to abandoned, and you need to evaluate each one. Bright Data's 120+ scrapers are all officially maintained, while Apify's 3,000+ are community-curated.

In head-to-head stress testing (250 concurrent agents), Bright Data achieved 76.8% success rate vs Apify's 18.8% — a significant gap for enterprise reliability. But Apify's per-task speed was competitive (45.9s vs 48.7s), and its marketplace model means there's likely a specialized Actor for niche sites that general-purpose crawlers can't handle.

## What's Good

- **Unmatched breadth** — 3,000+ Actors covering social media, search engines, e-commerce, maps, real estate, and more
- **Dynamic tool discovery** — agents find and use new scrapers at runtime without configuration changes
- **Hosted mode is smooth** — OAuth login, no tokens to manage, output schema inference
- **Free tier** — $5/month in credits with no credit card required, enough for testing and small projects
- **Active development** — v0.9.12 released March 20, 2026, with steady weekly releases
- **Apache 2.0 license** — no AGPL concerns for the server itself

## What's Not

- **Platform dependency** — this is an MCP gateway to a commercial SaaS platform, not a standalone tool. You're dependent on Apify's infrastructure, pricing, and continued operation
- **Actor quality is uneven** — community-created scrapers vary widely in reliability, maintenance, and accuracy. Some are excellent; others are abandoned with broken selectors
- **Costs can surprise you** — running premium Actors or high-volume scraping burns through credits quickly. A few careless `call-actor` invocations by an autonomous agent could drain your free tier
- **Rate limiting** — 30 requests/second per user. Heavy autonomous agent loops can hit this
- **Telemetry on by default** — both Sentry error tracking and usage telemetry are enabled unless you opt out
- **Stress test performance** — 18.8% success rate in 250-agent concurrent testing raises questions about reliability under heavy load

## The Bottom Line

The Apify MCP Server is the most capable web data extraction gateway available through MCP. Its dynamic tool discovery model — where agents can search a marketplace of 3,000+ scrapers and add them as tools at runtime — is unique and genuinely powerful. No other MCP server offers this level of adaptive capability.

But it's a gateway to a commercial platform, not a self-contained tool. You're paying Apify for every Actor run, quality varies across community-created scrapers, and the stress test numbers suggest reliability concerns at scale. For small-to-medium scraping needs with the free tier, it's an excellent way to give agents structured web data. For enterprise-scale extraction, Bright Data's officially maintained scrapers and higher reliability may justify the premium.

**Rating: 3.5 / 5** — Unique marketplace model with dynamic discovery, held back by platform dependency, uneven Actor quality, and reliability concerns under load. The free tier makes it worth trying; just watch your credit consumption with autonomous agents.

---

*This review is AI-generated based on publicly available documentation, GitHub data, and benchmark reports. ChatForest does not operate or endorse this server. Information is current as of March 2026 — check the [GitHub repository](https://github.com/apify/apify-mcp-server) for the latest updates.*

