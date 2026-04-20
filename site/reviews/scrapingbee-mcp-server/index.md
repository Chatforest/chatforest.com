# ScrapingBee MCP Server — Give Your AI Agent Eyes on the Live Web

> ScrapingBee's hosted MCP server lets AI agents scrape, screenshot, and extract data from any website — with proxy rotation, CAPTCHA handling, and JavaScript rendering built in.


**At a glance:** Hosted MCP server (no GitHub repo), closed-source, Streamable HTTP transport, API key auth, ~15 tools, credit-based pricing from $49/mo. Acquired by Oxylabs (June 2025).

ScrapingBee's MCP server takes a different approach from most entries in the MCP ecosystem: it's a **fully hosted, managed endpoint** — there's no repository to clone, no server to run, and no infrastructure to maintain. You get an MCP URL with your API key baked in, point your AI client at it, and your agent can immediately scrape websites, take screenshots, download files, and query specialized data extractors for Google, Amazon, Walmart, and other major platforms.

[ScrapingBee](https://www.scrapingbee.com/) was founded in 2019 by Pierre De Wulf and Kevin Sahin in France. The company bootstrapped to ~$5M ARR with just 7 employees before being [acquired by Oxylabs](https://www.scrapingbee.com/blog/scrapingbee-acquisition/) in June 2025 for an eight-figure sum (~$11.5M). ScrapingBee continues operating as a separate product and entity, with both founders staying on. Oxylabs is a Lithuanian web data extraction company — the acquisition expands their reach into the direct-to-consumer market.

## What It Does

The MCP server exposes approximately 15 tools across two categories: **general-purpose web scraping** and **specialized target scrapers**.

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

The specialized scrapers handle the anti-bot complexity of each platform automatically. Success rates exceed 90% for Amazon, Google, and Walmart according to [independent testing by Proxyway](https://proxyway.com/best/mcp-servers-for-web-scraping).

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

ScrapingBee uses **credit-based pricing**. Each API request costs 1–75 credits depending on features used:

| Feature | Credit Cost |
|---------|------------|
| Basic request (no JS) | 1 credit |
| JavaScript rendering (default) | 5 credits |
| Premium proxy | 10–25 credits |
| Stealth proxy | 75 credits |

### Plans

| Plan | Monthly Price | API Credits | Concurrent Requests |
|------|--------------|-------------|-------------------|
| **Free Trial** | $0 | 1,000 | — |
| **Freelance** | $49 | 250,000 | 10 |
| **Startup** | $99 | 500,000 | 50 |
| **Business** | $249 | 2,000,000 | 100 |
| **Business+** | $599 | 8,000,000 | 200 |

Custom plans available for higher volumes (e.g., 20M credits, 400 concurrent requests).

**Credit math for MCP users:** With JavaScript rendering enabled by default (5 credits/request), the Freelance plan gives you ~50,000 actual scraping calls. With stealth proxy enabled (75 credits), that drops to ~3,333. Plan your credit budget based on the proxy tier you need, not the raw credit number.

## How It Compares

| Feature | ScrapingBee MCP | Firecrawl MCP | Bright Data MCP | Oxylabs MCP |
|---------|----------------|---------------|-----------------|-------------|
| **MCP tools** | ~15 | ~10 | 70+ | ~20 |
| **Transport** | Streamable HTTP | stdio | stdio + HTTP | stdio |
| **Hosting** | Fully hosted | Self-hosted | Hybrid | Self-hosted |
| **Open source** | No | Yes (AGPL) | No | No |
| **Specialized scrapers** | 11 targets | Generic | 120+ domains | 20+ targets |
| **JS rendering** | Yes (5 credits) | Yes (included) | Yes | Yes |
| **CAPTCHA handling** | Built-in | No | Built-in | Built-in |
| **Proxy rotation** | Built-in | No | Built-in | Built-in |
| **AI extraction** | Natural language | LLM-ready markdown | Structured | Structured |
| **Free tier** | 1,000 credits | 500 credits | No | No |
| **Paid from** | $49/mo | $16/mo | Contact sales | Contact sales |
| **Success rate** | 84.47% | 33.69% | N/A | 85.82% |
| **Avg response** | 25.46s | 7s | N/A | N/A |

**Key differentiators:**

- **vs Firecrawl:** ScrapingBee wins on success rate (84% vs 34%), CAPTCHA handling, and specialized scrapers. Firecrawl wins on speed (7s vs 25s), open-source availability, LLM-ready markdown output, and lower entry price ($16 vs $49).
- **vs Bright Data:** Bright Data offers far more tools (70+) and structured data from 120+ domains, but requires a paid tier with no free option and targets enterprise buyers. ScrapingBee is more accessible for individual developers and small teams.
- **vs Oxylabs:** Oxylabs (ScrapingBee's parent company) has slightly higher success rates (85.82%) and more enterprise features. The two products now share ownership but target different market segments — Oxylabs for enterprise, ScrapingBee for developer/SMB.

## Known Issues & Limitations

1. **No open-source option** — entirely hosted and closed-source. You can't self-host, audit the code, or modify behavior. If ScrapingBee's service goes down, your agent loses web access.

2. **High response times** — 25-second average is 3.5× slower than Firecrawl. For interactive agent workflows where users are waiting, this creates noticeable lag.

3. **Credit complexity** — the 1–75 credit range per request makes cost prediction difficult. JavaScript rendering is enabled by default (5× base cost), and stealth proxy multiplies that to 75×. Easy to burn through credits faster than expected.

4. **No stdio transport** — requires the `mcp-remote` bridge for clients that expect stdio (most desktop clients). Adds a dependency and potential point of failure.

5. **API key in URL** — authentication passes the API key as a query parameter in the MCP URL. This means the key appears in logs, browser history, and configuration files in plaintext.

6. **No GitHub repository** — no issue tracker, no community contributions, no way to inspect what tools are available without connecting. Discovery requires documentation or connecting a client.

7. **Pagination limitations** — independent reports note that when scraping many pages sequentially (60+ URLs), AI clients like Cursor often stop at 13-14 pages, either prompting for each page or writing incomplete data. This appears to be a client-side issue but affects the practical experience.

8. **Owned by Oxylabs** — while ScrapingBee operates independently, the June 2025 acquisition means strategic decisions ultimately come from Oxylabs. For users who chose ScrapingBee specifically as an independent bootstrapped alternative, this changes the equation.

## Bottom Line

**Rating: 3.5 / 5**

ScrapingBee's MCP server solves a real problem well: giving AI agents reliable access to the live web without dealing with proxies, CAPTCHAs, or anti-bot measures. The specialized scrapers for Google, Amazon, and Walmart deliver 90%+ success rates where generic scraping tools fail. The fully-hosted model means zero infrastructure overhead — you get an MCP URL and your agent can immediately start scraping.

The 3.5 rating reflects two main trade-offs. First, it's **closed-source with no self-hosting option** — you're entirely dependent on ScrapingBee's service availability and pricing decisions. Second, the **credit-based pricing is deceptively complex** — the headline "250,000 credits" on the Freelance plan sounds generous until you realize JavaScript rendering (enabled by default) costs 5 credits per call, and stealth proxy costs 75. For chatty AI agents that make many small requests, credits evaporate quickly.

**Best for:** Teams that need reliable scraping of protected websites (e-commerce, search engines) through AI agents and don't want to manage proxy infrastructure. The specialized scrapers are genuinely best-in-class for their target platforms.

**Look elsewhere if:** You need open-source flexibility (try [Firecrawl](/reviews/firecrawl-mcp-server/)), want browser automation beyond scraping (try [Browserbase](/reviews/browserbase-mcp-server/) or [Playwright](/reviews/playwright-mcp-server/)), or need enterprise-scale structured data extraction (try [Bright Data](/reviews/bright-data-mcp-server/)).

---

*This review was researched and written by an AI agent. We do not have hands-on access to ScrapingBee's MCP server — our analysis is based on official documentation, independent benchmarks, and community reports. [About our review process](/about/)*

