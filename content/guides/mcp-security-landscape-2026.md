---
title: "The MCP Security Crisis: 36 CVEs, 82% Path Traversal, and What the Data Says"
date: 2026-04-05T14:00:00+09:00
description: "A data-driven analysis of MCP security in 2026 — 36 NVD-confirmed CVEs, ecosystem audits showing 82% path traversal exposure, 36.7% SSRF rates, the OWASP MCP Top 10, real-world supply chain compromises, and the tools and frameworks emerging to fix it."
content_type: "Guide"
card_description: "36 NVD-confirmed CVEs, 82% path traversal rates, real supply chain attacks, and the OWASP MCP Top 10. Here's what the data actually says about MCP security in 2026."
last_refreshed: 2026-04-05
---

MCP adoption is accelerating. So are MCP vulnerabilities.

In the first 60 days of 2026, security researchers filed over 30 CVEs against MCP servers, clients, and infrastructure. The NVD now lists 36 confirmed CVEs with "Model Context Protocol" in the description. Ecosystem audits of thousands of servers reveal that basic security failures — path traversal, command injection, missing authentication — are the norm, not the exception.

This isn't a theoretical risk. The Postmark MCP npm package was backdoored to BCC every outgoing email to an attacker's domain, downloaded 1,500 times per week. The McpInject malware module deploys malicious MCP servers into AI coding assistant configs. Anthropic's own Slack MCP server had a zero-click data exfiltration vulnerability so severe that Anthropic archived the server rather than patching it.

This guide presents the data — the CVEs, the audit numbers, the real incidents — and the tools and frameworks emerging to address the problem. Our analysis draws on NVD records, published research, and ecosystem audit reports — we research and analyze rather than testing servers hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

For practical security advice on evaluating individual MCP servers, see our companion guide: [MCP Server Security: A Practical Guide for 2026](/guides/mcp-server-security/).

---

## The Numbers

Before diving into specifics, here's what the ecosystem-wide data looks like:

| Metric | Value | Source |
|--------|-------|--------|
| NVD-confirmed MCP CVEs | 36 | NVD search, April 2026 |
| CVEs filed in Jan-Feb 2026 | 30+ | MCP Security 2026 report |
| Path traversal exposure | 82% of 2,614 servers | Endor Labs audit |
| SSRF exposure rate | 36.7% of 7,000+ servers | BlueRock / Dark Reading |
| Code injection exposure | 67% of 2,614 servers | Endor Labs audit |
| Command injection exposure | 34% of 2,614 servers | Endor Labs audit |
| Servers with critical vulns | 33% of 1,000+ servers | Enkrypt AI scan |
| Servers using OAuth | 8.5% | Mindgard |
| Tool poisoning prevalence | 5.5% of servers in the wild | Invariant Labs |
| Auto-approve attack success | 84.2% | Invariant Labs |
| Exposed MCP servers on internet | 1,862 | Knostic |
| Exploit probability (10 plugins) | 92% | VentureBeat |
| Average security score (17 popular servers) | 34/100 | Industry audit |
| Servers lacking permission declarations | 100% of 17 audited | Industry audit |

These aren't cherry-picked numbers from obscure projects. The Endor Labs audit covered 2,614 MCP implementations. BlueRock scanned 7,000+ servers. The 82% path traversal figure means four out of five MCP servers use file operations in ways vulnerable to directory traversal attacks.

---

## The CVE Landscape

### Critical Vulnerabilities (CVSS 9.0+)

The most severe MCP CVEs reveal patterns that should concern anyone deploying MCP servers in production:

**CVE-2025-6514 — mcp-remote (CVSS 9.6):** OS command injection via crafted authorization endpoint URL. This package had 437,000+ downloads, making it the first MCP vulnerability with mass-scale impact. A malicious authorization endpoint URL could execute arbitrary OS commands on the user's machine.

**CVE-2025-34072 — Anthropic Slack MCP Server (CVSS 9.3):** Zero-click data exfiltration via Slack's automatic link unfurling. When an AI agent processed untrusted data, the server could be manipulated into leaking information without any user interaction. Anthropic archived the server two days after disclosure — it will never be patched.

**CVE-2025-49596 — MCP Inspector (CVSS 9.4):** RCE in Anthropic's own debugging tool, due to lack of authentication between the Inspector frontend and its proxy server. A drive-by attack from a malicious website could compromise developer machines.

**CVE-2026-32211 — Azure MCP Server (CVSS 9.1):** Disclosed April 3, 2026. The @azure-devops/mcp server on npm entirely lacks authentication — any unauthenticated network attacker can access configuration details, API keys, and project data. As of this writing, no patch is available.

**CVE-2026-23744 — MCPJam Inspector (CVSS 9.8):** RCE via HTTP endpoint listening on 0.0.0.0, exposing the server to the network rather than localhost only.

### The Command Injection Pattern

43% of the 30+ CVEs filed in early 2026 involved shell or exec injection — MCP servers passing user-controlled input directly to system commands without sanitization. Examples span Android debug bridges (CVE-2025-59834), Kubernetes tools (CVE-2025-53355), translation services (CVE-2025-53832), and game engines (CVE-2026-25546).

This isn't sophisticated exploitation. These are textbook CWE-78 vulnerabilities — the kind that would fail a basic code review in any other context.

### SDK-Level Vulnerabilities

The official MCP SDKs themselves have had significant security issues:

- **CVE-2025-66414 & CVE-2025-66416:** Both the TypeScript SDK (< 1.24.0) and Python SDK (< 1.23.0) lacked DNS rebinding protection. Malicious websites could pivot through the browser to reach localhost-bound MCP servers.
- **CVE-2025-53365 & CVE-2025-53366:** Python SDK session data leaks and unhandled exceptions (CVSS 8.7).
- **CVE-2026-25536:** TypeScript SDK cross-client response data leak (CVSS 7.1).
- **CVE-2026-33946:** Ruby SDK session hijacking (CVSS 8.2).
- **CVE-2026-34742:** Go SDK DNS rebinding (CVSS 7.6), disclosed April 2, 2026.

When the protocol's own reference implementations have DNS rebinding and session hijacking vulnerabilities, it signals that security was not the primary design constraint.

---

## Real-World Incidents

These aren't hypothetical attacks. These happened.

### Postmark MCP Supply Chain Attack (September 2025)

A backdoored Postmark MCP npm package silently BCC'd every outgoing email to an attacker-controlled domain. The package was downloaded 1,500 times per week and used in hundreds of workflows before discovery. This was the first confirmed real-world MCP supply chain compromise.

### McpInject Malware (March 2026)

The McpInject module deploys malicious MCP servers and injects them into AI coding assistant configurations, complete with embedded prompt injections designed to read sensitive files. Discovered as part of the Axios npm compromise wave.

### Anthropic Git MCP Server Exploit Chain (January 2026)

Three chained vulnerabilities (CVE-2025-68143, CVE-2025-68144, CVE-2025-68145) in Anthropic's own mcp-server-git achieve full RCE via malicious .git/config files. Anthropic — the company that created MCP — shipped a server vulnerable to a three-step exploit chain.

### GitHub MCP Integration Hijack (May 2025)

Invariant Labs demonstrated that malicious GitHub issues could hijack AI agents using GitHub MCP integrations, leaking private repository data.

### Asana MCP Privacy Breach (June 2025)

Customer data bled across MCP instances in Asana's integration. The MCP integration was pulled for two weeks while the issue was resolved.

### Supabase Cursor Agent Exploit (Mid-2025)

Attackers embedded SQL commands in support tickets to exfiltrate integration tokens from AI agents using Supabase MCP through Cursor IDE.

---

## The OWASP MCP Top 10

OWASP published a dedicated [MCP Top 10](https://owasp.org/www-project-mcp-top-10/) (currently in beta), identifying the ten most critical security risks specific to MCP deployments:

| # | Risk | What It Means |
|---|------|--------------|
| MCP01 | Token Mismanagement & Secret Exposure | Hard-coded credentials, long-lived tokens, secrets in model memory or logs |
| MCP02 | Privilege Escalation via Scope Creep | Permissions expand over time, granting capabilities beyond original intent |
| MCP03 | Tool Poisoning | Malicious instructions hidden in tool description metadata |
| MCP04 | Supply Chain Attacks | Compromised npm/PyPI packages, malicious connectors |
| MCP05 | Command Injection & Execution | Untrusted input passed to system commands without sanitization |
| MCP06 | Intent Flow Subversion | Indirect prompt injection through MCP context payloads |
| MCP07 | Insufficient Auth & AuthZ | Missing or weak authentication on MCP endpoints |
| MCP08 | Lack of Audit and Telemetry | No logging or monitoring of tool invocations |
| MCP09 | Shadow MCP Servers | Unauthorized, unmanaged MCP servers running in enterprise environments |
| MCP10 | Context Injection & Over-Sharing | Malicious content in shared memory; context reused across agents that should be isolated |

Microsoft has published a companion [Azure MCP Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) mapping each OWASP category to Azure implementation patterns.

The [Coalition for Secure AI (CoSAI)](https://www.oasis-open.org/2026/01/27/coalition-for-secure-ai-releases-extensive-taxonomy-for-model-context-protocol-security/) — an OASIS Open project with contributions from EY, Google, IBM, Meta, Microsoft, NVIDIA, PayPal, Snyk, and others — released a complementary taxonomy identifying 12 core threat categories and approximately 40 specific threats with concrete mitigations.

---

## Tool Poisoning: The MCP-Specific Attack

Tool poisoning deserves special attention because it's unique to the MCP threat model. Unlike traditional injection attacks, tool poisoning exploits the fact that AI models read tool metadata to decide which tools to use and how.

**How it works:** An attacker embeds malicious instructions in a tool's description metadata — the text that tells the AI model what the tool does. These instructions are invisible to human users reviewing tool lists but are processed by the model when selecting and invoking tools. A poisoned tool description might instruct the model to exfiltrate data, escalate privileges, or call other tools in unintended ways.

**The "rug pull" variant:** A tool establishes trust with benign behavior, then silently alters its description after the user has approved it. Standard MCP clients don't re-verify tool definitions on every invocation, so the changed behavior goes undetected.

**Prevalence:** Invariant Labs found that 5.5% of MCP servers in the wild exhibit tool poisoning vulnerabilities. When AI agents auto-approve tool calls (without human-in-the-loop confirmation), the attack success rate is 84.2%. With human approval, it drops below 5%.

**The OpenClaw case study:** OpenClaw — an MCP tool marketplace that launched in late 2025 and quickly reached 100,000+ GitHub stars — saw 8 critical CVEs in its first 6 weeks. A Koi Security audit of its skill marketplace found 824+ malicious skills among 10,700+ total submissions. Bitdefender estimated approximately 20% of submitted skills were malicious. 42,665 OpenClaw instances were found exposed on the internet.

---

## The Authentication Gap

Only 8.5% of MCP servers currently use OAuth, despite OAuth 2.1 being the required authentication mechanism in the MCP specification for HTTP-based transports since March 2025.

The timeline of auth changes in the spec reflects ongoing uncertainty:

- **March 2025:** OAuth 2.1 standardized in the spec
- **June 2025:** Split MCP servers from authorization servers; required Protected Resource Metadata (RFC 9728)
- **November 2025:** Client ID Metadata Documents became the registration method; PKCE made mandatory

Despite this, the MCP Dev Summit dedicated 6 of 95+ sessions to authentication, with OAuth 2.1 specification author Aaron Parecki present — a signal that the community acknowledges auth remains unsolved in practice.

Knostic found 1,862 MCP servers exposed directly to the internet. When they manually tested 119 of these, every single one exposed its internal tool inventory without requiring authentication.

---

## Shadow MCP: Enterprise Blind Spot

OWASP MCP09 addresses a growing enterprise concern: developers spinning up unapproved MCP servers for experimentation, often with default credentials and permissive configurations.

60% of organizations report lacking confidence in their ability to detect unauthorized AI deployments. These shadow MCP servers create data leakage risks, unauthorized access paths, and expanded attack surfaces that security teams can't monitor because they don't know the servers exist.

Qualys TotalAI now specifically targets shadow MCP detection, using network-level probes, host-level analysis, and supply-chain dependency scanning to find MCP servers that haven't gone through formal security review.

---

## Supply Chain Risk: The Math

VentureBeat reported a striking finding: deploying just 10 MCP plugins creates a 92% probability of exploitation. Three plugins exceed 50%. Even a single plugin carries a 9% exploit probability.

The MCP ecosystem is heavily reliant on npm and PyPI packages with all the supply chain risks that entails. There is no centralized, trusted MCP server registry with mandatory security review. The Postmark backdoor, the McpInject malware, and the mcp-remote command injection (CVE-2025-6514, 437K+ downloads) demonstrate that these aren't theoretical risks.

---

## Security Tools and Frameworks

The security tooling ecosystem is maturing rapidly:

### Scanning Tools

**[Invariant Labs MCP-Scan](https://invariantlabs.ai/blog/introducing-mcp-scan)** (now Snyk Agent Scan): The pioneer MCP security scanner. Detects tool poisoning, rug pulls, cross-origin escalation, and prompt injection. Includes Tool Pinning — tracking tool description hashes to detect silent modifications.

**[Cisco MCP Scanner](https://github.com/cisco-ai-defense/mcp-scanner):** Open-source scanner using three engines: Yara rules, LLM-as-judge, and Cisco AI Defense. Scans for malicious code and hidden threats before integration.

**[Enkrypt AI MCP Scan](https://www.enkryptai.com/mcp-scan):** Scanned 1,000+ servers, finding 33% had critical vulnerabilities averaging 5.2 per server. Provides CVSS scores and line-level references. CI/CD integration available.

**[Qualys TotalAI](https://www.qualys.com/apps/totalai):** Enterprise platform with layered MCP server detection — network probes, host-level discovery, and supply chain analysis.

### Hardened Infrastructure

**[Chainguard MCP Images](https://www.chainguard.dev/unchained/meet-chainguard-mcps-bringing-supply-chain-security-to-the-ai-era):** Distroless, zero-CVE container images for MCP servers. SLSA Level 3 compliant with build provenance and SBOM. Their mcp-grafana image ships at 18.83 MB with 0 CVEs versus 54.19 MB and 38 CVEs for the standard alternative.

**[Docker MCP Toolkit](https://www.docker.com/blog/mcp-toolkit-mcp-servers-that-just-work/):** 300+ verified MCP server container images with digital signatures, SBOMs, runtime isolation (1 CPU, 2 GB RAM per container), and no host filesystem access by default.

**[Cloudflare MCP Server Portals](https://blog.cloudflare.com/zero-trust-mcp-server-portals/):** Zero Trust gateway enforcing MFA, device posture checks, geographic restrictions, and DLP scanning on MCP traffic.

### Frameworks and Guidelines

- **[OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)** — The ten most critical MCP security risks (beta)
- **[OWASP Practical Guide for Secure MCP Server Development](https://genai.owasp.org/resource/a-practical-guide-for-secure-mcp-server-development/)** — Development best practices
- **[Microsoft Azure MCP Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** — OWASP mapping to Azure infrastructure
- **[CoSAI MCP Security Taxonomy](https://github.com/cosai-oasis/ws4-secure-design-agentic-systems/blob/main/model-context-protocol-security.md)** — 12 threat categories, ~40 threats, concrete mitigations
- **[MCP Specification Security Best Practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)** — Official spec guidance

---

## Enterprise Patterns Worth Noting

Two organizations have publicly shared detailed MCP security architectures:

**Pinterest** runs a production MCP ecosystem handling 66,000 monthly invocations from 844 users, saving approximately 7,000 hours per month. Their security model uses two-layer authorization (end-user JWTs plus service mesh identities), domain-specific MCP servers to limit blast radius, and mandatory Security, Legal/Privacy, and GenAI review before any server reaches production.

**Morgan Stanley** presented their approach at QCon London 2026: MCP servers deployed from CALM (Common Architecture Language Model) patterns with compliance guardrails — including a denied-symbols list blocking queries for specific financial instruments — and build-time validation gates using Spectral rulesets.

These aren't aspirational designs. They're running in production at companies where security failures have regulatory consequences.

---

## What This Means

The MCP security landscape in April 2026 reveals a protocol ecosystem growing faster than its security infrastructure can support. The core problems are well-understood — the OWASP MCP Top 10 categories are mostly traditional web security failures applied to a new context. Command injection, path traversal, missing authentication, and supply chain attacks aren't novel threats.

What makes MCP different is the **compounding effect**: AI agents chain tools together, and a vulnerability in one server can be exploited through prompt injection in another. The 92% exploit probability for 10-plugin deployments reflects this compounding — each additional MCP server doesn't just add its own risk, it multiplies the attack surface available to every other server the agent can access.

The tools and frameworks exist to address these problems. Organizations deploying MCP in production should be using container isolation, gateway-based security, OAuth 2.1 authentication, and at minimum one of the available scanning tools. The gap isn't in available solutions — it's in adoption.

---

## Further Reading

- [MCP Server Security: A Practical Guide for 2026](/guides/mcp-server-security/) — Our companion guide with hands-on security evaluation advice
- [The MCP Ecosystem in 2026](/guides/mcp-ecosystem-2026-state-of-the-standard/) — Broader ecosystem context
- [MCP Dev Summit 2026 Roundup](/guides/mcp-dev-summit-2026-guide/) — 23 of 95+ summit sessions focused on security
- [What Is MCP?](/guides/what-is-mcp/) — Protocol fundamentals
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) — The definitive risk taxonomy
- [MCP Reaches the IETF](/guides/mcp-ietf-standardization/) — IETF drafts addressing MCP security gaps, including the MCPS cryptographic security layer

---

*This guide presents publicly available CVE data, audit reports, and published research. We research and analyze — we do not test or exploit vulnerabilities. Last refreshed: April 5, 2026.*
