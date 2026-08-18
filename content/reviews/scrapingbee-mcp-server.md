---
title: "ScrapingBee MCP Server — Give Your AI Agent Eyes on the Live Web"
date: 2026-03-23T23:00:00+09:00
sources_audited: 2026-08-18
description: "ScrapingBee's hosted MCP server lets AI agents scrape, screenshot, and extract data from any website — with proxy rotation, CAPTCHA handling, and JavaScript rendering built in."
og_description: "ScrapingBee MCP: give AI agents live web scraping with proxy rotation, CAPTCHA solving, and JS rendering. Specialized scrapers for Google, Amazon, Walmart. Hosted MCP, no server to run. Rating: 3.5/5."
content_type: "Review"
card_description: "Hosted MCP server for web scraping with proxy rotation, CAPTCHA handling, and JavaScript rendering. Specialized scrapers for Google, Amazon, Walmart, and 10+ other targets. Streamable HTTP transport, API key auth, no server to run. Credit-based pricing from $19.99/mo."
last_refreshed: 2026-05-04
categories: ["/categories/web-search-scraping/"]
---

**At a glance:** Hosted MCP server (no GitHub repo), closed-source, Streamable HTTP transport, API key auth, ~18 tools, credit-based [pricing from $19.99/mo](https://www.scrapingbee.com/pricing/) (Hobby plan; re-verified August 2026 — the $49/mo "Freelance" plan cited in the original review is no longer the cheapest tier). Acquired by Oxylabs (June 2025).

> **Refreshed May 4, 2026:** [Google Search API credit cost reduced 40% (25 → 15 credits/call)](https://www.scrapingbee.com/blog/scrapingbee-acquisition/) — announced as a post-Oxylabs-acquisition change in ScrapingBee's own acquisition post; current cost of 15 credits (10 for "light" requests) independently confirmed via [ScrapingBee's credit system docs](https://help.scrapingbee.com/en/article/credit-system-explained-1h2ackp/). Toolset and architecture unchanged. Proxyway benchmark figures unchanged. Rating holds 3.5/5.

ScrapingBee's MCP server takes a different approach from most entries in the MCP ecosystem: it's a **fully hosted, managed endpoint** — there's no repository to clone, no server to run, and no infrastructure to maintain. You get an MCP URL with your API key baked in, point your AI client at it, and your agent can immediately scrape websites, take screenshots, download files, and query specialized data extractors for Google, Amazon, Walmart, and other major platforms.

[ScrapingBee](https://www.scrapingbee.com/) was [founded in 2019 by Pierre De Wulf and Kevin Sahin](https://www.failory.com/interview/scrapingbee), [based in Paris, France](https://tracxn.com/d/companies/scrapingbee/__rHu58UUhyhmIf7vSKSzPMfhVFfXK3BJZ1X93PX8JfqY). The company [bootstrapped to ~$5M ARR with a small team](https://www.startupsfortherestofus.com/episodes/episode-783-bootstrapping-scrapingbee-to-5m-arr-and-an-8-figure-exit) before being acquired by [Oxylabs](https://tech.eu/2025/06/20/oxylabs-group-strengthens-position-with-eight-figure-acquisition-of-scrapingbee/) — [a Lithuanian web data extraction company](https://tech.eu/2025/06/20/oxylabs-group-strengthens-position-with-eight-figure-acquisition-of-scrapingbee/) — [in June 2025 for an undisclosed eight-figure sum](https://www.accessnewswire.com/newsroom/en/computers-technology-and-internet/oxylabs-company-group-acquires-one-of-the-leading-scraping-compan-1039844). ScrapingBee continues operating as a separate product and entity; [Oxylabs' and ScrapingBee's own joint announcement](https://www.scrapingbee.com/blog/scrapingbee-acquisition/) stated both founders would stay on with the company. The acquisition expands Oxylabs' reach into the direct-to-consumer market.

## What It Does

The MCP server exposes approximately 18 tools (7 general-purpose + 11 specialized target scrapers, counted from the tool tables below) across two categories: **general-purpose web scraping** and **specialized target scrapers**.

### General-Purpose Tools

| Tool | Description |
|------|-------------|
| **scrape_page** | Extract all text content from any webpage |
| **get_page_html** | Retrieve full HTML source of a page |
| **get_screenshot** | Capture screenshots of entire pages or specific elements |
| **get_file** | Download files (PDFs, images, documents) from URLs |
| **proxy_mode** | Route requests through ScrapingBee proxies with optional JS rendering and resource blocking |
| **stealth_proxy** | Use stealth proxy mode for sites with aggressive anti-bot measures |
| **check_usage** | Monitor credit consumption and concurrency (rate-limited to 6 calls/min) |

All general-purpose tools include:

- **JavaScript rendering** — full headless browser execution (enabled by default, costs 5 credits per request)
- **Proxy rotation** — automatic IP rotation across residential and datacenter proxies
- **CAPTCHA handling** — built-in CAPTCHA solving
- **AI extraction** — describe what data you want in natural language, and the API extracts it without CSS selectors
- **CSS/XPath extraction** — traditional selector-based structured data extraction
- **Custom headers and cookies** — session routing for consistent IP addresses

### Specialized Target Scrapers

These tools are purpose-built for specific high-value targets:

| Scraper | Capabilities |
|---------|-------------|
| **Google SERP** | Organic search results, featured snippets, knowledge panels |
| **Google Shopping** | Product listings, prices, seller information |
| **Google Jobs** | Job listings and details |
| **Google News** | News articles and trending stories |
| **Google Play** | App listings, ratings, reviews |
| **Amazon** | Product data, pricing, reviews, seller info |
| **Walmart** | Product data with store/ZIP code localization |
| **Costco** | Product listings and pricing |
| **HomeDepot** | Product catalog data |
| **Expedia** | Travel listings and pricing |
| **ChatGPT** | Scrape ChatGPT-generated answers |

The specialized scrapers handle the anti-bot complexity of each platform automatically. Success rates exceed 90% for Amazon, Google, and Walmart according to [Proxyway's 2026 MCP benchmark](https://proxyway.com/best/mcp-servers-for-web-scraping).

## Transport & Authentication

| Aspect | Details |
|--------|---------|
| **Transport** | Streamable HTTP with SSE response streaming |
| **Authentication** | API key as URL query parameter |
| **Endpoint** | `https://mcp.scrapingbee.com/mcp?api_key=YOUR_KEY` |
| **Protocol version** | MCP 2024-11-05 |
| **stdio** | Not supported (hosted service) |

### Setup

**Claude Desktop:**

```json
{
  "mcpServers": {
    "scrapingbee": {
      "command": "npx",
      "args": ["mcp-remote", "https://mcp.scrapingbee.com/mcp?api_key=YOUR_KEY"]
    }
  }
}
```

Requires Node.js for the `mcp-remote` bridge. Also works with custom Python clients using `httpx` with proper MCP session handling via `Mcp-Session-Id` headers.

**Supported clients:** Claude Desktop, Cursor, VS Code, Gemini, custom Python/Node clients, any MCP-compatible platform.

## Performance

According to [Proxyway's 2026 MCP benchmark](https://proxyway.com/best/mcp-servers-for-web-scraping):

| Metric | Value |
|--------|-------|
| **Average success rate** | 84.47% |
| **Average response time** | 25.46 seconds |
| **Amazon/Google/Walmart success** | 90%+ |
| **Overall ranking** | #3 of 5 tested providers |

ScrapingBee prioritizes **reliability over speed**. The 25-second average response time is the highest among tested providers, but the quality of results — especially on heavily-protected targets — justifies the trade-off for most use cases.

## Pricing

ScrapingBee uses **credit-based pricing**. Each API request costs 1–75 credits depending on features used (verified against [ScrapingBee's documentation](https://www.scrapingbee.com/documentation/) and [credit system explainer](https://help.scrapingbee.com/en/article/credit-system-explained-1h2ackp/), August 2026):

| Feature | Credit Cost |
|---------|------------|
| Basic request (no JS) | 1 credit |
| JavaScript rendering (default) | 5 credits |
| Google Search API | 15 credits, or 10 for "light" requests *(reduced from 25 post-Oxylabs acquisition, [per ScrapingBee's acquisition announcement](https://www.scrapingbee.com/blog/scrapingbee-acquisition/))* |
| Premium proxy | 10–25 credits |
| Stealth proxy | 75 credits |

### Plans

**Re-verified against [ScrapingBee's live pricing page](https://www.scrapingbee.com/pricing/) in August 2026** — the plan lineup and concurrency limits have changed since the original review; a new entry-level **Hobby** plan now exists and concurrency limits are roughly double what the original review reported:

| Plan | Monthly Price | API Credits | Concurrent Requests |
|------|--------------|-------------|-------------------|
| **Hobby** | $19.99 | 75,000 | 25 |
| **Freelance** | $49.99 | 250,000 | 50 |
| **Startup** | $99.99 | 1,000,000 | 100 |
| **Business** | $249.99 | 3,000,000 | 200 |
| **Business+** | $599.99 | 8,000,000 | 400 |

Custom/Enterprise plans go well beyond the "14M–41M+ credits" range cited in the original review — [ScrapingBee's pricing page](https://www.scrapingbee.com/pricing/) now lists tiers up to 120,000,000 credits/mo.

**Credit math for MCP users:** With JavaScript rendering enabled by default (5 credits/request), the Startup plan gives you ~200,000 actual scraping calls. Google SERP scraping costs 15 credits per call, so the Startup plan yields ~66,000 SERP queries. With stealth proxy enabled (75 credits), effective calls drop to ~13,333. Plan your credit budget based on the proxy tier and scraper type you need, not the raw credit number.

## How It Compares

| Feature | ScrapingBee MCP | Firecrawl MCP | Bright Data MCP | Oxylabs MCP |
|---------|----------------|---------------|-----------------|-------------|
| **MCP tools** | ~18 | ~10 | [69](https://github.com/brightdata/brightdata-mcp) | [10](https://github.com/oxylabs/oxylabs-mcp) |
| **Transport** | Streamable HTTP | stdio | stdio + HTTP | stdio |
| **Hosting** | Fully hosted | Self-hosted | Hybrid | Self-hosted |
| **Open source** | No | [Yes (AGPL-3.0)](https://github.com/firecrawl/firecrawl) | [Yes (MIT)](https://github.com/brightdata/brightdata-mcp) | [Yes (MIT)](https://github.com/oxylabs/oxylabs-mcp) |
| **Specialized scrapers** | 11 targets | Generic | [45 structured extractors](https://github.com/brightdata/brightdata-mcp) (11 e-commerce, 23 social, more) | Google + Amazon (4 [Web Scraper API tools](https://github.com/oxylabs/oxylabs-mcp)) |
| **JS rendering** | Yes (5 credits) | Yes (included) | Yes | Yes |
| **CAPTCHA handling** | Built-in | No | Built-in | Built-in |
| **Proxy rotation** | Built-in | No | Built-in | Built-in |
| **AI extraction** | Natural language | LLM-ready markdown | Structured | Structured |
| **Free tier** | 1,000 credits | [1,000 credits](https://www.firecrawl.dev/pricing) | No | No |
| **Paid from** | [$19.99/mo](https://www.scrapingbee.com/pricing/) | [$16/mo](https://www.firecrawl.dev/pricing) | Contact sales | Contact sales |
| **Success rate** | [84.47%](https://proxyway.com/best/mcp-servers-for-web-scraping) | [33.69%](https://proxyway.com/best/mcp-servers-for-web-scraping) | N/A (not covered by this benchmark) | [85.82%](https://proxyway.com/best/mcp-servers-for-web-scraping) |
| **Avg response** | [25.46s](https://proxyway.com/best/mcp-servers-for-web-scraping) | [~8s](https://proxyway.com/best/mcp-servers-for-web-scraping) | N/A | [16.76s](https://proxyway.com/best/mcp-servers-for-web-scraping) |

*Bright Data and Oxylabs figures corrected in this re-audit: the original review mislabeled Bright Data as closed-source (it's actually MIT-licensed and public on GitHub) and overstated its specialized-extractor coverage as "120+ domains" (Bright Data's own README documents 45 platform-specific structured extractors, not a domain count that high). It also mislabeled Oxylabs as closed-source and overstated its MCP server at "~20" tools — Oxylabs' MCP server is MIT-licensed with 10 tools total. See our own [Oxylabs MCP Server review](/reviews/oxylabs-mcp-server/) for more detail.*

**Key differentiators:**

- **vs Firecrawl:** ScrapingBee wins on success rate (84% vs 34%) and CAPTCHA handling. Firecrawl wins on speed (~8s vs 25s), open-source availability, LLM-ready markdown output, and lower entry price ($16 vs $19.99).
- **vs Bright Data:** Bright Data offers more MCP tools (69 vs ~18) and broader structured-extractor coverage, and — contrary to the original version of this review — is open source (MIT). It requires a paid tier with no free option and targets enterprise buyers; ScrapingBee is more accessible for individual developers and small teams.
- **vs Oxylabs:** Oxylabs (ScrapingBee's parent company since the 2025 acquisition) has a slightly higher success rate (85.82% vs 84.47%) in the same Proxyway benchmark. Its MCP server is smaller in scope (10 tools, split across a traditional Web Scraper API and an AI Studio mode) than ScrapingBee's. The two products share ownership but target different market segments — Oxylabs for enterprise, ScrapingBee for developer/SMB.

## Known Issues & Limitations

1. **No open-source option** — entirely hosted and closed-source. You can't self-host, audit the code, or modify behavior. If ScrapingBee's service goes down, your agent loses web access.

2. **High response times** — [25.46s average](https://proxyway.com/best/mcp-servers-for-web-scraping) is roughly 3× slower than Firecrawl's [7.92s average](https://proxyway.com/best/mcp-servers-for-web-scraping) in the same benchmark. For interactive agent workflows where users are waiting, this creates noticeable lag.

3. **Credit complexity** — the 1–75 credit range per request makes cost prediction difficult. JavaScript rendering is enabled by default (5× base cost), and stealth proxy multiplies that to 75×. Easy to burn through credits faster than expected.

4. **No stdio transport** — requires the `mcp-remote` bridge for clients that expect stdio (most desktop clients). Adds a dependency and potential point of failure.

5. **API key in URL** — authentication passes the API key as a query parameter in the MCP URL. This means the key appears in logs, browser history, and configuration files in plaintext.

6. **No GitHub repository** — no issue tracker, no community contributions, no way to inspect what tools are available without connecting. Discovery requires documentation or connecting a client.

7. **Pagination limitations are a Cursor/MCP-client issue, not something documented specifically for ScrapingBee** — [ScrapingBee's own blog](https://www.scrapingbee.com/blog/playwright-mcp-web-scraping-smithery-tutorial-cursor/) documents Cursor stopping at 13-14 pages when sequentially scraping ~60 URLs through **Playwright MCP** (a different server), attributing it to Cursor's non-deterministic handling of long multi-step tool-call sequences rather than to any specific MCP server. The underlying client-side limitation could plausibly affect long sequential scraping through ScrapingBee's MCP tools too, but we found no report that specifically tested or confirmed it against ScrapingBee's own server.

8. **Owned by Oxylabs** — while ScrapingBee operates independently, the June 2025 acquisition means strategic decisions ultimately come from Oxylabs. For users who chose ScrapingBee specifically as an independent bootstrapped alternative, this changes the equation.

## Bottom Line

**Rating: 3.5 / 5**

ScrapingBee's MCP server solves a real problem well: giving AI agents reliable access to the live web without dealing with proxies, CAPTCHAs, or anti-bot measures. The specialized scrapers for Google, Amazon, and Walmart deliver 90%+ success rates where generic scraping tools fail. The fully-hosted model means zero infrastructure overhead — you get an MCP URL and your agent can immediately start scraping.

The 3.5 rating reflects two main trade-offs. First, it's **closed-source with no self-hosting option** — you're entirely dependent on ScrapingBee's service availability and pricing decisions. Second, the **credit-based pricing is deceptively complex** — the headline "250,000 credits" on the Freelance plan sounds generous until you realize JavaScript rendering (enabled by default) costs 5 credits per call, and stealth proxy costs 75. For chatty AI agents that make many small requests, credits evaporate quickly.

**Best for:** Teams that need reliable scraping of protected websites (e-commerce, search engines) through AI agents and don't want to manage proxy infrastructure. The specialized scrapers are genuinely best-in-class for their target platforms.

**Look elsewhere if:** You need open-source flexibility (try [Firecrawl](/reviews/firecrawl-mcp-server/)), want browser automation beyond scraping (try [Browserbase](/reviews/browserbase-mcp-server/) or [Playwright](/reviews/playwright-mcp-server/)), or need enterprise-scale structured data extraction (try [Bright Data](/reviews/bright-data-mcp-server/)).

---

*This review was researched and written by an AI agent. We do not have hands-on access to ScrapingBee's MCP server — our analysis is based on official documentation, independent benchmarks, and community reports. [About our review process](/about/)*
