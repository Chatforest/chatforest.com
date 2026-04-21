---
title: "CI/CD MCP Servers — GitHub Actions, Jenkins, GitLab CI, CircleCI, and Beyond"
date: 2026-03-15T02:30:00+09:00
description: "CI/CD MCP servers let AI agents trigger builds, diagnose failures, analyze logs, and manage pipelines across GitHub Actions, Jenkins, GitLab CI, CircleCI, Azure DevOps, Buildkite, and Argo CD."
og_description: "CI/CD MCP servers: GitHub MCP v1.0.0 (29.1K stars, toolset filtering), Jenkins (4 servers, up to 37 tools), Buildkite official (v1.0.0), CircleCI (17 tools), Azure DevOps Remote MCP preview. Rating: 4.5/5."
content_type: "Review"
card_description: "CI/CD MCP servers across GitHub Actions, Jenkins, GitLab CI, CircleCI, Azure DevOps, Buildkite, and Argo CD. GitHub hits v1.0.0 with toolset filtering; Buildkite joins as new official vendor; Azure DevOps goes cloud-native."
last_refreshed: 2026-04-21
---

CI/CD pipelines are the backbone of modern software delivery. When they break, development stops. Giving an AI agent access to your build system — to read logs, diagnose failures, trigger rebuilds, and analyze flaky tests — is one of the highest-value MCP integrations you can set up.

The CI/CD MCP landscape is the strongest it's ever been. GitHub's official server hit v1.0.0 in April 2026 with toolset filtering. Buildkite joined as a new official vendor server. Azure DevOps launched a Remote MCP Server preview (cloud-hosted, no local setup). Jenkins now has four competing servers with up to 37 tools. CircleCI expanded to 17 diagnostic tools. GitLab's community server added OAuth, security hardening, and GraphQL work items. Here's the full picture.

**Category:** [Developer Tools](/categories/developer-tools/)

## The Landscape

### GitHub Actions

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | 29,100 | Go | 40+ (incl. Actions) | GitHub PAT / OAuth | MIT |
| [ko1ynnky/github-actions-mcp-server](https://github.com/ko1ynnky/github-actions-mcp-server) | ~2 | TypeScript | Actions-only | GitHub PAT | — |
| [onemarc/github-actions-mcp-server](https://github.com/onemarc/github-actions-mcp-server) | — | TypeScript | Actions-only | GitHub PAT | — |

### Jenkins

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [jenkinsci/mcp-server-plugin](https://github.com/jenkinsci/mcp-server-plugin) | 77 | Java | ~20 | Jenkins API token | MIT |
| [lanbaoshen/mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins) | 115 | Python | 24 | API token / OAuth / LDAP | MIT |
| [kud/mcp-jenkins](https://github.com/kud/mcp-jenkins) | 3 | TypeScript | 37 | Bearer / Basic / OAuth | MIT |
| [LokiMCPUniverse/jenkins-mcp-server](https://github.com/LokiMCPUniverse/jenkins-mcp-server) | 4 | Python | 20+ | API token / OAuth | — |

### GitLab CI

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [GitLab official MCP server](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server/) | — | — | 250+ (experimental) | OAuth 2.0 / PAT | — |
| [zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) | 1,400 | TypeScript | 85+ | PAT / OAuth2 / MCP OAuth | MIT |
| [Vijay-Duke/mcp-gitlab](https://github.com/Vijay-Duke/mcp-gitlab) | — | — | — | PAT | — |

### CircleCI

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [CircleCI-Public/mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci) | 84 | TypeScript | 17 | CircleCI token | Apache 2.0 |

### Buildkite (NEW)

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [buildkite/buildkite-mcp-server](https://github.com/buildkite/buildkite-mcp-server) | 50 | Go | Pipelines, builds, jobs, tests | Buildkite API token | MIT |

### Azure DevOps

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) | 1,600 | TypeScript | 30+ | Microsoft Entra ID | MIT |
| [Azure DevOps Remote MCP](https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server) | — | Hosted | Same as local | Entra ID | — |
| [Vortiago/mcp-azure-devops](https://github.com/Vortiago/mcp-azure-devops) | 80 | Python | 10+ | PAT | MIT |

### Argo CD (GitOps)

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [akuity/argocd-mcp](https://github.com/akuity/argocd-mcp) | 401 | TypeScript | 12 | Argo CD auth token | Apache 2.0 |

GitHub's official MCP server remains the clear leader — now at v1.0.0 with toolset filtering that addresses the "too many tools" problem. Jenkins has the deepest ecosystem with four competing servers. Buildkite is the newest official vendor entry. Azure DevOps is pioneering the cloud-native approach with a hosted Remote MCP Server. CircleCI still has the best diagnostic-first tooling.

## github/github-mcp-server — The Platform Play (v1.0.0)

[github/github-mcp-server](https://github.com/github/github-mcp-server) (29,100 stars, 4,000 forks, MIT) hit **v1.0.0 on April 16, 2026** — a milestone that signals production readiness. It covers repositories, issues, PRs, code search, and — critically — GitHub Actions workflows.

**Actions-specific capabilities:**

- **get_job_logs** — retrieve workflow job logs for debugging failed builds
- **list_workflow_runs** — check workflow status across branches
- **Deployment management** — track deployments and releases
- **set_issue_fields** — granular issue field control (new in v1.0.0)

The CI/CD tools are part of a much larger server (40+ tools total). You get Actions alongside everything else GitHub offers. For teams already on GitHub, this means one server handles version control, issue tracking, code review, *and* CI/CD.

**What's new since March 2026:**
- **v1.0.0** (April 16) — granular issue fields via `set_issue_fields`, MCP Apps UI support
- **v0.33.0** (April 14) — resolve review threads, `list_commits` with path/time filtering, granular PR/issue toolsets
- **v0.31.0** (February) — streamable HTTP support, Insiders Mode with MCP Apps
- **Toolset filtering** — `--toolsets` flag and `--exclude-tools` flag let you load only the tools you need
- **Scope-based filtering** — OAuth tokens automatically hide tools you can't use; classic PATs filter out inaccessible tools
- **Remote server** — `https://api.githubcopilot.com/mcp/` for hosted access (no local Docker needed)
- **Enterprise support** — GitHub Enterprise Server and Enterprise Cloud with data residency

### What works well

**Platform integration.** The power isn't in any single CI/CD tool — it's that your agent can connect a failing build to the PR that caused it, check the commit diff, read the error logs, and suggest a fix, all within one server. No context switching between separate CI/CD and version control MCP servers.

**Massive adoption.** 29,100 stars, 4,000 forks, 799 commits. This is the most widely deployed MCP server after Anthropic's reference implementations. Bugs get found and fixed quickly.

**Toolset filtering (NEW).** The `--toolsets` and `--exclude-tools` flags address the biggest complaint from our original review: you can now load only CI/CD-related tools instead of all 40+. Scope-based filtering automatically hides tools your token can't access. This is a significant improvement.

**Official maintenance.** GitHub actively develops this — 33+ releases since launch. The dedicated Actions MCP servers (ko1ynnky, onemarc) are being archived because the official server absorbed their functionality.

### What doesn't

**Limited diagnostic depth.** You can get job logs, but there's no built-in flaky test detection, no failure pattern analysis, no resource optimization suggestions. Compare this to CircleCI's MCP server, which was built specifically for CI/CD diagnostics.

**No workflow authoring.** You can monitor and trigger workflows, but you can't create or edit workflow YAML files through the MCP server. For pipeline configuration, you're still editing files manually.

---

## jenkinsci/mcp-server-plugin — The Official Plugin

[jenkinsci/mcp-server-plugin](https://github.com/jenkinsci/mcp-server-plugin) (77 stars, 51 forks, 168 commits, MIT) runs *inside* Jenkins as a native plugin. This is architecturally different from every other CI/CD MCP server — instead of an external process calling Jenkins's REST API, the MCP server is part of Jenkins itself.

**~20 tools across five categories:**

- **Job management** — getJob, getJobs, triggerBuild, getQueueItem
- **Build information** — getBuild, updateBuild, getBuildLog, searchBuildLog, rebuildBuild, getTestResults
- **Replay** — getReplayScripts, replayBuild (new — replay builds with modified scripts)
- **SCM integration** — getJobScm, getBuildScm, getBuildChangeSets, findJobsWithScmUrl
- **System** — whoAmI, getStatus

**What's new:** The plugin now includes `rebuildBuild`, `getReplayScripts`, `replayBuild`, and `getTestResults` — expanding from ~15 to ~20 tools. New operational features include a health endpoint (`/mcp-health`, no auth required), a metrics endpoint for connection statistics, configurable keep-alive messages, and graceful shutdown. Built on MCP Java SDK v0.17.2 (spec 2025-06-18).

**Transport options:** SSE, Streamable HTTP, and stateless endpoints. Three ways to connect depending on your client. Note: GitHub Copilot currently has compatibility issues with Streamable transport — use SSE instead.

**Install:** Install through Jenkins Plugin Manager. Authenticate with Jenkins API tokens. Requires Jenkins 2.533+.

### What works well

**Native integration.** Because it runs inside Jenkins, it has direct access to everything — no API rate limits, no network latency, no credential management headaches. The plugin sees exactly what Jenkins sees.

**SCM correlation.** The `findJobsWithScmUrl` tool lets an agent find all jobs associated with a specific repository. The `getBuildChangeSets` tool connects builds to commits. This is the kind of cross-referencing that's tedious to do manually but trivial for an agent.

**Extensible architecture.** The `McpServerExtension` interface lets other Jenkins plugins expose their own MCP tools. This means the ecosystem can grow without the core plugin becoming monolithic.

**Replay support (NEW).** The `replayBuild` and `getReplayScripts` tools let an agent replay a build with modified Groovy scripts — useful for debugging Pipeline issues without committing code changes.

### What doesn't

**Still growing.** 77 stars (up from 66). Jenkins has hundreds of thousands of installations, but the MCP plugin is still building adoption. The community hasn't fully battle-tested it yet.

**No pipeline-specific tools.** The plugin handles jobs and builds generically but doesn't have tools specifically designed for Jenkins Pipeline (Jenkinsfile) stage-level analysis or shared library management. The replay tools help, but for complex Pipeline setups, you'll still need to parse logs manually.

---

## lanbaoshen/mcp-jenkins — The Standalone Alternative

[lanbaoshen/mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins) (115 stars, 46 forks, MIT) is a standalone Python MCP server for Jenkins. Unlike the official plugin, it runs outside Jenkins and connects via the REST API. Now at **v3.2.0** (April 21, 2026) with 27 total releases.

**24 tools** (up from 18) covering job management, node administration, build queue operations, build information retrieval (console output, test reports), and execution control (stop builds).

**Key differentiators:**
- Multiple transport options (stdio, SSE, streamable-http)
- Read-only mode for safe exploration
- SSL verification control
- JetBrains IDE and VS Code Copilot integration

Higher star count than the official plugin (115 vs. 77), suggesting the community continues to find value in a standalone approach. The rapid release cadence (27 releases) shows active maintenance.

**Also new in the Jenkins ecosystem:** [kud/mcp-jenkins](https://github.com/kud/mcp-jenkins) (3 stars, TypeScript, MIT) is a newer entrant with **37 tools** — the highest tool count of any Jenkins MCP server. It covers jobs, builds, nodes, views, and CI/CD workflows with multi-instance support (connect to multiple Jenkins servers simultaneously), tool filtering via allowlist/blocklist, and flexible auth (bearer tokens, basic auth, OAuth). Early-stage adoption but worth watching for teams wanting the broadest Jenkins API coverage from a single TypeScript server.

---

## CircleCI-Public/mcp-server-circleci — Diagnostic-First CI/CD

[CircleCI-Public/mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci) (84 stars, 57 forks, 303 commits, Apache 2.0) is the most thoughtfully designed CI/CD MCP server. Where GitHub's server treats CI/CD as one feature among many, CircleCI's server was built specifically for pipeline diagnostics.

**17 tools (up from 15), purpose-built for CI/CD:**

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
- **Prompt templates** — generation and evaluation tools (new)

**Deployment options expanded:** NPX-based local servers, Docker containers, and self-managed remote MCP servers. Supports Cursor, VS Code, Claude Desktop, Windsurf, Claude Code, and Amazon Q Developer.

### What works well

**Diagnostic depth.** `find_flaky_tests` alone is worth the integration. Flaky tests are one of the most frustrating CI problems — they pass sometimes, fail sometimes, and waste hours of developer time. Having an agent automatically surface flaky test patterns from historical data is genuinely useful.

**Resource optimization.** `find_underused_resource_classes` analyzes your pipeline resource usage and identifies where you're paying for compute you don't need. This is the only CI/CD MCP server that helps you save money, not just debug failures.

**Structured output.** `get_build_failure_logs` returns structured error summaries rather than dumping raw log output. This matters because CI logs can be thousands of lines — an agent needs structured data, not a wall of text.

### What doesn't

**CircleCI-only.** Obviously. If you're on GitHub Actions or Jenkins, this server is irrelevant. But the *approach* — diagnostic-first tooling with flaky test detection and resource optimization — is something every CI/CD MCP server should learn from.

**Moderate adoption.** 84 stars for an official vendor server is low. CircleCI has a smaller market share than GitHub Actions or Jenkins, which limits the audience.

---

## zereight/gitlab-mcp — The Community Standard

[zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) (1,400 stars, MIT) is the dominant community GitLab MCP server, now at **v2.1.2** (April 18, 2026). It covers far more than CI/CD — merge requests, issues, repositories, branches, projects, labels, releases, users — but includes a dedicated pipeline toolset.

**85+ tools across modular toolsets:**

- **Pipelines (12 tools)** — list, get details, trigger, retry, cancel, get job output
- **Merge requests (31 tools)** — the largest toolset
- **Issues (14 tools)** — full issue lifecycle
- **Repositories (7 tools)** — file access, commits
- **Work items (NEW)** — GraphQL-based work item management
- Plus branches, projects, labels, releases, milestones, wiki, emoji reactions

**What's new since March 2026:**
- **MCP OAuth mode** — native OAuth proxy and per-request remote authorization (v2.0.36+)
- **Code search tools** — search across repositories (v2.1.1)
- **Work items via GraphQL** — group-level work item management (v2.1.2)
- **Security hardening** — CSRF, XSS, and stdio log leak prevention (v2.0.35)
- **Auto-refresh OAuth tokens** on 401 responses (v2.1.2)
- **Group-level wiki support** and emoji reactions for MRs/issues

GitLab also has an **official MCP server** (`glab mcp serve`) that provides 250+ tools through their CLI, with OAuth 2.0 authentication. The official server is still marked as **experimental** ("not ready for production use") but offers the broadest tool coverage — though at a cost of ~25K context tokens.

### What works well

**Toolset architecture.** Like Salesforce's MCP server, gitlab-mcp uses a modular toolset system. You can enable only the pipeline toolset if CI/CD is all you need, keeping your agent's context focused. Default toolsets load ~60 tools; optional toolsets (pipelines, milestones, wiki) add more.

**Security improvements (NEW).** The v2.0.35+ releases added CSRF protection, XSS prevention, and stdio log leak fixes — important for a server that handles OAuth tokens. Auto-refresh on 401 responses means fewer authentication failures in long-running sessions.

**Read-only mode.** For CI/CD monitoring where you want to diagnose but not trigger, read-only mode prevents accidental pipeline triggers or merge request modifications.

**Multi-project support.** You can restrict which project IDs the server can access — useful when your GitLab instance has hundreds of projects but you only care about CI/CD for a few.

### What doesn't

**Community-maintained.** Not official GitLab. The official server exists with 250+ tools but is still experimental. If GitLab's official MCP server matures, this community server may become redundant — but the official server's 25K token footprint makes it impractical for many agents.

**CI/CD is secondary.** Pipelines are one of several optional toolsets. The server's primary focus is merge requests and issues. The pipeline tools cover the basics but lack the diagnostic depth of CircleCI's purpose-built server.

---

## microsoft/azure-devops-mcp — Enterprise CI/CD (Remote MCP Preview)

[microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) (1,600 stars, 524 forks, 499 commits, MIT) is Microsoft's official MCP server for Azure DevOps, now at **v2.6.0** (April 18, 2026). The biggest development: Microsoft launched a **Remote MCP Server in public preview** — a cloud-hosted version that eliminates local setup entirely.

**30+ tools across domains:**

- **Pipelines** — build status, trigger builds, view logs
- **Work items** — query, create, update
- **Repositories** — code access, PRs
- **Test plans** — test management and results
- **Wiki** — documentation access
- **Advanced security** — security findings (new domain)

**Key differentiators:**
- Domain-based tool filtering — load only the pipeline tools if that's all you need
- Built into Visual Studio 2026 — zero-setup for VS users
- Browser-based Microsoft authentication — Entra ID, no tokens to manage
- One-click VS Code installation
- GitHub Copilot Chat integration — auto-detects relevant Azure DevOps tools

**What's new — Remote MCP Server (public preview):**
Microsoft's Remote MCP Server (`https://mcp.dev.azure.com/{organization}`) uses streamable HTTP transport and provides the same capabilities as the local server without any local installation. This is a significant architectural shift — Microsoft has stated that **future investments will primarily focus on the remote experience** and plans to eventually archive the local server repository when the remote reaches GA. Currently supported in Visual Studio and VS Code, with Microsoft Foundry and Copilot Studio support coming.

### What works well

**Enterprise integration.** Azure DevOps is used in environments where compliance, audit trails, and access control matter. The MCP server inherits Azure's security model — Entra ID authentication, role-based access, domain scoping.

**Cloud-native direction (NEW).** The Remote MCP Server preview eliminates the "install npm, run npx" friction. Connect your AI assistant directly to the Azure DevOps endpoint — no local process management, no Docker, no version updates. This is where CI/CD MCP is heading.

**Broad coverage.** This isn't just CI/CD — it covers the entire Azure DevOps platform. An agent can connect a build failure to the work item it's associated with, check the test plan, and read the wiki documentation, all in one server.

### What doesn't

**Azure-only.** If you're not on Azure DevOps, this is irrelevant. And Azure DevOps has less MCP community momentum than GitHub.

**Remote server limitations.** The preview requires Entra-backed organizations (no standalone MSAs). Only VS and VS Code are supported as clients so far. The local server remains the more flexible option until the remote reaches GA.

---

## akuity/argocd-mcp — GitOps Deployment

[akuity/argocd-mcp](https://github.com/akuity/argocd-mcp) (401 stars, 68 forks, Apache 2.0) is the official MCP server for Argo CD, now at **v0.6.0** (March 25, 2026). Argo CD is the dominant GitOps continuous delivery tool for Kubernetes.

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

## buildkite/buildkite-mcp-server — The New Official Vendor (NEW)

[buildkite/buildkite-mcp-server](https://github.com/buildkite/buildkite-mcp-server) (50 stars, 31 forks, 529 commits, MIT) is Buildkite's **official MCP server**, hitting **v1.0.0 on March 30, 2026**. Written in Go, it exposes Buildkite data to AI tooling and editors.

**Tools cover four areas:**

- **Pipelines** — pipeline definitions and configuration
- **Builds** — build status, history, triggering
- **Jobs** — job logs, artifacts, status
- **Tests** — test results and analysis

**Key characteristics:**
- Built from Chainguard static image, runs as unprivileged user (container-first security)
- 34 releases — rapid iteration since initial launch
- Recommended to run in container environment
- Go-based (like GitHub's MCP server) — low memory footprint

### What works well

**Official vendor support.** Buildkite is a popular CI/CD platform among fast-moving teams (Shopify, Airbnb, PagerDuty). Having an official MCP server means the integration stays current with Buildkite's API changes.

**Production-ready.** v1.0.0 with 529 commits and 34 releases signals maturity despite the relatively low star count. The container-based deployment model is well-suited for teams already running containerized infrastructure.

### What doesn't

**Low adoption so far.** 50 stars. Buildkite's market share is smaller than GitHub Actions, Jenkins, or GitLab CI, which limits the audience.

**Less diagnostic depth.** Compared to CircleCI's purpose-built diagnostics (flaky test detection, resource optimization), Buildkite's server is more of a standard API bridge. The tools expose Buildkite data but don't add analytical intelligence on top.

---

## The cross-platform comparison

| Feature | GitHub MCP | Jenkins Plugin | Jenkins (lanbaoshen) | CircleCI | GitLab (zereight) | Azure DevOps | Buildkite | Argo CD |
|---------|-----------|---------------|---------------------|----------|-------------------|-------------|-----------|---------|
| Stars | 29,100 | 77 | 115 | 84 | 1,400 | 1,600 | 50 | 401 |
| CI/CD tools | ~5 | ~20 | 24 | 17 | 12 | 10+ | 4 areas | 12 |
| Flaky test detection | No | No | No | **Yes** | No | No | No | No |
| Resource optimization | No | No | No | **Yes** | No | No | No | No |
| Read-only mode | No | No | **Yes** | No | **Yes** | No | No | **Yes** |
| Official/vendor | **Yes** | **Yes** | No | **Yes** | No | **Yes** | **Yes** | **Yes** |
| Toolset filtering | **Yes** (NEW) | No | No | No | **Yes** | **Yes** | No | No |
| Cloud/remote option | **Yes** | No | No | **Yes** | No | **Yes** (preview) | No | No |
| Self-hosted support | N/A | **Yes** | **Yes** | Enterprise | **Yes** | **Yes** | N/A | **Yes** |
| Deployment tools | Limited | **Yes** (replay) | No | **Yes** | Limited | **Yes** | No | **Yes** |
| Language | Go | Java (plugin) | Python | TypeScript | TypeScript | TypeScript | Go | TypeScript |

## Which one should you use?

**Already on GitHub Actions?** Use [github/github-mcp-server](https://github.com/github/github-mcp-server). Now at v1.0.0 with toolset filtering — use `--toolsets` to load only CI/CD tools. One server, no additional setup.

**Running Jenkins?** You have four options. [lanbaoshen/mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins) (115 stars, 24 tools) is the most battle-tested standalone. The [official plugin](https://github.com/jenkinsci/mcp-server-plugin) (77 stars, ~20 tools) is best for native Jenkins integration with replay support. [kud/mcp-jenkins](https://github.com/kud/mcp-jenkins) (37 tools) has the broadest API coverage if you need it.

**On GitLab?** Use [zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) (v2.1.2) for the broadest coverage with new MCP OAuth mode and security hardening. GitLab's official MCP server (`glab mcp serve`) has 250+ tools but is still experimental and consumes ~25K context tokens.

**Using CircleCI?** The [official CircleCI MCP server](https://github.com/CircleCI-Public/mcp-server-circleci) is the obvious choice — now with 17 tools and the best diagnostic tooling of any CI/CD MCP server.

**Using Buildkite?** The [official Buildkite MCP server](https://github.com/buildkite/buildkite-mcp-server) just hit v1.0.0. Go-based, container-first, 34 releases. The newest official vendor entry in this category.

**On Azure DevOps?** Try the new [Remote MCP Server](https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server) preview (`https://mcp.dev.azure.com/{org}`) for zero-setup hosted access. Or use [microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) locally with Entra ID authentication. If you're on Visual Studio 2026, it's already built in.

**Using Argo CD for GitOps?** [akuity/argocd-mcp](https://github.com/akuity/argocd-mcp) (v0.6.0) for deployment monitoring and management. Pair it with a CI server for build-side visibility.

## Security considerations

CI/CD MCP servers are high-risk integrations:

- **Build triggers.** An agent that can trigger builds can trigger deployments. Scope credentials carefully — read-only access for monitoring, write access only when you explicitly need it.
- **Log exposure.** Build logs often contain environment variables, API keys, and internal URLs. Make sure your CI system redacts secrets from logs before exposing them through MCP.
- **Pipeline modification.** Some servers can modify pipeline configurations. A misconfigured pipeline can deploy broken code to production. Use read-only modes where available.
- **Token scope.** Use the narrowest possible token scope. A GitHub PAT with `repo` and `workflow` permissions can do a lot of damage if compromised. Prefer fine-grained tokens.

## The verdict

**Rating: 4.5/5** — The CI/CD MCP ecosystem is the strongest vendor-backed category we track, and it just got stronger. GitHub hit v1.0.0 with toolset filtering. Buildkite joined as the seventh official vendor server. Azure DevOps launched a cloud-hosted Remote MCP Server preview. Jenkins expanded to four competing servers. Every major CI/CD platform now has at least one official or high-quality MCP server.

What elevates this category: **official vendor investment keeps deepening**. GitHub, Jenkins, CircleCI, Microsoft, Buildkite, and Akuity all maintain official servers — and they're shipping real features, not just wrappers. GitHub's toolset filtering, Azure DevOps's cloud-native pivot, Jenkins's replay support, and CircleCI's diagnostic tools show vendors building MCP-native capabilities, not just API bridges.

What holds it back: fragmentation. Each server only works with its own platform. There's no cross-platform CI/CD MCP server that could monitor GitHub Actions, Jenkins, and GitLab pipelines from a single interface. If you use multiple CI systems, you need multiple MCP servers. The cloud-native shift (GitHub's remote server, Azure DevOps Remote MCP) may eventually solve the setup friction but doesn't solve the cross-platform problem.

The strongest individual server is GitHub MCP (29,100 stars, v1.0.0, toolset filtering). The most innovative is CircleCI's (flaky test detection, resource optimization, 17 diagnostic tools). The deepest self-hosted ecosystem is Jenkins (4 servers, up to 37 tools). The broadest community server is GitLab's zereight/gitlab-mcp (1,400 stars, 85+ tools, MCP OAuth, security hardening). The most enterprise-integrated is Azure DevOps (Remote MCP preview, Visual Studio 2026 built-in, Entra ID auth).

*Reviewed by [ChatForest](https://chatforest.com). We research MCP servers by reading source code, documentation, GitHub issues, and community discussions. For our methodology, see [How We Review](/about/).*

*This review was last refreshed on 2026-04-21 using Claude Opus 4.6 (Anthropic).*
