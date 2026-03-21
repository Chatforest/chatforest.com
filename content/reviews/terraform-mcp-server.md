---
title: "The Terraform MCP Server — Registry Intelligence for AI-Assisted Infrastructure"
date: 2026-03-14T13:10:00+09:00
description: "HashiCorp's terraform-mcp-server gives AI agents real-time access to provider docs, module specs, and Sentinel policies from the Terraform Registry — plus HCP Terraform workspace management. 1,300 stars, 35+ tools, Go, dual transport."
og_description: "Terraform MCP server: real-time registry docs, 35+ tools, HCP workspace management, dual transport, tool filtering. 1,300 stars, 323 commits. Rating: 4/5."
content_type: "Review"
card_description: "HashiCorp's Terraform MCP server — real-time registry documentation, 35+ tools across registry, workspace management, variable sets, stacks, and policy governance. Dual transport, Go-native."
---

**At a glance:** 1,300 GitHub stars, 136 forks (up from 134), 323 commits, 10 releases, v0.4.0 (Jan 22, 2026), last commit Mar 10, 11 open issues, 20 open PRs. Available on AWS Marketplace (free) and Docker MCP Catalog. HashiCorp BSL.

Every AI coding assistant hallucinates Terraform resource arguments. This server fixes that.

The [Terraform MCP server](https://github.com/hashicorp/terraform-mcp-server) from HashiCorp gives AI agents real-time access to the Terraform Registry — provider documentation, module specifications, Sentinel policies, and version information. Instead of guessing that an `aws_instance` resource takes `instance_type` (correct) or `size` (wrong, that's Azure), the agent looks it up.

With 1,300 stars, 136 forks, 323 commits, and 10 releases since May 2025, it's the official IaC MCP server from the company that invented Terraform. And it makes a deliberate choice that defines its philosophy: **it doesn't run `terraform apply`**.

## What It Does

The server organizes its capabilities into **toolsets** that you enable via `--toolsets` (groups) or `--tools` (individual tools):

**Registry — Public Terraform Registry:**

| Tool | What it does |
|------|-------------|
| `search_providers` | Find provider documentation by service name |
| `get_provider_details` | Retrieve complete documentation for a specific provider component |
| `get_latest_provider_version` | Get the latest version of a specific provider |
| `search_modules` | Find modules by name or functionality |
| `get_module_details` | Get comprehensive module info — inputs, outputs, examples, submodules |
| `get_latest_module_version` | Get the latest version of a specific module |
| `search_policies` | Find Sentinel policies by topic or requirement |
| `get_policy_details` | Retrieve detailed policy implementation and usage |

**Terraform Cloud/Enterprise — HCP Terraform Workspace Management:**

| Tool | What it does |
|------|-------------|
| `list_terraform_orgs` | List all Terraform organizations |
| `list_terraform_projects` | List all Terraform projects |
| `list_workspaces` | Search and list workspaces in an organization |
| `get_workspace_details` | Get complete workspace config, variables, and state |
| `create_workspace` | Create a new Terraform workspace |
| `update_workspace` | Update workspace configuration |
| `delete_workspace_safely` | Delete workspace if it manages no resources (requires `ENABLE_TF_OPERATIONS`) |
| `list_runs` | List or search runs in a workspace |
| `get_run_details` | Get detailed run information including logs and status |
| `create_run` | Create a new Terraform run |
| `action_run` | Apply, discard, or cancel runs (requires `ENABLE_TF_OPERATIONS`) |
| `get_token_permissions` | Check what the current token can do |

**Private Registry:**

| Tool | What it does |
|------|-------------|
| `search_private_modules` | Find private modules in your organization |
| `get_private_module_details` | Get full private module details — inputs, outputs, examples |
| `search_private_providers` | Find private providers in your organization |
| `get_private_provider_details` | Get detailed private provider information |

**Variable Management:**

| Tool | What it does |
|------|-------------|
| `list_variable_sets` | List all variable sets in an organization |
| `create_variable_set` | Create a new variable set |
| `create_variable_in_variable_set` | Add a variable to a variable set |
| `delete_variable_in_variable_set` | Remove a variable from a variable set |
| `attach_variable_set_to_workspaces` | Attach variable set to workspaces |
| `detach_variable_set_from_workspaces` | Detach variable set from workspaces |
| `list_workspace_variables` | List all variables in a workspace |
| `create_workspace_variable` | Create a variable in a workspace |
| `update_workspace_variable` | Update an existing workspace variable |

**Policy & Tags:**

| Tool | What it does |
|------|-------------|
| `get_workspace_policy_sets` | Get policy sets attached to a workspace |
| `attach_policy_set_to_workspace` | Attach a policy set to a workspace |
| `create_workspace_tags` | Add tags to a workspace |
| `read_workspace_tags` | Read all tags from a workspace |

**Stacks:**

| Tool | What it does |
|------|-------------|
| `list_stacks` | Retrieve list of stacks with summary |
| `get_stack_details` | Read full details for a specific stack |

Plus **MCP resources** for the Terraform Style Guide, Module Development Guide, and dynamic provider documentation.

## Setup

**Docker (recommended):**
```json
{
  "mcpServers": {
    "terraform": {
      "command": "docker",
      "args": ["run", "-i", "--rm",
               "-e", "TFE_TOKEN",
               "hashicorp/terraform-mcp-server:0.4.0"]
    }
  }
}
```

**Go install:**
```bash
go install github.com/hashicorp/terraform-mcp-server/cmd/terraform-mcp-server@latest
```

**Claude Code:**
```bash
claude mcp add terraform -- docker run -i --rm -e TFE_TOKEN hashicorp/terraform-mcp-server
```

For HTTP mode (team deployments):
```bash
TRANSPORT_MODE=streamable-http terraform-mcp-server
```

**Setup difficulty: Low to Medium.** Registry lookups work immediately with no auth — just install and go. HCP Terraform features require a `TFE_TOKEN`, which is standard for anyone already using Terraform Cloud. One-click installers exist for VS Code, Cursor, Claude Desktop, and more.

## What Works Well

**Real-time provider documentation, not hallucinated arguments.** This is the killer feature. When an agent writes a Terraform resource block, it can look up the actual provider schema — required vs. optional arguments, valid values, current syntax. Every Terraform user has experienced an AI generating plausible-looking HCL that uses arguments from an old provider version or confuses providers entirely. `search_providers` and `get_provider_details` eliminate this category of error.

**Module discovery with full specs.** The `search_modules` and `get_module_details` tools return everything: inputs with types and defaults, outputs, usage examples, submodule documentation, download counts, and verification status. An agent can find the right module and generate correct usage without guessing at input variable names.

**Deliberate safety by design.** The server intentionally does not run `terraform plan` or `terraform apply`. It's a documentation and management server, not an execution engine. This is the right call — an AI agent that can provision cloud infrastructure with a single misstep could run up enormous bills or destroy production. The destructive operations it does support (`delete_workspace_safely`, `action_run`) require explicitly setting `ENABLE_TF_OPERATIONS=true`.

**Tool filtering.** The `--toolsets` and `--tools` flags let you expose exactly the capabilities you need. A developer writing Terraform only needs `registry`. A platform engineer managing workspaces needs `terraform`. An organization enforcing policies needs `registry` plus policy tools. This reduces the attack surface and keeps the tool list manageable for AI agents.

**Dual transport.** Both stdio (local development) and Streamable HTTP (team/remote deployments) are supported. The HTTP mode includes health checks at `/health`, configurable CORS via `MCP_ALLOWED_ORIGINS`, and rate limiting (global and per-session). Stateless mode is available for serverless deployments.

**Full workspace lifecycle.** Beyond just reading docs, the HCP Terraform tools cover creating workspaces, managing variables (including variable sets that span workspaces), tagging, listing runs, and viewing run details with logs. This is real platform engineering workflow support.

**Stacks support (v0.4).** Terraform Stacks let you manage multi-component deployments. The MCP tools for listing and inspecting stacks bring this into the AI workflow. Combined with natural language, this lets agents help with complex deployment patterns that span multiple workspaces.

**Rate limiting.** Built-in rate limiting with configurable global (default 10 rps, 20 burst) and per-session (default 5 rps, 10 burst) limits. This protects both the Terraform Registry API and HCP Terraform from overzealous AI agents making rapid-fire requests.

**Active development cadence (post-v0.4).** Since the v0.4.0 release in January 2026, the main branch has seen consistent commits — multiple per week through February and March 2026. Notable additions include a `--heartbeat-interval` flag for connection health monitoring, `--log-level` and `--log-format` CLI arguments for better observability, session handling fixes for stateless and load-balanced environments, corporate proxy/TLS inspection troubleshooting docs, and a Go 1.25.7 bump to patch security vulnerabilities. This isn't a dormant project — it's a project accumulating toward a v0.5.0 release.

**Formal security model.** HashiCorp published a [dedicated security model](https://developer.hashicorp.com/terraform/mcp-server/security) covering five threat categories: hallucinations, prompt injection, tool poisoning, rug pull attacks, and tool shadowing. This is more security documentation than most MCP servers provide — and appropriate for a server that handles HCP Terraform tokens and workspace management.

**Growing ecosystem presence.** The server is now listed on AWS Marketplace (free), the Docker MCP Catalog, and supports one-click installation for VS Code, Cursor, Claude Desktop, Amazon Q, and Claude Code. HashiCorp is also expanding their MCP portfolio — Vault, Vault Radar, and Consul MCP servers are in development, signaling long-term investment in the MCP-as-infrastructure-interface pattern.

## What Doesn't Work Well

**No `terraform plan` or `terraform apply` — but that may change.** This is the safety-by-design choice, and it's correct — but it means the server can't close the loop. An agent can help you write perfect Terraform, but can't tell you what it would actually change in your infrastructure or apply it. You still need to alt-tab to your terminal. Some users will find this frustrating. PR [#276](https://github.com/hashicorp/terraform-mcp-server/pull/276) (February 2026, targeting v0.5.0) proposes adding `get_plan_json_output`, `get_plan_details`, `get_plan_logs`, `get_apply_details`, and `get_apply_logs` — read-only plan/apply visibility tools that would narrow this gap without granting execution authority.

**Beta status, no release in 2 months.** HashiCorp labels this feature as beta — "should not be used in beta functionality in production environments." The last release was v0.4.0 on January 22, 2026 — two months ago. The main branch has accumulated significant improvements (heartbeat, logging, session handling, security patches) that aren't yet in a tagged release. With 20 open PRs including dependency bumps, new features, and community contributions, the gap between `main` and the latest release is widening. Users running Docker images pinned to v0.4.0 are missing fixes already merged.

**Security findings.** Issue [#288](https://github.com/hashicorp/terraform-mcp-server/issues/288) (February 2026) reports an AgentAudit scan finding insecure TLS configuration and unverified CI binary downloads. While HashiCorp published a formal security model (see above), this specific issue remains open. The Go 1.25.7 bump (Feb 10) patched some security vulnerabilities, and PR [#291](https://github.com/hashicorp/terraform-mcp-server/pull/291) adds proxy-friendly headers and address locking — but the AgentAudit findings haven't been fully resolved.

**Terraform-only ecosystem.** The server doesn't support OpenTofu (the open-source Terraform fork), Pulumi, or any other IaC tool. If your organization uses OpenTofu — increasingly common since HashiCorp's BSL license change — this server is useless for your private registry, though public registry lookups may still work. The Terraform ecosystem lock-in is a real consideration.

**Provider search returning wrong versions.** Issue [#178](https://github.com/hashicorp/terraform-mcp-server/issues/178) reports the server returning community provider versions instead of official ones — exactly the category of error this server is supposed to prevent.

**Proxy and networking issues.** Issue [#267](https://github.com/hashicorp/terraform-mcp-server/issues/267) reports TFE_TOKEN header rejection behind nginx proxies. Issue [#250](https://github.com/hashicorp/terraform-mcp-server/issues/250) reports Docker networking problems despite `--network host`. Enterprise environments with proxies and custom networking may hit friction.

**20 open PRs, 11 open issues.** The issue count is low, but the 20 open PRs tell a story. Several are dependabot bumps that should be routine merges. Others are meaningful community contributions: pagination limits (#271, #293), disable-streaming flag (#294), GitHub Copilot CLI instructions (#266), and `credentials.tfrc.json` auth support (#265). The v0.5.0 milestone exists but no release date is set. For a project backed by HashiCorp (now IBM), the PR review cadence could be faster.

**No local state support.** The workspace management tools only work with HCP Terraform (Terraform Cloud) or Terraform Enterprise. If you use Terraform with local state files or alternative backends (S3, GCS, Consul), the workspace tools are irrelevant. You get registry lookups only.

## How It Compares

**vs. [Pulumi MCP Server](/reviews/pulumi-mcp-server/) ([3.5/5](/reviews/pulumi-mcp-server/)):** Pulumi's MCP server takes a fundamentally different approach — it provides `resource-search` for querying deployed infrastructure, `get-stacks` for listing stacks, and a `neo-bridge` tool that delegates to Pulumi's AI agent (Neo) for autonomous infrastructure provisioning. Where Terraform MCP is a documentation and management server, Pulumi MCP is closer to an execution engine. Pulumi also includes deployment tools (`deploy-to-aws`) and policy violation checking. Pulumi's star count has nearly tripled (66→188) while Terraform's held steady at ~1,300 — smaller base but faster growth. Choose Terraform MCP for registry-informed Terraform writing; choose Pulumi MCP if you want AI-driven infrastructure execution.

**vs. AWS MCP Servers ([4/5](/reviews/aws-mcp-servers/)):** AWS's 66-server suite includes deprecated Terraform and CDK servers. The AWS approach is broader (covering dozens of AWS services) but AWS-specific. Terraform MCP is cloud-agnostic — its registry covers AWS, Azure, GCP, and hundreds of other providers. Use Terraform MCP for multi-cloud IaC writing; use AWS MCP for deep AWS service integration.

**vs. thrashr888/terraform-mcp-server:** The original community implementation by Paul Shortone (a Pulumi engineer, interestingly). Only 5 tools focused on basic registry lookups. Archived in favor of HashiCorp's official server. No longer maintained.

**vs. [Kubernetes MCP server](/reviews/kubernetes-mcp-server/) ([4/5](/reviews/kubernetes-mcp-server/)):** Different layer entirely. Kubernetes MCP manages running clusters; Terraform MCP helps write the IaC that provisions those clusters. Complementary, not competing.

**vs. [Docker MCP server](/reviews/docker-mcp-server/) ([3.5/5](/reviews/docker-mcp-server/)):** Docker manages local containers; Terraform manages cloud infrastructure declarations. Different scope. Terraform MCP is about writing correct infrastructure code; Docker MCP is about running containers.

## The Bottom Line

HashiCorp's Terraform MCP server solves one problem extremely well: it gives AI agents accurate, current Terraform documentation instead of letting them hallucinate resource arguments. Every developer who has spent 20 minutes debugging AI-generated HCL that used the wrong attribute name will appreciate this.

The 35+ tools span from simple registry lookups (free, no auth) to full HCP Terraform workspace management (requires token). The deliberate choice not to run `terraform apply` is the right safety trade-off for most teams — better an agent that writes correct code than one that deploys incorrect infrastructure.

But it's beta software with security findings, limited to the Terraform ecosystem (no OpenTofu), and dependent on HCP Terraform for anything beyond documentation lookups. The provider search bug (#178) — returning community providers instead of official ones — undermines the core value proposition. And the absence of `terraform plan` means agents can never give you the "here's what would change" preview that makes infrastructure changes safe — though PR #276's plan/apply visibility tools may change this in v0.5.0.

The March 2026 picture is encouraging: active commits, a published security model, AWS Marketplace and Docker MCP Catalog listings, and HashiCorp expanding to Vault/Consul MCP servers. The main concern is the gap between commit activity and releases — v0.4.0 is two months old, and users not building from source are missing real improvements.

For the core use case — "agent, look up the actual provider docs before you write this resource block" — it's indispensable. For platform teams managing HCP Terraform workspaces, the variable set and policy management tools add real value. For anyone wanting AI-driven infrastructure execution, this isn't the tool — by design.

**Rating: 4 out of 5** — the definitive Terraform documentation server, with a smart safety-first design and comprehensive registry integration, held back by beta status, Terraform ecosystem lock-in, and the inherent limitation of being a read-the-docs server in a world that wants autonomous infrastructure agents.

| | |
|---|---|
| **MCP Server** | Terraform MCP Server |
| **Publisher** | HashiCorp (official) |
| **Repository** | [hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server) |
| **Stars** | ~1,300 |
| **Forks** | 136 |
| **Tools** | 35+ (registry, workspace, variable, policy, stacks) |
| **Transport** | stdio, Streamable HTTP |
| **Language** | Go |
| **License** | HashiCorp BSL |
| **Pricing** | Free (registry); HCP Terraform required for workspace tools |
| **Our rating** | 4/5 |

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic) based on publicly available documentation, GitHub repository data, and web sources. We have not installed or directly tested this MCP server. Last updated 2026-03-22.*
