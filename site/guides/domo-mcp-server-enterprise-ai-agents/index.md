# Domo's MCP Server and AI Agent Builder: Connecting Enterprise Data to the AI Ecosystem

> Domo launched an MCP Server and AI Agent Builder at Domopalooza 2026 — connecting enterprise datasets, workflows, and interactive dashboards to external AI platforms like Claude, Gemini, and ChatGPT.


Most MCP servers return text. Domo's returns interactive dashboards — complete with filters and drilldowns — rendered directly inside AI chat interfaces. That's the headline feature from Domo's March 2026 Domopalooza announcements, but the broader story is about connecting governed enterprise data to the AI agent ecosystem through the Domo MCP Server, a low-code AI Agent Builder, and a new AI Toolkit architecture.

Our analysis draws on [Domo's official press release](https://www.domo.com/news/press/domo-launches-ai-agent-builder-and-mcp-serve), [Domo's product feature page](https://www.domo.com/product/new-features/ai-agents-mcp-domopalooza-announcements), [Domo's official MCP setup documentation](https://www.domo.com/docs/s/article/Connect-AI-Tools-to-Domo-Using-MCP), [BigDATAwire coverage](https://www.hpcwire.com/bigdatawire/this-just-in/domo-launches-ai-agent-builder-and-mcp-server-to-connect-enterprise-data-to-the-ai-ecosystem/), [TechIntelPro's analysis](https://techintelpro.com/news/ai/enterprise-ai/domo-launches-ai-agent-builder-and-mcp-server-for-enterprise-ai), and [Futurum Group's earnings analysis](https://futurumgroup.com/insights/domo-q4-fy-2026-earnings-show-record-billings-and-profitability-gains/) — we research and analyze rather than testing implementations hands-on. **Correction (2026-08-19):** an earlier version of this guide linked a GitHub repository (`DomoApps/domo-mcp-server`) as the server's open-source code and described specific tools, a license, and install steps drawn from it. That repository does not exist — it 404s, it has no Wayback Machine snapshot, and it appears nowhere in any of the sources above. None of Domo's own materials describe the MCP Server as open source. The fabricated repository details have been removed; see the note in the section below.

## Why This Matters

Enterprise data platforms have a persistent problem: they hold valuable data behind proprietary interfaces that only trained users can navigate. When AI agents need to answer business questions, they hit a wall — the data is locked inside BI platforms that weren't designed for programmatic AI access.

Domo's approach attacks this from both sides. The [MCP server lets AI agents query Domo datasets and analytics, trigger workflows, create dashboards, and configure alerts](https://www.domo.com/news/press/domo-launches-ai-agent-builder-and-mcp-serve). The enterprise platform goes further, letting AI agents manage broader business processes — all under the same governance controls that protect the data from human misuse.

The timing aligns with a broader industry shift. At Domopalooza, [Domo shared over 200 AI use cases from customers' live production environments](https://www.domo.com/news/press/domo-launches-ai-agent-builder-and-mcp-serve), signaling that enterprise AI is moving from pilot experiments to operational systems.

## The Domo MCP Server

Domo has not published the MCP Server's source code, a repository, a license, or a specific tool list in any of its own announcement materials (the press release, the product feature page, or its earnings coverage). An earlier version of this guide asserted the server was MIT-licensed Python with 8 GitHub stars and seven named tools, linked to `github.com/DomoApps/domo-mcp-server` — that repository returns a 404, has never been archived by the Wayback Machine, and the `DomoApps` GitHub organization has no MCP-related repositories in its public listing (checked 2026-08-19). None of the article's own cited sources mention it either. That entire technical profile was unsourced and has been removed rather than corrected, per this site's "cite it or cut it" standard — there is nothing to cite it to.

What Domo's own materials do confirm about the server: it is [built on the Model Context Protocol standard and connects AI Toolkits and agents to external AI platforms such as Claude, Gemini, and ChatGPT](https://www.domo.com/news/press/domo-launches-ai-agent-builder-and-mcp-serve). The March press release described AI assistants querying datasets and analytics, triggering workflows and automation, creating dashboards and applications, and configuring alerts and operational processes as the vision for the platform.

**Update (2026-08-26):** Domo has since published a first concrete implementation. [Official documentation dated 2026-08-24 describes the "Domo Essentials MCP Server,"](https://www.domo.com/docs/s/article/Connect-AI-Tools-to-Domo-Using-MCP) in public open beta, connecting Claude Desktop, Claude Code, or VS Code via standard OAuth or manual configuration. As documented, it supports four capabilities: querying data in Domo DataSets, listing and querying Document Collections stored in Domo, searching across a Domo instance, and querying Domo's own documentation. That is narrower than the March press release's full vision — the beta docs do not describe triggering workflows, creating dashboards, or configuring alerts. Domo AI (and this MCP beta) is available to customers on a consumption agreement; customers not on one can request a trial through their Customer Success Manager, per the same documentation. No source code, repository, or license is published for it — it is a hosted service reachable via OAuth, not an open-source package — so the "not open source" framing above still holds, but "no documented setup steps" no longer does.

## The Enterprise Platform: AI Agent Builder and Toolkits

The MCP server handles data queries and workflow actions. The broader enterprise announcement covers a full AI orchestration framework with three components.

### AI Agent Builder

AI Agent Builder is a low-code tool for creating conversational AI agents connected to Domo's data and workflow infrastructure. Agents can be built for specific business roles — a financial analyst agent that queries revenue datasets, an operations manager agent that monitors supply chain dashboards, a customer success agent that tracks account health metrics.

Each agent is built from AI Toolkits — packaged sets of capabilities that define what the agent can do. A toolkit combines:

- **Tools** — specific actions (query a dataset, trigger a workflow, create an alert)
- **Data connections** — which datasets and data sources the agent can access
- **Workflows** — multi-step business processes the agent can trigger
- **Instructions** — business context and rules that guide agent behavior
- **Governance rules** — what the agent is and isn't allowed to do

Toolkits can come from Domo, from customers building their own, or from external services. This composability means organizations can mix and match capabilities rather than building agents from scratch.

### AI Library

The AI Library is a centralized hub for curating and managing AI solutions across an organization. Think of it as an internal app store for AI agents and toolkits — administrators can publish, version, and control access to agents, ensuring consistent governance across the enterprise.

The AI Library is scheduled for availability in summer 2026.

### Interactive Dashboard Rendering

This is the most technically distinctive feature. When an external AI agent (Claude, Gemini, ChatGPT) connects to Domo through the MCP server, it can return interactive business experiences — not just text responses.

A sales leader asking "analyze pipeline risk this quarter" could receive an interactive dashboard with filters, drilldowns, and real-time data — rendered directly in the chat interface. This goes beyond the text-and-table responses that most MCP integrations provide.

The technical implementation leverages Domo's existing embedded analytics infrastructure. Domo already supports embedding dashboards in web applications; the MCP integration extends this capability into AI chat interfaces.

## Governance and Security

Enterprise data governance is Domo's central selling point for the MCP integration. The framework emphasizes:

- **Token-scoped access** — MCP server permissions match developer token permissions
- **Shared semantic context** — agents operate on the same governed data definitions as human users
- **Toolkit-level controls** — each toolkit explicitly declares what an agent can access and do
- **Centralized management** — the AI Library gives administrators visibility and control over all deployed agents

CEO Josh James framed the vision: the tools help users "build AI agents connected to trusted enterprise data and workflows, turning AI from an abstract capability into something that actually drives business outcomes."

InformData, a Domo customer, highlighted the governance angle: bringing data and workflows into "a single, connected environment" gives them "the control and context we need to build reliably."

## Competitive Context

### Domo vs. Other BI Platform MCP Servers

The BI MCP landscape is crowded. [Grafana's MCP server](/reviews/bi-reporting-mcp-servers/) leads with [3,300+ stars](https://github.com/grafana/mcp-grafana) and 40+ tools. [Power BI](/reviews/bi-reporting-mcp-servers/) ships two official servers, including [Microsoft's powerbi-modeling-mcp (1,000+ stars)](https://github.com/microsoft/powerbi-modeling-mcp). [Tableau](/reviews/bi-reporting-mcp-servers/) ships [tableau/tableau-mcp (300+ stars)](https://github.com/tableau/tableau-mcp). [Looker](/reviews/bi-reporting-mcp-servers/), [Qlik](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-server.htm), and [ThoughtSpot](/guides/mcp-data-visualization-business-intelligence/) all have official MCP support.

What differentiates Domo's approach:

| Feature | Domo | Grafana | Power BI | Tableau |
|---------|------|---------|----------|---------|
| **Interactive rendering** | Dashboards in chat | Text/JSON | Text/JSON | Text/JSON |
| **Agent builder** | Low-code, built-in | No | Copilot Studio (separate) | Tableau Pulse (limited) |
| **Toolkit architecture** | Composable packages | No | No | No |
| **Governance hub** | AI Library | No | Purview (separate) | No |
| **Public GitHub repo / license** | Not published | Yes (Apache-2.0) | Yes (MIT) | Yes (Apache-2.0) |
| **Stars** | Not published | 3,300+ | 1,000+ | 300+ |

*(Grafana, Power BI, and Tableau star/license figures verified live against their repos on 2026-08-19; an earlier version of this table listed a stale AGPLv3 license for Grafana and MIT for Tableau — both are Apache-2.0 — and cited 8 stars and an MIT license for Domo based on the fabricated repository described above.)*

Domo has not published a repository, star count, or tool list for its MCP server — unlike Grafana, Power BI, and Tableau, whose official servers are public. What the company has emphasized instead is the enterprise platform layer — Agent Builder, Toolkits, AI Library — which is more comprehensive than what any other BI vendor offers through MCP specifically.

### The Interactive Rendering Advantage

Most MCP servers return structured text or JSON that the AI client renders as markdown tables or code blocks. Domo's ability to return interactive dashboards is genuinely novel in the MCP ecosystem. It leverages Domo's existing embedded analytics infrastructure, which means the rendering isn't a prototype — it builds on production-grade embedding technology.

The limitation: this interactive rendering likely requires Domo's enterprise platform and may not work through the MCP server alone.

### Domo's Market Position

Domo is a publicly traded enterprise data platform (NASDAQ: DOMO) with [fiscal 2026 revenue of $318.9 million](https://www.domoinvestors.com/news/news-details/2026/Domo-Announces-Fourth-Quarter-and-Fiscal-2026-Financial-Results/default.aspx) and [over 2,600 customers](https://www.domo.com/customers). [Q4 FY2026 billings hit $111.2 million (up 8% year-over-year) — a company record](https://www.domoinvestors.com/news/news-details/2026/Domo-Announces-Fourth-Quarter-and-Fiscal-2026-Financial-Results/default.aspx). The company is shifting toward consumption-based pricing: [customers on consumption contracts (over $24.0 million in ARR) delivered 111% net revenue retention in Q4 FY2026](https://futurumgroup.com/insights/domo-q4-fy-2026-earnings-show-record-billings-and-profitability-gains/), and overall net retention improved for a sixth consecutive quarter. **Correction (2026-08-19):** an earlier version of this section claimed "84% of annual recurring revenue" comes from consumption contracts — that figure appears in neither the earnings release nor the Futurum analysis it was cited to and has been removed; the real, sourced number is the $24.0M consumption-cohort ARR and its 111% retention rate above.

Analyst Brad Shimmin at Futurum Group noted Domo is strategically shifting toward "workflow automation outcomes that are measurable and recurring," though he flagged potential misalignment with the broader market's move toward outcome-based pricing rather than token-based consumption.

[AI is discussed in nearly 70% of Domo's customer and prospect conversations, per management](https://futurumgroup.com/insights/domo-q4-fy-2026-earnings-show-record-billings-and-profitability-gains/) — indicating that the MCP and agent capabilities are central to the company's go-to-market strategy, not a side feature. (This figure is from Domo management's earnings-call commentary as reported by Futurum Group; it does not appear in Domo's own press release.)

## What This Signals for Enterprise MCP

Domo's announcement illustrates several trends in the enterprise MCP space:

**BI platforms are becoming agent platforms.** Domo isn't just adding MCP as an API wrapper — they're building agent creation, toolkit management, and governance infrastructure around it. This positions BI platforms as the coordination layer for enterprise AI agents, not just data sources.

**Interactive rendering raises the bar.** If Domo can render dashboards inside chat, other BI vendors will follow. This could shift expectations for what MCP integrations deliver — from text answers to interactive experiences.

**Governance is the enterprise differentiator.** Domo's initial beta implementation, [documented 2026-08-24](https://www.domo.com/docs/s/article/Connect-AI-Tools-to-Domo-Using-MCP), is narrower than the four capabilities the March press release described — it's currently query- and search-focused rather than workflow-triggering or dashboard-creating. The enterprise value Domo emphasizes is still the governance layer — toolkits with declared permissions, centralized AI Library, consumption-agreement gating, grant-based access. For regulated industries, that framing matters more than a tool count would.

**Open-source status is unclear.** Unlike Grafana, Power BI, and Tableau, whose MCP servers are public repositories developers can inspect, Domo has not published one for its MCP server, and this guide could not confirm whether it plans to. Developers evaluating Domo alongside those alternatives should treat that as an open question, not an assumption in either direction.

## Getting Started

As of 2026-08-24, Domo publishes an actual setup flow: [official documentation for connecting AI tools to Domo via MCP](https://www.domo.com/docs/s/article/Connect-AI-Tools-to-Domo-Using-MCP) covers OAuth and manual-configuration paths for Claude Desktop, Claude Code, and VS Code, gated behind a Domo AI consumption agreement (or a CSM-arranged trial). It does not mention Cursor. For individual users:

1. Confirm your Domo role has the "Use AI Services" and "Use AI Chat" grants, per [Domo's MCP documentation](https://www.domo.com/docs/s/article/Connect-AI-Tools-to-Domo-Using-MCP)
2. Follow Domo's guide to [connect via standard OAuth](https://www.domo.com/docs/s/article/Connect-AI-Tools-to-Domo-Using-MCP) (recommended) or configure the connection manually
3. Note that calls routed through Domo-provided models can incur input/output token charges, per the same documentation

This is a beta, hosted-service integration — Domo has not published a downloadable package, source code, or license for it. For broader API and developer-token access, [Domo's developer portal](https://developer.domo.com/) remains the general entry point.

For enterprise teams evaluating the AI Agent Builder, AI Toolkits, and AI Library — these features are being announced now with the AI Library scheduled for summer 2026. Contact Domo for access to the Agent Builder and Toolkit capabilities.

## Related

- [MCP and Data Visualization / Business Intelligence](/guides/mcp-data-visualization-business-intelligence/) — comprehensive guide covering 80+ servers across the analytics stack
- [BI & Reporting MCP Servers](/reviews/bi-reporting-mcp-servers/) — Grafana, Power BI, Tableau, Metabase, Looker, Superset reviews
- [Best Data Analytics MCP Servers](/guides/best-data-analytics-mcp-servers/) — curated picks across the data analytics ecosystem
- [MCP Enterprise Infrastructure](/guides/mcp-enterprise-infrastructure/) — patterns for deploying MCP in enterprise environments
- [Analytics MCP Servers](/reviews/analytics-mcp-servers/) — Google Analytics, Mixpanel, PostHog, Amplitude reviews

