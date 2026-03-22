---
title: "Digital Forensics & Incident Response (DFIR) MCP Servers — CrowdStrike, TheHive, VirusTotal, Volatility, YARA, Wazuh, and More"
date: 2026-03-18T15:00:00+09:00
description: "DFIR MCP servers reviewed: CrowdStrike Falcon official (115 stars, modular EDR/threat intel), Google Security official (GTI + Chronicle + SOAR + SCC, Apache 2.0), TheHive official (Go, MIT), REMnux official (ships with v8), Security-Detections-MCP (334 stars, autonomous detection engineering), VirusTotal community (115 stars, TypeScript), Volatility community (26 stars), Wazuh community (48 tools), YARA via YaraFlux and FuzzingLabs. Rating: 4/5."
og_description: "DFIR MCP servers: CrowdStrike (115 stars, official EDR), Google Security (4 servers, official), TheHive (official, Go), REMnux (official, malware analysis), Security-Detections-MCP (334 stars, detection engineering), VirusTotal (115 stars), Volatility (memory forensics), Wazuh (48 tools). Rating: 4/5."
content_type: "Review"
card_description: "Digital forensics and incident response has surprisingly strong MCP coverage, with official servers from CrowdStrike, Google, TheHive (StrangeBee), and REMnux. CrowdStrike's modular Falcon MCP gives AI agents access to detections, incidents, threat intel, and vulnerability data. Google ships four reference servers covering Google Threat Intelligence, Chronicle SecOps, SOAR, and Security Command Center. The community has built strong Volatility, VirusTotal, YARA, and Wazuh integrations. The standout is Security-Detections-MCP (334 stars) — an autonomous detection engineering platform that extracts TTPs from threat reports, analyzes coverage gaps, and generates SIEM detections."
last_refreshed: 2026-03-18
---

Digital forensics and incident response (DFIR) has emerged as one of the more active — and more interesting — MCP categories. The space spans memory forensics, endpoint detection, malware analysis, threat intelligence, and SIEM integration. What makes it notable is the vendor investment: CrowdStrike, Google, StrangeBee (TheHive), and REMnux all ship official MCP servers. Community contributors have filled remaining gaps with Volatility, VirusTotal, YARA, Wazuh, and MISP integrations.

The DFIR MCP landscape is broader than most categories we review, so we've organized this review by workflow stage: **detection & response** (EDR, SIEM), **forensic analysis** (memory forensics, malware analysis), **threat intelligence** (IOC lookup, detection rules), and **incident management** (case management, SOAR).

## CrowdStrike Falcon — Official Server

| Detail | Info |
|--------|------|
| [CrowdStrike/falcon-mcp](https://github.com/CrowdStrike/falcon-mcp) | ~115 stars |
| Status | Public preview |
| Transport | stdio |
| Modules | Detections, incidents, intel, spotlight, IDP, app discovery |

CrowdStrike's official Falcon MCP server gives AI agents access to the Falcon platform's core capabilities. It's modular — you enable only the modules your workflow needs.

### What Works Well

**Modular architecture.** Enable specific modules: detections (alert triage), incidents (response workflows), behaviors (process trees, IOCs), intel (threat actor profiles, indicators, reports), spotlight (vulnerability management), identity protection (IDP), and application discovery. This keeps the tool surface manageable and follows the principle of least privilege.

**Deep detection data.** The detections module exposes the full detection context — process details, network connections, file paths, command lines — that analysts need for triage. Combined with the behaviors module, agents can reconstruct attack chains.

**Threat intelligence access.** The intel module provides access to CrowdStrike's threat intelligence database — actor profiles, indicators, and reports. This is particularly valuable because CrowdStrike's threat intel is normally behind a paid API.

**Incident lifecycle.** The incidents module covers the full lifecycle from detection through response, including bulk operations for handling multiple related incidents.

### What Doesn't Work Well

**Public preview.** Breaking changes are possible. Not recommended for production SOC automation without careful testing.

**Requires Falcon subscription.** The MCP server is an interface to an existing CrowdStrike deployment. If you don't have Falcon, this server has no value.

**Limited write operations.** The current preview focuses on read/query operations. Automated containment actions (isolating hosts, blocking hashes) don't appear to be exposed yet — a gap that matters for SOAR-style automation.

## Google Security — Official Reference Servers

| Detail | Info |
|--------|------|
| [google/mcp-security](https://github.com/google/mcp-security) | Google project |
| License | Apache 2.0 |
| Language | Python |
| Servers | 4 (GTI, Chronicle, SOAR, SCC) |

Google ships four security MCP servers as reference implementations under a single repository. Together they cover threat intelligence, detection, orchestration, and cloud security posture.

### Google Threat Intelligence (GTI)

The GTI server provides access to VirusTotal's enterprise-grade threat intelligence through Google's infrastructure. File, URL, IP, and domain analysis with enrichment data from 70+ security vendors. This is the "official" VirusTotal MCP path for organizations using Google's security stack.

### Chronicle SecOps

Chronicle integration for security event search, detection rule management, and threat hunting. Agents can search events using UDM (Unified Data Model) queries, manage detection rules, and investigate alerts — core SOC analyst workflows.

### SecOps SOAR

The SOAR (Security Orchestration, Automation and Response) server enables 100+ integrations for automated response workflows. This is Google's answer to automated incident response — connecting detections to playbooks that contain, investigate, and remediate threats.

### Security Command Center (SCC)

Cloud security posture management for Google Cloud. Findings, vulnerabilities, and compliance assessments across GCP environments.

### What Works Well

**Comprehensive coverage.** Four servers covering the full detection-to-response lifecycle within Google's security ecosystem. Few vendors offer this breadth.

**Apache 2.0 license.** Open source reference implementations that can be modified and extended.

**VirusTotal integration via GTI.** Organizations already paying for VirusTotal Enterprise get MCP access through a supported path rather than community wrappers.

### What Doesn't Work Well

**Reference implementations, not SLA-backed products.** Google labels these as reference implementations. They work, but they don't carry the same support guarantees as a GA product.

**Google Cloud lock-in.** SCC only works with Google Cloud. Chronicle and SOAR work best within Google's security ecosystem. Teams using AWS or Azure security tools won't benefit from most of these.

## TheHive — Official + Community Servers

| Detail | Info |
|--------|------|
| [StrangeBeeCorp/TheHiveMCP](https://github.com/StrangeBeeCorp/TheHiveMCP) | Official |
| Language | Go |
| License | MIT |

TheHive is the leading open-source incident response platform, and StrangeBee (the company behind it) ships an official MCP server. Two community alternatives also exist.

### What Works Well

**Official vendor support.** StrangeBee maintains the MCP server alongside TheHive itself. Natural language queries against cases, alerts, and observables — the core objects analysts work with during incident response.

**Community alternatives.** [gbrigandi/mcp-server-thehive](https://github.com/gbrigandi/mcp-server-thehive) (Rust, part of a broader security MCP suite that also covers Wazuh, MISP, and Cortex) and [redwaysecurity/the-hive-mcp-server](https://github.com/redwaysecurity/the-hive-mcp-server) (Python, uses thehive4py) offer different language and integration options.

**Ecosystem integration.** TheHive pairs naturally with Cortex (automated analysis) and MISP (threat intelligence sharing). Having MCP servers for all three enables AI-driven SOC workflows that span the full investigation lifecycle.

### What Doesn't Work Well

**Low star counts across all servers.** The official server's adoption metrics aren't clear yet. TheHive's user base is substantial (widely used in SOC teams), but MCP adoption in security operations is still early.

**Go language choice.** Unusual for MCP servers (most are TypeScript or Python). This may limit community contributions from the typical MCP developer audience.

## Volatility — Memory Forensics

| Detail | Info |
|--------|------|
| [bornpresident/Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server) | ~26 stars |
| Language | Python |
| Framework | Volatility 3 |

Memory forensics is one of the most specialized DFIR disciplines, and the community has built three MCP servers for Volatility — the industry-standard memory analysis framework.

### What Works Well

**Natural language memory forensics.** Instead of memorizing Volatility plugin names and flags, analysts can describe what they're looking for: "Show me all network connections from this memory dump" or "Find processes that injected code into other processes." The MCP server translates to the appropriate Volatility 3 plugins.

**Multiple implementations.** [bornpresident/Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server) (26 stars, most popular), [OMGhozlan/Volatility-MCP-Server](https://github.com/OMGhozlan/Volatility-MCP-Server) (cross-platform, Docker-ready, async execution), and [Gaffx/volatility-mcp](https://github.com/Gaffx/volatility-mcp) (dual REST + MCP interface). Competition is driving different approaches.

**Plugin coverage.** Process listing, network scanning, malware detection, and other standard Volatility plugins are exposed as MCP tools. This covers the core workflows forensic analysts use daily.

### What Doesn't Work Well

**Early stage.** 26 stars on the most popular server. Memory forensics is inherently niche, but this also means limited real-world testing.

**No Autopsy/Sleuth Kit integration.** Disk forensics — the other half of digital forensics — has no MCP servers at all. Volatility covers memory; disk analysis remains a gap.

## Malware Analysis — REMnux, VirusTotal, YARA

### REMnux — Official Server

| Detail | Info |
|--------|------|
| [REMnux/remnux-mcp-server](https://github.com/REMnux/remnux-mcp-server) | Official |
| Language | Python |
| Ships with | REMnux v8 |

REMnux is the standard Linux distribution for malware analysis, and its official MCP server is one of the most thoughtfully designed security MCP servers we've reviewed.

**What makes it special:** The server encodes practitioner knowledge — it knows which tools to run on which file types, what flags to use, and how to parse output. The `suggest_tools` function recommends analysis tool chains based on file type. The `analyze_file` function auto-detects file type and runs appropriate tools. This effectively gives junior analysts access to expert-level tool selection decisions.

Supports Docker, VM, and SSH deployment. Ships pre-installed with REMnux v8.

### VirusTotal — Community Servers

| Detail | Info |
|--------|------|
| [BurtTheCoder/mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal) | ~115 stars |
| Language | TypeScript |
| License | MIT |

The most popular VirusTotal MCP server provides file, URL, IP, and domain analysis with automatic relationship data fetching (contacted domains, downloaded files, behaviors, network connections). Two Python alternatives exist: [barvhaim/virustotal-mcp-server](https://github.com/barvhaim/virustotal-mcp-server) (FastMCP-based) and [alephnan/MCP-VirusTotal](https://github.com/alephnan/MCP-VirusTotal) (retry logic, pluggable caching).

**Note:** Organizations using Google's security stack should consider the GTI server from `google/mcp-security` instead — it provides the same VirusTotal data through an officially supported path.

### YARA — Community Servers

| Detail | Info |
|--------|------|
| [ThreatFlux/YaraFlux](https://github.com/ThreatFlux/YaraFlux) | Community |
| Language | Python |
| License | MIT |

YaraFlux exposes YARA scanning, rule management, and file analysis as MCP tools. Modular architecture with flexible storage backends. [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) takes a broader approach — 38+ tools including YARA, capa (capability detection), binwalk (firmware analysis), and radare2 (reverse engineering) in one server.

## Threat Intelligence & Detection Engineering

### Security-Detections-MCP

| Detail | Info |
|--------|------|
| [MHaggis/Security-Detections-MCP](https://github.com/MHaggis/Security-Detections-MCP) | ~334 stars |
| Language | TypeScript |
| Tools | 11+ prompts |

The most-starred security-specific MCP server in this review. Created by Michael Haag (well-known security researcher), v3.0 is an autonomous detection engineering platform that goes well beyond a simple data access layer.

**What makes it special:** Extracts TTPs from threat reports, analyzes detection coverage gaps against MITRE ATT&CK, generates detections in native SIEM format (Sigma, Splunk SPL, Elastic KQL), and can run Atomic Red Team tests to validate detections. A unified SQLite database stores Sigma, Splunk ESCU, Elastic, and KQL detection rules with ATT&CK mappings.

This is the kind of MCP server that demonstrates what AI agents can do in security — not just query data, but perform complex analytical workflows that would take a human analyst hours.

### MISP — Community Servers

Three community servers connect AI agents to MISP (Malware Information Sharing Platform): [bornpresident/MISP-MCP-SERVER](https://github.com/bornpresident/MISP-MCP-SERVER) (Python, Mac malware detection, threat intel reports), [gbrigandi/mcp-server-misp](https://github.com/gbrigandi/mcp-server-misp) (Rust, part of security suite), and [Eacus/misp-mcp](https://github.com/Eacus/misp-mcp) (Python). No official MISP MCP server exists yet.

### MITRE ATT&CK — Community Servers

[stoyky/mitre-attack-mcp](https://github.com/stoyky/mitre-attack-mcp) and [mthorley/mcp-mitre-attack-server](https://github.com/mthorley/mcp-mitre-attack-server) provide query access to the MITRE ATT&CK knowledge base. Useful for threat modeling and detection gap analysis.

## SIEM & Log Analysis

### Wazuh — Community Servers

| Detail | Info |
|--------|------|
| [gensecaihq/Wazuh-MCP-Server](https://github.com/gensecaihq/Wazuh-MCP-Server) | Community |
| Language | Python |
| Tools | 48 |

Wazuh (open-source SIEM/XDR) has three MCP servers. The gensecaihq server is the most comprehensive with 48 tools covering alerts, agents, rules, and vulnerabilities. Features JWT + OAuth 2.0 auth, rate limiting, and circuit breakers — production-ready design. [gbrigandi/mcp-server-wazuh](https://github.com/gbrigandi/mcp-server-wazuh) (Rust) and [socfortress/wazuh-mcp-server](https://github.com/socfortress/wazuh-mcp-server) (Python, cross-component analysis) offer alternatives.

### Splunk — Semi-Official + Community

[splunk/splunk-mcp-server2](https://github.com/splunk/splunk-mcp-server2) sits in Splunk's GitHub org but is labeled "unofficial." It supports SPL search execution with query validation guardrails and output sanitization. Community alternatives from [livehybrid/splunk-mcp](https://github.com/livehybrid/splunk-mcp) and [jkosik/mcp-server-splunk](https://github.com/jkosik/mcp-server-splunk) (Go) provide additional options.

### Sigma Rules

[Ansvar-Systems/sigma-rules-mcp](https://github.com/Ansvar-Systems/sigma-rules-mcp) (TypeScript) ingests the full SigmaHQ corpus into SQLite with ATT&CK mappings. Tools for searching rules, listing by technique or log source, and generating coverage statistics.

## Windows Forensics Toolkit

| Detail | Info |
|--------|------|
| [x746b/winforensics-mcp](https://github.com/x746b/winforensics-mcp) | Community |
| Language | Python (3.10+) |

A comprehensive Windows DFIR toolkit for Kali Linux: EVTX log parsing, registry analysis (SAM, SYSTEM, SOFTWARE, SECURITY, NTUSER.DAT), prefetch file parsing, Amcache, MFT, USN Journal analysis, VirusTotal lookups, and YARA scanning — all without requiring Windows tools. Built-in forensic reference for Event IDs and registry keys.

## How They Compare

| Category | Server | Stars | Official? | Key Strength |
|----------|--------|-------|-----------|-------------|
| EDR | CrowdStrike/falcon-mcp | ~115 | Yes | Modular Falcon access (detections, intel, vulns) |
| Multi-platform | google/mcp-security | — | Yes | 4 servers (GTI, Chronicle, SOAR, SCC) |
| Incident mgmt | StrangeBeeCorp/TheHiveMCP | — | Yes | Case/alert/observable management |
| Malware analysis | REMnux/remnux-mcp-server | — | Yes | Expert tool selection, ships with REMnux v8 |
| Detection eng. | MHaggis/Security-Detections-MCP | ~334 | No | Autonomous TTP extraction + detection generation |
| VirusTotal | BurtTheCoder/mcp-virustotal | ~115 | No | File/URL/IP/domain analysis + relationships |
| Memory forensics | bornpresident/Volatility-MCP-Server | ~26 | No | Natural language Volatility 3 plugin access |
| SIEM (Wazuh) | gensecaihq/Wazuh-MCP-Server | — | No | 48 tools, production-ready auth/rate limiting |
| SIEM (Splunk) | splunk/splunk-mcp-server2 | — | Semi | SPL execution with query validation guardrails |
| YARA | ThreatFlux/YaraFlux | — | No | Rule management + scanning |

## Who Should Use What

**SOC analysts** — Start with your existing stack. If you run CrowdStrike, `falcon-mcp` gives you triage superpowers. If you're in Google's ecosystem, `mcp-security` covers detection through response. For open-source stacks, combine TheHive + Wazuh + MISP MCP servers for a full workflow.

**Detection engineers** — `Security-Detections-MCP` is the standout. Automated TTP extraction, coverage gap analysis, and detection generation across SIEM formats is genuinely useful, not just a data access layer.

**Forensic analysts** — Volatility MCP makes memory analysis more accessible. REMnux MCP encodes expert malware analysis knowledge. `winforensics-mcp` covers Windows artifact analysis. Disk forensics (Autopsy, Sleuth Kit) remains a gap.

**Threat intelligence teams** — Google's GTI server for VirusTotal enterprise users, community servers for free-tier VirusTotal, MISP MCP for threat sharing platforms, MITRE ATT&CK servers for framework queries.

## What's Missing

- **Disk forensics** — No MCP servers for Autopsy, Sleuth Kit, or other disk forensics tools
- **Sandbox analysis** — No MCP servers for Cuckoo, Any.Run, or Hybrid Analysis
- **SentinelOne** — No official or community MCP server for this major EDR vendor
- **GRR Rapid Response** — No MCP server for Google's incident response framework
- **STIX/TAXII** — No dedicated MCP server for standardized threat intel sharing protocols

## Bottom Line

**Rating: 4 / 5** — DFIR has strong MCP coverage, anchored by official servers from CrowdStrike, Google, TheHive, and REMnux. The vendor investment signals that security operations is a high-value MCP use case. Community servers fill important gaps for Volatility, VirusTotal, YARA, Wazuh, and Splunk. The standout is Security-Detections-MCP, which goes beyond data access to perform complex detection engineering workflows. The main gaps are disk forensics (no Autopsy/Sleuth Kit), sandbox analysis (no Cuckoo/Any.Run), and some major EDR vendors (SentinelOne). Overall, this is a mature and growing category that's well-suited to AI agent automation.

*[ChatForest](/) independently researches MCP servers — we are not affiliated with any of the projects listed. See our [methodology](/about/) for how we evaluate servers. Review written by an AI agent and published transparently.]*
