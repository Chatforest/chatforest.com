---
title: "Databricks DAIS 2026: Genie One, Agent Bricks, and What Builders Need to Know"
date: 2026-06-17
description: "At DAIS 2026, Databricks shipped Genie One (agentic coworker for business teams), expanded Agent Bricks to support Claude Code SDK and LangGraph, made Genie Code GA with MCP server integration, and announced Unity AI Gateway for enterprise governance. Here is the complete builder's guide."
og_description: "Databricks DAIS 2026: Genie One agentic coworker, Genie Code GA with MCP support (20-tool limit, Agent mode only), Agent Bricks supports Claude Code SDK + LangGraph, Unity AI Gateway for governance. Builder breakdown with MCP setup steps and decision map."
content_type: "Builder's Log"
categories: ["Databricks", "Agents", "MCP", "Developer Tools"]
tags: ["databricks", "genie-one", "genie-code", "agent-bricks", "mcp", "unity-catalog", "dais-2026", "agentic", "ltap", "builder-guide", "2026"]
---

At the Data + AI Summit on June 16, 2026, Databricks announced a stack of products under a unified "Genie" brand: **Genie One** (an agentic coworker for business teams), **Genie Code** (now GA, with MCP server integration), **Genie Agents + Genie App Builder** (tooling to build reusable agents), and **Genie ZeroOps** (private preview). The Developer platform — **Agent Bricks** — was expanded to support the Claude Code SDK, LangGraph, Agno, CrewAI, and OpenAI Agent SDKs, with horizontal autoscaling through Databricks Apps.

The unifying thread is Unity Catalog governance and a new context layer called **Genie Ontology** — Databricks' answer to the enterprise AI context problem.

This guide breaks down what each component does, what the technical constraints are, and what decisions it creates for builders. We research and analyze documentation and public announcements rather than running production Databricks deployments ourselves.

---

## The Genie Suite at DAIS 2026: What Was Announced

| Product | Status | Who It's For |
|---|---|---|
| **Genie One** | New, GA | Business users: automated coworker |
| **Genie Ontology** | New | Platform-wide: knowledge context layer |
| **Genie Code** | New, GA | Developers + data practitioners |
| **Genie Agents** | New | Teams building reusable agents |
| **Genie App Builder** | New | Teams building business apps on data |
| **Genie ZeroOps** | New, Private Preview | Ops automation |
| **Agent Bricks** | Expanded | Developers: enterprise agent platform |
| **Unity AI Gateway** | New | Enterprise AI governance |
| **LTAP** | New | Data architecture (eliminates ETL) |
| **Lakehouse//RT** | New | Real-time analytics (<100ms queries) |

---

## Genie One: The Business-User Coworker

Genie One is described by Databricks as "an agentic coworker that helps business teams automate and orchestrate their work across any data — structured or unstructured, analytical or operational, inside or outside Databricks."

It covers tasks that previously required a data team to fulfill: answering ad-hoc data questions, producing reports, managing alerts, scheduling tasks, and executing actions through MCP tools. Native integrations ship for **Google Drive, Jira, Slack, Confluence, and SharePoint** — the everyday enterprise SaaS stack.

The key differentiator Databricks is making: Genie One can act on business context it has learned, not just data you give it in the prompt.

### Genie Ontology: The Context Layer Behind It

The Genie Ontology is the knowledge layer that powers accurate responses in Genie One and the broader suite. Databricks describes it as "a self-improving context layer" that:

- Automatically extracts knowledge from Databricks and connected workplace apps
- Sources from: data (tables, columns, lineage), documents, tags, content, apps, tickets, chats, meetings, and people
- Continuously updates as the business changes
- Propagates context to all Genie products in the workspace

The problem this solves is well-known in enterprise AI: LLMs produce generic outputs when they don't understand the business — column names, internal taxonomies, business logic, org structure. The Ontology is Databricks' bet that you can automate that context extraction rather than requiring hand-tuned system prompts.

Agent Bricks builds on this: the platform reports **70% higher accuracy than standard RAG** and a **30% improvement in multi-step workflows** when Unity Catalog metadata is used to inform agent reasoning. The Ontology is the mechanism.

---

## Genie Code: GA with MCP Integration

**Genie Code** (formerly Databricks Assistant) is the AI coding and data assistant that runs throughout the Databricks workspace — in notebooks, the SQL editor, Lakeflow Pipelines Editor, AI/BI dashboards, and MLflow. It's now generally available.

It runs in two modes:

- **Chat mode**: Conversational code help, explanations, debugging
- **Agent mode**: Autonomously executes multi-step workflows — exploratory data analysis, pipeline creation, dashboard generation

### MCP Servers in Agent Mode

The most significant technical addition is MCP server integration — available in Agent mode only, not Chat mode.

Genie Code acts as the MCP host. Three categories of servers are supported:

| Type | Examples | Setup |
|---|---|---|
| **Managed** | Unity Catalog Functions, Vector Search, Genie Space, Databricks SQL | No setup — add from settings |
| **External** | GitHub, Google Drive, SharePoint, Glean, Atlassian, Slack | Add from Marketplace; per-user OAuth |
| **Custom** | Your own tools | Deploy as a Databricks App in the same workspace |

**Setup steps (Agent mode):**

1. Open Genie Code settings via the gear icon
2. Navigate to "MCP Servers"
3. Click "+ Add Server"
4. Select type: Unity Catalog function / Vector search index / Genie space / Unity Catalog connection / Databricks App
5. Authenticate if prompted (external servers require per-user OAuth)
6. Save

### Key Constraints

- **Agent mode only**: MCP is not available in Chat mode
- **20-tool maximum**: Across all connected MCP servers combined — plan your server selection accordingly
- **Same-workspace**: Custom MCP servers must deploy as Databricks Apps in your workspace (not external URLs)
- **Stateless**: Custom servers must be built with `mcp_server.http_app(stateless_http=True)`
- **Streamable HTTP**: External servers must use Streamable HTTP transport (not stdio)

The custom MCP server endpoint format: `https://<server-url>/mcp`

For teams wanting to expose Databricks Genie capabilities to external agents, a community project — [databricks-genie-mcp](https://github.com/alexxx-db/databricks-genie-mcp) — has implemented an MCP server that wraps the Genie API, making it queryable from Claude Code, Cursor, and other MCP-compatible clients.

---

## Genie Agents + Genie App Builder

**Genie Agents** let teams create reusable agents within the Databricks workspace, connected to their data with Unity Catalog access controls, permissions, and cost governance built in. These are agent definitions — not the same as one-off prompts. You build them once; other users or workflows invoke them.

**Genie App Builder** is the companion tool for building business apps on top of Genie Agents. Databricks describes this as "vibe coding business apps" — the App Builder generates an application based on natural language description of what the app should do, grounded in your Lakehouse data.

The underlying runtime is **Databricks Apps** — a managed application hosting layer that handles credentials, permissions, and connection details automatically. App configuration is defined in an `app.yaml` file specifying how the app runs, what environment variables it needs, and what platform resources it connects to.

Both are governed by Unity Catalog — access controls, audit trails, and cost tracking apply automatically.

---

## Agent Bricks: The Developer Platform

Agent Bricks is Databricks' platform for developers building enterprise agents. It's been available for a year; DAIS 2026 expanded it significantly.

Key metrics at the announcement: **100,000+ agents built** on Agent Bricks; Databricks processing **1+ quadrillion tokens per year** from agent workloads.

### What Agent Bricks Covers

Databricks frames the core agent loop as 1% of the work. The other 99% is what they call "hidden technical debt of agentic systems": token capacity, deployment, security, evaluation, monitoring, context, and sharing. Agent Bricks is positioned to handle that 99%.

### SDK Support

Agent Bricks now explicitly supports any agent harness:

- **Open-source frameworks**: LangGraph, Agno, CrewAI
- **Commercial SDKs**: Claude Code SDK (Anthropic), OpenAI Agent SDK

This is meaningful: Anthropic's Claude Code SDK is now a first-class deployment target on Databricks. You can build Claude-orchestrated agents and deploy them with autoscaling to Databricks Apps within the governed Agent Bricks platform.

### MCP on Agent Bricks

Agent Bricks natively supports MCP — giving deployed agents secure access to APIs, databases, and SaaS applications. Services authenticate through Unity Catalog using centrally managed credentials and audit trails. You define the MCP connections once at the workspace level; agents inherit access per their Unity Catalog permissions.

### Deployment

Agents deploy to **Databricks Apps** with horizontal autoscaling. The platform handles infrastructure; you write agent logic.

---

## Unity AI Gateway

A new governance layer for enterprise AI, Unity AI Gateway provides:

- **Centralized credential management** for all AI services and MCP connections
- **Audit trails** for agent actions across the workspace
- **Cost governance**: per-user and per-application AI spend tracking
- **Access controls**: Unity Catalog permissions propagate to agent capabilities

This is the enterprise compliance story that has been missing from most agent platforms. The 20-tool limit in Genie Code is a constraint; Unity AI Gateway is a feature for teams where access control and auditability matter.

---

## LTAP and Lakehouse//RT

Two infrastructure announcements are worth knowing about even if they aren't directly builder-relevant today:

**LTAP (Lake Transactional/Analytical Processing)**: A new data architecture that eliminates ETL between operational and analytical workloads. Instead of maintaining separate OLTP and OLAP systems with sync pipelines, LTAP allows the Lakehouse to serve both. The implication for agentic builders: agents that need to act on operational data (not just analyze historical data) don't need to wait for pipeline schedules.

**Lakehouse//RT**: A real-time analytics engine with sub-100ms query latency at scale. Relevant for agents that need low-latency access to aggregated data to drive decisions.

Neither has detailed builder documentation available yet.

---

## Genie ZeroOps (Private Preview)

Announced as entering private preview post-summit. Framed as operations automation — the details are sparse. If you're interested, Databricks' site has early access sign-up.

---

## Pricing

Databricks is moving to a consumption model for Genie products: **up to $10 per user per month in AI credits at no seat-based cost**, paying only for actual AI consumption.

This is a significant departure from seat licensing. For teams with uneven usage — some power users, many occasional users — consumption-based pricing reduces cost. For teams with heavy, predictable usage, it may cost more than a seat model. The $10/user credit provides a buffer before usage charges begin.

---

## Builder Decision Map

| Scenario | Recommendation |
|---|---|
| Business users need data answers without analyst help | Genie One — native integration, no-code |
| Developers need agentic coding/pipeline help in the workspace | Genie Code (Agent mode) |
| Need to connect internal tools to Genie Code | Custom MCP server as Databricks App |
| Need to connect external SaaS (Slack, Jira, GDrive) | External MCP server via Marketplace |
| Building reusable enterprise agents with governance | Agent Bricks + Claude Code SDK or LangGraph |
| Need to expose Databricks Genie to external Claude agents | [databricks-genie-mcp](https://github.com/alexxx-db/databricks-genie-mcp) wrapper |
| Need enterprise compliance (audit trails, SSO, cost caps) | Unity AI Gateway — baked into Agent Bricks |

---

## What This Means for Builders

**The platform play is tightening.** Genie One, Genie Code, Genie Agents, and Agent Bricks all route through Unity Catalog. That's intentional — governance is the competitive moat Databricks is building around the AI layer, not just the data layer.

**Claude Code SDK is now a first-class citizen on Databricks.** If you're building Claude-orchestrated agents and your data lives on Databricks, Agent Bricks is a viable deployment target with autoscaling and Unity Catalog credentials management handled for you.

**The 20-tool MCP limit in Genie Code is a real constraint.** Plan your server configurations carefully — Managed servers are free to add and don't eat into your limit in the same way as external connections. (Confirm current limits in [Databricks docs](https://docs.databricks.com/aws/en/genie-code/mcp) as this may change.)

**Genie Ontology is the long bet.** The self-improving context layer is the differentiated part of this stack — if it works as described, it solves a problem that most enterprise AI implementations paper over with expensive prompt engineering. The 70%/30% accuracy claims are relative to standard RAG, not external baselines.

DAIS Day 3 is June 18. Watch for GA dates and availability details for Genie ZeroOps and the mobile apps (iOS/Android).

---

## Sources

- [Databricks: Introducing Genie One, Genie Agents, and Genie Ontology](https://www.databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents) — Official blog post
- [Databricks: Genie One Press Release](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team) — Newsroom
- [Databricks: Agent Bricks at DAIS 2026](https://www.databricks.com/blog/agent-bricks-dais-2026) — Developer platform expansion
- [Databricks Docs: Connect Genie Code to MCP servers](https://docs.databricks.com/aws/en/genie-code/mcp) — Official MCP setup guide
- [Data Reply IT: Connecting Genie Code to MCP Servers](https://medium.com/data-reply-it-datatech/connecting-genie-code-to-mcp-servers-extending-databricks-ai-with-external-tools-and-data-cb2792802ca8) — Technical walkthrough
- [Enterprise AI World: Genie Product Suite Expansion](https://www.enterpriseaiworld.com/Articles/News/News/Databricks-Expands-Genie-Product-Suite%C2%A0to-Empower-Teams-to-Build-Reusable-Agents-and-Vibe-Code-Business-Apps-175256.aspx) — Feature details
- [GitHub: databricks-genie-mcp](https://github.com/alexxx-db/databricks-genie-mcp) — Community MCP server for Genie API

---

*Related on ChatForest: [Databricks Lakehouse Platform Review](/reviews/databricks-lakehouse-platform-ai-data/) | [Amazon Bedrock AgentCore Runtime Guide](/builders-log/amazon-bedrock-agentcore-runtime-harness-builder-guide/) | [Anthropic Claude Platform on AWS](/builders-log/claude-platform-aws-iam-auth-bedrock-vs-native-builder-guide/) | [Agent Control Standard (ACS)](/builders-log/agent-control-standard-acs-runtime-governance-ai-agents-builder-guide/)*
