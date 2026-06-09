---
title: "OpenCode: The Model-Agnostic Coding Agent That Overtook Claude Code on GitHub Stars"
date: 2026-06-10
description: "OpenCode hit 160K+ GitHub stars and 7.5M monthly active developers in under a year — outpacing every AI coding agent in GitHub history. The reason: it works with 75+ LLM providers, runs natively in the terminal, and costs nothing if you bring your own API key. Here is what builders need to know."
content_type: "Builder's Log"
categories: ["Developer Tools", "AI Coding Agents", "Open Source", "Terminal Tools", "Model Agnostic"]
tags: ["opencode", "coding-agent", "terminal", "model-agnostic", "open-source", "anomaly-innovations", "sst", "claude-code-alternative", "cursor-alternative", "byok", "builder-tools"]
---

On June 19, 2025, Anomaly Innovations — the team behind the open-source AWS framework SST — quietly released [OpenCode](https://opencode.ai/), a terminal-native AI coding agent built to work with any LLM. By May 2026, it had surpassed 160,000 GitHub stars and 7.5 million monthly active developers. No other AI coding agent has grown that fast.

A year in, OpenCode has a v1.16.0 release (June 5, 2026), 900+ contributors, and 13,000+ commits. For builders trying to understand the AI coding tool landscape, it has become impossible to ignore.

---

## What Makes It Different

Most AI coding agents are bound to a specific model or IDE:

- **Claude Code** requires an Anthropic subscription and only uses Claude models.
- **Cursor** is a VS Code fork — its AI features exist inside that editor.
- **GitHub Copilot** is an IDE extension with inline completions, not an autonomous agent.

OpenCode was designed around a different premise: the AI model is a pluggable dependency, not the product. The same agent works with Claude, GPT-5, Gemini 2.5, Grok, AWS Bedrock, Azure OpenAI, or a locally-hosted model via Ollama — all configured through a single `opencode.jsonc` file. Seventy-five providers are supported.

This matters for a few different reasons depending on your situation:

- **Budget control:** Switch to the cheapest model that handles a given task without changing your workflow.
- **Compliance:** Run entirely locally with Ollama for air-gapped or privacy-sensitive environments.
- **Resilience:** If one provider has an outage or changes pricing, you switch the config, not your tooling.

---

## The January 2026 Acceleration

OpenCode had steady growth through fall 2025, but it hit a second gear in January 2026 when Anthropic deployed server-side OAuth checks that blocked third-party tools — including OpenCode, Cline, and RooCode — from authenticating against Claude Pro and Max subscriptions. Developers who'd been using those tools to access Claude via their existing subscriptions suddenly needed alternatives.

OpenCode gained 18,000 stars in two weeks during that period. The irony was complete: Anthropic's attempt to protect Claude Code's market position helped make OpenCode the most-starred open-source coding agent in GitHub history.

That incident also clarified a real risk for builders: tools tied to a single provider's authentication model are exposed to that provider's policy decisions. OpenCode's model-agnostic architecture is not just a feature — it's insurance.

---

## Architecture and Interfaces

OpenCode is a Go CLI application using [Bubble Tea](https://github.com/charmbracelet/bubbletea) for its terminal UI. Sessions are stored in SQLite. The codebase is MIT-licensed.

**Interfaces available:**

| Mode | How to launch | Use case |
|------|-------------|----------|
| Terminal TUI | `opencode` | Interactive development sessions |
| Single prompt | `opencode -p "prompt" -f json` | Scripting, CI pipelines |
| Non-interactive | `opencode run "..."` | Automation |
| Headless HTTP | `opencode serve` | Integration with other tools |
| Web UI | `opencode web` | Browser access to headless server |
| Desktop app | Separate download | GUI preference |

The terminal TUI is the primary interface. It supports Language Server Protocol (LSP) integration, Plan Mode (preview changes before applying them), undo/redo across conversation steps and file edits, external editor support for composing prompts, and session sharing via link.

---

## Getting Started

**Install:**
```bash
curl -fsSL https://opencode.ai/install | bash
```

Alternative methods exist via npm (`npm install -g opencode-ai`), Homebrew, Arch pacman, or direct binary download.

**Configure providers:**

Run `opencode` to launch the TUI, then use `/connect` to add your LLM provider credentials. For a file-based setup, create `opencode.jsonc` in your project root:

```json
{
  "default_model": "anthropic/claude-sonnet-4-6",
  "small_model": "anthropic/claude-haiku-4-5",
  "providers": {
    "anthropic": {
      "api_key": "your-key-here"
    }
  }
}
```

**Initialize a project:**

```bash
opencode
# then inside the TUI:
/init
```

The `/init` command analyzes your codebase and generates an `AGENTS.md` file documenting the project structure. This is OpenCode's version of priming context — subsequent sessions use this file to orient the model without re-analyzing from scratch.

**Useful commands inside the TUI:**
- `/models` — list all available models from configured providers
- `/undo` / `/redo` — roll back or forward conversation steps and file edits
- `/share` — generate a shareable link to the current session
- `/help` — full command reference

---

## What v1.16.0 Added (June 5, 2026)

The most recent release introduced several workflow improvements relevant to teams:

- **Managed workspace cloning** that preserves dirty and untracked files — useful for running OpenCode sessions against feature branches without disrupting your working tree
- **Session mobility** between workspaces and directories, so you can pick up a session in a different context
- **AWS Bedrock OpenAI model support** expansion — more Bedrock-hosted models now available
- **Skill discovery and file-based agent loading** — similar to Claude Code's skill system, agents can now be loaded from files
- **GitHub Copilot usage tracking** for token-based billing visibility
- **`/run --replay`** for interactive session replay
- Significant **startup time improvements** across TUI and desktop

---

## Pricing

| Tier | Cost | What you pay for AI |
|------|------|---------------------|
| **Free (BYOK)** | $0 to OpenCode | Your own API costs directly to provider |
| **Go Plan** | $5 first month, $10/month after | Managed access to curated open-source models |
| **Zen Plan** | $20/month + pay-per-use | Optimized managed models, simplest setup |

The free tier is genuinely free. You bring your own API keys, connect them in the config, and pay your providers directly. OpenCode charges nothing for the software itself in this mode.

This makes OpenCode one of the cheapest entry points in the space. By comparison, Claude Code requires a Claude Pro subscription at $20/month, and Cursor Pro is also $20/month.

---

## Privacy: Read the Fine Print on Zen

OpenCode markets itself as privacy-respecting, but the specifics depend on which mode you use.

**With your own API keys (BYOK):** Your prompts and code go directly to your provider's API — OpenAI, Anthropic, etc. Nothing touches OpenCode's infrastructure. For fully local execution, Ollama support lets you run models entirely on your own hardware.

**With OpenCode's Zen service (the managed tier):** User prompts and AI responses are persisted to Cloudflare R2 storage. This has been documented and flagged by community members (see the linked GitHub issue). There is no documented opt-out mechanism.

For builders working on proprietary code, the answer is simple: use BYOK or Ollama. The free tier exists exactly for this use case.

---

## Comparison: OpenCode vs Claude Code vs Cursor

| | **OpenCode** | **Claude Code** | **Cursor** |
|---|---|---|---|
| **Model support** | 75+ providers | Anthropic only | Multi-model (Cursor-hosted) |
| **Interface** | Terminal-first, TUI | Terminal TUI | IDE (VS Code fork) |
| **License** | MIT (open source) | Proprietary | Proprietary |
| **Pricing** | Free (BYOK) | Requires Claude Pro ($20/mo) | $20/mo Pro |
| **Local execution** | Yes (Ollama) | No | No |
| **Vendor lock-in** | None | Anthropic | Cursor/cloud |
| **GitHub stars** | 160K+ | Not open source | Not open source |

A February 2026 survey of 15,000 developers found that 70% use two to four AI coding tools simultaneously. The tools are not mutually exclusive — OpenCode as a model-agnostic layer alongside Claude Code for Anthropic-specific workflows is a pattern that appears frequently in community discussion.

---

## Who Should Use OpenCode

**Strong fit:**
- Teams that need provider flexibility or want to hedge against pricing/availability changes
- Privacy-sensitive work where local execution (Ollama) is required
- Developers who want to avoid a $20/month subscription to evaluate AI coding tools
- Multi-model workflows where different tasks use different models
- Open-source projects and contributors who want auditable tooling

**Less obvious fit:**
- Developers deeply invested in a specific IDE who prefer inline completions over a separate terminal agent
- Teams already committed to Claude and wanting the tightest possible Anthropic integration

---

## The Bigger Signal

OpenCode overtaking Claude Code on GitHub stars is not just a metric. It reflects a genuine architectural split in how the developer community thinks about AI coding tools. One camp believes the model matters most — build around the best model and optimize from there. The other camp believes the workflow layer should be model-independent, with models as interchangeable components.

OpenCode is betting the second camp is right, and the star growth suggests a lot of developers agree.

Whether that bet holds as model quality continues to diverge between providers is a question worth watching. For now, the project is actively maintained, growing, and shipping — and the model-agnostic architecture remains its clearest differentiator.

---

*OpenCode is maintained by Anomaly Innovations (Jay V and Frank Wang, founders of SST/Serverless Stack). Repository: [github.com/opencode-ai/opencode](https://github.com/opencode-ai/opencode). Official docs: [opencode.ai/docs](https://opencode.ai/docs/).*
