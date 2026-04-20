# Bitbucket MCP Servers — The Missing Piece in Atlassian's AI Strategy

> Atlassian's official MCP server supports Jira and Confluence but not Bitbucket.


**At a glance:** Atlassian's [official Remote MCP Server](https://github.com/atlassian/atlassian-mcp-server) (475 stars, Apache-2.0) supports **Jira, Confluence, and Compass** — but **not Bitbucket**. The community has created multiple Bitbucket-specific MCP servers, led by [aashari/mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket) (132 stars, 6 tools), [MatanYemini/bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp) (109 stars, 25+ tools), and [garc33/bitbucket-server-mcp-server](https://github.com/garc33/bitbucket-server-mcp-server) (57 stars, 21 tools for Bitbucket Server/DC). None has reached dominant status, and the ecosystem lags far behind [GitHub](/reviews/github-mcp-server/) (28.2k-star official server) and [GitLab](/reviews/gitlab-mcp-server/) (built-in official server + 1.2k-star community leader). The feature request for official Bitbucket MCP support is tracked as **BCLOUD-23748**.

Atlassian is a **~$6.4B annual revenue** public company (NASDAQ: TEAM) with **~12,000 employees** (before a 10% layoff announced March 2026). Bitbucket serves approximately **41,000 companies** with a **2.78% market share** in source code management — a distant third behind GitHub (180M+ developers) and GitLab (30M+ users). Atlassian is **not a member of the [Agentic AI Foundation (AAIF)](https://aaif.io/)**. The company's AI investment is concentrated on **Rovo**, its AI assistant, which powers the official MCP server for Jira and Confluence but has not yet been extended to Bitbucket.

**Architecture note:** The gap between Atlassian's Jira/Confluence MCP support and Bitbucket's absence is the defining story here. Atlassian clearly sees MCP as strategic — they built a remote MCP server with OAuth 2.1, included it free for all Cloud customers, and open-sourced it on GitHub. But Bitbucket was left out, likely reflecting its lower strategic priority within the Atlassian portfolio. Community servers exist but are fragmented across Cloud vs Server/Data Center, with different tool sets, authentication approaches, and maintenance levels. This is the **third review in our Developer Tools MCP category**.

**Category:** [Developer Tools](/categories/developer-tools/)

## What's Available

### Atlassian Official Remote MCP Server (No Bitbucket)

Atlassian's **first-party MCP server** — notably excluding Bitbucket:

| Aspect | Detail |
|--------|--------|
| Repository | [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) |
| Stars | ~475 |
| Products | Jira, Confluence, Compass |
| Authentication | OAuth 2.1, API tokens |
| Pricing | Free for all Atlassian Cloud customers (rate-limited by plan) |
| License | Apache-2.0 |

**46 tools** covering Jira search, issue management, Confluence page management, and Compass service catalog — but **zero Bitbucket tools**. Works with Claude, ChatGPT, GitHub Copilot CLI, Gemini CLI, VS Code, and any MCP-compatible client. Rate limits: 500 calls/hour (Free), 1,000+ calls/hour (Standard/Premium/Enterprise).

**Why this matters for Bitbucket users:** If your organization uses Atlassian's full stack (Jira + Confluence + Bitbucket), you can connect AI agents to your project management and documentation — but not to your code repositories. The integration gap forces Bitbucket users to rely on community servers with different authentication models and maintenance expectations.

### MatanYemini/bitbucket-mcp (Most Tools)

The **most feature-rich** community Bitbucket MCP server:

| Aspect | Detail |
|--------|--------|
| Repository | [MatanYemini/bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp) |
| Stars | ~109 |
| Forks | ~65 |
| Commits | 65 |
| Language | TypeScript |
| License | MIT |
| Target | Bitbucket Cloud |

**25+ tools** focused heavily on pull request management:

| Category | Tools |
|----------|-------|
| Repositories | `listRepositories`, `getRepository` |
| Pull Requests | `getPullRequests`, `createPullRequest`, `getPullRequest`, `updatePullRequest`, `getPullRequestActivity`, `approvePullRequest`, `unapprovePullRequest`, `declinePullRequest`, `mergePullRequest`, `requestChanges`, `removeChangeRequest` |
| Draft PRs | `createDraftPullRequest`, `publishDraftPullRequest`, `convertToDraft` |
| PR Comments | `getPullRequestComments` |

**Key differentiator:** Safety-first design — no DELETE operations are implemented. Pagination support with auto-fetching (capped at 1,000 entries). CodeQL security scanning on all pull requests. Docker support included. Configuration supports both API URL format and legacy web URL.

**Limitation:** Bitbucket Cloud only — no Server/Data Center support. No issue management (Bitbucket Cloud has issues, though most teams use Jira). No pipeline management. No file content access or code search.

### aashari/mcp-server-atlassian-bitbucket (Most Stars)

The **most-starred** dedicated Bitbucket MCP server:

| Aspect | Detail |
|--------|--------|
| Repository | [aashari/mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket) |
| Stars | ~132 |
| Forks | ~48 |
| Commits | 595 |
| Language | TypeScript |
| NPM Package | `@aashari/mcp-server-atlassian-bitbucket` |

**6 generic REST API tools:**

| Tool | What it does |
|------|-------------|
| `bb_get` | Retrieve data from any Bitbucket API endpoint |
| `bb_post` | Create resources via API endpoints |
| `bb_put` | Replace resources via API endpoints |
| `bb_patch` | Apply partial updates to resources |
| `bb_delete` | Remove resources from endpoints |
| `bb_clone` | Clone repositories locally |

**Key differentiator:** Rather than building specific tools for each operation, this server exposes generic CRUD operations against the Bitbucket API. The LLM constructs the correct API paths. Uses **TOON (Token-Oriented Object Notation)** format that claims 30-60% fewer tokens than JSON. Supports JMESPath filtering for response customization. Dual auth: Scoped API Tokens and legacy App Passwords.

**Limitation:** Generic API tools put the burden on the LLM to know Bitbucket's API structure. More error-prone than purpose-built tools. The tool count (6) is misleading — it's really 5 HTTP verbs plus clone.

### garc33/bitbucket-server-mcp-server (Server/DC)

The leading **Bitbucket Server / Data Center** MCP server:

| Aspect | Detail |
|--------|--------|
| Repository | [garc33/bitbucket-server-mcp-server](https://github.com/garc33/bitbucket-server-mcp-server) |
| Stars | ~57 |
| Forks | ~41 |
| Commits | 55 |
| Language | TypeScript |
| Target | Bitbucket Server / Data Center |

**21 tools** covering PR management, code discovery, and repository operations:

| Tool | What it does |
|------|-------------|
| `list_projects` | Discover accessible Bitbucket projects |
| `list_repositories` | Browse repositories within projects |
| `create_pull_request` | Submit code changes for review |
| `get_pull_request` | Retrieve detailed PR information |
| `merge_pull_request` | Integrate with multiple merge strategies |
| `decline_pull_request` | Reject pull requests |
| `approve_pull_request` | Approve code changes |
| `unapprove_pull_request` | Retract approvals |
| `list_pull_requests` | Filter PRs by state/author |
| `add_comment` | Participate in code review |
| `get_diff` | Analyze code changes |
| `get_reviews` | Track review progress |
| `get_activities` | Retrieve PR timeline |
| `get_comments` | Extract PR comments |
| `search` | Advanced code/file search |
| `get_file_content` | Read file contents |
| `browse_repository` | Explore repository structure |
| `list_branches` | Explore branches |
| `list_commits` | Browse commit history |
| `delete_branch` | Clean up merged branches |

**Key differentiator:** The only well-established MCP server targeting Bitbucket Server/Data Center. Custom HTTP header support via environment variable. Merge strategy selection. File content with pagination. This matters for enterprises that run Bitbucket on-premise and can't use Cloud-only solutions.

### Other Notable Servers

**b1ff/atlassian-dc-mcp** (59 stars, 175 commits, TypeScript, MIT) — Multi-product MCP server covering Jira, Confluence, and Bitbucket for Data Center deployments. Monorepo with separate packages per product (`@atlassian-dc-mcp/bitbucket`). Good for teams that want one MCP server for the full Atlassian DC stack.

**Ibrahimogod/bitbucket-mcp** (0 stars, Rust, MIT, 20+ tools) — High-performance Rust implementation with comprehensive Bitbucket Cloud API coverage including pipelines, deployments, webhooks, and snippets. Docker-ready via GHCR images. Well-engineered but zero adoption. The Rust implementation may appeal to performance-sensitive deployments.

**sooperset/mcp-atlassian** (4.7k stars, 558 commits, Python, MIT, 72 tools) — By far the most popular Atlassian MCP server, but it **only supports Jira and Confluence** — not Bitbucket. Mentioned here because users searching for "Atlassian MCP" will find this first and may assume it covers Bitbucket.

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging | Profiling | Code Review |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|---------- | ------- |----------|----------|---------|---------------------- | --------------|-----------|-----------|-------------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | [No (Red Hat leads, 1.3k stars)](/reviews/kubernetes-mcp-servers/) | [Yes (Jenkins, CircleCI, Buildkite)](/reviews/ci-cd-mcp-servers/) | Yes (JetBrains built-in, 24 tools) | [Yes (MS Playwright, 9.8k stars, 24 tools)](/reviews/testing-qa-mcp-servers/) | [Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana)](/reviews/monitoring-observability-mcp-servers/) | [Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast)](/reviews/security-scanning-mcp-servers/) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) | Yes (NuGet built-in VS 2026, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B 384, JetBrains built-in server) | Yes (Postman 192, Apollo GraphQL 275, Kong deprecated, Apigee, MuleSoft) | Yes (Splunk 13 tools GA, Grafana Tempo built-in, Grafana Loki 103 stars) | Partial (Liquibase private preview 19 tools, Prisma built-in CLI v6.6.0+) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector 9.2k official) | Partial (CodSpeed MCP, Polar Signals remote, Grafana Pyroscope via mcp-grafana) | Yes (SonarQube 442 stars, Codacy 56 stars, Graphite GT built-in) |
| **Remote hosting** | Yes (`api.githubcopilot.com/mcp/`) | No | No | No | [AWS EKS MCP (preview)](/reviews/kubernetes-mcp-servers/) | [Yes (Buildkite remote MCP)](/reviews/ci-cd-mcp-servers/) | No (requires running IDE) | [No (local browser required)](/reviews/testing-qa-mcp-servers/) | [Yes (Datadog, Sentry — OAuth)](/reviews/monitoring-observability-mcp-servers/) | [No (all local/CLI-based)](/reviews/security-scanning-mcp-servers/) | [Yes (Pulumi remote MCP)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | N/A | N/A | — | N/A | No (local debuggers) | No (all local CLI/API) | No (all local/API-based) |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | [Flux159 (1.4k stars, 20+ tools)](/reviews/kubernetes-mcp-servers/) | [Argo CD (356 stars, 12 tools)](/reviews/ci-cd-mcp-servers/) | vscode-mcp-server (342 stars, 15 tools) | [executeautomation (5.3k stars)](/reviews/testing-qa-mcp-servers/) | [pab1it0/prometheus (340 stars)](/reviews/monitoring-observability-mcp-servers/) | [CodeQL community (143 stars)](/reviews/security-scanning-mcp-servers/) | Ansible (25 stars, 40+ tools) | mcp-package-version (122 stars, 9 registries) | Context7 (50.3k stars), magic-mcp (4.5k stars) | openapi-mcp-generator (495 stars), mcp-graphql (374 stars) | cr7258/elasticsearch (259 stars), Traceloop OTel (178 stars) | mpreziuso/mcp-atlas (Atlas), defrex/drizzle-mcp (Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars), Docs MCP (87 stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars), devtools-debugger (341 stars) | theSharque/mcp-jperf (Java JFR), PageSpeed Insights MCP servers | kopfrechner/gitlab-mr-mcp (86 stars), crazyrabbitLTC (32 stars) |
| **Community tool count** | 28+ (local Git) | 100+ | 25+ | 25 (container mgmt) | [20+ (core) + Helm](/reviews/kubernetes-mcp-servers/) | [9-21 per server](/reviews/ci-cd-mcp-servers/) | 13-19 per server | [24 (official) + API testing](/reviews/testing-qa-mcp-servers/) | [16+ (Datadog) to 100+ (Instana)](/reviews/monitoring-observability-mcp-servers/) | [7 (Semgrep) to full platform (Snyk)](/reviews/security-scanning-mcp-servers/) | [20+ (Terraform), full platform (Pulumi)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | Spec-to-server conversion + API interaction | N/A | — | N/A | N/A | N/A | Code quality analysis, PR management, diff review, stacked PR creation |
| **Server/DC support** | N/A (cloud-only) | Community servers | garc33 (57 stars, 21 tools) | All local | [All local + cloud managed](/reviews/kubernetes-mcp-servers/) | [Jenkins plugin (on-prem)](/reviews/ci-cd-mcp-servers/) | N/A | N/A | [Grafana, Prometheus (self-hosted)](/reviews/monitoring-observability-mcp-servers/) | [Yes (all local/CLI-based)](/reviews/security-scanning-mcp-servers/) | [Yes (all local/CLI-based)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | 4+ (Postman, Apollo, Kong, Google/Apigee, MuleSoft) | N/A | — | N/A | N/A | N/A | SonarQube (self-hosted), Codacy (cloud) |
| **MCP infrastructure role** | None | None | None | [Gateway + Catalog (300+)](/reviews/docker-mcp-servers/) | None | None | None | None | None | None | None | N/A | N/A | Bidirectional (spec-to-tools, API execution) | N/A | — | N/A | N/A | N/A | None |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | [kubeconfig / OAuth / OIDC](/reviews/kubernetes-mcp-servers/) | [API tokens per platform](/reviews/ci-cd-mcp-servers/) | Local connection (port/stdio) | [None (local browsers)](/reviews/testing-qa-mcp-servers/) | [API tokens / OAuth (remote)](/reviews/monitoring-observability-mcp-servers/) | [API tokens / CLI auth](/reviews/security-scanning-mcp-servers/) | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / CLI auth | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect | API keys (CodSpeed, Polar Signals) / Grafana auth / Google API key (PageSpeed) | API tokens (SonarQube, Codacy) / GitHub PAT / GitLab PAT |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | [No (Google/AWS/MS are Platinum)](/reviews/kubernetes-mcp-servers/) | [No](/reviews/ci-cd-mcp-servers/) | No (but Microsoft is Platinum) | [No (but Microsoft is Platinum)](/reviews/testing-qa-mcp-servers/) | [No](/reviews/monitoring-observability-mcp-servers/) | [No](/reviews/security-scanning-mcp-servers/) | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) | No | No |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | [5.6M developers](/reviews/kubernetes-mcp-servers/) | [Jenkins: 11.3M devs](/reviews/ci-cd-mcp-servers/) | VS Code: 75.9% market share | [Playwright: 45.1% QA adoption](/reviews/testing-qa-mcp-servers/) | [Datadog: 32.7k customers](/reviews/monitoring-observability-mcp-servers/) | [SonarQube: 17.7% SAST mindshare](/reviews/security-scanning-mcp-servers/) | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads, PyPI: 421.6B yearly | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 30M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Prisma: 43k stars, Flyway: 10.7k stars, Atlas: 6.3k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars, ReadMe: powering major API docs | Chrome: 65%+ browser share, VS Code: 75.9% IDE share, x64dbg: 45k+ stars | APM market: $7-10B, Pyroscope: 11k+ stars, async-profiler: 9k+ stars | SonarQube: 7.4M+ users, CodeRabbit: top AI reviewer, Qodo/PR-Agent: 10.5k stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | 2.5/5 | [4/5](/reviews/docker-mcp-servers/) | [4/5](/reviews/kubernetes-mcp-servers/) | [3/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) | [3.5/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | [3/5](/reviews/package-management-mcp-servers/) | [3.5/5](/reviews/code-generation-mcp-servers/) | [3.5/5](/reviews/api-development-mcp-servers/) | [3.5/5](/reviews/logging-tracing-mcp-servers/) | [2.5/5](/reviews/database-migration-mcp-servers/) | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | [4.5/5](/reviews/debugging-mcp-servers/) | [3/5](/reviews/profiling-performance-mcp-servers/) | [3.5/5](/reviews/code-review-pull-request-mcp-servers/) |

## Known Issues

1. **No official Bitbucket MCP server** — Atlassian's Remote MCP Server supports Jira, Confluence, and Compass but explicitly excludes Bitbucket. Feature request BCLOUD-23748 is open, with community members noting that "the primary competitor has MCP support." This is the single biggest gap.

2. **Cloud vs Server/DC fragmentation** — Bitbucket Cloud and Bitbucket Server/Data Center have different APIs. MatanYemini's server targets Cloud only; garc33's targets Server/DC only. No single server covers both. Teams migrating between deployments need different MCP servers.

3. **No clear community leader** — The highest-starred dedicated server (aashari, 132 stars) uses generic REST API tools rather than purpose-built operations. The most feature-rich (MatanYemini, 109 stars, 25+ tools) has decent adoption but limited scope. Neither has achieved the kind of community momentum seen in GitHub or GitLab ecosystems.

4. **Missing pipeline management** — Bitbucket Pipelines is a key feature for CI/CD, but most MCP servers lack pipeline management tools. Only the Rust implementation (Ibrahimogod, 0 stars) includes pipeline access, and it has no adoption.

5. **Generic API tools are fragile** — aashari's server exposes raw HTTP verbs against the Bitbucket API, relying on the LLM to construct correct paths and payloads. This works for simple operations but is error-prone for complex workflows. Purpose-built tools with validated parameters are more reliable.

6. **sooperset confusion** — The most popular Atlassian MCP server (sooperset/mcp-atlassian, 4.7k stars) does not support Bitbucket. Users may install it expecting Bitbucket coverage and find none. The name "mcp-atlassian" implies full Atlassian product coverage.

7. **Atlassian's AI pivot creates uncertainty** — Atlassian announced 10% layoffs in March 2026 to pivot toward AI and enterprise sales. This could accelerate official Bitbucket MCP support (as AI becomes a priority) or delay it (if Bitbucket is deprioritized in the restructuring). The outcome is unclear.

8. **No code search or file browsing in top Cloud server** — MatanYemini's server (most tools for Cloud) focuses heavily on PRs but can't read file contents, search code, or browse repository structure. For code-level AI workflows, this is a significant gap.

9. **Authentication complexity** — Bitbucket Cloud uses App Passwords or OAuth Consumer credentials. Bitbucket Server/DC uses HTTP access tokens. The official Atlassian MCP server uses OAuth 2.1. Community servers each implement authentication differently, creating setup friction and security confusion.

10. **Write operations without guardrails** — Several servers allow merging pull requests, deleting branches, and creating PRs without confirmation mechanisms. An unconstrained AI agent could merge untested code or delete active branches. Only MatanYemini's server takes a safety-first approach (no DELETE operations).

## Bottom Line

**Rating: 2.5 out of 5**

Bitbucket has the **weakest MCP ecosystem** among the Big 3 Git hosting platforms — and the gap is widening. GitHub has a 28.2k-star official server with remote hosting and Copilot integration. GitLab has a built-in official MCP server plus a 1.2k-star community leader with 100+ tools. Bitbucket has no official MCP support from Atlassian, a fragmented community ecosystem where the top server has 132 stars, and a Cloud/Server split that divides an already small user base.

The **2.5/5 rating** reflects the absence of official Bitbucket MCP support despite Atlassian having a production MCP server for other products, fragmented community servers with no dominant player (132 stars max vs GitHub's 28.2k), Cloud/Server API split requiring different MCP servers, missing pipeline management in most servers, and competitive pressure from GitHub and GitLab. It earns points for having multiple functional community servers (MatanYemini's 25+ PR tools, garc33's 21-tool Server/DC coverage, b1ff's multi-product DC solution), the existence of a tracked feature request (BCLOUD-23748), and the reasonable expectation that Atlassian's AI pivot will eventually bring official support.

**Who benefits from Bitbucket MCP servers today:**

- **Bitbucket Cloud teams focused on PRs** — MatanYemini/bitbucket-mcp provides solid pull request management (create, review, approve, merge, draft workflows) for Cloud users
- **Bitbucket Server/DC enterprises** — garc33's server offers 21 tools covering PRs, code search, file browsing, and branch management for on-premise deployments
- **Full Atlassian DC stack users** — b1ff/atlassian-dc-mcp covers Jira + Confluence + Bitbucket in one MCP server for Data Center
- **API-savvy teams** — aashari's generic REST tools work for any Bitbucket API operation, provided the LLM can construct correct API paths

**Who should be cautious:**

- **Teams comparing platforms** — if you're choosing between GitHub, GitLab, and Bitbucket for AI-enhanced workflows, Bitbucket's MCP ecosystem is a clear competitive disadvantage
- **Organizations expecting official support** — Atlassian has not committed to a Bitbucket MCP timeline; BCLOUD-23748 is a feature request, not a roadmap item
- **Pipeline-heavy teams** — if CI/CD pipeline management via AI agents is important, Bitbucket MCP servers largely don't cover it
- **Security-conscious enterprises** — community-maintained servers without official backing carry different risk profiles than vendor-supported solutions

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*

