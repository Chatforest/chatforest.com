---
title: "The Fetch MCP Server — Your Agent's Simplest Window to the Web (With the Lock Off)"
date: 2026-03-14T01:43:08+09:00
description: "The official Fetch MCP server gives AI agents basic web fetching with HTML-to-markdown conversion. One tool, wide adoption, and a security hole the README warns you about. Here's the honest review."
og_description: "The official Fetch MCP server lets agents fetch web pages and convert them to markdown. 85,800+ parent repo stars, ~244K weekly PyPI downloads, 1.33M monthly. CVE-2025-65513 SSRF vulnerability still unpatched after 17+ months — now two competing fix PRs, neither merged. Rating: 3.5/5."
content_type: "Review"
card_description: "Anthropic's reference web fetching server for AI agents. One tool, HTML-to-markdown conversion, robots.txt handling — but a critical SSRF CVE (17+ months unpatched, two open fix PRs stalled) and no JavaScript rendering limit it to trusted environments. ~244K weekly PyPI downloads, ~298K weekly PulseMCP visitors."
last_refreshed: 2026-05-18
categories: ["/categories/web-search-scraping/"]
---

**At a glance:** 85,800+ parent repo stars, ~244K weekly PyPI downloads, ~1.33M monthly, version 2025.4.7 (no new release since April 2025 — **13+ months**), 1 tool, ~298K weekly PulseMCP visitors (#2 globally, 28M all-time), CVE-2025-65513 (SSRF, CVSS 9.3) disclosed December 2025 — **still unpatched, 17+ months**.

The Fetch MCP server (`mcp-server-fetch`) is Anthropic's official reference implementation for giving AI agents web access. It does one thing: fetch a URL and return the content as markdown. One tool. No crawling, no search, no screenshots — just HTTP GET, content extraction, and markdown conversion.

It's one of the most widely deployed MCP servers, pulling ~202,000 weekly downloads on PyPI (~755K monthly) and 1.45 million Docker pulls. It's the #2 server on PulseMCP with 26.7 million all-time visitors. It's the default answer when someone asks "how do I let my agent read web pages?" And for basic page fetching in a trusted environment, it works fine.

But the README itself warns you: "This server can access local/internal IP addresses and may represent a security risk." That warning became more concrete in December 2025 when CVE-2025-65513 was disclosed — a critical SSRF vulnerability (CVSS 9.3) in the `is_ip_private()` validation function. As of April 2026, it remains unpatched — over 16 months since the last release.

## What's New (May 2026 Update)

The Fetch MCP server still has no new version since 2025.4.7 (April 7, 2025) — now **13+ months** without a release. Activity in the repo continues, but the pattern is consistent: PRs open, PRs accumulate, nothing merges.

**New PRs (April 22 – May 2026):**
- **Readability fallback** (PR #4002, April 22): When Readability strips >95% of content, fall back to raw HTML extraction. Open, no reviews yet.
- **HTTP content negotiation** (PR #4052, April 26): Request native markdown from servers that support it — skipping the readabilipy/markdownify pipeline for pages that already serve clean markdown. Open.
- **Second SSRF fix** (PR #4061, April 29): Submitted by OrbisAI Security, independently proposing a fix for the same SSRF vulnerability as PR #3180. Two competing security fixes, neither merged.
- **syncRoots idempotency** (PR #4107, May 5): Fixes error handling in root synchronization. Open.
- **urllib3 bump** (PR #4173, May 16): Dependabot update from 2.6.3 → 2.7.0. Open.
- **Streaming byte cap** (PR #4185, May 17): Adds an upper bound to prevent resource exhaustion from large streaming responses — a previously undocumented attack surface. Open.

**April 2026 PRs — status update:**
- **PR #3880** (Non-UTF-8 encoding): Still open; author requested merge in late April, no response.
- **PR #3876** (Tool annotations): Still open; bot-approved April 21, no human review.
- **PR #3982** (Null parameter handling): Still open.
- **PR #3739** (Page title in output): **Closed** April 19 — author closed due to maintainer inactivity.

**Security — CVE-2025-65513 now 17+ months unpatched:**
- Disclosed December 9, 2025 via Snyk advisory (discovered by Team off-course / K-Shield.Jr)
- The `is_ip_private()` function passes the full URL string instead of the hostname, causing the private IP check to always return false — enabling SSRF attacks to internal network services
- CVSS 9.3 (Critical), exploitability rated "Easy", prevalence "Common"
- **Two competing fix PRs** — #3180 (January 2026) and #4061 (April 29, OrbisAI Security) — both open, neither reviewed by maintainers. The situation has gotten worse, not better.
- The broader MCP ecosystem saw 30+ CVEs filed in January–February 2026 alone, with 43% being shell injection. A dedicated tracking project, [VulnerableMCP.info](https://vulnerablemcp.info/), now catalogs MCP-specific CVEs.

**Repo structure note:** The Fetch server remains in the active `modelcontextprotocol/servers` repo alongside Filesystem, Memory, Git, Time, Sequential Thinking, and Everything. Many other servers (AWS, GitHub, PostgreSQL, etc.) were moved to the separate `servers-archived` repository.

**What hasn't changed:** No new features, no new tools, no JavaScript rendering, no authenticated fetching, no batch mode. The server remains a single-tool reference implementation. PyPI weekly downloads have grown to ~244K (up from ~202K in April, +21%) and monthly to ~1.33M — adoption keeps rising even as the codebase stagnates.

### Earlier Updates (from our April 2026 review)

**PRs from March–April 2026 (at that time open):**
- **Non-UTF-8 encoding detection** (PR #3880, April 9): Properly detect and handle encoding for non-UTF-8 pages.
- **Tool annotations** (PR #3876, April 8): Add MCP tool annotations to improve client discovery.
- **Null parameter handling** (PR #3982, April 18): Accept null for optional parameters, fixing client compatibility issues.
- **Readability fallback** (multiple PRs, April 12–18): Attempting to fix cases where Readability strips SSR content.

**Q1 2026 fixes already merged:**
- **Malformed input crash fix** (PR #3515, March 15): Errors now caught gracefully instead of killing the server process.
- **httpx 0.28+ proxy compatibility** (PR #3293, March 7): Proxy parameter handling updated for newer httpx versions.
- **First-ever unit tests** added January 28, 2026.

## What It Does

The server exposes one tool and one prompt:

**Tool: `fetch`**
- `url` (string, required): The URL to retrieve
- `max_length` (integer, optional, default 5000): Maximum characters returned
- `start_index` (integer, optional, default 0): Starting position for content extraction — enables chunked reading of long pages
- `raw` (boolean, optional, default false): Return unprocessed content instead of extracted markdown

**Prompt: `fetch`** — Same functionality, but uses a "user-initiated" user agent string and ignores robots.txt by default. The distinction: tool calls are model-initiated (autonomous), prompt calls are user-initiated (you explicitly asked).

Under the hood, the pipeline is:

1. **HTTP request** via httpx with a 30-second timeout
2. **robots.txt check** via Protego (for tool calls; prompt calls skip this)
3. **Content extraction** via readabilipy — strips navigation, ads, boilerplate, pulls out the main article content
4. **Markdown conversion** via markdownify — ATX-style headers, clean formatting
5. **Truncation** to `max_length` with a continuation hint if content exceeds the limit

If Node.js is installed, it uses a "more robust" HTML simplifier. Otherwise, it falls back to Python-only extraction. Both paths work; the Node.js path handles edge cases better.

## Setup

It's a Python package. For Claude Desktop:

```json
{
  "mcpServers": {
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    }
  }
}
```

Or via Docker:

```json
{
  "mcpServers": {
    "fetch": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "mcp/fetch"
      ]
    }
  }
}
```

Optional flags: `--user-agent` (custom UA string), `--proxy-url` (HTTP proxy), `--ignore-robots-txt` (skip robots.txt globally).

Requirements: Python 3.10+ with uvx or pip. No API keys, no accounts.

**Setup difficulty: Very easy.** One line in your MCP config. The `uvx` approach handles dependency isolation automatically.

## What Works Well

**The HTML-to-markdown pipeline is solid.** The readabilipy + markdownify combination does a good job of extracting article content and stripping boilerplate. Navigation menus, sidebars, ads, cookie banners — most of it gets removed, leaving you with clean, readable markdown. For documentation pages, blog posts, and news articles, the output is consistently useful.

**Chunked reading handles long pages.** The `start_index` and `max_length` parameters let you paginate through long content without blowing up your context window. Fetch the first 5,000 characters, decide if you need more, then fetch the next chunk. The server helpfully tells you when there's more content remaining. This is a thoughtful design choice that respects token budgets.

**robots.txt handling is ethical and configurable.** Tool calls (autonomous agent behavior) respect robots.txt by default. Prompt calls (user-initiated) ignore it by default. This is the right split — an autonomous agent shouldn't crawl sites that ask not to be crawled, but a human explicitly requesting a page should be able to get it. The `--ignore-robots-txt` flag gives you full control. The user agent string is honest and identifiable.

**Proxy support works out of the box.** The `--proxy-url` flag lets you route requests through a proxy with no additional configuration. Useful for corporate environments or when you need to control egress.

**Wide adoption means good client support.** It works with Claude Desktop, VS Code (Copilot), Cursor, Windsurf, and Docker. One-click install buttons are available for VS Code. The server uses standard stdio transport — no exotic protocol requirements.

## What Doesn't Work Well

**No SSRF protection — CVE unpatched for 17+ months.** This remains the biggest problem, and it keeps getting worse. CVE-2025-65513 (CVSS 9.3, Critical) was disclosed in December 2025, confirming that the `is_ip_private()` function passes the full URL string instead of the hostname, causing the private IP check to always return false. The server will fetch any URL you give it, including `http://localhost:8080/admin`, `http://169.254.169.254/latest/meta-data/` (AWS instance metadata), and any other internal address. Now two competing fix PRs exist — #3180 (open since January 5, 2026) and #4061 (submitted April 29 by OrbisAI Security) — and neither has received maintainer review. A separate PR (#4185, May 17) has identified a related resource exhaustion vector from unbounded streaming responses. The broader MCP ecosystem saw 30+ CVEs in the first two months of 2026, and projects like [VulnerableMCP.info](https://vulnerablemcp.info/) now track MCP-specific vulnerabilities as a dedicated database. The README's warning is backed by a formal critical-severity CVE — this isn't theoretical risk, and it's getting more public attention, not less.

**No JavaScript rendering.** The server uses httpx for HTTP requests — plain HTTP, no browser engine. JavaScript-heavy SPAs, dynamically loaded content, and client-side rendered pages return empty or partial content. If the page you need relies on JavaScript to render its content (and increasingly, most do), Fetch won't help. You need a browser-based server like Playwright MCP or fetcher-mcp.

**5,000 character default limit is restrictive.** For many pages, 5,000 characters captures only the first few paragraphs. You'll need multiple chunked calls to read a full article, and agents don't always realize they need to continue. The limit protects context windows but creates friction. You can raise it (max 1,000,000), but then you risk the opposite problem — flooding context with a massive page dump.

**~~Crashes on malformed input.~~ Fixed (March 2026).** PR #3515 addressed the `raise_exceptions=True` issue — the server now catches errors that previously killed the process and returns them gracefully. This was a significant stability improvement.

**Single tool, no batch fetching.** You can fetch one URL per call. If your agent needs to compare three documentation pages, that's three sequential tool calls. No parallel fetching, no batch mode, no way to fetch a page and its linked resources in one call.

**No authenticated fetching.** There's no way to pass authentication headers, cookies, or API keys. If the page requires login or an API key, the server can't help. This limits it to public, unauthenticated content.

## Compared to Alternatives

**vs. zcaceres/fetch-mcp (739 GitHub stars, ~580 weekly PulseMCP visitors):** A TypeScript drop-in alternative with six tools instead of one: `fetch_html`, `fetch_markdown`, `fetch_txt`, `fetch_json`, `fetch_readable`, and `fetch_youtube_transcript`. Crucially, it includes **built-in SSRF protection** — blocks private/localhost addresses and DNS rebinding attacks. Custom headers supported. If you want the same basic fetching with better security and more output formats, this is the upgrade. PulseMCP traffic is declining though (#1,207 weekly rank), suggesting limited adoption growth.

**vs. jae-jae/fetcher-mcp (1,008 stars):** Uses a headless Playwright browser under the hood, so it **renders JavaScript**. Also supports batch URL fetching. Significantly heavier (requires a browser binary), but solves the two biggest gaps in the official server: JavaScript and batch operations. The right choice when you need to fetch modern web apps, not just static pages.

**vs. Firecrawl MCP (111,000+ parent repo stars):** The full-service option — scraping, crawling, search, JavaScript rendering, batch operations, browser automation, deep research. Cloud API with a paid tier. Now 14 tools (up from 12). Overkill for reading a docs page, but the right choice if you're building a serious web-data pipeline. In independent benchmarks, Firecrawl hits 83% accuracy on URL-to-markdown conversion. See our [browser MCP comparison](/guides/best-browser-mcp-servers/) for where Firecrawl fits in the broader landscape.

**vs. [Playwright MCP Server](/reviews/playwright-mcp-server/) (28,000+ stars):** A full browser automation server, not just a fetcher — but if your problem is "the page needs JavaScript to render," Playwright MCP solves it comprehensively via structured accessibility snapshots. Much heavier, much more capable. Different tool for a different problem, but they overlap when the issue is "Fetch returned an empty page."

**vs. Jina Reader:** Zero-config alternative — prepend `r.jina.ai/` to any URL to get markdown output. No server to install, no MCP config. For simple "fetch this doc page" use cases where you don't need a persistent MCP server, Jina Reader is the path of least resistance.

**vs. Bright Data MCP:** Enterprise-grade alternative with 100% success rate in benchmarks (single-agent), though drops to 76.8% under high concurrency (250 agents). Commercial product aimed at production scraping workloads where the official Fetch server's SSRF vulnerability and lack of JavaScript rendering are dealbreakers.

## Who Should Use This

**Yes, use it if:**
- You need basic web page fetching in a trusted, local environment
- The pages you're fetching are server-rendered (documentation, blogs, news articles)
- You want the simplest possible setup with no API keys or cloud dependencies
- You're building a prototype and need quick web access for your agent
- You control the environment and can manage the SSRF risk

**Don't use it if:**
- Your agent will fetch user-provided or untrusted URLs (SSRF risk)
- You need JavaScript-rendered content (SPAs, modern web apps)
- You need to fetch authenticated or API-key-protected content
- You need batch fetching or crawling
- You're deploying in a shared or production environment without network controls
- You need structured data extraction (JSON, tables) rather than markdown

{{< verdict rating="3.5" summary="The simplest web access for agents — just don't point it at anything internal" >}}
The Fetch MCP server does exactly what a reference implementation should: one tool, clearly defined behavior, easy setup. The HTML-to-markdown pipeline is solid, robots.txt handling is thoughtful, and with ~244K weekly PyPI downloads and ~298K weekly PulseMCP visitors it's the second most popular MCP server globally. Active development continues — encoding fixes, content negotiation, Readability improvements — even without formal releases. But the SSRF vulnerability (CVE-2025-65513, CVSS 9.3) has now been unpatched for 17+ months, and the situation has worsened: two competing fix PRs (#3180 and #4061) sit unreviewed by maintainers, and a new resource exhaustion vector (PR #4185) was identified in May 2026. No JavaScript rendering limits it to server-rendered pages, and the single-tool design means even simple multi-page tasks require multiple sequential calls. For personal use in a trusted environment fetching documentation and blog posts, it works well. For anything involving untrusted URLs, look at zcaceres/fetch-mcp (built-in SSRF protection). For JavaScript-heavy pages, look at fetcher-mcp or Playwright MCP. The official server remains the default starting point by adoption, but 13+ months without a version bump — while a critical CVE accumulates competing fix PRs that no one merges — is increasingly hard to square with "Anthropic reference implementation."
{{< /verdict >}}

*ChatForest does not test MCP servers hands-on. Our reviews are based on source code analysis, documentation review, GitHub activity, community reports, and publicly available data. We link to primary sources so you can verify our findings.*

*This review was last edited on 2026-05-18 using Claude Sonnet 4.6 (Anthropic).*
