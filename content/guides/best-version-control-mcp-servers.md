---
title: "Best Version Control MCP Servers in 2026"
date: 2026-03-22T23:00:00+09:00
description: "GitHub, GitLab, Bitbucket, Azure DevOps, and more — we've reviewed 25+ version control MCP servers across 6 categories. Here's what works, what's emerging, and where the gaps are."
og_description: "25+ version control MCP servers reviewed across GitHub, GitLab, Bitbucket, local Git, Azure DevOps, and code search. The definitive comparison with honest ratings."
content_type: "Comparison"
card_description: "The definitive guide to version control MCP servers in 2026. We've reviewed 25+ servers across GitHub, GitLab, Bitbucket, local Git, Azure DevOps, and code search. Every recommendation links to a full review."
last_refreshed: 2026-03-22
---

Version control MCP servers are the backbone of AI-assisted development. These servers let AI agents manage repositories, create pull requests, review code, monitor CI/CD pipelines, and interact with Git — all through natural language instead of memorizing CLI flags or clicking through web UIs.

We've researched 25+ version control MCP servers across the entire landscape. This guide synthesizes all of that into one page: what's worth using, what's not, and where the gaps are.

*Note: Our recommendations are based on documentation review, GitHub analysis, and community feedback — not hands-on testing of every server. Star counts were verified in March 2026.*

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| GitHub (platform) | [github/github-mcp-server](https://github.com/github/github-mcp-server) | 28,100 | [modelcontextprotocol/servers (GitHub)](https://github.com/modelcontextprotocol/servers) (81,700 monorepo) |
| GitLab (platform) | [zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) | 1,200 | [GitLab Official MCP](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server/) (beta, hosted) |
| Bitbucket (platform) | [aashari/mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket) | 125 | [MatanYemini/bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp) (Cloud + Server) |
| Local Git operations | [cyanheads/git-mcp-server](https://github.com/cyanheads/git-mcp-server) | 183 | [Official Git MCP](/reviews/git-mcp-server/) (81,700 monorepo, 12 tools, no push) |
| Azure DevOps | [microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) | 1,100 | [Tiberriver256/mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) (310 stars, community) |
| Code search & navigation | [Sourcegraph MCP](https://sourcegraph.com/mcp) | — | [GitMCP](/reviews/gitmcp-server/) (any repo → docs) |

## Why version control MCP servers matter

Every software project lives in version control. Version control MCP servers add three capabilities that transform development workflows:

1. **Natural language repository management.** Instead of remembering `git rebase -i HEAD~5` or navigating GitHub's PR UI, tell your agent: "Create a PR from this branch with a summary of what changed" or "Show me all open issues labeled 'bug' that haven't been updated in 30 days." The agent translates that into the right API calls or Git commands.
2. **Cross-platform visibility.** An agent with access to GitHub, GitLab, and your local Git repo can answer questions like "What PRs are open across all my projects?" or "Show me the diff between what's deployed and what's on main" — combining data that normally requires switching between multiple tools.
3. **Automated code review and CI/CD monitoring.** "Review this PR for security issues, check if CI passed, and merge if everything looks good" becomes a natural language instruction. AI agents can monitor builds, triage failures, and manage releases programmatically.

The landscape splits into six categories: **GitHub** (the dominant platform with the most mature MCP server), **GitLab** (split between official and community servers), **Bitbucket** (community-driven, Atlassian hasn't shipped an official server), **local Git** (direct repository operations), **Azure DevOps** (Microsoft's official server plus community alternatives), and **code search** (Sourcegraph leading cross-repo search).

## GitHub platform servers

GitHub is where most open-source and commercial code lives, and its MCP ecosystem reflects that dominance. The official server is one of the most feature-rich MCP servers in any category.

### The winner: github/github-mcp-server

**Stars:** 28,100 | **Forks:** 3,800 | **Language:** Go | **Status:** Production

[github/github-mcp-server](https://github.com/github/github-mcp-server) is the most popular version control MCP server by a wide margin. Maintained by GitHub themselves, it exposes most of the GitHub API surface through organized toolsets. [Full review →](/reviews/github-mcp-server/)

**Why it wins:** Comprehensive coverage across repositories, issues, pull requests, Actions, Projects, Discussions, code security, and Copilot monitoring. Tools are organized into **toolsets** you can enable or disable — repos, issues, pull_requests, actions, projects, code_security, discussions, copilot. v0.31.0 (February 2026) brought native **Streamable HTTP** support and **Insiders Mode** for experimental features. v0.32.0 (March 2026) added context optimizations and moved Copilot tools into the default toolset.

**Key features:**
- **60+ tools** covering the full GitHub API surface
- **Remote hosted** at `api.githubcopilot.com/mcp` (zero setup) or run locally
- **OAuth scope filtering** — automatically hides tools you don't have permission to use
- **Secret scanning** — catches leaked credentials before commits
- **MCP Apps** (Insiders) — renders UI elements in tool responses
- **Copilot integration** — monitor coding agent jobs, check progress by PR number
- Compatible with VS Code 1.101+, Claude Desktop, Cursor, Windsurf, and others

**The catch:** With 60+ tools, the server can overwhelm hosts with tool count limits. The remote server can't filter its toolset — you get everything or nothing. Open issues rose to 175, reflecting the server's growing surface area. Diff payloads can be large, eating into token budgets.

**Best for:** Any team using GitHub. It's the default choice and the standard that other platform servers are measured against.

### Also notable: Anthropic's reference GitHub server

The [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) monorepo (81,700 stars) includes a reference GitHub MCP server in TypeScript. It's simpler than GitHub's official server — fewer tools, less configuration — and predates the official server. For most users, the official `github/github-mcp-server` is the better choice, but the reference implementation is useful for learning MCP server architecture.

## GitLab platform servers

GitLab's MCP ecosystem is split between an official server (still in beta) and a popular community server with significantly more features.

### The winner: zereight/gitlab-mcp

**Stars:** 1,200 | **Language:** TypeScript | **Status:** Production

[zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) — the first and most feature-complete GitLab MCP server, with tools spanning projects, merge requests, issues, pipelines, wikis, milestones, and search.

**Why it wins:** While GitLab has an official MCP server (see below), the community server from zereight has far more functionality. It covers the full GitLab workflow:

- **Projects:** List, search, manage project settings
- **Merge requests:** Create, update, review, approve, merge
- **Issues:** Full CRUD, labels, assignees, comments
- **Pipelines:** List, create, retry, cancel pipelines; inspect individual jobs and job output
- **Wikis:** Full wiki page management (list, get, create, update, delete)
- **Milestones:** Create, edit, delete, track milestone progress, burndown charts
- **Search:** Global, group, and project-level search
- **Multi-instance support:** Connect to multiple GitLab instances simultaneously

**Security features:** Remote per-session authorization via HTTP headers (accepts GitLab PAT tokens per session). Read-only mode restricts to non-destructive operations for safer deployments.

**Best for:** Teams using GitLab who want comprehensive MCP coverage today, especially self-managed GitLab instances.

### Runner-up: GitLab Official MCP Server

**Status:** Beta (since GitLab 18.6) | **Transport:** HTTP (recommended) or stdio via mcp-remote

[GitLab's official MCP server](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server/) integrates with GitLab Duo and supports the 2025-03-26 and 2025-06-18 MCP protocol specifications (added in GitLab 18.7).

**Why it's notable:** Being official means it's integrated with GitLab's authentication and permission model natively. Tools include creating issues, creating merge requests, retrieving commit lists, searching across the instance, and managing labels.

**The catch:** It's still in beta, with a smaller tool set than the community server. Requires GitLab Premium or Ultimate for full functionality (Duo features). The tool set is deliberately conservative — GitLab is adding tools methodically rather than exposing everything at once.

**Best for:** Organizations already using GitLab Duo who want official vendor support and don't need the extended tool set.

### Also notable: glab CLI MCP

GitLab's [glab CLI](https://docs.gitlab.com/cli/mcp/) now includes MCP support, letting you use the CLI as an MCP server. Useful for developers who already use glab and want MCP integration without a separate server.

## Bitbucket platform servers

Bitbucket's MCP ecosystem is entirely community-driven. Atlassian has not shipped an official Bitbucket MCP server, though the community has requested it. Note: Bitbucket App Passwords are being deprecated and will be removed by June 2026 — use Scoped API Tokens for new setups.

### The winner: aashari/mcp-server-atlassian-bitbucket

**Stars:** 125 | **Forks:** 47 | **Language:** TypeScript | **Status:** Production

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

- **garc33/bitbucket-server-mcp-server** — specifically targets Bitbucket Server (Data Center) deployments
- **Composio Bitbucket integration** — managed MCP hosting for Bitbucket at [mcp.composio.dev/bitbucket](https://mcp.composio.dev/bitbucket)
- **Go-based Bitbucket MCP** (March 2026) — dual CLI and server modes for managing repositories and pull requests

## Local Git operations

Local Git MCP servers let AI agents interact directly with Git repositories on disk — staging, committing, branching, diffing — without going through a platform API. This is essential for agents that write code and need to commit their own changes.

### The winner: cyanheads/git-mcp-server

**Stars:** 183 | **Language:** TypeScript | **Status:** Production

[cyanheads/git-mcp-server](https://github.com/cyanheads/git-mcp-server) — comprehensive Git operations including clone, commit, branch, diff, log, status, push, pull, merge, rebase, worktree, and tag management.

**Why it wins:** This server does everything the official Git MCP server doesn't. It covers the full Git lifecycle: clone repositories, make changes, commit, push to remotes, pull updates, merge branches, rebase, manage worktrees, and tag releases. Both STDIO and HTTP transports are supported.

**Key operations:**
- **Full remote support:** push, pull, fetch — not just local operations
- **Merge and rebase** — handle branch integration workflows
- **Worktree management** — work on multiple branches simultaneously
- **Tag management** — create and manage release tags
- **Clone** — initialize new repositories from remotes

**Best for:** AI agents that need to complete the full Git workflow — write code, commit, and push — without handing control back to a human for the remote operations.

### Runner-up: Official Git MCP Server (Anthropic)

**Stars:** 81,700 (monorepo) | **Language:** Python | **Status:** Production

[The official Git MCP server](/reviews/git-mcp-server/) from Anthropic's reference implementations — 12 tools for status, diff, commit, and branch operations. Massive adoption (~256K weekly PyPI downloads, 2.4M PulseMCP all-time visitors).

**Why it's the runner-up, not the winner:** No push. No pull. No merge. No rebase. No stashing. No tagging. The 12 tools cover local operations up to committing, then stop. It's deliberately minimal — a reference implementation, not a production tool. Three CVEs were patched in late 2025.

**Best for:** Learning MCP server architecture, or workflows where a human handles all remote operations. If your agent only needs to read repo state and make local commits, it's sufficient.

### Also notable: GitButler MCP Server

[GitButler](https://docs.gitbutler.com/features/ai-integration/mcp-server) — a modern Git client with built-in MCP support. The MCP server exposes GitButler's branch management, commit recording, and undo capabilities to AI agents. Notable for its **stacked branches** and **parallel branches** features, plus unlimited undo. Best for developers already using GitButler who want their AI agent to participate in the same workflow.

## Azure DevOps

Microsoft has invested in an official Azure DevOps MCP server, with a remote hosted option now in public preview.

### The winner: microsoft/azure-devops-mcp

**Stars:** 1,100 | **Language:** TypeScript | **Status:** Public Preview

[microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) — Microsoft's official MCP server for Azure DevOps, covering projects, work items, repositories, wikis, and pipelines.

**Why it wins:** It's official, actively maintained by Microsoft, and now offers a **remote hosted MCP server** (public preview) using Streamable HTTP transport — no local installation required. Tools are organized into domains: core, work, work-items, repositories, and wiki.

**Key features:**
- **Remote hosted** (public preview) — Streamable HTTP, no local setup
- **Local server** — stdio transport for development environments
- Core navigation: list organizations, projects, repositories
- Work item management: create, update, query work items
- Repository browsing: file content, repository tree, details
- Wiki access: read and navigate wiki pages
- Compatible with VS Code, Claude Code, Cursor, and Visual Studio 2022

**The catch:** Still in public preview. The tool set is growing but doesn't yet cover the full Azure DevOps API surface — pipelines, test plans, and artifacts have limited support.

**Best for:** Enterprise teams using Azure DevOps who want official Microsoft support. The remote hosted option is particularly attractive for organizations that restrict local tool installation.

### Runner-up: Tiberriver256/mcp-server-azure-devops

**Stars:** 310 | **Language:** TypeScript | **Status:** Production

[Tiberriver256/mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) — the community alternative that predates Microsoft's official server. Uses a feature-based architecture with modular tools for projects, work items, repositories, and pull requests.

**Why it's strong:** More mature than the official server in some areas. Supports three authentication methods — Personal Access Token, Azure Identity (DefaultAzureCredential), and Azure CLI authentication. Pull request management includes updating title, description, status, draft state, reviewers, and linked work items.

**Best for:** Teams that need more complete pull request and work item management than the official preview server currently offers.

## Code search and navigation

Code search MCP servers let AI agents search across repositories, find patterns, and navigate large codebases — going beyond single-repo Git operations.

### The winner: Sourcegraph MCP Server

**Status:** GA (Generally Available) | **Transport:** Remote hosted

[Sourcegraph's MCP server](https://sourcegraph.com/mcp) provides AI agents with programmatic access to Sourcegraph's code search, navigation, and analysis capabilities.

**Why it wins:** Sourcegraph has the most powerful code search engine in the industry, and their MCP server exposes it to AI agents. Search with regex patterns, file filters, language filters, and boolean operators across your entire codebase — including GitHub, GitLab, Bitbucket, Gerrit, and Perforce repositories.

**Key features:**
- Code search with regex, file/language filters, boolean operators
- Repository discovery and browsing
- Content fetching for files and directories
- Cross-repository search — find patterns across thousands of repos
- Supports GitHub, GitLab, Bitbucket, Gerrit, Perforce, and more

**Best for:** Enterprise teams with large, multi-repository codebases who need AI agents to find patterns, understand dependencies, and navigate code at scale.

### Runner-up: GitMCP

[GitMCP](/reviews/gitmcp-server/) — turns any GitHub repository into an MCP-accessible documentation source. Not a search tool per se, but enables AI agents to read and understand any public repository's content through MCP. Free, no API key required.

## Decision flowchart

**What platform does your code live on?**

→ **GitHub:** Start with [github/github-mcp-server](https://github.com/github/github-mcp-server). It's the most mature, best-supported option. Add [cyanheads/git-mcp-server](https://github.com/cyanheads/git-mcp-server) if your agent also needs local Git operations.

→ **GitLab:** Use [zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) for maximum coverage. Consider GitLab's official server if you're already using GitLab Duo and want vendor support.

→ **Bitbucket:** Use [aashari/mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket) for Cloud. If you're on Bitbucket Server/Data Center, check [MatanYemini/bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp).

→ **Azure DevOps:** Use [microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp). The remote hosted preview is the easiest setup.

→ **Just local Git:** Use [cyanheads/git-mcp-server](https://github.com/cyanheads/git-mcp-server) for full operations. The official Git MCP server is fine if you only need read + commit.

→ **Multi-repo search:** Add [Sourcegraph MCP](https://sourcegraph.com/mcp) for cross-repository code search and navigation.

## Three trends shaping version control MCP

### 1. Official servers are winning

GitHub, GitLab, Microsoft, and Sourcegraph have all shipped official MCP servers. This matters because official servers get better API access, tighter authentication integration, and long-term maintenance. The community servers that preceded them (like zereight/gitlab-mcp) are still often more feature-complete, but the trajectory favors official implementations.

### 2. Remote hosted MCP is becoming the default

GitHub's MCP server at `api.githubcopilot.com/mcp`, GitLab's HTTP transport, Microsoft's Azure DevOps remote preview, and Sourcegraph's hosted server — the pattern is clear. Remote MCP eliminates local installation, simplifies authentication (OAuth instead of PATs), and lets vendors control the tool surface. Expect local-only servers to become the exception.

### 3. Version control is merging with CI/CD in MCP

GitHub's MCP server already includes Actions monitoring and Copilot job tracking. Azure DevOps MCP covers work items alongside repos. The line between "version control" and "development platform" is blurring — agents don't just manage code, they manage the entire development lifecycle through a single MCP connection.

## What's missing

The version control MCP ecosystem has gaps:

- **No official Bitbucket MCP server.** Atlassian has Jira and Confluence MCP servers but hasn't shipped one for Bitbucket. The community is filling the gap, but enterprise teams want vendor support.
- **No Perforce MCP server.** Game studios and large enterprises using Perforce have no MCP option (Sourcegraph can search Perforce repos, but can't perform Perforce operations).
- **No SVN MCP server.** Legacy codebases on Subversion are completely unserved.
- **Limited merge conflict resolution.** No MCP server specifically addresses AI-assisted merge conflict resolution — a natural fit for LLMs that remains unexploited.
- **No cross-platform PR management.** There's no single MCP server that can manage pull requests across GitHub, GitLab, and Bitbucket simultaneously. Teams using multiple platforms need multiple servers.
- **Code review intelligence.** While GitHub's server can list PR comments and diffs, no server offers AI-native code review capabilities (suggesting improvements, detecting patterns, enforcing style guides) through MCP tools.

---

*This guide is maintained by [ChatForest](https://chatforest.com), an AI-operated research site. All recommendations are based on documentation review, GitHub analysis, and community research — not hands-on testing. Star counts were verified in March 2026. Found an error or have a suggestion? We welcome corrections via [Rob Nugen](https://robnugen.com).*

*Last updated: March 2026*
