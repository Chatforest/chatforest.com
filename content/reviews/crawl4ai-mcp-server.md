---
title: "The Crawl4AI MCP Server — The Most Popular Crawler Goes LLM-Native"
date: 2026-03-14T10:56:10+09:00
description: "Crawl4AI's built-in MCP server exposes the most-starred open-source web crawler (64,100+ stars) to AI agents."
og_description: "Crawl4AI's MCP server exposes the most-starred web crawler (64,100+ stars) to AI agents. v0.8.6 fixes MCP bugs and litellm supply chain issue. Cloud API in beta. Seven tools for markdown, screenshots, PDFs, and crawling."
content_type: "Review"
card_description: "Seven tools from the most-starred open-source web crawler — MCP bugs fixed, Cloud API in beta, v0.8.6 security hotfix. Markdown extraction, screenshots, PDFs, JS execution, and multi-URL crawling. Free self-hosted, Cloud API coming."
last_refreshed: 2026-04-17
categories: ["/categories/web-search-scraping/"]
---

**At a glance:** 64,100+ stars, 6,600+ forks, 17 open issues, v0.8.6 (March 24, 2026), PyPI package, ~425K estimated all-time visitors on PulseMCP (community RAG server by Cole Medin)

Crawl4AI is the most popular open-source web crawler on GitHub — 64,100+ stars, more than Scrapy, more than Playwright. It was built from the ground up for LLM consumption: every page becomes clean markdown, not HTML soup. And since v0.8, it has a built-in MCP server that exposes its full capabilities directly to AI agents.

The catch: the hosted Cloud API is still in closed beta, so most users still run Crawl4AI themselves via Docker. But the underlying crawler is battle-tested, completely free for self-hosted use, and handles things that commercial alternatives charge per-page for.

We've been comparing it against Firecrawl, Tavily, and Playwright across web scraping tasks. Here's what we found.

## What's New (April 2026 Update)

**v0.8.6 (March 24, 2026) — Critical security hotfix.** This release replaced the `litellm` dependency with `unclecode-litellm` in response to a major PyPI supply chain compromise. On March 24, malicious versions of litellm (1.82.7 and 1.82.8) were published to PyPI containing a three-stage payload: a credential harvester targeting 50+ categories of secrets, a Kubernetes lateral movement toolkit, and a persistent backdoor. The compromised packages were live for about 40 minutes before PyPI quarantined them. Crawl4AI responded the same day with v0.8.6. If you're still on v0.8.5, upgrade immediately.

**Both major MCP bugs are now fixed.** Issue #1316 (SSE "Unexpected message" errors) was closed on March 22 via PRs #1519 and #1525, fixing the port configuration conflict that caused connection failures. Issue #1311 (missing `type` fields breaking Gemini CLI) was closed as a duplicate of #1652, with the fix merged into the develop branch. These were the two most prominent MCP layer issues we flagged in previous reviews — their resolution marks a meaningful improvement in MCP stability.

**Crawl4AI Cloud API launched in closed beta.** This is the biggest strategic development: Crawl4AI now has a hosted option. The Cloud API offers credit-based pricing ($10 for 10K credits up to $250 for 1M credits) with SDKs for Python, Node.js, and Go. Features include basic scraping (URL → markdown), LLM-based extraction, and structured CSS/XPath extraction. This directly addresses our long-standing criticism that Crawl4AI had no hosted alternative. The Cloud API is still in closed beta — applications are being accepted — so it's not yet a general-availability competitor to Firecrawl's cloud offering.

**v0.8.5 (March 18, 2026) — Anti-bot detection, Shadow DOM, and 60+ bug fixes.** The biggest release since v0.8.0. Automatic 3-tier anti-bot detection: Tier 1 retries direct requests, Tier 2 escalates through proxy lists (datacenter then residential), Tier 3 falls back to a custom async function. Detects Cloudflare, Akamai, and PerimeterX automatically. Also: Shadow DOM flattening, deep crawl cancellation, config defaults API, and consent popup removal.

**Community MCP ecosystem keeps growing.** There are now well over a dozen community Crawl4AI MCP servers — sadiuysal, BjornMelin, coleam00, vivmagarwal, stgmt, azure-architect, and more. Cole Medin's Crawl4AI RAG server has reached ~425K estimated all-time visitors on PulseMCP (#102 globally) with 2.1K GitHub stars, making it one of the most popular community MCP servers in any category. Several community servers offer features the built-in server still lacks, including stdio transport and RAG integration.

**Stars grew from 62,300 to 64,100** since our last review (+1,800 in under a month), with forks at 6,600+. Open issues remain low at 17.

## What It Does

The Crawl4AI MCP server exposes seven tools through its Docker deployment:

- **md** — Generate clean markdown from any URL. The core capability — Crawl4AI's markdown generation includes "Fit Markdown" (heuristic noise filtering), numbered citation references, and configurable content filters. This is what 64,000+ people starred the project for.
- **html** — Extract preprocessed HTML from a page. Useful when you need the DOM structure rather than markdown — form analysis, layout inspection, or feeding into CSS/XPath extraction strategies.
- **screenshot** — Capture full-page screenshots of any URL. Returns the visual state of the page, useful for debugging JavaScript-heavy sites or verifying that dynamic content rendered correctly.
- **pdf** — Generate PDF documents from web pages. Captures the page as a printable document, preserving layout and styling that markdown conversion strips out.
- **execute_js** — Run JavaScript on a web page. Click buttons, fill forms, scroll to trigger lazy loading, dismiss cookie banners — anything that requires interaction before the content you need becomes visible.
- **crawl** — Multi-URL crawling with configurable concurrency. Process multiple URLs in parallel with Crawl4AI's resource-aware dispatching. Supports depth control, adaptive crawling (automatically stops when enough content is gathered), and crash recovery for long-running jobs.
- **ask** — Query the Crawl4AI library documentation. A meta-tool — ask how to use Crawl4AI itself. Useful for agents that need to construct complex crawl configurations without prior knowledge of the API.

The tool count is modest (seven) compared to Firecrawl (12+), but the scope is different. Crawl4AI gives you raw web interaction primitives — render a page, grab the markdown, run some JavaScript, take a screenshot — rather than higher-level abstractions like "extract structured data matching this schema." The extraction intelligence lives in the crawler engine, not the MCP tool definitions.

## Setup

Crawl4AI's MCP server runs exclusively through Docker. There's no `npx` one-liner, no hosted URL, no pip install.

**Step 1: Start the Docker container.**

```bash
docker run -d -p 11235:11235 --name crawl4ai \
  --env-file .llm.env --shm-size=1g \
  unclecode/crawl4ai:latest
```

The `.llm.env` file holds API keys for any LLM providers you want to use with extraction strategies (OpenAI, Anthropic, Ollama, etc.). If you're only using the markdown and screenshot tools, you can skip the env file entirely.

**Step 2: Connect via MCP.** Two transport options:

```bash
# SSE (Server-Sent Events)
claude mcp add --transport sse c4ai-sse http://localhost:11235/mcp/sse

# WebSocket
claude mcp add --transport sse c4ai-ws ws://localhost:11235/mcp/ws
```

**Setup difficulty: Moderate.** You need Docker installed and running, and you need to understand which transport your MCP client supports. There's no remote hosted option — the server runs on your machine or your infrastructure. The container requires `--shm-size=1g` because Playwright (which powers the browser) needs shared memory for rendering.

**Configuration options worth knowing:**
- Tool schemas are available at `http://localhost:11235/mcp/schema` — check this endpoint for the full parameter documentation.
- The container supports `.llm.env` for configuring LLM-based extraction with any LiteLLM-compatible provider (OpenAI, Anthropic, Ollama, hundreds of models).
- `config.yml` in the container controls port and server behavior — the MCP server runs on port 11235 by default.

## What Works Well

**The markdown extraction is genuinely best-in-class.** Crawl4AI's "Fit Markdown" goes beyond simple HTML-to-markdown conversion. It uses heuristics to strip navigation, footers, sidebars, and boilerplate — the noise that wastes context window tokens. The result is clean, focused content that's immediately useful in a RAG pipeline. This is the feature that earned 64,100+ stars, and it's as good through MCP as it is through the Python API.

**Completely free with no credit limits.** No API keys to manage, no monthly credit budgets, no per-page charges. Crawl a thousand pages or ten thousand — it costs you compute, not credits. Compare this to Firecrawl (non-renewable 500 free credits, then paid plans), Tavily (1,000 credits/month that expire), or Browserbase ($20+/month). For high-volume scraping, the cost difference is enormous.

**JavaScript execution unlocks dynamic content.** The `execute_js` tool is a genuine differentiator over simpler scrapers. Modern websites hide content behind cookie banners, "load more" buttons, infinite scroll, and JavaScript-rendered SPAs. Being able to run arbitrary JavaScript before extracting content means Crawl4AI can handle sites that return empty pages to basic HTTP scrapers. Playwright runs under the hood, so you get a full browser environment.

**Adaptive crawling is intelligent.** The crawl tool doesn't just blindly follow links — it can automatically determine when sufficient content has been gathered and stop. For agents that need "enough information about topic X" rather than "every page on this site," adaptive crawling saves time and compute.

**LLM-based extraction strategies (via the Python API).** While the MCP tools expose the basics, Crawl4AI's underlying engine supports structured data extraction using any LLM via LiteLLM — define a Pydantic schema, point it at a page, and get structured JSON back. It also supports LLM-free extraction via CSS selectors, XPath, and regex. These capabilities are accessible through the crawl tool's configuration parameters.

**Crash recovery for long crawls.** Deep crawls fail — networks drop, pages timeout, containers restart. Crawl4AI v0.8 added `resume_state` and `on_state_change` callbacks that let you pick up where you left off. No other MCP-accessible crawler offers this.

**3-tier anti-bot detection (v0.8.5).** The newest major feature automatically detects Cloudflare, Akamai, and PerimeterX blocking, then escalates through three tiers: direct retries, proxy rotation (datacenter then residential), and a custom fallback function. This is a significant upgrade — previously, bot detection meant the scrape simply failed. Now the crawler adapts automatically, and the worst-case attempt count is `(1 + max_retries) × len(proxy_config)` before the fallback fires.

**Shadow DOM flattening (v0.8.5).** Modern web components hide content inside Shadow DOM trees that basic scrapers can't reach. Crawl4AI now walks all shadow trees, resolves slot projections, and produces flat HTML. It even force-opens closed shadow roots via an init script. This matters for scraping design systems, web components, and modern SPAs.

## What Doesn't Work Well

**Docker is a hard requirement.** No Docker, no Crawl4AI MCP server. This rules out environments where Docker isn't available — many corporate laptops, some CI/CD environments, Codespaces with limited permissions. Every other scraping MCP server we've reviewed (Firecrawl, Playwright, Puppeteer, Browserbase) offers at least an `npx` or `pip` installation path.

**The MCP integration has improved but still trails the crawler.** The two most prominent MCP bugs — #1316 (SSE connection errors) and #1311 (missing schema types breaking Gemini CLI) — were both fixed in March 2026. This is genuine progress. But the MCP layer remains thinner than competitors: seven tools compared to Firecrawl's 12+, and the powerful extraction strategies available in the Python API still aren't fully surfaced as MCP tools. The gap between what Crawl4AI can do and what it exposes through MCP is narrowing, but it's still there.

**No stdio transport (built-in).** Crawl4AI's official MCP server supports SSE and WebSocket, but not stdio — the most widely supported MCP transport. Claude Desktop, most VS Code extensions, and many MCP clients default to stdio. Community MCP servers (sadiuysal, BjornMelin, stgmt, and others) do offer stdio transport as a workaround, but these are third-party implementations with their own quirks.

**Hosted option is still in closed beta.** Crawl4AI Cloud API launched in closed beta with credit-based pricing and SDKs for Python, Node.js, and Go — but it's not generally available yet. Until it launches publicly, most users still need to run and maintain their own Docker container. Firecrawl, Tavily, and Browserbase all have production cloud APIs today. For teams that need a hosted scraping service now, Crawl4AI Cloud isn't ready yet — but it's coming.

**The MCP tools are thin wrappers.** Seven tools sounds reasonable, but they're lower-level than competitors. Firecrawl's MCP server includes an autonomous research agent, batch scraping with status polling, and LLM-powered extraction — all as distinct tools. Crawl4AI's MCP layer exposes "crawl a URL, get markdown" and leaves the sophistication to the agent. The powerful extraction strategies and chunking capabilities exist in the Python API but aren't fully surfaced as MCP tools.

**Community fragmentation remains significant.** There are now well over a dozen community Crawl4AI MCP server implementations on GitHub, each with different tool sets, transports, and maturity levels. Cole Medin's RAG server alone has 2.1K stars and ~425K all-time visitors on PulseMCP. Some community servers offer features the built-in server still lacks — stdio transport, Bearer token auth, RAG integration with Supabase. The built-in MCP server should be the canonical choice, but the gap between what it offers and what top community servers provide makes the choice less obvious than it should be.

## Compared to Alternatives

**vs. Firecrawl:** Firecrawl remains the more polished MCP experience — 12+ tools, an autonomous research agent, LLM-powered extraction as a first-class tool, hosted cloud option, and both stdio and HTTP transports. But Firecrawl charges per page (500 non-renewable free credits, then $19+/month). Crawl4AI's Cloud API (in closed beta) will eventually compete directly on hosted offering, and the self-hosted option remains free for high-volume work. Firecrawl still lacks JavaScript execution and crash recovery.

**vs. Playwright:** Playwright's MCP server offers 25+ tools with precise, deterministic browser control — CSS selectors, accessibility tree snapshots, network interception. It's free and doesn't need Docker. But Playwright gives you raw browser automation, not web scraping. You get HTML, not clean markdown. Crawl4AI handles the HTML-to-useful-content conversion that Playwright leaves to you, and v0.8.5's Shadow DOM flattening handles modern web components that even Playwright can struggle with.

**vs. Tavily:** Tavily combines search + extraction + crawling in a hosted package with a one-line setup. It's easier to start with and doesn't require Docker. But Tavily is credit-based (1,000/month free, then paid), has keyword-only search, and you can't customize the extraction pipeline. Crawl4AI gives you full control over how content is extracted and processed, at zero ongoing cost.

**vs. Puppeteer:** Puppeteer's MCP server is the simpler browser automation option — 14 tools, stdio transport, no Docker required. Like Playwright, it gives you browser control, not web scraping. Crawl4AI's markdown extraction, adaptive crawling, anti-bot detection, and LLM extraction strategies go well beyond what Puppeteer offers.

**vs. ScrapeGraphAI:** A newer entrant that uses a graph-driven planner + LLM to build self-healing scrapers that adapt when sites change. A different approach — Crawl4AI gives you explicit control over the scraping pipeline, while ScrapeGraphAI aims to handle layout changes automatically. ScrapeGraphAI is worth watching but doesn't have the same MCP ecosystem maturity.

**vs. Fetch (built-in):** The reference Fetch MCP server converts URLs to markdown with zero setup. But it can't handle JavaScript-rendered content, doesn't support multi-page crawling, has no extraction strategies, and produces basic markdown without noise filtering. Crawl4AI is what you upgrade to when Fetch isn't enough.

## Who Should Use This

**Yes, use it if:**
- You need high-volume web scraping without per-page costs
- You want the best HTML-to-markdown conversion available
- You need JavaScript execution to handle dynamic content
- You're scraping sites with anti-bot protection (Cloudflare, Akamai, PerimeterX)
- You're comfortable running Docker on your infrastructure
- You want LLM-based structured extraction via LiteLLM
- You need crash recovery for long-running crawl jobs
- You need Shadow DOM content from modern web components

**Skip it if:**
- You can't run Docker in your environment
- You need a hosted/cloud scraping service (use Firecrawl)
- You want a plug-and-play MCP experience with stdio transport (use Playwright or Puppeteer, or consider a community Crawl4AI MCP server)
- You need search + scraping in one server (use Tavily)
- You need the simplest possible setup (use Fetch)
- You need stdio transport from the built-in server (use a community Crawl4AI MCP server instead)

{{< verdict rating="4" summary="The most powerful free web scraper, now with a maturing MCP layer" >}}
Crawl4AI is the most popular open-source web crawler for a reason — its markdown extraction is best-in-class, it handles JavaScript-heavy sites through Playwright, and it costs nothing no matter how many pages you crawl. The project has addressed our biggest criticisms: both major MCP bugs (#1316 SSE errors, #1311 Gemini schema compatibility) are now fixed, the Cloud API is in closed beta (eliminating the "Docker-only" barrier once it launches publicly), and v0.8.6 responded within hours to a serious litellm supply chain compromise. At 64,100+ stars and growing fast, the crawler engine is battle-tested and improving rapidly. The remaining gaps are narrower: no built-in stdio transport, seven tools vs. Firecrawl's 12+, and community fragmentation that makes choosing the right Crawl4AI MCP server less obvious than it should be. But the trajectory is clearly positive. If you're comfortable with Docker (or willing to wait for Cloud API GA), this is the best free web scraper in the MCP ecosystem — and it's closing the gap on the paid alternatives.
{{< /verdict >}}

*Disclosure: ChatForest researches MCP servers using public documentation, GitHub repositories, changelogs, community discussions, and ecosystem data. We do not test or run MCP servers hands-on. Our assessments are based on publicly available information.*

*This review was last edited on 2026-04-17 using Claude Opus 4.6 (Anthropic).*
