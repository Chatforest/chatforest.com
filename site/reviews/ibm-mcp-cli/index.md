# IBM mcp-cli — A Feature-Rich Terminal Client for MCP Servers

> IBM mcp-cli reviewed: a Python CLI client for MCP servers with multi-provider LLM support (Ollama, OpenAI, Anthropic, watsonx, and more), execution plans, session management, and a real-time dashboard. Apache-2.0. Rating: 4.0/5.


Most MCP guides start with Claude Desktop: download, configure, done. But Claude Desktop is a GUI application. It does not compose into shell pipelines. It does not run without a display. It does not let you switch LLM providers in the middle of a conversation, save sessions for later, or build multi-step execution plans. For users who want the full power of MCP from a terminal — or from a script — a purpose-built CLI client is the better tool.

[IBM/mcp-cli](https://github.com/IBM/mcp-cli) is exactly that. It is a Python command-line client that connects to one or more MCP servers, routes prompts through your choice of nine LLM providers, and exposes a feature set that most GUI MCP clients have not caught up with yet. At approximately **2,000 GitHub stars** and v0.19 (released March 2, 2026), it is the most capable open-source MCP CLI client currently available.

This is not an IBM product integration. It does not require IBM Cloud or watsonx. The IBM connection is that the primary author, chrishayuk (Chris Hayuk), works at IBM and the project lives under the IBM GitHub organization — but mcp-cli is provider-agnostic, open source infrastructure for anyone. Part of our **[Developer Tools MCP category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Repo** | [IBM/mcp-cli](https://github.com/IBM/mcp-cli) |
| **Stars** | ~2,000 |
| **License** | Apache-2.0 |
| **Language** | Python |
| **Install** | `pip install mcp-cli` or `uvx mcp-cli` |
| **PyPI** | [mcp-cli](https://pypi.org/project/mcp-cli/) |
| **Latest version** | v0.19 (March 2026) |
| **Requires** | Python ≥3.11 |
| **First release** | December 2024 |
| **Primary author** | chrishayuk (Chris Hayuk) |

---

## What mcp-cli Does

mcp-cli is a client and host for the Model Context Protocol. It connects to MCP servers you configure, discovers the tools those servers expose, and routes user prompts to an LLM that can call those tools. The client handles the full loop: sending the prompt, receiving the tool-call request from the model, executing the call against the connected MCP server, feeding results back to the model, and streaming the final response to the terminal.

Connect it to a filesystem MCP server and an LLM with filesystem tools becomes available. Connect it to a SQLite MCP server and natural-language queries against a database become possible. Connect it to multiple servers simultaneously and those tool catalogs are automatically merged into a single namespace available to the model.

This is the same pattern as Claude Desktop or any other MCP host — the difference is that mcp-cli does it in a terminal, without a GUI, and with a much richer set of operating modes and controls.

---

## Three Modes

**Chat mode** (default) is a streaming conversational interface. Type a prompt, the model responds, tools are called automatically as needed. All the standard LLM chat UX — but grounded in whatever MCP servers you have connected.

**Interactive mode** is a shell for direct MCP operations. Instead of prompting an LLM, you call MCP tools directly, inspect server state, and work at the protocol layer. This is useful for MCP server development, debugging, or quick lookups without involving a model.

**Command mode** is the pipeline-friendly interface. Commands are passed as arguments, output is stdout-formatted for chaining, and there is no interactive session overhead. Useful for scripting, CI workflows, or integrating MCP-powered queries into shell automation.

---

## LLM Providers

The most notable feature of mcp-cli relative to alternatives is its multi-provider support. Nine providers are available out of the box:

| Provider | Notes |
|---|---|
| **Ollama** (default) | Local inference, no API key required. Default model: gpt-oss |
| **OpenAI** | GPT-5, GPT-4o, O3 family |
| **Anthropic** | Claude 4.5, Claude 3.5 Sonnet |
| **Azure OpenAI** | Enterprise GPT endpoints |
| **Google Gemini** | Gemini 2.0 Flash, 1.5 Pro |
| **Groq** | Fast inference, Llama 3.1, Mixtral |
| **Perplexity** | Sonar models with real-time search |
| **IBM watsonx** | Granite, Llama, enterprise compliance |
| **Mistral AI** | Mistral Large, Medium |

The default is **Ollama with gpt-oss** — meaning a working local mcp-cli session requires no API key and no cloud account. For teams evaluating MCP tooling without budget approval, this is a practical advantage.

Provider switching is live during a session: `/provider anthropic` or `/provider openai` mid-conversation shifts the model without restarting. `/model` switches between models within the same provider.

---

## Slash Commands

Chat mode supports a rich set of slash commands:

| Command | What it does |
|---|---|
| `/tools` | List all tools discovered from connected MCP servers |
| `/tool <name>` | Execute a specific MCP tool directly |
| `/servers` | List active MCP server connections |
| `/health` | Check server health status |
| `/provider <name>` | Switch active LLM provider |
| `/model <name>` | Switch model; `/models` lists available options |
| `/plan` | Create, list, show, run, delete, or resume execution plans |
| `/sessions` | Save, load, or list conversation sessions |
| `/export` | Export conversation as Markdown or JSON |
| `/attach` (or `/file`, `/image`) | Stage files for the next message |
| `@file:path/to/file` | Inline file reference syntax |
| `/memory` (or `/vm`, `/mem`) | View AI Virtual Memory state |
| `/usage` (or `/tokens`, `/cost`) | Token usage and cost tracking |
| `/dashboard` | Open real-time browser UI |
| `/theme` | Switch display theme (8 built-in options) |
| `/clear` | Clear conversation history |

---

## Execution Plans

Plans are the feature that moves mcp-cli beyond a simple chat client. A plan is a named, multi-step workflow — a sequence of actions, tool calls, and conditional logic that can be created, saved, reviewed, and re-executed.

Creating a plan with `/plan create` prompts the model to generate a structured workflow from a description. `/plan run` executes it. `/plan resume` picks up an interrupted plan. This is a lightweight form of agent orchestration built directly into the CLI — useful for recurring workflows that involve multiple MCP tool calls in sequence.

---

## AI Virtual Memory

The `/memory` command exposes what mcp-cli calls AI Virtual Memory — a mechanism for persisting state across sessions, allowing the model to maintain a working memory of facts, preferences, and intermediate results that carry forward to future conversations.

This feature is explicitly marked **experimental** in the documentation. It works, but the architecture is evolving and the behavior may change between releases. Worth knowing about, worth trying, but not a production-critical dependency yet.

---

## Session Management

`/sessions` saves the current conversation to a named session and loads it back in later runs. `/export` produces a shareable Markdown or JSON transcript. For users who run repeated workflows against MCP servers — daily reports, recurring queries, iterative research — persistent sessions are a meaningful quality-of-life feature.

---

## Installation

The recommended path using uv:

```bash
pip install uv                      # if not already installed
ollama pull gpt-oss                  # optional: for local-first default
uvx mcp-cli --help
```

Standard pip:

```bash
pip install mcp-cli
pip install "mcp-cli[apps]"          # includes dashboard/browser UI support
```

From source:

```bash
git clone https://github.com/IBM/mcp-cli
cd mcp-cli
pip install -e "."
```

Requires Python ≥3.11. Uses uv internally for fast dependency resolution.

---

## MCP Server Configuration

Servers are configured in a `server_config.json` file, passed via the `--config` flag or set as the default. Each entry specifies the transport (stdio or SSE), the command, and any arguments. Multiple servers can be listed and all are connected simultaneously when mcp-cli starts.

---

## Project Activity

mcp-cli is actively maintained. 50+ PyPI releases since December 2024, last commit March 2026, 4,300+ unit tests with a 60% minimum branch coverage gate. The primary contributor is chrishayuk; Renovate bot handles automated dependency updates. The PyPI release cadence averages roughly three releases per month across the project's lifetime.

One structural note: the project does not publish formal GitHub Releases. All versioning lives on PyPI. This is a minor friction point for users who track projects via GitHub release feeds or want clean changelogs — the history is there, but spread across commit messages rather than collected in release notes.

---

## Known Issues and Gaps

- **No GitHub Releases** — versioning is PyPI-only; no consolidated changelogs
- **Windows 11 compatibility** — filesystem MCP server issues reported on Windows 11
- **SSE server ping** — `ping` command does not work with SSE transport
- **OAuth errors** — 404 errors when connecting to MCP servers that do not implement OAuth; should fail gracefully
- **AI Virtual Memory** — experimental, behavior may change
- **No `--system-prompt` flag** in chat mode — feature request open, not yet implemented
- **Roadmap Tiers 7–12** — described in documentation, not yet implemented

None of these are blockers for the core use case (chat with MCP servers from a terminal), but they are worth knowing.

---

## Alternatives

**philschmid/mcp-cli** — A simpler Python CLI by Hugging Face engineer Philipp Schmid. Basic stdio MCP interaction only. No multi-provider support, no session management, no execution plans. Holds a different package name on PyPI. Better if you want minimal dependencies and a quick inspect of a single server.

**mcphost (mark3labs)** — Archived as of early 2026. 1,600 stars at archival. Users directed to migrate to Kit. Not an active alternative.

**MCP Inspector** — A development and debugging tool for MCP server authors, not a conversational client. Different target user: someone building a server, not someone using one.

**apify/mcpc** — A newer lightweight universal MCP CLI client. Supports persistent sessions, stdio/HTTP, OAuth 2.1, JSON output, and x402. More minimal than mcp-cli; useful if you want a lighter footprint or proxy functionality.

IBM mcp-cli is the right choice when you want the full feature set — multiple providers, execution plans, session persistence, a dashboard — and are comfortable with Python's runtime overhead versus a Go binary.

---

## Relationship to IBM MCP Servers

IBM/mcp-cli is separate from IBM's portfolio of MCP servers (data-intelligence, IBM i, watsonx.data, etc.) covered in our **[IBM MCP Servers review](/reviews/ibm-mcp-servers/)**. It is also separate from **[IBM ContextForge MCP Gateway](/reviews/ibm-contextforge-mcp-gateway/)**, which is a server-side federation and governance proxy. mcp-cli is the client. You could use mcp-cli to connect to IBM MCP servers through an IBM ContextForge gateway — or to any MCP servers from any vendor through any transport.

---

## Rating: 4.0 / 5

mcp-cli is the most feature-complete open-source MCP CLI client available. Multi-provider support, execution plans, session management, a browser dashboard, and a local-first default all distinguish it from the alternatives. The 4,300-test suite and regular PyPI releases indicate a project being maintained seriously.

The deductions: no formal GitHub Releases creates friction for changelogs. AI Virtual Memory is experimental and the name oversells it. Some compatibility issues (Windows, SSE, OAuth edge cases) remain open. The complexity is substantial for a CLI tool — the right mental model is a lightweight agent framework running in a terminal, not a simple prompt wrapper. That complexity pays off at scale but is overkill for ad-hoc tool inspection.

For developers building MCP-powered workflows, automating MCP tool calls in scripts, testing MCP servers across multiple LLM providers, or running MCP in environments without a GUI, mcp-cli is the practical choice.

---

*Reviewed 2026-05-05. Research based on public GitHub repository, PyPI package history, and project documentation. We do not have hands-on testing access to rate live performance.*

