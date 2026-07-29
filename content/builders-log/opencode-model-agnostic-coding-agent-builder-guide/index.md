---
title: "OpenCode: The Model-Agnostic Coding Agent That Overtook Claude Code on GitHub Stars"
date: 2026-06-10
description: "OpenCode hit 160K+ GitHub stars and 7.5M monthly active developers in under a year — outpacing every AI coding agent in GitHub history. The reason: it works with 75+ LLM providers, runs natively in the terminal, and costs nothing if you bring your own API key. Here is what builders need to know."
content_type: "Builder's Log"
categories: ["Developer Tools", "AI Coding Agents", "Open Source", "Terminal Tools", "Model Agnostic"]
tags: ["opencode", "coding-agent", "terminal", "model-agnostic", "open-source", "anomaly-innovations", "sst", "claude-code-alternative", "cursor-alternative", "byok", "builder-tools"]
sources_audited: 2026-07-30
---

On June 19, 2025, [Anomaly Innovations](https://www.ycombinator.com/companies/opencode) — founded by Jay V and Frank Wang, who also built the open-source AWS framework [SST](https://github.com/sst/sst) — released [OpenCode](https://opencode.ai/), a terminal-native AI coding agent built to work with any LLM. As of its own reported statistics, it has [surpassed 160,000 GitHub stars and 7.5 million monthly active developers](https://opencode.ai/) — among the fastest star-growth trajectories of any AI coding agent on GitHub.

A year in, OpenCode has a [v1.16.0 release](https://github.com/anomalyco/opencode/releases/tag/v1.16.0) (June 5, 2026) and, per its own published stats, [900+ contributors and 13,000+ commits](https://opencode.ai/). For builders trying to understand the AI coding tool landscape, it has become impossible to ignore.

---

## What Makes It Different

Most AI coding agents are bound to a specific model or IDE:

- **Claude Code** [requires a paid Anthropic plan](https://claude.com/pricing) and connects only to Anthropic's own Claude models.
- **Cursor** is [a fork of VS Code's open-source codebase](https://www.datacamp.com/blog/cursor-vs-vs-code) — its AI features are built into that editor.
- **GitHub Copilot** began as an inline-completion IDE extension, though GitHub has since added a [cloud-based autonomous coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent) that can plan and execute multi-step tasks from a GitHub issue — it remains tied to GitHub/VS Code rather than a standalone terminal tool.

OpenCode was designed around a different premise: the AI model is a pluggable dependency, not the product. The same agent works with Claude, GPT-5, Gemini 2.5, Grok, AWS Bedrock, Azure OpenAI, or a locally-hosted model via Ollama — all configured through a single `opencode.jsonc` file. OpenCode reports [75+ supported providers](https://opencode.ai/docs/providers/) through the AI SDK and Models.dev.

This matters for a few different reasons depending on your situation:

- **Budget control:** Switch to the cheapest model that handles a given task without changing your workflow.
- **Compliance:** Run entirely locally with Ollama for air-gapped or privacy-sensitive environments.
- **Resilience:** If one provider has an outage or changes pricing, you switch the config, not your tooling.

---

## The January 2026 Acceleration

OpenCode had steady growth through fall 2025, but it hit a second gear in January 2026 when [Anthropic deployed server-side checks](https://winbuzzer.com/2026/02/19/anthropic-bans-claude-subscription-oauth-in-third-party-apps-xcxwbn/) — enforced starting January 9, 2026 — that blocked third-party tools, including OpenCode, Cline, and RooCode, from authenticating against Claude Pro and Max subscriptions. [Anthropic later formalized the restriction](https://alternativeto.net/news/2026/2/anthropic-officially-bans-using-subscription-authentication-for-third-party-claude-use) in its terms, stating that OAuth tokens from Free, Pro, and Max plans may not be used with third-party tools or the Agent SDK. Developers who'd been using those tools to access Claude via their existing subscriptions suddenly needed alternatives.

OpenCode's [GitHub star count](https://github.com/anomalyco/opencode) accelerated sharply in the weeks that followed — reported figures for the exact size of that spike vary across secondary sources, so no single number is repeated here. What's well documented is the direction: the incident is widely cited by tech press as a turning point in OpenCode's growth relative to other open-source coding agents.

That incident also clarified a real risk for builders: tools tied to a single provider's authentication model are exposed to that provider's policy decisions. OpenCode's model-agnostic architecture is not just a feature — it's insurance.

---

## Architecture and Interfaces

OpenCode is a [Go CLI application](https://github.com/anomalyco/opencode) using [Bubble Tea](https://github.com/charmbracelet/bubbletea) for its terminal UI, with sessions stored in [SQLite](https://github.com/anomalyco/opencode/issues/13202). The codebase is [MIT-licensed](https://github.com/anomalyco/opencode).

**Interfaces available** ([per the CLI docs](https://opencode.ai/docs/cli/)):

| Mode | How to launch | Use case |
|------|-------------|----------|
| Terminal TUI | `opencode` | Interactive development sessions |
| Single prompt | `opencode run --format json "prompt"` | Scripting, CI pipelines |
| Non-interactive | `opencode run "..."` | Automation |
| Headless HTTP | `opencode serve` | Integration with other tools |
| Web UI | `opencode web` | Browser access to headless server |
| Desktop app | Separate download | GUI preference |

The terminal TUI is the primary interface. [It supports](https://opencode.ai/docs/) Language Server Protocol (LSP) integration, Plan Mode (preview changes before applying them), undo/redo across conversation steps and file edits, external editor support for composing prompts, and session sharing via link.

---

## Getting Started

**Install:**
```bash
curl -fsSL https://opencode.ai/install | bash
```

[Alternative methods](https://opencode.ai/docs/) exist via npm (`npm install -g opencode-ai`), Homebrew (`brew install anomalyco/tap/opencode`), Arch pacman (`sudo pacman -S opencode`), or direct binary download from GitHub Releases.

**Configure providers:**

Run `opencode` to launch the TUI, then use `/connect` to add your LLM provider credentials. For a file-based setup, create `opencode.jsonc` in your project root — [per the official config docs](https://opencode.ai/docs/config/), model selection uses a `model` (and optional `small_model`) key, not a `default_model` key:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-5",
  "small_model": "anthropic/claude-haiku-4-5",
  "provider": {
    "anthropic": {
      "options": {
        "apiKey": "your-key-here"
      }
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

The [`/init` command](https://opencode.ai/docs/) analyzes your codebase and generates an `AGENTS.md` file documenting the project structure. This is OpenCode's version of priming context — subsequent sessions use this file to orient the model without re-analyzing from scratch.

**Useful commands inside the TUI** ([docs](https://opencode.ai/docs/)):
- `/models` — list all available models from configured providers
- `/undo` / `/redo` — roll back or forward conversation steps and file edits
- `/share` — generate a shareable link to the current session
- `/help` — full command reference

---

## What v1.16.0 Added (June 5, 2026)

The [most recent release](https://github.com/anomalyco/opencode/releases/tag/v1.16.0) introduced several workflow improvements relevant to teams:

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
| **[Go Plan](https://opencode.ai/docs/go/)** | $5 first month, $10/month after | Managed access to curated open-source models |
| **[Zen Plan](https://opencode.ai/docs/zen/)** | Pay-as-you-go credits (auto-reloads $20 when balance drops below $5), no markup | Frontier models (Claude, GPT, Gemini) at provider cost |

The free tier is genuinely free. You bring your own API keys, connect them in the config, and pay your providers directly. OpenCode charges nothing for the software itself in this mode.

This makes OpenCode one of the cheapest entry points in the space. By comparison, [Claude Code requires a Claude Pro subscription at $20/month](https://claude.com/pricing), and [Cursor Pro is also $20/month](https://cursor.com/pricing).

---

## Privacy: Read the Fine Print on Zen

OpenCode markets itself as privacy-respecting, but the specifics depend on which mode you use.

**With your own API keys (BYOK):** Your prompts and code go directly to your provider's API — OpenAI, Anthropic, etc. Nothing touches OpenCode's infrastructure. For fully local execution, Ollama support lets you run models entirely on your own hardware.

**With OpenCode's Zen service (the managed tier):** User prompts and AI responses are persisted to Cloudflare R2 storage. This was documented and flagged by a community member in [a GitHub issue on the opencode repo](https://github.com/anomalyco/opencode/issues/14281), which states that "all user prompts and complete AI responses are persisted to a Cloudflare R2 bucket — with no opt-out mechanism and no documentation informing users about this" when using the opencode.ai-hosted Zen provider. That issue notes the behavior is specific to routing through Zen; direct provider API keys bypass it.

For builders working on proprietary code, the answer is simple: use BYOK or Ollama. The free tier exists exactly for this use case.

---

## Comparison: OpenCode vs Claude Code vs Cursor

| | **OpenCode** | **Claude Code** | **Cursor** |
|---|---|---|---|
| **Model support** | [75+ providers](https://opencode.ai/docs/providers/) | Anthropic only | Multi-model (Cursor-hosted) |
| **Interface** | Terminal-first, TUI | Terminal TUI | IDE (VS Code fork) |
| **License** | [MIT (open source)](https://github.com/anomalyco/opencode) | [Proprietary; repo is docs/distribution only, code is closed-source](https://github.com/anthropics/claude-code) | Proprietary |
| **Pricing** | Free (BYOK) | [Requires Claude Pro ($20/mo)](https://claude.com/pricing) | [$20/mo Pro](https://cursor.com/pricing) |
| **Local execution** | Yes (Ollama) | No | No |
| **Vendor lock-in** | None | Anthropic | Cursor/cloud |
| **GitHub stars** | [160K+](https://opencode.ai/) | [Its closed-source repo also carries a large public star count](https://github.com/anthropics/claude-code) (not the same as being open source) | Not open source, no public star count |

A [February 2026 survey of 15,000 developers](https://newsletter.pragmaticengineer.com/p/ai-tooling-2026) found that 70% use two to four AI coding tools simultaneously. The tools are not mutually exclusive — OpenCode as a model-agnostic layer alongside Claude Code for Anthropic-specific workflows is a pattern that appears frequently in community discussion.

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

OpenCode's star count overtaking that of [Claude Code's public repository](https://github.com/anthropics/claude-code) — even though that repo is closed-source distribution/issue-tracking rather than the actual codebase — is not just a metric. It reflects a genuine architectural split in how the developer community thinks about AI coding tools. One camp believes the model matters most — build around the best model and optimize from there. The other camp believes the workflow layer should be model-independent, with models as interchangeable components.

OpenCode is betting the second camp is right, and the star growth suggests a lot of developers agree.

Whether that bet holds as model quality continues to diverge between providers is a question worth watching. For now, the project is actively maintained, growing, and shipping — and the model-agnostic architecture remains its clearest differentiator.

---

*OpenCode is maintained by [Anomaly Innovations](https://www.ycombinator.com/companies/opencode) (Jay V and Frank Wang, founders of SST/Serverless Stack). Repository: [github.com/anomalyco/opencode](https://github.com/anomalyco/opencode) — note this is the currently active project; the similarly-named `opencode-ai/opencode` repo on GitHub is an unrelated, now-archived predecessor project that continued separately as [Crush](https://github.com/charmbracelet/crush). Official docs: [opencode.ai/docs](https://opencode.ai/docs/).*
