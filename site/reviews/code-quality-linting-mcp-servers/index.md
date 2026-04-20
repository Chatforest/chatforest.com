# Code Quality, Linting & Static Analysis MCP Servers — ESLint, SonarQube, Semgrep, Ruff, Biome, and More

> Code quality, linting, and static analysis MCP servers let AI agents run linters, formatters, and security scanners through the Model Context Protocol.


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

