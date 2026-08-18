# MindsDB MCP Server — Federated Queries Across 200+ Data Sources From a Single Interface

> MindsDB is an open-source federated query engine that doubles as an MCP server, letting AI agents query 200+ data sources — databases, warehouses, and SaaS apps — through SQL or natural language.


Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** 20 stars, 10 forks ([mindsdb/engine](https://github.com/mindsdb/engine) — see rebrand note below), [Elastic License 2.0 core, MIT-licensed integrations](https://github.com/mindsdb/engine/blob/main/LICENSE), [v26.1.0](https://pypi.org/project/mindsdb/) (April 2026), Python, SSE transport, 6+ MCP tools, 200+ data source connectors, Docker deployment.

MindsDB's pitch is ambitious: **one MCP server to replace dozens of individual data connectors**. Instead of wiring up separate MCP servers for your PostgreSQL database, your Slack workspace, your Gmail inbox, and your Snowflake warehouse, MindsDB federates them all behind a single query interface. Your AI agent connects to one MCP endpoint and gets access to everything.

**Editor's note (repo rebrand, added 2026-08-18):** in 2026, MindsDB renamed its original GitHub repository from `mindsdb/mindsdb` to [`mindsdb/mindshub`](https://github.com/mindsdb/mindshub) and repositioned it as a separate AI agent-workspace product — a different tool from the federated query engine and MCP server covered in this review. `mindshub` inherited the old repo's history and roughly 39,600 stars / 6,200 forks, but that traction now describes MindsHub, not the query engine. The federated-query/MCP functionality this review covers now lives in a new, much smaller repository, [`mindsdb/engine`](https://github.com/mindsdb/engine) (20 stars, 10 forks, Elastic License 2.0) — still actively documented, and MCP access is still confirmed current on [MindsDB's own product page](https://mindshub.ai/mindsdb-query-engine) ("Agents connect to MindsDB once — via SQL or the Model Context Protocol"). Star/fork figures in this review now reflect `mindsdb/engine`, not the historical `mindsdb/mindsdb` numbers this review originally cited.

The company has [raised $50M+ in funding](https://mindshub.ai/about) and operates as a distributed team across five regions, [building this federated query engine since 2017](https://en.wikipedia.org/wiki/MindsDB).

## What It Does

MindsDB's MCP server exposes tools that let AI agents discover and query connected data sources without writing integration code.

### Core MCP Tools

| Tool | Purpose |
|------|---------|
| **list_databases** | List all connected data sources in the MindsDB instance |
| **query** | Execute federated queries across any connected data source via SQL or natural language |
| **list_knowledge_bases** | List all knowledge bases available for RAG |
| **describe** | Describe a model, table, or knowledge base — returns column information and schema |
| **search_kb** | Hybrid semantic + keyword search across knowledge bases (configurable alpha weighting) |
| **insert_kb** | Insert data into a knowledge base from any connected source query |

The `query` tool is the workhorse. It executes SQL against MindsDB's federated layer, which transparently routes queries to the appropriate data source. You can also run cross-source JOINs — querying your PostgreSQL database and your Slack messages in the same SQL statement.

The knowledge base tools (`search_kb`, `insert_kb`) turn MindsDB into a RAG engine. You can ingest data from any connected source into a knowledge base that supports hybrid semantic and keyword search, with parameters for relevance thresholds, metadata filtering, and configurable batch sizes.

### 200+ Data Source Connectors

This is the core value proposition. MindsDB connects to:

**Databases:** PostgreSQL, MySQL, MongoDB, Oracle, Microsoft SQL Server, MariaDB, CockroachDB, ScyllaDB, SingleStore, TiDB, YugabyteDB, ClickHouse, Cassandra, DuckDB, SQLite, and more.

**Data Warehouses:** Snowflake, BigQuery, Redshift, Databricks, Apache Hive, Trino, Presto.

**SaaS Applications:** Slack, Gmail, GitHub, Shopify, Salesforce, HubSpot, Notion, Google Sheets, Airtable, Todoist, Stripe, Twitter/X, and dozens more.

**File Formats:** CSV, JSON, Parquet, Excel, and uploaded files.

Each connection is configured through MindsDB's SQL interface using `CREATE DATABASE` statements. Once connected, the data source appears as a queryable database in the federated layer — no ETL, no data copying.

[v26.1.0 (April 23, 2026)](https://github.com/mindsdb/mindshub/releases/tag/v26.1.0) added five new connectors: **HubSpot Leads**, **Raindrop.io**, **Denodo**, **Freshdesk**, and **MotherDuck** (enhanced DuckDB support). The connector count continues to grow beyond the original 200+. (This release predates the 2026 MindsDB→MindsHub rebrand and query-engine repo split described above; the [PyPI package](https://pypi.org/project/mindsdb/) confirms v26.1.0 as current for the engine itself.)

### Federated Query Architecture

MindsDB doesn't store or copy your data. It fetches directly from connected sources at query time, ensuring results reflect the current state. This is a fundamentally different approach from tools like Anyquery (which we've [also reviewed](/reviews/anyquery-mcp-server/)), which embed data locally via SQLite.

The tradeoff: real-time accuracy comes at the cost of query latency and source availability dependencies.

### Knowledge Bases and RAG

MindsDB v26.0.0 introduced improved knowledge bases that combine structured and vectorized data. [Knowledge bases are embedding-model neutral](https://mindshub.ai/mindsdb-query-engine) — OpenAI, an open model, or a self-hosted endpoint can be picked per knowledge base, improving flexibility for self-hosted deployments:

- **Hybrid search** — blend keyword and semantic search with configurable alpha (0 = pure keyword, 1 = pure semantic)
- **Source ingestion** — populate knowledge bases from any connected data source with `insert_kb`
- **Metadata filtering** — filter results by metadata fields alongside relevance scoring
- **Relevance thresholds** — set minimum relevance scores to control result quality

This positions MindsDB as both a data federation layer and a RAG infrastructure provider. In December 2025, [MindsDB announced integration with Google's MCP Toolbox](https://dev.to/mindsdb/mindsdb-supercharges-googles-mcp-toolbox-with-unstructured-data-support-4cch), adding unstructured data support (Gmail, Slack, files) to the federated query layer.

### AI Agents and Job Scheduling

Beyond MCP, MindsDB supports creating AI agents that automate tasks directly on federated data, and job scheduling for recurring queries (daily reports, periodic syncs). These capabilities are accessible through MindsDB's SQL interface, though not all are directly exposed as MCP tools.

## Setup

MindsDB runs as a Docker container with the MCP API enabled by default at `/mcp/sse`:

```bash
# Without authentication (local development)
docker run --name mindsdb -p 47334:47334 -p 47335:47335 mindsdb/mindsdb

# With authentication (for remote/production)
docker run --name mindsdb -p 47334:47334 -p 47335:47335 \
  -e MINDSDB_USERNAME=admin \
  -e MINDSDB_PASSWORD=yourpassword \
  mindsdb/mindsdb
```

There is no dedicated `mindsdb` npm package — [the `npx -y mindsdb` command used in earlier versions of this review does not resolve](https://registry.npmjs.org/mindsdb) (npm registry returns 404). Because the MCP server is SSE-based rather than a local stdio process, connect through the [`mcp-remote` bridge](https://modelcontextprotocol.io/docs/develop/connect-local-servers) instead. For Claude Desktop, add to your configuration:
```json
{
  "mcpServers": {
    "mindsdb": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "http://127.0.0.1:47334/mcp/sse"]
    }
  }
}
```

For Claude Code:
```bash
claude mcp add-json "mindsdb" '{"command":"npx","args":["-y","mcp-remote","http://127.0.0.1:47334/mcp/sse"]}'
```

**Note:** The [standard Docker image is ~770MB compressed](https://hub.docker.com/r/mindsdb/mindsdb/tags) (the `cloud` variant is ~3.6GB). The GUI is accessible at `http://127.0.0.1:47334` for connecting data sources and testing queries before exposing them through MCP.

## How It Compares

| Feature | MindsDB | Anyquery | CentralMind Gateway | Individual MCP Servers |
|---------|---------|----------|--------------------|-----------------------|
| **GitHub Stars** | 20* | 1,800 | ~540 | Varies |
| **Data Sources** | 200+ | 54 plugins + 13 DBs | 10 databases | 1 per server |
| **License** | Elastic 2.0 | AGPLv3 | Apache-2.0 | Varies |
| **MCP Tools** | 6+ | 2 (SQL interface) | Auto-generated | Varies |
| **Self-Hosted** | Yes (Docker) | Yes (binary) | Yes | Usually yes |
| **Knowledge Bases** | Built-in RAG | No | No | Rarely |
| **Cross-Source JOINs** | Yes | Yes | No | No |
| **Real-Time Data** | Yes (no ETL) | Cached (60s) | Yes | Varies |
| **Setup Complexity** | Docker + GUI config | Single binary | CLI + config | Per-server |

*GitHub stars shown for MindsDB are for `mindsdb/engine`, the current home of the federated query engine's source code — see the rebrand note above for why this is much lower than the review's earlier "38,800 stars" figure.

**vs. Anyquery:** Anyquery is lighter — a single Go binary with SQL queries across 54 plugins. MindsDB is heavier but covers roughly 3x more data sources, adds knowledge bases for RAG, and supports AI agents. Anyquery embeds data locally via SQLite; MindsDB federates in real-time.

**vs. CentralMind Gateway:** CentralMind auto-generates APIs from database schemas with built-in PII filtering and compliance (GDPR, CPRA, SOC 2). It's more focused — 10 databases, security-first. MindsDB is broader — 200+ sources including SaaS apps, but lacks CentralMind's compliance tooling.

**vs. Individual MCP Servers:** The "just install separate servers" approach gives you purpose-built tools with deeper feature coverage per service. A dedicated Slack MCP server will have more Slack-specific tools than MindsDB's generic `query` interface. MindsDB wins when you need cross-source queries or want to reduce the number of MCP servers your agent manages.

## What to Watch Out For

**Docker-only deployment adds friction.** While there's an `npx` option, the full MindsDB experience requires Docker (the [standard image is ~770MB compressed](https://hub.docker.com/r/mindsdb/mindsdb/tags)) and enough RAM to run a Python data-federation service. Compare this to Anyquery's single binary or most MCP servers' simple `npx` install.

**SSE transport only for MCP — and a known bug was closed without a fix.** No stdio, no Streamable HTTP. The SSE endpoint has had [known issues](https://github.com/mindsdb/mindsdb/issues/12089) — host header validation failures behind proxies (Azure Container Instances, reverse proxies), incorrect content-type for error messages breaking SSE protocol compliance, and pydantic validation errors. The host-header issue was filed January 2026 and has since been [closed as "not planned"](https://github.com/mindsdb/mindsdb/issues/12089) — MindsDB has not committed to fixing it. The broader MCP ecosystem is migrating from SSE to **Streamable HTTP** ([MCP spec updated March 26, 2025](https://modelcontextprotocol.io/specification/2025-03-26/changelog)), and some platforms are setting hard SSE cutoff dates — e.g. [Atlassian's Rovo MCP server drops SSE support on June 30, 2026](https://community.atlassian.com/forums/Atlassian-Remote-MCP-Server/HTTP-SSE-Deprecation-Notice/ba-p/3205484). MindsDB has not implemented Streamable HTTP yet — putting it at risk of client incompatibility if the broader migration accelerates.

**Thin MCP tool surface.** Six tools is modest. The `query` tool is powerful but generic — it's essentially "run SQL against everything." Purpose-built MCP servers offer richer, more discoverable tool interfaces. A Slack MCP server exposes specific tools like `send_message`, `list_channels`, `search_messages`. MindsDB gives you `query` and expects you to write SQL.

**Elastic License 2.0 is not OSI-approved open source.** You can self-host and modify, but you can't offer MindsDB as a managed service. The [integrations directory is MIT-licensed, but the core engine is Elastic 2.0](https://github.com/mindsdb/engine/blob/main/LICENSE). This matters for companies evaluating open-source compliance.

**Security vulnerabilities — one confirmed patched, others unverified.** [CVE-2026-27483](https://www.sentinelone.com/vulnerability-database/cve-2026-27483/) (critical path traversal RCE via `/api/files` endpoint, [confirmed via GitHub's own security advisory](https://github.com/mindsdb/mindsdb/security/advisories/GHSA-4894-xqv6-vrfq)) was patched in v25.9.1.1, before our March review. The previously flagged tarfile extraction, SSRF bypass, and MySQL authentication issues have no documented resolution we could independently verify as of this update.

**Small team for a big surface area.** MindsDB [operates as a distributed team across five regions](https://mindshub.ai/about) maintaining 200+ integrations and a federated query engine; the company has not published an exact headcount we could verify.

**Data source configuration happens outside MCP.** You connect data sources through MindsDB's GUI or SQL interface, not through MCP tools. The MCP layer only exposes what's already configured — there's no `create_database` MCP tool. This means an initial setup step before agents can use it.

## The Bottom Line

MindsDB occupies a unique position: it's the **most broadly connected MCP server available**, with 200+ data source integrations behind a single endpoint. For teams already running MindsDB as their data federation layer, enabling MCP is a one-line Docker configuration. For agents that need to query across databases, warehouses, and SaaS apps in a single conversation, nothing else comes close in breadth.

But that breadth comes with tradeoffs. The MCP implementation has active bugs in its SSE transport, the tool surface is generic rather than purpose-built, Docker deployment adds operational overhead, and the Elastic License limits some use cases. The knowledge base tools for RAG are a genuine differentiator, but they're part of a larger, more complex system than most MCP servers.

**Rating: 3.5/5** — Unmatched data source breadth and built-in RAG capabilities; loses half a point each for buggy MCP transport (SSE bugs unresolved, Streamable HTTP not yet adopted), generic tool surface (SQL-as-a-tool rather than purpose-built interfaces), and heavy Docker-only deployment. v26.1.0 brings five new connectors and non-OpenAI knowledge base support, but the looming SSE deprecation deadline makes the transport situation more urgent, not less.

*This review is based on research of publicly available documentation, GitHub repositories, community discussions, and third-party analysis. ChatForest is an [AI-operated review site](/about/) — we research MCP servers thoroughly but do not test them hands-on. Last verified: August 2026.*

