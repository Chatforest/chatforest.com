# Configuration Management MCP Servers — Ansible, NixOS, SaltStack, Consul, and More

> Configuration management MCP servers help AI agents manage infrastructure configuration, execute playbooks, query package databases, and orchestrate service discovery via the Model Context Protocol.


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

