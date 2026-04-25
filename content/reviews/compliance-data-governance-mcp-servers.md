---
title: "Compliance & Data Governance MCP Servers — SOC 2, HIPAA, GDPR, Data Catalogs, Metadata Management, and More"
date: 2026-03-16T09:00:00+09:00
description: "Compliance and data governance MCP servers let AI agents monitor security compliance, manage GRC workflows, enforce privacy regulations, discover data assets, and run data quality"
og_description: "Compliance & data governance MCP servers: Vanta (55 stars, 43 tools, SOC 2/HIPAA/GDPR monitoring), Secureframe (11 endpoints, multi-framework compliance), Drata (hosted MCP, VRM Agent), Collibra (27 stars, 26 tools, official), DataHub (73 stars, SQL-like filters), OpenMetadata (OAuth, bot impersonation), Atlan (AI agents for metadata), EU Compliance (61 regulations). 20+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Compliance and data governance MCP servers for security compliance monitoring, GRC workflows, privacy regulation enforcement, EU regulatory compliance, data catalog access, metadata management, and data quality validation. This is one of the strongest enterprise categories — major compliance and data governance platforms now have official MCP servers. **VantaInc/vanta-mcp-server is the compliance leader** — 55 stars, TypeScript, 43 tools (consolidated from 53) covering controls, tests, frameworks, risks, vulnerabilities, and more across SOC 2, ISO 27001, HIPAA, GDPR. **secureframe/secureframe-mcp-server offers deep compliance querying** — 11 read-only endpoints covering controls, tests, devices, users, vendors, frameworks, integrations, and repository mappings. Lucene query syntax. Public beta. **Drata MCP brings hosted AI-native trust management** — Drata hosts the MCP server for you in a hardened environment. VRM Agent autonomously handles vendor compliance. 8,000+ customers. SOC 2, HIPAA, ISO 27001. **CISO Assistant is the open-source GRC powerhouse** — 4,000+ stars, 130+ global frameworks with automatic control mapping. MCP server now exposes vulnerability management endpoints (v3.15.2). Risk management, AppSec, audit, TPRM, privacy. **Ansvar Systems EU Compliance MCP covers 61 EU regulations** — AI Act, DORA, GDPR, NIS2, MiFID II, eIDAS 2.0, CRA, MiCA and more. 4,095 articles, 709 control mappings, daily EUR-Lex updates. **ark-forge/mcp-eu-ai-act scans codebases for AI Act compliance** — detects 16 AI frameworks across 6 languages, generates remediation roadmaps for August 2026 enforcement. **DPO2U tackles GDPR/LGPD compliance** — self-hosted MCP server with homomorphic encryption and zero-knowledge proofs. **collibra/chip is the official Collibra MCP server** — 27 stars, Go, Apache 2.0, 26 tools (21 read, 5 write) for data asset discovery, glossary, lineage, classification, and data contracts. Also on Databricks Marketplace. **acryldata/mcp-server-datahub is the data governance standard** — 73 stars, v0.5.3 with SQL-like filter syntax replacing nested JSON, modular tool architecture, assertions tooling. **OpenMetadata MCP adds OAuth and bot impersonation** — March 2026 update with database-backed token persistence, audit logging, CVE-2026-34237 fix. Semantic search via vector embeddings. **Atlan MCP launches AI agents** — Description Propagation, Metadata Enrichment, and Business Glossary agents for automated metadata management. Activate 2026 context layer initiative. **Databricks managed MCP servers** — official managed servers with Unity Catalog integration (Public Preview April 2026), on-behalf-of-user auth, Genie, Vector Search, and UC Functions access. **gx-mcp-server exposes Great Expectations** — data quality validation with CSV, Snowflake, BigQuery support. **Remaining gaps** — no consent management platform MCPs (OneTrust, TrustArc), no automated data classification, no data retention policy enforcement, no NIST RMF standalone server. The category earns 4.5/5 — upgraded from 4/5 as EU compliance, Collibra, managed Databricks, and significant existing server improvements fill prior gaps."
last_refreshed: 2026-04-26
---

Compliance and data governance MCP servers are bringing regulatory intelligence and metadata management directly into AI workflows — monitoring security compliance across frameworks like SOC 2 and HIPAA, managing GRC workflows, enforcing privacy regulations, discovering data assets across catalogs, and running data quality checks, all through the Model Context Protocol. Instead of toggling between compliance dashboards, data catalogs, and quality monitoring tools, these servers let AI assistants handle governance-related queries and analysis natively. Part of our **[Security & Compliance MCP category](/categories/security-compliance/)**.

This review covers **compliance and data governance MCP servers** — compliance automation platforms, GRC tools, privacy/GDPR enforcement, data catalogs and metadata management, and data quality validation. For security scanning and vulnerability management, see our [Security MCP review](/reviews/security-scanning-mcp-servers/) if available. For database access and query tools, see our [Database MCP review](/reviews/database-admin-mcp-servers/).

The headline findings: **Vanta leads compliance with 55 stars and 43 tools**, Secureframe and Drata round out the big three — Drata now hosts its MCP server in a hardened environment with a VRM Agent. **CISO Assistant hits 4,000+ stars with 130+ frameworks** and new vulnerability management MCP endpoints. **EU regulatory compliance arrives** — Ansvar Systems covers 61 EU regulations (AI Act, DORA, GDPR, NIS2) and ark-forge scans codebases for AI Act compliance ahead of August 2026 enforcement. **Collibra launches an official MCP server** with 26 tools for data governance. **DataHub, OpenMetadata, and Atlan all level up** — DataHub adds SQL-like filters, OpenMetadata adds OAuth and bot impersonation, Atlan launches AI agents for automated metadata. **Databricks ships managed MCP servers** with Unity Catalog integration. Rating upgraded to **4.5/5**.

---

## Compliance Automation

### VantaInc/vanta-mcp-server — SOC 2, ISO 27001, HIPAA, GDPR Compliance Monitoring

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vanta-mcp-server](https://github.com/VantaInc/vanta-mcp-server) | 55 | TypeScript | MIT | 43 |

**The leading compliance MCP server** — provides AI assistants with direct access to Vanta's automated security compliance platform, which monitors SOC 2, ISO 27001, HIPAA, GDPR, and other frameworks:

- **43 consolidated tools** — smart consolidation from 53 tools covering controls (3), documents (2), frameworks (2), integrations (2), people (1), risks (1), tests (2), vulnerabilities (1), and additional resource operations
- **Comprehensive test monitoring** — access to 1,200+ automated security tests that continuously monitor compliance across your entire infrastructure
- **Filter by status** — view passing or failing tests, filter by cloud provider (AWS, Azure, GCP), or specific compliance frameworks
- **Automated tool registry** — new tools are automatically discovered and registered without manual configuration
- **Type-safe implementation** — full TypeScript coverage with DRY principles and centralized utilities

Currently in public preview with 96 commits on main. The server enables natural-language compliance queries like "show me all failing SOC 2 tests" or "which HIPAA controls need attention."

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

**Enterprise compliance meets AI workflows** — Drata's MCP server brings compliance, risk, and monitoring data to AI-native environments, now serving 8,000+ customers:

- **Hosted MCP solution** — Drata hosts the protocol in a hardened environment, so you're up and running in minutes with no servers, dependencies, or upkeep
- **Vendor Risk Management Agent** — autonomously retrieves vendor documents, evaluates them against criteria, and sends follow-up questionnaires
- **Summarize failed compliance tests** instantly across SOC 2, HIPAA, ISO 27001
- **Generate real-time risk and controls reports** from live compliance data
- **Evidence collection automation** — handles evidence gathering, control verification, and gap flagging

Plugs directly into Claude, IDEs, or orchestration agents. Designed for developers, GRC leaders, and internal platform teams who want to interact with trust data using natural language. Listed in the official MCP servers directory.

---

## GRC Platforms

### CISO Assistant — Open-Source GRC with 100+ Frameworks

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ciso-assistant-community](https://github.com/intuitem/ciso-assistant-community) | 4,000+ | Python | AGPL-3.0 | Multiple |

**The open-source GRC powerhouse** — a comprehensive platform for risk management, AppSec, compliance, audit, TPRM, privacy, and reporting with MCP support:

- **130+ global frameworks** with automatic control mapping — ISO 27001, NIST CSF, SOC 2, CIS, PCI DSS, NIS2, DORA, GDPR, HIPAA, CMMC, and more
- **Vulnerability management via MCP** — v3.15.2 (April 2026) exposes vulnerability management endpoints, allowing AI agents to query, create, and update vulnerabilities programmatically with reverse foreign keys for relationship tracking
- **Smart linking** between cybersecurity concepts — define assets, document risks, create controls, and map to frameworks
- **Embedded AI chat** — works with your own models alongside MCP support
- **API-first approach** — supports both UI interaction and external automation including MCP

Teams can define assets, document risks, create controls, and map those controls to security and compliance frameworks, with all elements connected through a shared data model emphasizing traceability. Planned RAG mode for document ingestion to extend AI capabilities. Currently at v3.15.9 with weekly releases.

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

### Ansvar Systems EU Compliance MCP — 61 EU Regulations

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [EU_compliance_MCP](https://github.com/Ansvar-Systems/EU_compliance_MCP) | 5 | TypeScript | Apache 2.0 | Multiple |

**The most comprehensive EU regulatory MCP server** — provides AI agents with structured access to 61 EU regulations including the AI Act, DORA, GDPR, NIS2, MiFID II, PSD2, eIDAS 2.0, Cyber Resilience Act, Chips Act, MiCA, Medical Device Regulation, and more:

- **4,095 articles** (including 50 addressable annexes) with 4,970 recitals and 1,448 official definitions
- **709 control mappings** to ISO 27001:2022 and NIST CSF 2.0
- **407 evidence requirements** and 323 sector applicability rules
- **16 regulation-specific guides** for implementation context
- **Daily automated EUR-Lex updates** — monitors for regulatory changes
- **Multiple deployment options** — remote HTTP endpoint (zero installation), local npm, or integration with Claude Desktop, Cursor, GitHub Copilot

Built by Ansvar Systems (Stockholm, Sweden) for compliance teams navigating European regulatory requirements. Particularly valuable as DORA enforcement is active and EU AI Act full application hits August 2, 2026.

### ark-forge/mcp-eu-ai-act — EU AI Act Compliance Scanner

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-eu-ai-act](https://github.com/ark-forge/mcp-eu-ai-act) | 4 | Python | — | Multiple |

**Codebase-level AI Act compliance scanning** — detects AI framework usage and evaluates compliance with the EU AI Act:

- **16 AI framework detection** — scans for TensorFlow, PyTorch, scikit-learn, and more across Python, JavaScript, TypeScript, Go, Java, and Rust
- **Compliance scoring** against binding legal requirements with mapping to specific AI Act articles
- **Week-by-week remediation roadmaps** leading to the August 2, 2026 enforcement deadline
- **Annex IV audit documentation** — generates audit-ready documentation packages
- **Cryptographic certification** via Trust Layer for tamper-proof compliance evidence
- **GDPR overlap detection** for dual-regulation scenarios

Operates as both a CLI utility and an MCP server, integrating with Claude, Cursor, and other AI development environments.

---

## Data Catalog & Metadata Management

### acryldata/mcp-server-datahub — DataHub Metadata Platform

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub) | 73 | Python | Apache 2.0 | 8+ |

**The data governance standard** — official MCP server for DataHub, the open-source metadata platform that unifies data discovery, governance, and observability. Now at v0.5.3 (March 2026) with significant improvements:

**Discovery & Analysis Tools:**
- **Search** — structured keyword search with boolean logic, filters, pagination, and sorting by usage metrics
- **SQL-like filter syntax** (v0.5.3) — human-readable filters like `"platform = snowflake AND env = PROD"` replace nested JSON structures, dramatically improving LLM agent usability
- **Lineage** — retrieve upstream or downstream lineage for datasets, columns, dashboards with filtering, hop control, and pagination. New `get_lineage_paths_between` tool finds exact paths between two assets
- **Metadata inspection** — fetch detailed metadata for entities by URN with batch retrieval support
- **SQL query analysis** — fetch real SQL queries referencing a dataset or column to understand usage patterns
- **Assertions** — new assertions tool module for data quality validation

**Metadata Modification Tools** (opt-in via `TOOLS_IS_MUTATION_ENABLED=true`):
- **Tags** — add or remove tags from entities or schema fields with bulk operations
- **Ownership** — manage ownership assignments with different types (technical owner, data owner, etc.)
- **Descriptions** — update, append, or remove descriptions with markdown formatting

**Document Tools:**
- Search documents with filters for platforms, domains, tags, glossary terms, and owners

**Architecture** — v0.5.3 introduces a modular tool architecture organized under a `tools/` directory with extracted GraphQL helpers and configurable view preferences. 18 releases to date with active development (last updated April 21, 2026).

### OpenMetadata MCP — Enterprise Metadata with DQ Tooling

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-openmetadata](https://github.com/yangkyeongmo/mcp-server-openmetadata) | — | Python | — | Multiple |

**First enterprise-grade MCP server for metadata** — OpenMetadata provides a unified metadata platform for data discovery, observability, and governance:

- **OAuth support** (March 2026) — database-backed token persistence with automatic refresh, plus MCP bot impersonation with audit logging and change event publishing
- **Data quality tooling** — test definitions, test case creation, and root cause analysis
- **Semantic search** — vector embeddings for entity search, supporting both Bedrock and OpenAI embeddings
- **Lineage management** — create and explore column-level data lineage
- **Full catalog access** — tables, topics, dashboards, pipelines, and ML models
- **Role-based access** — assume any role or policy defined in OpenMetadata
- **Security** — MCP Java SDK bumped to 1.1.1 to address CVE-2026-34237; OAuth callback servlet registration fix

Multiple community implementations available (yangkyeongmo, pfldy2850). The official OpenMetadata MCP supports any MCP client including Claude, Cursor, and OpenAI. The 1.12 release brought enhanced semantic search and additional tooling.

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
- **NEW: AI Agents** (2026) — Description Propagation Agent auto-syncs verified definitions across lineage, Metadata Enrichment Agent auto-creates documentation from business context, Business Glossary Agent discovers new terms and keeps definitions current

Available via Docker (recommended) or uv package manager. AI agents in Claude, Cursor, VS Code, Windsurf, Microsoft Copilot Studio, or custom applications connect to one endpoint and gain access to the full catalog. Atlan Activate 2026 focuses on a knowledge architecture where AI is the primary producer and consumer of metadata context.

### collibra/chip — Official Collibra Data Governance

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chip](https://github.com/collibra/chip) | 27 | Go | Apache 2.0 | 26 |

**Official Collibra MCP server** — a Go-based bridge between AI applications and Collibra's Data Governance Center, offering 26 tools (21 read, 5 write):

- **Data discovery** — natural language and keyword-based asset search
- **Business glossary** — access terms, definitions, and semantic relationships
- **Asset intelligence** — detailed information about data assets including attributes and connections
- **Lineage tracking** — both upstream (sources) and downstream (consumers) data flow
- **Data classification** — manage associations between data classes and assets
- **Data contracts** — manifest upload/download capabilities
- **Asset creation** — create new business terms and data assets with attributes

Supports stdio and HTTP transports. Also available on the Collibra Marketplace and Databricks Marketplace. Structured JSON output with auto-generated schemas. Currently at v0.0.31 (April 2026) with active development.

### Databricks Managed MCP Servers — Unity Catalog Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Databricks MCP](https://docs.databricks.com/aws/en/generative-ai/mcp/) | — | Python | ��� | Multiple |

**Official managed MCP servers from Databricks** (Public Preview, April 2026) — ready-to-use servers that connect AI agents to data stored in Unity Catalog:

- **Unity Catalog access** — browse catalogs, schemas, tables with full governance
- **On-behalf-of-user auth** — automatically respects user permissions established in Unity Catalog
- **Genie integration** — natural language queries against Databricks data
- **Vector Search** �� semantic search over Databricks data
- **UC Functions** — execute user-defined functions via MCP
- **External client support** — connect non-Databricks IDEs and AI assistants via `databricks-mcp` PyPI package

Enterprise-grade security with no additional governance layer needed — managed servers inherit existing Unity Catalog permissions.

### RafaelCartenet/mcp-databricks-server — Community Unity Catalog Access

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server) | — | TypeScript | — | Multiple |

**Community Databricks metadata server** — empowers agents to interact with Unity Catalog metadata:

- **Catalog exploration** — browse catalogs, schemas, and tables
- **Lineage analysis** — understand data relationships and dependencies
- **Notebook and job discovery** — find related computation resources
- **SQL execution** — run queries against Databricks directly

The original community server predating Databricks' official managed MCP. Still valuable for organizations wanting self-hosted control or customization beyond the managed offering.

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

The compliance and data governance MCP ecosystem has matured significantly, but gaps remain:

- **No consent management platforms** — OneTrust, TrustArc, and Cookiebot still lack MCP integrations despite being core to GDPR/privacy workflows
- **No automated data classification** — no MCP servers for discovering and classifying sensitive data (PII, PHI, PCI) automatically
- **No dedicated NIST RMF server** — the Risk Management Framework is widely used but lacks a standalone MCP implementation (though CISO Assistant covers it within its 130+ frameworks)
- **No data retention policy enforcement** — automated retention and deletion workflows are absent
- **No cross-framework gap analysis** — tools for identifying overlapping and divergent requirements across frameworks (Ansvar Systems' control mappings are a step in this direction)
- **Alation absent** — no MCP server from Alation despite being a major data catalog vendor

---

## The Bottom Line

The compliance and data governance category earns **4.5 out of 5** — upgraded from 4/5, this is now one of the most mature enterprise MCP categories. All three major compliance automation platforms (Vanta with 55 stars and 43 tools, Secureframe, Drata with hosted MCP and VRM Agent) have official servers. CISO Assistant has exploded to 4,000+ stars with 130+ frameworks and new vulnerability management MCP endpoints. The data catalog space is now comprehensive — Collibra joins with an official 26-tool server, DataHub reaches 73 stars with improved SQL-like filters, OpenMetadata adds OAuth and bot impersonation, Atlan launches AI agents for automated metadata, and Databricks ships official managed MCP servers with Unity Catalog integration.

The most significant improvement since our initial review is the arrival of EU regulatory compliance tooling — Ansvar Systems covers 61 EU regulations with daily EUR-Lex monitoring, and ark-forge provides codebase-level AI Act compliance scanning ahead of the August 2026 enforcement deadline. This fills what was previously the biggest gap in the category.

Remaining limitations center on consent management (OneTrust, TrustArc still absent), automated data classification, and data retention policy enforcement. But the trajectory is clear — this category is moving from "tooling exists" to "production-ready enterprise workflows," with official vendor investment, hosted solutions, and AI-powered automation becoming the norm rather than the exception.

*This review was refreshed on 2026-04-26. Originally published 2026-03-16. Written by Grove using Claude Opus 4.6 (Anthropic).*
