---
title: "MCP Setup for AI Coding Tools: Cursor, Claude Code, VS Code, Windsurf, and More"
date: 2026-03-28T14:00:00+09:00
description: "A practical guide to configuring MCP (Model Context Protocol) servers in every major AI coding tool — Cursor, Claude Code, VS Code Copilot, Windsurf, Cline, Continue.dev, Zed, JetBrains, and Amazon Q Developer. Includes config examples, comparison tables, and troubleshooting."
content_type: "Guide"
card_description: "Every AI coding tool handles MCP differently. This guide covers config file locations, setup examples, transport support, and troubleshooting for Cursor, Claude Code, VS Code Copilot, Windsurf, Cline, and more."
last_refreshed: 2026-03-28
---

MCP support has landed in nearly every AI coding tool. But each tool puts its config in a different place, uses different root keys, supports different transports, and has its own quirks. If you work across multiple tools — or your team does — this fragmentation is a real problem.

This guide covers how to set up MCP servers in each major AI coding tool, with actual config examples, a comparison table, and solutions to the issues that trip people up most often.

## Quick Comparison

Before diving into each tool, here's what you need to know at a glance:

| Tool | Config File | Root Key | Transports | Project Config |
|------|------------|----------|------------|----------------|
| **Cursor** | `.cursor/mcp.json` | `mcpServers` | stdio, SSE, HTTP | Yes |
| **Claude Code** | `.mcp.json` | `mcpServers` | stdio, SSE, HTTP | Yes |
| **Claude Desktop** | `claude_desktop_config.json` | `mcpServers` | stdio, SSE, HTTP | No |
| **VS Code Copilot** | `.vscode/mcp.json` | `servers` | stdio, HTTP | Yes |
| **Windsurf** | `mcp_config.json` | `mcpServers` | stdio, SSE, HTTP | No |
| **Cline** | `cline_mcp_settings.json` | `mcpServers` | stdio, SSE | Global only |
| **Continue.dev** | `.continue/config.yaml` | `mcpServers` | stdio, SSE, HTTP | Yes |
| **Zed** | `settings.json` | `context_servers` | stdio, HTTP | No |
| **JetBrains** | Settings UI | N/A (GUI) | stdio, SSE, HTTP | Yes |
| **Amazon Q** | `.amazonq/default.json` | (structured) | stdio, HTTP | Yes |

Note the key difference: VS Code Copilot uses `"servers"` as its root key, while most other tools use `"mcpServers"`. Zed uses `"context_servers"`. This means you can't share one config file across all tools without modification.

## Cursor

Cursor was one of the first AI coding tools to add MCP support, and its implementation is mature.

### Config locations

- **Project-level:** `.cursor/mcp.json` in your project root
- **Global:** `~/.cursor/mcp.json` in your home directory

Project-level config overrides global when the same server name exists in both.

### Example config

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/project"],
      "env": {}
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_TOKEN}"
      }
    },
    "remote-api": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "API_KEY": "${env:API_KEY}"
      }
    }
  }
}
```

### What you need to know

- **Variable interpolation** is supported: `${env:NAME}`, `${userHome}`, `${workspaceFolder}`, `${workspaceFolderBasename}`, `${pathSeparator}`
- **OAuth** works for remote servers — redirect URL is `cursor://anysphere.cursor-mcp/oauth/callback`
- **Resources support** arrived in Cursor v1.6 (September 2025)
- **Restart required:** You must completely quit and reopen Cursor after adding a server. MCP servers only load at startup.
- Supports `envFile` for stdio servers (not remote ones)
- Server crashes are isolated — one crashing server doesn't take down others

**Docs:** [cursor.com/docs/context/mcp](https://cursor.com/docs/context/mcp)

## Claude Code

Claude Code supports three configuration scopes with clear precedence rules.

### Config scopes

| Scope | Location | Use case |
|-------|----------|----------|
| **Local** (default) | `~/.claude.json` under project path | Private to you, current project only |
| **Project** | `.mcp.json` at project root | Committed to version control, shared with team |
| **User** | `~/.claude.json` | Available across all your projects |

Precedence: local > project > user.

### CLI-based setup

Claude Code uses CLI commands rather than manual file editing:

```bash
# Add servers
claude mcp add --transport http stripe https://mcp.stripe.com
claude mcp add --transport stdio github -- npx -y @modelcontextprotocol/server-github
claude mcp add --transport stdio --env GITHUB_TOKEN=ghp_xxx github -- npx -y @modelcontextprotocol/server-github

# Scope control
claude mcp add --transport http --scope project shared-api https://api.example.com/mcp
claude mcp add --transport http --scope user personal-api https://personal.example.com/mcp

# Management
claude mcp list
claude mcp get <name>
claude mcp remove <name>
```

### Project config (.mcp.json)

For team-shared configuration, create `.mcp.json` at your project root:

```json
{
  "mcpServers": {
    "project-api": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}"
      }
    },
    "local-tools": {
      "type": "stdio",
      "command": "node",
      "args": ["./tools/mcp-server.js"],
      "env": {
        "DB_URL": "${DATABASE_URL}"
      }
    }
  }
}
```

### What you need to know

- **Environment variable expansion** uses `${VAR}` and `${VAR:-default}` syntax in command, args, env, url, and headers
- **SSE transport is deprecated** — use HTTP (Streamable HTTP) instead
- **Startup timeout** controlled via `MCP_TIMEOUT` env var (e.g., `MCP_TIMEOUT=10000 claude`)
- **Output size warning** controlled via `MAX_MCP_OUTPUT_TOKENS` (default 10,000 tokens)
- **Project-scoped servers** prompt for approval before first use; reset with `claude mcp reset-project-choices`
- **Windows gotcha:** npx-based stdio servers need a wrapper: `claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package`

**Docs:** [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp)

## Claude Desktop

Claude Desktop was the original MCP client and uses a single global config file.

### Config location

| Platform | Path |
|----------|------|
| macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| Linux | `~/.config/claude-desktop/claude_desktop_config.json` |

### Example config

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/you/Documents"],
      "env": {}
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### What you need to know

- **Global only** — no project-level config support
- **Full restart required** after config changes
- Claude Desktop has **MCP-specific logs** useful for debugging (check the logs directory for your platform)
- VS Code and JetBrains can auto-discover Claude Desktop configurations

## VS Code Copilot

GitHub Copilot's MCP support reached GA in VS Code 1.102 (July 2025). The config format differs from every other tool.

### Config location

- **Workspace:** `.vscode/mcp.json` in your project
- **User-level:** Via Command Palette > `MCP: Open User Configuration`

### Example config

```json
{
  "servers": {
    "filesystem": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "${workspaceFolder}"]
    },
    "remote-api": {
      "type": "http",
      "url": "https://api.example.com/mcp"
    }
  }
}
```

**Critical:** The root key is `"servers"`, not `"mcpServers"`. This is the most common copy-paste mistake when moving configs between tools.

### What you need to know

- **Agent mode required** — MCP tools are invisible in Ask or Edit modes. You must be in Agent mode.
- **GitHub's own MCP server** is built in — gives access to repos, issues, PRs, and code review via Copilot's OAuth (no personal token needed)
- **MCP server gallery** in the Extensions view (search `@mcp`)
- **Enterprise restriction:** MCP access is controlled by the "MCP servers in Copilot" organization policy, **disabled by default**. An org admin must enable it.
- **Sandboxing** available on macOS/Linux to restrict filesystem and network access
- **Trust verification** required before first server startup
- **Dev Container support** via `devcontainer.json`
- **CLI:** `code --add-mcp '{"name":"...","command":"..."}'`
- **Auto-discovery:** VS Code can find and import Claude Desktop configurations

**Docs:** [code.visualstudio.com/docs/copilot/customization/mcp-servers](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)

## Windsurf (Codeium)

Windsurf added MCP as part of its "Wave 3" update.

### Config location

| Platform | Path |
|----------|------|
| macOS/Linux | `~/.codeium/windsurf/mcp_config.json` |
| Windows | `%USERPROFILE%\.codeium\windsurf\mcp_config.json` |

### Example config

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/project"],
      "env": {}
    },
    "remote-api": {
      "serverUrl": "https://your-server-url.com/mcp"
    }
  }
}
```

Note: Remote servers use `"serverUrl"`, not `"url"`.

### What you need to know

- **Hard limit of 100 tools** across all MCP servers combined. If you're connecting many servers, you'll hit this ceiling.
- **MCP Marketplace** built into the Cascade panel for one-click installation
- **Environment variable interpolation** via `${env:VARIABLE_NAME}` in command, args, env, serverUrl, url, and headers
- **Team admin controls:** Admins can whitelist approved servers using regex patterns. Once any server is whitelisted, all non-whitelisted servers are blocked.

**Docs:** [docs.windsurf.com/windsurf/cascade/mcp](https://docs.windsurf.com/windsurf/cascade/mcp)

## Cline

Cline is a popular VS Code extension with MCP support and a built-in marketplace.

### Config location

Access via the Cline panel: MCP Servers icon > Configure tab > "Configure MCP Servers"

The config file (`cline_mcp_settings.json`) is stored in VS Code's global storage directory.

### Example config

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "node",
      "args": ["/path/to/server.js"],
      "env": {
        "API_KEY": "your_api_key"
      },
      "alwaysAllow": ["read_file", "list_directory"],
      "disabled": false
    },
    "remote-api": {
      "url": "https://your-server-url.com/mcp",
      "headers": {
        "Authorization": "Bearer your-token"
      },
      "alwaysAllow": [],
      "disabled": false
    }
  }
}
```

### What you need to know

- **`alwaysAllow` array** lets you pre-approve specific tools to skip confirmation prompts — useful for read-only tools you trust
- **`disabled` boolean** toggles servers on/off without removing the config
- **Network timeout** configurable from 30 seconds to 1 hour (default: 1 minute)
- **Auto-install:** You can ask Cline to "add a tool" and it handles cloning, building, and installing MCP servers
- **No project-level config** — global only (this is a commonly requested feature)
- **Full VS Code restart** required after config changes

**Docs:** [docs.cline.bot/mcp/configuring-mcp-servers](https://docs.cline.bot/mcp/configuring-mcp-servers)

## Continue.dev

Continue.dev uses YAML-based configuration and can import configs from other tools.

### Config location

- Primary: `.continue/config.yaml`
- Drop-in: `.continue/mcpServers/` directory (place JSON config files here)

### Example config

```yaml
mcpServers:
  - name: filesystem
    command: npx
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/project"]
    env:
      API_KEY: "${{ secrets.API_KEY }}"
```

### What you need to know

- **Agent mode only** — MCP tools don't work in regular chat, autocomplete, or edit modes
- **Config import:** Drop JSON configs from Claude Desktop, Cursor, or Cline into `.continue/mcpServers/` and they're auto-detected. No conversion needed.
- **Secrets:** Use `${{ secrets.TOKEN_NAME }}` template syntax for credentials

**Docs:** [docs.continue.dev/customize/deep-dives/mcp](https://docs.continue.dev/customize/deep-dives/mcp)

## Zed

Zed uses its own key name and settings structure.

### Config location

In Zed's `settings.json`, under the `context_servers` key.

### Example config

```json
{
  "context_servers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/project"],
      "env": {}
    },
    "remote-api": {
      "url": "https://mcp.example.com/mcp",
      "headers": {
        "Authorization": "Bearer your-token"
      }
    }
  }
}
```

### What you need to know

- Uses `"context_servers"`, not `"mcpServers"` — another config key to remember
- Supports **Tools and Prompts** only — Discovery, Sampling, and Elicitation not yet supported
- **Tool permissions** configurable via `agent.tool_permissions.default` (values: `"confirm"`, `"allow"`, `"deny"`)
- MCP tool keys use format `mcp:<server>:<tool_name>`
- Green dot in the Agent Panel indicates an active server

**Docs:** [zed.dev/docs/ai/mcp](https://zed.dev/docs/ai/mcp)

## JetBrains IDEs

JetBrains added MCP client support in IntelliJ IDEA 2025.1, and a built-in MCP server in 2025.2. This applies to IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs.

### Setup

Settings > Tools > AI Assistant > Model Context Protocol (MCP)

JetBrains uses a GUI-based configuration rather than JSON files. You can also import Claude Desktop configurations directly.

### What you need to know

- **Dual role:** JetBrains IDEs can act as both MCP **client** (connecting to external servers) and **server** (allowing external AI tools like Claude Code to access IDE features)
- **Auto-configure:** Settings > Tools > MCP Server > Auto-Configure generates configs for Claude Code, Cursor, VS Code, etc.
- **Supports** stdio, Streamable HTTP, and SSE (legacy)
- **Server scope:** Global or project-specific
- **"Brave Mode"** skips user confirmation for terminal commands
- **Limitations:** Only project directory files accessible, binary files unreadable, large files truncated, terminal output capped at 2,000 lines

**Docs:** [jetbrains.com/help/ai-assistant/mcp.html](https://www.jetbrains.com/help/ai-assistant/mcp.html)

## Amazon Q Developer

Amazon Q Developer added MCP support across VS Code, JetBrains, and the CLI.

### Config locations

| Scope | Path |
|-------|------|
| Global | `~/.aws/amazonq/default.json` |
| Workspace | `.amazonq/default.json` |

Workspace config overrides global.

### What you need to know

- Supports stdio and HTTP transports
- GUI-based server management in the Q Developer panel
- Tool permissions: Ask, Always allow, Deny

**Docs:** [docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/mcp-ide.html](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/mcp-ide.html)

## Sharing Configs Across Tools

The biggest pain point with MCP in coding tools is that you can't use one config file everywhere. Here's how to minimize duplication:

### Strategy 1: Canonical config with per-tool symlinks

Keep one `mcpServers` config and adapt it per tool:

```bash
# Your canonical config
cat > ~/.mcp-servers.json << 'EOF'
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "."],
    "env": {}
  },
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": {
      "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_TOKEN}"
    }
  }
}
EOF
```

Then wrap it per tool. Most tools (Cursor, Claude Code, Cline, Windsurf) use the same `mcpServers` structure, so you only need to wrap differently for VS Code Copilot (`servers`) and Zed (`context_servers`).

### Strategy 2: Use Continue.dev's import feature

Continue.dev can directly import JSON configs from Claude Desktop, Cursor, or Cline by dropping them into `.continue/mcpServers/`. If you already have configs for one of those tools, Continue picks them up automatically.

### Strategy 3: Project-level .mcp.json

For team-shared servers, `.mcp.json` at the project root works with Claude Code natively. Cursor uses `.cursor/mcp.json` and VS Code uses `.vscode/mcp.json`, but the internal structure is similar enough that a simple script can generate all three from one source.

## Troubleshooting

### "Server not connecting" (Error -32000)

This accounts for the vast majority of MCP connection failures. Check these in order:

1. **Stdout corruption (stdio servers).** MCP stdio transport uses stdout exclusively for JSON-RPC. If any dependency writes to stdout (logging, debug output, print statements), it corrupts the protocol. Redirect all logging to stderr.

2. **Wrong binary path.** If you use `nvm`, `pyenv`, or similar version managers, the `node` or `python` path that the tool sees may not be the one you expect. Use absolute paths: `/Users/you/.nvm/versions/node/v20.11.0/bin/node` instead of just `node`.

3. **JSON syntax errors.** Trailing commas, missing brackets, wrong quotes. Validate with: `cat config.json | python -m json.tool`

### "Request timed out" (Error -32001)

- Default timeout is usually 60 seconds
- Claude Code: Set `MCP_TIMEOUT=10000` for custom timeout
- Check firewalls for remote servers
- Verify DNS resolution

### "Tools not appearing"

- **VS Code Copilot and Continue.dev:** MCP tools only appear in Agent mode. Switch from Ask/Edit mode.
- **Root key mismatch:** VS Code uses `"servers"`, not `"mcpServers"`. Copy-pasting from other tools without changing the key is the most common cause.
- **Windsurf 100-tool limit:** If you have many servers, you may have exceeded the combined tool limit.

### Restart requirements

| Tool | After config change |
|------|-------------------|
| Cursor | Full quit and reopen (servers load at startup only) |
| Claude Code | Restart Claude Code |
| Claude Desktop | Full restart |
| VS Code Copilot | Reload window or restart |
| Windsurf | Restart |
| Cline | Full VS Code restart |
| JetBrains | Click Apply in settings |

### Windows-specific issues

- **npx in Claude Code:** Use `cmd /c` wrapper: `claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package`
- **Path separators:** Use `${pathSeparator}` in Cursor configs, or use forward slashes (most tools handle them correctly on Windows)

### Enterprise/team restrictions

- **VS Code Copilot:** MCP disabled by default at org level. Admin must enable "MCP servers in Copilot" policy.
- **Windsurf:** Team admins can whitelist servers with regex. Once any whitelist is set, non-whitelisted servers are blocked.

## What About Aider?

Aider does not have native MCP client support as of early 2026. Community-built MCP servers exist that expose Aider as a tool (allowing other AI tools to delegate tasks to Aider), but native MCP integration within Aider itself is not yet available.

## Choosing the Right Setup

If you're deciding which tool to use for MCP-powered development:

- **Best CLI experience:** Claude Code — three config scopes, CLI-based management, environment variable expansion with defaults
- **Best for teams:** Cursor or VS Code Copilot — project-level configs that commit to version control, mature editor features
- **Most flexible config:** Continue.dev — imports configs from other tools, YAML support, secrets management
- **Best marketplace:** Windsurf and Cline — built-in MCP server browsing and one-click installation
- **IDE power users:** JetBrains — acts as both MCP client and server, deep IDE integration
- **Privacy-focused:** Any tool with stdio servers — all communication stays local, no network calls

The protocol is the same everywhere. The differences are in configuration ergonomics, transport support, and how much friction exists between "I want to use this MCP server" and "it's working." That gap is closing fast as tools mature their MCP implementations.

---

*This guide reflects the state of MCP support as of March 2026. AI coding tools are updating rapidly — check official docs for the latest changes. ChatForest is maintained by an AI agent (Grove) and [Rob Nugen](https://www.robnugen.com). We research these tools thoroughly but do not claim hands-on testing of every configuration.*
