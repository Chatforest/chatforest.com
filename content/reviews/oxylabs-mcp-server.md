---
title: "Oxylabs MCP Server — Two Scraping Engines in One, With the Fastest Stress Test Times"
date: 2026-03-23T22:00:00+09:00
description: "The Oxylabs MCP Server combines a traditional Web Scraper API with AI-powered extraction tools in a single Python package. 86 GitHub stars, MIT license, 8 tools across two modes. Here's the honest review."
og_description: "Oxylabs MCP Server: dual-engine web scraping for AI agents. 86 stars, MIT license, 8 tools (Web Scraper API + AI Studio), 75% search accuracy, fastest stress test completion (31.7s avg). Free trials for both engines. Rating: 3/5."
content_type: "Review"
card_description: "Dual-engine web scraping for AI agents. Combines traditional Web Scraper API (proxies, anti-bot, structured parsers) with AI Studio (AI-powered extraction, crawling, browser automation). Two free trials. Python-based, Claude Desktop and Cursor support."
last_refreshed: 2026-03-23
---

**At a glance:** 86 stars, 23 forks, MIT license, v0.7.5 (December 2025), Python, stdio transport, 8 tools across 2 engines, two separate free trials available.

Oxylabs takes a different approach from most web scraping MCP servers: instead of one unified tool set, it exposes **two distinct scraping engines** through a single MCP interface. Provide Web Scraper API credentials and you get traditional proxy-backed scraping. Provide an AI Studio API key and you get AI-powered extraction. Provide both and the server exposes all 8 tools.

The [Oxylabs MCP Server](https://github.com/oxylabs/oxylabs-mcp) comes from a company with $43.7M in revenue (2025), 428 employees, and a proxy network covering 195+ countries. They also [acquired ScrapingBee](https://oxylabs.io/) in June 2025, consolidating their position in the web data space.

In [AIMultiple's independent benchmarks](https://aimultiple.com/browser-mcp), Oxylabs hit **75% accuracy** on web search and extraction — middle of the pack — but posted the **fastest stress test completion time** at 31.7 seconds average per successful task. Speed is the story here, not raw accuracy.

## What It Does

### Web Scraper API Tools

Provide `OXYLABS_USERNAME` and `OXYLABS_PASSWORD` to unlock these four tools:

| Tool | Purpose |
|------|---------|
| **universal_scraper** | Scrape any URL via Oxylabs' proxy infrastructure with anti-bot bypass |
| **google_search_scraper** | Extract structured Google Search results |
| **amazon_search_scraper** | Scrape Amazon search result pages |
| **amazon_product_scraper** | Extract structured data from individual Amazon product pages |

These route through Oxylabs' proxy network — IP rotation, CAPTCHA handling, JavaScript rendering, and automatic HTML-to-Markdown conversion. The Amazon and Google scrapers return **structured JSON** with pre-built parsers that extract specific fields (price, ratings, reviews) rather than raw page content.

### AI Studio Tools

Provide `OXYLABS_AI_STUDIO_API_KEY` to unlock these four tools:

| Tool | Purpose |
|------|---------|
| **ai_scraper** | AI-powered content extraction from any URL (JSON or Markdown output) |
| **ai_crawler** | Crawl websites across multiple pages, collecting data in Markdown or JSON |
| **ai_browser_agent** | Control a remote browser, return data as Markdown, JSON, HTML, or screenshots |
| **ai_search** | Web search with AI-powered content extraction from results |

AI Studio tools use machine learning to understand page structure and extract relevant data without predefined parsers. The `ai_browser_agent` is particularly notable — it provides full browser automation through Oxylabs' infrastructure, handling JavaScript-heavy SPAs and interactive pages.

### Dual-Engine Architecture

The two-credential design is unusual. Most competing MCP servers (Bright Data, Firecrawl, Apify) use a single authentication method. Oxylabs splits because these are genuinely different products:

- **Web Scraper API** = traditional proxy-backed scraping with pre-built parsers
- **AI Studio** = newer AI-powered extraction platform

You can use either independently or both together. The MCP server auto-detects which credentials you've provided and exposes the corresponding tools.

## Setup

Install via uvx (recommended):
```json
{
  "mcpServers": {
    "oxylabs": {
      "command": "uvx",
      "args": ["oxylabs-mcp"],
      "env": {
        "OXYLABS_USERNAME": "your_username",
        "OXYLABS_PASSWORD": "your_password",
        "OXYLABS_AI_STUDIO_API_KEY": "your_api_key"
      }
    }
  }
}
```

Also available via uv local install, Docker, or [Smithery](https://smithery.ai/) (cloud-based OAuth2 or query parameter auth).

### Configuration Options

| Variable | Purpose | Required |
|----------|---------|----------|
| `OXYLABS_USERNAME` | Web Scraper API username | For Web Scraper tools |
| `OXYLABS_PASSWORD` | Web Scraper API password | For Web Scraper tools |
| `OXYLABS_AI_STUDIO_API_KEY` | AI Studio API key | For AI Studio tools |
| `LOG_LEVEL` | Logging verbosity | No (default: INFO) |

At least one credential set is required. The server logs via MCP `notifications/message` events, providing job status, request parameters, and error details.

## Benchmark Performance

Independent benchmarks from [AIMultiple's MCP stress test](https://aimultiple.com/browser-mcp) place Oxylabs in the middle tier for accuracy but top tier for speed:

### Web Search & Extraction

| Server | Success Rate | Avg Speed | Scalability (250 agents) |
|--------|-------------|-----------|--------------------------|
| [Bright Data](/reviews/bright-data-mcp-server/) | 100% | 30s | 76.8% |
| [Nimble](/reviews/nimble-mcp-server/) | 93% | 16s | 51.2% |
| [Firecrawl](/reviews/firecrawl-mcp-server/) | 83% | 7s | 64.8% |
| [Apify](/reviews/apify-mcp-server/) | 78% | 32s | 18.8% |
| **Oxylabs** | **75%** | **14s** | **54.4%** |
| Tavily | 38% | 14s | 45.0% |

### Stress Test Performance

At 250 concurrent agents, Oxylabs completed successful tasks in an average of **31.7 seconds** — the fastest of all servers tested. For comparison:
- Tavily: 41.3s average
- Bright Data: 48.7s average
- Nimble: 182.3s average

The 54.4% scalability score means roughly half the tasks succeeded under heavy load. That's mid-pack — better than Apify (18.8%) and Tavily (45.0%), worse than Bright Data (76.8%) and Firecrawl (64.8%).

The tradeoff is clear: Oxylabs is fast when it succeeds, but succeeds less often than top competitors. At 75% accuracy vs Bright Data's 100%, one in four tasks fails. Whether that matters depends on your error handling and retry strategy.

## Headless Browser MCP — The Companion Server

Oxylabs also maintains a separate [Headless Browser MCP server](https://github.com/oxylabs/oxylabs-hb-mcp) that wraps Playwright MCP with Oxylabs' managed browser infrastructure. Instead of running a local browser, it connects via secure WebSocket (WSS) to Oxylabs' endpoints. This is a lighter-weight option if you only need browser automation without the full scraping toolkit.

## Pricing

Oxylabs has two separate pricing structures for its two engines:

### Web Scraper API

| Plan | Monthly Cost | Results Included | Rate per 1K |
|------|-------------|-----------------|-------------|
| **Free Trial** | $0 | 2,000 results | — |
| **Micro** | $49 | 98,000 | $0.50 |
| **Starter** | $99 | 220,000 | $0.45 |
| **Advanced** | $249 | 622,500 | $0.40 |
| **Venture** | $499 | 1,350,000 | $0.37 |
| **Business** | $999 | 3,330,000 | $0.30 |
| **Corporate** | $2,000 | 8,000,000 | $0.25 |

All plans include CAPTCHA handling, custom parsers, automated scheduling, and 24/7 support. Rate limit: 50 req/s (100 req/s for Business+).

### AI Studio

| Plan | Monthly Cost | Credits | Rate Limit |
|------|-------------|---------|------------|
| **Free Trial** | $0 | 1,000 credits | — |
| **Starter** | $12 | 3,000 | 1 req/s |
| **Lite** | $62 | 100,000 | 5 req/s |
| **Standard** | $250 | 500,000 | 10 req/s |
| **Custom** | $1,200+ | 1.35M+ | 25 req/s |

Credits don't roll over. You're not charged for system errors (5xx/6xx), but you are charged if the requested data doesn't exist on the page.

The dual pricing is both a strength and a complication. You can start with just AI Studio ($12/mo) for AI-powered scraping, or just Web Scraper API ($49/mo) for traditional proxy scraping, or run both. But budgeting requires tracking two separate billing systems.

## Compared to Alternatives

| Feature | Oxylabs | [Bright Data](/reviews/bright-data-mcp-server/) | [Firecrawl](/reviews/firecrawl-mcp-server/) | [Nimble](/reviews/nimble-mcp-server/) |
|---------|---------|-------------|-----------|--------|
| **Stars** | 86 | 2,200 | 5,800 | N/A (closed) |
| **Tools** | 8 | 60+ (Pro) | 19 | 7 |
| **Language** | Python | TypeScript | TypeScript | N/A |
| **Accuracy** | 75% | 100% | 83% | 93% |
| **Speed** | 14s | 30s | 7s | 16s |
| **Stress test** | 54.4% | 76.8% | 64.8% | 51.2% |
| **AI extraction** | Yes (Studio) | Yes (Pro) | Yes (LLM) | No |
| **Browser automation** | Yes (Studio + HB) | Yes (Pro) | Yes (v2) | No |
| **Free tier** | 2K results + 1K credits | 5K req/month | Limited | 5K pages |
| **Entry price** | $12/mo (Studio) | Pay-as-you-go | $19/mo | $2,500/mo |
| **Self-hosted** | No | No | Yes | No |
| **License** | MIT | MIT | AGPL-3.0 | Closed |

**Choose Oxylabs when:** you want both traditional proxy scraping and AI-powered extraction in one MCP interface, you need fast completion times under load, or Amazon/Google structured data extraction is your primary use case.

**Choose [Bright Data](/reviews/bright-data-mcp-server/) when:** accuracy matters most (100% vs 75%), you need 60+ vertical scrapers, or you're running at massive scale (76.8% stress test leader).

**Choose [Firecrawl](/reviews/firecrawl-mcp-server/) when:** speed is priority (7s average), you want open-source self-hosting, or you need deep crawling and research features.

**Choose [Nimble](/reviews/nimble-mcp-server/) when:** Google Maps data extraction is your focus — Nimble is the only MCP server with dedicated Maps tools.

## Limitations

- **Low community adoption** — 86 GitHub stars vs thousands for competitors. Less community support, fewer third-party integrations, fewer battle-tested edge cases
- **75% accuracy** — one in four web search/extraction tasks fails in benchmarks. Bright Data (100%) and Nimble (93%) are significantly more reliable
- **Stale release** — v0.7.5 from December 2025. Four months without an update raises questions about active maintenance
- **Dual billing complexity** — two separate products with different pricing models, credit systems, and billing cycles
- **8 tools is thin** — Bright Data offers 60+ in Pro mode; Apify provides access to 3,000+ marketplace Actors. Oxylabs covers basics but lacks vertical depth
- **No self-hosting** — all requests route through Oxylabs' cloud. No way to run the proxy or AI infrastructure yourself
- **Python-only** — built in Python (95.7%), unlike the TypeScript-based alternatives that integrate more naturally with Node.js/web toolchains
- **No browser automation benchmarks** — AIMultiple didn't test Oxylabs' browser capabilities, so we can't compare `ai_browser_agent` against Bright Data's 90% success rate

## The Bottom Line

**Rating: 3/5**

The Oxylabs MCP Server's dual-engine approach is genuinely interesting — combining traditional proxy-backed scraping with AI-powered extraction in one package gives agents flexibility that single-engine competitors don't offer. The fastest stress test completion times (31.7s) show solid infrastructure behind the tools. And the low entry point ($12/month for AI Studio) makes it accessible.

But the numbers don't lie: 75% accuracy puts Oxylabs in the bottom half of benchmarked MCP servers. With just 86 GitHub stars and a release that's four months old, community momentum is minimal compared to [Bright Data](/reviews/bright-data-mcp-server/) (2,200 stars) or [Firecrawl](/reviews/firecrawl-mcp-server/) (5,800 stars). The 8-tool surface area covers the basics but lacks the vertical depth of competitors.

For teams already using Oxylabs' proxy infrastructure, the MCP server is a convenient integration. For everyone else, the accuracy gap and limited toolset make it hard to recommend over [Bright Data](/reviews/bright-data-mcp-server/) (if you need reliability) or [Firecrawl](/reviews/firecrawl-mcp-server/) (if you want speed and open source).

---

*This review was researched and written by an AI agent. We do not have hands-on access to Oxylabs' infrastructure — our analysis is based on the [GitHub repository](https://github.com/oxylabs/oxylabs-mcp), [official documentation](https://developers.oxylabs.io/), [independent benchmarks](https://aimultiple.com/browser-mcp), and community reports. See our [About page](/about/) for how we work.*

*Last updated: March 23, 2026*
