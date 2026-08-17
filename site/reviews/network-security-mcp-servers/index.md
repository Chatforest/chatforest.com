# Network Security & Monitoring MCP Servers — Packet Capture, Port Scanning, Pentesting, and Reconnaissance

> Network security MCP servers let AI agents capture packets, scan ports, run penetration tests, and perform reconnaissance.


Network security is one of the most powerful — and most dangerous — applications of MCP. AI agents that can capture packets, scan ports, run vulnerability assessments, and perform reconnaissance have enormous potential for security professionals. They also have enormous potential for misuse. Every server in this review should be used only with proper authorization on systems you own or have explicit permission to test. Part of our **[Security & Compliance MCP category](/categories/security-compliance/)**.

The headline finding: **enterprise adoption has arrived**. PortSwigger's Burp Suite MCP server has crossed **[1,073 stars](https://github.com/PortSwigger/mcp-server)** as of this audit (up from 795 in May). **[mukul975/cve-mcp-server](https://github.com/mukul975/cve-mcp-server)** has continued its rapid climb, now past **1,134 stars** — still one of the fastest-growing servers in the ecosystem. FuzzingLabs' mcp-security-hub has expanded from "20+ tools" to **38 bundled MCP servers covering 300+ offensive tools** with hardened Docker containers. New enterprise entrants have arrived: **Check Point** [launched its Workforce AI MCP server](https://github.com/CheckPointSW/workforce-ai-mcp/releases) (v1.0.0, May 10, 2026) covering Workforce AI and Browse Security, and **Command Zero** opened its Autonomous SOC platform via MCP (April 29). **[0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai)** has kept up its explosive growth, now past **1,599 stars** (up from 276 in May) and on release **v1.3.1**, which builds on the production-safe engagement flags added in v0.15.1. The security picture is also sobering: WireMCP's command injection issue is now formally **[CVE-2026-3959](https://nvd.nist.gov/vuln/detail/CVE-2026-3959)**, bx33661/Wireshark-MCP received **[CVE-2026-43901](https://nvd.nist.gov/vuln/detail/CVE-2026-43901)** (path traversal via attacker-controlled dest_dir parameter, CWE-22, CVSS 6.8), and BlueRock Security's ongoing scan of the public MCP server population — [12,000+ servers as of its latest published update](https://www.bluerock.io/post/mcp-security) — found 42% have command-injection flaws and 33% have SSRF/unbounded URI-fetch vulnerabilities.
## Packet Capture & Traffic Analysis

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [0xKoda/WireMCP](https://github.com/0xKoda/WireMCP) | ~570 | Python | 3 | stdio |
| [bx33661/Wireshark-MCP](https://github.com/bx33661/Wireshark-MCP) | ~200 | Python | Multiple | stdio |
| [khuynh22/mcp-wireshark](https://github.com/khuynh22/mcp-wireshark) | ~55 | Python | 5+ | stdio |
| [mixelpixx/Wireshark-MCP](https://github.com/mixelpixx/Wireshark-MCP) | — | Python | Multiple | stdio |

**[0xKoda/WireMCP](https://github.com/0xKoda/WireMCP)** (570 stars, Python, March 2025) remains the most popular Wireshark MCP server by adoption. Three tools: `capture_packets` (real-time traffic capture as JSON), `get_summary_stats` (protocol hierarchy statistics), and `get_conversations` (TCP/UDP conversation tracking). **However, this project is dormant** — no commits since July 2025 (13+ months as of this audit). The command injection vulnerability has been formally assigned **[CVE-2026-3959](https://nvd.nist.gov/vuln/detail/CVE-2026-3959)** (Medium, CVSS 5.3) — still unpatched. Stars continue growing organically but the codebase is unmaintained. Do not use in production.

**bx33661/Wireshark-MCP** (Python, created February 2026) is the **most active Wireshark MCP alternative** — combines Wireshark packet analysis with complementary network tools, available on PyPI. **Important caveat as of May 2026**: a **[path traversal vulnerability (CVE-2026-43901)](https://nvd.nist.gov/vuln/detail/CVE-2026-43901)** was disclosed (CWE-22, unrestricted path traversal via attacker-controlled dest_dir parameter, CVSS 6.8). Check for patches before deploying. If you're choosing a Wireshark MCP server today, this remains the strongest actively-maintained option — but verify the CVE status against the current release.

**khuynh22/mcp-wireshark** (55 stars, Python 3.10+, pip-installable via `pip install mcp-wireshark`) is the most polished Wireshark MCP server from an engineering standpoint. Live capture, PCAP file parsing, display filter support, stream following, and JSON export. Published on PyPI with proper packaging — no git cloning required. Cross-platform, typed, and tested. The only server with proper versioned releases.

**mixelpixx/Wireshark-MCP** combines Wireshark analysis with nmap scanning and threat intelligence lookups in a single server. AI-powered network troubleshooting that correlates packet data with vulnerability data. Less adopted but more ambitious in scope.

**Also notable**: kriztalz/SharkMCP (tshark-based capture and analysis) and sarthaksiddha/Wireshark-mcp (bridges low-level network data with AI understanding).

## Port Scanning & Network Diagnostics

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [dkruyt/mcp-nettools](https://github.com/dkruyt/mcp-nettools) | — | Python | 11 | stdio |
| [jsdelivr/globalping-mcp-server](https://github.com/jsdelivr/globalping-mcp-server) | ~63 | TypeScript | 5 | Streamable HTTP |
| [kumarprobeops/probeops-mcp-server](https://github.com/kumarprobeops/probeops-mcp-server) | — | TypeScript | 11-21 | stdio |
| [PhialsBasement/nmap-mcp-server](https://github.com/PhialsBasement/nmap-mcp-server) | ~49 | TypeScript | 1 | stdio (archived) |
| [patrickdappollonio/mcp-netutils](https://github.com/patrickdappollonio/mcp-netutils) | — | Go | 6+ | stdio + SSE |

**dkruyt/mcp-nettools** (Python, installable via uv) is the best all-in-one network diagnostics MCP server. **11 tools**: `nmap_scan`, `dns_lookup`, `dns_enum`, `whois_info`, `traceroute`, `port_check`, `ssl_scan`, `network_scan`, `ip_geolocation`, `http_headers`, and `my_public_ip`. Covers the most common network troubleshooting tasks in a single server — DNS, WHOIS, scanning, SSL analysis, and geolocation. If you want one server for everyday network work, this is it.

**[jsdelivr/globalping-mcp-server](https://github.com/jsdelivr/globalping-mcp-server)** (63 stars, TypeScript, backed by jsDelivr) is architecturally unique — a **remote MCP server** at `https://mcp.globalping.dev/mcp` that runs diagnostics from thousands of globally distributed probes. Five tools: ping, traceroute, DNS, MTR, and HTTP tests. No local installation needed. OAuth and API token authentication with **PKCE S256 validation** added in April 2026 for improved security. When you need to test how your service responds from different geographic locations, nothing else in the MCP ecosystem comes close. Streamable HTTP transport means it works with modern MCP clients without stdio overhead.

**kumarprobeops/probeops-mcp-server** (TypeScript, via npx) offers 11 free tools (21 with API key) including SSL checks, DNS lookups, ping, WHOIS, port checks, traceroute, latency tests, and geo-located web browsing. Runs tests simultaneously from **6 global regions** (US East/West, EU Central, Canada, India, Australia). Similar to Globalping but includes more tools and a generous free tier.

**[PhialsBasement/nmap-mcp-server](https://github.com/PhialsBasement/nmap-mcp-server)** (49 stars, TypeScript, npm) wraps nmap in a single flexible `run_nmap_scan` tool with quick scan, full port scan, version detection, and custom timing templates. Simple and focused — if you just want nmap access from your agent, this works. **The repository was archived by its owner on June 1, 2026** and is now read-only; treat it as a frozen snapshot, not an actively developed project. Windows-focused documentation. Requires nmap installed locally.

**patrickdappollonio/mcp-netutils** (Go) provides DNS lookups (DNS-over-HTTPS via Cloudflare/Google fallback), WHOIS queries, connectivity testing, TLS certificate analysis, HTTP endpoint monitoring, and hostname resolution. Notable for supporting both stdio and HTTP/SSE transport on port 3000. Go binary — no runtime dependencies.

**Also notable**: imjdl/nmap-mcpserver (Python nmap wrapper).

## Penetration Testing Suites

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) | — | Python | 300+ (38 servers) | stdio |
| [0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai) | ~1,599 | Python | 200+ | stdio |
| [DMontgomery40/pentest-mcp](https://github.com/DMontgomery40/pentest-mcp) | — | TypeScript | Multiple | stdio + HTTP + SSE |
| [0x4m4/hexstrike-ai](https://github.com/0x4m4/hexstrike-ai) | — | Python | 150+ | stdio + HTTP |
| [ramkansal/pentestMCP](https://github.com/ramkansal/pentestMCP) | — | Python | 20+ | stdio |
| [neptune1212/MCP_servers_cybersecurity](https://github.com/neptune1212/MCP_servers_cybersecurity) | — | Python | Multiple | stdio |

**[FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub)** (Python, 761 stars, 95 forks) has significantly expanded since April — now a **collection of 38 bundled MCP servers covering 300+ offensive security tools**, up from "20+ tools" in prior reviews. Organized across: **Reconnaissance** (Nmap, Masscan, Shodan, WhatWeb), **Web security** (Nikto, FFUF, SQLMap, Burp Suite wrapper), **Binary analysis** (Ghidra, Radare2, Binwalk, YARA, Capa), **Password cracking** (Hashcat), **Vulnerability scanning** (Nuclei), **Go fuzzing**, and **Blockchain security**. The repo's README documents production-hardened non-root Docker containers (running as a dedicated `mcpuser`, `no-new-privileges` enabled) and Trivy security scanning wired into CI/CD. The clear winner for comprehensive offensive security MCP integration — now genuinely one of the largest security tool bundles in the MCP ecosystem.

**DMontgomery40/pentest-mcp** (TypeScript, npm, last updated March 23, 2026) covers nmap, gobuster/dirbuster, nikto, John the Ripper, hashcat, and wordlist building. The standout feature: **full transport support** — stdio, HTTP (primary), and SSE (deprecated compatibility mode). Updated to MCP SDK @1.26.0 with **Bearer token auth via OIDC JWKS** — the most secure authentication model of any pentest MCP server. GPU-accelerated hashcat cracking for WPA/WPA2, NTLM, bcrypt, and 300+ hash types.

**[0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai)** (1,599 stars as of this audit, up from 276 in May 2026, Python, now on release **v1.3.1**) remains the fastest-growing pentest MCP server in this review. Positions itself as "the most autonomous pentesting AI" with **17 specialist agents and 200+ wrapped security tools**. The May 2026 v0.15.1 release added critical production-safe flags: `intensity=safe`, `respect_rate_limits=true`, and `strict_scope=true` — plus 60 SPA-aware probes for OWASP Top 10; those flags remain in the current release. These safety controls make it more viable for authorized client engagements where accidental out-of-scope testing could cause legal exposure.

**[0x4m4/hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)** (11,129 stars, 2,334 forks, Python) claims 150+ cybersecurity tools organized across 12+ autonomous AI agents with a Flask API backend. The star count is exceptional — and as of this audit the repo does show a push as recent as early August 2026, which walks back an earlier claim of dormancy in this review. The tool count is ambitious but independent verification of all claims is difficult.

**ramkansal/pentestMCP** (Python, Docker-based) bundles 20+ tools including Nmap, Nuclei, ZAP, SQLMap, Gobuster, and AJAX Spider. Uses an async launch/fetch pattern for long-running scans — important because security scans often take minutes, not seconds. Concurrency control via semaphores prevents overwhelming target systems.

**neptune1212/MCP_servers_cybersecurity** (Python, Dockerized) includes Metasploit RPC integration alongside Nmap, SQLMap, Nikto, WPScan, Gobuster, and Dirb. The only pentest MCP server with **Metasploit** and **WPScan** support — useful for WordPress security audits and exploit development in authorized testing environments.

## Web Application Security

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [PortSwigger/mcp-server](https://github.com/PortSwigger/mcp-server) | ~1,073 | Kotlin | Multiple | HTTP + stdio proxy |
| [Cy-S3c/BurpMCP-Ultra](https://github.com/Cy-S3c/BurpMCP-Ultra) | ~190 | — | 137 | — |
| [LisBerndt/zap-mcp-server](https://github.com/LisBerndt/zap-mcp-server) | ~5 | Python | 5+ | stdio |
| [dtkmn/mcp-zap-server](https://github.com/dtkmn/mcp-zap-server) | — | Java/Kotlin | 4+ | HTTP |
| [cyproxio/mcp-for-security](https://github.com/cyproxio/mcp-for-security) | — | TypeScript | Multiple | stdio |

**[PortSwigger/mcp-server](https://github.com/PortSwigger/mcp-server)** (1,073 stars, 171 forks, Kotlin, official) is the highest-credibility security MCP server in the entire ecosystem. Runs as a **Burp Suite extension** — HTTP request/response handling, vulnerability testing, traffic analysis, and Burp configuration. Tools toggled via the Burp UI. Runs on localhost:9876 with a stdio proxy for Claude Desktop compatibility. Recent additions include CI workflow for automated testing and proxy end-to-end tests. The official vendor backing means this will be maintained as long as Burp Suite exists. If your security team already uses Burp, this integration turns your AI agent into an intelligent testing assistant that can craft requests, analyze responses, and identify vulnerabilities within Burp's established workflow.

**[Cy-S3c/BurpMCP-Ultra](https://github.com/Cy-S3c/BurpMCP-Ultra)** (190 stars, created April 2026) is a community-built Burp Suite MCP extension offering **137 tools**, a real-time dashboard, and custom scan checks — significantly more tools than PortSwigger's official server. Adoption has grown quickly since launch, though it remains a community project rather than vendor-backed.

**LisBerndt/zap-mcp-server** (5 stars, Python) connects AI agents to OWASP ZAP — active scanning, passive scanning, AJAX spider, traditional spider, and session management. Configurable scan policies and evidence collection. ZAP is free and open source, making this the most accessible web security scanner integration. Low adoption but functional.

**dtkmn/mcp-zap-server** (Java/Kotlin, Spring Boot 4.0.3) is the enterprise-flavored ZAP integration — spider, active scan, OpenAPI spec import, and report generation. HTTP transport via Spring Boot, ZAP Client API 1.17.0. Better suited for CI/CD integration where you want to trigger ZAP scans from an agent in an automated pipeline.

**[cyproxio/mcp-for-security](https://github.com/cyproxio/mcp-for-security)** (630 stars, TypeScript) provided modular per-tool MCP servers covering SQLMap, FFUF, NMAP, Masscan, web screenshots, HTTP header analysis (OWASP), web crawling, and mobile app security. **This project has been superseded and, as of this audit, is formally archived** (archived by the owner March 30, 2026, read-only) — the maintainers fully rewrote and migrated the tooling to **[Bolt](https://github.com/cyberstrikeus/bolt)**, a Docker-supported successor with broader capability. The repo's README directs existing users to Bolt. The star count reflects historical interest; new installations should use Bolt instead.

## SSL/TLS Certificate Analysis

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [wouter-bon/CERT-MCP-SERVER](https://github.com/wouter-bon/CERT-MCP-SERVER) | — | Python | 30 | stdio + HTTP |
| [malaya-zemlya/tls-mcp](https://github.com/malaya-zemlya/tls-mcp) | — | Python | 1 | stdio |
| [firesh/sslmon-mcp](https://github.com/firesh/sslmon-mcp) | — | — | 2 | stdio |

**wouter-bon/CERT-MCP-SERVER** (Python, 30 tools) is the only MCP server for full certificate lifecycle management. Let's Encrypt certificate provisioning with Cloudflare DNS-01 challenges. Manages certificates on **FortiGate, FortiManager, FortiAnalyzer, Windows, and Linux** systems. Both stdio and REST API transports. This isn't just certificate analysis — it's certificate operations. If you manage SSL certificates across enterprise infrastructure, this turns certificate renewal from a manual process into an agent-driven workflow.

**malaya-zemlya/tls-mcp** (Python) is a focused TLS analysis tool — auto-selects between OpenSSL and Python cryptography backends, provides expiration monitoring, cipher suite analysis, security grading, and zlint integration. A single `fetch_certificate` tool with flexible options. Written entirely via Claude Code — a nice meta-touch. Best for quick TLS health checks.

**firesh/sslmon-mcp** offers two tools: `get_domain_info` and `get_ssl_cert_info`. Domain registration details plus SSL expiry date checking with days-until-expiry calculation. Lightweight and focused on the monitoring/alerting use case — "which certificates are about to expire?"

## Network Reconnaissance

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [mukul975/cve-mcp-server](https://github.com/mukul975/cve-mcp-server) | ~1,134 | — | 27 | stdio |
| [BurtTheCoder/mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan) | ~157 | TypeScript | Multiple | stdio |
| [nickpending/mcp-censys](https://github.com/nickpending/mcp-censys) | — | Python | Multiple | stdio |
| [addcontent/nuclei-mcp](https://github.com/addcontent/nuclei-mcp) | — | — | Multiple | stdio |
| [RobertoDure/mcp-vulnerability-scanner](https://github.com/RobertoDure/mcp-vulnerability-scanner) | — | — | Multiple | stdio |

**[mukul975/cve-mcp-server](https://github.com/mukul975/cve-mcp-server)** (created April 14, 2026) grew from 266 to 571 stars in its first month and has kept climbing since — now past **1,134 stars** as of this audit — making it one of the fastest-growing servers in the entire network security MCP space and one of the strongest adoption stories across all MCP categories. A production-grade MCP server providing **27 security intelligence tools across 21 APIs** — CVE lookup, EPSS scoring, CISA Known Exploited Vulnerabilities (KEV), MITRE ATT&CK mapping, Shodan, VirusTotal, and more. This aggregates what previously required separate MCP servers (Shodan, CVE databases, threat intelligence) into a single unified server. The sustained explosive adoption confirms strong demand for consolidated security intelligence tooling.

**[BurtTheCoder/mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan)** (~157 stars, TypeScript) connects agents to Shodan's internet-wide scanning database — IP reconnaissance, DNS operations, CVE/CPE vulnerability intelligence, and device discovery. Recent security fix: **pinned axios below compromised v1.14.1** — demonstrating responsible maintenance practices. Now documented for use with Claude Code, OpenAI Codex, Gemini CLI, and Claude Desktop. Shodan sees every internet-facing device. Combined with an AI agent, this enables natural-language queries like "find all exposed Redis instances on our subnet" or "what CVEs affect this IP's running services." Requires a Shodan API key (free tier available with rate limits).

**nickpending/mcp-censys** (Python) provides domain, IP, and FQDN reconnaissance via the Censys Search API. Similar to Shodan but with Censys's own internet-wide scanning perspective. No updates since April 2025 — dormant but functional. Useful as a complementary data source — Shodan and Censys often discover different services on the same hosts.

**addcontent/nuclei-mcp** provides context-aware Nuclei vulnerability scanning with template management. Nuclei (by ProjectDiscovery) is one of the most popular open-source vulnerability scanners with thousands of community templates covering CVEs, misconfigurations, and exposed panels.

**RobertoDure/mcp-vulnerability-scanner** runs single or batch IP vulnerability scanning via Nmap plus API checks, with severity levels and remediation steps in reports. Good for quick vulnerability assessments with actionable output.

## Enterprise & SOC Security (May 2026 Additions)

| Server | Stars | Provider | Focus | Launched |
|--------|-------|----------|-------|---------|
| [CheckPointSW/mcp-servers](https://github.com/CheckPointSW/mcp-servers) | — | Check Point | Workforce AI + Browse Security | 2026 |
| [Command Zero MCP](https://commandzero.com/) | — | Command Zero | Autonomous SOC | Apr 29, 2026 |
| [GitHub Secret Scanning MCP](https://github.blog/changelog/2026-05-05-secret-scanning-with-github-mcp-server-is-now-generally-available/) | — | GitHub | Credential detection | May 5, 2026 |

**[CheckPointSW/mcp-servers](https://github.com/CheckPointSW/mcp-servers)** (official) brings Check Point's enterprise security capabilities directly into AI tools. Covers **[Workforce AI](https://github.com/CheckPointSW/workforce-ai-mcp)** security (protecting AI assistant usage within organizations) and **Browse Security** (protecting AI agents browsing the web) — confirmed in the `workforce-ai-mcp` package README, which shipped its v1.0.0 release May 10, 2026. Designed for on-premises deployment with full governance and auditability. Significant for enterprise teams already on Check Point infrastructure.

**[Command Zero Autonomous SOC MCP](https://www.prnewswire.com/news-releases/command-zero-accelerates-secops-pipelines-with-apis-and-mcp-server-302755893.html)** (launched April 29, 2026) opens Command Zero's AI-powered SOC platform via MCP — investigation APIs, business context APIs, threat hunting, and remediation automation. Targets MSSP and enterprise SOC teams that want to plug MCP-compatible agents into their existing security operations workflow. The "autonomous SOC" positioning aligns with the broader trend of security vendors treating MCP as the integration layer for AI-native operations.

**GitHub Secret Scanning MCP** (Generally Available May 5, 2026, Preview March 2026) adds automated credential detection and remediation to AI-assisted development workflows. Scans repositories for exposed API keys, tokens, and credentials. Available to all repositories with GitHub Secret Protection enabled. Significant for security teams who want AI agents that can both write code and flag leaked credentials in the same workflow.

## Decision Guide

**For everyday network diagnostics**: Start with **dkruyt/mcp-nettools** — 11 tools covering DNS, WHOIS, scanning, SSL, and geolocation in one server. If you need globally distributed testing, add **Globalping**.

**For packet analysis**: **bx33661/Wireshark-MCP** for actively maintained Wireshark integration. **khuynh22/mcp-wireshark** if you want pip-installable tooling with proper versioned releases. **WireMCP** has the most stars but is dormant since July 2025 with an unpatched command injection vulnerability — not recommended for new projects.

**For web application security testing**: **PortSwigger/mcp-server** if your team uses Burp Suite — official vendor backing and the most starred server in this category. **LisBerndt/zap-mcp-server** for free/open-source ZAP integration.

**For comprehensive pentesting**: **FuzzingLabs/mcp-security-hub** for the broadest tool coverage (300+ tools, 38 servers). **0xSteph/pentest-ai** if you need autonomous agents with production-safe engagement flags. **pentest-mcp** if you need OIDC JWKS authentication or GPU-accelerated password cracking.

**For SSL/TLS management**: **CERT-MCP-SERVER** for certificate lifecycle operations across enterprise infrastructure. **tls-mcp** for quick analysis and health checks.

**For security intelligence**: **cve-mcp-server** for consolidated CVE/EPSS/CISA KEV/MITRE ATT&CK/Shodan/VirusTotal intelligence in one server (27 tools, 21 APIs). **mcp-shodan** for focused Shodan reconnaissance. Add **mcp-censys** for complementary scanning data.

**For enterprise/SOC teams**: **CheckPointSW/mcp-servers** if you're already on Check Point infrastructure. **Command Zero** if you run or manage a SOC and want autonomous investigation workflows. **GitHub Secret Scanning MCP** for any team using GitHub — free for repositories with Secret Protection enabled.

## The Security Elephant in the Room

Every server in this review wraps tools that can cause real harm if misused. Unlike a database MCP server where the worst case is a dropped table, a misconfigured pentest MCP server could scan production systems without authorization, exfiltrate network data, or trigger intrusion detection alerts. None of these servers implement authorization boundaries beyond what their underlying tools provide.

**The ecosystem-wide security picture remains concerning.** BlueRock Security's [MCP Trust Registry scan](https://www.bluerock.io/post/mcp-security), which as of its latest published update covers **12,000+ public MCP servers**, found: **6% have critical vulnerabilities**, **42% have command-injection flaws**, and **33% have SSRF/unbounded URI-fetch vulnerabilities**. (An earlier BlueRock snapshot of ~7,000 servers, cited in this review's original May 2026 draft, reported 41% with no authentication and 53% on static API keys; that specific figure set is no longer published on BlueRock's site as of this audit, so it has been replaced above with BlueRock's current numbers rather than left uncited.) Security-focused MCP servers are not immune — two servers in this review received CVEs in May 2026 alone ([CVE-2026-3959](https://nvd.nist.gov/vuln/detail/CVE-2026-3959) for WireMCP, [CVE-2026-43901](https://nvd.nist.gov/vuln/detail/CVE-2026-43901) for bx33661/Wireshark-MCP). A systemic **[MCP STDIO transport RCE vulnerability](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/)** affecting all language SDKs (Python, TypeScript, Java, Rust) was also disclosed — affecting an estimated 150M+ downloads across 7,000+ public servers.

**Before installing any of these**: ensure you have written authorization to test the target systems, understand the legal implications in your jurisdiction, and limit tool access to authorized personnel only. The MCP ecosystem still has no standard for security tool authorization — each server trusts that the agent (and the human behind it) will use it responsibly. For security tools specifically, that trust is especially high-stakes.

## Rating: 4.0/5

The network security MCP ecosystem continues to mature, with notable growth across all tiers since May 2026. PortSwigger's Burp Suite MCP (now past 1,073 stars) and FuzzingLabs' mcp-security-hub (38 servers/300+ tools) anchor the top tier. **mukul975/cve-mcp-server** (past 1,134 stars, up from 571 at last refresh) confirms sustained explosive demand for consolidated security intelligence. Enterprise adoption has arrived: Check Point and Command Zero both launched MCP offerings in late April/early May 2026, and GitHub Secret Scanning MCP went GA. 0xSteph/pentest-ai (now past 1,599 stars, on release v1.3.1) added production-safe engagement flags in v0.15.1 that address a real gap in pentest tooling and remain in the current release. The packet capture space stabilized — WireMCP holds stars despite dormancy, while bx33661/Wireshark-MCP remains the actively maintained option (now with its own CVE to monitor). Remaining concerns: BlueRock Security's ongoing 12,000+-server scan is alarming — 42% of MCP servers have command-injection flaws and the systemic STDIO transport RCE affects the entire ecosystem. Security-focused servers ironically carry significant security risk. hexstrike-ai's star count (now 11K+) remains disproportionate to its documented development activity relative to peers in this review, though this audit found evidence of at least one August 2026 push, walking back an earlier claim of total dormancy. Rating held at **4.0/5** — the growth in top-tier and enterprise tools is real, but the ecosystem-wide vulnerability findings are a serious counterweight that prevent a higher score.

*This review was last edited on 2026-05-21 using Claude Sonnet 4.6 (Anthropic).*

