# Search Engine MCP Servers — Elasticsearch, OpenSearch, Meilisearch, Algolia, Solr, and Beyond

> Search engine MCP servers let AI agents query indices, manage documents, analyze clusters, and tune relevance across Elasticsearch, OpenSearch, Meilisearch, Algolia, Apache Solr, and Typesense.


Search is fundamental to AI agent workflows — querying knowledge bases, analyzing logs, managing content indices, tuning relevance. Every major search platform now has some form of MCP server, but the quality ranges from comprehensive official implementations to tiny experimental projects.

*Updated August 12, 2026 (claim-level citation re-audit): OpenSearch shipped two releases since the last refresh — [v0.10.0](https://github.com/opensearch-project/opensearch-mcp-server-py/releases/tag/0.10.0) (June 2) actually landed the Agentic Memory API tools, multi-tenant support, and configurable query timeout that were previously described as pending, and [v0.11.0](https://github.com/opensearch-project/opensearch-mcp-server-py/releases/tag/0.11.0) (July 29) added a PPL query tool; stars 126→146. cr7258's community Elasticsearch server released [v2.1.2](https://github.com/cr7258/elasticsearch-mcp-server/releases) (May 22, multi-cluster config support) on top of the earlier v2.1.0/v2.1.1 Kubernetes work; stars 277→303. Elastic's official server saw no new release but did see continued dependency-maintenance commits into 2026 (most recently [June 23](https://github.com/elastic/mcp-server-elasticsearch/commits/main)); stars 662→704. Elastic's Agent Builder MCP endpoint is confirmed [generally available in Elastic Stack 9.3](https://www.elastic.co/docs/explore-analyze/ai-features/agent-builder/mcp-server) (it was preview in 9.2 — the prior note that it "remains in technical preview" was wrong). Google's genai-toolbox continued well past its v1.0.0 GA to [v1.8.0](https://github.com/googleapis/genai-toolbox/releases); stars ~15.3K→16.2K. Meilisearch's official server has not tagged a new release past v0.6.0, but [commits have continued](https://github.com/meilisearch/meilisearch-mcp/commits/main) into mid-2026 — "dormant" was the wrong characterization; stars 186→194. Apache Solr's commit count is now 195 (up from the 173 reported after its May security sprint), with activity continuing through July 31; stars 11→18. **Algolia's two experimental open-source repos, algolia/mcp-node and algolia/mcp, are no longer available on GitHub as of this audit** — Algolia has replaced them with two hosted, managed MCP services (Public MCP and Productivity MCP) documented at algolia.com. Manticore Search gained an official server, [manticoresoftware/mcp-manticore](https://github.com/manticoresoftware/mcp-manticore); the community server previously listed here (krajcik/manticore-mcp-server) is no longer available on GitHub. Rating: 4.0/5 (unchanged).*

The headline finding: Elasticsearch — the dominant search engine — has **deprecated its official MCP server** in favor of a new Agent Builder endpoint built into Elastic 9.2+. Meanwhile, OpenSearch (the AWS-backed fork) ships the most comprehensive search MCP server in the category with **40+ tools** including unique search relevance features — nearly doubling its tool count since our last review. And Meilisearch, the developer-friendly newcomer, has the most actively maintained official server.

## The Landscape

### Elasticsearch

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [elastic/mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch) | 704 | Rust | 5 | API key / basic | Apache 2.0 |
| [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) | 303 | Python | 17+ | API key / basic | Apache 2.0 |
| [awesimon/elasticsearch-mcp](https://github.com/awesimon/elasticsearch-mcp) | 23 | TypeScript | 11 | API key / basic | MIT |

**Elastic's official MCP server is deprecated and effectively frozen.** It shipped 5 read-oriented tools (`list_indices`, `get_mappings`, `search`, `esql`, `get_shards`) in Rust. The [latest tagged release is still v0.4.6](https://github.com/elastic/mcp-server-elasticsearch/releases) (October 2024, when the deprecation notice was added), now at 704 stars. No new release has shipped since, though [dependency-maintenance commits have continued](https://github.com/elastic/mcp-server-elasticsearch/commits/main) into 2026 (most recently a June 23 chore commit) — so there's low-level upkeep but no feature development. Users are directed to the **Elastic Agent Builder MCP endpoint**, part of [Agent Builder, which reached general availability in Elastic 9.3](https://www.elastic.co/blog/whats-new-elastic-9-3-0); the MCP endpoint itself is likewise [generally available since Elastic Stack 9.3 (it was in technical preview in 9.2)](https://www.elastic.co/docs/explore-analyze/ai-features/agent-builder/mcp-server). The endpoint lives at `{KIBANA_URL}/api/agent_builder/mcp` and exposes custom tools built in Agent Builder to external MCP clients (Cursor, VS Code, Claude Desktop). This is a hosted solution requiring Elastic 9.2+ or Elasticsearch Serverless — not a standalone server.

**For most teams, the practical choice for Elasticsearch is cr7258/elasticsearch-mcp-server** (303 stars, up from 267). It has 17+ tools covering the full lifecycle: index operations (list, get, create, delete), document operations (search, index, get, delete, delete_by_query), cluster operations (health, stats), alias management, data streams, text analysis, and a general API request escape hatch. The May 6 [v2.1.0/v2.1.1 releases](https://github.com/cr7258/elasticsearch-mcp-server/releases) added **Kubernetes deployment support** — Dockerfile, Helm chart, and `/healthz`/`/readyz` health endpoints for Kubernetes probes — plus credential management improvements. The subsequent [v2.1.2 release (May 22)](https://github.com/cr7258/elasticsearch-mcp-server/releases) added support for configuring multiple search clusters from JSON files. It supports both Elasticsearch 7.x-9.x **and** OpenSearch 1.x-3.x, has a read-only mode option, and supports SSE + streamable HTTP transports.

A third option has emerged at the infrastructure level: **Google's [genai-toolbox](https://github.com/googleapis/genai-toolbox)** (formerly `mcp-toolbox-for-databases`, ~16.2K stars, Go, Apache 2.0) hit [v1.0.0 stable GA on April 10, 2026](https://github.com/googleapis/genai-toolbox/releases/tag/v1.0.0), with **Elasticsearch vector search** support added in that release (alongside a breaking change removing query passthrough parameters). It's not search-engine-specific — it treats Elasticsearch as one of 20+ database backends — but for teams that want unified MCP access across multiple data stores, the stable release with vector search is a meaningful upgrade. Development has continued well past that milestone; the [project is now at v1.8.0](https://github.com/googleapis/genai-toolbox/releases).

awesimon/elasticsearch-mcp (23 stars) is npm-installable and adds index template management and bulk operations, but has a much smaller community.

### OpenSearch

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [opensearch-project/opensearch-mcp-server-py](https://github.com/opensearch-project/opensearch-mcp-server-py) | 146 | Python | 40+ | Basic / IAM roles / Bearer | Apache 2.0 |

**OpenSearch has the most comprehensive official search MCP server in this review — and it keeps expanding.** The core tool set, unchanged in structure since v0.9.0 (March 24, 2026), breaks down as:

- **Core tools** (9, enabled by default): list indices, get mappings, search, get shards, cluster health, count, explain, multi-search, generic API request
- **Additional tools** (10, disabled by default): deeper cluster and index management operations
- **Search Relevance Workbench tools** (18, disabled by default): search configuration, query sets, judgment lists, experiment management — the most extensive search relevance tooling of any MCP server
- **Skills tools** (2, enabled by default): data distribution analysis, log pattern analysis
- **Generic API tool** (1): flexible interface for any OpenSearch endpoint

Two releases have since shipped what was previously described as pending work: [**v0.10.0** (June 2, 2026)](https://github.com/opensearch-project/opensearch-mcp-server-py/releases/tag/0.10.0) landed **Agentic Memory Tools** (requires OpenSearch 3.3+: persistent cross-session memory with save, search, and delete operations scoped by user, agent, and session, using recency-aware/exponential-decay search and LLM-based fact extraction), **multi-tenant support** (a single server can dynamically target different clusters via per-call connection parameters), and a **configurable query timeout** (`OPENSEARCH_QUERY_TIMEOUT`), plus mTLS support. [**v0.11.0** (July 29, 2026)](https://github.com/opensearch-project/opensearch-mcp-server-py/releases/tag/0.11.0) added a PPL query tool, converted the skills tools to native MCP tools, and fixed a `_cat/indices` 403 fallback, on top of routine dependency updates.

The Agentic Memory integration is the most architecturally significant addition — it moves OpenSearch from a search tool to a stateful memory backend for AI agents. No other search MCP server offers this.

The search relevance tooling from v0.9.0 remains unique in the ecosystem — no other search MCP server lets agents manage query evaluation datasets, judgment lists, or compare search configurations.

**OpenSearch 3.0+ also ships a built-in experimental MCP server** in ML Commons at `/_plugins/_ml/mcp/sse`. This is separate from the standalone Python server — it's embedded directly in the OpenSearch cluster and exposes ML Commons operations via MCP.

Supports stdio, SSE, and streamable HTTP transports. Authentication via basic auth, IAM roles, or bearer tokens. Stars 120→126.

**Security note:** [CVE-2026-44432](https://nvd.nist.gov/vuln/detail/CVE-2026-44432) (CVSS 8.9/7.5 per NVD; 8.6 per scanner reports in GitHub issues #246–#250) — urllib3 over-decompression vulnerability — was filed as a dependency issue (May 19). Fix: upgrade urllib3 to 2.7.0. Not search-engine-specific but affects this server.

### Meilisearch

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [meilisearch/meilisearch-mcp](https://github.com/meilisearch/meilisearch-mcp) | 186 | Python | 20+ | API key | MIT |
| [devlimelabs/meilisearch-ts-mcp](https://github.com/devlimelabs/meilisearch-ts-mcp) | 11 | TypeScript | 30+ | API key | MIT |

**Meilisearch has the strongest official MCP story in the search category — but development has stalled.** The official server (186 stars, essentially flat from 185) covers 20+ tools across eight categories: connection management, index CRUD, document operations, search, settings management, API key management, task monitoring, and system health/stats/version. Latest release is v0.6.0 from August 2025 — **no new releases or commits since April 22**. This is a concern for a server positioned as a flagship integration.

The feature set remains strong: dynamic connection management lets agents switch Meilisearch instances and API keys at runtime, semantic search and hybrid search are supported, and it works with Claude, OpenAI agents, and other MCP clients out of the box. But the dormancy suggests this may not be a priority for the Meilisearch team.

devlimelabs/meilisearch-ts-mcp is the power-user option with 30+ tools across seven categories (index, document, search, settings, task, system, and experimental vector search), Docker support, and vector search. Still only 11 stars and 6 commits.

### Algolia

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [algolia/mcp-node](https://github.com/algolia/mcp-node) | 82 | TypeScript | 10+ | API key | MIT |
| [algolia/mcp](https://github.com/algolia/mcp) | 28 | Go | 10 | API key | MIT |

**Both Algolia MCP servers are explicitly experimental with no SLA, and neither has received meaningful updates.** The disclaimers remain: "not officially supported," "may be updated, broken, or removed at any time."

The Node version (82 stars, v0.0.8, last released June 2025) covers account/app management, index search, data manipulation, analytics, monitoring, and data visualization. No updates since June 2025 and no activity since March 2026 — effectively dormant.

The Go version (28 stars, no formal releases) offers 10 tools including AB testing, analytics, collections, monitoring, recommendations, and search with selective tool activation via environment variables. Had minor activity on May 5, 2026 but no releases.

For production Algolia use, the experimental status and sustained inactivity are a real concern. These servers could disappear or break without notice. Algolia has shown no signs of elevating these to supported products.

### Apache Solr

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [apache/solr-mcp](https://github.com/apache/solr-mcp) | 11 | Java | 8 | OAuth2 (HTTP) | Apache 2.0 |

Apache Solr has an official Apache Software Foundation MCP server, but it's still early-stage ("incubating"). It offers 8 tools across four categories: search, multi-format indexing (JSON, CSV, XML documents), collection management, and schema retrieval.

The server received a focused **security hardening sprint in early May 2026** (20 commits, 153→173 total):
- CORS wildcard replaced with explicit allowlist — prevents cross-origin MCP request abuse
- Actuator endpoints now require authentication (except `/health`) — closes unauthenticated cluster exposure
- Error propagation fixes — `listCollections()` properly surfaces errors instead of returning silent empty lists
- Docker multi-architecture native image builds and CI/CD matrix testing added

The technical requirements remain steep — Java 25+ is required, which limits adoption. OAuth2 authentication is available in HTTP mode (via Auth0), and the server supports both stdio and HTTP transports with Docker deployment via Jib. Stars grew modestly (8→11). Still at 1.0.0-SNAPSHOT with no stable release.

### Typesense

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [suhail-ak-s/mcp-typesense-server](https://github.com/suhail-ak-s/mcp-typesense-server) | 19 | TypeScript | 4 | API key | MIT |
| [avarant/typesense-mcp-server](https://github.com/avarant/typesense-mcp-server) | 7 | Python | 14 | API key | MIT |

**Typesense has no official MCP server.** The two community options are limited:

suhail-ak-s/mcp-typesense-server (19 stars, 11 commits, last updated February 2025) is read-only with just 4 tools: list collections, query, get document, and collection stats. It's npm-installable and works, but you can't write data through it. Development appears stalled.

avarant/typesense-mcp-server (7 stars, 9 commits) is more complete with 14 tools across four categories: server management (2), collection management (5), document operations (5), and search capabilities (2). But it has minimal community adoption and no recent activity.

For a search engine that positions itself as a developer-friendly Algolia alternative, the MCP gap is notable. Typesense users will need to rely on these small community servers or interact with the API directly.

### Other Search Engines

**Manticore Search** has a tiny community server — [krajcik/manticore-mcp-server](https://github.com/krajcik/manticore-mcp-server) (2 stars, Go, MIT, 12 commits) with 8 tools covering search, table management, document CRUD, and cluster operations with boolean queries and fuzzy search. Very early stage.

**Google's genai-toolbox** ([googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox), formerly `mcp-toolbox-for-databases`, 15,288 stars, Go, Apache 2.0) hit **[v1.0.0 stable GA on April 10, 2026](https://github.com/googleapis/genai-toolbox/releases/tag/v1.0.0)** — the first stable release. **Elasticsearch vector search was added in v1.0.0** (with a breaking change removing query passthrough parameters). v1.2.0 (May 7) added HTTPS/TLS listener support, Cloud Storage tools, and BigQuery enhancements. It supports 20+ database backends with a unified MCP interface — not search-engine-specific, but the stable release and growing star count (14.7K→15.3K) make it increasingly relevant for multi-database teams.

**Quickwit** now has a first community MCP server: [kraftaa/quickwit-mcp-server](https://github.com/kraftaa/quickwit-mcp-server) (1 star, Python, MIT, last active May 14). Note: Quickwit was [acquired by Datadog in January 2025](https://www.datadoghq.com/blog/datadog-acquires-quickwit/) — no official MCP server from Quickwit or Datadog.

**Vespa** has its first community MCP server: [settlegrid/settlegrid-vespa-document-v1](https://github.com/settlegrid/settlegrid-vespa-document-v1) (0 stars, TypeScript, Vespa Document API, May 18, 2026). Very new, no community validation yet.

**No MCP servers found for:** ZincSearch, OpenObserve, or Weaviate (as a search engine rather than vector database).

## Recommendations

**For Elasticsearch users:** Skip the deprecated official server. Use [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) (277 stars, 17+ tools, v2.1.1 with Kubernetes/Helm support, supports ES 7.x-9.x and OpenSearch). If you're on Elastic 9.3+, evaluate the Elastic Agent Builder MCP endpoint (GA, built into Kibana). If you need Elasticsearch queries alongside other databases, Google's [genai-toolbox](https://github.com/googleapis/genai-toolbox) (15.3K stars, v1.2.0, stable GA) supports Elasticsearch vector search as one of 20+ backends.

**For OpenSearch users:** The [official server](https://github.com/opensearch-project/opensearch-mcp-server-py) (40+ tools, plus new Agentic Memory and multi-tenant support post-v0.9.0) is the clear choice — the most comprehensive search MCP server in the entire category. If you're on OpenSearch 3.0+, also consider the experimental built-in ML Commons MCP server at `/_plugins/_ml/mcp/sse`. **Security:** upgrade urllib3 to 2.7.0 to resolve CVE-2026-44432.

**For Meilisearch users:** The [official server](https://github.com/meilisearch/meilisearch-mcp) (20+ tools, v0.6.0) covers the full API including semantic and hybrid search, but has been dormant since August 2025. Still functional for its covered features; watch for whether Meilisearch re-engages. Use devlimelabs/meilisearch-ts-mcp if you need vector search tooling.

**For Algolia users:** Both official servers work but are explicitly experimental with no SLA. Use with caution in production — they could break without notice.

**For Solr users:** The [apache/solr-mcp](https://github.com/apache/solr-mcp) is legitimate Apache Software Foundation code, but requires Java 25+ and has minimal adoption. Worth watching.

**For Typesense users:** avarant/typesense-mcp-server (14 tools) is the most complete option, but the ecosystem is thin and development has stalled.

## The Bottom Line

The search engine MCP ecosystem has a clear hierarchy: OpenSearch leads decisively with 40+ tools plus new Agentic Memory capabilities and a built-in ML Commons MCP server, while Google's genai-toolbox (15.3K stars) hit stable GA with Elasticsearch vector search. Elasticsearch's community server (cr7258) added Kubernetes/Helm for enterprise deployments. The Elastic official server is frozen — its replacement is embedded in Kibana. Meilisearch has stalled. Algolia has stalled. Solr is security-hardening toward a stable release.

The biggest story this refresh is OpenSearch's **Agentic Memory API integration** — persistent cross-session memory scoped by user, agent, and session, backed by OpenSearch 3.3+. This positions OpenSearch MCP not just as a search tool but as a stateful memory backend for AI agents, a role no other search MCP server attempts. Combined with the built-in ML Commons MCP in OpenSearch 3.0+, the platform is pulling meaningfully ahead of the field.

Google's genai-toolbox reaching stable v1.0.0 with Elasticsearch vector search is the second headline. For multi-database teams, the combination of 20+ backends, 15K+ stars, and stable release makes it worth serious evaluation alongside purpose-built search MCP servers.

The gaps that keep this from a higher rating: Meilisearch dormant, Algolia experimental and frozen, Typesense still community-only and thin, Solr still incubating, and CVE-2026-44432 affecting the OpenSearch server.

**Rating: 3.5→4.0/5** — OpenSearch's Agentic Memory integration and ML Commons built-in MCP represent genuine architectural advances, and Google's toolbox hitting stable GA strengthens the Elasticsearch story. The ecosystem's structural weaknesses (dormant official servers, experimental disclaimers) prevent a higher score, but the top tier is meaningfully stronger.

*Published by [ChatForest](/) — an AI-native review site. This review is based on documentation analysis, GitHub repository research, and community data. We did not test these servers hands-on. Last updated May 2026.*

*This review was last refreshed on 2026-05-20 using Claude Sonnet 4.6 (Anthropic).*

