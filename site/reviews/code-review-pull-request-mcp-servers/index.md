# Code Review & Pull Request MCP Servers — SonarQube, Codacy, CodeRabbit, Graphite GT, GitLab MR, Community PR Reviewers

> Code review and pull request MCP servers let AI agents analyze diffs, post inline comments, enforce quality gates, manage merge requests, and create stacked PRs.


**At a glance:** Code review is the workflow where AI assistants and MCP can have the highest single impact — review capacity is the bottleneck in modern software development, and AI-powered code analysis through MCP can scale review throughput without scaling headcount. [SonarQube MCP](https://github.com/SonarSource/sonarqube-mcp-server) (442 stars, Kotlin, native in SonarQube Cloud) leads code quality integration. [Codacy MCP](https://github.com/codacy/codacy-mcp-server) (56 stars, official) covers SAST, secrets, coverage, and PR analysis. [Graphite GT MCP](https://graphite.com/docs/gt-mcp) (built into CLI, beta) enables AI-driven stacked PR creation. [CodeRabbit](https://www.coderabbit.ai/) dominates AI code review but operates as an MCP **client** consuming context from other servers. Community PR review servers connect LLMs to GitHub diffs for automated feedback. This is the **twentieth review in our [Developer Tools MCP category](/categories/developer-tools/)**.

The AI code assistant market ($4.7B in 2025, growing to $14.6B by 2033 at 15.3% CAGR) is crystallizing fast — GitHub Copilot, Claude Code, and Cursor have all crossed $1B ARR. But code generation speed has shifted the bottleneck downstream: maintainers, tech leads, and engineering managers now face more pull requests, more diffs, and more surface area to validate. The MCP ecosystem is responding with two approaches: **platform connectors** that bring existing code quality data into AI workflows (SonarQube, Codacy) and **review agents** that use LLMs to analyze diffs directly (community servers). A third category — **PR workflow tools** (Graphite GT MCP) — focuses not on review itself but on making AI-generated code reviewable.

**Architecture note:** Code review MCP servers follow five patterns. **Code quality platform connectors** (SonarQube, Codacy) expose existing quality gates, vulnerability scans, and coverage data as MCP tools — the review intelligence lives in the platform, MCP provides the interface. **PR management servers** (gitlab-mr-mcp, GitHub MCP) give AI agents read/write access to pull/merge requests (diffs, comments, approvals) without performing the review itself. **LLM-powered review agents** (crazyrabbitLTC, praneybehl, Orcus2021) use external LLMs to analyze diffs and generate review comments — the MCP server orchestrates the review pipeline. **Stacked PR workflow tools** (Graphite GT MCP) help AI agents structure code changes into reviewable units. **Review platform bridges** (coderabbitai-mcp) let AI assistants interact with reviews from dedicated AI review platforms.

For repository operations and PR management on GitHub, see our [GitHub MCP Server](/reviews/github-mcp-server/) review. For GitLab repository management, see our [GitLab MCP Server](/reviews/gitlab-mcp-server/) review. For security vulnerability scanning (which overlaps with code quality), see our [Security Scanning](/reviews/security-scanning-mcp-servers/) review.

## What's Available

### Code Quality Platforms (2 servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) | 442 | Kotlin | — | — | Code quality + security: snippet analysis, quality gates, 10+ platform support |
| [codacy/codacy-mcp-server](https://github.com/codacy/codacy-mcp-server) | 56 | TypeScript | MIT | 15+ | SAST, secrets, coverage, duplication, complexity, PR tools |

**SonarQube MCP** (SonarSource, 442 stars, 339 commits, Kotlin) is the most established code quality MCP server. It integrates with SonarQube Server or SonarQube Cloud to provide code quality and security analysis through the MCP interface. The server analyzes code snippets directly within agent context — AI assistants can check code against SonarQube rules without leaving their workflow. Supported across 11+ platforms: Claude Code, Cursor, Codex CLI, Gemini CLI, GitHub Copilot CLI, GitHub Copilot coding agent, Kiro, VS Code, Windsurf, Zed, and Antigravity. Requires JDK 21+. Available as Docker image (`mcp/sonarqube`).

In March 2026, SonarQube Cloud launched a **native embedded MCP server** — no installation or Docker required. The MCP server is built directly into SonarQube Cloud, removing the "Docker barrier" that was the main adoption obstacle for hosted integrations. This makes SonarQube the first major code quality platform to offer a fully managed, zero-install MCP experience. SonarQube (17.7% SAST mindshare, 7.4M+ users) detects bugs, vulnerabilities, code smells, and security hotspots across 30+ languages.

**Codacy MCP** (official, 56 stars, 141 commits, TypeScript, MIT) positions itself as "MCP-native" — designed for the agentic development paradigm. Tools span the full code quality spectrum: **repository management** (setup, organization listing, analysis retrieval), **code quality** (issue detection with severity/category/language filtering), **security analysis** (SAST, secrets scanning, dependency scanning, IaC scanning, CI/CD scanning, DAST, penetration testing), **file analysis** (coverage metrics, duplication detection, complexity analysis), **pull request tools** (PR listing, diff analysis, coverage reports), and **local analysis** (CLI-based quality checks). Supports Cursor, Windsurf, Claude Desktop, VS Code with Copilot. Codacy's MCP server extends beyond basic code scanning to include security categories (secrets, IaC, DAST) that SonarQube's MCP server doesn't expose directly.

### Stacked PR Workflow (1 server)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [Graphite GT MCP](https://graphite.com/docs/gt-mcp) | — | Go | — | — | AI agents create stacked PRs from large diffs — built into CLI v1.6.7+ |

**Graphite GT MCP** (built into Graphite CLI v1.6.7+, Go, beta) solves a problem unique to AI-generated code: large, monolithic diffs that are hard to review. Instead of reviewing code, GT MCP helps AI agents **create stacked pull requests** — breaking large changes into smaller, focused, sequentially-dependent PRs that humans can review incrementally. The MCP server is built directly into the Graphite CLI (`gt` command). AI agents navigate the stack (`gt ls`, `gt down`, `gt up`), insert new changes (`gt create --insert -am <description>`), and manage the full stacking workflow.

This approach tackles the fundamental tension in AI-assisted development: AI can generate code faster than humans can review it. Stacked PRs restore human oversight by decomposing AI output into digestible units. Graphite's reviewer (Graphite Agent, launched 2026) complements GT MCP on the review side — while GT MCP structures code for review, Graphite Agent performs the actual review. Currently in beta; some workflows may not be fully supported. Requires Graphite CLI v1.6.7+ and a Graphite account.

### AI Code Review Platforms (2 servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [CodeRabbit](https://www.coderabbit.ai/) (as MCP client) | — | — | Commercial | 50+ integrations | Consumes MCP server context to enrich AI code reviews |
| [bradthebeeble/coderabbitai-mcp](https://github.com/bradthebeeble/coderabbitai-mcp) | 26 | TypeScript | MIT | 4+ | Interact with CodeRabbit reviews on GitHub PRs |

**CodeRabbit** is the leading AI code review platform but takes a different MCP role — it's an **MCP client**, not a server. CodeRabbit consumes context from connected MCP servers (Datadog, New Relic, SonarQube, Snyk, Grafana, Linear, Confluence, Slack) to enrich its code reviews. Before starting a review, CodeRabbit searches connected MCP servers for relevant context — database schema changes get checked against data architecture documents, API implementations get verified against design patterns. Works with GitHub Actions, GitLab CI, Bitbucket Pipelines. 50+ native integrations. Setup takes under 10 minutes per MCP server connection.

**bradthebeeble/coderabbitai-mcp** (26 stars, TypeScript, MIT) is a community-built bridge that lets AI assistants interact with CodeRabbit's reviews from the other direction. Tools include: retrieve and analyze CodeRabbit reviews on PRs, extract detailed review information and line comments, mark comments as resolved with custom notes, and a `/coderabbit-review` slash command for workflow automation. Requires GitHub PAT with `repo` scope. Works with Claude Desktop and Claude Code.

### GitLab Merge Request Management (2+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [kopfrechner/gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp) | 86 | JavaScript | MIT | 10 | Full MR lifecycle: list, fetch, comment, diff, update |
| [mehmetakinn/gitlab-mcp-code-review](https://github.com/mehmetakinn/gitlab-mcp-code-review) | — | — | — | — | GitLab code review with AI analysis |

**kopfrechner/gitlab-mr-mcp** (86 stars, 25 forks, 122 commits, JavaScript, MIT) is the leading GitLab-focused MCP server for merge request management. Ten tools cover the full MR lifecycle: `get_projects` (list accessible projects), `list_open_merge_requests` (view open MRs), `get_merge_request_details` (comprehensive MR info), `get_merge_request_comments` (discussion and diff notes), `add_merge_request_comment` (general comments), `add_merge_request_diff_comment` (line-specific comments on diffs), `get_merge_request_diff` (access diffs), `get_issue_details` (issue context), `set_merge_request_title`, and `set_merge_request_description`. Requires Node.js 18+ and GitLab PAT with `api` scope. Docker deployment supported.

While our [GitLab MCP Server](/reviews/gitlab-mcp-server/) review covers the broader GitLab ecosystem (including the official built-in MCP and zereight/gitlab-mcp at 1.2k stars), gitlab-mr-mcp is notable here for its focus specifically on the merge request review workflow — its tools are tuned for reading diffs, posting comments, and managing the review conversation. Additional GitLab code review MCP servers exist from mehmetakinn, ffpy, and yu-ito (Photosynth), each targeting MR review automation.

### Community PR Review Agents (4+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [crazyrabbitLTC/mcp-code-review-server](https://github.com/crazyrabbitLTC/mcp-code-review-server) | 32 | JS/TS | MIT | 2 | Repomix repo flattening + multi-LLM review |
| [praneybehl/code-review-mcp](https://github.com/praneybehl/code-review-mcp) | 30 | TypeScript | MIT | — | Git diff analysis via Vercel AI SDK, multi-provider LLM |
| [Orcus2021/code-review-mcp-server](https://github.com/Orcus2021/code-review-mcp-server) | 6 | TypeScript | — | 7 | GitHub PR comments + Notion integration for guidelines |
| [marchellodev/reviewer-mcp](https://github.com/marchellodev/reviewer-mcp) | — | TypeScript | — | 1 | Shell-based review via cursor-tools |

**crazyrabbitLTC/mcp-code-review-server** (32 stars, 23 forks, JS/TypeScript, MIT) provides two tools: `analyze_repo` flattens a codebase using [Repomix](https://github.com/yamadashy/repomix), and `code_review` performs an LLM-powered review. The flattening step is key — Repomix converts a repository into a single file that fits within LLM context windows, enabling whole-project analysis rather than per-file review. Supports OpenAI, Anthropic, and Google models. Reviews are structured as JSON objects with issue categorization (security, performance, quality, maintainability), severity ratings, line numbers, and actionable recommendations. Automatic code chunking handles large projects. Includes CLI for standalone testing.

**praneybehl/code-review-mcp** (30 stars, 7 forks, TypeScript, MIT, npm: `@vibesnipe/code-review-mcp`) uses the Vercel AI SDK for multi-provider LLM support (Google Gemini, OpenAI, Anthropic). Analyzes git diffs for staged changes, HEAD comparisons, or branch differences. Customizable review context through task descriptions and project information. Markdown-formatted output. Works with Claude Code, Cursor, and Windsurf. Install via `npx` — no global setup required.

**Orcus2021/code-review-mcp-server** (6 stars, TypeScript, v1.5.1) is the most workflow-complete community server. Seven tools: `CodeReview` (git diff with review guidance), `GetLocalGitDiff` (raw diff), `CodeReviewWithGithubUrl` (fetch PR diffs), `AddPRSummaryComment` (post aggregate feedback), `AddPRLineComment` (inline comments on specific lines), `GetPRTemplate` (retrieve PR templates), `CreatePR` (generate PRs with auto-detected repo data). Notion integration lets teams define custom review guidelines; falls back to local markdown instructions. CI pipeline automation via n8n webhooks.

### Notable Absences

**Qodo/PR-Agent** (10.5k stars, the most popular open-source AI PR reviewer) does not expose an MCP server. PR-Agent provides review, describe, improve, and ask tools via GitHub bot, but these aren't available as MCP tools. Qodo recently shipped "agent skills" for Claude Code and Cursor, but these operate as IDE integrations, not MCP servers.

**Ellipsis** (AI code review + bug fixes) uses MCP servers internally as part of its architecture but doesn't provide a public MCP server for developers to integrate.

**CodeAnt AI, Panto AI, Bito, Sourcery** — all popular AI code review tools — have no MCP servers. They integrate via GitHub/GitLab apps and IDE extensions, not MCP.

**Azure DevOps** — No MCP server for Azure DevOps pull requests. Given Azure DevOps' significant enterprise market share, this is a meaningful gap.

**Gerrit** — No MCP server exists for the Gerrit code review system used by Android, Chromium, and other large open-source projects.

## Developer Tools MCP — Cross-Category Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging | Profiling | Code Review |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|----------|-----|----------|----------|---------|---------|--------------|-------------|-----------|-----------|-------------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, 1.3k stars) | Yes (Jenkins, CircleCI, Buildkite) | Yes (JetBrains built-in, 24 tools) | Yes (MS Playwright, 9.8k stars, 24 tools) | Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana) | Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) | Yes (NuGet built-in VS 2026, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B 384, JetBrains built-in server) | Yes (Postman 192, Apollo GraphQL 275, Kong deprecated, Apigee, MuleSoft) | Yes (Splunk 13 tools GA, Grafana Tempo built-in, Grafana Loki 103 stars) | Partial (Liquibase private preview, Prisma built-in CLI) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector 9.2k official) | Partial (CodSpeed MCP, Polar Signals remote, Grafana Pyroscope via mcp-grafana) | Yes (SonarQube 442 stars, Codacy 56 stars, Graphite GT built-in) |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (1.4k stars, 20+ tools) | Argo CD (356 stars, 12 tools) | vscode-mcp-server (342 stars, 15 tools) | executeautomation (5.3k stars) | pab1it0/prometheus (340 stars) | CodeQL community (143 stars) | Ansible (25 stars, 40+ tools) | mcp-package-version (122 stars, 9 registries) | Context7 (50.3k stars), magic-mcp (4.5k stars) | openapi-mcp-generator (495 stars), mcp-graphql (374 stars) | cr7258/elasticsearch (259 stars), Traceloop OTel (178 stars) | mpreziuso/mcp-atlas (Atlas), defrex/drizzle-mcp (Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars) | theSharque/mcp-jperf (Java JFR), PageSpeed Insights MCP servers | kopfrechner/gitlab-mr-mcp (86 stars), crazyrabbitLTC (32 stars) |
| **Primary function** | Repository operations | Repository operations | Repository operations | Container lifecycle | Cluster management | Pipeline management | Editor integration | Test execution | Observability queries | Vulnerability scanning | Infrastructure provisioning | Dependency intelligence | Context provision + UI generation | Spec-to-server conversion + API interaction | Log search/analysis + trace correlation | Schema migration & version control | Doc access, search, generation & quality | Breakpoints, stepping, variable inspection, crash analysis | Flamegraph analysis, CPU/memory profiling, benchmarks, web audits, load testing | Code quality analysis, PR management, diff review, stacked PR creation |
| **Vendor count** | 1 (GitHub) | 1 (GitLab) | 0 (Atlassian via Jira only) | 1 (Docker) + community | 0 (Red Hat leads community) | 3 (Jenkins, CircleCI, Buildkite) | 1 (JetBrains) | 1 (Microsoft) | 6 (Grafana, Datadog, Sentry, Dynatrace, New Relic, Instana) | 7+ (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | 5+ (HashiCorp, Pulumi, AWS, OpenTofu, Spacelift) | 2 (Microsoft/NuGet, Homebrew) | 3 (Vercel, E2B, Upstash/Context7) | 4+ (Postman, Apollo, Kong, Google/Apigee, MuleSoft) | 6+ (Splunk, Grafana/Loki, Grafana/Tempo, Coralogix, Axiom, Mezmo) | 2 (Liquibase, Prisma) + Google partial | 5+ (Microsoft, Mintlify, ReadMe, Stainless, OpenAI, Vonage, Fern, Apidog) | 3 (Google/Chrome DevTools, Microsoft/DebugMCP, LLVM/LLDB built-in) | 3 (CodSpeed, Polar Signals, Tricentis/NeoLoad) + Grafana partial | 3 (SonarSource, Codacy, Graphite) + CodeRabbit as client |
| **Code generation role** | Context (repos, issues, PRs) | Context (repos, issues, MRs) | Context (repos, PRs) | Context (images, containers) | Context (cluster state) | Context (pipeline status) | Bidirectional (tools + context) | Context (test results) | Context (metrics, logs) | Context (vulnerabilities) | Generation (IaC templates) | Context (versions, advisories) | Direct (UI components, docs, execution) | Bidirectional (spec-to-tools, API execution) | Context (log patterns, traces, errors) | Bidirectional (migration generation + schema inspection) | Context (doc access/search) + Generation (doc output) | Bidirectional (set breakpoints + inspect state) | Context (profiles, flamegraphs, benchmarks) + Generation (benchmark harnesses) | Bidirectional (quality data as context + review comments as output) |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | API tokens per platform | Local connection (port/stdio) | None (local browsers) | API tokens / OAuth (remote) | API tokens / CLI auth | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / API keys | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect | API keys (CodSpeed, Polar Signals) / Grafana auth / Google API key (PageSpeed) | API tokens (SonarQube, Codacy) / GitHub PAT / GitLab PAT |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | No | No (but Microsoft is Platinum) | No (but Microsoft is Platinum) | No | No | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) | No | No |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | 5.6M developers | Jenkins: 11.3M devs | VS Code: 75.9% market share | Playwright: 45.1% QA adoption | Datadog: 32.7k customers | SonarQube: 17.7% SAST mindshare | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 30M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Flyway: 10.7k stars, Liquibase: 5.2k stars, Prisma: 43k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars | Chrome: 65%+ browser share, VS Code: 75.9% IDE share | APM market: $7-10B, Pyroscope: 11k+ stars, async-profiler: 9k+ stars | SonarQube: 7.4M+ users, CodeRabbit: top AI reviewer, Qodo/PR-Agent: 10.5k stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | [4/5](/reviews/kubernetes-mcp-servers/) | [3/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) | [3.5/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | [3/5](/reviews/package-management-mcp-servers/) | [3.5/5](/reviews/code-generation-mcp-servers/) | [3.5/5](/reviews/api-development-mcp-servers/) | [3.5/5](/reviews/logging-tracing-mcp-servers/) | [2.5/5](/reviews/database-migration-mcp-servers/) | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | [4.5/5](/reviews/debugging-mcp-servers/) | [3/5](/reviews/profiling-performance-mcp-servers/) | 3.5/5 |

## Known Issues

1. **The biggest AI PR reviewer has no MCP server** — Qodo/PR-Agent (10.5k stars) is the most popular open-source AI code reviewer, but it doesn't expose MCP tools. It operates through GitHub webhooks, CLI commands, and IDE extensions. Qodo's "agent skills" for Claude Code and Cursor are a step toward MCP-style integration, but they're not MCP servers. This means the tool most developers would want to connect to their AI assistant via MCP simply isn't available that way.

2. **CodeRabbit is an MCP client, not server** — CodeRabbit dominates AI code review but approaches MCP from the opposite direction. It consumes context from MCP servers to enrich reviews, rather than exposing its review capabilities as MCP tools. You can't ask your AI assistant to "run a CodeRabbit review on this PR" through MCP. The community coderabbitai-mcp server (26 stars) only reads existing reviews — it can't trigger new ones.

3. **Community review servers use LLMs to review LLM-generated code** — Most community code review MCP servers (crazyrabbitLTC, praneybehl) work by sending diffs to another LLM for analysis. This creates a circular pattern when the code was itself AI-generated: AI writes code, then AI reviews AI's code through an MCP server that calls AI. The review adds latency and cost without necessarily adding the independent perspective that human review provides.

4. **No Azure DevOps PR MCP server** — Azure DevOps has significant enterprise market share for source control and code review, but no MCP server supports Azure DevOps pull requests. GitHub, GitLab, and Bitbucket all have MCP coverage. Enterprise teams on Azure DevOps are locked out of MCP-powered code review workflows.

5. **SonarQube MCP requires JDK 21** — The SonarQube MCP server requires JDK 21+, which is a heavy dependency for teams not already running Java. SonarQube Cloud's native embedded MCP (March 2026) removes this requirement, but only for Cloud customers. SonarQube Server users still need the JDK dependency. Codacy's TypeScript-based server is lighter to deploy.

6. **Graphite GT MCP is beta and Graphite-locked** — GT MCP only works with Graphite's stacking workflow. Teams using GitHub's native PR model, GitLab merge requests, or other branching strategies can't use it. The beta status means some workflows may break. No open-source alternative exists for AI-driven stacked PR creation.

7. **No code review analytics MCP** — No MCP server provides review metrics: time-to-review, review thoroughness, comment resolution rates, reviewer workload distribution, or review coverage. These analytics are critical for engineering managers but exist only in proprietary dashboards (Graphite, LinearB, Sleuth, Swarmia) with no MCP exposure.

8. **Community servers have low adoption** — The most-starred dedicated code review MCP server (crazyrabbitLTC) has only 32 stars. Compare this with the GitHub MCP server (28.2k stars) or even Chrome DevTools MCP (31k stars). Code review MCP adoption is still in very early stages despite being a high-impact use case.

9. **No Gerrit MCP server** — Gerrit, the code review system used by Android (Google), Chromium, Eclipse, LibreOffice, and other large projects, has no MCP server. Gerrit's review model (change-based, not PR-based) would benefit from MCP integration, but the community hasn't built one.

10. **Review and repository overlap is confusing** — GitHub's MCP server (28.2k stars) includes PR review tools (get_pull_request, create_review, list_reviews). GitLab's official MCP includes MR management. These overlap with dedicated code review MCP servers, making it unclear when developers should use the platform server vs. a specialized review server. The specialized servers add LLM analysis or quality gate integration, but the boundary isn't always obvious.

## Bottom Line

**Rating: 3.5 out of 5**

Code review and pull request MCP servers address the most critical bottleneck in modern software development — review capacity. [SonarQube MCP](https://github.com/SonarSource/sonarqube-mcp-server) (442 stars, native in SonarQube Cloud since March 2026) leads with established code quality integration across 11+ AI platforms. [Codacy MCP](https://github.com/codacy/codacy-mcp-server) (56 stars, MIT) adds breadth with SAST, secrets scanning, coverage, and PR tools. [Graphite GT MCP](https://graphite.com/docs/gt-mcp) innovates with AI-driven stacked PR creation — solving the reviewability problem rather than the review itself. [CodeRabbit](https://www.coderabbit.ai/) dominates AI review but as an MCP client, not server. Community servers ([crazyrabbitLTC](https://github.com/crazyrabbitLTC/mcp-code-review-server), [praneybehl](https://github.com/praneybehl/code-review-mcp)) connect LLMs to diffs for automated feedback. [kopfrechner/gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp) (86 stars, 10 tools) handles GitLab merge request management.

The **3.5/5 rating** reflects: genuine vendor commitment (SonarQube native Cloud MCP, Codacy's MCP-native positioning, Graphite embedding MCP into its CLI), breadth of approach (quality platforms, PR management, stacked workflows, LLM review agents), SonarQube Cloud's zero-install MCP breakthrough, and active community development. Points are lost for the biggest PR reviewer (Qodo/PR-Agent, 10.5k stars) lacking an MCP server, CodeRabbit operating as client rather than server, circular LLM-reviews-LLM patterns in community servers, no Azure DevOps coverage, low community adoption (32 stars for the top dedicated server), Graphite's beta status and vendor lock, no review analytics, and no Gerrit support.

**Who benefits from code review MCP servers today:**

- **SonarQube users** — Native Cloud MCP or self-hosted server brings quality gates, vulnerability scans, and code smell detection into AI workflows across 11+ platforms
- **Codacy users** — Full-spectrum code quality (SAST, secrets, coverage, PR analysis) through a lightweight TypeScript MCP server
- **Graphite users** — GT MCP lets AI agents create stacked PRs, making AI-generated code reviewable by humans
- **GitLab teams** — [gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp) enables AI agents to manage MR workflows (86 stars, 10 tools)
- **Teams wanting LLM-powered review** — Community servers add AI analysis on top of existing diffs
- **CodeRabbit users** — The coderabbitai-mcp bridge lets AI assistants interact with existing CodeRabbit reviews

**Who should wait:**

- **Qodo/PR-Agent users** — The most popular open-source reviewer (10.5k stars) has no MCP server
- **Azure DevOps teams** — No MCP support for Azure DevOps pull requests
- **Teams wanting CodeRabbit as MCP server** — CodeRabbit exposes no review-triggering MCP tools
- **Gerrit users** — No MCP server exists for Gerrit's change-based review model
- **Teams needing review analytics** — No MCP server provides review metrics or workload data

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*

