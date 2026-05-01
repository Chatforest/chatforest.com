---
title: "AI Agent Supply Chain Security MCP Servers — Scanning, Vetting, and Securing the MCP Ecosystem"
date: 2026-03-18T23:30:00+09:00
description: "AI agent supply chain security MCP servers reviewed: OX Security STDIO RCE disclosure (200K servers exposed), Snyk Agent Scan (1,800 stars, Skill Inspector), Pipelock NEW (342 stars, runtime firewall), Docker MCP Gateway (1,300 stars, interceptors), Cisco Scanner v4.6 (830 stars), MCP Guardian (190 stars, Rust proxy). Rating: 4/5."
og_description: "AI agent supply chain security MCP servers: OX Security STDIO RCE disclosure April 2026 (200K servers, 150M downloads exposed, Anthropic says 'by design'). Snyk Agent Scan (1,800 stars, Skill Inspector web tool, v0.4.6). NEW Pipelock (342 stars, runtime firewall, DLP 48 patterns, SSRF, bidirectional MCP scanning). Docker MCP Gateway (1,300 stars, interceptors, secret blocking). Cisco Scanner v4.6 (830 stars). NEW MCP Guardian (190+ stars, Rust proxy, real-time tool call approval). MCP Authorization Spec OAuth 2.1 + Resource Indicators. Official MCP Registry launched. 30+ CVEs filed in 60 days. Rating upgraded 3.5→4/5."
content_type: "Review"
card_description: "AI agent supply chain security escalated from theoretical to crisis in April 2026. **OX Security's 'Mother of All AI Supply Chains' disclosure** revealed a systemic RCE flaw in MCP's STDIO interface — affecting 200,000 servers, 150M+ downloads, and projects like LiteLLM, LangChain, Cursor, and Windsurf. Anthropic confirmed the behavior is 'by design.' The response: **runtime security tools exploded.** **Pipelock** (342 stars, NEW) is a full AI agent firewall with DLP scanning (48 patterns), SSRF protection, bidirectional MCP scanning, tool poisoning detection, and prompt injection blocking — the first true runtime proxy scanner. **MCP Guardian** (190+ stars, NEW, Rust) enables real-time approval/denial of individual tool calls. **Snyk Agent Scan** (1,800 stars, v0.4.6) launched Skill Inspector — a free web tool for instant malicious skill detection — plus background monitoring for MDM/CrowdStrike integration. **Docker MCP Gateway** (1,300 stars) added interceptors for fine-grained policy enforcement and secret blocking. **Cisco MCP Scanner** v4.6 (830 stars) remains actively maintained. Protocol-level security improved: OAuth 2.1 authorization with Resource Indicators (RFC 8707) standardized, official MCP Registry launched with namespace authentication. But cryptographic tool signing still absent. The gap between 'scan for problems' and 'prevent problems' is narrowing — but 30+ CVEs filed in 60 days shows the threat is accelerating faster than defenses."
last_refreshed: 2026-05-02
---

AI agent supply chain security went from theoretical to crisis in April 2026. **OX Security's "Mother of All AI Supply Chains" disclosure** (April 15, 2026) revealed a systemic remote code execution flaw baked into MCP's STDIO interface — the command executes regardless of whether the process starts successfully. The impact: **200,000 vulnerable server instances, 7,000+ publicly accessible servers, 150 million+ downloads affected.** Anthropic confirmed the behavior is "by design" and declined to modify the protocol. CVE-2026-30623 was assigned for LiteLLM alone. The affected projects read like a who's-who of AI tooling: LiteLLM, LangChain, LangFlow, Flowise, LettaAI, LangBot, Windsurf, Cursor.

The ecosystem's response has been swift: **runtime security tools exploded**, the MCP Authorization Specification was formalized with OAuth 2.1, and an official MCP Registry launched. But 30+ CVEs filed in just 60 days (January–February 2026) showed the threat was already accelerating before the OX disclosure made headlines.

This review covers tools that **secure the MCP ecosystem itself** — scanning servers for malicious behavior, providing runtime enforcement, vetting dependencies, generating SBOMs, and providing infrastructure for safe MCP server distribution. For tools that scan your *application* code (SAST, SCA, IaC), see our [Code Security MCP review](/reviews/code-security-mcp-servers/). For physical supply chain logistics, see our [Logistics & Supply Chain review](/reviews/logistics-supply-chain-mcp-servers/).

The headline findings: **Snyk Agent Scan** (1,800 stars) still leads pre-deployment scanning with its new Skill Inspector web tool. **Pipelock** (342 stars, NEW) is the first true runtime firewall — sitting inline between agent and network with DLP, SSRF protection, and bidirectional MCP scanning. **MCP Guardian** (190+ stars, NEW) enables real-time approval/denial of individual tool calls. **Docker MCP Gateway** (1,300 stars) added interceptors for fine-grained policy enforcement. The category has shifted from "scan before deployment" to "enforce at runtime" — a critical maturation. Part of our **[Security & Compliance MCP category](/categories/security-compliance/)**.

## MCP Server / Agent Scanners

### Snyk Agent Scan (formerly Invariant Labs mcp-scan)

| Detail | Info |
|--------|------|
| [snyk/agent-scan](https://github.com/snyk/agent-scan) | ~1,800 stars |
| License | Apache-2.0 |
| Language | Python |
| Latest | v0.4.6 (April 2026) |
| Originally | [invariantlabs-ai/mcp-scan](https://github.com/invariantlabs-ai/mcp-scan) |

The definitive MCP security scanner. Started as Invariant Labs' mcp-scan (which pioneered tool poisoning detection research), then acquired by Snyk and expanded into a comprehensive agent security platform. Announced alongside Snyk's broader Agent Security solution at RSAC 2026 (March).

### What Works Well

**Auto-discovery is the killer feature.** Agent Scan finds MCP configurations across Claude, Cursor, Windsurf, Gemini CLI, and other agents automatically — you don't need to manually point it at config files. This is critical because most developers don't know exactly which MCP servers are installed across their tools.

**Broad threat detection.** 15+ distinct risk categories spanning two domains. MCP-specific: prompt injection, tool poisoning, tool shadowing, toxic flows. Skill-specific: prompt injection, malware payloads, untrusted content, credential handling, hardcoded secrets. The tool poisoning detection — identifying hidden malicious instructions in tool descriptions that are invisible to users but visible to AI models — was pioneered by the Invariant Labs team.

**Three operational modes.** CLI scanning for immediate assessment (`snyk-agent-scan`), continuous background monitoring for enterprise environments (MDM/CrowdStrike integration reporting to Snyk Evo), and **NEW: runtime proxy mode** that monitors and guardrails MCP traffic in real time — scanning for prompt injections, malicious code, and suspicious downloads as they happen.

**Skill Inspector (NEW).** A free, self-service web tool at labs.snyk.io that lets developers and security teams detect malicious skills, insecure configurations, and leaked secrets **before installation**. Instant risk visibility without CLI setup. This partly addresses the "agent can't self-assess" criticism.

### What Doesn't Work Well

**Not an MCP server itself.** Agent Scan is primarily a CLI tool and background daemon, not something your AI agent can invoke via MCP. The runtime proxy mode is the closest to inline protection, but the agent still can't self-assess through MCP.

**Snyk ecosystem deepening.** v0.4.4 added Snyk API Key requirement for analysis; v0.4.6 added Snyk CLI support. The tool works standalone for basic scanning, but advanced features increasingly require Snyk integration. Announced at RSAC alongside Snyk Evo AI-SPM (GA).

### Cisco MCP Scanner

| Detail | Info |
|--------|------|
| [cisco-ai-defense/mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner) | ~830 stars |
| License | Apache-2.0 |
| Language | Python |
| Latest | v4.6.0 (April 14, 2026) |

Cisco's open-source contribution to MCP security. The multi-engine architecture is the distinguishing feature. Actively maintained with rapid releases — v4.5.0 (April 6) and v4.6.0 (April 14) show continued investment.

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
| Latest | v2026.5.5 (April 3, 2026) |
| Analyzers | 79 (up from 76) |
| Detection rules | 9,600+ (up from 7,300+) |

An AI-first security scanner with specific MCP and AI agent security rules. Unlike the focused MCP scanners above, Medusa is a general security scanner that includes MCP-specific capabilities.

**Notable:** Covers repo poisoning detection for AI/ML, LLM agents, and MCP servers. 79 specialized analyzers with 9,600+ detection patterns (up 31% from 7,300+). Now includes **200 CVE detection rules including MCP-Remote RCE** — directly relevant to the OX Security STDIO disclosure. 11,500+ PyPI downloads. Can scan any GitHub repo directly with `medusa scan --git user/repo`. The breadth is impressive but the MCP-specific coverage is a subset of the overall tool.

**AGPL-3.0 license** means any modifications or derivative works must also be released under AGPL — important for enterprise adoption where copyleft can be a dealbreaker.

## Runtime Security — Firewalls, Proxies, and Inline Enforcement

*New section since our March 2026 review. The biggest gap identified previously — "no runtime policy enforcement" — is now being actively filled.*

### Pipelock (NEW)

| Detail | Info |
|--------|------|
| [luckyPipewrench/pipelock](https://github.com/luckyPipewrench/pipelock) | ~342 stars |
| License | Free community edition (paid multi-agent) |
| Language | — |
| Latest | v2.3.0 |
| Patterns | 48 built-in DLP patterns |

**The first true AI agent firewall.** Pipelock sits inline between your AI agent and the network — it's not a pre-deploy scanner like Snyk or Cisco, it's a **runtime proxy** that inspects tool descriptions on every session, arguments on every call, and responses on every reply. This is the category's most significant new entrant since our original review.

### What Works Well

**Bidirectional MCP scanning.** Scans both inbound (tool descriptions, responses) and outbound (arguments, data flows) MCP traffic. Detects tool poisoning, prompt injection, and exfiltration in real time — not retrospectively.

**DLP with 48 built-in patterns.** API keys, tokens, credentials, cryptocurrency keys, environment variable secrets, financial identifiers — all with checksum validation. This directly addresses the credential exposure problem (53% of MCP servers use static API keys).

**SSRF protection.** Blocks outbound requests to internal networks, cloud metadata endpoints, and other SSRF targets. Critical given the OX Security disclosure's finding of unauthenticated UI injection in AI frameworks.

**Compliance mapping.** EU AI Act mapping, OWASP mapping, and security assurance documentation — rare for a tool this early. Shows enterprise-grade thinking from day one.

**GitHub Actions integration.** `pipelock-agent-security-scan` action available in the GitHub Marketplace for CI/CD pipeline integration.

### What Doesn't Work Well

**New and unproven at scale.** 342 stars is healthy for a new tool but doesn't represent enterprise-scale validation yet. The free/paid split (multi-agent coordination requires paid plans) may limit adoption in larger organizations testing it out.

**Not an MCP server itself.** Like most tools in this category, Pipelock operates as infrastructure *around* MCP, not as an MCP server that agents can invoke.

### MCP Guardian (NEW)

| Detail | Info |
|--------|------|
| [eqtylab/mcp-guardian](https://github.com/eqtylab/mcp-guardian) | ~190+ stars |
| License | — |
| Language | Rust |

A security-first proxy that gives humans real-time control over their LLM's MCP activity. Where Pipelock is automated enforcement, MCP Guardian is human-in-the-loop approval.

### What Works Well

**Real-time tool call approval/denial.** Every MCP tool invocation can be approved or denied individually in real time. This is the most granular human-in-the-loop security control available — you see exactly what the agent wants to do before it does it.

**Message logging.** Full traces of all MCP server activity, providing audit trails and visibility into agent behavior.

**Configuration management.** Manages multiple MCP server configurations, allowing quick switching between server collections — useful for switching between development (permissive) and production (restricted) profiles.

**Rust implementation.** Memory-safe, fast, and suitable for high-throughput proxy workloads.

### What Doesn't Work Well

**Manual approval doesn't scale.** Approving individual tool calls works for security-sensitive operations but becomes a bottleneck for high-volume agent workflows. Automated scanning (marked "Coming Soon") would address this.

**Lower adoption than Pipelock.** At 190+ stars vs. Pipelock's 342, MCP Guardian has less community validation — though the Rust implementation and focused scope make it a solid choice for teams wanting human oversight.

## Secure MCP Infrastructure

### Docker MCP Gateway

| Detail | Info |
|--------|------|
| [docker/mcp-gateway](https://github.com/docker/mcp-gateway) | ~1,300 stars |
| License | MIT |
| Language | Go |
| Latest | v0.40.2 (February 27, 2026) |
| Catalog | 300+ verified servers |

Docker's approach to MCP security is infrastructure-level: **don't just scan servers, containerize them**. The MCP Gateway runs MCP servers in isolated Docker containers with restricted privileges, network access, and resource usage.

### What Works Well

**Defense in depth.** Every MCP server image in the Docker Catalog is built by Docker, digitally signed, and includes an SBOM. On pull, Docker verifies provenance and runs supply-chain checks via Docker Scout. At runtime, containers get 1 CPU, 2 GB memory, and no host filesystem access by default. This is the most comprehensive security posture available for running MCP servers.

**Interceptors (NEW).** MCP Gateway interceptors provide fine-grained policy enforcement, authentication, and request modification at the gateway level. Secret blocking scans inbound and outbound payloads for sensitive information (API tokens, credentials), preventing accidental or malicious exposure. Docker reports 60% reduction in security incidents for organizations using interceptors.

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

Understanding why these tools exist requires understanding the attacks — which escalated from theoretical to confirmed-at-scale in April 2026:

- **STDIO RCE (NEW — April 2026).** OX Security's "Mother of All AI Supply Chains" disclosure: MCP's STDIO interface executes any command passed to it, regardless of whether a valid server starts. Four exploitation families: unauthenticated UI injection in AI frameworks, hardening bypasses in "protected" tools (Flowise), zero-click prompt injection in AI coding IDEs (Windsurf, Cursor), and malicious package distribution through MCP marketplaces. **200,000 vulnerable instances. Anthropic: "by design."**
- **Tool poisoning:** Malicious instructions hidden in MCP tool descriptions that are invisible to users but executed by AI models. Invariant Labs demonstrated this could silently exfiltrate entire WhatsApp conversation histories.
- **Rug pulls:** Clean MCP servers submitted for approval, then updated with malicious tool descriptions. Most MCP clients don't re-verify descriptions after initial connection.
- **Typosquatting:** Counterfeit packages (like `postmark-mcp`) that mimic legitimate MCP servers. One caught package was BCC'ing every outgoing email to an attacker.
- **Credential exposure:** 88% of MCP servers require credentials, 53% use static API keys/PATs that are rarely rotated, and only 8.5% use OAuth. (The new MCP Authorization Specification addresses this, but adoption is gradual.)
- **Toxic flows:** Multi-server environments where data from one compromised server poisons another trusted server's context.
- **CVE flood (NEW).** 30+ CVEs filed targeting MCP servers, clients, and infrastructure between January–February 2026 — ranging from path traversals to a CVSS 9.6 RCE in a package with nearly half a million downloads.

A scan of 1,808 MCP servers found 66% had security findings. This isn't a theoretical threat — it's the current state of the ecosystem, now confirmed at massive scale by the OX Security disclosure.

## Protocol-Level Security Improvements

*New since our March 2026 review. The protocol itself is getting security primitives.*

**MCP Authorization Specification (OAuth 2.1).** The MCP spec now defines a standardized authorization framework: MCP servers act as OAuth 2.1 resource servers, MCP hosts act as OAuth clients on behalf of users. Resource Indicators (RFC 8707) are mandated — tokens are tightly scoped and only valid for the specific MCP server they were issued for. Role-based authorization enables fine-grained tool access control via annotations like `@RolesAllowed`.

**Official MCP Registry** ([registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io/)). The Agentic AI Foundation launched an official registry with namespace authentication — server names follow reverse DNS format (e.g., `io.github.username/server-name`) tied to verified GitHub accounts or domains. Publisher verification and automated security scanning for submitted servers are included.

**Limitation:** Enforcement is name-based, not cryptographic. There is no cryptographic signing or attestation tying a server name to a specific verified binary or endpoint. This means the registry reduces risk but cannot prevent a compromised publisher from pushing malicious updates.

## What's Missing

- **No unified MCP security server.** The best scanners (Snyk, Cisco) don't operate as MCP servers. The best MCP server (agent-bom, 32 tools) has minimal adoption. There's no "install this one MCP server and your agent can self-assess its security."
- **~~No runtime policy enforcement.~~** ~~Docker Gateway provides container-level isolation, but there's no protocol-level mechanism.~~ **PARTIALLY CLOSED:** Pipelock (342 stars) provides runtime inline enforcement; MCP Guardian (190+ stars) provides human-in-the-loop approval; Docker interceptors provide gateway-level policy. But no *protocol-level* permission declaration standard exists yet.
- **No cryptographic tool signing.** Tool descriptions can still change between connections (enabling rug pulls). The MCP protocol has no signing or pinning mechanism. The official registry uses name-based verification, not cryptographic attestation. **This remains the single biggest gap.**
- **~~No MCP server registry.~~** **CLOSED:** The official MCP Registry launched at registry.modelcontextprotocol.io with namespace authentication and publisher verification.
- **No SLSA or Sigstore integration.** Software supply chain standards like SLSA (Supply chain Levels for Software Artifacts) and signing via Sigstore/Cosign haven't been adopted by the MCP ecosystem. Organizations are recommended to provide cryptographic signatures and SBOMs, but this is advisory, not enforced.
- **STDIO RCE remains "by design."** The OX Security disclosure's core finding — that STDIO commands execute regardless of whether a valid MCP server starts — was confirmed as intentional by Anthropic. Sanitization is the developer's responsibility, but many frameworks (LiteLLM, LangChain, etc.) failed to sanitize. The attack surface persists.

## Rating: 4 / 5

**The good:** The category has matured dramatically in 45 days. Runtime security arrived — Pipelock (342 stars) and MCP Guardian (190+ stars) close the critical gap of "no inline enforcement." Docker interceptors add gateway-level secret blocking. The MCP Authorization Specification brings OAuth 2.1 with Resource Indicators. The official MCP Registry provides publisher verification. Snyk's Skill Inspector makes security assessment frictionless. Cisco Scanner hit v4.6 with continued active maintenance. Major vendors (Snyk, Cisco, Docker) remain committed.

**The bad:** The OX Security disclosure proved the ecosystem's worst fears — 200,000 servers vulnerable to RCE via a "by design" flaw that Anthropic won't fix. 30+ CVEs in 60 days shows threats accelerating faster than defenses. Cryptographic tool signing still doesn't exist in the protocol. Most security tools still operate *outside* MCP rather than as MCP servers. The official registry uses name-based verification (not cryptographic attestation), meaning a compromised publisher can still push malicious updates undetected.

**Bottom line:** Upgraded from 3.5 to 4.0. The arrival of runtime security tools (Pipelock, MCP Guardian, Docker interceptors) addresses our biggest criticism from the original review. The MCP Authorization Specification and official registry show the protocol is maturing its security story. But the OX Security disclosure's "by design" RCE flaw — and Anthropic's refusal to address it — means the ecosystem is building security *around* a protocol that has a known, unfixed, architectural vulnerability at its core. The gap is narrowing, but the foundation remains concerning.

---

---

## Refresh History {#refresh-history}

**2026-05-02 (first refresh):** THE OX SECURITY DISCLOSURE: "Mother of All AI Supply Chains" (April 15, 2026) revealed systemic RCE in MCP STDIO interface — 200K servers, 150M+ downloads, CVE-2026-30623 for LiteLLM, affects LangChain/LangFlow/Flowise/LettaAI/Cursor/Windsurf. Anthropic confirmed "by design," declined to fix. RUNTIME SECURITY EXPLODED: Pipelock NEW 342 stars v2.3.0 — first AI agent firewall, DLP 48 patterns, SSRF, bidirectional MCP scanning, tool poisoning, prompt injection blocking, GitHub Actions, EU AI Act mapping. MCP Guardian NEW 190+ stars — Rust proxy, real-time tool call approval/denial, message logging. Docker MCP Gateway added interceptors (policy enforcement, secret blocking, claims 60% incident reduction), holds 1,300 stars v0.40.2. Snyk Agent Scan 1,900→1,800 stars v0.4.6 — NEW Skill Inspector web tool, runtime proxy mode, MDM/CrowdStrike background monitoring, Snyk CLI integration, RSAC 2026 Agent Security launch. Cisco Scanner 850→830 stars v4.6.0 (April 14) actively maintained. Medusa 76→79 analyzers, 7,300→9,600+ rules, 200 CVE detection patterns including MCP-Remote RCE. PROTOCOL IMPROVEMENTS: MCP Authorization Specification formalized OAuth 2.1 + Resource Indicators (RFC 8707) + role-based access. Official MCP Registry launched at registry.modelcontextprotocol.io — namespace auth, publisher verification (name-based, not cryptographic). 30+ CVEs filed in 60 days (Jan–Feb 2026). Gaps: STDIO RCE unfixed ("by design"), no cryptographic tool signing, no SLSA/Sigstore. Rating upgraded 3.5→4/5.
