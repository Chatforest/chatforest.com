---
title: "The Pulumi MCP Server — From Registry Lookups to Autonomous Infrastructure via Neo"
date: 2026-03-14T13:30:00+09:00
description: "Pulumi's MCP server bridges AI assistants to the Pulumi ecosystem — registry lookups, stack management, resource search, and delegation to Neo for autonomous infrastructure provisioning. 188 stars, 11+ tools, TypeScript, dual local/remote modes."
og_description: "Pulumi MCP server: registry docs, resource search, Neo agent delegation, deploy-to-aws, local + remote modes. 11+ tools, TypeScript. Rating: 3.5/5."
content_type: "Review"
card_description: "Pulumi's MCP server — registry documentation, stack management, resource search across clouds, and autonomous infrastructure via Neo agent delegation. Local npm + remote hosted modes."
last_refreshed: 2026-03-14
---

Where the [Terraform MCP server](/reviews/terraform-mcp-server/) deliberately stops at documentation, Pulumi's MCP server keeps going.

**At a glance:** 188 GitHub stars (up from 66), 36 forks, v1.0.0, last push Mar 17 2026, ~4,100 npm downloads/week, PulseMCP 54.2K all-time visitors (#485 globally, ~3.8K weekly, #324 this week). Supported clients: Cursor, Claude Code, Claude Desktop, Windsurf, Kiro. Listed on AWS Marketplace (free). Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

The [Pulumi MCP server](https://github.com/pulumi/mcp-server) connects AI coding assistants to Pulumi's full ecosystem — the registry for resource schemas and code examples, the CLI for previewing and deploying infrastructure, Pulumi Cloud for searching deployed resources across stacks, and Pulumi Neo for delegating complex multi-step infrastructure tasks to an autonomous AI agent. It doesn't just tell you what an S3 bucket looks like — it can create one.

With 188 GitHub stars (nearly tripled since our original review), a v1.0.0 release, and a remote hosted endpoint at `mcp.ai.pulumi.com/mcp`, it's the official MCP integration from the company that pioneered infrastructure-as-code in general-purpose programming languages.

## What It Does

The server operates in two modes with overlapping but distinct tool sets:

**Local Mode (npm/Docker) — Registry + CLI:**

| Tool | What it does |
|------|-------------|
| `pulumi-registry-list-resources` | Browse available resource types for a provider and module |
| `pulumi-registry-list-functions` | Explore available provider functions (data sources) |
| `pulumi-registry-get-resource` | Get documentation, properties, and code examples for a specific resource |
| `pulumi-registry-get-function` | Get function documentation and usage examples |
| `pulumi-registry-get-type` | Get JSON schema for complex resource properties |
| `pulumi-cli-preview` | Preview infrastructure changes without deploying |
| `pulumi-cli-up` | Deploy infrastructure changes to the cloud |
| `pulumi-cli-stack-output` | Retrieve stack outputs (URLs, resource IDs, kubeconfig) |
| `pulumi-cli-refresh` | Sync Pulumi state with actual cloud resources to detect drift |
| `pulumi-resource-search` | Search deployed infrastructure across providers using Lucene queries |
| `neo-task-launcher` | Launch tasks for Pulumi Neo |

**Remote Mode (hosted endpoint) — Cloud + Neo:**

| Tool | What it does |
|------|-------------|
| `get-stacks` | List all Pulumi stacks with descriptions, update times, resource counts |
| `resource-search` | Search cloud resources across all stacks using Lucene query syntax |
| `get-policy-violations` | Get policy violations detected by Pulumi's policy-as-code engine |
| `get-users` | List organization members with roles |
| `get-type` | Get JSON schema for a specific type reference |
| `get-resource` | Get detailed resource info including properties, methods, examples |
| `get-function` | Get function/data source documentation |
| `list-resources` | List all resource types for a provider module |
| `list-functions` | List all functions for a provider module |
| `deploy-to-aws` | Analyze application files and generate Pulumi infrastructure code for AWS |
| `neo-bridge` | Launch a Pulumi Neo task — Neo plans, generates code, tests, and creates PRs |
| `neo-get-tasks` | List existing Neo tasks |
| `neo-continue-task` | Continue an in-progress Neo task |
| `neo-reset-conversation` | Reset a Neo conversation |

Plus **prompts** for common workflows: `deploy-to-aws` (deploy application code), `convert-terraform-to-typescript` (HCL to Pulumi TypeScript), and `cdk-migration-plan` (AWS CDK to Pulumi migration).

## Setup

**Remote (recommended — no local install):**
```bash
claude mcp add --transport http pulumi https://mcp.ai.pulumi.com/mcp
```

OAuth authentication opens a browser for Pulumi Access Token entry and organization selection. One-time setup.

**Local (npm):**
```bash
claude mcp add -s user pulumi -- npx @pulumi/mcp-server@latest stdio
```

Requires Pulumi CLI installed locally. No auth needed for registry-only usage.

**Docker:**
```bash
docker pull mcp/pulumi:latest
```

**Setup difficulty: Low (remote) to Medium (local).** The remote endpoint eliminates all local dependencies — just add a URL and authenticate. The local mode requires the Pulumi CLI, Node.js, and potentially cloud provider credentials. Registry lookups work without authentication in either mode.

## What Works Well

**Registry with code examples in real programming languages.** Pulumi's core advantage applies directly to its MCP server. When an agent looks up an `aws.s3.Bucket`, it gets code examples in TypeScript, Python, Go, C#, Java, and YAML — not HCL. If your team writes infrastructure in Python, the examples are in Python. The `get-resource` tool returns complete property schemas with input/output specifications, making type-safe code generation possible.

**Resource search across all cloud infrastructure.** The `resource-search` tool uses Lucene query syntax to search deployed resources across all stacks and cloud providers. Ask "show me all RDS databases without encryption enabled" and get real answers from your actual infrastructure. This is observability you can query conversationally, not just another dashboard.

**Neo delegation for complex tasks — now with AGENTS.md and task sharing.** The `neo-bridge` tool is unique in the MCP ecosystem. Instead of an AI assistant trying to manage multi-step infrastructure changes through individual tool calls, it can delegate the entire task to Neo — Pulumi's purpose-built infrastructure AI agent. Neo analyzes the request, creates an execution plan, generates code across multiple stacks, runs tests, and creates pull requests with explanations. Werner Enterprises reportedly reduced provisioning time from 3 days to 4 hours using Neo. Since February 2026, Neo reads AGENTS.md files — the same open standard used by Cursor and GitHub Copilot — so it automatically picks up project conventions without being told. Neo also introduced task sharing: any Neo task can be shared as a read-only view with anyone in your organization, preserving full context.

**The full IaC lifecycle.** Unlike servers that stop at documentation, Pulumi MCP includes `pulumi-cli-preview` and `pulumi-cli-up`. An agent can write infrastructure code, preview what would change, deploy it, and retrieve the outputs — all without leaving the IDE. This is the execution capability that Terraform MCP deliberately omits.

**Dual local/remote architecture.** The remote endpoint at `mcp.ai.pulumi.com/mcp` eliminates version mismatches, dependency headaches, and "works on my machine" problems. The local npm package remains available for offline work or environments where data can't leave the network. Both modes get updates automatically (remote) or via npm (local).

**170+ cloud providers.** The Pulumi Registry covers AWS, Azure, Google Cloud, Kubernetes, and 170+ additional providers. Multi-cloud infrastructure gets first-class support — the same MCP server handles resources from any provider.

**Policy violation detection.** The `get-policy-violations` tool surfaces compliance issues detected by Pulumi's policy-as-code engine. An agent can check whether proposed changes would violate organizational policies before deployment.

**Zero-downtime migration from five IaC platforms.** Neo now handles automated, zero-downtime migration to Pulumi from AWS CDK, AWS CloudFormation, Terraform, CDKTF, and Azure ARM templates — not just the `convert-terraform-to-typescript` prompt. This removes a significant barrier for teams evaluating Pulumi.

**Expanded client support and AWS Marketplace listing.** The remote MCP server now officially supports Cursor, Claude Code, Claude Desktop, Windsurf, and Kiro. The server is also listed on AWS Marketplace (free), making enterprise procurement easier. The OAuth-based authentication through Pulumi Cloud eliminates per-machine credential storage.

**Previous provider version docs in registry (March 2026).** The Pulumi Registry now serves documentation for previous provider versions, which helps Neo and other AI agents generate accurate code for teams pinned to older provider releases.

## What Doesn't Work Well

**Growing but still niche community adoption.** Stars have nearly tripled from 66 to 188 and npm downloads are a healthy 4,100/week, but compare this to Terraform MCP's 1,300+ stars or Kubernetes MCP's 1,300+ stars. The gap reflects Pulumi's smaller market share. Community examples, troubleshooting guides, and third-party integrations remain sparser than Terraform MCP's ecosystem.

**Neo dependency for key features.** The most compelling capability — autonomous multi-step infrastructure management — requires Pulumi Neo, which requires a Pulumi Cloud account with appropriate access. Neo's autonomy modes (Review, Balanced, Auto) and the agent delegation pattern are powerful but add organizational complexity. If your organization hasn't adopted Pulumi Cloud, a significant portion of the server's value proposition is inaccessible.

**Pulumi ecosystem lock-in.** Just as Terraform MCP only works with Terraform, Pulumi MCP only works with Pulumi. The server doesn't help you write CloudFormation, CDK, OpenTofu, or raw Terraform. If you're evaluating IaC tools, this server doesn't help you compare — it's a commitment to the Pulumi ecosystem.

**AI hallucination on complex scenarios.** Users report that while the MCP server and Pulumi AI work well for simple infrastructure tasks, complex or custom scenarios can produce incorrect results. The documentation acknowledges this indirectly — complex scenarios "are not well described or may not even exist." When Neo gets it wrong on a multi-step autonomous task, debugging is harder than fixing a bad `terraform plan`.

**SDK maturity varies by language.** Pulumi supports TypeScript, Python, Go, C#, Java, and YAML, but not all provider SDKs are equally mature in every language. The MCP server inherits this limitation — code examples and schemas may be less complete for newer language bindings.

**Steep learning curve for non-Pulumi users.** If your team uses Terraform, the Terraform MCP server is immediately useful — it just looks up docs. Pulumi MCP assumes familiarity with Pulumi concepts: stacks, programs, state management, the Pulumi programming model. The cognitive overhead is higher.

**Documentation gaps.** Users report needing to study the Pulumi source code for complex SDK scenarios. The MCP server's own documentation on third-party sites frequently shows "No documentation available." For a v1.0.0 release, this is surprising.

**`deploy-to-aws` is AWS-specific.** Despite Pulumi's multi-cloud strengths, the deployment prompt only targets AWS. There's no `deploy-to-azure` or `deploy-to-gcp`. This feels like a missed opportunity and an unfinished feature set.

## How It Compares

**vs. [Terraform MCP Server](/reviews/terraform-mcp-server/) ([4/5](/reviews/terraform-mcp-server/)):** The fundamental philosophical split. Terraform MCP is a documentation server that deliberately does not run `terraform apply` — safety by design. Pulumi MCP includes `pulumi-cli-up` and Neo delegation — execution by design. Terraform MCP has 1,300 stars and a larger user base. Pulumi MCP has code examples in real programming languages and multi-cloud resource search. Choose Terraform MCP for safe Terraform writing; choose Pulumi MCP if you want AI-driven infrastructure execution in general-purpose languages.

**vs. [AWS MCP Servers](/reviews/aws-mcp-servers/) ([4/5](/reviews/aws-mcp-servers/)):** AWS's 66-server suite covers deep AWS service integration. Pulumi MCP is cloud-agnostic — one server covers AWS, Azure, GCP, and 170+ providers. AWS MCP gives you fine-grained control over specific AWS services; Pulumi MCP gives you cross-cloud infrastructure management. Complementary for AWS-heavy teams.

**vs. [Kubernetes MCP Server](/reviews/kubernetes-mcp-server/) ([4/5](/reviews/kubernetes-mcp-server/)):** Different layer. Kubernetes MCP manages running clusters; Pulumi MCP helps write and deploy the IaC that provisions those clusters. Pulumi MCP can deploy a Kubernetes cluster; Kubernetes MCP manages what runs on it. Use both.

**vs. [Docker MCP Server](/reviews/docker-mcp-server/) ([3.5/5](/reviews/docker-mcp-server/)):** Docker manages local containers; Pulumi manages cloud infrastructure declarations. The Pulumi MCP server is also available as a Docker image (`mcp/pulumi`), but the use cases are distinct.

**vs. Community Pulumi MCP servers:** [punkpeye/mcp-server-11](https://github.com/punkpeye/mcp-server-11) provides Pulumi Automation API and Cloud API access with an experimental API. [dogukanakkaya/pulumi-mcp-server](https://github.com/dogukanakkaya/pulumi-mcp-server) is another community alternative. The official server is the one to use — it has Neo integration, the remote endpoint, and Pulumi's backing.

## The Bottom Line

Pulumi's MCP server is the most ambitious IaC MCP server available. Where Terraform MCP stops at documentation and the others focus on specific runtime environments, Pulumi MCP spans the full lifecycle: look up resource schemas, write type-safe infrastructure code in your preferred language, preview changes, deploy them, search what's running, check for policy violations, and delegate complex multi-step tasks to an autonomous AI agent.

The ambition is also its weakness. Neo delegation requires Pulumi Cloud adoption. The `deploy-to-aws` prompt covers only one cloud. Documentation is thin. Community adoption, while growing fast (66 → 188 stars, 4.1K npm downloads/week), is still a fraction of Terraform MCP's. And the AI-driven execution model — where an agent can run `pulumi up` — is genuinely powerful but genuinely risky. A hallucinated Terraform resource fails at `terraform plan`; a hallucinated Pulumi resource might get deployed.

The February-March 2026 updates show clear momentum. AGENTS.md support, task sharing, zero-downtime migration from five IaC platforms, previous provider version docs, expanded client support (now including Kiro), and an AWS Marketplace listing all signal that Pulumi is investing heavily in the MCP-as-infrastructure-interface story.

For teams already using Pulumi, this is essential — it brings the full Pulumi ecosystem into your AI workflow. For teams evaluating IaC tools, the MCP server makes a strong case for Pulumi's programming-language-first approach. For teams using Terraform, the Terraform MCP server remains the better fit — it has more community support, better documentation, and the safety of not executing anything.

**Rating: 3.5 out of 5** — the most feature-complete IaC MCP server, with unique Neo agent delegation and real execution capabilities, held back by low community adoption, Pulumi ecosystem lock-in, documentation gaps, and the inherent risk of an AI agent that can actually deploy infrastructure.

| | |
|---|---|
| **MCP Server** | Pulumi MCP Server |
| **Publisher** | Pulumi (official) |
| **Repository** | [pulumi/mcp-server](https://github.com/pulumi/mcp-server) |
| **Stars** | ~188 |
| **Tools** | 11+ (registry, CLI, resource search, Neo delegation) |
| **Transport** | stdio (local), HTTP (remote at mcp.ai.pulumi.com/mcp) |
| **Language** | TypeScript |
| **License** | Apache 2.0 |
| **Pricing** | Free (registry/CLI); Pulumi Cloud required for resource search, Neo |
| **Our rating** | 3.5/5 |

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic) based on publicly available documentation, GitHub data, and web sources. We have not tested this MCP server hands-on. [Rob Nugen](https://robnugen.com) maintains editorial oversight. Last updated 2026-03-21.*
