---
title: "SQL Server MCP Servers — Enterprise Database Gets AI-Powered Performance Monitoring"
date: 2026-03-23T23:30:00+09:00
description: "SQL Server's MCP ecosystem features 15+ dedicated servers, Microsoft's official SQL MCP Server via Data API Builder (production-grade), uniquely powerful performance monitoring from PerformanceMonitor (356 stars"
og_description: "SQL Server MCP ecosystem: official SQL MCP Server via Data API Builder (GA, production-grade), PerformanceMonitor (356 stars, 63 tools), RichardHan's mssql_mcp_server (341 stars), DBHub (2.7k stars), Google Toolbox (15k stars). SQL Server 2025 GA adds native vector + built-in MCP. Rating: 4/5."
content_type: "Review"
card_description: "SQL Server 2025 GA brought a production-ready official SQL MCP Server via Data API Builder — Microsoft's first non-experimental MCP offering. PerformanceMonitor (356 stars, weekly releases) remains the standout with 63 read-only performance analysis tools. DBHub (2.7k stars) and Google Toolbox (15k stars) add breadth. AWS still absent."
last_refreshed: 2026-05-04
---

**At a glance:** SQL Server has an **unexpectedly deep MCP ecosystem** with 15+ dedicated servers and a uniquely powerful performance monitoring story. The standout is [PerformanceMonitor](https://github.com/erikdarlingdata/PerformanceMonitor) (356 stars, C#, MIT) from SQL Server consultant Erik Darling — offering **63 read-only MCP tools** for query performance, execution plans, wait statistics, blocking, deadlocks, and more. That's the most performance-focused MCP tooling of any database. Microsoft now has a **production-ready official SQL MCP Server** via [Data API Builder](https://github.com/Azure/data-api-builder) — first-class in SQL Server 2025, launched GA. The most-starred dedicated general-purpose server is [RichardHan/mssql_mcp_server](https://github.com/RichardHan/mssql_mcp_server) (341 stars, Python, MIT), though it remains stalled. Multi-database servers [Bytebase DBHub](https://github.com/bytebase/dbhub) (2.7k stars) and [Google's MCP Toolbox](https://github.com/googleapis/genai-toolbox) (15k stars) also support SQL Server. Part of our **[Databases MCP category](/categories/databases/)**.

SQL Server is **Microsoft's flagship relational database** — commanding roughly **30% of the relational database market**, second only to MySQL. Born from a partnership with Sybase in 1987, Microsoft forked the product in 1994 and released SQL Server 6.0 (1995) as the first fully Microsoft-developed version. The current GA release is **SQL Server 2022** (November 2022, CU18+), with **SQL Server 2025** in preview. SQL Server's enterprise features — T-SQL, Always On availability groups, In-Memory OLTP, ColumnStore indexes, ML Services, and graph database capabilities — make it the default database for Windows/.NET enterprise shops. Notable users include Stack Overflow, Bank of America, Dell, and GEICO. Microsoft's cloud offerings include Azure SQL Database (PaaS) and Azure SQL Managed Instance.

**Architecture note:** SQL Server's MCP ecosystem has a distinctive shape. Unlike PostgreSQL's community-led approach or MySQL's community-only approach, SQL Server now has both an official production-grade offering (Data API Builder SQL MCP Server) and unmatched performance monitoring tooling (PerformanceMonitor + PerformanceStudio). The trade-off is ecosystem fragmentation across four languages and the most-starred dedicated general-purpose server remaining stalled.

## What's New (May 2026 Update)

**SQL Server 2025 GA — and a production-ready official SQL MCP Server.** SQL Server 2025 (17.x) launched GA at Microsoft Ignite on November 18, 2025. The most significant MCP-relevant change: the **SQL MCP Server is now a first-class, documented feature** in SQL Server 2025 — implemented through **Data API Builder (DAB) v1.7+** and listed directly in the SQL Server 2025 What's New documentation. This replaces the experimental Azure-Samples/MssqlMcp demo as Microsoft's canonical SQL Server MCP offering.

**Data API Builder SQL MCP Server is production-grade.** Unlike the Azure-Samples demo (explicitly "NOT intended for production use"), the DAB-based SQL MCP Server is open-source, free, actively maintained, and designed for real deployments. It supports SQL Server, Azure SQL, PostgreSQL, MySQL, and Cosmos DB through a single server. Critically, it does not attempt NL2SQL — instead using a deterministic NL2DAB model with proper RBAC, OpenTelemetry tracing, caching, and health checks. Tools: `describe_entities`, `create_record`, `read_records`, `update_record`, `delete_record`, `execute_entity`, `aggregate_records`. Custom tools via stored procedures. DAB v2.0 is in preview. (See the updated Microsoft section below.)

**SQL Server 2025 adds native vector support and AI-native T-SQL.** New features relevant to MCP/AI agents: native `vector` data type, `VECTOR_DISTANCE` and `VECTOR_NORMALIZE` functions, vector indexes (approximate nearest neighbor), `CREATE EXTERNAL MODEL` (manage Azure OpenAI/Ollama/Foundry connections), `AI_GENERATE_CHUNKS` and `AI_GENERATE_EMBEDDINGS` built into T-SQL, native regex (REGEXP_LIKE, REGEXP_REPLACE), and fuzzy string matching (EDIT_DISTANCE, JARO_WINKLER). SQL Server 2025 positions as an AI-ready database in a way 2022 did not.

**PerformanceMonitor is on a weekly release cadence.** Stars grew from 272 → 356 (+31%) since March 2026. Erik Darling shipped v2.6 through v2.9 in April alone. Recent additions include per-database collector exclusions, resume gap detection, Azure SQL DB collector hardening, Host OS column, and a nightly build channel. Still the most powerful performance monitoring tool in any database MCP ecosystem.

**PerformanceStudio growing fast.** Stars: 120 → 178 (+48%). Shipped v1.7.x through v1.9.0 in April alone — multiple releases per week. Now explicitly bills itself as having a "built-in MCP server for AI-assisted plan review." New: minimap, colored links, cursor-aware analysis rules.

**RichardHan/mssql_mcp_server remains stalled.** 323 → 341 stars (+6%), all organic discovery. Last commit: November 2, 2025. No activity in 2026. With the DAB SQL MCP Server now available as a maintained official option, the case for RichardHan as the go-to general-purpose server has weakened.

**AWS still has no SQL Server MCP server.** AWS's awslabs/mcp monorepo reached 8,941 stars (was 8.5k) with 60+ servers including dedicated PostgreSQL and MySQL entries — but SQL Server remains absent despite AWS offering RDS for SQL Server. This gap persists.

**microsoft/mcp catalog at 3,089 stars** (was 2,840) — still no standalone SQL Server entry. The official SQL Server MCP story runs through Data API Builder, not this catalog.

**Rating upgraded: 3.5/5 → 4/5.** The addition of a production-grade, actively maintained official Microsoft SQL MCP Server — combined with SQL Server 2025's native AI and vector capabilities, and PerformanceMonitor's rapid growth — materially improves the ecosystem picture. Penalties remain for: stalled top community server, fragmented ecosystem across four languages, continued AWS absence.

## What's Available

### PerformanceMonitor — erikdarlingdata/PerformanceMonitor

The **most impressive SQL Server MCP server** — and arguably the most powerful database performance MCP tool in any ecosystem:

| Aspect | Detail |
|--------|--------|
| GitHub | [erikdarlingdata/PerformanceMonitor](https://github.com/erikdarlingdata/PerformanceMonitor) — 356 stars, 32 forks, 100+ commits, MIT |
| Language | C# |
| Created by | [Erik Darling](https://www.erikdarlingdata.com/) (well-known SQL Server consultant) |
| Supports | SQL Server 2016–2025, Azure SQL MI, AWS RDS, Azure SQL Database |

**Two editions:**

| Edition | Collectors | MCP Tools | Storage | Install |
|---------|-----------|-----------|---------|---------|
| Full | 32 T-SQL collectors | **63 read-only tools** | PerformanceMonitor database, SQL Agent jobs | Requires SQL Server instance |
| Lite | 23 collectors | **52 read-only tools** | DuckDB + Parquet files | Standalone desktop app |

**What it monitors:**

- Query performance and execution plans with graphical plan viewer
- Wait statistics and CPU utilization
- Memory grants and buffer pool usage
- File I/O and TempDB activity
- Blocking chains and deadlock detection
- SQL Agent job history
- Real-time alerts for blocking, deadlocks, high CPU, long-running queries

**Key differentiator:** 63 read-only MCP tools for SQL Server performance monitoring. No other database MCP server in any ecosystem comes close to this depth of performance analysis. The 30-rule PlanAnalyzer evaluates execution plans for issues like memory grant problems, row estimate mismatches, missing indexes, spills, and parallel skew. Auto-installs community tools sp_WhoIsActive and sp_BlitzLock. No telemetry — all data stays local.

### PerformanceStudio — erikdarlingdata/PerformanceStudio

A **companion execution plan analyzer** with MCP integration:

| Aspect | Detail |
|--------|--------|
| GitHub | [erikdarlingdata/PerformanceStudio](https://github.com/erikdarlingdata/PerformanceStudio) — 178 stars, 20 forks, 100+ commits, MIT |
| Language | C# |
| MCP Tools | 13 tools (disabled by default, localhost only) |
| Install | Cross-platform GUI + CLI + SSMS extension (SSMS 18–22) |
| Transport | HTTP MCP |

**MCP tools include:** `analyze_plan`, `get_missing_indexes`, `compare_plans`, `get_query_store_top`. The 30+ analysis rules cover memory grants, row estimate mismatches, missing indexes, spills, and parallel skew. This is purpose-built for DBAs who want AI assistance with execution plan analysis.

### mssql_mcp_server — RichardHan/mssql_mcp_server

The **most-starred general-purpose SQL Server MCP server:**

| Aspect | Detail |
|--------|--------|
| GitHub | [RichardHan/mssql_mcp_server](https://github.com/RichardHan/mssql_mcp_server) — 341 stars, 90 forks, 26 commits, MIT |
| Language | Python |
| Install | `pip install microsoft_sql_server_mcp` or `uvx microsoft_sql_server_mcp` |
| Supports | SQL Server, SQL Server LocalDB, Azure SQL Database |

**Tools:** List tables, read data, execute SQL queries. Supports both SQL authentication (user/password) and Windows Authentication. Configuration via environment variables (MSSQL_SERVER, MSSQL_DATABASE, MSSQL_PORT).

**Concern:** Last push was November 2, 2025 — confirmed stalled with no 2026 activity, 26 total commits, 12 open issues. Despite being the most-starred dedicated community server, it's no longer the best-maintained option. With Microsoft's production-grade Data API Builder SQL MCP Server now available, RichardHan is no longer the recommended first choice for general-purpose SQL Server MCP access.

### mssql-mcp — Aaronontheweb/mssql-mcp

A **.NET-native SQL Server MCP server** for the C# ecosystem:

| Aspect | Detail |
|--------|--------|
| GitHub | [Aaronontheweb/mssql-mcp](https://github.com/Aaronontheweb/mssql-mcp) — 144 stars, 20 forks, 21 commits, Apache-2.0 |
| Language | C# |
| Tools | `execute_sql`, `list_tables`, `list_schemas` |
| Transport | stdio |

Uses Akka.NET for internal coordination and the official MCP C# SDK. Docker support available. The author's pitch: "Because the other MCP solutions...are generally janky...not on Windows." A natural fit for .NET shops already running SQL Server.

### mssql-mcp-server — dperussina/mssql-mcp-server

A **Node.js option** with pattern-based discovery:

| Aspect | Detail |
|--------|--------|
| GitHub | [dperussina/mssql-mcp-server](https://github.com/dperussina/mssql-mcp-server) — 74 stars, 41 forks, 20 commits, GPL-3.0 |
| Language | JavaScript |
| Transport | stdio + HTTP/SSE |

**Tools:** `discover_database`, `table_details`, `execute_query`, `discover_tables`, `get_query_results`. Pattern-based table discovery, pagination, CTEs/window functions/JSON operations. Read-only by default.

**Note:** GPL-3.0 license may be incompatible with some enterprise deployment policies.

### ConnorBritain/mssql-mcp-server — Enterprise-Grade

The **most governance-focused SQL Server MCP server:**

| Aspect | Detail |
|--------|--------|
| GitHub | [ConnorBritain/mssql-mcp-server](https://github.com/ConnorBritain/mssql-mcp-server) — 10 stars, 5 forks, 50 commits, MIT |
| Language | C# |
| Tools | 20 tools across 6 categories |

**Package tiers:** Reader (14 tools), Writer (17 tools), Server (all 20 tools). Multi-environment support (prod/staging/dev), audit logging (JSON Lines), secret management, and **Preview+Confirm for mutations** — the only SQL Server MCP server with built-in write-operation governance. Tools include `search_schema`, `profile_table`, `inspect_relationships`, `inspect_dependencies`, `explain_query`, and full CRUD.

### Microsoft's Official SQL MCP Server — Data API Builder

| Aspect | Detail |
|--------|--------|
| Code | [Azure/data-api-builder](https://github.com/Azure/data-api-builder) (DAB) |
| Status | **GA — production-ready, first-class in SQL Server 2025** |
| Databases supported | SQL Server, Azure SQL, PostgreSQL, MySQL, Cosmos DB |
| MCP tools | `describe_entities`, `create_record`, `read_records`, `update_record`, `delete_record`, `execute_entity`, `aggregate_records` |
| Custom tools | Via stored procedures (`custom-tool: true`) |
| Auth | Full RBAC, Azure AD |
| Observability | OpenTelemetry tracing, health checks, caching |

**The key upgrade:** The Azure-Samples/SQL-AI-samples/MssqlMcp experimental demo (306 stars, dormant since Nov 2025) has been superseded by the Data API Builder SQL MCP Server, which shipped GA in DAB v1.7+ and is referenced directly in the SQL Server 2025 What's New docs. Unlike the demo, this is an actively maintained, production-grade offering.

**Intentionally anti-NL2SQL.** The DAB SQL MCP Server does not expose raw SQL execution — instead using a deterministic NL2DAB (Natural Language to Data API Builder) model where the AI interacts with defined entities and operations. This is a deliberate security and reliability choice: agents work with schema-validated entity operations, not arbitrary query strings. For teams that need raw SQL, the community servers remain necessary.

**The experimental demo lives on (but dormant).** Azure-Samples/SQL-AI-samples (317 stars) still hosts the old MssqlMcp .NET and Node.js implementations — but the last meaningful push was November 2025. It's still accessible but no longer the canonical approach.

### Additional Notable Servers

| Server | Stars | Language | License | Key Feature |
|--------|-------|----------|---------|-------------|
| [JexinSam/mssql_mcp_server](https://github.com/JexinSam/mssql_mcp_server) | 56 | Python | MIT | Simple pip install, basic CRUD |
| [daobataotie/mssql-mcp](https://github.com/daobataotie/mssql-mcp) | 39 | Python | MIT | Basic MSSQL access |
| [aadversteeg/mssqlclient-mcp-server](https://github.com/aadversteeg/mssqlclient-mcp-server) | 32 | C# | MIT | Server Mode (multi-database), stored procedures, query profiling |
| [lorenzouriel/mssql-mcp-python](https://github.com/lorenzouriel/mssql-mcp-python) | 25 | Python | MIT | Controlled/secure access |
| [RodrigoPAml/MCP-SqlServer](https://github.com/RodrigoPAml/MCP-SqlServer) | 17 | C# | MIT | Tested with Claude Desktop |
| [c0h1b4/mssql-mcp-server](https://github.com/c0h1b4/mssql-mcp-server) | 15 | TypeScript | MIT | Blocks DROP/TRUNCATE/ALTER/CREATE |
| [bilims/mcp-sqlserver](https://github.com/bilims/mcp-sqlserver) | 10 | TypeScript | MIT | Read-only enforced, SQL injection protection, automatic TOP clause |

### Multi-Database Servers Supporting SQL Server

| Server | Stars | SQL Server Support | Other Databases |
|--------|-------|--------------------|-----------------|
| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | 15k | Yes (Cloud SQL for SQL Server) | PostgreSQL, MySQL, Spanner, Bigtable, AlloyDB |
| [bytebase/dbhub](https://github.com/bytebase/dbhub) | 2.7k | Yes | PostgreSQL, MySQL, MariaDB, SQLite |
| [Anarkh-Lee/universal-db-mcp](https://github.com/Anarkh-Lee/universal-db-mcp) | 674 | Yes | 17 databases total including MongoDB, Oracle |
| [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) | 397 | Yes (MS-SQL via SQLAlchemy) | PostgreSQL, MySQL, MariaDB, Oracle, SQLite + more |
| [executeautomation/mcp-database-server](https://github.com/executeautomation/mcp-database-server) | 326 | Yes | PostgreSQL, MySQL, SQLite |
| [wenb1n-dev/SmartDB_MCP](https://github.com/wenb1n-dev/SmartDB_MCP) | 113 | Yes | MySQL, PostgreSQL, MariaDB, DM8, Oracle |
| [skanga/DBchat](https://github.com/skanga/DBchat) | 91 | Yes (JDBC) | PostgreSQL, MySQL, Oracle, SQLite, MongoDB |
| [faucetdb/faucet](https://github.com/faucetdb/faucet) | 85 | Yes | Any SQL database |

**Google's Cloud SQL Remote MCP Server** also supports SQL Server in preview (auto-enabled after March 17, 2026).

**Notable absence:** AWS's awslabs/mcp monorepo (8.5k stars, 68 servers) has dedicated PostgreSQL and MySQL MCP servers but **no SQL Server MCP server**.

## Database MCP Comparison

| Feature | SQL Server (this review) | PostgreSQL (4.5/5) | MySQL (3.5/5) |
|---------|-------------------------|-------------------|---------------|
| Dedicated MCP servers | ~15+ | ~10+ | ~6 |
| Top server stars | 341 (RichardHan) | 2.4k (Postgres MCP Pro) | 1.4k (benborla) |
| Official vendor server | Yes (Microsoft, **Data API Builder — GA**) | None (community-governed) | None (Oracle silent) |
| Performance analysis MCP tools | **63 tools** (PerformanceMonitor) + 13 (PerformanceStudio) | 8 tools (Postgres MCP Pro) | None |
| Enterprise governance | ConnorBritain (Preview+Confirm, audit logging) | None at that level | None |
| Multi-DB support | DBHub (2.7k), Google (15k), mcp-alchemy (397) | DBHub (2.7k), Google (15k) | DBHub (2.7k), Google (15k) |
| Cloud vendor MCP servers | Azure (official, GA), Google | AWS, Azure, Google | AWS, Azure, Google |
| AWS MCP support | **None** | Yes (aurora-postgres) | Yes (aurora-mysql) |
| .NET/C# options | 6+ C# servers | 0 | 0 |
| Top community server maintenance | Stalled (Nov 2025) | Active | Active |
| Official server maintenance | Active (DAB v1.7+) | N/A | N/A |
| AAIF membership | No (Microsoft not a member) | Anthropic is founding member | No |
| Rating | **4/5** | **4.5/5** | **3.5/5** |

## Known Issues

1. **Official server is schema-centric, not SQL-flexible** — The Data API Builder SQL MCP Server is production-grade but does not expose raw SQL. It works through defined entity operations — appropriate for many enterprise use cases but not a drop-in replacement for community servers if you need arbitrary query execution. Teams wanting full SQL flexibility still need community servers like RichardHan or ConnorBritain.

2. **Most-starred general server appears stalled** — RichardHan/mssql_mcp_server (323 stars) last pushed in November 2025 with only 26 total commits and 12 open issues. The most popular server may not be actively maintained. Compare to PostgreSQL's Postgres MCP Pro (active) or MySQL's benborla (222 commits, actively maintained).

3. **Ecosystem fragmented across four languages** — SQL Server MCP servers span Python, C#, TypeScript, and JavaScript. While language diversity reflects SQL Server's cross-platform reach, it fragments community effort. C# servers make sense for .NET shops but can't be installed via pip or npm — the standard distribution channels for MCP servers.

4. **AWS has no SQL Server MCP server** — AWS's awslabs/mcp monorepo (8.5k stars, 68 servers) includes dedicated servers for PostgreSQL (aurora-postgres) and MySQL (aurora-mysql) but nothing for SQL Server — despite AWS offering RDS for SQL Server. This creates a cloud coverage gap.

5. **PerformanceMonitor is very new** — Created February 2026, PerformanceMonitor's 63 MCP tools are impressive but the project is only weeks old. Long-term maintenance and community adoption are unproven. It also requires SQL Server 2016+ — no support for older versions.

6. **GPL licensing on dperussina** — dperussina/mssql-mcp-server uses GPL-3.0, which may conflict with enterprise deployment policies or proprietary integration requirements. Most other SQL Server MCP servers use MIT or Apache-2.0.

7. **Windows Authentication complexity in containers** — Several servers support Windows Auth, but Docker deployments require `host.docker.internal` networking workarounds on Windows/macOS. Azure AD authentication has documented timeout issues even in Microsoft's own official server.

8. **No single dominant install path** — Unlike PostgreSQL (`pipx install postgres-mcp`) or MySQL (`npm install @benborla/mcp-server-mysql`), there's no obvious "just install this one" answer for SQL Server MCP. The choice depends on language preference, performance needs, and deployment model.

9. **Write-access governance is rare** — Only ConnorBritain/mssql-mcp-server (10 stars) provides Preview+Confirm for mutations and audit logging. Most servers either lack write support entirely or provide it without governance controls. For enterprise databases, this matters.

10. **No Anthropic reference server** — Anthropic's archived reference MCP servers included PostgreSQL and SQLite but never covered SQL Server. This means no blessed starting point for the community — everyone built from scratch, contributing to fragmentation.

## Bottom Line

**Rating: 4 out of 5**

SQL Server's MCP ecosystem has meaningfully matured since the March 2026 review. The missing piece — a production-ready, officially maintained Microsoft SQL MCP Server — is now filled by Data API Builder, documented as a first-class feature in SQL Server 2025. Combined with SQL Server 2025's native vector support and AI-ready T-SQL, Microsoft is no longer lagging behind the MCP curve.

The **split story** from March is still true, but the balance has shifted. PerformanceMonitor's 63 read-only MCP tools (shipping weekly, 356 stars) remain the best AI-assisted performance analysis available for any database — no other ecosystem comes close. The Data API Builder SQL MCP Server handles schema-based entity operations with RBAC, tracing, and production-grade reliability. The ecosystem gaps are real but narrowing: the top dedicated community server (RichardHan, 341 stars) remains stalled, AWS still has no SQL Server MCP entry, and four-language fragmentation persists.

The **4/5 rating** reflects: a production-grade official server, SQL Server 2025 AI-native features, unmatched performance monitoring depth, strong multi-database coverage (DBHub 2.7k, Google Toolbox 15k), and the only enterprise-grade governance server (ConnorBritain). It still loses for: stalled top community server, no AWS coverage, schema-only official server (no raw SQL), and lower community adoption than PostgreSQL.

**Who benefits most from SQL Server's MCP ecosystem:**

- **DBAs and performance engineers** — PerformanceMonitor (63 MCP tools, weekly releases) and PerformanceStudio (13 tools) provide AI-assisted performance analysis that no other database ecosystem can match
- **Teams deploying SQL Server 2025** — native vector support, `AI_GENERATE_EMBEDDINGS`, and first-class DAB SQL MCP Server mean AI-native workflows are built in, not bolted on
- **.NET/Windows shops** — 6+ C# servers mean native integration with existing .NET infrastructure and tooling
- **Multi-database teams** — DBHub and Google Toolbox provide SQL Server alongside PostgreSQL, MySQL, and others from a single MCP server
- **Enterprise teams with governance requirements** — ConnorBritain's server with Preview+Confirm, audit logging, and multi-environment support; DAB SQL MCP Server for RBAC-enforced entity access

**Who should be cautious:**

- **Teams needing raw SQL execution via official tooling** — the Data API Builder SQL MCP Server doesn't do NL2SQL; use community servers (RichardHan, ConnorBritain) for arbitrary SQL
- **AWS-centric teams** — no dedicated AWS SQL Server MCP server exists, unlike PostgreSQL and MySQL which both have aurora-* servers in AWS's monorepo
- **Teams on older SQL Server versions** — SQL Server 2025's AI features require the latest release; PerformanceMonitor requires SQL Server 2016+

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Updated May 2026. See our [About page](/about/) for details on our review process.*
