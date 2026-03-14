---
title: "The Fetch MCP Server — Your Agent's Simplest Window to the Web (With the Lock Off)"
date: 2026-03-14T01:43:08+09:00
description: "The official Fetch MCP server gives AI agents basic web fetching with HTML-to-markdown conversion. One tool, wide adoption, and a security hole the README warns you about. Here's the honest review."
og_description: "The official Fetch MCP server lets agents fetch web pages and convert them to markdown. Simple and widely adopted, but no SSRF protection and no JavaScript rendering. Rating: 3.5/5."
content_type: "Review"
card_description: "Anthropic's reference web fetching server for AI agents. One tool, HTML-to-markdown conversion, robots.txt handling — but no SSRF protection and no JavaScript rendering limit it for anything beyond trusted environments."
---

The Fetch MCP server (`mcp-server-fetch`) is Anthropic's official reference implementation for giving AI agents web access. It does one thing: fetch a URL and return the content as markdown. One tool. No crawling, no search, no screenshots — just HTTP GET, content extraction, and markdown conversion.

It's one of the most widely deployed MCP servers, pulling ~140,000 weekly downloads on PyPI. It's the default answer when someone asks "how do I let my agent read web pages?" And for basic page fetching in a trusted environment, it works fine.

But the README itself warns you: "This server can access local/internal IP addresses and may represent a security risk." That's not boilerplate — it's a genuine security gap that matters.

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

**No SSRF protection.** This is the biggest problem. The server will fetch any URL you give it, including `http://localhost:8080/admin`, `http://169.254.169.254/latest/meta-data/` (AWS instance metadata), and any other internal address. If an AI agent can be prompted to fetch URLs — and they can — this is a real attack surface. An open PR (#3180) proposes adding SSRF protection, but as of March 2026, it hasn't been merged. The README warns about this, but a warning isn't a fix.

**No JavaScript rendering.** The server uses httpx for HTTP requests — plain HTTP, no browser engine. JavaScript-heavy SPAs, dynamically loaded content, and client-side rendered pages return empty or partial content. If the page you need relies on JavaScript to render its content (and increasingly, most do), Fetch won't help. You need a browser-based server like Playwright MCP or fetcher-mcp.

**5,000 character default limit is restrictive.** For many pages, 5,000 characters captures only the first few paragraphs. You'll need multiple chunked calls to read a full article, and agents don't always realize they need to continue. The limit protects context windows but creates friction. You can raise it (max 1,000,000), but then you risk the opposite problem — flooding context with a massive page dump.

**Crashes on malformed input.** An open bug (#3359) reports that the server crashes instead of returning an error when given certain malformed inputs. The underlying cause is `raise_exceptions=True` in the HTTP client — errors that should be caught and returned gracefully instead kill the server process. For a reference implementation, this is a basic robustness gap.

**Single tool, no batch fetching.** You can fetch one URL per call. If your agent needs to compare three documentation pages, that's three sequential tool calls. No parallel fetching, no batch mode, no way to fetch a page and its linked resources in one call.

**No authenticated fetching.** There's no way to pass authentication headers, cookies, or API keys. If the page requires login or an API key, the server can't help. This limits it to public, unauthenticated content.

## Compared to Alternatives

**vs. zcaceres/fetch-mcp (714 GitHub stars):** A TypeScript drop-in alternative with six tools instead of one: `fetch_html`, `fetch_markdown`, `fetch_txt`, `fetch_json`, `fetch_readable`, and `fetch_youtube_transcript`. Crucially, it includes **built-in SSRF protection** — blocks private/localhost addresses and DNS rebinding attacks. Custom headers supported. If you want the same basic fetching with better security and more output formats, this is the upgrade.

**vs. jae-jae/fetcher-mcp (1,008 stars):** Uses a headless Playwright browser under the hood, so it **renders JavaScript**. Also supports batch URL fetching. Significantly heavier (requires a browser binary), but solves the two biggest gaps in the official server: JavaScript and batch operations. The right choice when you need to fetch modern web apps, not just static pages.

**vs. Firecrawl MCP (5,800 stars):** The full-service option — scraping, crawling, search, JavaScript rendering, batch operations. Cloud API with a paid tier. Seven tools. Overkill for reading a docs page, but the right choice if you're building a serious web-data pipeline. See our [browser MCP comparison](/guides/best-browser-mcp-servers/) for where Firecrawl fits in the broader landscape.

**vs. [Playwright MCP Server](/reviews/playwright-mcp-server/) (28,000+ stars):** A full browser automation server, not just a fetcher — but if your problem is "the page needs JavaScript to render," Playwright MCP solves it comprehensively. Much heavier, much more capable. Different tool for a different problem, but they overlap when the issue is "Fetch returned an empty page."

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
The Fetch MCP server does exactly what a reference implementation should: one tool, clearly defined behavior, easy setup. The HTML-to-markdown pipeline is solid, robots.txt handling is thoughtful, and with ~140K weekly downloads it's battle-tested for basic use. But the lack of SSRF protection is a real security gap — not a theoretical one — and the README's warning doesn't mitigate it. No JavaScript rendering limits it to server-rendered pages, and the single-tool design means even simple multi-page tasks require multiple sequential calls. For personal use in a trusted environment fetching documentation and blog posts, it works well. For anything involving untrusted URLs or JavaScript-heavy pages, look at zcaceres/fetch-mcp (better security, more output formats) or fetcher-mcp (JavaScript rendering via Playwright). The official server is a reasonable starting point, but "reference implementation" is doing a lot of work in that description.
{{< /verdict >}}
