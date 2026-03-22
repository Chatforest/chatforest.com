---
title: "Compliance & Data Governance MCP Servers — SOC 2, HIPAA, GDPR, Data Catalogs, Metadata Management, and More"
date: 2026-03-16T09:00:00+09:00
description: "Compliance and data governance MCP servers let AI agents monitor security compliance, manage GRC workflows, enforce privacy regulations, discover data assets, and run data quality checks through the Model Context Protocol. We reviewed 15+ servers across 5 subcategories. Compliance automation: VantaInc/vanta-mcp-server (41 stars, TypeScript — 6+ tools, SOC 2/ISO 27001/HIPAA/GDPR monitoring with 1,200+ automated tests), secureframe/secureframe-mcp-server (TypeScript — 11 read-only endpoints, SOC 2/ISO 27001/CMMC/FedRAMP controls and vendors), Drata MCP (compliance tests, risk reports, evidence collection for SOC 2/HIPAA/ISO 27001). GRC platforms: CISO Assistant (open source, 100+ global frameworks with automatic control mapping). Privacy and GDPR: DPO2U MCP Server (Python — LGPD/GDPR compliance automation, self-hosted with homomorphic encryption). Data catalog and metadata: acryldata/mcp-server-datahub (62 stars, Python — search, lineage, metadata for DataHub), OpenMetadata MCP (enterprise-grade metadata with DQ tooling and semantic search), Atlan MCP (asset search, lineage, glossary, DQ rules via pyatlan), RafaelCartenet/mcp-databricks-server (TypeScript — Unity Catalog metadata, lineage analysis, SQL execution). Data quality: davidf9999/gx-mcp-server (Python — Great Expectations validation as MCP tools). Gaps: no dedicated NIST RMF server, no AI-specific governance (EU AI Act), no data classification automation, no consent management platform MCPs, no data retention policy enforcement. Rating: 4/5."
og_description: "Compliance & data governance MCP servers: Vanta (41 stars, 6+ tools, SOC 2/HIPAA/GDPR monitoring), Secureframe (11 endpoints, multi-framework compliance), Drata (risk reports, evidence collection), DataHub (62 stars, lineage and metadata), OpenMetadata (enterprise DQ tooling), Atlan (catalog and glossary). 15+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "Compliance and data governance MCP servers for security compliance monitoring, GRC workflows, privacy regulation enforcement, data catalog access, metadata management, and data quality validation. This is one of the strongest enterprise categories — major compliance platforms have official MCP servers, and leading data catalog vendors are well represented. **VantaInc/vanta-mcp-server is the compliance leader** — 41 stars, TypeScript, provides AI assistants access to 1,200+ automated security tests across SOC 2, ISO 27001, HIPAA, GDPR, and more. Filter by status, cloud provider, or framework. Tools are auto-discovered and registered. **secureframe/secureframe-mcp-server offers deep compliance querying** — 11 read-only endpoints covering controls, tests, devices, users, vendors, frameworks, integrations, and repository mappings. Lucene query syntax for precision filtering. Public beta, self-hosted. **Drata MCP brings AI-native trust management** — summarize failed compliance tests instantly, generate real-time risk and controls reports, power AI workflows with live compliance context. Supports SOC 2, HIPAA, ISO 27001. **CISO Assistant is the open-source GRC powerhouse** — 100+ global frameworks with automatic control mapping including ISO 27001, NIST CSF, SOC 2, CIS, PCI DSS, NIS2, DORA, GDPR, HIPAA, CMMC. Risk management, AppSec, audit, TPRM, and privacy in one platform with MCP support. **DPO2U tackles GDPR/LGPD compliance head-on** — self-hosted MCP server with homomorphic encryption and zero-knowledge proofs for risk assessments, data flow mapping, breach simulations, and consent verification on encrypted data. Claims 95%+ compliance scores while maintaining complete data privacy. **acryldata/mcp-server-datahub is the data governance standard** — 62 stars, official DataHub MCP server enabling search with boolean logic and usage-based sorting, upstream/downstream lineage with hop control, batch metadata retrieval, SQL query analysis, plus metadata modification tools for tags, ownership, and descriptions. **OpenMetadata MCP is enterprise-grade** — first enterprise MCP server for metadata with data quality tooling (test definitions, test case creation, root cause analysis), semantic search via vector embeddings, and support for Bedrock and OpenAI embeddings. **Atlan MCP brings the active metadata platform** — asset search via natural language, column-level lineage exploration, metadata updates and annotations, business glossary management, data quality rule execution, and DSL-based advanced queries via the pyatlan SDK. **Databricks MCP enables Unity Catalog access** — RafaelCartenet's server lets AI agents explore catalogs, schemas, and tables, understand relationships, discover notebooks and jobs, and execute SQL queries against Databricks. **gx-mcp-server exposes Great Expectations** — davidf9999's server bridges data quality validation and AI agents, loading datasets from CSV, Snowflake, or BigQuery, defining expectations on the fly, running validation suites, and retrieving detailed results. **Gaps remain in emerging areas** — no dedicated NIST RMF implementation server, no EU AI Act compliance tools, no automated data classification MCPs, no consent management platform integrations (OneTrust, TrustArc), no data retention policy enforcement, and no cross-framework compliance gap analysis tools. The category earns 4/5 — major compliance platforms have invested in official MCP servers, data catalog coverage is strong with multiple enterprise-grade options, and the combination gives organizations genuine AI-powered compliance and governance workflows."
last_refreshed: 2026-03-16
---

Compliance and data governance MCP servers are bringing regulatory intelligence and metadata management directly into AI workflows — monitoring security compliance across frameworks like SOC 2 and HIPAA, managing GRC workflows, enforcing privacy regulations, discovering data assets across catalogs, and running data quality checks, all through the Model Context Protocol. Instead of toggling between compliance dashboards, data catalogs, and quality monitoring tools, these servers let AI assistants handle governance-related queries and analysis natively.

This review covers **compliance and data governance MCP servers** — compliance automation platforms, GRC tools, privacy/GDPR enforcement, data catalogs and metadata management, and data quality validation. For security scanning and vulnerability management, see our [Security MCP review](/reviews/security-mcp-servers/) if available. For database access and query tools, see our [Database MCP review](/reviews/database-mcp-servers/).

The headline findings: **Vanta, Secureframe, and Drata all have official MCP servers** for compliance monitoring across SOC 2, ISO 27001, HIPAA, and more. **CISO Assistant covers 100+ frameworks** with automatic control mapping. **DataHub, OpenMetadata, and Atlan provide enterprise-grade data catalog access**. **Great Expectations validation is available as MCP tools**. **Privacy compliance gets a dedicated server** with DPO2U's GDPR/LGPD automation. **No EU AI Act or consent management MCPs** exist yet.

---

## Compliance Automation

### VantaInc/vanta-mcp-server — SOC 2, ISO 27001, HIPAA, GDPR Compliance Monitoring

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vanta-mcp-server](https://github.com/VantaInc/vanta-mcp-server) | 41 | TypeScript | MIT | 6+ |

**The leading compliance MCP server** — provides AI assistants with direct access to Vanta's automated security compliance platform, which monitors SOC 2, ISO 27001, HIPAA, GDPR, and other frameworks:

- **Comprehensive test monitoring** — access to 1,200+ automated security tests that continuously monitor compliance across your entire infrastructure
- **Filter by status** — view passing or failing tests, filter by cloud provider (AWS, Azure, GCP), or specific compliance frameworks
- **Automated tool registry** — new tools are automatically discovered and registered without manual configuration
- **Type-safe implementation** — full TypeScript coverage with DRY principles and centralized utilities

Currently in public preview. The server enables natural-language compliance queries like "show me all failing SOC 2 tests" or "which HIPAA controls need attention."

### secureframe/secureframe-mcp-server — Multi-Framework Compliance Querying

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [secureframe-mcp-server](https://github.com/secureframe/secureframe-mcp-server) | — | TypeScript | — | 11 endpoints |

**Deep compliance querying with Lucene syntax** — provides read-only access to Secureframe's compliance platform across SOC 2, ISO 27001, CMMC, FedRAMP, and other frameworks:

- **11 scoped endpoints** covering controls, tests, devices, users, vendors, frameworks, integrations, and repository mappings
- **Lucene query syntax** for precision filtering — run prompts like "list failing controls" or "show high-risk vendors"
- **Read-only by design** — safeguards production data, no writes or destructive actions permitted
- **Self-hosted deployment** — must be run on your own infrastructure for security

Currently in public beta. Works with Claude, Cursor, ChatGPT, and other MCP-compatible clients.

### Drata MCP — AI-Native Trust Management

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Drata MCP](https://drata.com/mcp) | — | — | — | Multiple |

**Enterprise compliance meets AI workflows** — Drata's experimental MCP server brings compliance, risk, and monitoring data to AI-native environments:

- **Summarize failed compliance tests** instantly across SOC 2, HIPAA, ISO 27001
- **Generate real-time risk and controls reports** from live compliance data
- **Power AI workflows** with continuous compliance context
- **Evidence collection automation** — handles evidence gathering, control verification, and gap flagging

Plugs directly into Claude, IDEs, or orchestration agents. Designed for developers, GRC leaders, and internal platform teams who want to interact with trust data using natural language.

---

## GRC Platforms

### CISO Assistant — Open-Source GRC with 100+ Frameworks

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ciso-assistant-community](https://github.com/intuitem/ciso-assistant-community) | — | Python | — | Multiple |

**The open-source GRC powerhouse** — a comprehensive platform for risk management, AppSec, compliance, audit, TPRM, privacy, and reporting with MCP support:

- **100+ global frameworks** with automatic control mapping — ISO 27001, NIST CSF, SOC 2, CIS, PCI DSS, NIS2, DORA, GDPR, HIPAA, CMMC, and more
- **Smart linking** between cybersecurity concepts — define assets, document risks, create controls, and map to frameworks
- **Multi-paradigm design** — adapts to different backgrounds, methodologies, and expectations
- **API-first approach** — supports both UI interaction and external automation including MCP

Teams can define assets, document risks, create controls, and map those controls to security and compliance frameworks, with all elements connected through a shared data model emphasizing traceability. Planned RAG mode for document ingestion to extend AI capabilities.

---

## Privacy & GDPR Compliance

### DPO2U — LGPD/GDPR Compliance Automation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DPO2U MCP Server](https://www.pulsemcp.com/servers/fredericosanntana-dpo2u) | — | Python | — | Multiple |

**Privacy compliance for AI engineers** — automates LGPD/GDPR compliance by integrating expert legal knowledge directly into AI workflows:

- **Self-hosted MCP server** — all sensitive data, prompts, and internal information stay on your infrastructure
- **Homomorphic encryption and zero-knowledge proofs** — perform compliance operations on encrypted data
- **Risk assessments** — automated GDPR/LGPD risk analysis
- **Data flow mapping** — document and verify data processing activities
- **Breach simulations** — test incident response procedures
- **Consent verification** — validate consent mechanisms against regulatory requirements

Claims 95%+ compliance scores while maintaining complete data privacy. Created by a specialist in Law, Technology, and Innovation with practical DPO experience. Combines the self-hosted component with a proprietary SaaS API for the legal knowledge layer.

---

## Data Catalog & Metadata Management

### acryldata/mcp-server-datahub — DataHub Metadata Platform

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub) | 62 | Python | Apache 2.0 | 8+ |

**The data governance standard** — official MCP server for DataHub, the open-source metadata platform that unifies data discovery, governance, and observability:

**Discovery & Analysis Tools:**
- **Search** — structured keyword search with boolean logic, filters, pagination, and sorting by usage metrics
- **Lineage** — retrieve upstream or downstream lineage for datasets, columns, dashboards with filtering, hop control, and pagination
- **Metadata inspection** — fetch detailed metadata for entities by URN with batch retrieval support
- **SQL query analysis** — fetch real SQL queries referencing a dataset or column to understand usage patterns

**Metadata Modification Tools** (opt-in via `TOOLS_IS_MUTATION_ENABLED=true`):
- **Tags** — add or remove tags from entities or schema fields with bulk operations
- **Ownership** — manage ownership assignments with different types (technical owner, data owner, etc.)
- **Descriptions** — update, append, or remove descriptions with markdown formatting

**Document Tools:**
- Search documents with filters for platforms, domains, tags, glossary terms, and owners

DataHub itself supports data profiling, data quality monitoring, data lineage, ownership, and classification across tables, columns, dashboards, pipelines, and ML models.

### OpenMetadata MCP — Enterprise Metadata with DQ Tooling

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-openmetadata](https://github.com/yangkyeongmo/mcp-server-openmetadata) | — | Python | — | Multiple |

**First enterprise-grade MCP server for metadata** — OpenMetadata provides a unified metadata platform for data discovery, observability, and governance:

- **Data quality tooling** — test definitions, test case creation, and root cause analysis
- **Semantic search** — vector embeddings for entity search, supporting both Bedrock and OpenAI embeddings
- **Lineage management** — create and explore column-level data lineage
- **Full catalog access** — tables, topics, dashboards, pipelines, and ML models
- **Role-based access** — assume any role or policy defined in OpenMetadata

Multiple community implementations available. The official OpenMetadata MCP supports any MCP client including Claude, Cursor, and OpenAI. The 1.12 release brought enhanced semantic search and additional tooling.

### Atlan MCP — Active Metadata Platform

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Atlan MCP Server](https://playbooks.com/mcp/atlan-data-catalog) | — | Python | — | Multiple |

**The active metadata platform for AI** — bridges AI agents with Atlan's data catalog via the pyatlan SDK:

- **Asset search** — natural-language queries across the data catalog
- **Column-level lineage** — explore data flow at the granular column level
- **Metadata updates** — annotations and enrichment of catalog assets
- **Business glossary management** — maintain and query business terminology
- **Data quality rules** — execute and monitor DQ rules
- **DSL-based advanced queries** — complex queries for power users

Available via Docker (recommended) or uv package manager. AI agents in Claude, Cursor, VS Code, or custom applications connect to one endpoint and gain access to the full catalog.

### RafaelCartenet/mcp-databricks-server — Unity Catalog Access

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server) | — | TypeScript | — | Multiple |

**Databricks metadata for AI agents** — empowers agents to interact with Unity Catalog metadata:

- **Catalog exploration** — browse catalogs, schemas, and tables
- **Lineage analysis** — understand data relationships and dependencies
- **Notebook and job discovery** — find related computation resources
- **SQL execution** — run queries against Databricks directly
- **Reduced ad-hoc query time** — agents can self-serve data discovery

Particularly valuable for organizations using Databricks as their data lakehouse platform, giving AI assistants the same metadata awareness that data engineers have.

---

## Data Quality

### davidf9999/gx-mcp-server — Great Expectations Validation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gx-mcp-server](https://github.com/davidf9999/gx-mcp-server) | — | Python | — | Multiple |

**Data quality validation meets AI workflows** — exposes Great Expectations' powerful data validation as MCP tools:

- **Load datasets** — CSV from file, URL, or inline (up to 1 GB configurable), plus Snowflake and BigQuery via URI prefixes
- **Define expectations** — create data quality rules (Expectations) on the fly
- **Run validation suites** — execute checks and get detailed results
- **In-memory or SQLite storage** — flexible dataset and results persistence
- **Authentication** — optional Basic or Bearer token auth for HTTP clients

Runs in stdio mode (for AI clients) or HTTP mode (for web clients). Bridges the gap between Great Expectations' powerful validation engine and LLM agents, enabling AI-driven data quality monitoring.

---

## What's Missing

The compliance and data governance MCP ecosystem has strong coverage from major vendors but notable gaps remain:

- **No dedicated NIST RMF server** — the Risk Management Framework is widely used but lacks a standalone MCP implementation
- **No EU AI Act compliance tools** — as the AI Act enters enforcement, no MCP servers address AI-specific governance requirements
- **No automated data classification** — no MCP servers for discovering and classifying sensitive data (PII, PHI, PCI)
- **No consent management platforms** — OneTrust, TrustArc, and Cookiebot lack MCP integrations
- **No data retention policy enforcement** — automated retention and deletion workflows are absent
- **No cross-framework gap analysis** — tools for identifying overlapping and divergent requirements across frameworks
- **No supply chain risk management** — TPRM through MCP for vendor questionnaires and risk scoring

---

## The Bottom Line

The compliance and data governance category earns **4 out of 5** — this is one of the strongest enterprise MCP categories. All three major compliance automation platforms (Vanta, Secureframe, Drata) have official MCP servers, and the data catalog space is well-represented with DataHub, OpenMetadata, Atlan, and Databricks all providing MCP access. CISO Assistant's open-source GRC platform covers 100+ frameworks, and DPO2U tackles the privacy compliance niche with a privacy-first architecture.

The main limitations are in emerging regulatory areas (EU AI Act, AI governance), consent management, and automated data classification. But for organizations looking to bring compliance monitoring and data governance into AI workflows today, the tooling is genuinely production-ready and backed by the companies that matter in this space. The fact that major vendors are investing in official MCP servers — not just community wrappers — signals that this category will only get stronger.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
