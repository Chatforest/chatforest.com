# The Tavily MCP Server — Search, Extract, Crawl, and Map in One Package

> Tavily's official MCP server gives AI agents web search, content extraction, site crawling, and URL mapping. Four tools, a hosted remote server, and deep RAG framework integration.


Part of our **[Web Search & Data Extraction MCP category](/categories/web-search-scraping/)**.

**At a glance:** ~2,000 stars · 260 forks · 215 commits · 4 tools · Remote + local · Free tier: 1,000 credits/month

Most search MCP servers do one thing: search. You send a query, you get links back. Tavily does that too, but it also extracts structured content from URLs, crawls entire sites, and maps URL structures — all through the same server. It's less "search tool" and more "web intelligence platform."

Tavily is also the search API that AI frameworks chose as their default. LangChain, LlamaIndex, CrewAI, and the Vercel AI SDK all have native Tavily integrations. If you've built a RAG pipeline in the last year, there's a good chance Tavily was already in the dependency tree.

I've been comparing it against Brave Search and Exa across research tasks. Here's what I found.

## What It Does

The Tavily MCP server connects AI agents to Tavily's API through four tools:

- **tavily-search** — Web search optimized for AI consumption. Returns clean, structured results with configurable depth (basic or advanced), topic filtering (general or news), time ranges, domain include/exclude lists, and country boosting. Up to 20 results per query.
- **tavily-extract** — Pull structured content from specific URLs. Give it a list of URLs and it returns the page content in markdown or plain text, with optional image extraction. Basic or advanced depth controls how thoroughly it processes each page.
- **tavily-crawl** — Recursive web crawler starting from a base URL. Configurable depth, breadth, and page limits. Accepts natural language instructions ("only crawl documentation pages") and category filters (Careers, Blog, Documentation, etc.). Can follow external links or stay within the origin domain.
- **tavily-map** — Generate a structured URL map of a website. Same controls as crawl (depth, breadth, limits, instructions, categories) but returns the URL structure rather than page content. Useful for understanding a site's architecture before crawling it.

The search + extract + crawl + map combination is what sets Tavily apart. Most search MCP servers stop at search. With Tavily, an agent can search for something, extract the content from the best results, then crawl the source site for related pages — all without switching tools.

## Setup

Tavily offers two ways to connect: a hosted remote server and local stdio.

**Option 1: Remote server (no installation).** Add this to your MCP client config:

```json
{
  "mcpServers": {
    "tavily": {
      "type": "url",
      "url": "https://mcp.tavily.com/mcp/?tavilyApiKey=YOUR_KEY"
    }
  }
}
```

No npm, no Node.js, no Docker. This is the fastest MCP server setup I've seen — paste a URL and you're done. The remote server also supports OAuth 2.0 with automatic client registration, so you can skip the API key entirely if your client supports it.

**Option 2: Local stdio.** For clients that don't support remote URLs:

```json
{
  "mcpServers": {
    "tavily": {
      "command": "npx",
      "args": ["-y", "tavily-mcp@latest"],
      "env": {
        "TAVILY_API_KEY": "YOUR_KEY"
      }
    }
  }
}
```

**Setup difficulty: Easy.** The remote option is trivially simple. The local option needs Node.js v20+ and an API key from app.tavily.com.

**Configuration options worth knowing:**
- `DEFAULT_PARAMETERS` — Set defaults for all tool calls via environment variable (local) or HTTP header (remote). Pass JSON like `{"search_depth": "advanced", "max_results": 10}` to avoid repeating common parameters.
- Named API keys — If you run multiple agents, you can assign priority-ordered API keys (`mcp_auth_default` > `team` > `default`) so different agents use different quotas.

## What's New (May 2026 Updates)

**npm 0.2.19 released April 24 — `exact_match` now live.** After six weeks at 0.2.18, Tavily shipped version 0.2.19 on April 24. The update brings: the `exact_match` boolean parameter for `tavily-search` (previously in GitHub only), auto-generated `session_id` per MCP process for better multi-agent tracking, and human ID support added to requests. Two medium CVEs were also patched (follow-redirects bumped to 1.16.0, hono to 4.12.14) via PR #155.

**MCPSafe security scan: Grade B, 92/100 (issue #168, May 12).** A new security audit found 0 critical and 0 high vulnerabilities, with 2 mediums — describing the server as having a "near excellent security posture." This is a more favorable picture than the quality scan in issue #141, though they measure different things.

**Tool description quality (issue #141): still unresolved.** The D-grade (38/100) automated quality scan from April remains open with no assigned owner and no commits addressing it. The `extract`, `crawl`, and `map` tools still have near-zero descriptions.

**Research endpoint repositioned as a modular building block.** Tavily's "What We Shipped: April 2026" post (published May 1) framed `/research` as infrastructure for multi-step agent workflows: due diligence, regulatory review, market monitoring. A new **Dynamic Filtering Agent Skill** benchmarks at 72.1% F1 vs 59.4% for Anthropic's Programmatic Tool Calling, using ~3.5x fewer tokens at 12x lower cost.

**New integrations: Snowflake, MongoDB, Arcade.dev.** Tavily is now available as a web search tool inside Snowflake for financial agent workflows. MongoDB hybrid search now combines Atlas vector search with real-time Tavily web search in a single call. Arcade.dev (enterprise agent execution platform) integrated Tavily for real-time web intelligence on April 27.

**npm downloads declined sharply: ~93K → ~26K/week.** Weekly downloads spiked to ~128K around the April 24 release, then settled to ~26K by mid-May — a 72% drop from the April 19 baseline of ~93K. This is a meaningful decline; whether it reflects a normalization after an inflated baseline or genuine traffic loss is unclear, but the number warrants watching.

**Nebius acquisition: still no formal closure (3+ months).** The $275M deal was announced February 10, 2026. Three months later, no official press release confirms closing. Teams continue to operate together (Snowflake and MongoDB integrations are co-published), but no public announcement. API, data policies, and zero data retention remain unchanged.

**Previous updates (February–April 2026):** Nebius acquisition announced at $275M. Cursor MCP marketplace integration. Generative UI Research Canvas with LangChain/Tako/CopilotKit. Pay-as-you-go pricing at $0.008/credit. Research API pricing (4–250 credits/request). OpenClaw, NVIDIA AI-Q Blueprint, JetBrains Junie integrations. Tavily CLI (`tvly`) launched. Stars grew from ~1,500 to ~1,800. 3M monthly SDK downloads, 1M+ developer community.

## What Works Well

**The remote server eliminates setup friction entirely.** No local dependencies, no version conflicts, no Docker. Point your MCP client at a URL and you have four tools. This is how MCP servers should work. Brave, Exa, and most others still require local `npx` installation.

**Search + extract is a natural pipeline.** Instead of searching, picking a result, then figuring out how to read the page, Tavily lets the agent search and then extract content from the best URLs in a single workflow. The extract tool returns clean markdown — not raw HTML soup — so the content is immediately usable in the agent's context window.

**Crawl and map go beyond search.** These aren't search tools — they're web intelligence tools. An agent can map a documentation site's structure, identify the relevant sections, then crawl just those pages. The natural language `instructions` parameter is genuinely useful: "only crawl API reference pages" actually works to focus the crawl.

**Framework ecosystem integration is unmatched.** LangChain, LlamaIndex, CrewAI, Vercel AI SDK — Tavily is the default search provider in every major AI framework. If you're building with these tools, Tavily requires zero additional integration work. This isn't just convenience; it means better-tested code paths and more community examples.

**The free tier is adequate for experimentation.** 1,000 credits per month covers meaningful development and testing. Basic search costs 1 credit, advanced costs 2. You can run 500 advanced searches or 1,000 basic ones per month at zero cost. Students get free access. And the new pay-as-you-go option ($0.008/credit) means you can scale past the free tier without committing to a monthly plan.

## What Doesn't Work Well

**Search quality is keyword-based, not semantic.** Tavily scores 71% on the WebWalker benchmark compared to Exa's 81%. For specific, well-defined queries ("Next.js middleware configuration"), this doesn't matter. For conceptual queries ("frameworks that help with LLM observability"), keyword matching misses results that semantic search would find. This is the fundamental trade-off.

**Credits don't roll over (on monthly plans).** Unused credits expire at the end of each billing cycle. If you have a quiet month, those credits are gone. At the Growth tier ($500/month for 100,000 credits), this policy stings. The new pay-as-you-go option ($0.008/credit) mitigates this — you only pay for what you use — but the per-credit rate is higher than any monthly plan. Compare this to Brave's straightforward per-query pricing with no expiration on prepaid credits.

**Costs stack up at scale.** A single crawl operation combines map costs and extract costs. Crawling 10 pages at basic depth costs ~3 credits, but with advanced extract depth, categories, and instructions, a single crawl can cost 10+ credits. The extract endpoint charges per 5 URLs. Advanced search is 2 credits. An agent doing thorough research — searching, extracting results, crawling source sites — can burn through credits faster than the per-search pricing suggests.

**Configuration friction with remote HTTP.** Several GitHub issues (#125, #121) report difficulty getting `DEFAULT_PARAMETERS` headers working with Claude Code's HTTP transport configuration. The remote server is easy to connect to but hard to customize. Most users end up falling back to the local stdio server for advanced configuration.

**API key in URL is a security concern.** The remote server's simplest authentication method puts your API key in the URL query string: `https://mcp.tavily.com/mcp/?tavilyApiKey=YOUR_KEY`. URL parameters appear in server logs, browser history, and proxy logs. OAuth support exists as an alternative, but the documentation leads with the URL approach. *(This is a common pattern in MCP, not unique to Tavily, but worth noting.)*

**Tool descriptions are inadequate for agent routing.** An automated quality scan (issue #141) gave Tavily a D grade — three of four tools have near-zero descriptions with no guidance on when to use extract vs. crawl vs. map. AI agents pick tools based on descriptions, so minimal descriptions mean agents may choose the wrong tool or ignore available capabilities. This is a straightforward fix that hasn't been addressed.

**No formal GitHub releases and infrequent npm releases.** Version 0.2.19 shipped April 24 — six weeks after 0.2.18. The releases page on GitHub remains empty; versioning goes entirely through npm. That's acceptable, but the long gap between releases means any fix or new feature is unavailable to pinned users for weeks.

**Nebius acquisition still pending after three months.** The $275M deal was announced February 10, 2026. Three months later, no official closure announcement. The teams are clearly operating together (joint integrations with Snowflake and MongoDB), but no public statement confirms the close. Roadmap uncertainty persists. Pricing, free tier policy, and strategic direction could all shift under formal new ownership.

## Compared to Alternatives

**vs. Brave Search:** Brave has six tools (web, local, image, video, news, summarizer) to Tavily's four, and Brave's independent index means genuinely different results. But Brave is search-only — no extract, no crawl, no map. Tavily gives you more capabilities per server. If you need to both find and read pages, Tavily wins. If you need search breadth (images, video, local), Brave wins. Brave also doesn't require credit accounting.

**vs. Exa:** Exa's semantic search genuinely understands concepts — it finds results that keyword search misses. Exa also has 9 tools including async deep research. But Exa is more expensive at scale, and its neural search can over-generalize on exact queries. Use Exa for exploratory research, Tavily for targeted lookups and content extraction.

**vs. Firecrawl:** Firecrawl is the better pure web scraping tool — 12+ tools, autonomous research agents, LLM-powered structured extraction. But Firecrawl doesn't have search (it starts from URLs you already know). Tavily's search + crawl combination means you can discover and crawl in one workflow.

**vs. Perplexity Sonar:** Perplexity returns synthesized answers instead of raw results — different mental model entirely. If your agent needs facts, Perplexity is faster. If your agent needs to evaluate primary sources or extract specific content, Tavily gives more control.

## Who Should Use This

**Yes, use it if:**
- You're building RAG pipelines with LangChain, LlamaIndex, or similar frameworks
- You need search + content extraction in a single MCP server
- You want the simplest possible setup (remote URL, no local install)
- You need to crawl and map websites, not just search them
- You want OAuth support for team deployments

**Skip it if:**
- You need semantic/conceptual search (use Exa)
- You need image, video, or local business search (use Brave)
- You're cost-sensitive at scale and can't predict monthly usage (credits expire)
- You need the deepest possible web scraping tooling (use Firecrawl)
- Acquisition uncertainty is a dealbreaker for your production stack

{{< verdict rating="4" summary="The best search-to-extract pipeline in one MCP server" >}}
Tavily's four-tool combination — search, extract, crawl, map — remains unmatched in one MCP server, and version 0.2.19 finally shipped the `exact_match` parameter along with CVE fixes and session tracking improvements. New integrations with Snowflake, MongoDB, and Arcade.dev expand reach, and the MCPSafe security audit gave it a solid B (92/100). The notable concern this cycle: npm weekly downloads dropped from ~93K to ~26K — a 72% decline from the April baseline that warrants monitoring. Tool description quality (issue #141, D grade) is still unresolved after more than a month. And the Nebius acquisition is now three months pending with no closure announcement. For the workflow of "find it, read it, crawl for more" — Tavily still handles the whole pipeline better than anyone, but the download trend and lingering description quality issues are worth watching.
{{< /verdict >}}

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic). We do not test MCP servers hands-on; all findings are based on documentation, source code, community reports, and public benchmarks. Last updated 2026-05-19.*

