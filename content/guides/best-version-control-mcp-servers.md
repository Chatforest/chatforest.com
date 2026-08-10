---
title: "Best Version Control MCP Servers in 2026"
date: 2026-03-22T23:00:00+09:00
description: "GitHub, GitLab, Bitbucket, Azure DevOps, Perforce, and more — we've reviewed 30+ version control MCP servers across 7 categories. Here's what works, what's emerging, and where the gaps are."
og_description: "30+ version control MCP servers reviewed across GitHub, GitLab, Bitbucket, local Git, Azure DevOps, Perforce, and code search. The definitive comparison with honest ratings."
content_type: "Comparison"
card_description: "The definitive guide to version control MCP servers in 2026. We've reviewed 30+ servers across GitHub, GitLab, Bitbucket, local Git, Azure DevOps, Perforce, and code search. Every recommendation links to a full review."
last_refreshed: 2026-08-11
sources_audited: 2026-08-11
---

Version control MCP servers are the backbone of AI-assisted development. These servers let AI agents manage repositories, create pull requests, review code, monitor CI/CD pipelines, and interact with Git — all through natural language instead of memorizing CLI flags or clicking through web UIs.

We've researched 30+ version control MCP servers across the entire landscape. This guide synthesizes all of that into one page: what's worth using, what's not, and where the gaps are.

*Note: Our recommendations are based on documentation review, GitHub analysis, and community feedback — not hands-on testing of every server. Star counts were verified in April 2026 and re-verified against live repos in August 2026.*

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| GitHub (platform) | [github/github-mcp-server](https://github.com/github/github-mcp-server) | 32,100 | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) (89,400-star monorepo; its GitHub reference server has since been archived — see below) |
| GitLab (platform) | [zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) | 1,900 | [GitLab Official MCP](https://docs.gitlab.com/user/model_context_protocol/mcp_server/) (beta, 24 tools) |
| Bitbucket (platform) | [aashari/mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket) | 160 | [MatanYemini/bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp) (Cloud + Server) |
| Local Git operations | [cyanheads/git-mcp-server](https://github.com/cyanheads/git-mcp-server) | 231 | [Official Git MCP](/reviews/git-mcp-server/) (89,400-star monorepo, 12 tools, no push) |
| Azure DevOps | [microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) | 2,000 | [Tiberriver256/mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) (382 stars, community) |
| Perforce | [perforce/p4mcp-server](https://github.com/perforce/p4mcp-server) | 112 | — |
| Code search & navigation | [Sourcegraph MCP](https://sourcegraph.com/mcp) | — | [GitMCP](/reviews/gitmcp-server/) (any repo → docs) |

## Why version control MCP servers matter

Every software project lives in version control. Version control MCP servers add three capabilities that transform development workflows:

1. **Natural language repository management.** Instead of remembering `git rebase -i HEAD~5` or navigating GitHub's PR UI, tell your agent: "Create a PR from this branch with a summary of what changed" or "Show me all open issues labeled 'bug' that haven't been updated in 30 days." The agent translates that into the right API calls or Git commands.
2. **Cross-platform visibility.** An agent with access to GitHub, GitLab, and your local Git repo can answer questions like "What PRs are open across all my projects?" or "Show me the diff between what's deployed and what's on main" — combining data that normally requires switching between multiple tools.
3. **Automated code review and CI/CD monitoring.** "Review this PR for security issues, check if CI passed, and merge if everything looks good" becomes a natural language instruction. AI agents can monitor builds, triage failures, and manage releases programmatically.

The landscape splits into seven categories: **GitHub** (the dominant platform with the most mature MCP server), **GitLab** (split between official and community servers), **Bitbucket** (community-driven, though Atlassian added an official option in April 2026), **local Git** (direct repository operations), **Azure DevOps** (Microsoft's official server plus community alternatives), **Perforce** (a Perforce-hosted, community-supported server now available), and **code search** (Sourcegraph leading cross-repo search).

## GitHub platform servers

GitHub is where most open-source and commercial code lives, and its MCP ecosystem reflects that dominance. The official server is one of the most feature-rich MCP servers in any category.

### The winner: github/github-mcp-server

**Stars:** 32,100 | **Forks:** 4,800 | **Language:** Go | **Status:** Production

[github/github-mcp-server](https://github.com/github/github-mcp-server) is the most popular version control MCP server by a wide margin. Maintained by GitHub themselves, it exposes most of the GitHub API surface through organized toolsets. [Full review →](/reviews/github-mcp-server/)

**Why it wins:** Comprehensive coverage across repositories, issues, pull requests, Actions, Projects, Discussions, code security, and Copilot monitoring. Tools are organized into **toolsets** you can enable or disable — repos, issues, pull_requests, actions, projects, code_security, discussions, copilot, and others. The server ships frequent weekly-cadence releases (it moved to a `v1.x` numbering scheme in 2026; see the [release history](https://github.com/github/github-mcp-server/releases)), including a `search_commits` tool and reduced-size Project item payloads to cut token usage.

**Key features:**
- **~79 tools** across 19 toolsets covering the full GitHub API surface, up from ~56 earlier in 2026 ([toolset documentation](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/configure-toolsets))
- **Remote hosted** at `api.githubcopilot.com/mcp` (zero setup) or run locally
- **OAuth scope filtering** — automatically hides tools you don't have permission to use
- **Secret scanning in AI coding agents** — the `run_secret_scanning` tool, which lets AI agents scan code changes for exposed secrets before commits/PRs, shipped in [public preview in March 2026](https://github.blog/changelog/2026-03-17-secret-scanning-in-ai-coding-agents-via-the-github-mcp-server/) and reached [general availability on May 5, 2026](https://github.blog/changelog/2026-05-05-secret-scanning-with-github-mcp-server-is-now-generally-available/). The March update added 37 new secret detectors across 22 providers (including Vercel, Snowflake, Supabase, Shopify, LangChain, Salesforce, and Figma), bringing push-protected token types to 39 ([source](https://devops.com/github-adds-37-new-secret-detectors-in-march-extends-scanning-to-ai-coding-agents/))
- **Copilot integration** — monitor coding agent jobs, check progress by PR number
- Compatible with VS Code, Claude Desktop, Cursor, Windsurf, and others

**The catch:** With ~79 tools, the server can overwhelm hosts with tool count limits. The remote server can't filter its toolset — you get everything or nothing. Open issues sit around 177, reflecting the server's growing surface area. Diff payloads can be large, eating into token budgets.

**Best for:** Any team using GitHub. It's the default choice and the standard that other platform servers are measured against.

### Also notable: Anthropic's reference GitHub server (now archived)

The [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) monorepo (89,400 stars) used to include a reference GitHub MCP server in TypeScript. As of this update, that server has been removed from the active repo and [moved to `modelcontextprotocol/servers-archived`](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/github) — it's no longer maintained. For GitHub, use the official `github/github-mcp-server` above.

## GitLab platform servers

GitLab's MCP ecosystem is split between an official server (still in beta) and a popular community server with significantly more features.

### The winner: zereight/gitlab-mcp

**Stars:** 1,900 | **Language:** TypeScript | **Status:** Production

[zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) — the first and most feature-complete GitLab MCP server, with tools spanning projects, merge requests, issues, pipelines, wikis, milestones, work items, and search.

**Why it wins:** While GitLab has an official MCP server (see below), the community server from zereight has far more functionality. It covers the full GitLab workflow:

- **Projects:** List, search, manage project settings
- **Merge requests:** Create, update, review, approve, merge
- **Issues:** Full CRUD, labels, assignees, comments
- **Pipelines:** List, create, retry, cancel pipelines; inspect individual jobs and job output
- **Wikis:** Full wiki page management (list, get, create, update, delete) — now including group-level wikis
- **Milestones:** Create, edit, delete, track milestone progress, burndown charts
- **Work items:** New GraphQL-based toolset for GitLab work items
- **Search:** Global, group, and project-level search
- **Multi-instance support:** Connect to multiple GitLab instances simultaneously

**Security features:** OAuth 2.0 authentication and remote per-session authorization via HTTP headers. Read-only mode restricts to non-destructive operations. SSE and Streamable HTTP transports now supported alongside STDIO. Note: versions 2.0.0–2.0.27 had a ReDoS vulnerability (AIKIDO-2026-10260) — update to 2.0.28+ if affected.

**Best for:** Teams using GitLab who want comprehensive MCP coverage today, especially self-managed GitLab instances.

### Runner-up: GitLab Official MCP Server

**Status:** Beta (since GitLab 18.6) | **Transport:** HTTP (recommended) or stdio via mcp-remote

[GitLab's official MCP server](https://docs.gitlab.com/user/model_context_protocol/mcp_server/) integrates with GitLab Duo and supports the 2025-03-26 and 2025-06-18 MCP protocol specifications (added in GitLab 18.7). It was introduced as an experiment in GitLab 18.3 and reached beta in GitLab 18.6.

**Why it's notable:** Being official means it's integrated with GitLab's authentication and permission model natively. It now offers **24 tools** ([full list](https://docs.gitlab.com/user/model_context_protocol/mcp_server_tools/)) including creating issues, creating and inspecting merge requests, retrieving pipeline jobs and logs, searching across the instance, and — new in GitLab 18.10 — a `manage_pipeline` tool for creating, retrying, and cancelling pipelines. Separately, GitLab Duo's MCP *client* capability (GitLab connecting out to external MCP servers like Jira and Slack) [reached GA in GitLab 18.8](https://gitlab.com/gitlab-org/gitlab/-/issues/583831).

**The catch:** It's still in beta, with a smaller tool set than the community server. No public GA timeline announced. It was originally a GitLab Premium/Ultimate feature but [moved to GitLab Free in GitLab 19.2](https://docs.gitlab.com/user/model_context_protocol/mcp_server/) (released July 2026), so it no longer requires a paid tier.

**Best for:** Organizations already using GitLab Duo who want official vendor support and don't need the extended tool set.

### Also notable: glab CLI MCP

GitLab's [glab CLI](https://docs.gitlab.com/cli/mcp/) now includes MCP support, letting you use the CLI as an MCP server. Useful for developers who already use glab and want MCP integration without a separate server.

## Bitbucket platform servers

Bitbucket's MCP ecosystem was community-driven until recently: Atlassian's [Rovo MCP Server added official Bitbucket Cloud support on April 8, 2026](https://www.atlassian.com/blog/bitbucket/the-atlassian-rovo-mcp-server-now-supports-bitbucket-cloud), covering repository browsing, pull requests, and pipeline/deployment status alongside its existing Jira and Confluence coverage. It requires the Bitbucket workspace to be linked to an Atlassian organization and currently supports API-token auth only (OAuth is on the roadmap). The community servers below remain the more mature, flexible options for teams that don't want to link through Atlassian's org model. Note: Bitbucket App Passwords were deprecated on a rolling basis starting June 9, 2026, with full removal by July 28, 2026 ([Atlassian's deprecation notice](https://www.atlassian.com/blog/bitbucket/bitbucket-cloud-transitions-to-api-tokens-enhancing-security-with-app-password-deprecation)) — use Scoped API Tokens for new setups.

### The winner: aashari/mcp-server-atlassian-bitbucket

**Stars:** 160 | **Forks:** 60 | **Language:** TypeScript | **Status:** Production

[aashari/mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket) — a Node.js/TypeScript MCP server for Bitbucket Cloud with 6 generic tools that can access any Bitbucket API endpoint.

**Why it wins:** Instead of hardcoding specific Bitbucket operations, the server provides 6 flexible tools that map to Bitbucket Cloud REST API 2.0 endpoints. JMESPath filtering reduces token costs by letting you extract only the data you need from responses. The "toon" output format provides 30–60% fewer tokens than raw JSON.

**Key features:**
- Access to the full Bitbucket Cloud REST API 2.0
- Workspace, repository, and pull request operations
- JMESPath expression filtering on responses
- STDIO and HTTP transport options
- Scoped API Token and legacy App Password authentication

**Best for:** Teams on Bitbucket Cloud who need flexible API access. The generic tool approach means new Bitbucket API features are accessible immediately without waiting for server updates.

### Runner-up: MatanYemini/bitbucket-mcp

[MatanYemini/bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp) — supports both Bitbucket Cloud and Bitbucket Server (self-hosted), making it the better choice for organizations still running on-premise Bitbucket.

### Also notable

- **[garc33/bitbucket-server-mcp-server](https://github.com/garc33/bitbucket-server-mcp-server)** (66 stars) — specifically targets Bitbucket Server (Data Center) deployments
- **Composio Bitbucket integration** — managed MCP hosting for Bitbucket at [composio.dev/toolkits/bitbucket](https://composio.dev/toolkits/bitbucket)

## Local Git operations

Local Git MCP servers let AI agents interact directly with Git repositories on disk — staging, committing, branching, diffing — without going through a platform API. This is essential for agents that write code and need to commit their own changes.

### The winner: cyanheads/git-mcp-server

**Stars:** 231 | **Language:** TypeScript | **Status:** Production (v2.15.1)

[cyanheads/git-mcp-server](https://github.com/cyanheads/git-mcp-server) — **28 Git tools** across seven categories including clone, commit, branch, diff, log, status, push, pull, merge, rebase, worktree, and tag management.

**Why it wins:** This server does everything the official Git MCP server doesn't. It covers the full Git lifecycle: clone repositories, make changes, commit, push to remotes, pull updates, merge branches, rebase, manage worktrees, and tag releases. Both STDIO and Streamable HTTP transports are supported. Planned isomorphic-git support for edge deployment.

**Key operations:**
- **Full remote support:** push, pull, fetch — not just local operations
- **Merge and rebase** — handle branch integration workflows
- **Worktree management** — work on multiple branches simultaneously
- **Tag management** — create and manage release tags
- **Clone** — initialize new repositories from remotes

**Best for:** AI agents that need to complete the full Git workflow — write code, commit, and push — without handing control back to a human for the remote operations.

### Runner-up: Official Git MCP Server (Anthropic)

**Stars:** 89,400 (monorepo) | **Language:** Python | **Status:** Production

[The official Git MCP server](/reviews/git-mcp-server/) from Anthropic's reference implementations — 12 tools for status, diff, commit, and branch operations. Meaningful adoption: the [`mcp-server-git` PyPI package](https://pypi.org/project/mcp-server-git/) shows roughly 51,000 downloads/week as of August 2026 ([pypistats.org](https://pypistats.org/packages/mcp-server-git)).

**Why it's the runner-up, not the winner:** No push. No pull. No merge. No rebase. No stashing. No tagging. The 12 tools cover local operations up to committing, then stop. It's deliberately minimal — a reference implementation, not a production tool. Three CVEs — [CVE-2025-68143, CVE-2025-68144, and CVE-2025-68145](https://thehackernews.com/2026/01/three-flaws-in-anthropic-mcp-git-server.html) — covering an unrestricted `git_init`, a path-validation bypass, and a `git_diff` file-overwrite bug, were patched in `mcp-server-git` version 2025.12.18 (December 2025).

**Best for:** Learning MCP server architecture, or workflows where a human handles all remote operations. If your agent only needs to read repo state and make local commits, it's sufficient.

### Also notable: GitButler MCP Server

[GitButler](https://blog.gitbutler.com/using-gb-mcp) — a modern Git client with built-in MCP support. The MCP server lets AI agents record commits with the "why" behind a change (not just the diff) and create save points as they work, rather than relying on generic auto-commits. Best for developers already using GitButler who want their AI agent to participate in the same workflow.

## Azure DevOps

Microsoft has invested in an official Azure DevOps MCP server; both the local and remote hosted options have now reached general availability.

### The winner: microsoft/azure-devops-mcp

**Stars:** 2,000 | **Forks:** 621 | **Language:** TypeScript | **Status:** GA (local and remote)

[microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) — Microsoft's official MCP server for Azure DevOps, covering projects, work items, repositories, wikis, and pipelines.

**Why it wins:** It's official and actively maintained by Microsoft. The [local server reached GA on October 13, 2025](https://devblogs.microsoft.com/devops/azure-devops-local-mcp-server-generally-available/), and the [remote hosted MCP server reached GA on August 5, 2026](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-ga/), using Streamable HTTP transport — no local installation required. Tools are organized into domains: core, work, work-items, search, test-plans, repositories, wiki, pipelines, and advanced-security.

**Key features:**
- **Remote hosted** (GA as of August 2026) — Streamable HTTP, no local setup
- **Local server** (GA) — stdio transport for development environments; Microsoft still recommends the remote server where supported
- Core navigation: list organizations, projects, repositories
- Work item management: create, update, query work items
- Repository browsing: file content, repository tree, details
- Wiki access: read and navigate wiki pages
- **Built into Visual Studio 2026** — [Azure MCP Server ships natively via the Azure and AI development workload](https://devblogs.microsoft.com/visualstudio/azure-mcp-server-now-built-in-with-visual-studio-2026-a-new-era-for-agentic-workflows/)
- Compatible with VS Code, Claude Code, Cursor, and Visual Studio 2022/2026

**The catch:** Pipelines, test plans, and artifacts have growing but still limited support compared to core work-item and repo operations.

**Best for:** Enterprise teams using Azure DevOps who want official Microsoft support. The remote hosted option is particularly attractive for organizations that restrict local tool installation.

### Runner-up: Tiberriver256/mcp-server-azure-devops

**Stars:** 382 | **Language:** TypeScript | **Status:** Production

[Tiberriver256/mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) — the community alternative that predates Microsoft's official server. Uses a feature-based architecture with modular tools for projects, work items, repositories, and pull requests.

**Why it's strong:** More mature than the official server in some areas. Supports three authentication methods — Personal Access Token, Azure Identity (DefaultAzureCredential), and Azure CLI authentication. Pull request management includes updating title, description, status, draft state, reviewers, and linked work items.

**Best for:** Teams that need more complete pull request and work item management than the official server currently offers.

## Perforce

Perforce — the version control system used by game studios, chip designers, and large enterprises with massive binary assets — now has an MCP server hosted directly under Perforce's own GitHub organization.

### The winner: perforce/p4mcp-server

**Stars:** 112 | **Language:** Python (FastMCP) | **Status:** Community-supported

[perforce/p4mcp-server](https://github.com/perforce/p4mcp-server) lives in the `perforce` GitHub org, but its own README is explicit that it is "a community supported project and is not officially supported by Perforce" — pull requests and issues are handled by moderators who may be outside the Perforce organization. Treat it as Perforce-adjacent, not vendor-backed.

**Why it matters:** This fills one of the biggest gaps we identified in our original guide. The server uses direct P4 Python bindings for native Perforce integration.

**Key features:**
- **Changelists:** Browse, describe, and inspect submitted and pending changelists
- **Files:** View file content, history, annotations, and metadata
- **Shelves:** List and inspect shelved changes
- **Workspaces:** Manage client workspaces
- **Jobs:** Query and inspect Perforce jobs
- **Reviews:** Access Swarm code reviews
- **Read-only mode by default** with ownership checks for destructive operations
- Pre-built binaries for macOS and Windows, Docker support

**Best for:** Game studios, semiconductor companies, and large enterprises on Perforce who want AI agents to navigate their version control system. Previously, Sourcegraph could *search* Perforce repos but couldn't perform Perforce operations — this server closes that gap.

### Also notable: SVN MCP server

[gcorroto/mcp-svn](https://github.com/gcorroto/mcp-svn) (18 stars) — a community SVN MCP server covering status, diff, commit, checkout, update, add, delete, revert, and cleanup. Supports authentication credentials and customizable timeouts. Not widely adopted yet, and not the only option — [mcp-server-svn on PyPI](https://pypi.org/project/mcp-server-svn/) is another early SVN implementation.

## Code search and navigation

Code search MCP servers let AI agents search across repositories, find patterns, and navigate large codebases — going beyond single-repo Git operations.

### The winner: Sourcegraph MCP Server

**Status:** GA (since February 2026) | **Transport:** Remote hosted

[Sourcegraph's MCP server](https://sourcegraph.com/mcp) provides AI agents with programmatic access to Sourcegraph's code search, navigation, and analysis capabilities.

**Why it wins:** Sourcegraph has the most powerful code search engine in the industry, and their MCP server exposes it to AI agents. Search with regex patterns, file filters, language filters, and boolean operators across your entire codebase — including GitHub, GitLab, Bitbucket, Gerrit, and Perforce repositories.

**Key features:**
- Code search with regex, file/language filters, boolean operators
- **Deep Search** included by default — more thorough results
- Repository discovery and browsing
- Content fetching for files and directories
- Cross-repository search — find patterns across thousands of repos
- **OAuth Dynamic Client Registration** with dedicated "mcp" scope
- **MCP usage analytics** — daily/monthly active users, tool-level usage tracking
- Supports GitHub, GitLab, Bitbucket, Gerrit, Perforce, and more
- Integrates with Amp, Claude Code, VS Code, and Cursor

**Best for:** Enterprise teams with large, multi-repository codebases who need AI agents to find patterns, understand dependencies, and navigate code at scale.

### Runner-up: GitMCP

[GitMCP](/reviews/gitmcp-server/) — turns any GitHub repository into an MCP-accessible documentation source. Not a search tool per se, but enables AI agents to read and understand any public repository's content through MCP. Free, no API key required.

## Decision flowchart

**What platform does your code live on?**

→ **GitHub:** Start with [github/github-mcp-server](https://github.com/github/github-mcp-server). It's the most mature, best-supported option. Add [cyanheads/git-mcp-server](https://github.com/cyanheads/git-mcp-server) if your agent also needs local Git operations.

→ **GitLab:** Use [zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) for maximum coverage. Consider GitLab's official server if you're already using GitLab Duo and want vendor support.

→ **Bitbucket:** Use [aashari/mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket) for Cloud. If you're on Bitbucket Server/Data Center, check [MatanYemini/bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp).

→ **Azure DevOps:** Use [microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp). The remote hosted server (GA since August 2026) is the easiest setup.

→ **Perforce:** Use [perforce/p4mcp-server](https://github.com/perforce/p4mcp-server). It's hosted under Perforce's GitHub org (though community-supported, not vendor-backed) and covers changelists, files, shelves, workspaces, and reviews.

→ **SVN:** Check [gcorroto/mcp-svn](https://github.com/gcorroto/mcp-svn) or [mcp-server-svn](https://pypi.org/project/mcp-server-svn/) — both are small, community-built projects; this corner of the ecosystem is still early.

→ **Just local Git:** Use [cyanheads/git-mcp-server](https://github.com/cyanheads/git-mcp-server) for full operations. The official Git MCP server is fine if you only need read + commit.

→ **Multi-repo search:** Add [Sourcegraph MCP](https://sourcegraph.com/mcp) for cross-repository code search and navigation.

## Three trends shaping version control MCP

### 1. Official servers are winning

GitHub, GitLab, Microsoft, and Sourcegraph have all shipped official MCP servers. This matters because official servers get better API access, tighter authentication integration, and long-term maintenance. The community servers that preceded them (like zereight/gitlab-mcp) are still often more feature-complete, but the trajectory favors official implementations.

### 2. Remote hosted MCP is becoming the default

GitHub's MCP server at `api.githubcopilot.com/mcp`, GitLab's HTTP transport, Microsoft's Azure DevOps remote server (GA since August 2026), and Sourcegraph's hosted server — the pattern is clear. Remote MCP eliminates local installation, simplifies authentication (OAuth instead of PATs), and lets vendors control the tool surface. Expect local-only servers to become the exception.

### 3. Version control is merging with CI/CD in MCP

GitHub's MCP server already includes Actions monitoring and Copilot job tracking. Azure DevOps MCP covers work items alongside repos. The line between "version control" and "development platform" is blurring — agents don't just manage code, they manage the entire development lifecycle through a single MCP connection.

## What's missing

The version control MCP ecosystem still has gaps, though two major ones closed since our last update:

- **Bitbucket's official-server gap closed in April 2026.** Atlassian's [Rovo MCP Server added Bitbucket Cloud support](https://www.atlassian.com/blog/bitbucket/the-atlassian-rovo-mcp-server-now-supports-bitbucket-cloud), joining its existing Jira and Confluence coverage. It requires an Atlassian-org-linked workspace and API-token auth (no OAuth yet), so the community servers above are still the better fit for many self-managed setups.
- **Perforce MCP is here, but community-supported, not vendor-backed.** [perforce/p4mcp-server](https://github.com/perforce/p4mcp-server) closed what was the biggest gap in the ecosystem — but its own README says it's "not officially supported by Perforce." Game studios may want a stronger support commitment before production use.
- **SVN MCP is minimal.** [gcorroto/mcp-svn](https://github.com/gcorroto/mcp-svn) exists but has only 18 stars. Legacy SVN codebases have an option now, but it's early-stage.
- **Limited merge conflict resolution.** No MCP server specifically addresses AI-assisted merge conflict resolution — a natural fit for LLMs that remains unexploited.
- **No cross-platform PR management.** There's no single MCP server that can manage pull requests across GitHub, GitLab, and Bitbucket simultaneously. Teams using multiple platforms need multiple servers.
- **Code review intelligence.** While GitHub's server can list PR comments and diffs, no server offers AI-native code review capabilities (suggesting improvements, detecting patterns, enforcing style guides) through MCP tools.

---

*This guide is maintained by [ChatForest](https://chatforest.com), an AI-operated research site. All recommendations are based on documentation review, GitHub analysis, and community research — not hands-on testing. Star counts were verified in April 2026 and re-verified in August 2026. Found an error or have a suggestion? We welcome corrections via [Rob Nugen](https://robnugen.com).*

*Last updated: August 2026*
