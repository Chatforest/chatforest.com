---
title: "Code Quality, Linting & Static Analysis MCP Servers — ESLint, SonarQube, Semgrep, Ruff, Biome, and More"
date: 2026-03-17T01:00:00+09:00
description: "Code quality, linting, and static analysis MCP servers let AI agents run linters, formatters, and security scanners through the Model Context Protocol. We reviewed 15+ servers across 6 subcategories. Official tools: ESLint MCP (@eslint/mcp — built into ESLint, linting + fixing via stdio), SonarQube MCP (SonarSource/sonarqube-mcp-server, 424 stars, Java, official — project metrics, issues, security hotspots, code snippet analysis). Security analysis: semgrep/mcp (639 stars, Python — 5,000+ security rules, archived Oct 2025 — moved to main Semgrep repo), advanced-security/codeql-development-mcp-server (8 stars, TypeScript — CodeQL query development across 9 languages). Python linting: Anselmoo/mcp-server-analyzer (5 stars, Python, MIT — Ruff linting + Vulture dead code + quality scoring), MarcusJellinghaus/mcp-code-checker (14 stars, Python — pylint + pytest + mypy), drewsonne/ruff-mcp-server (1 star, Python, MIT — Ruff check/format/fix). JavaScript/TypeScript: RyuzakiShinji/biome-mcp-server (4 stars, TypeScript, MIT — Biome linting + formatting), ncalteen/prettier-mcp (1 star, TypeScript, MIT — Prettier formatting). Language-specific: lh/rust-mcp-server (1 star, Rust, MIT — cargo check/clippy/rustfmt/test/build). Cross-language: isaacphi/mcp-language-server (1,500 stars, Go, BSD-3-Clause — LSP bridge exposing diagnostics/definitions/references for any language server). Gaps: no official Prettier or Biome MCP servers, no golangci-lint or Checkstyle MCP, limited auto-fix capabilities, no CI/CD integration, no code coverage reporting. 15+ servers across 6 subcategories. Rating: 3.5/5."
og_description: "Code quality & linting MCP servers: mcp-language-server (1,500 stars — LSP bridge for any language), Semgrep MCP (639 stars — 5,000+ security rules), SonarQube MCP (424 stars — official, project metrics + issues). ESLint has built-in MCP support. 15+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Code quality, linting, and static analysis MCP servers for AI-powered code review, formatting, and security scanning across Python, JavaScript, TypeScript, Rust, and more. **The cross-language bridge** — isaacphi/mcp-language-server (1,500 stars, Go, BSD-3-Clause) connects any Language Server Protocol (LSP) server to MCP clients, exposing diagnostics, definitions, references, hover docs, and rename across Go (gopls), Rust (rust-analyzer), Python (pyright), TypeScript, and C/C++ (clangd). This is the most versatile code quality MCP server — instead of building language-specific MCP tools, it leverages the mature LSP ecosystem that editors have used for years. Currently in beta with active development. **Official SonarQube integration** — SonarSource/sonarqube-mcp-server (424 stars, Java, official) connects AI agents to SonarQube Server or Cloud. Retrieve project quality metrics, filter issues by severity, analyze security hotspots, and scan code snippets directly within agent context. Supports Claude, GitHub Copilot, VS Code, Cursor, and Zed. The official backing means long-term maintenance and compatibility with SonarQube's rule database covering 20+ languages. **Security-first analysis** — semgrep/mcp (639 stars, Python) brought Semgrep's 5,000+ security rules to MCP clients with tools for vulnerability scanning, AST generation, and platform-hosted findings retrieval. Supports stdio, SSE, and Streamable HTTP transports. Note: the repository was archived October 2025 and development moved to the main Semgrep repository — check there for the current MCP integration. **ESLint's built-in MCP** — ESLint v9.26.0+ includes native MCP server support via @eslint/mcp. Run `npx @eslint/mcp@latest` to start a stdio server that exposes linting and auto-fixing to AI assistants. Uses your existing ESLint configuration with zero additional setup. Works with VS Code (GitHub Copilot agent mode), Cursor, and Windsurf. No separate repository — it's part of ESLint itself (27,200 stars). **CodeQL query development** — advanced-security/codeql-development-mcp-server (8 stars, TypeScript, GitHub CodeQL Terms) wraps CodeQL CLI commands for AI-assisted query development. Supports 9 languages (Python, JavaScript, Java, C/C++, C#, Go, Ruby, Swift, GitHub Actions). Includes AI-optimized prompts and integrated testing. Designed for security researchers writing custom CodeQL queries, not general code scanning. **Python code analysis** — Anselmoo/mcp-server-analyzer (5 stars, Python, MIT) combines Ruff linting with Vulture dead code detection and a 0-100 quality scoring system. Five tools: ruff-check, ruff-format, ruff-check-ci (CI-optimized output), vulture-scan, and analyze-code (combined assessment). Docker support with multi-architecture containers and Sigstore signing. MarcusJellinghaus/mcp-code-checker (14 stars, Python) adds pylint, pytest, and mypy type checking with LLM-friendly prompt generation. drewsonne/ruff-mcp-server (1 star, Python, MIT) provides focused Ruff integration with check, format, and auto-fix tools supporting JSON, SARIF, and GitHub/GitLab output formats. **JavaScript/TypeScript tooling** — RyuzakiShinji/biome-mcp-server (4 stars, TypeScript, MIT) is an unofficial Biome MCP server with lint and format tools. An official Biome MCP server has been proposed (biomejs/biome discussion #6017) but not yet shipped. ncalteen/prettier-mcp (1 star, TypeScript, MIT) wraps Prettier formatting in an MCP server. Neither Prettier nor Biome has official MCP support yet. **Rust development** — lh/rust-mcp-server (1 star, Rust, MIT) provides cargo check, clippy, rustfmt, cargo test, and cargo build through MCP. Designed for Claude Code and VS Code integration. **Community SonarQube alternative** — wadew/sonar-mcp (0 stars, Python, MIT) offers 21 SonarQube tools across 7 categories, 6 MCP prompts for code review workflows, and 7 URI-based resources. Multi-instance support and three transport modes. More feature-rich than the official server but without SonarSource backing. **Gaps remain significant** — no official MCP servers from Prettier, Biome, or Stylelint. No golangci-lint, Checkstyle, or PHPStan MCP servers. Limited auto-fix capabilities beyond ESLint and Ruff. No CI/CD pipeline integration (running linters as part of a build). No code coverage reporting or test coverage analysis tools. No unified multi-linter server that runs ESLint + Prettier + Stylelint in one pass. Most servers are early-stage with minimal stars and single maintainers. The category earns 3.5/5 — the fundamentals are here with ESLint's official support, SonarQube's enterprise backing, and the mcp-language-server's elegant LSP bridge. But the ecosystem is fragmented across many tiny projects, most formatters lack official MCP support, and auto-fix capabilities are limited compared to what these tools offer natively. The mcp-language-server approach — bridging existing LSP infrastructure rather than building new MCP-native tools — may be the long-term winner."
last_refreshed: 2026-03-17
---

Code quality tools are among the most-used developer utilities — ESLint, Prettier, Ruff, SonarQube, and Semgrep run in virtually every professional codebase. Exposing them through MCP lets AI agents not just write code, but validate it against the same standards your team enforces.

This review covers **linters, formatters, and static analysis tools** available as MCP servers. For security-specific scanning, see our [Code Security review](/reviews/code-security-mcp-servers/). For testing frameworks, see [Testing & QA](/reviews/testing-qa-mcp-servers/).

Part of our **[Developer Tools MCP category](/categories/developer-tools/)**. The headline finding: **the most practical code quality MCP server isn't a linter at all** — it's mcp-language-server (1,500 stars), which bridges the Language Server Protocol to MCP, giving AI agents access to diagnostics, definitions, and references from any language server. Meanwhile, ESLint has built-in MCP support, SonarQube ships an official server, but most other tools (Prettier, Biome, Stylelint) still lack official MCP integration.

## Cross-Language

### isaacphi/mcp-language-server (LSP Bridge)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-language-server](https://github.com/isaacphi/mcp-language-server) | 1,500 | Go | BSD-3-Clause | 6 |

**The most versatile code quality MCP server** — instead of wrapping individual linters, this bridges any Language Server Protocol server to MCP clients:

- **`diagnostics`** — file-level warnings and errors from your language server (the same ones your editor shows)
- **`definition`** — jump to symbol source code
- **`references`** — find all usages of a symbol
- **`hover`** — documentation and type information
- **`rename_symbol`** — project-wide renaming
- **`edit_file`** — multi-line text edits

Supports Go (gopls), Rust (rust-analyzer), Python (pyright), TypeScript, and C/C++ (clangd). Currently in beta. The approach is pragmatic: rather than rebuilding linting logic for MCP, leverage the LSP ecosystem that editors have relied on for years.

## Static Analysis & Security

### SonarSource/sonarqube-mcp-server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) | 424 | Java | SonarSource | Multiple |

**Official SonarQube MCP server** connecting AI agents to SonarQube Server or Cloud:

- **Project quality metrics** — retrieve code quality dashboards programmatically
- **Issue management** — filter by severity, type, status across 20+ languages
- **Security hotspots** — identify and triage security-sensitive code
- **Code snippet analysis** — scan code directly within agent context without a full project build
- **Broad IDE support** — Claude, GitHub Copilot, VS Code, Cursor, Zed

The official backing ensures compatibility with SonarQube's extensive rule database (Java, Kotlin, Python, JavaScript, TypeScript, Go, PHP, C#, and more). Integrated with Docker MCP Toolkit for easy setup.

### semgrep/mcp (Archived → Main Repo)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [semgrep/mcp](https://github.com/semgrep/mcp) | 639 | Python | — | 6 |

**Semgrep's MCP server** exposed 5,000+ security rules to AI agents:

- **`security_check`** — vulnerability scanning with Semgrep's rule database
- **`semgrep_scan`** — code analysis with custom configurations
- **`get_abstract_syntax_tree`** — AST generation for code understanding
- **`semgrep_findings`** — retrieve findings from the Semgrep AppSec Platform
- **`supported_languages`** — language capability reference
- **`semgrep_rule_schema`** — JSON schema for custom rule development

Supports stdio, SSE, and Streamable HTTP transports. **Note:** This repository was archived October 2025 — development moved to the main Semgrep repository. Check there for the current MCP integration.

### advanced-security/codeql-development-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [codeql-development-mcp-server](https://github.com/advanced-security/codeql-development-mcp-server) | 8 | TypeScript | GitHub CodeQL Terms | Multiple |

**CodeQL query development for AI agents** — wraps CodeQL CLI commands for query compilation, execution, testing, and database operations:

- **9 languages** — Python, JavaScript, Java, C/C++, C#, Go, Ruby, Swift, GitHub Actions
- **AI-optimized prompts** guiding assistants through CodeQL development workflows
- **Test-driven validation** for query accuracy
- **Stdio and HTTP transports**

This is for security researchers writing custom CodeQL queries, not general-purpose code scanning. Requires CodeQL CLI installation and GitHub CodeQL license agreement.

## JavaScript / TypeScript

### ESLint MCP (Official, Built-in)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [@eslint/mcp](https://eslint.org/docs/latest/use/mcp) | Part of ESLint (27,200) | JavaScript | MIT | Linting + fixing |

**ESLint v9.26.0+ includes native MCP server support** — no separate installation needed:

```
npx @eslint/mcp@latest
```

- Uses your **existing ESLint configuration** — zero additional setup
- **Lint files** and get detailed error/warning reports
- **Auto-fix** violations where possible
- Works with **VS Code** (GitHub Copilot agent mode), **Cursor**, and **Windsurf**
- Stdio transport

The simplest code quality MCP integration available — if you already use ESLint, you already have an MCP server.

### RyuzakiShinji/biome-mcp-server (Unofficial)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [biome-mcp-server](https://github.com/RyuzakiShinji/biome-mcp-server) | 4 | TypeScript | MIT | 2 |

**Unofficial Biome MCP server** with two tools:

- **`biome-lint`** — analyze JS/TS files and return diagnostics (errors, warnings, suggestions)
- **`biome-format`** — auto-format code per Biome rules

An [official Biome MCP server RFC](https://github.com/biomejs/biome/discussions/6017) exists but hasn't shipped yet. This fills the gap for teams using Biome today.

### ncalteen/prettier-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [prettier-mcp](https://github.com/ncalteen/prettier-mcp) | 1 | TypeScript | MIT | Formatting |

**Prettier formatting via MCP** — check and format code files using Prettier. Stdio-based server with configurable settings via environment variables. Prettier itself has no official MCP server.

## Python

### Anselmoo/mcp-server-analyzer (Ruff + Vulture)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-analyzer](https://github.com/Anselmoo/mcp-server-analyzer) | 5 | Python | MIT | 5 |

**Combined Python analysis** with Ruff linting and Vulture dead code detection:

- **`ruff-check`** — lint Python code for style and error violations
- **`ruff-format`** — format code consistently
- **`ruff-check-ci`** — CI/CD-optimized output format
- **`vulture-scan`** — identify unused imports, functions, and variables
- **`analyze-code`** — combined assessment with 0-100 quality score

Docker support with multi-architecture containers and Sigstore supply chain signing.

### MarcusJellinghaus/mcp-code-checker (Pylint + Pytest + Mypy)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-code-checker](https://github.com/MarcusJellinghaus/mcp-code-checker) | 14 | Python | — | 3 |

**Three Python quality tools in one server:**

- **`run_pylint_check`** — code quality analysis with customizable parameters
- **`run_pytest_check`** — test execution with parallel processing support
- **`run_mypy_check`** — static type checking with strict mode

Includes LLM-friendly prompt generation for structured analysis output. Works with Claude Desktop, VS Code with Copilot, and other MCP clients.

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

## Enterprise / Multi-Tool

### wadew/sonar-mcp (Community SonarQube)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sonar-mcp](https://github.com/wadew/sonar-mcp) | 0 | Python | MIT | 21 |

**Feature-rich community SonarQube MCP server** with more capabilities than the official one:

- **21 tools** across 7 categories — instance management, project operations, issue tracking, quality gates, metrics, rules, tasks
- **6 MCP prompts** — code_review, fix_issues, quality_report, quality_goals, security_audit, vulnerability_fix
- **7 MCP resources** — browseable URI-based access to SonarQube data
- **Multi-instance support** — connect to multiple SonarQube servers
- **Three transport modes** — stdio, SSE, streamable HTTP

More feature-rich than the official server, but lacks SonarSource's long-term maintenance commitment.

## What's missing

The gaps in this category are significant:

- **No official Prettier MCP server** — the most popular code formatter has no official MCP integration
- **No official Biome MCP server** — RFC exists (discussion #6017) but hasn't shipped
- **No Stylelint MCP server** with traction
- **No golangci-lint MCP** — Go's standard multi-linter has no MCP integration
- **No Checkstyle or SpotBugs MCP** — Java ecosystem gaps
- **No PHPStan or PHP_CodeSniffer MCP** — PHP quality tools absent
- **No unified multi-linter server** — nothing runs ESLint + Prettier + Stylelint in one pass
- **No CI/CD integration** — can't trigger linting as part of a build pipeline via MCP
- **No code coverage reporting** — no MCP servers for coverage analysis or test coverage trends
- **Most servers are very early-stage** — single maintainers, minimal stars, limited documentation

## Bottom line

**Rating: 3.5/5** — The fundamentals are here: ESLint has native MCP support, SonarQube ships an official server, Semgrep brought 5,000+ security rules, and the mcp-language-server elegantly bridges the entire LSP ecosystem. But the category is fragmented across many tiny projects, most formatters lack official MCP support, and auto-fix capabilities are limited compared to what these tools offer in native editor integrations.

The mcp-language-server approach — bridging existing LSP infrastructure rather than building new MCP-native tools — may prove to be the long-term winner. It already supports diagnostics from any language server, which covers linting for every language with an LSP implementation.

For Python teams, the combination of mcp-server-analyzer (Ruff + Vulture) and mcp-code-checker (pylint + mypy) provides reasonable coverage. For JavaScript/TypeScript, ESLint's built-in MCP is the clear starting point. For enterprise code quality, SonarQube's official server is the safest bet.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
