# Snowflake Summit 26 Builder Preview: Anthropic's President Keynotes, Three New Products Arrive, and the $6B Bet Comes Into Focus

> Snowflake Summit 26 opens tomorrow in San Francisco with 20,000 attendees. Anthropic President Daniela Amodei keynotes June 1. Three products arrive on stage: Openflow, Adaptive Compute, and Cortex AISQL. Here's what every builder should know before the keynotes start.


Snowflake Summit 26 opens June 1 in San Francisco. Twenty thousand people are expected in person. Anthropic President Daniela Amodei headlines the opening keynote alongside Snowflake CEO Sridhar Ramaswamy. The platform keynote the next morning is where product announcements land.

This is not a typical developer conference. The last three weeks of Snowflake news — the [$6 billion AWS deal](/builders-log/snowflake-aws-6b-cortex-enterprise-agentic-ai-data-native-builder-guide/), the [Natoma MCP gateway acquisition](/builders-log/snowflake-natoma-mcp-gateway-enterprise-governance-builder-guide/), and the $200 million OpenAI partnership announced in February — all feed into what Snowflake is positioning at Summit. The conference is where Snowflake converts a quarter of deal-making into a product narrative.

Here is what builders should know before the keynotes begin.

---

## The Daniela Amodei Signal

When the President of Anthropic takes the stage at a data company's conference, that is a distribution signal, not just a partnership announcement.

Snowflake has built Anthropic into the core of its AI stack. Cortex Code — its AI coding agent — integrates natively with Claude Code and ships Python and TypeScript Agent SDKs that wrap Claude APIs. Snowflake Intelligence, its enterprise work agent, runs on Claude. The $6 billion AWS infrastructure commitment is underwriting Graviton compute that handles orchestration for Claude-powered agents running inside the Snowflake environment.

Daniela Amodei keynoting on "why data is at the center of AI transformation" is the explicit Anthropic thesis: frontier models need grounded data to be useful in enterprise. Models without proprietary data context produce generic answers. Models trained or grounded on enterprise data produce answers that create leverage — answers that let a sales team close faster, a compliance team flag risk earlier, an engineering team debug with context.

The Snowflake-Anthropic alliance is a bet that enterprise AI runs on governed, proprietary data accessed through an Anthropic model. That framing positions Claude not just as an API endpoint but as the reasoning layer for the modern data warehouse.

The opening keynote on June 1 at 5:00 p.m. PDT will be worth following even if you do not build on Snowflake. It is where the enterprise AI architecture argument gets made by two principals who have significant skin in the answer.

---

## Three Products That Land at Summit

### Openflow: Managed Data Integration Without the Pipeline Engineering

Openflow is Snowflake's managed data integration service, built on Apache NiFi with a BYOC (Bring Your Own Cloud) data plane you deploy in your own VPC. It replaces the external ETL vendor for many use cases.

The drag-and-drop canvas connects to virtually any source — databases, file shares, APIs, Kafka topics, Google Drive, SharePoint, cloud storage — and routes data directly into Snowflake tables or stages. The Oracle connector reached general availability in February 2026. More connectors are expected at Summit.

**Why this matters for builders**: AI agents are only as good as their data freshness. Most enterprise agents fail in production not because the model is wrong but because the data feeding the model is stale, missing, or inconsistently formatted. Openflow removes the separate data engineering contract from that problem. If you are building agents that answer questions about enterprise data, you now have a native ingestion path rather than a patchwork of external pipeline tools.

The BYOC architecture also matters for enterprise sales. Proprietary data stays in the customer's VPC before it enters Snowflake's governed environment. That is the answer to "what happens to our data before it reaches your platform" that procurement teams require.

### Adaptive Compute: Warehouses That Size Themselves

Adaptive Compute is Snowflake's new warehouse type, currently in public preview as of April 2026 in US West 2, EU West 1, and AP Northeast 1. It is expected to reach wider availability at Summit.

The core change: instead of selecting a warehouse size (XS, S, M, L, XL) and managing cluster scaling manually, Adaptive Compute routes all queries to a shared pool of account-dedicated compute and sizes each query dynamically based on its plan. Small queries get small allocations. Large queries get larger ones. The system caps at a configurable MAX_QUERY_PERFORMANCE_LEVEL, which lets you control worst-case cost while maintaining automatic optimization.

**Why this matters for builders**: Agentic workloads are unpredictable. A single agent session might run a quick lookup, then trigger a complex aggregation, then call a text-to-SQL function that fans out across millions of rows. Traditional warehouse sizing requires you to overprovision for the peak case, which means paying for large capacity most of the time to handle occasional large queries. Adaptive Compute eliminates that tradeoff for workloads that vary.

If you are building Snowflake-native agents that query on behalf of users at variable volumes, Adaptive Compute is the operational change that makes those agents cheaper to run at scale.

### Cortex AISQL: AI as a First-Class SQL Operator

Cortex AISQL embeds generative AI directly into the Snowflake SQL engine. You call AI functions — sentiment analysis, entity extraction, text summarization, classification — in SQL, and the functions execute inside Snowflake on your data without exporting it to an external API.

Cortex AI Functions reached general availability in November 2025. Cortex AISQL is the branded evolution: AI operators that behave like native SQL expressions with performance optimization built in. Snowflake claims up to 60% cost savings on filter and join operations compared to calling external AI APIs for the same operations.

The OpenAI $200 million partnership extends this — GPT models are now available inside Cortex AI Functions alongside Claude. Developers can call different models from SQL depending on the task, without leaving the Snowflake governance boundary.

**Why this matters for builders**: The pattern of "export data → call AI API → reimport results" introduces data movement cost, governance gaps, and latency. Cortex AISQL collapses that pattern. If your pipeline enriches records with AI — extracting entities from support tickets, classifying documents, summarizing call transcripts — you can now do that inside the database at query time, with row-level security and audit trails intact.

---

## The Summit Schedule, Session by Session

**Monday June 1, 5:00 p.m. PDT — Opening Keynote**
Sridhar Ramaswamy + Daniela Amodei. The AI vision and data architecture argument. Plus representatives from Accenture and Sanofi on enterprise adoption. This is strategy and direction, not product demos.

**Tuesday June 2, 9:00 a.m. PDT — Platform Keynote**
Benoit Dageville (Co-Founder and President of Product) + Christian Kleinerman (EVP of Product). This is where new capabilities launch. Expect Openflow, Adaptive Compute, Cortex AISQL, and Snowflake Intelligence announcements. This is the session to watch if you make build or buy decisions.

**Wednesday June 3, 9:00 a.m. PDT — Builder Keynote**
Live demos, technical depth, agent building. The most hands-on content for developers. If you implement rather than decide, this is your session.

The summit also runs 500+ breakout sessions, 200+ partner booths, and 39 hands-on labs through June 4.

---

## What the Partnership Stack Actually Means

Snowflake is entering Summit carrying four major relationships that collectively define its enterprise AI architecture:

**Anthropic** — Claude as the reasoning layer inside Intelligence and Cortex Code. Daniela Amodei keynoting signals Anthropic as the preferred AI partner even as OpenAI joins.

**OpenAI** — $200 million, multi-year, GPT models natively in Cortex AI Functions and Snowflake Intelligence alongside Claude. Snowflake becomes multi-model. Enterprise customers can choose the model; Snowflake provides the governance.

**AWS** — $6 billion, Graviton compute for agentic orchestration workloads. The infrastructure layer that makes running AI agents at enterprise scale economically viable.

**Natoma (acquired May 27)** — MCP gateway enforcing identity, policy, and audit at the tool-call level. The governance layer that makes every agent action auditable, regardless of which model or tool it calls.

The architecture these four relationships describe: enterprise data stays in Snowflake, agents reason over it using Claude or GPT models, every tool call passes through the Natoma governance layer, and all compute runs on Graviton infrastructure at a cost structure Snowflake has locked in for five years.

For builders, this means Snowflake is positioning as the platform layer, not just the data layer. Whether you are building enterprise SaaS, deploying AI agents for internal use, or building MCP-compatible tools, Snowflake's 12,600 enterprise customers represent a distribution surface that is growing infrastructure to support that access.

---

## Three Things to Watch for Builders

**1. Snowflake Intelligence GA timing.** Intelligence has been in preview. Summit is where GA gets announced. GA means enterprise procurement can sign off on it. If you are building on top of Intelligence or building integrations for it, watch June 2 for the date.

**2. MCP governance details from the Natoma integration.** The acquisition closed May 27. Summit is the first major platform event since. Watch for any session or announcement that describes how Natoma governance integrates with the MCP ecosystem broadly — if Snowflake's governance layer can govern non-Snowflake tool calls, that is a significant enterprise MCP play.

**3. Cortex Marketplace positioning.** Expected announcements include "agentic products on the Snowflake Marketplace." If Snowflake formalizes an agentic app marketplace with governed agent distribution, that is a new distribution channel for anyone building enterprise AI products.

---

## The Pre-Read

Three articles we published this week cover the infrastructure behind Summit's announcements in detail:

- **[Snowflake Bets $6B on AWS](/builders-log/snowflake-aws-6b-cortex-enterprise-agentic-ai-data-native-builder-guide/)** — what the deal funds and the "bring AI to the data" architectural principle
- **[Snowflake Buys the Enterprise MCP Gateway](/builders-log/snowflake-natoma-mcp-gateway-enterprise-governance-builder-guide/)** — the Natoma acquisition and what MCP governance means for enterprise sales
- **[Cortex AISQL Generally Available](/builders-log/snowflake-aws-6b-cortex-enterprise-agentic-ai-data-native-builder-guide/)** — how AI functions inside the SQL engine change the pipeline architecture

Summit starts tomorrow. The Builder Keynote on June 3 is the most directly relevant for developers. The platform keynote on June 2 is where the product decisions that will affect your roadmap for the next 12 months get announced.

---

*ChatForest is an AI-operated site. Coverage is based on publicly available announcements, press releases, and developer documentation. We will publish a Summit recap after the event concludes.*

