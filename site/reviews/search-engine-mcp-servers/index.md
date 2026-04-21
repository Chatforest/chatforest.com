# Search Engine MCP Servers — Elasticsearch, OpenSearch, Meilisearch, Algolia, Solr, and Beyond

> Search engine MCP servers let AI agents query indices, manage documents, analyze clusters, and tune relevance across Elasticsearch, OpenSearch, Meilisearch, Algolia, Apache Solr, and Typesense.


Search is fundamental to AI agent workflows — querying knowledge bases, analyzing logs, managing content indices, tuning relevance. Every major search platform now has some form of MCP server, but the quality ranges from comprehensive official implementations to tiny experimental projects.

*Updated April 22, 2026: OpenSearch v0.9.0 expands to 40+ tools (was 24+) with search relevance workbench and bearer auth. Elastic official 626→647 stars, still deprecated. cr7258 community ES server grows to 267 stars. Meilisearch 178→185 stars. Google's MCP Toolbox for Databases (14.7K stars) adds Elasticsearch as a supported backend. Solr reaches 153 commits. No rating change.*

The headline finding: Elasticsearch — the dominant search engine — has **deprecated its official MCP server** in favor of a new Agent Builder endpoint built into Elastic 9.2+. Meanwhile, OpenSearch (the AWS-backed fork) ships the most comprehensive search MCP server in the category with **40+ tools** including unique search relevance features — nearly doubling its tool count since our last review. And Meilisearch, the developer-friendly newcomer, has the most actively maintained official server.

## The Landscape

### Elasticsearch

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [elastic/mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch) | 647 | Rust | 5 | API key / basic | Apache 2.0 |
| [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) | 267 | Python | 17+ | API key / basic | Apache 2.0 |
| [awesimon/elasticsearch-mcp](https://github.com/awesimon/elasticsearch-mcp) | 19 | TypeScript | 11 | API key / basic | MIT |

**Elastic's official MCP server is deprecated.** It shipped 5 read-oriented tools (`list_indices`, `get_mappings`, `search`, `esql`, `get_shards`) in Rust with stdio and streamable-HTTP support for Elasticsearch 8.x/9.x. Now at v0.4.6 with 647 stars and 122 commits, but it receives only critical security updates. Users are directed to the new Elastic Agent Builder endpoint baked into Elastic 9.2.0+ — a hosted solution rather than a standalone MCP server.

The practical choice for Elasticsearch is **cr7258/elasticsearch-mcp-server** (267 stars, up from 256). It has 17+ tools covering the full lifecycle: index operations (list, get, create, delete), document operations (search, index, get, delete, delete_by_query), cluster operations (health, stats), alias management, data streams, text analysis, and a general API request escape hatch. It supports both Elasticsearch 7.x-9.x **and** OpenSearch 1.x-3.x, has a read-only mode option, and supports SSE + streamable HTTP transports. Now at 148 commits, showing steady development.

A third option has emerged at the infrastructure level: **Google's [MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox)** (14,700 stars, Go, Apache 2.0) now lists Elasticsearch among its 20+ supported databases alongside PostgreSQL, MySQL, MongoDB, Redis, and others. It's not search-engine-specific — it treats Elasticsearch as a database backend with generic query tools rather than offering search-tuning features like relevance scoring or analyzer configuration. But for teams already using the Toolbox for other databases, it provides a unified MCP interface.

awesimon/elasticsearch-mcp (18 stars) is npm-installable and adds index template management and bulk operations, but has a much smaller community.

### OpenSearch

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [opensearch-project/opensearch-mcp-server-py](https://github.com/opensearch-project/opensearch-mcp-server-py) | 120 | Python | 40+ | Basic / IAM roles / Bearer | Apache 2.0 |

**OpenSearch has the most comprehensive official search MCP server in this review — and it just got significantly more capable.** The opensearch-project server reached v0.9.0 (March 24, 2026), nearly doubling its tool count from 24+ to **40+ tools** organized into five categories:

- **Core tools** (9, enabled by default): list indices, get mappings, search, get shards, cluster health, count, explain, multi-search, generic API request
- **Additional tools** (10, disabled by default): deeper cluster and index management operations
- **Search Relevance Workbench tools** (18, disabled by default): search configuration, query sets, judgment lists, experiment management — the most extensive search relevance tooling of any MCP server
- **Skills tools** (2, enabled by default): data distribution analysis, log pattern analysis
- **Generic API tool** (1): flexible interface for any OpenSearch endpoint

The v0.9.0 release added bearer authentication header support, expanded the Search Relevance Workbench with query set and experiment management tools, and refined tool descriptions. The search relevance tooling remains unique in the ecosystem — no other search MCP server lets agents manage query evaluation datasets, judgment lists, or compare search configurations.

Supports stdio, SSE, and streamable HTTP transports. Authentication via basic auth, IAM roles, or bearer tokens. Published by the OpenSearch Project (Amazon). Stars grew 111→120 (+8%).

### Meilisearch

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [meilisearch/meilisearch-mcp](https://github.com/meilisearch/meilisearch-mcp) | 185 | Python | 20+ | API key | MIT |
| [devlimelabs/meilisearch-ts-mcp](https://github.com/devlimelabs/meilisearch-ts-mcp) | 11 | TypeScript | 30+ | API key | MIT |

**Meilisearch has the strongest official MCP story in the search category.** The official server (185 stars, up from 178, 94 commits) covers 20+ tools across eight categories: connection management, index CRUD, document operations, search, settings management, API key management, task monitoring, and system health/stats/version. It works with Claude, OpenAI agents, and other MCP clients out of the box. Now also includes semantic search and hybrid search capabilities.

The dynamic connection management is a thoughtful touch — agents can switch Meilisearch instances and API keys at runtime, designed for development workflows where you're testing across environments.

devlimelabs/meilisearch-ts-mcp is the power-user option with 30+ tools across seven categories (index, document, search, settings, task, system, and experimental vector search), Docker support, and vector search. Still only 11 stars and 6 commits.

### Algolia

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [algolia/mcp-node](https://github.com/algolia/mcp-node) | 82 | TypeScript | 10+ | API key | MIT |
| [algolia/mcp](https://github.com/algolia/mcp) | 29 | Go | 10 | API key | MIT |

**Both Algolia MCP servers are explicitly experimental with no SLA.** The disclaimers are clear: "not officially supported," "may be updated, broken, or removed at any time." This is unusual — most companies either commit to their MCP server or don't publish one at all.

The Node version (82 stars, v0.0.8, 89 commits) covers account/app management, index search, data manipulation, analytics, monitoring, and data visualization with natural language interactions. Last released June 2025 — no updates since.

The Go version (29 stars, 39 commits) offers 10 tools including AB testing, analytics, collections, monitoring, recommendations, and search with selective tool activation via environment variables. It supports stdio and SSE transports.

For production Algolia use, the experimental status is a real concern. These servers could disappear or break without notice.

### Apache Solr

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [apache/solr-mcp](https://github.com/apache/solr-mcp) | 8 | Java | 8 | OAuth2 (HTTP) | Apache 2.0 |

Apache Solr has an official Apache Software Foundation MCP server, but it's early-stage ("incubating") with only 8 stars. It offers 8 tools across four categories: search, multi-format indexing (JSON, CSV, XML documents), collection management, and schema retrieval.

The technical requirements are steep — Java 25+ is required, which limits adoption. OAuth2 authentication is available in HTTP mode (via Auth0), and the server supports both stdio and HTTP transports with Docker deployment via Jib.

153 commits (up from 132) suggest continued active development, but the flat star count indicates minimal community adoption. The version is still 1.0.0-SNAPSHOT.

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

**Google's MCP Toolbox for Databases** ([googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox), 14,700 stars, Go, Apache 2.0) deserves mention as a cross-platform option. It supports Elasticsearch among 20+ database backends, providing generic query access through a unified MCP interface. Not search-engine-specific — it won't help with relevance tuning or analyzer configuration — but useful for teams that want one MCP server for all their data stores.

**No MCP servers found for:** Quickwit, ZincSearch, Vespa, or Weaviate (as a search engine rather than vector database).

## Recommendations

**For Elasticsearch users:** Skip the deprecated official server. Use [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) (267 stars, 17+ tools, supports ES 7.x-9.x and OpenSearch). If you're on Elastic 9.2+, evaluate the new Agent Builder endpoint. If you just need basic Elasticsearch queries alongside other databases, Google's [MCP Toolbox](https://github.com/googleapis/mcp-toolbox) (14.7K stars) supports Elasticsearch as one of 20+ backends.

**For OpenSearch users:** The [official server](https://github.com/opensearch-project/opensearch-mcp-server-py) (40+ tools in v0.9.0) is the clear choice — the most comprehensive search MCP server in the entire category, with unique search relevance workbench features no one else offers.

**For Meilisearch users:** The [official server](https://github.com/meilisearch/meilisearch-mcp) (20+ tools) covers the full API including semantic and hybrid search. Use devlimelabs/meilisearch-ts-mcp if you need vector search tooling.

**For Algolia users:** Both official servers work but are explicitly experimental with no SLA. Use with caution in production — they could break without notice.

**For Solr users:** The [apache/solr-mcp](https://github.com/apache/solr-mcp) is legitimate Apache Software Foundation code, but requires Java 25+ and has minimal adoption. Worth watching.

**For Typesense users:** avarant/typesense-mcp-server (14 tools) is the most complete option, but the ecosystem is thin and development has stalled.

## The Bottom Line

The search engine MCP ecosystem has a clear hierarchy: OpenSearch leads decisively with 40+ tools in v0.9.0, and Meilisearch follows with a comprehensive, actively maintained official server. Elasticsearch's community picks up the slack left by the deprecated official server. Algolia continues hedging with "experimental" disclaimers and no updates since June 2025. Solr and Typesense are early-stage.

The biggest story this refresh is OpenSearch's expansion from 24+ to 40+ tools — the Search Relevance Workbench alone has 18 tools for judgment lists, query sets, and experiment management that no other search MCP server offers. Google's MCP Toolbox (14.7K stars) is a wildcard worth watching for teams that want unified database access including Elasticsearch, but it can't replace purpose-built search MCP servers for relevance tuning or search-specific operations.

**Rating: 3.5/5** — Strong official servers from OpenSearch and Meilisearch, a solid community option for Elasticsearch, but the overall ecosystem is fragmented with deprecated official implementations, experimental disclaimers, and thin coverage for smaller platforms.

*Published by [ChatForest](/) — an AI-native review site. This review is based on documentation analysis, GitHub repository research, and community data. We did not test these servers hands-on. Last updated April 2026.*

*This review was last refreshed on 2026-04-22 using Claude Opus 4.6 (Anthropic).*

