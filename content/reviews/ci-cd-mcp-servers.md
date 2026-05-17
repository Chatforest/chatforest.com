---
draft: true
title: "CI/CD MCP Servers — Build Pipelines Get an AI Interface"
date: 2026-03-23T22:00:00+09:00
description: "CI/CD MCP ecosystem maturing: Buildkite v1.0.0, Argo CD 415 stars, GitHub Actions now official (29.4k stars), NEW TeamCity (87 tools), Azure DevOps (480 commits). Rating: 3.5/5."
og_description: "CI/CD MCP ecosystem: Buildkite v1.0.0, Argo CD 415 stars +17%, GitHub Actions official in github-mcp-server 29.4k stars, NEW TeamCity 87 tools, Azure DevOps 480 commits. Jenkins 4 servers. Rating: 3.5/5."
content_type: "Review"
card_description: "CI/CD MCP servers are maturing fast. Buildkite reached v1.0.0 with cluster management. Argo CD grew to 415 stars. GitHub Actions is now official in the GitHub MCP server (29.4k stars). NEW platforms: TeamCity (87 tools in full mode), Azure DevOps (480 commits). Jenkins now has 4 competing servers. CircleCI added OpenTelemetry. The ecosystem is broadening from observation to operation."
last_refreshed: 2026-04-30
---

**At a glance:** The CI/CD MCP ecosystem is maturing fast. **Buildkite reached v1.0.0** with cluster management and build workflow tools. **Argo CD surged to 415 stars** (+17%), the clear community leader. **GitHub Actions is now officially supported** in the [GitHub MCP server](/reviews/github-mcp-server/) (29.4k stars) via the `actions` toolset — the standalone server is archived. **Two new platforms joined**: [Daghis/teamcity-mcp](https://github.com/Daghis/teamcity-mcp) (24 stars, 87 tools in full mode) brings JetBrains TeamCity, and [Jordiag/azure-devops-mcp-server](https://github.com/Jordiag/azure-devops-mcp-server) (14 stars, 480 commits) covers Azure DevOps pipelines. Jenkins now has **four competing servers** including [Jordan-Jarvis/jenkins-mcp-enterprise](https://github.com/Jordan-Jarvis/jenkins-mcp-enterprise) (27 stars) with AI-powered failure diagnostics. The community leader [lanbaoshen/mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins) grew to 117 stars with 25 tools. CircleCI added OpenTelemetry metrics tracking. This is the **sixth review in our [Developer Tools MCP category](/categories/developer-tools/)**.

CI/CD is one of the most automation-heavy domains in software engineering — yet the MCP ecosystem for build pipelines is catching up. While [GitHub](/reviews/github-mcp-server/) has 29.4k stars on its MCP server and [Kubernetes](/reviews/kubernetes-mcp-servers/) has two servers above 1,000 stars, the top CI/CD-specific MCP server (Argo CD) has grown to 415 stars — up 17% in five weeks. The gap is closing as platforms ship official servers, community projects mature, and new platforms (TeamCity, Azure DevOps) enter the ecosystem. CI/CD platforms are complex stateful systems where a wrong API call can deploy broken code to production, cancel critical builds, or expose secrets in build logs — but the safety story is improving, with Buildkite proactively removing dangerous delete tools.

**Architecture note:** CI/CD MCP servers divide into two camps: **build system observers** (read logs, diagnose failures, check pipeline status) and **pipeline operators** (trigger builds, cancel runs, manage deployments). The balance is shifting toward operation — Buildkite v1.0.0 added cancel/rebuild/retry tools, CircleCI now tracks tool usage via OpenTelemetry, and Jenkins Enterprise offers AI-powered failure diagnostics. The ecosystem is moving from "what happened?" to "fix it."

## What's Available

### Jenkins — Official Plugin + Three Community Servers

Jenkins dominates CI/CD with **~47% market share** and **11.26 million developers**. It now has an official MCP plugin and three community servers — the most competitive sub-ecosystem in CI/CD MCP:

**jenkinsci/mcp-server-plugin (Official)**

| Aspect | Detail |
|--------|--------|
| Repository | [jenkinsci/mcp-server-plugin](https://github.com/jenkinsci/mcp-server-plugin) |
| Stars | ~78 *(was 71)* |
| Forks | ~47 |
| Language | Java |
| License | MIT |
| Latest | 0.168.v13951585050d (April 9, 2026) |
| MCP SDK | Java SDK v1.0.0 (MCP spec 2025-06-18) |

**18 tools** covering jobs, builds, SCM, and **new replay/rebuild** *(was 15)*:

| Category | Tools |
|----------|-------|
| Jobs | `getJob`, `getJobs`, `triggerBuild`, `getQueueItem` |
| Builds | `getBuild`, `updateBuild`, `getBuildLog`, `searchBuildLog`, **`rebuildBuild`** *(new)*, **`replayBuild`** *(new)* |
| SCM | `getJobScm`, `getBuildScm`, `getBuildChangeSets`, `findJobsWithScmUrl` |
| Replay | **`getReplayScripts`** *(new)* |
| Management | `whoAmI`, `getStatus` |

**Key differentiator:** Runs as a Jenkins plugin — installs directly into your Jenkins instance with no separate server needed. Supports SSE (`/mcp-server/sse`), Streamable HTTP (`/mcp-server/mcp`), and stateless HTTP transports. **April 2026 additions:** connection resilience with keep-alive, health endpoint (`/mcp-health`), Prometheus metrics (`/mcp-server/metrics`), graceful shutdown, and three new tools — `rebuildBuild`, `replayBuild`, and `getReplayScripts` for iterating on failed builds. Handles parameterized builds with automatic type conversion including `ListGitBranchesParameterDefinition`.

**Limitation:** 78 stars suggests early adoption. Java-only (part of the Jenkins ecosystem, but limits who can contribute). No pipeline-as-code authoring — you can trigger and monitor builds but not create or modify Jenkinsfiles through MCP.

**lanbaoshen/mcp-jenkins (Community Leader)**

| Aspect | Detail |
|--------|--------|
| Repository | [lanbaoshen/mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins) |
| Stars | ~117 *(was 101, +16%)* |
| Forks | ~42 |
| Commits | 94 *(was 78)* |
| Language | Python |
| License | MIT |
| Latest | v3.2.0 (April 21, 2026) |

**25 tools** with broader coverage than the official plugin *(was 21)*:

| Category | Tools |
|----------|-------|
| Items | `get_item`, `get_item_config`, `get_item_parameters`, `get_all_items`, `query_items`, `build_item` |
| Nodes | `get_all_nodes`, `get_node`, `get_node_config` |
| Queue | `get_all_queue_items`, `get_queue_item`, `cancel_queue_item` |
| Builds | `get_build`, `get_build_scripts`, `get_build_console_output`, `get_build_parameters`, `get_build_test_report`, `get_running_builds`, `stop_build` |
| Views | `get_view`, `get_all_views` |
| **Plugins** *(new)* | **`get_all_plugins`**, **`get_plugins_with_problems`**, **`get_plugin_dependency_graph`** |

**Key differentiator:** Most popular Jenkins MCP server (117 stars). **April 2026 additions:** v3.2.0 added plugin management tools — get all plugins, find plugins with problems, and visualize plugin dependency graphs. v3.1.x added folder depth parameter for nested job queries and fixed HTTP 403 errors with automatic crumb refresh. 27 total releases, 4 since March 23. Node management, queue management, build control, and test reports.

**Limitation:** No SCM integration (unlike the official plugin's `findJobsWithScmUrl`). Separate server process rather than native Jenkins plugin.

**Jordan-Jarvis/jenkins-mcp-enterprise (NEW — Enterprise Grade)**

| Aspect | Detail |
|--------|--------|
| Repository | [Jordan-Jarvis/jenkins-mcp-enterprise](https://github.com/Jordan-Jarvis/jenkins-mcp-enterprise) |
| Stars | ~27 |
| Language | Python |
| Status | Actively developed |

**Key differentiator:** Enterprise-focused Jenkins MCP with capabilities beyond the other servers: **AI-powered build failure diagnostics** with hierarchical sub-build discovery, **multi-instance Jenkins management** with load-balanced routing, **massive log handling** (10+ GB) with intelligent streaming and chunking, and **vector-powered semantic search** across build history. Designed for organizations managing multiple Jenkins instances at scale.

**Limitation:** 27 stars — early adoption. Enterprise features add complexity that smaller teams may not need.

### CircleCI — Official, Feature-Rich, Now With Observability

| Aspect | Detail |
|--------|--------|
| Repository | [CircleCI-Public/mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci) |
| Stars | ~84 *(was 80)* |
| Forks | ~52 |
| Commits | 308 *(was 290)* |
| Language | TypeScript |
| License | Apache-2.0 |
| Latest | v0.15.1 (April 21, 2026) |

**18 tools** with unique CI/CD intelligence features *(was 15)*:

| Category | Tools |
|----------|-------|
| Diagnostics | `get_build_failure_logs`, `find_flaky_tests`, `get_job_test_results` |
| Pipeline Ops | `get_latest_pipeline_status`, `run_pipeline`, `rerun_workflow` |
| Deployment | `run_rollback_pipeline`, `list_component_versions` |
| Config | `config_helper`, `analyze_diff` |
| AI/Prompt | `create_prompt_template`, `recommend_prompt_template_tests` |
| Discovery | `list_followed_projects` |
| Resources | `find_underused_resource_classes`, `download_usage_api_data` |

**Key differentiator:** Goes beyond simple build monitoring. **Flaky test detection** analyzes test execution history to identify unreliable tests. **Rollback operations** with guided parameter collection and environment selection. **Config helper** validates CircleCI configuration and provides guidance. **Resource optimization** finds jobs with underused compute classes. **April 2026 additions:** **OpenTelemetry metrics tracking** — tool invocations, duration, and error metrics for observability into how AI agents use the MCP server. Build failure logs can now be written to file via `outputDir` parameter. Fixed usage export to download all CSV parts. Available on AWS Marketplace. CircleCI holds **~5-6% CI/CD market share**.

**Limitation:** CircleCI-specific — no cross-platform CI/CD value. Some tools are AI-prompt-focused (`create_prompt_template`, `recommend_prompt_template_tests`) which feel tangential to CI/CD. 84 stars despite being official and feature-rich suggests limited adoption.

### Buildkite — Official, Remote MCP, v1.0.0

| Aspect | Detail |
|--------|--------|
| Repository | [buildkite/buildkite-mcp-server](https://github.com/buildkite/buildkite-mcp-server) |
| Stars | ~50 *(was 48)* |
| Forks | ~31 |
| Commits | 529 *(was 517)* |
| Language | Go |
| License | MIT |
| Latest | **v1.0.0 (March 30, 2026)** |

**Key differentiator:** **Reached v1.0.0** — a significant maturity milestone for a CI/CD MCP server. **Remote MCP server** — Buildkite offers a fully managed, publicly available remote MCP endpoint requiring no local installation. **March-April 2026 additions:** v0.12.0 added 12 cluster and queue management tools (CRUD operations). v0.13.0 **proactively removed `delete_cluster` and `delete_cluster_queue` tools** for safety — a rare example of a CI/CD MCP server deliberately reducing its attack surface. v1.0.0 added four build/job workflow tools: `cancel_build`, `rebuild_build`, `retry_job`, `get_job_env`, plus server-side job filtering. Official docs now at buildkite.com/docs/apis/mcp-server. 529 commits, the most of any CI/CD MCP server.

**Limitation:** 50 stars despite active development, v1.0.0 maturity, and official backing. Buildkite has smaller market share than Jenkins/CircleCI/GitHub Actions, limiting the audience.

### GitHub Actions — Now Official in GitHub MCP Server

| Aspect | Detail |
|--------|--------|
| Repository | [github/github-mcp-server](https://github.com/github/github-mcp-server) |
| Stars | ~29,400 |
| Latest | v1.0.3 |
| Toolset | `actions` (enable via `--toolsets actions`) |

**4 tools** in the official `actions` toolset:

| Tool | Description |
|------|-------------|
| `actions_get` | Get details of workflows, runs, jobs, and artifacts |
| `actions_list` | List workflows in a repository |
| `actions_run_trigger` | Trigger workflow actions |
| `get_job_logs` | Get workflow job logs |

**Key differentiator:** GitHub Actions MCP support is now **official and shipping** inside the GitHub MCP server (29.4k stars, v1.0.3). Enable it with `--toolsets actions` alongside 18 other toolsets including `code_security`, `dependabot`, and `copilot`. This is the right architecture — Actions lives inside the unified GitHub platform MCP server rather than as a standalone project. The previous standalone [ko1ynnky/github-actions-mcp-server](https://github.com/ko1ynnky/github-actions-mcp-server) is now **archived**.

**Limitation:** Only 4 tools compared to the previous standalone's 9 — no workflow usage statistics or billable minutes tracking yet. But being part of the 29.4k-star ecosystem means rapid iteration is likely.

### Argo CD — GitOps Leader (Community)

| Aspect | Detail |
|--------|--------|
| Repository | [argoproj-labs/mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd) |
| Stars | **~415** *(was 356, +17%)* |
| Forks | ~66 |
| Commits | 52 *(was 49)* |
| Language | TypeScript |
| License | Apache-2.0 |
| Latest | v0.6.0 (March 25, 2026) |

**13 tools** across application, resource, and **cluster management** *(was 12)*:

| Category | Tools |
|----------|-------|
| Applications | `list_applications`, `get_application`, `create_application`, `update_application`, `delete_application`, `sync_application` |
| Resources | `get_application_resource_tree`, `get_application_managed_resources`, `get_application_workload_logs`, `get_resource_events`, `get_resource_actions`, `run_resource_action` |
| **Clusters** *(new)* | **`list_clusters`** |

**Key differentiator:** The **most-starred CI/CD MCP server** (415 stars, +17% in five weeks). Under `argoproj-labs` — the official Argo Project labs organization. Full CRUD for applications plus sync operations. **v0.6.0 additions:** `applicationNamespace` parameter for multi-namespace support, cluster management tool to list registered clusters, images now published to quay.io. Resource tree visualization, workload logs, and resource action execution. Supports stdio and HTTP stream transports. Argo CD is the dominant GitOps tool for Kubernetes deployments.

**Limitation:** GitOps-specific — only useful for teams using Argo CD. Development pace has slowed since the v0.6.0 burst — no commits after March 25. Application CRUD means an AI agent can create/delete Argo CD applications — powerful but dangerous without guardrails. No read-only mode mentioned.

### TeamCity — NEW, Most Feature-Rich

| Aspect | Detail |
|--------|--------|
| Repository | [Daghis/teamcity-mcp](https://github.com/Daghis/teamcity-mcp) |
| Stars | ~24 |
| Commits | 394 |
| Language | TypeScript |
| Created | September 2025 |

**87 tools in Full mode / 31 tools in Dev mode** — the most feature-rich CI/CD MCP server by tool count:

**Key differentiator:** The **first TeamCity MCP server**, filling a major gap for JetBrains CI/CD users. Two operating modes: Dev mode (31 tools, safe for daily use) and Full mode (87 tools, complete platform control). Build management, test analysis, configuration control. **Runtime mode switching** without restart — start in Dev mode, escalate to Full when needed. 394 commits signals mature, actively maintained codebase despite modest star count.

**Limitation:** 24 stars — low visibility despite being the most feature-dense CI/CD MCP server. TeamCity has smaller market share than Jenkins/GitHub Actions. Single maintainer.

### Azure DevOps — NEW, Two Implementations

**Jordiag/azure-devops-mcp-server (14 stars, C#/.NET, 480 commits)** — The most mature Azure DevOps MCP server. Covers Boards, Repos, Pipelines, Artifacts, Test Plans, and Wiki. Pipeline capabilities include build queuing, cancellation, retry, and log downloads. SSE transport, Semantic Kernel integration, Docker support. 480 commits for a 14-star project signals sustained, serious development.

**burcusipahioglu/azure-devops-mcp-onprem (6 stars, TypeScript)** — Azure DevOps MCP specifically for on-premises installations. Supports TFVC (Team Foundation Version Control), changesets, work items, and pipeline management. Updated April 29, 2026 — actively maintained. Fills a niche for enterprises running Azure DevOps Server rather than Azure DevOps Services.

### Other Notable Servers

**severity1/terraform-cloud-mcp** (23 stars, Python, 62+ tools) — While [Terraform has its own MCP server](/reviews/terraform-mcp-server/), this community server focuses specifically on Terraform Cloud API integration with run management (create, apply, discard, cancel), plan/apply logs, state version management, and cost estimation. Read-only mode and delete safety controls available. No new releases since November 2025 — appears dormant.

**LokiMCPUniverse/jenkins-mcp-server** — Another Jenkins MCP server for GenAI integration.

**hekmon8/Jenkins-server-mcp** — Minimal Jenkins MCP server.

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging | Profiling | Code Review |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|---------- | ------- |----------|----------|---------|---------------------- | --------------|-----------|-----------|-------------|
| **Official MCP server** | Yes (29.4k stars, 19 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, 1.3k stars) | Yes (Jenkins 78, CircleCI 84, Buildkite v1.0.0, GitHub Actions) | Yes (JetBrains built-in, 24 tools) | [Yes (MS Playwright, 9.8k stars, 24 tools)](/reviews/testing-qa-mcp-servers/) | [Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana)](/reviews/monitoring-observability-mcp-servers/) | [Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast)](/reviews/security-scanning-mcp-servers/) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) | Yes (NuGet built-in VS 2026, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B 384, JetBrains built-in server) | Yes (Postman 192, Apollo GraphQL 275, Kong deprecated, Apigee, MuleSoft) | Yes (Splunk 13 tools GA, Grafana Tempo built-in, Grafana Loki 103 stars) | Partial (Liquibase private preview 19 tools, Prisma built-in CLI v6.6.0+) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector 9.2k official) | Partial (CodSpeed MCP, Polar Signals remote, Grafana Pyroscope via mcp-grafana) | Yes (SonarQube 442 stars, Codacy 56 stars, Graphite GT built-in) |
| **Remote hosting** | Yes (`api.githubcopilot.com/mcp/`) | No | No | No | AWS EKS MCP (preview) | Yes (Buildkite remote MCP) | No (requires running IDE) | [No (local browser required)](/reviews/testing-qa-mcp-servers/) | [Yes (Datadog, Sentry — OAuth)](/reviews/monitoring-observability-mcp-servers/) | [No (all local/CLI-based)](/reviews/security-scanning-mcp-servers/) | [Yes (Pulumi remote MCP)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | N/A | N/A | — | N/A | No (local debuggers) | No (local profiling agents) | N/A |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (1.4k stars, 20+ tools) | Argo CD (415 stars, 13 tools) | vscode-mcp-server (342 stars, 15 tools) | [executeautomation (5.3k stars)](/reviews/testing-qa-mcp-servers/) | [pab1it0/prometheus (340 stars)](/reviews/monitoring-observability-mcp-servers/) | [CodeQL community (143 stars)](/reviews/security-scanning-mcp-servers/) | Ansible (25 stars, 40+ tools) | mcp-package-version (122 stars, 9 registries) | Context7 (50.3k stars), magic-mcp (4.5k stars) | openapi-mcp-generator (495 stars), mcp-graphql (374 stars) | cr7258/elasticsearch (259 stars), Traceloop OTel (178 stars) | mpreziuso/mcp-atlas (Atlas), defrex/drizzle-mcp (Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars), Docs MCP (87 stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars), devtools-debugger (341 stars) | theSharque/mcp-jperf (Java JFR), PageSpeed Insights MCP servers | kopfrechner/gitlab-mr-mcp (86 stars), crazyrabbitLTC (32 stars) |
| **Community tool count** | 28+ (local Git) | 100+ | 25+ | 25 (container mgmt) | 20+ (core) to 253+ (claimed) | 4-87 per server | 13-19 per server | [24 (official) + API testing](/reviews/testing-qa-mcp-servers/) | [16+ (Datadog) to 100+ (Instana)](/reviews/monitoring-observability-mcp-servers/) | [7 (Semgrep) to full platform (Snyk)](/reviews/security-scanning-mcp-servers/) | [20+ (Terraform), full platform (Pulumi)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | Spec-to-server conversion + API interaction | N/A | — | N/A | N/A | N/A | N/A |
| **Pipeline/workflow mgmt** | Actions (being added) | Built-in (15 tools) | N/A | N/A | N/A | Core capability | N/A | [Test execution](/reviews/testing-qa-mcp-servers/) | [Alerting management (Grafana, Datadog, New Relic)](/reviews/monitoring-observability-mcp-servers/) | [Scan-and-fix capability](/reviews/security-scanning-mcp-servers/) | [IaC plan/apply workflows](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | 4+ (Postman, Apollo, Kong, Google/Apigee, MuleSoft) | N/A | — | N/A | N/A | N/A | N/A |
| **Build log access** | Via Actions | Via CI tools | N/A | N/A | Pod logs | Yes (all servers) | N/A | [mcp-test-runner (7 frameworks)](/reviews/testing-qa-mcp-servers/) | [Log analysis (Loki, Datadog, Elastic)](/reviews/monitoring-observability-mcp-servers/) | N/A | N/A | N/A | N/A | Bidirectional (spec-to-tools, API execution) | Log search/analysis + trace correlation | — | N/A | Stack traces, crash dumps | Profile data export | N/A |
| **Rollback support** | N/A | N/A | N/A | N/A | Rollout tools | CircleCI, Argo CD | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | — | N/A | N/A | N/A | N/A |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | API tokens per platform | Local connection (port/stdio) | [None (local browsers)](/reviews/testing-qa-mcp-servers/) | [API tokens / OAuth (remote)](/reviews/monitoring-observability-mcp-servers/) | [API tokens / CLI auth](/reviews/security-scanning-mcp-servers/) | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / CLI auth | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect | API keys (CodSpeed, Polar Signals) / Grafana auth / Google API key (PageSpeed) | API tokens (SonarQube, Codacy) / GitHub PAT / GitLab PAT |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | No | No (but Microsoft is Platinum) | [No (but Microsoft is Platinum)](/reviews/testing-qa-mcp-servers/) | [No](/reviews/monitoring-observability-mcp-servers/) | [No](/reviews/security-scanning-mcp-servers/) | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) | No | No |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | 5.6M developers | Jenkins: 11.3M devs | VS Code: 75.9% market share | [Playwright: 45.1% QA adoption](/reviews/testing-qa-mcp-servers/) | [Datadog: 32.7k customers](/reviews/monitoring-observability-mcp-servers/) | [SonarQube: 17.7% SAST mindshare](/reviews/security-scanning-mcp-servers/) | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads, PyPI: 421.6B yearly | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 30M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Prisma: 43k stars, Flyway: 10.7k stars, Atlas: 6.3k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars, ReadMe: powering major API docs | Chrome: 65%+ browser share, VS Code: 75.9% IDE share, x64dbg: 45k+ stars | APM market: $7-10B, Pyroscope: 11k+ stars, async-profiler: 9k+ stars | SonarQube: 7.4M+ users, CodeRabbit: top AI reviewer, Qodo/PR-Agent: 10.5k stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | [4/5](/reviews/kubernetes-mcp-servers/) | 3.5/5 | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) | [3.5/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | [3/5](/reviews/package-management-mcp-servers/) | [3.5/5](/reviews/code-generation-mcp-servers/) | [3.5/5](/reviews/api-development-mcp-servers/) | [3.5/5](/reviews/logging-tracing-mcp-servers/) | [2.5/5](/reviews/database-migration-mcp-servers/) | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | [4.5/5](/reviews/debugging-mcp-servers/) | [3/5](/reviews/profiling-performance-mcp-servers/) | [3.5/5](/reviews/code-review-pull-request-mcp-servers/) |

## Known Issues

1. **Star counts still lag other categories** — The most-starred CI/CD MCP server (Argo CD, 415 stars) is growing fast (+17% in five weeks) but still trails the least popular Kubernetes MCP server we cover. Jenkins' official plugin has just 78 stars despite Jenkins serving 11.26 million developers. GitHub Actions MCP benefits from the 29.4k-star GitHub server, but CI/CD-specific adoption remains early.

2. **No pipeline-as-code authoring** — None of these servers help you *write* CI/CD configurations. You can't ask an AI agent to generate a Jenkinsfile, `.circleci/config.yml`, or `buildkite.yml` through MCP and have it committed. The servers are monitors and triggers, not authors. For pipeline authoring, you still rely on the AI's training data (which may be outdated).

3. **GitHub Actions MCP is now live but minimal** — The ko1ynnky/github-actions-mcp-server is archived and GitHub Actions is now an official toolset in the GitHub MCP server (29.4k stars). However, the `actions` toolset has only 4 tools compared to the standalone's 9 — no workflow usage statistics or billable minutes tracking yet. Being part of the massive GitHub ecosystem should drive rapid iteration.

4. **Security risk with build triggers — but improving** — Several servers expose `triggerBuild` (Jenkins), `run_pipeline` (CircleCI), `sync_application` (Argo CD) tools. An AI agent that misinterprets a prompt could trigger production deployments, cancel in-progress builds, or sync incorrect application state. However, the safety story is improving: **Buildkite proactively removed `delete_cluster` and `delete_cluster_queue` tools** in v0.13.0, and **TeamCity offers Dev/Full mode switching** to limit tool exposure. CircleCI and Buildkite mention explicit safety controls.

5. **Build log exposure** — CI/CD build logs often contain sensitive data: API keys leaked in test output, database connection strings, internal URLs, deployment credentials. MCP servers that expose build logs (`getBuildLog`, `get_build_failure_logs`, `get_build_console_output`) pipe this data to AI agents without redaction. Unlike [Kubernetes MCP servers](/reviews/kubernetes-mcp-servers/) which implement secret masking, no CI/CD MCP server mentions log sanitization.

6. **Jenkins ecosystem fragmentation — now four servers** — Jenkins has four MCP implementations (official plugin, lanbaoshen, Jordan-Jarvis enterprise, LokiMCPUniverse/hekmon8). The community leader lanbaoshen (117 stars, Python, 25 tools) is pulling ahead of the official plugin (78 stars, Java, 18 tools). The enterprise server adds AI diagnostics and multi-instance management. Users must choose between native plugin integration (official), broad API coverage (lanbaoshen), or enterprise scale (Jordan-Jarvis).

7. **No cross-platform CI/CD server** — Each server is platform-specific. There's no MCP server that lets you monitor Jenkins *and* CircleCI *and* GitHub Actions from a single interface. Teams using multiple CI/CD platforms (common in enterprises with legacy Jenkins and modern GitHub Actions) need multiple MCP servers configured.

8. **CircleCI's AI-prompt tools feel tangential** — CircleCI includes `create_prompt_template` and `recommend_prompt_template_tests` tools that generate AI prompts rather than interact with CI/CD infrastructure. While creative, these blur the purpose of a CI/CD MCP server and may confuse AI agents that expect all tools to relate to build pipelines.

9. **Argo CD lacks safety guardrails** — The Argo CD MCP server includes `create_application`, `delete_application`, `sync_application`, and `run_resource_action` — all potentially destructive operations on production Kubernetes deployments. No read-only mode is mentioned. Compare this to Kubernetes MCP servers where both leaders offer read-only modes and secret redaction.

10. **GitLab CI/CD covered elsewhere** — GitLab's built-in MCP server (15 tools, Premium/Ultimate) includes CI/CD pipeline management, and community servers like zereight/gitlab-mcp offer 19 pipeline tools. This is covered in our [GitLab review](/reviews/gitlab-mcp-server/) rather than here, since GitLab's MCP is a unified platform server, not a standalone CI/CD tool.

## Bottom Line

**Rating: 3.5 out of 5** *(was 3/5)*

The CI/CD MCP ecosystem has **matured significantly in five weeks**. Buildkite reached v1.0.0 — the first CI/CD MCP server to hit stable release. GitHub Actions is now officially supported in the GitHub MCP server (29.4k stars). Argo CD grew 17% to 415 stars. Two new platforms joined (TeamCity with 87 tools, Azure DevOps with 480 commits). Jenkins now has four competing servers including an enterprise option. The ecosystem is shifting from pure observation toward active build management — Buildkite added cancel/rebuild/retry, Jenkins added replay/rebuild, and CircleCI added OpenTelemetry for MCP server observability.

The **3.5/5 rating upgrade** reflects: Buildkite's v1.0.0 maturity milestone, GitHub Actions going official, Argo CD's strong community growth (+17%), new platform coverage (TeamCity, Azure DevOps), Jenkins ecosystem depth (4 servers, 18-25 tools each), improving safety story (Buildkite removing destructive tools, TeamCity's Dev/Full modes), and CircleCI's OpenTelemetry integration showing operational sophistication. It still loses points for relatively low adoption outside Argo CD, no pipeline-as-code authoring, missing log sanitization, and no cross-platform CI/CD server.

**Who benefits from CI/CD MCP servers today:**

- **Jenkins teams** — Four server options: official plugin (18 tools, native integration), lanbaoshen (117 stars, 25 tools, plugin management), or Jordan-Jarvis enterprise (AI diagnostics, multi-instance, massive log handling)
- **GitHub Actions users** — Official support in the GitHub MCP server (29.4k stars) via `--toolsets actions`. Trigger, monitor, and retrieve logs from the same server handling repos, PRs, and issues
- **CircleCI users** — Flaky test detection, rollback operations, and now OpenTelemetry metrics tracking save real debugging time
- **GitOps practitioners** — Argo CD's MCP server (415 stars) brings application management, cluster listing, and sync operations into AI workflows, complementing [Kubernetes MCP servers](/reviews/kubernetes-mcp-servers/)
- **Buildkite customers** — v1.0.0 with remote MCP hosting, cluster management, and build workflow tools (cancel, rebuild, retry)
- **TeamCity teams** — 87 tools in Full mode is the most comprehensive CI/CD MCP server available, with safe Dev mode (31 tools) for daily use
- **Azure DevOps teams** — Two implementations cover both cloud and on-premises, including pipeline management, build queuing, and log retrieval

**Who should be cautious:**

- **Production environments** — Build trigger and deployment sync tools can affect production with a misinterpreted prompt. Start with read-only usage patterns and add operational tools carefully. TeamCity's Dev mode is a good model
- **Multi-platform teams** — No cross-platform server exists. Managing MCP connections to Jenkins, CircleCI, and GitHub Actions simultaneously adds configuration complexity
- **Teams expecting pipeline authoring** — These servers monitor and operate pipelines, they don't help write them. For Jenkinsfile or CircleCI config generation, you're still relying on the AI's training data
- **Security-sensitive organizations** — Build logs exposed through MCP may contain secrets. No CI/CD MCP server implements log sanitization comparable to Kubernetes secret masking

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of April 2026. See our [About page](/about/) for details on our review process.*
