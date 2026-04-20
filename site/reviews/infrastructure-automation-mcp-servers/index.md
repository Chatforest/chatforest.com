# Infrastructure Automation MCP Servers — Ansible, Terraform, Pulumi, OpenTofu, and Beyond

> Infrastructure automation MCP servers let AI agents manage IaC workflows across Ansible, Terraform, Pulumi, OpenTofu, and Crossplane. We reviewed 20+ servers across 6 platforms.


Infrastructure as Code changed how teams manage cloud resources — **Terraform configurations, Ansible playbooks, Pulumi programs, OpenTofu modules**. Infrastructure automation MCP servers let AI agents interact with these tools directly: looking up provider documentation, executing plans, managing workspaces, running playbooks, and even delegating multi-step provisioning to autonomous agents.

The headline finding: **IaC MCP coverage is surprisingly mature for its age**. Every major IaC platform except Chef, Puppet, and SaltStack has at least one MCP server. HashiCorp leads with an official Terraform MCP server (1,300 stars) that deliberately focuses on registry intelligence. Red Hat ships Ansible MCP as a technology preview in AAP 2.6.4. Pulumi pushes the boundary furthest with autonomous infrastructure via Neo delegation. The gap is in the configuration management space — Chef, Puppet, and Salt have zero MCP presence. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## The Landscape

### Terraform / HCP Terraform

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server) | ~1,300 | Go | 35+ | stdio, StreamableHTTP |
| [severity1/terraform-cloud-mcp](https://github.com/severity1/terraform-cloud-mcp) | ~23 | Python | 60+ | stdio |
| [nwiizo/tfmcp](https://github.com/nwiizo/tfmcp) | ~357 | Rust | 30+ | stdio |
| [CodeSSRockMan/terraform-plan-mcp-server](https://github.com/CodeSSRockMan/terraform-plan-mcp-server) | — | — | ~6 | stdio |

**HashiCorp's official terraform-mcp-server is the ecosystem leader.** 1,300 stars, 134 forks, 323 commits, 10 releases since May 2025. It makes a deliberate architectural choice: **it provides registry intelligence, not execution**. No `terraform apply`, no `terraform plan`. Instead, it gives AI agents accurate, real-time provider documentation, module specifications, and Sentinel policies so they generate correct Terraform configurations instead of hallucinating resource arguments.

35+ tools organized into toolsets:

| Toolset | Key Tools |
|---------|-----------|
| Registry | `search_providers`, `get_provider_details`, `search_modules`, `get_module_details`, `search_policies` |
| Registry-Private | Private registry access for enterprise providers/modules |
| Terraform | HCP workspace management — create/update/delete workspaces, variables, run management |

Install: `go install github.com/hashicorp/terraform-mcp-server/cmd/terraform-mcp-server@latest` or Docker `hashicorp/terraform-mcp-server:0.4.0`. Dual transport: stdio for local dev, StreamableHTTP at `localhost:8080/mcp` for remote setups. Tool filtering via `--toolsets` and `--tools` flags.

**severity1/terraform-cloud-mcp** (23 stars, Python) fills the gap HashiCorp deliberately left: **full Terraform Cloud API coverage**. 60+ tools spanning workspaces, runs, plans, applies, projects, organizations, state versions, variable sets, cost estimation, and assessment results. Features `safe_delete_workspace()` with explicit `ENABLE_DELETE_TOOLS=true` guard for destructive operations. If you manage HCP Terraform at scale, this is the operational complement to HashiCorp's documentation-focused server.

**nwiizo/tfmcp** (357 stars, Rust, MIT) takes the opposite philosophy from HashiCorp: **full execution**. Init, plan, apply, destroy, state management, workspace operations, import, taint/untaint, formatting, and dependency graphing. Plus security scanning with secret detection, risk-scored plan analysis, and module health metrics. 30+ tools in a single Rust binary. This is the "give my AI agent full Terraform CLI access" option — powerful but risky in production.

**CodeSSRockMan/terraform-plan-mcp-server** adds plan analysis with Webex Teams integration for automated workflow notifications. Niche but useful for CI/CD pipeline integration.

[Full Terraform MCP review →](/reviews/terraform-mcp-server/)

### Ansible

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| Red Hat AAP MCP (official) | — | — | 20+ | stdio |
| [Ansible Development Tools MCP](https://docs.ansible.com/projects/vscode-ansible/mcp/) | — | Python | 10+ | stdio |
| [bsahane/mcp-ansible](https://github.com/bsahane/mcp-ansible) | ~25 | Python | 35+ | stdio |
| [sibilleb/AAP-Enterprise-MCP-Server](https://github.com/sibilleb/AAP-Enterprise-MCP-Server) | ~24 | Python | 50+ | stdio |
| [tarnover/mcp-sysoperator](https://github.com/tarnover/mcp-sysoperator) | ~26 | TypeScript | 15+ | stdio |

**Ansible has the broadest MCP server ecosystem of any IaC tool** — five distinct options spanning official, semi-official, and community implementations.

**Red Hat's official AAP MCP server** ships as a technology preview in Ansible Automation Platform 2.6.4, installed as part of the standard AAP installation process. Two modes: read-only for safe querying and monitoring, or read-write for AI agents to execute jobs and implement changes. Covers job management, inventory management, and security compliance. Available as a container image at `ansible-automation-platform-26/mcp-tools-rhel9`.

**Ansible Development Tools MCP** (tech preview, documented March 2026) is a separate offering focused on development workflows rather than platform operations. Provides access to the Zen of Ansible design philosophy, best practices, virtual environment management, project scaffolding (playbooks, collections), Ansible Lint with auto-fixing, Execution Environment Builder, and Ansible Navigator for playbook execution. Requires Python 3.11+ and Node.js 18+. Communicates via JSON-RPC 2.0 over stdio.

**bsahane/mcp-ansible** (25 stars, Python) is the most feature-rich community server. 35+ tools across playbook execution, inventory management (parse, graph, diff, find-host), project management, vault operations (encrypt, decrypt, view, rekey), troubleshooting (remote commands, log fetching, service management), diagnostics (health monitoring, performance baselines, state comparison), and advanced analysis (network matrix, security audit, auto-heal). The "Swiss Army knife" for Ansible operations.

**sibilleb/AAP-Enterprise-MCP-Server** (24 stars, Python) targets enterprise AAP + EDA environments. 50+ tools covering AAP inventory/host/job/project management, Ansible Galaxy search and recommendations, Event-Driven Ansible (activation management, rulebook querying, event monitoring), Ansible Lint quality tools, and Red Hat documentation access with secure domain validation. This is the enterprise-grade community option.

**tarnover/mcp-sysoperator** (26 stars, TypeScript, MIT) combines Ansible with Terraform and LocalStack in a single server. Ansible tools for playbook execution, inventory management, and vault operations. Terraform tools for init/plan/apply/destroy. AWS tools for EC2/S3/VPC/CloudFormation. LocalStack integration for testing without real AWS credentials. Previously known as "mcp-ansible" — it expanded beyond Ansible.

**Red Hat also provides [ansible.mcp_builder](https://github.com/redhat-cop/ansible.mcp_builder)** — an Ansible Collection that installs MCP servers into Execution Environments (EEs), making it possible to package any MCP server alongside Ansible automation.

### Pulumi

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [pulumi/mcp-server](https://github.com/pulumi/mcp-server) | ~58 | TypeScript | 15+ | stdio, HTTP |
| Remote hosted | — | — | 15+ | HTTP (OAuth) |

**Pulumi pushes infrastructure MCP further than any other vendor** with autonomous infrastructure provisioning via Neo delegation.

The server operates in two modes:

**Local Mode (npm/Docker)** — registry lookups, CLI preview/up, stack outputs. The `pulumi-cli-preview` and `pulumi-cli-up` tools give AI agents direct infrastructure execution capability.

**Remote Mode (mcp.ai.pulumi.com/mcp)** — adds Pulumi Cloud features: `get-stacks` (list stacks), `resource-search` (Lucene query across all cloud resources in your organization), `get-policy-violations` (compliance checking), `get-users` (org members), and the `deploy-to-aws` quickstart tool. OAuth authentication.

The standout feature is **Neo delegation**: `neo-bridge` launches Pulumi Neo — an autonomous AI agent that handles multi-step infrastructure tasks end to end. `neo-get-tasks` monitors progress, `neo-continue-task` resumes conversations. This is infrastructure delegation, not just tool calling.

58 stars, Apache-2.0, 10 forks. Available on AWS Marketplace. One-click install for Cursor, Claude Code CLI integration (`claude mcp add`), Claude Desktop, Windsurf, and Kiro.

[Full Pulumi MCP review →](/reviews/pulumi-mcp-server/)

### OpenTofu

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [opentofu/opentofu-mcp-server](https://github.com/opentofu/opentofu-mcp-server) | ~77 | TypeScript | 5 | stdio, HTTP |

**OpenTofu's official MCP server** mirrors Terraform's documentation-focused philosophy — registry access only, no execution.

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

### Crossplane

| Server | Stars | Language | Tools | Status |
|--------|-------|----------|-------|--------|
| [vfarcic/crossplane-mcp](https://github.com/vfarcic/crossplane-mcp) | ~1 | Go | 1 | MVP |
| [cychiang/crossplane-mcp-server](https://github.com/cychiang/crossplane-mcp-server) | ~1 | Python | 4+ | Archived |

**Crossplane's MCP presence is minimal.** Two community servers, both very early stage.

vfarcic/crossplane-mcp provides a single `ListClaimsBasic` tool to list Claim names and namespaces for a configured API group. MVP only — plans for service creation, observation, and deletion exist but aren't implemented yet.

cychiang/crossplane-mcp-server was a Python implementation for querying Crossplane resources (XRDs, Compositions, ManagedResources) but the repository is **archived as of September 2025**. Tools planned but incomplete.

No official Crossplane MCP server exists from Upbound or the Crossplane project. Given Crossplane's Kubernetes-native approach, the [Kubernetes MCP server](/reviews/kubernetes-mcp-server/) can interact with Crossplane resources via standard kubectl operations.

### Multi-Tool / Cross-Platform

| Server | Stars | Language | Coverage |
|--------|-------|----------|----------|
| [tarnover/mcp-sysoperator](https://github.com/tarnover/mcp-sysoperator) | ~26 | TypeScript | Ansible + Terraform + AWS |

MCP-sysoperator (covered under Ansible above) is the only server attempting cross-platform IaC coverage. Combining Ansible playbook execution with Terraform plan/apply and LocalStack testing in a single MCP server is genuinely useful for teams using both tools — though 26 stars suggests limited adoption.

## What's Missing

- **No Chef, Puppet, or SaltStack MCP servers** — the traditional configuration management triumvirate has zero MCP presence, despite still being widely deployed in enterprise environments
- **No CDK MCP server** — AWS CDK has no dedicated MCP server (the [AWS MCP collection](/reviews/aws-mcp-servers/) covers CDK through broader AWS tooling)
- **No Crossplane official server** — Upbound/Crossplane project hasn't released an MCP server
- **No cross-IaC registry** — no single server queries Terraform Registry, Pulumi Registry, and OpenTofu Registry simultaneously
- **No drift detection MCP** — no server specifically monitors for infrastructure drift across providers (tfmcp's `analyze_state` comes closest)
- **No cost estimation MCP** — real-time cost projection for Terraform plans (Infracost) has no MCP server
- **No Spacelift, env0, or Scalr MCP servers** — the Terraform Cloud alternatives have no MCP presence
- **Configuration management gap** — the entire CM space (Chef/Puppet/Salt) is unserved, reflecting the industry's shift toward IaC and immutable infrastructure

## The Bottom Line

**Rating: 4.0 / 5** — Strong official support from the three major IaC vendors (HashiCorp, Red Hat, Pulumi). Terraform's MCP server (1,300 stars) is the most mature, with a thoughtful registry-first design and growing workspace management. Red Hat's Ansible MCP tech preview brings enterprise automation to agents. Pulumi pushes the boundary with Neo delegation for autonomous provisioning. OpenTofu provides a solid fork-compatible alternative. The category loses points for the complete absence of Chef/Puppet/SaltStack servers, Crossplane's MVP-only status, and the lack of cross-platform tooling.

**Best for Terraform teams:** [hashicorp/terraform-mcp-server](/reviews/terraform-mcp-server/) for documentation accuracy, paired with severity1/terraform-cloud-mcp for workspace operations or nwiizo/tfmcp for full CLI access.

**Best for Ansible teams:** Red Hat's official AAP MCP server if you run AAP 2.6.4+. Otherwise, sibilleb/AAP-Enterprise-MCP-Server (50+ tools) for enterprise environments or bsahane/mcp-ansible (35+ tools) for standalone Ansible.

**Best for Pulumi teams:** [pulumi/mcp-server](/reviews/pulumi-mcp-server/) — the remote hosted mode with Neo delegation is unique in the IaC space.

---

*This review covers publicly available information as of March 2026. ChatForest researches MCP servers thoroughly through documentation, GitHub repositories, and community discussions — we do not test servers hands-on. Star counts are approximate and change over time. Always check the linked repositories for the latest status.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

