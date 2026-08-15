# Compliance & Data Governance MCP Servers — SOC 2, HIPAA, GDPR, Data Catalogs, Metadata Management, and More

> Compliance and data governance MCP servers let AI agents monitor security compliance, manage GRC workflows, enforce privacy regulations, discover data assets, and run data quality


Compliance and data governance MCP servers are bringing regulatory intelligence and metadata management directly into AI workflows — monitoring security compliance across frameworks like SOC 2 and HIPAA, managing GRC workflows, enforcing privacy regulations, discovering data assets across catalogs, and running data quality checks, all through the Model Context Protocol. Instead of toggling between compliance dashboards, data catalogs, and quality monitoring tools, these servers let AI assistants handle governance-related queries and analysis natively. Part of our **[Security & Compliance MCP category](/categories/security-compliance/)**.

This review covers **compliance and data governance MCP servers** — compliance automation platforms, GRC tools, privacy/GDPR enforcement, data catalogs and metadata management, and data quality validation. For security scanning and vulnerability management, see our [Security MCP review](/reviews/security-scanning-mcp-servers/) if available. For database access and query tools, see our [Database MCP review](/reviews/database-admin-mcp-servers/).

The headline findings: **Vanta led compliance with its 64-star, 43-tool open-source server** — but [that repo is now archived](https://github.com/VantaInc/vanta-mcp-server) and Vanta has moved to a [hosted MCP server](https://developer.vanta.com/docs/vanta-mcp) at `mcp.vanta.com`. Secureframe and Drata round out the big three — [Secureframe's open-source server is also now archived](https://github.com/secureframe/secureframe-mcp-server) in favor of its own hosted MCP, while [Drata hosts its MCP server](https://drata.com/blog/introducing-mcp-built-for-ai) in a hardened environment with a [VRM Agent](https://drata.com/blog/ai-agent-for-vrm) that autonomously reviews vendor evidence. **CISO Assistant hits 4,300+ stars with 130+ frameworks** and [gained vulnerability management MCP endpoints in v3.15.2](https://intuitem.com/whats-new-ciso-assistant-2026-w14/). **EU regulatory compliance arrives** — [Ansvar Systems' corpus covers 61 EU regulations](https://github.com/Ansvar-Systems/EU_compliance_MCP) (AI Act, DORA, GDPR, NIS2), though that standalone repo is now archived and folded into Ansvar's fleet monorepo, and [ark-forge scans codebases for AI Act compliance](https://github.com/ark-forge/mcp-eu-ai-act) ahead of the August 2, 2026 enforcement deadline. **Collibra launches an official MCP server** ([collibra/chip](https://github.com/collibra/chip)) with dozens of tools for data governance. **DataHub, OpenMetadata, and Atlan all level up** — [DataHub adds SQL-like filters](https://github.com/acryldata/mcp-server-datahub/releases), [OpenMetadata's official MCP server patches an OAuth callback bug and a bot-impersonation gap](https://github.com/open-metadata/OpenMetadata/releases/tag/1.12.5-release), [Atlan launches AI agents](https://blog.atlan.com/announcements/atlan-mcp-ai-metadata/) for automated metadata. **Databricks ships managed MCP servers** ([Public Preview](https://docs.databricks.com/aws/en/generative-ai/mcp/managed-mcp)) with Unity Catalog integration. Rating upgraded to **4.5/5**.

---

## Compliance Automation

### Vanta MCP — SOC 2, ISO 27001, HIPAA, GDPR Compliance Monitoring

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vanta-mcp-server](https://github.com/VantaInc/vanta-mcp-server) (archived) | 64 | TypeScript | MIT | 43 |
| [Vanta hosted MCP](https://developer.vanta.com/docs/vanta-mcp) | — | — | — | — |

**Status change since our last audit:** the open-source `VantaInc/vanta-mcp-server` repo is [now archived](https://github.com/VantaInc/vanta-mcp-server) — GitHub shows "This repository is no longer maintained," archived June 17, 2026, and the README calls the project deprecated in favor of Vanta's own hosted server. Vanta [now hosts a remote MCP server](https://developer.vanta.com/docs/vanta-mcp) directly (regional endpoints, e.g. `https://mcp.vanta.com/mcp`), currently in beta and available to all customers who are Vanta Admins, connecting Claude Code, Cursor, Claude Cowork, and Perplexity to SOC 2, ISO 27001, HIPAA, GDPR, and other framework data:

- **43 consolidated tools** (the archived open-source version) — smart consolidation from 53 tools covering controls, documents, frameworks, integrations, people, risks, tests, and vulnerabilities
- **Hosted server capabilities** — [per Vanta's docs](https://developer.vanta.com/docs/vanta-mcp), the hosted server can remediate failing tests via generated infrastructure-as-code fixes, manage controls and framework mappings, assess vendor risk, track vulnerabilities, govern policy documents, and analyze compliance gaps
- **Type-safe implementation** — the archived open-source server had full TypeScript coverage with DRY principles and centralized utilities

The server enables natural-language compliance queries like "show me all failing SOC 2 tests" or "which HIPAA controls need attention." Teams still running the old self-hosted server should plan to migrate to the hosted endpoint, since the open-source repo will no longer receive fixes.

### secureframe/secureframe-mcp-server — Multi-Framework Compliance Querying (archived)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [secureframe-mcp-server](https://github.com/secureframe/secureframe-mcp-server) (archived) | 8 | Python | MIT | 11 endpoints |

**Deep compliance querying with Lucene syntax, now archived** — [the repo](https://github.com/secureframe/secureframe-mcp-server) was archived by its owner on July 17, 2026 and is read-only; the README points users to "the Secureframe hosted MCP server" as the maintained alternative. While active, it provided read-only access to Secureframe's compliance platform across SOC 2, ISO 27001, CMMC, FedRAMP, and other frameworks:

- **11 scoped endpoints** covering controls, tests, devices, users, vendors, frameworks, integrations, and repository mappings
- **Lucene query syntax** for precision filtering — e.g. `health_status:fail AND frameworks:soc2_alpha`
- **Read-only by design** — no writes or destructive actions permitted
- **Self-hosted deployment** — had to be run on your own infrastructure for security

The README's public-beta language dates from before archival; new deployments should use Secureframe's hosted MCP offering instead of this repo.

### Drata MCP — AI-Native Trust Management

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Drata MCP](https://drata.com/mcp) | — | — | — | Multiple |

**Enterprise compliance meets AI workflows** — [Drata's MCP server](https://drata.com/blog/introducing-mcp-built-for-ai) brings compliance, risk, and monitoring data to AI-native environments:

- **Hosted MCP solution** — Drata hosts the protocol in a hardened environment, so ["you're up and running in minutes with no servers, dependencies, or upkeep"](https://drata.com/blog/introducing-mcp-built-for-ai)
- **[Vendor Risk Management Agent](https://drata.com/blog/ai-agent-for-vrm)** — ingests vendor questionnaires/criteria, automatically collects vendor documentation from Drata Trust Centers, evaluates evidence against assessment criteria (Met/Partially Met/Not Met/Inconclusive), and drafts follow-up questions that a human reviews and approves before sending
- **Summarize failed compliance tests** across SOC 2, HIPAA, ISO 27001
- **Generate risk and controls reports** from live compliance data
- **Evidence collection automation** — handles evidence gathering, control verification, and gap flagging

Plugs directly into Claude, IDEs, or orchestration agents. Drata [reports 8,000+ customers](https://www.prnewswire.com/news-releases/drata-expands-global-footprint-bringing-ai-powered-trust-management-to-the-asia-pacific-region-302581302.html) across 80+ countries as of its 2026 Asia-Pacific expansion announcement.

---

## GRC Platforms

### CISO Assistant — Open-Source GRC with 130+ Frameworks

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ciso-assistant-community](https://github.com/intuitem/ciso-assistant-community) | 4,300+ | Python/TypeScript | AGPL-3.0 (community edition) | Multiple |

**The open-source GRC powerhouse** — a comprehensive platform for risk management, AppSec, compliance, audit, TPRM, privacy, and reporting with MCP support:

- **130+ global frameworks** with automatic control mapping — ISO 27001, NIST CSF, SOC 2, CIS, PCI DSS, NIS2, DORA, GDPR, HIPAA, CMMC, and more
- **Vulnerability management via MCP** — [v3.15.2 (released April 5, 2026)](https://intuitem.com/whats-new-ciso-assistant-2026-w14/) exposes vulnerability management endpoints, allowing AI agents to query, create, and update vulnerabilities programmatically
- **MCP capabilities keep expanding** — [v3.17.1/v3.17.2 (June 2026)](https://intuitem.com/whats-new-ciso-assistant-2026-w23/) added vulnerability CRUD, asset classes, and richer risk-scenario reads over MCP, plus Third-Party Risk Management and EBIOS Risk Manager objects
- **Smart linking** between cybersecurity concepts — define assets, document risks, create controls, and map to frameworks
- **API-first approach** — supports both UI interaction and external automation including MCP

Teams can define assets, document risks, create controls, and map those controls to security and compliance frameworks, with all elements connected through a shared data model emphasizing traceability. The project [ships weekly point releases](https://intuitem.com/whats-new-ciso-assistant-2026-w30/), reaching v3.20.x by late July 2026.

---

## Privacy & GDPR Compliance

### DPO2U — LGPD/GDPR Compliance Automation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DPO2U MCP Server](https://www.pulsemcp.com/servers/fredericosanntana-dpo2u) | 2 | Python | — | Multiple |

**Privacy compliance for AI engineers, single small self-published project** — DPO2U is a solo/community project (2 GitHub stars) whose own listing describes it as automating LGPD/GDPR compliance. We have no independent (security-press, vendor, or peer) corroboration of its technical claims, so treat the following as **the vendor's own description, not verified fact**:

- **Self-hosted MCP server** — the listing states sensitive data, prompts, and internal information stay on your infrastructure
- **"Homomorphic encryption and zero-knowledge proofs"** — the listing claims compliance operations run on encrypted data; we could not independently verify this cryptographic claim
- Risk assessments, data flow mapping, breach simulations, and consent verification are listed as capabilities
- The listing claims **"95%+ compliance scores while maintaining complete data privacy"** — this is a self-reported figure with no methodology or independent audit disclosed; do not take it as an established fact

Given the single-source, unverified nature of these claims, evaluate this server's security promises independently before relying on them for real compliance work.

### Ansvar Systems EU Compliance MCP — 61 EU Regulations (archived, folded into ansvar-mcp-fleet)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [EU_compliance_MCP](https://github.com/Ansvar-Systems/EU_compliance_MCP) (archived) | 25 | TypeScript | Apache 2.0 | Multiple |

**A broad EU regulatory MCP server, now retired as a standalone repo** — the standalone repository is archived; its commit history shows a "docs: tombstone — repo retired, corpus folded into ansvar-mcp-fleet" note, and the EU-regulations corpus now lives under `mcps/eu-regulations/` in [Ansvar-Systems/ansvar-mcp-fleet](https://github.com/Ansvar-Systems/ansvar-mcp-fleet). The README (as archived) describes structured access to EU regulations including the AI Act, DORA, GDPR, NIS2, MiFID II, PSD2, eIDAS 2.0, Cyber Resilience Act, Chips Act, MiCA, Medical Device Regulation, and more:

- **Full-text, verbatim EUR-Lex sourcing** — a search tool returns short snippets and a get-article tool returns full article text (some articles are very large — MDR Article 123 alone runs roughly 70,000 tokens)
- **Control mappings to ISO 27001:2022 and NIST CSF 2.0** are referenced in the README, though we could not confirm the specific counts our earlier draft cited for total articles, recitals, definitions, and control mappings — those figures have been removed pending a source we can verify
- **60+ example queries** documented in the repo's TEST_QUERIES.md
- **Multiple deployment options** — remote HTTP endpoint (zero installation), local npm, or integration with Claude Desktop, Cursor, GitHub Copilot

Built by Ansvar Systems (Stockholm, Sweden) for compliance teams navigating European regulatory requirements. Particularly valuable as DORA enforcement is active and EU AI Act full application hits August 2, 2026. New integrations should target the `ansvar-mcp-fleet` monorepo rather than this archived standalone repo.

### ark-forge/mcp-eu-ai-act — EU AI Act Compliance Scanner

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-eu-ai-act](https://github.com/ark-forge/mcp-eu-ai-act) | 11 | Python | MIT | Multiple |

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
| [mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub) | 78 | Python | Apache 2.0 | 8+ |

**The data governance standard** — official MCP server for DataHub, the open-source metadata platform that unifies data discovery, governance, and observability. [Release v0.5.3](https://github.com/acryldata/mcp-server-datahub/releases) shipped March 17, 2026 with significant improvements:

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

**Architecture** — v0.5.3 introduces a modular tool architecture organized under a `tools/` directory with extracted GraphQL helpers and configurable view preferences. The project has [shipped 10+ tagged releases](https://github.com/acryldata/mcp-server-datahub/releases) with active development, reaching v0.6.0 by mid-May 2026.

### OpenMetadata MCP — Enterprise Metadata with DQ Tooling

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) (official, includes MCP) | 14,000+ | Java/TypeScript | Apache 2.0 | Multiple |
| [yangkyeongmo/mcp-server-openmetadata](https://github.com/yangkyeongmo/mcp-server-openmetadata) (community) | 24 | Python | MIT | Multiple |

**Note on which server is which** — [OpenMetadata's own marketing page](https://open-metadata.org/mcp) calls its official, built-in MCP server "the first Enterprise-grade MCP server for metadata"; that official server ships inside the main `open-metadata/OpenMetadata` repo, not the smaller community `yangkyeongmo/mcp-server-openmetadata` project (24 stars) that an earlier version of this review linked as if it carried the same features. OpenMetadata provides a unified metadata platform for data discovery, observability, and governance:

- **Two real MCP security fixes landed in [releases 1.12.5 and 1.12.6](https://github.com/open-metadata/OpenMetadata/releases/tag/1.12.5-release)** — a fix for the MCP OAuth callback servlet registration fallback, and the [MCP Java SDK bumped from 1.1.0 to 1.1.1 to address CVE-2026-34237](https://nvd.nist.gov/vuln/detail/CVE-2026-34237)
- **Bot-impersonation gap closed** — 1.12.5 enforces a bot-type check on the `generateToken` endpoint, preventing unauthorized JWT token generation that could impersonate a bot identity
- **Data quality tooling** — test definitions, test case creation, and root cause analysis
- **Lineage management** — create and explore column-level data lineage
- **Full catalog access** — tables, topics, dashboards, pipelines, and ML models
- **Role-based access** — the official server "reads from or writes to the integrations you already have set up in OpenMetadata, and can assume any role or policy you define," per [open-metadata.org/mcp](https://open-metadata.org/mcp)

Community-maintained alternatives (yangkyeongmo, pfldy2850) also exist and implement a different, smaller tool surface than the official server — check each repo's own README rather than assuming feature parity.

### Atlan MCP — Active Metadata Platform

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Atlan MCP Server](https://atlan.com/mcp-server/) | — | Python | — | Multiple |

**The active metadata platform for AI** — bridges AI agents with Atlan's data catalog via the pyatlan SDK:

- **Asset search** — natural-language queries across the data catalog
- **Column-level lineage** — explore data flow at the granular column level
- **Metadata updates** — annotations and enrichment of catalog assets
- **Business glossary management** — maintain and query business terminology
- **Data quality rules** — execute and monitor DQ rules
- **DSL-based advanced queries** — complex queries for power users
- **AI Agents** — per [Atlan's announcement](https://blog.atlan.com/announcements/atlan-mcp-ai-metadata/), a Description Propagation Agent auto-syncs verified definitions across lineage, a Metadata Enrichment Agent auto-creates documentation from business context, and a Business Glossary Agent discovers new terms and keeps definitions current

Available via Docker (recommended) or uv package manager. AI agents in Claude, Cursor, VS Code, Windsurf, Microsoft Copilot Studio, or custom applications connect to one endpoint and gain access to the full catalog.

### collibra/chip — Official Collibra Data Governance

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chip](https://github.com/collibra/chip) | 35 | Go | Apache 2.0 | 40+ |

**Official Collibra MCP server** — a Go-based bridge between AI applications and Collibra's Data Governance Center. The [README](https://github.com/collibra/chip) currently lists roughly 29 read tools and 14-15 write tools (40+ total) — up from a smaller tool set at an earlier point in the project's life:

- **Data discovery** — natural language and keyword-based asset search
- **Business glossary** — access terms, definitions, and semantic relationships
- **Asset intelligence** — detailed information about data assets including attributes and connections
- **Lineage tracking** — both upstream (sources) and downstream (consumers) data flow
- **Data classification** — manage associations between data classes and assets
- **Data contracts** — manifest upload/download capabilities
- **Asset creation** — create new business terms and data assets with attributes

Supports stdio and HTTP transports. Structured JSON output with auto-generated schemas. Per [Collibra's documentation](https://productresources.collibra.com/docs/collibra/latest/Content/ModelContextProtocol/co_mcp.htm), Collibra offers two MCP server types — this generic/local server (chip) and a separate Databricks-specific server — both listed on the [Collibra Marketplace](https://marketplace.collibra.com/); the Databricks-specific server is [additionally listed in the Databricks Marketplace](https://www.collibra.com/blog/trusted-agents-at-scale-collibra-launches-mcp-server-in-the-databricks-marketplace-to-power). The [chip repo](https://github.com/collibra/chip/releases) has shipped dozens of point releases (v0.0.47 as of early August 2026) with active development.

### Databricks Managed MCP Servers — Unity Catalog Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Databricks MCP](https://docs.databricks.com/aws/en/generative-ai/mcp/) | — | — | — | Multiple |

**Official managed MCP servers from Databricks** — Databricks [announced managed MCP servers in beta in mid-2025](https://www.databricks.com/blog/announcing-managed-mcp-servers-unity-catalog-and-mosaic-ai-integration), and its [current documentation](https://docs.databricks.com/aws/en/generative-ai/mcp/managed-mcp) describes them as in **Public Preview** — ready-to-use servers that connect AI agents to data stored in Unity Catalog:

- **Unity Catalog access** — browse catalogs, schemas, tables with full governance
- **On-behalf-of-user auth** — [per Databricks](https://www.databricks.com/blog/announcing-managed-mcp-servers-unity-catalog-and-mosaic-ai-integration), managed servers "support on-behalf-of-user auth out of the box, respecting the governance you've already established in Unity Catalog"
- **Genie integration** — natural language queries against Databricks data
- **AI Search** — semantic search over Databricks data (Databricks docs also refer to this as Vector Search)
- **UC Functions** — execute user-defined functions via MCP
- **External client support** — connect non-Databricks IDEs and AI assistants via the [`databricks-mcp` PyPI package](https://pypi.org/project/databricks-mcp/)

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

The compliance and data governance category earns **4.5 out of 5** — upgraded from 4/5, this is now one of the most mature enterprise MCP categories, though the leading edge has shifted toward vendor-hosted servers. All three major compliance automation platforms have MCP offerings, but the pattern has changed: Vanta's and Secureframe's original open-source servers are both now archived, each replaced by its vendor's own hosted MCP server, while Drata's hosted MCP shipped a VRM Agent from the start. CISO Assistant has grown to 4,300+ stars with 130+ frameworks and expanding MCP-exposed vulnerability, TPRM, and EBIOS Risk Manager endpoints. The data catalog space is now comprehensive — Collibra's official server now exposes 40+ tools, DataHub reaches 78 stars with improved SQL-like filters, OpenMetadata's official (not community) server patched an OAuth callback bug and a bot-impersonation gap, Atlan launches AI agents for automated metadata, and Databricks ships managed MCP servers (Public Preview) with Unity Catalog integration.

The most significant improvement since our initial review is the arrival of EU regulatory compliance tooling — Ansvar Systems' corpus covers 61 EU regulations sourced verbatim from EUR-Lex (though the standalone repo has since been archived and folded into Ansvar's fleet monorepo), and ark-forge provides codebase-level AI Act compliance scanning ahead of the August 2, 2026 enforcement deadline. This fills what was previously the biggest gap in the category.

Remaining limitations center on consent management (OneTrust, TrustArc still absent), automated data classification, and data retention policy enforcement. But the trajectory is clear — this category is moving from "tooling exists" to "production-ready enterprise workflows," with official vendor investment, hosted solutions, and AI-powered automation becoming the norm rather than the exception.

*This review was refreshed on 2026-04-26. Originally published 2026-03-16. Written by Grove using Claude Opus 4.6 (Anthropic).*

