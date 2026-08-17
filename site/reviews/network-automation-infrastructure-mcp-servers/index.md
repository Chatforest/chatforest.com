# Network Automation & Infrastructure MCP Servers — Multi-Vendor Management, NetBox, Netmiko, pyATS, Firewalls, Juniper, Network Diagnostics, and Digital Twins

> Network automation and infrastructure MCP servers let AI agents manage multi-vendor network devices, query DCIM/IPAM systems, run CLI commands over SSH, manage firewalls, perform DNS/WHOIS lookups


Network automation and infrastructure MCP servers let AI agents manage routers, switches, and firewalls across vendors, query DCIM/IPAM systems for device inventories, automate CLI commands over SSH, perform DNS and WHOIS lookups, trace network paths, and interact with network digital twins — all through natural language. Instead of writing Ansible playbooks or SSH scripts, an AI agent can ask "show me all BGP neighbors on the core routers" or "what IPs are available in the 10.0.1.0/24 subnet" and get structured results.

This review covers **network automation and infrastructure MCP servers** — multi-vendor management platforms, Cisco-specific tools, DCIM/IPAM, SSH device automation, network diagnostics, and network digital twins. For security-focused network tools (packet capture, port scanning, pentesting), see our [Network Security review](/reviews/network-security-mcp-servers/). For monitoring and observability platforms, see [Time-Series Database MCP](/reviews/time-series-database-mcp-servers/).

The headline findings: **Three of the biggest gaps have been filled** — Juniper now has an official MCP server, Palo Alto launched the Cortex MCP Server in open beta, and Fortinet has an entire ecosystem of 4 community servers. **netclaw has become a platform** — surging from 135 to 636 stars with 222 skills across 165 MCP servers, adding Cisco AI Defense governance, institutional memory, and a 3D operations dashboard. **NetBox MCP reached v1.0.0** with native field filtering and HTTP/SSE transport. **Itential brings enterprise orchestration** with 56+ tools and policy-driven automation. **Forward Networks announced Forward AI**, scheduled for GA April 2026, with MCP-powered agentic workflows built on its mathematically accurate digital twin. **IETF discussions on MCP for networking are underway** — multiple individual drafts (no working-group standing yet) propose extensions for YANG datastores and NETCONF integration. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

---

## Multi-Vendor Platforms

### E-Conners-Lab/NetworkOps_Platform — 178 Tools for Multi-Vendor Network Automation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [NetworkOps_Platform](https://github.com/E-Conners-Lab/NetworkOps_Platform) | 8 | Python | — | 178 |

**The most ambitious network automation MCP project** — supports Cisco, Juniper, Nokia, Arista, and Linux devices through natural language:

- **178 tools** for infrastructure management, configuration, and troubleshooting
- **Self-healing agents** that detect and remediate network issues autonomously
- **Drift detection** to identify configuration changes from baseline
- **Real-time web dashboard** with interactive force-directed network topology
- **Visualization** for OSPF adjacencies, BGP sessions with AS number annotations
- **RAG-powered chat** with live network queries and source citations
- **Demo mode** simulates a multi-device network for testing

The go-to platform for network engineers who manage heterogeneous environments and want AI-assisted operations across all their vendors.

### automateyournetwork/netclaw — Autonomous Network Engineering Agent ⬆️ SURGED

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [netclaw](https://github.com/automateyournetwork/netclaw) | 636 ⬆️ | Python | Apache-2.0 | 222 skills / 165 MCPs |

**An autonomous network engineering coworker**, not just a tool — netclaw operates as a peer engineer powered by Anthropic Claude. **SURGED from 135 to 636 stars (+371%)** and now the most comprehensive network automation agent available, per the [live repo](https://github.com/automateyournetwork/netclaw):

- **222 deployable skills** backed by **165 MCP servers** (was 82 skills / 37 MCPs, then 112/69) for comprehensive network operations
- **Device automation** via pyATS (IOS-XE, NX-OS, IOS-XR), Juniper PyEZ/NETCONF, Arista CloudVision
- **Platform integrations** — Cisco Catalyst Center, CML, NSO, ISE, Meraki, FMC, F5 BIG-IP
- **NEW DefenseClaw** — Cisco AI Defense integration with kernel-level sandbox isolation, component scanning, audit logging for SOC2/PCI-DSS compliance
- **NEW MemPalace** — institutional memory MCP server, learns protocols automatically from status responses
- **NEW DevOps integrations** — Jenkins, GitLab, Atlassian for CI/CD pipeline triggering
- **NEW observability** ��� Splunk and Datadog enterprise observability through natural language
- **NEW 3D operations dashboard** — Three.js visualization with device fleet status, BGP peering topology, inline Canvas/A2UI network visualizations rendered in chat
- **ITSM integration** — ServiceNow Change Requests and Incident Management workflow
- **Safety guardrails** — never guesses device state without running a show command, captures pre-change state before any config push, requires Change Request approval before execution
- **NVIDIA OpenShell** integration for enterprise deployment

Built on the OpenClaw agent framework. The safety constraints and governance features make this the most production-ready network automation agent available.

---

## Cisco Ecosystem

### Cisco ThousandEyes MCP Server (Official)

| Server | Stars | Language | Transport | Tools |
|--------|-------|----------|-----------|-------|
| [ThousandEyes-MCP-Server-official](https://github.com/CiscoDevNet/ThousandEyes-MCP-Server-official) | 3 | Remote hosted | Streamable HTTP | 28 |

**→ [Full review: Cisco ThousandEyes MCP Server](/reviews/thousandeyes-mcp-server/)**

**Cisco's official ThousandEyes MCP server is a fully hosted remote server** — no local software to deploy, no Docker containers to run. Connect Claude Desktop, Cursor, VS Code, or AWS Kiro to `https://api.thousandeyes.com/mcp` and authenticate via Bearer token or OAuth2 Dynamic Client Registration. Launched February 4, 2026.

ThousandEyes is Cisco's network intelligence platform — it monitors what's *between* users and services (internet paths, ISP routing, CDN health, BGP changes) rather than what's *inside* infrastructure. The MCP server exposes 28 tools across 9 categories:

- **Synthetic tests** — list, view, create, update, delete scheduled tests
- **Instant tests** — run on-demand tests against any target *(consumes billing units)*
- **Events and alerts** — triage active and historical network/application problems
- **Outage correlation** — search outages from Internet Insights data
- **Anomaly detection** — surface metric anomalies over time ranges
- **Path visualization** — hop-by-hop network path maps
- **BGP analysis** — routing data and reachability results
- **Endpoint monitoring** — employee device and wireless performance
- **Template deployment** — stand up complete test/dashboard/alert configurations from templates

Tools are split into two configurable permission groups: **read-only** (22 tools, safe to enable broadly) and **write/delete** (6 tools, test management and template deployment). Cisco recommends enabling only what you need — too many tools active simultaneously causes latency and timeouts.

The official GitHub repo is essentially a configuration guide (3 stars, 3 commits); the actual server is proprietary and Cisco-hosted. Notable gap: **Internet Insights data is not exposed** — the collective ISP/CDN outage intelligence that distinguishes ThousandEyes from general observability tools cannot be queried through MCP. Alert rule management is also absent.

**Target audience**: NOC engineers, MSPs, and SREs whose organizations already use ThousandEyes. ThousandEyes subscription with API Access role required. Government deployments not supported.

### pamosima/network-mcp-docker-suite — 10 Docker-Based Network MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [network-mcp-docker-suite](https://github.com/pamosima/network-mcp-docker-suite) | 52 | Python | — | 10 servers |

**A complete Docker-based MCP suite for Cisco-centric network operations**, featured on the Cisco Switzerland Technology Blog and Cisco Code Exchange:

- **Meraki MCP Server** (port 8000) — cloud network management via Dashboard API
- **NetBox MCP Server** (port 8001) — DCIM/IPAM infrastructure documentation
- **Catalyst Center MCP Server** (port 8002) — enterprise network management and assurance
- **IOS XE MCP Server** (port 8003) — direct SSH-based device management
- **ThousandEyes MCP Server** (port 8004) — network performance monitoring and path visualization (community implementation; the official remote server is the recommended production choice)
- **ISE MCP Server** (port 8005) — identity and access control
- **Splunk MCP Server** (port 8006) — log analysis and operational intelligence
- **GitLab MCP Server** (port 8009) — CI/CD pipeline triggering for network automation
- AI-ready with **LibreChat, Cursor, and other MCP clients**

Each server runs in its own Docker container with dedicated ports. Best for Cisco shops wanting all these tools in a single deployment without using the official hosted endpoints.

### automateyournetwork/pyATS_MCP — Cisco pyATS/Genie Device Interaction

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pyATS_MCP](https://github.com/automateyournetwork/pyATS_MCP) | 79 ⬆️ | Python | — | 5+ |

**Structured network device interaction** through Cisco's pyATS and Genie testing frameworks:

- **Connects to Cisco IOS/NX-OS devices** defined in a pyATS testbed
- **Safe execution** of validated CLI commands (show, ping)
- **Controlled configuration changes** with structured output
- **Returns parsed or raw output** — structured data for automation, raw for troubleshooting
- **STDIO-based** JSON-RPC 2.0 protocol — ideal for containerized or LangGraph integrations

pyATS is the standard testing framework for Cisco's own engineering teams. Having it accessible via MCP brings enterprise-grade device interaction to AI agents.

### automateyournetwork/MCPyATS — VibeOps Framework

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MCPyATS](https://github.com/automateyournetwork/MCPyATS) | 68 | Python | — | Multiple |

**VibeOps — a framework combining MCP, Agent-to-Agent (A2A), LangGraph, and Cisco pyATS** for intelligent distributed network agents:

- Multiple tool-integrated MCP servers with Docker deployment
- LangGraph agent backend with Streamlit UI frontend
- Supports Agent-to-Agent (A2A) communication between network agents
- Configurable LLM backend (default GPT-4o, supports Gemini and others)
- Modular and extensible architecture for adding new tools and services

### xorrkaz/cml-mcp — Cisco Modeling Labs

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cml-mcp](https://github.com/xorrkaz/cml-mcp) | 69 | Python | — | — |

**Speak your lab into existence** — create and manage Cisco Modeling Labs environments via natural language:

- Build network labs and topologies through conversational commands
- Available via PyPI: `pip install cml-mcp`

---

## DCIM/IPAM

### netboxlabs/netbox-mcp-server — Official NetBox DCIM/IPAM ⬆️ v1.0.0

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [netbox-mcp-server](https://github.com/netboxlabs/netbox-mcp-server) | 214 ⬆️ | Python | Apache 2.0 | 3 core tools |

**The official MCP server from NetBox Labs** for the industry-standard DCIM/IPAM platform. **Reached v1.0.0** — 127→214 stars (+69%), 232 commits, major maturity milestone, per the [live repo](https://github.com/netboxlabs/netbox-mcp-server):

- **Read-only access** to NetBox data — deliberately safe for AI agent queries
- **Three core tools**: get_objects (filtered retrieval), get_object_by_id (detail view), get_changelogs (audit trail)
- **NEW native field filtering** — leverages NetBox's filtering capabilities for efficient queries
- **NEW enhanced pagination** for large datasets
- **NEW HTTP/SSE transport** for web-based MCP clients
- **NEW Docker containerization** with proper environment variable handling
- **NEW global search** — cross-object searching across DCIM, IPAM, circuits, virtualization, tenancy, VPN, wireless
- **Smarter object type mapping** across all NetBox modules
- Part of the broader NetBox ecosystem (20,000+ stars for the core NetBox project)

NetBox is the premier source of truth for network infrastructure. The v1.0.0 release signals production readiness — "intentionally simple, easy to get started with, hard to misuse."

### Community NetBox MCPs

Additional NetBox MCP implementations exist:

- **[ardecode/netbox-mcp-server](https://github.com/ardecode/netbox-mcp-server)** — a lighter community alternative currently exposing 3 tools (`get_all_clusters`, `get_cluster_virtual_machines`, `get_cluster_interfaces`) for NetBox virtualization-cluster queries
- **[Deployment-Team/netbox-mcp](https://github.com/Deployment-Team/netbox-mcp)** — NetBox Cloud integration

### gt732/nautobot-app-mcp — Nautobot Network Source of Truth 🆕

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nautobot-app-mcp](https://github.com/gt732/nautobot-app-mcp) | 16 | Python | Apache 2.0 | Custom |

**Nautobot DCIM/IPAM MCP plugin** — an alternative to NetBox for organizations using Nautobot as their network source of truth:

- Runs an MCP server alongside Nautobot exposing tools for AI systems
- **Custom tool creation** via Python functions
- Web interface to view all registered tools with descriptions and parameters
- Configurable host, port, and custom tools directory
- Supports deployment via systemd service

Note: This repository has been archived, but provides a reference implementation for Nautobot-MCP integration.

---

## Juniper 🆕 GAP FILLED

### Juniper/junos-mcp-server — Official Juniper JunOS MCP 🆕

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [junos-mcp-server](https://github.com/Juniper/junos-mcp-server) | 103 | Python | Apache-2.0 | 5+ |

**FILLS THE BIGGEST VENDOR GAP** — Juniper Networks now has an official MCP server for Junos devices. Previously, Juniper access was only available through multi-vendor tools like netclaw:

- **PyEZ integration** for advanced network operations
- **SSH authentication** with device management
- **Dynamic device discovery** via `add_device` tool
- **Command guardrails** — block.cmd configuration prevents dangerous commands
- **Token-based authentication** for secure streamable-http transport
- **Docker deployment** support
- 99 commits, actively maintained with comprehensive documentation

The official Juniper investment in MCP validates the protocol for enterprise networking. Network engineers can now manage Junos devices through natural language with proper safety controls.

### Community Juniper Resources

- **Juniper community blog** — workshops on agentic AI using JunOS and Linux MCP servers
- **Managing Junos Devices with Context-File and JMCP Server** — February 2026 guide on LLM-driven Junos management

---

## Firewall & Security Vendors 🆕 GAP FILLED

### Palo Alto Networks — Official Cortex MCP + Community PanOS 🆕

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Cortex MCP Server](https://www.paloaltonetworks.com/blog/security-operations/introducing-the-cortex-mcp-server/) | Official | — | Commercial | SOC tools |
| [Palo-MCP](https://github.com/apius-tech/Palo-MCP) | 24 | TypeScript | — | 117 |
| [pan-os-mcp](https://github.com/cdot65/pan-os-mcp) | 12 | Python | MIT | 4+ |

**FILLS THE FIREWALL GAP** — Palo Alto Networks launched the Cortex MCP Server in open beta, plus two community PanOS servers:

- **[Cortex MCP Server](https://www.paloaltonetworks.com/blog/security-operations/introducing-the-cortex-mcp-server/) (Official, open beta)** — real-time intelligence from Cortex to LLM applications such as Claude for Desktop; lets analysts query cases, issues, assets, endpoints, compliance results, and tenant metadata, and pull event timelines and related-asset context for high-severity investigations
- **[apius-tech/Palo-MCP](https://github.com/apius-tech/Palo-MCP)** — **117 tools across 16 modules** for PanOS firewalls via XML API, with OS-keychain credential storage (never plaintext) and 103 commits. Every tool labeled READ-ONLY or MODIFIES CONFIG for safety. Supports Panorama centralized management
- **cdot65/pan-os-mcp** — MCP server for XML API interaction with NGFW appliances, supports standalone firewalls and Panorama, HTTP/SSE endpoints

The first major firewall vendor with an official MCP server marks a turning point for AI-driven security operations.

### Fortinet — Community Ecosystem Explosion 🆕

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [fortigate-mcp-server](https://github.com/alpadalar/fortigate-mcp-server) | 34 | Python | MIT | 33 |
| [fortianalyzer-mcp](https://github.com/rstierli/fortianalyzer-mcp) | 12 | Python | MIT | 73 |
| [fortimonitor-mcp-server](https://github.com/gjenkins20/unofficial-fortimonitor-mcp-server) | 3 | Python | MIT | 241 |

**Fortinet ecosystem EXPLODED from zero to 4 servers**, covering the full Fortinet Security Fabric:

- **[alpadalar/fortigate-mcp-server](https://github.com/alpadalar/fortigate-mcp-server)** — 33 tools for FortiGate firewall management (30 registrations via stdio, 31 via HTTP transport): policies, network objects, VIPs/NAT, routing, system health. Fully async Python with persistent HTTP pooling. Production-ready
- **[rstierli/fortianalyzer-mcp](https://github.com/rstierli/fortianalyzer-mcp)** — 73 tools across 12 categories for SOC operations: log analysis, real-time analytics (FortiView), alert management, incident tracking, device management, reporting (PDF/HTML/CSV/XML). Requires FortiAnalyzer 7.x
- **[gjenkins20/unofficial-fortimonitor-mcp-server](https://github.com/gjenkins20/unofficial-fortimonitor-mcp-server)** — **241 tools across 33 modules** for FortiMonitor/Panopta monitoring infrastructure. Near-complete coverage of the FortiMonitor v2 API
- **[jmpijll/fortimanager-mcp](https://github.com/jmpijll/fortimanager-mcp)** — Archived March 2026, deprecated in favor of **[fortimanager-code-mode-mcp](https://github.com/jmpijll/fortimanager-code-mode-mcp)**. Original had 590+ tools (118K+ tokens just for tool definitions — too many for LLM context); replacement uses a Code Mode pattern with just 2 tools (`search` + `execute`) for flexible API interaction

No official Fortinet MCP server yet, but the community has built comprehensive coverage across FortiGate, FortiAnalyzer, FortiMonitor, and FortiManager.

---

## Enterprise Orchestration 🆕

### itential/itential-mcp — Enterprise Network Automation Orchestration 🆕

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [itential-mcp](https://github.com/itential/itential-mcp) | 35 | Python | GPL v3 | 56+ |

**The AI control layer for enterprise network automation** — bridges AI-generated intent with infrastructure execution:

- **56+ automation tools** across 10 categories: device management, workflow operations, compliance, templates
- **Policy-driven execution** — every AI intent passes through validations and approvals
- **Device management** — configuration, backup, command execution across vendors
- **Workflow orchestration** — execution and job tracking with Itential Platform
- **Compliance management** — automated compliance plan execution
- **Template support** — Jinja2 and TextFSM template management
- **Multiple transports** — stdio, SSE, and HTTP with optional TLS
- Works with GPT, Claude, Gemini, or private models
- Available on PyPI: `pip install itential-mcp`

Itential positions MCP as the "universal translator" between AI and network orchestration, with Selector's AI surfacing critical events and Itential handling policy validation and automated remediation.

---

## Arista 🆕 GAP PARTIALLY FILLED

### Community Arista MCP Servers 🆕

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [arista-mcp-automation](https://github.com/jotasantos/arista-mcp-automation) | — | Python | — | — |

**Arista CloudVision and EOS MCP access** — community-built servers for Arista network management:

- **CloudVision MCP** (noredistribution) — device inventory, system events, connectivity monitoring, tag management through conversational prompts
- **arista-mcp-automation** (jotasantos) — AI-powered Arista network automation using Claude Code and MCP

Arista has publicly embraced MCP, with blog posts on "Generative and Agentic AI Networking Revolution" combining EOS and NetDL with MCP. No official server yet, but vendor investment signals one is likely.

---

## Device Automation (SSH/CLI)

### melihteke/mcp-server-netmiko — Multi-Vendor SSH Automation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-netmiko](https://github.com/melihteke/mcp-server-netmiko) | — | Python | — | 5+ |

**SSH-based network device management** using the industry-standard Netmiko library:

- **Multi-vendor support** — Cisco, Juniper, Arista, and dozens more device types
- **Show commands and configuration changes** across routers and switches
- **Log and metric collection** for analysis
- **Troubleshooting automation** — streamline diagnostic workflows

[Netmiko](https://github.com/ktbyers/netmiko) (4,200+ stars) is a widely used Python library for SSH to network devices. This MCP wrapper makes it accessible to AI agents.

### upa/mcp-netmiko-server — LLM-to-Device Interaction

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-netmiko-server](https://github.com/upa/mcp-netmiko-server) | — | Python | — | — |

Another Netmiko-based MCP server focused on enabling LLMs to interact directly with network devices via SSH sessions.

### melihteke/Subnet-Calculator-MCP-Server — IP Subnet Calculations

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Subnet-Calculator-MCP-Server](https://github.com/melihteke/Subnet-Calculator-MCP-Server) | — | Python | — | — |

Dedicated subnet calculator for AI agents — useful for IP planning tasks where you need to calculate network addresses, broadcast addresses, available hosts, and CIDR notation conversions.

---

## Network Diagnostics & DNS Tools

### patrickdappollonio/mcp-netutils — DNS, WHOIS, TLS, and Connectivity Testing (renamed)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-netutils](https://github.com/patrickdappollonio/mcp-netutils) | 10 | Go | — | 6+ |

**Comprehensive network and domain analysis** in a single MCP server (formerly mcp-domaintools, renamed to mcp-netutils):

- **DNS lookups** — resolve any record type (A, AAAA, MX, CNAME, TXT, etc.) with DNS-over-HTTPS support
- **WHOIS queries** — domain registration details and expiration dates
- **TLS certificate analysis** — inspect SSL certificates, chain validation, expiration
- **HTTP endpoint monitoring** — check status codes, response times, headers
- **Connectivity testing** — ping and port checks
- **Hostname resolution** — forward and reverse DNS
- **SSE support** — can run as an HTTP server
- Available via Docker, Homebrew, npm, and binary releases

The Swiss Army knife for domain and network diagnostics — handles the tasks network engineers do dozens of times daily.

### kumarprobeops/probeops-mcp-server — Global Infrastructure Diagnostics

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [probeops-mcp-server](https://github.com/kumarprobeops/probeops-mcp-server) | — | TypeScript | — | 8+ |

**Run diagnostics from 6 global regions simultaneously** — no API key required:

- **Distributed testing** from US East, US West, EU Central, Canada, India, Australia
- **SSL checks, DNS lookups, ping, WHOIS, port checks, traceroute, latency tests**
- Tests execute simultaneously from all regions for comparative analysis
- Run instantly via `npx @probeops/mcp-server`
- **Geo-proxy browsing** for testing geo-restricted content

Particularly valuable for diagnosing latency issues, DNS propagation problems, or verifying global service availability.

### deshabhishek007/domain-tools-mcp-server — Domain Analysis

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [domain-tools-mcp-server](https://github.com/deshabhishek007/domain-tools-mcp-server) | — | — | — | 3 |

**Focused domain analysis** with three core tools:

- **WHOIS lookup** — domain registration details
- **DNS record queries** — all record types
- **DNS health checking** — identify configuration issues

---

## Network Analysis & Digital Twins

### forwardnetworks/forward-mcp — Network Digital Twin with 54 Tools ⬆️ Forward AI GA

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [forward-mcp](https://github.com/forwardnetworks/forward-mcp) | 4 | Python | — | 54 |

**Enterprise-grade network analysis** powered by Forward Networks' vendor-agnostic digital twin technology. **[Forward AI was announced January 29, 2026, scheduled for GA in April 2026](https://www.forwardnetworks.com/newsroom/forward-networks-introduces-forward-ai/)** — agentic AI built on the mathematical network digital twin:

- **54 tools** (plus 6 workflow prompts and a network-context resource) for network topology analysis, path tracing, device management, and configuration auditing
- **NEW Forward AI** — agentic workflows that dynamically plan and execute multi-step operations across hybrid and multi-cloud environments, built on a "mathematically accurate digital twin" so results come with evidence teams can inspect and validate, per [Forward Networks' announcement](https://www.forwardnetworks.com/newsroom/forward-networks-introduces-forward-ai/)
- **Path verification** — trace traffic paths across the entire network, identify where packets would be dropped or redirected
- **Semantic search** using embedding-based similarity matching of network queries (NQE)
- **Bloomsearch integration** for efficient handling of large result sets with automatic bloom filter generation
- **Snapshot management** for point-in-time network state capture and comparison

Forward Enterprise creates a mathematical model of your entire network — this MCP server makes that model queryable by AI agents. Forward AI takes this further: instead of just answering queries, it plans and executes multi-step workflows while maintaining mathematical certainty about its recommendations.

---

## IETF Standardization 🆕

The networking industry is formalizing MCP for network management through multiple individual IETF Internet-Drafts (none yet adopted by a working group or carrying formal IETF standing):

- **[draft-zw-nmrg-mcp-network-mgmt](https://datatracker.ietf.org/doc/draft-zw-nmrg-mcp-network-mgmt/)** ("Model Context Protocol (MCP) Extensions for Network Equipment Management") — defines MCP extensions for network equipment, allowing routers/switches to act as MCP servers exposing CLI, YANG datastores, and event streams. The original draft-zeng-mcp-network-mgmt was replaced by draft-zw-rtgwg-mcp-network-mgmt, now current as draft-zw-nmrg-mcp-network-mgmt
- **[draft-yang-nmrg-mcp-nm](https://datatracker.ietf.org/doc/draft-yang-nmrg-mcp-nm/)** ("Applicability of MCP for the Network Management") — applicability of MCP for network management, comparing MCP with NETCONF/RESTCONF/gNMI; authored by contributors from Huawei, Telefónica, Deutsche Telekom, Orange, and Nokia
- **[draft-zeng-opsawg-applicability-mcp-a2a](https://datatracker.ietf.org/doc/draft-zeng-opsawg-applicability-mcp-a2a/)** ("When NETCONF Is Not Enough") — explores scenarios where MCP and Agent-to-Agent (A2A) complement traditional protocols
- **[draft-zeng-mcp-troubleshooting](https://datatracker.ietf.org/doc/draft-zeng-mcp-troubleshooting/)** ("Using MCP for Intent-Based Network Troubleshooting Automation") — now superseded by draft-zm-rtgwg-mcp-troubleshooting

These drafts signal that MCP is being discussed within the networking standards community, not just the AI community — though as individual submissions with no working-group adoption, they carry no formal IETF standing yet. The YANG datastore extensions are particularly significant — they could bridge model-driven programmability with AI-driven operations.

---

## What's Missing

Major gaps have been filled since the initial review, but some remain:

- ~~No dedicated Juniper MCP~~ — **FILLED**: Juniper/junos-mcp-server (103 stars, official)
- ~~No Palo Alto or Fortinet firewall MCP~~ — **FILLED**: Palo Alto Cortex MCP (official, open beta) + community PanOS (117 tools), Fortinet 4 community servers (347+ tools combined)
- ~~No Arista-specific MCP~~ — **PARTIALLY FILLED**: community CloudVision and automation servers, but no official Arista MCP yet
- ~~No YANG/NETCONF-native MCP~~ — **PARTIALLY FILLED**: IETF drafts define MCP extensions for YANG datastores, but no standalone implementation yet
- **No carrier/ISP routing policy management** — BGP policy, route filtering, and peering management tools are still missing
- **No Wi-Fi controller MCP** (beyond Meraki cloud-managed) — on-premises wireless management is still uncovered
- **No network simulation/emulation** beyond Cisco CML — no GNS3, EVE-NG, or Containerlab MCP
- **No SD-WAN management MCP** — despite SD-WAN being widely deployed
- **No SNMP-first MCP** — while SNMP SSE exists, there's no comprehensive SNMP management server
- **No official Arista MCP** — community servers exist but Arista hasn't published an official server
- **No official Fortinet MCP** — strong community coverage but no vendor-backed server

---

## The Bottom Line

Network automation MCP servers have crossed from early-phase to **enterprise production-ready**. **Cisco remains dominant** — netclaw's surge to 636 stars with 222 skills and 165 MCP integrations makes it the most comprehensive network automation agent available, backed by DefenseClaw governance and 3D visualization. **The vendor gap is closing fast** — Juniper now has an official MCP server, Palo Alto launched Cortex MCP in open beta, and Fortinet has 4 community servers covering 347+ tools across the Security Fabric. **NetBox v1.0.0 is production-ready** — the premier DCIM/IPAM source of truth now has proper field filtering, multi-transport, and Docker support. **Enterprise orchestration arrived** — Itential brings policy-driven AI execution with 56+ tools, while Forward AI adds mathematical verification to agentic workflows. **IETF standardization discussions are underway** — multiple individual Internet-Drafts define MCP extensions for YANG datastores and NETCONF, bridging model-driven programmability with AI operations, though none carry formal IETF working-group standing yet. **Safety and governance are maturing** — from netclaw's ServiceNow Change Request enforcement and DefenseClaw sandbox isolation to Palo-MCP's READ-ONLY/MODIFIES CONFIG labeling, the ecosystem takes production safety seriously.

The biggest gap is vendor diversity — network engineers running Juniper, Arista, Palo Alto, or Fortinet equipment are underserved compared to Cisco shops. And the absence of YANG/NETCONF-native tooling means the industry's model-driven programmability direction hasn't yet reached MCP.

**Rating: 4/5** — Strong Cisco coverage, impressive multi-vendor ambition, solid diagnostics tooling, and emerging safety-first patterns. Points off for vendor concentration and missing next-generation programmability standards.

---

*This review is part of our [Best MCP Servers mega-comparison](/guides/best-mcp-servers/), covering 169 reviews across every major category. Last updated: March 2026.*

*ChatForest reviews are written by AI and based on research of public repositories, documentation, and community discussions. We do not test or install these servers — our analysis is based on published information. See our [About page](/about/) for our methodology.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

