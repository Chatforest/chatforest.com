# Nimble MCP Server — Enterprise Web Intelligence With the Best Google Maps Tools

> The Nimble MCP Server gives AI agents structured web data through enterprise proxy infrastructure, 18 specialized tools, and the only Google Maps extraction suite in the MCP ecosystem.


Part of our **[Web Search & Data Extraction MCP category](/categories/web-search-scraping/)**.

**At a glance:** Closed-source (hosted only), no public GitHub repo, 18 tools (expanded from 7), Streamable HTTP transport, free trial (5,000 pages), pay-as-you-go from $1/1,000 pages, managed plans from $2,500/month. $47M Series B (February 2026). Databricks Marketplace one-click install.

Nimble (formerly Nimbleway) is an enterprise web data platform that raised [$47 million in Series B funding](https://techcrunch.com/2026/02/24/nimble-way-raises-47m-to-give-ai-agents-better-cleaner-data/) in February 2026 to build AI agent infrastructure. Databricks Ventures participated in that round and subsequently added Nimble to the Databricks Marketplace as a one-click install — making Nimble simultaneously an investor-backed and distribution-channel partner of Databricks. Their MCP server connects to the same proxy and scraping backend used by enterprise customers, wrapping it in a standard MCP interface so agents can pull structured web data in real time.

Since the original review, Nimble has significantly expanded its MCP surface: 7 tools have grown to 18, the transport has migrated from SSE to Streamable HTTP, and a new "Web Search Skills" layer launched in April 2026 with 10 pre-built vertical workflows.

The standout feature remains: Nimble is the only MCP server with dedicated **Google Maps intelligence tools** — business discovery, venue details (including real-time crowd levels), and structured review collection with sentiment analysis. No competitor has entered this niche.

The key question remains: at $2,500/month minimum for managed plans, is this justified when [Bright Data](/reviews/bright-data-mcp-server/) offers 60+ tools with a free tier, and [Firecrawl](/reviews/firecrawl-mcp-server/) handles general scraping at a fraction of the cost?

## What It Does

Nimble's MCP server now exposes 18 tools across five categories, expanded from the original 7 in three categories.

### Web Search & Extraction

| Tool | Purpose |
|------|---------|
| **nimble_deep_web_search** | Real-time search across Google, Bing, Yandex with full content extraction from results |
| **nimble_extract** | Direct URL scraping — returns parsed content in multiple formats (now including `links` output format and screenshot capture as base64 PNG) |

`deep_web_search` doesn't just return search results — it follows links and extracts the actual page content. A meaningful difference from SERP-only tools. The `nimble_extract` tool picked up screenshot capture (base64 PNG) in February 2026.

**Note (March 2026 breaking change):** HTML output is no longer returned from Extract by default — it now requires an explicit `formats` parameter opt-in. HTTP response headers are also excluded by default. Existing pipelines relying on HTML or headers need updating.

### Map & Crawl (New in 2026)

| Tool | Purpose |
|------|---------|
| **nimble_map** | Discover all URLs on a website by following links and reading sitemaps |
| **nimble_crawl** | Multi-page crawl with path filtering, subdomain control, and progress tracking |

These two tools fill a significant gap from the original review. `nimble_map` is the equivalent of Firecrawl's `map` tool — useful for understanding site structure before targeted scraping. `nimble_crawl` handles progressive multi-page extraction with depth controls, comparable to Firecrawl's crawl capability.

### Custom Agent Builder (New in 2026)

| Tool | Purpose |
|------|---------|
| **nimble_agents_list** | List available pre-built and custom extraction agents |
| **nimble_agents_get** | Get details on a specific agent's schema and configuration |
| **nimble_agents_run** | Execute a custom extraction agent against a target URL or query |

This category is Nimble's most differentiated new addition. Agents are reusable extractors — you define a schema once and Nimble applies it to any URL, returning structured JSON output matching your spec. The Claude Code plugin exposes this as an "Agent Builder" skill that can generate batch scripts and preview schemas interactively. Batch processing up to 1,000 agent requests in a single API call is supported via the underlying API.

### E-commerce & Targeted Scraping

| Tool | Purpose |
|------|---------|
| **nimble_targeted_engines** | Discover available pre-trained scraping templates and supported platforms |
| **nimble_targeted_retrieval** | Extract products, prices, and availability from Amazon, Best Buy, Target, Walmart, and more |

The `targeted_engines` tool acts as a discovery layer — your agent can ask what platforms are supported before attempting to scrape. The `targeted_retrieval` tool returns structured JSON with product data, not raw HTML.

### Google Maps Intelligence

| Tool | Purpose |
|------|---------|
| **nimble_google_maps_search** | Business discovery at scale — find businesses by query and location, get ratings and metadata |
| **nimble_google_maps_place** | Deep venue data including real-time crowd levels, amenities, operating hours |
| **nimble_google_maps_reviews** | Structured review collection with ratings, sentiment, and reviewer data |

This remains Nimble's unique differentiator. No other MCP server offers structured Google Maps extraction. For agents doing local business research, competitive analysis, or location intelligence, these three tools fill a real gap — and as of May 2026, that gap remains uncontested.

## Web Search Skills (April 22, 2026)

Alongside the MCP tools, Nimble launched 10 vertical "Web Search Skills" as a higher-level workflow layer. These aren't raw MCP tools — they're pre-built research workflows built on the same infrastructure, designed to run interactively or in autonomous scheduled mode:

- `competitor-intel`, `company-deep-dive`, `market-finder`, `competitor-positioning`, `seo-intel`
- `meeting-prep`, `local-places`
- `healthcare-providers-extract`, `healthcare-providers-enrich`, `healthcare-providers-verify`
- `talent-sourcer`

The Skills layer is available via Claude Code (`claude.com/plugins/nimble`) and as a standalone SDK (`Nimbleway/agent-skills`, v0.19.0). Skills accept natural-language inputs and return structured research reports — closer to what LangChain's agent frameworks provide than to raw MCP tool calls. For enterprise teams that don't want to build their own workflows, this is a meaningful addition.

## Benchmark Performance

In [independent testing by AIMultiple](https://aimultiple.com/browser-mcp) across multiple MCP servers:

**Web Search & Extraction (single-agent):**

| Server | Accuracy | Avg Response Time |
|--------|----------|-------------------|
| [Bright Data](/reviews/bright-data-mcp-server/) | 100% | 30s |
| **Nimble** | **93%** | **16s** |
| Firecrawl | 83% | 7s |
| Oxylabs | 75% | 14s |

Nimble ranked **second in accuracy** (93%) behind only Bright Data's perfect score. Response time was moderate at 16 seconds — faster than Bright Data but slower than Firecrawl.

**Stress Test (250 Concurrent Agents):**

| Server | Success Rate | Avg Completion Time |
|--------|-------------|-------------------|
| [Bright Data](/reviews/bright-data-mcp-server/) | 76.8% | 48.7s |
| Oxylabs | 54.4% | 31.7s |
| **Nimble** | **51.2%** | **182.3s** |
| Firecrawl | 64.8% | 77.6s |
| [Apify](/reviews/apify-mcp-server/) | 18.8% | — |

The concurrent load weakness has **not been publicly retested or resolved**. Under 250 simultaneous agents, Nimble's success rate dropped to 51.2% (down from 93%), and successful tasks averaged 182.3 seconds — nearly 4x slower than Oxylabs. The new batch endpoint (up to 1,000 agent requests per call) operates at the API layer but doesn't address the per-request latency and reliability degradation at scale. If high-volume parallel agent workflows are your use case, this remains a meaningful concern.

## Setup

Nimble migrated from SSE to **Streamable HTTP** transport. The old SSE endpoint (`/sse`) is no longer the official target — connect via the MCP endpoint instead:

```json
{
  "mcpServers": {
    "nimble": {
      "url": "https://mcp.nimbleway.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_NIMBLE_API_KEY"
      }
    }
  }
}
```

Via Claude Code CLI:
```bash
claude mcp add --transport http nimble-mcp-server https://mcp.nimbleway.com/mcp
```

Works with Claude Desktop, Cursor, qodo, Microsoft CoPilot, OpenAI Playground, Google ADK, Databricks, and more. Framework integrations for LangChain, LlamaIndex, Agno, and Microsoft AutoGen are documented.

**No self-hosting option.** All requests route through Nimble's infrastructure. This simplifies setup but means you're dependent on their uptime, pricing, and data handling.

## Pricing

### Pay-as-You-Go

| API | Cost |
|-----|------|
| Agent API | $1 per 1,000 pages |
| Search API (search) | $1 per 1,000 search inputs |
| Search API (answer) | $4 per request |
| Extract (standard) | $0.90 per 1,000 URLs |
| Extract (JS render) | $1.30 per 1,000 URLs |
| Extract (stealth) | $1.45 per 1,000 URLs |
| Residential Proxy | $7.50 per GB |

### Managed Plans

| Plan | Price/month | Concurrent Agents | Monthly Credits | Data Storage |
|------|-------------|-------------------|-----------------|--------------|
| Startup | $2,500 | 5 | 350K pages | 7 days |
| Scale | $7,000 | 10 | 1.2M pages | 30 days |
| Professional | $15,000 | 20 | 3M pages | 90 days |
| Enterprise | Custom | Unlimited | Custom | Custom |

All managed plans include MCP integration, custom agent ETL, and 15% discount on annual billing. **No pricing changes since the original review.**

**Free trial:** 5,000 web pages to test before committing. This is a one-time trial — not an ongoing free tier.

The pricing gap vs. alternatives remains significant. [Bright Data](/reviews/bright-data-mcp-server/) offers a free tier with 5,000 requests/month on an ongoing basis. [Firecrawl](/reviews/firecrawl-mcp-server/) has paid plans starting at $19/month. Nimble's managed tier starts 130x higher than Firecrawl's entry point.

## Security & Compliance

Nimble holds **AICPA SOC 2 certification** and claims GDPR and CCPA alignment. Infrastructure runs on AWS and GCP with role-based access controls. The platform now explicitly markets **zero data retention and PII masking** as security features — new positioning language since the prior review, useful for enterprise procurement conversations.

No new certifications (ISO 27001, FedRAMP) have been announced.

## How It Compares

| Feature | Nimble | [Bright Data](/reviews/bright-data-mcp-server/) | [Firecrawl](/reviews/firecrawl-mcp-server/) | [Apify](/reviews/apify-mcp-server/) |
|---------|--------|------------|-----------|-------|
| **Tools** | 18 | 60+ (Pro) | 19 | 17+ |
| **Search accuracy** | 93% | 100% | 83% | 78% |
| **Stress test** | 51.2% | 76.8% | 64.8% | 18.8% |
| **Google Maps** | 3 dedicated tools | No | No | Via Actors |
| **Crawl/Map** | Yes (new) | Yes | Yes | Yes |
| **Custom agents** | Yes (new) | No | No | Via marketplace |
| **E-commerce** | Structured templates | 10+ vertical scrapers | General extraction | Via marketplace |
| **Free tier** | Trial only (5K pages) | 5K req/month ongoing | 500 pages/month | $5/month credits |
| **Self-hosting** | No | Yes (local mode) | Yes (open source) | Yes (open source) |
| **Open source** | No | MIT license | AGPL | Apache 2.0 |
| **Min paid plan** | $2,500/month | Pay-as-you-go | $19/month | $49/month |
| **Transport** | Streamable HTTP | Both | Both | Both |
| **Marketplace** | Databricks | Multiple | Smithery | Smithery, npx |

## Limitations

- **No open source, no self-hosting.** You're fully locked into Nimble's infrastructure and pricing. If they raise prices or change terms, you have no alternative deployment option.
- **Stress test performance still unresolved.** 51.2% success at 182.3 seconds under concurrent load makes this unsuitable for high-volume parallel agent workflows, and no public fix or retest has been announced.
- **Expensive entry point.** $2,500/month minimum for managed plans, with only a one-time trial rather than an ongoing free tier. Pricing unchanged since February 2026.
- **Closed-source trust model.** No way to audit how your data is handled, what's cached, or how requests are routed. The SOC 2 certification partially addresses this, but transparency-minded teams may prefer open-source alternatives.
- **No public GitHub community.** No issue tracker, no community contributions, no way to report bugs publicly or track development velocity.
- **Limited grassroots traction.** Nimble MCP is absent from most independent "best MCP servers" roundup articles and has minimal Reddit or HackerNews discussion — Bright Data and Firecrawl dominate community mindshare.
- **Breaking change: HTML no longer returned by default from Extract** (March 2026) — existing pipelines using the API directly may need updates.

## The Bottom Line

Nimble has shipped meaningful improvements since its March launch: the tool count jumped from 7 to 18 with the addition of Map, Crawl, and custom Agent Builder categories; the transport migrated to Streamable HTTP; and the Web Search Skills layer adds pre-built vertical research workflows. The Databricks Marketplace listing gives enterprise teams a frictionless installation path.

The **Google Maps intelligence suite** remains Nimble's clearest differentiator — three dedicated tools for business discovery, venue details, and review extraction that no other MCP server offers. That niche is still uncontested as of May 2026.

What hasn't changed: the concurrent-load stress test weakness (51.2% success, 182.3s average) remains a concern for high-volume workloads, and the $2,500/month managed plan floor remains one of the highest entry points in the category. Community adoption continues to lag behind Bright Data and Firecrawl.

**Who should use this:** Teams building agents that need local business intelligence (Google Maps data), e-commerce price monitoring across major retailers, enterprises that require SOC 2 compliance documentation, or Databricks users who want a one-click install. The new Agent Builder tools and Web Search Skills layer also suit teams that want higher-level research workflows without building their own.

**Who should look elsewhere:** Individual developers, teams on a budget, anyone needing browser automation or social media scraping, or high-concurrency agent deployments. [Bright Data](/reviews/bright-data-mcp-server/) offers more tools with better stress performance at lower entry cost. [Firecrawl](/reviews/firecrawl-mcp-server/) handles general web scraping — including crawl and map — with an open-source self-hosted option starting at $19/month.

**Rating: 3.5/5** — The platform grew substantially (7 → 18 tools, Streamable HTTP, Web Search Skills, Databricks integration), and Google Maps exclusivity holds. Stress test performance and pricing floor remain limiting factors for broad recommendation.

