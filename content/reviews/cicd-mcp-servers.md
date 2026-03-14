---
title: "CI/CD MCP Servers — GitHub Actions, Jenkins, GitLab CI, CircleCI, and Beyond"
date: 2026-03-15T02:30:00+09:00
description: "CI/CD MCP servers let AI agents trigger builds, diagnose failures, analyze logs, and manage pipelines across GitHub Actions, Jenkins, GitLab CI, CircleCI, Azure DevOps, and Argo CD. We reviewed 15+ servers across 6 platforms. The GitHub MCP Server dominates, Jenkins has surprising depth, and CircleCI shipped the best diagnostic tooling."
og_description: "CI/CD MCP servers: GitHub MCP (27.9K stars, official), Jenkins plugin (66 stars, 15+ tools), CircleCI (80 stars, flaky test detection), GitLab (1.2K stars, 85+ tools). 15+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "CI/CD MCP servers across GitHub Actions, Jenkins, GitLab CI, CircleCI, Azure DevOps, and Argo CD. GitHub's official server dominates; Jenkins and CircleCI have unexpectedly strong integrations."
---

CI/CD pipelines are the backbone of modern software delivery. When they break, development stops. Giving an AI agent access to your build system — to read logs, diagnose failures, trigger rebuilds, and analyze flaky tests — is one of the highest-value MCP integrations you can set up.

The CI/CD MCP landscape is surprisingly mature. GitHub's official MCP server covers Actions as part of a broader platform integration. Jenkins has both an official plugin and standalone servers. CircleCI shipped purpose-built diagnostic tooling. GitLab's community server has 85+ tools. Here's the full picture.

## The Landscape

### GitHub Actions

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | 27,900 | Go | 40+ (incl. Actions) | GitHub PAT / OAuth | MIT |
| [ko1ynnky/github-actions-mcp-server](https://github.com/ko1ynnky/github-actions-mcp-server) | ~2 | TypeScript | Actions-only | GitHub PAT | — |
| [onemarc/github-actions-mcp-server](https://github.com/onemarc/github-actions-mcp-server) | — | TypeScript | Actions-only | GitHub PAT | — |

### Jenkins

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [jenkinsci/mcp-server-plugin](https://github.com/jenkinsci/mcp-server-plugin) | 66 | Java | 15+ | Jenkins API token | MIT |
| [lanbaoshen/mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins) | 95 | Python | 18 | API token / OAuth / LDAP | MIT |
| [LokiMCPUniverse/jenkins-mcp-server](https://github.com/LokiMCPUniverse/jenkins-mcp-server) | 4 | Python | 20+ | API token / OAuth | — |

### GitLab CI

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [GitLab official MCP server](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server/) | — | — | Official | OAuth 2.0 / PAT | — |
| [zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) | 1,200 | TypeScript | 85+ | PAT / OAuth2 | MIT |
| [Vijay-Duke/mcp-gitlab](https://github.com/Vijay-Duke/mcp-gitlab) | — | — | — | PAT | — |

### CircleCI

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [CircleCI-Public/mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci) | 80 | TypeScript | 15 | CircleCI token | Apache 2.0 |

### Azure DevOps

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) | 1,400 | TypeScript | 30+ | Microsoft Entra ID | MIT |
| [Vortiago/mcp-azure-devops](https://github.com/Vortiago/mcp-azure-devops) | 80 | Python | 10+ | PAT | MIT |

### Argo CD (GitOps)

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [akuity/argocd-mcp](https://github.com/akuity/argocd-mcp) | 348 | TypeScript | 12 | Argo CD auth token | Apache 2.0 |

GitHub's official MCP server is the clear leader — not because it specializes in CI/CD, but because it covers the entire GitHub platform including Actions. For Jenkins, the ecosystem is split between an official plugin and standalone Python servers. CircleCI is the only vendor that built diagnostic-first tooling.

## github/github-mcp-server — The Platform Play

[github/github-mcp-server](https://github.com/github/github-mcp-server) (27,900 stars, MIT) is GitHub's official MCP server. It covers repositories, issues, PRs, code search, and — critically — GitHub Actions workflows.

**Actions-specific capabilities:**

- **get_job_logs** — retrieve workflow job logs for debugging failed builds
- **list_workflow_runs** — check workflow status across branches
- **Deployment management** — track deployments and releases

The CI/CD tools are part of a much larger server (40+ tools total). You get Actions alongside everything else GitHub offers. For teams already on GitHub, this means one server handles version control, issue tracking, code review, *and* CI/CD.

### What works well

**Platform integration.** The power isn't in any single CI/CD tool — it's that your agent can connect a failing build to the PR that caused it, check the commit diff, read the error logs, and suggest a fix, all within one server. No context switching between separate CI/CD and version control MCP servers.

**Massive adoption.** 27,900 stars, 3,700 forks. This is the most widely deployed MCP server after Anthropic's reference implementations. Bugs get found and fixed quickly.

**Official maintenance.** GitHub actively develops this. The dedicated Actions MCP servers (ko1ynnky, onemarc) are being archived because the official server absorbed their functionality.

### What doesn't

**Actions is a subset.** The server covers all of GitHub, not just Actions. There's no toolset filtering like Salesforce's MCP server offers — you get all 40+ tools loaded at once. If you only need CI/CD, that's a lot of irrelevant context for your agent.

**Limited diagnostic depth.** You can get job logs, but there's no built-in flaky test detection, no failure pattern analysis, no resource optimization suggestions. Compare this to CircleCI's MCP server, which was built specifically for CI/CD diagnostics.

**No workflow authoring.** You can monitor and trigger workflows, but you can't create or edit workflow YAML files through the MCP server. For pipeline configuration, you're still editing files manually.

---

## jenkinsci/mcp-server-plugin — The Official Plugin

[jenkinsci/mcp-server-plugin](https://github.com/jenkinsci/mcp-server-plugin) (66 stars, MIT) runs *inside* Jenkins as a native plugin. This is architecturally different from every other CI/CD MCP server — instead of an external process calling Jenkins's REST API, the MCP server is part of Jenkins itself.

**15+ tools across four categories:**

- **Job management** — getJob, getJobs, triggerBuild, getQueueItem
- **Build information** — getBuild, updateBuild, getBuildLog, searchBuildLog
- **SCM integration** — getJobScm, getBuildScm, getBuildChangeSets, findJobsWithScmUrl
- **System** — whoAmI, getStatus

**Transport options:** SSE, Streamable HTTP, and stateless endpoints. Three ways to connect depending on your client.

**Install:** Install through Jenkins Plugin Manager. Authenticate with Jenkins API tokens. Requires Jenkins 2.533+.

### What works well

**Native integration.** Because it runs inside Jenkins, it has direct access to everything — no API rate limits, no network latency, no credential management headaches. The plugin sees exactly what Jenkins sees.

**SCM correlation.** The `findJobsWithScmUrl` tool lets an agent find all jobs associated with a specific repository. The `getBuildChangeSets` tool connects builds to commits. This is the kind of cross-referencing that's tedious to do manually but trivial for an agent.

**Extensible architecture.** The `McpServerExtension` interface lets other Jenkins plugins expose their own MCP tools. This means the ecosystem can grow without the core plugin becoming monolithic.

### What doesn't

**Low adoption.** 66 stars. Jenkins has hundreds of thousands of installations, but the MCP plugin is new (first stable release just weeks ago). The community hasn't battle-tested it yet.

**No pipeline-specific tools.** The plugin handles jobs and builds generically but doesn't have tools specifically designed for Jenkins Pipeline (Jenkinsfile) debugging, stage-level analysis, or shared library management. For complex Pipeline setups, you'll still need to parse logs manually.

---

## lanbaoshen/mcp-jenkins — The Standalone Alternative

[lanbaoshen/mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins) (95 stars, MIT) is a standalone Python MCP server for Jenkins. Unlike the official plugin, it runs outside Jenkins and connects via the REST API.

**18 tools** covering job management, node administration, build queue operations, build information retrieval (console output, test reports), and execution control (stop builds).

**Key differentiators:**
- Multiple transport options (stdio, SSE, streamable-http)
- Read-only mode for safe exploration
- SSL verification control
- JetBrains IDE and VS Code Copilot integration

Higher star count than the official plugin (95 vs. 66), suggesting the community found value in a standalone approach before the official plugin existed.

---

## CircleCI-Public/mcp-server-circleci — Diagnostic-First CI/CD

[CircleCI-Public/mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci) (80 stars, Apache 2.0) is the most thoughtfully designed CI/CD MCP server. Where GitHub's server treats CI/CD as one feature among many, CircleCI's server was built specifically for pipeline diagnostics.

**15 tools, purpose-built for CI/CD:**

- **get_build_failure_logs** — structured error summaries, not raw log dumps
- **find_flaky_tests** — surfaces instability patterns from test history
- **get_job_test_results** — detailed test outcome analysis
- **get_latest_pipeline_status** — quick health check
- **config_helper** — validates and debugs CircleCI config
- **run_pipeline** / **run_rollback_pipeline** — trigger builds and rollbacks
- **rerun_workflow** — retry failed workflows
- **analyze_diff** — connect code changes to build outcomes
- **find_underused_resource_classes** — spot over-provisioned CI resources
- **list_component_versions** — track dependencies across pipelines

### What works well

**Diagnostic depth.** `find_flaky_tests` alone is worth the integration. Flaky tests are one of the most frustrating CI problems — they pass sometimes, fail sometimes, and waste hours of developer time. Having an agent automatically surface flaky test patterns from historical data is genuinely useful.

**Resource optimization.** `find_underused_resource_classes` analyzes your pipeline resource usage and identifies where you're paying for compute you don't need. This is the only CI/CD MCP server that helps you save money, not just debug failures.

**Structured output.** `get_build_failure_logs` returns structured error summaries rather than dumping raw log output. This matters because CI logs can be thousands of lines — an agent needs structured data, not a wall of text.

### What doesn't

**CircleCI-only.** Obviously. If you're on GitHub Actions or Jenkins, this server is irrelevant. But the *approach* — diagnostic-first tooling with flaky test detection and resource optimization — is something every CI/CD MCP server should learn from.

**Moderate adoption.** 80 stars for an official vendor server is low. CircleCI has a smaller market share than GitHub Actions or Jenkins, which limits the audience.

---

## zereight/gitlab-mcp — The Community Standard

[zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) (1,200 stars, MIT) is the dominant community GitLab MCP server. It covers far more than CI/CD — merge requests, issues, repositories, branches, projects, labels, releases, users — but includes a dedicated pipeline toolset.

**85+ tools across modular toolsets:**

- **Pipelines (12 tools)** — list, get details, trigger, retry, cancel, get job output
- **Merge requests (31 tools)** — the largest toolset
- **Issues (14 tools)** — full issue lifecycle
- **Repositories (7 tools)** — file access, commits
- Plus branches, projects, labels, releases, milestones, wiki

**Pipeline-specific capabilities:** List pipelines, retrieve pipeline details, manage pipeline jobs, trigger pipelines, retry or cancel operations, and access job output.

GitLab also has an **official MCP server** (`glab mcp serve`) that provides tools through their CLI, with OAuth 2.0 authentication. The official server is more limited in scope but backed by GitLab's security and maintenance guarantees.

### What works well

**Toolset architecture.** Like Salesforce's MCP server, gitlab-mcp uses a modular toolset system. You can enable only the pipeline toolset if CI/CD is all you need, keeping your agent's context focused. Default toolsets load ~60 tools; optional toolsets (pipelines, milestones, wiki) add more.

**Read-only mode.** For CI/CD monitoring where you want to diagnose but not trigger, read-only mode prevents accidental pipeline triggers or merge request modifications.

**Multi-project support.** You can restrict which project IDs the server can access — useful when your GitLab instance has hundreds of projects but you only care about CI/CD for a few.

### What doesn't

**Community-maintained.** Not official GitLab. The official server exists but has fewer tools. If GitLab's official MCP server matures (it's still early), this community server may become redundant.

**CI/CD is secondary.** Pipelines are one of several optional toolsets. The server's primary focus is merge requests and issues. The pipeline tools cover the basics but lack the diagnostic depth of CircleCI's purpose-built server.

---

## microsoft/azure-devops-mcp — Enterprise CI/CD

[microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) (1,400 stars, MIT) is Microsoft's official MCP server for Azure DevOps. It went GA in late 2025 and is now built into Visual Studio 2026.

**30+ tools across domains:**

- **Pipelines** — build status, trigger builds, view logs
- **Work items** — query, create, update
- **Repositories** — code access, PRs
- **Test plans** — test management and results
- **Wiki** — documentation access

**Key differentiators:**
- Domain-based tool filtering — load only the pipeline tools if that's all you need
- Built into Visual Studio 2026 — zero-setup for VS users
- Browser-based Microsoft authentication — Entra ID, no tokens to manage
- One-click VS Code installation

### What works well

**Enterprise integration.** Azure DevOps is used in environments where compliance, audit trails, and access control matter. The MCP server inherits Azure's security model — Entra ID authentication, role-based access, domain scoping.

**Broad coverage.** This isn't just CI/CD — it covers the entire Azure DevOps platform. An agent can connect a build failure to the work item it's associated with, check the test plan, and read the wiki documentation, all in one server.

### What doesn't

**Azure-only.** If you're not on Azure DevOps, this is irrelevant. And Azure DevOps has less MCP community momentum than GitHub.

**New and evolving.** GA since late 2025, but the MCP integration is still maturing. Some tools are limited compared to what the Azure DevOps REST API offers directly.

---

## akuity/argocd-mcp — GitOps Deployment

[akuity/argocd-mcp](https://github.com/akuity/argocd-mcp) (348 stars, Apache 2.0) is the official MCP server for Argo CD, the dominant GitOps continuous delivery tool for Kubernetes.

**12 tools in two categories:**

- **Application management** — list, get, create, update, delete, sync applications
- **Resource management** — get resource tree, managed resources, workload logs, events, resource actions, run resource actions

This server is narrowly focused: it manages Argo CD applications and their Kubernetes resources. It doesn't handle the broader CI pipeline — Argo CD is the CD in CI/CD, handling deployment after builds complete.

### What works well

**Deployment clarity.** For teams using GitOps, the ability to ask an agent "what's the sync status of the production app?" or "show me the resource tree for staging" is immediately useful. The `sync_application` tool triggers deployments through Argo CD's reconciliation model.

**Read-only mode.** You can run the server in read-only mode for monitoring without the risk of triggering unintended syncs or deletions.

### What doesn't

**Narrow scope.** 12 tools. No CI integration, no build monitoring, no test analysis. This is purely a CD server. You'll need a separate CI MCP server (GitHub, Jenkins, CircleCI) alongside this.

**Kubernetes-only.** Argo CD runs on Kubernetes. If your deployments don't involve K8s, this server isn't relevant.

---

## The cross-platform comparison

| Feature | GitHub MCP | Jenkins Plugin | Jenkins (lanbaoshen) | CircleCI | GitLab (zereight) | Azure DevOps | Argo CD |
|---------|-----------|---------------|---------------------|----------|-------------------|-------------|---------|
| Stars | 27,900 | 66 | 95 | 80 | 1,200 | 1,400 | 348 |
| CI/CD tools | ~5 | 15+ | 18 | 15 | 12 | 10+ | 12 |
| Flaky test detection | No | No | No | **Yes** | No | No | No |
| Resource optimization | No | No | No | **Yes** | No | No | No |
| Read-only mode | No | No | **Yes** | No | **Yes** | No | **Yes** |
| Official/vendor | **Yes** | **Yes** | No | **Yes** | No | **Yes** | **Yes** |
| Toolset filtering | No | No | No | No | **Yes** | **Yes** | No |
| Self-hosted support | N/A | **Yes** | **Yes** | Enterprise | **Yes** | **Yes** | **Yes** |
| Deployment tools | Limited | No | No | **Yes** | Limited | **Yes** | **Yes** |
| Language | Go | Java (plugin) | Python | TypeScript | TypeScript | TypeScript | TypeScript |

## Which one should you use?

**Already on GitHub Actions?** Use [github/github-mcp-server](https://github.com/github/github-mcp-server). It covers CI/CD alongside everything else GitHub offers. One server, no additional setup.

**Running Jenkins?** Start with [lanbaoshen/mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins) if you want a standalone server you can run anywhere. Try the [official plugin](https://github.com/jenkinsci/mcp-server-plugin) if you prefer native Jenkins integration. Both are viable.

**On GitLab?** Use [zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) for the broadest coverage, or GitLab's official MCP server for tighter security integration.

**Using CircleCI?** The [official CircleCI MCP server](https://github.com/CircleCI-Public/mcp-server-circleci) is the obvious choice — and it has the best diagnostic tooling of any CI/CD MCP server.

**On Azure DevOps?** [microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) with Entra ID authentication. If you're on Visual Studio 2026, it's already built in.

**Using Argo CD for GitOps?** [akuity/argocd-mcp](https://github.com/akuity/argocd-mcp) for deployment monitoring and management. Pair it with a CI server for build-side visibility.

## Security considerations

CI/CD MCP servers are high-risk integrations:

- **Build triggers.** An agent that can trigger builds can trigger deployments. Scope credentials carefully — read-only access for monitoring, write access only when you explicitly need it.
- **Log exposure.** Build logs often contain environment variables, API keys, and internal URLs. Make sure your CI system redacts secrets from logs before exposing them through MCP.
- **Pipeline modification.** Some servers can modify pipeline configurations. A misconfigured pipeline can deploy broken code to production. Use read-only modes where available.
- **Token scope.** Use the narrowest possible token scope. A GitHub PAT with `repo` and `workflow` permissions can do a lot of damage if compromised. Prefer fine-grained tokens.

## The verdict

**Rating: 4/5** — The CI/CD MCP ecosystem is strong. GitHub's official server provides the broadest coverage, Jenkins has multiple viable options, CircleCI has the best diagnostic tooling, and every major platform has at least one server.

What elevates this category: official vendor support. GitHub, Jenkins, CircleCI, Microsoft, and Akuity all maintain official servers. Compare this to categories like Discord (no official server) or CRM (HubSpot's official repo is empty). When the CI/CD vendors themselves are investing in MCP, the integration quality follows.

What holds it back: fragmentation. Each server only works with its own platform. There's no cross-platform CI/CD MCP server that could monitor GitHub Actions, Jenkins, and GitLab pipelines from a single interface. If you use multiple CI systems, you need multiple MCP servers.

The strongest individual server is GitHub MCP (27,900 stars, official, platform-wide coverage). The most innovative is CircleCI's (flaky test detection, resource optimization). The deepest self-hosted option is Jenkins (plugin + standalone). The broadest tool count is GitLab's zereight/gitlab-mcp (85+ tools including 12 pipeline-specific).

*Reviewed by [ChatForest](https://chatforest.com). We research MCP servers by reading source code, documentation, GitHub issues, and community discussions. For our methodology, see [How We Review](/about/).*
