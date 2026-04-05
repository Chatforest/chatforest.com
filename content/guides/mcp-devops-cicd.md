---
title: "MCP for DevOps and CI/CD: AI Agents Meet Infrastructure Automation"
date: 2026-03-28T20:30:00+09:00
description: "A comprehensive guide to using MCP in DevOps workflows — covering Kubernetes, Terraform, CI/CD pipeline automation, GitHub Agentic Workflows, the AI agent gateway pattern, supply"
content_type: "Guide"
card_description: "MCP connects AI agents to your infrastructure. Here's how DevOps teams are using it for Kubernetes, Terraform, CI/CD, and incident response — plus the security risks you need to know."
last_refreshed: 2026-03-28
---

DevOps engineers spend significant time on repetitive infrastructure tasks: diagnosing pod crashes, writing Terraform configurations, triaging CI failures, and responding to incidents at 2 AM. MCP (Model Context Protocol) is changing this by giving AI agents structured access to the tools DevOps teams already use — kubectl, Terraform, GitHub Actions, cloud provider APIs, and monitoring systems.

The ecosystem has grown rapidly. There are now dedicated MCP servers for Kubernetes, Terraform, every major cloud provider, CI/CD platforms, and observability tools. GitHub shipped Agentic Workflows in February 2026, making AI agents a first-class part of CI/CD pipelines. HashiCorp released an official Terraform MCP server. And AWS, Azure, and GCP all have MCP integrations.

But giving an AI agent access to your infrastructure is fundamentally different from giving it access to a database or a file system. The blast radius of a bad `terraform apply` or a misconfigured Kubernetes deployment is production downtime. This guide covers what's available, how teams are using it, and where the real risks are. Our analysis draws on published documentation, security disclosures, and community project data — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## The DevOps MCP Server Landscape

The [awesome-devops-mcp-servers](https://github.com/rohitg00/awesome-devops-mcp-servers) repository catalogs 80+ MCP servers across DevOps categories. Here are the most significant ones by category.

### Infrastructure as Code

| Server | Maintainer | Language | Key Capability |
|--------|-----------|----------|---------------|
| [terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server) | HashiCorp (official) | Go | Registry docs, provider schemas, workspace management |
| [pulumi/mcp-server](https://github.com/pulumi/mcp-server) | Pulumi (official) | TypeScript | Automation API, multi-language IaC (TS/Python/Go) |
| [tfmcp](https://github.com/nwiizo/tfmcp) | Community | Rust | Local Terraform operations, plan/apply workflows |
| terraform-cloud-mcp | Community | Python | Terraform Cloud API, workspace CRUD |

**HashiCorp's official Terraform MCP server** is the most mature. It provides real-time access to Terraform Registry data — provider documentation, resource schemas, module interfaces, and configuration examples. Instead of an AI model relying on potentially outdated training data for Terraform syntax, it queries the live registry. The server also integrates with HCP Terraform and Terraform Enterprise for workspace management, variable handling, and run operations.

### Kubernetes and Containers

| Server | Maintainer | Language | Key Capability |
|--------|-----------|----------|---------------|
| [kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) | Red Hat | Go | Native K8s API, multi-cluster, OpenShift support |
| [kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server) | Community | TypeScript | Natural language cluster interaction |
| [k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server) | Community | Go | kubectl, helm, istioctl, argocd in Docker |
| [k8m](https://github.com/weibaohui/k8m) | Community | Go | Multi-cluster, 50+ tools, logging, metrics |
| [portainer-mcp](https://github.com/portainer/portainer-mcp) | Portainer | — | Container management interface |

Red Hat's [kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) stands out because it interacts directly with the Kubernetes API server rather than wrapping CLI commands. This means lower latency, native multi-cluster support, and CRUD operations on any Kubernetes resource type including custom resources. It ships as a single binary for Linux, macOS, and Windows.

### Cloud Providers

| Server | Maintainer | Coverage |
|--------|-----------|---------|
| [awslabs/mcp](https://github.com/awslabs/mcp) | AWS (official) | Lambda, ECS, EKS, S3, EC2, RDS |
| [Azure DevOps MCP](https://learn.microsoft.com/en-us/azure/devops/mcp-server/) | Microsoft (official) | Work items, PRs, builds, test plans, pipelines |
| gcp-mcp | Community | Compute Engine, Cloud Run, GKE |
| [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) | Cloudflare (official) | Workers, KV, R2, D1 |
| alibaba-cloud-ops-mcp-server | Alibaba (official) | ECS, monitoring |

The trend is clear: major cloud providers are releasing official MCP servers. AWS's official MCP server covers the most-used services and supports cost optimization analysis. Azure's integration connects to the full Azure DevOps suite. This official support matters for enterprise adoption — it means vetted security, maintained compatibility, and support channels.

### CI/CD Platforms

| Server | Platform | Capabilities |
|--------|---------|-------------|
| [github-mcp-server](https://github.com/github/github-mcp-server) | GitHub | Repos, issues, PRs, code review, Actions |
| [mcp-server-github-actions](https://github.com/Tiberriver256/mcp-server-github-actions) | GitHub Actions | Workflow triggers, run monitoring, log analysis |
| [server-gitlab](https://github.com/modelcontextprotocol/server-gitlab) | GitLab | Merge requests, pipelines, security scanning |
| Jenkins MCP | Jenkins | Build triggers, job status, log retrieval |
| [codemagic-mcp](https://github.com/stefanoamorelli/codemagic-mcp) | Codemagic | Mobile CI/CD pipeline management |

### Monitoring and Observability

| Server | What It Monitors |
|--------|-----------------|
| [prometheus-mcp-server](https://github.com/CaesarYangs/prometheus_mcp_server) | Time-series metrics, PromQL queries |
| Datadog MCP | Logs, monitors, traces |
| Grafana MCP | Dashboard generation, alerting |
| VictoriaMetrics MCP | Metrics at scale |
| Alertmanager MCP | Prometheus alert management |

For a broader look at MCP servers across all categories, see our [best MCP servers](/guides/best-mcp-servers/) roundup and category-specific guides for [DevOps](/guides/best-devops-mcp-servers/), [Kubernetes](/guides/best-kubernetes-container-mcp-servers/), and [observability](/guides/best-observability-mcp-servers/).

## GitHub Agentic Workflows: AI in CI/CD

GitHub shipped [Agentic Workflows](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/) in technical preview on February 13, 2026. This is the most significant development in AI-powered CI/CD so far — it makes AI agents a first-class part of the GitHub Actions ecosystem.

### How It Works

Instead of writing complex YAML, you define workflows in Markdown with YAML frontmatter:

```yaml
---
on:
  schedule: daily

permissions:
  contents: read
  issues: read
  pull-requests: read

safe-outputs:
  create-issue:
    title-prefix: "[repo status] "
    labels: [report]

tools:
  github:
---

# Daily Repo Status Report

Analyze all open issues and pull requests. Identify stale items
(no activity in 14+ days), failing CI checks, and PRs that need
review. Create a summary issue with findings and recommendations.
```

The `gh aw compile` command converts this Markdown into a standard GitHub Actions `.lock.yml` file. At runtime, a coding agent (GitHub Copilot, Claude Code, or OpenAI Codex) executes the natural language instructions within the defined constraints.

### Security Model

GitHub's security design is worth studying:

- **Read-only by default.** Workflows can read repository content but can't write unless explicitly allowed.
- **Safe outputs.** Write operations (creating issues, commenting on PRs) must be pre-approved in the frontmatter. The agent can only use approved output types.
- **Sandboxed execution.** Agents run in isolated containers with restricted network access.
- **No automatic merges.** Pull requests created by agentic workflows always require human review.
- **Guardrail checks.** Each run includes an automated guardrail verification step.

### Use Cases

GitHub identifies six "continuous" automation categories:

1. **Continuous triage** — auto-label and route new issues
2. **Continuous documentation** — keep READMEs aligned with code changes
3. **Continuous code simplification** — identify refactoring opportunities
4. **Continuous test improvement** — assess coverage gaps and add tests
5. **Continuous quality hygiene** — investigate CI failures and propose fixes
6. **Continuous reporting** — generate repository health summaries

This isn't a replacement for traditional CI/CD. You still write YAML for builds, tests, and deployments. Agentic Workflows handle the subjective, repetitive tasks that traditional CI/CD can't express — the kind of work that usually falls through the cracks or gets done inconsistently.

## The AI Agent Gateway Pattern

The most sophisticated approach to AI-driven infrastructure automation isn't giving agents direct access to your tools. It's the **agent gateway pattern**, documented in detail by [InfoQ](https://www.infoq.com/articles/building-ai-agent-gateway-mcp/).

### Architecture

```
Agent Request
    ↓
MCP Server Gateway (TypeScript)
  - Schema validation (Zod)
  - Identity extraction (JWT/mTLS)
  - Authorization delegation → OPA
    ↓
OPA Policy Engine (Rego)
  - RBAC: which agents can modify which environments
  - Integrity: plan hash verification
  - Safety: block destructive operations
  - Change windows: time-based restrictions
    ↓
Job Queue (never direct execution)
    ↓
Ephemeral Runner (Python)
  - Unique Kubernetes namespace per execution
  - Run Terraform/OpenTofu plan
  - Mandatory cleanup (even on failure)
    ↓
OpenTelemetry Observability
  - Policy decision traces
  - Execution audit logs
  - Cleanup verification
```

The key insight: **the gateway never executes infrastructure changes directly**. It validates, authorizes, and queues. Execution happens in ephemeral Kubernetes namespaces that are created for each job and destroyed afterward — even on failure.

### OPA Policy Examples

Authorization is defined in Rego, not application code:

```rego
# Which agents can modify which environments
allow_actor := {
    "sre-bot":    {"dev": true, "staging": true, "prod": true},
    "deploy-bot": {"dev": true, "staging": true}
}

# Block destructive operations
deny[msg] {
    endswith(input.plan, "-destroy.plan")
    msg := "Destructive plans are not allowed"
}

# Change window enforcement
deny[msg] {
    not is_business_hours
    msg := "Deployments only allowed Mon-Fri, 09:00-17:00 UTC"
}
```

This moves security policy out of code and into reviewable, testable, version-controlled policy files.

### Service Level Objectives

The reference implementation targets:
- Policy decisions: < 100ms
- Runner startup: < 2–5 seconds
- Sandbox cleanup: < 30 seconds
- Audit availability: < 5 minutes

For enterprise environments, the pattern scales to signed plan catalogs, Firecracker VM isolation, human approval gates for production changes, and geographic execution policies for data residency compliance.

## Three Deployment Models

How you deploy MCP servers for infrastructure access depends on your team size and security requirements.

### 1. Developer Laptop (Getting Started)

The simplest approach: run MCP servers locally alongside your AI assistant.

- Credentials from `~/.kube/config` and `~/.aws/credentials`
- Zero infrastructure overhead
- Good for individual exploration and learning

**Limitation:** Inconsistent configurations across team members. No audit trail. No access controls beyond what the developer already has.

### 2. Bastion Host (Team Use)

A centralized jump box running MCP servers that team members connect to via SSH.

- Unified audit logging
- Consistent RBAC configuration
- Single point for credential management

**Limitation:** Bastion maintenance overhead. SSH connection management. Still relatively simple security model.

### 3. Kubernetes Sidecar (Enterprise)

Per-team pods running MCP servers with Kubernetes-native security:

- Network policies restrict what each MCP server can reach
- Service accounts provide fine-grained RBAC
- Multi-tenant scaling with security boundaries
- Native integration with secrets management (Vault, AWS Secrets Manager)

**Limitation:** Requires Kubernetes expertise and infrastructure. More complex to set up and maintain.

For production use, the Kubernetes sidecar model combined with the agent gateway pattern provides the strongest security posture. See our [MCP enterprise infrastructure guide](/guides/mcp-enterprise-infrastructure/) and [credential management guide](/guides/mcp-credential-secret-management/) for deeper coverage of these patterns.

## Practical Use Cases

### Incident Response: The 2 AM Scenario

**Without MCP (25+ minutes):**
1. SSH into bastion host
2. Run `kubectl get pods` to find the problem
3. Check pod events, describe the deployment
4. Tail logs across multiple containers
5. Check resource limits and node pressure
6. Identify OOMKilled, update deployment manifest
7. Apply fix, monitor rollout

**With MCP (~45 seconds):**
> "Why is the checkout service crashing in production?"

The agent checks pod status, events, logs, resource limits, node pressure, and recent deployments. It identifies OOMKilled events, recommends increasing the memory limit from 256Mi to 512Mi, and can generate the patch — waiting for human approval before applying.

This isn't hypothetical. Kubernetes MCP servers like Red Hat's implementation include [specialized diagnostic prompts](https://developers.redhat.com/articles/2025/09/25/kubernetes-mcp-server-ai-powered-cluster-management) that guide systematic troubleshooting: identifying issues, collecting evidence, and suggesting remediation.

### Terraform Workflow Acceleration

Instead of context-switching to read Terraform documentation:

> "Create a new EKS cluster in us-west-2 with managed node groups, using the latest recommended AMI and the vpc module for networking"

With HashiCorp's official MCP server, the agent queries live registry data for current provider schemas, module interfaces, and recommended patterns. The generated configuration uses current syntax — not outdated patterns from training data.

### CI/CD Pipeline Debugging

> "The deploy workflow failed on the last 3 runs. What's the pattern?"

A GitHub Actions MCP server retrieves workflow run logs, identifies the common failure point, and suggests a fix. This replaces the manual process of clicking through GitHub's UI to compare log outputs across runs.

### Infrastructure Drift Detection

> "Compare what's in our Terraform state with what's actually running in AWS"

Combining Terraform MCP (for state data) with AWS MCP (for live infrastructure) lets agents identify drift without custom scripting.

## Security: The Risks Are Real

Connecting AI agents to infrastructure tools creates attack surfaces that traditional security models don't cover. The MCP ecosystem has already seen serious incidents.

### The GitHub MCP Prompt Injection Attack

In May 2025, researchers demonstrated a critical vulnerability in GitHub's MCP integration. The attack chain:

1. Attacker creates a malicious issue in a public repository
2. Developer's AI assistant reads the issue through the GitHub MCP server
3. Hidden instructions in the issue text prompt-inject the agent
4. The compromised agent uses its GitHub MCP access to read private repositories
5. Sensitive data is exfiltrated through crafted API calls

This attack worked because the agent had both read access to public issues (where the injection payload lived) and read access to private repositories (the target). The combination of permissions created the vulnerability — neither permission alone was dangerous.

### The mcp-remote Supply Chain Attack (CVE-2025-6514)

A critical OAuth vulnerability in `mcp-remote` — a widely-used MCP proxy package with nearly half a million users — enabled remote code execution. This was the first documented case of full system compromise through MCP infrastructure, turning a trusted development tool into an attack vector.

### The NeighborJack Vulnerability

Hundreds of MCP servers were found configured to bind to `0.0.0.0` by default, exposing them to the network. Combined with OS command injection vulnerabilities, this gave attackers complete control over host systems. For infrastructure MCP servers, this could mean access to Kubernetes clusters, cloud credentials, and CI/CD pipelines.

### Infrastructure-Specific Risks

| Risk | Scenario | Mitigation |
|------|---------|-----------|
| Credential exposure | Agent sends cloud keys through MCP transport | Use stdio transport for sensitive operations; never HTTP |
| Blast radius amplification | Agent with Terraform + cloud access can destroy infrastructure | Separate MCP servers per concern; least-privilege RBAC |
| Prompt injection → infrastructure change | Malicious content in monitored systems triggers agent actions | Human approval gates for write operations; OPA policies |
| Supply chain compromise | Malicious MCP server package installed | Pin versions; verify checksums; use official servers |
| Unauthorized escalation | Agent discovers and uses unintended tool combinations | Explicit tool allowlisting; no wildcard permissions |

### Security Best Practices for DevOps MCP

1. **Use stdio transport for infrastructure operations.** Network transports expose credentials. As one CISO put it: "I can explain a breach in my infrastructure to the board. I cannot explain why I gave our production keys to a startup."

2. **Implement least-privilege from day one.** Start with read-only access. Add write permissions only for specific, approved operations.

3. **Separate your MCP servers by concern.** Don't give one agent access to both your source code and your production infrastructure. Permission combinations create attack surfaces.

4. **Require human approval for destructive operations.** No `terraform destroy`, no `kubectl delete namespace`, no production deployments without a human in the loop.

5. **Log everything.** Every tool call, every argument, every result. Infrastructure MCP audit logs should feed into your existing SIEM.

6. **Pin MCP server versions.** Don't auto-update infrastructure tooling. Review changes before upgrading.

7. **Use official servers where available.** HashiCorp, AWS, Microsoft, Cloudflare, and GitHub all maintain official MCP servers. Prefer these over community alternatives for production use.

For comprehensive coverage of MCP security, see our [MCP server security guide](/guides/mcp-server-security/), [attack vectors and defense](/guides/mcp-attack-vectors-defense/), and [credential management guide](/guides/mcp-credential-secret-management/).

## Cicaddy: MCP Agents Inside CI Pipelines

[Cicaddy](https://developers.redhat.com/articles/2026/03/12/how-develop-agentic-workflows-ci-pipeline-cicaddy) is a Python framework from Red Hat that runs AI-driven tasks inside CI pipeline jobs with MCP server connectivity. Instead of AI agents triggering CI from outside, cicaddy puts agents inside the pipeline.

This inverts the typical pattern:

- **Typical:** AI agent → triggers CI/CD → waits for results
- **Cicaddy:** CI/CD pipeline → runs AI agent step → agent uses MCP tools → continues pipeline

Use cases include intelligent test selection (agent decides which tests to run based on changed files), deployment verification (agent checks health metrics after deploy), and incident auto-remediation within runbook-defined boundaries.

## Transport Considerations for DevOps

The choice of MCP transport protocol matters more for infrastructure than for other MCP use cases.

**stdio (recommended for production):**
- Credentials never cross the network
- No additional attack surface
- Works with local credential stores (`~/.kube/config`, `~/.aws/credentials`)
- Compatible with all MCP clients

**HTTP/SSE:**
- Required for remote/shared MCP servers
- Introduces network credential exposure
- Needs TLS, authentication, and rate limiting
- Useful for the bastion host or gateway patterns

**Streamable HTTP (MCP 2025-03-26 spec):**
- Modern replacement for SSE
- Better connection management
- Still requires the same network security controls

The general rule: use stdio for anything touching production infrastructure. Use HTTP transports only when you need shared, centralized access — and put a gateway in front of it.

For a deeper dive into transport protocols, see our [MCP transports guide](/guides/mcp-transports-explained/).

## What's Coming Next

The DevOps MCP ecosystem is evolving fast:

- **Multi-agent orchestration.** Coordinated agents managing Terraform, Kubernetes, and monitoring simultaneously. Early implementations exist but production patterns are still forming.
- **Centralized MCP gateways.** Enterprise-grade proxies with authentication, rate limiting, audit logging, and policy enforcement. [PolicyLayer's Intercept](https://github.com/PolicyLayer/Intercept) enforces YAML security policies on MCP traffic.
- **Execution policy layers.** Moving beyond tool-level permissions to workflow-level policies — "this agent can deploy to staging but not production, and only during business hours."
- **Signed artifact verification.** Extending the agent gateway pattern with cryptographic verification of infrastructure plans and configurations.
- **Kubernetes SIG exploration.** The Kubernetes community is actively evaluating MCP integration patterns for cluster management.

## Getting Started

If you're exploring MCP for DevOps, start small:

1. **Pick one tool.** Don't install 10 MCP servers at once. Start with the one you use most — probably kubectl or Terraform.
2. **Read-only first.** Configure your MCP server for read-only access. Get comfortable with the agent's behavior before enabling write operations.
3. **Use official servers.** HashiCorp's Terraform MCP, GitHub's MCP server, AWS's official MCP, and Red Hat's Kubernetes MCP are all maintained by the tool vendors.
4. **Local transport.** Start with stdio. Move to network transports only when you have a specific need.
5. **Log and review.** Check what your agent is doing. MCP tool calls should be visible and auditable.

For related guidance, see our guides on [building MCP clients](/guides/building-mcp-clients/), [MCP in production](/guides/mcp-in-production/), [Docker and containers](/guides/mcp-docker-containers/), [logging and observability](/guides/mcp-logging-observability/), and [gateway patterns](/guides/mcp-gateway-proxy-patterns/).

## Further Reading

- [What is MCP?](/guides/what-is-mcp/) — if you're new to the Model Context Protocol
- [Best DevOps MCP Servers](/guides/best-devops-mcp-servers/) — our curated list with ratings
- [Best Kubernetes MCP Servers](/guides/best-kubernetes-container-mcp-servers/) — container-focused picks
- [MCP Agent Workflow Patterns](/guides/mcp-agent-workflow-patterns/) — how agents coordinate multi-step tasks
- [MCP Authorization and OAuth](/guides/mcp-authorization-oauth/) — authentication patterns for MCP servers
- [MCP Enterprise Infrastructure](/guides/mcp-enterprise-infrastructure/) — scaling MCP for organizations
- [How to Build an AI Agent](/guides/how-to-build-ai-agent/) — fundamentals of agent architecture
- [Red Hat's MCP Ecosystem for RHEL](/guides/red-hat-mcp-server-rhel-lightspeed/) — read-only MCP servers for log analysis, vulnerability management, image building, and infrastructure health
