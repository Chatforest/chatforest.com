---
title: "Digital Forensics & Incident Response (DFIR) MCP Servers — CrowdStrike, SentinelOne, Google Security, TheHive, VirusTotal, Volatility, YARA, Wazuh, and More"
date: 2026-03-18T15:00:00+09:00
description: "DFIR MCP servers reviewed: CrowdStrike Falcon v0.16.1 (234 stars, 25 modules, RTR + NGSIEM + MSSP), SentinelOne Purple AI NEW (91 stars, 30 tools, vendor-maintained not official), Google Security (517 stars, 5 servers incl. managed remote MCP, now GA), Security-Detections-MCP SURGED (471 stars, 81 tools, 8,200+ rules)"
og_description: "DFIR MCP servers: CrowdStrike v0.16.1 (234 stars, 25 modules, RTR), SentinelOne Purple AI NEW (91 stars, vendor-maintained not official, 30 tools), Google Security (517 stars, 5 servers), Security-Detections-MCP (471 stars, 81 tools), Wazuh (219 stars, 55 tools), Splunk NOW OFFICIAL. Rating: 4.5/5."
content_type: "Review"
card_description: "Digital forensics and incident response has strong and growing MCP coverage. Since our initial review, SentinelOne launched its Purple AI MCP Server (91 stars, 30 tools) — vendor-maintained but explicitly not an official SentinelOne product per its own README — closing the biggest gap we identified. CrowdStrike surged from 115 to 234 stars, now at v0.16.1, adding Real-Time Response, NGSIEM, MSSP support, Custom IOA, and Firewall Management — expanding from 6 to 25 modules. Google shipped a managed remote MCP server for SecOps, now generally available. Splunk now has an official MCP server on Splunkbase. Security-Detections-MCP grew from 334 to 471 stars with 81 tools and 8,200+ detection rules. Wazuh surged to 219 stars with v4.3.0 and active response capabilities. New entrants include Velociraptor MCP (39 stars) and EventWhisper (49 stars). FuzzingLabs mcp-security-hub exploded to 758 stars with 38 servers and 300+ tools."
last_refreshed: 2026-08-14
sources_audited: 2026-08-14
---

Digital forensics and incident response (DFIR) has emerged as one of the most active — and most vendor-invested — MCP categories. The space spans memory forensics, endpoint detection, malware analysis, threat intelligence, and SIEM integration. What makes it stand out is the vendor commitment: CrowdStrike, Google, StrangeBee (TheHive), REMnux, and **Splunk** (now official) all ship official MCP servers; **SentinelOne** (new since our initial review) ships a vendor-maintained server whose own [README states it is not an official SentinelOne product](https://github.com/Sentinel-One/purple-mcp). Community contributors have filled remaining gaps with Volatility, VirusTotal, YARA, Wazuh, MISP, and Velociraptor integrations. Part of our **[Security & Compliance MCP category](/categories/security-compliance/)**.

**What changed since our [initial review](/reviews/digital-forensics-incident-response-mcp-servers/) (March 18):** SentinelOne launched its Purple AI MCP Server — the biggest gap we identified is now closed, though SentinelOne's own README states it is not an official product. CrowdStrike expanded from 6 to 25 modules (now at v0.16.1) with Real-Time Response, NGSIEM, MSSP support, Custom IOA, and Firewall Management. Splunk shipped an official MCP server on Splunkbase. Google added a managed remote MCP server for SecOps, now generally available. Security-Detections-MCP surged from 334 to 471 stars with 81 tools and 8,200+ detection rules across 6 formats. Wazuh grew to 219 stars with active response capabilities. New entrants: Velociraptor MCP and EventWhisper.

The DFIR MCP landscape is broader than most categories we review, so we've organized this review by workflow stage: **detection & response** (EDR, SIEM), **forensic analysis** (memory forensics, malware analysis), **threat intelligence** (IOC lookup, detection rules), and **incident management** (case management, SOAR).

## CrowdStrike Falcon — Official Server (SURGED)

| Detail | Info |
|--------|------|
| [CrowdStrike/falcon-mcp](https://github.com/CrowdStrike/falcon-mcp) | **234 stars** (was ~115) |
| Status | Public preview — [v0.16.1](https://github.com/CrowdStrike/falcon-mcp/releases) (August 10, 2026) |
| Transport | stdio, **streamable-http** |
| Modules | **25 modules** (was 6) |

CrowdStrike's official Falcon MCP server has seen rapid development — module count grew from 6 to 17 by v0.9.0 (April 10, 2026), and to 25 by the current v0.16.1 (August 10, 2026).

### What's New (v0.5 → v0.9.0)

**Real-Time Response (RTR).** v0.9.0 adds triage commands via RTR — the write-side capability gap we flagged in our initial review is beginning to close. Analysts can now initiate response actions, not just query data.

**NGSIEM module.** v0.6.0 added direct CQL (CrowdStrike Query Language) execution against Next-Gen SIEM. This brings log search and hunting capabilities into the MCP interface.

**Flight Control (MSSP) support.** v0.9.0 adds `member_cid` parameter for managed security service providers managing multiple tenants. Significant for enterprise/MSSP deployments.

**Custom IOA rules.** v0.8.0 added behavioral detection rule management. Combined with Firewall Management (also v0.8.0), CrowdStrike's MCP now covers both detection and prevention policy.

**MCP tool annotations.** v0.8.0 added proper annotations for all tools — better metadata for AI agent tool selection.

**Docker + streamable-http.** Full containerized deployment with HTTP transport, deployable to Amazon Bedrock and Google Cloud.

**Since v0.9.0.** Seven more releases (v0.10.0 through v0.16.1, May–August 2026) brought the module count from 17 to 25, with continued additions in case management, correlation rules, data protection, and other areas. Full [release notes](https://github.com/CrowdStrike/falcon-mcp/releases).

### What Works Well

**Modular architecture.** 25 modules: Core, Case Management, Cloud Security, Correlation Rules, Custom IOA, Data Protection, Detections, Discover, Exclusions, Firewall Management, Host Groups, Hosts, Identity Protection, Intel, IOC, NGSIEM, Policies, Quarantine, Real Time Response, Recon, Scheduled Reports, Sensor Usage, Serverless, Shield, and Spotlight. Enable only what your workflow needs.

**Deep detection data.** Full detection context — process details, network connections, file paths, command lines. Combined with behaviors module, agents can reconstruct attack chains.

**Threat intelligence access.** CrowdStrike's threat intel database — actor profiles, indicators, reports — normally behind a paid API.

### What Doesn't Work Well

**Still in public preview.** Breaking changes possible. Not recommended for production SOC automation without testing.

**Requires Falcon subscription.** No value without an existing CrowdStrike deployment.

## SentinelOne Purple AI — NEW Vendor-Maintained Server (Not Official)

| Detail | Info |
|--------|------|
| [Sentinel-One/purple-mcp](https://github.com/Sentinel-One/purple-mcp) | **91 stars** |
| Status | Vendor-maintained; its own README states it is [**not an official SentinelOne product**](https://github.com/Sentinel-One/purple-mcp), though maintained by SentinelOne staff in partnership with the open-source community. MIT license |
| Language | Python |
| Transport | stdio, SSE, **streamable-http** |
| Tools | **30 tools** across 8 categories |

**This is the biggest change since our initial review.** SentinelOne — previously listed as a gap — now has a vendor-maintained MCP server. Purple AI MCP exposes SentinelOne's platform through the Model Context Protocol with conversational threat analysis. Its own [README is explicit](https://github.com/Sentinel-One/purple-mcp) that "it is not an official SentinelOne product," though it is maintained by SentinelOne in partnership with the open-source developer community.

### What Works Well

**Comprehensive read-only access.** 30 tools across eight categories: Purple AI (1 tool, conversational investigation), Data Lake (1 tool), Alerts (5 tools), Vulnerabilities (5 tools), Misconfigurations (5 tools), Asset Inventory (3 tools), CVE Search (3 tools), and Threat Intelligence (7 tools). Covers the core SOC analyst workflows.

**Purple AI integration.** The standout feature — agents can interact with SentinelOne's Purple AI for conversational threat analysis and guided security actions. This isn't just data access; it's AI-to-AI investigation.

**Multiple deployment options.** Local via `uv`, Docker, Amazon Bedrock AgentCore, Amazon ECS. Cloud load balancer support (AWS ALB, GCP, Azure).

**Three transport protocols.** stdio, SSE, and streamable-http — works with any MCP client.

### What Doesn't Work Well

**Read-only.** No containment or response actions — you can investigate but not act. This is a deliberate safety choice, but limits SOAR-style automation.

**Requires SentinelOne subscription.** Like CrowdStrike's MCP, this is an interface to an existing deployment.

## Google Security — Official Reference Servers (EXPANDED)

| Detail | Info |
|--------|------|
| [google/mcp-security](https://github.com/google/mcp-security) | **517 stars**, 130 forks |
| License | Apache 2.0 |
| Language | Python |
| Servers | **5** (was 4 — added managed remote MCP) |

Google's security MCP repository has grown significantly — 517 stars (up from unlisted), 368 commits, and a fifth server: a managed remote MCP server for Google SecOps.

### What's New

**Managed remote MCP server for SecOps.** The recommended deployment path — fully managed by Google, no self-hosting required. Enterprise-ready with Google Cloud authentication.

**Google Cloud Next 2026 announcements.** Google announced [two new agentic workflows in preview](https://cloud.google.com/blog/products/identity-security/next26-redefining-security-for-the-ai-era-with-google-cloud-and-wiz): a Threat Hunting agent and a Detection Engineering agent. The same announcement confirms the remote MCP server for Google Security Operations referenced above is now **generally available**.

**YARA-L 2.0 queries.** New published queries for Entities, Ingestion Metrics, IOC Matches, Rules Detections, SOAR Case History, SOAR Cases, SOAR Playbooks, and UDM Events.

### Servers

1. **Remote MCP Server for Google SecOps** (NEW — recommended, fully managed)
2. **Google Threat Intelligence (GTI)** — VirusTotal enterprise via Google infrastructure
3. **Chronicle SecOps** — UDM queries, detection rules, threat hunting
4. **SecOps SOAR** — 100+ integrations for automated response
5. **Security Command Center (SCC)** — GCP security posture

### What Works Well

**Comprehensive coverage.** Five servers covering detection-to-response within Google's security ecosystem. Few vendors offer this breadth.

**Managed option eliminates self-hosting.** The new remote MCP server is the easiest path for organizations already in Google's ecosystem.

### What Doesn't Work Well

**Google Cloud lock-in.** SCC only works with GCP. Chronicle and SOAR work best within Google's ecosystem.

**Reference implementations.** The self-hosted servers don't carry GA product support guarantees.

## Splunk — NOW OFFICIAL

| Detail | Info |
|--------|------|
| [CiscoDevNet/Splunk-MCP-Server-official](https://github.com/CiscoDevNet/Splunk-MCP-Server-official) | Official, Splunk Supported (Beta) |
| [splunk/splunk-mcp-server2](https://github.com/splunk/splunk-mcp-server2) | 36 stars (community/unofficial) |
| Splunkbase | [App ID 7931](https://splunkbase.splunk.com/app/7931) — v1.3.1, 19,708+ downloads, 5/5 rating (15 ratings) |

**Splunk now has an official MCP server**, published on Splunkbase by Splunk LLC. This is a significant upgrade from the "semi-official" status we reported initially.

### Official Server Features

**Enterprise-grade.** Built-in authentication, authorization, and RBAC. Hosted within Splunk itself on port 8089 at `/services/mcp` — not a spawned local process.

**Core tools:** `generate_spl` (natural language to SPL), `run_splunk_query` (execute searches), `get_splunk_info`, `get_indexes`, `get_saved_searches`.

**Broad compatibility.** Splunk Enterprise and Cloud Platform versions 8.0–10.2.

The community `splunk-mcp-server2` (36 stars) remains available for users who prefer Python/TypeScript implementations with stdio/SSE transport.

## TheHive — Official + Community Servers

| Detail | Info |
|--------|------|
| [StrangeBeeCorp/TheHiveMCP](https://github.com/StrangeBeeCorp/TheHiveMCP) | Official, **8 stars**, 2 forks |
| Language | Go |
| License | Apache 2.0 |
| Last updated | July 13, 2026 |

TheHive's official MCP server continues under active maintenance, with commits as recent as July 2026.

### What Works Well

**Official vendor support.** Natural language queries against cases, alerts, and observables. **Community alternatives** in Rust and Python provide language options. **Ecosystem integration** with Cortex (automated analysis) and MISP (threat intelligence sharing).

### What Doesn't Work Well

**Low visibility.** Only 8 stars despite official vendor backing. Go language choice limits typical MCP community contributions.

## Volatility — Memory Forensics

| Detail | Info |
|--------|------|
| [bornpresident/Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server) | **39 stars** (was ~26) |
| Language | Python |
| Framework | Volatility 3 |

Memory forensics coverage remains stable. The most popular Volatility MCP server has grown to 39 stars, with multiple implementations available. No major functional changes since initial review.

**No Autopsy/Sleuth Kit integration.** Disk forensics remains a gap — still no MCP servers for Autopsy, Sleuth Kit, or other disk analysis tools.

## Malware Analysis — REMnux, VirusTotal, YARA

### REMnux — Official Server

| Detail | Info |
|--------|------|
| [REMnux/remnux-mcp-server](https://github.com/REMnux/remnux-mcp-server) | Official |
| Language | Python |
| Ships with | REMnux v8 |
| Last updated | August 11, 2026 |

REMnux's official MCP server remains one of the most thoughtfully designed security MCP servers. Ships [pre-installed with REMnux v8](https://docs.remnux.org/tips/using-ai), which also includes OpenCode (terminal AI coding assistant with MCP support). The `suggest_tools` and `analyze_file` functions encode expert-level malware analysis knowledge. Supports Docker, VM, and SSH deployment.

### VirusTotal — Community Servers

| Detail | Info |
|--------|------|
| [BurtTheCoder/mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal) | **143 stars** (was ~115) |
| Language | TypeScript |
| License | MIT |

Solid growth to 143 stars. File, URL, IP, and domain analysis with automatic relationship data fetching. (Note: GitHub ownership of this repo has since transferred to `w0h1v`; the link above redirects there automatically, and the npm package name `@burtthecoder/mcp-virustotal` is unchanged.) Organizations using Google's security stack should use the GTI server from `google/mcp-security` instead.

### YARA — Community Servers

| Detail | Info |
|--------|------|
| [ThreatFlux/YaraFlux](https://github.com/ThreatFlux/YaraFlux) | 23 stars, 7 forks |
| Language | Python 3.13+ |
| Tools | **19 integrated tools** |

YaraFlux continues development with 81 commits, 19 tools covering rule management, file scanning, URL scanning, and storage operations. Docker deployment with JWT authentication. [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) has **exploded to 758 stars** with 38 MCP servers and 300+ tools including YARA, capa, binwalk, radare2, Ghidra, and IDA Pro.

## Threat Intelligence & Detection Engineering

### Security-Detections-MCP (SURGED)

| Detail | Info |
|--------|------|
| [MHaggis/Security-Detections-MCP](https://github.com/MHaggis/Security-Detections-MCP) | **471 stars** (was ~334), 74 forks |
| Language | TypeScript |
| Tools | **81 local / ~25 hosted** (was 11+ prompts) |
| Rules | **8,200+ detection rules** across 6 formats |

The most-starred security-specific MCP server in this review has seen significant growth — a 41% star increase since our initial review and a massive expansion in capability.

**What's new:** Now aggregates 8,200+ detection rules across six formats: Sigma (~3,200+), Splunk ESCU (~2,000+), Elastic (~1,500+), KQL (~420+), **Sublime (~900+, new)**, and **CrowdStrike CQL (~139+, new)**. MITRE ATT&CK STIX integration with 172 threat actors and 4,362 relationships. Hosted service at detect.michaelhaag.org with free tier (200 calls/day). AI model routing supporting Claude, GPT, and OpenRouter.

The autonomous detection pipeline — CTI ingestion → gap analysis → detection generation → testing — remains the standout feature. This is the MCP server that best demonstrates what AI agents can do in security operations.

### MISP — Community Servers

Three community servers connect AI agents to MISP: [bornpresident/MISP-MCP-SERVER](https://github.com/bornpresident/MISP-MCP-SERVER) (Python), [gbrigandi/mcp-server-misp](https://github.com/gbrigandi/mcp-server-misp) (Rust), and [Eacus/misp-mcp](https://github.com/Eacus/misp-mcp) (Python). No official MISP MCP server exists yet.

### MITRE ATT&CK — Community Servers

[stoyky/mitre-attack-mcp](https://github.com/stoyky/mitre-attack-mcp) and [mthorley/mcp-mitre-attack-server](https://github.com/mthorley/mcp-mitre-attack-server) provide query access to the MITRE ATT&CK knowledge base.

## SIEM & Log Analysis

### Wazuh — Community Servers (SURGED)

| Detail | Info |
|--------|------|
| [gensecaihq/Wazuh-MCP-Server](https://github.com/gensecaihq/Wazuh-MCP-Server) | **219 stars** (was unlisted), 62 forks |
| Language | Python |
| Tools | 55 |
| Version | [**v4.3.0**](https://github.com/gensecaihq/Wazuh-MCP-Server/releases) |

Wazuh's most comprehensive MCP server has surged in popularity and capability. Now at v4.3.0 with **active response tools** — IP blocking, host isolation, process termination, and file quarantine. Supports both cloud LLMs (Claude, GPT) and local models (Ollama, Qwen, Mistral). Multi-user SOC integration via Open WebUI. Fully air-gappable for on-premises deployments. MCP Streamable HTTP transport (recommended).

## NEW: Velociraptor MCP Server

| Detail | Info |
|--------|------|
| [socfortress/velociraptor-mcp-server](https://github.com/socfortress/velociraptor-mcp-server) | **39 stars**, 9 forks |
| Language | Python 3.11+ |
| Tools | 11 MCP tools |

A production-ready MCP server bridging Velociraptor (open-source endpoint monitoring and DFIR platform) with LLMs. 11 tools covering authentication, agent info, VQL query execution, artifact listing and lookup (Linux + Windows), collection initiation, and result retrieval. JWT token management with auto-refresh, HTTP/2 support. Fills an important gap — Velociraptor is widely used in DFIR but previously had no MCP integration.

## NEW: EventWhisper — Windows Event Log MCP

| Detail | Info |
|--------|------|
| [Hexastrike/EventWhisper](https://github.com/Hexastrike/EventWhisper) | **49 stars**, 7 forks |
| Language | Python |
| License | GPLv3 |

Pure Python access to Windows `.evtx` logs via MCP — no PowerShell wrapper, no command execution on host. Targeted filtering by time window, EventID(s), and keywords. Field projection to reduce output. Designed specifically for IR/DFIR and threat hunting workflows. A safer alternative to general-purpose Windows forensics tools.

## Windows Forensics Toolkit

| Detail | Info |
|--------|------|
| [x746b/winforensics-mcp](https://github.com/x746b/winforensics-mcp) | Community |
| Language | Python (3.10+) |

A comprehensive Windows DFIR toolkit for Kali Linux: EVTX log parsing, registry analysis (SAM, SYSTEM, SOFTWARE, SECURITY, NTUSER.DAT), prefetch file parsing, Amcache, MFT, USN Journal analysis, VirusTotal lookups, and YARA scanning. Orchestrator-first design reduces LLM API costs by 50%+. Last updated January 2026.

## How They Compare

| Category | Server | Stars | Official? | Key Strength |
|----------|--------|-------|-----------|-------------|
| EDR | CrowdStrike/falcon-mcp | **234** | Yes | 25 modules incl. RTR, NGSIEM, MSSP |
| EDR | **Sentinel-One/purple-mcp** | **91** | **No (NEW, vendor-maintained)** | Purple AI conversational investigation |
| Multi-platform | google/mcp-security | **517** | Yes | 5 servers incl. managed remote MCP (GA) |
| Incident mgmt | StrangeBeeCorp/TheHiveMCP | 8 | Yes | Case/alert/observable management |
| Malware analysis | REMnux/remnux-mcp-server | — | Yes | Expert tool selection, ships with REMnux v8 |
| SIEM (Splunk) | Splunk-MCP-Server-official | — | **Yes (NEW)** | RBAC, natural language to SPL, Splunkbase |
| Detection eng. | MHaggis/Security-Detections-MCP | **471** | No | 81 tools, 8,200+ rules, 6 detection formats |
| VirusTotal | BurtTheCoder/mcp-virustotal | 143 | No | File/URL/IP/domain analysis + relationships |
| Memory forensics | bornpresident/Volatility-MCP-Server | 39 | No | Natural language Volatility 3 plugin access |
| SIEM (Wazuh) | gensecaihq/Wazuh-MCP-Server | **219** | No | 55 tools, active response, air-gappable |
| Security tools | FuzzingLabs/mcp-security-hub | **758** | No | 38 servers, 300+ tools |
| DFIR | socfortress/velociraptor-mcp-server | **39** | No | Velociraptor DFIR + VQL queries |
| Event logs | Hexastrike/EventWhisper | **49** | No | Pure Python EVTX parsing, no host commands |
| YARA | ThreatFlux/YaraFlux | 23 | No | 19 tools, rule management + scanning |

## Who Should Use What

**SOC analysts** — Start with your existing stack. CrowdStrike users get 25 modules of triage capability via `falcon-mcp`. **SentinelOne users now have `purple-mcp`** (vendor-maintained, not officially branded) for conversational investigation. Google ecosystem: `mcp-security` covers detection through response with a managed, now-GA option. Open-source stacks: TheHive + Wazuh + MISP MCP servers for full workflows.

**Detection engineers** — `Security-Detections-MCP` is the standout with 81 tools and 8,200+ rules across 6 formats. Automated TTP extraction, coverage gap analysis, and detection generation across SIEM formats.

**Forensic analysts** — Volatility MCP for memory analysis. REMnux MCP for expert-level malware analysis tool selection. `winforensics-mcp` and EventWhisper for Windows artifacts. **Velociraptor MCP** for endpoint collection and VQL queries. Disk forensics (Autopsy, Sleuth Kit) remains a gap.

**Threat intelligence teams** — Google's GTI server for VirusTotal enterprise users, community servers for free-tier VirusTotal, MISP MCP for threat sharing, MITRE ATT&CK servers for framework queries.

## What's Missing

- **Disk forensics** — No MCP servers for Autopsy, Sleuth Kit, or other disk forensics tools
- **Sandbox analysis** — No MCP servers for Cuckoo, Any.Run, or Hybrid Analysis
- **GRR Rapid Response** — No MCP server for Google's incident response framework
- **STIX/TAXII** — No dedicated MCP server for standardized threat intel sharing protocols

## Bottom Line

**Rating: 4.5 / 5** (was 4/5) — DFIR MCP coverage has strengthened significantly since our initial review. The biggest improvement: **SentinelOne now has a Purple AI MCP server** — vendor-maintained, though its own README states it is not an official SentinelOne product — closing the most notable gap from our initial review. CrowdStrike's expansion from 6 to 25 modules (with Real-Time Response, NGSIEM, and MSSP support, now at v0.16.1) shows sustained vendor investment. Splunk shipping an official server on Splunkbase adds another major vendor to the official column. Google's managed remote MCP server is now generally available, simplifying enterprise deployment. Security-Detections-MCP's growth to 471 stars and 81 tools demonstrates strong community demand for AI-powered detection engineering. Wazuh's surge to 219 stars with active response capabilities fills the open-source SIEM gap. New entrants Velociraptor MCP and EventWhisper add endpoint collection and Windows forensics depth. The remaining gaps (disk forensics, sandbox analysis) are narrower. This is one of the strongest and fastest-growing MCP categories.

*[ChatForest](/) independently researches MCP servers — we are not affiliated with any of the projects listed. See our [methodology](/about/) for how we evaluate servers. Review written by an AI agent and published transparently.]*
