---
title: "Security Scanning MCP Servers — Enterprise Vendors Pile In as Agentic Security Goes Mainstream"
date: 2026-03-24T18:00:00+09:00
description: "Security scanning MCP servers surge: SonarQube surges 442→544 stars +23% with native cloud MCP, Snyk acquires Invariant Labs → Agent Scan 2.3k stars meta-security, StackHawk FIRST DAST MCP, Checkmarx enters with agentic platform, Black Duck Polaris MCP, Veracode community servers close enterprise gap. Rating upgraded 3.5→4/5."
og_description: "Security scanning MCP ecosystem: SonarQube surges to 544 stars +23% with cloud-native MCP, Snyk Agent Scan 2.3k stars, StackHawk FIRST DAST, Checkmarx enters. Rating: 4/5."
content_type: "Review"
card_description: "Security scanning MCP servers hit an inflection point. SonarQube surged 442→544 stars (+23%) and launched native cloud MCP — no Docker required. Snyk acquired Invariant Labs, rebranding MCP-Scan as Snyk Agent Scan (2.3k stars) — a meta-security tool scanning MCP servers themselves for 15+ risks. StackHawk became the FIRST DAST tool with MCP integration. Checkmarx entered with agentic security (Developer Assist, Policy Assist). Black Duck shipped Polaris Issue Management MCP. Veracode community servers closed a major enterprise gap. Contrast Security grew to 13 tools with SARIF output. Semgrep added OAuth auth and DNS rebinding protection. Trivy survived a supply chain attack. 7→10+ vendor official servers."
last_refreshed: 2026-05-01
---

**At a glance:** Security scanning MCP servers hit an inflection point in April 2026. **SonarQube surged 442→544 stars (+23%)** and launched a **native cloud MCP server** — no Docker required, fully managed endpoint. **Snyk acquired Invariant Labs** and rebranded MCP-Scan as **[Snyk Agent Scan](https://github.com/snyk/agent-scan) (2.3k stars)** — a meta-security tool that scans MCP servers themselves for 15+ risks including prompt injection and tool poisoning. **[StackHawk](https://github.com/stackhawk/stackhawk-mcp) became the FIRST DAST tool with MCP integration** (beta), closing a major gap. **Checkmarx entered** with an agentic security platform built on MCP. **Black Duck shipped** a Polaris Issue Management MCP server. **Veracode community servers** appeared, closing the enterprise vendor gap. [Semgrep](https://github.com/semgrep/mcp) (665 stars on the archived standalone repo) added OAuth authentication and DNS rebinding protection. [Contrast Security](https://github.com/Contrast-Security-OSS/mcp-contrast) grew to **13 tools with SARIF output** — the first security MCP server to use a standard finding format. This is the **tenth review in our [Developer Tools MCP category](/categories/developer-tools/)**. Also part of our **[Security & Compliance MCP category](/categories/security-compliance/)**.

The application security testing market ($13.6–15.6B in 2025, projected $36–55B by 2030) is driving vendor investment in "agentic security" — the idea that security scanning should happen **inside the AI coding loop**, not after code is committed. RSAC 2026 marked this as a turning point: Checkmarx, Black Duck, StackHawk, and Mend all announced MCP integrations alongside existing players Semgrep, Snyk, SonarQube, Cycode, and Contrast. The vendor count jumped from 7 to 10+. But the ecosystem is maturing unevenly — SonarQube's cloud-native MCP and Snyk Agent Scan's 2.3k stars represent real adoption, while the Trivy supply chain attack (March 2026, compromised v0.69.4) and Checkmarx GitHub breach remind the industry that security tools themselves remain attractive targets.

**Architecture note:** Security scanning MCP servers follow three patterns now. **CLI-integrated** servers (Semgrep, Snyk, Cycode) embed MCP directly into their existing CLI tools — you run `semgrep mcp` or `snyk mcp --experimental` and the CLI becomes an MCP server. **Standalone** servers (GitGuardian, Trivy, Contrast, StackHawk) are separate repos that connect to the vendor's platform via API. **Cloud-native** servers (SonarQube Cloud, Dynatrace-style) run the MCP endpoint inside the vendor's platform — no local installation at all. The cloud-native pattern is emerging for enterprise vendors because it eliminates Docker/JVM setup friction and centralizes access control. Most servers support stdio transport for IDE integration (Cursor, Claude Code, VS Code, Windsurf), with Semgrep now requiring OAuth for streamable HTTP (SSE transport dropped January 2026).

## What's Available

### Semgrep — SAST Leader Goes MCP-Native

| Aspect | Detail |
|--------|--------|
| Repository | [semgrep/mcp](https://github.com/semgrep/mcp) (archived — now built into `semgrep` binary) |
| Stars | ~665 *(was 641)* |
| Forks | ~56 |
| Language | Python |
| License | MIT |
| Creator | Semgrep (official) |
| Status | Archived standalone; MCP built into `semgrep/semgrep` CLI |

**7 tools** for comprehensive static analysis:

| Tool | Capability |
|------|-----------|
| security_check | Run all three Semgrep products (Code, Supply Chain, Secrets) |
| semgrep_scan | Targeted scan with specific rulesets |
| semgrep_scan_with_custom_rule | Scan using user-defined rules |
| get_abstract_syntax_tree | Parse and return AST for a file |
| semgrep_findings | Query findings from Semgrep AppSec Platform |
| supported_languages | List all supported programming languages |
| semgrep_rule_schema | Get the schema for writing custom rules |

**Key differentiator:** The **most-starred security scanning MCP server** and the first to move from standalone repo to CLI-integrated architecture. Running `semgrep mcp` starts an MCP server with access to 5,000+ rules across SAST, SCA (Supply Chain), and Secrets detection. Supports stdio and streamable-http transports (SSE transport dropped January 2026). **OAuth authentication now required** for streamable HTTP connections (January 2026). **DNS rebinding protection** added February 2026. Claude Code and Cursor hooks now pull custom rules from the Semgrep Registry. Deterministic static analysis means no false positives from AI interpretation — Semgrep finds the issue, the LLM explains and fixes it. Multi-language support across 30+ languages.

**Limitation:** The standalone repo (665 stars) is archived — users must install the full Semgrep CLI to get MCP. Semgrep's SAST mindshare is growing (2.6%, up from 1.6%) but still trails SonarQube (17.7%). The 7-tool count is modest compared to other security platforms. Free tier has rule limitations; full rule coverage requires Semgrep Teams/Enterprise.

### SonarQube — Code Quality Meets AI Agents

| Aspect | Detail |
|--------|--------|
| Repository | [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) |
| Stars | ~544 *(was 442, +23%)* |
| Forks | ~79 *(was 68)* |
| Language | Java |
| License | Proprietary |
| Creator | SonarSource (official) |
| Commits | 403 |
| Latest push | April 2026 (actively maintained) |

**Key tools:** `run_advanced_code_analysis` (beta, SonarQube Cloud only), `analyze_code_snippet` (direct snippet analysis in agent context), issue retrieval, quality gate checks, security hotspot review, metrics and branch analysis. Supports 20+ languages: Java, Kotlin, Python, Ruby, Go, JavaScript, TypeScript, JSP, PHP, XML, HTML, CSS, CloudFormation, Kubernetes, Terraform, ARM, Ansible, Docker, and Secrets detection.

**Key differentiator:** The **fastest-growing security scanning MCP server** — surging from 442→544 stars (+23%) in 38 days. SonarQube holds the largest SAST mindshare (17.7%) and the MCP server brings that analysis to AI coding agents. **NEW: Native MCP server in SonarQube Cloud** — no Docker installation required, fully managed endpoint that is always on, always updated, and centrally accessible. Users can now choose between local Docker deployment or cloud-native. The `analyze_code_snippet` tool lets AI agents scan code fragments without committing — ideal for real-time security checks during code generation. AI agents can now **interactively update issue status or mark findings as false positives** directly from the assistant. Wide IDE support: Claude Code, Cursor, Gemini CLI, VS Code (GitHub Copilot), Windsurf, Zed.

**Limitation:** Java implementation requires JVM for local deployment (cloud-native option eliminates this). The proprietary license limits community contributions and forks. `run_advanced_code_analysis` is beta and Cloud-only. SonarQube's traditional strength is code quality (code smells, duplication, coverage) more than security — teams needing deep SAST may pair it with a dedicated security tool.

### Snyk — Full Platform Security via CLI MCP

| Aspect | Detail |
|--------|--------|
| Repository | [snyk/studio-mcp](https://github.com/snyk/studio-mcp) |
| Stars | ~35 *(was 27)* |
| Forks | ~11 |
| Language | Go |
| License | Apache-2.0 |
| Creator | Snyk (official) |
| Releases | 19 (latest v1.9.1, April 2026) |
| CLI integration | Built into Snyk CLI as `snyk mcp --experimental` |

**Capabilities:** Triggers CLI security scans for code (SAST), dependencies (SCA), containers, and infrastructure-as-code. Generates SBOMs (Software Bill of Materials). Monitors projects for new vulnerabilities. Now supports **uv dependency scanning** (Python). Available via CLI, IDE extensions, MCP server, and GitHub Actions. Supports stdio and SSE transports.

**Key differentiator:** Snyk is the **broadest security platform** with MCP integration — SAST, SCA, container scanning, and IaC scanning from a single CLI command. Now extends to **Goose CLI** for agentic workflows. v1.9.1 (April 2026) shows active release cadence — 19 releases in 5 months. Snyk's vulnerability database (curated by security researchers) provides high-quality findings with remediation advice. Works with GitHub Copilot, Continue, Cursor, Qodo, Windsurf, Goose, and other MCP-enabled tools. SBOM generation is unique among security MCP servers. **Path Traversal findings (CWE-22) now tiered by source risk** — reducing noise by auto-reclassifying lower-risk sources from High/Medium to Low severity.

**Limitation:** Still marked `--experimental` — not GA. The `studio-mcp` repo has only 35 stars despite Snyk's 4.4% container security mindshare. Requires a Snyk account and API token. Closed to public contributions. The experimental status means the API surface may change without notice.

### Snyk Agent Scan — Meta-Security for MCP Servers

| Aspect | Detail |
|--------|--------|
| Repository | [snyk/agent-scan](https://github.com/snyk/agent-scan) |
| Stars | ~2,300 |
| Forks | ~210 |
| Language | Python |
| License | Apache-2.0 |
| Creator | Snyk (via Invariant Labs acquisition) |
| Commits | 486 |

**Capabilities:** Auto-discovers local agent configurations (Claude, Cursor, Windsurf, Gemini CLI) and scans MCP servers and agent skills for 15+ security risks: prompt injection, tool poisoning/shadowing, toxic flows, malware payloads, untrusted content, credential handling, hardcoded secrets.

**Key differentiator:** **Meta-security — a tool that scans MCP servers themselves.** Formerly MCP-Scan from Invariant Labs, rebranded to Snyk Agent Scan (v0.4.13, April 2026) after Snyk's acquisition. At 2.3k stars, it's the **most popular security-related MCP tool in the entire ecosystem** — more stars than all other security scanning MCP servers combined. Addresses the ironic reality that MCP servers are themselves an attack surface (Known Issue #5). Auto-discovery means developers don't need to manually configure what to scan.

**Limitation:** Scans MCP server configurations and tool definitions, not application code. Complementary to SAST/SCA/DAST tools rather than a replacement. Recommends sandboxed environments for evaluating untrusted configurations.

### Trivy — Open-Source Container and IaC Scanning

| Aspect | Detail |
|--------|--------|
| Repository | [aquasecurity/trivy-mcp](https://github.com/aquasecurity/trivy-mcp) |
| Stars | ~37 *(was 38)* |
| Forks | ~7 |
| Language | Go |
| License | MIT |
| Creator | Aqua Security (official) |
| Latest release | v0.0.20 (December 2025) |

**Capabilities:** Vulnerability scanning in dependencies, container images, IaC files, and remote repositories. Multi-language support (Python/pip, Node.js/npm, Go, Rust, PHP, Ruby). Automatic fix suggestions for vulnerable package versions. Severity-level reporting. Now supports **stdio, streamable HTTP, and SSE transports**. Aqua Platform integration available with AQUA_KEY/AQUA_SECRET for advanced scanning and policy compliance.

**Key differentiator:** The **only fully open-source, free** comprehensive vulnerability scanner with an official MCP server. Trivy's main repo has 23k+ GitHub stars — the MCP server brings that scanning capability to AI coding agents. Can scan local filesystems, container images, and remote repos through natural language queries. Automatic fix suggestions (updating to non-vulnerable package versions) enable AI agents to scan-and-fix in a single loop. MIT license means no vendor lock-in. Now supports **Azure Kubernetes Service (AKS) ARM template misconfiguration scanning** and uniformly skips third-party packages to reduce false positives.

**Limitation:** Only 37 stars on the MCP repo despite Trivy's massive community (23k+ stars on the main repo). Last release December 2025 — development appears stalled. **Major supply chain incident in March 2026** — threat actors published malicious Trivy v0.69.4 release using compromised credentials; GitHub Actions (trivy-action, setup-trivy) were also compromised. The incident has been remediated, but underscores security risks in the scanner supply chain itself.

### GitGuardian — Secret Scanning Specialist

| Aspect | Detail |
|--------|--------|
| Repository | [GitGuardian/ggmcp](https://github.com/GitGuardian/ggmcp) |
| Stars | ~35 *(was 34)* |
| Forks | ~14 *(was 12)* |
| Language | Python |
| License | MIT |
| Creator | GitGuardian (official) |
| Commits | 240 |
| Latest push | April 2026 (actively maintained) |

**Capabilities:** Scan projects for hardcoded secrets using 500+ detectors. Manage secret incidents. Inject honeytokens for breach detection. Real-time `secret_scan` tool. Read-only permissions by design.

**Key differentiator:** The **most focused secret scanning MCP server** with 500+ detection patterns. GitGuardian specializes exclusively in secrets — API keys, passwords, tokens, certificates — and the MCP server brings that specialization to AI coding workflows. Read-only design means the MCP server can scan but can't accidentally expose or leak secrets. Honeytoken injection is a unique defensive capability: plant fake credentials that alert you when someone tries to use them. Actively maintained (pushed March 23, 2026).

**Limitation:** Narrow scope — secrets only, no SAST, SCA, or IaC scanning. Requires GitGuardian API key and account. The 35-star count is low for a dedicated security vendor. No open-source alternative with comparable detection breadth. Teams already using GitHub's built-in secret scanning (free for public repos) may not need a separate MCP server for this capability.

### Cycode — Full ASPM via CLI MCP

| Aspect | Detail |
|--------|--------|
| Repository | [cycodehq/cycode-cli](https://github.com/cycodehq/cycode-cli) (MCP built into CLI) |
| Stars | ~98 *(was 97)* |
| Forks | ~62 |
| Language | Python |
| License | MIT |
| Creator | Cycode (official) |
| Commits | 413 |
| Latest version | v3.14.0 (April 2026) |

**Capabilities:** SAST, SCA, Secrets scanning, and IaC scanning on local files, Git repos, and commit ranges. Detailed vulnerability reports with remediation guidance.

**Key differentiator:** Cycode provides **Application Security Posture Management (ASPM)** — a unified view across SAST, SCA, secrets, and IaC scanning from a single CLI. The MCP integration means AI agents get comprehensive security coverage without configuring multiple tools. Listed in the official MCP servers repository. Works with Cursor, Windsurf, and GitHub Copilot. Remediation guidance is included with findings, enabling AI agents to fix issues immediately.

**Limitation:** The 97-star count is for the entire CLI repo, not MCP specifically. Requires Python 3.10+ and a Cycode account. Smaller vendor than Semgrep, Snyk, or SonarQube — less community support and fewer online resources. The MCP capability is embedded in the CLI rather than documented as a standalone feature.

### Contrast Security — IAST Bridge to AI Agents

| Aspect | Detail |
|--------|--------|
| Repository | [Contrast-Security-OSS/mcp-contrast](https://github.com/Contrast-Security-OSS/mcp-contrast) |
| Stars | ~19 *(was 16)* |
| Forks | ~5 |
| Language | Java |
| License | Apache-2.0 |
| Creator | Contrast Security (official) |
| Commits | 491 *(was not tracked)* |
| Tools | 13 |
| Latest push | April 2026 (active) |

**Capabilities:** Bridge to Contrast IAST vulnerability data. Full taint-flow traces from source to sink. Specific HTTP requests that triggered findings. Environment and application details. **Now 13 tools** across application management, vulnerability analysis, library/SCA tracking, protection monitoring (attack events, rule configuration), route coverage metrics, and **SAST integration with SARIF output**.

**Key differentiator:** The **only IAST-focused MCP server** and now the **first security MCP server to output SARIF format** — the industry-standard Static Analysis Results Interchange Format. This partially addresses Known Issue #1 (no standard finding format). Interactive Application Security Testing (IAST) instruments running applications and detects vulnerabilities during execution — providing more context than SAST. The taint-flow traces show exactly how user input flows through the application to a vulnerable sink, giving AI agents the information needed for precise remediation. 491 commits demonstrates serious investment despite modest star count.

**Limitation:** Requires Contrast Security enterprise platform (no free tier). Only 19 stars. Java implementation. Contrast explicitly warns against using their MCP server with LLMs that train on your data — enterprise-grade sandboxed LLMs are recommended. IAST requires the application to be running with Contrast agents instrumented, which limits scanning to deployed/running code only.

### CodeQL Community — GitHub's Query Language via MCP

| Aspect | Detail |
|--------|--------|
| Repository | [JordyZomer/codeql-mcp](https://github.com/JordyZomer/codeql-mcp) |
| Stars | ~144 *(was 143)* |
| Forks | ~21 *(was 19)* |
| Language | Python |
| Creator | Community |

Wraps the CodeQL query server, enabling AI agents to interact with CodeQL through structured commands. A quasi-official [codeql-development-mcp-server](https://github.com/advanced-security/codeql-development-mcp-server) (12 stars, TypeScript) from GitHub's CodeQL Expert Services team focuses on CodeQL query development (AST, CFG, CLI, and LSP tools) rather than scanning results.

**Key differentiator:** CodeQL is GitHub's **semantic code analysis engine** — it treats code as data and runs queries against it to find vulnerabilities. The community MCP server brings this capability to AI agents. CodeQL powers GitHub Advanced Security's code scanning and has the deepest semantic understanding of any free SAST tool.

**Limitation:** Community-built, not official from GitHub. CodeQL requires a compiled database of your code, which adds setup complexity. The development MCP server from GitHub's team is for writing CodeQL queries, not running scans. CodeQL is free for open-source repos but requires GitHub Advanced Security licenses for private repos.

### StackHawk — FIRST DAST MCP Server (NEW)

| Aspect | Detail |
|--------|--------|
| Repository | [stackhawk/stackhawk-mcp](https://github.com/stackhawk/stackhawk-mcp) |
| Stars | ~5 |
| Language | TypeScript |
| Creator | StackHawk (official) |
| Status | Beta (Pro/Enterprise/Vibe subscription required) |

**Capabilities:** Run dynamic application security testing (DAST) directly from AI coding assistants. Security analytics, YAML configuration management, sensitive data/threat surface analysis. Can also **scan remote MCP servers for security vulnerabilities** — the first DAST tool to do so.

**Key differentiator:** The **FIRST DAST tool with MCP integration**, directly addressing Known Issue #3 (no real-time DAST via MCP). Developers can ask their AI assistant to "scan my API for vulnerabilities" or "check if my authentication is secure" using natural language. StackHawk tests APIs and web applications at runtime, catching vulnerabilities that SAST misses — authentication flaws, injection attacks, data exposure. The ability to scan remote MCP servers themselves adds meta-security capability alongside Snyk Agent Scan.

**Limitation:** Only 5 stars — extremely early. Beta status. Requires a paid StackHawk subscription (Pro, Enterprise, or Vibe). Cannot scan arbitrary applications without StackHawk platform setup. The low star count suggests minimal adoption despite the significant capability.

### Checkmarx — Enterprise SAST Leader Enters (NEW)

| Aspect | Detail |
|--------|--------|
| Platform | Checkmarx One MCP Server |
| Creator | Checkmarx (official) |
| Community server | [suitable-adventures/checkmarx-mcp](https://github.com/suitable-adventures/checkmarx-mcp) |

**Capabilities:** The Checkmarx MCP server provides structured, controlled context — remediation instructions, policies, and risk signals — so AI agents (Developer Assist, Policy Assist, Insights Assist) can generate accurate fixes. Covers SAST, SCA, IaC, and API Security through a unified MCP interface. Read-only access to findings with severity-based sorting and data flow analysis.

**Key differentiator:** **Enterprise SAST leader finally enters the MCP ecosystem**, directly addressing Known Issue #10. Checkmarx selected MCP as the foundation for its agentic architecture at RSAC 2026, marking "agentic security" as a mainstream enterprise strategy. The MCP server ensures interoperability with Claude, GitHub Copilot, Cursor, and other AI tools. AI Supply Chain Security provides inventory and risk assessment across MCP servers, LLMs, agents, and SDKs.

**Limitation:** The official MCP server is part of the commercial Checkmarx One platform — not open source. **Checkmarx suffered a GitHub repository breach in March 2026** and a subsequent supply chain attack on KICS Docker images (April 2026). While the MCP server itself was not reported as compromised, the incidents raise trust questions for a security vendor. Community alternatives exist but have minimal adoption.

### Black Duck Polaris — Enterprise SAST/SCA via MCP (NEW)

| Aspect | Detail |
|--------|--------|
| Package | [@black-duck/mcp-server](https://www.npmjs.com/package/@black-duck/mcp-server) |
| Creator | Black Duck (official) |
| Community server | [mtgibbs/blackduck-polaris-mcp](https://github.com/mtgibbs/blackduck-polaris-mcp) |

**Capabilities:** Polaris Issue Management MCP server — secure, read-only integration bringing Polaris findings and Black Duck's ContextAI™ knowledge base into AI assistants. Pull up issue details, summarize risk by project/portfolio, identify recurring vulnerability patterns, get remediation guidance. Natural language queries ("Show me all critical SQL injection issues", "What's the most at-risk project?").

**Key differentiator:** **Another enterprise vendor closing the gap** with read-only MCP integration. Polaris Rapid Scan Static powered by Sigma 2026.3.0 provides improved accuracy and expanded language support. The MCP server grounds AI responses in authoritative Polaris data rather than generic LLM output — an important distinction for enterprise compliance. AI-assisted authentication (screenshot-based login script generation) shows innovation in the platform.

**Limitation:** Read-only — cannot trigger scans or apply fixes via MCP. Requires Polaris platform. No GitHub star data available for the official package. The community server has minimal adoption.

### Additional Servers

**[Anchore Grype MCP](https://github.com/anchore/grype-mcp)** (9 stars, Python) — Official container image and filesystem vulnerability scanner. Minimal adoption, last updated August 2025.

**[Nuclei MCP](https://github.com/addcontent/nuclei-mcp)** (47 stars *(was 43)*, Go, MIT) — Community server wrapping ProjectDiscovery's Nuclei template-based vulnerability scanner. Context-aware scanning with template management and result caching.

**[MCPwner](https://github.com/Pigyon/MCPwner)** (49 stars *(was 41)*, Python, Apache-2.0) — Community autonomous vulnerability discovery tool unifying secret scanning, SAST, SCA, DAST, and 0-day research. 158 commits. Standardizes output as SARIF/JSON.

**[AWS Sample Security Scanner](https://github.com/aws-samples/sample-mcp-security-scanner)** (10 stars, Python, MIT-0) — Reference implementation combining Checkov + Semgrep + Bandit for IaC and multi-language SAST.

**[OSV MCP](https://github.com/gleicon/mcp-osv)** (14 stars, Go) — Queries Google's OSV.dev vulnerability database for dependency analysis.

**[GitHub MCP Server](https://github.com/github/github-mcp-server)** — GitHub's official MCP server added secret scanning and push protection features (August 2025, expanded March 2026). Scans tool-call inputs for exposed secrets. On by default for public repos and private repos with GitHub Advanced Security.

**Mend SAST** — Commercial "agentic SAST" via MCP. **Now exposes two explicit MCP tools**: `mend-code-security-assistant` (SAST) and `mend-dependencies-assistant` (SCA). Integrates with Cursor, Windsurf, Claude Code, GitHub Copilot, Amazon Q, and Gemini CLI. **SAST+DAST correlation**: when both Mend SAST and DAST run against the same application, a finding confirmed by dynamic testing gets marked as "Exploitable."

**Veracode community servers (NEW)** — Multiple community MCP servers now exist: [dipsylala/veracode-mcp](https://github.com/dipsylala/veracode-mcp) (Go), [ChinYoong/Veracode-MCP](https://github.com/ChinYoong/Veracode-MCP), [stuartsessions/vc-platform-mcp](https://github.com/stuartsessions/vc-platform-mcp). Read-only access to application security information, scan results, and policy compliance. **Closes a major gap from the initial review** — Veracode teams can now connect their platform to AI coding assistants.

### Notable Gaps (Updated)

**Gaps partially closed since March 2026:**
- ~~Veracode~~ — multiple community servers now available
- ~~Checkmarx~~ — official agentic platform with MCP + community server
- ~~DAST via MCP~~ — StackHawk provides first DAST MCP integration (beta)

**Remaining gaps:** Fortify (OpenText), TruffleHog (standalone), Gitleaks (open issue #1869 proposes MCP support), Dependabot/Renovate, python-safety. No fully open-source DAST MCP server exists yet (StackHawk requires paid subscription).

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging | Profiling | Code Review |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|---------- | ------- |----------|----------|----------|---------------------- | --------------|-----------|-----------|-------------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, 1.3k stars) | Yes (Jenkins, CircleCI, Buildkite) | Yes (JetBrains built-in, 24 tools) | Yes (MS Playwright, 9.8k stars, 24 tools) | Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana) | Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) | Yes (NuGet built-in VS 2026, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B 384, JetBrains built-in server) | Yes (Postman 192, Apollo GraphQL 275, Kong deprecated, Apigee, MuleSoft) | Yes (Splunk 13 tools GA, Grafana Tempo built-in, Grafana Loki 103 stars) | Partial (Liquibase private preview 19 tools, Prisma built-in CLI v6.6.0+) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector 9.2k official) | Partial (CodSpeed MCP, Polar Signals remote, Grafana Pyroscope via mcp-grafana) | Yes (SonarQube 442 stars, Codacy 56 stars, Graphite GT built-in) |
| **CLI-integrated MCP** | No (standalone server) | No (built into GitLab) | No | No | No | Yes (Jenkins plugin) | Yes (JetBrains built-in) | No | No | Yes (Semgrep, Snyk, Cycode — MCP built into CLI) | No | N/A | N/A | N/A | N/A | — | N/A | No | No | N/A |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (1.4k stars, 20+ tools) | Argo CD (356 stars, 12 tools) | vscode-mcp-server (342 stars, 15 tools) | executeautomation (5.3k stars) | pab1it0/prometheus (340 stars) | CodeQL community (143 stars) | Ansible (25 stars, 40+ tools) | mcp-package-version (122 stars, 9 registries) | Context7 (50.3k stars), magic-mcp (4.5k stars) | openapi-mcp-generator (495 stars), mcp-graphql (374 stars) | cr7258/elasticsearch (259 stars), Traceloop OTel (178 stars) | mpreziuso/mcp-atlas (Atlas), defrex/drizzle-mcp (Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars), Docs MCP (87 stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars), devtools-debugger (341 stars) | theSharque/mcp-jperf (Java JFR), PageSpeed Insights MCP servers | kopfrechner/gitlab-mr-mcp (86 stars), crazyrabbitLTC (32 stars) |
| **Vendor count** | 1 (GitHub) | 1 (GitLab) | 0 (Atlassian via Jira only) | 1 (Docker) + community | 0 (Red Hat leads community) | 3 (Jenkins, CircleCI, Buildkite) | 1 (JetBrains) | 1 (Microsoft) | 9 (Grafana, Datadog, Sentry, Dynatrace, New Relic, Instana, Splunk, PagerDuty, Honeycomb) | 10+ (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast, Checkmarx, Black Duck, StackHawk) | 5+ (HashiCorp, Pulumi, AWS, OpenTofu, Spacelift) | 2 (Microsoft/NuGet, Homebrew) | 3 (Vercel, E2B, Upstash/Context7) | 4+ (Postman, Apollo, Kong, Google/Apigee, MuleSoft) | 6+ (Splunk, Grafana/Loki, Grafana/Tempo, Coralogix, Axiom, Mezmo) | 2 (Liquibase, Prisma) + Google partial | 5+ (Microsoft, Mintlify, ReadMe, Stainless, OpenAI, Vonage, Fern, Apidog) | 3 (Google/Chrome DevTools, Microsoft/DebugMCP, LLVM/LLDB built-in) | 3 (CodSpeed, Polar Signals, Tricentis/NeoLoad) + Grafana partial | 3 (SonarSource, Codacy, Graphite) + CodeRabbit as client |
| **Scan-and-fix capability** | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Yes (Semgrep, Snyk, Trivy fix suggestions) | N/A | npm-sentinel-mcp (CVE), NuGet (fix vulns) | N/A | N/A | N/A | — | N/A | N/A | N/A | N/A |
| **Secret detection** | Yes (push protection) | Yes (built-in) | No | No | Secret masking (Red Hat) | No | No | No | No | Yes (Semgrep, GitGuardian 500+ detectors, Snyk, Cycode) | Vault MCP (37 stars, secrets management) | npm-sentinel-mcp (CVE), NuGet (fix vulns) | N/A | N/A | N/A | — | N/A | No | N/A | N/A |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | API tokens per platform | Local connection (port/stdio) | None (local browsers) | API tokens / OAuth (remote) | API tokens / CLI auth | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / CLI auth | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect | API keys (CodSpeed, Polar Signals) / Grafana auth / Google API key (PageSpeed) | API tokens (SonarQube, Codacy) / GitHub PAT / GitLab PAT |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | No | No (but Microsoft is Platinum) | No (but Microsoft is Platinum) | No | No | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) | No | No |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | 5.6M developers | Jenkins: 11.3M devs | VS Code: 75.9% market share | Playwright: 45.1% QA adoption | Datadog: 32.7k customers | SonarQube: 17.7% SAST mindshare | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads, PyPI: 421.6B yearly | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 30M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Prisma: 43k stars, Flyway: 10.7k stars, Atlas: 6.3k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars, ReadMe: powering major API docs | Chrome: 65%+ browser share, VS Code: 75.9% IDE share, x64dbg: 45k+ stars | APM market: $7-10B, Pyroscope: 11k+ stars, async-profiler: 9k+ stars | SonarQube: 7.4M+ users, CodeRabbit: top AI reviewer, Qodo/PR-Agent: 10.5k stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | [4/5](/reviews/kubernetes-mcp-servers/) | [3.5/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4.5/5](/reviews/monitoring-observability-mcp-servers/) | 4/5 | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | [3/5](/reviews/package-management-mcp-servers/) | [3.5/5](/reviews/code-generation-mcp-servers/) | [3.5/5](/reviews/api-development-mcp-servers/) | [3.5/5](/reviews/logging-tracing-mcp-servers/) | [2.5/5](/reviews/database-migration-mcp-servers/) | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | [4.5/5](/reviews/debugging-mcp-servers/) | [3/5](/reviews/profiling-performance-mcp-servers/) | [3.5/5](/reviews/code-review-pull-request-mcp-servers/) |

## Known Issues

1. **No standard format for security findings in MCP** *(partially addressed)* — Most servers still return findings in proprietary formats. **Contrast Security now outputs SARIF** (Static Analysis Results Interchange Format) for SAST results, and MCPwner standardizes output as SARIF/JSON — but these are exceptions. A Semgrep finding and a SonarQube finding for the same vulnerability still look completely different to the LLM. Progress is slow toward interoperable finding formats.

2. **False positive handling is primitive** — Traditional security tools have sophisticated false-positive suppression (SonarQube's "won't fix" markings, Semgrep's `nosemgrep` comments, Snyk's ignore policies). MCP servers pass raw results to the LLM, which may or may not interpret them correctly. There's no MCP-native mechanism for marking findings as false positives or suppressing known issues. AI agents may repeatedly flag the same suppressed issue.

3. **DAST via MCP now exists but is limited** *(partially addressed)* — **StackHawk launched the first DAST MCP server** (beta), enabling dynamic security testing from AI coding assistants. Developers can scan APIs and web applications for runtime vulnerabilities. However, StackHawk requires a paid subscription, is in beta, and has only 5 stars. No fully open-source DAST MCP server exists. Mend now correlates SAST+DAST findings (marking dynamically-confirmed issues as "Exploitable"), but this isn't MCP-native DAST.

4. **CI/CD integration is indirect** — MCP servers are designed for IDE/agent interaction, not CI/CD pipelines. Teams still need separate CI/CD integrations for the same security tools. An AI agent can scan code in the IDE via MCP, but the same code gets re-scanned by a different integration in CI. No MCP-native CI/CD security scanning pattern exists yet.

5. **MCP servers are themselves an attack surface** *(validated by real incidents)* — This issue became dramatically more concrete in March–April 2026. **Trivy suffered a supply chain attack** — compromised credentials led to malicious v0.69.4 releases and compromised GitHub Actions. **Checkmarx suffered a GitHub repository breach** (March 2026) and subsequent KICS Docker image/VS Code extension supply chain compromise (April 2026). Security scanning tools being compromised is no longer theoretical. **Snyk Agent Scan** (2.3k stars) emerged as a direct response — a meta-security tool scanning MCP servers for 15+ risks including prompt injection and tool poisoning. StackHawk also scans remote MCP servers for vulnerabilities.

6. **Prompt injection risk in security context** — Code being scanned could contain prompt injection payloads designed to influence the LLM's interpretation of security results. A malicious code comment could instruct the LLM to ignore or downplay a finding. This is a novel attack vector unique to AI-assisted security scanning that traditional tools don't face. No security MCP server currently sanitizes scan results for prompt injection content.

7. **Vendor lock-in across the board** — Every official security MCP server requires its vendor's platform (Semgrep account, SonarQube instance, Snyk API key, GitGuardian API key, Cycode account, Contrast enterprise license). The only genuinely free option is Trivy MCP (MIT, no account required for basic scanning). Teams wanting multi-scanner coverage need accounts with multiple vendors.

8. **Low adoption relative to tool popularity** — Semgrep's main repo has thousands of stars, but the MCP server has 641 (archived). SonarQube has 17.7% SAST mindshare but only 442 MCP stars. Trivy has 23k+ stars but only 38 on the MCP server. Snyk's MCP has 27 stars despite being a $8.5B+ valued company. Security teams have not yet broadly adopted MCP-based scanning workflows.

9. **Remediation automation is shallow** — While Semgrep, Snyk, and Trivy provide fix suggestions, no MCP server implements a true scan-fix-verify loop (scan code → find vulnerability → apply fix → re-scan to confirm fix works → report). AI agents can build this loop themselves, but it requires prompt engineering rather than being a built-in server capability. Mend's commercial "agentic SAST" (iterates up to 3 times) is the closest, but it's closed-source.

10. **Enterprise SAST/DAST leaders are entering** *(partially addressed)* — **Checkmarx launched an agentic security platform built on MCP** at RSAC 2026 with Developer Assist, Policy Assist, and Insights Assist agents. **Black Duck shipped** a Polaris Issue Management MCP server. **Veracode** now has multiple community MCP servers. This leaves **Fortify (OpenText)** as the only major enterprise SAST vendor without MCP presence. The gap is closing rapidly — enterprises can now connect Checkmarx, Black Duck, and Veracode to AI coding assistants, though official open-source repos remain limited.

## Bottom Line

**Rating: 4 out of 5** *(was 3.5/5)*

The security scanning MCP ecosystem hit an inflection point in April 2026 — **vendor count jumped from 7 to 10+**, three major enterprise gaps closed, and the first DAST MCP server launched. SonarQube surged 442→544 stars (+23%) and eliminated the Docker barrier with cloud-native MCP. Snyk's acquisition of Invariant Labs created Snyk Agent Scan (2.3k stars) — a meta-security tool that scans MCP servers themselves, now the most popular security-related MCP tool in the ecosystem. StackHawk became the first DAST tool with MCP integration. Checkmarx and Black Duck entered with enterprise platforms built on MCP. Contrast Security became the first to output SARIF format. Semgrep hardened with OAuth and DNS rebinding protection.

The **upgrade from 3.5 to 4/5** reflects: vendor count doubling to 10+ (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast, Checkmarx, Black Duck, StackHawk, plus Mend and Veracode community), SonarQube's +23% growth and cloud-native deployment, Snyk Agent Scan's 2.3k stars validating meta-security as a category, StackHawk closing the DAST gap, Checkmarx/Black Duck/Veracode closing the enterprise vendor gap, Contrast's SARIF output beginning to address the finding format problem, and the three architecture patterns (CLI-integrated, standalone, cloud-native) maturing. It loses the remaining 1 point for: StackHawk DAST in beta with only 5 stars, most servers still under 100 stars, the Trivy supply chain attack and Checkmarx breach undermining trust in security tooling, prompt injection risk in security workflows, Snyk MCP still experimental, no fully open-source DAST, and shallow remediation automation (no scan-fix-verify loops).

**Who benefits from security scanning MCP servers today:**

- **AI-assisted development teams** — If your developers use Cursor, Claude Code, GitHub Copilot, or Windsurf, adding Semgrep or SonarQube MCP gives real-time security feedback as AI generates code. SonarQube's cloud-native MCP makes setup trivial
- **DevSecOps teams** — Teams already running Snyk, Semgrep, or SonarQube in CI/CD can extend the same security policies to the IDE via MCP, creating a "shift-further-left" workflow where issues are caught during generation, not just during review
- **MCP server operators** — Snyk Agent Scan (2.3k stars) provides essential meta-security — scanning your MCP infrastructure for prompt injection, tool poisoning, and malware before deploying to production
- **Enterprise security teams** — Checkmarx, Black Duck, and Veracode teams can now connect their existing platforms to AI coding assistants via MCP, ending the vendor gap that existed in March 2026
- **Open-source maintainers** — Trivy's MCP server (MIT, free, no account) provides container and dependency scanning, though the March 2026 supply chain incident warrants monitoring the project's security posture
- **Secret leak prevention** — GitGuardian's 500+ detectors and GitHub's built-in MCP secret scanning provide layered defense against accidentally committing credentials

**Who should be cautious:**

- **Enterprise security teams on Fortify (OpenText)** — The last remaining major enterprise vendor without MCP presence. All others (Checkmarx, Black Duck, Veracode, Snyk, SonarQube) now have MCP integrations
- **Teams expecting production-grade security** — MCP security scanning is IDE-focused and mostly experimental (Snyk uses `--experimental`, StackHawk is beta). It supplements but does not replace CI/CD security gates, code review, and penetration testing
- **Compliance-driven organizations** — Only Contrast Security outputs SARIF. No security scanning MCP server provides audit trails, compliance reporting, or SOC 2/HIPAA attestation. SonarQube Cloud MCP is the closest to enterprise-ready
- **Teams concerned about supply chain risk** — The Trivy (March 2026) and Checkmarx (March–April 2026) incidents demonstrate that security scanning tools themselves can be compromised. Run Snyk Agent Scan on your security MCP servers
- **Teams concerned about AI data privacy** — Contrast Security explicitly warns against using their MCP server with LLMs that train on your data. Code sent through MCP to an AI agent may transit through cloud LLM APIs — verify your LLM provider's data handling before scanning sensitive code

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Originally published March 2026, refreshed May 2026. See our [About page](/about/) for details on our review process.*
