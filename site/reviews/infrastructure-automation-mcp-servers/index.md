# Infrastructure Automation MCP Servers — Ansible, Terraform, Pulumi, OpenTofu, and Beyond

> Infrastructure automation MCP servers let AI agents manage IaC workflows across Ansible, Terraform, Pulumi, OpenTofu, and Crossplane. We reviewed 20+ servers across 6 platforms.


Infrastructure as Code changed how teams manage cloud resources — **Terraform configurations, Ansible playbooks, Pulumi programs, OpenTofu modules**. Infrastructure automation MCP servers let AI agents interact with these tools directly: looking up provider documentation, executing plans, managing workspaces, running playbooks, and even delegating multi-step provisioning to autonomous agents.

The headline finding: **IaC MCP is rapidly expanding beyond documentation into execution and governance**. HashiCorp's Terraform MCP server (1,300 stars) crossed a major threshold with v0.5.0 — adding plan/apply tools alongside its registry intelligence, plus Stacks support and policy set management. Pulumi surged to 188 stars (+224%) with Neo delegation for autonomous provisioning. Three previously missing gaps are now filled: **env0 launched an official MCP server**, **Infracost has a community cost estimation MCP**, and **Upbound shipped a Crossplane marketplace MCP server** with 9 tools. Red Hat deepened its Ansible MCP ecosystem with the ansible.mcp collection enabling playbooks to discover and call MCP servers. The remaining gap is configuration management — Chef (EOL November 2026), Puppet/OpenVox, and Salt still have zero MCP presence. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## The Landscape

### Terraform / HCP Terraform

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server) | ~1,300 | Go | 40+ | stdio, StreamableHTTP |
| [severity1/terraform-cloud-mcp](https://github.com/severity1/terraform-cloud-mcp) | ~23 | Python | 60+ | stdio |
| [nwiizo/tfmcp](https://github.com/nwiizo/tfmcp) | ~363 | Rust | 31 | stdio |
| [CodeSSRockMan/terraform-plan-mcp-server](https://github.com/CodeSSRockMan/terraform-plan-mcp-server) | — | — | ~6 | stdio |

**HashiCorp's official terraform-mcp-server is the ecosystem leader.** 1,300 stars, 146 forks, 343 commits. Now at **v0.5.1** (April 2026), the server has crossed a significant architectural threshold — **it now includes plan and apply tools alongside its registry intelligence**. This is a major shift from the original documentation-only philosophy.

v0.4.0 (January 2026) added **Terraform Stacks support** (`list_stacks`, `get_stack_details`), policy set management (`attach_policy_set_to_workspaces`), `get_token_permissions`, and granular `--toolsets`/`--tools` flags for selective capability enablement. v0.5.0 (April 2026) added **five plan/apply tools** for structured JSON plan output and execution logs, bearer token authorization, heartbeat interval configuration for load-balanced environments, and **OpenTelemetry instrumentation** for tool usage metrics. v0.5.1 fixed TLS flag propagation for air-gapped environments.

40+ tools now organized into toolsets:

| Toolset | Key Tools |
|---------|-----------|
| Registry | `search_providers`, `get_provider_details`, `search_modules`, `get_module_details`, `search_policies` |
| Registry-Private | Private registry access for enterprise providers/modules |
| Terraform | Workspace management, variables, runs, **plan/apply operations**, **Stacks**, **policy sets**, token permissions |

Install: `go install github.com/hashicorp/terraform-mcp-server/cmd/terraform-mcp-server@latest` or Docker `hashicorp/terraform-mcp-server:0.5.1`. Dual transport: stdio for local dev, StreamableHTTP at `localhost:8080/mcp` for remote setups. Tool filtering via `--toolsets` (registry, registry-private, terraform) and `--tools` flags.

**severity1/terraform-cloud-mcp** (23 stars, 80 commits, Python, v0.8.20) fills the gap HashiCorp deliberately left: **full Terraform Cloud API coverage**. 60+ tools spanning workspaces, runs, plans, applies, projects, organizations, state versions, variable sets, cost estimation, and assessment results. Features `safe_delete_workspace()` with explicit `ENABLE_DELETE_TOOLS=true` guard for destructive operations and audit-safe response filtering. If you manage HCP Terraform at scale, this is the operational complement to HashiCorp's server.

**nwiizo/tfmcp** (363 stars, 58 commits, Rust, MIT, v0.1.9) takes the opposite philosophy: **full execution**. Init, plan, apply, destroy, state management, workspace operations, import, taint/untaint, formatting, and dependency graphing. Plus security scanning with secret detection, risk-scored plan analysis, drift detection, and module health metrics. 31 tools in a single Rust binary. Now available via **Homebrew** (`brew install tfmcp`). Migrated to Rust Edition 2024 (requires Rust 1.85.0+). This is the "give my AI agent full Terraform CLI access" option — powerful but risky in production.

**CodeSSRockMan/terraform-plan-mcp-server** adds plan analysis with Webex Teams integration for automated workflow notifications. Niche but useful for CI/CD pipeline integration.

[Full Terraform MCP review →](/reviews/terraform-mcp-server/)

### Ansible

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| Red Hat AAP MCP (official) | — | — | 20+ | stdio |
| [Ansible Development Tools MCP](https://docs.ansible.com/projects/vscode-ansible/mcp/) | — | Python | 10+ | stdio |
| [ansible-collections/ansible.mcp](https://github.com/ansible-collections/ansible.mcp) | ~4 | Python | MCP plugins | stdio |
| [bsahane/mcp-ansible](https://github.com/bsahane/mcp-ansible) | ~26 | Python | 35+ | stdio |
| [sibilleb/AAP-Enterprise-MCP-Server](https://github.com/sibilleb/AAP-Enterprise-MCP-Server) | ~28 | Python | 50+ | stdio |
| [tarnover/mcp-sysoperator](https://github.com/tarnover/mcp-sysoperator) | ~26 | TypeScript | 15+ | stdio |

**Ansible has the broadest MCP server ecosystem of any IaC tool** — six distinct options spanning official, semi-official, and community implementations. Red Hat has also expanded the ecosystem with the **ansible.mcp collection** enabling playbooks to dynamically discover and call MCP servers.

**Red Hat's official AAP MCP server** ships as a technology preview in Ansible Automation Platform 2.6.4, installed as part of the standard AAP installation process. Two modes: read-only for safe querying and monitoring, or read-write for AI agents to execute jobs and implement changes. Covers job management, inventory management, and security compliance. Available as a container image at `ansible-automation-platform-26/mcp-tools-rhel9`. Telemetry data is automatically collected for AAP MCP deployments on January 2026+ patch releases.

**Ansible Development Tools MCP** (tech preview, documented March 2026) is a separate offering focused on development workflows rather than platform operations. Provides access to the Zen of Ansible design philosophy, best practices, virtual environment management, project scaffolding (playbooks, collections), Ansible Lint with auto-fixing, Execution Environment Builder, and Ansible Navigator for playbook execution. Requires Python 3.11+ and Node.js 18+. Communicates via JSON-RPC 2.0 over stdio.

**ansible-collections/ansible.mcp** (4 stars, 112 commits, GPL-3.0, created September 2025) is the official **Ansible MCP Collection** — not an MCP server itself, but Ansible plugins that let playbooks interact with MCP servers. Playbooks can dynamically discover available MCP servers, retrieve tool lists, and execute tools from within automation workflows. This is the complement to mcp_builder: where mcp_builder installs MCP servers into Execution Environments, ansible.mcp lets playbooks consume them.

**bsahane/mcp-ansible** (26 stars, Python) is the most feature-rich community server. 35+ tools across playbook execution, inventory management (parse, graph, diff, find-host), project management, vault operations (encrypt, decrypt, view, rekey), troubleshooting (remote commands, log fetching, service management), diagnostics (health monitoring, performance baselines, state comparison), and advanced analysis (network matrix, security audit, auto-heal). The "Swiss Army knife" for Ansible operations.

**sibilleb/AAP-Enterprise-MCP-Server** (28 stars, 10 commits, Python) targets enterprise AAP + EDA environments. 50+ tools covering AAP inventory/host/job/project management, Ansible Galaxy search and recommendations, Event-Driven Ansible (activation management, rulebook querying, event monitoring), Ansible Lint quality tools, and Red Hat documentation access with secure domain validation. This is the enterprise-grade community option.

**tarnover/mcp-sysoperator** (26 stars, 37 commits, TypeScript, MIT) combines Ansible with Terraform and LocalStack in a single server. Ansible tools for playbook execution, inventory management, and vault operations. Terraform tools for init/plan/apply/destroy. AWS tools for EC2/S3/VPC/CloudFormation. LocalStack integration for testing without real AWS credentials. Still in active development with a disclaimer against production use.

**Red Hat also provides [ansible.mcp_builder](https://github.com/redhat-cop/ansible.mcp_builder)** (1 star, 77 commits, v1.0.3 January 2026) — an Ansible Collection that installs MCP servers into Execution Environments (EEs) from npm, PyPI, or compiled Go binaries, with a unified registry system and auto-generated manifest files.

### Pulumi

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [pulumi/mcp-server](https://github.com/pulumi/mcp-server) | ~188 | TypeScript | 15+ | stdio, HTTP |
| Remote hosted | — | — | 15+ | HTTP (OAuth) |

**Pulumi pushes infrastructure MCP further than any other vendor** with autonomous infrastructure provisioning via Neo delegation. **Stars surged from 58 to 188 (+224%)** since our last review — the fastest growth rate in this category.

The server operates in two modes:

**Local Mode (npm/Docker)** — registry lookups, CLI preview/up, stack outputs. The `pulumi-cli-preview` and `pulumi-cli-up` tools give AI agents direct infrastructure execution capability. Install via `npx -y @pulumi/mcp-server`.

**Remote Mode (mcp.ai.pulumi.com/mcp)** — adds Pulumi Cloud features: `get-stacks` (list stacks), `resource-search` (Lucene query across all cloud resources in your organization), `get-policy-violations` (compliance checking), `get-users` (org members), and the `deploy-to-aws` quickstart tool. OAuth authentication.

The standout feature is **Neo delegation**: `neo-bridge` launches Pulumi Neo — an autonomous AI agent that handles multi-step infrastructure tasks end to end. `neo-get-tasks` monitors progress, `neo-continue-task` resumes conversations. Neo now executes filesystem edit tools locally, matching the schema of upstream MCP Claude Code tools. This is infrastructure delegation, not just tool calling.

188 stars, Apache-2.0. Available on AWS Marketplace. One-click install for Cursor, Claude Code CLI integration (`claude mcp add`), Claude Desktop, Windsurf, and Kiro.

[Full Pulumi MCP review →](/reviews/pulumi-mcp-server/)

### OpenTofu

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [opentofu/opentofu-mcp-server](https://github.com/opentofu/opentofu-mcp-server) | ~89 | TypeScript | 5 | stdio, HTTP |

**OpenTofu's official MCP server** (89 stars, 33 commits) mirrors Terraform's documentation-focused philosophy — registry access only, no execution.

5 tools:

| Tool | What it does |
|------|-------------|
| `search-opentofu-registry` | Search for providers, modules, resources, data sources |
| `get-provider-details` | Comprehensive provider documentation |
| `get-module-details` | Detailed module specifications |
| `get-resource-docs` | Resource-specific documentation |
| `get-datasource-docs` | Data source documentation |

v1.0.0, MPL-2.0 licensed. Available as a hosted service at `mcp.opentofu.org` or locally via `npx @opentofu/opentofu-mcp-server`. Cloudflare Worker deployment option for self-hosted remote.

Functionally similar to Terraform's registry tools but for the OpenTofu ecosystem. If you've migrated from Terraform to OpenTofu, this is the direct replacement — though it lacks workspace management, policy tools, and the broader toolset coverage of HashiCorp's server.

### Crossplane / Upbound

| Server | Stars | Language | Tools | Status |
|--------|-------|----------|-------|--------|
| [upbound/marketplace-mcp-server](https://github.com/upbound/marketplace-mcp-server) | ~6 | Go | 9 | Active |
| [vfarcic/crossplane-mcp](https://github.com/vfarcic/crossplane-mcp) | ~1 | Go | 1 | MVP |
| [cychiang/crossplane-mcp-server](https://github.com/cychiang/crossplane-mcp-server) | ~1 | Python | 4+ | Archived |

**Crossplane's MCP presence improved significantly with Upbound's marketplace server.**

**upbound/marketplace-mcp-server** (6 stars, 43 commits, Go) is the **first official Crossplane-ecosystem MCP server** from Upbound, the company behind UXP 2.0 (AI-native Crossplane distro). 9 tools for searching, discovering, and managing packages in the Upbound Marketplace: `search_packages`, `get_package_metadata`, `get_package_assets`, `get_repositories`, `reload_auth`, `get_package_version_resources`, `get_package_version_composition_resources`, `get_package_version_groupkind_resources`, `get_package_version_examples`. Supports HTTP and stdio transport. Requires UP CLI authentication.

vfarcic/crossplane-mcp provides a single `ListClaimsBasic` tool to list Claim names and namespaces for a configured API group. MVP only — plans for service creation, observation, and deletion exist but aren't implemented yet.

cychiang/crossplane-mcp-server was a Python implementation for querying Crossplane resources (XRDs, Compositions, ManagedResources) but the repository is **archived as of September 2025**.

The [Kubernetes MCP server](/reviews/kubernetes-mcp-server/) can also interact with Crossplane resources via standard kubectl operations.

### Terraform Cloud Alternatives

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [env0/mcp-server](https://github.com/env0/mcp-server) | ~4 | TypeScript | 10+ | stdio |

**env0 launched an official MCP server** (4 stars, 46 commits, TypeScript) — the **first Terraform Cloud alternative with MCP support**. Connects AI agents to env0's platform for environment deployment, cancellation, and log retrieval, plus **Cloud Compass** integration for retrieving cloud resource configurations with advanced filtering. Can generate Terraform/OpenTofu code from existing cloud resources. Compatible with Cursor, Claude Code, VS Code, Windsurf, Cline, Zed, JetBrains, and others. env0's platform also includes Cloud Analyst (AI-powered infrastructure insights via natural language) and Code Optimizer (beta, IaC security/config scanning with actionable Git fixes).

Spacelift and Scalr still have no MCP presence.

### Cost Estimation

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [phildougherty/infracost_mcp](https://github.com/phildougherty/infracost_mcp) | ~2 | TypeScript | 16 | stdio |

**phildougherty/infracost_mcp** (2 stars, 10 commits, MIT) is the **first Infracost MCP server** — filling a gap we flagged in the previous version of this review. 16 tools: cost breakdown generation (JSON, HTML, table, diff formats), configuration comparison (`diff`), Infracost Cloud upload for centralized tracking, PR commenting (GitHub, GitLab, Azure Repos, Bitbucket), tagging policy management (create/list/get/update/delete with ANY/LIST/REGEX validation), cost guardrail management (thresholds that block PRs), and usage YAML templates (small/medium/large). Early-stage but functional.

### Multi-Tool / Cross-Platform

| Server | Stars | Language | Coverage |
|--------|-------|----------|----------|
| [tarnover/mcp-sysoperator](https://github.com/tarnover/mcp-sysoperator) | ~26 | TypeScript | Ansible + Terraform + AWS |

MCP-sysoperator (covered under Ansible above) is the only server attempting cross-platform IaC coverage. Combining Ansible playbook execution with Terraform plan/apply and LocalStack testing in a single MCP server is genuinely useful for teams using both tools — though 26 stars suggests limited adoption.

## What's Missing

- **No Chef, Puppet/OpenVox, or SaltStack MCP servers** — Chef Infra Server hits end-of-life November 2026, Puppet's community forked to OpenVox after Perforce restricted binary access, and SaltStack remains quiet. Zero MCP presence across all three, reflecting the industry's accelerating shift toward IaC and immutable infrastructure
- **No CDK MCP server** — AWS CDK has no dedicated MCP server (the [AWS MCP collection](/reviews/aws-mcp-servers/) covers CDK through broader AWS tooling)
- **No cross-IaC registry** — no single server queries Terraform Registry, Pulumi Registry, and OpenTofu Registry simultaneously
- **No Spacelift or Scalr MCP servers** — only env0 among Terraform Cloud alternatives has shipped MCP support
- **No drift detection MCP** — no server specifically monitors for infrastructure drift across providers (tfmcp's `analyze_state` comes closest)
- ~~No cost estimation MCP~~ — **gap filled**: phildougherty/infracost_mcp now provides 16 tools for Terraform cost estimation, though still early-stage (2 stars)
- ~~No Crossplane official server~~ — **gap filled**: upbound/marketplace-mcp-server provides 9 tools for Crossplane package discovery
- ~~No env0 MCP server~~ — **gap filled**: env0 shipped an official MCP server with Cloud Compass integration

## The Bottom Line

**Rating: 4.0 / 5** — The category is maturing rapidly. HashiCorp's Terraform MCP server (1,300 stars, v0.5.1) crossed the execution threshold with plan/apply tools, Stacks support, and policy management — it's no longer just registry intelligence. Pulumi surged to 188 stars (+224%) with Neo delegation for autonomous provisioning. Red Hat deepened the Ansible ecosystem with the ansible.mcp collection for playbook-level MCP integration. Three previously flagged gaps are now filled: env0 shipped an official MCP server, Infracost has community cost estimation, and Upbound launched a Crossplane marketplace server. The category still loses points for the configuration management gap (Chef EOL November 2026, no Puppet/OpenVox or SaltStack MCP servers) and limited cross-platform tooling.

**Best for Terraform teams:** [hashicorp/terraform-mcp-server](/reviews/terraform-mcp-server/) for registry intelligence + plan/apply (v0.5.1), paired with severity1/terraform-cloud-mcp for full TFC API coverage or nwiizo/tfmcp for direct CLI access.

**Best for Ansible teams:** Red Hat's official AAP MCP server if you run AAP 2.6.4+. Otherwise, sibilleb/AAP-Enterprise-MCP-Server (50+ tools) for enterprise environments or bsahane/mcp-ansible (35+ tools) for standalone Ansible.

**Best for Pulumi teams:** [pulumi/mcp-server](/reviews/pulumi-mcp-server/) — the remote hosted mode with Neo delegation is unique in the IaC space.

**Best for cost management:** phildougherty/infracost_mcp for Terraform cost estimation — early-stage but fills a critical gap.

---

*This review covers publicly available information as of April 2026. ChatForest researches MCP servers thoroughly through documentation, GitHub repositories, and community discussions — we do not test servers hands-on. Star counts are approximate and change over time. Always check the linked repositories for the latest status.*

*This review was last edited on 2026-04-25 using Claude Opus 4.6 (Anthropic).*

