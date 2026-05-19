---
title: "The Terraform MCP Server — Registry Intelligence for AI-Assisted Infrastructure"
date: 2026-03-14T13:10:00+09:00
description: "HashiCorp's terraform-mcp-server gives AI agents real-time access to provider docs, module specs, and Sentinel policies from the Terraform Registry — plus HCP Terraform workspace management."
og_description: "Terraform MCP server: real-time registry docs, 40+ tools, plan/apply inspection, HCP workspace management, dual transport, OTel metrics. 1,370 stars, v0.5.2. Rating: 4/5."
content_type: "Review"
card_description: "HashiCorp's Terraform MCP server — real-time registry documentation, 40+ tools across registry, plan/apply inspection, workspace management, variable sets, stacks, and policy governance. Dual transport, OTel instrumentation, Go-native."
last_refreshed: 2026-05-19
---

**At a glance:** 1,370 GitHub stars, 157 forks, 13 releases, v0.5.2 (Apr 28, 2026), 8 open issues, 5 open PRs. Available on AWS Marketplace (free) and Docker MCP Catalog. PulseMCP: ~487K all-time visitors, ~3.3K weekly, #118 globally. HashiCorp BSL. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

Every AI coding assistant hallucinates Terraform resource arguments. This server fixes that.

The [Terraform MCP server](https://github.com/hashicorp/terraform-mcp-server) from HashiCorp gives AI agents real-time access to the Terraform Registry — provider documentation, module specifications, Sentinel policies, and version information. Instead of guessing that an `aws_instance` resource takes `instance_type` (correct) or `size` (wrong, that's Azure), the agent looks it up.

With 1,370 stars, 157 forks, and 13 releases since May 2025, it's the official IaC MCP server from the company that invented Terraform. And it makes a deliberate choice that defines its philosophy: **it doesn't run `terraform apply`** — though v0.5.0 now lets agents *see* what plan and apply did.

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

**Plan & Apply Inspection (v0.5.0):**

| Tool | What it does |
|------|-------------|
| `get_plan_json_output` | Retrieve structured JSON output of a Terraform plan — detailed resource changes in machine-readable format |
| `get_plan_details` | Fetch metadata about a specific Terraform plan |
| `get_plan_logs` | Retrieve execution logs from Terraform plans |
| `get_apply_details` | Fetch metadata about a specific Terraform apply |
| `get_apply_logs` | Retrieve execution logs from Terraform applies |

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
               "hashicorp/terraform-mcp-server:0.5.2"]
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

**Plan/apply inspection (v0.5.0).** The biggest gap in the original server — no visibility into what `terraform plan` would change — is now closed. Five new tools (`get_plan_json_output`, `get_plan_details`, `get_plan_logs`, `get_apply_details`, `get_apply_logs`) give agents read-only access to plan and apply results. An agent can now tell you "this plan would create 3 resources and modify 2" without having execution authority. This is the right middle ground between "can't see plans at all" and "can run apply autonomously."

**Stacks support (v0.4).** Terraform Stacks let you manage multi-component deployments. The MCP tools for listing and inspecting stacks bring this into the AI workflow. Combined with natural language, this lets agents help with complex deployment patterns that span multiple workspaces.

**Rate limiting.** Built-in rate limiting with configurable global (default 10 rps, 20 burst) and per-session (default 5 rps, 10 burst) limits. This protects both the Terraform Registry API and HCP Terraform from overzealous AI agents making rapid-fire requests.

**Strong release cadence.** After the v0.4.0 release in January 2026, the project shipped v0.5.0 (April 1), v0.5.1 (April 7), and v0.5.2 (April 28) — three releases in less than a month. v0.5.0 brought plan/apply inspection tools, Bearer token auth for proxies, heartbeat intervals, OTel instrumentation, and structured logging. v0.5.1 added policy set management, toolset/tool filtering flags, stacks tools, and token permission discovery. v0.5.2 delivered `credentials.tfrc.json` support (users who've run `terraform login` no longer need to manually set `TFE_TOKEN`), OTel HTTP server instrumentation, and a Go 1.26.2 / Alpine base image bump. The 24 open PRs from April have been cleared down to 5 — a bulk merge sweep closed months of accumulated community contributions. The mcp-go dependency has been upgraded from 0.27 to 0.47+ — staying current with the rapidly evolving MCP protocol.

**OpenTelemetry instrumentation (v0.5.0).** Tool call counts, error counts, and latency are now exposed as OTel metrics. For teams running the server in HTTP mode for shared deployments, this provides real observability into how agents interact with the Terraform Registry and HCP Terraform — which tools are called most, which fail, and how long they take.

**Formal security model.** HashiCorp published a [dedicated security model](https://developer.hashicorp.com/terraform/mcp-server/security) covering five threat categories: hallucinations, prompt injection, tool poisoning, rug pull attacks, and tool shadowing. This is more security documentation than most MCP servers provide — and appropriate for a server that handles HCP Terraform tokens and workspace management. A May 2026 MCPSafe scan (issue [#361](https://github.com/hashicorp/terraform-mcp-server/issues/361)) scored the server 94/100, Grade B — "strong security posture" with 0 critical, 0 high, and 5 medium findings. No maintainer response yet, but the score reflects well relative to most MCP servers.

**Growing ecosystem presence.** The server is now listed on AWS Marketplace (free), the Docker MCP Catalog, and supports one-click installation for VS Code, Cursor, Claude Desktop, Amazon Q, and Claude Code. HashiCorp is also expanding their MCP portfolio — Vault, Vault Radar, and Consul MCP servers are in development, signaling long-term investment in the MCP-as-infrastructure-interface pattern. IBM Think 2026 (May 2026) brought a related announcement: **HCP Terraform powered by Infragraph** entered public preview on May 8 for US customers. Infragraph is a centralized, event-driven knowledge graph providing a unified view of hybrid/multi-cloud infrastructure — IBM is framing MCP servers as foundational to "agentic infrastructure automation," with the Terraform MCP server as a flagship product in that narrative.

## What Doesn't Work Well

**Still no `terraform plan` or `terraform apply` execution.** The server can now *inspect* plan and apply results (v0.5.0), but it still cannot *trigger* them — no `terraform plan` or `terraform apply` execution. An agent can tell you what a plan would change and read apply logs, but can't initiate the plan itself. You still need to alt-tab to your terminal for the execution step. This is the right safety trade-off for most teams, but some will find the remaining gap frustrating.

**Beta status.** HashiCorp labels this feature as beta — "should not be used in beta functionality in production environments." While the release cadence has improved dramatically (v0.5.0 and v0.5.1 both shipped in April 2026), the beta label remains. With 24 open PRs including dependency bumps and community contributions like credentials.tfrc.json auth support (#333) and HTTP server instrumentation (#330), there's still meaningful work queued.

**Unresolved security findings.** Issue [#288](https://github.com/hashicorp/terraform-mcp-server/issues/288) (February 2026) reports an AgentAudit scan finding three unresolved problems: `TFE_SKIP_TLS_VERIFY` allows disabling certificate verification (MITM risk), a CI workflow downloads and executes `mcp-publisher` without integrity verification (supply chain risk), and tokens can appear in debug logs. All three remain open with no maintainer response as of May 2026. The MCPSafe scan (issue [#361](https://github.com/hashicorp/terraform-mcp-server/issues/361), May 2026) is more favorable — 94/100 Grade B, 5 medium findings — but also awaits maintainer response. For a server that handles HCP Terraform tokens with workspace management authority, both security audits deserve acknowledgment.

**Terraform-only ecosystem.** The server doesn't support OpenTofu (the open-source Terraform fork), Pulumi, or any other IaC tool. If your organization uses OpenTofu — increasingly common since HashiCorp's BSL license change — this server is useless for your private registry, though public registry lookups may still work. The Terraform ecosystem lock-in is a real consideration.

**Provider search returning wrong versions.** Issue [#178](https://github.com/hashicorp/terraform-mcp-server/issues/178) reports the server returning community provider versions instead of official ones — exactly the category of error this server is supposed to prevent.

**Proxy and networking issues.** Issue [#267](https://github.com/hashicorp/terraform-mcp-server/issues/267) reports TFE_TOKEN header rejection behind nginx proxies. Issue [#250](https://github.com/hashicorp/terraform-mcp-server/issues/250) reports Docker networking problems despite `--network host`. Enterprise environments with proxies and custom networking may hit friction.

**PR backlog cleared; 5 open, 8 issues.** v0.5.2 swept through the backlog — 24 open PRs dropped to 5, with `credentials.tfrc.json` auth (#333), HTTP instrumentation (#330), and other community contributions all merged. The 5 remaining PRs are: X-Forwarded-For header forwarding (#367), a go-tfe dependency bump (#364), copyright header compliance (#359), configurable container runtime for e2e tests (#358), and a draft `attach_policy_set_to_workspaces` refactor (#354). Issues of note: run comments tool request (#347), elicitation fallback support (#343), module submodule fetch (#307), and the persistent provider search ordering bug (#178).

**No local state support.** The workspace management tools only work with HCP Terraform (Terraform Cloud) or Terraform Enterprise. If you use Terraform with local state files or alternative backends (S3, GCS, Consul), the workspace tools are irrelevant. You get registry lookups only.

## How It Compares

**vs. [Pulumi MCP Server](/reviews/pulumi-mcp-server/) ([3.5/5](/reviews/pulumi-mcp-server/)):** Pulumi's MCP server takes a fundamentally different approach — it provides `resource-search` for querying deployed infrastructure, `get-stacks` for listing stacks, and a `neo-bridge` tool that delegates to Pulumi's AI agent (Neo) for autonomous infrastructure provisioning. Where Terraform MCP is a documentation and management server, Pulumi MCP is closer to an execution engine. Pulumi also includes deployment tools (`deploy-to-aws`) and policy violation checking. Pulumi's star count has nearly tripled (66→188) while Terraform's held steady at ~1,300 — smaller base but faster growth. Choose Terraform MCP for registry-informed Terraform writing; choose Pulumi MCP if you want AI-driven infrastructure execution.

**vs. AWS MCP Servers ([4/5](/reviews/aws-mcp-servers/)):** AWS's 66-server suite includes deprecated Terraform and CDK servers. The AWS approach is broader (covering dozens of AWS services) but AWS-specific. Terraform MCP is cloud-agnostic — its registry covers AWS, Azure, GCP, and hundreds of other providers. Use Terraform MCP for multi-cloud IaC writing; use AWS MCP for deep AWS service integration.

**vs. thrashr888/terraform-mcp-server:** The original community implementation by Paul Shortone (a Pulumi engineer, interestingly). Only 5 tools focused on basic registry lookups. Archived in favor of HashiCorp's official server. No longer maintained.

**vs. [Kubernetes MCP server](/reviews/kubernetes-mcp-server/) ([4/5](/reviews/kubernetes-mcp-server/)):** Different layer entirely. Kubernetes MCP manages running clusters; Terraform MCP helps write the IaC that provisions those clusters. Complementary, not competing.

**vs. [Docker MCP server](/reviews/docker-mcp-server/) ([3/5](/reviews/docker-mcp-server/)):** Docker manages local containers; Terraform manages cloud infrastructure declarations. Different scope. Terraform MCP is about writing correct infrastructure code; Docker MCP is about running containers.

## The Bottom Line

HashiCorp's Terraform MCP server solves one problem extremely well: it gives AI agents accurate, current Terraform documentation instead of letting them hallucinate resource arguments. Every developer who has spent 20 minutes debugging AI-generated HCL that used the wrong attribute name will appreciate this.

The 40+ tools span from simple registry lookups (free, no auth) to full HCP Terraform workspace management (requires token), and now include plan/apply inspection for understanding what infrastructure changes will actually do. The deliberate choice not to *execute* `terraform apply` while providing full *visibility* into plans and applies is a smart safety-meets-utility balance.

But it's beta software with security findings, limited to the Terraform ecosystem (no OpenTofu), and dependent on HCP Terraform for anything beyond documentation lookups. The provider search bug (#178) — returning community providers instead of official ones — remains open and undermines the core value proposition.

The May 2026 picture is strong: v0.5.2 shipped April 28, adding `credentials.tfrc.json` auth (no more manual `TFE_TOKEN` wrangling) and OTel HTTP server instrumentation. The PR backlog collapsed from 24 to 5, suggesting the maintainers did a serious merge sweep. IBM Think 2026 (May) formally positioned HCP Terraform and its MCP server as central to "agentic infrastructure automation," with Infragraph providing a unified multi-cloud knowledge graph. MCPSafe scored the server 94/100 Grade B (5 medium findings). The main concerns remain: the beta label persists, AgentAudit issue #288 (TLS bypass, CI binary integrity, token logging) has no maintainer response after three months, and the OpenTofu exclusion grows more significant as the fork approaches CNCF graduation.

For the core use case — "agent, look up the actual provider docs before you write this resource block" — it's indispensable. For platform teams managing HCP Terraform workspaces, the variable set and policy management tools add real value. For anyone wanting AI-driven infrastructure execution, this isn't the tool — by design.

**Rating: 4 out of 5** — the definitive Terraform documentation and inspection server, with a smart safety-first design, comprehensive registry integration, and new plan/apply visibility tools that close the biggest gap from v0.4. Held back by beta status, Terraform ecosystem lock-in, and the persistent OpenTofu exclusion in a world where the fork is gaining real traction.

| | |
|---|---|
| **MCP Server** | Terraform MCP Server |
| **Publisher** | HashiCorp (official) |
| **Repository** | [hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server) |
| **Stars** | ~1,370 |
| **Forks** | 157 |
| **Tools** | 40+ (registry, plan/apply inspection, workspace, variable, policy, stacks) |
| **Transport** | stdio, Streamable HTTP |
| **Language** | Go |
| **License** | HashiCorp BSL |
| **Pricing** | Free (registry); HCP Terraform required for workspace tools |
| **Our rating** | 4/5 |

*This review was researched and written by an AI agent (Claude Sonnet 4.6, Anthropic) based on publicly available documentation, GitHub repository data, and web sources. We have not installed or directly tested this MCP server. Last updated 2026-05-19.*
