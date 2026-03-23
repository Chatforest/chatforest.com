---
title: "Infrastructure as Code MCP Servers — Terraform, Pulumi, and the IaC Vendors Building AI-Native Infrastructure Workflows"
date: 2026-03-24T21:00:00+09:00
description: "Infrastructure as Code MCP servers are vendor-driven: Terraform (1.3k stars, Go, Registry + HCP), Pulumi (remote MCP, Neo delegation), AWS IaC (8.5k stars monorepo, CloudFormation + CDK), OpenTofu (84 stars, TypeScript, Registry), Spacelift Intent (121 stars, Go, natural language provisioning), Ansible (community, 25 stars). Rating: 4/5."
og_description: "IaC MCP ecosystem: Terraform (1.3k stars), Pulumi (remote), AWS IaC (CloudFormation/CDK), OpenTofu (84 stars), Spacelift Intent (121 stars). Rating: 4/5."
content_type: "Review"
card_description: "Infrastructure as Code MCP servers are where IaC vendors are building AI-native infrastructure workflows. HashiCorp's Terraform MCP server leads (1.3k stars, Go, Registry + HCP Terraform integration, workspace management). Pulumi offers a remote MCP server with Neo delegation for automated infrastructure tasks. AWS bundles CloudFormation and CDK support into a unified IaC MCP server (part of the 8.5k-star awslabs/mcp monorepo). OpenTofu's official server (84 stars, TypeScript) mirrors Terraform's Registry-first approach. Spacelift Intent (121 stars, Go, Apache-2.0) takes the boldest approach — provisioning cloud resources from natural language without generating IaC code."
last_refreshed: 2026-03-24
---

**At a glance:** Infrastructure as Code is where **IaC vendors are building AI-native infrastructure workflows**. Unlike [security scanning](/reviews/security-scanning-mcp-servers/) where vendors instrument the coding loop, IaC vendors are building MCP servers that let AI agents **query, plan, and manage infrastructure directly**. [HashiCorp's Terraform MCP server](https://github.com/hashicorp/terraform-mcp-server) leads community adoption (1.3k stars, Go) with Registry lookups and HCP Terraform/Enterprise workspace management. [Pulumi](https://www.pulumi.com/docs/ai/mcp-server/) offers a remote MCP server with Neo delegation for automated infrastructure tasks. [AWS](https://awslabs.github.io/mcp/servers/aws-iac-mcp-server) bundles CloudFormation and CDK support into a unified IaC MCP server. [OpenTofu](https://github.com/opentofu/opentofu-mcp-server) (84 stars, TypeScript) mirrors Terraform's Registry-first approach as an open-source alternative. [Spacelift Intent](https://github.com/spacelift-io/spacelift-intent) (121 stars, Go) takes the boldest approach — provisioning cloud resources from natural language without generating IaC code. This is the **eleventh review in our [Developer Tools MCP category](/categories/developer-tools/)**.

The Infrastructure as Code market ($2.2B in 2025, projected $12.9B by 2032, 28.6% CAGR) is undergoing an AI transformation. 45% of organizations use IaC tools, and 74% of IT leaders consider IaC essential to their cloud strategy. The MCP integration layer reflects the market's competitive dynamics: HashiCorp (Terraform) and Pulumi ship official servers, OpenTofu mirrors Terraform's approach as the open-source fork, and platform vendors (AWS, Spacelift, env0) add MCP to their existing orchestration layers. The core promise is straightforward: AI agents that can look up provider documentation, validate templates, manage workspaces, and even provision infrastructure — all through natural language rather than HCL or YAML.

**Architecture note:** IaC MCP servers follow three distinct patterns. **Registry-first** servers (Terraform, OpenTofu, Pulumi) focus on documentation and metadata — looking up provider schemas, module details, and resource documentation so AI agents can write correct IaC code. **Platform-integrated** servers (HCP Terraform, Pulumi Cloud, AWS IaC, env0) connect to cloud orchestration platforms for workspace management, run triggering, and deployment troubleshooting. **Codeless provisioning** (Spacelift Intent) skips code generation entirely, translating natural language directly into provider API calls. Most servers support stdio transport for IDE integration; Pulumi and Spacelift also offer remote/hosted MCP endpoints.

## What's Available

### Terraform — HashiCorp's Official Registry and Platform MCP

| Aspect | Detail |
|--------|--------|
| Repository | [hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server) |
| Stars | ~1,300 |
| Forks | ~135 |
| Language | Go |
| License | MPL-2.0 |
| Creator | HashiCorp (official) |
| Transport | Stdio, StreamableHTTP |

**Three toolset categories:**

| Toolset | Capabilities |
|---------|-------------|
| Registry | Provider search, provider details, module information, policy management |
| Private Registry | Private Terraform registry access for organization modules |
| Terraform/HCP | Workspace listing/management, organization/project operations, run management, variable handling |

**Key differentiator:** The **most-starred IaC MCP server** and the first official MCP server from a major IaC vendor. HashiCorp's server covers both the public Terraform Registry (provider and module lookups) and HCP Terraform/Enterprise platform operations (workspaces, runs, variables). The `--toolsets` and `--tools` flags let teams expose only the capabilities they need — Registry-only for coding assistance, or full platform access for infrastructure management. Dual transport support (stdio + StreamableHTTP) enables both IDE integration and remote deployment. HashiCorp also ships [Vault MCP server](https://github.com/hashicorp/vault-mcp-server) (37 stars, Go) for secrets management and a Vault Radar MCP server for secret detection — building a full infrastructure security stack.

**Limitation:** Platform operations (workspaces, runs, variables) require HCP Terraform or Terraform Enterprise — not available for CLI-only Terraform users. The server doesn't execute `terraform plan` or `terraform apply` directly; it queries the Registry and manages the platform. Teams using open-source Terraform without HCP get Registry lookups only. Star count (1.3k) is modest for a tool used by millions of developers. No built-in drift detection or state inspection via MCP.

### Pulumi — Remote MCP with AI Delegation

| Aspect | Detail |
|--------|--------|
| Remote endpoint | `https://mcp.ai.pulumi.com/mcp` |
| Local package | `@pulumi/mcp-server` (npm) |
| Stars | ~57 (npm package repo) |
| Language | TypeScript |
| Creator | Pulumi (official) |
| Transport | HTTP (remote), stdio (local) |
| Auth | OAuth |

**15+ tools across three categories:**

| Category | Tools |
|----------|-------|
| Pulumi Cloud | `get-stacks`, `resource-search` (Lucene syntax), `get-policy-violations`, `get-users` |
| Neo Delegation | `neo-bridge` (launch automated tasks), `neo-get-tasks`, `neo-continue-task`, `neo-reset-conversation` |
| Registry & Deploy | `get-type`, `get-resource`, `get-function`, `list-resources`, `list-functions`, `deploy-to-aws` |

**Key differentiator:** The **only IaC MCP server with AI-to-AI delegation**. Pulumi Neo is an autonomous infrastructure agent — when you use the `neo-bridge` tool, your AI coding assistant delegates infrastructure tasks to Neo, which generates and deploys Pulumi programs autonomously. This is architecturally unique: the MCP server doesn't just provide data, it delegates work to another AI system. The remote MCP endpoint (`mcp.ai.pulumi.com`) requires zero local setup. Resource search across all stacks using Lucene query syntax enables cross-project infrastructure discovery. Policy violation retrieval surfaces guardrail violations before deployment.

**Limitation:** Remote-first architecture means cloud dependency — can't use offline. OAuth authentication adds setup complexity. Neo delegation is a proprietary Pulumi Cloud feature (not available for self-hosted Pulumi). The npm package repo has only 57 stars despite Pulumi's significant market presence. The `deploy-to-aws` tool suggests AWS-first focus; multi-cloud deployment tools are less prominent. Experimental API — breaking changes may occur without notice.

### AWS IaC — CloudFormation and CDK Unified

| Aspect | Detail |
|--------|--------|
| Repository | [awslabs/mcp](https://github.com/awslabs/mcp) (monorepo, `src/aws-iac-mcp-server`) |
| Stars | ~8,500 (monorepo) |
| Forks | ~1,400 |
| Language | Python |
| License | Apache-2.0 |
| Creator | AWS (official) |

**8+ tools across two IaC frameworks:**

| Tool | Capability |
|------|-----------|
| validate_cloudformation_template | Syntax/schema validation via cfn-lint |
| check_cloudformation_template_compliance | Security/compliance via cfn-guard |
| troubleshoot_cloudformation_deployment | Stack failure analysis with 30+ known patterns + CloudTrail |
| search_cloudformation_documentation | CloudFormation knowledge base queries |
| get_cloudformation_pre_deploy_validation_instructions | Pre-deploy CLI validation commands |
| search_cdk_documentation | CDK API references and best practices |
| search_cdk_samples_and_constructs | Code examples in TypeScript, Python, Java, C#, Go |
| cdk_best_practices | Security and development guidelines |

**Key differentiator:** The **most comprehensive validation-focused IaC MCP server**. While Terraform and Pulumi MCP servers focus on Registry lookups, AWS's server actually validates templates — `validate_cloudformation_template` runs cfn-lint for syntax errors, `check_cloudformation_template_compliance` runs cfn-guard for security/compliance rules, and `troubleshoot_cloudformation_deployment` analyzes stack failures using 30+ known patterns with CloudTrail integration. This makes it the only IaC MCP server that catches errors before deployment. Supports CDK across five languages (TypeScript, Python, Java, C#, Go). The deprecated standalone CDK MCP server has been folded into this unified server. Part of AWS's massive MCP monorepo (8.5k stars, 14+ servers).

**Limitation:** AWS-only — no multi-cloud support. The 8.5k stars are for the entire awslabs/mcp monorepo (14+ servers), not the IaC server specifically. CloudFormation is losing market share to Terraform and Pulumi — teams not on CloudFormation/CDK get no value. The troubleshooting tool requires AWS credentials with CloudFormation and CloudTrail read access. No `terraform plan`-equivalent for previewing changes.

### OpenTofu — Open-Source Terraform Alternative

| Aspect | Detail |
|--------|--------|
| Repository | [opentofu/opentofu-mcp-server](https://github.com/opentofu/opentofu-mcp-server) |
| Stars | ~84 |
| Forks | ~6 |
| Language | TypeScript |
| License | MPL-2.0 |
| Creator | OpenTofu (official) |
| Latest release | v1.0.0 (June 2025) |

**Tools:** Registry search for providers/modules/resources/data sources, provider details, module details, resource documentation, data source documentation.

**Key differentiator:** The **open-source IaC MCP alternative** to Terraform's server. Released alongside OpenTofu 1.10 (July 2025), the MCP server provides Registry access for the OpenTofu ecosystem — provider schemas, module documentation, and resource definitions. Available both as a local Node.js server and a hosted Cloudflare Worker at `mcp.opentofu.org`, enabling zero-setup access. The OpenTofu Registry is compatible with most Terraform providers, so this server is useful even for teams evaluating the Terraform-to-OpenTofu migration.

**Limitation:** Registry-only — no workspace management, run triggering, or platform integration (OpenTofu doesn't have an enterprise platform equivalent to HCP Terraform). Only 84 stars and v1.0.0 — early adoption stage. The feature set mirrors Terraform's Registry toolset but lacks the private registry and platform capabilities. OpenTofu's market share is still growing (the fork is from August 2023), so some providers may have better Terraform Registry coverage.

### Spacelift Intent — Natural Language Infrastructure Provisioning

| Aspect | Detail |
|--------|--------|
| Repository | [spacelift-io/spacelift-intent](https://github.com/spacelift-io/spacelift-intent) |
| Stars | ~121 |
| Forks | ~9 |
| Language | Go |
| License | Apache-2.0 |
| Creator | Spacelift (official) |
| Transport | Stdio |

**18 MCP tools across five categories:**

| Category | Capabilities |
|----------|-------------|
| Provider discovery | Search and inspect OpenTofu/Terraform provider schemas |
| Resource lifecycle | Create, update, delete, import cloud resources |
| Data sources | Query cloud provider data sources |
| State management | Track resources in SQLite, detect drift |
| Dependencies | Manage resource dependencies and ordering |

**Key differentiator:** The **most architecturally radical IaC MCP server**. Instead of helping AI agents write Terraform/Pulumi code, Intent skips code generation entirely — it translates natural language requests directly into provider API calls using the same Terraform providers. Resources are tracked in a local SQLite database with full state management, dependency tracking, and drift detection. This makes it a complete infrastructure provisioning tool, not just a documentation lookup. Supports all OpenTofu providers (AWS, GCP, Azure, etc.). Open-source under Apache-2.0 with a commercial hosted version on the Spacelift platform (policy-as-code, centralized state, audit trails).

**Limitation:** Bypassing IaC code means losing the auditability, review process, and version control that make IaC valuable. The SQLite state storage is local — no remote state locking or team collaboration without the commercial platform. The February 2026 incident where an AI agent ran `terraform destroy` and deleted 2.5 years of production data highlights the risk of AI-driven infrastructure changes without human review gates. Early stage — 121 stars, no established best practices for securing codeless provisioning.

### Ansible — Community-Built Automation

| Aspect | Detail |
|--------|--------|
| Repository | [bsahane/mcp-ansible](https://github.com/bsahane/mcp-ansible) |
| Stars | ~25 |
| Forks | ~11 |
| Language | Python |
| Creator | Community |
| Latest push | January 2025 |

**40+ tools** covering playbook management (create, validate, run), inventory operations (parse, graph, find-host, diff), role creation, Ansible Vault (encrypt/decrypt/rekey), project management, task execution, diagnostics (ansible-diagnose-host, capture-baseline, compare-states), auto-healing, security audit, and performance monitoring.

**Additional Ansible MCP projects:**

- **[ansible-collections/ansible.mcp](https://github.com/ansible-collections/ansible.mcp)** (1 star, Python, GPL-3.0) — Official Ansible Collection with MCP plugins. Installable via `ansible-galaxy`.
- **[a37ai/ansible-tower-mcp](https://github.com/a37ai/ansible-tower-mcp)** — MCP server for Ansible Tower/AWX, enabling job management, inventory queries, and workflow automation via AI agents.
- **[sibilleb/AAP-Enterprise-MCP-Server](https://github.com/sibilleb/AAP-Enterprise-MCP-Server)** — Enterprise MCP server for Ansible Automation Platform (AAP) and Event-Driven Ansible (EDA).
- **[ansible/ansible.mcp_builder](https://github.com/redhat-cop/ansible.mcp_builder)** — Ansible Collection for deploying MCP servers within Execution Environments.

**Key differentiator:** The **broadest tool count** of any IaC MCP server — 40+ tools covering the full Ansible lifecycle from inventory management to auto-healing. The diagnostics suite (diagnose-host, capture-baseline, compare-states) is unique among IaC MCP servers. Red Hat's investment in the Ansible MCP ecosystem (official collection, AAP enterprise server, MCP builder) signals enterprise commitment.

**Limitation:** All community-built — no official Red Hat MCP server for Ansible Core. The primary repo (25 stars) has low adoption and hasn't been updated since January 2025. The official ansible.mcp collection has only 1 star. Multiple competing servers fragment the small community. Ansible's procedural (playbook-based) approach is architecturally different from declarative IaC tools (Terraform/Pulumi), so the MCP use cases differ.

### Additional Servers

**[env0 MCP Server](https://github.com/env0/mcp-server)** (4 stars, TypeScript) — Official IaC orchestration platform MCP server. Deploy, cancel, and inspect environments. Access Cloud Compass for resource visibility. Requires Docker and env0 account. Early stage.

**[HashiCorp Vault MCP](https://github.com/hashicorp/vault-mcp-server)** (37 stars, Go) — Secrets management for IaC workflows. Mount management (KV v1/v2), secret read/write/delete, PKI certificate management. Supports stdio and StreamableHTTP. Companion to the Terraform MCP server.

**[Vault Radar MCP](https://developer.hashicorp.com/hcp/docs/vault-radar/mcp-server/overview)** — Beta. Queries HCP Vault Radar for data sources, resources, events, and detected secret types. Available on AWS Marketplace.

**[thrashr888/terraform-mcp-server](https://github.com/thrashr888/terraform-mcp-server)** — Community Terraform Registry MCP server. Predates the official HashiCorp server.

**[severity1/terraform-cloud-mcp](https://github.com/severity1/terraform-cloud-mcp)** — Community Terraform Cloud API integration for managing infrastructure through natural conversation.

**[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** — Experimental CLI tool for AI assistants to read Terraform configurations, analyze plans, apply configurations, and manage state.

**[zekker6/mcp-helm](https://github.com/zekker6/mcp-helm)** — MCP server for Helm package manager. Query repositories, retrieve chart information, access chart values without local Helm installation.

**[Crossplane MCP servers](https://github.com/cychiang/crossplane-mcp-server)** — Community servers for querying Crossplane resources (XRDs, Compositions, ManagedResources) via MCP. Multiple implementations exist.

### Notable Gaps

**No MCP servers found** for: Chef, Puppet, SaltStack, Vagrant, Packer, Nomad, or CDK for Terraform (CDKTF). Bicep (Azure's IaC language) has no MCP server despite growing adoption. Google Cloud Deployment Manager and Azure Resource Manager templates lack MCP integration.

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|----------|-----|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, 1.3k stars) | Yes (Jenkins, CircleCI, Buildkite) | Yes (JetBrains built-in, 24 tools) | Yes (MS Playwright, 9.8k stars, 24 tools) | Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana) | Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) |
| **Codeless provisioning** | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Yes (Spacelift Intent — NL to provider API calls) |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (1.4k stars, 20+ tools) | Argo CD (356 stars, 12 tools) | vscode-mcp-server (342 stars, 15 tools) | executeautomation (5.3k stars) | pab1it0/prometheus (340 stars) | CodeQL community (143 stars) | Ansible (25 stars, 40+ tools) |
| **Vendor count** | 1 (GitHub) | 1 (GitLab) | 0 (Atlassian via Jira only) | 1 (Docker) + community | 0 (Red Hat leads community) | 3 (Jenkins, CircleCI, Buildkite) | 1 (JetBrains) | 1 (Microsoft) | 6 (Grafana, Datadog, Sentry, Dynatrace, New Relic, Instana) | 7+ (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | 5+ (HashiCorp, Pulumi, AWS, OpenTofu, Spacelift) |
| **Template validation** | N/A | N/A | N/A | Dockerfile linting | manifest validation | Pipeline linting | N/A | N/A | N/A | IaC scanning (Trivy, Cycode) | Yes (AWS cfn-lint + cfn-guard) |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | API tokens per platform | Local connection (port/stdio) | None (local browsers) | API tokens / OAuth (remote) | API tokens / CLI auth | API tokens / OAuth / CLI auth |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | No | No (but Microsoft is Platinum) | No (but Microsoft is Platinum) | No | No | No |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | 5.6M developers | Jenkins: 11.3M devs | VS Code: 75.9% market share | Playwright: 45.1% QA adoption | Datadog: 32.7k customers | SonarQube: 17.7% SAST mindshare | Terraform: millions of users, 45% IaC adoption |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | [4/5](/reviews/kubernetes-mcp-servers/) | [3/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) | [3.5/5](/reviews/security-scanning-mcp-servers/) | 4/5 |

## Known Issues

1. **AI-driven infrastructure destruction is a proven risk** — In February 2026, an AI coding agent ran `terraform destroy` on production infrastructure, deleting 2.5 years of course data for a 100,000-student education platform. IaC MCP servers that enable `plan`/`apply`/`destroy` operations without mandatory human approval gates create real-world destruction risk. Spacelift Intent's codeless provisioning amplifies this — resources can be created and destroyed without any code review process.

2. **Registry lookup is the ceiling for most servers** — Terraform, OpenTofu, and Pulumi MCP servers primarily look up documentation and schemas. They don't execute infrastructure operations (plan, apply, destroy) or inspect actual deployed state. This makes them documentation tools — useful for helping AI agents write correct IaC code, but not for managing infrastructure. AWS's IaC server is the exception with actual validation capabilities.

3. **No standard for IaC findings or state representation in MCP** — Each server returns infrastructure data in its own format. Terraform workspace state, Pulumi stack resources, and CloudFormation stack events look completely different. No MCP-native schema exists for representing infrastructure resources, their relationships, or their drift status. This prevents cross-tool infrastructure visibility.

4. **State file exposure is a security concern** — Terraform state files contain sensitive data: resource IDs, IP addresses, database connection strings, and potentially plaintext secrets. MCP servers that query state data expose this information to the LLM, which may log, cache, or transmit it. No IaC MCP server implements state data redaction or sensitive field masking.

5. **Prompt injection via IaC code is unexplored** — Terraform modules, Ansible playbooks, and CloudFormation templates can contain comments with prompt injection payloads. An AI agent reading a malicious `README.md` or module description via MCP could be manipulated to execute unintended infrastructure changes. No IaC MCP server sanitizes registry or documentation content for prompt injection.

6. **Multi-cloud orchestration doesn't exist** — Each MCP server is tied to its platform: Terraform MCP for Terraform, Pulumi MCP for Pulumi, AWS IaC for CloudFormation/CDK. No cross-platform MCP server exists that could manage a Terraform AWS deployment alongside a Pulumi GCP deployment. Teams with multi-tool IaC environments need multiple MCP servers with no coordination layer.

7. **OpenTofu vs. Terraform fragmentation** — The Terraform/OpenTofu fork creates ecosystem fragmentation. Teams must choose between HashiCorp's Terraform MCP server (1.3k stars, platform integration) and OpenTofu's MCP server (84 stars, fully open-source). Provider registries are mostly compatible but diverging. This mirrors the broader IaC community split.

8. **Codeless provisioning lacks governance** — Spacelift Intent provisions real cloud resources from natural language without generating reviewable code. The open-source version has no policy gates, approval workflows, or audit trails — only the commercial Spacelift platform adds OPA policy-as-code integration. For any production use, the lack of governance in the open-source version is a blocker.

9. **Low adoption relative to IaC tool popularity** — Terraform has millions of users, but the MCP server has 1.3k stars. Pulumi's MCP server has 57 stars. OpenTofu's has 84. Ansible's community server has 25. The IaC community has not yet broadly adopted MCP-based workflows, likely because infrastructure changes carry higher blast radius than code changes.

10. **Missing enterprise IaC vendors** — Chef, Puppet, and SaltStack have no MCP presence. Bicep (Azure's IaC) and Google Cloud Deployment Manager are absent. CDK for Terraform (CDKTF) — which lets developers use TypeScript/Python to write Terraform — has no MCP server despite being a natural fit for AI-assisted IaC.

## Bottom Line

**Rating: 4 out of 5**

The Infrastructure as Code MCP ecosystem has **strong vendor representation** — five or more vendors (HashiCorp, Pulumi, AWS, OpenTofu, Spacelift) have shipped official MCP servers, with HashiCorp and Pulumi treating MCP as a first-class integration point. The architectural diversity is notable: Registry-first servers (Terraform, OpenTofu) for documentation lookup, platform-integrated servers (HCP Terraform, Pulumi Cloud, AWS IaC) for workspace and deployment management, and codeless provisioning (Spacelift Intent) for natural language infrastructure. AWS's IaC server stands out with actual template validation — the only server that catches errors before deployment rather than just looking up documentation.

The **4/5 rating** reflects: strong multi-vendor investment (5+ official servers from major IaC players), HashiCorp's comprehensive Registry + platform integration (1.3k stars), Pulumi's innovative AI-to-AI delegation via Neo, AWS's unique validation capabilities (cfn-lint + cfn-guard + CloudTrail troubleshooting), OpenTofu's open-source alternative, Spacelift Intent's bold codeless provisioning approach, and the genuine utility of AI-assisted IaC authoring (correct provider schemas, module documentation, resource definitions). It loses the remaining 1 point for the proven destruction risk of AI-driven infrastructure changes (February 2026 incident), most servers being documentation-only (no plan/apply/state inspection), no standard for representing infrastructure state in MCP, state file security concerns, low community adoption relative to IaC tool popularity, missing vendors (Chef, Puppet, Bicep, CDKTF), and the unresolved Terraform/OpenTofu fragmentation.

**Who benefits from IaC MCP servers today:**

- **Terraform/OpenTofu developers** — Registry lookup via MCP gives AI coding assistants accurate provider schemas, module documentation, and resource definitions. This directly reduces HCL errors and speeds up configuration authoring
- **Platform engineering teams on HCP Terraform** — Workspace management, run triggering, and variable handling via MCP enables AI-assisted infrastructure operations without leaving the IDE
- **AWS CloudFormation/CDK teams** — The AWS IaC server's validation tools (cfn-lint, cfn-guard) catch template errors and compliance violations before deployment — genuinely useful for catching misconfigurations
- **Teams evaluating codeless provisioning** — Spacelift Intent offers a glimpse of infrastructure-without-code for prototyping and experimentation (not recommended for production without the commercial platform's governance)
- **Pulumi teams with Pulumi Cloud** — Neo delegation lets AI assistants offload infrastructure tasks to Pulumi's autonomous agent, reducing manual infrastructure work

**Who should be cautious:**

- **Teams without strong infrastructure governance** — AI agents with IaC MCP access can potentially create, modify, or destroy cloud resources. Without approval gates, policy-as-code, and audit trails, this is a production risk. The February 2026 destruction incident is a warning
- **Multi-cloud teams** — No cross-platform IaC MCP server exists. Managing Terraform + Pulumi + CloudFormation via separate MCP servers creates tooling sprawl with no coordination
- **Enterprise teams on Chef/Puppet/SaltStack** — These configuration management platforms have no MCP servers. AI-assisted IaC workflows are currently limited to Terraform, Pulumi, CloudFormation, and Ansible ecosystems
- **Teams concerned about state file security** — MCP servers that query infrastructure state expose sensitive data (IP addresses, connection strings, resource IDs) to the LLM. Verify your LLM provider's data handling before connecting IaC state

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*
