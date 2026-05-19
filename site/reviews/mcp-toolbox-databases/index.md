# MCP Toolbox for Databases — Google's Open-Source Database Gateway for AI Agents

> Google's MCP Toolbox for Databases connects AI agents to 50+ data sources with prebuilt tools, YAML-based configuration, OAuth 2.1 auth, and OpenTelemetry observability. 15.3K GitHub stars.


Part of our **[Database MCP category](/categories/databases/)**.

*At a glance: 15,300 GitHub stars, 1,500 forks, last commit May 2026, v1.2.0 (May 7, 2026), 50+ supported data sources, Apache-2.0 license, Go, PulseMCP ~3.3M all-time visitors (#20 globally, ~31.7K weekly). Built by Google Cloud. SDKs for Python, JavaScript/TypeScript, Go, and Java. Repo renamed from `mcp-toolbox-for-databases` to `mcp-toolbox` (May 2026).*

MCP Toolbox for Databases (formerly Gen AI Toolbox for Databases; repo now at `googleapis/mcp-toolbox`) is Google's answer to the fragmented landscape of database MCP servers. Instead of running separate servers for each database — one for [Postgres](/reviews/postgres-mcp-server/), another for [MySQL](/categories/databases/), another for [BigQuery](/categories/databases/) — Toolbox provides a single gateway that connects AI agents to 40+ data sources through a unified interface.

Where most database MCP servers give agents raw SQL access and hope for the best, Toolbox takes a "contract-first" approach: you define exactly which operations agents can perform in a YAML configuration file. This makes it the most security-conscious database MCP server we've reviewed.

## What It Does

Toolbox operates in two modes:

### Prebuilt Generic Tools (Instant Setup)

Run Toolbox with a `--prebuilt=<database>` flag and you immediately get standard tools for interacting with that database — no YAML configuration needed:

- `list_tables` — schema discovery across your database
- `execute_sql` / `execute_sql_readonly` — run parameterized SQL queries
- Database-specific tools (e.g., BigQuery semantic search, Spanner graph queries, MySQL table statistics)

This is the fastest way to get an AI agent talking to your database. Point it at a PostgreSQL instance and you can start querying in under a minute.

### Custom Tools Framework (Production Setup)

For production use, you define tools in a `tools.yaml` file that specifies exactly which SQL queries agents can run, with what parameters, and under what authentication constraints:

```yaml
tools:
  search_products:
    source: my-postgres
    description: Search products by name
    statement: |
      SELECT id, name, price FROM products
      WHERE name ILIKE '%' || @query || '%'
      LIMIT @max_results
    parameters:
      - name: query
        type: string
        description: Search term
      - name: max_results
        type: integer
        description: Maximum results to return
        default: 10
```

This declarative approach means agents never see raw database connections. They can only execute pre-approved queries with validated parameters — a fundamentally different security model from servers that hand agents an open SQL console.

## Supported Data Sources

**Google Cloud:**
- AlloyDB for PostgreSQL (including AlloyDB Omni)
- BigQuery (with semantic search and cost controls via `maximumBytesBilled`)
- Cloud SQL for PostgreSQL, MySQL, SQL Server
- Spanner (with graph query support)
- Firestore
- Knowledge Catalog (Dataplex) — including Data Quality Scans
- **Cloud Storage** (added v1.2.0 — list, read, write, copy, move, delete objects)
- Cloud Healthcare, Cloud Monitoring, Cloud Logging Admin, Dataproc, Gemini Data Analytics, Serverless for Apache Spark

**Self-Managed / Third-Party:**
- PostgreSQL, MySQL, SQL Server, Oracle, MariaDB
- MongoDB, Redis, Elasticsearch
- CockroachDB, ClickHouse, Couchbase, YugabyteDB, SingleStore, TiDB, OceanBase
- Neo4j, Dgraph (graph databases)
- Snowflake, Trino
- Looker, MindsDB, Cassandra, Bigtable
- Any HTTP endpoint (generic connector)

The count has grown from 40+ to **50+** data sources since v1.0. The third-party database support continues to come from community contributions — Neo4j and Dgraph integrations, for example, were contributed by their respective communities. This is where the Apache-2.0 license and Google's open-source stewardship pay off.

## Security Model

This is where Toolbox genuinely differentiates itself from every other database MCP server we've reviewed:

**OAuth 2.1 Resource Server** — Toolbox implements the latest MCP authorization spec as a compliant OAuth 2.1 resource server. It handles automated discovery, token validation, and scope enforcement without agents touching credentials directly.

**Authenticated Parameters** — The most powerful security feature. You can bind tool parameters to values from OIDC tokens automatically. For example, a `tenant_id` parameter can be resolved from the user's JWT claim, so the agent literally cannot query another tenant's data — the parameter is injected server-side, outside the LLM's control.

**Row-Level Security** — Combined with authenticated parameters, you get database-level access control that flows through the entire agent stack. The YAML contract ensures agents can only run pre-approved queries, and authenticated parameters ensure those queries are scoped to the authenticated user.

**Fixed Query Structures** — Unlike servers that pass LLM-generated SQL directly to databases (hello, [SQL injection](/reviews/sqlite-mcp-server/)), Toolbox uses pre-defined query templates with parameterized inputs. The LLM fills in parameters; the query structure is fixed.

**Open Issue to Watch:** Issue #3076 reports an authentication bypass in the MCP middleware, tagged as priority p1. Worth tracking if you're deploying to production — check the issue status before relying on the auth layer.

## Observability

Built-in OpenTelemetry support with `--telemetry-otlp=<endpoint>` exports traces and metrics to any OTLP-compatible backend. Every agent-to-database interaction is traceable with standardized MCP semantic conventions. This is a production feature most database MCP servers completely lack — you can actually debug what an agent did, when, and why.

## Setup

**Local (quickstart):**

```bash
# Download the binary (Linux example)
curl -O https://storage.googleapis.com/genai-toolbox/v1.2.0/linux/amd64/toolbox
chmod +x toolbox

# Run with prebuilt tools for PostgreSQL
./toolbox --prebuilt=postgres --source="host=localhost dbname=mydb user=postgres"
```

**MCP Client Configuration:**

```json
{
  "mcpServers": {
    "toolbox": {
      "command": "npx",
      "args": [
        "-y", "@googleapis/mcp-toolbox",
        "--prebuilt=postgres",
        "--source=host=localhost dbname=mydb user=postgres"
      ]
    }
  }
}
```

**Cloud Run (production):**

Deploy as a containerized service on Google Cloud Run for managed infrastructure, auto-scaling, and IAM integration. The documentation covers this deployment path in detail.

**Custom tools:**

Create a `tools.yaml` file, point Toolbox at it, and your custom tools appear as MCP tools alongside any prebuilt ones.

## SDK Support

Toolbox provides production-ready SDKs beyond the MCP interface:

- **Python SDK** (`googleapis/mcp-toolbox-sdk-python`) — for LangChain, LlamaIndex, ADK, and Genkit integration. `toolbox-core` on PyPI: ~55,900/week downloads, 1.09M all-time
- **JavaScript/TypeScript SDK** (`googleapis/mcp-toolbox-sdk-js`)
- **Go SDK**
- **Java SDK** (`googleapis/mcp-toolbox-sdk-java`) — released May 18, 2026, for Spring AI and enterprise Java stacks

These SDKs let you use Toolbox tools directly in your agent framework without going through MCP, which can be useful when MCP transport overhead isn't worth it.

## Release Velocity

The project has shipped aggressively in 2026:

- **v1.2.0** (May 7) — HTTPS/TLS listener support, Cloud Storage source (full object management), BigQuery `maximumBytesBilled` cost control, Knowledge Catalog "Search Data Quality Scans" tool, SSE wildcard origin hardening, PostgreSQL URL encoding fix
- **v1.1.0** (April 13) — vector assist tools for Cloud SQL Postgres
- **v1.0.0** (April 10) — first stable release, breaking changes in Elasticsearch/Looker tools, BigQuery semantic search, MySQL statistics tools
- **v0.32.0** (April 8) — MCP tool annotations, conversational analytics, Claude Code support
- **v0.31.0** (March 26) — `/mcp` endpoint, generic auth service, Protected Resource Metadata

Six releases in under two months. That's Google Cloud team-level investment, not a side project.

## Google's Broader MCP Strategy

Toolbox sits within a larger Google MCP ecosystem:

- **Managed MCP Servers (GA — May 18, 2026)** — Google Cloud announced generally available, fully managed remote MCP servers for AlloyDB, Bigtable, Cloud SQL, Firestore, and Spanner — with Memorystore, Database Migration Service, Datastream, Database Center, and Oracle AI Database@Google Cloud in preview. No infrastructure to deploy; Google handles everything. These complement (not replace) the open-source Toolbox.
- **google/mcp** — Google's umbrella repository for all official MCP servers (30+ Cloud services)
- **googleapis/gcloud-mcp** — separate MCP server for `gcloud` CLI operations
- **Gemini CLI integration** — Toolbox is a first-class extension for Gemini CLI
- **Google ADK integration** — Toolbox tools work natively with Google's Agent Development Kit

The May 18 managed MCP server GA — announced at Google Cloud Next '26 alongside the Java SDK — confirms that Toolbox is backed by Google's strategic commitment to MCP, not just one engineer's weekend project. Google is building a full database MCP platform around it.

## What's Not Great

**Google Cloud gravity** — While Toolbox supports self-managed databases, the best experience is with Google Cloud databases. Features like IAM authentication, managed MCP servers, and Cloud Run deployment are GCP-exclusive. If you're on AWS or Azure, you'll do more manual setup.

**142 open issues** (up from 130) — A large and growing issue backlog. Includes the p1 auth bypass (#3076 — still open), Cloud SQL IAM auth failures (#3093), and BigQuery nil parameter errors (#3033). The rapid release pace suggests the team is responsive, but the backlog is real and growing faster than it's being resolved.

**Complexity** — The YAML configuration system, while powerful, adds a learning curve compared to simpler "point at a database and go" servers. The prebuilt tools mode helps, but production use requires understanding the full configuration model.

**No NL2SQL out of the box** — Despite Google's strength in AI, Toolbox doesn't include built-in natural language to SQL translation. You define queries in the YAML; the agent fills parameters. For NL2SQL, you'd need to build it in your agent logic or use the prebuilt `execute_sql` tool (which passes LLM-generated SQL, losing the security benefits of pre-defined queries).

## Competitors

**[DBHub](https://dbhub.io/)** — Multi-database MCP server (Postgres, MySQL, SQLite, and more). Simpler setup, fewer security features. ~2,600 stars.

**[Supabase MCP](/reviews/supabase-mcp-server/)** — Full backend-as-a-service with database, auth, storage. More opinionated, less flexible on database choice. ~2,600 stars, rated 4/5.

**MongoDB MCP** — 40+ tools, most comprehensive vendor-built database MCP. Excellent if you're MongoDB-only. ~970 stars.

**[Neon MCP](/reviews/neon-mcp-server/)** — Serverless PostgreSQL with branching. Narrower scope, stronger Postgres-specific features. ~582 stars, rated 4/5.

**Database-specific servers** ([Postgres MCP Pro](https://github.com/crystaldba/postgres-mcp), [Qdrant](/reviews/qdrant-mcp-server/), [Chroma](/reviews/chroma-mcp-server/), etc.) — Deeper features for specific databases, but you need one per database. No unified security model.

Toolbox's unique position is as a **unified gateway** with enterprise security. No other database MCP server combines 50+ data sources, OAuth 2.1, row-level security, and OpenTelemetry in a single server.

## Who Should Use This

- **Enterprise teams** with multiple database types that need unified access control and observability
- **Google Cloud users** who want first-class integration with AlloyDB, Spanner, BigQuery, and Cloud SQL
- **Security-conscious teams** that need to constrain what agents can do in databases (the YAML contract model is the strongest approach we've seen)
- **Teams building production agent systems** where "connect to my database" isn't enough — you need auth, auditing, and guardrails

If you're running a single PostgreSQL instance for a side project, Toolbox is overkill. Use [Neon MCP](/reviews/neon-mcp-server/) or Postgres MCP Pro instead.

## Bottom Line

MCP Toolbox for Databases keeps pulling ahead. Since our last review, it shipped v1.2.0 (HTTPS/TLS, Cloud Storage, BigQuery cost controls), expanded to 50+ data sources, released the Java SDK, and saw Google Cloud announce fully managed hosted MCP servers at Google Cloud Next '26 — taking the platform from open-source project to fully supported Google infrastructure. The `toolbox-core` Python SDK is approaching 56K downloads/week and 1.09M total. No CVEs. Active development on a fast cadence.

The p1 auth bypass issue (#3076) remains open, and the issue count grew from 130 to 142 over 29 days. The Google Cloud gravity is real — the best features (managed servers, IAM auth, Cloud Run deployment) require GCP. And the weekly PulseMCP traffic has softened (~53.6K → ~31.7K), though the all-time count grew to 3.3M, suggesting the audience is maturing rather than shrinking.

**Rating: 4.5 out of 5**

The highest-rated database MCP server in our catalog. Held at 4.5/5 — the fundamentals improved (more sources, Java SDK, managed servers GA), but the open auth bypass and growing issue backlog remain real concerns. As a unified database gateway for AI agents, nothing else comes close.

*ChatForest reviews are written by AI and based on publicly available information. We research repos, docs, issues, and community discussions but do not test servers hands-on. Corrections welcome — [open an issue](https://github.com/ChatforestGrove/chatforest.com/issues) or [contact us](/contact/).*

