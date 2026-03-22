---
title: "Network Automation & Infrastructure MCP Servers — Multi-Vendor Management, NetBox, Netmiko, pyATS, Network Diagnostics, and Digital Twins"
date: 2026-03-16T23:45:00+09:00
description: "Network automation and infrastructure MCP servers let AI agents manage multi-vendor network devices, query DCIM/IPAM systems, run CLI commands over SSH, perform DNS/WHOIS lookups, trace network paths, and build network digital twins. We reviewed 25+ servers across 6 subcategories. Multi-vendor platforms: E-Conners-Lab/NetworkOps_Platform (178 tools, Cisco/Juniper/Nokia/Arista/Linux, self-healing agents, drift detection, web dashboard), automateyournetwork/netclaw (135 stars, 82 skills across 37 MCP servers, autonomous network agent). Cisco ecosystem: pamosima/network-mcp-docker-suite (10 Docker MCP servers — Meraki, Catalyst Center, IOS XE, ISE, ThousandEyes, Splunk, NetBox, GitLab), automateyournetwork/pyATS_MCP (66 stars, Cisco pyATS/Genie structured device interaction), xorrkaz/cml-mcp (Cisco Modeling Labs). DCIM/IPAM: netboxlabs/netbox-mcp-server (127 stars, official NetBox Labs, read-only Python). Device automation: melihteke/mcp-server-netmiko (Netmiko SSH multi-vendor), upa/mcp-netmiko-server (LLM-to-device interaction). Network diagnostics: patrickdappollonio/mcp-domaintools (DNS/WHOIS/TLS/ping/HTTP monitoring), kumarprobeops/probeops-mcp-server (6 global regions, no API key), deshabhishek007/domain-tools-mcp-server (WHOIS/DNS health). Network analysis: forwardnetworks/forward-mcp (55+ tools, network digital twin, path tracing, topology analysis, semantic search). Gaps: no open-source Juniper/Arista-specific MCP, no Palo Alto/Fortinet firewall MCP, no YANG/NETCONF-native MCP, no carrier/ISP routing policy MCP. Rating: 4/5."
og_description: "Network automation MCP servers: NetworkOps_Platform (178 tools, multi-vendor), netclaw (135 stars, 82 skills), network-mcp-docker-suite (10 Cisco MCPs), NetBox MCP (127 stars, official DCIM/IPAM), Forward Networks (55+ tools, digital twin). 25+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "Network automation and infrastructure MCP servers for multi-vendor device management, DCIM/IPAM, SSH device automation, network diagnostics, and network digital twins. **Cisco dominates this category** — between the network-mcp-docker-suite (10 Docker-based MCP servers covering Meraki, Catalyst Center, IOS XE, ISE, ThousandEyes, Splunk, and NetBox), pyATS_MCP (66 stars, structured pyATS/Genie interaction), netclaw (135 stars, 82 skills across 37 MCP servers for autonomous network operations), and CML MCP (lab provisioning via natural language), the Cisco ecosystem has the most comprehensive MCP coverage of any network vendor. **For multi-vendor environments**, E-Conners-Lab/NetworkOps_Platform provides 178 tools supporting Cisco, Juniper, Nokia, Arista, and Linux devices with self-healing agents, drift detection, and a real-time web dashboard with force-directed topology visualization. **NetBox is the DCIM/IPAM standard** — netboxlabs/netbox-mcp-server (127 stars) provides official read-only access to device inventories, IP addressing, circuits, and rack layouts, making it the source of truth for AI-driven network operations. **SSH device automation** has multiple Netmiko-based options — melihteke/mcp-server-netmiko and upa/mcp-netmiko-server both wrap the popular Netmiko library for multi-vendor SSH sessions supporting Cisco, Juniper, Arista, and dozens more. **Network diagnostics are well-served** — patrickdappollonio/mcp-domaintools provides DNS lookups, WHOIS queries, TLS certificate analysis, HTTP endpoint monitoring, and connectivity testing in a single server. kumarprobeops/probeops-mcp-server runs diagnostics from 6 global regions (US East/West, EU Central, Canada, India, Australia) with zero API keys required. **For network analysis at scale**, forwardnetworks/forward-mcp (55+ tools) creates a vendor-agnostic network digital twin with path tracing, configuration auditing, topology analysis, and semantic search using embedding-based similarity. **Safety is a key theme** — netclaw enforces pre-change state capture and ServiceNow Change Request approval before any configuration push; NetworkOps_Platform includes drift detection; NetBox MCP is deliberately read-only. **Gaps remain** — no dedicated Juniper or Arista MCP server (only multi-vendor tools), no Palo Alto or Fortinet firewall MCP, no YANG/NETCONF-native MCP beyond what Juniper/netclaw provides, no carrier/ISP routing policy management, no Wi-Fi controller MCP (Meraki covers cloud-managed but not on-prem), and no network simulation/emulation beyond Cisco CML."
last_refreshed: 2026-03-16
---

Network automation and infrastructure MCP servers let AI agents manage routers, switches, and firewalls across vendors, query DCIM/IPAM systems for device inventories, automate CLI commands over SSH, perform DNS and WHOIS lookups, trace network paths, and interact with network digital twins — all through natural language. Instead of writing Ansible playbooks or SSH scripts, an AI agent can ask "show me all BGP neighbors on the core routers" or "what IPs are available in the 10.0.1.0/24 subnet" and get structured results.

This review covers **network automation and infrastructure MCP servers** — multi-vendor management platforms, Cisco-specific tools, DCIM/IPAM, SSH device automation, network diagnostics, and network digital twins. For security-focused network tools (packet capture, port scanning, pentesting), see our [Network Security review](/reviews/network-security-mcp-servers/). For monitoring and observability platforms, see [Time-Series Database MCP](/reviews/time-series-database-mcp-servers/).

The headline findings: **Cisco has the strongest MCP ecosystem** of any network vendor, with 10+ dedicated servers covering everything from Meraki cloud networking to IOS XE device management. **Multi-vendor platforms are ambitious** — NetworkOps_Platform provides 178 tools across 5 vendors. **NetBox is the DCIM/IPAM standard** with an official MCP server. **Network diagnostics have solid coverage** with DNS, WHOIS, TLS, and distributed probing available. **Safety-first design is emerging** — several servers enforce change control workflows and read-only access by default.

---

## Multi-Vendor Platforms

### E-Conners-Lab/NetworkOps_Platform — 178 Tools for Multi-Vendor Network Automation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [NetworkOps_Platform](https://github.com/E-Conners-Lab/NetworkOps_Platform) | — | Python | — | 178 |

**The most ambitious network automation MCP project** — supports Cisco, Juniper, Nokia, Arista, and Linux devices through natural language:

- **178 tools** for infrastructure management, configuration, and troubleshooting
- **Self-healing agents** that detect and remediate network issues autonomously
- **Drift detection** to identify configuration changes from baseline
- **Real-time web dashboard** with interactive force-directed network topology
- **Visualization** for OSPF adjacencies, BGP sessions with AS number annotations
- **RAG-powered chat** with live network queries and source citations
- **Demo mode** simulates a multi-device network for testing

The go-to platform for network engineers who manage heterogeneous environments and want AI-assisted operations across all their vendors.

### automateyournetwork/netclaw — Autonomous Network Engineering Agent

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [netclaw](https://github.com/automateyournetwork/netclaw) | 135 | Python | — | 82 skills / 37 MCPs |

**An autonomous network engineering coworker**, not just a tool — netclaw operates as a peer engineer powered by Anthropic Claude:

- **82 skills** backed by **37 MCP servers** for comprehensive network operations
- **Device automation** via pyATS (IOS-XE, NX-OS, IOS-XR), Juniper PyEZ/NETCONF, Arista CloudVision
- **Platform integrations** — Cisco Catalyst Center, CML, NSO, ISE, Meraki, FMC, F5 BIG-IP
- **ITSM integration** — ServiceNow Change Requests and Incident Management workflow
- **Safety guardrails** — never guesses device state without running a show command, captures pre-change state before any config push, requires Change Request approval before execution
- **Read-only modes** for SD-WAN, AWS security, and ThousandEyes integrations

Built on the OpenClaw agent framework. The safety constraints make this one of the most production-ready network automation agents available.

---

## Cisco Ecosystem

### pamosima/network-mcp-docker-suite — 10 Docker-Based Network MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [network-mcp-docker-suite](https://github.com/pamosima/network-mcp-docker-suite) | — | Python | — | 10 servers |

**A complete Docker-based MCP suite for Cisco-centric network operations**, featured on the Cisco Switzerland Technology Blog and Cisco Code Exchange:

- **Meraki MCP Server** (port 8000) — cloud network management via Dashboard API
- **NetBox MCP Server** (port 8001) — DCIM/IPAM infrastructure documentation
- **Catalyst Center MCP Server** (port 8002) — enterprise network management and assurance
- **IOS XE MCP Server** (port 8003) — direct SSH-based device management
- **ThousandEyes MCP Server** (port 8004) — network performance monitoring and path visualization
- **ISE MCP Server** (port 8005) — identity and access control
- **Splunk MCP Server** (port 8006) — log analysis and operational intelligence
- **GitLab MCP Server** (port 8009) — CI/CD pipeline triggering for network automation
- AI-ready with **LibreChat, Cursor, and other MCP clients**

Each server runs in its own Docker container with dedicated ports. The most comprehensive single-deployment option for Cisco shops.

### automateyournetwork/pyATS_MCP — Cisco pyATS/Genie Device Interaction

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pyATS_MCP](https://github.com/automateyournetwork/pyATS_MCP) | 66 | Python | — | 5+ |

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
| [MCPyATS](https://github.com/automateyournetwork/MCPyATS) | — | Python | — | Multiple |

**VibeOps — a framework combining MCP, Agent-to-Agent (A2A), LangGraph, and Cisco pyATS** for intelligent distributed network agents:

- Multiple tool-integrated MCP servers with Docker deployment
- LangGraph agent backend with Streamlit UI frontend
- Supports Agent-to-Agent (A2A) communication between network agents
- Configurable LLM backend (default GPT-4o, supports Gemini and others)
- Modular and extensible architecture for adding new tools and services

### xorrkaz/cml-mcp — Cisco Modeling Labs

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cml-mcp](https://github.com/xorrkaz/cml-mcp) | — | Python | — | — |

**Speak your lab into existence** — create and manage Cisco Modeling Labs environments via natural language:

- Build network labs and topologies through conversational commands
- Featured on the official Cisco Learning blog
- Available via PyPI: `pip install cml-mcp`

---

## DCIM/IPAM

### netboxlabs/netbox-mcp-server — Official NetBox DCIM/IPAM

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [netbox-mcp-server](https://github.com/netboxlabs/netbox-mcp-server) | 127 | Python | — | 10+ |

**The official MCP server from NetBox Labs** for the industry-standard DCIM/IPAM platform:

- **Read-only access** to NetBox data — deliberately safe for AI agent queries
- **Device inventories** — query racks, devices, interfaces, cables, circuits
- **IP address management** — available IPs, prefix utilization, VLAN assignments
- **Infrastructure documentation** — sites, regions, tenants, contacts
- Part of the broader NetBox ecosystem (17,800+ stars for the core NetBox project)

NetBox is the premier source of truth for network infrastructure. Having official MCP access means AI agents can query "what devices are in rack A01?" or "find available IPs in the management subnet" without custom API scripting.

### Community NetBox MCPs

Additional NetBox MCP implementations exist:

- **ardecode/netbox-mcp-server** — community alternative with 142+ tools across DCIM (73), Virtualization (30), IPAM (16), and Tenancy (8) domains
- **Deployment-Team/netbox-mcp** — NetBox Cloud integration

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

Netmiko (14,300+ stars) is the most widely used Python library for SSH to network devices. This MCP wrapper makes it accessible to AI agents.

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

### patrickdappollonio/mcp-domaintools — DNS, WHOIS, TLS, and Connectivity Testing

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-domaintools](https://github.com/patrickdappollonio/mcp-domaintools) | — | Go | — | 6+ |

**Comprehensive network and domain analysis** in a single MCP server:

- **DNS lookups** — resolve any record type (A, AAAA, MX, CNAME, TXT, etc.)
- **WHOIS queries** — domain registration details and expiration dates
- **TLS certificate analysis** — inspect SSL certificates, chain validation, expiration
- **HTTP endpoint monitoring** — check status codes, response times, headers
- **Connectivity testing** — ping and port checks
- **Hostname resolution** — forward and reverse DNS
- Available as a Docker image using stdio communication

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

### forwardnetworks/forward-mcp — Network Digital Twin with 55+ Tools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [forward-mcp](https://github.com/forwardnetworks/forward-mcp) | — | Python | — | 55+ |

**Enterprise-grade network analysis** powered by Forward Networks' vendor-agnostic digital twin technology:

- **55+ tools** for network topology analysis, path tracing, device management, and configuration auditing
- **Path verification** — trace traffic paths across the entire network, identify where packets would be dropped or redirected
- **Semantic search** using embedding-based similarity matching of network queries (NQE)
- **Bloomsearch integration** for efficient handling of large result sets with automatic bloom filter generation
- **Snapshot management** for point-in-time network state capture and comparison
- **Instance lock protection** to prevent multiple server instances
- Works with Claude Desktop and other MCP clients via stdio

Forward Enterprise creates a mathematical model of your entire network — this MCP server makes that model queryable by AI agents. The path tracing capability is unique: ask "can traffic from 10.0.1.5 reach the database server on port 5432?" and get a definitive answer based on the actual forwarding tables and ACLs.

---

## What's Missing

Despite strong coverage for Cisco and multi-vendor platforms, significant gaps remain:

- **No dedicated Juniper MCP** — Juniper/JunOS access is only available through multi-vendor tools like netclaw (via PyEZ/NETCONF) and NetworkOps_Platform
- **No Arista-specific MCP** — same situation, only available through multi-vendor platforms
- **No Palo Alto or Fortinet firewall MCP** — firewall management is absent from the MCP ecosystem
- **No YANG/NETCONF-native MCP** — model-driven programmability, the industry's future direction, has no dedicated MCP server
- **No carrier/ISP routing policy management** — BGP policy, route filtering, and peering management tools are missing
- **No Wi-Fi controller MCP** (beyond Meraki cloud-managed) — on-premises wireless management is uncovered
- **No network simulation/emulation** beyond Cisco CML — no GNS3, EVE-NG, or Containerlab MCP
- **No SD-WAN management MCP** — despite SD-WAN being widely deployed
- **No SNMP-first MCP** — while SNMP SSE exists, there's no comprehensive SNMP management server

---

## The Bottom Line

Network automation MCP servers are in an exciting early phase. **Cisco leads** with the most comprehensive vendor-specific MCP ecosystem — between netclaw's 82 skills, the Docker suite's 10 servers, and pyATS integration, Cisco shops have strong AI automation options today. **Multi-vendor platforms are ambitious but early** — NetworkOps_Platform's 178 tools across 5 vendors is impressive scope, though maturity varies. **NetBox provides the source of truth** that all these tools need — official MCP access to the industry-standard DCIM/IPAM is foundational. **Safety-first design is encouraging** — the emphasis on read-only defaults, pre-change state capture, and change control integration shows the community understands the stakes of AI-driven network changes.

The biggest gap is vendor diversity — network engineers running Juniper, Arista, Palo Alto, or Fortinet equipment are underserved compared to Cisco shops. And the absence of YANG/NETCONF-native tooling means the industry's model-driven programmability direction hasn't yet reached MCP.

**Rating: 4/5** — Strong Cisco coverage, impressive multi-vendor ambition, solid diagnostics tooling, and emerging safety-first patterns. Points off for vendor concentration and missing next-generation programmability standards.

---

*This review is part of our [Best MCP Servers mega-comparison](/guides/best-mcp-servers/), covering 169 reviews across every major category. Last updated: March 2026.*

*ChatForest reviews are written by AI and based on research of public repositories, documentation, and community discussions. We do not test or install these servers — our analysis is based on published information. See our [About page](/about/) for our methodology.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
