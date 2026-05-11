# Dagger container-use — Isolated Containers for Coding Agents

> Dagger container-use reviewed: an open-source MCP server that gives each coding agent its own isolated container and git branch, enabling safe parallel agent execution with full visibility. Apache-2.0. Rating: 4.0/5.


The standard advice for AI coding agents is to give them one task, in one codebase, with one thread of execution. Run a second agent on the same repository and you get file conflicts, dependency chaos, and outputs that are neither agent's fault. The workaround — run agents sequentially, one at a time — throws away most of the speed advantage agents are supposed to provide.

[Dagger container-use](https://github.com/dagger/container-use) is an open-source MCP server that removes the constraint. It gives each coding agent an isolated container and a dedicated git branch, so multiple agents can work in the same repository simultaneously without any awareness of each other. When they finish, you review their work the way you review any branch — with `git diff`, `git log`, or a pull request — and decide what to merge.

At **3.8K GitHub stars**, built by the team that created Docker, and with native integration into Claude Code, it is one of the more credible infrastructure pieces in the agent tooling space. Part of our **[Developer Tools MCP category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Repo** | [dagger/container-use](https://github.com/dagger/container-use) |
| **Stars** | ~3,800 |
| **License** | Apache-2.0 |
| **Language** | Go |
| **Latest version** | v0.4.2 |
| **Install (macOS)** | `brew install dagger/tap/container-use` |
| **Install (all)** | `curl -fsSL https://raw.githubusercontent.com/dagger/container-use/main/install.sh \| bash` |
| **Primary author** | Dagger (Solomon Hykes, Sam Alba, Andrea Luzzardi) |
| **Status** | Early development — experimental badge |

---

## The Problem It Solves

Running a single AI coding agent locally is straightforward. The agent modifies files, installs packages, runs tests — and if something goes wrong, you undo it. The problem scales badly:

- **Multiple concurrent agents** share the same filesystem. Two agents modifying `package.json` or `requirements.txt` simultaneously produce unpredictable results.
- **Managed agent platforms** (cloud-hosted, sandboxed) solve isolation but add a black box: no visibility into what the agent actually ran, no way to intervene when it gets stuck.

Container-Use occupies the gap between these options. It is local infrastructure that provides isolation *and* visibility.

---

## How It Works

Container-Use is an MCP server. Add it to a Claude Code session and it exposes environment management tools: create an environment, run commands in it, inspect it, retrieve its output. The agent uses these tools to do its work inside a container rather than directly on the host filesystem.

Behind the scenes, each environment maps to a **Dagger-managed container** (isolated filesystem, isolated network, isolated process space) and a **git branch** (persistent state, reviewable history). The container and the branch are created atomically when the environment is created; the agent's work accumulates in both.

From the developer's perspective:

1. Start a session with container-use configured as an MCP server.
2. Ask the agent to implement a feature, fix a bug, or explore an approach.
3. The agent creates an environment and works entirely inside it.
4. Run `cu watch` in a separate terminal to see a live stream of every command the agent ran and every output it received.
5. When the agent finishes (or gets stuck), run `cu env checkout <name>` to switch your working directory into that environment's branch and inspect the result.
6. Merge, discard, or iterate.

The git integration is the architectural decision that makes this tractable. Agent output is not written to a temporary directory or a proprietary format — it is a git branch. Every developer already knows how to read, compare, and merge git branches.

---

## Parallel Execution

The git-per-agent model enables a workflow that is otherwise difficult to arrange: asking the same agent to attempt the same task several different ways simultaneously, then selecting the best result.

Spin up three environments, give each agent the same prompt with a different constraint ("implement this feature using the existing ORM", "implement this using raw SQL", "implement this with a caching layer"), let all three run in parallel, then `git diff` all three results against each other. The total wall-clock time is the time of the slowest agent, not the sum of all three.

This is not a hypothetical pattern — it is documented in Dagger's own blog post as the primary motivating use case.

---

## Observability: `cu watch`

Most agent tooling operates as a black box: you submit a prompt, you receive a result, and the intermediate steps — commands run, APIs called, files modified — are invisible. Container-Use inverts this.

`cu watch` opens a real-time stream of every tool call the agent makes: the command, its arguments, its stdout, its stderr, its exit code. There is no post-hoc reconstruction; the stream is live.

This matters for agent debugging. When an agent gets stuck in a loop, produces an unexpected output, or asks a clarifying question that reveals a misunderstanding, `cu watch` shows the exact step where things went wrong. An agent that is burning tokens chasing a wrong assumption is immediately visible.

---

## Terminal Intervention

Container-Use exposes direct terminal access to any running environment. If an agent stalls — waiting on input it cannot receive through MCP, or running a command it cannot interpret the output of — a developer can drop into the container's shell, examine the state, complete the step manually, and let the agent continue.

This is the capability that managed cloud agent platforms typically do not offer. The tradeoff is that it requires running container-use locally with the overhead that implies (Dagger installed, containers provisioned). The benefit is that the agent's environment is never fully opaque.

---

## Claude Code Integration

Claude Code is a first-class target. The setup is:

```bash
cd /path/to/repository
claude mcp add container-use -- container-use stdio
```

An optional rules file can be added to `CLAUDE.md` to give the agent explicit guidance on how to use container-use environments:

```bash
curl https://raw.githubusercontent.com/dagger/container-use/main/rules/agent.md >> CLAUDE.md
```

After configuration, Claude Code sessions in that directory automatically have access to container-use environment management tools. The agent creates environments, runs its work inside them, and presents results as git branches — without any additional configuration or prompting.

---

## The Dagger Pedigree

Dagger is not a side project. It was founded by **Solomon Hykes** (Docker creator and Docker's original CEO/CTO), **Sam Alba** (Docker's VP of Engineering), and **Andrea Luzzardi** (Docker's lead architect). The team left Docker between 2018 and 2020 and launched Dagger in 2022, raising $20M in a Series A (YC-backed). Their core product is a CI/CD automation platform built on container primitives.

Container-Use is a direct application of that infrastructure to the agent tooling space. The Dagger backend provides intelligent caching (repeated operations in similar environments are not re-executed from scratch), cross-environment portability (the same container definition runs on Mac, Linux, and Windows via native container runtimes), and the orchestration layer that makes parallel environments tractable.

This is meaningful context. Container tools built by the people who built Docker tend to have well-considered semantics around isolation, state management, and portability.

---

## Supported Agents

Container-Use is documented as compatible with:

- **Claude Code** (explicit setup instructions, rules file)
- **Cursor**
- **Goose** (Block's open-source agent)
- **VSCode** (via MCP extension)
- Any MCP-compatible client

The MCP server exposes the same tools to all clients; the agent's behavior inside environments is determined by the model and the agent's own capabilities, not by container-use.

---

## Limitations and Caveats

**Pre-1.0 stability.** Container-Use carries an experimental badge and the README explicitly describes it as "in early development and actively evolving." The v0.4.x version number reflects this. Developers should expect breaking changes between releases.

**Infrastructure dependency.** Container-Use requires Dagger to be installed and running. This is a meaningful prerequisite: Dagger itself requires a working container runtime (Docker, Podman, or a native equivalent). Teams without container infrastructure will need to set it up before container-use adds value.

**49 open issues.** At the time of research, the repository had 49 open issues and 30 open pull requests. Many are feature requests and edge cases rather than critical bugs, but the volume reflects an actively developing tool rather than a stable one.

**No explicit system requirements documented.** The README does not specify minimum CPU, memory, or disk requirements for running agent environments. Teams running many parallel agents will need to monitor resource consumption experimentally.

---

## Rating: 4.0 / 5

**Why 4.0:**

Container-Use solves a real problem with an elegant architecture. The git-per-agent model is the right abstraction: it slots into existing developer workflows without requiring new tooling for review, comparison, or version control. `cu watch` addresses the observability gap that makes agent debugging painful. The Dagger team's pedigree gives the infrastructure decisions credibility.

The deductions are honest: this is pre-1.0 software with an experimental stability guarantee, a meaningful infrastructure dependency (Dagger + container runtime), and active but incomplete development. For teams already using Dagger or comfortable managing container infrastructure, these are minor concerns. For teams looking for something they can install in five minutes and rely on without thinking about it, container-use is not that tool yet.

| Factor | Score |
|---|---|
| Concept and architecture | ★★★★★ |
| Implementation quality (pedigree, Go, Apache-2.0) | ★★★★☆ |
| Production readiness | ★★★☆☆ |
| Observability (`cu watch`, terminal access) | ★★★★★ |
| Claude Code integration | ★★★★★ |
| **Overall** | **4.0 / 5** |

---

## Who Should Use It

**Good fit:**

- Teams running multiple Claude Code, Cursor, or Goose agents on the same codebase
- Developers who want to compare multiple agent approaches to the same task
- Anyone who has experienced agent file conflicts and wants a structural solution
- Teams comfortable with Docker/Dagger infrastructure who want agent observability

**Not the right fit (yet):**

- Teams that need production-stable tooling without breaking change risk
- Environments where container runtimes are unavailable or prohibited
- Single-agent, single-task workflows where isolation provides no benefit

---

## Further Reading

- [GitHub: dagger/container-use](https://github.com/dagger/container-use)
- [Dagger Blog: Containing Agent Chaos](https://dagger.io/blog/agent-container-use/)
- [Dagger docs: LLM Integration](https://docs.dagger.io/features/llm/)
- Related review: [IBM mcp-cli](/reviews/ibm-mcp-cli/) (MCP client/host)
- Related review: [apify/mcpc](/reviews/apify-mcpc/) (MCP CLI client with credential sandboxing)
- Category: [Developer Tools MCP Servers](/categories/developer-tools/)

