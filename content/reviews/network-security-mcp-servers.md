---
title: "Network Security & Monitoring MCP Servers — Packet Capture, Port Scanning, Pentesting, and Reconnaissance"
date: 2026-03-15T07:04:00+09:00
description: "Network security MCP servers let AI agents capture packets, scan ports, run penetration tests, and perform reconnaissance."
og_description: "Network security MCP servers: Burp Suite (795 stars, official), FuzzingLabs mcp-security-hub (38 servers/300+ offensive tools), WireMCP (443 stars, CVE-2026-3959 unpatched), cve-mcp-server (571 stars, 27 tools/21 security APIs), 0xSteph pentest-ai (276 stars, v0.15.1), NEW CheckPointSW enterprise MCP, NEW Command Zero Autonomous SOC. 35+ servers reviewed. Rating: 4.0/5."
content_type: "Review"
card_description: "Network security MCP servers across packet capture, port scanning, pentesting, web security, SSL/TLS, CVE intelligence, and reconnaissance. PortSwigger's Burp Suite MCP leads with 795 stars and official vendor backing. FuzzingLabs' mcp-security-hub expanded to 38 bundled servers covering 300+ offensive tools. mukul975/cve-mcp-server surged to 571 stars aggregating 27 tools across 21 security APIs. Enterprise entrants: Check Point MCP and Command Zero Autonomous SOC launched in May 2026."
last_refreshed: 2026-05-21
---

Network security is one of the most powerful — and most dangerous — applications of MCP. AI agents that can capture packets, scan ports, run vulnerability assessments, and perform reconnaissance have enormous potential for security professionals. They also have enormous potential for misuse. Every server in this review should be used only with proper authorization on systems you own or have explicit permission to test. Part of our **[Security & Compliance MCP category](/categories/security-compliance/)**.

The headline finding: **enterprise adoption has arrived**. PortSwigger's Burp Suite MCP server has crossed **795 stars** (+12.6% since April). **mukul975/cve-mcp-server** exploded from 266 to **571 stars** in a month — the fastest-growing server in the ecosystem. FuzzingLabs' mcp-security-hub has expanded from "20+ tools" to **38 bundled MCP servers covering 300+ offensive tools** with hardened Docker containers. New enterprise entrants have arrived: **Check Point** launched official MCP servers (May 11) for Workforce AI and Browse Security, and **Command Zero** opened its Autonomous SOC platform via MCP (April 29). **0xSteph/pentest-ai** surged from 59 to **276 stars** with v0.15.1 adding production-safe engagement flags. The security picture is also sobering: WireMCP's command injection issue is now formally **CVE-2026-3959**, bx33661/Wireshark-MCP received **CVE-2026-43901** (arbitrary file write, CVSS 6.8, May 11), and a BlueRock Security ecosystem-wide analysis found 41% of MCP servers have no authentication and 53% use static API keys.

## Packet Capture & Traffic Analysis

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [0xKoda/WireMCP](https://github.com/0xKoda/WireMCP) | ~443 | Python | 3 | stdio |
| [bx33661/Wireshark-MCP](https://github.com/bx33661/Wireshark-MCP) | ~107 | Python | Multiple | stdio |
| [khuynh22/mcp-wireshark](https://github.com/khuynh22/mcp-wireshark) | ~31 | Python | 5+ | stdio |
| [mixelpixx/Wireshark-MCP](https://github.com/mixelpixx/Wireshark-MCP) | — | Python | Multiple | stdio |

**0xKoda/WireMCP** (443 stars, Python, March 2025) remains the most popular Wireshark MCP server by adoption. Three tools: `capture_packets` (real-time traffic capture as JSON), `get_summary_stats` (protocol hierarchy statistics), and `get_conversations` (TCP/UDP conversation tracking). **However, this project is dormant** — no commits since July 2025 (10+ months). The command injection vulnerability has been formally assigned **CVE-2026-3959** (Medium, CVSS 5.3) — still unpatched. Stars continue growing organically but the codebase is unmaintained. Do not use in production.

**bx33661/Wireshark-MCP** (Python, created February 2026) is the **most active Wireshark MCP alternative** — combines Wireshark packet analysis with complementary network tools, available on PyPI. **Important caveat as of May 2026**: an **arbitrary file write vulnerability was disclosed as CVE-2026-43901** (CVSS 6.8, published May 11, 2026). Check for patches before deploying. If you're choosing a Wireshark MCP server today, this remains the strongest actively-maintained option — but verify the CVE status against the current release.

**khuynh22/mcp-wireshark** (31 stars, Python 3.10+, pip-installable via `pip install mcp-wireshark`, v0.2.0) is the most polished Wireshark MCP server from an engineering standpoint. Live capture, PCAP file parsing, display filter support, stream following, and JSON export. Published on PyPI with proper packaging — no git cloning required. Cross-platform, typed, and tested. The only server with proper versioned releases.

**mixelpixx/Wireshark-MCP** combines Wireshark analysis with nmap scanning and threat intelligence lookups in a single server. AI-powered network troubleshooting that correlates packet data with vulnerability data. Less adopted but more ambitious in scope.

**Also notable**: kriztalz/SharkMCP (tshark-based capture and analysis) and sarthaksiddha/Wireshark-mcp (bridges low-level network data with AI understanding).

## Port Scanning & Network Diagnostics

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [dkruyt/mcp-nettools](https://github.com/dkruyt/mcp-nettools) | — | Python | 11 | stdio |
| [jsdelivr/globalping-mcp-server](https://github.com/jsdelivr/globalping-mcp-server) | ~54 | TypeScript | 5 | Streamable HTTP |
| [kumarprobeops/probeops-mcp-server](https://github.com/kumarprobeops/probeops-mcp-server) | — | TypeScript | 11-21 | stdio |
| [PhialsBasement/nmap-mcp-server](https://github.com/PhialsBasement/nmap-mcp-server) | ~45 | TypeScript | 1 | stdio |
| [patrickdappollonio/mcp-netutils](https://github.com/patrickdappollonio/mcp-netutils) | — | Go | 6+ | stdio + SSE |

**dkruyt/mcp-nettools** (Python, installable via uv) is the best all-in-one network diagnostics MCP server. **11 tools**: `nmap_scan`, `dns_lookup`, `dns_enum`, `whois_info`, `traceroute`, `port_check`, `ssl_scan`, `network_scan`, `ip_geolocation`, `http_headers`, and `my_public_ip`. Covers the most common network troubleshooting tasks in a single server — DNS, WHOIS, scanning, SSL analysis, and geolocation. If you want one server for everyday network work, this is it.

**jsdelivr/globalping-mcp-server** (54 stars, TypeScript, backed by jsDelivr) is architecturally unique — a **remote MCP server** at `https://mcp.globalping.dev/mcp` that runs diagnostics from thousands of globally distributed probes. Five tools: ping, traceroute, DNS, MTR, and HTTP tests. No local installation needed. OAuth and API token authentication with **PKCE S256 validation** added in April 2026 for improved security. When you need to test how your service responds from different geographic locations, nothing else in the MCP ecosystem comes close. Streamable HTTP transport means it works with modern MCP clients without stdio overhead.

**kumarprobeops/probeops-mcp-server** (TypeScript, via npx) offers 11 free tools (21 with API key) including SSL checks, DNS lookups, ping, WHOIS, port checks, traceroute, latency tests, and geo-located web browsing. Runs tests simultaneously from **6 global regions** (US East/West, EU Central, Canada, India, Australia). Similar to Globalping but includes more tools and a generous free tier.

**PhialsBasement/nmap-mcp-server** (45 stars, TypeScript, npm) wraps nmap in a single flexible `run_nmap_scan` tool with quick scan, full port scan, version detection, and custom timing templates. Simple and focused — if you just want nmap access from your agent, this works. No commits since January 2026. Windows-focused documentation. Requires nmap installed locally.

**patrickdappollonio/mcp-netutils** (Go) provides DNS lookups (DNS-over-HTTPS via Cloudflare/Google fallback), WHOIS queries, connectivity testing, TLS certificate analysis, HTTP endpoint monitoring, and hostname resolution. Notable for supporting both stdio and HTTP/SSE transport on port 3000. Go binary — no runtime dependencies.

**Also notable**: imjdl/nmap-mcpserver (Python nmap wrapper).

## Penetration Testing Suites

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) | — | Python | 300+ (38 servers) | stdio |
| [0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai) | ~276 | Python | 200+ | stdio |
| [DMontgomery40/pentest-mcp](https://github.com/DMontgomery40/pentest-mcp) | — | TypeScript | Multiple | stdio + HTTP + SSE |
| [0x4m4/hexstrike-ai](https://github.com/0x4m4/hexstrike-ai) | — | Python | 150+ | stdio + HTTP |
| [ramkansal/pentestMCP](https://github.com/ramkansal/pentestMCP) | — | Python | 20+ | stdio |
| [neptune1212/MCP_servers_cybersecurity](https://github.com/neptune1212/MCP_servers_cybersecurity) | — | Python | Multiple | stdio |

**FuzzingLabs/mcp-security-hub** (Python) has significantly expanded since April — now a **collection of 38 bundled MCP servers covering 300+ offensive security tools**, up from "20+ tools" in prior reviews. Organized across: **Reconnaissance** (Nmap, Masscan, Shodan, WhatWeb), **Web security** (Nikto, FFUF, SQLMap, Burp Suite wrapper), **Binary analysis** (Ghidra, Radare2, Binwalk, YARA, Capa), **Password cracking** (Hashcat), **Vulnerability scanning** (Nuclei), **Go fuzzing**, and **Blockchain security**. The May 2026 update adds production-hardened non-root Docker containers and Trivy security scanning for container images. Actively maintained with 72 forks. The clear winner for comprehensive offensive security MCP integration — now genuinely one of the largest security tool bundles in the MCP ecosystem.

**DMontgomery40/pentest-mcp** (TypeScript, npm, last updated March 23, 2026) covers nmap, gobuster/dirbuster, nikto, John the Ripper, hashcat, and wordlist building. The standout feature: **full transport support** — stdio, HTTP (primary), and SSE (deprecated compatibility mode). Updated to MCP SDK @1.26.0 with **Bearer token auth via OIDC JWKS** — the most secure authentication model of any pentest MCP server. GPU-accelerated hashcat cracking for WPA/WPA2, NTLM, bcrypt, and 300+ hash types.

**0xSteph/pentest-ai** (276 stars, Python, v0.15.1 May 16, 2026) has grown from 59 to 276 stars in a month — the fastest-growing pentest MCP server this cycle. Positions itself as "the most autonomous pentesting AI" with **17 specialist agents and 200+ wrapped security tools**. The May 2026 release added critical production-safe flags: `intensity=safe`, `respect_rate_limits=true`, and `strict_scope=true` — plus 60 SPA-aware probes for OWASP Top 10. These safety controls make it more viable for authorized client engagements where accidental out-of-scope testing could cause legal exposure.

**0x4m4/hexstrike-ai** (8,284 stars, Python) claims 150+ cybersecurity tools organized across 12+ autonomous AI agents with a Flask API backend. The star count is exceptional but warrants caution — no commits since March 2026, no releases, and the star-to-fork ratio (8.3K stars, 1.8K forks) is atypical for this space. The tool count is ambitious but independent verification of all claims is difficult.

**ramkansal/pentestMCP** (Python, Docker-based) bundles 20+ tools including Nmap, Nuclei, ZAP, SQLMap, Gobuster, and AJAX Spider. Uses an async launch/fetch pattern for long-running scans — important because security scans often take minutes, not seconds. Concurrency control via semaphores prevents overwhelming target systems.

**neptune1212/MCP_servers_cybersecurity** (Python, Dockerized) includes Metasploit RPC integration alongside Nmap, SQLMap, Nikto, WPScan, Gobuster, and Dirb. The only pentest MCP server with **Metasploit** and **WPScan** support — useful for WordPress security audits and exploit development in authorized testing environments.

## Web Application Security

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [PortSwigger/mcp-server](https://github.com/PortSwigger/mcp-server) | ~795 | Kotlin | Multiple | HTTP + stdio proxy |
| [Cy-S3c/BurpMCP-Ultra](https://github.com/Cy-S3c/BurpMCP-Ultra) | ~16 | — | 137 | — |
| [LisBerndt/zap-mcp-server](https://github.com/LisBerndt/zap-mcp-server) | ~5 | Python | 5+ | stdio |
| [dtkmn/mcp-zap-server](https://github.com/dtkmn/mcp-zap-server) | — | Java/Kotlin | 4+ | HTTP |
| [cyproxio/mcp-for-security](https://github.com/cyproxio/mcp-for-security) | — | TypeScript | Multiple | stdio |

**PortSwigger/mcp-server** (795 stars, +12.6% since April, Kotlin, official) is the highest-credibility security MCP server in the entire ecosystem. Runs as a **Burp Suite extension** — HTTP request/response handling, vulnerability testing, traffic analysis, and Burp configuration. Tools toggled via the Burp UI. Runs on localhost:9876 with a stdio proxy for Claude Desktop compatibility. Recent additions include CI workflow for automated testing and proxy end-to-end tests. The official vendor backing means this will be maintained as long as Burp Suite exists. If your security team already uses Burp, this integration turns your AI agent into an intelligent testing assistant that can craft requests, analyze responses, and identify vulnerabilities within Burp's established workflow.

**Cy-S3c/BurpMCP-Ultra** (16 stars, created April 2026) is a community-built Burp Suite MCP extension offering **137 tools**, a real-time dashboard, and custom scan checks — significantly more tools than PortSwigger's official server. Early adoption but ambitious scope for teams wanting deeper Burp integration.

**LisBerndt/zap-mcp-server** (5 stars, Python) connects AI agents to OWASP ZAP — active scanning, passive scanning, AJAX spider, traditional spider, and session management. Configurable scan policies and evidence collection. ZAP is free and open source, making this the most accessible web security scanner integration. Low adoption but functional.

**dtkmn/mcp-zap-server** (Java/Kotlin, Spring Boot 4.0.3) is the enterprise-flavored ZAP integration — spider, active scan, OpenAPI spec import, and report generation. HTTP transport via Spring Boot, ZAP Client API 1.17.0. Better suited for CI/CD integration where you want to trigger ZAP scans from an agent in an automated pipeline.

**cyproxio/mcp-for-security** (318 stars, TypeScript) provided modular per-tool MCP servers covering SQLMap, FFUF, NMAP, Masscan, web screenshots, HTTP header analysis (OWASP), web crawling, and mobile app security. **Note (May 2026): this project has been superseded** — the maintainers have fully rewritten and migrated the tooling to **Bolt**, a Docker-supported successor with broader capability. Existing users are directed to the Bolt project. The star count reflects historical interest; new installations should use Bolt instead.

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
| [mukul975/cve-mcp-server](https://github.com/mukul975/cve-mcp-server) | ~571 | — | 27 | stdio |
| [BurtTheCoder/mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan) | ~110 | TypeScript | Multiple | stdio |
| [nickpending/mcp-censys](https://github.com/nickpending/mcp-censys) | — | Python | Multiple | stdio |
| [addcontent/nuclei-mcp](https://github.com/addcontent/nuclei-mcp) | — | — | Multiple | stdio |
| [RobertoDure/mcp-vulnerability-scanner](https://github.com/RobertoDure/mcp-vulnerability-scanner) | — | — | Multiple | stdio |

**mukul975/cve-mcp-server** (571 stars, created April 14, 2026) has grown from 266 to **571 stars in a single month** — making it the fastest-growing server in the entire network security MCP space and one of the strongest adoption stories across all MCP categories. A production-grade MCP server providing **27 security intelligence tools across 21 APIs** — CVE lookup, EPSS scoring, CISA Known Exploited Vulnerabilities (KEV), MITRE ATT&CK mapping, Shodan, VirusTotal, and more. This aggregates what previously required separate MCP servers (Shodan, CVE databases, threat intelligence) into a single unified server. The sustained explosive adoption confirms strong demand for consolidated security intelligence tooling.

**BurtTheCoder/mcp-shodan** (~110 stars, TypeScript) connects agents to Shodan's internet-wide scanning database — IP reconnaissance, DNS operations, CVE/CPE vulnerability intelligence, and device discovery. Recent security fix: **pinned axios below compromised v1.14.1** — demonstrating responsible maintenance practices. Now documented for use with Claude Code, OpenAI Codex, Gemini CLI, and Claude Desktop. Shodan sees every internet-facing device. Combined with an AI agent, this enables natural-language queries like "find all exposed Redis instances on our subnet" or "what CVEs affect this IP's running services." Requires a Shodan API key (free tier available with rate limits).

**nickpending/mcp-censys** (Python) provides domain, IP, and FQDN reconnaissance via the Censys Search API. Similar to Shodan but with Censys's own internet-wide scanning perspective. No updates since April 2025 — dormant but functional. Useful as a complementary data source — Shodan and Censys often discover different services on the same hosts.

**addcontent/nuclei-mcp** provides context-aware Nuclei vulnerability scanning with template management. Nuclei (by ProjectDiscovery) is one of the most popular open-source vulnerability scanners with thousands of community templates covering CVEs, misconfigurations, and exposed panels.

**RobertoDure/mcp-vulnerability-scanner** runs single or batch IP vulnerability scanning via Nmap plus API checks, with severity levels and remediation steps in reports. Good for quick vulnerability assessments with actionable output.

## Enterprise & SOC Security (May 2026 Additions)

| Server | Stars | Provider | Focus | Launched |
|--------|-------|----------|-------|---------|
| [CheckPointSW/mcp-servers](https://github.com/CheckPointSW/mcp-servers) | — | Check Point | Workforce AI + Browse Security | May 11, 2026 |
| [Command Zero MCP](https://commandzero.com/) | — | Command Zero | Autonomous SOC | Apr 29, 2026 |
| [GitHub Secret Scanning MCP](https://github.blog/changelog/2026-05-05-secret-scanning-with-github-mcp-server-is-now-generally-available/) | — | GitHub | Credential detection | May 5, 2026 |

**CheckPointSW/mcp-servers** (official, launched May 11, 2026) brings Check Point's enterprise security capabilities directly into AI tools. Covers **Workforce AI** security (protecting AI assistant usage within organizations) and **Browse Security** (protecting AI agents browsing the web). Designed for on-premises deployment with full governance and auditability. The first major network security vendor to launch a dedicated MCP presence. Significant for enterprise teams already on Check Point infrastructure.

**Command Zero Autonomous SOC MCP** (launched April 29, 2026) opens Command Zero's AI-powered SOC platform via MCP — investigation APIs, business context APIs, threat hunting, and remediation automation. Targets MSSP and enterprise SOC teams that want to plug MCP-compatible agents into their existing security operations workflow. The "autonomous SOC" positioning aligns with the broader trend of security vendors treating MCP as the integration layer for AI-native operations.

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

**The ecosystem-wide security picture has gotten worse**, not better. A May 2026 analysis by BlueRock Security of MCP servers at large found: **41% have no authentication**, **53% use static API keys** (vs. proper OAuth), **36.7% are vulnerable to SSRF**, and only **8.5% use OAuth**. Security-focused MCP servers are not immune — two servers in this review received CVEs in May 2026 alone (CVE-2026-3959 for WireMCP, CVE-2026-43901 for bx33661/Wireshark-MCP). A systemic **MCP STDIO transport RCE vulnerability** affecting all language SDKs (Python, TypeScript, Java, Rust) was also disclosed — affecting an estimated 150M+ downloads across 7,000+ public servers.

**Before installing any of these**: ensure you have written authorization to test the target systems, understand the legal implications in your jurisdiction, and limit tool access to authorized personnel only. The MCP ecosystem still has no standard for security tool authorization — each server trusts that the agent (and the human behind it) will use it responsibly. For security tools specifically, that trust is especially high-stakes.

## Rating: 4.0/5

The network security MCP ecosystem continues to mature, with notable growth across all tiers in May 2026. PortSwigger's Burp Suite MCP (795 stars) and FuzzingLabs' mcp-security-hub (now 38 servers/300+ tools) anchor the top tier. **mukul975/cve-mcp-server** (571 stars in 5 weeks) confirms explosive demand for consolidated security intelligence. Enterprise adoption has arrived: Check Point and Command Zero both launched MCP offerings in late April/early May 2026, and GitHub Secret Scanning MCP went GA. 0xSteph/pentest-ai (276 stars, v0.15.1) added production-safe engagement flags that address a real gap in pentest tooling. The packet capture space stabilized — WireMCP holds stars despite dormancy, while bx33661/Wireshark-MCP remains the actively maintained option (now with its own CVE to monitor). Remaining concerns: the BlueRock Security ecosystem-wide analysis is alarming — 41% of MCP servers have no authentication and the systemic STDIO transport RCE affects the entire ecosystem. Security-focused servers ironically carry significant security risk. Some projects still show suspicious star inflation (hexstrike-ai at 8K+ stars with minimal development remains unexplained). Rating held at **4.0/5** — the growth in top-tier and enterprise tools is real, but the ecosystem-wide vulnerability findings are a serious counterweight that prevent a higher score.

*This review was last edited on 2026-05-21 using Claude Sonnet 4.6 (Anthropic).*
