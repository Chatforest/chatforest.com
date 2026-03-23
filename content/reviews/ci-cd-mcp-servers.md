---
title: "CI/CD MCP Servers — Build Pipelines Get an AI Interface"
date: 2026-03-23T22:00:00+09:00
description: "CI/CD platforms are embracing MCP with official servers from Jenkins (71 stars, Java plugin), CircleCI (80 stars, 15 tools), and Buildkite (48 stars, Go). Plus community Argo CD (356 stars, 12 tools) and GitHub Actions (40 stars, being archived). Jenkins leads with 47% CI/CD market share but the MCP ecosystem is early and fragmented."
og_description: "CI/CD MCP ecosystem: Jenkins official plugin, CircleCI 15 tools, Buildkite remote MCP, Argo CD 356 stars. Official servers from 4 platforms, community GitOps. Rating: 3/5."
content_type: "Review"
card_description: "CI/CD platforms are building MCP servers, led by Jenkins (official plugin, 15 tools), CircleCI (15 tools with flaky test detection and rollback), Buildkite (official Go server with remote hosting), and community Argo CD (356 stars, 12 tools for GitOps). GitHub Actions support is being absorbed into the official GitHub MCP server. The ecosystem is early — no platform offers full pipeline-as-code authoring through MCP yet."
last_refreshed: 2026-03-23
---

**At a glance:** CI/CD platforms are building MCP integrations, but the ecosystem is early. **Four platforms have official MCP servers**: Jenkins ([jenkinsci/mcp-server-plugin](https://github.com/jenkinsci/mcp-server-plugin), 71 stars, Java, 15 tools), CircleCI ([CircleCI-Public/mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci), 80 stars, TypeScript, 15 tools), Buildkite ([buildkite/buildkite-mcp-server](https://github.com/buildkite/buildkite-mcp-server), 48 stars, Go, remote MCP available), and the community-maintained [lanbaoshen/mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins) (101 stars, Python, 21 tools). On the GitOps side, [argoproj-labs/mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd) (356 stars, TypeScript, 12 tools) leads with application sync and resource management. GitHub Actions MCP support is being absorbed into the [official GitHub MCP server](/reviews/github-mcp-server/). With **Jenkins holding ~47% CI/CD market share** and **GitHub Actions at 62% personal use**, the MCP ecosystem has a long way to go. This is the **sixth review in our [Developer Tools MCP category](/categories/developer-tools/)**.

CI/CD is one of the most automation-heavy domains in software engineering — yet ironically, the MCP ecosystem for build pipelines lags behind other developer tools. While [GitHub](/reviews/github-mcp-server/) has 28.2k stars on its MCP server and [Kubernetes](/reviews/kubernetes-mcp-servers/) has two servers above 1,000 stars, the top CI/CD-specific MCP server (Argo CD) has 356 stars. The reason is structural: CI/CD platforms are complex stateful systems where a wrong API call can deploy broken code to production, cancel critical builds, or expose secrets in build logs. MCP servers for CI/CD must be careful about what they expose.

**Architecture note:** CI/CD MCP servers divide into two camps: **build system observers** (read logs, diagnose failures, check pipeline status) and **pipeline operators** (trigger builds, cancel runs, manage deployments). Most current servers lean observer — they help AI agents understand what happened in a build, not control what happens next. This is the right starting point for safety, but limits the value proposition compared to CI/CD platform UIs.

## What's Available

### Jenkins — Official Plugin + Community Server

Jenkins dominates CI/CD with **~47% market share** and **11.26 million developers**. It has both an official MCP plugin and a community server:

**jenkinsci/mcp-server-plugin (Official)**

| Aspect | Detail |
|--------|--------|
| Repository | [jenkinsci/mcp-server-plugin](https://github.com/jenkinsci/mcp-server-plugin) |
| Stars | ~71 |
| Forks | ~47 |
| Commits | 158 |
| Language | Java |
| License | MIT |
| MCP SDK | Java SDK 0.17.2 (MCP spec 2025-06-18) |

**15 tools** covering jobs, builds, and SCM:

| Category | Tools |
|----------|-------|
| Jobs | `getJob`, `getJobs`, `triggerBuild`, `getQueueItem` |
| Builds | `getBuild`, `updateBuild`, `getBuildLog`, `searchBuildLog` |
| SCM | `getJobScm`, `getBuildScm`, `getBuildChangeSets`, `findJobsWithScmUrl` |
| Management | `whoAmI`, `getStatus` |

**Key differentiator:** Runs as a Jenkins plugin — installs directly into your Jenkins instance with no separate server needed. Supports SSE (`/mcp-server/sse`), Streamable HTTP (`/mcp-server/mcp`), and stateless HTTP transports. Handles parameterized builds (String, Boolean, Choice, Text, Password, Run parameters) with automatic type conversion. Paginated log retrieval and regex-based log searching.

**Limitation:** 71 stars suggests early adoption. Java-only (part of the Jenkins ecosystem, but limits who can contribute). No pipeline-as-code authoring — you can trigger and monitor builds but not create or modify Jenkinsfiles through MCP.

**lanbaoshen/mcp-jenkins (Community Leader)**

| Aspect | Detail |
|--------|--------|
| Repository | [lanbaoshen/mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins) |
| Stars | ~101 |
| Forks | ~42 |
| Commits | 78 |
| Language | Python |
| License | MIT |

**21 tools** with broader coverage than the official plugin:

| Category | Tools |
|----------|-------|
| Items | `get_item`, `get_item_config`, `get_item_parameters`, `get_all_items`, `query_items`, `build_item` |
| Nodes | `get_all_nodes`, `get_node`, `get_node_config` |
| Queue | `get_all_queue_items`, `get_queue_item`, `cancel_queue_item` |
| Builds | `get_build`, `get_build_scripts`, `get_build_console_output`, `get_build_parameters`, `get_build_test_report`, `get_running_builds`, `stop_build` |
| Views | `get_view`, `get_all_views` |

**Key differentiator:** Node management (get node config, list all nodes), queue management (cancel queue items), build control (stop running builds), and test report access. More community traction (101 vs 71 stars) despite being unofficial. Python with Docker support.

**Limitation:** 78 commits for 21 tools suggests some may be thin. No SCM integration (unlike the official plugin's `findJobsWithScmUrl`). Separate server process rather than native Jenkins plugin.

### CircleCI — Official, Feature-Rich

| Aspect | Detail |
|--------|--------|
| Repository | [CircleCI-Public/mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci) |
| Stars | ~80 |
| Forks | ~52 |
| Commits | 290 |
| Language | TypeScript |
| License | Apache-2.0 |

**15 tools** with unique CI/CD intelligence features:

| Category | Tools |
|----------|-------|
| Diagnostics | `get_build_failure_logs`, `find_flaky_tests`, `get_job_test_results` |
| Pipeline Ops | `get_latest_pipeline_status`, `run_pipeline`, `rerun_workflow` |
| Deployment | `run_rollback_pipeline`, `list_component_versions` |
| Config | `config_helper`, `analyze_diff` |
| AI/Prompt | `create_prompt_template`, `recommend_prompt_template_tests` |
| Discovery | `list_followed_projects` |
| Resources | `find_underused_resource_classes`, `download_usage_api_data` |

**Key differentiator:** Goes beyond simple build monitoring. **Flaky test detection** analyzes test execution history to identify unreliable tests. **Rollback operations** with guided parameter collection and environment selection. **Config helper** validates CircleCI configuration and provides guidance. **Resource optimization** finds jobs with underused compute classes. **Diff analysis** against cursor rules for violations. Available on AWS Marketplace. CircleCI holds **~5-6% CI/CD market share** with **~360 employees** and **$105M revenue** (2025).

**Limitation:** CircleCI-specific — no cross-platform CI/CD value. Some tools are AI-prompt-focused (`create_prompt_template`, `recommend_prompt_template_tests`) which feel tangential to CI/CD. 80 stars despite being official and feature-rich suggests limited adoption.

### Buildkite — Official, Remote MCP

| Aspect | Detail |
|--------|--------|
| Repository | [buildkite/buildkite-mcp-server](https://github.com/buildkite/buildkite-mcp-server) |
| Stars | ~48 |
| Forks | ~31 |
| Commits | 517 |
| Language | Go |
| License | MIT |
| Latest | v0.11.4 (March 23, 2026) |

Exposes pipeline, build, job, and test data to AI tools:

**Key differentiator:** **Remote MCP server** — Buildkite offers a fully managed, publicly available remote MCP endpoint requiring no local installation. This is rare in the CI/CD MCP space. 517 commits (most of any CI/CD MCP server) signal active development. Built from Chainguard's static base image, runs unprivileged. Available via Docker, Homebrew, or native binary. v0.11.4 with 23 contributors shows sustained investment.

**Limitation:** 48 stars despite active development and official backing. Go API explicitly marked "unstable, subject to breaking changes." Buildkite has smaller market share than Jenkins/CircleCI/GitHub Actions, limiting the audience.

### GitHub Actions — Being Absorbed

| Aspect | Detail |
|--------|--------|
| Repository | [ko1ynnky/github-actions-mcp-server](https://github.com/ko1ynnky/github-actions-mcp-server) |
| Stars | ~40 |
| Forks | ~18 |
| Commits | 58 |
| Language | TypeScript |
| License | MIT |

**9 tools**: `list_workflows`, `get_workflow`, `get_workflow_usage`, `list_workflow_runs`, `get_workflow_run`, `get_workflow_run_jobs`, `trigger_workflow`, `cancel_workflow_run`, `rerun_workflow`.

**Key differentiator:** Complete workflow lifecycle — list, view, trigger, cancel, rerun. Usage statistics including billable minutes.

**Limitation:** The repository carries an explicit notice: **"This repository will be archived soon as the official GitHub MCP server is adding Actions support."** GitHub Actions CI/CD capabilities are being folded into the [official GitHub MCP server](/reviews/github-mcp-server/) (28.2k stars), which already covers repositories, issues, PRs, and code search. This is the right move — Actions is tightly integrated with GitHub's platform. Standalone Actions MCP servers will become redundant.

### Argo CD — GitOps Leader (Community)

| Aspect | Detail |
|--------|--------|
| Repository | [argoproj-labs/mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd) |
| Stars | ~356 |
| Forks | ~66 |
| Commits | 49 |
| Language | TypeScript |
| License | Apache-2.0 |

**12 tools** across application and resource management:

| Category | Tools |
|----------|-------|
| Applications | `list_applications`, `get_application`, `create_application`, `update_application`, `delete_application`, `sync_application` |
| Resources | `get_application_resource_tree`, `get_application_managed_resources`, `get_application_workload_logs`, `get_resource_events`, `get_resource_actions`, `run_resource_action` |

**Key differentiator:** The **most-starred CI/CD MCP server** (356 stars). Under `argoproj-labs` — the official Argo Project labs organization. Full CRUD for applications plus sync operations. Resource tree visualization, workload logs, and resource action execution. Supports stdio and HTTP stream transports. Argo CD is the dominant GitOps tool for Kubernetes deployments.

**Limitation:** GitOps-specific — only useful for teams using Argo CD. 49 commits for 12 tools is reasonable but shallow. Application CRUD means an AI agent can create/delete Argo CD applications — powerful but dangerous without guardrails. No read-only mode mentioned.

### Other Notable Servers

**severity1/terraform-cloud-mcp** (23 stars, Python, 62+ tools) — While [Terraform has its own MCP server](/reviews/terraform-mcp-server/), this community server focuses specifically on Terraform Cloud API integration with run management (create, apply, discard, cancel), plan/apply logs, state version management, and cost estimation. Read-only mode and delete safety controls available.

**LokiMCPUniverse/jenkins-mcp-server** — Another Jenkins MCP server for GenAI integration.

**hekmon8/Jenkins-server-mcp** — Minimal Jenkins MCP server.

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, 1.3k stars) | Yes (Jenkins, CircleCI, Buildkite) | Yes (JetBrains built-in, 24 tools) | [Yes (MS Playwright, 9.8k stars, 24 tools)](/reviews/testing-qa-mcp-servers/) | [Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana)](/reviews/monitoring-observability-mcp-servers/) |
| **Remote hosting** | Yes (`api.githubcopilot.com/mcp/`) | No | No | No | AWS EKS MCP (preview) | Yes (Buildkite remote MCP) | No (requires running IDE) | [No (local browser required)](/reviews/testing-qa-mcp-servers/) | [Yes (Datadog, Sentry — OAuth)](/reviews/monitoring-observability-mcp-servers/) |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (1.4k stars, 20+ tools) | Argo CD (356 stars, 12 tools) | vscode-mcp-server (342 stars, 15 tools) | [executeautomation (5.3k stars)](/reviews/testing-qa-mcp-servers/) | [pab1it0/prometheus (340 stars)](/reviews/monitoring-observability-mcp-servers/) |
| **Community tool count** | 28+ (local Git) | 100+ | 25+ | 25 (container mgmt) | 20+ (core) to 253+ (claimed) | 9-21 per server | 13-19 per server | [24 (official) + API testing](/reviews/testing-qa-mcp-servers/) | [16+ (Datadog) to 100+ (Instana)](/reviews/monitoring-observability-mcp-servers/) |
| **Pipeline/workflow mgmt** | Actions (being added) | Built-in (15 tools) | N/A | N/A | N/A | Core capability | N/A | [Test execution](/reviews/testing-qa-mcp-servers/) | [Alerting management (Grafana, Datadog, New Relic)](/reviews/monitoring-observability-mcp-servers/) |
| **Build log access** | Via Actions | Via CI tools | N/A | N/A | Pod logs | Yes (all servers) | N/A | [mcp-test-runner (7 frameworks)](/reviews/testing-qa-mcp-servers/) | [Log analysis (Loki, Datadog, Elastic)](/reviews/monitoring-observability-mcp-servers/) |
| **Rollback support** | N/A | N/A | N/A | N/A | Rollout tools | CircleCI, Argo CD | N/A | N/A | N/A |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | API tokens per platform | Local connection (port/stdio) | [None (local browsers)](/reviews/testing-qa-mcp-servers/) | [API tokens / OAuth (remote)](/reviews/monitoring-observability-mcp-servers/) |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | No | No (but Microsoft is Platinum) | [No (but Microsoft is Platinum)](/reviews/testing-qa-mcp-servers/) | [No](/reviews/monitoring-observability-mcp-servers/) |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | 5.6M developers | Jenkins: 11.3M devs | VS Code: 75.9% market share | [Playwright: 45.1% QA adoption](/reviews/testing-qa-mcp-servers/) | [Datadog: 32.7k customers](/reviews/monitoring-observability-mcp-servers/) |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | [4/5](/reviews/kubernetes-mcp-servers/) | 3/5 | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) |

## Known Issues

1. **Low star counts across the board** — The most-starred CI/CD MCP server (Argo CD, 356 stars) has fewer stars than the *least popular* Kubernetes MCP server we cover (strowk, 377 stars). Jenkins' official plugin has just 71 stars despite Jenkins serving 11.26 million developers. This suggests CI/CD MCP is very early stage — most teams haven't connected their build systems to AI agents yet.

2. **No pipeline-as-code authoring** — None of these servers help you *write* CI/CD configurations. You can't ask an AI agent to generate a Jenkinsfile, `.circleci/config.yml`, or `buildkite.yml` through MCP and have it committed. The servers are monitors and triggers, not authors. For pipeline authoring, you still rely on the AI's training data (which may be outdated).

3. **GitHub Actions being absorbed, not standalone** — The ko1ynnky/github-actions-mcp-server is explicitly being archived in favor of the official GitHub MCP server. This is the right architectural decision, but it means there's no dedicated Actions MCP experience — Actions tools will be a small subset of the GitHub server's 28.2k-star ecosystem.

4. **Security risk with build triggers** — Several servers expose `triggerBuild` (Jenkins), `run_pipeline` (CircleCI), `sync_application` (Argo CD) tools. An AI agent that misinterprets a prompt could trigger production deployments, cancel in-progress builds, or sync incorrect application state. Only CircleCI and Buildkite mention explicit safety controls around destructive operations.

5. **Build log exposure** — CI/CD build logs often contain sensitive data: API keys leaked in test output, database connection strings, internal URLs, deployment credentials. MCP servers that expose build logs (`getBuildLog`, `get_build_failure_logs`, `get_build_console_output`) pipe this data to AI agents without redaction. Unlike [Kubernetes MCP servers](/reviews/kubernetes-mcp-servers/) which implement secret masking, no CI/CD MCP server mentions log sanitization.

6. **Jenkins ecosystem fragmentation** — Jenkins has three MCP implementations (official plugin, lanbaoshen, LokiMCPUniverse, hekmon8) with no clear winner. The official plugin (71 stars, Java) and community leader (101 stars, Python) have different tool sets — the official has SCM integration but the community version has node and queue management. Users must choose between native plugin integration and broader API coverage.

7. **No cross-platform CI/CD server** — Each server is platform-specific. There's no MCP server that lets you monitor Jenkins *and* CircleCI *and* GitHub Actions from a single interface. Teams using multiple CI/CD platforms (common in enterprises with legacy Jenkins and modern GitHub Actions) need multiple MCP servers configured.

8. **CircleCI's AI-prompt tools feel tangential** — CircleCI includes `create_prompt_template` and `recommend_prompt_template_tests` tools that generate AI prompts rather than interact with CI/CD infrastructure. While creative, these blur the purpose of a CI/CD MCP server and may confuse AI agents that expect all tools to relate to build pipelines.

9. **Argo CD lacks safety guardrails** — The Argo CD MCP server includes `create_application`, `delete_application`, `sync_application`, and `run_resource_action` — all potentially destructive operations on production Kubernetes deployments. No read-only mode is mentioned. Compare this to Kubernetes MCP servers where both leaders offer read-only modes and secret redaction.

10. **GitLab CI/CD covered elsewhere** — GitLab's built-in MCP server (15 tools, Premium/Ultimate) includes CI/CD pipeline management, and community servers like zereight/gitlab-mcp offer 19 pipeline tools. This is covered in our [GitLab review](/reviews/gitlab-mcp-server/) rather than here, since GitLab's MCP is a unified platform server, not a standalone CI/CD tool.

## Bottom Line

**Rating: 3 out of 5**

The CI/CD MCP ecosystem is **functional but early**. Four platforms have official servers (Jenkins, CircleCI, Buildkite, with GitHub Actions being absorbed into the GitHub MCP server), and the GitOps community has a solid Argo CD server (356 stars). The tools focus on **build observation** — reading logs, checking pipeline status, diagnosing failures — with some **operational capability** — triggering builds, managing runs, rollback support.

The **3/5 rating** reflects: official vendor investment across multiple platforms (Jenkins, CircleCI, Buildkite all maintain MCP servers), useful diagnostic tools (CircleCI's flaky test detection, Jenkins' log search, Argo CD's resource tree), and practical operational capabilities (build triggers, rollbacks, application sync). It loses points for very low adoption (356 max stars vs 1,400+ for Kubernetes), no pipeline-as-code authoring, missing safety features (no log sanitization, limited read-only modes), platform fragmentation (each server is platform-specific with no cross-platform option), and the fundamental limitation that CI/CD MCP servers are *monitors* that don't yet help you *write* better pipelines.

**Who benefits from CI/CD MCP servers today:**

- **Jenkins teams** — The official plugin or lanbaoshen's server enables AI-assisted build monitoring, log analysis, and build triggering for Jenkins' massive install base
- **CircleCI users** — Flaky test detection and rollback operations through natural language save real debugging time
- **GitOps practitioners** — Argo CD's MCP server brings application management and sync operations into AI workflows, complementing [Kubernetes MCP servers](/reviews/kubernetes-mcp-servers/)
- **Buildkite customers** — Remote MCP hosting means zero setup for AI-assisted pipeline monitoring

**Who should be cautious:**

- **Production environments** — Build trigger and deployment sync tools can affect production with a misinterpreted prompt. Start with read-only usage patterns and add operational tools carefully
- **Multi-platform teams** — No cross-platform server exists. Managing MCP connections to Jenkins, CircleCI, and GitHub Actions simultaneously adds configuration complexity
- **Teams expecting pipeline authoring** — These servers monitor pipelines, they don't help write them. For Jenkinsfile or CircleCI config generation, you're still relying on the AI's training data
- **Security-sensitive organizations** — Build logs exposed through MCP may contain secrets. No CI/CD MCP server implements log sanitization comparable to Kubernetes secret masking

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*
