# IBM MCP Servers — watsonx.data, IBM i, Data Intelligence, webMethods, QRadar, and More

> IBM's MCP server ecosystem reviewed: data-intelligence (70+ tools, v1.0.2), IBM i/AS400 (59 stars, v0.5.1), watsonx.data lakehouse (32 tools, v0.1.3), webMethods integration (v1.3.2), QRadar SIEM (27 tools), FileNet content services (4 configs). All Apache-2.0. Rating: 3.5/5.


IBM operates the largest enterprise software portfolio in the world — from mainframes and AS/400 systems to cloud data lakehouses, API gateways, SIEM platforms, and governance tooling. In 2025 and early 2026, IBM began systematically publishing MCP servers across this portfolio. The result is the most diverse enterprise MCP ecosystem in existence: 13+ official servers spanning five decades of product lines, all Apache-2.0 licensed, all targeting specific enterprise use cases. Part of our **[Enterprise Software MCP category](/categories/enterprise/)**.

The headline finding: **IBM's MCP coverage is broader than any vendor except Microsoft and AWS — but deeply uneven.** The **watsonx.data Intelligence server** (70+ tools, v1.0.2) is genuinely production-ready. The **IBM i server** (v0.5.1, TypeScript, SQL-powered) is the most technically mature individual server. The **watsonx.data lakehouse server** covers the full engine-management-to-query pipeline. But most other servers carry explicit "not for production" warnings, lack formal releases, or have star counts in single digits. IBM also publishes across multiple GitHub organizations (IBM/, instana/, ibmbpm/, ibm-ecm/) — a fragmentation that makes discovery harder than it should be.

Two IBM products — **IBM Instana** (100+ tools, enterprise observability) and **IBM OpenPages** (official, ontology-based GRC server) — have dedicated coverage in our [monitoring and observability roundup](/reviews/monitoring-observability-mcp-servers/) and [compliance and audit automation roundup](/reviews/compliance-audit-automation-mcp-servers/) respectively. This review covers the rest of IBM's MCP portfolio.

---

## Overview: IBM's MCP Portfolio

IBM's MCP servers live under the [IBM/mcp](https://github.com/IBM/mcp) monorepo (~373 stars), which serves as a catalog index linking to ~29 individual servers across IBM's product lines. Each server ships as a separate repository. Nearly all are Apache-2.0.

| Server | Repo | Stars | Version | Status |
|--------|------|-------|---------|--------|
| watsonx.data Intelligence | IBM/data-intelligence-mcp-server | 17 | v1.0.2 (Apr 2026) | Production-ready |
| IBM i / AS400 | IBM/ibmi-mcp-server | 59 | v0.5.1 (Apr 2024) | Stable |
| watsonx.data Lakehouse | IBM/ibm-watsonxdata-mcp-server | 6 | v0.1.3 (Apr 2025) | Early/Active |
| webMethods Integration | IBM/WxMCPServer | 19 | v1.3.2 (Feb 2026) | Active |
| QRadar SIEM | IBM/qradar-mcp | 2 | No releases (Phase 1) | MVP |
| FileNet Content Services | ibm-ecm/ibm-content-services-mcp-server | 11 | No releases | Early |
| Business Automation Workflow | ibmbpm/ibm-baw-mcp-server | 7 | No releases | Early |
| Master Data Management | IBM/mdm-mcp-server | 3 | No releases | Early |
| Storage Scale | IBM/ibm-storage-scale-mcp-server | 4 | No releases | Pre-release |
| Guardium Data Protection | IBM/gdp-mcp-server | 1 | No releases | MVP only |
| watsonx.governance Catalog | IBM/ibm-watsonx-gov-catalog-mcp-server | 1 | No releases | Early |
| IBM Instana | instana/mcp-instana | 20 | No releases | Active (see [observability roundup](/reviews/monitoring-observability-mcp-servers/)) |
| IBM OpenPages | IBM/ibm-openpages-mcp-server | 0 | No releases | Active (see [compliance roundup](/reviews/compliance-audit-automation-mcp-servers/)) |

**Not covered here:** [IBM ContextForge](https://github.com/IBM/mcp-context-forge) (3,655 stars, v1.0.0 GA May 2026) is IBM's MCP gateway/federation proxy — it sits in front of any MCP, A2A, or REST API and adds auth, RBAC, rate limiting, and observability. It is not an IBM product connector and deserves its own review. IBM's [mcp-cli](https://github.com/IBM/mcp-cli) (~2,000 stars) is a multi-provider client, also not covered here.

---

## watsonx.data Intelligence — Flagship (70+ Tools, v1.0.2)

| | |
|---|---|
| **Repo** | [IBM/data-intelligence-mcp-server](https://github.com/IBM/data-intelligence-mcp-server) |
| **Stars** | ~17 |
| **Latest version** | v1.0.2 (April 24, 2026) |
| **PyPI package** | `ibm-watsonx-data-intelligence-mcp-server` |
| **License** | Apache-2.0 |
| **Requires** | IBM watsonx.data Intelligence SaaS, or Cloud Pak for Data 5.2.1+ |

The watsonx.data Intelligence MCP server is IBM's most capable and actively maintained MCP server. It maps to IBM's data governance and intelligence platform — the product formerly known as Watson Knowledge Catalog — and exposes 70+ tools across 11 service domains covering the full data governance lifecycle.

**70+ tools across 11 domains:**

- **Data Product Service (18 tools)** — create, publish, search, and subscribe to data products; contract management; full lifecycle of governed data product delivery
- **Metadata Enrichment Service (10 tools)** — create and execute enrichment areas, automated profiling, AI-assisted term generation
- **Search Service (7 tools)** — dynamic asset search, container listing, asset lookup by ID or lineage
- **Reporting / Text-to-SQL (5 tools)** — natural language to SQL translation, query execution against governed datasets, reporting
- **Lineage Service (5 tools)** — graph traversal, version comparison, asset search by lineage relationships
- **Data Quality Service (5 tools)** — quality metrics retrieval, find and run quality rules, create rules, set validation relations
- **Workflow Service (6 tools)** — governance task inbox, approval workflows, task routing
- **Glossary Service (4 tools)** — explain business terms, get linked terms, CSV import/export for bulk glossary management
- **Metadata Import Service (4 tools)** — create and run metadata import jobs from external catalogs
- **Projects Service (2 tools)** — create projects, manage collaborators
- **Connections/Data Protection (3 tools)** — copy connections, create data protection rules, search governance artifacts

**What makes this the flagship server:** The active release cadence (v1.0.2 as of April 2026, with multiple prior releases) signals real production intent. The text-to-SQL capability lets AI agents translate governance questions into executable queries against IBM Cloud data assets. The data product service tools cover a workflow that enterprise data teams run daily but that has historically required navigating multiple UI screens.

**Limitations:** Low star count (17) suggests enterprise adoption rather than broad community discovery. Requires either IBM watsonx.data Intelligence SaaS or Cloud Pak for Data 5.2.1+ — not a standalone deployment. The 70+ tool count may require careful filtering to avoid context window pressure in agents that load all tools simultaneously.

**Target audience:** Data governance teams, data stewards, and CDO offices at enterprises running IBM Cloud Pak for Data or watsonx.data Intelligence SaaS.

---

## IBM i / AS400 — Most Mature Individual Server (v0.5.1)

| | |
|---|---|
| **Repo** | [IBM/ibmi-mcp-server](https://github.com/IBM/ibmi-mcp-server) |
| **Stars** | ~59 |
| **Latest version** | v0.5.1 (April 2024) |
| **npm package** | `@ibm/ibmi-mcp-server` |
| **License** | Apache-2.0 |
| **Requires** | Mapepire gateway on IBM i (port 8076) |

The IBM i MCP server is the most starred individual IBM MCP server and the most technically mature in terms of versioning. It targets IBM i systems (formerly AS/400, iSeries) — the platform running everything from SAP Business One backends to major banking transaction processing systems worldwide. The architecture is elegant: tools are defined in YAML files by category, all executing via the Mapepire WebSocket SQL gateway, which modernizes Db2 for i access without requiring JDBC or legacy connectors.

**Tool categories (YAML-defined):**
- **Performance** — `system_status`, `system_activity`, CPU/memory metrics, active job monitoring
- **Security operations** — user profile analysis, authority inspection, security event review
- **Library list security** — security assessment of library lists (a uniquely IBM i concern)
- **System administration** — system metadata, administration operations
- **PTF management** — Program Temporary Fix tracking, patch status, fix validation (a critical IBM i operational workflow)
- **Developer tools** — object statistics, dependency analysis, application topology
- **CLI distribution** — same SQL engine also ships as `@ibm/ibmi-cli` for standalone terminal use

**Why this matters:** IBM i systems run an estimated $4.5 trillion in annual commerce transactions and are present at 95% of Fortune 500 companies that process high-volume transactions. The gap between "modern AI tooling" and "IBM i operations" has been historically enormous. This server begins to close it — letting AI agents query system health, inspect user authorities, and review PTF status without requiring green-screen terminal expertise.

**Prerequisite:** Mapepire must be running on the IBM i system. Mapepire is an open-source WebSocket-based SQL gateway for Db2 for i (also from IBM). If your shop doesn't already run Mapepire, that's an installation prerequisite.

**Limitations:** v0.5.1 was released April 2024 — the server may lag behind MCP spec evolution (current spec: 2025-06-18). YAML-defined tools are flexible but require reading the repository to understand the full tool surface. No write tools confirmed in the published categories (read/monitor focused).

**Target audience:** IBM i operations teams (sysadmins, DBAs, DevOps) managing AS/400/IBM i estates who want AI-assisted monitoring, security auditing, and job management.

---

## watsonx.data Lakehouse — Full Engine Pipeline (32 Tools, v0.1.3)

| | |
|---|---|
| **Repo** | [IBM/ibm-watsonxdata-mcp-server](https://github.com/IBM/ibm-watsonxdata-mcp-server) |
| **Stars** | ~6 |
| **Latest version** | v0.1.3 (April 2025) |
| **PyPI package** | `ibm-watsonxdata-mcp-server` |
| **License** | Apache-2.0 |
| **Requires** | IBM watsonx.data on IBM Cloud (IBM Cloud IAM API key + instance CRN) |

The watsonx.data lakehouse MCP server covers IBM's open lakehouse data platform — the Presto and Spark compute layer that sits over object storage in IBM Cloud. Its 32 tools span the complete engine-management-to-query lifecycle.

**32 tools across 6 domains:**
- **Engine management (11 tools)** — `list_engines`, create/pause/resume/restart/scale Presto engines, create/update/pause/resume Spark engines
- **Catalog and schema (7 tools)** — `list_schemas`, `list_tables`, `describe_table`, `create_schema`, `rename_table`, `add_columns`, `rename_column`
- **Query execution (5 tools)** — `execute_select`, `execute_insert`, `execute_update`, `explain_query`, `explain_analyze_query`
- **Spark applications (4 tools)** — `submit_spark_application`, `list_spark_applications`, `get_spark_application_status`, `stop_spark_application`
- **Data ingestion (4 tools)** — `create_ingestion_job`, `list_ingestion_jobs`, `get_ingestion_job`, `delete_ingestion_job`
- **Platform (1 tool)** — `get_instance_details`

**Notable capability:** The `explain_analyze_query` tool lets AI agents inspect query execution plans and identify performance bottlenecks — a meaningful step beyond simple SQL execution.

**Limitations:** IBM Cloud only — no on-premises or Cloud Pak for Data support confirmed. No read-only mode: full credentials are required for engine management operations. v0.1.x signals early-stage, and 6 stars reflect limited community discovery. Both stdio and streamable HTTP transports are supported.

**Target audience:** Data engineers working with IBM watsonx.data lakehouses on IBM Cloud who want AI-assisted cluster management and query operations.

---

## webMethods Integration — Dynamic API Gateway Exposure (v1.3.2)

| | |
|---|---|
| **Repo** | [IBM/WxMCPServer](https://github.com/IBM/WxMCPServer) |
| **Stars** | ~19 |
| **Latest version** | v1.3.2 (February 2, 2026) |
| **License** | Apache-2.0 |
| **Requires** | IBM webMethods Hybrid Integration v11.1+ |

IBM acquired Software AG's webMethods integration platform in 2024. The webMethods MCP server (WxMCPServer) takes a distinctive approach: rather than defining a fixed tool list, it dynamically exposes whatever APIs are already published in your webMethods API Gateway catalog as MCP tools. Every API your integration platform manages becomes an AI-accessible tool automatically.

**Architecture:** The server connects to the webMethods API Gateway, enumerates the API catalog at startup, and generates MCP tool definitions for each published API. API key and OAuth authentication are both supported. When a new API is published to the gateway, it appears as a new MCP tool without any server-side changes.

**Target audience:** Integration architects and platform teams using IBM webMethods Hybrid Integration (IWHI) who want AI agents to access business services through the established API governance layer. This is particularly useful in organizations where webMethods is the canonical integration hub — every downstream service already has an API in the catalog.

**Limitations:** Requires webMethods Hybrid Integration v11.1 or later. Dynamic tool generation means the tool surface changes as the API catalog changes — agents need to handle this variability. No fixed tool count (depends entirely on your API catalog). 19 stars, though the February 2026 release (v1.3.2) shows active maintenance.

---

## QRadar SIEM — 27 Read-Only Security Tools (Phase 1)

| | |
|---|---|
| **Repo** | [IBM/qradar-mcp](https://github.com/IBM/qradar-mcp) |
| **Stars** | ~2 |
| **Version** | No formal releases (Phase 1) |
| **License** | Apache-2.0 |
| **Requires** | IBM QRadar SIEM deployment |

IBM QRadar is one of the largest enterprise SIEM platforms worldwide. The QRadar MCP server (Phase 1) is read-only — 27 tools for querying QRadar state without modifying it. Write operations are planned for Phase 2.

**27 read-only tools across 8 domains:**
- **Offense management** — list and inspect security offenses, offense sources and destinations
- **Reference data** — query reference sets, maps, and tables used in correlation rules
- **Asset management** — enumerate network assets, asset properties, vulnerability data
- **Log source management** — list and inspect log sources and log source groups
- **Analytics rules** — inspect correlation rules, building blocks, rule performance
- **System administration** — QRadar system info, deployment health, license status
- **Forensics** — case management, forensic investigation artifacts
- **Vulnerability management** — CVE and vulnerability scan result retrieval

**The read-only constraint is intentional:** QRadar offenses drive security response workflows. IBM chose not to expose offense close/modify operations in Phase 1, consistent with how other security MCP servers (CrowdStrike, Splunk) have staged write capabilities cautiously.

**Limitations:** No AQL (Ariel Query Language) support in Phase 1 — the most powerful QRadar query capability is absent. Very low adoption signal (2 stars). No formal release. Phase 2 (write operations) timeline not published.

**Target audience:** SOC analysts and security engineers at organizations running IBM QRadar who want AI-assisted threat investigation workflows.

---

## FileNet Content Services — Four Specialized Configurations

| | |
|---|---|
| **Repo** | [ibm-ecm/ibm-content-services-mcp-server](https://github.com/ibm-ecm/ibm-content-services-mcp-server) |
| **Stars** | ~11 (10 forks) |
| **Version** | No formal releases (9 commits) |
| **License** | Not confirmed |
| **Requires** | IBM FileNet Content Manager 5.5.8+ |

IBM FileNet is the dominant enterprise content management platform, running document lifecycles at banks, insurers, and government agencies. The Content Services MCP server ships four distinct configurations, each targeting a different use pattern:

**Four server configurations:**
- **Core Content Server (26 tools)** — document creation, versioning, search, folder management, security classification, workflow initiation, audit, trash management. The primary interface for content operations.
- **Property Extraction Server (2 tools)** — AI-assisted extraction of structured properties from unstructured documents. Requires IBM Content Platform Engine.
- **Legal Hold Server (6 tools)** — legal hold creation, custodian assignment, matter management. Targets legal departments and ediscovery workflows.
- **AI Document Insight Server (6 tools)** — document analysis, content summarization, and insights. Requires IBM Content Assistant add-on.

**Known limitation:** Watson Orchestrate incompatibility with complex Pydantic input classes — some tools may not function correctly in Orchestrate-based agent workflows. This is a Python/Pydantic serialization issue documented in the repository.

**Target audience:** Content management teams, legal departments, and records managers at enterprises running IBM FileNet Content Manager 5.5.8+.

---

## Remaining Servers: Early Stage

### IBM Business Automation Workflow (BAW)
[ibmbpm/ibm-baw-mcp-server](https://github.com/ibmbpm/ibm-baw-mcp-server) — 7 stars, no formal releases. Dynamically generates MCP tools from BAW REST services exposed by workflow automations. Requires IBM BAW v25.0.1+ or Cloud Pak for Business Automation (CP4BA). Key limitations: no async support, name conflicts in complex types, recursive types unsupported, no hot-reload. The dynamic generation approach is architecturally similar to webMethods (above) — whatever your BAW instance exposes becomes available as MCP tools.

### IBM Master Data Management (MDM)
[IBM/mdm-mcp-server](https://github.com/IBM/mdm-mcp-server) — 3 stars, Apache-2.0. Five read-oriented tools: `search_master_data`, `get_data_model`, `get_record`, `get_entity`, `get_records_entities_by_record_id`. Minimal but coherent: AI agents can query and navigate master data relationships without write risk. Target: data architects and MDM administrators.

### IBM Storage Scale
[IBM/ibm-storage-scale-mcp-server](https://github.com/IBM/ibm-storage-scale-mcp-server) — 4 stars, no releases. Covers cluster management via REST API v2/v3, CLI via SSH, filesystem operations, and policy management. Carries an explicit "provided as-is without warranties" statement. Pre-release/experimental status.

### IBM Guardium Data Protection
[IBM/gdp-mcp-server](https://github.com/IBM/gdp-mcp-server) — 1 star, 1 commit, explicitly "NOT for production use." MVP-only. Tools: API search across 579+ Guardium endpoints, compliance reports (SOX, GDPR, PCI-DSS), Guard CLI, S-TAP monitoring. Significant potential for security-conscious organizations, but not ready for deployment.

### watsonx.governance Catalog
[IBM/ibm-watsonx-gov-catalog-mcp-server](https://github.com/IBM/ibm-watsonx-gov-catalog-mcp-server) — 1 star, no releases. Exposes governed agentic tool catalogs (OOTB and custom tools). Stdio transport only; SaaS-only (Sydney and Toronto regions). This is how IBM envisions governed tool access — curated, access-controlled tool catalogs that AI agents query rather than raw API endpoints.

---

## What's Missing

**No watsonx.ai MCP server.** IBM has not built an MCP server for its foundation model inference platform (Granite models, watsonx.ai). Organizations wanting AI agents to call watsonx.ai for inference must use the standard SDK or API directly. The watsonx.governance catalog server is the closest thing — it exposes governed tools, not inference endpoints.

**ABAP / IBM Z mainframe gap.** IBM Z (mainframe) has no official MCP server. IBM CICS, IMS, and Db2 for z/OS — platforms running the world's largest transaction volumes — are not represented in the IBM MCP portfolio. This may be deliberate (mainframe security posture) or simply a matter of resourcing.

**Fragmented GitHub presence.** IBM publishes across IBM/, instana/, ibmbpm/, and ibm-ecm/ GitHub organizations. The IBM/mcp monorepo provides an index, but there's no unified documentation site, no consistent naming convention, and no central "IBM MCP" landing page. Discovery is harder than it should be for a vendor of IBM's scale.

**Inconsistent maturity signals.** The data-intelligence server has v1.0.2 and an active release cadence; 9 of 13 servers have zero formal releases. Enterprises evaluating IBM MCP servers need to evaluate each server independently — there is no IBM-wide maturity standard.

---

## Rating: 3.5 / 5

IBM has assembled the most diverse enterprise MCP portfolio in the ecosystem — 13+ servers spanning five decades of product lines, all Apache-2.0, targeting everything from AS/400 transaction monitoring to cloud data lakehouse management. The **watsonx.data Intelligence server** (70+ tools, v1.0.2) is genuinely enterprise-ready: it covers data governance, cataloging, lineage, quality, and text-to-SQL in a single package with an active release cadence. The **IBM i server** (v0.5.1, 59 stars) demonstrates that MCP can meaningfully reach legacy systems — a category no other vendor has attempted. **webMethods** and **watsonx.data lakehouse** fill important integration and data platform gaps.

What holds IBM back is the other side of the ledger: most servers have no formal releases, star counts in single digits, and explicit "not for production" caveats. IBM publishes across multiple GitHub organizations without a unified discovery mechanism. The notable absence of a watsonx.ai MCP server means IBM's flagship AI platform has no MCP integration despite being one of the largest enterprise AI investments in the market. And IBM Z/ABAP — the foundation of IBM's installed base — remains untouched.

For organizations already running IBM enterprise software, these MCP servers are worth evaluating product-by-product. The data-intelligence and IBM i servers can deliver immediate value. The others represent IBM's intent to build out MCP coverage systematically — the roadmap is clear, even if the execution is still in progress.

