# Databricks DAIS 2026: Genie One, Agent Bricks, and What Builders Need to Know

> At DAIS 2026, Databricks shipped Genie One (agentic coworker for business teams), expanded Agent Bricks to support Claude Code SDK and LangGraph, made Genie Code GA with MCP server integration, and announced Unity AI Gateway for enterprise governance. Here is the complete builder's guide.


At the [Data + AI Summit](https://www.databricks.com/company/newsroom/press-releases/databricks-announces-2026-data-ai-summit-keynote-lineup-and) on June 16, 2026, Databricks announced a stack of products under a unified "Genie" brand: **Genie One** (an agentic coworker for business teams), **Genie Code** (now GA, with MCP server integration), **Genie Agents + Genie App Builder** (tooling to build reusable agents), and **Genie ZeroOps** (private preview). ([Databricks: Genie One press release](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team)) The Developer platform — **Agent Bricks** — was expanded to support the Claude Code SDK, LangGraph, Agno, CrewAI, and OpenAI Agent SDKs, with horizontal autoscaling through Databricks Apps. ([Databricks: Agent Bricks at DAIS 2026](https://www.databricks.com/blog/agent-bricks-dais-2026))

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

Genie One is described by Databricks as "an all-new agentic coworker that helps business teams automate and orchestrate their work across any data — structured or unstructured, analytical or operational, inside or outside Databricks." ([Databricks: Genie One press release](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team))

It covers tasks that previously required a data team to fulfill: answering ad-hoc data questions, producing reports, managing alerts, scheduling tasks, and executing actions through MCP tools. Native integrations ship for **Google Drive, Jira, Slack, Confluence, and SharePoint**, plus 50+ additional connected apps — the everyday enterprise SaaS stack. ([Databricks: Genie One press release](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team))

The key differentiator Databricks is making: Genie One can act on business context it has learned, not just data you give it in the prompt.

### Genie Ontology: The Context Layer Behind It

The Genie Ontology is the knowledge layer that powers accurate responses in Genie One and the broader suite. Databricks describes it as "a new self-improving context layer that solves one of enterprise AI's hardest problems." ([Databricks: Genie One press release](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team)) Per Databricks, the Ontology:

- Automatically extracts and continuously updates business knowledge from Databricks and connected workplace apps
- Sources from: data, documents, tags, content, apps, tickets, chats, meetings, and people ([Databricks: Genie One press release](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team))
- Continuously updates as the business changes
- Propagates context to all Genie products in the workspace

The problem this solves is well-known in enterprise AI: LLMs produce generic outputs when they don't understand the business — column names, internal taxonomies, business logic, org structure. The Ontology is Databricks' bet that you can automate that context extraction rather than requiring hand-tuned system prompts.

Agent Bricks separately reports **70% higher accuracy than standard RAG** and a **30% improvement in multi-step workflows** when agents use Unity Catalog business context — schema, business definitions, lineage, permissions, and data quality signals — instead of raw retrieval. ([Databricks: Agent Bricks — the governed enterprise agent platform](https://www.databricks.com/blog/agent-bricks-governed-enterprise-agent-platform)) The Ontology is a related mechanism for the same underlying idea: grounding agents in governed metadata rather than raw unstructured retrieval.

---

## Genie Code: GA with MCP Integration

**Genie Code** (formerly Databricks Assistant) is the AI coding and data assistant that runs throughout the Databricks workspace — in notebooks, the SQL editor, the Lakeflow Pipelines Editor, AI/BI dashboards, and MLflow. ([Databricks docs: Genie Code](https://docs.databricks.com/aws/en/genie-code/)) It's now generally available. ([Databricks: Genie One press release](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team))

At DAIS 2026 it ran in two modes:

- **Chat mode**: Conversational code help, explanations, debugging
- **Agent mode**: Autonomously executes multi-step workflows — exploratory data analysis, pipeline creation, dashboard generation

**Update (post-DAIS):** Databricks' June 2026 platform release notes state the Chat/Agent mode selector has since been removed from the Genie Code pane and that "Genie Code now runs exclusively in Agent mode" — so the mode distinction described below no longer applies to the current product, though it was accurate as announced at DAIS. ([Databricks release notes, June 2026](https://docs.databricks.com/aws/en/release-notes/product/2026/june))

### MCP Servers in Agent Mode

The most significant technical addition at DAIS was MCP server integration — available in Agent mode only, not Chat mode, at announcement. (As noted above, Databricks has since removed the mode selector; see the Update note.) ([Data Reply IT: Connecting Genie Code to MCP Servers](https://medium.com/data-reply-it-datatech/connecting-genie-code-to-mcp-servers-extending-databricks-ai-with-external-tools-and-data-cb2792802ca8))

Genie Code acts as the MCP host. **Update (2026-08-22):** Databricks has since restructured this into native third-party connectors plus a manual "Add Server" flow with its own categories — the table below reflects the current docs, not the DAIS-day naming (which used "Vector Search," "Genie Space," and "Databricks SQL" as managed-type labels; those are now "AI Search," "Genie Agent," and no longer listed, respectively).

| Type | Examples | Setup |
|---|---|---|
| **Native connectors** | Google Drive, SharePoint, GitHub, Glean, Atlassian, Slack | Built-in; per-user OAuth. Each has its own limits (e.g. Google Drive/SharePoint cap file size at 10MB and support only native Office/Workspace formats) |
| **Managed (workspace)** | Unity Catalog function, AI Search index, Genie Agent | Add manually from Genie Code settings — no external auth |
| **External** | A Unity Catalog connection exposed as an MCP server | Add manually; select the UC connection |
| **Custom** | Your own tools | Deploy as a Databricks App in the same workspace |

([Databricks docs: Connect Genie Code to MCP servers](https://docs.databricks.com/aws/en/genie-code/mcp), current as of 2026-08-22)

**Setup steps (current, per Databricks docs):**

1. Open Genie Code settings (gear icon → Settings)
2. Under "MCP Servers," click "Add Server"
3. Select the MCP servers you want to add
4. Click Save

([Databricks docs: Connect Genie Code to MCP servers](https://docs.databricks.com/aws/en/genie-code/mcp))

### Key Constraints

- **Agent mode only** (at DAIS announcement): MCP was not available in Chat mode
- **20-tool maximum**: Across all connected MCP servers combined — plan your server selection accordingly
- **Same-workspace**: Custom MCP servers must deploy as Databricks Apps in your workspace (not external URLs) ([Databricks docs: Connect Genie Code to MCP servers](https://docs.databricks.com/aws/en/genie-code/mcp))
- **Stateless**: Custom servers must be built with `mcp_server.http_app(stateless_http=True)` ([Databricks docs: Connect Genie Code to MCP servers](https://docs.databricks.com/aws/en/genie-code/mcp))
- **Streamable HTTP**: External servers must use Streamable HTTP transport (not stdio)

([Data Reply IT: Connecting Genie Code to MCP Servers](https://medium.com/data-reply-it-datatech/connecting-genie-code-to-mcp-servers-extending-databricks-ai-with-external-tools-and-data-cb2792802ca8) — the 20-tool limit and Streamable HTTP requirement are documented in this technical walkthrough; Databricks' own docs page confirms the same-workspace and stateless requirements but does not spell out the tool cap or transport requirement in as much detail)

The custom MCP server endpoint format: `https://<server-url>/mcp` ([Databricks docs: Connect Genie Code to MCP servers](https://docs.databricks.com/aws/en/genie-code/mcp))

For teams wanting to expose Databricks Genie capabilities to external agents, a community project — [databricks-genie-mcp](https://github.com/alexxx-db/databricks-genie-mcp) — has implemented an MCP server that wraps the Genie API. Its README documents setup for **Claude Desktop** specifically; because it implements the standard MCP protocol, other MCP-compatible clients should work in principle, but the project doesn't document or claim support for them, so treat that as unverified. This is a third-party, community-maintained tool, not a Databricks product.

---

## Genie Agents + Genie App Builder

**Genie Agents** let teams create reusable agents within the Databricks workspace, "connected to their data with access controls, permissions, and cost governance built in." ([Enterprise AI World: Genie Product Suite Expansion](https://www.enterpriseaiworld.com/Articles/News/News/Databricks-Expands-Genie-Product-Suite%C2%A0to-Empower-Teams-to-Build-Reusable-Agents-and-Vibe-Code-Business-Apps-175256.aspx)) These are agent definitions — not the same as one-off prompts. You build them once; other users or workflows invoke them.

**Genie App Builder** is the companion tool for building business apps on top of Genie Agents. Databricks describes it as "a fully managed vibe coding environment built for the enterprise" ([Databricks: Genie One press release](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team)) — the App Builder generates an application based on natural language description of what the app should do, grounded in your Lakehouse data.

The underlying runtime is **Databricks Apps** — a managed application hosting layer that handles credentials, permissions, and connection details automatically. App configuration is defined in an `app.yaml` file specifying how the app runs, what environment variables it needs, and what platform resources it connects to. ([Databricks developer docs: App configuration](https://developers.databricks.com/docs/apps/configuration))

Both are governed by Unity Catalog — access controls, audit trails, and cost tracking apply automatically.

---

## Agent Bricks: The Developer Platform

Agent Bricks is Databricks' platform for developers building enterprise agents, introduced at DAIS 2025 on June 11, 2025 ([Databricks: Introducing Agent Bricks](https://www.databricks.com/blog/introducing-agent-bricks)); DAIS 2026 expanded it significantly.

Key metrics at the DAIS 2026 announcement: "over 100k+ agents have been built, and we are now processing 1+ quadrillion tokens per year of agents" since Agent Bricks' 2025 launch. ([Databricks: Agent Bricks at DAIS 2026](https://www.databricks.com/blog/agent-bricks-dais-2026))

### What Agent Bricks Covers

Databricks frames the core agent loop as 1% of the work. The other 99% is what they call "hidden technical debt of agentic systems": token capacity, deployment, security, evaluation, monitoring, context, and sharing. Agent Bricks is positioned to handle that 99%.

### SDK Support

Agent Bricks now explicitly supports any agent harness: "from open-source frameworks such as LangGraph, Agno, CrewAI to harnesses such as Claude Code SDK or OpenAI Agent SDKs." ([Databricks: Agent Bricks at DAIS 2026](https://www.databricks.com/blog/agent-bricks-dais-2026))

- **Open-source frameworks**: LangGraph, Agno, CrewAI
- **Commercial SDKs**: Claude Code SDK (Anthropic), OpenAI Agent SDK

This is meaningful: Anthropic's Claude Code SDK is now a first-class deployment target on Databricks. You can build Claude-orchestrated agents and deploy them with autoscaling to Databricks Apps within the governed Agent Bricks platform.

### MCP on Agent Bricks

Agent Bricks natively supports MCP: "by adding MCP support to Unity Catalog, agents in Agent Bricks can securely connect to external data sources such as Google Drive, JIRA, Slack, Github, and more." ([Databricks: Agent Bricks at DAIS 2026](https://www.databricks.com/blog/agent-bricks-dais-2026)) You define the MCP connections once at the workspace level; agents inherit access per their Unity Catalog permissions.

### Deployment

Agents deploy to **Databricks Apps** with horizontal autoscaling. The platform handles infrastructure; you write agent logic.

---

## Unity AI Gateway

A new governance layer for enterprise AI, Unity AI Gateway provides:

- **Centralized credential and connection management** for AI services and MCP connections — admins govern foundation model and MCP access through Unity Catalog using the same fine-grained policies used for data
- **Audit trails**: admins can "enforce runtime controls with contextual policies" that apply "based on the user, agent, model, MCP service, tool being invoked, or the contents of the request and response," and gateway traces feed into Lakewatch to "detect suspicious activity, investigate policy violations, and accelerate AI security investigations"
- **Cost governance**: teams can "analyze AI spend and set budgets by user, team, tool, and use case"
- **Access controls**: Unity Catalog permissions propagate to agent capabilities

([Databricks: AI governance at Data + AI Summit 2026 — what's new with Unity AI Gateway](https://www.databricks.com/blog/ai-governance-data-ai-summit-2026-whats-new-unity-ai-gateway))

This is the enterprise compliance story that has been missing from most agent platforms. The 20-tool limit in Genie Code is a constraint; Unity AI Gateway is a feature for teams where access control and auditability matter.

---

## LTAP and Lakehouse//RT

Two infrastructure announcements are worth knowing about even if they aren't directly builder-relevant today:

**LTAP (Lake Transactional/Analytical Processing)**: A new data architecture that eliminates ETL between operational and analytical workloads — "there are no pipelines synchronizing operational and analytical stores, replicas to maintain, or connectors moving data between systems." ([Databricks: Launches LTAP, first Lake Transactional/Analytical Processing architecture](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-ltap-first-lake-transactionalanalytical)) Databricks describes it as "coming soon as a part of Lakebase" — as of this update (2026-08-22) it is still pre-release, not GA. Instead of maintaining separate OLTP and OLAP systems with sync pipelines, LTAP allows the Lakehouse to serve both. The implication for agentic builders: agents that need to act on operational data (not just analyze historical data) don't need to wait for pipeline schedules.

**Lakehouse//RT**: A real-time analytics engine delivering "sub-100 millisecond latency at 12,000 queries per second," with response times as low as 10ms on smaller datasets. ([Databricks: Launches Lakehouse//RT](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-lakehousert-bring-real-time-analytics-directly)) Relevant for agents that need low-latency access to aggregated data to drive decisions. It's currently in Beta.

Neither has detailed builder documentation available yet.

---

## Genie ZeroOps (Private Preview)

Genie ZeroOps is a background agent that monitors production data/AI assets (pipelines, jobs, tables, ML models), investigates failures using platform lineage and telemetry, and proposes fixes tested in a sandbox before reaching production. Databricks announced it is "entering private preview in the coming weeks, starting with support for jobs, pipelines, tables and ML workloads." ([Databricks: Introducing Genie ZeroOps](https://www.databricks.com/blog/introducing-genie-zeroops)) If you're interested, Databricks' site has early access sign-up.

---

## Pricing

At DAIS announcement, Databricks described a consumption model for Genie products with **$10 of free monthly AI usage per user**, paying only for actual AI consumption beyond that. ([Databricks: Genie One press release](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team))

**Update (2026-08-22) — this has since changed twice:**

- **Since July 8, 2026**, Genie products (Genie One, Genie Agents, Genie Code) moved to a formal pay-as-you-go model: each user (excluding service principals) gets **150 Databricks Units (DBUs) of free LLM usage per month**, worth about $10.50 in the US East region, before usage-based billing kicks in. ([Databricks release notes, July 2026](https://docs.databricks.com/aws/en/release-notes/product/2026/july))
- **Since July 15, 2026**, Databricks paused billing for **Genie One and Genie Agents specifically** — usage by users (again excluding service principals) is **free through January 31, 2027**, plus a 25% discount on any billed Genie usage during that promotional window. **Genie Code is not included in this pause** and continues to bill under the pay-as-you-go model above. ([Databricks docs: Monitor and understand your Genie cost](https://docs.databricks.com/aws/en/genie/monitor-cost))

Net effect for builders as of this writing: Genie One and Genie Agents are effectively free to try through January 2027; Genie Code usage is metered from the first DBU past the 150/user monthly allowance. Confirm current terms before budgeting, since this has already shifted twice since the DAIS announcement.

---

## Builder Decision Map

| Scenario | Recommendation |
|---|---|
| Business users need data answers without analyst help | Genie One — native integration, no-code |
| Developers need agentic coding/pipeline help in the workspace | Genie Code (Agent mode) |
| Need to connect internal tools to Genie Code | Custom MCP server as Databricks App |
| Need to connect external SaaS (Slack, Jira, GDrive) | External MCP server via Marketplace |
| Building reusable enterprise agents with governance | Agent Bricks + Claude Code SDK or LangGraph |
| Need to expose Databricks Genie to Claude Desktop | [databricks-genie-mcp](https://github.com/alexxx-db/databricks-genie-mcp) wrapper (community, unofficial) |
| Need enterprise compliance (audit trails, SSO, cost caps) | Unity AI Gateway — baked into Agent Bricks |

---

## What This Means for Builders

**The platform play is tightening.** Genie One, Genie Code, Genie Agents, and Agent Bricks all route through Unity Catalog. That's intentional — governance is the competitive moat Databricks is building around the AI layer, not just the data layer.

**Claude Code SDK is now a first-class citizen on Databricks.** If you're building Claude-orchestrated agents and your data lives on Databricks, Agent Bricks is a viable deployment target with autoscaling and Unity Catalog credentials management handled for you.

**The 20-tool MCP limit in Genie Code is a real constraint.** Plan your server configurations carefully — Managed servers are free to add and don't eat into your limit in the same way as external connections. (Confirm current limits in [Databricks docs](https://docs.databricks.com/aws/en/genie-code/mcp) as this may change.)

**Genie Ontology is the long bet.** The self-improving context layer is the differentiated part of this stack — if it works as described, it solves a problem that most enterprise AI implementations paper over with expensive prompt engineering. The 70%/30% accuracy claims are relative to standard RAG, not external baselines.

The Data + AI Summit runs through June 18, 2026. ([Databricks: 2026 Data + AI Summit keynote lineup](https://www.databricks.com/company/newsroom/press-releases/databricks-announces-2026-data-ai-summit-keynote-lineup-and)) Watch for GA dates and availability details for Genie ZeroOps and the mobile apps (iOS/Android).

---

## Sources

- [Databricks: Introducing Genie One, Genie Agents, and Genie Ontology](https://www.databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents) — Official blog post
- [Databricks: Genie One Press Release](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team) — Newsroom
- [Databricks: Agent Bricks at DAIS 2026](https://www.databricks.com/blog/agent-bricks-dais-2026) — Developer platform expansion
- [Databricks: Introducing Agent Bricks (2025 launch)](https://www.databricks.com/blog/introducing-agent-bricks) — Original announcement, June 11, 2025
- [Databricks: Agent Bricks — the governed enterprise agent platform](https://www.databricks.com/blog/agent-bricks-governed-enterprise-agent-platform) — Source of the 70%/30% accuracy stats
- [Databricks Docs: Genie Code](https://docs.databricks.com/aws/en/genie-code/) — Product overview
- [Databricks Docs: Connect Genie Code to MCP servers](https://docs.databricks.com/aws/en/genie-code/mcp) — Official MCP setup guide
- [Databricks release notes, June 2026](https://docs.databricks.com/aws/en/release-notes/product/2026/june) — Chat/Agent mode merger
- [Databricks release notes, July 2026](https://docs.databricks.com/aws/en/release-notes/product/2026/july) — Pay-as-you-go pricing shift (July 8, 2026)
- [Databricks docs: Monitor and understand your Genie cost](https://docs.databricks.com/aws/en/genie/monitor-cost) — Current Genie One/Agents/Code billing status
- [Data Reply IT: Connecting Genie Code to MCP Servers](https://medium.com/data-reply-it-datatech/connecting-genie-code-to-mcp-servers-extending-databricks-ai-with-external-tools-and-data-cb2792802ca8) — Technical walkthrough (20-tool limit, Streamable HTTP)
- [Enterprise AI World: Genie Product Suite Expansion](https://www.enterpriseaiworld.com/Articles/News/News/Databricks-Expands-Genie-Product-Suite%C2%A0to-Empower-Teams-to-Build-Reusable-Agents-and-Vibe-Code-Business-Apps-175256.aspx) — Feature details
- [Databricks: AI governance at DAIS 2026 — Unity AI Gateway](https://www.databricks.com/blog/ai-governance-data-ai-summit-2026-whats-new-unity-ai-gateway) — Governance feature details
- [Databricks: Launches LTAP](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-ltap-first-lake-transactionalanalytical) — Newsroom
- [Databricks: Launches Lakehouse//RT](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-lakehousert-bring-real-time-analytics-directly) — Newsroom
- [Databricks: Introducing Genie ZeroOps](https://www.databricks.com/blog/introducing-genie-zeroops) — Official blog post
- [Databricks: 2026 Data + AI Summit keynote lineup](https://www.databricks.com/company/newsroom/press-releases/databricks-announces-2026-data-ai-summit-keynote-lineup-and) — Summit dates (June 15-18, 2026)
- [Databricks developer docs: App configuration](https://developers.databricks.com/docs/apps/configuration) — `app.yaml` reference
- [GitHub: databricks-genie-mcp](https://github.com/alexxx-db/databricks-genie-mcp) — Community MCP server for Genie API

---

*Related on ChatForest: [Databricks Lakehouse Platform Review](/reviews/databricks-lakehouse-platform-ai-data/) | [Amazon Bedrock AgentCore Runtime Guide](/builders-log/amazon-bedrock-agentcore-runtime-harness-builder-guide/) | [Anthropic Claude Platform on AWS](/builders-log/claude-platform-aws-iam-auth-bedrock-vs-native-builder-guide/) | [Agent Control Standard (ACS)](/builders-log/agent-control-standard-acs-runtime-governance-ai-agents-builder-guide/)*

