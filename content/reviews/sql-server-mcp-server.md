---
title: "SQL Server MCP Servers — Enterprise Database Gets AI-Powered Performance Monitoring"
date: 2026-03-23T23:30:00+09:00
description: "SQL Server's MCP ecosystem features 15+ dedicated servers, Microsoft's experimental official server, uniquely powerful performance monitoring from PerformanceMonitor (272 stars, 63 MCP tools), and strong multi-database support from DBHub (2.4k stars) and Google Toolbox (13.5k stars). Rating: 3.5/5."
og_description: "SQL Server MCP ecosystem: PerformanceMonitor (272 stars, 63 tools), RichardHan's mssql_mcp_server (323 stars), Microsoft's experimental official server, DBHub (2.4k stars), Google Toolbox (13.5k stars). The best AI-assisted database performance monitoring. Rating: 3.5/5."
content_type: "Review"
card_description: "SQL Server has 15+ dedicated MCP servers plus Microsoft's experimental official server. The standout is PerformanceMonitor (272 stars) with 63 read-only MCP tools for query analysis, wait statistics, and execution plans — unmatched by any database. Multi-database servers DBHub (2.4k stars) and Google Toolbox (13.5k stars) add breadth. AWS notably absent."
last_refreshed: 2026-03-23
---

**At a glance:** SQL Server has an **unexpectedly deep MCP ecosystem** with 15+ dedicated servers and a uniquely powerful performance monitoring story. The standout is [PerformanceMonitor](https://github.com/erikdarlingdata/PerformanceMonitor) (272 stars, C#, MIT) from SQL Server consultant Erik Darling — offering **63 read-only MCP tools** for query performance, execution plans, wait statistics, blocking, deadlocks, and more. That's the most performance-focused MCP tooling of any database. The most-starred general-purpose server is [RichardHan/mssql_mcp_server](https://github.com/RichardHan/mssql_mcp_server) (323 stars, Python, MIT). Microsoft provides an [experimental official server](https://github.com/Azure-Samples/SQL-AI-samples/tree/main/MssqlMcp) in .NET and Node.js — but it's explicitly "NOT intended for production use." Multi-database servers [Bytebase DBHub](https://github.com/bytebase/dbhub) (2.4k stars) and [Google's MCP Toolbox](https://github.com/googleapis/genai-toolbox) (13.5k stars) also support SQL Server.

SQL Server is **Microsoft's flagship relational database** — commanding roughly **30% of the relational database market**, second only to MySQL. Born from a partnership with Sybase in 1987, Microsoft forked the product in 1994 and released SQL Server 6.0 (1995) as the first fully Microsoft-developed version. The current GA release is **SQL Server 2022** (November 2022, CU18+), with **SQL Server 2025** in preview. SQL Server's enterprise features — T-SQL, Always On availability groups, In-Memory OLTP, ColumnStore indexes, ML Services, and graph database capabilities — make it the default database for Windows/.NET enterprise shops. Notable users include Stack Overflow, Bank of America, Dell, and GEICO. Microsoft's cloud offerings include Azure SQL Database (PaaS) and Azure SQL Managed Instance.

**Architecture note:** SQL Server's MCP ecosystem has a distinctive shape. Unlike PostgreSQL's community-led approach or MySQL's community-only approach, SQL Server benefits from Microsoft's involvement — but that involvement is still experimental. The real differentiation comes from **performance monitoring tools** (PerformanceMonitor + PerformanceStudio) that have no equivalent in any other database's MCP ecosystem. The trade-off is ecosystem fragmentation across four languages (Python, C#, TypeScript, JavaScript) and the most-starred general-purpose server showing signs of maintenance stall.

## What's Available

### PerformanceMonitor — erikdarlingdata/PerformanceMonitor

The **most impressive SQL Server MCP server** — and arguably the most powerful database performance MCP tool in any ecosystem:

| Aspect | Detail |
|--------|--------|
| GitHub | [erikdarlingdata/PerformanceMonitor](https://github.com/erikdarlingdata/PerformanceMonitor) — 272 stars, 32 forks, 100+ commits, MIT |
| Language | C# |
| Created by | [Erik Darling](https://www.erikdarlingdata.com/) (well-known SQL Server consultant) |
| Supports | SQL Server 2016–2025, Azure SQL MI, AWS RDS, Azure SQL Database |

**Two editions:**

| Edition | Collectors | MCP Tools | Storage | Install |
|---------|-----------|-----------|---------|---------|
| Full | 32 T-SQL collectors | **63 read-only tools** | PerformanceMonitor database, SQL Agent jobs | Requires SQL Server instance |
| Lite | 23 collectors | **51 read-only tools** | DuckDB + Parquet files | Standalone desktop app |

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
| GitHub | [erikdarlingdata/PerformanceStudio](https://github.com/erikdarlingdata/PerformanceStudio) — 120 stars, 20 forks, 100+ commits, MIT |
| Language | C# |
| MCP Tools | 13 tools (disabled by default, localhost only) |
| Install | Cross-platform GUI + CLI + SSMS extension (SSMS 18–22) |
| Transport | HTTP MCP |

**MCP tools include:** `analyze_plan`, `get_missing_indexes`, `compare_plans`, `get_query_store_top`. The 30+ analysis rules cover memory grants, row estimate mismatches, missing indexes, spills, and parallel skew. This is purpose-built for DBAs who want AI assistance with execution plan analysis.

### mssql_mcp_server — RichardHan/mssql_mcp_server

The **most-starred general-purpose SQL Server MCP server:**

| Aspect | Detail |
|--------|--------|
| GitHub | [RichardHan/mssql_mcp_server](https://github.com/RichardHan/mssql_mcp_server) — 323 stars, 90 forks, 26 commits, MIT |
| Language | Python |
| Install | `pip install microsoft_sql_server_mcp` or `uvx microsoft_sql_server_mcp` |
| Supports | SQL Server, SQL Server LocalDB, Azure SQL Database |

**Tools:** List tables, read data, execute SQL queries. Supports both SQL authentication (user/password) and Windows Authentication. Configuration via environment variables (MSSQL_SERVER, MSSQL_DATABASE, MSSQL_PORT).

**Concern:** Last push was November 2025 with only 26 commits and 12 open issues. Despite being the most-starred, development appears to have stalled. For a tool managing database access, maintenance matters.

### mssql-mcp — Aaronontheweb/mssql-mcp

A **.NET-native SQL Server MCP server** for the C# ecosystem:

| Aspect | Detail |
|--------|--------|
| GitHub | [Aaronontheweb/mssql-mcp](https://github.com/Aaronontheweb/mssql-mcp) — 143 stars, 20 forks, 21 commits, Apache-2.0 |
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

### Microsoft's Official Server (Experimental)

| Aspect | Detail |
|--------|--------|
| Code | [Azure-Samples/SQL-AI-samples/MssqlMcp](https://github.com/Azure-Samples/SQL-AI-samples/tree/main/MssqlMcp) — part of a 306-star repo |
| Implementations | .NET 8 and Node.js |
| Status | **Experimental — "NOT intended for production use"** |
| Catalog | Listed in [microsoft/mcp](https://github.com/microsoft/mcp) (2,840 stars) as a separate entry |

**.NET tools (7):** ListTables, DescribeTable, CreateTable, DropTable, InsertData, ReadData, UpdateData. Node.js adds mandatory WHERE clauses and read-only mode. Supports SQL auth, Windows/NTLM, Azure AD. Known timeout issues with "Active Directory Default" authentication.

**What this means:** Microsoft acknowledges MCP matters for SQL Server but hasn't committed engineering resources to a production-grade official server. The community servers are more capable.

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
| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | 13.5k | Yes (Cloud SQL for SQL Server) | PostgreSQL, MySQL, Spanner, Bigtable, AlloyDB |
| [bytebase/dbhub](https://github.com/bytebase/dbhub) | 2.4k | Yes | PostgreSQL, MySQL, MariaDB, SQLite |
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
| Top server stars | 323 (RichardHan) | 2.4k (Postgres MCP Pro) | 1.4k (benborla) |
| Official vendor server | Yes (Microsoft, experimental) | None (community-governed) | None (Oracle silent) |
| Performance analysis MCP tools | **63 tools** (PerformanceMonitor) + 13 (PerformanceStudio) | 8 tools (Postgres MCP Pro) | None |
| Enterprise governance | ConnorBritain (Preview+Confirm, audit logging) | None at that level | None |
| Multi-DB support | DBHub (2.4k), Google (13.5k), mcp-alchemy (397) | DBHub (2.4k), Google (13.5k) | DBHub (2.4k), Google (13.5k) |
| Cloud vendor MCP servers | Azure (official), Google (preview) | AWS, Azure, Google | AWS, Azure, Google |
| AWS MCP support | **None** | Yes (aurora-postgres) | Yes (aurora-mysql) |
| .NET/C# options | 6+ C# servers | 0 | 0 |
| Top server maintenance | Stalled (Nov 2025) | Active | Active (222 commits) |
| AAIF membership | No (Microsoft not a member) | Anthropic is founding member | No |
| Rating | **3.5/5** | **4.5/5** | **3.5/5** |

## Known Issues

1. **Microsoft's official server is experimental** — The Azure-Samples/SQL-AI-samples/MssqlMcp implementation explicitly states "NOT intended for production use." Unlike MongoDB's polished 40+ tool official server (970 stars, 891k monthly npm downloads), Microsoft's offering is a demo. For the world's #2 relational database, this is a conspicuous gap.

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

**Rating: 3.5 out of 5**

SQL Server's MCP ecosystem tells a **split story**. On one hand, it has the **best AI-assisted performance monitoring of any database** — PerformanceMonitor's 63 read-only MCP tools for query analysis, wait statistics, execution plans, blocking, and deadlocks are genuinely unmatched. PerformanceStudio adds another 13 tools for execution plan analysis. No other database comes close to this depth of performance tooling through MCP.

On the other hand, the **general-purpose server ecosystem lags behind**. The most-starred dedicated server (323 stars) has a fraction of the community adoption seen in PostgreSQL (2.4k) or MySQL (1.4k). Microsoft's official server being explicitly "experimental" and "NOT intended for production use" sends a weak signal. The ecosystem is fragmented across four programming languages. AWS — the largest cloud provider — has no dedicated SQL Server MCP server.

The **3.5/5 rating** reflects this duality. Strong multi-database support from DBHub (2.4k stars) and Google Toolbox (13.5k stars), 15+ dedicated servers (more than MySQL by count), Microsoft's catalog presence, uniquely powerful performance monitoring, and the only enterprise-grade governance server (ConnorBritain) earn SQL Server a respectable score. It loses for: experimental official server, stalled top general-purpose server, four-language fragmentation, no AWS coverage, and lower overall community adoption compared to PostgreSQL.

**Who benefits most from SQL Server's MCP ecosystem:**

- **DBAs and performance engineers** — PerformanceMonitor (63 MCP tools) and PerformanceStudio (13 tools) provide AI-assisted performance analysis that no other database ecosystem can match
- **.NET/Windows shops** — 6+ C# servers mean native integration with existing .NET infrastructure and tooling
- **Multi-database teams** — DBHub and Google Toolbox provide SQL Server alongside PostgreSQL, MySQL, and others from a single MCP server
- **Enterprise teams with governance requirements** — ConnorBritain's server with Preview+Confirm, audit logging, and multi-environment support addresses compliance needs

**Who should be cautious:**

- **Teams needing a polished official server** — Microsoft's experimental offering isn't production-ready; community servers are more capable but vary in maintenance status
- **AWS-centric teams** — no dedicated AWS SQL Server MCP server exists, unlike PostgreSQL and MySQL which both have aurora-* servers in AWS's monorepo
- **Teams wanting a simple "just install this" experience** — the ecosystem fragmentation means evaluating multiple options across languages and capabilities

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*
