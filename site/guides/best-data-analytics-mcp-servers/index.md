# Best Data & Analytics MCP Servers in 2026

> Analytics platforms, data pipelines, visualization, and data warehouses — we've reviewed 60+ data and analytics MCP servers across 4 categories. Here are the ones that matter.


Data teams are the next frontier for MCP adoption. The pattern is clear: instead of switching between your IDE and five analytics dashboards, data warehouse consoles, and pipeline orchestrators, you work through a single AI conversation. Query PostHog, build a dbt model, visualize the results, push to Snowflake — all without leaving your editor.

We've published [3 in-depth data and analytics reviews](/reviews/) covering 60+ MCP servers across the data stack. This guide pulls it all together: what's worth using, what's not, and where the gaps are.

## The short version

| Category | Our pick | Rating | Runner-up |
|----------|----------|--------|-----------|
| Analytics (product) | [PostHog MCP](/reviews/analytics-mcp-servers/) | 3.5/5 | [Google Analytics](/reviews/analytics-mcp-servers/) (2,900+ stars, official) |
| Analytics (hosted) | [Amplitude MCP](/reviews/analytics-mcp-servers/) | 3.5/5 | [Mixpanel](/reviews/analytics-mcp-servers/) (12 tools, hosted) |
| Data pipeline / ETL | [dbt MCP](/reviews/data-pipeline-etl-mcp-servers/) | 4/5 | [Snowflake MCP](/reviews/data-pipeline-etl-mcp-servers/) (295 stars, Cortex AI) |
| Data visualization | [AntV Chart MCP](/reviews/data-visualization-mcp-servers/) | 3.5/5 | [Vizro MCP](/reviews/data-visualization-mcp-servers/) (McKinsey, dashboards) |
| Enterprise BI | [Qlik MCP](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-server.htm) | — | [Domo MCP](https://www.barchart.com/story/news/948839/domo-launches-ai-agent-builder-and-mcp-server-to-connect-enterprise-data-to-the-ai-ecosystem) ([interactive dashboards](/guides/domo-mcp-server-enterprise-ai-agents/)) |
| Multi-source integration | [CorpusIQ](https://www.corpusiq.io/enterprise) (small vendor, unverified independently) | — | — |
| Data warehouse | Google BigQuery (managed) | — | [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) (128 stars, community) |

## Why data MCP servers matter now

Three forces are converging:

1. **The modern data stack is fragmented.** A typical data team touches 5-10 tools daily — warehouse, transformation, orchestration, BI, product analytics, reverse ETL. MCP servers collapse that into one interface.
2. **Vendors are going all-in.** Google, Snowflake, dbt Labs, PostHog, Amplitude, Mixpanel, Fivetran, and Airbyte all ship official MCP servers or managed endpoints now. This isn't community hobby projects anymore.
3. **The AI-native data workflow is emerging.** dbt's 60+ tool MCP server means an AI agent can write SQL, build models, run transformations, query the semantic layer, and generate documentation — the entire dbt workflow through conversation.

## Analytics Platforms — Product Intelligence via Natural Language

**[Full review: Analytics MCP Servers →](/reviews/analytics-mcp-servers/)** | Rating: 3.5/5

The analytics category has the strongest vendor adoption of any data MCP segment. Google, PostHog, Amplitude, and Mixpanel all ship official servers. The question isn't whether your analytics platform has MCP support — it's which implementation is best.

### The winner: PostHog MCP

PostHog's MCP server ships inside the PostHog monorepo (the standalone [`PostHog/mcp` repo](https://github.com/PostHog/mcp) was archived January 19, 2026). **[27+ tools](https://posthog.com/docs/model-context-protocol)** covering event analytics, funnels, session replays, feature flags, experiments, and user cohorts. Open source under MIT, self-hostable.

Why PostHog wins: breadth. No other analytics MCP server gives you event tracking, funnel analysis, session replay access, and feature flag management in a single integration. The self-hostable option matters for teams with data residency requirements.

### Strong alternatives

**Google Analytics** ([googleanalytics/google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)) — 2,900+ stars, the most-starred analytics MCP server by far. Official, Apache-2.0. Read-only tools (account/property retrieval, core reports, realtime reports) with [Application Default Credentials auth](https://github.com/googleanalytics/google-analytics-mcp). Clean and simple — but read-only means you can't create reports or modify configurations through the agent.

**[Amplitude](https://amplitude.com/docs/amplitude-ai/amplitude-mcp)** — official hosted server with OAuth 2.0. 24+ tools across core analytics (dashboards, charts, experiments, custom queries), content management, and user insights (session recordings, event properties). US and EU data residency. Polished but closed-source with no self-hosting option.

**[Mixpanel](https://docs.mixpanel.com/docs/mcp)** — official hosted endpoint at `mcp.mixpanel.com/mcp` (beta). 12 tools covering events, funnels, flows, retention, session replays, cohort analysis, and JQL queries. OAuth authentication, multi-region (US/EU/India). The community alternative ([dragonkhoi/mixpanel-mcp](https://github.com/dragonkhoi/mixpanel-mcp), 19 stars) is still active.

### The gap: privacy-first analytics

Plausible, Matomo, Umami, and other privacy-focused analytics platforms have minimal MCP support. If your analytics stack is built around privacy compliance rather than product depth, the MCP ecosystem hasn't caught up yet.

## Data Pipelines & ETL — The Gold Standard Category

**[Full review: Data Pipeline & ETL MCP Servers →](/reviews/data-pipeline-etl-mcp-servers/)** | Rating: 4/5

This is the strongest category in data MCP. dbt's server alone justifies the rating — it's the most comprehensive single-tool MCP server we've reviewed across any category.

### The winner: dbt MCP

[dbt-labs/dbt-mcp](https://github.com/dbt-labs/dbt-mcp) — 595 stars, 127 forks, Apache-2.0. **60+ tools across 9 categories**: SQL execution, Semantic Layer queries, model discovery, CLI operations, Admin API, codegen, LSP integration, product documentation, and metadata exploration. [PulseMCP](https://www.pulsemcp.com/servers/dbt) ranks it #101 globally with ~698K all-time visitors.

What makes dbt MCP exceptional: it's not just a wrapper around `dbt run`. The Semantic Layer integration means an agent can query business metrics by name ("what's revenue by region this quarter?") without writing SQL. The codegen tools generate models from natural language descriptions. The LSP integration provides IDE-level awareness. No other data MCP server comes close to this level of integration.

### Strong alternatives

**Snowflake** ([Snowflake-Labs/mcp](https://github.com/Snowflake-Labs/mcp)) — 295 stars, 104 forks, official. Six capability areas: Cortex Search, Cortex Analyst, Cortex Agent, object management, SQL execution, and semantic view querying. The Cortex AI integration is unique — no other warehouse MCP server bundles ML capabilities alongside SQL.

**Fivetran** ([fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp)) — 21 stars but don't let that fool you. **80+ tools across 14 categories** covering connectors, destinations, external logging, groups, HVR, hybrid deployment agents, metadata, and more. Supports read-only and read-write modes. The tool count rivals dbt, though Fivetran focuses on connector management rather than transformation.

**Airbyte** — fragmented story. PyAirbyte includes an [experimental MCP server module](https://docs.airbyte.com/developers/mcp-servers/pyairbyte-mcp). A separate Airbyte Knowledge MCP Server provides documentation and API spec access at `airbyte.mcp.kapa.ai`. No single unified Airbyte MCP server exists yet.

### New entrant: managed warehouse MCP

**Databricks** launched [Managed MCP Servers in Public Preview](https://docs.databricks.com/aws/en/release-notes/product/2026/january) (January 2026). Accessed through Workspace > Agents > MCP Servers — not a standalone GitHub repo. [Connects to Unity Catalog, AI Search indexes, and Genie Agents](https://docs.databricks.com/aws/en/agents/mcp-tools/managed-mcp). Community alternatives exist: [JustTryAI/databricks-mcp-server](https://github.com/JustTryAI/databricks-mcp-server) (48 stars, 11 tools) and [RafaelCartenet/mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server) (42 stars, Unity Catalog focus).

**Google BigQuery** now offers a [fully managed remote MCP server](https://cloud.google.com/blog/products/data-analytics/using-the-fully-managed-remote-bigquery-mcp-server-to-build-data-ai-agents) (Preview since January 7, 2026). [Starting March 17, 2026, no separate enablement is needed](https://docs.cloud.google.com/mcp/release-notes) when the BigQuery API is enabled. Community options remain for self-hosted setups: [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) (128 stars, 3 tools) and [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) (146 stars, read-only with 1GB processing cap).

### The gap: stream processing and data catalogs

No MCP servers exist for Apache Flink, Spark Streaming, or Kafka Streams. Data catalogs (Alation, Collibra, Amundsen) are completely unserved. Change data capture (Debezium) and data observability (Monte Carlo, Bigeye) are also absent. The pipeline category is strong for batch/ELT workflows but has nothing for real-time.

## Data Visualization — Charts Without Dashboards

**[Full review: Data Visualization MCP Servers →](/reviews/data-visualization-mcp-servers/)** | Rating: 3.5/5

Visualization MCP servers generate charts and dashboards from within AI conversations. The category is dominated by Chinese tech ecosystem projects (AntV, ECharts) with limited BI platform coverage.

### The winner: AntV Chart MCP

[antvis/mcp-server-chart](https://github.com/antvis/mcp-server-chart) — 4,300 stars, 26+ tools covering 26+ chart types (line, bar, scatter, pie, treemap, sankey, funnel, word cloud, and more). The star count dwarfs everything else in the category, and the tool breadth is unmatched.

The limitation: most output is static images (PNG) or standalone HTML. Interactive, embedded dashboards are not the strong suit here.

### Strong alternatives

**ECharts** — two options. The [official Apache ECharts MCP server](https://github.com/apache/echarts-mcp) (77 stars) exists alongside [hustcc/mcp-echarts](https://github.com/hustcc/mcp-echarts) (257 stars), a community alternative. Apache ECharts is a widely used open-source charting library, so the MCP integration is a natural extension of an existing tool.

**[Vizro MCP](https://github.com/mckinsey/vizro/tree/main/vizro-mcp)** (McKinsey, part of the [Vizro](https://github.com/mckinsey/vizro) toolkit, 3,700+ stars) — unique as the only MCP server focused on dashboard generation rather than individual charts. If you need a complete dashboard layout rather than a single visualization, Vizro is the only option.

**[xoniks/mcp-visualization-duckdb](https://github.com/xoniks/mcp-visualization-duckdb)** (DuckDB+Plotly) — provides an end-to-end data-to-visualization workflow: query data with DuckDB locally, then render with Plotly. The only MCP server that combines data querying and visualization in one tool.

### Enterprise BI: Qlik leads, the gap keeps closing

Tableau, Power BI, and Looker — the three most widely used enterprise BI platforms — still lack official MCP integrations. But the gap has narrowed significantly, with Qlik now setting the standard.

**Qlik** ([official MCP server](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-server.htm)) — [GA February 10, 2026](https://www.qlik.com/us/news/company/press-room/press-releases/qlik-brings-agentic-analytics-to-general-availability-and-launches-mcp-server-for-third-party-assistants). **[69 tools across 12 categories](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-server-tools.htm)**: app discovery and metadata, automations, bookmarks, business glossary management (12 tools), datasets and data quality (9 tools), data exploration and analysis, data products (8 tools), knowledge bases, lineage, master items, selections and filtering, and visualization and sheets. The most comprehensive official enterprise BI MCP server by tool count. Qlik's MCP server exposes the full analytics engine to third-party assistants including Claude — agents can search apps, ask natural language questions against governed data, create dashboards and visualizations via prompts, manage business glossaries, inspect data lineage, and work with data products. [Four out-of-the-box agents ship](https://www.qlik.com/us/news/company/press-room/press-releases/qlik-brings-agentic-analytics-to-general-availability-and-launches-mcp-server-for-third-party-assistants) for structured analytics, unstructured knowledge, anomaly discovery, and help/assistance. Available in Qlik Cloud with OAuth authentication. Note: sharing Qlik data with third-party AI systems means data is processed outside Qlik's control — review your governance requirements.

Community alternatives exist: [bintocher/qlik-sense-mcp](https://github.com/bintocher/qlik-sense-mcp) (36 stars, 24 tools for Qlik Sense Enterprise — 12 of which are hidden in JWT-authenticated mode), [arthurfantaci/qlik-mcp-server](https://github.com/arthurfantaci/qlik-mcp-server) (9 tools), and [jwaxman19/qlik-mcp](https://github.com/jwaxman19/qlik-mcp) (Qlik Cloud API).

**Domo** — [unveiled at the company's Domopalooza conference on March 25, 2026](https://www.barchart.com/story/news/948839/domo-launches-ai-agent-builder-and-mcp-server-to-connect-enterprise-data-to-the-ai-ecosystem), alongside AI Agent Builder, AI Toolkits, and a centralized AI Library. The bigger story is Domo's AI Toolkits architecture — packaged capability sets that define what agents can do, exposed externally via MCP to Claude, Gemini, and ChatGPT. Unlike traditional MCP servers that return plain text, Domo's implementation renders interactive business experiences (dashboards, visualizations) directly inside chat interfaces. The AI Agent Builder (available now) and [AI Library (available this summer)](https://www.barchart.com/story/news/948839/domo-launches-ai-agent-builder-and-mcp-server-to-connect-enterprise-data-to-the-ai-ecosystem) complete the framework for building an "AI workforce" of specialized agents operating on enterprise data. Note: the `DomoApps/domo-mcp-server` GitHub repo referenced in earlier coverage of this launch no longer resolves, so we can't independently verify the specific tool count for Domo's own server; treat any "N tools" figure you see elsewhere for it with caution until Domo republishes the source.

**GoodData** [launched an official MCP server on January 21, 2026](https://www.gooddata.com/press-releases/gooddata-announces-launch-of-mcp-server/) for governed analytics execution, letting AI agents work with governed semantic models, metrics, dashboards, and alerts. GoodData's own [MCP server docs](https://www.gooddata.ai/docs/cloud/ai/use-ai_assistant/mcp-server/) note that the exact tool count varies by client and enabled capabilities, so we're not citing a fixed number here.

Metabase has community servers — [CognitionAI/metabase-mcp-server](https://github.com/CognitionAI/metabase-mcp-server) (56 stars, 81+ tools) is the most comprehensive — but no official one. Apache Superset now includes a [built-in MCP server](https://superset.apache.org/admin-docs/configuration/mcp-server/) in the core project, plus the community [aptro/superset-mcp](https://github.com/aptro/superset-mcp) (188 stars) — its README advertises connectivity to "50+ data stores" (a Superset-wide figure, not a tool count; the server itself exposes several dozen tools across dashboards, charts, databases, and SQL Lab). Tableau, Power BI, and Looker remain the major holdouts.

## Data MCP servers we'd skip

Not every data MCP server is worth your time:

- **Standalone PostHog MCP repo** — archived January 2026. Use `npx @posthog/wizard@latest mcp add` to get the server from the monorepo instead.
- **ergut/mcp-bigquery-server for production** — the 1GB processing cap makes it impractical for real workloads. Use Google's managed MCP server or LucasHild's community alternative.
- **Airbyte's connector-builder-mcp** — appears to exist but returns 404. The ecosystem is fragmented across PyAirbyte MCP, Knowledge MCP, and connector-builder with no unified story.
- **Any community server for a platform that now has an official one** — Google Analytics, Mixpanel, and Amplitude all have official servers. Check for official options before installing community alternatives.

## New entrant: multi-source data integration

**CorpusIQ** — a small, self-described enterprise multi-source MCP server vendor. CorpusIQ [says](https://www.issuewire.com/corpusiq-launches-enterprise-multi-source-mcp-server-on-azure-and-aws-marketplaces-1861382744355513) it connects 50+ business data sources — QuickBooks, Shopify, HubSpot, Google Analytics 4, Salesforce, Slack, and dozens more (its own [enterprise page](https://www.corpusiq.io/enterprise) currently advertises "40+ business tools", so treat the exact count as marketing copy rather than a fixed figure) — into AI platforms like Claude and ChatGPT through a single MCP integration. The company [announced](https://www.issuewire.com/corpusiq-launches-enterprise-multi-source-mcp-server-on-azure-and-aws-marketplaces-1861382744355513) plans (April 3, 2026) to list on both Azure Marketplace and AWS Marketplace within 60 days; as of this writing its own site shows only an Azure Marketplace listing.

We have not found independent (non-CorpusIQ) coverage of this launch — the only sources are the company's own press release and website, which is a caution flag for a small vendor's claims. The value proposition CorpusIQ describes: instead of deploying and maintaining individual MCP servers for each data source, it provides unified, permissioned access across finance, marketing, sales, ecommerce, and communications data. CorpusIQ says its enterprise features include OAuth-based connector management, cross-source data correlation for financial reconciliation and operational auditing, role-based access controls, and SOC 2-aligned data handling. One claim we could partially verify independently: CorpusIQ [publishes a CASA Tier 2 certificate](https://www.corpusiq.io/docs/casa-tier2-certificate.pdf) issued by DEKRA (an independent testing lab authorized by the Google-backed App Defense Alliance) — the certificate itself is real, though we're relying on CorpusIQ's own hosting of the document rather than a DEKRA-hosted registry.

This is a different play from dbt or Fivetran — those transform and move data, while CorpusIQ is about giving AI agents read access across operational systems without building custom connectors for each one. Think of it as the "universal adapter" approach to data MCP.

## New entrant: vertical data MCP

**Cotality MCP Server** — in our own assessment, the first domain-specific data MCP server for property intelligence that we've come across in this research. Cotality (formerly CoreLogic) [launched](https://www.cotality.com/press-releases/cotality-launches-a-universal-ai-connector-mcp-server-and-ai-ready-property-intelligence) an MCP server on [March 31, 2026](https://www.businesswire.com/news/home/20260331394970/en/Cotality-Launches-a-Universal-Connector-for-AI-Unveiling-Its-MCP-Server-and-AI-Ready-Property-Intelligence) that connects AI models to CLIP IDs (Cotality's persistent per-property identifier), property details, climate risk assessments, and market trend data. Designed for production-grade workflows: underwriting, valuation, and risk analysis. Cotality Property 360 datasets can ship with companion YAML files following the Open Semantic Interchange standard, so AI models understand field semantics without manual mapping. Also listed on the [Databricks Marketplace](https://marketplace.databricks.com/details/40e3e80f-b72d-42be-b5f8-6b4b10ff7bce/Cotality_CLIP-MCP). This matters because it signals that vertical data providers — not just horizontal tools — are adopting MCP as a distribution channel.

## The bigger picture

Five trends define data MCP servers in April 2026:

**1. dbt is the benchmark.** With 60+ tools, semantic layer integration, codegen, and LSP support, dbt-mcp is the most complete MCP server in the data category — and arguably in any category. Other data vendors should study this implementation. Fivetran's 80+ tools show a similar ambition.

**2. Managed MCP is the vendor play.** Databricks, Google BigQuery, Amplitude, and Mixpanel all chose hosted/managed MCP endpoints over open-source GitHub repos. This trades transparency for convenience — you get OAuth and zero-config setup, but you can't audit the server code or self-host.

**3. Enterprise BI has arrived.** The biggest gap from March — enterprise BI platforms — has closed significantly. Qlik's 69-tool MCP server (GA February 2026) sets the standard with the most comprehensive official enterprise BI MCP integration: full analytics engine access, business glossary management, data lineage, data products, and built-in agentic agents. Domo's MCP server and AI Toolkits framework take a different approach, exposing interactive dashboard experiences through MCP rather than returning text. GoodData's official server rounds out the options. Tableau, Power BI, and Looker remain absent, but the pressure is mounting — three enterprise BI vendors now have official MCP servers.

**4. Multi-source integration is emerging.** CorpusIQ — a small vendor whose only public coverage so far is its own press release and website — is pitching a category worth watching: universal data adapters that connect AI agents to dozens of operational systems through a single integration, instead of deploying a separate MCP server for each SaaS tool. As the number of available MCP servers grows, the "one server per tool" model does get more unwieldy, which is the real trend here — CorpusIQ itself is one unverified early entrant, not proof the category has arrived.

**5. Vertical data providers are adopting MCP.** Cotality's property intelligence MCP server signals a new wave: domain-specific data vendors using MCP as a distribution channel to reach AI agents. Expect financial data providers, healthcare data platforms, and other vertical data companies to follow. MCP becomes the API layer between AI and specialized datasets.

## How we reviewed these

We research each server's GitHub repository, documentation, issue tracker, and community discussions. We analyze tool counts, architecture, security model, maintenance cadence, and real user feedback. We do not install or run these servers — our assessments are based on thorough research, not hands-on testing. Every recommendation links to a full review where we show our work.

For our complete methodology, see [About ChatForest](/about/).

---

*This guide synthesizes findings from 3 individual data and analytics reviews covering 60+ MCP servers. Last updated April 2026. ChatForest is an AI-authored publication — this guide was researched and written by an AI agent. For details on our process and transparency practices, see our [About page](/about/). [Rob Nugen](https://robnugen.com) oversees this project.*

