# Google Colab CLI: Your Agents Can Now Provision A100s and H100s From the Terminal

> Google's new Colab CLI removes the browser requirement from Colab GPU/TPU access. Any agent with terminal access — Claude Code, Antigravity, Codex — can now provision T4 through H100 and TPU v5e1/v6e1 compute, execute scripts remotely, and retrieve results without a Jupyter kernel in sight.


Google shipped [the Colab CLI on June 5, 2026](https://developers.googleblog.com/introducing-the-google-colab-cli/). It is an open source command-line tool that gives you — and your agents — direct access to Colab GPU and TPU runtimes from any terminal, with no browser, no Jupyter notebook, and no kernel management required.

This is a meaningful change for builders running ML workloads on Colab. It's not Colab's first agent-oriented interface, either — Google shipped a [Colab MCP server in March 2026](https://developers.googleblog.com/announcing-the-colab-mcp-server-connect-any-ai-agent-to-google-colab/) that gives MCP-compatible agents structured, protocol-based access to the same runtimes. The CLI adds a second, shell-native path to the same compute.

---

## What Changed

Before the CLI, using Colab GPU compute required a browser session. You opened a notebook, attached a runtime, ran cells in order, and downloaded outputs manually. That worked for interactive development but did not compose well with pipelines, scripts, or autonomous agents.

The Colab CLI changes the access model: you install a lightweight CLI, authenticate once, and from that point on Colab GPU runtimes are addressable with shell commands. Any tool that can run a shell command — scripts, Makefiles, CI runners, or AI agents — can now use Colab compute.

---

## Hardware Available

The CLI's own documentation lists the accelerators you can request with the `--gpu` and `--tpu` flags: **T4, L4, G4, H100, and A100** GPUs, plus **TPU v5e1 and v6e1** — the same pool the web interface draws from ([GitHub README](https://github.com/googlecolab/google-colab-cli)).

Google does not publish a fixed table mapping each accelerator to a specific subscription tier. Its own Colaboratory FAQ says GPU/TPU availability "vary[ies] over time" and that premium GPUs are available "subject to availability" to paid-plan subscribers ([Colab FAQ](https://research.google.com/colaboratory/faq.html)) — it deliberately declines to guarantee that a given tier gets a given chip. In practice, T4 is the accelerator free-tier users can expect; A100, H100, and TPU access are effectively gated behind a paid plan, but which chip you actually get on any given run depends on real-time capacity, not a fixed entitlement. There is no CLI-specific pricing — the CLI is open source under Apache-2.0, and accelerator access is billed the same compute-unit way it always has been.

---

## Key Commands

Command syntax below is taken directly from the [project README](https://github.com/googlecolab/google-colab-cli):

```bash
# Provision a new named session
colab new -s trainer --gpu A100

# List running sessions
colab sessions

# Execute a local script on a named session's remote hardware
colab exec -s trainer -f train.py

# Or provision-and-run a script on fresh hardware in one shot
colab run --gpu T4 train.py

# Interactive REPL / shell on the remote runtime
colab repl
colab console

# Install packages on a named session
colab install -s trainer torch transformers

# Retrieve outputs
colab download -s trainer checkpoints/model.bin ./model.bin

# Tail the execution log
colab log -s trainer -o execution_log.md

# Terminate a named session
colab stop -s trainer
```

The `colab exec` and `colab run` commands do what Colab notebooks do when you click Run All — execute Python on the remote runtime — without requiring a notebook structure. Local scripts run on the remote hardware and results come back to your local environment. Most subcommands take a `-s`/`--session` name so you can address a specific running runtime.

---

## The Agent Angle: COLAB_SKILL.md

This is the part that distinguishes the Colab CLI from a standard developer tool.

The CLI repository ships with a file called `COLAB_SKILL.md`. This is a prepackaged context document written specifically for AI agents. When an agent (Claude Code, Antigravity, Codex, or any other agent with file and terminal access) reads this file, it gets structured guidance on how to use the CLI — what commands are available, what the outputs look like, and how to handle common workflows.

Google's own [launch post](https://developers.googleblog.com/introducing-the-google-colab-cli/) walks through an example using its Antigravity agent platform, and notes the CLI "can easily be used by Claude Code, Codex, and other agents" with terminal access — a compatibility claim, not a report of Google having formally tested every agent. [MarkTechPost's launch coverage](https://www.marktechpost.com/2026/06/06/googles-new-colab-cli-lets-developers-and-ai-agents-run-python-on-remote-colab-gpus-and-tpus-from-the-terminal/) covers the same example. An agent can:

1. Read `COLAB_SKILL.md` once as context
2. Provision a GPU runtime (`colab new -s trainer --gpu A100`)
3. Execute a script (`colab exec -s trainer -f fine_tune.py`)
4. Monitor progress through logs (`colab log -s trainer`)
5. Download results (`colab download -s trainer checkpoints/model.bin ./model.bin`)
6. Terminate the session (`colab stop -s trainer`)

No human required in the loop. The agent handles the entire lifecycle.

This makes Colab a plausible compute layer for agentic ML workflows that were previously impractical without a cloud account, Kubernetes cluster, or expensive managed service.

---

## Colab CLI vs. Colab MCP Server

Google also shipped a [Colab MCP server on March 17, 2026](https://developers.googleblog.com/announcing-the-colab-mcp-server-connect-any-ai-agent-to-google-colab/) that provides structured protocol-based access to Colab runtimes via Model Context Protocol. These are two separate tools solving the same problem at different layers:

| | Colab MCP Server | Colab CLI |
|---|---|---|
| Protocol | MCP (structured tool calls) | Shell commands |
| Agent requirement | MCP-compatible host | Terminal access |
| Integration pattern | Tool use in MCP workflow | Script or agent shell call |
| When to use | MCP-native agent stacks | Universal: any script, CI, or agent |

For MCP-native stacks (Claude, Gemini, any host supporting MCP), the MCP server gives you tighter integration with tool call semantics. For everything else — shell scripts, CI/CD pipelines, Makefile orchestration, or agents that work via terminal — the CLI is simpler and more portable.

---

## Builder Implications

**Fine-tuning and evaluation pipelines.** If you have a fine-tuning script that normally requires a cloud GPU instance, you can now run it via `colab exec -s trainer -f fine_tune.py` from a local machine or a CI runner. The hardware cost is covered by your Colab subscription rather than a separate GPU cloud bill.

**Long-running jobs without browser babysitting.** Colab's browser-based approach historically timed out if you left the tab idle. The CLI runs jobs as headless remote processes. Session-length ceilings still apply per plan: Google's own FAQ puts the free tier at up to 12 hours of continuous execution, versus up to 24 hours for Colab Pro+ ([Colab FAQ](https://research.google.com/colaboratory/faq.html)).

**Agent-triggered compute.** If you are building an agentic system that needs to train, evaluate, or run inference on demand, the CLI makes Colab a callable compute resource. An agent that hits a model performance threshold can autonomously trigger a fine-tuning job on an A100 and retrieve updated weights.

**CI/CD integration.** `colab run` and `colab exec` are shell commands, so they can be called from GitHub Actions, GitLab CI, or any CI runner the same way any other CLI tool would be — no notebook export step or browser automation workaround required.

---

## What to Watch

The CLI is versioned separately from the Colab web product. The GitHub repository is at `github.com/googlecolab/google-colab-cli` and is accepting contributions under Apache-2.0.

Free tier constraints apply the same way they do in the browser — don't expect uninterrupted A100 access on a free plan. The CLI does not unlock hardware that your subscription plan does not cover.

Availability is also subject to Colab's capacity pool, which varies. The CLI does not give you priority over the browser when hardware is constrained.

---

*The Google Colab CLI is open source under Apache-2.0 and available at [github.com/googlecolab/google-colab-cli](https://github.com/googlecolab/google-colab-cli). Colab Pro is priced at $9.99/month and Pro+ at $49.99/month ([Colab Pro/Pro+ overview, NC State Office of Information Technology](https://software.ncsu.edu/google-colab-pro-colab-pro)); check [Colab's own signup page](https://colab.research.google.com/signup) for current pricing.*

