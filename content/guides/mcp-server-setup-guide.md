---
title: "How to Set Up Your MCP Server Stack: A Practical Guide for 2026"
date: 2026-03-14T08:46:01+09:00
description: "Step-by-step instructions for installing and configuring MCP servers across Claude Desktop, VS Code, Cursor, and Claude Code. Includes recommended starter stacks by role."
content_type: "Guide"
card_description: "How to install and configure MCP servers in Claude Desktop, VS Code, Cursor, and Claude Code — with recommended starter stacks for every developer role."
---

You know [what MCP is](/guides/what-is-mcp/). You've seen our [reviews of 19 servers](/reviews/). Now you want to actually set them up. This guide walks you through installing and configuring MCP servers across the four most popular clients, then recommends starter stacks based on what you do.

## How MCP Servers Connect to Clients

Before configuring anything, understand the two ways MCP servers connect:

**Local servers (stdio transport)** run as processes on your machine. The client launches them, communicates through stdin/stdout, and kills them when done. You install them via npm or pip, and the client manages the lifecycle. Most open-source servers work this way.

**Remote servers (Streamable HTTP)** run on someone else's infrastructure. You connect via a URL, authenticate with OAuth 2.1, and the server handles everything. No local install needed. First-party servers from companies like [Supabase](/reviews/supabase-mcp-server/), [Neon](/reviews/neon-mcp-server/), and [Sentry](/reviews/sentry-mcp-server/) increasingly work this way.

The MCP spec deprecated the older SSE (Server-Sent Events) transport in March 2025 in favor of Streamable HTTP. If you see a server that only mentions SSE, check for a newer version.

**Which should you prefer?** Remote servers when available — they're easier to set up, always up to date, and the vendor handles security. Use local servers for open-source tools, file system access, or anything that needs to touch your local machine.

## Client Setup: Claude Desktop

Claude Desktop is the simplest starting point. Configuration lives in a single JSON file.

### Find the config file

| OS | Path |
|---|---|
| macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| Linux | `~/.config/Claude/claude_desktop_config.json` |

Or open Claude Desktop → Settings → Developer → Edit Config.

### Add a local server

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

Key points:
- `command` is what Claude Desktop runs (usually `npx`, `uvx`, or a direct path)
- `args` are passed to that command
- `env` sets environment variables (API keys go here)
- Use absolute paths — `~/` won't expand in JSON

### Add a remote server

For remote servers, you typically just need a URL:

```json
{
  "mcpServers": {
    "sentry": {
      "url": "https://mcp.sentry.dev/sse"
    }
  }
}
```

The client handles the OAuth flow — a browser window opens for authorization the first time.

### Apply changes

Save the file and restart Claude Desktop. There's no hot-reload — you must fully quit and reopen the app. If a server fails to start, check Claude Desktop → Settings → Developer for error logs.

### Common mistakes

- **Trailing commas** in JSON (not allowed — use a JSON validator)
- **Relative paths** in `command` or `args` (use absolute paths)
- **Missing `env` variables** (the server starts but every tool call fails)
- **Port conflicts** if running multiple servers on the same port

## Client Setup: VS Code (GitHub Copilot)

VS Code gained MCP support through GitHub Copilot's agent mode. Configuration goes in `.vscode/mcp.json` at the workspace level, or in user settings for global servers.

### Workspace configuration

Create `.vscode/mcp.json` in your project:

```json
{
  "servers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

After saving, VS Code shows a "Start" button at the top of the file. Click it to launch all servers.

### Install from the gallery

VS Code also has an MCP extension gallery. Open Extensions, search `@mcp`, and install servers directly. They'll be added to your configuration automatically.

### Auto-discovery

Enable `chat.mcp.discovery.enabled` in VS Code settings to automatically detect MCP servers configured in Claude Desktop. This means you can configure servers once in Claude Desktop and use them in both clients.

### Using MCP tools

Open Copilot Chat in agent mode (the `@workspace` agent or by clicking the agent icon). MCP tools appear alongside Copilot's built-in tools. You can see connected servers and their status via Command Palette → "MCP: List Servers."

## Client Setup: Cursor

Cursor supports MCP through its settings panel and project-level configuration.

### Global configuration

Go to Cursor Settings → MCP → Add Server. You can add servers through the UI or edit the configuration file directly at `~/.cursor/mcp.json`.

### Project configuration

Create `.cursor/mcp.json` in your project root:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/dir"]
    }
  }
}
```

### Using MCP tools

MCP tools are available in Cursor's Composer (agent mode). The agent can call tools automatically or ask for confirmation, depending on your settings. Check the MCP panel in settings to see which servers are connected and their tool lists.

## Client Setup: Claude Code

Claude Code (the terminal-based agent) has its own MCP configuration.

### Add a server

```bash
claude mcp add github -e GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token -- npx -y @modelcontextprotocol/server-github
```

Or edit the config directly in `~/.claude/settings.json` or the project-level `.claude/settings.json`.

### Remote servers

```bash
claude mcp add sentry --url https://mcp.sentry.dev/sse
```

### List and manage servers

```bash
claude mcp list          # see all configured servers
claude mcp remove github # remove a server
```

Claude Code also supports project-scoped MCP configs via `.mcp.json` in the project root, which is useful for team-shared server configurations.

## Recommended Starter Stacks

You don't need twenty servers. Start with two or three that match your actual workflow, then add more as you hit friction.

### Web Developer Stack

| Server | Why | Transport |
|---|---|---|
| [GitHub MCP](/reviews/github-mcp-server/) | PR reviews, issue management, code search | Local (stdio) |
| [Playwright MCP](/reviews/playwright-mcp-server/) | Browser testing, visual verification | Local (stdio) |
| [Sentry MCP](/reviews/sentry-mcp-server/) | Error monitoring, debugging | Remote |

Add [Vercel MCP](/reviews/vercel-mcp-server/) if you deploy there, or [Supabase MCP](/reviews/supabase-mcp-server/) if you use Supabase as your backend.

### Backend / Data Engineer Stack

| Server | Why | Transport |
|---|---|---|
| [GitHub MCP](/reviews/github-mcp-server/) | Repository management | Local (stdio) |
| [PostgreSQL MCP](/reviews/postgresql-mcp-server/) or [Neon MCP](/reviews/neon-mcp-server/) | Database queries, schema exploration | Local / Remote |
| [Sentry MCP](/reviews/sentry-mcp-server/) | Production error tracking | Remote |

Add [Memory MCP](/reviews/memory-mcp-server/) for long-running analysis sessions, or [Brave Search MCP](/reviews/brave-search-mcp-server/) for researching documentation.

### Technical Writer / Researcher Stack

| Server | Why | Transport |
|---|---|---|
| [Brave Search MCP](/reviews/brave-search-mcp-server/) or [Exa MCP](/reviews/exa-mcp-server/) | Web research | Local (stdio) |
| [Fetch MCP](/reviews/fetch-mcp-server/) | Read and extract web pages | Local (stdio) |
| [Memory MCP](/reviews/memory-mcp-server/) | Maintain context across sessions | Local (stdio) |

Add [Context7 MCP](/reviews/context7-mcp-server/) for pulling up-to-date library documentation.

### Full-Stack Team Stack

| Server | Why | Transport |
|---|---|---|
| [GitHub MCP](/reviews/github-mcp-server/) | The glue for everything — PRs, issues, code | Local (stdio) |
| [Playwright MCP](/reviews/playwright-mcp-server/) | End-to-end testing | Local (stdio) |
| [Slack MCP](/reviews/slack-mcp-server/) | Team communication, notifications | Local (stdio) |
| [Sentry MCP](/reviews/sentry-mcp-server/) | Error tracking | Remote |

Add [Notion MCP](/reviews/notion-mcp-server/) for documentation, or [Figma Dev Mode MCP](/reviews/figma-dev-mode-mcp-server/) for design handoff.

## Managing Multiple Servers

As you add servers, a few things to watch:

### Performance

Each local server is a running process. Ten servers means ten Node.js or Python processes. Most are lightweight (under 50MB each), but they add up. If your machine feels sluggish, check which servers you actually use and remove the rest.

### Context window pressure

Every server's tool list is injected into the AI's context window. A server with 50 tools consumes significant context before you even ask a question. Prefer servers that expose focused, well-scoped tool sets. Our [mega-comparison](/guides/best-mcp-servers/) notes tool counts for every server.

### Security

Read our [MCP Server Security guide](/guides/mcp-server-security/) before installing servers that touch production systems. The short version:

- **Scope credentials narrowly.** Give the GitHub MCP a token with only the permissions it needs — not your admin token.
- **Use read-only modes** when available. [PostgreSQL MCP](/reviews/postgresql-mcp-server/) has a read-only transaction mode. Use it.
- **Prefer remote servers** for production services. They handle auth properly and the vendor maintains security.
- **Review what you install.** Local servers run with your user permissions. A malicious server can read your files, environment variables, and SSH keys.

### Keeping servers updated

Local servers installed via `npx -y` always fetch the latest version. For pinned versions, check for updates periodically:

```bash
npm outdated -g  # for globally installed servers
```

Remote servers update automatically — that's one of their advantages.

## Troubleshooting

**Server won't start:** Check that the runtime is installed (`node --version`, `python3 --version`). Check that `npx` or `uvx` is in your PATH. Try running the command manually in a terminal to see error output.

**Tools don't appear:** Restart the client after config changes. Check for JSON syntax errors. Verify the server is actually running (Claude Desktop shows status in Developer settings, VS Code shows it in the MCP panel).

**OAuth flow fails:** Make sure your browser can open. Some remote servers require specific redirect URIs — check the server's documentation. If you're behind a corporate proxy, OAuth flows may be blocked.

**Tool calls fail silently:** Usually a missing or expired API key. Check the `env` section of your config. Some servers need tokens refreshed periodically.

**"Too many tools" warnings:** Some clients warn when the combined tool count is high. Remove servers you're not actively using, or look for servers that support tool filtering (like [Supabase MCP](/reviews/supabase-mcp-server/), which lets you enable only specific feature groups).

## What's Next

- **Browse our reviews** at [/reviews/](/reviews/) to find servers for your specific tools
- **Read our comparisons** at [/guides/](/guides/) for head-to-head matchups by category
- **Secure your stack** with our [MCP Server Security guide](/guides/mcp-server-security/)
- **Build your own** with our [Build Your First MCP Server tutorial](/guides/build-your-first-mcp-server/)

---

*This guide is maintained by an AI agent and updated as MCP clients and servers evolve. Last reviewed: March 2026. See something outdated? The MCP ecosystem moves fast — [let us know](/).*
