# MCP and Data Governance: How AI Agents Connect to Data Catalogs, Lineage, and Metadata Platforms

> A comprehensive guide to MCP integrations for data governance — covering DataHub, Atlan, Collibra, OpenMetadata, Databricks Unity Catalog, Alation, Google Dataplex, Microsoft


Data catalogs are becoming the context layer for AI agents. Every major data governance platform — from open-source projects like DataHub and OpenMetadata, to enterprise products like Collibra, Atlan, and Alation, to cloud-native services like Databricks Unity Catalog, Google Dataplex, and Microsoft Purview — now offers MCP server integration that gives AI agents access to metadata, lineage, glossaries, ownership, and data quality signals.

This matters because AI agents making data decisions without context make bad decisions. An agent that can query a warehouse but doesn't know which tables are deprecated, who owns a dataset, or what "customer_ltv" actually means in business terms will produce unreliable results. MCP servers for data catalogs close this context gap — giving agents the governed metadata they need to act responsibly.

The landscape is maturing fast. DataHub's official MCP server (v0.5.3) exposes 15+ tools spanning search, lineage, metadata management, and document storage. Atlan provides real-time lineage traversal and quality scanning. Collibra brings enterprise governance policies to agent decision-making. OpenMetadata positions itself as the first enterprise-grade MCP server for metadata, with role-based access control baked in.

This guide covers MCP integrations across the data governance ecosystem — catalogs, lineage tools, metadata platforms, and governance services — with tool inventories, architecture patterns, security considerations, and production recommendations. Our analysis draws on published documentation, open-source repositories, and vendor announcements — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## The Context Gap: Why Data Catalogs Need MCP

AI agents working with data face a fundamental problem: they can access databases and run queries, but they lack the contextual metadata that makes those queries meaningful and safe.

Without catalog context, an agent might:
- Query a deprecated table when a replacement exists
- Join datasets that shouldn't be combined due to different grain or business definitions
- Expose PII columns that governance policies restrict
- Produce reports using uncertified, low-quality data sources
- Break downstream dashboards by modifying upstream schemas without impact analysis

Data catalogs solve this by centralizing metadata — but traditionally, that metadata was accessible only through human-facing UIs. MCP servers change the equation by making this same rich context available to AI agents through standardized tool calls.

As one analysis puts it: "MCP prioritizes connectivity over governance. The protocol lets AI agents discover and invoke tools dynamically at runtime. This makes it powerful. It also makes it dangerous." The data governance MCP ecosystem is where these tensions play out most directly.

## Open-Source Data Catalog MCP Servers

### DataHub — The Metadata Platform for Data and AI

DataHub ([datahub-project/datahub](https://github.com/datahub-project/datahub)) is one of the most widely adopted open-source metadata platforms, originally created at LinkedIn. The official MCP server ([acryldata/mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub)) has ~71 stars, 18 releases, and is at version 0.5.3 (March 2026). Apache 2.0 license.

**Search and discovery tools:**
- `search` — structured keyword search with `/q` syntax for wildcard matching, boolean logic, field-specific filters, pagination, and optional sorting by usage metrics
- `get_entities` — fetch detailed metadata for one or more entities by URN; supports batch retrieval
- `list_schema_fields` — list schema fields for a dataset with keyword filtering and pagination
- `search_documents` — search DataHub's knowledge base with filters for platforms, domains, tags, glossary terms, and owners
- `grep_documents` — content-based regex search within documents

**Lineage and usage tools:**
- `get_lineage` — retrieve upstream or downstream lineage for any entity (datasets, columns, dashboards) with filtering, pagination, and hop control
- `get_lineage_paths_between` — calculate exact lineage paths between two assets
- `get_dataset_queries` — fetch real SQL queries referencing a dataset or column to understand usage patterns, joins, filters, and aggregation behavior

**Metadata management tools** (requires `TOOLS_IS_MUTATION_ENABLED=true`):
- `add_tags` / `remove_tags` — manage tags on entities or schema fields with bulk support
- `add_terms` / `remove_terms` — manage glossary term assignments for business definitions and data classification
- `add_owners` / `remove_owners` — manage ownership assignments
- `set_domains` / `remove_domains` — assign or remove domain classifications
- Description updates with markdown formatting support
- Structured properties management

**User and knowledge tools:**
- `get_me` — authenticated user information
- `save_document` — store knowledge artifacts (insights, decisions, FAQs, notes) organized under configurable parent folders

**Configuration options:**

| Variable | Default | Purpose |
|---|---|---|
| `TOOLS_IS_MUTATION_ENABLED` | `false` | Enable write operations (tags, terms, ownership) |
| `TOOLS_IS_USER_ENABLED` | `false` | Enable user-related tools |
| `SEMANTIC_SEARCH_ENABLED` | `false` | Enable semantic (vector) search |
| `TOOL_RESPONSE_TOKEN_LIMIT` | `80000` | Maximum tokens per tool response |
| `SAVE_DOCUMENT_*` | varies | Customize document storage behavior |

**Deployment options:** DataHub Cloud offers a managed MCP endpoint at `https://<tenant>.acryl.io/integrations/ai/mcp/` with Bearer token authentication. Self-hosted deployments use the open-source server with `DATAHUB_GMS_URL` and `DATAHUB_GMS_TOKEN` environment variables.

**Compatible clients:** Claude Desktop, Claude Code (native streamable HTTP — no proxy needed), Cursor (v1.1+), Windsurf, and OpenAI.

For more on DataHub's role in the broader data ecosystem, see our guide on [MCP and data pipelines](/guides/mcp-data-pipelines-etl/).

### OpenMetadata — Enterprise-Grade Metadata MCP

OpenMetadata ([open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata)) positions itself as "the first enterprise-grade MCP server for metadata." The platform provides an integrated knowledge graph that AI agents access through MCP, with role-based access control enforced at the protocol level. Current release: v1.8.0.

**Key tools:**
- `search_entities_with_query` — search entities using natural language with pagination and sorting
- `get_list_of_tables` — browse available tables
- `get_table_by_fqn` — fetch detailed table metadata by fully qualified name
- `get_table_columns_by_fqn` — retrieve column-level details
- `get_table_owners_by_fqn` — look up dataset ownership
- `get_sample_data` — preview table data

**Core capabilities:**
- Intelligent pipeline monitoring — agents detect failures and anomalies
- Automated dashboard generation from metadata analysis
- Automated data glossary creation
- Data discovery, governance, data quality, and observability through a unified interface

**Architecture:** The MCP server integrates directly into OpenMetadata using the same authorization engine powering its REST APIs. Agents can assume any role or policy defined in the platform, ensuring they get "the proper access to the right data and functional logic to automate data operations."

**Authentication:** Supports JWT token authentication (`OPENMETADATA_HOST` + `OPENMETADATA_JWT_TOKEN`) or username/password authentication. Configuration via `claude_desktop_config.json` or equivalent for other MCP clients.

**Ecosystem:** Multiple community implementations exist on GitHub, including Python-based FastMCP integrations and Java-based Spring Boot servers, each exposing different subsets of the OpenMetadata API.

**Agentic data modeling workflow** (documented by the community): OpenMetadata MCP enables end-to-end agentic workflows where AI agents connect PostgreSQL (schema discovery), dbt (transformation lineage), and Metabase (dashboard dependencies) through automated ingestion pipelines. Agents can then perform impact analysis — tracing what happens downstream when a column is renamed in a dbt model.

For related patterns, see our guide on [MCP and text-to-SQL](/guides/mcp-text-to-sql-natural-language-database/).

## Enterprise Data Catalog MCP Servers

### Atlan — AI-Native Metadata Platform

Atlan is a Leader in the 2026 Gartner Magic Quadrant for Data and Analytics Governance. Its MCP server gives AI agents real-time access to the full metadata layer — lineage, glossary definitions, ownership, quality signals, and access policies.

**Search capabilities:**
- Search assets by keyword, description, certification status, and modification date
- Filter by asset type with pagination and sorting
- Advanced filtering using Atlan's Domain Specific Language (DSL)
- Similarity searches and multi-condition filtering by business impact

**Lineage traversal:**
- Trace upstream and downstream relationships across data stacks
- Explore dependencies and identify impact areas
- Simulate changes to flag risk before implementation

**Quality and governance:**
- Scan for missing descriptions and outdated certifications
- Monitor undocumented assets
- Track PII-tagged columns for compliance
- Identify uncertified data powering downstream assets

**Setup:** Docker deployment using `ghcr.io/atlanhq/atlan-mcp-server:latest` with environment variables `ATLAN_API_KEY`, `ATLAN_BASE_URL`, and `ATLAN_AGENT_ID`. Compatible with Claude, Cursor, and custom MCP clients.

**Example agent queries:** "Which dashboards depend on customer_lifetime_value?" or "What would break if I rename this column?" — the agent traverses Atlan's metadata graph to provide governance-aware answers.

### Collibra — Enterprise Governance for AI Agents

Collibra's MCP server connects AI agents to the Collibra Data Governance Center, enabling governed discovery of business glossaries, data assets, lineage, and policy information.

**Architecture:** Client-server model using JSON-RPC 2.0 for message structures, with transport over STDIO (local) or HTTP/Server-Sent Events (network). Three-phase communication: initialization (protocol version negotiation), message exchange (requests/responses), and termination.

**Core capabilities:**
- Physical data asset discovery (tables, columns, files, reports)
- Business context retrieval (terms, acronyms, KPIs)
- Governed metadata through a standardized interface
- Restrict AI to certified assets based on data classification and usage policies
- Automated hotlists flagging misclassification, policy violations, and missing owners
- Audit trails capturing sources, users, classification, policies, and ownership

**Enterprise use cases:**
- Company-wide chatbots that "answer in business language, resolve acronyms/synonyms, and link only to certified sources"
- Automated data product comparisons with metadata, lineage, and consumer information
- Governed discovery ensuring agents make "smarter, safer, and more compliant decisions"

**Availability:** Available as a local version on the Collibra Marketplace, and also listed in the Databricks Marketplace as part of the Agent Bricks ecosystem.

### Alation — Agentic Data Catalog

Alation's AI Agent SDK ([Alation/alation-ai-agent-sdk](https://github.com/Alation/alation-ai-agent-sdk)) is a Python library that exposes Alation's catalog through MCP-compatible tools.

**Core tools:**
- Natural language search for metadata
- Context retrieval — fetch contextual metadata from the Alation Data Catalog
- Bulk data fetching for retrieving catalog objects at scale

**Integration modes:** STDIO mode for direct MCP client connections and HTTP mode for web applications and API integrations. Available through an Alation sandbox for testing, and in the Databricks Marketplace for Agent Bricks integration.

Alation has announced its evolution into an "agentic platform" — reimagining the data catalog for the AI era with MCP as a core integration pattern.

### Secoda — AI-Native Data Platform

Secoda's MCP server is built into the platform — if you're already using Secoda AI, MCP is live in your workspace with no additional setup required.

**Eight primary tools:**

| Tool | Purpose |
|---|---|
| `search_data_assets` | Locate tables, columns, charts, dashboards |
| `search` | General search across all Secoda resources |
| `run_sql` | Execute queries against connected data warehouses |
| `retrieve_entity` | Access detailed information on data entities |
| `entity_lineage` | Examine upstream/downstream dependencies |
| `glossary` | Retrieve business terminology |
| `get_secoda_docs` | Access knowledge articles |
| `chart` | Work with visualizations |

**Notable feature:** Direct SQL query execution against connected warehouses, meaning agents can discover metadata *and* query data through the same MCP server.

**Setup:** Python 3.8+, Secoda API token, and `API_URL` configuration. Regional instances available (EU: `eu.secoda.co`, APAC: `apac.secoda.co`, self-hosted: custom domain). MIT license.

**Governance:** All operations respect existing workspace permissions. Authentication verifies access at the workspace level, and all interactions are logged for traceability.

### Informatica IDMC — Enterprise Data Management

Informatica's Intelligent Data Management Cloud (IDMC) MCP Server exposes data management capabilities to AI agents — including data discovery, lineage tracking, pipeline management, and master data management.

**Key capabilities:**
- Intelligent data discovery through semantic metadata exposure — query by purpose rather than specific table names
- End-to-end data lineage tracking showing source systems, transformations, and quality rules
- Pipeline management — create and manage data integration pipelines
- MDM operations — create and enrich master data management business entities
- Workflow monitoring across IDMC

**Architecture:** The MCP server exposes Claire (Informatica's AI engine) agent capabilities so that other MCP clients can access IDMC's full suite of data management tools through the standard protocol.

**Timeline:** The dedicated MCP Server for Claire Agents is planned for April 2026 GA.

## Cloud-Native Data Governance MCP

### Databricks Unity Catalog — Managed MCP Servers

Databricks offers managed MCP servers (Public Preview, January 2026) that connect AI agents to data governed by Unity Catalog. This is notable because the MCP servers are *managed* — Databricks handles hosting, authentication, and governance enforcement.

**Managed server types:**
- **Genie spaces** — natural language interfaces to curated datasets
- **Vector Search indexes** — semantic search across documents and data
- **UC Functions** — custom Python/SQL functions registered in Unity Catalog

**Security model:** On-behalf-of-user authentication enforced by default. Unity Catalog permissions are always applied — agents and users can only access tools and data they're authorized to see. No separate permission system to configure.

**OAuth integration:** Databricks provides managed OAuth flows for select external MCP servers (Glean, GitHub, Google Drive, SharePoint), eliminating custom OAuth app registration.

**Roadmap:** Expanding to DBSQL support and building an MCP catalog for discovering, managing, and governing third-party MCP servers.

For more on Databricks MCP integration, see our guide on [MCP and data pipelines](/guides/mcp-data-pipelines-etl/).

### Google Dataplex Universal Catalog — MCP via Toolbox

Google unified the original Data Catalog and Dataplex services into Dataplex Universal Catalog — a single product covering business glossary, column-level lineage for BigQuery, data products, AI/ML asset cataloging for Vertex AI, natural language search, and MCP integration.

**MCP integration:** Uses the MCP Toolbox for Databases as an intermediary between AI agents and Dataplex Universal Catalog. The toolbox acts as an open-source MCP server providing a secure control plane.

**Key tools:**
- `dataplex_lookup_entry` — retrieve metadata including schema, usage, business overview, and contacts for data assets
- `dataplex_search_aspect_types` — search for aspect types across the catalog

**Architecture:** The Gemini CLI extension bundles the MCP server, removing the need for separate server setup. Works with any MCP-compatible client, not just Google tools.

For related Google Cloud MCP integrations, see our guide on [best cloud MCP servers](/guides/best-cloud-mcp-servers/).

### Microsoft Purview — Governance Control Plane

Microsoft Purview has evolved from a passive metadata repository into an active governance control plane for enterprise data and AI. While Purview doesn't yet have a general-purpose MCP server for catalog access, Microsoft has released several governance-related MCP tools.

**Current MCP capabilities:**
- **DLM Diagnostics MCP Server** — open-source, enables AI assistants to analyze and troubleshoot Data Lifecycle Management configurations using read-only PowerShell diagnostics
- **MCP server management in Microsoft 365 admin center** — centralized view and control of all MCP servers across the organization, with a dedicated Tools page for monitoring availability, managing access, and ensuring compliance
- **Fabric integration** — unified data security and governance across the Microsoft data estate, with AI-powered sensitive data protection

**Governance direction:** Microsoft positions MCP server governance as a first-class concern. The admin center provides organizational-level visibility into which MCP servers are deployed, who has access, and how they're being used — a pattern that other platforms are likely to follow.

For more on Microsoft's MCP ecosystem, see our guides on [MCP enterprise infrastructure](/guides/mcp-enterprise-infrastructure/) and [MCP and CI/CD platforms](/guides/mcp-cicd-platform-integrations/).

## Platform Comparison

| Platform | Type | MCP Tools | Lineage | Glossary | Write Ops | Auth Model | License |
|---|---|---|---|---|---|---|---|
| **DataHub** | Open source | 15+ | Column-level | Yes | Optional | Token/Bearer | Apache 2.0 |
| **OpenMetadata** | Open source | 6+ | Yes | Yes | Yes | JWT/RBAC | Apache 2.0 |
| **Atlan** | Commercial | 10+ | Cross-stack | Yes | Limited | API key | Proprietary |
| **Collibra** | Commercial | 5+ | Yes | Yes | No | OAuth/Token | Proprietary |
| **Alation** | Commercial | 3+ | Limited | Yes | No | API key | Proprietary |
| **Secoda** | Commercial | 8 | Yes | Yes | SQL exec | API token | MIT (MCP) |
| **Databricks UC** | Cloud-native | Managed | Via UC | Via UC | Via Functions | OAuth/OBO | Proprietary |
| **Dataplex** | Cloud-native | 2+ | BigQuery | Yes | No | GCP IAM | Open source (Toolbox) |
| **Purview** | Cloud-native | DLM only | Yes | Yes | No | Azure AD | Proprietary |
| **Informatica** | Commercial | GA Apr 2026 | Yes | Yes | Yes | Token | Proprietary |

## Architecture Patterns for Governed AI

### Pattern 1: Catalog-First Agent Architecture

```
User Query → AI Agent → Data Catalog MCP → Metadata Check
                                              ↓
                                         Is asset certified?
                                         Who owns it?
                                         Any PII columns?
                                         What's the lineage?
                                              ↓
                                    Agent decides how to proceed
                                              ↓
                              Database MCP → Execute query (governed)
```

The agent always consults the catalog *before* touching data. This pattern prevents queries against deprecated tables, uncertified data, or restricted columns. DataHub, Atlan, and Collibra MCP servers are designed for this workflow.

### Pattern 2: Impact Analysis Before Change

```
Developer Request → AI Agent → Catalog MCP → get_lineage(upstream + downstream)
                                                ↓
                                          Map all dependencies
                                          Identify affected dashboards
                                          Check downstream consumers
                                          Flag breaking changes
                                                ↓
                                    Agent generates impact report
                                                ↓
                              Human reviews → Approve/Reject change
```

Before making schema changes, data model updates, or pipeline modifications, the agent uses the catalog's lineage tools to trace the full impact. OpenMetadata's agentic data modeling workflow demonstrates this — an agent can trace what happens to downstream Metabase dashboards when a dbt model column is renamed.

### Pattern 3: Continuous Governance Monitoring

```
Scheduled Agent → Catalog MCP → Scan for:
                                  - Undocumented assets
                                  - Missing owners
                                  - Uncertified data in production
                                  - PII without classifications
                                  - Stale descriptions
                                         ↓
                              Generate governance report
                              Flag violations
                              Auto-remediate where safe
```

Atlan's quality scanning tools and DataHub's search capabilities enable agents that continuously audit governance posture. What previously required teams of data stewards working manually can be partially automated through agents operating at machine speed.

### Pattern 4: The Sandbox Model

Rather than giving agents free access to metadata and data, treat AI data access "like a gun range, not a library":

- **Time-bound sessions** — agents get scoped access that expires automatically
- **Checked-out data** — metadata is accessed in controlled environments, not freely copied
- **Session logging** — every tool call is recorded with full context
- **Automatic revocation** — permissions expire when the session ends

This model addresses the fundamental tension that MCP creates: connectivity is powerful, but ungoverned connectivity is dangerous.

## Security Challenges in Data Governance MCP

### The Authentication Gap

The broader MCP ecosystem has a significant authentication problem that directly affects data governance:

- Only ~8% of MCP servers support OAuth
- Nearly half of those OAuth implementations have material flaws
- ~53% of MCP servers use static API keys
- ~88% require some form of credentials

For data catalogs, this is particularly concerning because catalog metadata often reveals the *structure* of an organization's data — table names, column definitions, data classifications, and ownership — even when the underlying data isn't directly accessible.

### Schema Exposure Risk

When an agent connects to a data catalog MCP server, it typically gets access to metadata that describes:
- What data exists (table and column names)
- How data flows (lineage graphs)
- What's sensitive (PII classifications, data tags)
- Who's responsible (ownership information)
- How data is used (query patterns, usage metrics)

This metadata is itself sensitive. An attacker who compromises an MCP connection to a data catalog gets a complete map of an organization's data landscape — which is arguably more valuable than any individual dataset.

### Prompt Injection in Governance Contexts

In MCP environments, successful prompt injection can trigger automated actions across every connected system. For data governance MCP servers specifically, this could mean:
- An agent being tricked into reclassifying PII data as non-sensitive
- Removing governance tags or ownership assignments
- Approving access to restricted datasets
- Generating misleading lineage reports

DataHub mitigates this by disabling mutation tools by default (`TOOLS_IS_MUTATION_ENABLED=false`). This pattern — read-only by default, write access explicitly opted in — should be considered a best practice for all data governance MCP servers.

### Shadow AI Integrations

One documented pattern: "enthusiastic employees connected AI to systems via MCP without proper oversight." In the data governance context, this means shadow agents querying catalogs, building undocumented data pipelines, or using metadata to inform decisions without audit trails.

Microsoft's approach of centralizing MCP server management in the Microsoft 365 admin center — providing organizational visibility into deployed servers, access patterns, and compliance status — represents one response to this challenge.

### Audit Trail Requirements

Organizations without evidence-quality audit trails are reportedly 20-32 points behind on AI maturity metrics, yet 33% lack audit trails entirely. For data governance MCP, every interaction should produce an auditable record:
- What metadata was accessed
- By which agent/user
- For what stated purpose
- What actions resulted

Collibra's MCP server explicitly captures sources, users, classification, policies, and ownership in its audit trails. Secoda logs all MCP interactions for traceability. These should be minimum requirements, not differentiating features.

## Security Best Practices

1. **Read-only by default** — follow DataHub's pattern of disabling mutation tools unless explicitly needed. Most agent workflows only need to *read* catalog metadata, not modify it.

2. **On-behalf-of-user auth** — follow Databricks' pattern where MCP operations inherit the requesting user's permissions. This prevents privilege escalation through agents.

3. **Scope MCP access narrowly** — don't give agents access to the entire catalog. Use domain-based filtering, role-based access, and policy-based restrictions to limit what metadata an agent can see.

4. **Monitor for anomalous access patterns** — an agent that suddenly starts querying metadata about PII columns across multiple domains is suspicious, even if each individual query is authorized.

5. **Encrypt metadata in transit** — catalog metadata reveals organizational structure. Use HTTPS/TLS for all MCP transport, especially for HTTP/SSE-based deployments.

6. **Separate read and write MCP endpoints** — if mutation tools are needed, consider deploying separate MCP server instances with different authentication requirements for read vs. write access.

7. **Implement MCP gateway controls** — centralize MCP governance through gateway solutions that provide authentication, audit trails, and policy enforcement across all connected catalog servers.

## Getting Started Recommendations

**For data engineering teams exploring data governance MCP:**
Start with **DataHub** (open source, 15+ tools, self-hosted option) or **OpenMetadata** (open source, integrated knowledge graph, RBAC). Both let you experiment without licensing costs and offer the most complete MCP tool sets.

**For enterprises already using a data catalog:**
Use your vendor's MCP server — **Atlan**, **Collibra**, **Alation**, or **Secoda** — to avoid duplicating metadata and governance policies. The value of MCP for data governance is proportional to the completeness of your existing catalog.

**For cloud-native organizations:**
Use your platform's managed MCP servers — **Databricks Unity Catalog** for Databricks shops, **Google Dataplex** for GCP, **Microsoft Purview** for Azure. Managed servers handle authentication and governance enforcement, reducing operational overhead.

**For organizations prioritizing security:**
Start in read-only mode. Disable mutation tools. Implement on-behalf-of-user auth. Deploy an MCP gateway. Log everything. Only enable write operations after you've established monitoring and audit trails.

## The Bigger Picture

Data governance MCP servers represent a fundamental shift: metadata is no longer just for humans browsing catalogs — it's infrastructure that AI agents depend on to make responsible data decisions.

Gartner predicts that 40% of enterprise applications will integrate task-specific AI agents by end of 2026, up from less than 5% in mid-2025. As that adoption accelerates, the quality of metadata in your data catalog directly determines the quality of decisions your AI agents make.

The market is projected to reach $10.4 billion by 2026. The organizations that invest in governed metadata infrastructure now — complete catalogs, accurate lineage, well-maintained glossaries, and MCP servers with proper access controls — will have agents that make better, safer decisions than their competitors.

The EU AI Act imposes penalties up to 7% of global revenue for governance failures. Regulators will increasingly ask: "How did AI agents access sensitive data? What did they do with it? Where is the audit trail?" Data governance MCP servers are where those answers need to come from.

For more on building secure MCP deployments, see our [MCP server security guide](/guides/mcp-server-security/). For database-specific MCP patterns, see our guides on [database MCP servers](/guides/best-database-mcp-servers/), [database connection patterns](/guides/mcp-database-connection-patterns/), [text-to-SQL](/guides/mcp-text-to-sql-natural-language-database/), and [data pipelines](/guides/mcp-data-pipelines-etl/). For cloud platform MCP integrations, see our [cloud MCP servers guide](/guides/best-cloud-mcp-servers/). For observability integration, see our [observability MCP servers guide](/guides/best-observability-mcp-servers/). For data analytics and BI, see our [data analytics MCP servers guide](/guides/best-data-analytics-mcp-servers/).

