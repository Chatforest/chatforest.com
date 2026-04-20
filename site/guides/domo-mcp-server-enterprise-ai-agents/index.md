# Domo's MCP Server and AI Agent Builder: Connecting Enterprise Data to the AI Ecosystem

> Domo launched an MCP Server and AI Agent Builder at Domopalooza 2026 — connecting enterprise datasets, workflows, and interactive dashboards to external AI platforms like Claude, Gemini, and ChatGPT.


Most MCP servers return text. Domo's returns interactive dashboards — complete with filters and drilldowns — rendered directly inside AI chat interfaces. That's the headline feature from Domo's March 2026 Domopalooza announcements, but the broader story is about connecting governed enterprise data to the AI agent ecosystem through an open-source MCP server, a low-code AI Agent Builder, and a new AI Toolkit architecture.

Our analysis draws on [Domo's official press release](https://www.domo.com/news/press/domo-launches-ai-agent-builder-and-mcp-serve), [Domo's product feature page](https://www.domo.com/product/new-features/ai-agents-mcp-domopalooza-announcements), [BigDATAwire coverage](https://www.hpcwire.com/bigdatawire/this-just-in/domo-launches-ai-agent-builder-and-mcp-server-to-connect-enterprise-data-to-the-ai-ecosystem/), [TechIntelPro's analysis](https://techintelpro.com/news/ai/enterprise-ai/domo-launches-ai-agent-builder-and-mcp-server-for-enterprise-ai), [Futurum Group's earnings analysis](https://futurumgroup.com/insights/domo-q4-fy-2026-earnings-show-record-billings-and-profitability-gains/), and the [open-source GitHub repository](https://github.com/DomoApps/domo-mcp-server) — we research and analyze rather than testing implementations hands-on.

## Why This Matters

Enterprise data platforms have a persistent problem: they hold valuable data behind proprietary interfaces that only trained users can navigate. When AI agents need to answer business questions, they hit a wall — the data is locked inside BI platforms that weren't designed for programmatic AI access.

Domo's approach attacks this from both sides. The open-source MCP server gives any AI agent SQL access to Domo datasets. The enterprise platform goes further, letting AI agents trigger workflows, create dashboards, and manage business processes — all under the same governance controls that protect the data from human misuse.

The timing aligns with a broader industry shift. At Domopalooza, Domo shared over 200 AI use cases from customers' live production environments, signaling that enterprise AI is moving from pilot experiments to operational systems.

## The Open-Source MCP Server

The [Domo MCP Server](https://github.com/DomoApps/domo-mcp-server) is an MIT-licensed Python server that connects AI agents to Domo's API through the Model Context Protocol.

### Technical Details

| Detail | Info |
|--------|------|
| **Repository** | [DomoApps/domo-mcp-server](https://github.com/DomoApps/domo-mcp-server) |
| **Stars** | 8 |
| **Language** | Python (96.9%) |
| **License** | MIT |
| **Transport** | stdio |
| **Requirements** | Python 3.11+ or Docker |
| **Authentication** | Developer access token + Domo host URL |

### Seven MCP Tools

The server exposes seven tools:

1. **`search_datasets(query)`** — find datasets by name, the natural starting point for data exploration
2. **`get_dataset_metadata(dataset_id)`** — retrieve dataset metadata (owner, creation date, row count, update frequency)
3. **`get_dataset_schema(dataset_id)`** — get column names, types, and structure
4. **`query_dataset(dataset_id, query)`** — execute SQL queries against any dataset the token can access
5. **`list_roles()`** — enumerate all roles in the Domo instance
6. **`create_role(name, from_role_id, description)`** — create new roles (cloned from existing ones)
7. **`list_role_authorities(role_id)`** — inspect what permissions a role grants

The first four tools form the data exploration workflow: search for a dataset, understand its structure, then query it. The role management tools (5-7) are notable — they indicate Domo is thinking about governance from the MCP layer, not just data access.

### Setup

The server runs locally via Python or Docker. Configuration goes in your MCP client's settings (VS Code, Claude Desktop, Cursor):

```json
{
  "mcpServers": {
    "domo-mcp-server": {
      "command": "python",
      "args": ["-m", "domo_mcp_server"],
      "env": {
        "DOMO_DEVELOPER_TOKEN": "your-token-here",
        "DOMO_HOST": "your-instance.domo.com"
      }
    }
  }
}
```

For Docker deployment:

```bash
docker build -t domo-mcp-server .
```

Authentication uses Domo's developer access tokens. The token's permissions scope what datasets and operations the MCP server can access — the same permission model that governs human API access.

## The Enterprise Platform: AI Agent Builder and Toolkits

The open-source server handles data queries. The broader enterprise announcement covers a full AI orchestration framework with three components.

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

The BI MCP landscape is crowded. [Grafana's MCP server](/reviews/bi-reporting-mcp-servers/) leads with 2,600+ stars and 40+ tools. [Power BI](/reviews/bi-reporting-mcp-servers/) ships two official servers. [Tableau](/reviews/bi-reporting-mcp-servers/), [Looker](/reviews/bi-reporting-mcp-servers/), [Qlik](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-server.htm), and [ThoughtSpot](/guides/mcp-data-visualization-business-intelligence/) all have official MCP support.

What differentiates Domo's approach:

| Feature | Domo | Grafana | Power BI | Tableau |
|---------|------|---------|----------|---------|
| **Interactive rendering** | Dashboards in chat | Text/JSON | Text/JSON | Text/JSON |
| **Agent builder** | Low-code, built-in | No | Copilot Studio (separate) | Tableau Pulse (limited) |
| **Toolkit architecture** | Composable packages | No | No | No |
| **Governance hub** | AI Library | No | Purview (separate) | No |
| **Open-source server** | Yes (MIT) | Yes (AGPLv3) | Yes (MIT) | Yes (MIT) |
| **Stars** | 8 | 2,600+ | 500+ | 200+ |

Domo's MCP server has far fewer stars and tools than Grafana or Power BI, but the enterprise platform layer — Agent Builder, Toolkits, AI Library — is more comprehensive than what any other BI vendor offers through MCP specifically.

### The Interactive Rendering Advantage

Most MCP servers return structured text or JSON that the AI client renders as markdown tables or code blocks. Domo's ability to return interactive dashboards is genuinely novel in the MCP ecosystem. It leverages Domo's existing embedded analytics infrastructure, which means the rendering isn't a prototype — it builds on production-grade embedding technology.

The limitation: this interactive rendering likely requires Domo's enterprise platform and may not work through the open-source MCP server alone.

### Domo's Market Position

Domo is a publicly traded enterprise data platform (NASDAQ: DOMO) with fiscal 2026 revenue of $318.9 million and over 2,600 customers. Q4 FY2026 billings hit $111.2 million (up 8% year-over-year) — a company record. The company is shifting to consumption-based pricing, with 84% of annual recurring revenue now from consumption contracts and a 111% net retention rate for that cohort.

Analyst Brad Shimmin at Futurum Group noted Domo is strategically shifting toward "workflow automation outcomes that are measurable and recurring," though he flagged potential misalignment with the broader market's move toward outcome-based pricing rather than token-based consumption.

AI is discussed in nearly 70% of Domo's customer and prospect conversations, per management — indicating that the MCP and agent capabilities are central to the company's go-to-market strategy, not a side feature.

## What This Signals for Enterprise MCP

Domo's announcement illustrates several trends in the enterprise MCP space:

**BI platforms are becoming agent platforms.** Domo isn't just adding MCP as an API wrapper — they're building agent creation, toolkit management, and governance infrastructure around it. This positions BI platforms as the coordination layer for enterprise AI agents, not just data sources.

**Interactive rendering raises the bar.** If Domo can render dashboards inside chat, other BI vendors will follow. This could shift expectations for what MCP integrations deliver — from text answers to interactive experiences.

**Governance is the enterprise differentiator.** The open-source server is straightforward (7 tools, dataset queries). The enterprise value is in the governance layer — toolkits with declared permissions, centralized AI Library, token-scoped access. For regulated industries, this matters more than tool count.

**The open-source server is a gateway.** The MIT-licensed server is intentionally limited. It gets developers experimenting with Domo + MCP, but the interactive dashboards, agent builder, and toolkit architecture require the commercial platform. This is a familiar enterprise open-source strategy.

## Getting Started

For individual developers:

1. Clone the [open-source server](https://github.com/DomoApps/domo-mcp-server)
2. Generate a [Domo developer access token](https://developer.domo.com/)
3. Configure your MCP client (Claude Desktop, VS Code, Cursor)
4. Start with `search_datasets` to explore available data, then `query_dataset` for SQL access

For enterprise teams evaluating the AI Agent Builder, AI Toolkits, and AI Library — these features are being announced now with the AI Library scheduled for summer 2026. Contact Domo for access to the Agent Builder and Toolkit capabilities.

## Related

- [MCP and Data Visualization / Business Intelligence](/guides/mcp-data-visualization-business-intelligence/) — comprehensive guide covering 80+ servers across the analytics stack
- [BI & Reporting MCP Servers](/reviews/bi-reporting-mcp-servers/) — Grafana, Power BI, Tableau, Metabase, Looker, Superset reviews
- [Best Data Analytics MCP Servers](/guides/best-data-analytics-mcp-servers/) — curated picks across the data analytics ecosystem
- [MCP Enterprise Infrastructure](/guides/mcp-enterprise-infrastructure/) — patterns for deploying MCP in enterprise environments
- [Analytics MCP Servers](/reviews/analytics-mcp-servers/) — Google Analytics, Mixpanel, PostHog, Amplitude reviews

