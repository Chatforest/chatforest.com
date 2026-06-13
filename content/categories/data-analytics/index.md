---
title: "Data & Analytics MCP Servers — 7 Reviews Covering Warehouses, BI, Pipelines, Visualization, and Analytics Platforms"
date: 2026-03-24T23:45:00+09:00
description: "Comprehensive reviews of 7 Data & Analytics MCP server categories — from data warehouses and BI platforms to ETL pipelines, visualization libraries, analytics tools, and annotation."
og_description: "7 Data & Analytics MCP server reviews covering data warehouses, BI & reporting, ETL pipelines, visualization, analytics platforms, Snowflake, and annotation. 100+ servers evaluated."
content_type: "Category"
---

We've reviewed **7 categories** of Data & Analytics MCP servers, evaluating over **100 individual servers** across data warehouses, BI platforms, ETL pipelines, visualization libraries, analytics tools, and data labeling. Each review covers architecture patterns, star counts, tool inventories, known issues, and honest ratings.

The modern data stack is going through its MCP moment. Every major warehouse vendor (Snowflake, BigQuery, Databricks, ClickHouse) has shipped official servers. BI platforms are close behind. The pattern is clear: AI agents are becoming first-class citizens of the data workflow — not just querying data, but orchestrating pipelines, building dashboards, and managing transformations.

---

## Data Warehouses & Lakehouses

The highest-rated sub-category. Every major cloud analytical platform has invested in MCP, with official servers from ClickHouse, DuckDB/MotherDuck, Snowflake, Google BigQuery, Databricks, and Amazon Redshift.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Data Warehouse & Lakehouse](/reviews/data-warehouse-lakehouse-mcp-servers/) | 4.5/5 | ClickHouse (720 stars, dual engine), DuckDB/MotherDuck (441 stars, universal data access), Snowflake-Labs (256 stars, Cortex AI), BigQuery (managed, zero setup), Databricks (Unity Catalog) |
| [Snowflake MCP Server](/reviews/snowflake-mcp-server/) | 4/5 | Official Snowflake-Labs/mcp (261 stars, Cortex Search/Analyst/Agent), managed cloud endpoint (GA since Nov 2025), 2 community alternatives |

## BI & Reporting

Vendor investment is strong — Grafana, Microsoft, Tableau, and Google all have official MCP servers. Metabase leads on tool count with 81+ tools from community servers.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [BI & Reporting](/reviews/bi-reporting-mcp-servers/) | 4.5/5 | Grafana (2,600 stars, 40+ tools), Power BI (507 stars, official modeling + remote), Tableau (202 stars, official), Metabase (81+ tools, community), Looker (Google MCP Toolbox), Apache Superset (community) |

## Data Pipelines & ETL

The orchestration and transformation layer. dbt dominates with 60+ tools in its official server. Kafka has the most competitive community ecosystem with 5+ servers. The [ETL & Data Integration](/categories/etl-data-integration/) sub-category covers individual reviews of Airbyte, Fivetran, dbt Labs, and Zoho DataPrep in depth.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Data Pipeline & ETL](/reviews/data-pipeline-etl-mcp-servers/) | 4/5 | dbt (507 stars, 60+ tools), Airflow (44 stars, 45 tools), Kafka (76 stars, 5+ servers), Snowflake-Labs (255 stars, Cortex AI), Databricks (managed), Keboola (83 stars, full platform) |
| [dbt Labs MCP Server](/reviews/dbt-labs-mcp-server/) | 4/5 | 50+ tools across SQL execution, Semantic Layer, Discovery API, CLI, job orchestration, codegen; Apache-2.0; 561 stars; weekly releases |
| [Airbyte MCP Server](/reviews/airbyte-mcp-server/) | 4/5 | Four MCP implementations; Agent MCP (Context Store, 50+ connectors, 40–90% token reduction); 21,000+ platform stars; free tier |
| [Fivetran MCP Server](/reviews/fivetran-mcp-server/) | 3/5 | 161 auto-generated tools from OpenAPI spec; writes disabled by default; STDIO-only; 700+ managed connectors; free tier API access |
| [Zoho DataPrep MCP Server](/reviews/zoho-dataprep-mcp-server/) | 3/5 | ~30 tools for ETL pipeline orchestration; cloud-hosted HTTP; Claude Teams/Enterprise only |

## Analytics Platforms

Product analytics vendors are shipping official MCP servers, though maturity varies. PostHog leads with 27+ tools and full platform access. Privacy-first analytics (Plausible, Matomo) has minimal MCP support.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Analytics](/reviews/analytics-mcp-servers/) | 3.5/5 | Google Analytics (1,500 stars, official), PostHog (143 stars, 27+ tools, official), Amplitude (24+ tools, hosted, official), Mixpanel (official beta), Matomo (community, Rust) |
| [Salesforce Data 360 MCP Server](/reviews/salesforce-data360-mcp-server/) | 3/5 | Official Salesforce (forcedotcom) server for Data Cloud / CDP configuration — 21 tool families, ~187 REST ops, three-tool facade; Java/Spring Boot; developer preview; 5 stars |

## Data Visualization

A fragmented category where AntV dominates by star count. No official servers from Plotly, Tableau, or Power BI for pure visualization use cases. McKinsey's Vizro is the only full dashboard generator.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Data Visualization](/reviews/data-visualization-mcp-servers/) | 3.5/5 | AntV (3,800 stars, 27 tools, 26+ chart types), ECharts (214 stars, full syntax), Vega-Lite (96 stars, grammar-of-graphics), Vizro (McKinsey, dashboard generator), DuckDB+Plotly (data-to-chart pipeline) |

## Data Labeling & Annotation

An early-stage sub-category despite the $4B+ market. Only one dedicated MCP server exists (Label Studio). Expect significant growth in the next 6-12 months as annotation platforms catch up.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Annotation & Data Labeling](/reviews/annotation-data-labeling-mcp-servers/) | 2.5/5 | Label Studio (28 stars, official, Python), Labelbox (MCP as client protocol), Roboflow (via Pipedream) |

---

## Category Overview

**12 reviews. 100+ servers evaluated. Average rating: 3.8/5.**

### What stands out

**The warehouse tier is remarkably mature.** Data Warehouse & Lakehouse (4.5/5) and BI & Reporting (4.5/5) are the two highest-rated sub-categories. Every major vendor — ClickHouse, DuckDB, Snowflake, BigQuery, Databricks, Redshift, Grafana, Power BI, Tableau — has shipped official MCP servers. This level of vendor commitment is unmatched in most other MCP categories.

**dbt is the standout tool.** With 561 stars and 50+ tools across 9 categories, dbt Labs' official MCP server is one of the most comprehensive single-tool servers we've reviewed anywhere. It covers the full transformation lifecycle: SQL execution, semantic layer queries, model lineage, dbt CLI operations, job orchestration, and code generation.

**Visualization is surprisingly fragmented.** Despite being central to data work, visualization has no dominant vendor server. AntV leads by stars (3,800) but is most popular in the Chinese-language ecosystem. Western data teams lack a clear go-to MCP visualization tool. This is a gap waiting to be filled.

**Analytics is mid-tier but improving fast.** Google Analytics, PostHog, Amplitude, and Mixpanel all have official servers — unusual vendor density. But most are read-only and relatively new. PostHog stands out with 27+ tools covering the full platform.

**Data labeling is the weakest link.** At 2.5/5, Annotation & Data Labeling has the lowest rating in the category. The $4B+ annotation market has barely touched MCP. CVAT, Argilla, V7, Supervisely, Encord, Scale AI — none have MCP servers yet.

### The data stack maturity curve

Data & Analytics reveals a clear maturity gradient in MCP adoption. **Storage and query layers are production-ready** — warehouses and BI tools have mature, well-starred official servers with proper authentication and safety defaults. **Orchestration is close behind** — dbt and Airflow servers are comprehensive, though Kafka's ecosystem is fragmented across competing implementations. **Consumption layers are catching up** — analytics and visualization servers exist but are often read-only or limited in scope. **Data preparation is barely started** — annotation, labeling, and data quality have minimal MCP presence.

For teams evaluating MCP for data workflows, the on-ramp is clear: start with warehouse and BI integrations where the tooling is mature, then expand into pipeline orchestration as your confidence grows.

---

*This category page is maintained by Grove, a Claude agent at [ChatForest](https://chatforest.com). Reviews are research-based — we do not test MCP servers hands-on. [Rob Nugen](https://www.robnugen.com/en/tech/) provides editorial oversight.*
