# Databricks Data+AI Summit 2026: What Builders Need to Know Before June 15

> The world's largest data and AI conference returns June 15-18 in San Francisco (and free virtual). Here's what's on the keynote stage, why Lakebase is the dark-horse announcement, and which sessions are worth your time if you're building AI applications on data infrastructure.


Databricks Data+AI Summit 2026 runs June 15-18 at the Moscone Center in San Francisco, with a free virtual stream available to anyone who registers. If you are building AI applications that sit on top of data infrastructure — which in 2026 means most serious AI applications — this is the conference where the Databricks stack evolves in public. This year has a specific reason to pay attention: **Lakebase** is now generally available and its implications for AI app developers are still not widely understood.

Here's a builder-focused preview of what to watch.

## Quick Facts

- **Dates:** June 15-18, 2026
- **Location:** Moscone Center, San Francisco, CA
- **Virtual:** Free with registration; streams to 150+ countries
- **Scale:** 30,000+ in-person attendees expected; 800+ breakout sessions
- **Registration:** Open at [databricks.com/dataaisummit](https://www.databricks.com/dataaisummit)

If you cannot travel, the free virtual track gives you access to the keynotes and most technical sessions. For data/AI practitioners who prefer watching announcements live to reading summaries the next day, the virtual option is worth registering for now.

## The Keynote Lineup

The keynote stage is the Databricks co-founder lineup: **Ali Ghodsi** (CEO), **Matei Zaharia** (CTO), **Arsalan Tavakoli-Shiraji**, and **Reynold Xin**, each expected to drive live product demos and announcements. This is where Databricks historically drops its major feature releases — not in a press release before the event, but live on stage.

External keynote guests include a pre-recorded fireside with **Satya Nadella** (Microsoft) and **Greg Brockman** (OpenAI). The Nadella/Brockman pairing is notable given Microsoft's recent MAI model rollout and its complicated relationship with OpenAI; don't expect dramatic disclosures, but it frames the competitive context for everything else on stage.

More useful for builders: featured technical sessions from **Anthropic**, **Cognition**, **CrewAI**, **LangChain**, **LlamaIndex**, **Lovable**, **OpenAI**, and **Replit**. This is the ecosystem showing up in one place to discuss how their tools sit on top of Databricks infrastructure.

## Why Lakebase Is the Announcement to Watch

The most underreported development coming into this summit is **Lakebase GA**.

Lakebase is Databricks' serverless PostgreSQL product. It launched in June 2025 and has been in general availability since early 2026. At its simplest, it's a managed Postgres database. At its architecturally interesting level, it unifies OLTP transactional workloads, analytical queries, and AI/vector workloads on a single governed data foundation — inside the same Unity Catalog governance layer you're already using for your data lakehouse.

The practical implications for AI application builders:

**Instant database branching.** You can spin up isolated copies of your production database for dev, test, or CI environments in seconds. For teams building AI apps with complex data dependencies, this is a meaningful workflow change.

**No separate vector database.** Lakebase includes vector search alongside standard SQL, which means you can avoid maintaining a separate Pinecone or Weaviate instance if your data already lives in Databricks. This matters for RAG pipelines built on structured + unstructured data.

**Governance without compromise.** Unity Catalog lineage and access control apply to Lakebase tables the same way they apply to Delta Lake tables. If you're building in a regulated industry (finance, healthcare) or for an enterprise that requires audit trails, this is a meaningful differentiator versus managing a standalone Postgres instance.

Lakebase has grown adoption at more than 2x the pace of Databricks' core data warehousing product since its launch — which is a striking figure given how established the warehousing business is. Expect the June 15 keynote to feature Lakebase prominently, with at least one major announced capability or partnership that extends the product.

## The Technical Track: What Else Is Worth Attending

The summit's 800+ sessions span data engineering, MLOps, governance, analytics, agentic applications, and platform development. For builders, the highest-signal tracks:

**MLflow.** MLflow 3.0 shipped earlier this year with native agent tracing, multi-turn conversation tracking, and AI Gateway support. Summit sessions will cover practical patterns for production ML and LLM observability. If you're not using MLflow for experiment tracking and deployment, the summit is a good forcing function to understand whether you should be.

**Delta Lake and Apache Iceberg interoperability.** The table format wars have moved from "pick a side" to "use both." Databricks has been investing in Iceberg compatibility for Delta tables; expect announcements on parity and migration tooling.

**Databricks Apps.** This is Databricks' hosted application runtime for deploying Streamlit, Gradio, and custom Python apps directly inside the Lakehouse. It's relatively new and underused by the Databricks community; sessions here will address whether it's ready for production AI app deployments.

**Unity Catalog for AI governance.** With enterprise AI governance becoming a compliance requirement rather than a best practice, Unity Catalog's AI governance features — model registries, lineage, access control for model endpoints — are increasingly the reason enterprises standardize on Databricks.

## The Agent Infrastructure Angle

Databricks is not an agent framework company. But it is the data layer that most enterprise AI agents run on. The presence of Anthropic, CrewAI, LangChain, and LlamaIndex in the featured sessions signals that the summit is explicitly positioning Databricks as the data foundation for agentic applications, not just batch analytics.

What to watch for in these sessions: patterns for giving agents access to governed data without bypassing Unity Catalog controls; patterns for agent memory and state management on Lakebase; and integration points between Databricks' inference tables (automatic logging of model inputs/outputs) and agent observability frameworks.

## How to Make the Most of It

**If you're attending in-person:** The networking events are notable. There's a Welcome Reception on the evening of June 16, and a Data After Hours party on June 17 at Oracle Park (headlined by The Chainsmokers, for whatever that's worth to you). More usefully, the in-person community skews heavily toward data engineers, ML engineers, and platform architects — a different slice of the technical community than you'd find at, say, a pure AI developer conference.

**If you're watching virtually:** Register in advance rather than hunting for recordings after the fact. The virtual stream typically includes live Q&A access for keynotes and selected breakout sessions, which is lost if you wait for the on-demand release.

**The sessions to block first:** Ghodsi's keynote for major product announcements; any Lakebase deep-dive session for architectural detail; the Anthropic or LangChain session for the agent-on-data-infrastructure angle; and the Delta Lake/Iceberg interoperability session if table format decisions are live questions in your stack.

## What We're Writing After the Summit

If the Lakebase session produces architectural details that change how AI app builders should think about data persistence, we'll cover that. If any of the framework integrations (CrewAI, LangChain, LlamaIndex on Databricks) surface patterns worth documenting, we'll document them.

The summit runs June 15-18. We'll have post-summit analysis up the week of June 22.

---

*This article is based on pre-summit research. Session details and keynote announcements are subject to change. Registration and agenda information accurate as of June 8, 2026.*

