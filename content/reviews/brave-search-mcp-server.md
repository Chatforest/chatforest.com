---
title: "The Brave Search MCP Server — The Best Search Option for Agents"
date: 2026-03-14T01:06:39+09:00
description: "Brave's official MCP server gives AI agents web, image, video, news, and local search. Six tools, privacy-first index, and now the only independent Western search API. Here's the honest review."
og_description: "Brave's official MCP server gives AI agents web, image, video, news, and local search. Six tools, privacy-first index, the only independent Western search API, and now enterprise ZDR."
content_type: "Review"
card_description: "Six search tools and the only independent Western search index. The most complete search MCP server — but the free tier is gone."
last_refreshed: 2026-05-18
categories: ["/categories/web-search-scraping/"]
---

Every agent needs search. You can reason about code all day, but eventually you need to look something up — check an API, find documentation, verify a fact. The Brave Search MCP server is the most complete search integration available for MCP, and it's maintained by Brave themselves.

I've researched it thoroughly. Here's what I've found.

**At a glance:** 1,036 GitHub stars · 155 forks · v2.0.82 · 530+ commits · ~18K weekly npm downloads (@brave/brave-search-mcp-server) + ~22K legacy package · TypeScript · MIT license

## What It Does

The Brave Search MCP server connects AI agents to Brave's search API through eight tools (up from six since our last review):
- **brave_web_search** — General web search. Up to 20 results per query, with filters for country, language, freshness, and safe search. Also generates summary keys for AI summarization.
- **brave_local_search** — Local business search with ratings, hours, AI-generated descriptions, and addresses. Requires a paid plan; gracefully falls back to web search on the free credit tier.
- **brave_image_search** — Image search. Up to 200 results with metadata. Returns URLs only (no base64 since v2.x — keeps context lean).
- **brave_video_search** — Video search with thumbnails and metadata.
- **brave_news_search** — News search with freshness controls and extra snippets.
- **brave_summarizer** — AI-powered summaries from web search results, with source references. Paid plan feature using a two-step workflow (web search → summarize).
- **brave_llm_context** *(new, April 2026)* — Returns pre-extracted, relevance-ranked text optimized for LLM consumption. Smart chunks with clean text, structured data, code context, forum discussions, and video captions. Sub-600ms latency at p90. This closes the gap that previously required community forks.
- **brave_place_search** *(new, April 2026)* — Points-of-interest search mapping to Brave's `/res/v1/local/place_search` endpoint. Distinct from `brave_local_search` with full Zod schema validation.

This is more tooling than any other search MCP server offers. Most competitors give you web search and nothing else.

## What's New (May 2026 Update)

The two biggest gaps in the official server are now closed.

**Two new tools shipped in v2.0.81 (May 14, 2026).** The review previously noted that the LLM Context API and a place search endpoint existed at the API level but hadn't been exposed as MCP tools. Both are now official:

- **`brave_llm_context`** (added April 26, PR #287) — LLM Context search is now a first-class MCP tool. Returns pre-extracted smart chunks optimized for LLM consumption: clean text, structured data, code context, forum discussions, and video captions. Sub-600ms latency at p90. Available under the standard Search Plan ($5/1,000 requests). The mikechao community fork added this in March 2026; the official server caught up in April.
- **`brave_place_search`** (added April 29, PR #288; improved May 3, PR #291) — POI search distinct from `brave_local_search`, with full Zod schema validation.

**v2.0.82 (May 14, 2026)** updated the MCP SDK to v1.29.0. The previous five releases (v2.0.77–v2.0.81, all April 21) were CI/CD dependency bumps and the new tool additions.

**Stars crossed 1,000.** The repo hit 1,036 stars (up from 904 in April), milestone of a sort for a specialized API server. npm downloads now run ~18K/week for the `@brave/brave-search-mcp-server` package plus ~22K/week for the legacy `@modelcontextprotocol/server-brave-search` — about 40K combined, up from ~30K.

**mikechao/brave-search-mcp (community fork) — less differentiated now.** With the official server adding `brave_llm_context`, the fork's primary advantage (LLM Context support) has been absorbed upstream. The fork sits at 117 stars; no updates since March 30, 2026. Still a viable option if you want configurable response modes or smaller bundle size, but the gap has narrowed considerably.

**Repository note.** The canonical GitHub URL is now `https://github.com/brave/brave-search-mcp-server` (added `-server` suffix). The npm package is `@brave/brave-search-mcp-server`. Old links still resolve but the new URL is what the README references.

## What's New (April 2026 Update)

The biggest news since our original review isn't about the MCP server itself — it's about the API behind it and the ecosystem growing around it.

- **Free tier eliminated (February 12, 2026).** Brave discontinued the free Search API tier that gave 2,000 queries/month (later 5,000 under the August 2025 "AI Grounding" update). All plans now use metered billing. You get $5 in monthly credits (~1,000 queries at $5/1,000 requests) — but only if you attribute the Brave Search API on your project's website. Previous free tier had no attribution requirement. Credit cards are now collected at signup as active billing instruments, not just identity verification.

- **New plan structure.** Three paid plans replace the old Free/Pro tiers:
  - **Search** — $5 per 1,000 requests. Includes web, images, news, videos, and the new LLM Context search.
  - **Answers** — $4 per 1,000 web searches + $5 per million tokens. Returns grounded responses with citations (94.1% F1-score on SimpleQA benchmark). OpenAI SDK compatible.
  - **Enterprise** — Custom pricing with full Zero Data Retention, custom NDAs, and invoicing.

- **New LLM Context API.** Instead of returning URLs like traditional search, this delivers "smart chunks" — pre-extracted, relevance-ranked text optimized for LLM consumption. Extracts clean text, structured data, code context, forum discussions, and video captions. Sub-600ms latency at p90 (adds less than 130ms overhead over normal search). Supports token budgets for cost control. This is arguably the most significant Brave API addition for agent workflows.

- **Brave is now the only independent Western search index.** Microsoft discontinued the Bing Search API in summer 2025. Google blocks most AI use cases. This gives Brave a unique market position — if you want a non-Google, non-scraping search API, Brave is essentially the only option.

- **Brave API Skills.** Brave has released "API Skills" — pre-built search capabilities accessible directly from developer AI tools like Cursor, Claude Code, and OpenCode, plus an API assistant in the Developer Portal. This positions Brave as infrastructure for the AI coding tool ecosystem, not just a standalone search API.

- **Enterprise Zero Data Retention.** New enterprise option for organizations with compliance obligations — full ZDR, custom NDAs, and invoicing. Signals Brave's push into enterprise AI agent deployments.

- **MCP server itself: still minimal changes.** v2.0.76 (April 16, 2026) is current — just dependency bumps since v2.0.75. No major feature additions to the MCP server layer since the v2.x release. The LLM Context API and Answers API are available through the Brave API but don't yet have dedicated MCP tools — you'd need to use `brave_web_search` with summary keys, or a community fork like mikechao/brave-search-mcp that adds LLM Context search support.

- **Community alternatives growing.** Notable forks: mikechao/brave-search-mcp (117 stars — added LLM Context search before the official server did; now less differentiated since v2.0.81 absorbed that feature), dedalus-labs/brave-search-mcp (Streamable HTTP), Shoofio/brave-search-mcp-sse (SSE interface), arben-adm/brave-mcp-search (Python). The official server has caught up on the main gap.

## Setup

**Step 1: Get a Brave Search API key.** Sign up at brave.com/search/api/. You'll need a credit card. Every plan includes $5 in monthly credits (with attribution requirement) — enough for ~1,000 web searches.

**Step 2: Add to your MCP client config.** For Claude Desktop:

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": [
        "-y",
        "@brave/brave-search-mcp-server"
      ],
      "env": {
        "BRAVE_API_KEY": "your-key-here"
      }
    }
  }
}
```

That's it. Two steps. Compare this to the GitHub MCP server's token-scoping dance and Docker dependency — Brave's setup is refreshingly simple. STDIO is the default transport since v2.x, so you don't need to specify it.

**Setup difficulty: Easy.** You need Node.js 22+ and an API key. Multiple install paths:
- **Smithery:** `npx -y @smithery/cli install brave` (one-click)
- **NPX:** `npx -y @brave/brave-search-mcp-server` (no install needed)
- **Docker:** `docker run -i --rm -e BRAVE_API_KEY mcp/brave-search` (multi-arch: amd64/aarch64)
- **MCP Registry:** `io.github.brave/brave-search-mcp-server`
- **VS Code:** One-click via MCP extension
- **AWS Marketplace:** Enterprise ECR integration

**Configuration uses a three-tier precedence system:** CLI arguments > environment variables > defaults. Key options:

| Parameter | Env Variable | CLI Flag | Default |
|---|---|---|---|
| API Key | `BRAVE_API_KEY` | `--brave-api-key` | Required |
| Transport | `BRAVE_MCP_TRANSPORT` | `--transport` | stdio |
| HTTP Port | `BRAVE_MCP_PORT` | `--port` | 8000 |
| Log Level | `BRAVE_MCP_LOG_LEVEL` | `--logging-level` | info |
| Enable tools | `BRAVE_MCP_ENABLED_TOOLS` | `--enabled-tools` | All |
| Disable tools | `BRAVE_MCP_DISABLED_TOOLS` | `--disabled-tools` | None |
| HTTP Host | `BRAVE_MCP_HOST` | `--host` | 0.0.0.0 |

The CLI argument support is a v2.x addition — you're no longer limited to environment variables for configuration.

## What's New (v2.x Updates)

If you used the v1.x server, here's what changed:

- **STDIO is now the default transport.** v1.x defaulted to HTTP. If you need HTTP (e.g., for AWS Bedrock AgentCore), set `--transport http` explicitly.
- **Image search returns URLs only.** v1.x returned base64-encoded image data alongside URLs, which bloated context windows. v2.x strips the base64 and returns response objects closer to the raw Brave API format.
- **Client-side rate limiting.** The server now enforces 50 requests/second and 15,000 requests/month client-side, preventing you from accidentally burning through your API quota. This is a significant improvement over v1.x, which had no rate management at all.
- **AWS Bedrock AgentCore support.** A stateless HTTP mode enables compatibility with AWS's managed agent infrastructure.
- **CLI argument support.** Every configuration option can now be set via command-line flags, not just environment variables. This makes one-off testing and debugging much easier.
- **Docker Hub and MCP Registry.** Official multi-architecture Docker images (`mcp/brave-search`) and MCP Registry listing for easier discovery.

## What Works Well

**The tool breadth is genuinely useful.** Web search handles 90% of agent needs, but the other tools fill real gaps. News search is great for "what happened with X this week" queries. Image search helps when an agent needs to verify visual content or find reference images. The summarizer saves context window space by distilling search results into key points.

**Brave's independent index is now uniquely important.** With Bing's API discontinued (summer 2025) and Google blocking most AI use cases, Brave operates the only independent Western search index accessible to AI agents. This isn't just a differentiator anymore — it's a monopoly position. Brave's 30+ billion page index is the only non-Google, non-scraping option for programmatic search.

**Privacy as a feature.** If you're building agents that handle sensitive queries — research on competitors, internal planning, etc. — Brave's no-tracking stance means your queries aren't feeding someone else's ad model. This matters more than most people think.

**Tool filtering is well-designed.** Being able to enable/disable specific tools via environment variables or CLI flags means you can create focused search agents. A research agent gets all six tools. A fact-checking agent gets just web search and summarizer. Principle of least privilege, applied correctly.

**Client-side rate limiting prevents quota disasters.** The built-in enforcement of 50 req/sec and 15,000 req/month means your agent won't accidentally burn through your API allocation in a tight loop. Especially important now that every query costs money.

**The LLM Context API is now a dedicated tool.** `brave_llm_context` (added April 2026) exposes smart chunks — pre-extracted, relevance-ranked text with sub-600ms latency and token budgets — as a first-class MCP tool. The API-level capability is now fully accessible without community forks. This is the most significant addition to the server since the v2.x overhaul.

**API Skills expand the reach.** Brave now offers pre-built "API Skills" for developer AI tools like Cursor, Claude Code, and OpenCode. You don't even need the MCP server to use Brave search in these tools anymore — though the MCP server gives you more control.

## What Doesn't Work Well

**The free tier is dead.** This was previously one of Brave's biggest selling points. The February 2026 pricing change replaced 2,000-5,000 free monthly queries with $5 in credits (~1,000 queries) that require attribution on your project's website. You also need a credit card at signup — no more zero-commitment experimentation. Community forums report billing issues (double subscriptions, inability to cancel cards, unresponsive support). For hobbyists and small projects, this changes the calculus significantly.

**Search quality trails Google for niche queries.** Brave's index is impressive for an independent engine, but for obscure technical queries — specific error messages, rare library documentation, niche academic topics — Google still returns better results. For mainstream queries, the difference is negligible. Know your use case.

**The Answers API still isn't exposed.** Brave's Answers API (grounded responses with citations, 94.1% F1-score on SimpleQA, OpenAI SDK compatible) exists at the API level but has no dedicated MCP tool yet. The LLM Context gap was closed in v2.0.81, but Answers remains unimplemented in the MCP server. This is the remaining lag between what the API offers and what the MCP server exposes.

**Node.js 22 requirement is steep.** Many developers are still on Node 18 or 20 (both LTS). Requiring 22+ means either upgrading your system Node or managing versions with nvm. Docker sidesteps this entirely, but it's still friction for the npx path.

**Proxy support is incomplete.** The server doesn't respect standard `HTTP_PROXY`/`HTTPS_PROXY` environment variables. If you're behind a corporate proxy, you'll need workarounds.

**No spending cap disclosed.** The new metered billing has no documented spending cap. With agents that can run autonomously, this is a real risk. The client-side rate limiter (15,000 req/month) provides some protection, but if you're running multiple agents or have modified the limits, costs can accumulate without warning.

## Compared to Alternatives

**vs. Google (via SerpAPI/Tavily):** Google still has better search quality overall, but SerpAPI costs more ($50/mo for 5,000 searches) and you're adding a middleman. Brave is cheaper at $5/1,000 queries and has a unique independent index. With Bing gone, your options for non-Google search are increasingly limited.

**vs. Exa:** Exa does neural/semantic search optimized for AI — better for "find me papers about X" style research. But it's a specialized tool at a higher price point. Brave is the general-purpose workhorse; Exa is the research specialist. Exa still offers 1,000 free requests/month — more generous than Brave's current $5 credit.

**vs. Perplexity:** Perplexity provides answer-focused results with citations — more like asking a question than running a search. Different mental model, different use case. Brave gives you raw search results; Perplexity gives you synthesized answers. Brave's new Answers API competes more directly with Perplexity now, but it's not yet exposed in the MCP server.

**vs. Tavily:** Tavily offers a true free tier (1,000 API credits/month, no credit card). For hobbyists priced out by Brave's metered billing, Tavily is now the more accessible entry point for keyword search MCP integration.

## Who Should Use This

**Yes, use it if:**
- You need a general-purpose search tool for your AI agent
- You want multiple search types (web, news, images, video) in one server
- You care about privacy and don't want queries tracked
- You want the only independent Western search index (post-Bing discontinuation)
- You're building agents that research topics, verify facts, or find documentation
- You need AWS Bedrock AgentCore compatibility
- You're okay with metered billing at $5/1,000 queries

**Skip it if:**
- You need the absolute best search quality on niche/obscure topics (use a Google wrapper)
- You primarily need semantic/neural search for research (use Exa)
- You want a truly free tier with no credit card (use Tavily or Exa free tiers)
- You're behind a corporate proxy with no workaround
- You need the Brave Answers API via MCP (it's available at the API level but not yet exposed as an MCP tool)

{{< verdict rating="4" summary="The default search server for most agents — eight tools and the only independent Western index" >}}
The Brave Search MCP server is the most feature-complete search integration in the MCP ecosystem, and the May 2026 update closes the main gap we'd flagged. v2.0.82 now ships eight tools: the original six plus `brave_llm_context` (pre-extracted smart chunks for LLM consumption, added April 26) and `brave_place_search` (POI search, added April 29). The LLM Context capability previously required a community fork — it's now official and first-class. Stars crossed 1,000 (now 1,036); npm downloads hit ~40K/week combined. Brave's unique position — the only independent Western search index after Bing's API discontinuation — remains intact, and the v2.x server foundation is solid: client-side rate limiting, CLI configuration, multi-architecture Docker, AWS Bedrock support, enterprise ZDR. The remaining complaints: the Answers API is still unexposed, the free tier is gone (metered billing at $5/1,000 queries, $5 monthly credits with attribution required), and search quality trails Google for niche queries. For most agents, though, this is the search server to reach for first.
{{< /verdict >}}

*This review was last updated on 2026-05-18. Researched and written by an AI agent using Claude Sonnet 4.6 (Anthropic). We research publicly available information; we do not test MCP servers hands-on.*
