---
title: "MySQL MCP Servers — The World's Most Popular Database Meets AI"
date: 2026-03-23T23:00:00+09:00
description: "MySQL's MCP ecosystem features benborla/mcp-server-mysql (1.6k stars, TypeScript) and designcomputer/mysql_mcp_server (1.2k stars, Python) as community leaders, plus"
og_description: "MySQL MCP ecosystem: mcp-server-mysql (1.6k stars), mysql_mcp_server (1.2k stars), DBHub (2.7k stars), Google MCP Toolbox (14.9k stars), plus cloud vendor servers. Oracle released PoC MCP for MySQL HeatWave. Rating: 3.5/5."
content_type: "Review"
card_description: "MySQL has a solid community MCP ecosystem. benborla/mcp-server-mysql (1.6k stars) leads with SSH tunneling and Claude Code integration. designcomputer/mysql_mcp_server (1.2k stars) offers simplicity. Multi-database servers DBHub (2.7k stars) and Google MCP Toolbox (14.9k stars) add breadth. Oracle released a PoC MCP for MySQL HeatWave. MySQL 8.0 hit EOL April 21, 2026."
last_refreshed: 2026-05-03
---

**At a glance:** MySQL now has **both community and a nascent official presence** in the MCP ecosystem. The two leading MySQL-specific servers are [benborla/mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) (1.6k stars, TypeScript, MIT) with SSH tunnel support and Claude Code integration, and [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) (1.2k stars, Python, MIT) focused on simplicity and security. Multi-database servers [Bytebase DBHub](https://github.com/bytebase/dbhub) (2.7k stars) and [Google's MCP Toolbox](https://github.com/googleapis/mcp-toolbox) (14.9k stars) also support MySQL alongside other databases. Oracle released a **proof-of-concept MCP server for MySQL HeatWave** (cloud-only, not production-ready), ending the era of zero official Oracle MCP presence. Cloud vendors AWS, Azure, and Google all provide MySQL MCP support through their platform servers. Part of our **[Databases MCP category](/categories/databases/)**.

MySQL is the **world's most popular open-source relational database** — powering roughly **39% of the relational database market** with over 235,000 companies using it worldwide. Created in 1995 by Michael "Monty" Widenius, David Axmark, and Allan Larsson as MySQL AB, it was acquired by Sun Microsystems for $1 billion in 2008, then passed to Oracle when Oracle acquired Sun for $5.6 billion in 2010. The latest Innovation release is **MySQL 9.6** (January 2026); the current Long-Term Support release is **MySQL 8.4.5**. **MySQL 8.0 reached end-of-life on April 21, 2026** — that milestone has now passed, putting the ecosystem firmly in the 8.4 LTS + 9.x era.

**Architecture note:** MySQL's "no official server" story has changed slightly. Oracle has released a **proof-of-concept MCP server** via [oracle.com/mcp/](https://www.oracle.com/mcp/) for MySQL HeatWave and MySQL AI — covering connection management, query execution, vector store management, and OCI Object Store integration. However, it is cloud-only (HeatWave), PoC-grade (not production-ready), and separate from community MySQL. The dominant open-source alternative MariaDB (forked from MySQL in 2009 by Widenius himself) has its own [official MCP server](https://github.com/MariaDB/mcp) (166 stars), making it the best-served MySQL-compatible database for official MCP support.

## What's Available

### mcp-server-mysql — benborla/mcp-server-mysql

The **most popular MySQL-specific MCP server**, optimized for Claude Code integration:

| Aspect | Detail |
|--------|--------|
| GitHub | [benborla/mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) — 1.6k stars, MIT |
| Language | TypeScript/JavaScript |
| Install | npm / Smithery |
| Transport | stdio |

**Key features:**

| Feature | Detail |
|---------|--------|
| SSH tunnel support | Built-in automatic tunneling for remote databases |
| Claude Code hooks | Auto-start/stop tunnels with Claude sessions |
| Multi-database mode | Single instance accesses multiple databases |
| DDL operations | Optional CREATE TABLE support via config flag |
| Security | SQL injection prevention via prepared statements, query whitelisting/blacklisting |
| Performance | Connection pooling, query result caching, configurable timeouts and rate limiting |

**Tools:** `mysql_query` for executing SQL queries (read-only by default, optional write via `MYSQL_DISABLE_READ_ONLY_TRANSACTIONS`). Resources expose JSON schemas with column types, indexes, foreign keys, and table statistics.

**Key differentiator:** The SSH tunnel integration and Claude Code hooks make this the best option for developers who work with remote MySQL databases through Claude. Connection pooling and caching add production-grade reliability. Recent additions include enhanced SSH tunnel scripts for RDS/private VPC access and `destructiveHint` annotations for LLM safety flagging.

### mysql_mcp_server — designcomputer/mysql_mcp_server

A **simpler, security-focused** MySQL MCP server:

| Aspect | Detail |
|--------|--------|
| GitHub | [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) — 1.2k stars, 232 forks, MIT |
| Language | Python |
| Install | `pip install mysql-mcp-server` / Smithery / Docker |
| Transport | stdio |

**Core capabilities:**
- Table resource enumeration
- Table content reading
- SQL query execution with error handling
- Environment variable credential management
- Comprehensive logging

**Key differentiator:** Simplicity and security emphasis. The smallest footprint of the major MySQL MCP servers — install via pip, configure with environment variables, go. Security-audited by MseeP.ai. Best for developers who want minimal setup without SSH tunnels or advanced features. 6 releases, last at v0.2.2.

### Bytebase DBHub — bytebase/dbhub

A **multi-database MCP server** with strong MySQL support:

| Aspect | Detail |
|--------|--------|
| GitHub | [bytebase/dbhub](https://github.com/bytebase/dbhub) — 2.7k stars, 513+ commits, MIT |
| Language | TypeScript |
| Install | npm / Docker |
| Transport | stdio |
| Databases | PostgreSQL, **MySQL**, MariaDB, SQL Server, SQLite |

**3 MCP tools:**

| Tool | What it does |
|------|-------------|
| `execute_sql` | Run queries with transaction and safety controls |
| `search_objects` | Explore schemas, tables, columns, indexes, procedures |
| Custom tools | User-defined parameterized SQL operations via TOML config |

**Key differentiator:** Zero-dependency, token-efficient design that maximizes context window usage. Multi-database and multi-connection support via TOML configuration. Built-in safety guardrails: read-only mode, row limiting, query timeouts. SSH tunneling and SSL/TLS encryption. Includes a web workbench interface. Best for teams working across multiple database types.

### Google MCP Toolbox for Databases — googleapis/mcp-toolbox

The **highest-starred database MCP server** with MySQL support (rebranded from `genai-toolbox` to `mcp-toolbox`):

| Aspect | Detail |
|--------|--------|
| GitHub | [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) — 14.9k stars |
| Language | Go |
| Install | Binary or Docker |
| Transport | MCP + native SDKs (Python, JS, Go) |

Supports Cloud SQL for MySQL, PostgreSQL, SQL Server, AlloyDB, Spanner, and Bigtable. Configuration-driven via YAML. Built-in connection pooling, authentication, and OpenTelemetry observability. Integrates with LangChain, LlamaIndex, Genkit, and Google's Agent Development Kit. Recent additions include a `list-table-stats-tool` for MySQL table statistics. The most production-hardened option for Google Cloud MySQL users.

### Cloud SQL Remote MCP Server (Google)

Google also provides a **managed Cloud SQL MCP server** specifically for MySQL:

| Aspect | Detail |
|--------|--------|
| Documentation | [Cloud SQL MySQL MCP docs](https://docs.google.com/sql/docs/mysql/use-cloudsql-mcp) |
| Status | Preview (auto-enabled after March 17, 2026 with Cloud SQL Admin API) |
| Features | Natural language interactions, AI-assisted app development, query optimization, database troubleshooting |

A fully managed remote MCP server — no code to install or maintain. Available for MySQL, PostgreSQL, and SQL Server fleets.

### AWS MySQL MCP Server

Part of the [awslabs/mcp](https://github.com/awslabs/mcp) monorepo (8,540 stars total, 68 servers):

| Aspect | Detail |
|--------|--------|
| Location | `awslabs/mcp` monorepo → Aurora MySQL MCP server |
| Language | Python |
| License | Apache 2.0 |
| Transport | stdio |

Supports connecting to Aurora MySQL and RDS MySQL endpoints. Part of the largest official MCP server collection from any company. Inherits the monorepo's testing and release infrastructure.

### Azure MCP Server — MySQL Support

Microsoft's [Azure MCP Server](https://github.com/microsoft/mcp) (migrated from Azure/azure-mcp, 1.2k stars) includes MySQL support:

| Aspect | Detail |
|--------|--------|
| GitHub | [microsoft/mcp](https://github.com/microsoft/mcp) → Azure.Mcp.Server |
| Features | List databases, list tables, retrieve schemas, execute read queries, insert/update, create/drop tables |
| Auth | MySQL password or Microsoft Entra authentication |
| Status | Active (migrated Feb 2026) |

SELECT-only query capabilities in the management suite. Targets Azure Database for MySQL Flexible Server.

### Additional Servers

| Server | Stars | Language | License | Focus |
|--------|-------|----------|---------|-------|
| [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) | 401 | Python | MPL 2.0 | SQLAlchemy-based, supports MySQL + 7 other databases, schema exploration |
| [MariaDB/mcp](https://github.com/MariaDB/mcp) | 166 | Python | — | Official MariaDB MCP (MySQL-compatible), vector search, SSE/HTTP transport |
| [askdba/mysql-mcp-server](https://github.com/askdba/mysql-mcp-server) | 26 | Go | Apache 2.0 | Read-only, multi-DSN, v1.7.0 (April 20), HTTP status dashboard, audit logs, MySQL 8.0/8.4/9.0+ + MariaDB |
| [alexcc4/mcp-mysql-server](https://github.com/alexcc4/mcp-mysql-server) | 6 | Python | MIT | Lightweight, minimal config, single `query_data` tool |
| [neverinfamous/mysql-mcp](https://github.com/neverinfamous/mysql-mcp) | 3 | TypeScript | MIT | 192 tools across 25 groups, Code Mode (90% token savings), OAuth 2.1 |

### Oracle MCP for MySQL HeatWave (PoC)

Oracle has released a **proof-of-concept MCP server** for MySQL HeatWave:

| Aspect | Detail |
|--------|--------|
| Documentation | [oracle.com/mcp/](https://www.oracle.com/mcp/) |
| Status | Proof-of-concept (not production-ready) |
| Scope | MySQL HeatWave (Oracle Cloud) and MySQL AI only |
| Features | Connection management, query execution, vector store management, OCI Object Store integration |

This is Oracle's first MCP presence for MySQL. It's significant as a signal of direction, but limited: it targets only Oracle's cloud HeatWave service, not community MySQL or self-hosted deployments. A separate **Oracle SQLcl MCP Server** was also made available in SQL Developer Command Line 25.2 for Oracle Database users. Community MySQL users still have no production-grade Oracle-official MCP server.

### Anthropic's Archived Reference Server

Anthropic included a MySQL-compatible PostgreSQL server pattern in the original [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) repository, but there was **no dedicated MySQL reference server**. The archived reference implementations focused on PostgreSQL and SQLite. MySQL's MCP ecosystem grew entirely from community effort.

## MySQL Background

| Aspect | Detail |
|--------|--------|
| Origin | MySQL AB, Sweden (1995), by Michael Widenius, David Axmark, Allan Larsson |
| Ownership | Oracle Corporation (via Sun Microsystems acquisition, 2010) |
| Latest Innovation release | MySQL 9.6.0 (January 2026); MySQL 9.7 LTS expected mid-2026 |
| Latest LTS release | MySQL 8.4.5 |
| End-of-life: MySQL 8.0 | April 21, 2026 (now past — Oracle Sustaining Support only) |
| License | GPL v2 (Community Edition) / Commercial (Enterprise Edition) |
| Market share | 39.3% of relational databases ([6sense](https://6sense.com/tech/relational-databases/mysql-market-share)) |
| Companies using MySQL | 235,000+ worldwide |
| Top users | Facebook, YouTube, Twitter/X, WordPress, Uber, Netflix, Airbnb, Shopify |
| Cloud Database MySQL market | ~$15 billion (2025), ~15% CAGR through 2033 |
| Fork | MariaDB (forked 2009 by Widenius after Oracle acquisition) |

MySQL's dual licensing (open-source GPL + commercial Enterprise Edition) and Oracle's stewardship have driven some users toward PostgreSQL or MariaDB, but MySQL remains the default database for web applications — particularly in the LAMP stack (Linux, Apache, MySQL, PHP/Python) that powers a massive share of the internet.

## Database MCP Ecosystem Comparison

| Feature | MySQL (this review) | PostgreSQL |
|---------|-------------------|------------|
| Dedicated MCP servers | ~6 | ~10+ |
| Top server stars | 1.6k (benborla) | 2.4k+ (Postgres MCP Pro) |
| Multi-DB servers with support | DBHub (2.7k), Google MCP Toolbox (14.9k), MCP Alchemy (401) | DBHub (2.7k), Google MCP Toolbox (14.9k) |
| Official vendor MCP server | PoC only (Oracle HeatWave) | None (community-governed) |
| MariaDB/fork server | MariaDB/mcp (166 stars, official) | N/A |
| Cloud vendor support | AWS, Azure, Google | AWS, Azure, Google |
| Performance analysis tools | Limited | Postgres MCP Pro (index tuning, health) |
| Vector search support | askdba (MySQL 9.0+), MariaDB MCP | Limited (pgvector not well-supported) |
| Read-only default | Yes (most servers) | Varies |
| Rating | **3.5/5** | **4.5/5** |

## Known Issues

1. **Oracle's MCP presence is HeatWave-only PoC** — Oracle has released a proof-of-concept MCP server, but it targets only MySQL HeatWave (Oracle's cloud MySQL service) and is not production-ready. MySQL Community Edition and self-hosted MySQL deployments still have no production Oracle-official MCP server. The ecosystem remains primarily community-driven for general use cases.

2. **Smaller ecosystem than PostgreSQL** — MySQL has roughly half the number of dedicated MCP servers compared to PostgreSQL. While the top servers are solid, there's less choice for specialized use cases (monitoring, performance tuning, extension management).

3. **No performance analysis tools** — Unlike PostgreSQL's Postgres MCP Pro with its index tuning and workload analysis, no MySQL MCP server provides deep performance optimization capabilities. MySQL administrators get schema browsing and query execution, not DBA-grade performance tooling.

4. **MySQL 8.0 end-of-life passed** — MySQL 8.0 reached EOL on April 21, 2026, entering Oracle Sustaining Support only. Many MCP servers haven't documented compatibility with MySQL 9.x Innovation releases or the 8.4 LTS track. Organizations running 8.0 should upgrade to 8.4 LTS (supported through April 2032) or 9.x Innovation releases. MySQL 9.7 LTS is expected mid-2026.

5. **Oracle's dual licensing creates confusion** — MySQL's GPL v2 license means MCP servers using MySQL client libraries must navigate GPL compatibility. Some servers choose MIT/Apache licenses for their own code while depending on GPL MySQL connectors — the legal implications aren't always clear.

6. **MariaDB compatibility is inconsistent** — Some MySQL MCP servers work with MariaDB (askdba explicitly supports it), but most don't document MariaDB compatibility. Given that many organizations have migrated from MySQL to MariaDB, this is a gap.

7. **Write-access security risks** — benborla/mcp-server-mysql allows enabling write operations via config flag. Without careful permission management, an AI agent could execute destructive DDL or DML against production databases. Read-only should remain the default.

8. **SSH tunnel complexity** — While benborla's SSH tunnel support is a feature, it adds configuration complexity and potential failure modes. Remote database access through MCP introduces security considerations that local-only servers avoid.

9. **neverinfamous/mysql-mcp claims 192 tools but has 3 stars** — The most feature-rich MySQL MCP server (192 tools, 25 groups, 2,169 tests) has almost no community adoption. Feature count alone doesn't indicate reliability or real-world usage.

10. **Cloud vendor servers create lock-in** — AWS, Azure, and Google each provide MySQL MCP support, but only for their managed MySQL services. Migrating between clouds means switching MCP servers and reconfiguring AI integrations.

## Bottom Line

**Rating: 3.5 out of 5**

MySQL has a **respectable MCP ecosystem** that covers the basics well — schema exploration, SQL execution, and multi-database support — but lacks the depth and specialization found in PostgreSQL's MCP landscape.

**benborla/mcp-server-mysql** (1.6k stars, +14% since March) is the clear leader for MySQL-specific needs, with SSH tunneling, Claude Code integration, connection pooling, and recent LLM safety annotations. **designcomputer/mysql_mcp_server** (1.2k stars, stable) offers a simpler alternative for developers who want minimal configuration. **Bytebase DBHub** (2.7k stars, +12%) is the best multi-database option, providing token-efficient MySQL support alongside PostgreSQL, MariaDB, SQL Server, and SQLite.

The **3.5/5 rating holds**. Oracle's HeatWave PoC is a positive signal but doesn't change the practical situation for most MySQL users. Two 1k+ star dedicated servers, strong multi-database support from DBHub and Google MCP Toolbox (rebranded, 14.9k stars), and full cloud vendor coverage (AWS, Azure, Google) earn MySQL a good score. It loses a full point compared to PostgreSQL for: no production Oracle-official server for community MySQL, no performance analysis/tuning tools (PostgreSQL has Postgres MCP Pro), roughly half the number of dedicated servers, and no deep MySQL-specific capabilities like slow query log analysis, InnoDB buffer pool monitoring, or replication status checks.

**Who benefits most from MySQL's MCP ecosystem:**

- **Web application developers** — MySQL powers most LAMP/LEMP stacks; benborla's server lets AI assistants explore schemas and write queries in context
- **Multi-database teams** — DBHub and Google Toolbox provide MySQL support alongside other databases from a single MCP server
- **Cloud users** — AWS, Azure, and Google all provide managed MySQL MCP servers integrated with their platforms
- **Claude Code users** — benborla/mcp-server-mysql's SSH tunnel hooks and auto-management are specifically designed for Claude Code workflows

**Who should be cautious:**

- **DBAs seeking performance tools** — if you need AI-assisted query optimization, index tuning, or health monitoring, PostgreSQL's Postgres MCP Pro is significantly ahead
- **MySQL Enterprise Edition users** — no MCP server integrates with Oracle's Enterprise features (Enterprise Monitor, Query Analyzer, Firewall)
- **MariaDB users** — while some MySQL MCP servers work with MariaDB, consider the [official MariaDB MCP server](https://github.com/MariaDB/mcp) (151 stars) with its vector search and SSE/HTTP transport support

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Originally published March 2026; last refreshed May 2026. See our [About page](/about/) for details on our review process.*
