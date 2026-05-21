---
title: "Code Quality, Linting & Static Analysis MCP Servers — ESLint, SonarQube, Semgrep, Ruff, Biome, and More"
date: 2026-03-17T01:00:00+09:00
description: "Code quality, linting, and static analysis MCP servers let AI agents run linters, formatters, and security scanners through the Model Context Protocol."
og_description: "Code quality & linting MCP servers: SonarQube MCP (556 stars — official, settled at v1.18.1), Skylos (439 stars — v4.16.2, now GitLab/GH Actions scanning + Dart), mcp-language-server (1,531 stars — LSP bridge for any language), jonrad/lsp-mcp (183 stars — second LSP bridge). Semgrep MCP built into semgrep binary. Codacy official (59 stars, 25+ tools). ESLint MCP v0.3.5. CodeQL 20→25 stars v2.25.4. 25+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "Code quality, linting, and static analysis MCP servers for AI-powered code review, formatting, and security scanning across Python, JavaScript, TypeScript, Rust, Go, C#, and more. **The cross-language bridge** — isaacphi/mcp-language-server (1,531 stars, Go, BSD-3-Clause) connects any Language Server Protocol (LSP) server to MCP clients, exposing diagnostics, definitions, references, hover docs, and rename across Go (gopls), Rust (rust-analyzer), Python (pyright), TypeScript, and C/C++ (clangd). A second LSP bridge — jonrad/lsp-mcp (183 stars, TypeScript, MIT) — supports multiple LSPs simultaneously with dynamic schema generation. **SonarQube STABLE** — SonarSource/sonarqube-mcp-server (556 stars, Java, official) settled at v1.18.1 after adding Context Augmentation, workspace mounting, and mcp.sonarqube.com config generator. **Codacy OFFICIAL** — codacy/codacy-mcp-server (59 stars, MIT, 25+ tools) covers SAST, SCA, DAST, secrets, coverage, and quality gates with Codacy Guardrails real-time enforcement. **Skylos EXPANDING** — duriantaco/skylos (439 stars, v4.16.2, Apache 2.0) surged to v4.16 in one cycle — added Docker, GitLab CI scanner, GitHub Actions workflow scanning, Dart language, and Deep Mode audit. **Qartez gains dashboard** — kuberstar/qartez-mcp (50 stars, v0.9.10, Rust) added local web UI via `qartez dashboard` subcommand with live FS event updates. **CodeQL ACTIVE** — advanced-security/codeql-development-mcp-server (25 stars, v2.25.4) added SQLite backend, 14 new opt-in tools, Rust language support, and Models-as-Data Extensions. **NDepend for .NET** — ndepend/NDepend.MCP.Server (37 stars, 14 tools) delivers privacy-first on-premises .NET static analysis. **Semgrep BUILT-IN** — standalone semgrep/mcp (667 stars) archived, MCP in main binary with bug fixes in May 2026. **ESLint MCP v0.3.5** — maintenance update, ESLint 10.3.0 dependency. **Biome RFC NARROWED** — official MCP deprioritized for format/lint; Resources-only scope for docs/GritQL access. **mcp-code-checker expanded** — v0.1.10 adds tach (dependency/layer enforcement) and lint-imports tools (now 17 stars). The category earns 4/5 — enterprise platforms have strong MCP support, remaining gaps are official Prettier, Biome format/lint, and golangci-lint."
last_refreshed: 2026-05-21
---

Code quality tools are among the most-used developer utilities — ESLint, Prettier, Ruff, SonarQube, and Semgrep run in virtually every professional codebase. Exposing them through MCP lets AI agents not just write code, but validate it against the same standards your team enforces.

This review covers **linters, formatters, and static analysis tools** available as MCP servers. For security-specific scanning, see our [Code Security review](/reviews/code-security-mcp-servers/). For testing frameworks, see [Testing & QA](/reviews/testing-qa-mcp-servers/).

Part of our **[Developer Tools MCP category](/categories/developer-tools/)**. The headline finding: **enterprise code quality platforms are maturing** — SonarQube settled at 556 stars and v1.18.1 after a strong growth cycle, Skylos surged to v4.16.2 with Docker, GitLab CI scanning, GitHub Actions workflow scanning, and Dart language support, and CodeQL added a SQLite backend with 14 new opt-in tools. The LSP bridge servers continue accumulating stars despite dormant code, confirming the approach's long-term value.

## Cross-Language

### isaacphi/mcp-language-server (LSP Bridge)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-language-server](https://github.com/isaacphi/mcp-language-server) | 1,531 | Go | BSD-3-Clause | 6 |

**The most versatile code quality MCP server** — instead of wrapping individual linters, this bridges any Language Server Protocol server to MCP clients:

- **`diagnostics`** — file-level warnings and errors from your language server (the same ones your editor shows)
- **`definition`** — jump to symbol source code
- **`references`** — find all usages of a symbol
- **`hover`** — documentation and type information
- **`rename_symbol`** — project-wide renaming
- **`edit_file`** — multi-line text edits

Supports Go (gopls), Rust (rust-analyzer), Python (pyright), TypeScript, and C/C++ (clangd). Currently in beta at v0.1.1 with 104 commits and 126 forks. No code changes since March 2026 — growing organically on star count alone. The approach is pragmatic: rather than rebuilding linting logic for MCP, leverage the LSP ecosystem that editors have relied on for years.

### jonrad/lsp-mcp (Second LSP Bridge)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lsp-mcp](https://github.com/jonrad/lsp-mcp) | 183 | TypeScript | MIT | Multiple |

**Second LSP-to-MCP bridge** — validates the LSP bridge approach with a TypeScript implementation:

- **Multiple LSPs simultaneously** — run several language servers at once
- **Dynamic schema generation** from LSP JSON Schema
- **Supports Claude Desktop, Cursor, and MCP CLI Client**
- **POC state** — functional but still early

62 commits, 26 forks. Dormant since March 2025 — but still accumulating stars (+2 this cycle). The existence of a second LSP bridge implementation with 183 stars confirms that bridging existing LSP infrastructure is a viable long-term strategy for code quality MCP.

## Static Analysis & Security

### SonarSource/sonarqube-mcp-server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) | 556 | Java | SonarSource | Multiple |

**Official SonarQube MCP server** connecting AI agents to SonarQube Server or Cloud — **settled at v1.18.1 after a strong growth cycle**:

- **Context Augmentation (CAG)** — Open Beta, provides AI agents with enriched code context (STDIO mode, restricted users)
- **Workspace mounting** — reads files directly from disk to reduce context bloat instead of passing content through agent contexts
- **mcp.sonarqube.com** — new configuration generator for easy setup
- **Project quality metrics** — retrieve code quality dashboards programmatically
- **Issue management** — filter by severity, type, status across 20+ languages
- **Security hotspots** — identify and triage security-sensitive code
- **Advanced analysis** — code snippet scanning with improved accuracy
- **HTTP headers** — `SONARQUBE_TOOLSETS` and `SONARQUBE_READ_ONLY` for fine-grained tool control
- **Multi-tenant support** — HTTP mode for SonarQube Cloud
- **Broad IDE support** — Claude Code, GitHub Copilot, VS Code, Cursor, Windsurf, Zed

Now at 400+ commits and 78 forks, stable at v1.18.1 (May 11, 2026). No new releases since then. The features added this cycle — config generator, sandbox fix, CAG, AC/DC coverage tools — represent a substantial feature investment now settling into adoption.

### Semgrep MCP (Built into Semgrep Binary)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [semgrep/mcp](https://github.com/semgrep/mcp) (archived) | 667 | Python | — | 6+ |

**Semgrep's MCP server is now built directly into the main semgrep binary** — the standalone repo (667 stars) was archived October 2025:

- **Plugin bundles MCP + Hooks + Skills** — single install gives AI agents Semgrep Code, Supply Chain, and Secrets scanning
- **Scans every file an agent generates** — integrated with Claude Code, Cursor, Windsurf, and Codex
- **OAuth required for Streamable HTTP** — added January 2026
- **SSE transport dropped** — deprecated April 2026, Streamable HTTP only
- **DNS rebinding protection** — added February 2026
- **Custom rules from Semgrep Registry** — Hooks for Claude Code and Cursor pull rules automatically
- **Hosted endpoint** — available at mcp.semgrep.ai

The move from standalone repo to built-in integration signals maturity — Semgrep treats MCP as a core distribution channel, not an add-on.

### advanced-security/codeql-development-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [codeql-development-mcp-server](https://github.com/advanced-security/codeql-development-mcp-server) | 25 | TypeScript | GitHub CodeQL Terms | Multiple |

**CodeQL query development for AI agents** — **grew 25% (20→25 stars) this cycle**, now at v2.25.4 with active releases:

- **9 languages** — Python, JavaScript, Java, C/C++, C#, Go, Ruby, Swift, GitHub Actions; **Rust added in v2.25.2**
- **SQLite backend** — new in v2.25.2 with 14 additional opt-in tools (annotation, audit, query result caching)
- **Models-as-Data (MaD) Extensions** — v2.25.4 added auto-infer `codeql_query_run` format from `@kind` for result caching
- **AI-optimized prompts** guiding assistants through CodeQL development workflows
- **Test-driven validation** for query accuracy
- **Supply chain hardening** — Node.js security patches and invalid JSON Schema fix in v2.25.3
- **Stdio and HTTP transports**
- **Active development** — maintained by GitHub's CodeQL Expert Services team

This is for security researchers writing custom CodeQL queries, not general-purpose code scanning. Requires CodeQL CLI installation and GitHub CodeQL license agreement.

### codacy/codacy-mcp-server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [codacy-mcp-server](https://github.com/codacy/codacy-mcp-server) | 59 | TypeScript | MIT | 25+ |

**Official Codacy MCP server** — first enterprise code quality platform with comprehensive MCP coverage:

- **SAST, SCA, DAST, secrets, IaC, CI/CD** — full security analysis spectrum
- **Code quality analysis** — filter by severity, category, language, and author
- **File-level metrics** — issues, coverage, and duplication detection
- **Pull request evaluation** — diff coverage and issue detection
- **Quality gates** — automated pass/fail criteria
- **Local CLI analysis** — run analysis without cloud upload
- **Codacy Guardrails** — real-time enforcement scanning AI-generated code as it's written

143 commits, 20 forks. Integrates with VS Code (Copilot), Cursor, and Windsurf. The Guardrails feature is a differentiator — it catches quality issues in AI-generated code before commit.

### duriantaco/skylos (Dead Code + SAST)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [skylos](https://github.com/duriantaco/skylos) | 439 | Python | Apache 2.0 | Multiple |

**The most actively developed code quality MCP server this cycle** — surged from v4.3 to v4.16.2 in one cycle, expanding from dead code + SAST into a broader multi-language security and architecture audit platform:

- **Dead code detection** — unused functions, classes, imports with framework awareness (Django, FastAPI, Flask)
- **Security analysis** — SQL injection, XSS, SSRF, path traversal across Python, TypeScript/JavaScript, Java, Go, PHP, Rust; **Dart added in May 2026**
- **Secrets detection** — hardcoded credentials and high-entropy strings
- **AI code guardrails** — catches phantom security calls, missing decorators, unfinished stubs, and disabled controls from AI-generated code
- **CI/CD scanning** — GitLab CI scanner and GitHub Actions workflow scanning added (v4.12–v4.16)
- **Official Docker image** on GHCR (v4.5.0)
- **JS/JSX support** and PHP foundation (v4.6.0)
- **Deep Mode audit** — foundation added (v4.16.x)
- **Framework-aware** — 98% recall with reduced false positives vs traditional tools
- **MCP server** — exposes all scans to AI agents via dedicated `/skylos_mcp` module

700+ commits, 19 forks. Unlike Vulture (dead code only) or Bandit (security only), Skylos combines both with a hybrid AST + optional LLM engine. Privacy-first — core analysis runs locally without cloud uploads.

### kuberstar/qartez-mcp (Semantic Code Intelligence)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [qartez-mcp](https://github.com/kuberstar/qartez-mcp) | 50 | Rust | Dual | Multiple |

**Semantic code intelligence server designed for AI agents** — builds knowledge graphs for code analysis, now with a local web dashboard:

- **37 languages** supported
- **Knowledge graph indexing** — symbols, imports, and call edges
- **Impact analysis** — blast radius of file changes
- **Code complexity** — cyclomatic complexity and PageRank scoring
- **Modification guard** — prevents AI from editing critical files blindly
- **`qartez dashboard`** — new in v0.9.8: local web UI via axum HTTP server + SvelteKit frontend with live filesystem event updates
- **Cross-process file locking + workspace fingerprinting** — fast startup (v0.9.7)
- **macOS watcher fix** — reduced per-save latency for large repos (v0.9.10)
- **~92% token savings** vs grep/read workflows

Active through v0.9.10 (May 2026). The dashboard subcommand is a notable new capability — moves code intelligence from CLI-only to an interactive browser UI. Supports 19 editors including Claude Code, Cursor, and Zed.

## JavaScript / TypeScript

### ESLint MCP (Official, Built-in)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [@eslint/mcp](https://eslint.org/docs/latest/use/mcp) | Part of ESLint (27,300) | JavaScript | MIT | Linting + fixing |

**ESLint includes native MCP server support** via @eslint/mcp, now at **v0.3.5** — no separate installation needed:

```
npx @eslint/mcp@latest
```

- Uses your **existing ESLint configuration** — zero additional setup
- **Lint files** and get detailed error/warning reports
- **Auto-fix** violations where possible
- Works with **VS Code** (GitHub Copilot agent mode), **Cursor**, and **Windsurf**
- Stdio transport

v0.3.5 (May 1, 2026) updated the ESLint dependency to 10.3.0 — maintenance release. The simplest code quality MCP integration available — if you already use ESLint, you already have an MCP server.

### RyuzakiShinji/biome-mcp-server (Unofficial)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [biome-mcp-server](https://github.com/RyuzakiShinji/biome-mcp-server) | 5 | TypeScript | MIT | 2 |

**Unofficial Biome MCP server** with two tools:

- **`biome-lint`** — analyze JS/TS files and return diagnostics (errors, warnings, suggestions)
- **`biome-format`** — auto-format code per Biome rules

The [official Biome MCP server RFC](https://github.com/biomejs/biome/discussions/6017) has narrowed in scope: format/lint via MCP was deprioritized because editor integrations already handle those workflows. The refined direction is MCP **Resources** to expose Biome documentation and GritQL resources for AI agents writing plugins and configuration — no implementation timeline set. This unofficial server remains the only option for teams wanting Biome format/lint via MCP today.

### ncalteen/prettier-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [prettier-mcp](https://github.com/ncalteen/prettier-mcp) | 1 | TypeScript | MIT | Formatting |

**Prettier formatting via MCP** — check and format code files using Prettier. Stdio-based server with configurable settings via environment variables. Prettier itself has no official MCP server.

## Python

### Anselmoo/mcp-server-analyzer (Ruff + Vulture)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-analyzer](https://github.com/Anselmoo/mcp-server-analyzer) | 8 | Python | MIT | 5 |

**Combined Python analysis** with Ruff linting and Vulture dead code detection:

- **`ruff-check`** — lint Python code for style and error violations
- **`ruff-format`** — format code consistently
- **`ruff-check-ci`** — CI/CD-optimized output format
- **`vulture-scan`** — identify unused imports, functions, and variables
- **`analyze-code`** — combined assessment with 0-100 quality score

Docker support with multi-architecture containers and Sigstore supply chain signing. Now at v0.1.2 (April 2026).

### MarcusJellinghaus/mcp-code-checker (Pylint + Pytest + Mypy)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-code-checker](https://github.com/MarcusJellinghaus/mcp-code-checker) | 17 | Python | — | 5+ |

**Growing Python quality toolbox** — expanded from 3 to 5+ tools this cycle:

- **`run_pylint_check`** — code quality analysis with customizable parameters
- **`run_pytest_check`** — test execution with parallel processing support
- **`run_mypy_check`** — static type checking with strict mode
- **`run_tach_check`** — dependency boundary and layer enforcement (added v0.1.9)
- **`lint-imports`** — structured import linting output (added v0.1.10)

Includes LLM-friendly prompt generation for structured analysis output. Active through v0.1.10 (May 2026). Works with Claude Desktop, VS Code with Copilot, and other MCP clients.

### drewsonne/ruff-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ruff-mcp-server](https://github.com/drewsonne/ruff-mcp-server) | 1 | Python | MIT | 3 |

**Focused Ruff integration** with three tools:

- **`ruff_check`** — lint with detailed violation reports
- **`ruff_format`** — format or check formatting compliance
- **`ruff_fix`** — auto-fix violations where possible

Supports multiple output formats: JSON, text, GitHub, GitLab, JUnit, and SARIF.

## Rust

### lh/rust-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rust-mcp-server](https://github.com/lh/rust-mcp-server) | 1 | Rust | MIT | 5 |

**Full Rust toolchain via MCP:**

- **`cargo_check`** — syntax and type validation
- **`cargo_clippy`** — lint with improvement suggestions
- **`rustfmt`** — format according to Rust style guidelines
- **`cargo_test`** — run tests with detailed output
- **`cargo_build`** — build in debug or release mode

Designed for Claude Code and VS Code environments.

## .NET

### ndepend/NDepend.MCP.Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [NDepend.MCP.Server](https://github.com/ndepend/NDepend.MCP.Server) | 37 | C# | NDepend | 14 |

**Privacy-first .NET static analysis** — fills the .NET code quality gap:

- **14 tools** covering initialization, analysis, metrics, dependencies, issues, rules, quality gates, source code inspection, and code querying
- **On-premises analysis** — code never leaves your machine
- **Structured intelligence** — provides AI with reliable data instead of raw file dumps
- **Custom code queries and rules** — natural language interaction with code data
- **Dependency tracking** — SVG diagrams of code dependencies
- **Issues from multiple sources** — NDepend rules, Roslyn Analyzers, and ReSharper Code Inspections

Requires .NET 10.0+ and NDepend 2026.1.3+. Works with GitHub Copilot and VS Code. The first dedicated .NET code quality MCP server with production backing.

## Enterprise / Multi-Tool

### wadew/sonar-mcp (Community SonarQube)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sonar-mcp](https://github.com/wadew/sonar-mcp) | 1 | Python | MIT | 21 |

**Feature-rich community SonarQube MCP server** with more capabilities than the official one:

- **21 tools** across 7 categories — instance management, project operations, issue tracking, quality gates, metrics, rules, tasks
- **6 MCP prompts** — code_review, fix_issues, quality_report, quality_goals, security_audit, vulnerability_fix
- **7 MCP resources** — browseable URI-based access to SonarQube data
- **Multi-instance support** — connect to multiple SonarQube servers
- **Three transport modes** — stdio, SSE, streamable HTTP

More feature-rich than the official server, but lacks SonarSource's long-term maintenance commitment.

## What's missing

The gaps are closing but some remain:

- **No official Prettier MCP server** — the most popular code formatter still has no official MCP integration
- **No Biome format/lint MCP server** — the official RFC narrowed scope to Resources-only (docs/GritQL); format and lint via MCP is explicitly deprioritized
- **No Stylelint MCP server** with traction
- **No golangci-lint MCP** — Go's standard multi-linter has no dedicated MCP integration (fpt/go-dev-mcp covers Go documentation but not golangci-lint)
- **No Checkstyle or SpotBugs MCP** — Java linting gaps persist
- **No PHPStan or PHP_CodeSniffer MCP** — PHP quality tools absent
- **No unified multi-linter server** — nothing runs ESLint + Prettier + Stylelint in one pass

## Bottom line

**Rating: 4/5** *(held)* — The category continued maturing this cycle. SonarQube settled at 556 stars and v1.18.1 after a strong development run. Skylos was the standout — surging from v4.3 to v4.16.2 in one cycle, adding Docker, GitLab CI and GitHub Actions scanning, Dart, and Deep Mode audit, making it the most actively developed server in the category. CodeQL added a SQLite backend, 14 new opt-in tools, and Rust support. mcp-code-checker expanded to 5+ tools with tach and lint-imports. The Biome RFC narrowed scope away from format/lint, closing that door for now.

The category is stable at the enterprise end and actively expanding at the mid-tier. The main remaining gaps are official MCP servers from Prettier and golangci-lint.

**Recommendations:** For enterprise code quality, SonarQube's official server (556 stars) is the clear leader. For security scanning, Semgrep's built-in MCP integration is the most seamless. For dead code and SAST with active development, Skylos (439 stars, v4.16.2) is the most comprehensive. For cross-language diagnostics, the LSP bridge approach (mcp-language-server or lsp-mcp) gives you coverage across all LSP-supported languages. For JavaScript/TypeScript, ESLint's built-in MCP (v0.3.5) requires zero setup. For .NET, NDepend is the first dedicated option. For CodeQL query development, the official server is now at v2.25.4 with SQLite-backed caching.

*This review was last refreshed on 2026-05-21 using Claude Sonnet 4.6 (Anthropic).*
