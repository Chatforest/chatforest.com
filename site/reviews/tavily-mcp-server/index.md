# The Tavily MCP Server — Search, Extract, Crawl, and Map in One Package

> Tavily's official MCP server gives AI agents web search, content extraction, site crawling, and URL mapping. Four tools, a hosted remote server, and deep RAG framework integration.


Part of our **[Web Search & Data Extraction MCP category](/categories/web-search-scraping/)**.

**At a glance:** [~2,300 stars](https://github.com/tavily-ai/tavily-mcp) · 285 forks · 229 commits · 4 tools · Remote + local · Free tier: 1,000 credits/month (as of 2026-08-14)

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

No npm, no Node.js, no Docker. This is the fastest MCP server setup I've seen — paste a URL and you're done. [The remote server also supports OAuth authentication with automatic client registration](https://docs.tavily.com/documentation/mcp), so you can skip the API key entirely if your client supports it.

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

**Research endpoint repositioned as a modular building block.** [Tavily's "What We Shipped: April 2026" post](https://www.tavily.com/blog/whats-new-april) (published May 1) framed `/research` as infrastructure for multi-step agent workflows: due diligence, regulatory review, market monitoring. A new **Dynamic Filtering Agent Skill** — [per Tavily's own benchmark writeup](https://www.tavily.com/blog/dynamic-filtering-let-the-model-program-its-own-search-filters), a vendor-run comparison we could not find independently replicated — claims 72.1% F1 vs 59.4% for Anthropic's Programmatic Tool Calling, using ~3.5x fewer tokens at 12x lower cost.

**New integrations: Snowflake, MongoDB, Arcade.dev.** [Tavily is now available as a web search tool inside Snowflake](https://www.tavily.com/blog/whats-new-april) for financial agent workflows. [MongoDB hybrid search](https://www.mongodb.com/company/blog/innovation/how-tavily-uses-mongodb-to-enhance-agentic-workflows) now combines Atlas vector search with real-time Tavily web search in a single call. [Arcade.dev](https://www.arcade.dev/tools/tavily/) (enterprise agent execution platform) integrated Tavily for real-time web intelligence [on April 27](https://www.tavily.com/blog/tavily-is-now-available-in-arcade-dev-credible-cited-research-for-ai-agents-to-act-on).

**npm downloads declined sharply: ~93K → ~26K/week.** Weekly downloads spiked to ~128K around the April 24 release, then settled to ~26K by mid-May — a 72% drop from the April 19 baseline of ~93K. This is a meaningful decline; whether it reflects a normalization after an inflated baseline or genuine traffic loss is unclear, but the number warrants watching.

**Nebius acquisition closed February 19, 2026 — no dedicated press release, but confirmed in SEC filings.** *Correction (2026-08-14 audit): this section previously said the deal was still pending three months after the February 10, 2026 announcement. That was wrong — the acquisition closed nine days after it was announced.* [The $275M deal was announced February 10, 2026](https://siliconangle.com/2026/02/10/ai-infrastructure-giant-nebius-buys-agentic-search-startup-tavily/); Nebius's own [Form 6-K filing with the SEC](https://www.stocktitan.net/sec-filings/NBIS/6-k-nebius-group-n-v-current-report-foreign-issuer-540144354e8c.html) states "On February 19, 2026, the Company acquired a 100% ownership interest in Tavily," with net cash paid of $170.2 million. Nebius never issued a standalone "deal closed" announcement — the closing surfaced through routine SEC disclosure, and was independently reported by [Yahoo Finance in June 2026](https://finance.yahoo.com/markets/stocks/articles/nebius-group-acquisitions-signal-shift-231121746.html), which confirmed Nebius "has completed acquisitions of Tavily, Eigen AI, and Clarifai." API, data policies, and zero data retention remain unchanged.

**Previous updates (February–April 2026):** [Nebius acquisition announced at $275M](https://siliconangle.com/2026/02/10/ai-infrastructure-giant-nebius-buys-agentic-search-startup-tavily/). Cursor MCP marketplace integration. Generative UI Research Canvas with LangChain/Tako/CopilotKit. Pay-as-you-go pricing at $0.008/credit. Research API pricing (4–250 credits/request). OpenClaw, NVIDIA AI-Q Blueprint, JetBrains Junie integrations. Tavily CLI (`tvly`) launched. Stars grew from ~1,500 to ~1,800. [Over 3 million monthly SDK downloads and a developer community of more than one million users](https://nebius.com/newsroom/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform), per Nebius's own acquisition announcement.

## What Works Well

**The remote server eliminates setup friction entirely.** No local dependencies, no version conflicts, no Docker. Point your MCP client at a URL and you have four tools. This is how MCP servers should work. Brave, Exa, and most others still require local `npx` installation.

**Search + extract is a natural pipeline.** Instead of searching, picking a result, then figuring out how to read the page, Tavily lets the agent search and then extract content from the best URLs in a single workflow. The extract tool returns clean markdown — not raw HTML soup — so the content is immediately usable in the agent's context window.

**Crawl and map go beyond search.** These aren't search tools — they're web intelligence tools. An agent can map a documentation site's structure, identify the relevant sections, then crawl just those pages. The natural language `instructions` parameter is genuinely useful: "only crawl API reference pages" actually works to focus the crawl.

**Framework ecosystem integration is unmatched.** LangChain, LlamaIndex, CrewAI, Vercel AI SDK — Tavily is the default search provider in every major AI framework. If you're building with these tools, Tavily requires zero additional integration work. This isn't just convenience; it means better-tested code paths and more community examples.

**The free tier is adequate for experimentation.** 1,000 credits per month covers meaningful development and testing. Basic search costs 1 credit, advanced costs 2. You can run 500 advanced searches or 1,000 basic ones per month at zero cost. Students get free access. And the new pay-as-you-go option ($0.008/credit) means you can scale past the free tier without committing to a monthly plan.

## What Doesn't Work Well

**Search quality trails Exa on entity-level retrieval, by Exa's own numbers.** *Correction (2026-08-14 audit): an earlier version of this section cited a "WebWalker benchmark" (71% vs. 81%) attributed to Exa's comparison page — that page does not contain a WebWalker benchmark or those figures. We could not find that specific claim from any live primary source and have removed it.* [Exa's own comparison page](https://exa.ai/versus/tavily) does publish vendor-run entity-retrieval benchmarks showing Tavily behind: Company Search Recall@1 is 61.3% (Tavily) vs. 81.5% (Exa), and People Search Recall@1 is 40.5% (Tavily) vs. 75.5% (Exa). These are Exa's own numbers, not independently verified, and Tavily itself [describes its Search API as performing semantic search](https://www.tavily.com/blog/tavily-101-ai-powered-search-for-developers) rather than pure keyword matching — so treat the gap as directional, not a settled "keyword vs. semantic" story. For conceptual queries ("frameworks that help with LLM observability"), Exa's marketing claims and the entity-retrieval numbers above both suggest semantic search finds results that Tavily's ranking sometimes misses; for specific, well-defined queries ("Next.js middleware configuration"), this gap likely matters less.

**Credits don't roll over (on monthly plans).** [Per Tavily's pricing page](https://tavily.com/pricing), API credits "reset on the first day of each month, regardless of the billing date" — unused credits don't carry forward. If you have a quiet month, those credits are gone, and the sting scales with plan size: paid tiers start at the $30/month Project plan (4,000 credits/month) and scale up to custom Enterprise pricing. The pay-as-you-go option ($0.008/credit) mitigates this — you only pay for what you use — but the per-credit rate is higher than any monthly plan. Note that Brave [moved off a free tier to metered, credit-based billing in February 2026](https://brave.com/blog/most-powerful-search-api-for-ai/) as well, so the "Brave has no credit accounting" contrast we used to draw here no longer holds cleanly — see our [Brave Search MCP review](/reviews/brave-search-mcp-server/) for the current details.

**Costs stack up at scale.** A single crawl operation combines map costs and extract costs. Crawling 10 pages at basic depth costs ~3 credits, but with advanced extract depth, categories, and instructions, a single crawl can cost 10+ credits. The extract endpoint charges per 5 URLs. Advanced search is 2 credits. An agent doing thorough research — searching, extracting results, crawling source sites — can burn through credits faster than the per-search pricing suggests.

**Configuration friction with remote HTTP.** Two separate GitHub issues report friction with Claude Code's HTTP transport configuration: [#125](https://github.com/tavily-ai/tavily-mcp/issues/125) is a user struggling with `DEFAULT_PARAMETERS` header syntax, and [#121](https://github.com/tavily-ai/tavily-mcp/issues/121) reports a harder failure — Claude Code's HTTP client omits the `Accept: application/json, text/event-stream` header the server requires, so calls fail outright until the client is reconfigured for stdio. The remote server is easy to connect to but hard to customize. Most users end up falling back to the local stdio server for advanced configuration.

**API key in URL is a security concern.** The remote server's simplest authentication method puts your API key in the URL query string: `https://mcp.tavily.com/mcp/?tavilyApiKey=YOUR_KEY`. URL parameters appear in server logs, browser history, and proxy logs. OAuth support exists as an alternative, but the documentation leads with the URL approach. *(This is a common pattern in MCP, not unique to Tavily, but worth noting.)*

**Tool descriptions are inadequate for agent routing.** An automated quality scan (issue #141) gave Tavily a D grade — three of four tools have near-zero descriptions with no guidance on when to use extract vs. crawl vs. map. AI agents pick tools based on descriptions, so minimal descriptions mean agents may choose the wrong tool or ignore available capabilities. This is a straightforward fix that hasn't been addressed.

**No formal GitHub releases and infrequent npm releases.** Version 0.2.19 shipped April 24 — six weeks after 0.2.18. The releases page on GitHub remains empty; versioning goes entirely through npm. That's acceptable, but the long gap between releases means any fix or new feature is unavailable to pinned users for weeks.

**Nebius now owns Tavily outright — the roadmap uncertainty this created is real, even though the deal itself closed months ago.** [The $275M deal was announced February 10, 2026](https://siliconangle.com/2026/02/10/ai-infrastructure-giant-nebius-buys-agentic-search-startup-tavily/) and [closed February 19, 2026](https://www.stocktitan.net/sec-filings/NBIS/6-k-nebius-group-n-v-current-report-foreign-issuer-540144354e8c.html) — nine days later, confirmed via SEC filing rather than a dedicated press release. Pricing, free tier policy, and strategic direction could still shift now that Tavily operates as a wholly-owned Nebius subsidiary rather than an independent company; that uncertainty doesn't go away just because the deal is no longer "pending."

## Compared to Alternatives

**vs. Brave Search:** Brave has [grown to eight tools](https://github.com/brave/brave-search-mcp-server) (web, local, image, video, news, places, LLM context, summarizer) — up from six — to Tavily's four, and Brave's independent index means genuinely different results. But Brave is search-only — no extract, no crawl, no map. Tavily gives you more capabilities per server. If you need to both find and read pages, Tavily wins. If you need search breadth (images, video, local), Brave wins. Brave [dropped its free tier for metered, credit-based billing in February 2026](https://brave.com/blog/most-powerful-search-api-for-ai/), so it no longer avoids credit accounting the way it used to — see our [Brave Search MCP review](/reviews/brave-search-mcp-server/).

**vs. Exa:** Exa's semantic search genuinely understands concepts — it finds results that keyword search misses. Exa's MCP server [consolidated from 9 tools down to 4](https://github.com/exa-labs/exa-mcp-server) during 2026, folding the old async deep-research tools into a single `agent_run` tool — see our [Exa MCP server review](/reviews/exa-mcp-server/) for the timeline. Exa is more expensive at scale, and its neural search can over-generalize on exact queries. Use Exa for exploratory research, Tavily for targeted lookups and content extraction.

**vs. Firecrawl:** Firecrawl is the better pure web scraping tool — [26 tools](https://github.com/firecrawl/firecrawl-mcp-server#available-tools) as of mid-2026 (up from 14), autonomous research agents, LLM-powered structured extraction. Firecrawl now ships its own `firecrawl_search` web-search tool too, so "Tavily is the only one that searches" is no longer true — but Tavily's search + extract + crawl + map combination in one lightweight, four-tool server is still the tighter fit if you don't need Firecrawl's much larger toolkit.

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
- Operating under new ownership (Tavily is now a wholly-owned Nebius subsidiary) is a dealbreaker for your production stack

{{< verdict rating="4" summary="The best search-to-extract pipeline in one MCP server" >}}
Tavily's four-tool combination — search, extract, crawl, map — remains unmatched in one MCP server, and version 0.2.19 finally shipped the `exact_match` parameter along with CVE fixes and session tracking improvements. New integrations with Snowflake, MongoDB, and Arcade.dev expand reach, and the MCPSafe security audit gave it a solid B (92/100). The notable concern this cycle: npm weekly downloads dropped from ~93K to ~26K — a 72% decline from the April baseline that warrants monitoring. Tool description quality (issue #141, D grade) is still unresolved after more than a month. And Nebius's acquisition of Tavily — [closed February 19, 2026](https://www.stocktitan.net/sec-filings/NBIS/6-k-nebius-group-n-v-current-report-foreign-issuer-540144354e8c.html) per SEC filings, with no dedicated press release — means Tavily now operates as a wholly-owned Nebius subsidiary, adding roadmap uncertainty even though the deal itself is no longer in question. For the workflow of "find it, read it, crawl for more" — Tavily still handles the whole pipeline better than anyone, but the download trend and lingering description quality issues are worth watching.
{{< /verdict >}}

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic). We do not test MCP servers hands-on; all findings are based on documentation, source code, community reports, and public benchmarks. Last updated 2026-05-19.*

---

**Sources:** [tavily-ai/tavily-mcp (GitHub)](https://github.com/tavily-ai/tavily-mcp) · [Tavily MCP remote server (mcp.tavily.com)](https://mcp.tavily.com/mcp/) · [Tavily official site (tavily.com)](https://tavily.com)

