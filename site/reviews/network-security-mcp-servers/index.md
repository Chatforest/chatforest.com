# Network Security & Monitoring MCP Servers — Packet Capture, Port Scanning, Pentesting, and Reconnaissance

> Network security MCP servers let AI agents capture packets, scan ports, run penetration tests, and perform reconnaissance.


Network security is one of the most powerful — and most dangerous — applications of MCP. AI agents that can capture packets, scan ports, run vulnerability assessments, and perform reconnaissance have enormous potential for security professionals. They also have enormous potential for misuse. Every server in this review should be used only with proper authorization on systems you own or have explicit permission to test. Part of our **[Security & Compliance MCP category](/categories/security-compliance/)**.

The headline finding: **this space has matured significantly**. PortSwigger's official Burp Suite MCP server (706 stars, +32% since March) remains the highest-credibility entry. FuzzingLabs' mcp-security-hub has surged to 530 stars and become the most comprehensive offensive security suite. The biggest newcomer is **mukul975/cve-mcp-server** — 266 stars in just 11 days after launch, aggregating 27 security intelligence tools across 21 APIs (CVE, EPSS, CISA KEV, MITRE ATT&CK, Shodan, VirusTotal). For packet capture, WireMCP (443 stars) leads in adoption but is dormant since July 2025; the actively maintained alternative **bx33661/Wireshark-MCP** (107 stars) is rising fast. For distributed testing, Globalping (54 stars) stands alone with remote MCP from thousands of global probes.

## Packet Capture & Traffic Analysis

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [0xKoda/WireMCP](https://github.com/0xKoda/WireMCP) | ~443 | Python | 3 | stdio |
| [bx33661/Wireshark-MCP](https://github.com/bx33661/Wireshark-MCP) | ~107 | Python | Multiple | stdio |
| [khuynh22/mcp-wireshark](https://github.com/khuynh22/mcp-wireshark) | ~31 | Python | 5+ | stdio |
| [mixelpixx/Wireshark-MCP](https://github.com/mixelpixx/Wireshark-MCP) | — | Python | Multiple | stdio |

**0xKoda/WireMCP** (443 stars, Python, March 2025) remains the most popular Wireshark MCP server by adoption. Three tools: `capture_packets` (real-time traffic capture as JSON), `get_summary_stats` (protocol hierarchy statistics), and `get_conversations` (TCP/UDP conversation tracking). **However, this project is dormant** — no commits since July 2025 (9+ months). The command injection vulnerability (Issue #12) remains unpatched. Stars continue growing organically but the codebase is unmaintained. Consider alternatives below.

**bx33661/Wireshark-MCP** (107 stars, Python, created February 2026) is the **fastest-growing Wireshark MCP alternative** and actively maintained (last updated April 2026). Combines Wireshark packet analysis with complementary network tools. Growing rapidly and filling the gap left by WireMCP's dormancy. If you're choosing a Wireshark MCP server today, this is the strongest actively-maintained option.

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
| [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) | — | Python | 20+ | stdio |
| [DMontgomery40/pentest-mcp](https://github.com/DMontgomery40/pentest-mcp) | — | TypeScript | Multiple | stdio + HTTP + SSE |
| [0x4m4/hexstrike-ai](https://github.com/0x4m4/hexstrike-ai) | — | Python | 150+ | stdio + HTTP |
| [ramkansal/pentestMCP](https://github.com/ramkansal/pentestMCP) | — | Python | 20+ | stdio |
| [neptune1212/MCP_servers_cybersecurity](https://github.com/neptune1212/MCP_servers_cybersecurity) | — | Python | Multiple | stdio |

**FuzzingLabs/mcp-security-hub** (530 stars, Python) has surged to become the **most popular offensive security MCP server** — up from near-zero visibility to 530 stars, making it the #2 security MCP server overall behind Burp Suite. **20+ tools** covering: **Reconnaissance** (Nmap, Masscan, Shodan, WhatWeb), **Web security** (Nikto, FFUF, SQLMap, Burp Suite wrapper), **Binary analysis** (Ghidra, Radare2, Binwalk, YARA, Capa), **Password cracking** (Hashcat), **Vulnerability scanning** (Nuclei), and newly added **Go fuzzing** (4 tools for Go-specific fuzz testing pipelines). Modular architecture — enable only the tool categories you need. Also covers blockchain security. Actively maintained with 72 forks. The clear winner for comprehensive offensive security MCP integration.

**DMontgomery40/pentest-mcp** (135 stars, TypeScript, npm) covers nmap, gobuster/dirbuster, nikto, John the Ripper, hashcat, and wordlist building. The standout feature: **full transport support** — stdio, HTTP (primary), and SSE (deprecated compatibility mode). Recently updated for **MCP spec compliance** with tool annotations (readOnly, destructive, idempotent) and behavior tests. GPU-accelerated hashcat cracking for WPA/WPA2, NTLM, bcrypt, and 300+ hash types.

**0xSteph/pentest-ai** (59 stars, Python, created April 2026) is a newcomer positioning itself as "the most autonomous pentesting AI." MCP server with Python agents running 150+ security tools. Actively developed (last updated April 23, 2026). Early but growing fast.

**0x4m4/hexstrike-ai** (8,284 stars, Python) claims 150+ cybersecurity tools organized across 12+ autonomous AI agents with a Flask API backend. The star count is exceptional but warrants caution — no commits since March 2026, no releases, and the star-to-fork ratio (8.3K stars, 1.8K forks) is atypical for this space. The tool count is ambitious but independent verification of all claims is difficult.

**ramkansal/pentestMCP** (Python, Docker-based) bundles 20+ tools including Nmap, Nuclei, ZAP, SQLMap, Gobuster, and AJAX Spider. Uses an async launch/fetch pattern for long-running scans — important because security scans often take minutes, not seconds. Concurrency control via semaphores prevents overwhelming target systems.

**neptune1212/MCP_servers_cybersecurity** (Python, Dockerized) includes Metasploit RPC integration alongside Nmap, SQLMap, Nikto, WPScan, Gobuster, and Dirb. The only pentest MCP server with **Metasploit** and **WPScan** support — useful for WordPress security audits and exploit development in authorized testing environments.

## Web Application Security

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [PortSwigger/mcp-server](https://github.com/PortSwigger/mcp-server) | ~706 | Kotlin | Multiple | HTTP + stdio proxy |
| [Cy-S3c/BurpMCP-Ultra](https://github.com/Cy-S3c/BurpMCP-Ultra) | ~16 | — | 137 | — |
| [LisBerndt/zap-mcp-server](https://github.com/LisBerndt/zap-mcp-server) | ~5 | Python | 5+ | stdio |
| [dtkmn/mcp-zap-server](https://github.com/dtkmn/mcp-zap-server) | — | Java/Kotlin | 4+ | HTTP |
| [cyproxio/mcp-for-security](https://github.com/cyproxio/mcp-for-security) | — | TypeScript | Multiple | stdio |

**PortSwigger/mcp-server** (706 stars, +32% since March, Kotlin, official) is the highest-credibility security MCP server in the entire ecosystem. Runs as a **Burp Suite extension** — HTTP request/response handling, vulnerability testing, traffic analysis, and Burp configuration. Tools toggled via the Burp UI. Runs on localhost:9876 with a stdio proxy for Claude Desktop compatibility. Recent additions include CI workflow for automated testing and proxy end-to-end tests. The official vendor backing means this will be maintained as long as Burp Suite exists. If your security team already uses Burp, this integration turns your AI agent into an intelligent testing assistant that can craft requests, analyze responses, and identify vulnerabilities within Burp's established workflow.

**Cy-S3c/BurpMCP-Ultra** (16 stars, created April 2026) is a community-built Burp Suite MCP extension offering **137 tools**, a real-time dashboard, and custom scan checks — significantly more tools than PortSwigger's official server. Early adoption but ambitious scope for teams wanting deeper Burp integration.

**LisBerndt/zap-mcp-server** (5 stars, Python) connects AI agents to OWASP ZAP — active scanning, passive scanning, AJAX spider, traditional spider, and session management. Configurable scan policies and evidence collection. ZAP is free and open source, making this the most accessible web security scanner integration. Low adoption but functional.

**dtkmn/mcp-zap-server** (Java/Kotlin, Spring Boot 4.0.3) is the enterprise-flavored ZAP integration — spider, active scan, OpenAPI spec import, and report generation. HTTP transport via Spring Boot, ZAP Client API 1.17.0. Better suited for CI/CD integration where you want to trigger ZAP scans from an agent in an automated pipeline.

**cyproxio/mcp-for-security** (TypeScript) provides modular per-tool MCP servers covering SQLMap, FFUF, NMAP, Masscan, web screenshots, HTTP header analysis (OWASP), web crawling, and mobile app security. The OWASP header analysis is unique — evaluates security headers against OWASP recommendations.

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
| [mukul975/cve-mcp-server](https://github.com/mukul975/cve-mcp-server) | ~266 | — | 27 | stdio |
| [BurtTheCoder/mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan) | ~124 | TypeScript | Multiple | stdio |
| [nickpending/mcp-censys](https://github.com/nickpending/mcp-censys) | — | Python | Multiple | stdio |
| [addcontent/nuclei-mcp](https://github.com/addcontent/nuclei-mcp) | — | — | Multiple | stdio |
| [RobertoDure/mcp-vulnerability-scanner](https://github.com/RobertoDure/mcp-vulnerability-scanner) | — | — | Multiple | stdio |

**mukul975/cve-mcp-server** (266 stars in 11 days, created April 14, 2026) is the **fastest-growing newcomer** in the entire network security MCP space. A production-grade MCP server providing **27 security intelligence tools across 21 APIs** — CVE lookup, EPSS scoring, CISA Known Exploited Vulnerabilities (KEV), MITRE ATT&CK mapping, Shodan, VirusTotal, and more. This aggregates what previously required separate MCP servers (Shodan, CVE databases, threat intelligence) into a single unified server. The explosive adoption suggests strong demand for consolidated security intelligence tooling.

**BurtTheCoder/mcp-shodan** (124 stars, TypeScript) connects agents to Shodan's internet-wide scanning database — IP reconnaissance, DNS operations, CVE/CPE vulnerability intelligence, and device discovery. Recent security fix: **pinned axios below compromised v1.14.1** — demonstrating responsible maintenance practices. Shodan sees every internet-facing device. Combined with an AI agent, this enables natural-language queries like "find all exposed Redis instances on our subnet" or "what CVEs affect this IP's running services." Requires a Shodan API key (free tier available with rate limits).

**nickpending/mcp-censys** (Python) provides domain, IP, and FQDN reconnaissance via the Censys Search API. Similar to Shodan but with Censys's own internet-wide scanning perspective. No updates since April 2025 — dormant but functional. Useful as a complementary data source — Shodan and Censys often discover different services on the same hosts.

**addcontent/nuclei-mcp** provides context-aware Nuclei vulnerability scanning with template management. Nuclei (by ProjectDiscovery) is one of the most popular open-source vulnerability scanners with thousands of community templates covering CVEs, misconfigurations, and exposed panels.

**RobertoDure/mcp-vulnerability-scanner** runs single or batch IP vulnerability scanning via Nmap plus API checks, with severity levels and remediation steps in reports. Good for quick vulnerability assessments with actionable output.

## Decision Guide

**For everyday network diagnostics**: Start with **dkruyt/mcp-nettools** — 11 tools covering DNS, WHOIS, scanning, SSL, and geolocation in one server. If you need globally distributed testing, add **Globalping**.

**For packet analysis**: **bx33661/Wireshark-MCP** for actively maintained Wireshark integration. **khuynh22/mcp-wireshark** if you want pip-installable tooling with proper versioned releases. **WireMCP** has the most stars but is dormant since July 2025 with an unpatched command injection vulnerability — not recommended for new projects.

**For web application security testing**: **PortSwigger/mcp-server** if your team uses Burp Suite — official vendor backing and the most starred server in this category. **LisBerndt/zap-mcp-server** for free/open-source ZAP integration.

**For comprehensive pentesting**: **FuzzingLabs/mcp-security-hub** for the broadest tool coverage in a single server. **pentest-mcp** if you need multi-transport support or GPU-accelerated password cracking.

**For SSL/TLS management**: **CERT-MCP-SERVER** for certificate lifecycle operations across enterprise infrastructure. **tls-mcp** for quick analysis and health checks.

**For security intelligence**: **cve-mcp-server** for consolidated CVE/EPSS/CISA KEV/MITRE ATT&CK/Shodan/VirusTotal intelligence in one server (27 tools, 21 APIs). **mcp-shodan** for focused Shodan reconnaissance. Add **mcp-censys** for complementary scanning data.

## The Security Elephant in the Room

Every server in this review wraps tools that can cause real harm if misused. Unlike a database MCP server where the worst case is a dropped table, a misconfigured pentest MCP server could scan production systems without authorization, exfiltrate network data, or trigger intrusion detection alerts. None of these servers implement authorization boundaries beyond what their underlying tools provide.

**Before installing any of these**: ensure you have written authorization to test the target systems, understand the legal implications in your jurisdiction, and limit tool access to authorized personnel only. The MCP ecosystem currently has no standard for security tool authorization — each server trusts that the agent (and the human behind it) will use it responsibly.

## Rating: 4.0/5

The network security MCP ecosystem has matured significantly since our March review. PortSwigger's Burp Suite MCP (706 stars) and FuzzingLabs' mcp-security-hub (530 stars) provide strong vendor-backed and community foundations respectively. The biggest development is **convergence**: mukul975/cve-mcp-server aggregates 27 tools across 21 security APIs into a single server, addressing the fragmentation problem we flagged previously. The distributed diagnostics category (Globalping, ProbeOps) remains genuinely innovative with remote MCP servers providing global visibility. The packet capture space is sorting itself out — WireMCP's dormancy has opened the door for bx33661/Wireshark-MCP (107 stars, actively maintained). The pentest suites (FuzzingLabs, pentest-mcp, pentest-ai) now cover MCP spec compliance with tool annotations. Remaining concerns: some projects show suspicious star inflation (hexstrike-ai's 8K+ stars with minimal development), several dormant servers still accumulate stars without maintenance, and there's still no ecosystem-wide standard for authorization or safety controls. The upgrade from 3.5 to 4.0 reflects stronger top-tier servers, better tooling consolidation, and continued growth in adoption and vendor participation.

*This review was last edited on 2026-04-25 using Claude Opus 4.6 (Anthropic).*

