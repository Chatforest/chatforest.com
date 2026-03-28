---
title: "CI/CD Platform MCP Servers: How GitHub, GitLab, Jenkins, CircleCI, and Argo CD Connect to AI Agents"
date: 2026-03-29T18:00:00+09:00
description: "A deep dive into MCP integrations for every major CI/CD platform — covering GitHub Actions, GitLab CI, Jenkins, CircleCI, Argo CD, Tekton, Azure DevOps, Harness, and CloudBees with tool inventories, setup patterns, AI code review workflows, AI-powered testing, OWASP MCP Top 10 risks, and real incident case studies."
content_type: "Guide"
card_description: "Every major CI/CD platform now has an MCP server. This guide covers platform-specific tool inventories, setup patterns, AI code review and testing workflows, security risks from the OWASP MCP Top 10, and real-world incident case studies."
last_refreshed: 2026-03-29
---

Every major CI/CD platform now has an MCP server — either official or community-maintained. GitHub's has 26,400+ stars. GitLab built theirs into the platform itself. Jenkins, CircleCI, Argo CD, Tekton, Azure DevOps, Harness, and CloudBees all ship dedicated MCP integrations.

This means AI agents can now monitor builds, analyze test failures, trigger deployments, review pull requests, detect flaky tests, and roll back releases — all through standardized MCP tool calls instead of custom API integrations.

But the implementations differ significantly. Some platforms expose nine tools, others expose sixty. Some require OAuth 2.1, others work with a simple API token. Some run as standalone servers, others embed directly into the CI pipeline. This guide covers each platform's MCP integration in detail — what tools are available, how to set them up, how they handle security, and what workflows they enable.

For a broader overview of MCP in DevOps including infrastructure-as-code, Kubernetes, cloud providers, and the agent gateway architecture pattern, see our [MCP for DevOps and CI/CD guide](/guides/mcp-devops-cicd/). Our analysis draws on published documentation, open-source implementations, and vendor announcements — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## Platform-by-Platform Deep Dive

### GitHub Actions — The 26K-Star Ecosystem

GitHub's MCP integration is the largest and most mature, spanning an official MCP server, a dedicated CI/CD action, and a new agentic workflows system.

**Official GitHub MCP Server** ([github/github-mcp-server](https://github.com/github/github-mcp-server)) — 26,400+ stars. Released April 2025, became generally available as a remote server in September 2025. This is the most-used CI/CD-adjacent MCP server.

CI/CD-relevant tools:
- **Workflow intelligence:** Monitor GitHub Actions runs, analyze build failures, view workflow logs
- **Code review:** Create and manage pull requests, post review comments, request reviewers
- **Repository management:** Branch operations, file CRUD, commit history
- **Security:** Dependabot alerts, code scanning results
- **Project management:** Issues, labels, milestones, Projects (added January 2026)

The January 2026 update added OAuth scope filtering (restrict which tools are available per connection), consolidated Projects toolset, native Streamable HTTP support, and **Lockdown mode** — a security feature that blocks content from untrusted contributors in public repositories, specifically designed to prevent prompt injection attacks through issues and PRs.

**Claude Code Action** ([anthropics/claude-code-action](https://github.com/marketplace/actions/claude-code-action-official)) — runs Claude Code as a GitHub Actions agent. Launched with Claude Code 2.0 in September 2025. Two modes:

- **Interactive mode:** Responds to `@claude` mentions in PR comments and issues. The agent reads the context, analyzes code, and posts responses.
- **Automation mode:** Runs headlessly on every matching event (PR open, push, issue creation). Prompt is defined directly in workflow YAML.

```yaml
# Example: AI code review on every PR
name: AI Code Review
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          prompt: |
            Review this PR for logic errors, security vulnerabilities,
            broken edge cases, and regressions. Post findings as
            inline comments on specific lines.
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

Claude Code Action uses a fleet of specialized agents that examine logic errors, security vulnerabilities, broken edge cases, and subtle regressions. It has 5+ documented copy-paste workflow recipes for common CI/CD scenarios.

**GitHub Actions-specific MCP server** ([ko1ynnky/github-actions-mcp-server](https://github.com/ko1ynnky/github-actions-mcp-server)) — 40 stars, community-maintained. Predates the official server (released March 2025). Focused specifically on workflow operations: listing, triggering, canceling, and rerunning workflows. Useful when you only need Actions control without the broader GitHub MCP surface.

For more on GitHub's broader AI integration including Agentic Workflows, see our [MCP for DevOps and CI/CD guide](/guides/mcp-devops-cicd/).

### GitLab CI — Built Into the Platform

GitLab took a different approach from GitHub: instead of a standalone MCP server, they built MCP support directly into the GitLab platform starting with version 18.6 (November 2025).

**GitLab MCP Server** — built-in, Premium/Ultimate tier. Supports MCP protocol versions 2025-03-26 and 2025-06-18 (added in 18.7). Requires OAuth dynamic client registration.

CI/CD-specific tools:
| Tool | What It Does |
|------|-------------|
| `get_merge_request_pipelines` | List pipelines for a merge request |
| `get_pipeline_jobs` | Get jobs within a specific pipeline |
| `manage_pipeline` | List, create, retry, cancel, update, delete pipelines |

Plus broader tools for issues, merge request management, and semantic code search.

**Claude Code GitLab CI/CD** (beta, maintained by GitLab) — full `.gitlab-ci.yml` integration. Event-driven: triggers on `@claude` mentions in MR and issue comments. Runs in isolated containers with workspace-scoped permissions.

```yaml
# Example: Claude as MR reviewer in GitLab CI
claude-review:
  image: anthropic/claude-code:latest
  script:
    - claude-code --prompt "$AI_FLOW_INPUT"
  variables:
    AI_FLOW_INPUT: "Review this merge request for issues"
    AI_FLOW_CONTEXT: "$CI_MERGE_REQUEST_IID"
    AI_FLOW_EVENT: "merge_request_comment"
  rules:
    - if: '$CI_PIPELINE_SOURCE == "chat"'
```

Key architecture differences from GitHub:
- **Authentication:** OAuth 2.1 with dynamic client registration (vs. GitHub's PAT or OAuth)
- **Deployment:** No separate server to install — it's a platform feature
- **Permissions:** All changes go through MRs; sandboxed execution with workspace-scoped access
- **Cloud backends:** Supports Claude API directly, AWS Bedrock (OIDC), and Google Vertex AI (Workload Identity Federation)

Community alternatives: [yoda-digital/mcp-gitlab-server](https://github.com/yoda-digital/mcp-gitlab-server) (60+ tools, community-maintained) and [zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) (bug fixes over the original Anthropic GitLab server).

### Jenkins — Plugin Architecture

Jenkins's MCP integration follows its traditional plugin model: install a plugin and Jenkins itself becomes an MCP server.

**Official Jenkins MCP Server Plugin** ([jenkinsci/mcp-server-plugin](https://plugins.jenkins.io/mcp-server)) — based on MCP Java SDK v0.17.2, implementing MCP spec 2025-06-18. Auto-sets up endpoints on installation. Supports parameterized jobs. Integrates with GitHub Copilot and other MCP clients. Also available through CloudBees CI plugins.

Key characteristic: the plugin turns Jenkins into an MCP _server_, not a client. Your AI assistant connects to Jenkins and can:
- List and trigger builds
- Monitor job status and queue
- Retrieve build logs and test results
- Manage parameterized job configurations

Community alternatives:
- [kud/mcp-jenkins](https://github.com/kud/mcp-jenkins) — 25+ tools for managing jobs, builds, and CI/CD workflows
- [hekmon8/Jenkins-server-mcp](https://github.com/hekmon8/Jenkins-server-mcp) — querying Jenkins from AI assistants
- [lanbaoshen/mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins) — LLM bridge via Anthropic's MCP spec

### CircleCI — Purpose-Built for CI Debugging

CircleCI's MCP server is notable for being the most CI-focused: every tool is designed for pipeline debugging and management, not general-purpose repository operations.

**Official CircleCI MCP Server** ([CircleCI-Public/mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci)) — nine tools, all CI-specific:

| Tool | Purpose |
|------|---------|
| `get_build_failure_logs` | Structured failure logs with exit codes and error messages |
| `find_flaky_tests` | Leverages CircleCI's built-in flaky test detection analytics |
| `config_helper` | Assists with `.circleci/config.yml` syntax and best practices |
| `get_latest_pipeline_status` | Current pipeline health at a glance |
| `get_job_test_results` | Test failure and performance analytics |
| `run_pipeline` | Trigger new pipeline runs |
| `list_followed_projects` | List projects the user follows |
| `rerun_workflow` | Re-execute failed or partial workflows |
| `run_rollback_pipeline` | First-class rollback support |

The `get_build_failure_logs` tool returns structured output including exit codes and failure messages — designed for AI parsing rather than human reading. The `find_flaky_tests` tool analyzes test execution history over time, surfacing patterns that would take manual effort to identify.

Setup requires a CircleCI API token. Integrates with Cursor, Windsurf, and Augment Code. Featured in an AWS blog for use with AWS Agentic AI.

### Argo CD — GitOps via Natural Language

**Official Argo CD MCP Server** ([akuity/argocd-mcp](https://github.com/akuity/argocd-mcp)) — 379 stars, by Akuity (the company behind Argo CD). Released May 2025.

Tools:
- `list_applications` — list all Argo CD applications
- `get_application` — detailed application status
- Sync deployments — trigger GitOps syncs
- View logs — application and pod logs
- Application health — sync status, health checks

Supports both stdio and Streamable HTTP transport. Requires `ARGOCD_BASE_URL` and `ARGOCD_API_TOKEN` environment variables.

The value proposition is specific: GitOps workflows typically require switching between `argocd` CLI, the web UI, and `kubectl` to understand deployment state. An MCP-connected agent can answer "what's the sync status of all production applications?" or "why did the last sync fail for the payments service?" by querying Argo CD directly.

### Tekton — Cloud-Native Pipeline Control

**Tekton MCP Server** ([tektoncd/mcp-server](https://github.com/tektoncd/mcp-server)) — community-maintained, part of the official Tekton project. Tekton v1.3.1 LTS (August 2025, supported through August 2026) added MCP integration alongside OPA/Kyverno policy enforcement and OpenTelemetry observability.

Capabilities:
- **Inspection:** "List all pipelines in namespace production"
- **Execution:** Trigger pipeline runs with parameters
- **Monitoring:** Stream pipeline and task logs
- **Troubleshooting:** Diagnose failed pipeline runs

Tekton's MCP integration is significant because Tekton runs as Kubernetes Custom Resources. The MCP server translates natural language into the correct CRD operations — creating PipelineRuns, querying TaskRun status, fetching logs from the right pods.

### Azure DevOps — Enterprise GA

**Official Azure DevOps MCP Server** ([microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp)) — exited public preview, generally available since late 2025. TypeScript server.

Tools cover the full Azure DevOps suite:
- **Work items:** Create, update, query, sprint planning
- **Pull requests:** Create, review, merge
- **Pipelines:** Trigger runs, monitor status, view logs
- **Repos:** Branch management, file operations
- **Wikis:** Documentation access
- **Test plans:** Test case generation, execution, results

Supports OAuth 2.1, local mode (stdio), and cloud mode via Microsoft Foundry (remote hosted — zero local installation). The Microsoft Foundry integration means enterprise teams can use Azure DevOps MCP without installing anything locally.

### Harness — DORA Metrics and Deployment Intelligence

**Harness MCP Server** — official, available on AWS Marketplace's AI Agents and Tools category.

What sets Harness apart is the _data_ it exposes through MCP:
- Pipeline execution history (success/failure, duration, stage-level details)
- Deployment frequency metrics
- Rollback event history
- Feature flag states
- Approval gate activity
- **DORA metrics** — deployment frequency, lead time, change failure rate, MTTR

Agents can also _act_: trigger pipeline runs, roll back deployments, update feature flags, and manage approval gates. Integrates with Amazon Q, Windsurf, Cursor, and Claude Desktop.

The DORA metrics exposure is unique. An engineering manager can ask "what's our deployment frequency this quarter compared to last quarter?" and get an answer drawn from live pipeline data, not a manually compiled report.

### CloudBees — Enterprise Jenkins + AI

**CloudBees Unify MCP Server** — enterprise-grade, launched on AWS Marketplace July 2025. Acts as a bridge between CloudBees Unify and the LLM ecosystem.

Key differentiator: CloudBees targets enterprise DevSecOps workflows that span multiple tools. Their MCP server enables agents to:
- Auto-triage and fix flaky tests
- Open PRs with fixes
- Enforce pipeline policies
- Reduce Mean Time to Recovery (MTTR) through automated diagnosis

Works with both Jenkins and CloudBees Unify pipelines. Natural language interface for DevSecOps workflows across the platform.

## Platform Comparison

| Platform | Server Type | Tools | Auth | Transport | Notable Feature |
|----------|-----------|-------|------|-----------|----------------|
| GitHub | Official standalone | Broad (repos, PRs, Actions, security) | PAT, OAuth | stdio, Streamable HTTP | Lockdown mode, 26K+ stars |
| GitLab | Built-in platform | CI/CD + code + issues | OAuth 2.1 dynamic | Platform-native | No install needed (18.6+) |
| Jenkins | Official plugin | Build/job management | Jenkins auth | stdio | Turns Jenkins into MCP server |
| CircleCI | Official standalone | 9 CI-focused tools | API token | stdio | `find_flaky_tests`, rollback tool |
| Argo CD | Official standalone | GitOps app management | API token | stdio, Streamable HTTP | Natural language GitOps |
| Tekton | Community (official project) | Pipeline CRD operations | K8s auth | stdio | Cloud-native K8s pipelines |
| Azure DevOps | Official standalone | Full ADO suite | OAuth 2.1 | stdio, Foundry (remote) | Zero-install cloud mode |
| Harness | Official | Pipelines + DORA metrics | Platform auth | stdio | DORA metrics exposure |
| CloudBees | Official | Jenkins + Unify pipelines | Platform auth | stdio | Enterprise DevSecOps |

## AI Code Review with MCP

AI-powered code review through MCP is becoming a standard CI/CD workflow pattern. Three approaches have emerged.

### Pattern 1: AI Agent as PR Reviewer

The most common pattern — an AI agent reviews every PR automatically.

**Claude Code Action** does this natively: configure it in your GitHub Actions workflow, and it analyzes every PR for logic errors, security vulnerabilities, edge cases, and regressions. It posts findings as inline comments on specific code lines.

**CodeRabbit** uses MCP servers to enrich review context — connecting to Jira, Linear, and web queries to understand the _intent_ behind changes, not just the diff. This means reviews can flag when a change contradicts a linked ticket's requirements.

**Qodo (formerly CodiumAI)** operates as an agentic code integrity platform. Its open-source [`qodo-ai/pr-agent`](https://github.com/qodo-ai/pr-agent) reviews PRs and generates tests.

### Pattern 2: MCP-Connected IDE Reviews

GitHub Copilot now uses MCP to manage PRs. With `--allowedTools mcp__github`, Copilot analyzes code changes across files, related issues, project context, and team review patterns to suggest appropriate reviewers and flag potential issues before the PR is even opened.

### Pattern 3: Custom Review Pipelines

Teams build custom review workflows by connecting Claude or other models to their GitHub/GitLab MCP servers:

1. CI pipeline triggers on PR open/sync
2. Agent reads the diff via MCP
3. Agent fetches related issues and past discussions for context
4. Agent posts structured review comments
5. Human reviewer sees AI analysis alongside the diff

The key limitation as of early 2026: AI code review remains advisory. The tools function as assistants, surfacing potential issues for human reviewers to evaluate. Fully autonomous approval (merge without human review) isn't recommended — the models can miss subtle architectural issues, business logic implications, and cross-service dependencies that require human judgment.

## AI-Powered Testing in CI

MCP enables AI agents to participate in the testing phase of CI/CD in three ways.

### Failure Analysis

The most immediately useful pattern. When tests fail, instead of manually reading logs:

```
Agent: "Why did the checkout service tests fail in the last build?"

CircleCI MCP → get_build_failure_logs
→ "Test test_payment_flow failed with exit code 1:
   AssertionError: Expected status 200 but got 503.
   The payment gateway mock returned an unexpected response."

Agent: "This is a test infrastructure issue, not a code bug.
The payment gateway mock is returning 503. Check if the mock
server container started successfully."
```

CircleCI's `get_build_failure_logs` returns structured output designed for AI parsing — exit codes, failure messages, and log context.

### Flaky Test Detection

CircleCI's `find_flaky_tests` tool analyzes test execution history across runs, identifying tests that pass and fail intermittently. The agent can then:
1. Identify the flaky tests
2. Analyze their failure patterns (time-based? resource-based? order-dependent?)
3. Suggest fixes or quarantine strategies

CloudBees takes this further — their MCP server enables agents to auto-triage flaky tests and open PRs with fixes.

### Multi-Agent Testing Workflows

An emerging pattern uses multiple specialized agents in a testing pipeline:

1. **Requirement Parser Agent** — extracts testable requirements from tickets
2. **Test Generator Agent** — creates test cases from requirements
3. **Test Code Agent** — writes executable test code
4. **Execution Agent** — runs tests on CI/CD infrastructure
5. **Analysis Agent** — interprets results, detects flaky tests, scores release readiness

MCP serves as the routing protocol between agents, with each agent using CI/CD MCP tools (GitHub for code access, CircleCI/Jenkins for execution, monitoring MCP for production comparison).

A key engineering challenge: managing non-deterministic LLM outputs requires disciplined prompt engineering, low model temperatures, and version-controlled prompts for repeatable test outcomes.

For more on testing MCP servers specifically, see our [best testing and QA MCP servers guide](/guides/best-testing-qa-mcp-servers/) and our [MCP testing guide](/guides/mcp-testing-qa/).

## Architecture Patterns for MCP in CI/CD

Four architecture patterns have emerged for integrating MCP with CI/CD systems.

### 1. Facade / API Gateway

The MCP server acts as a unified interface abstracting multiple CI/CD backends. One MCP server exposes tools for GitHub, Jenkins, and ArgoCD simultaneously. The AI agent doesn't need to know which backend handles which operation.

```
AI Agent → MCP Gateway Server → GitHub Actions API
                              → Jenkins API
                              → Argo CD API
                              → Monitoring API
```

### 2. Adapter

Each CI/CD platform has its own dedicated MCP server that translates between the MCP protocol and the platform's native API. This is the current dominant pattern — GitHub has its MCP server, CircleCI has its MCP server, Jenkins has its plugin.

### 3. Sidecar

The MCP server runs alongside the CI/CD job as a companion container. Red Hat's [Cicaddy](https://developers.redhat.com/articles/2026/03/12/how-develop-agentic-workflows-ci-pipeline-cicaddy) framework implements this pattern: instead of AI agents triggering CI from outside, the agent runs _inside_ the pipeline as a step. This inverts the typical flow — the pipeline orchestrates the agent, not the other way around.

### 4. Event-Driven

CI/CD events (webhooks, PR comments, pipeline failures) trigger agent actions. GitLab's `@claude` comment triggers a CI pipeline that runs Claude with MCP tools. CircleCI integrates with Cursor and Windsurf, triggering on pipeline events. This is the pattern behind GitHub's Agentic Workflows and GitLab's Claude CI/CD integration.

For more on architecture patterns, see our [MCP agent workflow patterns guide](/guides/mcp-agent-workflow-patterns/) and [event-driven MCP patterns guide](/guides/event-driven-mcp-patterns/).

## The OWASP MCP Top 10: CI/CD Security Risks

OWASP published a dedicated [MCP Top 10](https://owasp.org/www-project-mcp-top-10/) project identifying the most critical security risks. Several are particularly dangerous in CI/CD contexts.

### MCP01: Token Mismanagement and Secret Exposure

Hard-coded credentials and long-lived tokens in model memory or logs. In CI/CD, this means:
- API tokens for GitHub, CircleCI, or Jenkins stored in MCP configuration
- Cloud credentials passed through MCP tool calls and logged
- AI agents accumulating tokens in conversation context, then referencing them in other tool calls

**CI/CD impact:** Lateral movement from a compromised CI agent to cloud storage, production infrastructure, and issue trackers.

### MCP03: Tool Poisoning

Adversaries compromise tool metadata — descriptions, parameters, hidden instructions — to manipulate AI agent behavior. In CI/CD:
- A compromised MCP server could return tool descriptions that instruct the agent to skip security checks
- Malicious tool schemas could extract secrets from the agent's context

### MCP04: Software Supply Chain Attacks

Compromised MCP server packages alter agent behavior. This has already happened:
- **Postmark MCP Supply Chain Breach (2025):** Hackers created a backdoor in an npm package used in MCP automation pipelines for transactional emails. The malicious code blind-copied every outgoing email to attackers.
- **CVE-2025-6514** (CVSS 9.6): Critical OS command injection in `mcp-remote` versions 0.0.5–0.1.15 — an OAuth proxy package with 437,000+ downloads. A malicious MCP server could send a crafted `authorization_endpoint` URL that, when passed to the shell by `mcp-remote`, executed arbitrary code. Fixed in v0.1.16.

### MCP05: Command Injection

AI constructs commands from untrusted input without sanitization. In CI/CD, this could mean:
- An agent builds a shell command from PR title or commit message content
- Pipeline parameters containing injection payloads reach MCP tool calls

### MCP06: Intent Flow Subversion

Malicious instructions embedded in context hijack agent operations. In CI/CD:
- Issue descriptions, PR comments, or commit messages containing hidden prompt injection
- CI logs from previous runs containing embedded instructions

GitHub's Lockdown mode was specifically designed to mitigate this — it blocks content from untrusted contributors when the MCP server processes public repository data.

### MCP09: Shadow MCP Servers

Unapproved MCP server deployments outside governance. In CI/CD:
- Developers adding unauthorized MCP servers to their CI configurations
- Community MCP servers used without security review

### MCP Ecosystem Security Statistics (Astrix Research, 2025)

Based on analysis of 5,000+ MCP server implementations:
- **88%** of MCP servers require credentials
- **53%** use static API keys or personal access tokens (rarely rotated)
- **Only 8.5%** adopt OAuth for secure authentication
- **79%** pass API keys through environment variables

These numbers are concerning for CI/CD environments where MCP servers have access to build infrastructure, deployment credentials, and source code.

## Real-World Incident Case Studies

### The Supabase Cursor Agent Incident (2025)

A Cursor agent running with privileged service-role access processed support tickets containing user-supplied SQL instructions. The agent, following the instructions embedded in the ticket content, exfiltrated sensitive integration tokens to a public support thread. Three factors combined to create the breach:
1. **Privileged access** — the agent had service-role credentials
2. **Untrusted input** — support tickets contained user-supplied content
3. **External communication** — the agent could post to public threads

This is exactly the pattern that occurs when CI/CD agents process PR descriptions, issue comments, or commit messages with broad tool access.

### Cisco DevOps Case Study (2025)

On the positive side, Cisco documented production use of MCP-connected AI for CI/CD automation — builds, tests, deployments, and notifications through Cisco Webex. GitHub MCP integration for managing branches, reviewing PRs, triaging issues, and scanning vulnerabilities across their development workflow.

### Docker MCP Catalog: Verified Supply Chain

Docker's response to supply chain risks: the [Docker MCP Catalog](https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/) — 300+ verified MCP servers packaged as container images with versioning, provenance, cryptographic signatures, SBOMs, and security updates. The Docker MCP Toolkit runs MCP servers in isolated containers with signed image verification and an intelligent gateway that intercepts and blocks malicious requests before they reach tools.

For CI/CD teams, pulling MCP servers from Docker's verified catalog is significantly safer than installing community npm packages directly.

## Security Best Practices for CI/CD MCP

### 1. Use Dedicated, Scoped Tokens

Create CI-specific tokens for MCP servers. Never reuse personal access tokens. Scope to the minimum permissions required:
- Read-only for monitoring and analysis
- Write only for specific approved operations (PR comments, issue creation)
- Never admin or delete permissions

### 2. Container Isolation

Run MCP servers in Docker containers with explicit network policies, filesystem isolation, and resource limits. The Docker MCP Toolkit provides this out of the box.

### 3. Pin Versions and Verify Signatures

Pin MCP server versions in CI configurations. Use Docker images from the verified MCP Catalog with cryptographic signature verification. Never use `latest` tags for MCP servers in CI.

### 4. Secrets Management via Vault

HashiCorp's [Vault MCP Server](https://developer.hashicorp.com/vault/docs/mcp-server/overview) (public beta) provides KV static secrets, PKI certificate management, and secrets engine management through MCP. Security model: uses end-user's Vault token (never root or shared), with `ENABLE_VAULT_OPERATIONS` flag to restrict writes.

CI/CD use case: AI agent fetches temporary database credentials for integration tests in sandboxed environments, with credentials that expire after the test run.

### 5. Human-in-the-Loop for Destructive Operations

No production deployments, rollbacks, or infrastructure changes without human approval. CircleCI's `run_rollback_pipeline` and Harness's deployment triggers should always require confirmation in production environments.

### 6. Audit Everything

Every MCP tool call in CI should be logged with: timestamp, agent identity, tool name, parameters, and result. Feed these logs into your existing SIEM. AWS's Cloud Control API MCP server does this natively via CloudTrail.

## Getting Started: Choosing Your Platform's MCP Integration

**If you use GitHub Actions** — start with the [official GitHub MCP Server](https://github.com/github/github-mcp-server). For AI code review, add [Claude Code Action](https://github.com/marketplace/actions/claude-code-action-official). Enable Lockdown mode for public repositories.

**If you use GitLab CI** — upgrade to GitLab 18.6+ and enable the built-in MCP server. For `@claude` MR review, configure the Claude Code GitLab CI/CD integration.

**If you use Jenkins** — install the [MCP Server Plugin](https://plugins.jenkins.io/mcp-server). It auto-configures endpoints on installation.

**If you use CircleCI** — install the [official MCP server](https://github.com/CircleCI-Public/mcp-server-circleci) with a CircleCI API token. Start with `get_build_failure_logs` and `find_flaky_tests` for immediate value.

**If you use Argo CD** — install the [official MCP server](https://github.com/akuity/argocd-mcp). Useful for natural language GitOps queries even if you don't automate sync operations.

**If you want multi-platform** — consider the agent gateway pattern described in our [MCP for DevOps guide](/guides/mcp-devops-cicd/). A single AI agent connects to multiple CI/CD MCP servers and orchestrates across them.

## Further Reading

- [MCP for DevOps and CI/CD](/guides/mcp-devops-cicd/) — broader overview including infrastructure-as-code, Kubernetes, and the agent gateway architecture
- [MCP Server Security](/guides/mcp-server-security/) — comprehensive security guide
- [MCP Attack Vectors and Defense](/guides/mcp-attack-vectors-defense/) — threat models and mitigations
- [MCP Credential and Secret Management](/guides/mcp-credential-secret-management/) — secrets handling patterns
- [Best DevOps MCP Servers](/guides/best-devops-mcp-servers/) — curated server list
- [Best Testing and QA MCP Servers](/guides/best-testing-qa-mcp-servers/) — testing tool roundup
- [Best Kubernetes and Container MCP Servers](/guides/best-kubernetes-container-mcp-servers/) — container orchestration tools
- [MCP Docker and Containers](/guides/mcp-docker-containers/) — container patterns
- [MCP Authentication and OAuth](/guides/mcp-authentication-oauth/) — OAuth 2.1 implementation
- [Event-Driven MCP Patterns](/guides/event-driven-mcp-patterns/) — webhook and event architectures
- [MCP Agent Workflow Patterns](/guides/mcp-agent-workflow-patterns/) — multi-agent orchestration
- [MCP Performance Testing and Benchmarking](/guides/mcp-performance-testing-benchmarking/) — measuring MCP server performance
