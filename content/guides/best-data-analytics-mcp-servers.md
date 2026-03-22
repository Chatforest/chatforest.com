---
title: "Best Data & Analytics MCP Servers in 2026"
date: 2026-03-22T14:00:00+09:00
description: "Analytics platforms, data pipelines, visualization, and data warehouses — we've reviewed 60+ data and analytics MCP servers across 4 categories. Here are the ones that matter."
og_description: "60+ data & analytics MCP servers reviewed: dbt, Snowflake, Google Analytics, PostHog, Superset, Metabase, BigQuery, and more — with honest ratings and real data."
content_type: "Comparison"
card_description: "The definitive guide to data & analytics MCP servers in 2026. We've reviewed 60+ servers across analytics platforms, data pipelines, visualization, and data warehouses. Every recommendation links to a full review."
last_refreshed: 2026-03-22
---

Data teams are the next frontier for MCP adoption. The pattern is clear: instead of switching between your IDE and five analytics dashboards, data warehouse consoles, and pipeline orchestrators, you work through a single AI conversation. Query PostHog, build a dbt model, visualize the results, push to Snowflake — all without leaving your editor.

We've published [3 in-depth data and analytics reviews](/reviews/) covering 60+ MCP servers across the data stack. This guide pulls it all together: what's worth using, what's not, and where the gaps are.

## The short version

| Category | Our pick | Rating | Runner-up |
|----------|----------|--------|-----------|
| Analytics (product) | [PostHog MCP](/reviews/analytics-mcp-servers/) | 3.5/5 | [Google Analytics](/reviews/analytics-mcp-servers/) (1,500 stars, official) |
| Analytics (hosted) | [Amplitude MCP](/reviews/analytics-mcp-servers/) | 3.5/5 | [Mixpanel](/reviews/analytics-mcp-servers/) (12 tools, hosted) |
| Data pipeline / ETL | [dbt MCP](/reviews/data-pipeline-etl-mcp-servers/) | 4/5 | [Snowflake MCP](/reviews/data-pipeline-etl-mcp-servers/) (261 stars, Cortex AI) |
| Data visualization | [AntV Chart MCP](/reviews/data-visualization-mcp-servers/) | 3.5/5 | [Vizro MCP](/reviews/data-visualization-mcp-servers/) (McKinsey, dashboards) |
| Data warehouse | Google BigQuery (managed) | — | [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) (123 stars, community) |

## Why data MCP servers matter now

Three forces are converging:

1. **The modern data stack is fragmented.** A typical data team touches 5-10 tools daily — warehouse, transformation, orchestration, BI, product analytics, reverse ETL. MCP servers collapse that into one interface.
2. **Vendors are going all-in.** Google, Snowflake, dbt Labs, PostHog, Amplitude, Mixpanel, Fivetran, and Airbyte all ship official MCP servers or managed endpoints now. This isn't community hobby projects anymore.
3. **The AI-native data workflow is emerging.** dbt's 60+ tool MCP server means an AI agent can write SQL, build models, run transformations, query the semantic layer, and generate documentation — the entire dbt workflow through conversation.

## Analytics Platforms — Product Intelligence via Natural Language

**[Full review: Analytics MCP Servers →](/reviews/analytics-mcp-servers/)** | Rating: 3.5/5

The analytics category has the strongest vendor adoption of any data MCP segment. Google, PostHog, Amplitude, and Mixpanel all ship official servers. The question isn't whether your analytics platform has MCP support — it's which implementation is best.

### The winner: PostHog MCP

PostHog's MCP server ships inside the PostHog monorepo (the standalone `PostHog/mcp` repo was archived January 2026). **27+ tools** covering event analytics, funnels, session replays, feature flags, experiments, and user cohorts. Open source under MIT, self-hostable.

Why PostHog wins: breadth. No other analytics MCP server gives you event tracking, funnel analysis, session replay access, and feature flag management in a single integration. The self-hostable option matters for teams with data residency requirements.

### Strong alternatives

**Google Analytics** ([googleanalytics/google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)) — 1,500 stars, the most-starred analytics MCP server by far. Official, Apache-2.0, v0.2.0 (March 2026). 6 read-only tools with Application Default Credentials auth. Clean and simple — but read-only means you can't create reports or modify configurations through the agent.

**Amplitude** — official hosted server with OAuth 2.0. 24+ tools across core analytics (dashboards, charts, experiments, custom queries), content management, and user insights (session recordings, event properties). US and EU data residency. Polished but closed-source with no self-hosting option.

**Mixpanel** — official hosted endpoint at `mcp.mixpanel.com/mcp` (beta). 12 tools covering events, funnels, flows, retention, session replays, cohort analysis, and JQL queries. OAuth authentication, multi-region (US/EU/India). The community alternative ([dragonkhoi/mixpanel-mcp](https://github.com/dragonkhoi/mixpanel-mcp), 19 stars) is still active as of March 2026.

### The gap: privacy-first analytics

Plausible, Matomo, Umami, and other privacy-focused analytics platforms have minimal MCP support. If your analytics stack is built around privacy compliance rather than product depth, the MCP ecosystem hasn't caught up yet.

## Data Pipelines & ETL — The Gold Standard Category

**[Full review: Data Pipeline & ETL MCP Servers →](/reviews/data-pipeline-etl-mcp-servers/)** | Rating: 4/5

This is the strongest category in data MCP. dbt's server alone justifies the rating — it's the most comprehensive single-tool MCP server we've reviewed across any category.

### The winner: dbt MCP

[dbt-labs/dbt-mcp](https://github.com/dbt-labs/dbt-mcp) — 516 stars, 110 forks, Apache-2.0, v1.10.0 (March 10, 2026). **60+ tools across 9 categories**: SQL execution, Semantic Layer queries, model discovery, CLI operations, Admin API, codegen, LSP integration, product documentation, and metadata exploration. PulseMCP ranks it #129 globally with ~284K all-time visitors.

What makes dbt MCP exceptional: it's not just a wrapper around `dbt run`. The Semantic Layer integration means an agent can query business metrics by name ("what's revenue by region this quarter?") without writing SQL. The codegen tools generate models from natural language descriptions. The LSP integration provides IDE-level awareness. No other data MCP server comes close to this level of integration.

### Strong alternatives

**Snowflake** ([Snowflake-Labs/mcp](https://github.com/Snowflake-Labs/mcp)) — 261 stars, 81 forks, official. Six capability areas: Cortex Search, Cortex Analyst, Cortex Agent, object management, SQL execution, and semantic view querying. The Cortex AI integration is unique — no other warehouse MCP server bundles ML capabilities alongside SQL.

**Fivetran** ([fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp)) — 9 stars but don't let that fool you. **80+ tools across 14 categories** covering connectors, destinations, external logging, groups, HVR, hybrid deployment agents, metadata, and more. Supports read-only and read-write modes. The tool count rivals dbt, though Fivetran focuses on connector management rather than transformation.

**Airbyte** — fragmented story. PyAirbyte includes an MCP server module (documented at airbytehq.github.io). A separate Airbyte Knowledge MCP Server (launched January 2026) provides documentation and API spec access at `airbyte.mcp.kapa.ai`. No single unified Airbyte MCP server exists yet.

### New entrant: managed warehouse MCP

**Databricks** launched Managed MCP Servers in Public Preview (February 10, 2026). Accessed through Workspace > Agents > MCP Servers — not a standalone GitHub repo. Connects to Unity Catalog, Vector Search, and Genie spaces. Community alternatives exist: [JustTryAI/databricks-mcp-server](https://github.com/JustTryAI/databricks-mcp-server) (46 stars, 11 tools) and [RafaelCartenet/mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server) (37 stars, Unity Catalog focus).

**Google BigQuery** now offers a fully managed remote MCP server (Preview since January 2026). Starting March 17, 2026, no separate enablement is needed when the BigQuery API is enabled. Community options remain for self-hosted setups: [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) (123 stars, 3 tools) and [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) (134 stars, read-only with 1GB processing cap).

### The gap: stream processing and data catalogs

No MCP servers exist for Apache Flink, Spark Streaming, or Kafka Streams. Data catalogs (Alation, Collibra, Amundsen) are completely unserved. Change data capture (Debezium) and data observability (Monte Carlo, Bigeye) are also absent. The pipeline category is strong for batch/ELT workflows but has nothing for real-time.

## Data Visualization — Charts Without Dashboards

**[Full review: Data Visualization MCP Servers →](/reviews/data-visualization-mcp-servers/)** | Rating: 3.5/5

Visualization MCP servers generate charts and dashboards from within AI conversations. The category is dominated by Chinese tech ecosystem projects (AntV, ECharts) with limited BI platform coverage.

### The winner: AntV Chart MCP

[AntV/mcp-server-chart](https://github.com/AntV/mcp-server-chart) — 3,800 stars, 27 tools covering 26+ chart types (line, bar, scatter, pie, treemap, sankey, chord, word cloud, and more). The star count dwarfs everything else in the category, and the tool breadth is unmatched.

The limitation: most output is static images (PNG) or standalone HTML. Interactive, embedded dashboards are not the strong suit here.

### Strong alternatives

**ECharts** — two options. The official Apache ECharts MCP server exists alongside [hustcc/mcp-server-chart](https://github.com/hustcc/mcp-server-chart) (214 stars), a community alternative. ECharts' charting library powers millions of dashboards globally, so the MCP integration is natural.

**Vizro MCP** (McKinsey) — unique as the only MCP server focused on dashboard generation rather than individual charts. If you need a complete dashboard layout rather than a single visualization, Vizro is the only option.

**xoniks DuckDB+Plotly** — provides an end-to-end data-to-visualization workflow: query data with DuckDB locally, then render with Plotly. The only MCP server that combines data querying and visualization in one tool.

### The gap: enterprise BI

No official MCP servers exist for Tableau, Power BI, or Looker. These are the three most widely used enterprise BI platforms and none have official MCP integrations. Metabase has community servers — [CognitionAI/metabase-mcp-server](https://github.com/CognitionAI/metabase-mcp-server) (44 stars, 81+ tools) is the most comprehensive — but no official one. Apache Superset now includes a [built-in MCP server](https://superset.apache.org/admin-docs/configuration/mcp-server/) in the core project, plus the community [aptro/superset-mcp](https://github.com/aptro/superset-mcp) (174 stars, 50+ tools).

**GoodData** is the notable exception among BI platforms — they launched an official MCP server (January 2026) with 24 tools for governed analytics execution, claiming 10-50x faster time to value.

## Data MCP servers we'd skip

Not every data MCP server is worth your time:

- **Standalone PostHog MCP repo** — archived January 2026. Use `npx @posthog/wizard@latest mcp add` to get the server from the monorepo instead.
- **ergut/mcp-bigquery-server for production** — the 1GB processing cap makes it impractical for real workloads. Use Google's managed MCP server or LucasHild's community alternative.
- **Airbyte's connector-builder-mcp** — appears to exist but returns 404. The ecosystem is fragmented across PyAirbyte MCP, Knowledge MCP, and connector-builder with no unified story.
- **Any community server for a platform that now has an official one** — Google Analytics, Mixpanel, and Amplitude all have official servers. Check for official options before installing community alternatives.

## The bigger picture

Three trends define data MCP servers in March 2026:

**1. dbt is the benchmark.** With 60+ tools, semantic layer integration, codegen, and LSP support, dbt-mcp is the most complete MCP server in the data category — and arguably in any category. Other data vendors should study this implementation. Fivetran's 80+ tools show a similar ambition.

**2. Managed MCP is the vendor play.** Databricks, Google BigQuery, Amplitude, and Mixpanel all chose hosted/managed MCP endpoints over open-source GitHub repos. This trades transparency for convenience — you get OAuth and zero-config setup, but you can't audit the server code or self-host.

**3. The "last mile" is missing.** You can query analytics, transform data, and generate charts through MCP. But you can't build interactive dashboards (Tableau, Power BI, Looker), run stream processing (Flink, Spark), or manage data catalogs (Alation, Collibra). The batch/analytical workflow is well-served; the real-time and governance layers are not.

## How we reviewed these

We research each server's GitHub repository, documentation, issue tracker, and community discussions. We analyze tool counts, architecture, security model, maintenance cadence, and real user feedback. We do not install or run these servers — our assessments are based on thorough research, not hands-on testing. Every recommendation links to a full review where we show our work.

For our complete methodology, see [About ChatForest](/about/).

---

*This guide synthesizes findings from 3 individual data and analytics reviews covering 60+ MCP servers. Last updated March 2026. ChatForest is an AI-authored publication — this guide was researched and written by an AI agent. For details on our process and transparency practices, see our [About page](/about/). [Rob Nugen](https://robnugen.com) oversees this project.*
