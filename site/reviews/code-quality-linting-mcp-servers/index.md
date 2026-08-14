# Code Quality, Linting & Static Analysis MCP Servers — ESLint, SonarQube, Semgrep, Ruff, Biome, and More

> Code quality, linting, and static analysis MCP servers let AI agents run linters, formatters, and security scanners through the Model Context Protocol.


Code quality tools are among the most-used developer utilities — ESLint, Prettier, Ruff, SonarQube, and Semgrep run in virtually every professional codebase. Exposing them through MCP lets AI agents not just write code, but validate it against the same standards your team enforces.

This review covers **linters, formatters, and static analysis tools** available as MCP servers. For security-specific scanning, see our [Code Security review](/reviews/code-security-mcp-servers/). For testing frameworks, see [Testing & QA](/reviews/testing-qa-mcp-servers/).

Part of our **[Developer Tools MCP category](/categories/developer-tools/)**. The headline finding: **enterprise code quality platforms are maturing** — SonarQube has been shipping monthly releases (now at [v1.24.0](https://github.com/SonarSource/sonarqube-mcp-server/releases), 623 stars), Skylos surged past v4.16 with Docker, GitLab CI scanning, GitHub Actions workflow scanning, and Dart language support and has kept growing since (now [v4.33.2](https://github.com/duriantaco/skylos/releases)), and CodeQL added a SQLite backend with new opt-in tools. The LSP bridge servers continue accumulating stars despite dormant code, confirming the approach's long-term value.

## Cross-Language

### isaacphi/mcp-language-server (LSP Bridge)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-language-server](https://github.com/isaacphi/mcp-language-server) | 1,577 | Go | BSD-3-Clause | 6 |

**The most versatile code quality MCP server** — instead of wrapping individual linters, this bridges any Language Server Protocol server to MCP clients:

- **`diagnostics`** — file-level warnings and errors from your language server (the same ones your editor shows)
- **`definition`** — jump to symbol source code
- **`references`** — find all usages of a symbol
- **`hover`** — documentation and type information
- **`rename_symbol`** — project-wide renaming
- **`edit_file`** — multi-line text edits

Supports Go (gopls), Rust (rust-analyzer), Python (pyright), TypeScript, and C/C++ (clangd). Currently in beta at [v0.1.1](https://github.com/isaacphi/mcp-language-server/releases/tag/v0.1.1) with 143 forks. No new [tagged releases](https://github.com/isaacphi/mcp-language-server/tags) since v0.1.1 (May 2025) and no commits since March 2026 — growing organically on star count alone. The approach is pragmatic: rather than rebuilding linting logic for MCP, leverage the LSP ecosystem that editors have relied on for years.

### jonrad/lsp-mcp (Second LSP Bridge)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lsp-mcp](https://github.com/jonrad/lsp-mcp) | 191 | TypeScript | MIT | Multiple |

**Second LSP-to-MCP bridge** — validates the LSP bridge approach with a TypeScript implementation:

- **Multiple LSPs simultaneously** — run several language servers at once
- **Dynamic schema generation** from LSP JSON Schema
- **Supports Claude Desktop, Cursor, and MCP CLI Client**
- **POC state** — functional but still early

29 forks. [Dormant since March 2025](https://github.com/jonrad/lsp-mcp) — but still accumulating stars. The existence of a second LSP bridge implementation with 191 stars confirms that bridging existing LSP infrastructure is a viable long-term strategy for code quality MCP.

## Static Analysis & Security

### SonarSource/sonarqube-mcp-server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) | 623 | Java | SonarSource | Multiple |

**Official SonarQube MCP server** connecting AI agents to SonarQube Server or Cloud — actively maintained with [monthly releases](https://github.com/SonarSource/sonarqube-mcp-server/releases):

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

Now at 94 forks. [v1.18.1](https://github.com/SonarSource/sonarqube-mcp-server/releases/tag/v1.18.1.2664) shipped May 20, 2026 (a sandboxed-container startup-crash fix), and SonarSource has kept shipping since — [v1.19.0 through v1.24.0](https://github.com/SonarSource/sonarqube-mcp-server/releases) followed through early August 2026, adding automatic project-key resolution, branch-support fixes, an MCP Java SDK 2.0.0 upgrade, agentic-readiness assessment tools, and Cloud-organization auto-detection. *(Correction, 2026-08-14 audit: an earlier version of this review said SonarQube had "settled" at v1.18.1 with no new releases since — that was only true for the ~3 weeks immediately after v1.18.1 shipped; six more releases followed through August.)* The config generator, workspace mounting, and CAG features described above shipped across this same active-release run rather than in one isolated cycle.

### Semgrep MCP (Built into Semgrep Binary)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [semgrep/mcp](https://github.com/semgrep/mcp) (archived) | 683 | Python | — | 6+ |

**Semgrep's MCP server is now built directly into the main semgrep binary** — the standalone repo (683 stars) was [archived October 28, 2025](https://github.com/semgrep/mcp), with the [`semgrep mcp` subcommand introduced in v1.141.0 (October 23, 2025)](https://github.com/semgrep/semgrep/blob/develop/CHANGELOG.md):

- **Plugin bundles MCP + Hooks + Skills** — single install gives AI agents Semgrep Code, Supply Chain, and Secrets scanning
- **Scans every file an agent generates** — integrated with Claude Code, Cursor, Windsurf, and Codex
- **DNS rebinding protection** — [added in v1.146.0, December 17, 2025](https://github.com/semgrep/semgrep/blob/develop/CHANGELOG.md)
- **SSE transport dropped** — [deprecated in v1.148.0, January 14, 2026](https://github.com/semgrep/semgrep/blob/develop/CHANGELOG.md), Streamable HTTP only
- **OAuth required for Streamable HTTP** — [added in v1.150.0, January 29, 2026](https://github.com/semgrep/semgrep/blob/develop/CHANGELOG.md)
- **Custom rules from Semgrep Registry** — Hooks for Claude Code and Cursor pull rules automatically
- **Hosted endpoint** — available at mcp.semgrep.ai

The move from standalone repo to built-in integration signals maturity — Semgrep treats MCP as a core distribution channel, not an add-on. *(Correction, 2026-08-14 audit: an earlier version of this review dated the SSE deprecation to "April 2026" and the DNS-rebinding protection to "February 2026" — Semgrep's own changelog puts them at January 14, 2026 and December 17, 2025 respectively, both earlier than previously stated.)*

### advanced-security/codeql-development-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [codeql-development-mcp-server](https://github.com/advanced-security/codeql-development-mcp-server) | 31 | TypeScript | GitHub CodeQL Terms | Multiple |

**CodeQL query development for AI agents** — grew from 20 to 31 stars over this review's tracking period, now at [v2.26.2](https://github.com/advanced-security/codeql-development-mcp-server/releases) with active releases:

- **9 languages** — Python, JavaScript, Java, C/C++, C#, Go, Ruby, Swift, GitHub Actions; **Rust added in v2.25.2**
- **SQLite backend** — [new in v2.25.2](https://github.com/advanced-security/codeql-development-mcp-server/releases) with additional opt-in tools (annotation, audit, query result caching)
- **Models-as-Data (MaD) Extensions** — [v2.25.4 added auto-infer](https://github.com/advanced-security/codeql-development-mcp-server/releases) `codeql_query_run` format from `@kind` for result caching
- **AI-optimized prompts** guiding assistants through CodeQL development workflows
- **Test-driven validation** for query accuracy
- **Supply chain hardening** — [Node.js security patches and invalid JSON Schema fix in v2.25.3](https://github.com/advanced-security/codeql-development-mcp-server/releases)
- **Stdio and HTTP transports**
- **Active development** — maintained by GitHub's CodeQL Expert Services team, with further releases (through v2.26.2) since the SQLite/MaD work above shipped

This is for security researchers writing custom CodeQL queries, not general-purpose code scanning. Requires CodeQL CLI installation and GitHub CodeQL license agreement.

### codacy/codacy-mcp-server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [codacy-mcp-server](https://github.com/codacy/codacy-mcp-server) | 62 | TypeScript | MIT | 8 categories |

**Official Codacy MCP server** — first enterprise code quality platform with comprehensive MCP coverage. Its [README](https://github.com/codacy/codacy-mcp-server) groups tools into 8 categories rather than publishing a single tool count:

- **SAST, SCA, DAST, secrets, IaC, CI/CD** — full security analysis spectrum
- **Code quality analysis** — filter by severity, category, language, and author
- **File-level metrics** — issues, coverage, and duplication detection
- **Pull request evaluation** — diff coverage and issue detection
- **Quality gates** — automated pass/fail criteria
- **Local CLI analysis** — run analysis without cloud upload
- **[Codacy Guardrails](https://blog.codacy.com/codacy-guardrails-free-real-time-enforcement-of-security-and-quality-standards)** — real-time enforcement scanning AI-generated code as it's written, catching non-compliant code inside the IDE (Cursor, Windsurf, GitHub Copilot, JetBrains) before it's accepted

23 forks. Integrates with VS Code (Copilot), Cursor, and Windsurf. The Guardrails feature is a differentiator — it catches quality issues in AI-generated code before commit. *(Correction, 2026-08-14 audit: an earlier version cited "25+ tools" and "143 commits" — we could not independently verify either number against the current README or a commit-history source, so both are removed; the tool-category breakdown above is what the README itself documents.)*

### duriantaco/skylos (Dead Code + SAST)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [skylos](https://github.com/duriantaco/skylos) | 537 | Python | Apache 2.0 | Multiple |

**The most actively developed code quality MCP server we track** — surged from v4.3 to v4.16.2 in one earlier review cycle and has kept shipping since, reaching [v4.33.2 as of August 9, 2026](https://github.com/duriantaco/skylos/releases), expanding from dead code + SAST into a broader multi-language security and architecture audit platform:

- **Dead code detection** — unused functions, classes, imports with framework awareness (Django, FastAPI, Flask)
- **Security analysis** — SQL injection, XSS, SSRF, path traversal across Python, TypeScript/JavaScript, Java, Go, PHP, Rust; **Dart added in May 2026**, still current in the [README](https://github.com/duriantaco/skylos)
- **Secrets detection** — hardcoded credentials and high-entropy strings
- **AI code guardrails** — catches phantom security calls, missing decorators, unfinished stubs, and disabled controls from AI-generated code
- **CI/CD scanning** — [GitLab CI scanner and GitHub Actions workflow scanning](https://github.com/duriantaco/skylos), still current, added v4.12–v4.16
- **Official Docker image** on GHCR ([`ghcr.io/duriantaco/skylos`](https://github.com/duriantaco/skylos))
- **JS/JSX support** and PHP foundation (v4.6.0)
- **MCP server** — exposes all scans to AI agents via dedicated `/skylos_mcp` module

29 forks. Unlike Vulture (dead code only) or Bandit (security only), Skylos combines both with a hybrid AST + optional LLM engine. Privacy-first — core analysis runs locally without cloud uploads. *(Correction, 2026-08-14 audit: an earlier version of this review claimed "98% recall with reduced false positives vs traditional tools" — we could not find this figure in the project's [README](https://github.com/duriantaco/skylos) or [BENCHMARK.md](https://github.com/duriantaco/skylos/blob/main/BENCHMARK.md), which reports per-language recall on labeled regression suites instead and explicitly cautions against using those numbers as an unqualified marketing claim. We removed the "98%" figure. We also removed a "Deep Mode audit" bullet we could not verify still exists as a current, named feature.)*

### kuberstar/qartez-mcp (Semantic Code Intelligence)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [qartez-mcp](https://github.com/kuberstar/qartez-mcp) | 67 | Rust | Dual | Multiple |

**Semantic code intelligence server designed for AI agents** — builds knowledge graphs for code analysis, now with a local web dashboard:

- **[37 languages](https://github.com/kuberstar/qartez-mcp)** supported (tree-sitter parsing with regex fallbacks)
- **Knowledge graph indexing** — symbols, imports, and call edges
- **Impact analysis** — blast radius of file changes
- **Code complexity** — cyclomatic complexity and PageRank scoring
- **Modification guard** — prevents AI from editing critical files blindly
- **`qartez dashboard`** — new in v0.9.8: local web UI via axum HTTP server + SvelteKit frontend with live filesystem event updates
- **Cross-process file locking + workspace fingerprinting** — fast startup (v0.9.7)
- **macOS watcher fix** — reduced per-save latency for large repos (v0.9.10)
- **[+91.8% aggregate token savings](https://github.com/kuberstar/qartez-mcp)** vs a Glob + Grep + Read + git log baseline, per the project's own benchmark

Active through [v0.11.0 (July 3, 2026)](https://github.com/kuberstar/qartez-mcp/releases), which added cross-file dependency graphs for Kustomize/Helm/ArgoCD/Terraform and a `qartez_path` shortest-path tool. The dashboard subcommand (v0.9.8) moved code intelligence from CLI-only to an interactive browser UI. Supports [19 editors](https://github.com/kuberstar/qartez-mcp) including Claude Code, Cursor, and Zed.

## JavaScript / TypeScript

### ESLint MCP (Official, Built-in)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [@eslint/mcp](https://eslint.org/docs/latest/use/mcp) | Part of ESLint (27,300) | JavaScript | MIT | Linting + fixing |

**ESLint includes native MCP server support** via @eslint/mcp, now at [v0.3.10](https://www.npmjs.com/package/@eslint/mcp?activeTab=versions) — no separate installation needed:

```
npx @eslint/mcp@latest
```

- Uses your **existing ESLint configuration** — zero additional setup
- **Lint files** and get detailed error/warning reports
- **Auto-fix** violations where possible
- Works with **VS Code** (GitHub Copilot agent mode), **Cursor**, and **Windsurf**
- Stdio transport

[v0.3.5 (May 1, 2026)](https://www.npmjs.com/package/@eslint/mcp?activeTab=versions) updated the ESLint peer dependency to 10.3.0; five more maintenance releases have followed roughly every two weeks since, reaching [v0.3.10 (July 27, 2026)](https://www.npmjs.com/package/@eslint/mcp?activeTab=versions) with an ESLint 10.8.0 dependency. The simplest code quality MCP integration available — if you already use ESLint, you already have an MCP server.

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
| [mcp-server-analyzer](https://github.com/Anselmoo/mcp-server-analyzer) | 11 | Python | MIT | 8 |

**Python analysis with Ruff and Vulture, now expanded to JS/TS via Biome:**

- **`ruff-check`** — lint Python code for style and error violations
- **`ruff-format`** — format code consistently
- **`ruff-check-ci`** — CI/CD-optimized output format
- **`ty-check`** — type checking with `ty`
- **`vulture-scan`** — identify unused imports, functions, and variables
- **[`biome-check` / `biome-format`](https://github.com/Anselmoo/mcp-server-analyzer)** — JavaScript/TypeScript linting and formatting, added since our last check
- **`analyze-code`** — combined assessment with 0-100 quality score

Docker support with multi-architecture containers and Sigstore supply chain signing. Now at [v0.3.0 (July 1, 2026)](https://github.com/Anselmoo/mcp-server-analyzer/releases), up from v0.1.2 — the Biome addition took this from a Python-only tool to covering JS/TS as well.

### MarcusJellinghaus/mcp-tools-py (Pylint + Pytest + Mypy)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-tools-py](https://github.com/MarcusJellinghaus/mcp-tools-py) | 18 | Python | — | 5+ |

**Growing Python quality toolbox** — expanded from 3 to 5+ tools this cycle:

- **`run_pylint_check`** — code quality analysis with customizable parameters
- **`run_pytest_check`** — test execution with parallel processing support
- **`run_mypy_check`** — static type checking with strict mode
- **`run_tach_check`** — dependency boundary and layer enforcement ([added v0.1.9, April 27, 2026](https://github.com/MarcusJellinghaus/mcp-tools-py/releases))
- **`lint-imports`** — structured import linting output ([added v0.1.10, May 6, 2026](https://github.com/MarcusJellinghaus/mcp-tools-py/releases))

Includes LLM-friendly prompt generation for structured analysis output. Active through v0.1.10 (May 2026). Works with Claude Desktop, VS Code with Copilot, and other MCP clients. *(Correction, 2026-08-14 audit: this repo was previously named `mcp-code-checker`; the maintainer has renamed it to `mcp-tools-py`. The old URL redirects; we've updated the name and link above.)*

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
| [NDepend.MCP.Server](https://github.com/ndepend/NDepend.MCP.Server) | 41 | C# | NDepend | 14 |

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
- **No golangci-lint MCP** — Go's standard multi-linter has no dedicated MCP integration ([fpt/go-dev-mcp](https://github.com/fpt/go-dev-mcp) covers Go/Rust/Python documentation search and code navigation, not golangci-lint)
- **No Checkstyle or SpotBugs MCP** — Java linting gaps persist
- **No PHPStan or PHP_CodeSniffer MCP** — PHP quality tools absent
- **No unified multi-linter server** — nothing runs ESLint + Prettier + Stylelint in one pass

## Bottom line

**Rating: 4/5** *(held)* — The category continued maturing this cycle. SonarQube has been in continuous active development, shipping monthly through [v1.24.0](https://github.com/SonarSource/sonarqube-mcp-server/releases) (623 stars). Skylos was the standout — surging from v4.3 to v4.16.2 in one earlier cycle and continuing to [v4.33.2](https://github.com/duriantaco/skylos/releases) since, adding Docker, GitLab CI and GitHub Actions scanning, and Dart, making it the most actively developed server in the category. CodeQL added a SQLite backend and Rust support, now at [v2.26.2](https://github.com/advanced-security/codeql-development-mcp-server/releases). mcp-tools-py (renamed from mcp-code-checker) expanded to 5+ tools with tach and lint-imports. The Biome RFC narrowed scope away from format/lint, closing that door for now.

The category is stable at the enterprise end and actively expanding at the mid-tier. The main remaining gaps are official MCP servers from Prettier and golangci-lint.

**Recommendations:** For enterprise code quality, SonarQube's official server (623 stars) is the clear leader. For security scanning, Semgrep's built-in MCP integration is the most seamless. For dead code and SAST with active development, Skylos (537 stars, v4.33.2) is the most comprehensive. For cross-language diagnostics, the LSP bridge approach (mcp-language-server or lsp-mcp) gives you coverage across all LSP-supported languages. For JavaScript/TypeScript, ESLint's built-in MCP (v0.3.10) requires zero setup. For .NET, NDepend is the first dedicated option. For CodeQL query development, the official server is now at v2.26.2 with SQLite-backed caching.

*This review was originally written using Claude Sonnet 4.6 (Anthropic) and last refreshed with a full citation re-audit on 2026-08-14.*

