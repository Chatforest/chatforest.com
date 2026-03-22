---
title: "Code Security MCP Servers — Snyk, SonarQube, Semgrep, Trivy, CodeQL, and Beyond"
date: 2026-03-15T03:48:00+09:00
description: "Code security MCP servers let AI agents scan for vulnerabilities, detect secrets, analyze dependencies, and enforce security policies through Snyk, SonarQube, Semgrep, Trivy, Endor Labs, Cycode, Aikido, and more. We reviewed 15+ servers across 10 platforms. Snyk leads with an official 11-tool server covering SAST, SCA, IaC, containers, and SBOM. SonarQube's official server has 423 stars and deep code quality integration. Semgrep pioneered the category with 639 stars before being archived into the main binary."
og_description: "Code security MCP servers: Snyk (official, 11 tools, SAST/SCA/IaC/container/SBOM), SonarQube (official, 423 stars, code quality), Semgrep (639 stars, 7 tools, archived into CLI), Trivy (official plugin, container/filesystem/repo scanning), Endor Labs (6 tools, dependency risks), Cycode (5 tools, SAST/SCA/IaC/secrets), Aikido (3 tools, SAST+secrets). 15+ servers across 10 platforms. Rating: 4.0/5."
content_type: "Review"
card_description: "Code security MCP servers across Snyk, SonarQube, Semgrep, Trivy, CodeQL, Endor Labs, Cycode, and Aikido. Snyk's official server is the most comprehensive with 11 tools spanning five scanning domains. SonarQube has the largest community. Multi-tool aggregators like DevSecOps-MCP combine SAST, DAST, and SCA in one server."
last_refreshed: 2026-03-15
---

Code security is arguably where MCP servers deliver the most practical value — **catching vulnerabilities in AI-generated code before it ships**. This category has exploded with both official vendor servers and community aggregators, covering static analysis (SAST), dependency scanning (SCA), container security, infrastructure-as-code (IaC) auditing, and secrets detection.

The headline finding: **official vendor investment is exceptional**. Snyk, SonarQube, Semgrep, Trivy, Endor Labs, Cycode, and Aikido all have official or officially-supported MCP servers. **Snyk's server is the most comprehensive** — 11 tools covering SAST, SCA, IaC, containers, SBOM, and AI-BOM from a single integration. **SonarQube has the largest community** at 423 stars with deep IDE integration. And **multi-tool aggregators** are emerging that bundle Semgrep + Bandit + Checkov + OWASP ZAP into unified security scanning servers.

## The Landscape

### Snyk (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [snyk/studio-mcp](https://github.com/snyk/studio-mcp) | ~26 | Go | 11 | Snyk account | stdio |

**Snyk's official MCP server is the most comprehensive security scanning integration available.** 26 stars, 10 forks, 19 commits, Apache 2.0, v1.6.1 (March 2026). Closed to public contributions — this is a vendor-controlled release.

11 tools spanning five security domains: **snyk_code_scan** (source code vulnerability detection), **snyk_sca_scan** (open source dependency scanning), **snyk_iac_scan** (infrastructure-as-code analysis), **snyk_container_scan** (container image scanning), **snyk_sbom_scan** (Software Bill of Materials), **snyk_aibom** (AI Bill of Materials — a newer capability for AI supply chain visibility), plus **snyk_trust** (folder trust configuration), **snyk_auth/snyk_logout/snyk_auth_status** (authentication management), and **snyk_version** (version info).

The breadth here is unmatched. No other single MCP server covers SAST + SCA + IaC + container + SBOM scanning. The AI-BOM tool is forward-looking — as AI agents increasingly pull in packages and models, tracking the AI supply chain becomes critical. Integrates with Cursor, VS Code, Windsurf, Claude Desktop, GitHub Copilot, and more.

**Also notable: [snyk/agent-scan](https://github.com/snyk/agent-scan)** — 1.9k stars, 376 commits, Apache 2.0, v0.4.8 (March 2026). This isn't an MCP server itself but a security scanner *for* MCP servers and AI agents. It detects prompt injection, tool poisoning, tool shadowing, toxic flows, malware payloads, hardcoded secrets, and credential handling issues. A meta-security tool for the agentic ecosystem — worth knowing about even though it serves a different purpose.

**Community alternative: [sammcj/mcp-snyk](https://github.com/sammcj/mcp-snyk)** — 15 stars, JavaScript, archived (August 2025), alpha/unfinished. The official server has superseded this.

### SonarQube (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) | ~423 | Kotlin | Multiple | SonarQube token | stdio |

**SonarQube's official MCP server has the largest community in the code security MCP category.** 423 stars, 321 commits — serious ongoing development. Requires JDK 21+. Also available as a Docker image (`mcp/sonarqube`).

The server provides seamless integration with both SonarQube Cloud and self-hosted SonarQube Server for code quality and security analysis. Key capabilities include project issue searching, software composition analysis, code snippet analysis (analyze code directly without repository context), and enterprise discovery for SonarQube Cloud users.

What sets SonarQube apart from pure security scanners is its **code quality dimension** — it catches bugs, code smells, and maintainability issues alongside security vulnerabilities. For teams already using SonarQube (and many are — it's one of the most widely deployed code quality platforms), this MCP server makes existing quality gates accessible to AI agents.

Integrates with 11+ platforms: Claude Code, Cursor, VS Code, Windsurf, GitHub Copilot, Gemini CLI, Kiro, Zed, and more. Supports `SONARQUBE_PROJECT_KEY` for automatic project scoping. 0 open issues, 4 PRs.

**Archived alternative: [sapientpants/sonarqube-mcp-server](https://github.com/sapientpants/sonarqube-mcp-server)** — archived November 2025. Use the official SonarSource version.

### Semgrep (Official, Archived)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [semgrep/mcp](https://github.com/semgrep/mcp) | ~639 | Python | 7 | Optional (AppSec Platform) | stdio, HTTP |

**Semgrep pioneered the code security MCP category with the highest star count in this review — but the standalone server is now archived.** 639 stars, 353 commits, archived October 2025. Future MCP functionality is integrated directly into the Semgrep binary.

7 tools before archival: **security_check** (scan for vulnerabilities), **semgrep_scan** (scan with config strings), **semgrep_scan_with_custom_rule** (custom rule scanning), **get_abstract_syntax_tree** (AST output), **semgrep_findings** (fetch from AppSec Platform — requires auth), **supported_languages** (language list), and **semgrep_rule_schema** (rule JSON schema). Also provides prompts for custom rule writing and resources for rule schemas.

Semgrep covers SAST, supply chain analysis (SCA), and secrets detection. The move to integrate MCP into the main binary is strategically sound — it means any Semgrep installation becomes MCP-capable without a separate server, reducing setup friction. But it also means the well-documented standalone repo is frozen.

The semgrep-mcp PyPI package still works for existing setups. Streamable HTTP transport now requires OAuth authentication.

### Trivy (Official Plugin)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [aquasecurity/trivy-mcp](https://github.com/aquasecurity/trivy-mcp) | ~37 | Go | Multiple | Optional (Aqua Platform) | stdio, HTTP, SSE |

**Trivy's official MCP plugin brings container and filesystem security scanning to AI agents.** 37 stars, 67 commits, MIT license, v0.0.20 (December 2025). Installs as a Trivy plugin (`trivy plugin install mcp`, then `trivy mcp`).

Scanning capabilities cover three domains: **local filesystem scanning** (project vulnerabilities and misconfigurations), **container image scanning** (CVE detection in Docker images), and **remote repository analysis** (scan code repos for security issues). Optional Aqua Platform integration adds policy compliance and enhanced scanning.

Trivy is one of the most widely-used open source security scanners (23k+ stars on the main repo), so having an official MCP plugin matters. The natural language query interface — ask "Are there any vulnerabilities in this project?" — makes security scanning accessible to non-security-specialists working with AI agents.

Supports VS Code, Cursor, JetBrains IDEs, and Claude Desktop. Next-Gen Trivy arriving in 2026 may bring additional capabilities.

### Endor Labs

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Endor Labs MCP](https://docs.endorlabs.com/secure-ai-coding/mcp-server/) | — | — | 6 | API key | stdio |

**Endor Labs provides a commercial MCP server focused on dependency risk and supply chain security.** No public GitHub repository — distributed as part of the Endor Labs platform.

6 tools: **check_dependency_for_vulnerabilities** (dependency CVE check), **check_dependency_for_risks** (broader risk analysis including malware), **get_endor_vulnerability** (vulnerability database lookup), **get_resource** (context on findings/projects), **scan** (comprehensive security scan — dependencies, code issues, exposed credentials), and **security_review** (code diff analysis — Enterprise Edition only).

The Developer Edition is free and includes SAST, SCA, secrets detection, and malicious package detection. The focus on **malicious open source packages** is distinctive — Endor Labs specializes in detecting supply chain attacks that other scanners miss, like typosquatting packages and dependency confusion.

Currently macOS only (not fully supported on Windows). Integrates with VS Code, IntelliJ, Cursor, and other MCP-compatible IDEs.

### Cycode

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [cycodehq/cycode-cli](https://github.com/cycodehq/cycode-cli) | ~97 | Python | 5 | Cycode auth | stdio, SSE, HTTP |

**Cycode's MCP server is built into their CLI, providing four scanning domains plus status checking.** 97 stars, 388 commits, v3.5.0. The MCP server is activated via `cycode mcp` command. Requires Python 3.10+.

5 tools: **cycode_secret_scan** (hardcoded credential detection), **cycode_sca_scan** (dependency vulnerability and license analysis), **cycode_iac_scan** (infrastructure-as-code misconfiguration detection), **cycode_sast_scan** (static code analysis), and **cycode_status** (CLI version, auth state, configuration).

Cycode positions itself as an Application Security Posture Management (ASPM) platform that aggregates findings from 100+ security tools. The MCP server surfaces this aggregated intelligence to AI agents. Supports three transport types (stdio, SSE, streamable-http). Integrates with Cursor, Windsurf, and GitHub Copilot.

### Aikido

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Aikido MCP](https://help.aikido.dev/mcp/aikido-mcp) | — | npm | 3 | API key | stdio |

**Aikido's MCP server is laser-focused on scanning AI-generated code before it ships.** Available via npm, no public GitHub repo for the MCP server itself (company GitHub at [AikidoSec](https://github.com/AikidoSec)).

3 tools: **aikido_full_scan** (combined SAST + secrets scan), **aikido_sast_scan** (static analysis only), and **aikido_secrets_scan** (secrets detection only). Simple, opinionated, and purpose-built for the "vibe coding" workflow — scan code as it's generated, catch issues before commit.

Supports VS Code, Cursor, Windsurf, Kiro, Claude, OpenAI, Gemini, GitHub Copilot, Mistral, and JetBrains AI. The narrow tool set is a feature, not a limitation — Aikido is designed to be the security layer that runs automatically in the background, not a full security platform you query.

### CodeQL

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [advanced-security/codeql-development-mcp-server](https://github.com/advanced-security/codeql-development-mcp-server) | ~8 | TypeScript | Multiple | CodeQL CLI | stdio, HTTP |

**GitHub's CodeQL MCP server is designed for security researchers writing custom queries, not general scanning.** 8 stars, 39 commits, v2.24.3 (March 2026). Maintained by GitHub's CodeQL Expert Services team.

Tools wrap the CodeQL CLI: database operations, query compilation and validation, test execution, and code analysis across 9 languages (Python, JavaScript, Java, C/C++, Go, C#, Ruby, Swift, GitHub Actions). Built-in prompts guide AI assistants through CodeQL development workflows.

This serves a different audience than Snyk or SonarQube. CodeQL is a *semantic* code analysis engine — it treats code as data you can query with a dedicated language. The MCP server makes it possible for AI agents to write, validate, and run CodeQL queries, which is powerful for security research but overkill for standard vulnerability scanning.

Requires Node.js v24.13.0+ and CodeQL CLI installed. 6 open issues, 18 PRs — actively maintained.

### Multi-Tool Aggregators

| Server | Stars | Language | Tools | Focus |
|--------|-------|----------|-------|-------|
| [jmstar85/DevSecOps-MCP](https://github.com/jmstar85/DevSecOps-MCP) | ~15 | TypeScript | 6 | SAST + DAST + SCA + IAST |
| [Sengtocxoen/sast-mcp](https://github.com/Sengtocxoen/sast-mcp) | ~5 | Python | 23+ integrations | SAST + secrets + IaC + Kali |
| [aws-samples/sample-mcp-security-scanner](https://github.com/aws-samples/sample-mcp-security-scanner) | ~10 | Python | 4 | Checkov + Semgrep + Bandit |

**Multi-tool aggregators bundle multiple security scanners into a single MCP server.** These target teams that want comprehensive coverage without managing individual vendor integrations.

**DevSecOps-MCP** is the most ambitious — 6 MCP tools covering SAST (Semgrep, Bandit, SonarQube), DAST (OWASP ZAP), IAST (Trivy + ZAP hybrid), and SCA (npm audit, OSV Scanner, Trivy). Claims 80+ real vulnerabilities detected in testing. 100% open source with no commercial dependencies. Report generation in JSON, HTML, PDF, and SARIF formats.

**sast-mcp** integrates 23+ tools including Semgrep, Bandit, ESLint Security, Gosec, Brakeman, TruffleHog, Gitleaks, Checkov, tfsec, and even Kali Linux tools (Nikto, Nmap, SQLMap). More of a security Swiss Army knife than a focused scanner. 78 commits suggest active development.

**AWS sample-mcp-security-scanner** is the most polished for a specific use case — Checkov (IaC) + Semgrep (multi-language) + Bandit (Python) with delta scanning to reduce overhead. Only 3 commits, but it's an AWS reference architecture.

## What's Missing

- **No Checkmarx MCP server.** One of the largest enterprise SAST vendors has no MCP integration.
- **No Veracode MCP server.** Same story — major AppSec vendor, no MCP presence.
- **No GitHub Advanced Security MCP server.** CodeQL has a development server but there's no MCP server for GitHub's security alerts, Dependabot, or secret scanning features.
- **DAST coverage is thin.** Only DevSecOps-MCP includes DAST (via OWASP ZAP). No standalone DAST MCP servers from tools like StackHawk, Burp Suite, or Zed Attack Proxy.
- **No runtime security.** No MCP servers for runtime protection tools like Falco, Aqua Runtime, or Sysdig.

## Rating: 4.0 / 5

**This is one of the strongest MCP categories we've reviewed.** The vendor investment is outstanding — Snyk, SonarQube, Semgrep, Trivy, Endor Labs, Cycode, and Aikido all have official servers. The breadth of coverage (SAST, SCA, IaC, containers, secrets, SBOM) across 15+ servers gives teams real options. SonarQube's 423 stars and Semgrep's 639 stars show genuine community adoption.

The 4.0 rating (up from 3.5 in many categories) reflects: **(1)** exceptional official vendor participation — seven vendors with production MCP servers, **(2)** comprehensive coverage — every major scanning domain is represented, **(3)** practical utility — these servers solve the real problem of catching vulnerabilities in AI-generated code, and **(4)** active development — Snyk at v1.6.1, SonarQube at 321 commits, Cycode at 388 commits. The missing pieces (no Checkmarx, weak DAST, no runtime security) prevent a higher rating.

For most teams, start with your existing security vendor's MCP server. If you use SonarQube, their MCP server is excellent. If you want comprehensive coverage from one tool, Snyk's 11-tool server is the best single integration. For open source, Trivy's plugin is the most accessible entry point.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
