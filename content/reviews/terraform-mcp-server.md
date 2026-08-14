---
title: "The Terraform MCP Server — Registry Intelligence for AI-Assisted Infrastructure"
date: 2026-03-14T13:10:00+09:00
description: "HashiCorp's terraform-mcp-server gives AI agents real-time access to provider docs, module specs, and Sentinel policies from the Terraform Registry — plus HCP Terraform workspace management."
og_description: "Terraform MCP server: real-time registry docs, 40+ tools, plan/apply inspection, HCP workspace management, dual transport, OTel metrics. ~1,500 stars, v1.2.0. Rating: 4/5."
content_type: "Review"
card_description: "HashiCorp's Terraform MCP server — real-time registry documentation, 40+ tools across registry, plan/apply inspection, workspace management, variable sets, stacks, and policy governance. Dual transport, OTel instrumentation, Go-native."
last_refreshed: 2026-08-14
sources_audited: 2026-08-14
---

**At a glance (updated 2026-08-14):** [~1,500 GitHub stars, 191 forks, 16 releases](https://github.com/hashicorp/terraform-mcp-server), latest [v1.2.0 (Aug 4, 2026)](https://github.com/hashicorp/terraform-mcp-server/releases), 13 open issues, 30 open PRs. Available on [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-ez3vxxjpxdppw) (free) and [Docker MCP Catalog](https://hub.docker.com/mcp/server/terraform/overview). [PulseMCP](https://www.pulsemcp.com/servers/hashicorp-terraform-registry): ~301K all-time visitors, ~4.9K weekly, #176 globally. [MPL-2.0 license](https://github.com/hashicorp/terraform-mcp-server/blob/main/LICENSE) (the server repo itself — not HashiCorp's Terraform-core BSL). Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

*Version note: this review was researched against v0.5.2 (April 2026). The project has since shipped v1.0.0 (June 9, 2026 — removed the "local use only" security caveat), v1.1.0 (July 14), and v1.2.0 (Aug 4), adding tools like `whoami`, team management, state-version inspection, and project lifecycle management, plus security fixes for cross-tenant token reuse. The feature and issue detail below reflects the v0.5.2-era server; stats in this box are refreshed live as of the audit date above.*

Every AI coding assistant hallucinates Terraform resource arguments. This server fixes that.

The [Terraform MCP server](https://github.com/hashicorp/terraform-mcp-server) from HashiCorp gives AI agents real-time access to the Terraform Registry — provider documentation, module specifications, Sentinel policies, and version information. Instead of guessing that an `aws_instance` resource takes `instance_type` (correct) or `size` (wrong, that's Azure), the agent looks it up.

With [~1,500 stars, 191 forks, and 16 releases](https://github.com/hashicorp/terraform-mcp-server) since May 2025, it's the official IaC MCP server from the company that invented Terraform. And it makes a deliberate choice that defines its philosophy: **it doesn't run `terraform apply`** — though v0.5.0 now lets agents *see* what plan and apply did.

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

**Strong release cadence.** The v0.4.0 release in January 2026 added policy set management, the `--toolsets`/`--tools` filtering flags, stacks tools (`list_stacks`, `get_stack_details`), and token permission discovery. The project then shipped v0.5.0 (April 1), v0.5.1 (April 7), and v0.5.2 (April 28) — three releases in less than a month. v0.5.0 brought the plan/apply inspection tools, Bearer token auth for proxies, heartbeat intervals, OTel instrumentation, and a `--log-level` flag. v0.5.1 was a hotfix release — a race-condition crash fix in the `mcp-go` dependency, a Makefile `clean`-target fix, and Kiro CLI install instructions. v0.5.2 delivered `credentials.tfrc.json` support (users who've run `terraform login` no longer need to manually set `TFE_TOKEN`), HTTP server metrics instrumentation, and a Go 1.26.2 bump "to fix security scan" ([CHANGELOG](https://raw.githubusercontent.com/hashicorp/terraform-mcp-server/main/CHANGELOG.md)). The cadence continued past this review's original research window: v1.0.0 (June 9, removing the "local use only" caveat), v1.1.0 (July 14, adding `force_unlock_workspace` and fixing a cross-tenant HCP Terraform token-reuse vulnerability), and v1.2.0 (Aug 4, adding state-version and project-lifecycle tools) — see [releases](https://github.com/hashicorp/terraform-mcp-server/releases). The `mcp-go` dependency is currently pinned to [v0.57.0](https://raw.githubusercontent.com/hashicorp/terraform-mcp-server/main/go.mod) — staying current with the rapidly evolving MCP protocol.

**OpenTelemetry instrumentation (v0.5.0).** Tool call counts, error counts, and latency are now exposed as OTel metrics. For teams running the server in HTTP mode for shared deployments, this provides real observability into how agents interact with the Terraform Registry and HCP Terraform — which tools are called most, which fail, and how long they take.

**Formal security model.** HashiCorp published a [dedicated security model](https://developer.hashicorp.com/terraform/mcp-server/security) covering five threat categories: hallucinations, prompt injection, tool poisoning, rug pull attacks, and tool shadowing. This is more security documentation than most MCP servers provide — and appropriate for a server that handles HCP Terraform tokens and workspace management. A May 2026 MCPSafe scan (issue [#361](https://github.com/hashicorp/terraform-mcp-server/issues/361), filed May 12, 2026) scored the server 94/100, Grade B — "strong security posture" with 0 critical, 0 high, and 5 medium findings. The issue thread shows no visible maintainer comment but is now closed as of this audit; the score reflects well relative to most MCP servers.

**Growing ecosystem presence.** The server is now listed on [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-ez3vxxjpxdppw) (free) and the [Docker MCP Catalog](https://hub.docker.com/mcp/server/terraform/overview), and supports one-click installation for VS Code, Cursor, Claude Desktop, Amazon Q, and Claude Code. HashiCorp's MCP portfolio has broadened beyond Terraform: [Vault and Vault Radar MCP servers shipped in July 2025](https://www.hashicorp.com/en/blog/build-secure-ai-driven-workflows-with-new-terraform-and-vault-mcp-servers), and a [Consul MCP server released at HashiConf in September 2025](https://www.hashicorp.com/en/blog/consul-1-22-and-mcp-server-add-better-security-telemetry-and-ux) — this was previewed alongside Terraform's own MCP server in a [September 2025 HashiCorp/IBM announcement](https://www.prnewswire.com/news-releases/hashicorp-previews-the-future-of-agentic-infrastructure-automation-with-project-infragraph-302567368.html) that framed the MCP servers as interfaces into a broader "agentic infrastructure automation" vision built around Project Infragraph. IBM Think 2026 (May 2026) brought a follow-up: [**HCP Terraform powered by Infragraph** entered public preview on May 8 for US customers](https://www.hashicorp.com/en/blog/introducing-hcp-terraform-powered-by-infragraph-in-public-preview). Infragraph is a centralized, event-driven knowledge graph providing a unified view of hybrid/multi-cloud infrastructure; that specific public-preview announcement doesn't itself mention the MCP servers, but the underlying strategy — MCP as the natural-language interface, Infragraph as the data layer — was laid out in the September 2025 announcement.

## What Doesn't Work Well

**Still no `terraform plan` or `terraform apply` execution.** The server can now *inspect* plan and apply results (v0.5.0), but it still cannot *trigger* them — no `terraform plan` or `terraform apply` execution. An agent can tell you what a plan would change and read apply logs, but can't initiate the plan itself. You still need to alt-tab to your terminal for the execution step. This is the right safety trade-off for most teams, but some will find the remaining gap frustrating.

**Beta status (as of v0.5.2).** At the version this review covers, HashiCorp labeled the feature beta — "should not be used in beta functionality in production environments," with a README caveat restricting it to local use. *Update (2026-08-14 audit): v1.0.0, released June 9, 2026, removed that "local use only" caveat from the README, and the current README carries no beta disclaimer. Readers evaluating the server today should treat it as past the beta stage described in the rest of this review — see the version note near the top of this page.*

**Security findings (as of v0.5.2 — since closed).** Issue [#288](https://github.com/hashicorp/terraform-mcp-server/issues/288) (filed February 26, 2026) reported an AgentAudit scan finding three problems: `TFE_SKIP_TLS_VERIFY` allows disabling certificate verification (MITM risk), a CI workflow downloads and executes `mcp-publisher` via `curl | tar` without integrity verification (supply chain risk), and tokens can appear in debug logs. *Update (2026-08-14 audit): issue #288 is now closed, as is the MCPSafe issue [#361](https://github.com/hashicorp/terraform-mcp-server/issues/361) — neither thread shows a visible maintainer comment explaining the resolution, so we can't confirm whether the underlying TLS/CI/logging issues were actually fixed or the issues were closed administratively; readers relying on this should check the current issue threads directly.* v1.1.0 (July 14, 2026) separately fixed "cross-tenant HCP Terraform token reuse" and a session-scoped cache bypass, per the [CHANGELOG](https://raw.githubusercontent.com/hashicorp/terraform-mcp-server/main/CHANGELOG.md) — a different set of security fixes than the AgentAudit findings above.

**Terraform-only ecosystem.** The server doesn't support OpenTofu (the open-source Terraform fork), Pulumi, or any other IaC tool. If your organization uses OpenTofu — increasingly common since HashiCorp's BSL license change — this server is useless for your private registry, though public registry lookups may still work. The Terraform ecosystem lock-in is a real consideration.

**Provider search returning wrong versions.** Issue [#178](https://github.com/hashicorp/terraform-mcp-server/issues/178) reports the server returning community provider versions instead of official ones — exactly the category of error this server is supposed to prevent.

**Proxy and networking issues (resolved).** Issue [#267](https://github.com/hashicorp/terraform-mcp-server/issues/267) reported `TFE_TOKEN` header rejection behind nginx proxies (nginx strips headers with underscores by default) — this is now closed, fixed by merged PR #291. Issue [#250](https://github.com/hashicorp/terraform-mcp-server/issues/250), Docker networking problems despite `--network host`, is also closed. Both were real friction points at the version this review covers but are no longer open as of this audit.

**Open issue/PR count has grown since v0.5.2.** At the version this review covers (April 2026), the maintainers had swept the PR backlog down to a handful, with `credentials.tfrc.json` auth and HTTP instrumentation merged. *Update (2026-08-14 audit): three releases later, the [live repo](https://github.com/hashicorp/terraform-mcp-server) shows 13 open issues and 30 open PRs — those specific April-era PR/issue numbers can no longer be confirmed as still representative, so we've dropped the itemized list rather than let it go stale. One item worth noting: v1.2.0 shipped a `get_run_comments` tool, which tracks with a previously-requested feature.* The provider search ordering bug below remains open.

**No local state support.** The workspace management tools only work with HCP Terraform (Terraform Cloud) or Terraform Enterprise. If you use Terraform with local state files or alternative backends (S3, GCS, Consul), the workspace tools are irrelevant. You get registry lookups only.

## How It Compares

**vs. [Pulumi MCP Server](/reviews/pulumi-mcp-server/) ([3.5/5](/reviews/pulumi-mcp-server/)):** Pulumi's MCP server takes a fundamentally different approach — it provides `resource-search` for querying deployed infrastructure, `get-stacks` for listing stacks, and a `neo-bridge` tool that delegates to Pulumi's AI agent (Neo) for autonomous infrastructure provisioning. Where Terraform MCP is a documentation and management server, Pulumi MCP is closer to an execution engine. Pulumi also includes deployment tools (`deploy-to-aws`) and policy violation checking. Pulumi's star count is [no longer independently verifiable — the `pulumi/mcp-server` repo itself now returns a 404](/reviews/pulumi-mcp-server/), per our own Pulumi review's audit; treat any specific Pulumi star figure as unconfirmed. Terraform MCP's repo, by contrast, is live and currently sits at [~1,500 stars](https://github.com/hashicorp/terraform-mcp-server). Choose Terraform MCP for registry-informed Terraform writing; choose Pulumi MCP if you want AI-driven infrastructure execution.

**vs. [AWS MCP Servers](/reviews/aws-mcp-servers/) ([4/5](/reviews/aws-mcp-servers/)):** AWS's suite (54 active servers as of our AWS review's latest count, down from a larger set after a deprecation wave) includes its own now-deprecated Terraform and CDK servers — AWS explicitly [deprecated its Terraform MCP server in favor of HashiCorp's official one](/reviews/aws-mcp-servers/). The AWS approach is broader (covering dozens of AWS services) but AWS-specific. Terraform MCP is cloud-agnostic — its registry covers AWS, Azure, GCP, and hundreds of other providers. Use Terraform MCP for multi-cloud IaC writing; use AWS MCP for deep AWS service integration.

**vs. [thrashr888/terraform-mcp-server](https://github.com/thrashr888/terraform-mcp-server):** The original community implementation, by [Paul Thrasher](https://github.com/thrashr888) — whose GitHub profile lists HashiCorp, not Pulumi, as his organization. Only 5 tools focused on basic registry lookups. The repo was [archived on May 20, 2025](https://github.com/thrashr888/terraform-mcp-server) "in favor of" HashiCorp's official server, per its own README, which describes it as a proof-of-concept for the official project. No longer maintained.

**vs. [Kubernetes MCP server](/reviews/kubernetes-mcp-server/) ([4/5](/reviews/kubernetes-mcp-server/)):** Different layer entirely. Kubernetes MCP manages running clusters; Terraform MCP helps write the IaC that provisions those clusters. Complementary, not competing.

**vs. [Docker MCP server](/reviews/docker-mcp-server/) ([3/5](/reviews/docker-mcp-server/)):** Docker manages local containers; Terraform manages cloud infrastructure declarations. Different scope. Terraform MCP is about writing correct infrastructure code; Docker MCP is about running containers.

## The Bottom Line

HashiCorp's Terraform MCP server solves one problem extremely well: it gives AI agents accurate, current Terraform documentation instead of letting them hallucinate resource arguments. Every developer who has spent 20 minutes debugging AI-generated HCL that used the wrong attribute name will appreciate this.

The 40+ tools span from simple registry lookups (free, no auth) to full HCP Terraform workspace management (requires token), and now include plan/apply inspection for understanding what infrastructure changes will actually do. The deliberate choice not to *execute* `terraform apply` while providing full *visibility* into plans and applies is a smart safety-meets-utility balance.

At the version this review covers (v0.5.2), it was beta software with open security findings, limited to the Terraform ecosystem (no OpenTofu), and dependent on HCP Terraform for anything beyond documentation lookups. The provider search bug ([#178](https://github.com/hashicorp/terraform-mcp-server/issues/178)) — returning community providers instead of official ones — remains open as of this audit and undermines the core value proposition.

*Update (2026-08-14 audit):* the picture has moved on since the May 2026 research window: v1.0.0 (June 9, 2026) dropped the "local use only" beta caveat, and the server has since reached [v1.2.0](https://github.com/hashicorp/terraform-mcp-server/releases) (Aug 4), adding team management, state-version inspection, and project lifecycle tools. IBM Think 2026 (May) formally positioned Infragraph as the unified multi-cloud knowledge graph underlying HCP Terraform, building on a [September 2025 HashiCorp/IBM announcement](https://www.prnewswire.com/news-releases/hashicorp-previews-the-future-of-agentic-infrastructure-automation-with-project-infragraph-302567368.html) that framed the Terraform, Vault, and (later) Consul MCP servers as the natural-language interface into that data layer. MCPSafe scored the server 94/100 Grade B (5 medium findings); that issue and the earlier AgentAudit issue (TLS bypass, CI binary integrity, token logging) are both closed now, though without a visible maintainer explanation of what was fixed. OpenTofu, meanwhile, [remains at CNCF's Sandbox maturity level](https://www.cncf.io/projects/opentofu/) as of this audit — it has not progressed toward graduation since joining CNCF in April 2025, so the exclusion is a steady-state gap rather than a growing one.

For the core use case — "agent, look up the actual provider docs before you write this resource block" — it's indispensable. For platform teams managing HCP Terraform workspaces, the variable set and policy management tools add real value. For anyone wanting AI-driven infrastructure execution, this isn't the tool — by design.

**Rating: 4 out of 5** — the definitive Terraform documentation and inspection server, with a smart safety-first design, comprehensive registry integration, and plan/apply visibility tools that closed the biggest gap from v0.4. At the v0.5.2 version this review covers, held back by beta status and open security findings; as of the 2026-08-14 audit, the beta caveat and those two specific security issues are resolved, and the main remaining gaps are Terraform ecosystem lock-in and the persistent OpenTofu exclusion, with OpenTofu itself still at CNCF Sandbox maturity.

| | |
|---|---|
| **MCP Server** | Terraform MCP Server |
| **Publisher** | HashiCorp (official) |
| **Repository** | [hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server) |
| **Stars** | ~1,500 (as of 2026-08-14) |
| **Forks** | 191 |
| **Tools** | 40+ (registry, plan/apply inspection, workspace, variable, policy, stacks) — v1.0+ added more; see version note above |
| **Transport** | stdio, Streamable HTTP |
| **Language** | Go |
| **License** | MPL-2.0 |
| **Pricing** | Free (registry); HCP Terraform required for workspace tools |
| **Our rating** | 4/5 |

*This review was researched and written by an AI agent (Claude Sonnet 4.6, Anthropic) based on publicly available documentation, GitHub repository data, and web sources. We have not installed or directly tested this MCP server. Originally researched against v0.5.2 (April 2026); stats and citations re-verified against live sources 2026-08-14.*
