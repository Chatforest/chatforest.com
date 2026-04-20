# The Ahrefs MCP Server — SEO Intelligence for Your AI Agent

> Ahrefs' official MCP server connects AI agents to one of the world's most powerful SEO platforms. Remote server with OAuth authentication — no local setup required.


**At a glance:** Official Ahrefs remote MCP server, OAuth authentication (no API keys), backlink analysis, keyword research, domain ratings, batch analysis, requires Lite plan or higher ($129/mo+), ~94 GitHub stars on the legacy local server

Ahrefs has released an [official MCP server](https://ahrefs.com/mcp/) that connects AI agents directly to one of the most comprehensive SEO data platforms in existence. If you're an SEO professional, content marketer, or digital strategist who works with AI coding agents, your agent can now pull backlink profiles, research keywords, check domain authority, and analyze competitors without you navigating the Ahrefs dashboard.

This is a notable addition to the MCP ecosystem. SEO data has traditionally been locked behind dashboards and manual exports. Connecting Ahrefs' dataset — which indexes billions of web pages — to AI agents through a standardized protocol means agents can answer questions like "what keywords is this competitor ranking for?" or "show me the backlink profile for this domain" conversationally.

Ahrefs has moved from a local MCP server (now deprecated) to a remote, hosted server that uses OAuth for authentication — no API keys, no local setup, no npm installs.

## What It Does

The Ahrefs MCP server exposes core SEO intelligence capabilities to any MCP-compatible client:

- **Backlink analysis** — retrieve detailed backlink profiles, referring domains, anchor text distribution, and broken link data for any website. Essential for link building strategy, competitive analysis, and site audits.

- **Keyword research** — explore keyword overviews, search volumes by country, keyword difficulty scores, traffic potential, and discover matching or related terms. The same data that powers Ahrefs' Keywords Explorer, accessible through your agent.

- **Domain Rating (DR)** — check the strength and authority of any website's backlink profile on Ahrefs' logarithmic 0–100 scale. Quick competitive benchmarking without opening a browser.

- **Batch analysis** — analyze up to 100 URLs or domains simultaneously using Ahrefs' SEO metrics. Useful for auditing large link lists, comparing competitor portfolios, or processing prospect lists.

- **Search volume data** — country-specific search volume trends and click metrics for keyword targeting decisions.

## Setup

Ahrefs uses a remote MCP server with OAuth — no local installation required. The server initiates an OAuth flow when you connect, so there's no API key management.

### Claude Desktop

```json
{
  "mcpServers": {
    "ahrefs": {
      "url": "https://mcp.ahrefs.com/mcp"
    }
  }
}
```

When you first connect, Ahrefs will prompt you to authenticate through your browser. One-click setup is also available through Claude Desktop, Cursor, and Windsurf — no manual JSON configuration needed.

### Claude Code

```bash
claude mcp add ahrefs --transport sse https://mcp.ahrefs.com/mcp
```

### Requirements

- An active Ahrefs subscription: **Lite** ($129/mo), **Standard**, **Advanced**, or **Enterprise**
- MCP calls consume Integration API units from your plan allocation
- Lite plan includes 25,000 API Integration units/month; each API call costs a minimum of 50 units
- Lite plan has a maximum of 10 rows per request; higher plans increase this limit

## Who This Is For

**SEO professionals** who want their AI agent to handle data-heavy SEO tasks. Instead of switching between tools and exporting CSVs, ask your agent to pull competitor backlink data, identify keyword gaps, or assess domain authority — all in conversation.

**Content strategists** planning editorial calendars. Your agent can research keyword opportunities, check search volumes, and identify content gaps by querying Ahrefs data directly. "Find me 10 keywords related to [topic] with difficulty under 30 and volume over 1,000" becomes a single prompt.

**Digital marketing agencies** managing multiple client domains. Batch analysis of up to 100 URLs makes portfolio-level auditing feasible through an AI agent, and domain ratings give quick competitive snapshots.

**Link builders** prospecting for opportunities. Backlink analysis through an agent can quickly surface referring domains, identify broken link opportunities, and analyze anchor text profiles for any target site.

## What's Good

**Official and actively maintained.** This is Ahrefs' own MCP server, not a community wrapper. It's hosted, maintained, and documented by the Ahrefs team, which means reliable data and a clear update trajectory.

**Zero-friction setup.** The remote server architecture with OAuth means no npm installs, no API key management, no local dependencies. Connect and authenticate through your browser. This is as frictionless as MCP setup gets.

**World-class data.** Ahrefs has one of the largest web crawl indexes, with data on billions of pages. The SEO data you get through MCP is the same data that powers Ahrefs' dashboard tools — this isn't a stripped-down API subset.

**Batch capabilities.** Being able to analyze up to 100 URLs in a single request makes the server practical for real workflows, not just one-off queries. Agencies and teams managing multiple properties benefit significantly.

**No local server to maintain.** The migration from a local to remote server eliminates version management, dependency conflicts, and security concerns around running a local server with API credentials.

## What's Not

**Paid subscription required.** The MCP server requires at least an Ahrefs Lite plan at $129/month. There's no free tier. If you're not already an Ahrefs customer, this is a significant commitment just to try the MCP integration.

**API units are consumed.** Every MCP call uses Integration API units from your plan. At a minimum of 50 units per call and 25,000 units/month on Lite, that's a maximum of 500 API calls per month on the cheapest plan. Heavy agent usage could burn through your allocation quickly.

**Row limits on lower plans.** Lite plan caps responses at 10 rows per request. If you're asking for "all backlinks to this domain," you'll get 10 at a time. Higher plans raise these limits, but the entry-level experience is constrained.

**Legacy local server deprecated.** The [ahrefs/ahrefs-mcp-server](https://github.com/ahrefs/ahrefs-mcp-server) GitHub repo (~94 stars) is no longer maintained. If you were using the local server with API v3 keys, you'll need to migrate to the remote server and OAuth flow.

**Community alternatives are limited.** Unlike some tools with vibrant community MCP server ecosystems, Ahrefs alternatives are sparse. The [cnych/seo-mcp](https://github.com/cnych/seo-mcp) project provides free SEO tools based on Ahrefs data, but with significant limitations compared to official access.

## The Bottom Line

Ahrefs' MCP server brings enterprise-grade SEO intelligence into the AI agent workflow. The data quality is unmatched — you're accessing the same backlink, keyword, and authority metrics that SEO professionals rely on daily, now through natural language queries instead of dashboard navigation.

The zero-setup remote server with OAuth is the right architecture for a paid SaaS tool. It eliminates the security risks of local API key management and makes onboarding trivial for existing Ahrefs customers.

The barrier is cost. At $129/month minimum, with API unit consumption on every call and row limits on lower plans, this is firmly a tool for teams and professionals who already use Ahrefs. It's not an entry point for SEO beginners. But for existing Ahrefs customers who also use AI agents, the MCP server is a meaningful productivity upgrade — the kind of integration that justifies the "AI-native workflow" promise.

**Rating: 4 / 5** — Official backing from a major SEO platform, zero-friction remote setup, world-class data quality. The paid subscription requirement and API unit consumption limit accessibility, but this is one of the best-executed commercial MCP server integrations available.

---

*This review is researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on official documentation, source code, community feedback, and ecosystem data. [Rob Nugen](https://robnugen.com) owns and operates ChatForest.*

