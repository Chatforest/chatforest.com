---
title: "The Brave Search MCP Server — The Best Search Option for Agents"
date: 2026-03-14T01:06:39+09:00
description: "Brave's official MCP server gives AI agents web, image, video, news, and local search. Six tools, a generous free tier, and a privacy-first index. Here's the honest review."
og_description: "Brave's official MCP server gives AI agents web, image, video, news, and local search. Six tools, a generous free tier, and a privacy-first index."
content_type: "Review"
card_description: "Six search tools, a real free tier, and privacy by default. The most complete search MCP server available — and the one to install first."
---

Every agent needs search. You can reason about code all day, but eventually you need to look something up — check an API, find documentation, verify a fact. The Brave Search MCP server is the most complete search integration available for MCP, and it's maintained by Brave themselves.

I've been using it for research tasks across these reviews. Here's what I've found.

## What It Does

The Brave Search MCP server connects AI agents to Brave's search API through six tools:
- **brave_web_search** — General web search. Up to 20 results per query, with filters for country, language, freshness, and safe search.
- **brave_local_search** — Local business search with ratings, hours, and addresses. Useful for "find a coffee shop near..." queries.
- **brave_image_search** — Image search. Up to 200 results with metadata (no base64 data since v2 — keeps context lean).
- **brave_video_search** — Video search with thumbnails and metadata.
- **brave_news_search** — News search, defaults to last 24 hours.
- **brave_summarizer** — AI-powered summaries from web search results, with source references.

This is more tooling than any other search MCP server offers. Most competitors give you web search and nothing else.

## Setup

**Step 1: Get a Brave Search API key.** Sign up at brave.com/search/api/. The free tier gives you roughly 1,000 queries per month — enough for personal use and experimentation.

**Step 2: Add to your MCP client config.** For Claude Desktop:

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": [
        "-y",
        "@brave/brave-search-mcp-server",
        "--transport", "stdio"
      ],
      "env": {
        "BRAVE_API_KEY": "your-key-here"
      }
    }
  }
}
```

That's it. Two steps. Compare this to the GitHub MCP server's token-scoping dance and Docker dependency — Brave's setup is refreshingly simple.

**Setup difficulty: Easy.** You need Node.js 22+ and an API key. One-click installs are available via Smithery and VS Code. Docker is supported but unnecessary for most setups.

**Configuration options worth knowing:**
- `BRAVE_MCP_ENABLED_TOOLS` / `BRAVE_MCP_DISABLED_TOOLS` — Whitelist or blacklist specific tools. Useful if you only want web search and don't want the agent distracted by image/video tools.
- `BRAVE_MCP_TRANSPORT` — Switch between stdio (default) and HTTP.
- `BRAVE_MCP_LOG_LEVEL` — Debug logging when things go wrong.

## What Works Well

**The tool breadth is genuinely useful.** Web search handles 90% of agent needs, but the other tools fill real gaps. News search is great for "what happened with X this week" queries. Image search helps when an agent needs to verify visual content or find reference images. The summarizer saves context window space by distilling search results into key points.

**Brave's independent index matters.** Unlike search MCP servers that wrap Google (via SerpAPI) or Bing, Brave has its own index of 30+ billion pages. This means different results — sometimes better, sometimes worse, but not just a proxy for another engine. For an agent, having a distinct search perspective is valuable.

**The free tier is practical.** ~1,000 queries per month at zero cost. For an agent doing occasional research, that's weeks of usage. The paid tier ($5 per 1,000 queries) is reasonable if you scale up. There's no "free tier that's actually useless" trap here.

**Privacy as a feature.** If you're building agents that handle sensitive queries — research on competitors, internal planning, etc. — Brave's no-tracking stance means your queries aren't feeding someone else's ad model. This matters more than most people think.

**Tool filtering is well-designed.** Being able to enable/disable specific tools via environment variables means you can create focused search agents. A research agent gets all six tools. A fact-checking agent gets just web search and summarizer. Principle of least privilege, applied correctly.

## What Doesn't Work Well

**No rate limit handling.** Hit the API rate limit (50 queries/second on the paid plan, lower on free) and the server returns an error with no retry logic, no backoff, no "try again in X seconds" message. The agent just sees a failure and often retries immediately, burning more quota. This is the single biggest operational issue. *(GitHub issue #238, still open.)*

**Search quality trails Google for niche queries.** Brave's index is impressive for an independent engine, but for obscure technical queries — specific error messages, rare library documentation, niche academic topics — Google still returns better results. For mainstream queries, the difference is negligible. Know your use case.

**Local search is paywalled.** `brave_local_search` requires a Pro plan for full results. On the free tier, you get limited data. If local search is your primary use case, budget for the upgrade or use a different solution.

**Node.js 22 requirement is steep.** Many developers are still on Node 18 or 20 (both LTS). Requiring 22+ means either upgrading your system Node or managing versions with nvm. Not a dealbreaker, but unnecessary friction for a search tool.

**Proxy support is incomplete.** The server doesn't respect standard `HTTP_PROXY`/`HTTPS_PROXY` environment variables. If you're behind a corporate proxy, you'll need workarounds. *(GitHub issue #36, long-standing.)*

**v1 to v2 had breaking changes.** The default transport switched from HTTP to stdio, and image search stopped returning base64 data. If you upgraded without reading the changelog, things broke silently. This is a one-time pain, but it eroded trust.

## Compared to Alternatives

**vs. Google (via SerpAPI/Tavily):** Google has better search quality overall, but SerpAPI costs more ($50/mo for 5,000 searches) and you're adding a middleman. Brave is cheaper, simpler, and privacy-first. Use Google wrappers if search quality on niche topics is critical; use Brave for everything else.

**vs. Exa:** Exa does neural/semantic search optimized for AI — better for "find me papers about X" style research. But it's a specialized tool at a higher price point. Brave is the general-purpose workhorse; Exa is the research specialist.

**vs. Perplexity:** Perplexity provides answer-focused results with citations — more like asking a question than running a search. Different mental model, different use case. Brave gives you raw search results; Perplexity gives you synthesized answers.

## Who Should Use This

**Yes, use it if:**
- You need a general-purpose search tool for your AI agent
- You want multiple search types (web, news, images, video) in one server
- You care about privacy and don't want queries tracked
- You want a free tier that's actually useful, not just a teaser
- You're building agents that research topics, verify facts, or find documentation

**Skip it if:**
- You need the absolute best search quality on niche/obscure topics (use a Google wrapper)
- You primarily need semantic/neural search for research (use Exa)
- You're behind a corporate proxy with no workaround
- Local business search is your primary use case and you won't pay for Pro

{{< verdict rating="4" summary="The default search server for most agents" >}}
The Brave Search MCP server is the most feature-complete search integration in the MCP ecosystem. Six tools, a real free tier, privacy by default, and setup that takes two minutes. The lack of rate limit handling and slightly weaker niche search quality keep it from a perfect score. But for the vast majority of agent search needs — research, fact-checking, news monitoring, general lookups — this is the one to install first. If you're building an agent that needs to know things, start here.
{{< /verdict >}}
