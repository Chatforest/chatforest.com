---
title: "AWS AgentCore + Databricks: The Enterprise AI Stack Integration Announced at DAIS 2026"
date: 2026-06-16
description: "At Databricks Data + AI Summit 2026, AWS and Databricks formalized a joint enterprise agent architecture: AgentCore handles the agent runtime (microVMs, memory, identity, MCP gateway), Databricks handles data governance (Unity Catalog, Unity AI Gateway, Genie Spaces). Here's the technical architecture and builder decision tree."
og_description: "AgentCore agents now have a formal integration path to Unity Catalog-governed data via Databricks Apps and Genie Spaces. The governance boundary is MCP. Here's what that means for enterprise builders."
content_type: "Builder's Log"
categories: ["AWS", "Databricks", "Agent Infrastructure", "Enterprise AI"]
tags: ["aws", "amazon", "bedrock", "agentcore", "databricks", "unity-catalog", "mcp", "genie-spaces", "lakebase", "enterprise", "agents", "dais-2026", "data-governance", "production-ai"]
sources_audited: 2026-07-30
---

AWS and Databricks have been partners for years, sharing enterprise customers who store data in Databricks and run compute on AWS. At the [Databricks Data + AI Summit (DAIS) 2026](https://www.databricks.com/dataaisummit) — running June 15–18 at Moscone Center in San Francisco — they made the agentic layer of that partnership explicit.

The announcement: AgentCore agents now have a supported, governed path to Unity Catalog data via Databricks Apps and Genie Spaces, with MCP as the integration boundary and Unity Catalog handling all access control, [per the joint AWS/Databricks DAIS 2026 announcement](https://www.databricks.com/blog/aws-and-databricks-data-ai-summit-2026-accelerating-real-world-ai-innovation).

This is not a new product. Both [AgentCore (GA October 2025)](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available) and [Databricks Managed MCP](https://www.databricks.com/en/blog/announcing-managed-mcp-servers-unity-catalog-and-mosaic-ai-integration) (public preview, January 2026) existed independently. What DAIS 2026 formalized was the architecture showing how they work together — and validated it with real customers at scale.

---

## What Each Layer Does

Before looking at the integration, a quick orientation on each component:

**Amazon Bedrock AgentCore** is AWS's managed agent infrastructure layer. It sits between your agent code and AWS compute, handling:

- **Session isolation**: each user session runs in a [dedicated Firecracker microVM](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html) (same isolation model as Lambda). Sessions can't see each other's state.
- **Duration**: [up to 8 hours per session](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html), vs [Lambda's 15-minute execution ceiling](https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html).
- **Memory management**: [short-term (turn-by-turn), long-term (cross-session), and built-in strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) (summarization, semantic facts, user preferences).
- **Tool gateway (MCP)**: [AgentCore Gateway transforms existing APIs and Lambda functions into MCP-compatible tools](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/). Agents talk to one gateway endpoint; routing and auth are managed.
- **Identity**: [OAuth 2.0 / OIDC with JWT validation at runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-authentication.html). Integrates with Okta, Entra, Amazon Cognito.
- **Framework-agnostic**: [LangGraph, CrewAI, LlamaIndex, Strands, or custom code](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) — AgentCore runs all of them.

AgentCore is not a framework and not Bedrock Agents. Bedrock Agents is a higher-level config-driven orchestration service built on top of AgentCore. Use AgentCore when you need more control, more flexibility, or a non-Amazon model provider.

**Databricks Unity Catalog** is the [data governance layer for the Databricks platform](https://docs.databricks.com/aws/en/data-governance/unity-catalog/) — controlling who can access which tables, functions, and ML models, with full audit logging. If you're on Databricks, Unity Catalog is how you enforce data access policies across users and service principals.

**Unity AI Gateway** ([announced April 15, 2026](https://www.databricks.com/blog/ai-gateway-governance-layer-agentic-ai)) is Databricks' MCP governance layer: a central control plane that governs all AI interactions across an organization, including model calls, tool invocations, and agent actions. It extends Unity Catalog's existing governance model — the same permissions, auditing, and policy controls — to agentic AI traffic.

**Genie Spaces** (renamed **Genie Agents** in 2026 documentation) are curated collections of [up to 30 Unity Catalog tables](https://docs.databricks.com/aws/en/genie/best-practices) that agents can query in natural language (the limit was raised from 25 to 30 in a February 2026 release, before DAIS 2026). Genie translates the agent's question into SQL, executes against the warehouse, and returns results — with Unity Catalog permissions enforced per requesting user. Genie Spaces are for structured data only (tables, not PDFs or documents).

**Lakebase** is Databricks' [managed Postgres-compatible OLTP service](https://www.databricks.com/blog/databricks-lakebase-generally-available), designed for low-latency reads/writes; it reached general availability on AWS on February 3, 2026. At DAIS 2026, it was positioned specifically as the agent state store in multi-turn conversations — complementing AgentCore Memory for teams that want SQL-level control over conversation context.

---

## The Integration Architecture

The data path from AgentCore agent to Unity Catalog looks like this:

```
AgentCore Agent
    ↓ MCP tool call
AgentCore Gateway (MCP endpoint)
    ↓ routes to registered Databricks tool
Databricks Apps (hosts MCP gateway)
    ↓ query
Unity AI Gateway (governance check)
    ↓ access control
Unity Catalog (table permissions)
    ↓ SQL execution
Delta Lake / SQL Warehouse
    ↑ governed results
```

The key design decision: agents don't query Unity Catalog directly. They ask questions of **Genie Spaces**, which are scoped collections of tables that already have access policies defined. This constraint limits the blast radius of agent queries — an agent can only see what its Genie Space was configured to expose.

Auth flows through existing Databricks identity. [The MCP connection uses managed OAuth; Databricks stores credentials and handles token refresh, so the agent never sees them](https://docs.databricks.com/aws/en/generative-ai/mcp/managed-mcp). Unity Catalog applies per-user permissions, so a request from User A might return different rows than the same request from User B, even from the same agent.

For agent state storage in long-running conversations, teams can use **Lakebase** (managed Postgres) alongside AgentCore Memory. Lakebase gives you SQL semantics and explicit control over what state is persisted; AgentCore Memory gives you semantic retrieval across sessions. Most enterprise use cases will use both.

---

## What Was Net-New at DAIS 2026

The core components existed before. What DAIS 2026 added:

1. **Formalized integration path**: AWS and Databricks jointly demonstrated and documented the AgentCore → Databricks Apps → Unity Catalog path. Before DAIS, teams were connecting these systems ad hoc; now there's a reference architecture.

2. **Live demos at [AWS Booth #100](https://www.databricks.com/blog/aws-and-databricks-data-ai-summit-2026-accelerating-real-world-ai-innovation)**: Joint demos showing AgentCore agents querying Unity Catalog-governed data via Genie Spaces, with Lakebase handling agent state.

3. **Customer presence at scale**: [Addepar (managing nearly $9 trillion in assets)](https://databricks.com/blog/how-addepar-scales-investment-workflows-databricks-ai-agents), [Talkdesk](https://www.databricks.com/customers/talkdesk/aws), [Mastercard](https://aws.amazon.com/blogs/big-data/access-databricks-unity-catalog-data-using-catalog-federation-in-the-aws-glue-data-catalog/), nCino, and Workday were all named in AWS and Databricks' own DAIS 2026 coverage as running Databricks-on-AWS workloads — not just in sandbox environments. (Mastercard's specific DAIS 2026 demo was catalog federation between Unity Catalog and AWS Glue, not the AgentCore agent path described above.)

4. **Explicit MCP positioning**: The DAIS announcement positioned MCP as the governance boundary between AWS agent infrastructure and Databricks data. This matters for teams building multi-vendor agent stacks — MCP means neither vendor owns the integration protocol.

---

## Customer Examples

**[Addepar](https://databricks.com/blog/how-addepar-scales-investment-workflows-databricks-ai-agents)** (investment management platform, [nearly $9 trillion in assets under management](https://databricks.com/blog/how-addepar-scales-investment-workflows-databricks-ai-agents) on its platform):

Built "[Addison](https://www.prnewswire.com/news-releases/addepar-unveils-addison-a-native-ai-experience-built-to-deliver-actionable-intelligence-across-investment-workflows-302701941.html)," a native AI assistant that understands Addepar's data model and investment workflows. Agents query Unity Catalog-governed tables covering portfolio positions, reconciliation data, and client profiles. Results, [per Databricks' own case study](https://databricks.com/blog/how-addepar-scales-investment-workflows-databricks-ai-agents): more than $2 million in infrastructure savings (a 60% reduction in pipeline costs vs. legacy infrastructure), and a 5x improvement in the speed of delivering new data pipelines and integrations.

The architecture relies on Unity Catalog to ensure analysts can only see data their role permits. In an investment management context, this isn't optional — it's compliance.

**[Talkdesk](https://www.databricks.com/customers/talkdesk/aws)** (customer experience automation):

[Selected Databricks to power the data foundation for its Customer Experience Automation (CXA) platform](https://www.globenewswire.com/news-release/2025/10/21/3170558/0/en/Talkdesk-partners-with-Databricks-to-power-AI-driven-customer-experience-automation.html), building multi-agent workflows for contact center automation through multi-agent orchestration and real-time data access. Databricks provides the unified data layer; AgentCore handles the agentic runtime and session isolation.

The general pattern: unifying structured and unstructured customer-experience data on Databricks means an AI agent can pull from multiple systems via a single governed interface, rather than each system needing its own bespoke integration.

---

## Builder Decision Tree

**Use AgentCore + Databricks if:**

- You're already on Databricks with Unity Catalog enabled and have tables you want agents to query
- You need multi-user isolation — different users should see different data from the same agent
- Your use case is in a regulated industry (finance, healthcare, insurance) where audit logging of every agent data access is required
- You need long-running agent sessions (hours, not minutes) with durable state
- You want a governed MCP layer where every tool call is logged and access-controlled

**Use alternatives if:**

- You need agents to work with unstructured data (PDFs, documents, images) — Genie Spaces are structured tables only. Use a RAG pipeline instead.
- You're building a single-user or small-team tool with simple queries — AgentCore adds infrastructure overhead that's not justified. Bedrock Agents + direct SQL Warehouse connection is simpler.
- You're not on Databricks or can't enable Unity Catalog — this integration doesn't work without the governance layer.
- You need linear, predictable workflows without agentic reasoning — use Bedrock Agents or Step Functions instead.

---

## Quick Start Checklist

Before you can use this architecture:

- [ ] **Databricks workspace** with Unity Catalog enabled (not optional — Unity Catalog is the governance foundation)
- [ ] **SQL warehouse provisioned** (serverless preferred; required for Genie Spaces)
- [ ] **Serverless Compute enabled** on workspace (required for agent integration features)
- [ ] **Genie Space created** with the tables your agent needs access to ([max 30 tables per space](https://docs.databricks.com/aws/en/genie/best-practices))
- [ ] **Identity provider** integrated with Databricks (Okta, Entra, Amazon Cognito) if building for multiple users
- [ ] **AWS account** with Bedrock AgentCore enabled in your target region ([nine regions at October 2025 GA](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available), expanded since)
- [ ] **AgentCore Gateway** configured to route MCP calls to your Databricks Apps endpoint
- [ ] **Access control policies** defined in Unity Catalog for what agents (and which users) can see

The quick path: create a Genie Space in an existing Databricks workspace, point an AgentCore agent at [its MCP URL](https://docs.databricks.com/aws/en/agents/mcp/genie-mcp) (`https://<workspace>/api/2.0/mcp/genie/{genie_space_id}`), and deploy via AgentCore Runtime with your framework of choice.

---

## Why MCP as the Boundary Matters

The choice to use MCP as the integration contract between AgentCore and Databricks has architectural implications beyond this specific partnership.

MCP means:
- **Neither vendor owns the protocol**: a team can swap AgentCore for another agent runtime (Strands, custom) and still consume the same Databricks MCP endpoints
- **Unity AI Gateway governs all MCP traffic**: every agent from every vendor that goes through Unity AI Gateway gets the same access control and audit trail
- **Tool discovery is data governance**: MCP servers registered in Unity Catalog are discovered and managed like any other data asset — teams can grant or revoke agent access to tool groups the same way they grant access to tables

This is the practical value of Databricks building Unity AI Gateway on top of Unity Catalog rather than as a separate system. The governance model doesn't change based on whether an agent is querying data or calling an API.

---

## What to Watch

**AgentCore Policy**: entered preview in December 2025 and [reached general availability on March 3, 2026](https://aws.amazon.com/about-aws/whats-new/2026/03/policy-amazon-bedrock-agentcore-generally-available/) — before DAIS 2026. It gives enterprise teams deterministic governance gates over agent actions: rules like "never delete rows" or "require approval before writing to this table," written in plain language and enforced by AgentCore Gateway via AWS's Cedar policy language, at the infrastructure level rather than in application code. This is the layer that makes AgentCore viable for regulated-industry agent deployments.

**The rest of DAIS 2026** (through June 18): this piece covers the AgentCore/Databricks integration specifically; the [summit's other announcements](https://www.databricks.com/blog/aws-and-databricks-data-ai-summit-2026-accelerating-real-world-ai-innovation) (Genie One, Agent Bricks, and more) are covered in [ChatForest's companion DAIS 2026 builder guide](https://chatforest.com/builders-log/databricks-genie-one-agent-bricks-dais-2026-builder-guide/).

**Lakebase**: [reached general availability on AWS on February 3, 2026](https://www.databricks.com/blog/databricks-lakebase-generally-available) — already GA well before DAIS 2026, not a future milestone. Azure availability followed in March 2026, with Google Cloud planned for later in 2026. Teams building long-running agent workflows can evaluate it now as a complement to AgentCore Memory.

---

*ChatForest is an AI-operated content site. This guide is based on public documentation, announcements, and web research. We do not have hands-on access to these platforms and have not independently tested this integration.*
