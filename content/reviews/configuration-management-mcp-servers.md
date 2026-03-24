---
title: "Configuration Management MCP Servers — Ansible, NixOS, SaltStack, Consul, and More"
date: 2026-03-16T23:00:00+09:00
description: "Configuration management MCP servers help AI agents manage infrastructure configuration, execute playbooks, query package databases, and orchestrate service discovery via the Model Context Protocol. We reviewed 15+ servers across 5 subcategories. Ansible: ansible/aap-mcp-server (22 stars, TypeScript, Apache-2.0 — official AAP MCP service with Controller/Galaxy/Gateway/EDA integration, role-based toolsets, Prometheus metrics), bsahane/mcp-ansible (25 stars, Python — advanced Ansible MCP with inventory/playbook/role management, troubleshooting suite, health diagnostics), sibilleb/AAP-Enterprise-MCP-Server (24 stars, Python — enterprise Red Hat ecosystem with 17+ AAP tools, 9 ansible-lint tools, 8 EDA tools, 5 Galaxy tools, 8 Red Hat docs tools), mancubus77/mcp-server-aap (3 stars, Python — lightweight AAP template launcher with job monitoring), ansible-collections/ansible.mcp (1 star, Python, GPL-3.0 — official Ansible Collection for MCP plugins), redhat-cop/ansible.mcp_builder (1 star, Shell, GPL-3.0 — MCP server installation in Execution Environments). NixOS: utensils/mcp-nixos (476 stars, Python, MIT — 130K+ packages, 23K+ options, Home Manager, nix-darwin, Nixvim, FlakeHub, Noogle, 2 unified tools), natsukium/mcp-servers-nix (215 stars, Nix, Apache-2.0 — 25 pre-configured MCP server modules with Nix framework), aloshy-ai/nix-mcp-servers (23 stars, Nix, MIT — declarative MCP server configuration for Claude/Cursor on NixOS/Darwin). SaltStack: Bearbobs/saltstack-mcp (0 stars, Python, MIT — Salt API integration with minion management and command execution). Consul: kocierik/consul-mcp-server (16 stars, TypeScript, MIT — service discovery, KV store, health checks, session management, ACL operations). Multi-tool: tarnover/mcp-sysoperator (26 stars, TypeScript, MIT — Ansible + Terraform + LocalStack + AWS in one MCP server), washyu/ansible-mcp-server (6 stars, JavaScript, MIT — Ansible + Terraform with 58 tools, archived Oct 2025), bjeans/homelab-mcp (18 stars, Python, MIT — 7 integrated MCP servers including Ansible inventory for homelabs). Gaps: no Chef/Puppet/CFEngine MCP servers, no unified multi-tool configuration management, no drift detection or compliance enforcement, no configuration version comparison, no rollback management. 15+ servers across 5 subcategories. Rating: 3/5."
og_description: "Configuration management MCP servers: utensils/mcp-nixos (476 stars — 130K+ NixOS packages, 23K+ options), mcp-sysoperator (26 stars — Ansible + Terraform unified), bsahane/mcp-ansible (25 stars — advanced playbook/inventory management), AAP-Enterprise-MCP-Server (24 stars — 47+ Red Hat ecosystem tools), ansible/aap-mcp-server (22 stars — official AAP MCP). 15+ servers reviewed. Rating: 3/5."
content_type: "Review"
card_description: "Configuration management MCP servers for AI-powered infrastructure automation, playbook execution, package queries, and service discovery across Ansible, NixOS, SaltStack, and Consul. **The NixOS knowledge base** — utensils/mcp-nixos (476 stars, Python, MIT) is the standout server in this category, providing real-time access to 130K+ NixOS packages, 23K+ system configuration options, 5K+ Home Manager options, 1K+ nix-darwin macOS settings, 5K+ Nixvim options, 600+ FlakeHub flakes, and 2K+ Nix functions via Noogle. Remarkably token-efficient with just 2 unified tools (~1,030 tokens total). Runs anywhere Python runs — no NixOS installation required. Also provides NixOS Wiki documentation, nix.dev guides, and binary cache status checking. **Official Ansible Automation Platform MCP** — ansible/aap-mcp-server (22 stars, TypeScript, Apache-2.0) is the official MCP service for Red Hat's Ansible Automation Platform. Integrates with Controller, Galaxy, Gateway, and Event-Driven Ansible via OpenAPI specifications. Features role-based access with custom toolsets, session management with automatic user permission detection, Prometheus metrics for observability, and support for both local and remote OpenAPI specs. Requires Node.js 22+. Registered via Claude CLI for HTTP transport. **Advanced Ansible operations** — bsahane/mcp-ansible (25 stars, Python) exposes comprehensive Ansible utilities: playbook creation/validation/execution, ad-hoc task execution, role scaffolding, inventory parsing with ansible.cfg awareness, group/host graph visualization, host variable resolution, connectivity testing, vault operations. Advanced troubleshooting suite includes remote command execution, log analysis, service management, host health diagnostics with scoring, system baseline comparison, automated problem detection, network connectivity matrix testing, and security vulnerability assessments. **Enterprise Red Hat ecosystem** — sibilleb/AAP-Enterprise-MCP-Server (24 stars, Python) provides 47+ tools across five domains: 17+ AAP management tools (inventory, jobs, projects, templates, hosts), 9 ansible-lint quality assurance tools (progressive quality profiles, project-wide analysis), 8 Event-Driven Ansible tools (activation lifecycle, rulebook management), 5 Galaxy discovery tools (collection/role search with AI-powered suggestions), and 8 Red Hat documentation tools (domain-validated official sources with PDF-first strategy). **Multi-tool infrastructure operator** — tarnover/mcp-sysoperator (26 stars, TypeScript, MIT) combines Ansible, Terraform, LocalStack, and AWS resource management in a single MCP server. Execute playbooks with parameter support, validate syntax, manage Terraform operations (init/plan/apply/destroy), and interact with AWS resources (EC2, S3, VPC, CloudFormation). Includes LocalStack integration for local testing without credentials. Active development, not recommended for production. **Lightweight AAP integration** — mancubus77/mcp-server-aap (3 stars, Python) is a minimal MCP server for launching Ansible job templates via the AAP API. Template discovery, job launching with custom variables, status monitoring, output retrieval, and connection testing with exponential backoff retry logic. **Ansible Collection for MCP** — ansible-collections/ansible.mcp (1 star, Python, GPL-3.0) is the official Ansible Collection providing MCP plugins, installable via ansible-galaxy. Active development with 88 commits. **MCP server installer for Execution Environments** — redhat-cop/ansible.mcp_builder (1 star, Shell, GPL-3.0) automates installation of MCP servers (AWS, Azure, GitHub) into Ansible Execution Environments via npm, PyPI, or compiled Go binaries. Registry system with automatic manifest generation. Compatible with ansible-builder 3.x. **Nix framework for MCP servers** — natsukium/mcp-servers-nix (215 stars, Nix, Apache-2.0) provides a modular Nix-based configuration framework with 25 pre-configured MCP server modules. Reproducible builds, security-focused credential handling via envFile and passwordCommand, integration with Flakes, flake-parts, devenv, and Home Manager. **Declarative MCP configuration** — aloshy-ai/nix-mcp-servers (23 stars, Nix, MIT) is a Nix flake for declaratively configuring MCP servers for Claude Desktop and Cursor. Cross-platform support for NixOS, Darwin, and Home Manager. CLI tool available via nix run. **SaltStack minion management** — Bearbobs/saltstack-mcp (0 stars, Python, MIT) provides basic Salt API integration with four tools: list_all_minions, ping_minions, get_minion_info, and execute_salt_command. Docker deployment with credential management. Minimal but functional for salt-master interaction. **Consul service discovery** — kocierik/consul-mcp-server (16 stars, TypeScript, MIT) provides access to HashiCorp Consul's functionality: service management (list/register/deregister), health checks, key-value store operations (get/list/put/delete), session management, event handling, prepared queries, cluster status (leader/peers), and agent operations. Installable via npx or Smithery. **Homelab infrastructure** — bjeans/homelab-mcp (18 stars, Python, MIT) bundles 7 MCP servers for homelab management including Ansible inventory integration. 39 total tools with MCP annotations. Docker/Podman containers, Ollama models, Pi-hole DNS, Unifi networks, UPS monitoring, and Ansible-managed host querying. v3.0.0 with FastMCP framework. **Ansible + Terraform combo** — washyu/ansible-mcp-server (6 stars, JavaScript, MIT) provided 58 infrastructure management tools spanning Ansible operations, hardware scanning, security assessments, and service deployment. Archived October 2025 — read-only but still functional as reference. **Gaps remain in several areas** — no Puppet MCP server exists despite Puppet being a major configuration management tool. No Chef Infra or Chef InSpec MCP servers. No CFEngine, mgmt, or Bcfg2 MCP integration. No unified configuration management server spanning multiple tools with drift detection. No configuration version comparison or diff tools. No automated rollback management. No compliance enforcement via MCP (distinct from ansible-lint — think cross-platform policy engines like Open Policy Agent for config management). No configuration testing or dry-run simulation tools beyond what individual servers provide. The SaltStack server is minimal with only 4 tools and 0 stars. The category earns 3/5 — Ansible dominates with six dedicated servers including an official Red Hat implementation, but the broader configuration management ecosystem is thin. NixOS stands out with the most polished and popular server (mcp-nixos at 476 stars), while Puppet, Chef, and SaltStack — tools used by thousands of organizations — have virtually no MCP presence. The Nix framework projects (mcp-servers-nix, nix-mcp-servers) serve a different purpose — managing MCP server installations rather than infrastructure configuration. Consul has basic coverage. The category would benefit significantly from official vendors (Puppet Labs, Progress Chef) creating MCP servers for their platforms."
last_refreshed: 2026-03-16
---

Configuration management MCP servers let AI assistants manage infrastructure configuration, execute automation playbooks, query package databases, and orchestrate service discovery through the Model Context Protocol. Instead of writing YAML by hand or memorizing CLI flags, AI agents can manage configuration at scale conversationally.

This review covers the **configuration management** ecosystem — Ansible automation, NixOS package and option queries, SaltStack minion management, Consul service discovery, and multi-tool infrastructure operators. For related servers, see our [Infrastructure Automation review](/reviews/infrastructure-automation-mcp-servers/) and [Container/Docker/Kubernetes review](/reviews/container-docker-kubernetes-mcp-servers/).

The headline findings: **Ansible dominates with six dedicated servers** including an official Red Hat AAP implementation. **NixOS has the most polished single server** (mcp-nixos, 476 stars) with remarkable token efficiency. **Puppet and Chef have zero MCP presence** — a significant gap given their enterprise adoption. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## Ansible

### ansible/aap-mcp-server — Official AAP MCP Service

| Server | Stars | Language | License | Components |
|--------|-------|----------|---------|------------|
| [aap-mcp-server](https://github.com/ansible/aap-mcp-server) | 22 | TypeScript | Apache-2.0 | 4 |

The **official MCP service for Ansible Automation Platform** from Red Hat:

- **Multi-service integration** — Controller, Galaxy, Gateway, and Event-Driven Ansible
- **Role-based toolsets** — custom toolsets enable permission-based tool filtering
- **Session management** — token validation with automatic user permission detection
- **Observability** — Prometheus metrics for HTTP requests, tool execution, and system health
- **Flexible specs** — supports both local OpenAPI files and remote URLs

Requires Node.js 22+. Register via `claude mcp add aap-mcp -t http http://localhost:3000/mcp`. Production-quality with 187 commits.

### bsahane/mcp-ansible — Advanced Ansible MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-ansible](https://github.com/bsahane/mcp-ansible) | 25 | Python | — | 30+ |

**Comprehensive Ansible utilities** for playbooks, inventories, roles, and workflows:

- **Core operations** — playbook creation, validation, and execution; ad-hoc task execution; role scaffolding; Galaxy dependency installation
- **Inventory suite** — parsing with ansible.cfg awareness, group/host graph visualization, host variable resolution, connectivity testing, YAML validation, vault operations
- **Troubleshooting** — remote command execution with enhanced parsing, log fetching and pattern analysis, service management, host health diagnostics with scoring, system baseline capture and comparison
- **Advanced diagnostics** — automated problem detection, network connectivity matrix testing, security vulnerability assessments, continuous monitoring with trend analysis, performance benchmarking

Requires Python 3.10+. Configure for Cursor or Claude Desktop via MCP config files.

### sibilleb/AAP-Enterprise-MCP-Server — Enterprise Red Hat Ecosystem

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AAP-Enterprise-MCP-Server](https://github.com/sibilleb/AAP-Enterprise-MCP-Server) | 24 | Python | — | 47+ |

**The most feature-rich Ansible MCP server** — five integrated domains:

- **AAP management** (17+ tools) — inventory, host, job template, project, and SCM management; ad-hoc command execution; job monitoring
- **ansible-lint** (9 tools) — progressive quality profiles, project-wide analysis with comprehensive reporting, rule management and best practice enforcement
- **Event-Driven Ansible** (8 tools) — activation lifecycle management, rulebook handling, decision environment management
- **Ansible Galaxy** (5 tools) — collection and role discovery with AI-powered suggestions, detailed content information
- **Red Hat documentation** (8 tools) — domain-validated official sources with PDF-first strategy, semantic version sorting, intelligent recommendations

Install via UV (recommended) or pip. Requires API tokens for AAP/EDA.

### mancubus77/mcp-server-aap — Lightweight AAP Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-aap](https://github.com/mancubus77/mcp-server-aap) | 3 | Python | — | 5 |

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
| [ansible.mcp](https://github.com/ansible-collections/ansible.mcp) | 1 | Python | GPL-3.0 | Collection |

The **official Ansible Collection for MCP plugins**, installable via `ansible-galaxy collection install ansible.mcp`. Active development with 88 commits. Provides MCP integration as native Ansible plugins rather than a standalone server.

### redhat-cop/ansible.mcp_builder — MCP Server Installer for EEs

| Server | Stars | Language | License | Type |
|--------|-------|----------|---------|------|
| [ansible.mcp_builder](https://github.com/redhat-cop/ansible.mcp_builder) | 1 | Shell | GPL-3.0 | Builder |

**Automates MCP server installation into Ansible Execution Environments** — roles for AWS (Cloud Control, CDK, Core, IAM), Azure, and GitHub MCP servers. Supports npm, PyPI, and compiled Go binary installation methods. Registry system with automatic manifest generation. Compatible with ansible-builder 3.x, Podman 4.x, Docker 24.x. v1.0.3 released January 2026.

## NixOS

### utensils/mcp-nixos — NixOS Knowledge Base

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-nixos](https://github.com/utensils/mcp-nixos) | 476 | Python | MIT | 2 |

**The standout server in this category** — real-time NixOS ecosystem data that prevents AI hallucinations:

- **130K+ NixOS packages** — search and query the full package database
- **23K+ NixOS options** — system configuration reference
- **5K+ Home Manager options** — user environment configuration
- **1K+ nix-darwin settings** — macOS system configuration
- **5K+ Nixvim options** — Neovim configuration via Nix
- **600+ FlakeHub flakes** — flake discovery and exploration
- **2K+ Nix functions** — via Noogle function search
- **Documentation** — NixOS Wiki and nix.dev guides
- **Binary cache status** — check package build availability

Remarkably token-efficient: **2 unified tools using ~1,030 tokens total** (consolidated from 17 original tools). Install via `uvx mcp-nixos`, pip, Nix, or Docker. Runs anywhere Python runs — no NixOS installation required. 415 commits and active maintenance.

### natsukium/mcp-servers-nix — Nix Configuration Framework

| Server | Stars | Language | License | Modules |
|--------|-------|----------|---------|---------|
| [mcp-servers-nix](https://github.com/natsukium/mcp-servers-nix) | 215 | Nix | Apache-2.0 | 25 |

**A Nix-based framework for configuring MCP servers** — not an MCP server itself, but a reproducible way to deploy them:

- **25 pre-configured modules** — filesystem, GitHub, Notion, Playwright, Terraform, and more
- **Security-focused** — credential handling via `envFile` and `passwordCommand`
- **Integration** — Flakes, flake-parts, devenv, and Home Manager
- **Modular** — consistent interface across all server configurations

724 commits. Useful for NixOS users who want declarative MCP server management.

### aloshy-ai/nix-mcp-servers — Declarative MCP Configuration

| Server | Stars | Language | License | Clients |
|--------|-------|----------|---------|---------|
| [nix-mcp-servers](https://github.com/ismail-kattakath/nix-mcp-servers) | 23 | Nix | MIT | 2 |

**Declarative MCP server configuration for Claude Desktop and Cursor** via Nix flakes. Cross-platform support for NixOS, Darwin, and Home Manager. CLI tool available via `nix run`. 145 commits.

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
| [homelab-mcp](https://github.com/bjeans/homelab-mcp) | 18 | Python | MIT | 7 |

**Seven integrated MCP servers for homelab management:**

- Docker/Podman container monitoring
- Ollama AI model management
- Pi-hole DNS administration
- Unifi network management
- UPS monitoring
- Ping connectivity checks
- **Ansible inventory** — read-only query access to hosts, groups, and configuration

39 total tools with MCP annotations. v3.0.0 built on FastMCP framework. 171 commits.

### washyu/ansible-mcp-server — Ansible + Terraform (Archived)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ansible-mcp-server](https://github.com/washyu/ansible-mcp-server) | 6 | JavaScript | MIT | 58 |

**58 infrastructure management tools** spanning Ansible operations, infrastructure discovery, security capabilities, and service deployment. Includes hardware scanning, port scanning, password audits, and environment-based deployments. **Archived October 2025** — read-only but still useful as reference. The breadth of tools (58) shows what a comprehensive config management MCP server could look like.

## What's Missing

The configuration management MCP ecosystem has significant gaps:

- **No Puppet MCP server** — despite Puppet being used by thousands of organizations for compliance-driven infrastructure management
- **No Chef Infra or InSpec MCP server** — no way to manage Chef cookbooks, recipes, or compliance profiles via MCP
- **No CFEngine, mgmt, or Bcfg2 integration** — older but still-used configuration management tools are absent
- **No drift detection** — no MCP server provides configuration drift detection or remediation across managed hosts
- **No compliance enforcement** — beyond ansible-lint, no cross-platform policy engine (like OPA for config management) exists as an MCP server
- **No configuration diffing** — no tools for comparing configuration versions or visualizing changes before apply
- **No rollback management** — no MCP server provides configuration rollback or state restoration capabilities
- **SaltStack is minimal** — only 4 tools and 0 stars; needs significantly more development

## The Bottom Line

**Rating: 3/5** — Configuration management MCP servers are an uneven category. Ansible dominates with six dedicated servers spanning official Red Hat tooling, enterprise ecosystems, and community implementations. NixOS punches above its weight with mcp-nixos (476 stars) — the most polished and popular server in the category by a wide margin. Consul has basic but functional coverage.

The glaring gaps are Puppet and Chef — two tools used across thousands of enterprise environments with zero MCP presence. SaltStack's single server is barely functional. The multi-tool servers (mcp-sysoperator, the archived ansible-mcp-server) hint at what a unified configuration management MCP could become, but none are production-ready.

For teams using Ansible, the MCP ecosystem is genuinely useful today. For everyone else, this category needs significant investment from tool vendors and the community.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
