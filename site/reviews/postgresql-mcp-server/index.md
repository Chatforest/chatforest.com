# PostgreSQL MCP Servers — The Database That Ate the World Gets an AI Interface

> PostgreSQL has the richest MCP server ecosystem of any database: 2.4k-star Postgres MCP Pro for performance analysis, vendor servers from Supabase (2.6k stars), Neon, pgEdge


**At a glance:** PostgreSQL has the **richest MCP server ecosystem of any database**. The standout is [Postgres MCP Pro](https://github.com/crystaldba/postgres-mcp) (2.4k stars, MIT) from CrystalDBA — offering performance analysis, index tuning, and configurable read/write access. Vendor-backed servers from [Supabase](https://github.com/supabase-community/supabase-mcp) (2.6k stars), [Neon](https://github.com/neondatabase/mcp-server-neon) (565 stars), [pgEdge](https://github.com/pgEdge/pgedge-postgres-mcp) (91 stars), Azure, AWS, and [Google's MCP Toolbox](https://github.com/googleapis/genai-toolbox) (13.5k stars) provide platform-specific integrations. Anthropic's original [reference PostgreSQL server](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres) (now archived) helped catalyze the ecosystem. Part of our **[Databases MCP category](/categories/databases/)**.

PostgreSQL is the **world's most popular open-source relational database** — and it's not close. Originally developed at UC Berkeley in 1986 as the POSTGRES project, PostgreSQL now commands an **18.3% share of the relational database market** with over 39,000 verified enterprise users. The latest release is **PostgreSQL 18** (September 2025, currently at 18.2), which introduced async I/O for up to 3× storage read performance, virtual generated columns, `uuidv7()`, OAuth authentication, and temporal constraints. PostgreSQL's extensibility — with extensions like pgvector for AI embeddings, PostGIS for geospatial data, and pg_stat_statements for query analytics — makes it the default database for modern applications.

**Architecture note:** Unlike the AI provider reviews in our series, PostgreSQL doesn't have a single "official" MCP server from one company. Instead, the ecosystem is **distributed across multiple maintainers** — CrystalDBA, Supabase, Neon, pgEdge, AWS, Azure, Google, and independent developers — each serving different use cases. This distributed model means more choice but also more fragmentation.

## What's Available

### Postgres MCP Pro — crystaldba/postgres-mcp

The **most capable general-purpose PostgreSQL MCP server**, focused on database performance:

| Aspect | Detail |
|--------|--------|
| GitHub | [crystaldba/postgres-mcp](https://github.com/crystaldba/postgres-mcp) — 2.4k stars, 259 forks, 79 commits, MIT |
| Language | Python |
| Install | `pipx install postgres-mcp` or `docker pull crystaldba/postgres-mcp` |
| Transport | stdio + SSE |
| Created by | [CrystalDBA](https://www.crystaldba.ai/) |

**8 MCP tools:**

| Tool | What it does |
|------|-------------|
| `list_schemas` | Enumerate database schemas |
| `list_objects` | Browse schema objects (tables, views, sequences, etc.) |
| `get_object_details` | Inspect table structures, columns, constraints |
| `execute_sql` | Run queries with configurable read-only or unrestricted mode |
| `explain_query` | View execution plans with hypothetical indexing via HypoPG |
| `get_top_queries` | Identify slow queries via pg_stat_statements |
| `analyze_workload_indexes` | Generate index recommendations using industrial-strength algorithms |
| `analyze_db_health` | Comprehensive health assessment (index health, connection utilization, buffer cache, vacuum health) |

**Key differentiator:** Industrial-grade index tuning and performance analysis. The `analyze_workload_indexes` tool uses algorithms that go beyond simple CREATE INDEX suggestions — it evaluates workload-wide index interactions. Requires `pg_stat_statements` and `hypopg` extensions for full performance features.

### Supabase MCP — supabase-community/supabase-mcp

A **full platform management server** for Supabase (which runs PostgreSQL under the hood):

| Aspect | Detail |
|--------|--------|
| GitHub | [supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp) — 2.6k stars, 325 forks, 360 commits, Apache 2.0 |
| Language | TypeScript |
| Install | npm / Smithery |
| Transport | stdio |

**8 feature groups** covering account management, database operations, edge functions, storage, branching, debugging, development, and documentation search. Supports read-only mode and project scoping for security. This is a **Supabase platform server** — it manages more than just PostgreSQL (edge functions, storage, auth) but includes full SQL execution and migration support.

### Neon MCP — neondatabase/mcp-server-neon

**Serverless PostgreSQL management** with natural language:

| Aspect | Detail |
|--------|--------|
| GitHub | [neondatabase/mcp-server-neon](https://github.com/neondatabase/mcp-server-neon) — 565 stars, 103 forks, 189 commits, MIT |
| Language | TypeScript |
| Install | `neonctl@latest init` or manual config |
| Transport | Remote MCP (hosted on Vercel at mcp.neon.tech) |

**30+ tools** across project management, branch operations, SQL execution, database migrations, query optimization, authentication, and documentation search. Unique "prepare/complete" pattern for migrations — test on temporary branches before production. Supports OAuth and API key authentication. **Note:** Intended for local development and IDE integrations only; not recommended for production environments.

### Google MCP Toolbox for Databases — googleapis/genai-toolbox

The **highest-starred database MCP server** (though it covers multiple databases, not just PostgreSQL):

| Aspect | Detail |
|--------|--------|
| GitHub | [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) — 13.5k stars, 1.3k forks, 1,614 commits |
| Language | Go |
| Install | Binary or Docker |
| Transport | MCP + native SDKs (Python, JS, Go) |

Supports PostgreSQL, Cloud SQL for PostgreSQL, AlloyDB, MySQL, SQL Server, Spanner, and Bigtable. Configuration-driven via YAML. Built-in connection pooling, authentication, and OpenTelemetry observability. Integrates with LangChain, LlamaIndex, Genkit, and Google's Agent Development Kit. While not PostgreSQL-specific, it's the most production-hardened option for Google Cloud users.

### AWS Aurora Postgres MCP Server

Part of the [awslabs/mcp](https://github.com/awslabs/mcp) monorepo (8,540 stars total, 68 servers):

| Aspect | Detail |
|--------|--------|
| Location | `awslabs/mcp` monorepo → `src/postgres-mcp-server` |
| Language | Python |
| License | Apache 2.0 |
| Transport | stdio |

Supports connecting to multiple Aurora/RDS PostgreSQL endpoints. Part of the largest official MCP server collection from any company. Inherits the monorepo's comprehensive testing and release infrastructure.

### Additional Servers

| Server | Stars | Language | License | Focus |
|--------|-------|----------|---------|-------|
| [HenkDz/postgresql-mcp-server](https://github.com/HenkDz/postgresql-mcp-server) | 175 | TypeScript | AGPLv3 | 17 consolidated tools (from 46), schema/query/monitoring |
| [call518/MCP-PostgreSQL-Ops](https://github.com/call518/MCP-PostgreSQL-Ops) | 142 | Python | MIT | 30+ ops/monitoring tools, PG 12–18, production-safe |
| [Azure-Samples/azure-postgresql-mcp](https://github.com/Azure-Samples/azure-postgresql-mcp) | 33 | Python | MIT | Azure Database for PostgreSQL, Entra auth, preview |
| [pgEdge/pgedge-postgres-mcp](https://github.com/pgEdge/pgedge-postgres-mcp) | 91 | Go | PostgreSQL License | NLP CLI + Web UI, hybrid search (BM25+MMR+vector), custom YAML tools, **GA April 2026** |
| [neverinfamous/postgres-mcp](https://github.com/neverinfamous/postgres-mcp) | 5 | TypeScript | MIT | 232 capabilities, Code Mode (90% token savings), OAuth 2.1 |

### Anthropic's Archived Reference Server

Anthropic included a PostgreSQL server in the original [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) repository as a reference implementation. It has since been moved to [servers-archived](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres) and is **no longer maintained**. It provided read-only access with schema inspection — useful as an educational example but superseded by the community servers above.

The npm package [@modelcontextprotocol/server-postgres](https://www.npmjs.com/package/@modelcontextprotocol/server-postgres) still exists but points to the archived codebase.

## PostgreSQL Background

| Aspect | Detail |
|--------|--------|
| Origin | UC Berkeley POSTGRES project (1986), nearly 40 years of development |
| Latest version | PostgreSQL 18.2 (February 2026) |
| License | PostgreSQL License (permissive, similar to MIT/BSD) |
| Market share | 18.3% of relational databases ([6sense](https://6sense.com/tech/relational-databases/postgresql-market-share)) |
| Enterprise users | 39,000+ verified companies |
| Top countries | US (44%), Brazil (12%), India (9%) |
| Key extensions | pgvector (AI embeddings), PostGIS (geospatial), pg_stat_statements (query analytics), HypoPG (hypothetical indexes), pg_cron (scheduling) |
| Governance | PostgreSQL Global Development Group (community-driven, no single company) |

PostgreSQL 18 highlights: async I/O subsystem (up to 3× storage read improvement), virtual generated columns, `uuidv7()` for timestamp-ordered UUIDs, OAuth authentication, skip scan for multicolumn B-tree indexes, temporal PRIMARY KEY/UNIQUE/FOREIGN KEY constraints.

## Ecosystem Comparison

| Feature | Postgres MCP Pro | Supabase MCP | Neon MCP | Google Toolbox | AWS Aurora MCP |
|---------|-----------------|--------------|----------|----------------|----------------|
| Stars | 2.4k | 2.6k | 565 | 13.5k | Part of 8.5k monorepo |
| Language | Python | TypeScript | TypeScript | Go | Python |
| License | MIT | Apache 2.0 | MIT | Apache 2.0 | Apache 2.0 |
| PostgreSQL-specific | Yes | Supabase platform | Neon platform | Multi-database | Aurora/RDS |
| Read/write | Configurable | Yes (read-only option) | Yes | Yes | Yes |
| Performance analysis | Yes (index tuning, health) | No | Yes (query optimization) | No | No |
| Transport | stdio + SSE | stdio | Remote (Vercel) | MCP + SDKs | stdio |
| Vendor lock-in | None | Supabase | Neon | Google Cloud | AWS |
| Best for | Any PostgreSQL | Supabase users | Neon users | Google Cloud | AWS users |

## Known Issues

1. **No single "official" PostgreSQL MCP server** — Unlike databases backed by a single company, PostgreSQL's community-driven nature means there's no canonical MCP server endorsed by the PostgreSQL Global Development Group. Developers must evaluate multiple options.

2. **Fragmented ecosystem** — With 10+ PostgreSQL MCP servers of varying quality, developers face choice overload. Postgres MCP Pro and Supabase MCP lead in stars, but different use cases call for different servers.

3. **Anthropic's reference server is archived** — The original MCP PostgreSQL server that helped launch the ecosystem is no longer maintained. Developers who set it up early may not realize it's been superseded.

4. **Security risks with write access** — Several servers support unrestricted SQL execution. Without careful configuration, an AI agent could `DROP TABLE` or corrupt data. Read-only mode should be the default for production databases.

5. **Vendor-specific servers create lock-in** — Supabase MCP, Neon MCP, and Azure PostgreSQL MCP tie you to their platforms. Migrating databases means switching MCP servers too.

6. **Performance features require extensions** — Postgres MCP Pro's best features (index tuning, slow query analysis) require `pg_stat_statements` and `hypopg` extensions. Not all managed PostgreSQL providers support these.

7. **Google Toolbox is not PostgreSQL-focused** — At 13.5k stars, googleapis/genai-toolbox is the highest-starred option, but it's a multi-database tool. PostgreSQL-specific features are limited compared to dedicated servers.

8. **Transport fragmentation** — Some servers use stdio only, others SSE, others remote hosting. No single transport works across all options, complicating setup for users with specific MCP client requirements.

9. **Some servers are early-stage** — pgEdge reached GA in April 2026 but community adoption (91 stars) is still limited; neverinfamous/postgres-mcp has only 5 stars despite 232 capabilities and 370 commits. Neither has been battle-tested at scale by the community.

10. **No MCP server handles PostgreSQL extensions well** — While pg_stat_statements and HypoPG get some support, the broader extension ecosystem (pgvector, PostGIS, pg_cron, pg_partman) lacks deep MCP integration. An AI agent asking about vector similarity search or geospatial queries gets limited help.

## Bottom Line

**Rating: 4.5 out of 5**

PostgreSQL has the **deepest MCP server ecosystem of any database** — and it's not even close. Where most databases have zero or one MCP server, PostgreSQL has **10+ actively maintained options** spanning general-purpose tools, vendor-specific integrations, and specialized monitoring solutions.

**Postgres MCP Pro** (2.4k stars) is the standout for developers who want to bring AI-powered database expertise to any PostgreSQL instance. Its index tuning, workload analysis, and health monitoring tools go well beyond simple SQL execution. **Supabase MCP** (2.6k stars) leads for platform users, offering full Supabase lifecycle management. **Google's Toolbox** (13.5k stars) provides the most production-hardened infrastructure but sacrifices PostgreSQL depth for multi-database breadth.

The **4.5/5 rating** reflects the unmatched variety and quality of PostgreSQL MCP servers. Multiple high-quality options exist (Postgres MCP Pro, Supabase MCP, Neon MCP, Google Toolbox, AWS), the ecosystem is actively maintained with recent commits across all major servers, and both generic and vendor-specific needs are covered. It loses half a point for fragmentation (no canonical server, choice overload), security concerns with write-access defaults, and limited deep extension support (pgvector, PostGIS lack MCP integration).

**Who benefits most from PostgreSQL's MCP ecosystem:**

- **Database administrators** — Postgres MCP Pro's health analysis, index tuning, and slow query identification make it a powerful AI-assisted DBA tool for any PostgreSQL instance
- **Supabase/Neon/AWS users** — vendor-specific servers provide seamless integration with platform features beyond raw PostgreSQL
- **Application developers** — schema exploration and SQL execution via MCP lets AI assistants help write and debug database queries in context
- **DevOps teams** — MCP-PostgreSQL-Ops and similar monitoring-focused servers bring observability to AI workflows

**Who should be cautious:**

- **Production database operators** — carefully evaluate write-access defaults and configure read-only mode; an unconstrained AI agent executing SQL against production data is a significant risk
- **Extension-heavy users** — if your PostgreSQL setup relies heavily on pgvector, PostGIS, or pg_cron, current MCP servers provide limited extension-aware capabilities
- **Teams wanting simplicity** — the sheer number of options can be overwhelming; start with Postgres MCP Pro for general use or your vendor's server for platform-specific needs

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*

