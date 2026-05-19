---
title: "CI/CD MCP Servers — GitHub Actions, Jenkins, GitLab CI, CircleCI, and Beyond"
date: 2026-03-15T02:30:00+09:00
description: "CI/CD MCP servers let AI agents trigger builds, diagnose failures, analyze logs, and manage pipelines across GitHub Actions, Jenkins, GitLab CI, CircleCI, Azure DevOps, Buildkite, and Argo CD."
og_description: "CI/CD MCP servers: GitHub MCP v1.0.5 (30K stars), Jenkins now 5 servers, GitLab v2.1.12 (40% payload cut, audit logging), Argo CD 467 stars (+16%), TeamCity new entrant. Rating: 4.5/5."
content_type: "Review"
card_description: "CI/CD MCP servers across GitHub Actions, Jenkins, GitLab CI, CircleCI, Azure DevOps, Buildkite, Argo CD, and now TeamCity. GitHub v1.0.5 adds collaborators + discussion writes; GitLab v2.1.12 adds audit logging and 40% payload reduction; Argo CD grows 16% in 30 days."
last_refreshed: 2026-05-20
---

CI/CD pipelines are the backbone of modern software delivery. When they break, development stops. Giving an AI agent access to your build system — to read logs, diagnose failures, trigger rebuilds, and analyze flaky tests — is one of the highest-value MCP integrations you can set up.

The CI/CD MCP landscape continues to mature. GitHub's official server is now at v1.0.5 with five patch releases since hitting v1.0.0 in April. GitLab's community server hit v2.1.12 with a major capability leap: 40% payload reduction, audit logging, dynamic tool discovery, and tool policy controls. Argo CD grew 16.5% in 30 days — the fastest-growing server in this category. Jenkins expanded to five servers with two new entrants. TeamCity joins as a new platform with a 31–87 tool server supporting runtime mode switching. Here's the full picture.

**Category:** [Developer Tools](/categories/developer-tools/)

## The Landscape

### GitHub Actions

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | 30,000 | Go | 40+ (incl. Actions) | GitHub PAT / OAuth | MIT |
| [ko1ynnky/github-actions-mcp-server](https://github.com/ko1ynnky/github-actions-mcp-server) | ~2 | TypeScript | Actions-only | GitHub PAT | — |
| [onemarc/github-actions-mcp-server](https://github.com/onemarc/github-actions-mcp-server) | — | TypeScript | Actions-only | GitHub PAT | — |

### Jenkins

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [jenkinsci/mcp-server-plugin](https://github.com/jenkinsci/mcp-server-plugin) | 83 | Java | ~20 | Jenkins API token | MIT |
| [lanbaoshen/mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins) | 121 | Python | 26+ | API token / OAuth / LDAP | MIT |
| [kud/mcp-jenkins](https://github.com/kud/mcp-jenkins) | 7 | TypeScript | 37 | Bearer / Basic / OAuth | MIT |
| [LokiMCPUniverse/jenkins-mcp-server](https://github.com/LokiMCPUniverse/jenkins-mcp-server) | 4 | Python | 20+ | API token / OAuth | — |
| [Jordan-Jarvis/jenkins-mcp-enterprise](https://github.com/Jordan-Jarvis/jenkins-mcp-enterprise) | 29 | Python | — | — | GPL v3 |

### GitLab CI

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [GitLab official MCP server](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server/) | — | — | 250+ (experimental) | OAuth 2.0 / PAT | — |
| [zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) | 1,500 | TypeScript | 85+ | PAT / OAuth2 / MCP OAuth | MIT |
| [Vijay-Duke/mcp-gitlab](https://github.com/Vijay-Duke/mcp-gitlab) | — | — | — | PAT | — |

### CircleCI

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [CircleCI-Public/mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci) | 84 | TypeScript | 17 | CircleCI token | Apache 2.0 |

### Buildkite

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [buildkite/buildkite-mcp-server](https://github.com/buildkite/buildkite-mcp-server) | 49 | Go | Pipelines, builds, jobs, tests | Buildkite API token | MIT |

### Azure DevOps

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) | 1,700 | TypeScript | 30+ | Microsoft Entra ID | MIT |
| [Azure DevOps Remote MCP](https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server) | — | Hosted | Same as local | Entra ID | — |
| [Vortiago/mcp-azure-devops](https://github.com/Vortiago/mcp-azure-devops) | 80 | Python | 10+ | PAT | MIT |

### Argo CD (GitOps)

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [akuity/argocd-mcp](https://github.com/akuity/argocd-mcp) | 467 | TypeScript | 12 | Argo CD auth token | Apache 2.0 |

### TeamCity (NEW)

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [Daghis/teamcity-mcp](https://github.com/Daghis/teamcity-mcp) | 25 | TypeScript | 31–87 | TeamCity API token | — |

GitHub's official MCP server remains the clear leader — now at v1.0.5 with five patch releases since v1.0.0. Jenkins has the deepest ecosystem with five servers. Buildkite is a stable official vendor entry. Azure DevOps is pioneering the cloud-native approach with a hosted Remote MCP Server still in public preview. CircleCI still has the best diagnostic-first tooling. Argo CD's 16.5% star growth in 30 days is the strongest momentum signal in this category.

## github/github-mcp-server — The Platform Play (v1.0.5)

[github/github-mcp-server](https://github.com/github/github-mcp-server) (30,000 stars, 4,000 forks, MIT) hit v1.0.0 on April 16, 2026, and has shipped five patch releases since. Now at **v1.0.5 (May 18, 2026)** with 852 commits total. It covers repositories, issues, PRs, code search, and — critically — GitHub Actions workflows.

**Actions-specific capabilities:**

- **get_job_logs** — retrieve workflow job logs for debugging failed builds
- **list_workflow_runs** — check workflow status across branches
- **Deployment management** — track deployments and releases
- **set_issue_fields** — granular issue field control

**What's new since April 21, 2026:**
- **v1.0.5** (May 18) — list repository collaborators; discussion comment write operations; pagination for `get_reviews`; code search returns minimal results with text match snippets; go-github upgraded to v0.87
- **v1.0.4** (May 11) — fixed Dependabot error messaging; handled lightweight tags
- **v1.0.3** (Apr 24) — fixed lockdown mode permission check
- **v1.0.2** (Apr 22) — fixed `set_issue_fields` mutation
- **v1.0.1** (Apr 21) — fixed Content-Type rejection; restored browser-based client support
- **Toolset filtering** — `--toolsets` flag and `--exclude-tools` flag let you load only the tools you need
- **Scope-based filtering** — OAuth tokens automatically hide tools you can't use; classic PATs filter out inaccessible tools
- **Remote server** — `https://api.githubcopilot.com/mcp/` for hosted access (no local Docker needed)
- **Enterprise support** — GitHub Enterprise Server and Enterprise Cloud with data residency

### What works well

**Platform integration.** The power isn't in any single CI/CD tool — it's that your agent can connect a failing build to the PR that caused it, check the commit diff, read the error logs, and suggest a fix, all within one server. No context switching between separate CI/CD and version control MCP servers.

**Massive adoption.** 30,000 stars, 4,000 forks, 852 commits. This is the most widely deployed MCP server after Anthropic's reference implementations. Bugs get found and fixed quickly — five patch releases in five weeks demonstrates the response cadence.

**Toolset filtering.** The `--toolsets` and `--exclude-tools` flags address the biggest complaint from our original review: you can now load only CI/CD-related tools instead of all 40+. Scope-based filtering automatically hides tools your token can't access.

**Official maintenance.** GitHub actively develops this — 37+ releases since launch. The dedicated Actions MCP servers (ko1ynnky, onemarc) are being archived because the official server absorbed their functionality.

### What doesn't

**Limited diagnostic depth.** You can get job logs, but there's no built-in flaky test detection, no failure pattern analysis, no resource optimization suggestions. Compare this to CircleCI's MCP server, which was built specifically for CI/CD diagnostics.

**No workflow authoring.** You can monitor and trigger workflows, but you can't create or edit workflow YAML files through the MCP server. For pipeline configuration, you're still editing files manually.

---

## jenkinsci/mcp-server-plugin — The Official Plugin

[jenkinsci/mcp-server-plugin](https://github.com/jenkinsci/mcp-server-plugin) (83 stars, 51 forks, MIT) runs *inside* Jenkins as a native plugin. This is architecturally different from every other CI/CD MCP server — instead of an external process calling Jenkins's REST API, the MCP server is part of Jenkins itself.

**~20 tools across five categories:**

- **Job management** — getJob, getJobs, triggerBuild, getQueueItem
- **Build information** — getBuild, updateBuild, getBuildLog, searchBuildLog, rebuildBuild, getTestResults
- **Replay** — getReplayScripts, replayBuild
- **SCM integration** — getJobScm, getBuildScm, getBuildChangeSets, findJobsWithScmUrl
- **System** — whoAmI, getStatus

**What's new since April 21, 2026:** Release 0.172.v9db_cb_43cdb_cc (May 9) — authentication refactoring (replaced `User` with `Authentication`), dependency bumps (Swagger 2.2.49, BouncyCastle 2.30.1.84). The plugin continues shipping steady maintenance releases on Jenkins's rolling update cadence.

**Transport options:** SSE, Streamable HTTP, and stateless endpoints. Note: GitHub Copilot currently has compatibility issues with Streamable transport — use SSE instead.

**Install:** Install through Jenkins Plugin Manager. Authenticate with Jenkins API tokens. Requires Jenkins 2.533+.

### What works well

**Native integration.** Because it runs inside Jenkins, it has direct access to everything — no API rate limits, no network latency, no credential management headaches. The plugin sees exactly what Jenkins sees.

**SCM correlation.** The `findJobsWithScmUrl` tool lets an agent find all jobs associated with a specific repository. The `getBuildChangeSets` tool connects builds to commits. This is the kind of cross-referencing that's tedious to do manually but trivial for an agent.

**Extensible architecture.** The `McpServerExtension` interface lets other Jenkins plugins expose their own MCP tools. This means the ecosystem can grow without the core plugin becoming monolithic.

**Replay support.** The `replayBuild` and `getReplayScripts` tools let an agent replay a build with modified Groovy scripts — useful for debugging Pipeline issues without committing code changes.

### What doesn't

**Still growing.** 83 stars (up from 77). Jenkins has hundreds of thousands of installations, but the MCP plugin is still building adoption.

**No pipeline-specific tools.** The plugin handles jobs and builds generically but doesn't have tools specifically designed for Jenkins Pipeline (Jenkinsfile) stage-level analysis or shared library management.

---

## lanbaoshen/mcp-jenkins — The Standalone Alternative

[lanbaoshen/mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins) (121 stars, 46 forks, MIT) is a standalone Python MCP server for Jenkins. Unlike the official plugin, it runs outside Jenkins and connects via the REST API. Now at **v3.3.0** (May 6, 2026) with 28 total releases.

**26+ tools** covering job management, node administration, build queue operations, build information retrieval (console output, test reports), artifact access, and execution control.

**What's new since April 21, 2026:**
- **v3.3.0** (May 6) — fixed HTTP 414 error when sending large build parameters; **added artifact support** — agents can now access and retrieve build artifacts directly
- **v3.2.0** (Apr 21) — plugin management tools: retrieve all plugins, identify problematic plugins, visualize plugin dependency graphs

**Key differentiators:**
- Multiple transport options (stdio, SSE, streamable-http)
- Read-only mode for safe exploration
- SSL verification control
- JetBrains IDE and VS Code Copilot integration
- Built on fastmcp v3 (migrated in v3.0.0)

Higher star count than the official plugin (121 vs. 83), showing continued community preference for the standalone approach.

**Also in the Jenkins ecosystem:** [kud/mcp-jenkins](https://github.com/kud/mcp-jenkins) (7 stars, TypeScript, MIT) has **37 tools** — the highest tool count of any Jenkins MCP server — with multi-instance support, allowlist/blocklist tool filtering, and flexible auth. Early adoption but worth watching.

**New entrant: [Jordan-Jarvis/jenkins-mcp-enterprise](https://github.com/Jordan-Jarvis/jenkins-mcp-enterprise)** (29 stars, v1.0.3 May 3, GPL v3) takes an enterprise-focused approach with **multi-instance Jenkins management**, AI-powered build failure analysis, and vector-based semantic search across build history. 10 forks already — higher adoption signal than its star count suggests. Python-based, open source.

---

## CircleCI-Public/mcp-server-circleci — Diagnostic-First CI/CD

[CircleCI-Public/mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci) (84 stars, 57 forks, 308 commits, Apache 2.0) is the most thoughtfully designed CI/CD MCP server. Where GitHub's server treats CI/CD as one feature among many, CircleCI's server was built specifically for pipeline diagnostics. Now at **v0.15.1** (last updated April 21, 2026 — no new releases since last review).

**17 tools, purpose-built for CI/CD:**

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
- **listArtifacts** — retrieve build artifacts
- **Prompt templates** — generation and evaluation tools

**Deployment options:** NPX-based local servers, Docker containers, and self-managed remote MCP servers. Supports Cursor, VS Code, Claude Desktop, Windsurf, Claude Code, and Amazon Q Developer.

### What works well

**Diagnostic depth.** `find_flaky_tests` alone is worth the integration. Flaky tests are one of the most frustrating CI problems — they pass sometimes, fail sometimes, and waste hours of developer time. Having an agent automatically surface flaky test patterns from historical data is genuinely useful.

**Resource optimization.** `find_underused_resource_classes` analyzes your pipeline resource usage and identifies where you're paying for compute you don't need. This is the only CI/CD MCP server that helps you save money, not just debug failures.

**Structured output.** `get_build_failure_logs` returns structured error summaries rather than dumping raw log output. This matters because CI logs can be thousands of lines — an agent needs structured data, not a wall of text.

### What doesn't

**CircleCI-only.** Obviously. If you're on GitHub Actions or Jenkins, this server is irrelevant. But the *approach* — diagnostic-first tooling with flaky test detection and resource optimization — is something every CI/CD MCP server should learn from.

**Flat adoption.** 84 stars for an official vendor server, unchanged in 30 days. CircleCI has a smaller market share than GitHub Actions or Jenkins, which limits the audience.

---

## zereight/gitlab-mcp — The Community Standard (v2.1.12)

[zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) (1,500 stars, MIT) is the dominant community GitLab MCP server, now at **v2.1.12** (May 17, 2026). It covers far more than CI/CD — merge requests, issues, repositories, branches, projects, labels, releases, users — but includes a dedicated pipeline toolset.

**85+ tools across modular toolsets:**

- **Pipelines (12 tools)** — list, get details, trigger, retry, cancel, get job output
- **Merge requests (31 tools)** — the largest toolset
- **Issues (14 tools)** — full issue lifecycle
- **Repositories (7 tools)** — file access, commits
- **Work items** — GraphQL-based work item management
- Plus branches, projects, labels, releases, milestones, wiki, emoji reactions, code search

**What's new since April 21, 2026 — major capability leap:**
- **~40% payload reduction per tool** — stripping schema metadata from tool responses; agents consume significantly less context per call
- **Tool annotations** — `readOnlyHint`, `destructiveHint`, `confirmationHint`, `openWorldHint` added to all tools; MCP clients can now display confirmation prompts before destructive operations
- **Policy controls** — `GITLAB_TOOL_POLICY_APPROVE` and `GITLAB_TOOL_POLICY_HIDDEN` env vars let admins restrict which tools are visible or require confirmation; enterprise-grade access control without code changes
- **Dynamic tool discovery** — `discover_tools` meta-tool for on-demand toolset activation; start with a minimal tool footprint and expand as needed
- **Audit logging** — structured logs for every tool execution with duration metrics; compliance-ready for regulated environments
- **Security hardening** — refuses unauthenticated Streamable HTTP startup when server-side token is configured
- **Code search tools** — search across repositories (v2.1.1)
- **Auto-refresh OAuth tokens** on 401 responses (v2.1.2)

GitLab also has an **official MCP server** (`glab mcp serve`) providing 250+ tools with OAuth 2.0 authentication. Still marked **experimental** — not ready for production use — and carries a ~25K context token footprint that makes it impractical for many agents.

### What works well

**The v2.1.x improvements are substantial.** The 40% payload reduction isn't cosmetic — it means an agent can invoke more tools before hitting context limits. Audit logging means security-conscious teams can actually use this in regulated environments. Policy controls mean admins can restrict what agents can do without forking the server.

**Tool annotations.** The MCP spec's tool annotation hints (`destructiveHint`, `confirmationHint`) are now implemented across all tools. Clients that support these annotations will automatically surface confirmation dialogs before an agent does something irreversible.

**Dynamic tool discovery.** Starting with a minimal toolset and activating more on demand is a meaningful UX improvement — it keeps context clean without sacrificing coverage.

**Toolset architecture.** Modular toolsets mean you can enable only the pipeline toolset if CI/CD is all you need. Default toolsets load ~60 tools; optional toolsets (pipelines, milestones, wiki) add more.

**Security hardening.** The CSRF, XSS, and stdio log leak fixes from prior releases, combined with new auth-required startup enforcement, make this server meaningfully more secure than it was in March.

### What doesn't

**Community-maintained.** Not official GitLab. The official server exists with 250+ tools but is still experimental. If GitLab's official MCP server matures, this community server may become redundant.

**CI/CD is secondary.** Pipelines are one of several optional toolsets. The server's primary focus is merge requests and issues. The pipeline tools cover the basics but lack the diagnostic depth of CircleCI's purpose-built server.

---

## microsoft/azure-devops-mcp — Enterprise CI/CD (Remote MCP Preview)

[microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) (1,700 stars, 524 forks, MIT) is Microsoft's official MCP server for Azure DevOps, now at **v2.7.0** (April 23, 2026). The biggest development: Microsoft's **Remote MCP Server** remains in **public preview** — a cloud-hosted version that eliminates local setup entirely.

**30+ tools across domains:**

- **Pipelines** — build status, trigger builds, view logs
- **Work items** — query, create, update
- **Repositories** — code access, PRs
- **Test plans** — test management and results
- **Wiki** — documentation access
- **Advanced security** — security findings

**Key differentiators:**
- Domain-based tool filtering — load only the pipeline tools if that's all you need
- Built into Visual Studio 2026 — zero-setup for VS users
- Browser-based Microsoft authentication — Entra ID, no tokens to manage
- One-click VS Code installation
- GitHub Copilot Chat integration — auto-detects relevant Azure DevOps tools

**What's new since April 21:** v2.7.0 (Apr 23) — character validation improvements in work items markdown handling; removed default value for work item field format; dependency bumps to @azure/msal-node. Steady maintenance, no major capability additions. Remote MCP Server remains public preview; Microsoft has stated future investments will primarily focus on the remote experience and plans to eventually archive the local server repository when the remote reaches GA.

### What works well

**Enterprise integration.** Azure DevOps is used in environments where compliance, audit trails, and access control matter. The MCP server inherits Azure's security model — Entra ID authentication, role-based access, domain scoping.

**Cloud-native direction.** The Remote MCP Server preview eliminates the "install npm, run npx" friction. Connect your AI assistant directly to `https://mcp.dev.azure.com/{org}` — no local process management, no Docker, no version updates. This is where CI/CD MCP is heading.

**Broad coverage.** This isn't just CI/CD — it covers the entire Azure DevOps platform. An agent can connect a build failure to the work item it's associated with, check the test plan, and read the wiki documentation, all in one server.

### What doesn't

**Azure-only.** If you're not on Azure DevOps, this is irrelevant.

**Remote server limitations.** The preview requires Entra-backed organizations (no standalone MSAs). Only VS and VS Code are supported as clients so far. The local server remains the more flexible option until the remote reaches GA.

---

## akuity/argocd-mcp — GitOps Deployment (Fastest Growing)

[akuity/argocd-mcp](https://github.com/akuity/argocd-mcp) (467 stars, 68 forks, Apache 2.0) is the official MCP server for Argo CD, now at **v0.7.0** (May 2, 2026). Up from 401 stars in 30 days — **+16.5%**, the strongest growth rate in this category. Argo CD is the dominant GitOps continuous delivery tool for Kubernetes.

**12 tools in two categories:**

- **Application management** — list, get, create, update, delete, sync applications
- **Resource management** — get resource tree, managed resources, workload logs, events, resource actions, run resource actions

**What's new since April 21:**
- **v0.7.0** (May 2) — added **stateless mode** for horizontal pod autoscaling (HPA) in Kubernetes deployments; added **healthz endpoint** in HTTP mode. The stateless mode is architecturally significant — it enables running the MCP server at scale in Kubernetes without session affinity requirements.

### What works well

**Deployment clarity.** For teams using GitOps, the ability to ask an agent "what's the sync status of the production app?" or "show me the resource tree for staging" is immediately useful. The `sync_application` tool triggers deployments through Argo CD's reconciliation model.

**Scalability (NEW).** Stateless mode + HPA support means you can run this server at production scale in Kubernetes — load balanced across replicas. The only CI/CD MCP server in this roundup designed for horizontal scaling.

**Read-only mode.** You can run the server in read-only mode for monitoring without the risk of triggering unintended syncs or deletions.

### What doesn't

**Narrow scope.** 12 tools. No CI integration, no build monitoring, no test analysis. This is purely a CD server. You'll need a separate CI MCP server (GitHub, Jenkins, CircleCI) alongside this.

**Kubernetes-only.** Argo CD runs on Kubernetes. If your deployments don't involve K8s, this server isn't relevant.

---

## buildkite/buildkite-mcp-server — The Official Vendor Entry (v1.1.0)

[buildkite/buildkite-mcp-server](https://github.com/buildkite/buildkite-mcp-server) (49 stars, 31 forks, 537 commits, MIT) is Buildkite's **official MCP server**, now at **v1.1.0** (May 19, 2026) — 35 total releases since v1.0.0 in March. Written in Go.

**Tools cover four areas:**

- **Pipelines** — pipeline definitions and configuration
- **Builds** — build status, history, triggering
- **Jobs** — job logs, artifacts, status
- **Tests** — test results and analysis

**What's new since April 21:**
- **v1.1.0** (May 19) — extended annotation options; upgraded all dependencies; refactored pipeline to use mise
- Built from Chainguard static image, runs as unprivileged user (container-first security)

### What works well

**Official vendor support.** Buildkite is a popular CI/CD platform among fast-moving teams (Shopify, Airbnb, PagerDuty). Having an official MCP server means the integration stays current with Buildkite's API changes.

**Production-ready.** 537 commits and 35 releases signals maturity despite the relatively low star count.

### What doesn't

**Low adoption.** 49 stars — essentially flat over 30 days. Buildkite's market share is smaller than GitHub Actions, Jenkins, or GitLab CI.

**Less diagnostic depth.** Compared to CircleCI's purpose-built diagnostics (flaky test detection, resource optimization), Buildkite's server is more of a standard API bridge.

---

## Daghis/teamcity-mcp — TeamCity Joins the Category (NEW)

[Daghis/teamcity-mcp](https://github.com/Daghis/teamcity-mcp) (25 stars, TypeScript) is JetBrains TeamCity's MCP server — a new entrant that fills the last major CI/CD gap. TeamCity powers significant enterprise CI/CD (JetBrains' own build infrastructure, among others) and now has MCP coverage.

**Two operating modes:**

- **Dev mode** — 31 tools, ~14K context tokens: essential build/test/agent operations
- **Full mode** — 87 tools, ~26K context tokens: comprehensive TeamCity API coverage
- **Runtime mode switching** — change between Dev and Full without server restart

The runtime mode switching is a thoughtful feature: start agents in Dev mode for routine operations, switch to Full when you need the breadth of coverage.

**Supports TeamCity 2020.1+.** Integrates with Claude Code, Cursor, and Windsurf. Node.js 20+ required.

### What works well

**Fills the last major gap.** GitHub Actions, Jenkins, GitLab, CircleCI, Azure DevOps, Buildkite, and Argo CD were all covered. TeamCity was the missing major platform. Now every significant CI/CD system has at least one MCP server.

**Tiered mode design.** The Dev/Full mode distinction is a practical solution to the context window problem. Many MCP servers overwhelm agents with tools by default; TeamCity's server makes the tradeoff explicit and user-controllable.

### What doesn't

**New and unvalidated.** 25 stars, no formal releases yet. The server may work well, but community testing is limited.

**Not official.** JetBrains doesn't maintain this — it's a community contribution. If TeamCity changes APIs significantly, maintenance depends on the community.

---

## The cross-platform comparison

| Feature | GitHub MCP | Jenkins Plugin | Jenkins (lanbaoshen) | CircleCI | GitLab (zereight) | Azure DevOps | Buildkite | Argo CD | TeamCity |
|---------|-----------|---------------|---------------------|----------|-------------------|-------------|-----------|---------|---------|
| Stars | 30,000 | 83 | 121 | 84 | 1,500 | 1,700 | 49 | 467 | 25 |
| CI/CD tools | ~5 | ~20 | 26+ | 17 | 12 | 10+ | 4 areas | 12 | 31–87 |
| Flaky test detection | No | No | No | **Yes** | No | No | No | No | No |
| Resource optimization | No | No | No | **Yes** | No | No | No | No | No |
| Read-only mode | No | No | **Yes** | No | **Yes** | No | No | **Yes** | No |
| Official/vendor | **Yes** | **Yes** | No | **Yes** | No | **Yes** | **Yes** | **Yes** | No |
| Toolset filtering | **Yes** | No | No | No | **Yes** | **Yes** | No | No | **Yes** (modes) |
| Cloud/remote option | **Yes** | No | No | **Yes** | No | **Yes** (preview) | No | No | No |
| Self-hosted support | N/A | **Yes** | **Yes** | Enterprise | **Yes** | **Yes** | N/A | **Yes** | **Yes** |
| Deployment tools | Limited | **Yes** (replay) | No | **Yes** | Limited | **Yes** | No | **Yes** | No |
| Audit logging | No | No | No | No | **Yes** (NEW) | No | No | No | No |
| HPA/stateless | No | No | No | No | No | No | No | **Yes** (NEW) | No |
| Language | Go | Java (plugin) | Python | TypeScript | TypeScript | TypeScript | Go | TypeScript | TypeScript |

## Which one should you use?

**Already on GitHub Actions?** Use [github/github-mcp-server](https://github.com/github/github-mcp-server). Now at v1.0.5 — five patch releases since v1.0.0, active maintenance, list collaborators and discussion writes added. Use `--toolsets` to load only CI/CD tools.

**Running Jenkins?** You have five options. [lanbaoshen/mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins) (v3.3.0, artifact support, 121 stars) is the most battle-tested standalone. The [official plugin](https://github.com/jenkinsci/mcp-server-plugin) (83 stars, ~20 tools) is best for native Jenkins integration with replay support. [Jordan-Jarvis/jenkins-mcp-enterprise](https://github.com/Jordan-Jarvis/jenkins-mcp-enterprise) is worth evaluating for multi-instance setups needing AI-powered failure analysis.

**On GitLab?** Use [zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) (v2.1.12, 1,500 stars) — the v2.1.x updates are substantial: 40% payload reduction, audit logging, policy controls, dynamic tool discovery, and tool annotations. GitLab's official MCP server (`glab mcp serve`) has 250+ tools but is still experimental and consumes ~25K context tokens.

**Using CircleCI?** The [official CircleCI MCP server](https://github.com/CircleCI-Public/mcp-server-circleci) is the obvious choice — 17 diagnostic tools, the best flaky test detection of any CI/CD MCP server. No new releases since April 21, but it remains the category's most intelligent server.

**Using Buildkite?** The [official Buildkite MCP server](https://github.com/buildkite/buildkite-mcp-server) is at v1.1.0 (May 19). Go-based, container-first, 35 releases.

**On Azure DevOps?** Try the [Remote MCP Server](https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server) preview (`https://mcp.dev.azure.com/{org}`) for zero-setup hosted access. Or use [microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) locally.

**Using Argo CD for GitOps?** [akuity/argocd-mcp](https://github.com/akuity/argocd-mcp) (v0.7.0, 467 stars) with new stateless mode for Kubernetes-scale deployments. Pair it with a CI server for build-side visibility.

**On TeamCity?** [Daghis/teamcity-mcp](https://github.com/Daghis/teamcity-mcp) is the only option — early-stage but architecturally sensible. The Dev/Full mode design is worth the experiment.

## Security considerations

CI/CD MCP servers are high-risk integrations:

- **Build triggers.** An agent that can trigger builds can trigger deployments. Scope credentials carefully — read-only access for monitoring, write access only when you explicitly need it.
- **Log exposure.** Build logs often contain environment variables, API keys, and internal URLs. Make sure your CI system redacts secrets from logs before exposing them through MCP.
- **Pipeline modification.** Some servers can modify pipeline configurations. A misconfigured pipeline can deploy broken code to production. Use read-only modes where available.
- **Token scope.** Use the narrowest possible token scope. A GitHub PAT with `repo` and `workflow` permissions can do a lot of damage if compromised. Prefer fine-grained tokens.
- **Tool policy controls.** GitLab's new `GITLAB_TOOL_POLICY_APPROVE` and `GITLAB_TOOL_POLICY_HIDDEN` env vars are the first implementation of MCP-level policy enforcement in this category. Worth watching as a pattern for other servers.

## The verdict

**Rating: 4.5/5** — The CI/CD MCP ecosystem remains the strongest vendor-backed category we track. GitHub's five post-v1.0.0 patches show production-quality maintenance. GitLab's zereight server had its biggest capability release since launch: 40% payload reduction, audit logging, policy controls, and dynamic tool discovery make it meaningfully more enterprise-ready. Argo CD grew 16.5% in 30 days — the fastest momentum in the category. TeamCity coverage fills the last major CI/CD gap. Jenkins now has five servers including an enterprise-grade entrant with AI-powered failure analysis and vector search.

The category's structural strengths hold: official vendor investment from GitHub, Jenkins, CircleCI, Microsoft, Buildkite, and Akuity. Real feature development — not just API bridges. The 40% payload reduction in GitLab's server and stateless scaling in Argo CD show MCP-native thinking, not just wrappers.

What still holds it back: fragmentation. No cross-platform CI/CD MCP server monitors GitHub Actions, Jenkins, and GitLab pipelines from a single interface. If you use multiple CI systems, you need multiple MCP servers. Azure DevOps Remote MCP remains in public preview. And CircleCI — which has the category's best diagnostic tooling — has had no new releases since April 21, a worrying sign for the platform overall.

The strongest individual server is GitHub MCP (30,000 stars, v1.0.5, active maintenance). The most innovative is CircleCI's (flaky test detection, resource optimization). The deepest self-hosted ecosystem is Jenkins (five servers, up to 87 tools including TeamCity's Dev mode). The most-improved this cycle is GitLab's zereight/gitlab-mcp (v2.1.12, audit logging, 40% payload reduction). The fastest growing is Argo CD (+16.5%, stateless scaling).

*Reviewed by [ChatForest](https://chatforest.com). We research MCP servers by reading source code, documentation, GitHub issues, and community discussions. For our methodology, see [How We Review](/about/).*

*This review was last refreshed on 2026-05-20 using Claude Sonnet 4.6 (Anthropic).*
