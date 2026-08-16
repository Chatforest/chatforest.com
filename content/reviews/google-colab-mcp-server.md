---
title: "The Google Colab MCP Server — GPU-Powered Notebooks for Your AI Agent"
date: 2026-03-22T15:00:00+09:00
description: "Google's official open-source MCP server connects any AI agent to Google Colab notebooks."
og_description: "Google's official Colab MCP server lets AI agents drive a browser-based Colab notebook, including GPU access. Open-source, 850+ stars. No commits since April 1, 2026. Rating: 3.5/5."
content_type: "Review"
card_description: "Google's official open-source MCP server for Colab. Agents can create notebooks, write and execute Python code, and manage dependencies through the browser-based session proxy. An initial runtime/direct-kernel mode shipped at launch but was removed from the codebase 5 days later and never returned. Released March 17, 2026. No releases since v1.0.2 (March 27, 2026); no commits since April 1, 2026."
last_refreshed: 2026-08-16
sources_audited: 2026-08-16
---

**At a glance:** [850+ GitHub stars](https://github.com/googlecolab/colab-mcp/stargazers) (up from 27 at launch), [168 forks](https://github.com/googlecolab/colab-mcp/network/members), [Apache-2.0 open-source](https://github.com/googlecolab/colab-mcp/blob/main/LICENSE), [v1.0.2](https://github.com/googlecolab/colab-mcp/releases), session-proxy access to a browser-based Colab notebook (runtime/direct-kernel mode was removed 5 days after launch), [Python 3.13+ required](https://github.com/googlecolab/colab-mcp/blob/main/pyproject.toml), [no commits since April 1, 2026](https://github.com/googlecolab/colab-mcp/commits/main/)

*First reviewed March 22, 2026. Refreshed May 3, 2026. Re-audited August 16, 2026.*

Google [announced the Colab MCP server](https://developers.googleblog.com/announcing-the-colab-mcp-server-connect-any-ai-agent-to-google-colab/) on March 17, 2026 (the [first tagged GitHub release, v1.0.0, followed two days later](https://github.com/googlecolab/colab-mcp/releases/tag/v1.0.0)), making Google Colab the latest major platform to ship official MCP support. The server lets any MCP-compatible AI agent — Claude Code, Gemini CLI, or custom orchestration frameworks — treat a Colab notebook you already have open in your browser as a remote execution environment.

This matters because most local AI coding agents can't run GPU workloads. If your agent needs to train a model, run inference, or process data at scale, it's stuck unless you give it access to cloud compute. The Colab MCP server bridges that gap: your agent writes code, pushes it into your open Colab notebook, executes it on whatever runtime Colab has allocated — CPU or GPU, [depending on your plan and availability](https://research.google.com/colaboratory/faq.html) — and gets results back, all without you manually copying code into the browser tab.

By August 2026, the repo had grown from 27 to [850+ stars](https://github.com/googlecolab/colab-mcp/stargazers) — real developer interest. But [development stopped after a docs-only commit on April 1, 2026](https://github.com/googlecolab/colab-mcp/commits/main/), [no code has shipped since v1.0.2 on March 27](https://github.com/googlecolab/colab-mcp/releases), the top UX bug remains unresolved, and maintainers are not accepting outside contributions. It's promising, but stalled.

**Category:** [Developer Tools](/categories/developer-tools/)

---

## What It Does

The server provides programmatic control over a Google Colab notebook through a single shipping mode — [session proxy](https://github.com/googlecolab/colab-mcp/blob/main/src/colab_mcp/session.py):

### Session Proxy Mode (the only mode that currently ships)

Establishes a WebSocket bridge between your browser-based Colab frontend and your MCP client. Your agent interacts with the notebook you already have open in your browser — adding cells, editing content, executing code, and reading outputs. Think of it as giving your AI agent a remote control for your Colab tab. It's enabled by default and requires a Colab notebook to be open in your browser; the current [`__init__.py` entry point](https://github.com/googlecolab/colab-mcp/blob/main/src/colab_mcp/__init__.py) exposes only a `-p`/`--enable-proxy` flag (on by default) and a `-l`/`--log` flag.

### Runtime Mode — shipped at launch, removed 5 days later

Early coverage (including our own initial review) described a second, opt-in "runtime mode" for direct programmatic access to Jupyter kernels without a browser. That mode was real in the initial `v1.0.0` release but was deleted in a [March 24, 2026 cleanup commit](https://github.com/googlecolab/colab-mcp/pull/55) that dropped `runtime.py`, `client.py`, `auth.py`, and the `-r`/`--enable-runtime` and `-c`/`--client-oauth-config` flags, with the PR description noting the functionality was "coming later elsewhere." As of this audit (August 2026) it has not come back — the current source tree has no runtime/direct-kernel mode at all. Our earlier "two modes" framing was stale; we've corrected it here.

### Key Capabilities

- **Notebook lifecycle management** — [create new .ipynb files, add and structure cells (code + markdown)](https://developers.googleblog.com/announcing-the-colab-mcp-server-connect-any-ai-agent-to-google-colab/), organize analysis workflows
- **Code execution** — [run Python code within the Colab notebook in real time](https://developers.googleblog.com/announcing-the-colab-mcp-server-connect-any-ai-agent-to-google-colab/), using whatever runtime (CPU or GPU) your Colab session is connected to
- **Persistent state** — variables persist across execution steps within the same notebook session, since code runs in the live Colab kernel rather than a fresh sandbox each call
- **Dynamic dependencies** — [agents can run `pip install` commands to configure the environment on the fly](https://developers.googleblog.com/announcing-the-colab-mcp-server-connect-any-ai-agent-to-google-colab/)
- **Visualization** — plots, charts, and other cell outputs render in the notebook the same as any interactive Colab session

## How It Works Under the Hood

The server exposes a single MCP tool at startup: [`open_colab_browser_connection`](https://github.com/googlecolab/colab-mcp/blob/main/src/colab_mcp/session.py). After that connection succeeds, the notebook editing tools (add_cell, run_cell, etc.) are dynamically registered via [`notifications/tools/list_changed`](https://github.com/googlecolab/colab-mcp/blob/main/README.md) — the README states this explicitly as a client requirement. This dynamic registration approach is architecturally interesting — but it's also the server's biggest practical problem (see below).

Per the source, `open_colab_browser_connection` opens a browser URL carrying a one-time `mcpProxyToken` and waits up to [60 seconds](https://github.com/googlecolab/colab-mcp/blob/main/src/colab_mcp/session.py) (`UI_CONNECTION_TIMEOUT = 60.0`) for the browser tab to connect back. The [WebSocket server](https://github.com/googlecolab/colab-mcp/blob/main/src/colab_mcp/websocket_server.py) then enforces bearer-token or URL-parameter authentication, allows only one connected MCP client at a time (enforced via an async connection lock), and accepts WebSocket connections only from `colab.research.google.com` or `colab.google.com`. The server always opens a fresh scratch notebook for this connection rather than attaching to an existing one.

## Setup

The server is installed from GitHub directly (not on PyPI). Per the [current README](https://github.com/googlecolab/colab-mcp/blob/main/README.md) and [entry point](https://github.com/googlecolab/colab-mcp/blob/main/src/colab_mcp/__init__.py), no mode flag is needed — session proxy is on by default and no other mode ships:

```bash
uvx git+https://github.com/googlecolab/colab-mcp
```

For Claude Code:
```bash
claude mcp add-json colab '{"command":"uvx","args":["git+https://github.com/googlecolab/colab-mcp"]}'
```

**Note:** [Python 3.13 or later is required](https://github.com/googlecolab/colab-mcp/blob/main/pyproject.toml). Earlier documentation (including an earlier version of this review) referenced `--session-proxy` and `--runtime` flags; neither exists in the current codebase — the only flags are `-l`/`--log` and `-p`/`--enable-proxy` (already true by default).

## Who This Is For

**ML engineers and data scientists** who use AI coding agents but need GPU compute for their actual work. Instead of context-switching between your IDE and Colab, your agent can push code directly to a GPU-backed notebook.

**Researchers** running experiments who want an AI assistant to help iterate on code without leaving the agent workflow.

**Teams building agent pipelines** that need cloud execution as a step — data processing, model evaluation, batch inference.

## What's Good

**Fills a real gap.** Before this, MCP servers for notebooks were community-built and not backed by a major platform. Google [shipping this officially](https://developers.googleblog.com/announcing-the-colab-mcp-server-connect-any-ai-agent-to-google-colab/) gives it credibility, even if maintenance has since stalled (see below).

**GPU access through MCP.** This is the main differentiator. Most MCP servers interact with APIs or databases. This one gives your agent access to whatever compute [Colab has allocated to your notebook](https://research.google.com/colaboratory/faq.html) — including GPU runtimes, subject to your plan and availability.

**Persistent state.** Because the server drives the live browser session rather than spinning up a fresh sandbox per call, your agent can build up context across multiple execution steps within the same notebook. This enables genuine iterative development, not just one-shot code execution.

**850+ stars, up from 27 at launch.** [The community found this fast.](https://github.com/googlecolab/colab-mcp/stargazers) That growth happened almost entirely in the first six weeks, before development stalled — it signals real demand from ML/data science developers, not just casual interest.

**Open-source.** [Apache-2.0 licensed](https://github.com/googlecolab/colab-mcp/blob/main/LICENSE), hosted under the official `googlecolab` organization.

**Gemini CLI is a first-class client.** [The README explicitly lists Gemini CLI alongside Claude Code and Windsurf](https://github.com/googlecolab/colab-mcp/blob/main/README.md) as clients meeting its requirements, making this cross-ecosystem rather than tied to a single agent platform.

## What's Not

**Development has stopped.** [Three releases in the first 10 days](https://github.com/googlecolab/colab-mcp/releases) (v1.0.0 March 19, v1.0.1 March 27, v1.0.2 March 27), one more docs-only commit on April 1, then nothing — [no commits of any kind for over four months as of this audit](https://github.com/googlecolab/colab-mcp/commits/main/). Worse, a real capability (runtime/direct-kernel mode) was cut five days after launch and never came back (see above). The project reads as a well-intentioned early release that Google hasn't actively resourced since March.

**The #1 UX bug is unresolved.** Many MCP clients — Claude Desktop on Windows, OpenAI Codex — cache the initial tool list at startup and never re-query. Since the notebook editing tools are only registered after `open_colab_browser_connection` succeeds, these clients never see those tools. [Issue #50, opened March 20, remains open](https://github.com/googlecolab/colab-mcp/issues/50) as of this audit. A [community fork (SebastianGilPinzon/colab-mcp)](https://github.com/SebastianGilPinzon/colab-mcp) works around this by pre-registering all tools at startup.

**No headless/remote server mode.** The server opens a browser window by default, which breaks for users running agents on cloud VMs or SSH. [PR #62 (headless mode with a `--port` flag) has been open since March 28](https://github.com/googlecolab/colab-mcp/pull/62) — still unmerged as of this audit, pending a CLA sign-off — and maintainers are explicitly not accepting external contributions due to bandwidth. It's stalled.

**Scratch notebooks only.** The server always opens a new scratch notebook; connecting to an existing notebook is a frequently requested but unimplemented feature.

**Python 3.13 minimum.** [More restrictive than many projects](https://github.com/googlecolab/colab-mcp/blob/main/pyproject.toml) and may block users on slightly older Python installs.

**Browser dependency, no way around it.** Session proxy mode requires a Colab notebook to be open in your browser — and since runtime mode never shipped (see above), there is currently no way to drive the server without a browser tab open. This rules out fully headless automation.

**Colab's own limitations apply.** [Free Colab notebooks run for at most 12 hours depending on availability, GPU/TPU types vary over time, and idle sessions time out](https://research.google.com/colaboratory/faq.html). Your agent inherits all of these constraints.

**Not on PulseMCP.** Despite 850+ stars, [a search of PulseMCP's directory (22,000+ servers, updated daily) for "googlecolab" returns zero results](https://www.pulsemcp.com/servers) as of this audit, which reduces discoverability for users browsing the broader MCP ecosystem.

## The Bottom Line

The Google Colab MCP server is the right idea and it found a real audience fast. The [star growth since launch](https://github.com/googlecolab/colab-mcp/stargazers) (27 → 850+) isn't noise — ML and data science developers genuinely want this capability. The session-proxy architecture is a reasonable v1 — but it's also the *only* mode that ships; the more powerful direct-kernel "runtime mode" that early coverage (including our own initial review) described was [removed from the codebase five days after launch](https://github.com/googlecolab/colab-mcp/pull/55) and hasn't returned.

The project has now gone [over four months without a single commit](https://github.com/googlecolab/colab-mcp/commits/main/). The biggest usability bug (dynamic tool registration failing in major clients) [sits unresolved](https://github.com/googlecolab/colab-mcp/issues/50). The headless mode PR is [stalled](https://github.com/googlecolab/colab-mcp/pull/62) with no response from maintainers. Google open-sourced this in a burst of activity in March and hasn't returned to it since.

If you're comfortable with the rough edges and primarily use session proxy mode in Gemini CLI or Claude Code, it may work well. If you're on Windows with Claude Desktop, or need to run agents on a remote server, you'll likely hit the known blockers. The [community fork SebastianGilPinzon/colab-mcp](https://github.com/SebastianGilPinzon/colab-mcp) addresses some of these — but it's unofficial.

Check back if Google resumes active development. The foundation is solid; it just needs maintenance commitment — and, ideally, a real second mode.

**Rating: 3.5 / 5** — Strong concept backed by Google, genuine utility for ML/data science workflows, and real community demand (850+ stars, up from 27 at launch). No commits since April 1, 2026, top UX bug unresolved, headless mode stalled, and the launch-era "runtime mode" was quietly cut. The gap it fills is real; the execution needs a recommitment from Google.

---

*This review is researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on official documentation, source code, community feedback, and ecosystem data. [Rob Nugen](https://robnugen.com) owns and operates ChatForest.*
