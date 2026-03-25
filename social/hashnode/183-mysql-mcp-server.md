---
title: "MySQL MCP Servers — The World's Most Popular Database Meets AI"
slug: mysql-mcp-servers-review
description: "MySQL's MCP ecosystem features benborla/mcp-server-mysql (1.4k stars) and designcomputer/mysql_mcp_server (1.2k stars) as community leaders, plus multi-database servers from Bytebase DBHub (2.4k stars) and Google Toolbox (13.5k stars). No Oracle-official server. Rating: 3.5/5."
tags: mcp, ai, mysql, database
canonical_url: https://chatforest.com/reviews/mysql-mcp-server/
---

**At a glance:** MySQL has a **solid community-driven MCP ecosystem** — but no official server from Oracle. The two leading MySQL-specific servers are [benborla/mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) (1.4k stars, TypeScript, MIT) with SSH tunnel support and Claude Code integration, and [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) (1.2k stars, Python, MIT) focused on simplicity and security. Multi-database servers [Bytebase DBHub](https://github.com/bytebase/dbhub) (2.4k stars) and [Google's MCP Toolbox](https://github.com/googleapis/genai-toolbox) (13.5k stars) also support MySQL alongside other databases. Cloud vendors AWS, Azure, and Google all provide MySQL MCP support through their platform servers. Part of our **[Databases MCP category](https://chatforest.com/categories/databases/)**.

MySQL is the **world's most popular open-source relational database** — powering roughly **39% of the relational database market** with over 235,000 companies using it worldwide. Created in 1995, acquired by Oracle via Sun Microsystems in 2010. The latest Innovation release is **MySQL 9.6** (January 2026); MySQL 8.0 reaches end-of-life in **April 2026**.

## What's Available

### mcp-server-mysql — benborla/mcp-server-mysql

The **most popular MySQL-specific MCP server**, optimized for Claude Code integration:

| Aspect | Detail |
|--------|--------|
| GitHub | [benborla/mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) — 1.4k stars, 181 forks, 222 commits, MIT |
| Language | TypeScript/JavaScript |
| Install | npm / Smithery |
| Transport | stdio |

**Key features:** SSH tunnel support with auto-start/stop via Claude Code hooks, multi-database mode, optional DDL operations, SQL injection prevention via prepared statements, connection pooling, query result caching, configurable timeouts and rate limiting.

### mysql_mcp_server — designcomputer/mysql_mcp_server

A **simpler, security-focused** MySQL MCP server:

| Aspect | Detail |
|--------|--------|
| GitHub | [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) — 1.2k stars, 229 forks, 69 commits, MIT |
| Language | Python |
| Install | `pip install mysql-mcp-server` / Smithery / Docker |

**Key differentiator:** Simplicity and security emphasis. The smallest footprint of the major MySQL MCP servers — install via pip, configure with environment variables, go. Security-audited by MseeP.ai.

### Bytebase DBHub — bytebase/dbhub

A **multi-database MCP server** with strong MySQL support:

| Aspect | Detail |
|--------|--------|
| GitHub | [bytebase/dbhub](https://github.com/bytebase/dbhub) — 2.4k stars, 194 forks, 482 commits, MIT |
| Databases | PostgreSQL, **MySQL**, MariaDB, SQL Server, SQLite |

3 MCP tools: `execute_sql`, `search_objects`, and custom parameterized SQL operations via TOML config. Zero-dependency, token-efficient design. SSH tunneling and SSL/TLS encryption. Includes a web workbench interface.

### Google MCP Toolbox for Databases

| Aspect | Detail |
|--------|--------|
| GitHub | [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) — 13.5k stars, 1.3k forks, 1,614 commits |
| Language | Go |

Supports Cloud SQL for MySQL, PostgreSQL, SQL Server, AlloyDB, Spanner, and Bigtable. Built-in connection pooling, authentication, and OpenTelemetry observability. The most production-hardened option for Google Cloud MySQL users.

### Cloud Vendor Support

- **Google Cloud SQL** — Managed remote MCP server (Preview), natural language interactions, query optimization
- **AWS** — Aurora MySQL MCP server in [awslabs/mcp](https://github.com/awslabs/mcp) monorepo (8,540 stars total)
- **Azure** — MySQL support in [microsoft/mcp](https://github.com/microsoft/mcp), MySQL password or Entra authentication

### Additional Servers

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) | 397 | Python | SQLAlchemy-based, MySQL + 7 other databases |
| [MariaDB/mcp](https://github.com/MariaDB/mcp) | 151 | Python | Official MariaDB MCP (MySQL-compatible), vector search |
| [askdba/mysql-mcp-server](https://github.com/askdba/mysql-mcp-server) | 16 | Go | Read-only, multi-DSN, vector search (MySQL 9.0+) |

## Database MCP Ecosystem Comparison

| Feature | MySQL (this review) | PostgreSQL |
|---------|-------------------|------------|
| Dedicated MCP servers | ~6 | ~10+ |
| Top server stars | 1.4k (benborla) | 2.4k (Postgres MCP Pro) |
| Official vendor MCP server | None (Oracle) | None (community-governed) |
| Cloud vendor support | AWS, Azure, Google | AWS, Azure, Google |
| Performance analysis tools | Limited | Postgres MCP Pro (index tuning, health) |
| Rating | **3.5/5** | **4.5/5** |

## Known Issues

1. **No Oracle-official MCP server** — The ecosystem is entirely community-driven
2. **Smaller ecosystem than PostgreSQL** — roughly half the dedicated servers
3. **No performance analysis tools** — no DBA-grade performance optimization via MCP
4. **MySQL 8.0 end-of-life approaching** (April 2026) — compatibility with 9.x not always documented
5. **MariaDB compatibility is inconsistent** across MySQL MCP servers

## Bottom Line

**Rating: 3.5 out of 5**

**benborla/mcp-server-mysql** (1.4k stars) is the clear leader for MySQL-specific needs. **designcomputer/mysql_mcp_server** (1.2k stars) offers a simpler alternative. **Bytebase DBHub** (2.4k stars) is the best multi-database option. Two 1k+ star dedicated servers, strong multi-database support, and full cloud vendor coverage earn MySQL a good score. It loses a full point vs PostgreSQL for: no Oracle-official server, no performance analysis tools, and roughly half the number of dedicated servers.

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of March 2026. See our [About page](https://chatforest.com/about/) for details on our review process.*
