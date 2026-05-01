# Package Management MCP Servers — NuGet, npm, PyPI, Maven, and the Quest for AI-Assisted Dependency Intelligence

> Package management MCP servers: NuGet official v1.4.1 (2.5M downloads, transitive vuln remediation), Socket MCP (101 stars, supply chain security npm/PyPI/Cargo), mcp-package-version ARCHIVED March 2026


**At a glance:** Package management MCP servers are where **the gap between ecosystem importance and MCP investment is widest** — and the gap just got wider. The former community leader [mcp-package-version](https://github.com/sammcj/mcp-package-version) (121 stars, Go, 9 registries) was **ARCHIVED on March 29, 2026**, with its maintainer migrating to a consolidated mcp-devtools server. [Microsoft's NuGet MCP server](https://learn.microsoft.com/en-us/nuget/concepts/nuget-mcp-server) remains the clear standout — now at **v1.4.1 with 2.5 million downloads** and new transitive dependency vulnerability remediation. The biggest new entry is [Socket MCP](https://github.com/SocketDev/socket-mcp) (101 stars), which brings **supply chain security scoring** for npm, PyPI, and Cargo with a free public hosted server at mcp.socket.dev. The **Rust/Cargo gap is now closed** by [cratesio-mcp](https://github.com/joshrotenberg/cratesio-mcp) (23 tools, MIT/Apache-2.0). [maven-tools-mcp](https://github.com/arvindand/maven-tools-mcp) grew to 23 stars with v2.1.0 adding **private repository authentication**. [Homebrew](https://docs.brew.sh/MCP-Server) expanded with development commands and progress reporting. This is the **twelfth review in our [Developer Tools MCP category](/categories/developer-tools/)**.

The package management market is substantial: the private package repository market alone hit $1.05B in 2025 (projected $3.96B by 2035, 14.2% CAGR), while the broader package management solutions market is valued at $8.2B. npm leads with 25.3% market share by package type, with 5+ billion weekly downloads. PyPI served 421.6 billion downloads in 2025. Maven Central handles 828+ billion Java component requests annually. Yet MCP adoption is minimal — the most-starred package management MCP server has just 122 stars. The core problem: package registries already have excellent CLIs (`npm`, `pip`, `mvn`, `cargo`, `dotnet`), established IDE integrations, and mature ecosystems. MCP servers add AI-assisted intelligence — vulnerability scanning, version recommendations, dependency conflict resolution — but these capabilities are incremental rather than transformative.

**Architecture note:** Package management MCP servers follow three patterns. **Version checkers** (mcp-package-version, dependency-mcp) query multiple registries for latest versions, helping AI agents recommend current dependencies during code generation. **Deep registry analyzers** (npm-sentinel-mcp, pypi-query-mcp-server) focus on a single ecosystem with security scanning, trend analysis, and dependency trees. **Platform-integrated servers** (NuGet MCP, Homebrew MCP) ship directly with the package manager or IDE, providing tight integration without external setup. Most are community-built and read-only; NuGet is the exception with actual package modification capabilities (update, fix vulnerabilities).

## What's Available

### NuGet MCP Server — Microsoft's First-Party IDE Integration

| Aspect | Detail |
|--------|--------|
| Documentation | [Microsoft Learn](https://learn.microsoft.com/en-us/nuget/concepts/nuget-mcp-server) |
| Package | [NuGet.Mcp.Server](https://www.nuget.org/packages/NuGet.Mcp.Server/) |
| Version | v1.4.1 (April 30, 2026) |
| Downloads | 2.5 million |
| Language | C# (.NET) |
| Creator | Microsoft / NuGet team (official) |
| IDE support | Visual Studio 2026 (built-in), VS 2022 17.14+, VS Code, GitHub Copilot Agent |

**Key capabilities:**

| Capability | Detail |
|-----------|--------|
| Vulnerability fixing | Analyzes dependencies and transitive dependencies, suggests updates for known CVEs |
| Transitive vuln remediation | **NEW in v1.4.1** — scans and remediates vulnerabilities in transitive dependency chains |
| Version management | Update all packages to latest compatible versions |
| Targeted updates | Update specific package to specific version |
| Compatibility checking | Respects target framework(s) when suggesting updates |
| GitHub Copilot Agent | Configurable as MCP server in Copilot coding agent workflows |

**Key differentiator:** The **only package registry MCP server with first-party IDE integration** — and now with **2.5 million downloads**, the most widely deployed package management MCP server by orders of magnitude. NuGet MCP is built into Visual Studio 2026, requires zero setup, and goes beyond read-only registry lookups with genuine write capabilities (vulnerability fixing, version updates). The v1.4.1 release (April 30, 2026) added **transitive dependency vulnerability remediation** — scanning and fixing vulnerabilities not just in direct dependencies but across the entire dependency chain. The GitHub Copilot Agent integration means it works in CI/CD contexts too.

**Limitation:** .NET ecosystem only — no npm, PyPI, or Maven support. Requires .NET 10 SDK. No dependency tree visualization or conflict resolution. No security advisory aggregation beyond what NuGet already provides. Star count not publicly visible (ships as a NuGet package, not a standalone GitHub repo).

### Homebrew MCP Server — Built-in Package Manager Integration

| Aspect | Detail |
|--------|--------|
| Documentation | [docs.brew.sh/MCP-Server](https://docs.brew.sh/MCP-Server) |
| Command | `brew mcp-server` |
| Creator | Homebrew (official) |
| Transport | stdio |

**Tools:** `brew search`, `brew install`, `brew uninstall`, `brew upgrade` — exposed as MCP tools for AI assistants. For Homebrew contributors, development commands (`brew style`, `brew typecheck`, `brew tests`) are also available.

**Key differentiator:** The **simplest MCP server setup of any package manager** — it ships with Homebrew itself. Run `brew mcp-server` and it's available. No installation, no configuration, no API keys. Works with Cursor, Claude Desktop, VS Code, Claude Code, and Zed out of the box. Recent updates added **progress reporting for long-running operations** (keeps MCP clients from timing out during installs) and **development commands** for Homebrew contributors.

**Limitation:** macOS/Linux only. Core user-facing tools remain limited to four operations (search, install, uninstall, upgrade). No `brew info`, `brew deps`, `brew doctor`, `brew outdated`, cask management, or tap operations for end users. Community alternative [jeannier/homebrew-mcp](https://github.com/jeannier/homebrew-mcp) offers broader command coverage including info, outdated, deps, and cleanup.

### mcp-package-version — Multi-Registry Version Checker (ARCHIVED)

| Aspect | Detail |
|--------|--------|
| Repository | [sammcj/mcp-package-version](https://github.com/sammcj/mcp-package-version) |
| Stars | ~121 |
| Forks | ~22 |
| Language | Go |
| License | MIT |
| Creator | Community (sammcj) |
| Status | **ARCHIVED March 29, 2026** — read-only, migrating to mcp-devtools |

**Supported registries:**

| Registry | Ecosystem |
|----------|-----------|
| npm | JavaScript/Node.js |
| PyPI | Python |
| Maven Central | Java/JVM |
| Go Proxy | Go modules |
| Swift Packages | Swift/Apple |
| Docker Hub | Container images |
| GitHub Container Registry | Container images |
| AWS Bedrock | AI models |
| GitHub Actions | CI/CD actions |

**Key differentiator:** Was the **most-starred and broadest package management MCP server** — 9 registries in a single Go binary. Docker Hub, GitHub Container Registry, AWS Bedrock models, and GitHub Actions version support. Docker tag queries support regex filtering. Constraint-based filtering enables version range recommendations. Dual transport (stdio + SSE) and Docker deployment support.

**⚠️ ARCHIVED:** The repository was **archived on March 29, 2026** and is now read-only. The maintainer is migrating functionality to a consolidated `mcp-devtools` server. Users should consider alternatives: [Artmann/package-registry-mcp](https://github.com/Artmann/package-registry-mcp) for multi-registry search, or [niradler/dependency-mcp](https://github.com/niradler/dependency-mcp) for cross-registry version checking. The archival of the category's most-adopted server highlights the fragility of community-maintained MCP tooling.

### npm-sentinel-mcp — Deep npm Analysis

| Aspect | Detail |
|--------|--------|
| Repository | [Nekzus/npm-sentinel-mcp](https://github.com/Nekzus/npm-sentinel-mcp) |
| Stars | ~18 |
| Forks | ~8 |
| Language | TypeScript |
| Creator | Community |

**18+ tools:**

| Tool | Capability |
|------|-----------|
| npmVulnerabilities | Security scanning with CVE identification |
| npmDeps | Dependency tree analysis via deps.dev |
| npmSize | Bundle size and import cost analysis |
| npmTrends | Download statistics over customizable periods |
| npmCompare | Multi-package comparative metrics |
| npmScore | Package quality scoring |
| npmLicenseCompatibility | License analysis and compatibility checking |
| npmMaintenance | Maintainer activity assessment |
| npmAlternatives | Alternative package suggestions |
| npmQuality | Comprehensive quality metrics |
| npmSearch | Package discovery |
| npmVersions | Complete version history |
| npmTypes | TypeScript support verification |
| npmLatest | Latest version lookup |
| npmMaintainers | Maintainer information |
| npmPackageReadme | README content retrieval |
| npmRepoStats | Repository statistics |
| npmDeprecated | Deprecation status checking |
| npmChangelogAnalysis | Changelog analysis |

**Key differentiator:** The **deepest single-registry MCP server** in the package management space. 18+ specialized tools cover security (CVE scanning), quality (scoring, maintenance activity), economics (bundle size, download trends), legal (license compatibility), and discovery (alternatives, comparisons). The vulnerability scanning with CVE identification goes beyond simple `npm audit` — it provides recursive dependency checks. Bundle size analysis helps AI agents recommend lightweight alternatives. License compatibility checking prevents legal issues in dependency selection.

**Limitation:** npm-only — no cross-ecosystem coverage. Low adoption (18 stars). No write operations (can't install, update, or remove packages). Relies on external services (deps.dev, npm registry) that may rate-limit. The breadth of 18+ tools risks context window bloat — AI agents loading all tools consume significant token budget even before making a query.

### PyPI Query MCP Server — Python Package Intelligence

| Aspect | Detail |
|--------|--------|
| Repository | [loonghao/pypi-query-mcp-server](https://github.com/loonghao/pypi-query-mcp-server) |
| Stars | ~18 |
| Forks | ~5 |
| Language | Python |
| Creator | Community |

**25+ tools** covering package metadata, version tracking, Python version compatibility, recursive dependency resolution, download statistics, package downloading with dependency collection, top packages ranking and trends, and structured prompt templates for quality analysis, security auditing, migration planning, and comparison.

**Key differentiator:** The **most comprehensive Python package MCP server** — 25+ tools with prompt templates for decision-making. Private PyPI repository support and multi-mirror configuration make it enterprise-ready. Recursive dependency resolution with transitive analysis goes deeper than `pip show`. Download statistics and popularity metrics help AI agents recommend well-maintained packages.

**Limitation:** Python-only. Low adoption (18 stars). The 25+ tools and prompt templates risk overwhelming the context window. No vulnerability database integration (relies on PyPI's own advisory data). Package downloading capability raises security concerns — an AI agent downloading arbitrary packages could introduce supply chain risks.

### Maven Tools MCP — JVM Dependency Intelligence

| Aspect | Detail |
|--------|--------|
| Repository | [arvindand/maven-tools-mcp](https://github.com/arvindand/maven-tools-mcp) |
| Stars | ~23 |
| Forks | ~5 |
| Version | v2.1.0 (April 5, 2026) |
| Language | Java |
| License | MIT |
| Creator | Community |

**Tools:** Latest version detection with stability filtering, version existence verification, bulk dependency lookups, upgrade comparison analysis, dependency age assessment, release pattern evaluation, version timeline inspection, project health auditing, plus Context7 documentation integration.

**Supported build tools:** Maven, Gradle, SBT, Mill — any JVM project using Maven Central.

**Key differentiator:** The **only JVM-focused MCP server** with multi-build-tool support. Works with Maven, Gradle, SBT, and Mill equally — it queries Maven Central regardless of which build tool manages the project. The "agent-driven dependency maintenance" capability uses its own weekly self-update workflow as a demo: AI evaluates and proposes safe dependency updates via pull requests. Context7 documentation integration bridges version intelligence with library documentation.

**Limitation:** ~~Maven Central only~~ **v2.1.0 added private repository authentication**, enabling enterprise teams to query internal Nexus/Artifactory servers. Still no Gradle Plugin Portal or JitPack support. Modest adoption (23 stars). Java-based, which is unusual for MCP servers. No vulnerability scanning against CVE databases.

### Socket MCP — Supply Chain Security Scoring (NEW)

| Aspect | Detail |
|--------|--------|
| Repository | [SocketDev/socket-mcp](https://github.com/SocketDev/socket-mcp) |
| Stars | ~101 |
| Forks | ~17 |
| Language | TypeScript |
| License | MIT |
| Creator | Socket (official) |
| Public server | [mcp.socket.dev](https://mcp.socket.dev/) — no setup required |

**Key capabilities:**

| Capability | Detail |
|-----------|--------|
| Dependency scoring | Multi-dimensional security scores (supply chain, quality, maintenance, vulnerability, license) |
| Batch processing | Multiple dependencies in a single request |
| Ecosystem coverage | npm, PyPI, Cargo, and additional registries via Socket API |
| Hosted service | Free public server at mcp.socket.dev — no API key needed |
| Transport | stdio, HTTP, and hosted remote |

**Key differentiator:** The **most adopted security-focused package MCP server** — 101 stars and a free public hosted server that requires zero setup. Socket's `depscore` tool provides comprehensive supply chain security scoring that goes far beyond vulnerability databases, covering data exfiltration risk, maintainer patterns, quality signals, and license compliance. The batch processing capability is practical for auditing entire dependency trees. Works with Claude, VS Code Copilot, Cursor, and other MCP clients out of the box. This is the server you'd use to answer "should I trust this dependency?" before adding it to your project.

**Limitation:** Read-only security scoring — can't install, update, or remove packages. The depscore tool is the primary interface, so the tool surface is narrow compared to deep analyzers like npm-sentinel-mcp. Requires network access to Socket API. Early development stage (the project notes it's "rapidly evolving"). No lockfile analysis or build tool integration.

### cratesio-mcp — Rust/Cargo Package Intelligence (NEW, Gap Closure)

| Aspect | Detail |
|--------|--------|
| Repository | [joshrotenberg/cratesio-mcp](https://github.com/joshrotenberg/cratesio-mcp) |
| Stars | ~5 |
| Forks | ~4 |
| Version | 0.1.4 (March 19, 2026) |
| Language | Rust |
| License | MIT / Apache-2.0 |
| Creator | Community |
| Public server | [cratesio-mcp.fly.dev](https://cratesio-mcp.fly.dev/) |

**23 tools** covering crate search, version history, documentation retrieval, dependency analysis, vulnerability auditing, and download statistics. Also provides 4 resources for quick metadata access and 2 prompts for guided crate analysis.

**Key differentiator:** The **first dedicated crates.io MCP server**, closing the Rust/Cargo gap identified in the original review. 23 tools is a comprehensive surface area — more than npm-sentinel-mcp (18 tools) and approaching pypi-query-mcp-server territory. The dual MIT/Apache-2.0 license follows Rust ecosystem conventions. Hosted instance on Fly.dev means zero-setup access. Supports both stdio and HTTP/SSE transport.

**Limitation:** Very low adoption (5 stars). Version 0.1.4 suggests early maturity. Focused on crates.io querying rather than Cargo build operations (for that, see [cargo-mcp](https://crates.io/crates/cargo-mcp) which wraps cargo build/test/add/remove commands). No dependency conflict resolution or lockfile awareness.

### Multi-Registry and Other Servers

**[Artmann/package-registry-mcp](https://github.com/Artmann/package-registry-mcp)** (36 stars, TypeScript, MIT) — Cross-registry search and information for npm, Cargo, PyPi, NuGet, and Go. 15+ tools including search, metadata, version history, and GitHub Security Advisory integration. The security advisory integration is unique — provides vulnerability data alongside package information.

**[niradler/dependency-mcp](https://github.com/niradler/dependency-mcp)** (TypeScript) — Version checking across 7 registries (npm, PyPI, Maven, NuGet, RubyGems, Crates.io, Go). Six tools with batch processing (up to 100 packages in parallel). Focused on version lookup rather than deep analysis.

**[pinkpixel-dev/npm-helper-mcp](https://github.com/pinkpixel-dev/npm-helper-mcp)** (8 stars, TypeScript, MIT) — npm-focused with dependency upgrade management, conflict resolution, and peer dependency handling. The `upgradePackages` tool with peer dependency awareness is practical for real-world npm projects.

**[loonghao/pypi-query-mcp-server](https://github.com/loonghao/pypi-query-mcp-server)** (see above) and **[jackkuo666/pypi-mcp-server](https://pypi.org/project/mcp-pypi/)** — Python package intelligence servers with varying depth.

**[Bigsy/maven-mcp-server](https://github.com/Bigsy/maven-mcp-server)** — Lightweight Maven dependency version checker. Simpler than maven-tools-mcp but focused on the core use case.

**[qianniuspace/mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit)** (~47 stars) — npm security audit server with real-time vulnerability scanning. Provides severity levels, fix recommendations, CVSS scores, and CVE references. Supports npm, pnpm, and yarn. The **most-starred npm-specific security audit MCP server**.

**[meanands/npm-package-docs-mcp](https://github.com/meanands/npm-package-docs-mcp)** — Fetches latest README documentation for npm packages from GitHub or npm. Useful for keeping AI agents informed about current API surfaces.

**[snyk-labs/mcp-server-npm-goof](https://github.com/snyk-labs/mcp-server-npm-goof)** — Snyk Labs npm package management MCP server. Demonstrates Snyk's approach to npm dependency intelligence.

**[oshvartz/nuget-packages-mcp-server](https://github.com/oshvartz/nuget-packages-mcp-server)** — **NEW.** Community NuGet MCP server with flexible feed support (any NuGet v3 compatible feed, not just nuget.org). Unique features: API contract extraction generates markdown documentation of public interfaces from packages, and dependency analysis shows version requirements per target framework. Fills the private NuGet feed gap that the official server doesn't address.

**[dmclain/uv-mcp](https://github.com/dmclain/uv-mcp)** — **NEW.** Python environment introspection via the [uv](https://github.com/astral-sh/uv) package manager. Gives AI agents direct access to inspect and manage Python environments — dependency management, environment inspection, and troubleshooting. Relevant as uv replaces pip/poetry/pyenv for many Python developers.

**[cargo-mcp](https://crates.io/crates/cargo-mcp)** — **NEW.** Cargo operations MCP server for Rust projects. Wraps cargo commands (check, clippy, test, fmt, build, bench, add, remove, update, clean, run) with environment variable and toolchain configuration. Complements cratesio-mcp's registry querying with actual build operations.

### Notable Gaps

**Gaps closed since original review:**
- **Cargo/crates.io** — now served by cratesio-mcp (23 tools) and cargo-mcp (build operations)
- **Private Maven repositories** — maven-tools-mcp v2.1.0 added private repository authentication
- **Private NuGet feeds** — oshvartz/nuget-packages-mcp-server supports any NuGet v3 feed
- **uv (Python)** — uv-mcp provides environment introspection via the fast Rust-based package manager

**Still missing:** RubyGems (standalone), Composer/Packagist (PHP), CocoaPods (iOS), pub.dev (Dart/Flutter), Conda/conda-forge (data science), Hex (Elixir), or CPAN (Perl). Private registry platforms (JFrog Artifactory, Sonatype Nexus, GitHub Packages, GitLab Package Registry, AWS CodeArtifact) have no dedicated MCP servers beyond NuGet feed support. System package managers beyond Homebrew (apt, yum/dnf, pacman, Chocolatey, winget, Scoop) lack MCP servers.

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging | Profiling | Code Review |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|----------|-----|----------|----------|----------|---------------------- | --------------|-----------|-----------|-------------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, 1.3k stars) | Yes (Jenkins, CircleCI, Buildkite) | Yes (JetBrains built-in, 24 tools) | Yes (MS Playwright, 9.8k stars, 24 tools) | Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana) | Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) | Yes (NuGet built-in VS 2026, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B 384, JetBrains built-in server) | Yes (Postman 192, Apollo GraphQL 275, Kong deprecated, Apigee, MuleSoft) | Yes (Splunk 13 tools GA, Grafana Tempo built-in, Grafana Loki 103 stars) | Partial (Liquibase private preview 19 tools, Prisma built-in CLI v6.6.0+) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector 9.2k official) | Partial (CodSpeed MCP, Polar Signals remote, Grafana Pyroscope via mcp-grafana) | Yes (SonarQube 442 stars, Codacy 56 stars, Graphite GT built-in) |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (1.4k stars, 20+ tools) | Argo CD (356 stars, 12 tools) | vscode-mcp-server (342 stars, 15 tools) | executeautomation (5.3k stars) | pab1it0/prometheus (340 stars) | CodeQL community (143 stars) | Ansible (25 stars, 40+ tools) | Socket MCP (101 stars, supply chain security), mcp-package-version (121 stars, ARCHIVED) | Context7 (50.3k stars), magic-mcp (4.5k stars) | openapi-mcp-generator (495 stars), mcp-graphql (374 stars) | cr7258/elasticsearch (259 stars), Traceloop OTel (178 stars) | mpreziuso/mcp-atlas (Atlas), defrex/drizzle-mcp (Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars), Docs MCP (87 stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars), devtools-debugger (341 stars) | theSharque/mcp-jperf (Java JFR), PageSpeed Insights MCP servers | kopfrechner/gitlab-mr-mcp (86 stars), crazyrabbitLTC (32 stars) |
| **Registry coverage** | 1 platform | 1 platform | 1 platform | Docker Hub + registries | N/A | Per CI platform | Per IDE | Per framework | Per vendor | Per scanner | Per IaC tool | Multi-registry (npm, PyPI, Maven, NuGet, Cargo, Go) | N/A (platforms, not registries) | N/A | N/A | — | N/A | N/A | N/A | N/A |
| **Vendor count** | 1 (GitHub) | 1 (GitLab) | 0 (Atlassian via Jira only) | 1 (Docker) + community | 0 (Red Hat leads community) | 3 (Jenkins, CircleCI, Buildkite) | 1 (JetBrains) | 1 (Microsoft) | 6 (Grafana, Datadog, Sentry, Dynatrace, New Relic, Instana) | 7+ (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | 5+ (HashiCorp, Pulumi, AWS, OpenTofu, Spacelift) | 2 (Microsoft/NuGet, Homebrew) | 3 (Vercel, E2B, Upstash/Context7) | 4+ (Postman, Apollo, Kong, Google/Apigee, MuleSoft) | 6+ (Splunk, Grafana/Loki, Grafana/Tempo, Coralogix, Axiom, Mezmo) | 2 (Liquibase, Prisma) + Google partial | 5+ (Microsoft, Mintlify, ReadMe, Stainless, OpenAI, Vonage, Fern, Apidog) | 3 (Google/Chrome DevTools, Microsoft/DebugMCP, LLVM/LLDB built-in) | 3 (CodSpeed, Polar Signals, Tricentis/NeoLoad) + Grafana partial | 3 (SonarSource, Codacy, Graphite) + CodeRabbit as client |
| **Vulnerability scanning** | Dependabot/secret scanning | SAST/DAST | N/A | Image scanning | N/A | N/A | N/A | N/A | N/A | Full SAST/SCA/Secrets | cfn-guard compliance | npm-sentinel-mcp (CVE), NuGet (fix vulns) | N/A | N/A | N/A | — | N/A | N/A | N/A | N/A |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | API tokens per platform | Local connection (port/stdio) | None (local browsers) | API tokens / OAuth (remote) | API tokens / CLI auth | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / CLI auth | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect | API keys (CodSpeed, Polar Signals) / Grafana auth / Google API key (PageSpeed) | API tokens (SonarQube, Codacy) / GitHub PAT / GitLab PAT |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | No | No (but Microsoft is Platinum) | No (but Microsoft is Platinum) | No | No | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) | No | No |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | 5.6M developers | Jenkins: 11.3M devs | VS Code: 75.9% market share | Playwright: 45.1% QA adoption | Datadog: 32.7k customers | SonarQube: 17.7% SAST mindshare | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads, PyPI: 421.6B yearly | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 30M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Prisma: 43k stars, Flyway: 10.7k stars, Atlas: 6.3k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars, ReadMe: powering major API docs | Chrome: 65%+ browser share, VS Code: 75.9% IDE share, x64dbg: 45k+ stars | APM market: $7-10B, Pyroscope: 11k+ stars, async-profiler: 9k+ stars | SonarQube: 7.4M+ users, CodeRabbit: top AI reviewer, Qodo/PR-Agent: 10.5k stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | [4/5](/reviews/kubernetes-mcp-servers/) | [3/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) | [3.5/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | 3/5 | [3.5/5](/reviews/code-generation-mcp-servers/) | [3.5/5](/reviews/api-development-mcp-servers/) | [3.5/5](/reviews/logging-tracing-mcp-servers/) | [2.5/5](/reviews/database-migration-mcp-servers/) | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | [4.5/5](/reviews/debugging-mcp-servers/) | [3/5](/reviews/profiling-performance-mcp-servers/) | [3.5/5](/reviews/code-review-pull-request-mcp-servers/) |

## Known Issues

1. **Almost no official servers from major registries — and the community leader just archived** — npm (GitHub/Microsoft), PyPI (Python Software Foundation), Maven Central (Sonatype), and RubyGems have no official MCP servers. Only NuGet (Microsoft) and Homebrew provide first-party MCP integration. The archival of mcp-package-version (March 29, 2026) — the most-starred community server — underscores the fragility: the category's best cross-registry tool is now read-only with no clear successor at equivalent adoption.

2. **Package installation via MCP is a supply chain risk** — MCP servers that can install packages (Homebrew) or download them (pypi-query-mcp-server) give AI agents the ability to modify the dependency tree. The 2025 npm supply chain attacks (compromising chalk, debug, and 16 other packages with 2.6B weekly downloads) demonstrate the risk. An AI agent installing a compromised package via MCP would bypass the human review that currently catches suspicious dependencies. Most servers wisely stick to read-only operations.

3. **Version checking is the ceiling for cross-registry servers** — mcp-package-version and dependency-mcp can tell you the latest version of a package, but they can't resolve dependency conflicts, check compatibility between packages, or analyze the full dependency tree. The most common developer need — "will upgrading package X break my project?" — requires build-tool-specific context that cross-registry checkers don't have.

4. **No private registry support in most servers** — Enterprise teams use JFrog Artifactory, Sonatype Nexus, GitHub Packages, GitLab Package Registry, or AWS CodeArtifact. Only pypi-query-mcp-server and NuGet MCP support private registries. Teams can't use community MCP servers to query their internal packages without modifying the servers to support authentication.

5. **Context window pressure from deep analyzers** — npm-sentinel-mcp exposes 18+ tools, pypi-query-mcp-server offers 25+ tools. Loading all tools into an AI agent's context consumes significant tokens before any query is made. Tools like `npmChangelogAnalysis` and `npmPackageReadme` return large text payloads that further compress available context. No server implements tool pagination or selective loading.

6. **Security advisory data is fragmented** — npm has the GitHub Advisory Database, PyPI has its own advisory system, NuGet has its vulnerability database, and Maven has OSV. Package management MCP servers query these independently with different formats, severity scales, and coverage. No server aggregates vulnerability data across registries for projects with mixed-language dependencies (e.g., a Python backend with an npm frontend).

7. **No lockfile analysis** — Developers manage dependencies through lockfiles (package-lock.json, poetry.lock, Cargo.lock, go.sum). No package management MCP server reads lockfiles to understand the actual resolved dependency tree. Without lockfile awareness, version recommendations may conflict with existing pinned versions.

8. **Homebrew MCP is too minimal** — Four tools (search, install, uninstall, upgrade) is a starting point, but misses `brew info`, `brew deps`, `brew doctor`, `brew outdated`, cask management, and tap operations. Developers using Homebrew through an AI agent can install packages but can't diagnose issues or explore the dependency graph.

9. **No build tool integration** — Package management MCP servers query registries, but they don't integrate with build tools (webpack, vite, gradle, cargo build). An AI agent can recommend upgrading a package but can't verify that the upgrade doesn't break the build. The gap between "latest version available" and "latest version that works in your project" remains unbridged.

10. **Missing ecosystems — Rust gap closed, but others persist** — The Rust/Cargo gap was closed by cratesio-mcp (23 tools) and cargo-mcp (build operations). But standalone MCP servers still don't exist for RubyGems, Composer (PHP), CocoaPods (iOS), pub.dev (Dart/Flutter), Conda (data science), Hex (Elixir), or CPAN (Perl). System package managers (apt, yum, pacman, Chocolatey, winget) are absent except Homebrew.

## Bottom Line

**Rating: 3 out of 5**

The package management MCP ecosystem remains **surprisingly thin given the centrality of dependency management to software development** — and the archival of mcp-package-version (the category's most-starred community server) in March 2026 makes the landscape even more fragile. Microsoft's NuGet MCP server continues to pull away from the pack: now at **v1.4.1 with 2.5 million downloads** and new transitive dependency vulnerability remediation, it's the model every other registry should follow. The biggest positive is [Socket MCP](https://github.com/SocketDev/socket-mcp) (101 stars) bringing supply chain security scoring with a free public hosted server — addressing one of the ecosystem's most critical gaps. The Rust/Cargo gap is now closed by cratesio-mcp (23 tools). maven-tools-mcp added private repository authentication (v2.1.0).

The **3/5 rating holds** despite mixed signals. Positives: NuGet's continued dominance (2.5M downloads), Socket MCP filling the security gap (101 stars), Rust/Cargo gap closed, private Maven repos now supported, Homebrew adding progress reporting and dev commands. Negatives: mcp-package-version archived (biggest community server is dead), near-total absence of official servers from npm/PyPI/Maven Central, version checking still the ceiling for most servers, missing ecosystems (Ruby, PHP, iOS, Dart, Elixir), and the fundamental challenge that existing CLIs handle most package management needs well.

**Who benefits from package management MCP servers today:**

- **.NET developers using Visual Studio 2026** — NuGet MCP is the gold standard: built-in, zero-setup, with vulnerability fixing and version management through Copilot Chat. This is the model every other registry should follow
- **Teams concerned about dependency security** — Socket MCP (101 stars) provides free, zero-setup supply chain security scoring at mcp.socket.dev, covering npm, PyPI, and Cargo with batch processing for full dependency audits
- **npm-heavy projects with security concerns** — npm-sentinel-mcp's 18+ tools provide deeper analysis than `npm audit`, including bundle size, license compatibility, and alternative package suggestions
- **macOS developers** — Homebrew's built-in MCP server adds zero friction for AI-assisted package installation and upgrades

**Who should wait:**

- **Enterprise teams with private registries** — Most servers only support public registries. Without Artifactory/Nexus/CodeArtifact support, these tools can't see your internal packages
- **Teams needing dependency resolution** — No server can answer "will this upgrade break my project?" They check versions but don't resolve conflicts or verify builds
- **Ruby, PHP, iOS, or Dart developers** — Your ecosystems still have no dedicated MCP servers. (Rust developers: see cratesio-mcp with 23 tools)
- **Teams concerned about supply chain security** — MCP servers that install packages give AI agents unreviewed dependency modification power. Until approval workflows exist, this is a risk

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of May 2026 (first refreshed from March 2026 original). See our [About page](/about/) for details on our review process.*

