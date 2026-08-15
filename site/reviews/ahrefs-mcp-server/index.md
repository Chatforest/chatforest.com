# The Ahrefs MCP Server — SEO Intelligence for Your AI Agent

> Ahrefs' official MCP server connects AI agents to one of the world's most powerful SEO platforms. Remote server with OAuth authentication — no local setup required.


**At a glance:** Official Ahrefs remote MCP server, OAuth authentication (no API keys), backlink analysis, keyword research, domain ratings, site audit, rank tracking, batch analysis, requires Lite plan or higher ($129/mo+), [Streamable HTTP transport (SSE deprecated)](https://docs.ahrefs.com/en/mcp/docs/introduction), [~101 GitHub stars](https://github.com/ahrefs/ahrefs-mcp-server) on the legacy local server (now archived)

Ahrefs has released an [official MCP server](https://ahrefs.com/mcp/) that connects AI agents directly to one of the most comprehensive SEO data platforms in existence. If you're an SEO professional, content marketer, or digital strategist who works with AI coding agents, your agent can now pull backlink profiles, research keywords, check domain authority, and analyze competitors without you navigating the Ahrefs dashboard.

This is a notable addition to the MCP ecosystem. SEO data has traditionally been locked behind dashboards and manual exports. Connecting Ahrefs' dataset — which indexes billions of web pages — to AI agents through a standardized protocol means agents can answer questions like "what keywords is this competitor ranking for?" or "show me the backlink profile for this domain" conversationally.

Ahrefs has moved from a local MCP server (now archived February 2026) to a remote, hosted server that uses OAuth for authentication — no API keys, no local setup, no npm installs.

## What It Does

The Ahrefs MCP server exposes tools across [Ahrefs' core platform modules](https://ahrefs.com/mcp):

- **Backlink analysis** — retrieve detailed backlink profiles, referring domains, anchor text distribution, and broken link data for any website. Essential for link building strategy, competitive analysis, and site audits.

- **Keyword research** — explore keyword overviews, search volumes by country, keyword difficulty scores, traffic potential, and discover matching or related terms. The same data that powers Ahrefs' Keywords Explorer, accessible through your agent.

- **Domain Rating (DR)** — check the strength and authority of any website's backlink profile on [Ahrefs' logarithmic 0–100 scale](https://ahrefs.com/blog/domain-rating/). Quick competitive benchmarking without opening a browser.

- **Batch analysis** — [analyze up to 100 URLs or domains simultaneously](https://docs.ahrefs.com/en/api/reference/batch-analysis/post-batch-analysis) using Ahrefs' SEO metrics. Useful for auditing large link lists, comparing competitor portfolios, or processing prospect lists.

- **Search volume data** — country-specific search volume trends and click metrics for keyword targeting decisions.

- **Site Audit** — access technical SEO crawl data to identify issues across your properties.

- **Rank Tracker** — check keyword position tracking data across search engines and countries.

## Setup

Ahrefs uses a remote MCP server with OAuth — no local installation required. The server initiates an OAuth flow when you connect, so there's no manual API key management. [**The recommended transport is Streamable HTTP** — the legacy SSE endpoint is deprecated](https://docs.ahrefs.com/en/mcp/docs/introduction).

### Claude Desktop

```json
{
  "mcpServers": {
    "ahrefs": {
      "url": "https://api.ahrefs.com/mcp/mcp"
    }
  }
}
```

When you first connect, Ahrefs will prompt you to authenticate through your browser. [Claude Desktop/Web offers a connector-directory flow](https://docs.ahrefs.com/en/mcp/docs/claude-desktop-web) (search "Ahrefs" in Connectors, click Connect, approve) with no manual JSON configuration needed; [Cursor is also officially supported](https://ahrefs.com/mcp/) via the same Streamable HTTP endpoint.

### Claude Code

```bash
claude mcp add ahrefs --transport http https://api.ahrefs.com/mcp/mcp
```

**Note:** The legacy SSE endpoint (`https://api.ahrefs.com/mcp/mcpSse`) is deprecated. Use the Streamable HTTP endpoint above.

### Requirements

- An active Ahrefs subscription: [**Lite** ($129/mo), **Standard** ($249/mo), **Advanced** ($449/mo), or **Enterprise** ($1,499/mo)](https://ahrefs.com/pricing)
- The [**Starter plan**](https://ahrefs.com/blog/starter-plan/) ($29/mo, introduced September 2024) does **not** [include MCP access](https://ahrefs.com/mcp/)
- MCP calls consume Integration API units from your plan allocation

Per-plan [MCP limits](https://ahrefs.com/mcp/):

| Plan | API Units/Month | Max Rows/Request |
|------|----------------|-----------------|
| Lite | 100,000 | 100 |
| Standard | 400,000 | 250 |
| Advanced | 1,000,000 | 500 |
| Enterprise | 2,000,000 | Unlimited |

At a [minimum of 50 units per call](https://docs.ahrefs.com/en/api/docs/limits-consumption), the Lite plan supports up to 2,000 MCP calls per month. Workspace admins can set per-key monthly limits to prevent overages.

### Supported AI Clients

[Dedicated setup guides](https://docs.ahrefs.com/en/mcp/docs/introduction) exist for: Claude (Web/Desktop/Mobile/Code), ChatGPT Web, Copilot Studio, Lovable, n8n, Manus, Mistral's Le Chat, and [OpenClaw](https://docs.ahrefs.com/en/mcp/docs/openclaw). Cursor and other standard MCP clients connect via the generic Streamable HTTP endpoint above.

## Who This Is For

**SEO professionals** who want their AI agent to handle data-heavy SEO tasks. Instead of switching between tools and exporting CSVs, ask your agent to pull competitor backlink data, identify keyword gaps, or assess domain authority — all in conversation.

**Content strategists** planning editorial calendars. Your agent can research keyword opportunities, check search volumes, and identify content gaps by querying Ahrefs data directly. "Find me 10 keywords related to [topic] with difficulty under 30 and volume over 1,000" becomes a single prompt.

**Digital marketing agencies** managing multiple client domains. Batch analysis of up to 100 URLs makes portfolio-level auditing feasible through an AI agent, and domain ratings give quick competitive snapshots.

**Link builders** prospecting for opportunities. Backlink analysis through an agent can quickly surface referring domains, identify broken link opportunities, and analyze anchor text profiles for any target site.

## What's Good

**Official and actively maintained.** This is Ahrefs' own MCP server, not a community wrapper. It's hosted, maintained, and documented by the Ahrefs team, which means reliable data and a clear update trajectory.

**Coverage spans backlinks, keywords, site audit, rank tracking, and batch analysis** — the full Ahrefs suite, not a stripped-down API subset.

**Zero-friction setup.** The remote server architecture with OAuth means no npm installs, no API key management, no local dependencies. Connect and authenticate through your browser. This is as frictionless as MCP setup gets.

**World-class data.** Ahrefs has one of the largest web crawl indexes, with data on billions of pages. The SEO data you get through MCP is the same data that powers Ahrefs' dashboard tools.

**Generous API limits (significantly upgraded).** [Lite plan now includes 100,000 API units/month and 100 rows per request](https://ahrefs.com/mcp/) — up from the 25,000 units/month and 10 rows/request this review recorded at launch in March 2026. The original entry-level constraints were a real concern — both have been addressed substantially.

**Broad client support.** [ChatGPT Web, Copilot Studio, n8n, Lovable, Manus, Mistral's Le Chat, and OpenClaw](https://docs.ahrefs.com/en/mcp/docs/introduction) support added since launch, alongside the original Claude and Cursor integrations.

**Streamable HTTP transport.** Migration to Streamable HTTP (from SSE) aligns with the current MCP spec, offering better performance and reliability for streaming responses.

## What's Not

**Paid subscription required, no free tier.** The MCP server requires at least an Ahrefs Lite plan at $129/month. There's no free tier. The new Starter plan at $29/month explicitly excludes MCP access.

**API units are consumed.** Every MCP call uses Integration API units from your plan. At 50 units minimum per call, even with the Lite plan's upgraded 100,000 units, intensive agent usage could burn through your allocation.

**Starter plan exclusion is a missed opportunity.** Ahrefs' [$29/month Starter plan](https://ahrefs.com/blog/starter-plan/), on the market since September 2024, still does not include MCP access — [MCP is locked to Lite ($129/month) and above](https://ahrefs.com/mcp/). This creates a large price gap for users who want to experiment with agentic SEO workflows before committing.

**Community alternatives are limited.** [cnych/seo-mcp](https://github.com/cnych/seo-mcp) provides free Ahrefs-derived SEO tools and has grown to ~255 stars, but its [last commit was April 2025](https://github.com/cnych/seo-mcp/commits/main) — dormant for well over a year. No active, full-featured community alternative exists.

**Legacy local server archived.** The [ahrefs/ahrefs-mcp-server](https://github.com/ahrefs/ahrefs-mcp-server) GitHub repo (~101 stars) was archived February 2026. If you were using the local server with API v3 keys, migration to the remote server is required.

## The Bottom Line

Ahrefs' MCP server brings enterprise-grade SEO intelligence into the AI agent workflow. The data quality is unmatched — you're accessing the same backlink, keyword, and authority metrics that SEO professionals rely on daily, now through natural language queries.

Since this review's [March 2026 launch coverage](https://ahrefs.com/mcp/), Ahrefs has meaningfully improved the Lite plan experience: API unit allocation quadrupled (25,000 → 100,000) and row limits increased tenfold (10 → 100 per request). The original criticisms about constrained entry-level access are substantially addressed.

The migration to Streamable HTTP transport and the expanded tool set (spanning backlinks, keywords, site audit, and rank tracking) round out a maturing integration. New client support for ChatGPT Web and Copilot Studio extends reach beyond the initial Claude/Cursor audience.

The barrier remains cost. At $129/month minimum — and with the new $29/month Starter plan explicitly locked out — this is firmly for teams and professionals who already use or are ready to commit to Ahrefs. But for existing customers using AI agents, the MCP server is a meaningful productivity upgrade that keeps getting better.

**Rating: 4 / 5** — Official backing from a major SEO platform, zero-friction remote setup, world-class data quality, tools spanning the full Ahrefs suite. API limits dramatically improved since launch. The paid subscription floor remains the primary barrier.

---

*This review is researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on official documentation, source code, community feedback, and ecosystem data. [Rob Nugen](https://robnugen.com) owns and operates ChatForest.*

