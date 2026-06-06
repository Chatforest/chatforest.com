---
title: "Google Colab CLI: Your Agents Can Now Provision A100s and H100s From the Terminal"
date: 2026-06-07
description: "Google's new Colab CLI removes the browser requirement from Colab GPU/TPU access. Any agent with terminal access — Claude Code, Antigravity, Codex — can now provision T4 through H100 and TPU v5e/v6e compute, execute scripts remotely, and retrieve results without a Jupyter kernel in sight."
og_description: "Colab GPU access no longer requires a browser. The new Google Colab CLI lets builders and AI agents provision T4, A100, and H100 compute directly from the terminal. COLAB_SKILL.md gives Claude Code and Antigravity native context to use it autonomously."
content_type: "Builder's Log"
categories: ["Google", "Infrastructure", "AI Agents", "Developer Tools"]
tags: ["google-colab", "colab-cli", "gpu", "tpu", "terminal", "ai-agents", "claude-code", "antigravity", "codex", "ml-infrastructure", "builder-guide", "open-source", "h100", "a100"]
---

Google shipped the Colab CLI on June 5, 2026. It is an open source command-line tool that gives you — and your agents — direct access to Colab GPU and TPU runtimes from any terminal, with no browser, no Jupyter notebook, and no kernel management required.

This is a meaningful change for builders running ML workloads on Colab. It is also the first time Colab has shipped a first-party interface designed explicitly for agent use.

---

## What Changed

Before the CLI, using Colab GPU compute required a browser session. You opened a notebook, attached a runtime, ran cells in order, and downloaded outputs manually. That worked for interactive development but did not compose well with pipelines, scripts, or autonomous agents.

The Colab CLI changes the access model: you install a lightweight CLI, authenticate once, and from that point on Colab GPU runtimes are addressable with shell commands. Any tool that can run a shell command — scripts, Makefiles, CI runners, or AI agents — can now use Colab compute.

---

## Hardware Available

The CLI gives access to the same accelerator pool as the Colab web interface. What you can actually provision depends on your subscription tier:

| Hardware | Free Plan | Colab Pro/Pro+ |
|----------|-----------|----------------|
| T4 GPU | Limited access | ✓ |
| L4 GPU | — | ✓ |
| A100 GPU | — | ✓ |
| H100 GPU | — | ✓ |
| TPU v5e | — | ✓ |
| TPU v6e | — | ✓ |

Free plan users get the same constrained T4 access they would get through the browser. Pro and Pro+ subscribers unlock the full stack. There is no CLI-specific pricing — the CLI is open source under Apache-2.0 and costs nothing; accelerator access is billed the same way it has always been.

---

## Key Commands

```bash
# Provision a new runtime
colab new --gpu T4
colab new --gpu A100

# Shorthand provisioning
colab --gpu A100

# Execute a local script on remote hardware
colab exec train.py
colab run pipeline.py

# Interactive REPL on the remote runtime
colab repl
colab console

# Install packages on the runtime
colab install torch torchvision

# Retrieve outputs
colab download results/
colab log

# Terminate the runtime
colab stop
```

The `colab exec` and `colab run` commands do what Colab notebooks do when you click Run All — execute Python on the remote runtime — without requiring a notebook structure. Local scripts run as-is on the remote hardware and results come back to your local environment.

---

## The Agent Angle: COLAB_SKILL.md

This is the part that distinguishes the Colab CLI from a standard developer tool.

The CLI repository ships with a file called `COLAB_SKILL.md`. This is a prepackaged context document written specifically for AI agents. When an agent (Claude Code, Antigravity, Codex, or any other agent with file and terminal access) reads this file, it gets structured guidance on how to use the CLI — what commands are available, what the outputs look like, and how to handle common workflows.

Google explicitly tested the CLI with Antigravity (their own agentic platform) and Claude Code. An agent can:

1. Read `COLAB_SKILL.md` once as context
2. Provision a GPU runtime (`colab new --gpu A100`)
3. Execute a script (`colab exec fine_tune.py`)
4. Monitor progress through logs (`colab log`)
5. Download results (`colab download checkpoints/`)
6. Terminate the session (`colab stop`)

No human required in the loop. The agent handles the entire lifecycle.

This makes Colab a plausible compute layer for agentic ML workflows that were previously impractical without a cloud account, Kubernetes cluster, or expensive managed service.

---

## Colab CLI vs. Colab MCP Server

Google also shipped a Colab MCP server in March 2026 that provides structured protocol-based access to Colab runtimes via Model Context Protocol. These are two separate tools solving the same problem at different layers:

| | Colab MCP Server | Colab CLI |
|---|---|---|
| Protocol | MCP (structured tool calls) | Shell commands |
| Agent requirement | MCP-compatible host | Terminal access |
| Integration pattern | Tool use in MCP workflow | Script or agent shell call |
| When to use | MCP-native agent stacks | Universal: any script, CI, or agent |

For MCP-native stacks (Claude, Gemini, any host supporting MCP), the MCP server gives you tighter integration with tool call semantics. For everything else — shell scripts, CI/CD pipelines, Makefile orchestration, or agents that work via terminal — the CLI is simpler and more portable.

---

## Builder Implications

**Fine-tuning and evaluation pipelines.** If you have a fine-tuning script that normally requires a cloud GPU instance, you can now run it via `colab exec fine_tune.py` from a local machine or a CI runner. The hardware cost is covered by your Colab subscription rather than a separate GPU cloud bill.

**Long-running jobs without browser babysitting.** Colab's browser-based approach historically timed out if you left the tab idle. The CLI runs jobs as headless remote processes, removing that constraint for Pro+ subscribers who have extended session access.

**Agent-triggered compute.** If you are building an agentic system that needs to train, evaluate, or run inference on demand, the CLI makes Colab a callable compute resource. An agent that hits a model performance threshold can autonomously trigger a fine-tuning job on an A100 and retrieve updated weights.

**CI/CD integration.** `colab exec` can be called from GitHub Actions, GitLab CI, or any CI runner. This is the first time Colab has been composable with standard CI tooling without third-party workarounds.

---

## What to Watch

The CLI is versioned separately from the Colab web product. The GitHub repository is at `github.com/googlecolab/google-colab-cli` and is accepting contributions under Apache-2.0.

Free tier constraints apply the same way they do in the browser — don't expect uninterrupted A100 access on a free plan. The CLI does not unlock hardware that your subscription plan does not cover.

Availability is also subject to Colab's capacity pool, which varies. The CLI does not give you priority over the browser when hardware is constrained.

---

*The Google Colab CLI is open source under Apache-2.0 and available at github.com/googlecolab/google-colab-cli. Colab Pro starts at $9.99/month; Pro+ at $49.99/month.*
