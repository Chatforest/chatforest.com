# Data Quality & Data Observability MCP Servers — Monte Carlo, Bigeye, Elementary, Validio, Qualytics, and More

> Data quality and data observability MCP servers reviewed: Monte Carlo mc-agent-toolkit (77 stars, 14 skills, OAuth 2.1, official), Bigeye (47+ tools, official), Elementary (cloud MCP, dbt-native), Validio (hosted, commercial), Qualytics (Data Control Layer, AgentQ), Acceldata xLake MCP-DC (distributed compute), Atlan agent-toolkit (29 stars, 15 tools), Delpha (13 tools, contact data quality), Dingo (687 stars, 100+ metrics, AI data evaluation). Rating: 3.5/5.


Data quality and data observability have become critical concerns as organizations rely on data pipelines feeding AI systems, analytics, and business decisions. MCP servers in this space let AI agents monitor data health, investigate incidents, trace lineage, validate schemas, and automate remediation — all through natural language. The ecosystem is splitting between **commercial platforms with official MCP servers** (Monte Carlo, Bigeye, Validio, Qualytics) and the **open-source data quality stack** (Great Expectations, Soda, dbt tests) which has almost no MCP representation. Part of our **[Data & Databases MCP category](/categories/data-databases/)**.

This review covers **data observability platforms** (Monte Carlo, Bigeye, Elementary, Validio, Acceldata), **data quality platforms** (Qualytics, Delpha, Dingo), **data catalog platforms with quality features** (Atlan), **dbt-adjacent quality tools** (dbt MCP, Data Product Hub), and the landscape of missing open-source players. For data governance and compliance, see our [Compliance & Data Governance MCP Servers](/reviews/compliance-data-governance-mcp-servers/) review. For data pipeline and ETL tooling, see [Data Pipeline & ETL MCP Servers](/reviews/data-pipeline-etl-mcp-servers/).

The headline finding: **Monte Carlo has the most sophisticated MCP integration** with 14 AI skills covering the full incident lifecycle. **Bigeye has the most tools** (47+) with unique agent lineage tracking. **The open-source data quality stack is almost entirely absent** — Great Expectations, Soda, Anomalo, and Lightup have no MCP servers. **Commercial platforms dominate** this category, with hosted/remote MCP emerging as the default deployment model. **Acceldata's xLake MCP-DC is the most architecturally ambitious** approach, introducing distributed compute for cross-lake policy enforcement.

## Data Observability Platforms

### Monte Carlo (Official)

| Server | Stars | Language | License | Tools/Skills | Official |
|--------|-------|----------|---------|-------|----------|
| mc-agent-toolkit | ~77 | Python | Apache 2.0 | 14 skills | Yes |

**Monte Carlo's mc-agent-toolkit** ([monte-carlo-data/mc-agent-toolkit](https://github.com/monte-carlo-data/mc-agent-toolkit), 77 stars, Apache 2.0, Python, v1.8.2 April 2026) is the most comprehensive data observability MCP offering. Unlike simple tool-based servers, Monte Carlo bundles **14 AI skills** — each an orchestrated workflow combining multiple API calls:

- **Asset Health** — structured trust reports: status (healthy/degraded/unhealthy), active alerts, monitoring coverage, upstream dependency health
- **Incident Response** — orchestrates triage, investigation, root cause identification, remediation, and monitoring to prevent recurrence
- **Automated Triage** — scores alerts, runs deep troubleshooting on high-signal ones, classifies, and takes action
- **Analyze Root Cause** — systematic investigation using TSA (Time Series Analysis) root cause analysis
- **Monitoring Advisor** — recommends monitoring configurations based on table usage patterns
- **Proactive Monitoring** — sets up monitoring before issues occur
- **Prevent** — blocks pipeline execution when data quality thresholds are breached
- **Generate Validation Notebook** — creates monitors-as-code with validation queries
- **Push Ingestion** — metadata and metric ingestion from external systems
- **Storage Cost Analysis** — identifies cost optimization opportunities
- **Performance Diagnosis** — query and pipeline performance investigation
- **Remediation** — guided fix workflows for known issue patterns
- **Tune Monitor** — adjusts sensitivity and thresholds of existing monitors
- **Connection Auth Rules** — manages data source connection authentication

Authentication is **OAuth 2.1** via Monte Carlo's remote MCP server (HTTP transport), with header-based auth for legacy clients. Requires an Editor role or higher on a Monte Carlo account. The plugin bundles the MCP server, hooks, and agent-specific capabilities — no separate configuration needed.

Supported clients: Claude Code, Cursor, Copilot CLI, OpenCode, Codex. Monte Carlo is the most widely deployed data observability platform, using ML to learn normal data patterns and alerting on freshness, volume, schema, distribution, or lineage deviations.

### Bigeye (Official)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| bigeye-mcp-server | ~1 | Python | — | 47+ tools | Yes |

**Bigeye MCP Server** ([bigeyedata/bigeye-mcp-server](https://github.com/bigeyedata/bigeye-mcp-server), 1 star, Python, 59 commits) provides the **deepest tool coverage** of any data quality MCP server with **47+ tools across 8 categories**:

- **Issue Management (8+ tools)** — `list_issues`, `get_issue`, `search_issues`, `list_related_issues`, `list_table_issues`, `update_issue`, `create_incident`, `delete_incident_members`, `get_resolution_steps`
- **Metrics & Quality (6 tools)** — `list_table_metrics`, `list_table_level_metrics`, `create_metric`, `get_table_profile`, `create_profile_job`, `get_profile_job_status`
- **Data Lineage (5+ tools)** — `get_lineage_graph`, `get_lineage_node`, `list_lineage_node_issues`, `search_lineage_nodes`, `lineage_explore_catalog`, `lineage_delete_node`
- **Root Cause & Impact Analysis (4 tools)** — `get_upstream_root_causes`, `get_downstream_impact`, `get_issue_lineage_trace`, `list_report_upstream_issues`
- **Agent Lineage Tracking (5 tools)** — `lineage_track_data_access`, `lineage_commit_agent`, `lineage_get_tracking_status`, `lineage_clear_tracked_assets`, `lineage_cleanup_agent_edges` — **unique feature** that tracks which data assets AI agents access
- **Sensitive Data Scanning (2 tools)** — `list_data_classes`, `get_scan_findings`
- **Data Dimensions (7 tools)** — full CRUD for data quality dimensions and coverage metrics
- **Tags (7 tools)** — entity tagging and management
- **System (3 tools)** — `get_health_status`, `list_resources`, `list_data_sources`

Authentication via API key (`BIGEYE_API_KEY`, `BIGEYE_BASE_URL`, `BIGEYE_WORKSPACE_ID`). Supports Docker-based deployment (long-lived or ephemeral containers) and multi-environment setup. The **agent lineage tracking** capability is architecturally notable — it records which data assets AI agents read during automated workflows, creating an audit trail for AI-driven data access.

### Elementary (Cloud MCP)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| Elementary MCP Server | — | Hosted | — | Multiple | Yes |

**Elementary** ([elementary-data.com](https://www.elementary-data.com/), main repo 2.3K stars, Apache 2.0) is a dbt-native data observability platform that ships a hosted MCP server through its cloud product. The MCP server exposes:

- **Discovery & Lineage** — explore all data assets, metadata, and end-to-end lineage including column-level relationships
- **Tests & Coverage** — test results, coverage gaps, and anomaly detection across pipelines
- **Health & Incidents** — real-time incident management, health scores, historical incident patterns

The Elementary MCP Server works with dbt metadata and tests, exposing lineage and health context for assets in Snowflake, BigQuery, Databricks, and similar cloud data platforms. Supported integrations include Claude Desktop, Cursor, and dbt-MCP for chained workflows.

Elementary is the strongest **dbt-native** option in this category. The platform offers both cloud and open-source options, though the MCP server requires the cloud product. The open-source `elementary` CLI (2.3K stars) and `dbt-data-reliability` package power the underlying data quality detection and metadata collection.

### Validio (Hosted MCP)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| Validio MCP Server | — | Hosted | Commercial | Multiple | Yes |

**Validio** ([validio.io](https://validio.io/)) provides a hosted MCP server that combines catalog, lineage, data quality incidents, and validator recommendations into a single interface for AI assistants. Key capabilities:

- **Incident inspection and management** — query data quality incidents across the platform
- **Catalog asset listing and filtering** — browse and search data assets
- **Lineage integration** — automated data flow relationships for root cause analysis
- **Data profiling** — table schemas, distributions, and patterns
- **Validator recommendations** — AI-powered suggestions for monitoring setup

The server is hosted by Validio, requiring only client-side connection. Supports Claude Code, Cursor, Gemini CLI, and any MCP-enabled assistant. Validio recommends enhancing agent workflows by creating `CLAUDE.md` or `GEMINI.md` files with business-specific instructions, naming conventions, and root cause analysis procedures. Documentation at [docs.validio.io](https://docs.validio.io/docs/validio-mcp-server). Available to existing Validio customers.

### Acceldata xLake MCP-DC

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| xLake MCP-DC Server | — | — | Commercial | — | Yes |

**Acceldata** ([acceldata.io](https://www.acceldata.io/)) introduced the **xLake MCP-DC Server** (MCP with Distributed Compute) at Autonomous 25 — described as the first distributed data control plane purpose-built for intelligent agents. Unlike basic MCP implementations that treat context as static metadata, MCP-DC is dynamic and executable:

- **Distributed Policy Compute Engine** — executes governance, quality, and security policies natively on each platform (Snowflake, Databricks, on-prem), eliminating bottlenecks of centralized execution
- **Cross-Lake Coordination Protocol** — enables agents to operate seamlessly across data lakes, warehouses, and pipelines, enriching context and enhancing policy accuracy

This is the most architecturally ambitious MCP approach in the data quality space. However, it is a commercial product with no public GitHub repository. Generally available as of mid-2025.

## Data Quality Platforms

### Qualytics (Data Control Layer + MCP)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| Qualytics MCP Server | — | Hosted (SSE) | Commercial | Multiple | Yes |

**Qualytics** ([qualytics.ai](https://qualytics.ai/)) launched its **Data Control Layer** in April 2026, including AgentQ and MCP server support. The MCP server exposes the entire Qualytics data quality infrastructure as callable tools:

- **Triggering scans and quality checks**
- **Retrieving quality scores and anomaly context**
- **Initiating remediation workflows**
- **Natural-language rule authoring** — create data quality rules through conversation
- **Anomaly investigation** — investigate detected issues with AI assistance

The MCP server uses HTTP with Server-Sent Events (SSE) transport. External copilots (ChatGPT, Claude, Microsoft Copilot) access governed quality signals through MCP, while autonomous systems use the Qualytics API for real-time threshold enforcement. Available to all Qualytics customers.

### Delpha Data Quality MCP

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| DelphaMCP | ~2 | Python | MIT | 13 tools | Yes |

**Delpha** ([Delpha-Assistant/DelphaMCP](https://github.com/Delpha-Assistant/DelphaMCP), 2 stars, MIT, Python, v0.1.19) is an AI-powered **contact data quality** platform providing 13 MCP tools for validation and enrichment:

- **Email** — `findAndValidateEmail`, `getEmailResult`, `getEmailInsights` (signature-based field extraction)
- **Address** — `findAndValidateAddress`, `getAddressResult`
- **Website** — `findAndValidateWebsite`, `getWebsiteResult`
- **LinkedIn** — `findAndValidateLinkedin`, `getLinkedinResult`, `submitLinkedinImport`, `getLinkedinImportResult`, `submitLinkedinScraper`, `getLinkedinScraperResult`
- **Phone** — `findAndValidatePhone`, `getPhoneResult`
- **Name** — `findAndValidateName`, `getNameResult`
- **Legal ID** — `findAndValidateLegalID`, `getLegalIDResult` — company identifier validation across countries

Authentication via OAuth2 (client ID and secret). This is a niche but useful tool for CRM data quality — validating and enriching contact fields, deduplication with AI scoring, and bulk LinkedIn data ingestion. More suited to customer data platforms than general data pipeline monitoring.

### Dingo (AI Data Quality Evaluation)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| Dingo | ~687 | Python | Apache 2.0 | MCP server | Yes |

**Dingo** ([MigoXLab/dingo](https://github.com/MigoXLab/dingo), 687 stars, Apache 2.0, Python) is a comprehensive AI data, model, and application quality evaluation tool designed for ML practitioners. It includes a built-in MCP server exposing evaluation capabilities:

- **100+ evaluation metrics** across pretrain text (completeness, effectiveness, similarity, security), SFT data (3H evaluation: honest, helpful, harmless), RAG assessment (faithfulness, context precision, answer relevancy), hallucination detection (HHEM-2.1-Open), multimodal quality (image-text relevance), and security (PII detection, toxicity)
- **Hybrid evaluation** — rule-based (30+ built-in rules for speed) and LLM-based (GPT-4o or compatible) assessment
- MCP server supports SSE and stdio transport, integrates with Claude Desktop and Cursor

Dingo targets **AI/ML data quality** specifically — evaluating training data, fine-tuning datasets, and production AI outputs. It's the highest-starred open-source project in this review and the most relevant for teams building or validating AI training pipelines.

## Data Catalog Platforms with Quality Features

### Atlan Agent Toolkit

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| agent-toolkit | ~29 | Python | MIT | 15 tools | Yes |

**Atlan** ([atlanhq/agent-toolkit](https://github.com/atlanhq/agent-toolkit), 29 stars, MIT, Python, v0.3.3 February 2026) provides a data catalog MCP server with quality monitoring capabilities. **15 MCP tools** (12 enabled by default, 3 via feature flags):

- **Search & Discovery** — semantic search across data assets
- **Lineage** — upstream/downstream tracing
- **Quality Monitoring** — create and schedule validation rules, surface quality issues
- **Glossary & Governance** — term management, Data Mesh organization with domains and data products
- **Metadata Updates** — userDescription, certificateStatus, readme

Authentication via OAuth at `mcp.atlan.com/mcp` — no API keys required for the Claude Code Plugin. Also available as an official Docker image. Atlan positions itself as "the official Atlan plugin for Claude Code." While Atlan is primarily a data catalog, the quality monitoring and validation rule creation capabilities make it relevant for teams who want unified catalog + quality in one MCP interface.

## dbt-Adjacent Quality Tools

### dbt MCP Server

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| dbt-mcp | ~544 | Python | Apache 2.0 | 50+ tools | Yes |

**dbt MCP** ([dbt-labs/dbt-mcp](https://github.com/dbt-labs/dbt-mcp), 544 stars, Apache 2.0, Python, v1.15.1 April 2026) is the official dbt MCP server with 50+ tools across 9 categories. Data quality-relevant tools include:

- `test` — runs tests to validate data and model integrity
- `get_model_health` — health signals: run status, test results, upstream source freshness
- `get_model_performance` — execution history with optional test result inclusion
- `get_job_run_error` — error/warning details from job runs

While primarily a dbt project management tool, these quality-focused tools make it relevant for teams using dbt's built-in testing framework (dbt tests, dbt-expectations, dbt-utils) as their primary data quality layer. The server also provides semantic layer queries, column-level lineage, and semantic search for model discovery.

### Data Product Hub

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| data-product-hub | ~8 | Python | MIT | 8 tools | No |

**Data Product Hub** ([armalite/data-product-hub](https://github.com/armalite/data-product-hub), 8 stars, MIT, Python) is a composite MCP server aggregating data product insights from dbt, GitHub, Monte Carlo, and DataHub into a unified interface. Quality-relevant tools:

- `assess_data_product_quality` — quality scoring for dbt models
- `check_metadata_coverage` — project-wide metadata assessment
- `analyze_dbt_model_with_ai` — AI-powered analysis including quality recommendations
- `get_project_lineage` — dependency mapping

Uses GitHub App authentication. Future integrations planned for Monte Carlo and DataHub. Early-stage project focused on dbt repository quality assessment.

## What's Missing

The most significant gap in this category is the **absence of the open-source data quality stack from MCP**:

- **Great Expectations** — the most popular open-source data validation framework has **no MCP server**. No official or major community implementation exists.
- **Soda** (Soda Core v4, data contracts) — **no MCP server**. Despite Soda Core's SQL-based checks being well-suited to MCP tool exposure, neither official nor community implementations exist.
- **Anomalo** — AI-powered anomaly detection platform, **no MCP server** despite being a 2026 market leader.
- **Lightup** — continuous data quality monitoring, **no MCP server**.
- **Sifflet** — data observability with lineage, **no MCP server**.
- **Metaplane** (acquired by Datadog April 2025) — **no dedicated MCP server**. Datadog has a general observability MCP but not Metaplane-specific data quality tools.
- **DataKitchen** — open-source DataOps TestGen and DataOps Observability have **no MCP server** despite active development and Apache 2.0 licensing.
- **DQLabs** — **no MCP server**.

Other gaps:
- **No data contract validation MCP** — despite data contracts gaining traction (Soda v4, Atlan, OpenDataMesh), no MCP server focuses specifically on contract validation
- **No schema evolution tracking** — monitoring breaking schema changes via MCP
- **No cross-platform data quality aggregation** — a single MCP that queries quality status across Monte Carlo + Great Expectations + dbt tests simultaneously
- **No data freshness monitoring as standalone** — freshness is embedded in larger platforms but no lightweight MCP exists for just checking "when was this table last updated?"

## Rating: 3.5 / 5

**Strong commercial coverage, weak open-source representation.** Monte Carlo and Bigeye lead with sophisticated official MCP servers that go beyond basic API wrappers — Monte Carlo's skill-based architecture and Bigeye's agent lineage tracking represent genuinely new patterns in how AI agents interact with data quality platforms. The hosted MCP model (Validio, Qualytics, Elementary, Acceldata) reduces friction but locks users into specific commercial platforms.

The major weakness is the **complete absence of open-source data quality tools** from MCP. Great Expectations and Soda together represent the majority of open-source data quality usage, yet neither has any MCP implementation. This means teams using the modern open-source data stack (dbt + Great Expectations/Soda + Airflow) cannot access their quality layer through AI agents without building custom tooling.

**Bottom line:** If you're already on Monte Carlo or Bigeye, the MCP experience is excellent. If you're using open-source data quality tools, you'll be waiting — or building your own MCP wrapper. The category will likely improve rapidly as data observability vendors compete on AI agent integration, but today it's a commercial-first story.

