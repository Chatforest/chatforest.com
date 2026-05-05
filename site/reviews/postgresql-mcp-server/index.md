# PostgreSQL MCP Servers — The Database That Ate the World Gets an AI Interface

> PostgreSQL has the richest MCP server ecosystem of any database: bytebase/dbhub (2.7k stars) joins Postgres MCP Pro (2.7k), Supabase MCP (2.7k), Timescale pg-aiguide (1.7k), Neon MCP (594)


**At a glance:** PostgreSQL has the **richest MCP server ecosystem of any database**. Two new major entries join the leader board: [bytebase/dbhub](https://github.com/bytebase/dbhub) (2,687 stars, zero-dependency, token-efficient, multi-database) and [timescale/pg-aiguide](https://github.com/timescale/pg-aiguide) (1,712 stars, the first PostgreSQL AI skills server from a major database vendor). The established leaders — [Postgres MCP Pro](https://github.com/crystaldba/postgres-mcp) (2,686 stars, MIT) from CrystalDBA, [Supabase MCP](https://github.com/supabase-community/supabase-mcp) (2,665 stars, v0.8.0 with RLS advisory injection), and [Neon MCP](https://github.com/neondatabase/mcp-server-neon) (594 stars, heavy OAuth security hardening) — continue to evolve. [Google's MCP Toolbox](https://github.com/googleapis/genai-toolbox) (14,937 stars) hit v1.0.0 GA on April 10 and followed with v1.1.0 adding vector assist tools for Cloud SQL Postgres. Part of our **[Databases MCP category](/categories/databases/)**.

PostgreSQL is the **world's most popular open-source relational database** — and it's not close. Originally developed at UC Berkeley in 1986 as the POSTGRES project, PostgreSQL now commands an **18.3% share of the relational database market** with over 39,000 verified enterprise users. The latest release is **PostgreSQL 18** (September 2025, currently at 18.2), which introduced async I/O for up to 3× storage read performance, virtual generated columns, `uuidv7()`, OAuth authentication, and temporal constraints. PostgreSQL's extensibility — with extensions like pgvector for AI embeddings, PostGIS for geospatial data, and pg_stat_statements for query analytics — makes it the default database for modern applications.

**Architecture note:** Unlike the AI provider reviews in our series, PostgreSQL doesn't have a single "official" MCP server from one company. Instead, the ecosystem is **distributed across multiple maintainers** — CrystalDBA, Bytebase, Supabase, Neon, Timescale, pgEdge, AWS, Azure, Google, and independent developers — each serving different use cases. This distributed model means more choice but also more fragmentation.

## What's Available

### Bytebase/dbhub — Zero-Dependency Multi-Database MCP Server (NEW)

*Not covered in previous reviews — 2,687 stars puts this neck-and-neck with Postgres MCP Pro.*

| Aspect | Detail |
|--------|--------|
| GitHub | [bytebase/dbhub](https://github.com/bytebase/dbhub) — 2,687 stars, MIT |
| Language | TypeScript |
| Install | Zero-dependency npm install |
| Transport | stdio |
| Created | March 2025, actively maintained (updated May 4, 2026) |

**Zero-dependency, token-efficient** multi-database MCP server supporting PostgreSQL, MySQL, SQL Server, MariaDB, and SQLite. Bytebase — the company behind the widely-used database schema change management tool — built dbhub as a lean alternative to heavier database MCP servers. The emphasis on token efficiency matters: bloated tool descriptions waste context window space, especially for LLMs with smaller context limits.

**Why it matters:** At 2,687 stars (matching crystaldba's 2,686), dbhub has achieved in a year what took Postgres MCP Pro longer — and it covers multiple databases from a single install. For teams working across PostgreSQL and MySQL, this is more practical than running separate MCP servers. Bytebase's background in database tooling gives dbhub credibility that most community MCP servers lack.

### Postgres MCP Pro — crystaldba/postgres-mcp

The **most capable general-purpose PostgreSQL MCP server**, focused on database performance:

| Aspect | Detail |
|--------|--------|
| GitHub | [crystaldba/postgres-mcp](https://github.com/crystaldba/postgres-mcp) — 2,686 stars, 259 forks, MIT |
| Language | Python |
| Install | `pipx install postgres-mcp` or `docker pull crystaldba/postgres-mcp` |
| Transport | stdio + SSE |
| Latest release | v0.3.0 (May 2025 — **no new release in 12 months**) |
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

**Stagnation concern:** The last formal release (v0.3.0) was May 2025 — over 12 months ago. Organic star growth continues, but the absence of v0.4.x or any release since May 2025 raises questions about active development. The project remains excellent for its intended use case, but teams evaluating it should check for recent commit activity before committing to it for production workflows.

### Timescale pg-aiguide — PostgreSQL AI Skills & Documentation (NEW)

*Not covered in previous reviews — 1,712 stars from a major database vendor.*

| Aspect | Detail |
|--------|--------|
| GitHub | [timescale/pg-aiguide](https://github.com/timescale/pg-aiguide) — 1,712 stars, Apache-2.0 |
| Language | Python |
| Latest | v0.5.0 (April 28, 2026) |
| Install | `npx` skills or pip |
| Transport | stdio |

**The first dedicated PostgreSQL AI skills server from a major database vendor.** Timescale — best known for TimescaleDB, the PostgreSQL extension for time-series data — built pg-aiguide to help AI coding tools generate better PostgreSQL code. Rather than focusing on query execution or performance analysis, pg-aiguide provides **documentation search, best-practice skills, and PostgreSQL-specific knowledge** that makes LLMs significantly better at writing PostgreSQL code.

**v0.5.0 (April 28, 2026) highlights:**
- PostGIS versioning support
- `npx` skills with a Postgres router — run multiple PostgreSQL skills via a single MCP server
- **Hybrid documentation search using Reciprocal Rank Fusion (RRF)** — combines vector and keyword search for significantly better retrieval quality

**Why it matters:** This fills a unique gap in the ecosystem. Postgres MCP Pro and dbhub help agents *query and manage* PostgreSQL databases. pg-aiguide helps agents *write better PostgreSQL code*. For developers using Claude Code or Cursor to write PostgreSQL queries, migrations, or stored procedures, pg-aiguide provides the PostgreSQL-specific context that makes generated code actually correct.

### Supabase MCP — supabase-community/supabase-mcp

A **full platform management server** for Supabase (which runs PostgreSQL under the hood):

| Aspect | Detail |
|--------|--------|
| GitHub | [supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp) — 2,665 stars, 325 forks, Apache 2.0 |
| Language | TypeScript |
| Install | npm / Smithery |
| Transport | stdio |
| Latest | v0.8.1 (May 1, 2026) |

**8 feature groups** covering account management, database operations, edge functions, storage, branching, debugging, development, and documentation search. Supports read-only mode and project scoping for security. This is a **Supabase platform server** — it manages more than just PostgreSQL (edge functions, storage, auth) but includes full SQL execution and migration support.

**v0.8.0 (April 30, 2026) — significant update:**
- **RLS advisory injection into table listings** — Row-Level Security policies are now surfaced in table listings, helping AI agents understand access controls before attempting data operations
- Improved platform schema validation
- Updated server instructions
- Management API type sync
- **v0.8.1** (May 1): Bug fix for tools not loading on stdio server (issues #269/#261)

### Neon MCP — neondatabase/mcp-server-neon

**Serverless PostgreSQL management** with natural language:

| Aspect | Detail |
|--------|--------|
| GitHub | [neondatabase/mcp-server-neon](https://github.com/neondatabase/mcp-server-neon) — 594 stars, 103 forks, MIT |
| Language | TypeScript |
| Install | `neonctl@latest init` or manual config |
| Transport | Remote MCP (hosted on Vercel at mcp.neon.tech) |

**30+ tools** across project management, branch operations, SQL execution, database migrations, query optimization, authentication, and documentation search. Unique "prepare/complete" pattern for migrations — test on temporary branches before production. Supports OAuth and API key authentication.

**April/May 2026 — extensive OAuth security hardening:**
- OAuth race condition on token refresh fixed
- Removed grant embedding in OAuth state
- OpenAI verification token + tool annotations added
- OAuth Keyv store reinit on connection errors
- **SSE sessions now bound to caller identity** (security fix — previously sessions could be reused across identities)
- OAuth refresh path hardened against missing fields
- Added "Add to Kiro" install badge (new IDE integration)
- Supply chain hardening for GitHub Actions
- Migrated from Bun to pnpm

The flurry of OAuth fixes reflects the broader MCP ecosystem's push toward secure hosted MCP servers in 2026. Neon's remote-hosted transport means these fixes matter more than for stdio-only servers. **Note:** Intended for local development and IDE integrations only; not recommended for production environments.

### Google MCP Toolbox for Databases — googleapis/genai-toolbox

The **highest-starred database MCP server** (though it covers multiple databases, not just PostgreSQL):

| Aspect | Detail |
|--------|--------|
| GitHub | [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) — 14,937 stars, 1.3k forks |
| Language | Go |
| Install | Binary or Docker |
| Transport | MCP + native SDKs (Python, JS, Go) |
| GA milestone | v1.0.0 (April 10, 2026) |
| Latest | v1.1.0 (April 13, 2026) |

Supports PostgreSQL, Cloud SQL for PostgreSQL, AlloyDB, MySQL, SQL Server, Spanner, and Bigtable. Configuration-driven via YAML. Built-in connection pooling, authentication, and OpenTelemetry observability. Integrates with LangChain, LlamaIndex, Genkit, and Google's Agent Development Kit.

**v1.0.0 GA (April 10, 2026):** After months of rapid pre-release iteration, Google's MCP Toolbox hit general availability — the first major multi-database MCP server to reach a stable, supported release milestone.

**v1.1.0 (April 13, 2026 — three days after GA):**
- **Vector assist tools for Cloud SQL Postgres** — AI-native vector search tooling for PostgreSQL running on Google Cloud SQL
- Fixed Looker configuration YAML (→ flat format)
- Documentation: renamed dataplex → knowledge-catalog

The three-day GA-to-v1.1.0 turnaround signals active development rather than post-GA stabilization. For Google Cloud PostgreSQL users, the vector assist tools are meaningful — bringing pgvector-style capabilities to Cloud SQL Postgres through a managed MCP layer.

### subnetmarco/pgmcp — Natural Language Postgres (Previously Untracked)

| Aspect | Detail |
|--------|--------|
| GitHub | [subnetmarco/pgmcp](https://github.com/subnetmarco/pgmcp) — 529 stars |
| Language | Go |
| Focus | "Query any Postgres database in natural language" |
| Last updated | April 23, 2026 |

Natural language interface to PostgreSQL — translates natural language queries to SQL and executes them. 529 stars for a September 2025 project suggests organic traction. Not yet battle-tested enough to rank with the top-tier servers, but worth monitoring.

### AWS Aurora Postgres MCP Server

Part of the [awslabs/mcp](https://github.com/awslabs/mcp) monorepo (8,900 stars total):

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
| [HenkDz/postgresql-mcp-server](https://github.com/HenkDz/postgresql-mcp-server) | 180 | TypeScript | AGPLv3 | 14 consolidated tools, schema/query/monitoring, updated Apr 27 |
| [call518/MCP-PostgreSQL-Ops](https://github.com/call518/MCP-PostgreSQL-Ops) | 150 | Python | MIT | 30+ ops/monitoring tools, PG 12–18, maintenance-only since April |
| [Azure-Samples/azure-postgresql-mcp](https://github.com/Azure-Samples/azure-postgresql-mcp) | 33 | Python | MIT | Azure Database for PostgreSQL, Entra auth, preview |
| [pgEdge/pgedge-postgres-mcp](https://github.com/pgEdge/pgedge-postgres-mcp) | 91 | Go | PostgreSQL License | NLP CLI + Web UI, hybrid search (BM25+MMR+vector), custom YAML tools, GA April 2026 |
| [neverinfamous/postgres-mcp](https://github.com/neverinfamous/postgres-mcp) | 5 | TypeScript | MIT | 232 capabilities, Code Mode (90% token savings), OAuth 2.1 |

### Anthropic's Archived Reference Server

Anthropic included a PostgreSQL server in the original [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) repository as a reference implementation. It has since been moved to [servers-archived](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres) and is **no longer maintained**. It provided read-only access with schema inspection — useful as an educational example but superseded by the community servers above.

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

| Feature | dbhub (Bytebase) | Postgres MCP Pro | pg-aiguide (Timescale) | Supabase MCP | Neon MCP | Google Toolbox |
|---------|-----------------|-----------------|----------------------|--------------|----------|----------------|
| Stars | 2,687 | 2,686 | 1,712 | 2,665 | 594 | 14,937 |
| Language | TypeScript | Python | Python | TypeScript | TypeScript | Go |
| License | MIT | MIT | Apache 2.0 | Apache 2.0 | MIT | Apache 2.0 |
| PostgreSQL-specific | No (multi-DB) | Yes | Yes | Supabase platform | Neon platform | Multi-database |
| Read/write | Yes | Configurable | No (docs/skills) | Yes (read-only option) | Yes | Yes |
| Performance analysis | No | Yes (index tuning, health) | No | No | Yes (query optimization) | No |
| Token-efficient | Yes | Moderate | Yes | Moderate | Moderate | No |
| Transport | stdio | stdio + SSE | stdio | stdio | Remote (Vercel) | MCP + SDKs |
| Vendor lock-in | None | None | None | Supabase | Neon | Google Cloud |
| Best for | Multi-DB, lean setups | Any PostgreSQL performance | Writing better PG code | Supabase users | Neon users | Google Cloud |
| Latest release | — | v0.3.0 (May 2025) | v0.5.0 (Apr 2026) | v0.8.1 (May 2026) | Active commits | v1.1.0 (Apr 2026) |

## Known Issues

1. **No single "official" PostgreSQL MCP server** — Unlike databases backed by a single company, PostgreSQL's community-driven nature means there's no canonical MCP server endorsed by the PostgreSQL Global Development Group. Developers must evaluate multiple options.

2. **Fragmented ecosystem** — With 12+ PostgreSQL MCP servers of varying quality, developers face choice overload. Multiple servers now tie for the top star count, which doesn't simplify the decision.

3. **Postgres MCP Pro stagnation** — The leading dedicated server (crystaldba/postgres-mcp) has had no release since v0.3.0 (May 2025). Star growth continues organically, but lack of releases for 12 months signals slow development. Bytebase/dbhub now ties it in stars with active maintenance.

4. **Anthropic's reference server is archived** — The original MCP PostgreSQL server that helped launch the ecosystem is no longer maintained. Developers who set it up early may not realize it's been superseded.

5. **Security risks with write access** — Several servers support unrestricted SQL execution. Without careful configuration, an AI agent could `DROP TABLE` or corrupt data. Read-only mode should be the default for production databases.

6. **Vendor-specific servers create lock-in** — Supabase MCP, Neon MCP, and Azure PostgreSQL MCP tie you to their platforms. Migrating databases means switching MCP servers too.

7. **Performance features require extensions** — Postgres MCP Pro's best features (index tuning, slow query analysis) require `pg_stat_statements` and `hypopg` extensions. Not all managed PostgreSQL providers support these.

8. **Google Toolbox is not PostgreSQL-focused** — At 14,937 stars, googleapis/genai-toolbox is the highest-starred option, but it's a multi-database tool. PostgreSQL-specific features are limited compared to dedicated servers.

9. **Transport fragmentation** — Some servers use stdio only, others SSE, others remote hosting. No single transport works across all options, complicating setup for users with specific MCP client requirements.

10. **Some servers are early-stage** — subnetmarco/pgmcp (529 stars) and others haven't been battle-tested at scale. Neither has been widely validated for production use.

11. **No MCP server handles PostgreSQL extensions deeply** — While pg_stat_statements and HypoPG get some support, the broader extension ecosystem (pgvector, PostGIS, pg_cron, pg_partman) lacks deep MCP integration. pg-aiguide's PostGIS versioning support in v0.5.0 is a step forward, but comprehensive extension-aware tooling doesn't exist yet.

## Bottom Line

**Rating: 4.5 out of 5**

PostgreSQL has the **deepest MCP server ecosystem of any database** — and it's not even close. Two major entries have emerged since our last review:

**bytebase/dbhub** (2,687 stars) ties Postgres MCP Pro in stars and takes a different approach: zero-dependency, token-efficient, multi-database. Built by Bytebase — a credible database tooling company — dbhub is the lean alternative for teams who want PostgreSQL MCP without extension requirements or for teams running mixed database environments. It's now the first choice for simplicity.

**timescale/pg-aiguide** (1,712 stars, v0.5.0) fills a unique gap: the first PostgreSQL AI skills server. Where other servers help agents query and manage databases, pg-aiguide helps agents *write better PostgreSQL code* — hybrid documentation search via RRF, PostGIS versioning, npx skills routing. For developers using AI coding tools with PostgreSQL, this is the missing piece.

**Postgres MCP Pro** remains the leader for performance analysis and index tuning — but 12 months without a release raises a yellow flag. **Supabase MCP** (v0.8.0, RLS advisory injection) continues to be the best option for Supabase platform users. **Neon MCP** shows strong OAuth security investment through April/May. **Google's Toolbox** hit v1.0.0 GA and immediately delivered Cloud SQL Postgres vector tools in v1.1.0.

The ecosystem has grown from 10+ to 12+ actively maintained options with real traction. The 4.5/5 rating holds — the variety and quality remain unmatched across databases. The half-point deduction remains for fragmentation (no canonical server, choice overload), Postgres MCP Pro's 12-month release gap, and still-limited deep extension support despite pg-aiguide's PostGIS progress.

**Who benefits most from PostgreSQL's MCP ecosystem:**

- **Multi-database teams** — bytebase/dbhub provides lean, token-efficient coverage across PostgreSQL, MySQL, SQL Server, MariaDB, and SQLite in one server
- **Database administrators** — Postgres MCP Pro's health analysis, index tuning, and slow query identification make it a powerful AI-assisted DBA tool for any PostgreSQL instance
- **AI coding tool users** — timescale/pg-aiguide's documentation search and skills help LLMs generate correct PostgreSQL code instead of generic SQL
- **Supabase/Neon/AWS users** — vendor-specific servers provide seamless integration with platform features beyond raw PostgreSQL
- **Application developers** — schema exploration and SQL execution via MCP lets AI assistants help write and debug database queries in context

**Who should be cautious:**

- **Production database operators** — carefully evaluate write-access defaults and configure read-only mode; an unconstrained AI agent executing SQL against production data is a significant risk
- **Extension-heavy users** — if your PostgreSQL setup relies heavily on pgvector or PostGIS, pg-aiguide (v0.5.0 with PostGIS support) helps with code generation, but no server provides deep runtime extension-aware tooling
- **Teams wanting simplicity** — the sheer number of options can be overwhelming; start with bytebase/dbhub for general use, Postgres MCP Pro for performance analysis, or your vendor's server for platform-specific needs

---

## Refresh History {#refresh-history}

**2026-05-05 (first refresh):** TWO MAJOR NEW ENTRIES FOUND: **bytebase/dbhub** (2,687 stars, MIT, TypeScript) — zero-dependency multi-database MCP server from Bytebase that wasn't previously tracked, now ties Postgres MCP Pro in stars. **timescale/pg-aiguide** (1,712 stars, Apache-2.0, Python, v0.5.0 April 28) — Timescale's official PostgreSQL AI skills/documentation server, unique focus on helping LLMs write better PostgreSQL code, hybrid search via RRF. **subnetmarco/pgmcp** (529 stars, Go) — natural language Postgres queries, also previously untracked. **Google Toolbox** 13.5k→14.9k stars, v1.0.0 GA April 10, v1.1.0 April 13 adds Cloud SQL Postgres vector assist tools. **Supabase MCP** v0.8.0/v0.8.1 — RLS advisory injection in table listings, stdio bug fix. **Neon MCP** 565→594 stars, extensive OAuth security hardening throughout April/May (race conditions, SSE session identity binding, token refresh hardening). **Postgres MCP Pro** stagnation: no release since v0.3.0 May 2025 (12 months). Stars crystaldba 2.4k→2.7k, bytebase/dbhub now tied at 2.7k. HenkDz 175→180, call518 142→150. Added dbhub, pg-aiguide, pgmcp to review. Updated ecosystem comparison table. Rating holds 4.5/5.

**2026-03-23 (original review):** Initial review covering Postgres MCP Pro (2.4k stars), Supabase MCP (2.6k stars), Neon MCP (565 stars), Google Toolbox (13.5k stars), AWS Aurora MCP, and 5 additional servers. Rating 4.5/5.

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. See our [About page](/about/) for details on our review process.*

*This review was last refreshed on 2026-05-05 using Claude Sonnet 4.6 (Anthropic).*

