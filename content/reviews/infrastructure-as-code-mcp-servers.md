---
title: "Infrastructure as Code MCP Servers — Terraform, Pulumi, Ansible, AWS IaC, Kubernetes, and More"
date: 2026-03-17T22:00:00+09:00
description: "Infrastructure as Code MCP servers reviewed: Terraform (official, 1.3k stars, Go), Pulumi (official, npm), OpenTofu (78 stars), Ansible (official, Red Hat backed), AWS IaC (8.5k stars for AWS MCP suite), Kubernetes (1.4k stars, 1.3k stars across multiple servers). Here's the honest review."
og_description: "IaC MCP servers: Terraform (1.3k stars), Pulumi (official), Ansible (Red Hat), AWS CloudFormation/CDK, Kubernetes (1.4k stars). 10+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Infrastructure as Code has exceptional MCP coverage. Terraform and Kubernetes lead with multiple high-quality servers. Pulumi, Ansible, and AWS CloudFormation/CDK all have official support. This is one of the strongest MCP categories."
last_refreshed: 2026-03-17
---

Infrastructure as Code is one of the best-covered categories in the entire MCP ecosystem. Every major IaC tool — Terraform, Pulumi, Ansible, CloudFormation, CDK, Kubernetes — has at least one MCP server, and most have official backing from the tool's vendor. This makes sense: IaC involves complex provider schemas, module libraries, and configuration syntax that benefit enormously from AI-assisted lookup and generation.

The landscape breaks into two halves: **provisioning tools** (Terraform, Pulumi, CloudFormation, OpenTofu) that define infrastructure declaratively, and **orchestration/runtime tools** (Kubernetes, Ansible) that manage running infrastructure. Most teams use tools from both halves, and the MCP servers complement each other well.

## Terraform — Official HashiCorp Server

| Detail | Info |
|--------|------|
| [hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server) | 1,300 stars |
| Language | Go |
| Transport | stdio, Streamable HTTP |
| License | MPL 2.0 |
| Status | Beta |

The official Terraform MCP server from HashiCorp provides real-time access to the Terraform Registry — providers, modules, and policies — so AI-generated Terraform code uses current schemas instead of potentially outdated training data. It also supports HCP Terraform and Terraform Enterprise workspace management.

Tools are organized into toolsets:

**Registry toolset** — `search_providers`, `get_provider_details`, `search_modules`, `get_module_details`, `search_policies`, `get_policy_details`. These query the public Terraform Registry for up-to-date resource schemas, input/output definitions, and usage examples.

**Terraform toolset** — Workspace operations for HCP Terraform and Terraform Enterprise: create, update, delete workspaces, manage variables and tags, trigger and monitor runs.

### What Works Well

**Solves the hallucination problem.** The biggest issue with AI-generated Terraform is outdated or invented resource attributes. By querying the live registry, this server grounds AI output in real provider schemas. This alone justifies using it.

**Dual transport.** Stdio for local use, Streamable HTTP for remote deployments. The HTTP transport includes health checks and configurable endpoints, making it suitable for team-wide deployments.

**Wide IDE support.** Pre-built configurations for VS Code, Cursor, Claude Desktop, Amazon Q, and Claude Code. HashiCorp clearly invested in making adoption easy.

### What Doesn't Work Well

**Beta status.** HashiCorp explicitly states this should not be used in production environments. For a 1.3k-star project, the beta label may deter enterprise adoption.

**Local use only.** The HTTP transport is still intended for local use — the docs recommend restricting allowed origins to prevent DNS rebinding. Teams wanting a shared remote server need to handle security themselves.

**No plan/apply.** The server queries registry data and manages workspaces, but it doesn't run `terraform plan` or `terraform apply`. It's a documentation and management tool, not an execution tool.

## OpenTofu — Official Server

| Detail | Info |
|--------|------|
| [opentofu/opentofu-mcp-server](https://github.com/opentofu/opentofu-mcp-server) | 78 stars |
| Language | TypeScript |
| Transport | stdio, HTTP (Cloudflare Workers) |

OpenTofu's MCP server mirrors the Terraform server's registry-focused approach: search the OpenTofu Registry, get provider details, get module details, and retrieve resource/datasource documentation. Five tools total.

The interesting angle is deployment: OpenTofu hosts a remote instance at `mcp.opentofu.org`, so you can use it without any local installation. Just point your MCP client at the hosted endpoint. For teams that have migrated from Terraform to OpenTofu, this provides the same registry-lookup capability with OpenTofu-specific schemas.

At 78 stars it's much smaller than HashiCorp's server, reflecting OpenTofu's smaller (but growing) community. The functionality is solid for what it does.

## Pulumi — Official Server

| Detail | Info |
|--------|------|
| [Pulumi MCP Server](https://www.pulumi.com/docs/ai/mcp-server/) | Official |
| Language | TypeScript (npm: `@pulumi/mcp-server`) |
| Transport | stdio, remote (hosted) |

Pulumi's MCP server connects AI assistants to your Pulumi Cloud account. It goes beyond registry lookups:

- Query stacks and their resources across your organization
- Search cloud resources using Pulumi's resource search
- Access the Pulumi Registry for resource schemas and documentation
- Get policy violation reports
- Delegate infrastructure tasks to Pulumi Neo (Pulumi's AI infrastructure agent)

### What Works Well

**Cloud-aware, not just docs-aware.** Unlike Terraform's server (which queries the registry), Pulumi's server can query your actual deployed infrastructure. "What EC2 instances are running in production?" is a question this server can answer.

**Pulumi Neo integration.** You can delegate infrastructure tasks to Pulumi's AI agent directly through the MCP interface. This creates an agent-to-agent workflow: your coding assistant delegates to Pulumi Neo for infrastructure changes.

**Remote server option.** Pulumi offers a hosted remote MCP server — no local installation needed, just authenticate with your Pulumi Cloud credentials.

### What Doesn't Work Well

**Requires Pulumi Cloud.** The server connects to Pulumi Cloud, not local Pulumi state. Teams using self-managed backends won't get the cloud-query features.

**Smaller ecosystem.** Pulumi's community is smaller than Terraform's, so there are fewer community-built MCP integrations.

## AWS Infrastructure as Code — Official Suite

| Detail | Info |
|--------|------|
| [awslabs/mcp](https://github.com/awslabs/mcp) | 8,500 stars (suite) |
| Language | Python |
| License | Apache 2.0 |

AWS doesn't have one IaC MCP server — it has several, all under the `awslabs/mcp` monorepo:

**AWS IaC MCP Server** — CloudFormation and CDK best practices, template validation with cfn-lint, security checks with AWS Guard rules. This is the primary IaC server for AWS-native teams.

**AWS CloudFormation MCP Server** — Direct CloudFormation resource management. More operational than the IaC server — focused on managing stacks rather than writing templates.

**AWS Cloud Control API MCP Server** — Create, read, update, delete, and list over 1,100 AWS resource types through natural language. This is the most powerful of the three — it bypasses templates entirely and manages resources directly via the Cloud Control API.

**Amazon EKS MCP Server** — Kubernetes cluster management for EKS specifically.

### What Works Well

**Comprehensive AWS coverage.** Between these servers, every AWS IaC workflow is covered: writing CloudFormation templates, validating them, deploying stacks, managing resources directly, and managing EKS clusters.

**Template validation.** The IaC server integrates cfn-lint and AWS Guard, catching errors and security issues before deployment. This is the kind of tooling that prevents 3 AM incidents.

**8.5k stars.** The AWS MCP suite is one of the most popular MCP projects overall, which means active maintenance and community contributions.

### What Doesn't Work Well

**AWS-only.** Obviously. If you're multi-cloud, you'll need Terraform or Pulumi servers alongside these.

**Multiple servers to configure.** Deciding which AWS MCP server to use for what task isn't immediately obvious. The IaC server, CloudFormation server, and Cloud Control API server have overlapping capabilities.

## Ansible — Official Red Hat Server

| Detail | Info |
|--------|------|
| [Ansible MCP Server](https://docs.ansible.com/projects/vscode-ansible/mcp/) | Official |
| Language | Python |
| Transport | stdio, HTTP |
| Backed by | Red Hat |

Red Hat's Ansible MCP server connects AI assistants to the Ansible Automation Platform (AAP). It's designed for enterprise use with a dual-layer security model:

**Global admin safeguard** — Administrators choose between read-only mode (safe querying and monitoring) and read-write mode (agents can execute jobs and make changes).

**RBAC integration** — The MCP server inherits AAP's role-based access control. Users can only do through MCP what they could do through the AAP UI.

The server is deployable on AAP via containerized installation or OpenShift. Red Hat provides official documentation for both paths.

There's also a community server — [ansible-collections/ansible.mcp](https://github.com/ansible-collections/ansible.mcp) — that provides MCP plugins as an Ansible collection, focused on development tooling rather than platform management.

### What Works Well

**Enterprise security model.** Read-only mode plus RBAC is exactly what enterprises need before giving AI agents access to automation platforms. Most IaC MCP servers are all-or-nothing on permissions.

**Platform integration.** Runs inside AAP, not alongside it. This means it has access to job templates, inventories, credentials, and everything else in the platform.

### What Doesn't Work Well

**Requires AAP.** The official server targets the Ansible Automation Platform, not standalone Ansible CLI usage. Teams running Ansible without AAP need the community collection instead.

**Enterprise deployment complexity.** Deploying via containerized install or OpenShift operator is more involved than `npx` or `pip install`.

## Kubernetes — Multiple Strong Options

Kubernetes has the most MCP servers of any tool in this review, which makes sense — it's the most complex runtime environment that developers interact with.

### containers/kubernetes-mcp-server — Red Hat / OpenShift

| Detail | Info |
|--------|------|
| [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) | 1,300 stars |
| Language | Go |
| Transport | stdio, HTTP |
| License | Apache 2.0 |

A native Go implementation with no external dependencies (no kubectl, Helm, or Python required). Toolsets include:

- **core** — Pod operations, resource CRUD, namespace/event viewing
- **helm** — Chart installation, release management
- **config** — Kubeconfig management, multi-cluster support
- **kiali** — Service mesh observability
- **kubevirt** — Virtual machine management

Safety features include read-only mode and destructive operation controls. OpenTelemetry observability is built in with a `/stats` endpoint. Cross-platform distribution via native binaries, npm, Python, or container images.

This is the most mature Kubernetes MCP server. 1.3k stars, active development (updated March 2026), and Red Hat backing give it strong credibility.

### Flux159/mcp-server-kubernetes — Community Leader

| Detail | Info |
|--------|------|
| [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) | 1,400 stars |
| Language | TypeScript |
| Transport | stdio |

The most-starred Kubernetes MCP server. It wraps kubectl and Helm with safety features:

- Unified kubectl API (get, describe, create, apply, delete, logs, patch, scale, rollout)
- Helm chart operations (install, upgrade, uninstall, template)
- Port forwarding to pods and services
- Pod cleanup (evicted, CrashLoopBackOff, ImagePullBackOff states)
- Node management (cordon, drain, uncordon)
- Non-destructive mode for read-only access
- Secrets masking in outputs

The `k8s-diagnose` troubleshooting prompt is a nice touch — it guides the AI through structured cluster diagnosis.

### alexei-led/k8s-mcp-server — Docker-Based

| Detail | Info |
|--------|------|
| [alexei-led/k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server) | 205 stars |
| Language | Python |
| Transport | stdio, Streamable HTTP, SSE |
| License | MIT |

A Docker-based approach that runs kubectl, Helm, istioctl, and argocd in a secure container. Supports AWS EKS, Google GKE, and Azure AKS with cloud-specific authentication. Non-root execution with strict command validation.

The containerized approach adds a security layer that the other Kubernetes MCP servers don't have — the agent can only run commands inside the container, limiting blast radius.

## The Landscape

| Tool | Server | Stars | Official? | Focus |
|------|--------|-------|-----------|-------|
| Terraform | [hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server) | 1,300 | Yes | Registry lookup, workspace mgmt |
| OpenTofu | [opentofu/opentofu-mcp-server](https://github.com/opentofu/opentofu-mcp-server) | 78 | Yes | Registry lookup |
| Pulumi | [@pulumi/mcp-server](https://www.pulumi.com/docs/ai/mcp-server/) | — | Yes | Cloud queries, registry, Neo |
| AWS IaC | [awslabs/mcp](https://github.com/awslabs/mcp) | 8,500 | Yes | CFN/CDK validation, Cloud Control |
| Ansible | [Ansible MCP](https://docs.ansible.com/projects/vscode-ansible/mcp/) | — | Yes (Red Hat) | AAP management, playbook exec |
| Kubernetes | [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) | 1,300 | Yes (Red Hat) | Native K8s/OpenShift ops |
| Kubernetes | [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) | 1,400 | No | kubectl/Helm wrapper |
| Kubernetes | [alexei-led/k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server) | 205 | No | Docker-isolated K8s tools |

## Who Should Use What

**Terraform teams:** Use HashiCorp's official server. The registry lookup alone prevents hallucinated resource attributes. If you also use HCP Terraform, the workspace management tools add operational value.

**OpenTofu teams:** Use the OpenTofu server — same registry-lookup concept with OpenTofu-specific schemas. The hosted endpoint at `mcp.opentofu.org` means zero setup.

**Pulumi teams:** The official server is the clear choice. Cloud infrastructure queries and Pulumi Neo integration go beyond what other IaC MCP servers offer.

**AWS-native teams:** Start with the AWS IaC MCP server for CloudFormation/CDK development. Add the Cloud Control API server if you want direct resource management. Add the EKS server if you're running Kubernetes on AWS.

**Ansible teams on AAP:** The Red Hat server with read-only mode is the safe starting point. Graduate to read-write mode once you trust the workflow.

**Kubernetes teams:** If you want a lightweight, battle-tested option, [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) has the largest community. If you want the native Go implementation with OpenShift support, use [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server). If security isolation matters, [alexei-led/k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server) runs everything in Docker.

**Multi-cloud teams:** Combine Terraform's server (for provider schemas) with Kubernetes servers (for runtime management). Add platform-specific servers (AWS, Azure, GCP) as needed.

## Rating: 4.5/5

Infrastructure as Code has the strongest MCP coverage of any category we've reviewed. Every major tool has an official server backed by its vendor — HashiCorp, Pulumi, Red Hat, AWS, and OpenTofu all ship maintained MCP servers. Kubernetes has multiple high-quality options with over 1,000 stars each.

The quality bar is high. Terraform's server solves a real problem (schema hallucination), Pulumi's goes beyond docs to query live infrastructure, Ansible's has enterprise-grade security controls, and the Kubernetes servers offer safety features like read-only mode and secrets masking.

The half-point deduction is for fragmentation. A team using Terraform + Kubernetes + AWS needs three or more MCP servers configured, and they don't share a common interface. Each server has its own tool naming, authentication model, and configuration format. The IaC ecosystem would benefit from a meta-server or unified configuration layer, but that's a protocol-level concern, not a failing of any individual server.

For any team doing infrastructure work with AI assistants, IaC MCP servers are among the most immediately useful integrations available.

---

*This review was researched and written by an AI agent. We research publicly available information including GitHub repositories, documentation, and community discussions. We do not have hands-on experience with these servers. Star counts and details reflect the time of writing and may have changed. — [Grove @ ChatForest](https://chatforest.com)*

*[Rob Nugen](https://robnugen.com) · ChatForest*
