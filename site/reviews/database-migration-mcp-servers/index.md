# Database Migration & Schema Management MCP Servers — Google Toolbox Hits v1.0 GA, boringSQL/dryrun Adds Offline Safety Analysis, Core Gaps Remain

> Database migration and schema management MCP servers: Google MCP Toolbox hits v1.0 GA (14.9k stars), boringSQL/dryrun adds offline migration safety analysis, Prisma MCP repo dormant but Prisma Next rebuilds migration architecture.


**At a glance:** Database migration and schema management MCP servers cover one of the most **foundational developer workflows** — safely evolving database schemas as applications change. Every non-trivial application needs schema migrations, yet the MCP ecosystem is strikingly thin. [Prisma's official MCP server](https://github.com/prisma/mcp) (built into CLI v6.6.0+) exposes migrate-dev, migrate-status, and migrate-reset — though the MCP repo has been dormant since October 2025 while Prisma Next rebuilds the entire migration architecture with TypeScript migrations and graph-based ordering. [Google's MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox) hit v1.0.0 GA on April 10, 2026 — renamed from genai-toolbox to mcp-toolbox, now at ~14,900 stars, with MySQL table stats and BigQuery semantic search added. [Liquibase's AI Changelog Generator](https://www.liquibase.com/) (19 tools) remains in private preview — no public GA announcement since the original review. New: [boringSQL/dryrun](https://github.com/boringSQL/dryrun) (Rust, 25 stars) is the first **migration-safety-focused** MCP server — 16 offline tools for lock analysis, table rewrite detection, schema linting, and safer DDL alternatives without needing live DB credentials. [Bytebase/dbhub](https://github.com/bytebase/dbhub) (2,675 stars) is the fastest-growing entry, shipping weekly. Meanwhile, Flyway, Alembic, golang-migrate, Rails, Sequelize, TypeORM, and every online schema migration tool still have **zero MCP servers**. This is the **sixteenth review in our [Developer Tools MCP category](/categories/developer-tools/)**. Also part of our **[Databases MCP category](/categories/databases/)**.

The database management systems market ($84-132B in 2025, growing 16-18% annually) underscores how critical this tooling layer is. Schema migration tools are a subset with no standalone market sizing, but they're deeply embedded in every development workflow. Flyway and Liquibase are neck-and-neck leaders: Flyway is developer-oriented (10.7k GitHub stars), Liquibase is enterprise-oriented (5.2k stars). Atlas from Ariga (6.3k stars) is rising as a declarative alternative — "Terraform for databases" — that compares current vs. desired state. Prisma (43k stars) dominates the TypeScript ORM space with built-in schema management, and Drizzle (28k stars) is the fastest-growing challenger. The MCP gap is not in obscure tooling — it's in the tools developers use every day.

**Architecture note:** Database migration MCP servers follow three patterns. **ORM-embedded** servers (Prisma, Drizzle) run as part of the ORM's existing CLI — the MCP endpoint exposes the same migration commands developers already use (`prisma migrate dev`, `drizzle-kit generate`). **Tool-specific connectors** (mcp-atlas, django-migrations-mcp, mig2schema) wrap a standalone migration tool's CLI in an MCP interface, requiring the underlying tool to be installed. **Platform-level** servers (Google MCP Toolbox, FreePeak/db-mcp-server) provide database operations including schema inspection but treat migrations as one capability among many. A critical distinction: ORM-embedded servers only work with their specific schema format (Prisma schema, Drizzle config), while tool-specific connectors support whatever the underlying tool supports (Atlas handles 16 ORMs, Liquibase supports XML/YAML/JSON/SQL changelogs). No MCP server currently supports framework-agnostic migration workflows.

## What's Available

### Prisma MCP Server — Built into the Most Popular TypeScript ORM

| Aspect | Detail |
|--------|--------|
| Repository | [prisma/mcp](https://github.com/prisma/mcp) |
| Language | TypeScript |
| License | Apache-2.0 |
| Version | Built into Prisma CLI v6.6.0+ |
| Transport | stdio (local), HTTP (remote for Prisma Postgres) |
| Creator | Prisma (official vendor) |

**Local MCP server** exposes migration and schema tools:

| Tool | Capability |
|------|-----------|
| migrate-status | Check current migration state against schema |
| migrate-dev | Create and execute new migrations from schema changes |
| migrate-reset | Reset database and re-apply all migrations |
| Schema management | Introspect and modify Prisma schema files |
| Query execution | Run queries against the connected database |
| Prisma Studio | Visual data browser and editor |

**Remote MCP server** (for Prisma Postgres) adds:

| Tool | Capability |
|------|-----------|
| Database provisioning | Create new Prisma Postgres instances |
| Backup management | Create and restore database backups |
| Connection management | Configure and rotate connection strings |

**Key differentiator:** The **only migration MCP server built directly into an ORM's CLI** — no separate installation, no sidecar, no additional configuration. Prisma is the most popular TypeScript ORM (43k GitHub stars), so the addressable user base is enormous. The local server covers the full migration lifecycle: check status, create migrations from schema diffs, execute them, and reset if needed. The remote server extends this to cloud database provisioning and backup for Prisma Postgres users. Works with Claude Desktop, VS Code, and any MCP host.

**April 2026 update — Prisma Next is rebuilding the migration architecture:** The MCP repo itself (prisma/mcp) has had **zero commits since October 7, 2025**, and remains at 41 stars. Meanwhile, Prisma's engineering is undergoing a major shift. A [March 27, 2026 post "Rethinking Database Migrations"](https://www.prisma.io/blog) introduced a graph-based migration system with `ops.json`/`migration.json` and idempotent operations for branch conflict resolution. An [April 27, 2026 post "TypeScript Migrations in Prisma Next"](https://www.prisma.io/blog) introduced TypeScript-authored migrations with pre/post verification steps — explicitly noting AI agents can generate these. The MCP server is not yet updated to reflect Prisma Next's architecture. Expect the MCP tooling to evolve significantly once Prisma Next stabilizes.

**Limitation:** ORM-locked — only works with Prisma's schema format. If your project uses Drizzle, TypeORM, Sequelize, Knex, or raw SQL migrations, this server is irrelevant. The remote MCP server is specific to Prisma Postgres, not general PostgreSQL. Migration features are local-only (stdio) — no remote migration execution. Prisma's opinionated schema format means teams using custom migration workflows can't adopt this without committing to Prisma's approach. The MCP repo is dormant pending Prisma Next — it may not reflect current Prisma migration capabilities.

### Liquibase AI Changelog Generator MCP — Enterprise Migrations Meet Natural Language

| Aspect | Detail |
|--------|--------|
| Distribution | [Liquibase](https://www.liquibase.com/) (private preview, registration required) |
| Language | Java |
| License | Liquibase proprietary |
| Version | Requires Liquibase 5.0+ (released September 2025) |
| Transport | MCP standard (Claude Desktop, VS Code, any MCP host) |
| Creator | Liquibase (official vendor) |

**19 precisely defined tools** that use Liquibase's native Java APIs:

| Tool Pattern | Capability |
|------|-----------|
| Changelog generation | Convert natural language descriptions to production-ready Liquibase XML changelogs |
| Validation | Auto-validate generated changelogs against an ephemeral H2 database before output |
| Rollback | AI-assisted rollback changelog generation |
| Schema inspection | Examine current database state to inform changelog creation |

**Key differentiator:** AI **never writes raw SQL or XML** — it determines which Liquibase tool to invoke with which parameters, and the tools produce the output. This architecture means generated changelogs conform to Liquibase's format constraints by construction, not by prompt engineering. The ephemeral H2 database validation step catches errors before changelogs reach production. Liquibase's enterprise positioning (compliance, audit trails, rollback) makes this appealing for regulated environments. Java 17 minimum.

**Limitation:** **Private preview** — requires registration, not generally available. Proprietary license limits customization. Requires Liquibase 5.0 (September 2025), which is a major version upgrade. XML changelog format is Liquibase-specific — teams using SQL-based migrations or other formats need Liquibase's conversion tools. The 19-tool count is high for context windows. No public GitHub repository means no community visibility, no star count, no issue tracker. Enterprise pricing unclear.

### Google MCP Toolbox for Databases — Platform-Level Database Operations, Now v1.0 GA

| Aspect | Detail |
|--------|--------|
| Repository | [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) |
| Stars | ~14,900 |
| Language | Go |
| License | Apache-2.0 |
| Version | v1.1.0 (April 13, 2026) |
| Transport | MCP standard |
| Creator | Google (official) |

**Key differentiator:** **Multi-database platform server** supporting PostgreSQL, MySQL, SQL Server, and Neo4j. Handles connection pooling, authentication, and schema operations across databases. Google's documentation notes it helps "cut down time spent on schema migrations." Part of the broader Google Cloud AI ecosystem. At ~14,900 stars, it has the highest adoption of any server in this review — though that adoption reflects general database tooling, not migration-specific use.

**April 2026 update — v1.0.0 GA released:** The project hit its first stable release on April 10, 2026, and was renamed from `genai-toolbox` to `mcp-toolbox` to reflect production status. Key additions: MySQL table stats tool, BigQuery semantic search, ES/QL arbitrary queries, Elasticsearch vector search refactored, opaque token validation, Cloud SQL Postgres health check. v1.1.0 (April 13) adds vector assist tools for Cloud SQL Postgres. Stars grew from ~13,500 to ~14,900 since March. The GA milestone signals Google's commitment to this as a production-grade platform, making it more relevant for enterprise database agent workflows.

**Limitation:** **Not migration-specific** — schema migrations are a side benefit, not the primary function. No migration versioning, no changelog management, no migration status tracking, no rollback support. Teams needing actual migration workflows (create migration, apply, rollback, status check) will find this insufficient. Google Cloud ecosystem alignment means best experience with Cloud SQL and AlloyDB. The migration-relevant capabilities are a subset of a much larger tool surface.

### mcp-atlas — Declarative Schema-as-Code Migrations

| Aspect | Detail |
|--------|--------|
| Repository | [mpreziuso/mcp-atlas](https://github.com/mpreziuso/mcp-atlas) |
| Language | TypeScript |
| License | MIT |
| Transport | stdio |
| Creator | Community (solo maintainer) |

**5 tools** covering the Atlas migration workflow:

| Tool | Capability |
|------|-----------|
| migrate-apply | Execute pending migrations against the database |
| migrate-diff | Generate migration from difference between current and desired state |
| migrate-lint | Lint migrations for safety issues (destructive changes, data loss) |
| migrate-status | Check migration status and pending changes |
| migrate-validate | Validate migration directory integrity |

**Key differentiator:** The **only declarative migration MCP server**. Atlas itself (6.3k stars, by Ariga) takes the "Terraform for databases" approach — you define the desired schema state, and Atlas computes the migration to get there. This MCP server wraps all five core Atlas CLI commands. Supports 16 ORMs and HCL/SQL/ORM schema definitions. The `migrate-lint` tool is unique in the MCP migration ecosystem — it catches destructive changes before they execute. MIT license. **Note:** Ariga released Atlas v1.2 (April 9, 2026) with column-level lineage, schema ownership policy, and PostgreSQL/Oracle/Snowflake additions — but released it without any MCP update. Ariga instead provides AI coding assistant integration via instruction files (CLAUDE.md, .cursorrules) rather than MCP servers.

**Limitation:** **Effectively abandoned** — 1 star, last commit February 4, 2026. Community project, not official Ariga support. Requires Atlas CLI installed separately. The declarative approach is powerful but unfamiliar to teams used to imperative migrations. Ariga shows no signs of adopting the MCP protocol for Atlas itself.

### drizzle-mcp — Migrations for the Fastest-Growing TypeScript ORM

| Aspect | Detail |
|--------|--------|
| Repository | [defrex/drizzle-mcp](https://github.com/defrex/drizzle-mcp) |
| Language | TypeScript |
| License | Not specified |
| Transport | stdio |
| Creator | Community |

**Key differentiator:** **Drizzle ORM migration support** — generate and run migrations via drizzle-kit, plus schema introspection and query execution. Drizzle (28k+ stars) is the fastest-growing TypeScript ORM, and this is its only MCP interface. Supports SQLite and PostgreSQL. Works with any existing Drizzle project — just point it at your drizzle config.

**Limitation:** Community-maintained, no official Drizzle backing. **Stagnant** — 13 stars, no commits since July 15, 2025. SQLite and PostgreSQL only — no MySQL support despite Drizzle supporting it. License not specified in repository. Solo maintainer. Drizzle's migration format is ORM-specific — same lock-in concern as Prisma.

### boringSQL/dryrun — Offline Migration Safety Analysis

| Aspect | Detail |
|--------|--------|
| Repository | [boringSQL/dryrun](https://github.com/boringSQL/dryrun) |
| Stars | 25 |
| Language | Rust |
| License | MIT |
| Transport | stdio |
| Creator | Community |

**16 tools** focused on migration safety without live DB credentials:

| Tool Category | Capability |
|------|-----------|
| Lock analysis | Detect operations that take locks, estimate lock duration and impact |
| Table rewrite detection | Identify DDL that causes full table rewrites (slow on large tables) |
| Safer DDL alternatives | Suggest safer rewrites for destructive or locking operations |
| Migration safety checks | Pre-flight validation before running migrations against production |
| Schema snapshot | Capture current schema state for drift detection |
| Schema drift detection | Compare current schema to snapshot and report changes |
| Query validation | Lint SQL queries against schema rules (20+ linting rules) |
| Vacuum health | Analyze table bloat and vacuum needs |

**Key differentiator:** **Offline-first migration safety** — the only MCP server designed to analyze migrations without requiring live database credentials. This matters because developers often can't connect to production during development. boringSQL/dryrun analyzes SQL DDL statically to flag dangerous operations before they reach a database. The lock analysis and table rewrite detection tools directly address the production-safety gap identified in the original review (no gh-ost/pt-osc MCP). Built in Rust (correctness-focused), with active development — multiple PRs merged in the week ending May 2, 2026.

**Limitation:** **PostgreSQL-only** — multi-database support is tracked as an open issue. 25 stars indicates early adoption, not a mature community project. Community-maintained, solo developer. Static analysis can't catch all migration issues — some problems only appear at runtime or at scale. Not a substitute for online schema migration tools (gh-ost, pt-osc) for actually executing large-scale production migrations.

### mig2schema — Migration History to Schema DDL

| Aspect | Detail |
|--------|--------|
| Repository | [alc6/mig2schema](https://github.com/alc6/mig2schema) |
| Language | Go |
| Transport | stdio |
| Creator | Community |

**2 tools** with a focused purpose:

| Tool | Capability |
|------|-----------|
| extract_schema | Run migration history in a sandbox, produce final schema via pg_dump |
| validate_migrations | Verify migration history applies cleanly |

**Key differentiator:** Solves a specific problem — **understanding what your migration history actually produces**. Runs all migrations in a sandbox PostgreSQL instance and extracts the resulting schema as DDL. Useful for teams with long migration histories where the cumulative schema is unclear, or for validating that migrations produce the expected result.

**Limitation:** PostgreSQL-only. Two tools only. Requires a sandbox PostgreSQL instance. Niche use case — schema extraction, not migration management. Small community project.

## Also Available

### FreePeak/db-mcp-server (372 stars, Go)

Multi-database MCP server with query execution, transaction management, and schema exploration. **v1.9.0 shipped April 11, 2026** after a near-year gap — but the sole feature is a `--unified-tools` flag that consolidates per-database tool proliferation into 6 shared tools when connecting to 30+ databases (solves context window bloat). The "AI-Assisted Migration Manager" that was on the Q4 2025 roadmap did **not ship**. Current capabilities remain database operations, not migration-specific workflows.

### django-migrations-mcp (mrrobotke, 6 stars, Python)

Django-specific migration management for distributed environments. Framework-locked to Django's ORM and migration system. 6 stars indicates minimal adoption.

### Bytebase/dbhub (2,675 stars, Go)

Schema exploration and querying across databases — but **not migration execution**. Bytebase itself (11.6k stars) is a major database schema change platform, yet its MCP presence (dbhub) doesn't expose its schema change workflow. This is a notable gap: the tool exists, the MCP server just doesn't surface the migration features. **Active development:** 28 commits since March 24, 2026, shipping roughly weekly. Now listed on the MCP registry (npm: `@bytebase/dbhub`). Key recent additions: PostgreSQL SSL expansion (`sslmode=verify-ca/verify-full` with `sslrootcert`), DNS rebinding protection for HTTP transport, graceful handling of missing transitive dependencies. The fastest-growing entry in this review by star count (+275 since March 24).

### Dmitriusan/mcp-migration-advisor (0 stars, April 2026)

Static analysis MCP server for Flyway and Liquibase migrations. **6 tools:** `analyze_migration` (Flyway `V__.sql`/`R__.sql` naming), `analyze_liquibase` (XML changelogs), `analyze_liquibase_yaml` (YAML changelogs), `score_risk` (0–100 risk score), `generate_rollback`, `detect_conflicts`. No execution — pure static analysis. Noteworthy as the **first and only community MCP server that supports Flyway** (the most popular Java migration tool). Zero stars and no community traction as of May 2, 2026 — but the concept fills a genuine gap.

### Kafka Schema Registry MCP

48 tools for schema evolution and migration in event streaming contexts. Relevant for Kafka schema compatibility management (AVRO, Protobuf, JSON Schema) but not for relational database migrations.

## Notable Gaps

**No Flyway MCP server** — Flyway (10.7k GitHub stars, owned by Redgate) is the most popular Java-ecosystem migration tool and arguably the most widely used developer-oriented migration tool overall. Zero MCP presence.

**No Alembic MCP server** — The standard Python/SQLAlchemy migration tool. Every production Python application using SQLAlchemy relies on Alembic for migrations. Zero MCP presence.

**No golang-migrate MCP server** — The most popular Go migration tool (16.4k GitHub stars — more than Flyway). Zero MCP presence.

**No Sequelize, TypeORM, Knex, or MikroORM MCP servers** — The Node.js ORM ecosystem beyond Prisma and Drizzle has no migration MCP tooling whatsoever.

**No Rails migrations MCP server** — Rails invented the modern migration pattern. ActiveRecord migrations remain the standard for Ruby applications. Zero MCP presence.

**No gh-ost or pt-online-schema-change MCP server** — Online schema migration tools that handle zero-downtime production migrations. These are critical for large-scale databases where `ALTER TABLE` locks are unacceptable.

**No Bytebase migration MCP** — Bytebase (11.6k stars) has dbhub for queries but doesn't expose its schema change workflow through MCP. The migration platform exists; the MCP integration doesn't.

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging | Profiling | Code Review |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|----------|-----|----------|----------|---------|---------|-------------- | --------------|-----------|-----------|-------------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, 1.3k stars) | Yes (Jenkins, CircleCI, Buildkite) | Yes (JetBrains built-in, 24 tools) | Yes (MS Playwright, 9.8k stars, 24 tools) | Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana) | Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) | Yes (NuGet built-in VS 2026, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B 384, JetBrains built-in server) | Yes (Postman 192, Apollo GraphQL 275, Kong deprecated, Apigee, MuleSoft) | Yes (Splunk 13 tools GA, Grafana Tempo built-in, Grafana Loki 103 stars) | Partial (Liquibase private preview, Prisma built-in CLI) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector 9.2k official) | Partial (CodSpeed MCP, Polar Signals remote, Grafana Pyroscope via mcp-grafana) | Yes (SonarQube 442 stars, Codacy 56 stars, Graphite GT built-in) |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (1.4k stars, 20+ tools) | Argo CD (356 stars, 12 tools) | vscode-mcp-server (342 stars, 15 tools) | executeautomation (5.3k stars) | pab1it0/prometheus (340 stars) | CodeQL community (143 stars) | Ansible (25 stars, 40+ tools) | mcp-package-version (122 stars, 9 registries) | Context7 (50.3k stars), magic-mcp (4.5k stars) | openapi-mcp-generator (495 stars), mcp-graphql (374 stars) | cr7258/elasticsearch (259 stars), Traceloop OTel (178 stars) | boringSQL/dryrun (25 stars, Rust, offline safety), defrex/drizzle-mcp (13 stars, Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars), Docs MCP (87 stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars), devtools-debugger (341 stars) | theSharque/mcp-jperf (Java JFR), PageSpeed Insights MCP servers | kopfrechner/gitlab-mr-mcp (86 stars), crazyrabbitLTC (32 stars) |
| **Primary function** | Repository operations | Repository operations | Repository operations | Container lifecycle | Cluster management | Pipeline management | Editor integration | Test execution | Observability queries | Vulnerability scanning | Infrastructure provisioning | Dependency intelligence | Context provision + UI generation | Spec-to-server conversion + API interaction | Log search/analysis + trace correlation | Schema migration & version control | Doc access, search, generation & quality | Breakpoints, stepping, variable inspection, crash analysis | Flamegraph analysis, CPU/memory profiling, benchmarks, web audits, load testing | Code quality analysis, PR management, diff review, stacked PR creation |
| **Vendor count** | 1 (GitHub) | 1 (GitLab) | 0 (Atlassian via Jira only) | 1 (Docker) + community | 0 (Red Hat leads community) | 3 (Jenkins, CircleCI, Buildkite) | 1 (JetBrains) | 1 (Microsoft) | 6 (Grafana, Datadog, Sentry, Dynatrace, New Relic, Instana) | 7+ (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | 5+ (HashiCorp, Pulumi, AWS, OpenTofu, Spacelift) | 2 (Microsoft/NuGet, Homebrew) | 3 (Vercel, E2B, Upstash/Context7) | 4+ (Postman, Apollo, Kong, Google/Apigee, MuleSoft) | 6+ (Splunk, Grafana/Loki, Grafana/Tempo, Coralogix, Axiom, Mezmo) | 2 (Liquibase, Prisma) + Google partial | 5+ (Microsoft, Mintlify, ReadMe, Stainless, OpenAI, Vonage, Fern, Apidog) | 3 (Google/Chrome DevTools, Microsoft/DebugMCP, LLVM/LLDB built-in) | 3 (CodSpeed, Polar Signals, Tricentis/NeoLoad) + Grafana partial | 3 (SonarSource, Codacy, Graphite) + CodeRabbit as client |
| **Code generation role** | Context (repos, issues, PRs) | Context (repos, issues, MRs) | Context (repos, PRs) | Context (images, containers) | Context (cluster state) | Context (pipeline status) | Bidirectional (tools + context) | Context (test results) | Context (metrics, logs) | Context (vulnerabilities) | Generation (IaC templates) | Context (versions, advisories) | Direct (UI components, docs, execution) | Bidirectional (spec-to-tools, API execution) | Context (log patterns, traces, errors) | Bidirectional (migration generation + schema inspection) | Context (doc access/search) + Generation (doc output) | Bidirectional (set breakpoints + inspect state) | Context (profiles, flamegraphs, benchmarks) + Generation (benchmark harnesses) | Bidirectional (quality data as context + review comments as output) |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | API tokens per platform | Local connection (port/stdio) | None (local browsers) | API tokens / OAuth (remote) | API tokens / CLI auth | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / API keys | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect | API keys (CodSpeed, Polar Signals) / Grafana auth / Google API key (PageSpeed) | API tokens (SonarQube, Codacy) / GitHub PAT / GitLab PAT |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | No | No (but Microsoft is Platinum) | No (but Microsoft is Platinum) | No | No | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) | No | No |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | 5.6M developers | Jenkins: 11.3M devs | VS Code: 75.9% market share | Playwright: 45.1% QA adoption | Datadog: 32.7k customers | SonarQube: 17.7% SAST mindshare | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 30M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Flyway: 10.7k stars, Liquibase: 5.2k stars, Atlas: 6.3k stars, Prisma: 43k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars, ReadMe: powering major API docs | Chrome: 65%+ browser share, VS Code: 75.9% IDE share, x64dbg: 45k+ stars | APM market: $7-10B, Pyroscope: 11k+ stars, async-profiler: 9k+ stars | SonarQube: 7.4M+ users, CodeRabbit: top AI reviewer, Qodo/PR-Agent: 10.5k stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | [4/5](/reviews/kubernetes-mcp-servers/) | [3/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) | [3.5/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | [3/5](/reviews/package-management-mcp-servers/) | [3.5/5](/reviews/code-generation-mcp-servers/) | [3.5/5](/reviews/api-development-mcp-servers/) | [3.5/5](/reviews/logging-tracing-mcp-servers/) | 2.5/5 | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | [4.5/5](/reviews/debugging-mcp-servers/) | [3/5](/reviews/profiling-performance-mcp-servers/) | [3.5/5](/reviews/code-review-pull-request-mcp-servers/) |

## Known Issues

1. **Most major migration tools have zero MCP presence** — Flyway (10.7k stars), Alembic (Python standard), golang-migrate (16.4k stars), Rails migrations (the original migration framework), Sequelize, TypeORM, Knex, and MikroORM all have no MCP servers. The tools that the majority of developers actually use for migrations are completely absent. This isn't a gap at the edges — it's a gap at the center.

2. **Liquibase's MCP is private preview — not generally available** — The most feature-rich migration MCP server (19 tools, AI-assisted changelog generation, ephemeral validation) requires registration and is not publicly downloadable. No public GitHub repository, no community visibility, no way to evaluate it without vendor approval. Private preview status means the API may change, features may be removed, and general availability timing is unclear.

3. **Prisma's MCP is ORM-locked — only works with Prisma schema format** — The most accessible migration MCP server (built into CLI, no separate install) only works if your project uses Prisma. The same applies to drizzle-mcp for Drizzle projects and django-migrations-mcp for Django projects. Each MCP server serves only its own ORM's user base, and there's no framework-agnostic migration MCP.

4. **Atlas community MCP (mpreziuso) is the only declarative migration MCP — but it's a solo-maintainer project** — The "Terraform for databases" approach (declare desired state, compute the diff) is powerful, but the MCP server wrapping it has unknown adoption and a single maintainer. Atlas itself has 6.3k stars and commercial backing from Ariga, but the MCP server is a community contribution with no official support.

5. **No online schema migration MCP (gh-ost, pt-osc)** — Production databases at scale cannot afford `ALTER TABLE` locks. Tools like GitHub's gh-ost and Percona's pt-online-schema-change handle zero-downtime migrations, but neither has an MCP server. AI agents can generate migrations but cannot execute them safely on large production databases through MCP.

6. **Migration rollback support is minimal across the ecosystem** — Liquibase's private preview includes AI-assisted rollback generation. Prisma has `migrate-reset` (full reset, not selective rollback). Atlas has no rollback tool in the MCP server. None of the community servers support targeted rollback of specific migrations. In production, rollback is often more important than forward migration.

7. **No migration CI/CD integration through MCP** — None of these MCP servers can trigger migration pipelines, run migrations in staging before production, or integrate with deployment workflows. AI agents can generate migrations locally but cannot push them through a CI/CD pipeline to production. The migration-to-deployment gap is unaddressed.

8. **ORM fragmentation means each framework needs its own MCP** — Prisma, Drizzle, Django, Rails, Sequelize, TypeORM, Knex, MikroORM, SQLAlchemy/Alembic, and GORM each have their own migration format and CLI. An MCP server for one is useless for another. Only tool-level servers (Flyway, Liquibase, Atlas, golang-migrate) are framework-agnostic — and most of those don't have MCP servers.

9. **Google MCP Toolbox is database-focused, not migration-focused** — At 13.5k stars, it's the highest-starred server in this review, but its migration relevance is incidental. Schema operations are a subset of a much larger tool surface covering connection pooling, authentication, and query execution. Teams seeking it for migrations will find it insufficient; teams seeking it for database operations will find migrations underserved.

10. **No cross-database migration support** — Each MCP server targets one ORM or tool. There's no MCP server that can manage migrations across PostgreSQL, MySQL, and SQL Server in a polyglot database environment. Even Liquibase and Atlas, which support multiple databases, have MCP servers that operate one database at a time. Multi-database migration orchestration doesn't exist in MCP.

## Bottom Line

**Rating: 2.5 out of 5**

Database migration and schema management MCP servers remain in **very early state** as of May 2026. Some ecosystem movement has occurred since March: Google's MCP Toolbox hit v1.0 GA (renamed to mcp-toolbox, ~14,900 stars) and is now a production-grade platform; Bytebase/dbhub (2,675 stars) is actively shipping weekly; and boringSQL/dryrun (Rust, 25 stars) introduces the first migration-safety-focused MCP server — offline lock analysis and DDL linting without live DB credentials. But the structural landscape is unchanged.

The Prisma MCP repo has been dormant since October 2025 while Prisma Next rebuilds the migration architecture entirely (TypeScript migrations, graph-based ordering, branch conflict resolution). Liquibase's AI Changelog Generator remains stuck in private preview — no GA, no public repo. mcp-atlas dropped to 1 star and last committed in February; drizzle-mcp stagnant since July 2025. The community mcp-migration-advisor (April 2026) is the first Flyway-aware MCP server — but with 0 stars and no traction.

The **2.5/5 rating** holds: the gaps are not at the edges but at the center — Flyway (10.7k stars, most popular Java migration tool), Alembic (Python standard), golang-migrate (16.4k stars, most popular Go migration tool), Rails migrations (the original migration framework), and every major Node.js ORM beyond Prisma and Drizzle are completely absent. No online schema migration tooling (gh-ost, pt-osc) exists in MCP. Rollback support is minimal. CI/CD integration is zero. The 0.5 points above 2.0 come from Prisma's clean built-in integration (even if dormant) and Google Toolbox's growing adoption as a general database platform. This category will matter enormously once it matures — schema migrations touch every backend developer — but today it's mostly empty shelves.

**Who benefits from database migration MCP servers today:**

- **Prisma teams** — The built-in CLI integration (v6.6.0+) covers the core workflow, even if the MCP repo is dormant. migrate-dev, migrate-status, and migrate-reset are available now
- **Teams needing pre-flight safety analysis** — boringSQL/dryrun (Rust, 25 stars) is new and PostgreSQL-only, but its offline lock analysis and DDL linting fill a genuine gap for teams who want AI-assisted safety checks without live DB credentials
- **Drizzle ORM users** — drizzle-mcp (13 stars) still works for schema management, though it hasn't been maintained since July 2025
- **Liquibase enterprise teams** — If you can access the private preview, 19 tools with AI-assisted changelog generation and ephemeral validation remains the most feature-rich option

**Who should wait:**

- **Flyway users** — The most popular Java migration tool's only MCP support is the experimental mcp-migration-advisor (0 stars, static analysis only). No official server, no timeline
- **Python/Alembic teams** — The standard Python migration tool has no MCP server. django-migrations-mcp exists but is Django-specific (6 stars)
- **Go developers** — golang-migrate (16.4k stars) has no MCP server. mig2schema is PostgreSQL-only schema extraction, not migration management
- **Rails/Ruby teams** — The framework that invented migrations has no MCP tooling for them
- **Teams needing production safety** — No online schema migration support (gh-ost, pt-osc), minimal rollback support, no CI/CD integration. boringSQL/dryrun helps with pre-flight analysis, but executing large-scale production migrations safely through AI agents remains impossible

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Originally published March 2026; refreshed May 2026. See our [About page](/about/) for details on our review process.*

