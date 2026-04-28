# Configuration Management MCP Servers — Ansible, NixOS, Chef, SaltStack, Consul, and More

> Configuration management MCP servers help AI agents manage infrastructure configuration, execute playbooks, query package databases, and orchestrate service discovery via the Model Context Protocol.


Configuration management MCP servers let AI assistants manage infrastructure configuration, execute automation playbooks, query package databases, and orchestrate service discovery through the Model Context Protocol. Instead of writing YAML by hand or memorizing CLI flags, AI agents can manage configuration at scale conversationally.

This review covers the **configuration management** ecosystem — Ansible automation, NixOS package and option queries, Chef migration and data access, SaltStack minion management, Consul service discovery, and multi-tool infrastructure operators. For related servers, see our [Infrastructure Automation review](/reviews/infrastructure-automation-mcp-servers/) and [Container/Docker/Kubernetes review](/reviews/container-docker-kubernetes-mcp-servers/).

The headline findings: **mcp-nixos surged 27% to 606 stars** with 5 releases in April including a FastMCP 3.x upgrade. **The Chef gap is closing** — three servers now exist, led by souschef (95 tools for multi-platform migration). **Official Ansible tooling is maturing** — AAP 2.7 specs, CI integration tests, and 50+ enterprise tools. **Puppet still has zero MCP presence**. **Configuration drift detection is emerging** as a new subcategory. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

*Updated April 28, 2026 — [what changed](#changelog)*

## Ansible

### ansible/aap-mcp-server — Official AAP MCP Service

| Server | Stars | Language | License | Components |
|--------|-------|----------|---------|------------|
| [aap-mcp-server](https://github.com/ansible/aap-mcp-server) | 24 | TypeScript | Apache-2.0 | 4 |

The **official MCP service for Ansible Automation Platform** from Red Hat:

- **Multi-service integration** — Controller, Galaxy, Gateway, and Event-Driven Ansible
- **AAP 2.7 support** — updated OpenAPI specs from AAP 2.6 to 2.7 (April 2026)
- **Auth hardening** — early auth checks for MCP POSTs against unauthenticated DoS (April 2026)
- **Role-based toolsets** — custom toolsets enable permission-based tool filtering
- **Session management** — token validation with automatic user permission detection
- **Observability** — Prometheus metrics for HTTP requests, tool execution, and system health
- **Flexible specs** — supports both local OpenAPI files and remote URLs

Requires Node.js 22+. Register via `claude mcp add aap-mcp -t http http://localhost:3000/mcp`. Production-quality with 193 commits.

### bsahane/mcp-ansible — Advanced Ansible MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-ansible](https://github.com/bsahane/mcp-ansible) | 27 | Python | — | 30+ |

**Comprehensive Ansible utilities** for playbooks, inventories, roles, and workflows:

- **Core operations** — playbook creation, validation, and execution; ad-hoc task execution; role scaffolding; Galaxy dependency installation
- **Inventory suite** — parsing with ansible.cfg awareness, group/host graph visualization, host variable resolution, connectivity testing, YAML validation, vault operations
- **Troubleshooting** — remote command execution with enhanced parsing, log fetching and pattern analysis, service management, host health diagnostics with scoring, system baseline capture and comparison
- **Advanced diagnostics** — automated problem detection, network connectivity matrix testing, security vulnerability assessments, continuous monitoring with trend analysis, performance benchmarking

Requires Python 3.10+. Configure for Cursor or Claude Desktop via MCP config files.

### sibilleb/AAP-Enterprise-MCP-Server — Enterprise Red Hat Ecosystem

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AAP-Enterprise-MCP-Server](https://github.com/sibilleb/AAP-Enterprise-MCP-Server) | 29 | Python | — | 50+ |

**The most feature-rich Ansible MCP server** — five integrated domains with 4-server architecture:

- **AAP management** (17+ tools) — inventory, host, job template, project, and SCM management; ad-hoc command execution; job monitoring
- **ansible-lint** (9 tools) — progressive quality profiles, project-wide analysis with comprehensive reporting, rule management and best practice enforcement
- **Event-Driven Ansible** (8 tools) — activation lifecycle management, rulebook handling, decision environment management
- **Ansible Galaxy** (5 tools) — collection and role discovery with AI-powered suggestions, detailed content information
- **Red Hat documentation** (8 tools) — domain-validated official sources with PDF-first strategy, semantic version sorting, intelligent recommendations

Install via UV (recommended) or pip. Requires API tokens for AAP/EDA.

### mancubus77/mcp-server-aap — Lightweight AAP Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-aap](https://github.com/mancubus77/mcp-server-aap) | 4 | Python | — | 5 |

**Minimal MCP server for AAP job template management:**

- Template discovery from AAP projects
- Job template launching with custom variables
- Job status monitoring and output retrieval
- Connection testing and authentication verification
- Retry logic with exponential backoff

Good for teams that need simple job template execution without the full enterprise feature set.

### ansible-collections/ansible.mcp — Official Ansible Collection

| Server | Stars | Language | License | Type |
|--------|-------|----------|---------|------|
| [ansible.mcp](https://github.com/ansible-collections/ansible.mcp) | 4 | Python | GPL-3.0 | Collection |

The **official Ansible Collection for MCP plugins**, installable via `ansible-galaxy collection install ansible.mcp`. Quadrupled stars since March with 24 new commits (now 112 total). **New in April:** CI integration test workflows, testing strategy documentation, tool classification for indirect node counting, and regex verb matching improvements. Gaining real traction as native Ansible integration.

### redhat-cop/ansible.mcp_builder — MCP Server Installer for EEs

| Server | Stars | Language | License | Type |
|--------|-------|----------|---------|------|
| [ansible.mcp_builder](https://github.com/redhat-cop/ansible.mcp_builder) | 1 | Shell | GPL-3.0 | Builder |

**Automates MCP server installation into Ansible Execution Environments** — roles for AWS (Cloud Control, CDK, Core, IAM), Azure, and GitHub MCP servers. Supports npm, PyPI, and compiled Go binary installation methods. Registry system with automatic manifest generation. Compatible with ansible-builder 3.x, Podman 4.x, Docker 24.x. v1.0.3 released January 2026.

## NixOS

### utensils/mcp-nixos — NixOS Knowledge Base

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-nixos](https://github.com/utensils/mcp-nixos) | 606 | Python | MIT | 2 |

**The standout server in this category** — surged 27% (476→606 stars) with 5 releases in April alone. Real-time NixOS ecosystem data that prevents AI hallucinations:

- **130K+ NixOS packages** — search and query the full package database
- **23K+ NixOS options** — system configuration reference
- **5K+ Home Manager options** — user environment configuration
- **1K+ nix-darwin settings** — macOS system configuration
- **5K+ Nixvim options** — Neovim configuration via Nix
- **600+ FlakeHub flakes** — flake discovery and exploration
- **2K+ Nix functions** — via Noogle function search
- **Documentation** — NixOS Wiki and nix.dev guides
- **Binary cache status** — check package build availability

**April 2026 releases:** v2.4.3 (LLM discoverability — intent-trigger prose, deterministic API surface), v2.4.0 (FastMCP 3.x upgrade — major framework update), v2.4.2/v2.4.1 (dotenv crash fix, flake overlay compatibility), v2.3.2 (local agent tool descriptions).

Remarkably token-efficient: **2 unified tools using ~1,030 tokens total** (consolidated from 17 original tools). Install via `uvx mcp-nixos`, pip, Nix, or Docker. Runs anywhere Python runs — no NixOS installation required. 434 commits and rapid iteration.

### natsukium/mcp-servers-nix — Nix Configuration Framework

| Server | Stars | Language | License | Modules |
|--------|-------|----------|---------|---------|
| [mcp-servers-nix](https://github.com/natsukium/mcp-servers-nix) | 244 | Nix | Apache-2.0 | 25+ |

**A Nix-based framework for configuring MCP servers** — not an MCP server itself, but a reproducible way to deploy them. Grew 13% (215→244 stars) with 58 new commits:

- **25+ pre-configured modules** — filesystem, GitHub, Notion, Playwright, Terraform, and more
- **Security-focused** — credential handling via `envFile` and `passwordCommand`
- **Integration** — Flakes, flake-parts, devenv, and Home Manager
- **Automated updates** — daily package auto-updates keep MCP server versions current

782 commits. The go-to Nix packaging framework for MCP servers.

### aloshy-ai/nix-mcp-servers — Declarative MCP Configuration

| Server | Stars | Language | License | Clients |
|--------|-------|----------|---------|---------|
| [nix-mcp-servers](https://github.com/ismail-kattakath/nix-mcp-servers) | 23 | Nix | MIT | 2 |

**Declarative MCP server configuration for Claude Desktop and Cursor** via Nix flakes. Cross-platform support for NixOS, Darwin, and Home Manager. CLI tool available via `nix run`. 145 commits.

## Chef

### kpeacocke/souschef — AI-Powered Migration Engine

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [souschef](https://github.com/kpeacocke/souschef) | 6 | TypeScript | MIT | 95 |

**The most significant new entry in this refresh** — an AI-powered MCP server for migrating from Chef (and other platforms) to Ansible:

- **Multi-platform migration** — Chef, SaltStack, Puppet, PowerShell, and Bash → Ansible
- **95 MCP tools** across six migration categories
- **Web UI + CLI** — visual interface plus CI/CD integration
- **91% test coverage** — model-agnostic, well-tested
- **v7.0.0** (March 2026) — added SaltStack, Bash, PowerShell, Puppet migration support

1,022 commits. While migration-focused rather than Chef management, it fills the Chef gap by providing a practical path forward for Chef users entering the MCP ecosystem.

### aknarts/chef-server-mcp — Read-Only Chef Server Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chef-server-mcp](https://github.com/aknarts/chef-server-mcp) | 3 | TypeScript | MIT | 16 |

**Read-only access to Chef Server data:**

- Nodes, roles, cookbooks, data bags, and environments
- Docker deployment with multi-org support
- 16 tools for querying Chef infrastructure

11 commits. Stable but not actively developed (last commit January 2025).

### trickyearlobe-chef/chef-mcp — Chef Infra Access

| Server | Stars | Language | License | Type |
|--------|-------|----------|---------|------|
| [chef-mcp](https://github.com/trickyearlobe-chef/chef-mcp) | 0 | Go | Apache-2.0 | Server |

**New (March 2026)** — read-only MCP server for Chef Infra using existing Chef Workstation credentials:

- Zero-config setup — uses your existing Chef credentials
- Go-based with cross-platform binaries (macOS/Linux/Windows, amd64/arm64)
- v0.1.1 released March 26, 2026
- Author appears to be affiliated with Chef

13 commits. Early stage but a promising sign of vendor interest.

## SaltStack

### Bearbobs/saltstack-mcp — Salt Minion Management

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [saltstack-mcp](https://github.com/Bearbobs/saltstack-mcp) | 0 | Python | MIT | 4 |

**Basic Salt API integration** for AI-assisted minion management:

- `list_all_minions` — enumerate available minions
- `ping_minions` — test connectivity
- `get_minion_info` — retrieve minion details
- `execute_salt_command` — run Salt commands on minions

Docker deployment with credential management via secrets. Minimal but functional — only 2 commits. The SaltStack ecosystem clearly needs more MCP investment.

## Consul

### kocierik/consul-mcp-server — Service Discovery & KV Store

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [consul-mcp-server](https://github.com/kocierik/consul-mcp-server) | 16 | TypeScript | MIT | 12+ |

**HashiCorp Consul integration** for service discovery and configuration:

- **Service management** — list, register, and deregister services
- **Health checks** — register, deregister, and retrieve health status
- **Key-value store** — get, list, put, and delete KV pairs
- **Session management** — list and destroy sessions
- **Events** — fire and list events
- **Prepared queries** — create and execute
- **Cluster status** — leader and peer information
- **Agent operations** — system health monitoring

Install via `npx -y consul-mcp-server` or Smithery. Supports stdio and StreamableHTTP transports. 15 commits.

## Multi-Tool

### tarnover/mcp-sysoperator — Ansible + Terraform + AWS

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-sysoperator](https://github.com/tarnover/mcp-sysoperator) | 26 | TypeScript | MIT | 15+ |

**Unified infrastructure-as-code MCP server** combining multiple tools:

- **Ansible** — playbook execution with parameter support (inventory, variables, tags, limits), inventory listing, syntax validation
- **Terraform** — init, plan, apply, destroy operations
- **AWS** — EC2, S3, VPC, and CloudFormation resource management
- **LocalStack** — local AWS testing without credentials

Active development with 37 commits. Developers note it's not recommended for production use.

### bjeans/homelab-mcp — Homelab Infrastructure

| Server | Stars | Language | License | Servers |
|--------|-------|----------|---------|---------|
| [homelab-mcp](https://github.com/bjeans/homelab-mcp) | 25 | Python | MIT | 7 |

**Seven integrated MCP servers for homelab management** — surged 39% (18→25 stars):

- Docker/Podman container monitoring
- Ollama AI model management
- Pi-hole DNS administration
- Unifi network management
- UPS monitoring
- Ping connectivity checks
- **Ansible inventory** — read-only query access to hosts, groups, and configuration

39 total tools with MCP annotations. v3.0.0 built on FastMCP framework. 190 commits.

### jade-pico/antrieb-mcp-server — Disposable VM Clusters

| Server | Stars | Language | License | Type |
|--------|-------|----------|---------|------|
| [antrieb-mcp-server](https://github.com/jade-pico/antrieb-mcp-server) | 12 | TypeScript | Apache-2.0 | Server |

**Instant disposable VM clusters for validating LLM-generated infrastructure:**

- Multi-node clusters with real Linux distros and network appliances
- Includes **Ansible control node** with collections pre-installed
- 10-minute TTL clusters for testing — spin up, validate, tear down
- Designed for AI agents to test infrastructure code before committing

97 commits. A novel approach to infrastructure testing via MCP.

### washyu/ansible-mcp-server — Ansible + Terraform (Archived)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ansible-mcp-server](https://github.com/washyu/ansible-mcp-server) | 7 | JavaScript | MIT | 58 |

**58 infrastructure management tools** spanning Ansible operations, infrastructure discovery, security capabilities, and service deployment. Includes hardware scanning, port scanning, password audits, and environment-based deployments. **Archived October 2025** — read-only but still useful as reference. The breadth of tools (58) shows what a comprehensive config management MCP server could look like.

## Configuration Drift Detection

### DriftGuard/DriftGuard — GitOps Drift Detection for Kubernetes

| Server | Stars | Language | License | Type |
|--------|-------|----------|---------|------|
| [DriftGuard](https://github.com/DriftGuard/DriftGuard) | 5 | Go/Python | MIT | MCP-integrated |

**GitOps configuration drift detection** — compares live Kubernetes cluster state against Git desired state. Uses MCP for communication between Go infrastructure components and Python AI/ML analysis. Not a standalone MCP server, but demonstrates MCP as an integration layer for drift detection workflows. 59 commits.

### kiskander/driftguard-agentic-network — Network Drift Auto-Remediation

| Server | Stars | Language | License | Type |
|--------|-------|----------|---------|------|
| [driftguard-agentic-network](https://github.com/kiskander/driftguard-agentic-network) | 4 | — | — | Agentic workflow |

**Agentic network drift detection** (March 2026) — combines n8n workflows, AI agents, and MCP servers to detect and auto-remediate network configuration drift. A proof-of-concept for autonomous configuration management using MCP.

## NixOS Fleet Management

### vespo92/mcp-nixos-ops — NixOS SSH Fleet Management

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-nixos-ops](https://github.com/vespo92/mcp-nixos-ops) | 0 | TypeScript | MIT | 9 |

**New: NixOS machine management over SSH** for fleet management:

- 9 operations with safety gates for destructive actions (apply config, rollback)
- SSH connection multiplexing and bastion host support
- ZFS pool verification
- Early stage (3 commits) but fills a gap for NixOS fleet operators

## What's Missing

The configuration management MCP ecosystem still has notable gaps, though several from March have started closing:

- **No Puppet MCP server** — despite Puppet being used by thousands of organizations for compliance-driven infrastructure management, this remains the biggest gap in the category
- **Chef coverage is migration-focused** — souschef helps you migrate *away* from Chef; chef-server-mcp and chef-mcp provide read-only access. No server manages Chef cookbooks, recipes, or compliance profiles (InSpec) via MCP for ongoing Chef operations
- **No CFEngine, mgmt, or Bcfg2 integration** — older but still-used configuration management tools are absent
- **Drift detection is emerging but immature** — DriftGuard and driftguard-agentic-network exist but are early-stage proofs of concept, not production-ready MCP servers
- **No compliance enforcement** — beyond ansible-lint, no cross-platform policy engine (like OPA for config management) exists as an MCP server
- **No configuration diffing** — no tools for comparing configuration versions or visualizing changes before apply
- **No rollback management** — no MCP server provides configuration rollback or state restoration capabilities (though mcp-nixos-ops has safety gates)
- **SaltStack is minimal** — only 4 tools and 0 stars; dormant since September 2025. souschef supports Salt-to-Ansible migration as an alternative

## The Bottom Line

**Rating: 3.5/5** *(up from 3/5 in March)* — Configuration management MCP servers are maturing. The Chef gap is narrowing with three new servers — souschef (95 tools, migration-focused), chef-server-mcp (read-only data), and chef-mcp (vendor-adjacent, Go-based). The official Ansible ecosystem is consolidating around AAP 2.7, CI-tested collections, and 50+ enterprise tools. mcp-nixos surged 27% to 606 stars with rapid iteration (5 April releases, FastMCP 3.x upgrade). Configuration drift detection is emerging as a new subcategory.

The remaining gaps: **Puppet is still completely absent** — the most significant omission in the category. SaltStack remains dormant. Chef coverage is read-only or migration-focused, not operational. Drift detection and compliance enforcement are nascent.

For Ansible and NixOS users, this category delivers genuine value today. For Chef teams, there's now at least a migration path. For Puppet shops, the wait continues.

## Changelog

**April 28, 2026 refresh:**
- mcp-nixos surged 476→606 stars (+27%), 5 releases in April, FastMCP 3.x upgrade
- AAP-Enterprise-MCP-Server 24→29 stars (+21%), now 50+ tools
- ansible-collections/ansible.mcp 1→4 stars, 88→112 commits, CI integration tests
- ansible/aap-mcp-server 22→24 stars, AAP 2.7 specs, auth hardening
- homelab-mcp 18→25 stars (+39%), v3.0.0 FastMCP migration
- natsukium/mcp-servers-nix 215→244 stars (+13%), 58 new commits
- bsahane/mcp-ansible 25→27 stars
- NEW: kpeacocke/souschef — 6 stars, 95 tools, Chef/Salt/Puppet/Bash→Ansible migration
- NEW: aknarts/chef-server-mcp — 3 stars, 16 tools, read-only Chef Server data
- NEW: trickyearlobe-chef/chef-mcp — 0 stars, Go, read-only Chef Infra (March 2026)
- NEW: jade-pico/antrieb-mcp-server — 12 stars, disposable VM clusters for infra validation
- NEW: DriftGuard/DriftGuard — 5 stars, GitOps drift detection for Kubernetes
- NEW: kiskander/driftguard-agentic-network — 4 stars, network drift auto-remediation
- NEW: vespo92/mcp-nixos-ops — 0 stars, NixOS SSH fleet management
- Rating upgraded 3→3.5/5

*This review was last refreshed on 2026-04-28 using Claude Opus 4.6 (Anthropic).*

