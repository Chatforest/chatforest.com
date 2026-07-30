---
title: "HashiCorp Terraform MCP Server: Infrastructure-as-Code Intelligence for AI Agents (Builder Guide)"
date: 2026-06-17
description: "HashiCorp's official Terraform MCP Server (v1.1.0, generally available) gives AI agents real-time access to the Terraform Registry — provider docs, module specs, and HCP Terraform workspace management — without execution authority."
og_description: "The Terraform MCP Server gives AI agents accurate, current provider documentation and workspace management without letting them trigger plan or apply. Here is what builders need to know to wire it into Claude or any MCP-compatible agent."
content_type: "Builder's Log"
categories: ["MCP", "Infrastructure", "DevOps", "AI Agents"]
tags: ["hashicorp", "terraform", "mcp", "infrastructure-as-code", "hcp-terraform", "terraform-registry", "workspace-management", "claude", "claude-code", "cursor", "ai-agents", "builder-guide", "iac", "devops"]
sources_audited: 2026-07-30
---

AI coding assistants hallucinate Terraform. Not occasionally — routinely. They invent resource attributes that do not exist, use argument names from the wrong provider version, and confuse AWS argument names with Azure equivalents. When the generated HCL looks plausible but fails on `terraform validate`, you have lost time you cannot recover.

HashiCorp's official Terraform MCP Server — [generally available](https://www.hashicorp.com/en/blog/terraform-mcp-server-is-now-generally-available) since [v1.0.0](https://github.com/hashicorp/terraform-mcp-server/releases/tag/v1.0.0) in June 2026, now at [v1.1.0](https://github.com/hashicorp/terraform-mcp-server/releases/tag/v1.1.0) — solves this at the source. Instead of letting an agent guess at provider schemas, you give it a tool call to look them up. The server connects your AI agent to the live Terraform Registry — provider documentation, module specifications, Sentinel policies — and to HCP Terraform workspace management, variable sets, and plan/apply inspection.

The server deliberately does not run `terraform plan` or `terraform apply`. That is a feature, not a gap.

---

## What the Terraform MCP Server Is

The Terraform MCP Server is a Model Context Protocol server, officially maintained by HashiCorp — acquired by IBM in a deal that [closed February 27, 2025](https://techcrunch.com/2025/02/27/ibm-closes-6-4b-hashicorp-acquisition/) ([SiliconANGLE confirms](https://siliconangle.com/2025/02/27/ibm-completes-6-4b-hashicorp-acquisition-following-regulatory-approvals/)) — that gives AI agents structured access to Terraform infrastructure. It translates MCP tool calls into Terraform Registry API requests and HCP Terraform API requests, returning real documentation and real workspace data to the agent.

It ships with **stdio** and **StreamableHTTP** [transport support](https://github.com/hashicorp/terraform-mcp-server), making it compatible with Claude for Desktop, Claude Code, Cursor, VS Code, Amazon Q, and any MCP-compliant client. Tool filtering lets you expose exactly the capability surface you need — from pure registry lookups with no auth, to full workspace management with an HCP Terraform token.

**Current status:** [Generally available](https://www.hashicorp.com/en/blog/terraform-mcp-server-is-now-generally-available) as of June 2026. The server moved fast to get there: [v0.5.0, v0.5.1, and v0.5.2 shipped within four weeks](https://github.com/hashicorp/terraform-mcp-server/releases) in April 2026, followed by the [v1.0.0 GA release](https://github.com/hashicorp/terraform-mcp-server/releases/tag/v1.0.0) in June and [v1.1.0](https://github.com/hashicorp/terraform-mcp-server/releases/tag/v1.1.0) in July — the latter a security-patch release (three CVEs; see Limitations below). Run at least v1.1.0.

---

## The Problem: Agents Writing Terraform Without Documentation

When a developer writes Terraform, they have years of provider experience, IDE completion, and a browser tab open to the registry. When an AI agent writes Terraform, it has whatever was in the training data — which may be outdated, misremembered, or simply wrong.

The Terraform ecosystem makes this worse than most. There are thousands of providers. Provider schemas change between versions. The `aws_instance` resource looks different from 2020 to 2026. Azure VM arguments differ from AWS VM arguments in ways that are easy to confuse. A plausible-looking HCL block can fail at validate, plan, or only surface as a bug in production.

The standard agent workflow — "write Terraform, human reviews and fixes" — puts all the hallucination cost on the human reviewer. The Terraform MCP Server moves that cost earlier: the agent looks up the actual schema before generating code. The reviewer is checking business logic, not syntax.

---

## Architecture: Toolsets and Filtering

The Terraform MCP Server organizes its 40+ tools into [**toolsets**](https://github.com/hashicorp/terraform-mcp-server/blob/main/README.md) that you enable selectively via `--toolsets`. This is a deliberate design choice: not every workflow needs every capability, and a smaller tool surface keeps agent context manageable and the security perimeter tighter.

**There are only three toolsets** — fewer than you might expect, and not split as finely as some builder writeups (including an earlier version of this guide) assume:

| Flag | What it controls |
|------|-----------------|
| `--toolsets registry` | Public Terraform Registry: providers, modules, Sentinel policies (no auth required) — this is the default |
| `--toolsets registry-private` | Private registry providers/modules in HCP Terraform or Terraform Enterprise (requires `TFE_TOKEN`) |
| `--toolsets terraform` | Everything else on HCP Terraform/TFE in one bundle: orgs, projects, workspaces, runs, plan/apply inspection, variable sets, policy sets, workspace tags, and Stacks (requires `TFE_TOKEN`) |
| `--toolsets all` | Every toolset enabled |
| `--tools <name1>,<name2>,...` | Enable specific individual tools by name instead of a whole toolset |

There is **no** separate toolset for variables, policies, plan/apply, or Stacks — those all live inside the single `terraform` toolset. If you want a narrower slice (e.g., read-only plan inspection without workspace-modifying tools), use `--tools` with specific tool names rather than `--toolsets terraform`.

For local development and IaC writing, `--toolsets registry` is all you need — and it requires no authentication at all.

---

## Installation

Three deployment paths are supported.

### Docker (Recommended)

```json
{
  "mcpServers": {
    "terraform": {
      "command": "docker",
      "args": ["run", "-i", "--rm",
               "-e", "TFE_TOKEN",
               "hashicorp/terraform-mcp-server:1.1.0"]
    }
  }
}
```

For registry-only use (no HCP Terraform), omit `TFE_TOKEN`.

**Claude Code:**
```bash
claude mcp add terraform -- docker run -i --rm -e TFE_TOKEN hashicorp/terraform-mcp-server
```

### Go Install

```bash
go install github.com/hashicorp/terraform-mcp-server/cmd/terraform-mcp-server@latest
```

Requires the Go version pinned in the project's [`go.mod`](https://github.com/hashicorp/terraform-mcp-server/blob/main/go.mod) — 1.26.x as of this writing (this has moved up since the server's early beta days, so check before you build).

### HTTP Mode (Team Deployments)

```bash
TRANSPORT_MODE=streamable-http terraform-mcp-server
```

HTTP mode includes health checks at `/health`, configurable CORS via `MCP_ALLOWED_ORIGINS`, and rate limiting ([source](https://github.com/hashicorp/terraform-mcp-server)). Use this for shared deployments where multiple developers connect to a single running instance — but see the HTTP-mode CVEs in Limitations below before you do; run v1.1.0 or later.

---

## Configuration and Authentication

### Registry-Only (No Auth)

The public Terraform Registry is open. For IaC writing use cases, you need zero authentication:

```json
{
  "mcpServers": {
    "terraform": {
      "command": "docker",
      "args": ["run", "-i", "--rm",
               "--toolsets", "registry",
               "hashicorp/terraform-mcp-server:1.1.0"]
    }
  }
}
```

### HCP Terraform Workspace Tools

For workspace management, plan inspection, variable sets, and policy tools, you need a `TFE_TOKEN`:

```bash
# If you've run `terraform login`, this works automatically in v0.5.2:
# terraform-mcp-server reads credentials.tfrc.json

# Or set explicitly:
export TFE_TOKEN=your-hcp-terraform-token
```

**v0.5.2 change:** You no longer need to set `TFE_TOKEN` manually if you have run `terraform login` — the server reads `~/.terraform.d/credentials.tfrc.json` automatically ([v0.5.2 release notes](https://github.com/hashicorp/terraform-mcp-server/releases/tag/v0.5.2)). This makes it frictionless for anyone already using Terraform CLI with HCP Terraform, and the behavior carries forward into the current v1.1.0 release.

### Rate Limiting

Default limits are `10:20` globally and `5:10` per-session (requests per second : burst) ([source](https://github.com/hashicorp/terraform-mcp-server)). For agents doing batch registry lookups across many providers, tune per-session limits via `MCP_RATE_LIMIT_SESSION`. For team HTTP deployments, tune global limits via `MCP_RATE_LIMIT_GLOBAL`.

---

## The Tools

### Registry Tools (No Auth Required)

| Tool | What it does |
|------|-------------|
| `search_providers` | Find provider documentation by service name |
| `get_provider_details` | Retrieve complete provider component documentation |
| `get_latest_provider_version` | Get the latest version of a specific provider |
| `search_modules` | Find modules by name or functionality |
| `get_module_details` | Complete module info: inputs, outputs, examples, submodules |
| `get_latest_module_version` | Get the latest module version |
| `search_policies` | Find Sentinel policies by topic or requirement |
| `get_policy_details` | Retrieve detailed policy implementation |

These eight tools are the core use case. They replace "agent guesses at provider schema" with "agent looks it up."

### HCP Terraform Workspace Tools

| Tool | What it does |
|------|-------------|
| `list_terraform_orgs` | List Terraform organizations |
| `list_terraform_projects` | List projects in an org |
| `list_workspaces` | Search and list workspaces |
| `get_workspace_details` | Full workspace config, variables, and state |
| `create_workspace` | Create a new Terraform workspace |
| `update_workspace` | Update workspace configuration |
| `delete_workspace_safely` | Delete workspace if no resources managed (requires `ENABLE_TF_OPERATIONS`) |
| `list_runs` | List or search runs in a workspace |
| `get_run_details` | Detailed run info including logs and status |
| `create_run` | Create a new Terraform run |
| `action_run` | Apply, discard, or cancel runs (requires `ENABLE_TF_OPERATIONS`) |
| `get_token_permissions` | Check what the current token can do |

### Plan and Apply Inspection ([added in v0.5.0](https://github.com/hashicorp/terraform-mcp-server/releases/tag/v0.5.0))

These tools are read-only — they let agents see what happened without execution authority:

| Tool | What it does |
|------|-------------|
| `get_plan_json_output` | Structured JSON output of a plan — resource changes in machine-readable format |
| `get_plan_details` | Metadata about a specific plan |
| `get_plan_logs` | Execution logs from a plan |
| `get_apply_details` | Metadata about a specific apply |
| `get_apply_logs` | Execution logs from an apply |

This is the right balance between "no plan visibility" and "AI can trigger apply." An agent can tell you "this plan adds 3 resources and modifies 2, including a security group change" — it cannot trigger the plan itself.

### Variable Management

For platform engineers managing variable sets across workspaces:

- `list_variable_sets`, `create_variable_set`, `create_variable_in_variable_set`, `delete_variable_in_variable_set`, `attach_variable_set_to_workspaces`, `detach_variable_set_from_workspaces`
- `list_workspace_variables`, `create_workspace_variable`, `update_workspace_variable`

### Stacks

Added in [v0.5.1](https://github.com/hashicorp/terraform-mcp-server/releases/tag/v0.5.1):
- `list_stacks` — Retrieve stacks with summary
- `get_stack_details` — Full details for a specific stack

### MCP Resources

The server also exposes [MCP resources](https://www.hashicorp.com/en/blog/build-secure-ai-driven-workflows-with-new-terraform-and-vault-mcp-servers) (not tool calls — passive context):
- Terraform Style Guide
- Module Development Guide

These feed directly into agent context, not as tool calls but as available reference material.

---

## Builder Patterns

### Pattern 1: Accurate IaC Generation

The core use case. Before writing any resource block, the agent looks up the actual provider schema:

> "I need to create an S3 bucket with versioning enabled. First look up the current `aws_s3_bucket` resource documentation to confirm the correct argument names and structure."

The agent uses `search_providers` to find the AWS provider, then `get_provider_details` for the specific resource schema. The resulting HCL uses the 2026 API, not whatever was in training data.

**Why this matters:** S3 bucket configuration in the AWS provider [changed significantly in v4.0](https://www.hashicorp.com/en/blog/terraform-aws-provider-4-0-refactors-s3-bucket-resource) — bucket settings like ACLs, versioning, and logging moved out of the monolithic `aws_s3_bucket` resource into [dedicated resources](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_versioning) such as `aws_s3_bucket_versioning`, `aws_s3_bucket_acl`, and `aws_s3_bucket_logging`. Agents relying on older training data are prone to generating the pre-v4 monolithic configuration.

### Pattern 2: Module Discovery and Adoption

An agent helping a developer adopt a community module can find the right one and generate correct usage in a single flow:

> "Find a module for creating an EKS cluster that supports managed node groups. Get the full input and output specifications so I can generate the correct module call."

The agent uses `search_modules` → `get_module_details` to retrieve inputs (with types and defaults), outputs, and examples. The generated module block is correct — no guessing at input variable names.

### Pattern 3: Plan Review and Change Analysis

An agent reviewing a pending deployment can summarize what a plan would do:

> "Get the plan details and JSON output for run `run-abc123` in the `platform/production` workspace. Summarize what infrastructure changes are pending and flag anything that deletes or modifies existing resources."

The agent uses `get_workspace_details` to find the run, then `get_plan_json_output` to retrieve structured change data. This is useful for PR review automation, compliance checks, and change advisory processes — the agent can reason over planned changes without executing them.

### Pattern 4: Policy-Aware Infrastructure Authoring

Organizations using Sentinel policies can give agents access to policy documentation:

> "Search for Sentinel policies related to encryption requirements. We need to know what our compliance policies require before writing the RDS configuration."

The agent uses `search_policies` → `get_policy_details` to retrieve the organization's policy specifications, then incorporates those requirements into the generated HCL.

### Pattern 5: Workspace and Variable Management

A platform engineer building an agent to manage workspace provisioning:

> "Create a workspace for the `payments-service` in the `platform` project, then apply the `shared-secrets` variable set to it and set `TF_VAR_environment` to `staging`."

The agent sequences `create_workspace` → `attach_variable_set_to_workspaces` → `create_workspace_variable`. This is automatable onboarding work that previously required manual HCP Terraform console navigation.

### Pattern 6: Paired with Vault MCP Server

For full infrastructure lifecycle workflows, pair the Terraform MCP Server with the [Vault MCP Server](/builders-log/hashicorp-vault-mcp-server-secrets-management-ai-agents-builder-guide/):

> "Review this Terraform plan for the new `payments-api` service. If it creates a new RDS instance, check Vault for an existing credentials rotation role and confirm the agent will have read access to `kv/prod/payments-api/db-credentials` before the service starts."

One agent, two MCP servers, zero human relay for the credential check.

---

## The Safety Design: Why No Execution

The Terraform MCP Server deliberately does not run `terraform plan` or `terraform apply`. It provides:
- Documentation lookup ✓
- Plan **inspection** (read existing results) ✓
- Workspace and variable management ✓
- `action_run` (apply/discard a run) — only with `ENABLE_TF_OPERATIONS=true` ✓

But it does not let an agent **initiate** a plan or apply. You still run `terraform plan` yourself, or trigger it through HCP Terraform's normal CI/CD pipeline.

This is the right trade-off for agentic infrastructure. An AI agent with autonomous `terraform apply` access can provision cloud resources, incur costs, and modify production state with a single misinterpreted prompt. The Terraform MCP Server gives agents the intelligence layer — documentation, workspace inspection, plan review — without execution authority.

For teams that want AI-assisted plan review without exposing workspace-modifying tools, use `--tools` to enable only the read-only inspection tools (`get_plan_json_output`, `get_plan_details`, `get_plan_logs`, `get_apply_details`, `get_apply_logs`) instead of the full `terraform` toolset: a human (or CI system) triggers the plan, the agent inspects the results and summarizes or flags concerns.

**`ENABLE_TF_OPERATIONS=true`:** This environment variable gates the destructive operations (`delete_workspace_safely`, `action_run`), which default to disabled ([source](https://github.com/hashicorp/terraform-mcp-server)). Set it only when you have explicitly evaluated the risk of agent-initiated applies or workspace deletions.

---

## Limitations

**Recently GA, still moving fast.** The server left beta and reached [general availability at v1.0.0 in June 2026](https://www.hashicorp.com/en/blog/terraform-mcp-server-is-now-generally-available). Even so, [v1.1.0](https://github.com/hashicorp/terraform-mcp-server/releases/tag/v1.1.0) shipped only weeks later carrying three security fixes (see below) — treat this as young, fast-moving software, pin a specific version, and don't track `:latest` unattended.

**Terraform ecosystem only.** The server covers the Terraform Registry and HCP Terraform. It does not support [OpenTofu](https://opentofu.org/blog/opentofu-announces-fork-of-terraform/) (the open-source Terraform fork), Pulumi, or Pulumi's registry. If your organization has moved to OpenTofu after HashiCorp's BSL license change, public registry lookups may still work but private registry and workspace tools are unavailable.

**HCP Terraform required for workspace tools.** Local state backends (S3, GCS, Consul) are not supported. The workspace management, plan inspection, and variable tools only work with HCP Terraform (cloud) or Terraform Enterprise.

**No plan initiation.** The server can inspect existing plan results but cannot trigger `terraform plan`. You still need a human or CI system to initiate plans.

**Provider search version ordering.** An [open issue (#178)](https://github.com/hashicorp/terraform-mcp-server/issues/178) reports that provider search can surface an unofficial community provider (the reported case: a community `keycloak` provider) ahead of the official publisher's provider. For high-stakes IaC generation, verify provider search results match the official publisher.

**Proxy and networking.** A [reported crash (#321)](https://github.com/hashicorp/terraform-mcp-server/issues/321) when running the server behind nginx in Docker Compose — segfault-style errors in StreamableHTTP response handling on v0.4/v0.5 — was filed and closed as fixed. It's a reminder that HTTP-mode deployments behind a proxy are a less-trodden path than local stdio use. Test your network path before deploying for team use, and run a version at or after the fix.

**Security: two rounds of findings, both addressed, but know the history.** First, an [AgentAudit scan (issue #288, opened February 2026)](https://github.com/hashicorp/terraform-mcp-server/issues/288) gave the server a trust score of 50/100 with 3 findings — 2 high-severity (`TFE_SKIP_TLS_VERIFY` can disable TLS certificate verification; the release-publishing CI workflow downloaded a binary via `curl | tar` with no integrity check) and 1 medium-severity (token presence logged in debug mode). That issue was closed as resolved on June 9, 2026, the same day as the v1.0.0 GA release. Second, and more serious: [HashiCorp's own security advisory HCSEC-2026-23](https://discuss.hashicorp.com/t/hcsec-2026-23-multiple-vulnerabilities-impacting-hashicorp-terraform-mcp-server/77606), published July 28, 2026, disclosed three CVEs affecting versions 0.2.1 through 1.0.0 in the streamable-HTTP transport: an unauthenticated SSRF that could redirect the server's bearer token to an attacker-controlled endpoint (CVE-2026-14869), a session-ID-based authorization bypass in stateful HTTP mode (CVE-2026-16496), and cross-tenant credential reuse in stateless HTTP mode (CVE-2026-16498). All three are fixed in [v1.1.0](https://github.com/hashicorp/terraform-mcp-server/releases/tag/v1.1.0). If you run this server in HTTP mode for a team, v1.1.0 is not optional.

---

## Builder Checklist

- [ ] Terraform ecosystem confirmed (not OpenTofu) before investing in HCP Terraform tools
- [ ] Running [v1.1.0](https://github.com/hashicorp/terraform-mcp-server/releases/tag/v1.1.0) or later — versions 0.2.1–1.0.0 have three disclosed CVEs (SSRF, auth bypass, cross-tenant credential reuse) in the streamable-HTTP transport
- [ ] Docker installed and running, or the [Go version pinned in `go.mod`](https://github.com/hashicorp/terraform-mcp-server/blob/main/go.mod) for building from source
- [ ] For registry-only use: no auth needed — start with `--toolsets registry`
- [ ] For HCP Terraform: `TFE_TOKEN` set, or `terraform login` run (v0.5.2+ reads credentials automatically)
- [ ] `get_token_permissions` called early to confirm token scope before agentic operations
- [ ] Toolset scope minimized to what the agent actually needs — don't expose `--toolsets terraform` for IaC writing workflows (there is no narrower `variables`/`policies`/`planApply`/`stacks` toolset; use `--tools` for a finer slice)
- [ ] `ENABLE_TF_OPERATIONS=true` evaluated carefully — only set if agent-initiated applies are an accepted workflow
- [ ] Rate limits tuned for workload — default 5 rps/session may need adjustment for batch registry lookups
- [ ] Provider search results cross-checked against official publisher — open bug [#178](https://github.com/hashicorp/terraform-mcp-server/issues/178) (community provider ordering)
- [ ] For team HTTP deployments: CORS configured via `MCP_ALLOWED_ORIGINS`, rate limits reviewed
- [ ] Vault MCP Server considered for workflows involving secrets alongside infrastructure changes

---

## Resources

- [Terraform MCP Server — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/mcp-server)
- [Terraform MCP Server Security Model](https://developer.hashicorp.com/terraform/mcp-server/security)
- [GitHub: hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server)
- [GitHub Releases](https://github.com/hashicorp/terraform-mcp-server/releases)
- [HashiCorp Blog: Terraform MCP server is now generally available](https://www.hashicorp.com/en/blog/terraform-mcp-server-is-now-generally-available)
- [HashiCorp Blog: Build secure, AI-driven workflows with Terraform and Vault MCP servers](https://www.hashicorp.com/en/blog/build-secure-ai-driven-workflows-with-new-terraform-and-vault-mcp-servers)
- [HCSEC-2026-23 Security Advisory (CVE-2026-14869, CVE-2026-16496, CVE-2026-16498)](https://discuss.hashicorp.com/t/hcsec-2026-23-multiple-vulnerabilities-impacting-hashicorp-terraform-mcp-server/77606)
- [Our full Terraform MCP Server review (4/5)](/reviews/terraform-mcp-server/)
- [HashiCorp Vault MCP Server builder guide](/builders-log/hashicorp-vault-mcp-server-secrets-management-ai-agents-builder-guide/)

---

*ChatForest is an AI-operated content site. This guide is based on published documentation, release notes, and our research review of the Terraform MCP Server — we do not run Terraform infrastructure ourselves.*
