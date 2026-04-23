# How to Set Up Your MCP Server Stack: A Practical Guide for 2026

> Step-by-step instructions for installing and configuring MCP servers across Claude Desktop, VS Code, Cursor, Claude Code, and more. Includes recommended starter stacks by role.


You know [what MCP is](/guides/what-is-mcp/). You've seen our [reviews of 300+ servers](/reviews/). Now you want to actually set them up. This guide walks you through installing and configuring MCP servers across seven major clients, then recommends starter stacks based on what you do.

## How MCP Servers Connect to Clients

Before configuring anything, understand the two ways MCP servers connect:

**Local servers (stdio transport)** run as processes on your machine. The client launches them, communicates through stdin/stdout, and kills them when done. You install them via npm or pip, and the client manages the lifecycle. Most open-source servers work this way.

**Remote servers (Streamable HTTP)** run on someone else's infrastructure. You connect via a URL, authenticate with OAuth 2.1, and the server handles everything. No local install needed. First-party servers from companies like [Supabase](/reviews/supabase-mcp-server/), [Neon](/reviews/neon-mcp-server/), [Sentry](/reviews/sentry-mcp-server/), [Stripe](/reviews/stripe-mcp-server/), [Asana](https://mcp.asana.com), [ClickUp](https://mcp.clickup.com/mcp), and [Google Workspace](https://developers.google.com/workspace/guides/configure-mcp-servers) work this way. As of April 2026, remote is the default for vendor-operated servers.

The MCP spec deprecated the older SSE (Server-Sent Events) transport in March 2025 in favor of Streamable HTTP. SSE shutdown deadlines are now arriving — Atlassian's SSE endpoint dies June 30, 2026, and Asana V1 (SSE) shuts down May 11, 2026. If you see a server that only mentions SSE, check for a newer version immediately.

**Which should you prefer?** Remote servers when available — they're easier to set up, always up to date, and the vendor handles security and auth. Use local servers for open-source tools, file system access, or anything that needs to touch your local machine.

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
    },
    "stripe": {
      "url": "https://mcp.stripe.com"
    }
  }
}
```

The client handles the OAuth flow — a browser window opens for authorization the first time. You can also add remote servers via Settings → Connectors → Add Custom Connector without editing JSON.

### Install via Desktop Extensions

Claude Desktop now supports **Desktop Extensions** (`.dxt` files) — packaged MCP servers you can install with one click. Download a `.dxt` file, drag it into Settings → Extensions, and you're done. No JSON editing, no restart needed. The DXT format is becoming the preferred distribution method for Claude Desktop servers.

To create your own: `npm install -g @anthropic-ai/dxt`, then `dxt init` / `dxt pack`.

### Apply changes

Save the config file and restart Claude Desktop. There's no hot-reload for manual JSON changes — you must fully quit and reopen the app. (Desktop Extensions install without restart.) If a server fails to start, check Claude Desktop → Settings → Developer for error logs.

### Common mistakes

- **Trailing commas** in JSON (not allowed — use a JSON validator)
- **Relative paths** in `command` or `args` (use absolute paths)
- **Missing `env` variables** (the server starts but every tool call fails)
- **Port conflicts** if running multiple servers on the same port

## Client Setup: VS Code (GitHub Copilot)

As of VS Code 1.116, Copilot is built in — no extension install needed. MCP support comes out of the box. Configuration goes in `.vscode/mcp.json` at the workspace level, or in user settings for global servers.

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

VS Code has an MCP extension gallery. Open Extensions, search `@mcp`, and install servers directly. You can also browse servers via the Chat Customizations UI, which provides a unified interface for managing MCP servers, agents, and plugins.

### Auto-discovery

Enable `chat.mcp.discovery.enabled` in VS Code settings to automatically detect MCP servers configured in Claude Desktop. This means you can configure servers once in Claude Desktop and use them in both clients.

### MCP sandbox (macOS/Linux)

VS Code can run local MCP servers in a **restricted sandbox** that limits file and network access. This adds a layer of protection when testing unfamiliar servers.

### Enterprise governance

Admins can enforce **MCP server allowlists** through GitHub org policies, controlling which servers team members can install. MCP servers configured in VS Code also work in Copilot CLI and Claude agent sessions.

### Using MCP tools

Open Copilot Chat in agent mode (the `@workspace` agent or by clicking the agent icon). MCP tools appear alongside Copilot's built-in tools. You can see connected servers and their status via Command Palette → "MCP: List Servers."

## Client Setup: Cursor

Cursor supports MCP through its settings panel, project-level configuration, and a marketplace.

### Global configuration

Go to Cursor Settings → MCP → Add Server. You can add servers through the UI, browse the **MCP Marketplace** at cursor.com/marketplace for one-click installs, or edit the configuration file directly at `~/.cursor/mcp.json`.

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

### Dynamic context management

Cursor now uses dynamic context management that reduces token overhead by ~47% when running multiple MCP servers simultaneously. This makes running 5-6 servers practical without overwhelming the context window.

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
claude mcp add stripe --url https://mcp.stripe.com
```

### List and manage servers

```bash
claude mcp list          # see all configured servers
claude mcp get github    # see details for a specific server
claude mcp remove github # remove a server
```

Use `/mcp` in-session to check server status, enable/disable, or reconnect servers without restarting.

### MCP Tool Search (context optimization)

Claude Code uses **lazy tool loading** via MCP Tool Search — instead of injecting all tool descriptions into context upfront, it loads only the tools needed for each request. This reduces MCP token overhead by up to 85%, making it practical to configure many servers without context bloat.

### Organization controls

For teams, Claude Code supports `managed-mcp.json` for locked-down server sets and allowlist/denylist policies that control which MCP servers team members can use.

Claude Code also supports project-scoped MCP configs via `.mcp.json` in the project root, which is useful for team-shared server configurations.

## Client Setup: Windsurf

Windsurf (formerly Codeium) has native MCP integration with a built-in marketplace.

### Configuration

Edit `~/.codeium/windsurf/mcp_config.json`, or add servers through the built-in MCP Marketplace. Supports stdio, Streamable HTTP, and SSE transports.

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

**Limit:** 100 tools active at once. If you hit this, disable servers you're not actively using.

## Client Setup: ChatGPT

ChatGPT gained MCP support in beta. Setup: Settings → Connectors → Advanced → Developer Mode.

- **Business/Enterprise/Edu** plans get full read-write MCP access
- **Plus/Pro** plans are limited to read-only tools
- Requires HTTPS URLs — local stdio servers are not supported
- Supports SSE and Streamable HTTP + optional OAuth

This means ChatGPT only works with remote MCP servers, not local ones.

## Client Setup: JetBrains IDEs

JetBrains IDEs (IntelliJ, WebStorm, PhpStorm, etc.) added MCP support in the 2026.1 release.

### Configuration

Go to Settings → Tools → MCP Server. Add servers via the UI or JSON config. JetBrains can also auto-detect MCP configs from external clients (Claude Code, Cursor, VS Code) in the project.

## Recommended Starter Stacks

You don't need twenty servers. Start with two or three that match your actual workflow, then add more as you hit friction.

### Web Developer Stack

| Server | Why | Transport |
|---|---|---|
| [GitHub MCP](/reviews/github-mcp-server/) | PR reviews, issue management, code search (51 tools) | Local (stdio) |
| [Playwright MCP](/reviews/playwright-mcp-server/) | Browser testing, visual verification | Local (stdio) |
| [Sentry MCP](/reviews/sentry-mcp-server/) | Error monitoring, debugging | Remote |

Add [Vercel MCP](/reviews/vercel-mcp-server/) if you deploy there, or [Supabase MCP](/reviews/supabase-mcp-server/) if you use Supabase as your backend.

### Backend / Data Engineer Stack

| Server | Why | Transport |
|---|---|---|
| [GitHub MCP](/reviews/github-mcp-server/) | Repository management | Local (stdio) |
| [PostgreSQL MCP](/reviews/postgresql-mcp-server/) or [Neon MCP](/reviews/neon-mcp-server/) | Database queries, schema exploration | Local / Remote |
| [Sentry MCP](/reviews/sentry-mcp-server/) | Production error tracking | Remote |

Add [Memory MCP](/reviews/memory-mcp-server/) for long-running analysis sessions, or [Context7 MCP](/reviews/context7-mcp-server/) for pulling up-to-date library documentation (50K+ stars, 240K+ weekly npm downloads — the fastest-growing MCP server in 2026).

### Technical Writer / Researcher Stack

| Server | Why | Transport |
|---|---|---|
| [Brave Search MCP](/reviews/brave-search-mcp-server/) or [Exa MCP](/reviews/exa-mcp-server/) | Web research | Local (stdio) |
| [Fetch MCP](/reviews/fetch-mcp-server/) | Read and extract web pages | Local (stdio) |
| [Memory MCP](/reviews/memory-mcp-server/) | Maintain context across sessions | Local (stdio) |

Add [Context7 MCP](/reviews/context7-mcp-server/) for pulling up-to-date library documentation, or the [official MCP PDF server](/reviews/official-mcp-pdf-server/) for document extraction (779K+ npm downloads/month).

### Full-Stack Team Stack

| Server | Why | Transport |
|---|---|---|
| [GitHub MCP](/reviews/github-mcp-server/) | The glue for everything — PRs, issues, code | Local (stdio) |
| [Playwright MCP](/reviews/playwright-mcp-server/) | End-to-end testing | Local (stdio) |
| [Slack MCP](/reviews/slack-mcp-server/) | Team communication, notifications | Local (stdio) |
| [Sentry MCP](/reviews/sentry-mcp-server/) | Error tracking | Remote |

Add [Notion MCP](/reviews/notion-mcp-server/) for documentation, or [Figma Dev Mode MCP](/reviews/figma-dev-mode-mcp-server/) for design handoff.

### Google Workspace Stack (new)

| Server | Why | Transport |
|---|---|---|
| [Google Calendar MCP](https://calendarmcp.googleapis.com/mcp/v1) | Meeting management, scheduling | Remote (Google Official) |
| [Google Drive MCP](https://drivemcp.googleapis.com/mcp/v1) | File search and access | Remote (Google Official) |
| [Gmail MCP](https://gmailmcp.googleapis.com/mcp/v1) | Email management (10 tools) | Remote (Google Official) |

Google's official MCP servers launched in early 2026 for Calendar, Drive, Gmail, Chat, and People. Setup requires enabling MCP services in your Google Cloud project and configuring OAuth. Docs/Sheets/Slides are not yet available. For a community alternative with more features, see [nspady/google-calendar-mcp](/reviews/google-calendar-mcp-server/) (1,100+ stars, 13 tools).

## Managing Multiple Servers

As you add servers, a few things to watch:

### Performance

Each local server is a running process. Ten servers means ten Node.js or Python processes. Most are lightweight (under 50MB each), but they add up. If your machine feels sluggish, check which servers you actually use and remove the rest.

### Context window pressure

Every server's tool list is injected into the AI's context window. A server with 50 tools consumes significant context before you even ask a question. This is improving — Claude Code now uses **MCP Tool Search** to lazy-load only the tools needed per request (up to 85% token reduction), and Cursor's dynamic context management cuts overhead by ~47%. But most clients still load everything upfront.

**Mitigations:**
- Prefer servers that expose focused, well-scoped tool sets. Our [mega-comparison](/guides/best-mcp-servers/) notes tool counts for every server
- Use servers that support **toolset filtering** — [Supabase MCP](/reviews/supabase-mcp-server/), [Datadog MCP](/reviews/datadog-mcp-server/), and [GitHub MCP](/reviews/github-mcp-server/) (which auto-hides tools your OAuth token can't access) all support this
- Remove servers you're not actively using rather than keeping them all connected

### Security

Read our [MCP Server Security guide](/guides/mcp-server-security/) before installing servers that touch production systems. The short version:

- **Scope credentials narrowly.** Give the GitHub MCP a token with only the permissions it needs — not your admin token. GitHub's MCP server now auto-hides tools your token can't use.
- **Use read-only modes** when available. [PostgreSQL MCP](/reviews/postgresql-mcp-server/) has a read-only transaction mode. Use it.
- **Prefer remote servers** for production services. They handle auth via OAuth 2.1 with PKCE (now mandatory in the spec) and the vendor maintains security.
- **Review what you install.** Local servers run with your user permissions. A malicious server can read your files, environment variables, and SSH keys. VS Code's MCP sandbox (macOS/Linux) can help mitigate this.
- **Watch for CVEs.** The MCP ecosystem saw 30+ CVEs filed in early 2026. Notable: prompt injection attacks, SSRF vulnerabilities, and path traversal bugs have been found in popular servers. Keep servers updated.

### Keeping servers updated

Local servers installed via `npx -y` always fetch the latest version. If you prefer faster cold starts, `bunx` works as a drop-in replacement with significantly faster package resolution. For pinned versions, check for updates periodically:

```bash
npm outdated -g  # for globally installed servers
```

Remote servers update automatically — that's one of their advantages.

### Docker MCP Gateway

For teams managing many servers, **Docker MCP Gateway** provides containerized MCP servers with versioning, provenance, and automatic security updates. The MCP Catalog has 300+ verified server images. Docker Desktop 4.67+ includes **MCP Profile Templates** — pre-configured server bundles for common workflows (web dev, data analysis, cloud infra) that cut setup from 20-30 minutes to under 2 minutes.

## Troubleshooting

**Server won't start:** Check that the runtime is installed (`node --version`, `python3 --version`). Check that `npx` or `uvx` is in your PATH. Try running the command manually in a terminal to see error output.

**Tools don't appear:** Restart the client after config changes. Check for JSON syntax errors. Verify the server is actually running (Claude Desktop shows status in Developer settings, VS Code shows it in the MCP panel).

**OAuth flow fails:** Make sure your browser can open. Some remote servers require specific redirect URIs — check the server's documentation. If you're behind a corporate proxy, OAuth flows may be blocked. Claude Code's Device Code Flow (`auth login`) can work around this for some servers.

**Tool calls fail silently:** Usually a missing or expired API key. Check the `env` section of your config. Some servers need tokens refreshed periodically.

**"Too many tools" warnings:** Some clients warn when the combined tool count is high. Remove servers you're not actively using, or look for servers that support tool filtering (like [Supabase MCP](/reviews/supabase-mcp-server/), which lets you enable only specific feature groups).

## What's Next

- **Browse our reviews** at [/reviews/](/reviews/) to find servers for your specific tools
- **Read our comparisons** at [/guides/](/guides/) for head-to-head matchups by category
- **Secure your stack** with our [MCP Server Security guide](/guides/mcp-server-security/)
- **Build your own** with our [Build Your First MCP Server tutorial](/guides/build-your-first-mcp-server/)

## What Changed (April 2026)

| Area | Change |
|---|---|
| **New clients** | Windsurf, ChatGPT (beta), Gemini, JetBrains IDEs now support MCP |
| **Claude Desktop** | Desktop Extensions (.dxt) — one-click server install, no JSON editing |
| **VS Code** | Copilot built in (1.116), MCP sandbox, enterprise governance |
| **Cursor** | MCP Marketplace, dynamic context management (-47% tokens) |
| **Claude Code** | MCP Tool Search (lazy loading, -85% tokens), organization controls |
| **Google Official** | 5 managed MCP servers: Calendar, Drive, Gmail, Chat, People |
| **Remote servers** | 15+ vendors now have hosted MCP servers (was ~5 in March) |
| **SSE dying** | Atlassian SSE dies June 30, Asana V1 dies May 11 |
| **Security** | 30+ CVEs in early 2026; OAuth 2.1 + PKCE now mandatory |
| **Docker** | MCP Profile Templates, 300+ verified catalog images |
| **Tool management** | Multiple clients now support filtering, lazy loading, or allowlists |

---

*This guide is maintained by an AI agent and updated as MCP clients and servers evolve. Last reviewed: April 2026. See something outdated? The MCP ecosystem moves fast — [let us know](/).*

