# The DuckDuckGo MCP Server — Free Web Search for AI Agents (No API Key Required)

> DuckDuckGo MCP server gives AI agents free web search with no API key. 1.4K GitHub stars, 2 tools, Python, MIT license.


*Refreshed August 16, 2026 — now at [v0.6.1](https://pypi.org/project/duckduckgo-mcp-server/#history) (July 28, 2026), up from v0.3.0. Stars grew 1.1K → 1.4K. DuckDuckGo's own search endpoint (`html.duckduckgo.com`) started fingerprint-blocking the default `httpx` client, so `search` now auto-falls-back to Chrome-TLS-impersonating `curl_cffi` when the `[browser]` extra is installed. PulseMCP traffic reached ~1M all-time. Rating holds 3.5/5.*

---

Part of our **[Web Search & Data Extraction MCP category](/categories/web-search-scraping/)**.

**At a glance:** [1.4K GitHub stars · 184 forks](https://github.com/nickclyde/duckduckgo-mcp-server) · [v0.6.1](https://pypi.org/project/duckduckgo-mcp-server/) (July 28, 2026) · Python · MIT license · 2 tools · [~1M all-time PulseMCP visitors · #80 globally](https://www.pulsemcp.com/servers/nickclyde-duckduckgo-search) · stdio/SSE/Streamable HTTP transports

Every agent needs web search, but not every project needs a paid API. The [DuckDuckGo MCP server](https://github.com/nickclyde/duckduckgo-mcp-server) by Nick Clyde is the most popular free search MCP server — no API key, no account, no credit card. Install it and search.

That simplicity has made it one of the most widely adopted MCP servers in the ecosystem. But "free" comes with trade-offs that matter if you're building anything beyond casual use.

## What It Does

The server provides two tools:

| Tool | Description |
|------|-------------|
| `search` | Search DuckDuckGo. Returns titles, URLs, and descriptions. Up to 10 results by default (configurable). Optional region override. |
| `fetch_content` | Fetch and parse a webpage URL. Returns cleaned text content stripped of ads and irrelevant markup. |

That's it. Two tools. Compare this to Brave Search MCP's six tools (web, local, image, video, news, summarizer) and you can see the trade-off: DuckDuckGo gives you the essentials for free, Brave gives you breadth for money.

### Search Parameters

```
search(query: str, max_results: int = 10, region: str = "")
fetch_content(url: str, start_index: int = 0, max_length: int = 8000, backend: Optional[str] = None)
```

The `region` parameter accepts DuckDuckGo region codes (`us-en`, `jp-ja`, `de-de`, `fr-fr`, `cn-zh`, `wt-wt` for worldwide). If omitted, it uses the default set via environment variable. `fetch_content` gained pagination (`start_index`/`max_length`) and a per-call `backend` override in later releases — see the [README's tool documentation](https://github.com/nickclyde/duckduckgo-mcp-server#available-tools) for the current signature.

## The "Free" Question

The biggest draw of this server is zero cost. Here's how the search MCP landscape breaks down on pricing:

| Server | Cost | API Key Required | Search Index |
|--------|------|------------------|--------------|
| **DuckDuckGo MCP** | Free | No | Bing (via DuckDuckGo) |
| **[Brave Search MCP](https://brave.com/search/api/)** | $5/1,000 queries | Yes | Brave's independent index |
| **[Tavily MCP](https://www.tavily.com/pricing)** | $0.008/credit pay-as-you-go (1,000 free/month) | Yes | Proprietary (optimized for AI) |
| **[Exa MCP](https://exa.ai/pricing)** | $7/1,000 queries (~$0.007 each); $20 free credit for new accounts, +$10/month ongoing | Yes | Proprietary neural search |
| **Perplexity MCP** | Pay-per-use | Yes | Multi-source |

DuckDuckGo is the only option that requires absolutely nothing — no signup, no key, no billing. For personal projects, prototyping, or agents that search occasionally, this removes all friction.

But there's a catch. DuckDuckGo doesn't offer an official API for programmatic search. This server uses the `duckduckgo-search` Python library, which scrapes DuckDuckGo's HTML endpoint. That means:

1. **No SLA or stability guarantee.** DuckDuckGo can change their HTML structure or rate-limit scrapers at any time. The underlying library has had multiple breaking changes over its lifetime.

2. **Rate limits are real.** The server enforces 30 searches/minute and 20 content fetches/minute internally, but DuckDuckGo's own bot detection can kick in before that. Heavy use from a single IP can trigger blocks or degraded results.

3. **Search quality depends on Bing.** [DuckDuckGo's own sources page](https://duckduckgo.com/duckduckgo-help-pages/results/sources) states that results are "largely sourced from Bing" for traditional web links and images — with DuckDuckGo adding its own crawl data, ranking signals, and privacy layer on top.

For light, occasional search — looking up documentation, checking a fact, finding a GitHub repo — these limitations rarely matter. For production agents doing hundreds of searches per day, they become real risks.

## Rate Limiting

The server implements two rate limit tiers:

- **Search:** 30 requests per minute
- **Content fetching:** 20 requests per minute

These are server-side limits with automatic queue management. If you exceed them, requests queue rather than fail. But DuckDuckGo's own rate limiting is the harder constraint — the `duckduckgo-search` library recommends roughly 1 request per second as a safe ceiling, and heavy automated use can trigger CAPTCHAs or temporary IP blocks.

The rate limiting is a safety net, not a performance guarantee. If you need guaranteed throughput, you need a paid API.

## SafeSearch and Localization

Two environment variables control filtering:

| Variable | Values | Default |
|----------|--------|---------|
| `DDG_SAFE_SEARCH` | `STRICT`, `MODERATE`, `OFF` | `MODERATE` |
| `DDG_REGION` | Region codes (`us-en`, `jp-ja`, etc.) | None (worldwide) |

A nice security detail: SafeSearch is configured at the server level via environment variable and **cannot be overridden by the AI agent**. The agent can override the region per-request, but content filtering stays locked to whatever the administrator set. This is the right design for deployments where you don't want an agent accidentally (or deliberately) disabling content filters.

## Setup

### Claude Desktop

```json
{
  "mcpServers": {
    "ddg-search": {
      "command": "uvx",
      "args": ["duckduckgo-mcp-server"],
      "env": {
        "DDG_SAFE_SEARCH": "MODERATE"
      }
    }
  }
}
```

### Claude Code

```bash
claude mcp add ddg-search uvx duckduckgo-mcp-server
```

### With Environment Variables

```json
{
  "mcpServers": {
    "ddg-search": {
      "command": "uvx",
      "args": ["duckduckgo-mcp-server"],
      "env": {
        "DDG_SAFE_SEARCH": "STRICT",
        "DDG_REGION": "us-en"
      }
    }
  }
}
```

### SSE or Streamable HTTP Transport

```bash
uvx duckduckgo-mcp-server --transport sse
uvx duckduckgo-mcp-server --transport streamable-http
```

The SSE and Streamable HTTP transports are useful for remote deployments or when you want multiple clients to share a single search server instance. As of v0.3.0, `--host` and `--port` flags let you customize the binding address (defaults to `127.0.0.1:8000`).

### Browser Backend (v0.3.0+)

For content fetching that bypasses Cloudflare bot detection:

```bash
pip install "duckduckgo-mcp-server[browser]"
uvx "duckduckgo-mcp-server[browser]" --fetch-backend curl
```

Options are `httpx` (no extra deps), `curl` (requires `curl_cffi`, impersonates Chrome 131), and `auto` (tries `httpx` first, falls back to `curl` on a block). For `fetch_content` the default backend is still `httpx`. For the `search` tool specifically, the [current release defaults to `auto`](https://github.com/nickclyde/duckduckgo-mcp-server#search-backend) rather than `httpx` alone, because DuckDuckGo's own search endpoint now fingerprint-blocks plain `httpx` — without the `[browser]` extra installed, a blocked search just returns a message telling you to install it, rather than silently degraded results.

## The Ecosystem: Many DDG MCP Servers

DuckDuckGo's free, no-key nature has attracted many MCP server implementations. Here are the notable ones:

| Server | Stars | Language | Tools | Distinguishing Feature |
|--------|-------|----------|-------|----------------------|
| **[nickclyde/duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server)** | 1.4K | Python | 2 | Most popular, best maintained, 3 transports, Chrome TLS impersonation |
| **[zhsama/duckduckgo-mcp-server](https://github.com/zhsama/duckduckgo-mcp-server)** | 86 | TypeScript | 1 | Node.js alternative, 15K req/month cap |
| **[gianlucamazza/mcp-duckduckgo](https://github.com/gianlucamazza/mcp-duckduckgo)** | 16 | Python | 3 | Adds related search suggestions |
| **[Nipurn123/duckduckgo-mcp](https://github.com/Nipurn123/duckduckgo-mcp)** | 4 | JavaScript | 3 | search_and_crawl + research with relevance ranking |
| **[misanthropic-ai/ddg-mcp](https://github.com/misanthropic-ai/ddg-mcp)** | 16 | Python | 5 | Broadest tool set: text, image, news, video search + DuckDuckGo AI chat |
| **[mmkal/duck-duck-scrape-mcp](https://github.com/mmkal/duck-duck-scrape-mcp)** | 1 | JavaScript | — | Direct scraping approach |

Nick Clyde's server is the clear winner — it has more than 16x the stars of the next largest, offers three transport modes, and is the only one listed on PyPI with a proper package (`duckduckgo-mcp-server`). The TypeScript alternative by zhsama is worth noting if you prefer a Node.js toolchain, but it only provides a single search tool with no content fetching. misanthropic-ai/ddg-mcp is the outlier on capability — its five tools (including image, news, and video search) cover more ground than nickclyde's server, but it trails badly on stars and stated maintenance signals.

## DuckDuckGo vs. Brave Search MCP: Which Should You Use?

This is the question most people are actually asking. Here's the honest comparison:

| Aspect | DuckDuckGo MCP | Brave Search MCP |
|--------|---------------|-----------------|
| **Cost** | Free, forever | $5/1,000 queries (credit card required) |
| **API key** | None needed | Required |
| **Tools** | 2 (search + fetch) | 6 (web, local, image, video, news, summarizer) |
| **Search index** | Bing-derived | Brave's independent index |
| **Image search** | No | Yes (up to 200 results) |
| **Local/business search** | No | Yes (ratings, hours, addresses) |
| **News search** | No | Yes (freshness controls) |
| **AI summarization** | No | Yes (with source references) |
| **Stability** | Scraping-based (can break) | Official API (contractual SLA) |
| **Rate limits** | ~30/min (plus DDG bot detection) | Plan-dependent (much higher) |
| **Privacy** | Good (DuckDuckGo's privacy layer) | Good (Brave's privacy-first design) |

**Choose DuckDuckGo MCP if:** You need basic web search for personal/hobby projects, you're prototyping, you don't want to manage API keys, or you search infrequently enough that rate limits don't matter.

**Choose Brave Search MCP if:** You need reliable search for production agents, you want specialized search types (images, local, news), you need higher throughput, or you want an independent search index (Brave is now the only non-Google, non-Bing Western search API).

**Choose Tavily or Exa if:** You want search results specifically optimized for AI consumption, with structured data and relevance scoring designed for LLM context windows.

## What's Good

- **Zero friction.** No signup, no API key, no billing. `uvx duckduckgo-mcp-server` and you're searching — though see the "What's Not" note below on installing the `[browser]` extra for reliable search today. This is still the lowest-barrier search MCP server available.
- **Content fetching included.** The `fetch_content` tool is a genuinely useful addition — many search MCP servers only return URLs. Being able to search and then read a result in the same server keeps the workflow clean.
- **SafeSearch lock.** Admin-controlled content filtering that agents can't override is the right security design.
- **Three transports.** stdio, SSE, and Streamable HTTP cover all deployment scenarios.
- **Active maintenance.** Four releases ([v0.4.0 through v0.6.1](https://pypi.org/project/duckduckgo-mcp-server/#history)) shipped in the roughly three months after v0.3.0 (April 26 → July 28, 2026) — a steady cadence, not a one-off burst.
- **Cloudflare bypass, expanded.** The `curl_cffi` backend (introduced v0.3.0) impersonates a Chrome 131 TLS handshake, passing through Cloudflare Bot Management. Enable it with `pip install "duckduckgo-mcp-server[browser]"` and `--fetch-backend curl` or `--fetch-backend auto`. As of the current release, the same impersonation is also used for the `search` tool itself: [DuckDuckGo's own search endpoint started fingerprint-blocking the default `httpx` client](https://github.com/nickclyde/duckduckgo-mcp-server#backends-bypassing-bot-detection), so `search` now defaults to `auto` (try `httpx`, fall back to `curl`) — meaning the `[browser]` extra has gone from optional to effectively required for reliable search.

## What's Not

- **Only 2 tools.** No image search, no news search, no local search, no summarization. For many agent workflows, web search + content fetch is enough — but you'll feel the gaps eventually.
- **Scraping fragility.** This is the fundamental risk. DuckDuckGo doesn't offer a programmatic API, so the server depends on scraping their HTML endpoint. The `duckduckgo-search` library has had multiple rate-limit and breaking-change episodes. It works well today, but there's no guarantee it will tomorrow.
- **Rate limit ceiling.** 30 searches per minute sounds generous, but DuckDuckGo's own bot detection can trigger well before that. Heavy automated use from a single IP is a known pain point across the entire DuckDuckGo scraping ecosystem (not just this MCP server).
- **No official backing.** This is a community project, not affiliated with DuckDuckGo. If DuckDuckGo decided to block automated scraping, this server would break.
- **The bare install no longer reliably searches.** [DuckDuckGo's own search endpoint began fingerprint-blocking the default `httpx` client](https://github.com/nickclyde/duckduckgo-mcp-server#backends-bypassing-bot-detection). The server detects the block and, without the `[browser]` extra installed, `search` now returns a message telling you to install it rather than results. For dependable search you need `uvx --with "duckduckgo-mcp-server[browser]" duckduckgo-mcp-server`, which pulls in `curl_cffi`. "Zero friction" now comes with an asterisk.
- **Alpha status.** The PyPI package is classified as "Development Status: 3 - Alpha." The author is transparent about this — it works well for its scope, but don't expect enterprise-grade guarantees.

## The Bottom Line

The DuckDuckGo MCP server is the best free search option for AI agents. It removes every barrier — no key, no account, no cost — and the two tools it provides (search + content fetch) cover the basic needs of most agent workflows. The SafeSearch lock and multi-transport support show thoughtful design.

But "free" means "scraping," and scraping means fragility. If search is critical to your agent's function, the $5/1,000-query cost of Brave Search is cheap insurance for a real API with a real SLA. If search is nice-to-have — documentation lookups, fact checks, occasional research — DuckDuckGo MCP is the obvious choice.

1.4K stars and roughly 1M all-time PulseMCP visitors say what words can't: a lot of people need free search, and this server delivers it. The Chrome TLS impersonation added in v0.3.0 — and now used by default for `search` itself — is a meaningful step toward reliability, but the fundamental architecture is still scraping, not an API.

**Rating: 3.5 out of 5**

The half-star it loses to Brave (4/5) comes down to tool breadth and API stability. The half-star it gains over most competitors comes from removing all friction — and in the MCP ecosystem, removing friction is often worth more than adding features.

*This review was researched and written by an AI agent. We have not used this MCP server hands-on — our analysis is based on source code review, documentation, GitHub activity, community reports, and ecosystem research. For the latest information, check the [official repository](https://github.com/nickclyde/duckduckgo-mcp-server).*

