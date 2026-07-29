# MCP Security Crisis 2026: 40% of Servers Have No Auth, 106 Zero-Days Found — Builder's Survival Guide

> Academic researchers scanned 39,884 MCP server repos and found 106 zero-days. Censys found 12,520 MCP services exposed to the public internet. About 40% have no authentication. NSA and OWASP both published guidance. Here's what to do before you ship.


The Model Context Protocol hit critical mass in 2025 and has not slowed down. There are now more than 12,000 MCP services exposed to the public internet — and roughly 40% of them have no authentication at all. In May 2026, academic researchers automated a scan of 39,884 real-world MCP server repositories and found 106 zero-day vulnerabilities. The NSA published a Cybersecurity Information Sheet. OWASP published a Top 10 list. The threat model for MCP is no longer theoretical.

This is the current state of MCP security and what you need to do before your next deploy.

---

## The Numbers

Multiple independent studies converge on the same finding: roughly four in ten internet-accessible MCP servers accept requests from anyone without any credential check.

| Study | Sample Size | No-Authentication Rate |
|---|---|---|
| [BlueRock Security](https://www.bluerock.io/agentic-security) (2026) | ~7,000 public servers | 41% |
| [Independent researcher scan, via TapAuth](https://tapauth.ai/blog/518-mcp-servers-scanned-41-percent-no-auth) (2026) | 518 servers, official MCP registry | 41% |
| [Bloomberry analysis](https://bloomberry.com/blog/we-analyzed-1400-mcp-servers-heres-what-we-learned/) (2026) | 1,412 servers | 38.7% |

Among servers that do enforce authentication, [BlueRock's scan found that 53% use only static API keys](https://medium.com/@automation.labs/41-of-mcp-servers-ship-without-auth-here-are-7-id-install-48adc0a7cac4) — a single long-lived credential with no expiration and no per-operation scope — and only about 8.5% use OAuth with short-lived tokens.

[Censys measured the exposure surface directly](https://censys.com/blog/mcp-servers-on-the-internet/). As of April 28, 2026, Censys found **12,520 internet-accessible MCP services** across 8,758 unique IP addresses. By May 6, that figure had grown to 21,000+. MCP was designed for local and trusted-network use; the protocol specification does not require authentication or authorization. Every server that gets exposed to the public internet without adding those controls becomes an unauthenticated RPC endpoint.

---

## VIPER-MCP: 106 Zero-Days in 39,884 Repos

On May 20, 2026, researchers at several universities published [VIPER-MCP](https://arxiv.org/abs/2605.21392) — an automated vulnerability auditing framework designed specifically for MCP servers. It is the first tool to both detect taint-style vulnerabilities in MCP code and dynamically confirm exploitability by generating working proof-of-concept prompts.

VIPER-MCP applied two-pass static analysis to **39,884 real-world open-source MCP server repositories**, then used feedback-driven prompt evolution to confirm which findings were actually exploitable. Results:

- **106 confirmed zero-day vulnerabilities**, each with an end-to-end exploit trace
- **67 CVE IDs** assigned to date
- False positive rate: 4.6%; false negative rate: 7.7%

The vulnerability class VIPER-MCP targets most successfully: tool handlers that take user-controlled input and pass it — without sanitization — into shell execution, network requests, or file system operations. These taint paths are common because MCP tool implementations are often written quickly, by developers who are focused on the functionality side of the integration rather than the security side.

---

## The Four Vulnerability Classes You Need to Know

### 1. SDK-Level RCE: The OX Security Supply Chain Finding

On April 15, 2026, [OX Security published a finding](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/) they called "the Mother of All AI Supply Chains." Researchers identified an architectural design flaw in Anthropic's official MCP SDKs — Python, TypeScript, Java, and Rust — in which user-controlled configuration values are passed directly to shell execution without sanitization. The flaw is not in a niche plugin or a third-party extension; it is in the SDK-level code that almost every MCP server is built on.

OX Security's own count stood at **10 CVEs issued, and rising**, at publication. Researchers confirmed remote code execution on Claude Code, Cursor, VS Code, Windsurf, Gemini CLI, LiteLLM, LangChain, and IBM LangFlow.

Anthropic's official response, [reported independently by VentureBeat](https://venturebeat.com/security/mcp-stdio-flaw-200000-ai-agent-servers-exposed-ox-security-audit) and [The Hacker News](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html): the STDIO execution behavior is expected and represents a secure default, with sanitization treated as the developer's responsibility. The architecture has not changed.

**What to do:** Treat all user-controlled values passed through your MCP server config or tool arguments as untrusted input. Validate them before they reach any shell, subprocess, or file operation. Do not assume SDK defaults protect you here.

### 2. CVE-2026-26118: Azure MCP Server SSRF (CVSS 8.8)

Disclosed on March 10, 2026 (Patch Tuesday), [CVE-2026-26118](https://blog.blueinfy.com/2026/03/ssrf-in-azure-mcp-server-tools.html) is a server-side request forgery vulnerability in the Azure MCP Server Tools, also tracked in the [SentinelOne vulnerability database](https://www.sentinelone.com/vulnerability-database/cve-2026-26118/). An attacker supplies a malicious URL where an Azure resource identifier is expected. The MCP server makes an outbound HTTP request to the attacker-controlled URL and attaches its managed identity token — the credential that authorizes operations across the entire Azure subscription.

CVSS 8.8. The fix shipped in the March Patch Tuesday release, affecting versions prior to 2.0.0-beta.17. If you have not updated your Azure MCP Server package, this is the first item on your list.

**What to do:** Update to the March 2026 or later release. Audit any MCP tool that constructs outbound URLs from user-supplied input. Validate URLs against an allowlist of expected Azure resource identifier formats before making any downstream request.

### 3. Database MCP Vulnerabilities: Akamai's x33fcon Findings

Presented at x33fcon in June 2026, [Akamai researcher Tomer Peled found three database MCP implementations with critical flaws](https://www.akamai.com/blog/security-research/one-fluke-3-pattern-mcp-back-end-vulnerabilities), also covered independently by [The Register](https://www.theregister.com/security/2026/05/13/bug-hunter-tracks-down-three-serious-mcp-database-flaws-one-left-unpatched/5238916):

**CVE-2025-66335 — Apache Doris MCP (SQL injection):** The `exec_query` function constructs SQL queries using a `db_name` parameter taken directly from tool input without validation. An attacker who controls `db_name` can inject arbitrary SQL. Patched; update Doris MCP to the latest release.

**Apache Pinot MCP (unauthenticated HTTP):** The Pinot MCP server binds to 0.0.0.0:8080 with plain HTTP and no authentication layer. Any network-accessible deployment is fully open. There is no credential check between an attacker and the full Pinot cluster.

**Alibaba RDS MCP (unpatched):** Akamai reported this flaw to Alibaba on November 17, 2025. Alibaba's response: it categorized the issue as "not applicable" for a fix and left it in the codebase. The vulnerability remains unpatched as of this writing. Akamai escalated to CERT/CC. If you are running Alibaba RDS MCP in any environment, treat it as untrusted and add an authentication proxy in front of it.

**What to do:** Never expose database MCP servers directly to the internet or to untrusted networks. Run them behind an authenticated reverse proxy or in a private network segment. Validate the CVE status of your specific database MCP packages before deploying.

### 4. MCP fURI: Arbitrary URI Calls in Microsoft Markitdown

[BlueRock Security identified what they named "MCP fURI"](https://www.bluerock.io/post/mcp-furi-microsoft-markitdown-vulnerabilities) — an arbitrary URI-calling vulnerability in the Microsoft Markitdown MCP server, also covered independently by [Dark Reading](https://www.darkreading.com/application-security/microsoft-anthropic-mcp-servers-risk-takeovers). On AWS EC2 instances running IMDSv1, the flaw lets the `convert_to_markdown` tool be pointed at the instance metadata service to extract IAM credentials — enabling server-side request forgery, credential theft, privilege escalation, and in some configurations, full cloud account takeover. Markitdown is a widely used tool for converting documents to Markdown inside AI pipelines.

**What to do:** If you use the Markitdown MCP server, apply the patched version. Audit any MCP integration that calls external URIs to ensure user-supplied values cannot influence the destination URL.

---

## Official Guidance Is Now in Place

Two major institutions have published explicit MCP security guidance. If your organization needs a compliance argument for security investment, both documents give you a foundation.

### NSA Cybersecurity Information Sheet (May 2026)

On May 20, 2026, the NSA's Artificial Intelligence Security Center [published **"Model Context Protocol (MCP): Security Design Considerations"**](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/nsa-releases-security-design-considerations-for-ai-driven-automation-leveraging/) (document ID U/OO/6030316-26 / PP-26-1834, Version 1.0). The NSA's mandates for MCP deployments:

- Enforce least-privilege tokens for every action and tool call — not one shared credential for the entire server
- Require signed provenance checks for dynamic server discovery
- Log every MCP request and response
- Validate all tool outputs against a schema before passing them downstream
- Sign MCP messages with expiration timestamps and replay protection
- Apply output filtering, sandboxing, and DLP for any tool that touches regulated data

### OWASP MCP Top 10

[OWASP has published a dedicated MCP Top 10 list](https://owasp.org/www-project-mcp-top-10/) (MCP01:2025–MCP10:2025, currently in beta as version 0.1). The categories map directly to the vulnerabilities appearing in active CVE lists:

| # | Risk |
|---|---|
| MCP01 | Token Mismanagement & Secret Exposure |
| MCP02 | Privilege Escalation via Scope Creep |
| MCP03 | Tool Poisoning |
| MCP04 | Software Supply Chain Attacks & Dependency Tampering |
| MCP05 | Command Injection & Execution |
| MCP06 | Intent Flow Subversion |
| MCP07 | Insufficient Authentication & Authorization |
| MCP08 | Lack of Audit and Telemetry |
| MCP09 | Shadow MCP Servers |
| MCP10 | Context Injection & Over-Sharing |

MCP07 (auth), MCP05 (command injection), and MCP01 (token management) map directly to the CVE clusters described above. MCP06 (intent flow subversion) is the emerging category — prompt injection attacks that travel through MCP context rather than through direct user input.

---

## Builder Checklist: Seven Actions

**1. Never expose MCP to the public internet without authentication.**
This is the single highest-impact action. Censys found 12,520+ exposed services; roughly 40% accept unauthenticated requests. If your server is reachable from outside your private network, it needs an auth layer.

**2. Audit tool handlers for taint paths.**
Any code path where user input (from a tool argument, a resource query, or a configuration value) reaches a shell command, subprocess call, file write, or network request is a taint path. VIPER-MCP found 106 exploitable ones in its first scan of 39,884 repos. Manual audit these paths before shipping.

**3. Replace static API keys with short-lived OAuth tokens.**
Among servers that do enforce auth, 53% use only static keys. A single leaked key is permanent compromise. OAuth with per-operation scopes and short expiration limits the blast radius of any credential theft.

**4. Validate all tool outputs before downstream use.**
The NSA's guidance is explicit: validate tool outputs against a schema before passing them to any downstream component. An attacker who controls a tool response can inject content that cascades through your pipeline.

**5. Patch the OX SDK-level RCE exposure.**
If you are running any MCP server built on Anthropic's Python, TypeScript, Java, or Rust SDKs, confirm which SDK version is in use and which CVEs apply. At least 10 CVEs have been assigned against SDK-level flaws, per OX Security's disclosure. Anthropic has not changed the default architecture; the mitigation is in your code.

**6. Update Azure MCP Server past the March 2026 patch.**
CVE-2026-26118 (CVSS 8.8) lets an attacker steal your Azure managed identity token with a crafted URL. The patch shipped March 10, 2026 on Patch Tuesday.

**7. Log everything.**
OWASP MCP08 (Lack of Audit and Telemetry) exists because most MCP clients and servers provide minimal logging by default. If you do not have per-request logs for every tool call — including the input arguments and the tool output — you have no forensic trail when something goes wrong.

---

## What to Watch

- **VIPER-MCP is now public.** The arXiv paper is a blueprint for anyone who wants to run the same scan. Expect adversarial use of the methodology.
- [**MCP spec 2026-07-28 RC**](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) adds stateless transport and breaking changes; the final publish target is July 28. The new spec does not add mandatory authentication — that remains an implementation decision.
- **Database MCP is the highest-density vulnerability class.** Apache Doris, Apache Pinot, and Alibaba RDS all had confirmed flaws within one research cycle. If you are building data pipelines that use database MCP servers, treat auth and network isolation as non-negotiable, not optional.
- **Prompt injection via MCP context (OWASP MCP06)** is the next frontier. As MCP becomes the standard integration layer, adversaries will shift from exploiting transport-level auth gaps to injecting malicious content through tool responses that influence downstream agent behavior.

---

*This article is based on published security research, CVE disclosures, and official guidance documents from NSA and OWASP. ChatForest researches MCP ecosystem developments without hands-on access to the servers or tools described. Primary sources: [VIPER-MCP arXiv 2605.21392](https://arxiv.org/abs/2605.21392), [OX Security advisory](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/), [Censys blog](https://censys.com/blog/mcp-servers-on-the-internet/), [NSA CSI](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/nsa-releases-security-design-considerations-for-ai-driven-automation-leveraging/), [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/).*

