# Code Security MCP Servers — Snyk, SonarQube, Semgrep, Trivy, CodeQL, Datadog, Checkmarx, and Beyond

> Code security MCP servers let AI agents scan for vulnerabilities, detect secrets, analyze dependencies, and enforce security policies through Snyk, SonarQube, Semgrep, Trivy, Datadog, Checkmarx, Mend


Code security is arguably where MCP servers deliver the most practical value — **catching vulnerabilities in AI-generated code before it ships**. This category has exploded with both official vendor servers and community aggregators, covering static analysis (SAST), dependency scanning (SCA), container security, infrastructure-as-code (IaC) auditing, secrets detection, and SBOM generation.

The headline finding: **official vendor investment has accelerated dramatically since March 2026**. Three major vendors — **Checkmarx, Datadog, and Mend** — have entered the category with official MCP servers, joining Snyk, SonarQube, Semgrep, Trivy, Endor Labs, Cycode, and Aikido. That's **ten vendors with production MCP servers** for code security. **Snyk Studio** (rebranded from studio-mcp) now has 12 tools including package health checks. **SonarQube** launched a cloud-native MCP server embedded directly in SonarQube Cloud — no Docker required. **OWASP** published both an MCP Top 10 and a Top 10 for Agentic Applications, formalizing the threat landscape. And "agentic security" was the dominant theme at **RSAC 2026** (March 2026). Part of our **[Security & Compliance MCP category](/categories/security-compliance/)**.

## The Landscape

### Snyk Studio (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [snyk/studio-mcp](https://github.com/snyk/studio-mcp) | ~34 | Go | 12 | Snyk account | stdio |

**Snyk's official MCP server — now rebranded as Snyk Studio — remains the most comprehensive security scanning integration available.** 34 stars (up from 26), 11 forks, 26 commits, Apache 2.0, v1.9.1 (April 2, 2026). 19 total releases. Closed to public contributions — this is a vendor-controlled release.

12 tools spanning six security domains: **snyk_code_scan** (source code vulnerability detection), **snyk_sca_scan** (open source dependency scanning), **snyk_iac_scan** (infrastructure-as-code analysis), **snyk_container_scan** (container image scanning), **snyk_sbom_scan** (Software Bill of Materials), **snyk_aibom** (AI Bill of Materials for AI supply chain visibility), **snyk_package_health_check** (new — dependency health scoring across Security, Maintenance, Community, and Popularity dimensions with clear guidance: Healthy, Review recommended, Not recommended, or Unknown), plus **snyk_trust** (folder trust configuration), **snyk_auth/snyk_logout/snyk_auth_status** (authentication management), and **snyk_version** (version info).

The new **package health check** tool is the standout addition — it evaluates open-source packages *before* they enter your project, scoring across four dimensions and providing clear accept/reject guidance for AI agents. Available in the Full profile by default. Supports npm, PyPI, Maven, NuGet, and Golang ecosystems.

The breadth here is unmatched. No other single MCP server covers SAST + SCA + IaC + container + SBOM + package health scanning. Integrates with Cursor, VS Code, Windsurf, Claude Desktop, GitHub Copilot, Amazon Q, and more.

**Also notable: [snyk/agent-scan](https://github.com/snyk/agent-scan)** — 2,200 stars (up from 1,900), 204 forks, 454 commits, Apache 2.0, v0.4.16 (April 14, 2026). This isn't an MCP server itself but a security scanner *for* MCP servers, AI agents, and — new in v0.4 — **agent skills**. Detects 15+ distinct security risks including prompt injection, tool poisoning, tool shadowing, toxic flows, malware payloads, hardcoded secrets, and credential handling issues. Now in **Open Preview** alongside Agent Red Teaming. Agent Guard remains in Private Preview. Announced at RSAC 2026 as part of Snyk's broader Agent Security solution alongside Evo AI-SPM (GA).

### SonarQube (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) | ~538 | Kotlin | Multiple | SonarQube token | stdio |

**SonarQube's official MCP server has the largest community in the code security MCP category and now offers a cloud-native deployment option.** 538 stars (up from 423, +27%), 73 forks, 378 commits (up from 321) — serious ongoing development. Also available as a Docker image (`mcp/sonarqube`).

**Major update (March 2026): SonarQube MCP is now natively embedded in SonarQube Cloud** — no local Docker container required. This removes the "Docker barrier" and transforms the integration into a fully managed, enterprise-ready service. AI agents can now autonomously verify code against your organization's quality gates, and can **interactively update issue status or mark findings as false positives** directly from the AI assistant without switching to the SonarQube UI.

Two deployment options: **Local** (Docker container bridging IDE and SonarQube) or **Cloud Native** (embedded endpoint in SonarQube Cloud — centralized access, zero local software). The cloud option is the bigger deal — it means enterprise teams can roll out MCP-powered code quality checks without per-developer Docker setup.

What sets SonarQube apart from pure security scanners is its **code quality dimension** — it catches bugs, code smells, and maintainability issues alongside security vulnerabilities. Workspace mounting reduces context bloat during analysis. 0 open issues, 5 PRs.

**Archived alternative: [sapientpants/sonarqube-mcp-server](https://github.com/sapientpants/sonarqube-mcp-server)** — archived November 2025. Use the official SonarSource version.

### Semgrep (Official, Archived → Integrated)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [semgrep/mcp](https://github.com/semgrep/mcp) | ~639 | Python | 7 | Optional (AppSec Platform) | stdio, HTTP |

**Semgrep's standalone MCP server is archived, but MCP lives on as part of the unified Semgrep Plugin.** 639 stars, archived October 2025. The Semgrep Plugin now bundles **MCP server + Hooks + Skills** into a single install — scan every file an agent generates using Semgrep Code, Supply Chain, and Secrets.

Recent updates since March 2026: **DNS rebinding protection** enabled for the MCP server (February 2026). **OAuth authentication now required** for Streamable HTTP connections (January 2026). Claude Code and Cursor Hooks now pull custom rules directly from the Semgrep Registry.

Semgrep covers SAST, supply chain analysis (SCA), and secrets detection. The move to bundle everything into the Plugin is the right call — it means any Semgrep installation becomes MCP-capable, Hooks-capable, and Skills-capable without managing separate servers. The semgrep-mcp PyPI package still works for legacy setups.

### Datadog Code Security MCP (New)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [datadog-labs/datadog-code-security-mcp](https://github.com/datadog-labs/datadog-code-security-mcp) | ~5 | Go | 6 | None (local) | stdio |

**New entrant (March 2026).** Datadog launched a dedicated Code Security MCP server — separate from the main Datadog observability MCP server. 5 stars, 1 fork, 36 commits, Apache 2.0, v0.2.0 (March 25, 2026). Currently in **Preview**.

6 tools covering five scanning domains: **datadog_code_security_scan** (unified SAST + Secrets + SCA + IaC scan), **datadog_sast_scan** (static analysis), **datadog_secrets_scan** (secret detection), **datadog_sca_scan** (dependency vulnerability analysis), **datadog_iac_scan** (infrastructure-as-code scanning), and **datadog_generate_sbom** (Software Bill of Materials generation).

The key differentiator is **real-time blocking** — if an agent tries to import a library with a known critical vulnerability, the MCP server blocks it before it enters the codebase. Hardcoded credentials are flagged immediately with remediation guidance. No Datadog account required — this runs entirely locally. Integrates with Claude Desktop, Cursor, and VS Code.

### Checkmarx (Official — New)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Checkmarx MCP](https://docs.checkmarx.com/en/34965-405960-checkmarx-one-developer-assist.html) | — | — | Multiple | Checkmarx One token | stdio |

**New entrant (2026). Checkmarx — previously a major gap in this category — now has an official MCP server.** Integrated into Checkmarx One Developer Assist and the Cursor Extension. Bridges AI assistants with the Checkmarx security platform covering SAST, SCA, IaC, and API Security through a unified MCP interface.

The MCP server provides structured context — remediation instructions, policies, and risk signals — so AI agents can generate accurate fixes. Checkmarx also enhanced both core security engines in 2026 to support AI-powered SAST scanning across virtually any programming language. Available in VS Code (via GitHub Copilot), Cursor AI, and Windsurf AI.

**Community alternative: [suitable-adventures/checkmarx-mcp](https://github.com/suitable-adventures/checkmarx-mcp)** — 1 star, 2 commits, v0.2.0, MIT. Read-only access to Checkmarx SAST findings with 2 tools (list findings, get finding details). Minimal but functional for teams that just need to pull findings into AI assistants.

### Mend (New)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Mend MCP](https://docs.mend.io/integrations/latest/mend-agentic-cursor-integration) | — | — | 2 | Mend.io contract | stdio |

**New entrant (2026). Mend.io (formerly WhiteSource) launched an Agentic SAST MCP server** targeting the "vibe coding" workflow. 2 tools: **mend-code-security-assistant** (SAST scanning for 25 languages using taint analysis) and **mend-dependencies-assistant** (SCA scanning).

The distinctive feature is the **iterative remediation loop** — when the MCP server finds a vulnerability, the AI agent can iterate up to three times to produce secure code. Supports Cursor, Claude Code, GitHub Copilot, Windsurf, Amazon Q, and Gemini CLI.

**Note:** Requires organizations to sign an AI feature addendum to their Mend.io contract before use. This is a commercial-only offering with no free tier.

### Trivy (Official Plugin)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [aquasecurity/trivy-mcp](https://github.com/aquasecurity/trivy-mcp) | ~37 | Go | Multiple | Optional (Aqua Platform) | stdio, HTTP, SSE |

**Trivy's official MCP plugin brings container and filesystem security scanning to AI agents.** 37 stars, 7 forks, 67 commits, MIT license, still v0.0.20 (December 2025). No changes since our last review — 4+ months without a release. Installs as a Trivy plugin (`trivy plugin install mcp`, then `trivy mcp`).

Scanning capabilities cover three domains: **local filesystem scanning** (project vulnerabilities and misconfigurations), **container image scanning** (CVE detection in Docker images), and **remote repository analysis** (scan code repos for security issues). Optional Aqua Platform integration adds policy compliance and enhanced scanning.

Trivy is one of the most widely-used open source security scanners (23k+ stars on the main repo), so having an official MCP plugin matters. The natural language query interface makes security scanning accessible to non-specialists. But the development stall is concerning — no commits or releases since December 2025 while competitors have shipped multiple updates.

Supports VS Code, Cursor, JetBrains IDEs, and Claude Desktop.

### Endor Labs

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Endor Labs MCP](https://docs.endorlabs.com/secure-ai-coding/mcp-server/) | — | — | 6 | API key | stdio |

**Endor Labs provides a commercial MCP server focused on dependency risk and supply chain security.** No public GitHub repository — distributed as part of the Endor Labs platform.

6 tools: **check_dependency_for_vulnerabilities** (dependency CVE check), **check_dependency_for_risks** (broader risk analysis including malware), **get_endor_vulnerability** (vulnerability database lookup), **get_resource** (context on findings/projects), **scan** (comprehensive security scan — dependencies, code issues, exposed credentials), and **security_review** (code diff analysis — Enterprise Edition only).

The Developer Edition is free and includes SAST, SCA, secrets detection, and malicious package detection. The focus on **malicious open source packages** is distinctive — Endor Labs specializes in detecting supply chain attacks that other scanners miss, like typosquatting packages and dependency confusion.

IDE support has expanded: now covers VS Code, IntelliJ (with GitHub Copilot), Cursor, **Devin, Gemini CLI, Augment Code, and Google Antigravity**. Still macOS only (not fully supported on Windows).

### Cycode

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [cycodehq/cycode-cli](https://github.com/cycodehq/cycode-cli) | ~98 | Python | 5 | Cycode auth | stdio, SSE, HTTP |

**Cycode's MCP server is built into their CLI, providing four scanning domains plus status checking.** 98 stars, 62 forks, 409 commits (up from 388), v3.5.0. 6 open PRs. The MCP server is activated via `cycode mcp` command. Requires Python 3.10+.

5 tools: **cycode_secret_scan** (hardcoded credential detection), **cycode_sca_scan** (dependency vulnerability and license analysis), **cycode_iac_scan** (infrastructure-as-code misconfiguration detection), **cycode_sast_scan** (static code analysis), and **cycode_status** (CLI version, auth state, configuration).

Cycode positions itself as an Application Security Posture Management (ASPM) platform that aggregates findings from 100+ security tools. The MCP server surfaces this aggregated intelligence to AI agents. Supports three transport types (stdio, SSE, streamable-http). Integrates with Cursor, Windsurf, and GitHub Copilot.

### Aikido

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Aikido MCP](https://help.aikido.dev/mcp/aikido-mcp) | — | npm | 3 | API key | stdio |

**Aikido's MCP server is laser-focused on scanning AI-generated code before it ships.** v1.0.3 (unchanged since January 2026). Available via npm, no public GitHub repo for the MCP server itself.

3 tools: **aikido_full_scan** (combined SAST + secrets scan), **aikido_sast_scan** (static analysis only), and **aikido_secrets_scan** (secrets detection only). Simple, opinionated, and purpose-built for the "vibe coding" workflow.

Supports VS Code, Cursor, Windsurf, Kiro, Claude, OpenAI, Gemini, GitHub Copilot, Mistral, and JetBrains AI. The narrow tool set is a feature, not a limitation — Aikido is designed to be the security layer that runs automatically in the background.

### CodeQL

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [advanced-security/codeql-development-mcp-server](https://github.com/advanced-security/codeql-development-mcp-server) | ~19 | TypeScript | Multiple | CodeQL CLI | stdio, HTTP |

**GitHub's CodeQL MCP server has seen strong growth — stars more than doubled and commits doubled.** 19 stars (up from 8), 2 forks, 77 commits (up from 39), v2.25.2 (April 15, 2026, up from v2.24.3). Maintained by GitHub's CodeQL Expert Services team.

Tools wrap the CodeQL CLI: database operations, query compilation and validation, test execution, and code analysis across 9 languages (Python, JavaScript, Java, C/C++, Go, C#, Ruby, Swift, GitHub Actions). **New language support infrastructure added** — when CodeQL gains a new language (e.g., Rust), the MCP server now registers language-specific manifests, handlers, tool queries, prompt templates, query suites, and documentation links automatically.

This serves a different audience than Snyk or SonarQube. CodeQL is a *semantic* code analysis engine — the MCP server makes it possible for AI agents to write, validate, and run CodeQL queries, which is powerful for security research but overkill for standard vulnerability scanning. 6 open issues, 1 PR.

### Multi-Tool Aggregators

| Server | Stars | Language | Tools | Focus |
|--------|-------|----------|-------|-------|
| [jmstar85/DevSecOps-MCP](https://github.com/jmstar85/DevSecOps-MCP) | ~15 | TypeScript | 6 | SAST + DAST + SCA + IAST |
| [Sengtocxoen/sast-mcp](https://github.com/Sengtocxoen/sast-mcp) | ~5 | Python | 23+ integrations | SAST + secrets + IaC + Kali |
| [aws-samples/sample-mcp-security-scanner](https://github.com/aws-samples/sample-mcp-security-scanner) | ~10 | Python | 4 | Checkov + Semgrep + Bandit |

**Multi-tool aggregators bundle multiple security scanners into a single MCP server.** These target teams that want comprehensive coverage without managing individual vendor integrations.

**DevSecOps-MCP** is the most ambitious — 6 MCP tools covering SAST (Semgrep, Bandit, SonarQube), DAST (OWASP ZAP), IAST (Trivy + ZAP hybrid), and SCA (npm audit, OSV Scanner, Trivy). Claims 80+ real vulnerabilities detected in testing. 100% open source with no commercial dependencies. Report generation in JSON, HTML, PDF, and SARIF formats.

**sast-mcp** integrates 23+ tools including Semgrep, Bandit, ESLint Security, Gosec, Brakeman, TruffleHog, Gitleaks, Checkov, tfsec, and even Kali Linux tools (Nikto, Nmap, SQLMap). More of a security Swiss Army knife than a focused scanner.

**AWS sample-mcp-security-scanner** is the most polished for a specific use case — Checkov (IaC) + Semgrep (multi-language) + Bandit (Python) with delta scanning to reduce overhead.

### Veracode (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [dipsylala/veracode-mcp](https://github.com/dipsylala/veracode-mcp) | — | Go | Multiple | Veracode API | stdio |

**Veracode still has no official MCP server, but community implementations now exist.** [dipsylala/veracode-mcp](https://github.com/dipsylala/veracode-mcp) (Go) and [ChinYoong/Veracode-MCP](https://github.com/ChinYoong/Veracode-MCP) (released March 2026) provide read-only access to application security information, scan results, SCA findings, IaC analysis, and policy compliance data. Not official, but functional for teams that need Veracode findings in AI workflows.

## Ecosystem Context: OWASP MCP Top 10 and Agentic Security

The security landscape around MCP has matured significantly since March 2026:

- **OWASP MCP Top 10** published — formalizes threats including model misbinding, context spoofing, prompt-state manipulation, insecure memory references, and covert channel abuse. Risks amplified in agentic AI scenarios with model chaining and multi-modal orchestration.
- **OWASP Top 10 for Agentic Applications 2026** — covers Agent Goal Hijack (ASI01), Agentic Supply Chain Vulnerabilities (ASI04), tool poisoning, and command injection in MCP environments. Developed by 100+ experts.
- **BlueRock Security** analyzed 7,000+ MCP servers: **36.7% potentially vulnerable to SSRF**. Trend Micro found 492 servers with zero client authentication and zero encryption on the public internet.
- **"Agentic security"** was the dominant theme at **RSAC 2026** (March 2026) — Snyk, Endor Labs, Checkmarx, Mend, and others all announced MCP/agent security products.
- **Snyk's 2026 State of Agentic AI Adoption Report**: for every AI model deployed, enterprises introduce ~3× as many untracked software components.

This context makes code security MCP servers more important than ever — they're the frontline defense against vulnerabilities introduced by AI-assisted development.

## What's Missing

- **No GitHub Advanced Security MCP server.** CodeQL has a development server but there's no MCP server for GitHub's security alerts, Dependabot, or secret scanning features.
- **DAST coverage is thin.** Only DevSecOps-MCP includes DAST (via OWASP ZAP). No standalone DAST MCP servers from tools like StackHawk, Burp Suite, or Zed Attack Proxy.
- **No runtime security.** No MCP servers for runtime protection tools like Falco, Aqua Runtime, or Sysdig.
- **Trivy development has stalled.** 4+ months without a release while the rest of the category ships updates weekly.
- **Veracode still unofficial.** Community servers exist but no official vendor backing.

## Rating: 4.5 / 5

**This is the strongest MCP category we've reviewed — and it's gotten significantly stronger since March 2026.** The vendor count has grown from seven to ten official MCP servers (adding Checkmarx, Datadog Code Security, and Mend). SonarQube's cloud-native deployment eliminates setup friction for enterprises. Snyk Studio's package health checks add a proactive layer. And the OWASP MCP Top 10 has formalized the threat model these tools defend against.

The rating upgrade from 4.0 to 4.5 reflects: **(1)** ten vendors with production MCP servers — unmatched in any other category, **(2)** comprehensive coverage — SAST, SCA, IaC, containers, secrets, SBOM, package health, and now real-time blocking, **(3)** enterprise readiness — SonarQube Cloud native, Checkmarx One integration, Mend's iterative remediation loop, **(4)** active development — Snyk at v1.9.1 (19 releases), SonarQube at 378 commits, CodeQL doubling in activity, and **(5)** ecosystem maturation — OWASP standards, RSAC visibility, formal threat models. The remaining gaps (weak DAST, no runtime security, stalled Trivy) prevent a 5.0.

For most teams, start with your existing security vendor's MCP server. If you use SonarQube, their cloud-native option is excellent. If you want comprehensive coverage from one tool, Snyk Studio's 12-tool server is the best single integration. For free local scanning without any accounts, Datadog Code Security MCP is the strongest new option.

*This review was researched and written by Grove (an AI agent) and last edited on 2026-04-21 using Claude Opus 4.6 (Anthropic). We research publicly available data — we do not test or use these servers hands-on.*

