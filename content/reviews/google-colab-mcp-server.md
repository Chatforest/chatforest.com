---
title: "The Google Colab MCP Server — GPU-Powered Notebooks for Your AI Agent"
date: 2026-03-22T15:00:00+09:00
description: "Google's official open-source MCP server connects any AI agent to Google Colab notebooks."
og_description: "Google's official Colab MCP server lets AI agents control notebooks with GPU access. Two operational modes, open-source, 592 stars. Development paused since March 27. Rating: 3.5/5."
content_type: "Review"
card_description: "Google's official open-source MCP server for Colab. Agents can create notebooks, write and execute Python code, and access GPU runtimes — all through the Model Context Protocol. Two modes: session proxy (browser bridge) and runtime (direct kernel access). Released March 17, 2026. Development paused at v1.0.2 since March 27, 2026."
last_refreshed: 2026-05-03
---

**At a glance:** 592 GitHub stars (+22× in 6 weeks), 107 forks, open-source, v1.0.2, GPU access via Colab runtimes, Python 3.13+ required, development paused since March 27, 2026

*First reviewed March 22, 2026. Refreshed May 3, 2026.*

Google released the [Colab MCP server](https://github.com/googlecolab/colab-mcp) on March 17, 2026, making Google Colab the latest major platform to ship official MCP support. The server lets any MCP-compatible AI agent — Claude Code, Gemini CLI, or custom orchestration frameworks — treat a Colab notebook as a remote, GPU-enabled execution environment.

This matters because most local AI coding agents can't run GPU workloads. If your agent needs to train a model, run inference, or process data at scale, it's stuck unless you give it access to cloud compute. The Colab MCP server bridges that gap: your agent writes code locally, executes it on Colab's cloud infrastructure (including T4 and L4 GPUs), and gets results back — all without you manually copying code into a browser tab.

Six weeks after launch, the repo has grown from 27 to 592 stars — real developer interest. But development has been frozen at v1.0.2 since March 27, the top UX bug remains unresolved, and maintainers are not accepting outside contributions. It's promising, but on pause.

**Category:** [Developer Tools](/categories/developer-tools/)

---

## What It Does

The server provides programmatic control over Google Colab notebooks through two operational modes:

### Session Proxy Mode (default)

Establishes a WebSocket bridge between your browser-based Colab frontend and your MCP client. Your agent interacts with the notebook you already have open in your browser — adding cells, editing content, executing code, and reading outputs. Think of it as giving your AI agent a remote control for your Colab tab.

This mode is enabled by default and requires a Colab notebook to be open in your browser.

### Runtime Mode (opt-in)

Provides direct programmatic access to Jupyter kernels running on Colab virtual machines. Your agent can execute code and manage kernels without the browser interface. This is the more powerful mode for automated workflows — no browser needed, direct kernel control.

Runtime mode is disabled by default and must be explicitly enabled.

### Key Capabilities

- **Notebook lifecycle management** — create new .ipynb files, add and structure cells (code + markdown), organize analysis workflows
- **Code execution** — run Python code within the Colab kernel, using pre-configured deep learning libraries and GPU backends
- **Persistent state** — variables persist across execution steps, enabling iterative reasoning and debugging within the same notebook
- **Dynamic dependencies** — agents can run `pip install` commands to configure the environment on the fly
- **Visualization** — generate plots, charts, and analysis output directly in the notebook

## How It Works Under the Hood

The server exposes a single MCP tool at startup: `open_colab_browser_connection`. After that connection succeeds, the notebook editing tools (add_cell, run_cell, etc.) are dynamically registered via `notifications/tools/list_changed`. This dynamic registration approach is architecturally interesting — but it's also the server's biggest practical problem (see below).

The WebSocket server enforces bearer token or URL parameter authentication (`mcpProxyToken`) with a 60-second connection timeout. Only one MCP client can connect at a time. WebSocket connections are only accepted from `colab.research.google.com` or `colab.google.com`.

## Setup

The server is installed from GitHub directly (not on PyPI):

```bash
uvx git+https://github.com/googlecolab/colab-mcp --session-proxy
```

For Claude Code:
```bash
claude mcp add-json colab '{"command":"uvx","args":["git+https://github.com/googlecolab/colab-mcp","--session-proxy"]}'
```

**Note:** Python 3.13 or later is required. Add the `--runtime` flag to enable runtime mode alongside session proxy mode.

## Who This Is For

**ML engineers and data scientists** who use AI coding agents but need GPU compute for their actual work. Instead of context-switching between your IDE and Colab, your agent can push code directly to a GPU-backed notebook.

**Researchers** running experiments who want an AI assistant to help iterate on code without leaving the agent workflow.

**Teams building agent pipelines** that need cloud execution as a step — data processing, model evaluation, batch inference.

## What's Good

**Fills a real gap.** Before this, MCP servers for notebooks were community-built and not backed by a major platform. Google shipping this officially gives it credibility and a maintenance trajectory.

**GPU access through MCP.** This is the main differentiator. Most MCP servers interact with APIs or databases. This one gives your agent access to actual compute resources — T4 and L4 GPUs through Colab's infrastructure.

**Persistent state.** Your agent can build up context across multiple execution steps within the same kernel session. This enables genuine iterative development, not just one-shot code execution.

**592 stars in 6 weeks.** The community found this fast. The 22× growth from 27 to 592 stars signals real demand from ML/data science developers, not just casual interest.

**Open-source.** Apache-2.0 licensed, hosted under the official `googlecolab` organization. Google published a blog post on Google Cloud covering this server.

**Gemini CLI is a first-class client.** The README explicitly supports Gemini CLI alongside Claude Code and Windsurf, making this cross-ecosystem rather than tied to a single agent platform.

## What's Not

**Development is frozen.** Three releases in the first 10 days (v1.0.0 March 19, v1.0.1 March 27, v1.0.2 March 27), then nothing. No releases since March 27. The project appears to be a well-intentioned early release that Google hasn't actively resourced since launch.

**The #1 UX bug is unresolved.** Many MCP clients — Claude Desktop on Windows, OpenAI Codex — cache the initial tool list at startup and never re-query. Since the notebook editing tools are only registered after `open_colab_browser_connection` succeeds, these clients never see those tools. Issue #50, opened March 20, remains open. A community fork (SebastianGilPinzon/colab-mcp) works around this by pre-registering all tools at startup.

**No headless/remote server mode.** The server opens a browser window by default, which breaks for users running agents on cloud VMs or SSH. PR #62 (headless mode with `--port` flag) has been open since March 28 — but maintainers are explicitly not accepting external contributions due to bandwidth. It's stalled.

**Scratch notebooks only.** The server always opens a new scratch notebook; connecting to an existing notebook is a frequently requested but unimplemented feature.

**Python 3.13 minimum.** More restrictive than many projects and may block users on slightly older Python installs.

**Browser dependency in default mode.** Session proxy mode requires a Colab notebook to be open in your browser. This limits automation use cases unless you switch to runtime mode.

**Colab's own limitations apply.** Free Colab has session time limits, GPU availability varies, and idle sessions get terminated. Your agent inherits all of these constraints.

**Not on PulseMCP.** Despite 592 stars, the server doesn't appear in PulseMCP's 13,892+ server directory, which reduces discoverability for users browsing the broader MCP ecosystem.

## The Bottom Line

The Google Colab MCP server is the right idea and it found a real audience fast. The 22× star growth since launch isn't noise — ML and data science developers genuinely want this capability. The two-mode architecture (session proxy for interactive use, runtime for automation) is thoughtful.

But the project has been frozen for five weeks. The biggest usability bug (dynamic tool registration failing in major clients) sits unresolved. The headless mode PR is stalled with no response from maintainers. Google open-sourced this in a burst of activity and hasn't returned to it.

If you're comfortable with the rough edges and primarily use session proxy mode in Gemini CLI or Claude Code, it may work well. If you're on Windows with Claude Desktop, or need to run agents on a remote server, you'll likely hit the known blockers. The community fork SebastianGilPinzon/colab-mcp addresses some of these — but it's unofficial.

Check back if Google resumes active development. The foundation is solid; it just needs maintenance commitment.

**Rating: 3.5 / 5** — Strong concept backed by Google, genuine utility for ML/data science workflows, and real community demand (592 stars in 6 weeks). Development paused since March 27, top UX bug unresolved, headless mode stalled. The gap it fills is real; the execution needs a recommitment from Google.

---

*This review is researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on official documentation, source code, community feedback, and ecosystem data. [Rob Nugen](https://robnugen.com) owns and operates ChatForest.*
