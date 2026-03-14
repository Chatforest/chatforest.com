---
title: "Best DevOps & Infrastructure MCP Servers in 2026"
date: 2026-03-14T08:32:19+09:00
description: "Docker vs Kubernetes vs Terraform vs AWS vs Azure DevOps — which DevOps MCP servers should your AI agent use? We compare containers, infrastructure as code, cloud management, and CI/CD with clear recommendations."
og_description: "Docker vs Kubernetes vs Terraform vs AWS vs Azure DevOps — which DevOps MCP server should your agent use? We compared them all."
content_type: "Comparison"
card_description: "Docker vs Kubernetes vs Terraform vs AWS vs Azure DevOps — five DevOps and infrastructure MCP servers compared head-to-head with clear recommendations."
---

DevOps is where MCP servers get serious. These aren't read-only tools querying documentation or fetching search results — they manage infrastructure, deploy containers, modify cloud resources, and trigger CI/CD pipelines. One bad tool call can take down production.

That risk is also why DevOps MCP servers add the most value. Infrastructure management involves remembering exact CLI flags, translating between YAML dialects, and context-switching between cloud consoles. An AI agent with direct access to your infrastructure APIs can handle the tedious parts while you focus on architecture decisions.

The category has matured fast. Docker, HashiCorp, AWS, Microsoft, Cloudflare, and the Kubernetes community all ship official MCP servers now. We've [reviewed the GitHub MCP server](/reviews/github-mcp-server/) (4.5/5) and [Cloudflare MCP server](/reviews/cloudflare-mcp-server/) (4.5/5). Here's how the rest of the DevOps landscape compares.

## The Contenders

| Server | Domain | Maintainer | Transport | Auth Model | Tools | Free Tier | Best For |
|--------|--------|------------|-----------|------------|-------|-----------|----------|
| [Cloudflare MCP](/reviews/cloudflare-mcp-server/) | Cloud infra | Cloudflare (official) | Remote (Streamable HTTP) | OAuth / API token | 2 (Code Mode) + 16 servers | Yes (Workers free) | Cloudflare platform management |
| Docker MCP | Containers | Docker (official) | Local (Desktop) | Docker Desktop | Catalog (300+) | Yes (Desktop) | Container management + MCP server discovery |
| Kubernetes MCP | Cluster mgmt | Red Hat / Community | Local (stdio) | kubeconfig | 15+ | Yes (any cluster) | Kubernetes operations |
| Terraform MCP | IaC | HashiCorp (official) | Both (stdio + HTTP) | HCP token | 15+ | Yes (registry) | Infrastructure as code |
| AWS MCP | Cloud infra | AWS Labs (official) | Local (stdio) | AWS credentials | 60+ | Yes (free tier) | AWS resource management |
| Azure DevOps MCP | DevOps platform | Microsoft (official) | Local + Remote (planned) | OAuth / PAT | 30+ | Yes (5 users) | Azure DevOps workflows |

**Also relevant:** Our [GitHub MCP server review](/reviews/github-mcp-server/) (4.5/5) covers Actions-based CI/CD, pull request automation, and repository management. GitHub's MCP server is the strongest CI/CD option in the ecosystem.

## Three DevOps Layers

DevOps MCP servers operate at different layers of the stack. Understanding which layer you need matters more than comparing tool counts.

### 1. Container & Orchestration (Docker, Kubernetes)

These servers manage the runtime environment — building images, running containers, managing pods, scaling deployments. Docker handles single-machine containers; Kubernetes handles cluster orchestration.

**When to use this layer:** You're debugging a failing container, scaling a deployment, checking pod logs, or managing Docker images. Your agent interacts with the runtime directly.

### 2. Infrastructure as Code (Terraform, AWS)

These servers manage the infrastructure itself — provisioning cloud resources, writing IaC configurations, querying provider documentation. Terraform works across clouds; AWS MCP is AWS-specific but deeper.

**When to use this layer:** You're provisioning new infrastructure, looking up Terraform provider docs, managing AWS resources, or writing IaC modules. Your agent helps you define and modify infrastructure declarations.

### 3. DevOps Platform (Azure DevOps, GitHub)

These servers manage the development workflow — work items, pipelines, pull requests, builds. They're the orchestration layer that ties code changes to deployments.

**When to use this layer:** You're managing sprints, triggering CI/CD pipelines, reviewing build failures, or coordinating releases. Your agent manages the software delivery process.

## The Servers in Detail

### Docker MCP — The Container & Discovery Platform

**[Docker MCP Catalog and Toolkit](https://www.docker.com/products/mcp-catalog-and-toolkit/)** | Official

Docker's MCP play is bigger than a single server — it's an entire ecosystem. The **MCP Catalog** hosts 300+ verified MCP server images on Docker Hub, each containerized, signed, and shipped with an SBOM. The **MCP Toolkit** is a management layer inside Docker Desktop that lets you browse, install, configure, and run MCP servers in sandboxed containers.

The standout feature is **Dynamic MCP**: AI agents can search the catalog and add new MCP servers mid-conversation. Instead of pre-configuring every tool, your agent discovers and installs the tools it needs on the fly. Each server runs in a container limited to 2GB memory with no host filesystem access by default.

For container management itself, Docker's MCP server handles image building, container lifecycle, network management, and volume operations — the standard Docker workflow exposed as MCP tools.

**Strengths:** 300+ verified server catalog, Dynamic MCP for on-demand tool discovery, containerized sandboxing (2GB memory limit, no host access), signed images with SBOMs, profile-based organization for different projects.

**Weaknesses:** Requires Docker Desktop (not available on servers/CI), catalog is a discovery layer rather than a deep management tool, Dynamic MCP adds setup latency, desktop-only means no headless automation.

**Best for:** Developers who use Docker Desktop and want a curated, secure way to discover and manage MCP servers alongside container operations.

### Kubernetes MCP — Cluster Operations via Natural Language

**[containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server)** | Red Hat / Community | Multiple implementations

The Kubernetes MCP ecosystem is fragmented — there are at least six implementations on GitHub. The most mature is Red Hat's `containers/kubernetes-mcp-server`, a Go binary that interacts directly with the Kubernetes API server (not just wrapping kubectl). Other notable options include `rohitg00/kubectl-mcp-server` (npm/pip installable), `Flux159/mcp-server-kubernetes`, and Microsoft's `Azure/mcp-kubernetes`.

Red Hat's implementation supports generic CRUD operations on any Kubernetes or OpenShift resource, pod management (list, get, delete, logs, exec), running container images, field selector filtering, and multi-cluster support via kubeconfig. A **read-only mode** prevents write operations — critical for safely connecting AI agents to production clusters.

The direct API interaction (rather than shelling out to kubectl) gives better performance and avoids the overhead of spawning processes for each operation.

**Strengths:** Native Go binary (fast, no runtime dependencies), direct K8s API interaction, multi-cluster support, read-only mode for safety, supports any K8s/OpenShift resource type, field selector filtering.

**Weaknesses:** Fragmented ecosystem (6+ competing implementations), no official CNCF or Kubernetes project server, Red Hat's server requires Go build or binary download, Helm/Istio/ArgoCD not included (see `alexei-led/k8s-mcp-server` for those), no remote transport option.

**Best for:** Platform engineers who want AI-assisted Kubernetes operations with safety controls. Use Red Hat's implementation for core K8s operations; use `k8s-mcp-server` if you also need Helm, Istio, or ArgoCD.

### Terraform MCP — Infrastructure as Code Intelligence

**[hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server)** | Official, Beta

HashiCorp's Terraform MCP server is focused on making AI agents write better Terraform configurations. Rather than managing infrastructure directly, it gives agents access to the Terraform Registry — provider documentation, module details, policy libraries, and workspace management.

The core tools let agents search provider documentation (so they generate correct resource blocks), find modules with inputs/outputs/examples, look up Sentinel policies for compliance, and manage HCP Terraform workspaces and variables. Version 0.4 added **Terraform Stacks** support (deploy and manage Stacks via natural language) and `attach_policy_set_to_workspaces` for governance workflows.

The server supports both stdio and StreamableHTTP transports, making it usable in local IDEs and remote setups. Auth uses HCP Terraform tokens for workspace operations; registry lookups are public and free.

**Strengths:** Deep Terraform Registry integration (providers, modules, policies), helps agents write correct IaC (not just guess), Stacks support for complex deployments, dual transport (stdio + HTTP), workspace and variable management, public registry access is free.

**Weaknesses:** Still beta, focused on documentation/registry (not direct infrastructure provisioning), requires HCP Terraform for workspace features, no `terraform plan/apply` execution (by design — too dangerous), limited to Terraform ecosystem (not OpenTofu, Pulumi, etc.).

**Best for:** Teams writing Terraform configurations who want AI agents that reference current provider docs and module specifications instead of hallucinating resource arguments.

### AWS MCP — The Cloud Infrastructure Suite

**[awslabs/mcp](https://github.com/awslabs/mcp)** | Official, Open Source

AWS doesn't ship one MCP server — it ships a suite of 60+ specialized servers covering the breadth of AWS services. The flagship is the **AWS MCP Server**, a managed remote server that provides authenticated access to most of the 15,000+ AWS APIs via a single `aws___call_aws` tool. Specialized servers cover CDK (infrastructure as code), CloudFormation, Lambda, ECS, S3, DynamoDB, Bedrock, CloudWatch, Cost Analysis, and more.

The **Cloud Control API MCP Server** deserves special mention — it provides natural language infrastructure management using AWS's unified API for creating, reading, updating, deleting, and listing any AWS resource that supports Cloud Control.

The **Knowledge MCP Server** indexes AWS documentation including What's New posts, Getting Started guides, Builder Center guidance, blog posts, architectural references, and Well-Architected framework guidance. This is the AWS equivalent of what Terraform MCP does for the HashiCorp registry.

**Strengths:** Broadest coverage of any MCP server suite (60+ servers), covers infrastructure, compute, data, AI/ML, security, cost analysis, and more, official AWS maintenance, Cloud Control API for unified resource management, free and open source.

**Weaknesses:** Overwhelming number of servers to choose from, each server has its own setup and auth requirements, stdio transport only (no remote hosting), requires existing AWS credentials and IAM configuration, AWS-specific (no multi-cloud).

**Best for:** Teams building on AWS who want AI agents with deep access to AWS services, documentation, and infrastructure management.

### Azure DevOps MCP — The DevOps Workflow Hub

**[microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp)** | Official, GA

Microsoft's Azure DevOps MCP Server connects AI agents to the Azure DevOps platform — work items, pull requests, builds, pipelines, test plans, and wikis. It reached General Availability in late 2025, making it one of the most mature DevOps MCP servers.

The GA release brought improved authentication (OAuth and PAT), domain-scoping for tool management, and refined internal APIs based on preview feedback. Azure DevOps MCP is now built into **Visual Studio 2026** out-of-the-box, meaning Azure users get MCP integration without any setup.

A **Remote MCP Server** is on the 2026 roadmap — a hosted version that eliminates the need to run a local server. The initial release will focus on core platform capabilities and work item management.

Microsoft also ships a separate **Azure MCP Server** for Azure cloud resources (compute, storage, databases, etc.), which is distinct from the DevOps server. Together, they cover both the development workflow and the cloud infrastructure.

**Strengths:** GA status (most mature in this comparison), built into Visual Studio 2026, covers work items, PRs, builds, pipelines, tests, and wikis, OAuth authentication, remote server coming in 2026, backed by Microsoft.

**Weaknesses:** Azure DevOps-specific (doesn't help GitHub/GitLab users), local-only transport currently, separate from Azure cloud resource management, enterprise-focused (less relevant for small teams or startups).

**Best for:** Teams using Azure DevOps for project management and CI/CD who want AI-assisted workflow management directly in their IDE.

## Feature Comparison

| Feature | Docker MCP | Kubernetes MCP | Terraform MCP | AWS MCP | Azure DevOps MCP |
|---------|-----------|----------------|---------------|---------|-----------------|
| Container mgmt | Deep | Via pods | No | Via ECS/EKS | No |
| Cluster ops | No | Deep | No | Via EKS | No |
| IaC | No | No | Deep | Via CDK/CFn | No |
| Cloud resources | No | No | No (registry only) | Deep (60+ servers) | Azure resources (separate server) |
| CI/CD | No | No | No | Via CodePipeline | Deep (pipelines + builds) |
| Work items | No | No | No | No | Deep |
| Documentation | Catalog | No | Registry docs | Knowledge server | Wiki |
| Auth model | Docker Desktop | kubeconfig | HCP token | AWS credentials | OAuth / PAT |
| Transport | Local | Local (stdio) | Both | Local (stdio) | Local (remote planned) |
| Status | GA | Active | Beta | Active | GA |
| Open source | Partial | Yes | Yes | Yes | Yes |

## How to Choose

**Start with your existing stack.** DevOps MCP servers are tightly coupled to their platforms. There's no point installing the Terraform MCP server if you use Pulumi, or the Azure DevOps server if you're on GitHub.

### Decision Flowchart

**"I write Terraform all day"** → **Terraform MCP**. Your agent references current provider docs instead of hallucinating resource arguments. Pair with AWS MCP or Azure MCP for direct resource management.

**"I manage Kubernetes clusters"** → **Kubernetes MCP** (Red Hat's `containers/kubernetes-mcp-server`). Start in read-only mode for safety. Add `k8s-mcp-server` if you need Helm and ArgoCD.

**"I'm all-in on AWS"** → **AWS MCP** suite. Start with the Knowledge server (documentation) and Cloud Control API (resource management). Add specialized servers as needed.

**"I use Azure DevOps for project management"** → **Azure DevOps MCP**. GA, built into VS 2026, covers the full DevOps workflow. Add Azure MCP Server for cloud resource management.

**"I want to discover and manage MCP servers themselves"** → **Docker MCP Toolkit**. The catalog and Dynamic MCP features are unique — no other tool lets agents discover and install MCP servers on the fly.

**"I need CI/CD automation"** → **[GitHub MCP Server](/reviews/github-mcp-server/)** (4.5/5). It's the strongest CI/CD option in the ecosystem, covering Actions workflows, build logs, and deployment management.

### The Stack We'd Recommend

Most DevOps teams need servers at **two layers**:

1. **An infrastructure server** — Terraform MCP (multi-cloud IaC), AWS MCP (AWS-specific), or Azure MCP (Azure-specific)
2. **A workflow server** — [GitHub MCP](/reviews/github-mcp-server/) (CI/CD + code), Azure DevOps MCP (enterprise DevOps), or Kubernetes MCP (cluster ops)

Add Docker MCP Toolkit if you want managed, sandboxed MCP server discovery. It's more of a meta-tool than a DevOps tool, but it solves a real problem — securely running MCP servers without trusting random npm packages.

## Safety Warning

DevOps MCP servers can modify production infrastructure. Before connecting any of these to a real environment:

1. **Use read-only modes** where available (Kubernetes MCP supports this)
2. **Scope credentials tightly** — least-privilege IAM roles for AWS, read-only PATs for Azure DevOps
3. **Start with non-production** — connect to staging clusters and dev accounts first
4. **Review before applying** — Terraform MCP deliberately doesn't run `terraform apply` for this reason

The most dangerous MCP server is one with broad write access to production infrastructure and no human review step. Don't be that team.

## The Bigger Picture

DevOps is the fastest-growing MCP server category. A year ago, none of these servers existed. Now every major platform has an official implementation, and AWS alone ships 60+ specialized servers.

The trend we're watching: **IaC servers are documentation-first, not execution-first.** Both Terraform MCP and AWS Knowledge MCP focus on helping agents *write correct configurations* rather than *executing changes directly*. This is a deliberate safety choice — the industry learned from early Copilot incidents that AI-generated infrastructure code needs human review before `apply`.

The exception is Kubernetes, where the community has built execution-capable servers with safety modes. This makes sense — Kubernetes operations (checking pod status, reading logs, scaling deployments) are often safe and time-sensitive. The read-only mode flag is the key innovation here.

For related tools, see our reviews of the [GitHub MCP server](/reviews/github-mcp-server/) (4.5/5) for CI/CD, and our comparison guides for [databases](/guides/best-database-mcp-servers/), [observability](/guides/best-observability-mcp-servers/), and [productivity](/guides/best-productivity-mcp-servers/).
