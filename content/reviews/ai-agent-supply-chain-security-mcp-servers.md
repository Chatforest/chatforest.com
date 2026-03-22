---
title: "AI Agent Supply Chain Security MCP Servers — Scanning, Vetting, and Securing the MCP Ecosystem"
date: 2026-03-18T23:30:00+09:00
description: "AI agent supply chain security MCP servers reviewed: Snyk Agent Scan (1,900 stars, Python, Apache-2.0, auto-discovers and scans MCP servers for 15+ threat types including tool poisoning, prompt injection, and rug pulls), Docker MCP Gateway (1,300 stars, Go, MIT, containerized MCP execution with SBOM, provenance, and runtime isolation), Cisco MCP Scanner (850 stars, Python, Apache-2.0, multi-engine YARA + LLM + Cisco AI Defense analysis), Socket MCP (90 stars, TypeScript, MIT, real-time dependency security scores for npm/PyPI), agent-bom (10 stars, Python, Apache-2.0, 32 MCP tools, CVE/blast-radius/compliance), MCPShield (5 stars, JavaScript, MIT, typosquat/CVE/credential detection in configs), MCP SBOM Server (3 stars, Python, Trivy CycloneDX generation), SecureChain MCP (2 stars, Python, GPL-3.0, 6 ecosystems, graph analysis). Also covered: Medusa (160 stars, AGPL-3.0, 76 analyzers), MCP_SAST_SCA_SBOM (2 stars, MIT, Snyk+CycloneDX+secrets), SlowMist MCP Security Checklist (819 stars), MCP Server Security Standard (MSSS). Rating: 3.5/5."
og_description: "AI agent supply chain security MCP servers: Snyk Agent Scan (1,900 stars, 15+ threat types), Docker MCP Gateway (1,300 stars, containerized isolation), Cisco MCP Scanner (850 stars, multi-engine), Socket MCP (90 stars, dependency scoring), agent-bom (10 stars, 32 tools), MCPShield (5 stars, typosquat detection). Plus SBOM generators, security checklists, and certification standards. Rating: 3.5/5."
content_type: "Review"
card_description: "AI agent supply chain security is an entirely new security domain that emerged alongside the MCP ecosystem itself. The threat is real: **66% of 1,808 scanned MCP servers had security findings**, counterfeit npm packages have been caught BCC'ing emails to attackers, and tool poisoning attacks can silently exfiltrate data through hidden instructions in MCP tool descriptions. **Snyk Agent Scan** (1,900 stars, Python, Apache-2.0) leads the space — originally Invariant Labs' mcp-scan, now acquired by Snyk — auto-discovering MCP configs across Claude, Cursor, Windsurf, and Gemini CLI, and scanning for 15+ threat types including prompt injection, tool poisoning, tool shadowing, and rug pulls. **Docker MCP Gateway** (1,300 stars, Go, MIT) takes the infrastructure approach — running MCP servers in isolated containers with SBOM generation, provenance verification, restricted CPU/memory, and no host filesystem access by default. **Cisco MCP Scanner** (850 stars, Python, Apache-2.0) brings enterprise muscle with three scanning engines (YARA rules, LLM-as-judge, and Cisco AI Defense API). **Socket MCP** (90 stars, TypeScript, MIT) is the only true MCP server in the category — providing real-time dependency security scores for npm, PyPI, and other ecosystems via the Model Context Protocol, with a free public endpoint at mcp.socket.dev requiring no authentication. **agent-bom** (10 stars, Python, Apache-2.0) offers the deepest MCP integration with 32 tools covering CVE scanning, blast radius analysis, policy enforcement, compliance across 14 frameworks, and runtime proxy with 7 behavioral detectors. The category's strength is that major security vendors (Snyk, Cisco, Docker) are investing heavily. The weakness: most tools scan MCP servers rather than operating *as* MCP servers — the AI agent can't self-assess its own supply chain security through MCP in most cases."
last_refreshed: 2026-03-18
---

AI agent supply chain security is a category that didn't exist two years ago. The explosive growth of the MCP ecosystem — from 714 servers in January 2025 to over 16,000 by early 2026 — has created a new attack surface: **the AI agent's own tool supply chain**. When an AI agent connects to MCP servers, it trusts their tool descriptions, executes their code, and passes sensitive context through them. If any of those servers are compromised, the agent becomes the attack vector.

This review covers tools that **secure the MCP ecosystem itself** — scanning servers for malicious behavior, vetting dependencies, generating SBOMs, and providing infrastructure for safe MCP server distribution. For tools that scan your *application* code (SAST, SCA, IaC), see our [Code Security MCP review](/reviews/code-security-mcp-servers/). For physical supply chain logistics, see our [Logistics & Supply Chain review](/reviews/logistics-supply-chain-mcp-servers/).

The headline findings: **Snyk Agent Scan dominates** at 1,900 stars with the most comprehensive MCP/agent scanning. **Docker MCP Gateway provides the best infrastructure** for secure server distribution. **Cisco brings enterprise-grade scanning**. But **most tools are scanners, not MCP servers** — the irony is that the tools securing the MCP ecosystem mostly operate outside of it.

## MCP Server / Agent Scanners

### Snyk Agent Scan (formerly Invariant Labs mcp-scan)

| Detail | Info |
|--------|------|
| [snyk/agent-scan](https://github.com/snyk/agent-scan) | ~1,900 stars |
| License | Apache-2.0 |
| Language | Python |
| Originally | [invariantlabs-ai/mcp-scan](https://github.com/invariantlabs-ai/mcp-scan) |

The definitive MCP security scanner. Started as Invariant Labs' mcp-scan (which pioneered tool poisoning detection research), then acquired by Snyk and expanded into a comprehensive agent security platform.

### What Works Well

**Auto-discovery is the killer feature.** Agent Scan finds MCP configurations across Claude, Cursor, Windsurf, Gemini CLI, and other agents automatically — you don't need to manually point it at config files. This is critical because most developers don't know exactly which MCP servers are installed across their tools.

**Broad threat detection.** 15+ distinct risk categories spanning two domains. MCP-specific: prompt injection, tool poisoning, tool shadowing, toxic flows. Skill-specific: prompt injection, malware payloads, untrusted content, credential handling, hardcoded secrets. The tool poisoning detection — identifying hidden malicious instructions in tool descriptions that are invisible to users but visible to AI models — was pioneered by the Invariant Labs team.

**Two operational modes.** CLI scanning for immediate assessment, plus continuous background monitoring for production environments. The background mode catches "rug pull" attacks where servers change tool descriptions after initial approval.

### What Doesn't Work Well

**Not an MCP server itself.** Agent Scan is a CLI tool and background daemon, not something your AI agent can invoke via MCP. The agent can't self-assess its own supply chain — a human or CI pipeline must run the scan externally.

**Snyk ecosystem lock-in risk.** While Apache-2.0 licensed, the acquisition trajectory suggests deeper Snyk integration over time. The tool works standalone today, but enterprise features may increasingly require a Snyk account.

### Cisco MCP Scanner

| Detail | Info |
|--------|------|
| [cisco-ai-defense/mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner) | ~850 stars |
| License | Apache-2.0 |
| Language | Python |

Cisco's open-source contribution to MCP security. The multi-engine architecture is the distinguishing feature.

### What Works Well

**Three scanning engines.** YARA rules for pattern detection, LLM-as-judge for semantic analysis of tool descriptions, and the Cisco AI Defense inspect API for cloud-based threat intelligence. These can run independently or together, giving flexibility between air-gapped environments (YARA-only) and maximum coverage (all three).

**Behavioral code analysis.** Goes beyond scanning tool descriptions — actually analyzes MCP server source code for suspicious patterns. This catches threats that static description scanning misses.

**Production readiness scanning.** A distinct "readiness" mode checks for operational issues like missing timeouts, missing retry logic, and inadequate error handling — not just security threats but reliability concerns.

**Multiple deployment modes.** CLI tool for one-off scans, REST API server for integration into pipelines, and offline JSON scanning for CI/CD environments without network access.

### What Doesn't Work Well

**Cisco AI Defense API dependency.** The most powerful scanning engine requires the Cisco AI Defense cloud service. Without it, you're limited to YARA rules and whatever LLM you configure for the judge engine.

**Not an MCP server.** Same limitation as Agent Scan — it scans MCP servers but doesn't operate as one.

### Medusa

| Detail | Info |
|--------|------|
| [Pantheon-Security/medusa](https://github.com/Pantheon-Security/medusa) | ~160 stars |
| License | AGPL-3.0 |
| Language | Python |
| Analyzers | 76 |
| Detection rules | 7,300+ |

An AI-first security scanner with specific MCP and AI agent security rules. Unlike the focused MCP scanners above, Medusa is a general security scanner that includes MCP-specific capabilities.

**Notable:** Covers repo poisoning detection for AI/ML, LLM agents, and MCP servers. 76 specialized analyzers with 7,300+ detection patterns. Can scan any GitHub repo directly with `medusa scan --git user/repo`. The breadth is impressive but the MCP-specific coverage is a subset of the overall tool.

**AGPL-3.0 license** means any modifications or derivative works must also be released under AGPL — important for enterprise adoption where copyleft can be a dealbreaker.

## Secure MCP Infrastructure

### Docker MCP Gateway

| Detail | Info |
|--------|------|
| [docker/mcp-gateway](https://github.com/docker/mcp-gateway) | ~1,300 stars |
| License | MIT |
| Language | Go |
| Catalog | 300+ verified servers |

Docker's approach to MCP security is infrastructure-level: **don't just scan servers, containerize them**. The MCP Gateway runs MCP servers in isolated Docker containers with restricted privileges, network access, and resource usage.

### What Works Well

**Defense in depth.** Every MCP server image in the Docker Catalog is built by Docker, digitally signed, and includes an SBOM. On pull, Docker verifies provenance and runs supply-chain checks via Docker Scout. At runtime, containers get 1 CPU, 2 GB memory, and no host filesystem access by default. This is the most comprehensive security posture available for running MCP servers.

**300+ verified servers.** The Docker MCP Catalog is a curated collection — not every MCP server on GitHub, but ones that have passed Docker's vetting pipeline including security code review, dependency analysis, malware scans, and policy validation.

**Custom catalogs for enterprises.** Organizations can fork Docker's catalog, host images in their own registry, and publish a private catalog exposed via MCP Gateway. This solves the "which servers are approved?" problem at the organizational level.

**Built-in audit logging.** Call-tracing and logging across all MCP tool invocations provides visibility and governance — critical for regulated environments.

### What Doesn't Work Well

**Docker Desktop dependency.** The MCP Toolkit (the management UI) requires Docker Desktop. The Gateway can run independently, but the full experience assumes you're in Docker's ecosystem.

**Performance overhead.** Running each MCP server in its own container adds latency compared to native execution. For interactive AI workflows where response time matters, this overhead is noticeable.

## MCP Servers for Dependency Security

### Socket MCP

| Detail | Info |
|--------|------|
| [SocketDev/socket-mcp](https://github.com/SocketDev/socket-mcp) | ~90 stars |
| License | MIT |
| Language | TypeScript |
| Tools | 1 (`depscore`) |

**The most practically useful server in this category for AI agents.** Socket MCP is an actual MCP server that AI agents can query to check dependency security before installing packages. The `depscore` tool returns comprehensive security scores across supply chain risk, quality, maintenance, vulnerability, and license dimensions for npm, PyPI, and other package ecosystems.

### What Works Well

**Zero-setup public endpoint.** `https://mcp.socket.dev/` requires no API key, no authentication, no local installation. Point your MCP client at it and start querying. This is the lowest friction security tool in the entire MCP ecosystem.

**Batch processing.** Analyze multiple dependencies in a single request — essential for evaluating a `package.json` or `requirements.txt` worth of dependencies without hitting rate limits.

**Actionable scores.** Returns structured data across five dimensions (supply chain, quality, maintenance, vulnerability, license) rather than a binary safe/unsafe. AI agents can make nuanced decisions — "this package has a low maintenance score but no known vulnerabilities" vs. "this package has active supply chain risk indicators."

### What Doesn't Work Well

**Single tool limitation.** One tool (`depscore`) doing one thing. No vulnerability details, no remediation suggestions, no transitive dependency analysis. For deeper analysis, you still need Snyk or Trivy.

**Coverage gaps.** Works best for npm and PyPI. Go, Rust, and other ecosystems have thinner coverage.

### SecureChain MCP Server

| Detail | Info |
|--------|------|
| [securechaindev/securechain-mcp-server](https://github.com/securechaindev/securechain-mcp-server) | ~2 stars |
| License | GPL-3.0 |
| Language | Python |
| Ecosystems | PyPI, NPM, Maven, Cargo, RubyGems, NuGet |

More ambitious than Socket MCP in scope: **six package ecosystems** with vulnerability intelligence, supply chain graph analysis via Neo4j, and VEX (Vulnerability Exploitability eXchange) document retrieval. The graph database approach for modeling dependency relationships is architecturally interesting — it can trace how a vulnerability in a deep transitive dependency propagates up through the dependency chain.

**The catch:** 2 stars, GPL-3.0 license, requires MongoDB + Neo4j infrastructure. This is an early-stage project with heavy infrastructure requirements. The vision is compelling but adoption is minimal.

### agent-bom

| Detail | Info |
|--------|------|
| [msaad00/agent-bom](https://github.com/msaad00/agent-bom) | ~10 stars |
| License | Apache-2.0 |
| Language | Python |
| MCP tools | 32 |

The most MCP-native security tool in the category. While Snyk Agent Scan and Cisco Scanner operate as CLI tools, agent-bom exposes **32 tools** via MCP, meaning AI agents can invoke security scanning directly.

### What Works Well

**AI agent self-assessment.** Because it operates as an MCP server, an AI agent can scan its own environment — check which MCP servers are installed, assess their CVE exposure, trace blast radius from a vulnerability through packages to servers to agents to credentials to tools. This is the "agent securing itself" model that other tools lack.

**Comprehensive scanning.** CVE scanning against OSV, NVD, GHSA, EPSS, and CISA KEV databases. 22 MCP client auto-discovery. Instruction file auditing (analyzes CLAUDE.md and .cursorrules for malicious patterns). 14-framework compliance mapping (OWASP, NIST, MITRE, CIS, ISO, SOC 2, EU AI Act).

**Runtime proxy.** Goes beyond static scanning with 7 behavioral detectors: rug pull detection, injection detection, credential leak detection, exfiltration detection, cloaking detection, rate limiting, and vector DB injection detection.

### What Doesn't Work Well

**10 stars = minimal community vetting.** For a security tool, this is concerning. The tool itself could be a supply chain risk — there's no evidence of third-party security audit.

**Scope creep.** 32 MCP tools, 14 compliance frameworks, 17 output formats, 7 runtime detectors — this attempts to be everything. Whether it does any of them well at 10 stars of community validation is an open question.

## SBOM Generation via MCP

### MCP SBOM Server (Trivy)

| Detail | Info |
|--------|------|
| [gkhays/mcp-sbom-server](https://github.com/gkhays/mcp-sbom-server) | ~3 stars |
| License | — |
| Language | Python |
| Format | CycloneDX |

A minimal MCP server that wraps Trivy to generate SBOMs in CycloneDX format. Receives scan requests via MCP, executes Trivy locally, and returns structured SBOM data. Simple, focused, useful — but 3 stars and no stated license make it a niche tool for personal use rather than production deployment.

### MCP_SAST_SCA_SBOM

| Detail | Info |
|--------|------|
| [blackkhawkk/mcp_sast_sca_sbom](https://github.com/blackkhawkk/mcp_sast_sca_sbom) | ~2 stars |
| License | MIT |
| Language | TypeScript/Python |
| Tools | 4 (Snyk CLI, SBOM Generator, Secrets Scanner, SAST Engine) |

A comprehensive security analysis framework wrapping Snyk CLI, CycloneDX SBOM generation, secrets scanning, and SAST into a single MCP server. Built as a demo against OWASP Juice Shop — analyzed 145 dependencies, found 1,974 code patterns, detected 62 secrets, tracked 779 components. The breadth is impressive for a 2-star project, but the OWASP Juice Shop focus suggests it's more proof-of-concept than production tool.

### MCPShield

| Detail | Info |
|--------|------|
| [mcpshield/mcpshield](https://github.com/mcpshield/mcpshield) | ~5 stars |
| License | MIT |
| Language | JavaScript |

A focused supply chain scanner for MCP configurations. Detects typosquat packages (using Levenshtein distance against 40+ known legitimate MCP packages), checks for known CVEs, identifies hardcoded credentials, flags dangerous filesystem permissions, and verifies publishers. Supports Claude Desktop, Cursor, VS Code, and Windsurf configs. Integrates into CI/CD with exit codes (0=safe, 1=high risk, 2=critical).

**Niche but useful:** The typosquat detection is particularly relevant — the `postmark-mcp` incident (a counterfeit npm package that BCC'd all outgoing emails to an attacker) proved this attack vector is real, not theoretical.

## Standards and Checklists

### SlowMist MCP Security Checklist

| Detail | Info |
|--------|------|
| [slowmist/MCP-Security-Checklist](https://github.com/slowmist/MCP-Security-Checklist) | ~819 stars |
| Origin | SlowMist (blockchain security) |

Not a tool or server — a comprehensive security checklist for MCP-based AI tools. Built by SlowMist, a well-known blockchain security firm that brought their supply chain security expertise to the MCP ecosystem. Covers server plugins, client applications, and multi-MCP scenarios. Useful as a reference when evaluating MCP servers manually or building security policies.

### MCP Server Security Standard (MSSS)

| Detail | Info |
|--------|------|
| [mcp-security-standard/mcp-server-security-standard](https://github.com/mcp-security-standard/mcp-server-security-standard) | Community Review Draft |
| Released | January 15, 2026 |

An open, testable security control standard for certifying MCP servers. Four compliance levels based on deployment context, data sensitivity, and potential impact — not a maturity progression but a risk-based selection model. Includes evidence requirements and reporting schemas. Still in draft but represents the first attempt at formalizing MCP server certification.

## The Threat Landscape

Understanding why these tools exist requires understanding the attacks:

- **Tool poisoning:** Malicious instructions hidden in MCP tool descriptions that are invisible to users but executed by AI models. Invariant Labs demonstrated this could silently exfiltrate entire WhatsApp conversation histories.
- **Rug pulls:** Clean MCP servers submitted for approval, then updated with malicious tool descriptions. Most MCP clients don't re-verify descriptions after initial connection.
- **Typosquatting:** Counterfeit packages (like `postmark-mcp`) that mimic legitimate MCP servers. One caught package was BCC'ing every outgoing email to an attacker.
- **Credential exposure:** 88% of MCP servers require credentials, 53% use static API keys/PATs that are rarely rotated, and only 8.5% use OAuth.
- **Toxic flows:** Multi-server environments where data from one compromised server poisons another trusted server's context.

A scan of 1,808 MCP servers found 66% had security findings. This isn't a theoretical threat — it's the current state of the ecosystem.

## What's Missing

- **No unified MCP security server.** The best scanners (Snyk, Cisco) don't operate as MCP servers. The best MCP server (agent-bom, 32 tools) has minimal adoption. There's no "install this one MCP server and your agent can self-assess its security."
- **No runtime policy enforcement standard.** Docker Gateway provides container-level isolation, but there's no protocol-level mechanism for MCP servers to declare their required permissions or for clients to enforce least-privilege access.
- **No signed tool descriptions.** Tool descriptions can change between connections (enabling rug pulls) because there's no cryptographic signing or pinning mechanism in the MCP protocol itself.
- **No MCP server registry with security ratings.** Docker's catalog (300+ verified servers) is the closest, but it's Docker-specific. A vendor-neutral registry with security scores, attestations, and community ratings doesn't exist.
- **No SLSA or Sigstore integration.** Software supply chain standards like SLSA (Supply chain Levels for Software Artifacts) and signing via Sigstore/Cosign haven't been adopted by the MCP ecosystem.

## Rating: 3.5 / 5

**The good:** Major vendors are investing seriously. Snyk (1,900 stars), Docker (1,300 stars), and Cisco (850 stars) have all shipped open-source MCP security tools within the past year. The threat research from Invariant Labs/Snyk and Docker's containerized approach represent genuine innovation. Socket MCP proves that security data can flow through MCP itself.

**The bad:** Most tools scan MCP servers from the outside rather than operating as MCP servers. The agent can't protect itself — a human or CI pipeline must intervene. Adoption of MCP-native security tools (agent-bom, MCPShield, SBOM servers) is negligible — single-digit stars across the board. And the MCP protocol itself lacks security primitives (signed descriptions, permission declarations, attestations) that would make supply chain security enforceable rather than advisory.

**Bottom line:** The MCP ecosystem's security story is better than most emerging tech ecosystems at this stage. Having Snyk, Cisco, and Docker engaged within 18 months of the protocol's launch is remarkable. But the gap between "tools exist to scan for problems" and "the ecosystem is actually secure" remains wide. The protocol-level gaps (no signing, no permissions, no attestation) mean even perfect scanning tools can only detect threats, not prevent them.
