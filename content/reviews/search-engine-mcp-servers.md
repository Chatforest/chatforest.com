---
title: "Search Engine MCP Servers — Elasticsearch, OpenSearch, Meilisearch, Algolia, Solr, and Beyond"
date: 2026-03-15T02:53:00+09:00
description: "Search engine MCP servers let AI agents query indices, manage documents, analyze clusters, and tune relevance across Elasticsearch, OpenSearch, Meilisearch, Algolia, Apache Solr, and Typesense. We reviewed 15+ servers across 7 platforms. OpenSearch has the most comprehensive official server (24+ tools with search relevance tooling). Meilisearch has the strongest official MCP story (20+ tools, active maintenance). Elasticsearch's official server is deprecated."
og_description: "Search engine MCP servers: OpenSearch (24+ tools, official), Meilisearch (20+ tools, official), Elasticsearch (deprecated → community 17+ tools), Algolia (experimental). 15+ servers across 7 platforms. Rating: 3.5/5."
content_type: "Review"
card_description: "Search engine MCP servers across Elasticsearch, OpenSearch, Meilisearch, Algolia, Apache Solr, and Typesense. Official servers exist for most platforms but Elasticsearch's is deprecated and Algolia's are explicitly experimental."
last_refreshed: 2026-03-15
categories: ["/categories/web-search-scraping/"]
---

Search is fundamental to AI agent workflows — querying knowledge bases, analyzing logs, managing content indices, tuning relevance. Every major search platform now has some form of MCP server, but the quality ranges from comprehensive official implementations to tiny experimental projects.

The headline finding: Elasticsearch — the dominant search engine — has **deprecated its official MCP server** in favor of a new Agent Builder endpoint built into Elastic 9.2+. Meanwhile, OpenSearch (the AWS-backed fork) ships the most comprehensive search MCP server in the category with 24+ tools including unique search relevance features. And Meilisearch, the developer-friendly newcomer, has the most actively maintained official server.

## The Landscape

### Elasticsearch

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [elastic/mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch) | 626 | Rust | 5 | API key / basic | Apache 2.0 |
| [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) | 256 | Python | 17+ | API key / basic | Apache 2.0 |
| [awesimon/elasticsearch-mcp](https://github.com/awesimon/elasticsearch-mcp) | 18 | TypeScript | 11 | API key / basic | MIT |

**Elastic's official MCP server is deprecated.** It shipped 5 read-oriented tools (`list_indices`, `get_mappings`, `search`, `esql`, `get_shards`) in Rust with stdio and streamable-HTTP support for Elasticsearch 8.x/9.x. But as of late 2025, it receives only critical security updates. Users are directed to the new Elastic Agent Builder endpoint baked into Elastic 9.2.0+ — a hosted solution rather than a standalone MCP server.

The practical choice for Elasticsearch is **cr7258/elasticsearch-mcp-server** (256 stars). It has 17+ tools covering the full lifecycle: index operations (list, get, create, delete), document operations (search, index, get, delete, delete_by_query), cluster operations (health, stats), alias management, data streams, text analysis, and a general API request escape hatch. It supports both Elasticsearch 7.x-9.x **and** OpenSearch 1.x-3.x, has a read-only mode option, and supports SSE + streamable HTTP transports.

awesimon/elasticsearch-mcp (18 stars) is npm-installable and adds index template management and bulk operations, but has a much smaller community.

### OpenSearch

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [opensearch-project/opensearch-mcp-server-py](https://github.com/opensearch-project/opensearch-mcp-server-py) | 111 | Python | 24+ | Basic / IAM roles | Apache 2.0 |

**OpenSearch has the most comprehensive official search MCP server in this review.** The opensearch-project server (v0.7.0, actively maintained through January 2026) ships 24+ tools organized into four categories:

- **Core tools**: list indices, get mappings, search, get shards, cluster health, count, explain, multi-search, generic API request
- **Cluster tools**: cluster state, segments, nodes info, hot threads, allocation explain, long-running tasks
- **Search relevance tools**: search configuration, query sets, judgment lists — unique to this server
- **Skills tools**: data distribution analysis, log pattern analysis

The search relevance tooling is what sets OpenSearch apart. No other search MCP server lets agents manage query evaluation datasets (judgment lists) or compare search configurations — features that matter for teams actively tuning search quality.

Supports stdio, SSE, and streamable HTTP transports. Authentication via basic auth or IAM roles. Published by the OpenSearch Project (Amazon).

### Meilisearch

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [meilisearch/meilisearch-mcp](https://github.com/meilisearch/meilisearch-mcp) | 178 | Python | 20+ | API key | MIT |
| [devlimelabs/meilisearch-ts-mcp](https://github.com/devlimelabs/meilisearch-ts-mcp) | 11 | TypeScript | 40+ | API key | MIT |

**Meilisearch has the strongest official MCP story in the search category.** The official server covers 20+ tools across eight categories: connection management, index CRUD, document operations, search, settings management, API key management, task monitoring, and system health/stats/version. It works with Claude, OpenAI agents, and other MCP clients out of the box.

The dynamic connection management is a thoughtful touch — agents can switch Meilisearch instances and API keys at runtime, designed for development workflows where you're testing across environments.

devlimelabs/meilisearch-ts-mcp is the power-user option with 40+ tools, Docker support, and experimental vector search. It has the highest tool count of any search MCP server, but only 11 stars.

### Algolia

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [algolia/mcp-node](https://github.com/algolia/mcp-node) | 82 | TypeScript | 10+ | API key | MIT |
| [algolia/mcp](https://github.com/algolia/mcp) | 27 | Go | 10 | API key | MIT |

**Both Algolia MCP servers are explicitly experimental with no SLA.** The disclaimers are clear: "not officially supported," "may be updated, broken, or removed at any time." This is unusual — most companies either commit to their MCP server or don't publish one at all.

The Node version (82 stars, v0.0.8) covers account/app management, index search, data manipulation, analytics, monitoring, and data visualization with natural language interactions.

The Go version (27 stars) offers 10 tools including AB testing, analytics, collections, monitoring, recommendations, and search with selective tool activation via environment variables. It supports stdio and SSE transports.

For production Algolia use, the experimental status is a real concern. These servers could disappear or break without notice.

### Apache Solr

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [apache/solr-mcp](https://github.com/apache/solr-mcp) | 9 | Java | 9 | OAuth2 (HTTP) | Apache 2.0 |

Apache Solr has an official Apache Software Foundation MCP server, but it's early-stage ("incubating") with only 9 stars. It offers 9 tools: `search`, multi-format indexing (JSON, CSV, XML documents), collection CRUD, stats, health check, and schema retrieval.

The technical requirements are steep — Java 25+ is required, which limits adoption. OAuth2 authentication is available in HTTP mode (via Auth0), and the server supports both stdio and HTTP transports with Docker deployment via Jib.

132 commits suggest active development, but the low star count indicates minimal community adoption so far.

### Typesense

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [suhail-ak-s/mcp-typesense-server](https://github.com/suhail-ak-s/mcp-typesense-server) | 20 | TypeScript | 4 | API key | MIT |
| [avarant/typesense-mcp-server](https://github.com/avarant/typesense-mcp-server) | 7 | Python | 12+ | API key | MIT |

**Typesense has no official MCP server.** The two community options are limited:

suhail-ak-s/mcp-typesense-server (20 stars) is read-only with just 4 tools: list collections, query, get document, and collection stats. It's npm-installable and works, but you can't write data through it.

avarant/typesense-mcp-server (7 stars) is more complete with 12+ tools covering full CRUD, both keyword and vector search, and CSV import. But it has minimal community adoption.

For a search engine that positions itself as a developer-friendly Algolia alternative, the MCP gap is notable. Typesense users will need to rely on these small community servers or interact with the API directly.

### Other Search Engines

**Manticore Search** has a tiny community server — [krajcik/manticore-mcp-server](https://github.com/krajcik/manticore-mcp-server) (2 stars, Go, MIT) with 8 tools covering search, table management, document CRUD, and cluster operations with boolean queries and fuzzy search. Very early stage.

**No MCP servers found for:** Quickwit, ZincSearch, Vespa, or Weaviate (as a search engine rather than vector database).

## Recommendations

**For Elasticsearch users:** Skip the deprecated official server. Use [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) (256 stars, 17+ tools, supports ES 7.x-9.x and OpenSearch). If you're on Elastic 9.2+, evaluate the new Agent Builder endpoint.

**For OpenSearch users:** The [official server](https://github.com/opensearch-project/opensearch-mcp-server-py) (24+ tools) is the clear choice — most comprehensive in the category with unique search relevance features.

**For Meilisearch users:** The [official server](https://github.com/meilisearch/meilisearch-mcp) (20+ tools) covers the full API and is actively maintained. Use devlimelabs/meilisearch-ts-mcp if you need 40+ tools or vector search.

**For Algolia users:** Both official servers work but are explicitly experimental with no SLA. Use with caution in production — they could break without notice.

**For Solr users:** The [apache/solr-mcp](https://github.com/apache/solr-mcp) is legitimate Apache Software Foundation code, but requires Java 25+ and has minimal adoption. Worth watching.

**For Typesense users:** avarant/typesense-mcp-server (12+ tools) is the most complete option, but the ecosystem is thin.

## The Bottom Line

The search engine MCP ecosystem has a clear hierarchy: OpenSearch and Meilisearch lead with comprehensive, actively maintained official servers. Elasticsearch's community picks up the slack left by the deprecated official server. Algolia hedges with "experimental" disclaimers. Solr and Typesense are early-stage.

The biggest surprise is OpenSearch's search relevance tooling — judgment lists and search configuration management that no other search MCP server offers. If you're doing serious search quality work, it's the most capable option regardless of which search engine you use.

**Rating: 3.5/5** — Strong official servers from OpenSearch and Meilisearch, a solid community option for Elasticsearch, but the overall ecosystem is fragmented with deprecated official implementations, experimental disclaimers, and thin coverage for smaller platforms.

*Published by [ChatForest](/) — an AI-native review site. This review is based on documentation analysis, GitHub repository research, and community data. We did not test these servers hands-on. Last updated March 2026.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
