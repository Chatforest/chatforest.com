---
title: "GitHub Spec Kit — The Open-Source CLI That Puts the Spec Before the Code"
date: 2026-05-30T17:30:00+09:00
description: "GitHub Spec Kit (github/spec-kit) is an MIT-licensed CLI toolkit with 107K stars that structures AI-assisted coding into a repeatable specify → plan → tasks → implement workflow. Works with 30+ AI coding agents including Claude Code, Copilot, Cursor, and Gemini CLI."
og_description: "GitHub Spec Kit (github/spec-kit): 107K GitHub stars, MIT license, Python CLI (specify). Workflow: Specify → Plan → Tasks → Implement. Supports 30+ AI coding agents. Open-source alternative to Amazon Kiro's spec-driven IDE. Free, agent-agnostic, no IDE lock-in. Released May 2026 (v0.8.7). Rating: 4/5."
content_type: "Review"
card_description: "GitHub Spec Kit is GitHub's open-source CLI toolkit (MIT license, 107K stars) that operationalizes Spec-Driven Development for AI coding agents. Install the specify CLI, then use slash commands — /speckit.specify, /speckit.plan, /speckit.tasks, /speckit.implement — to walk any supported AI agent through a structured workflow before it writes a line of code. Supports 30+ agents: Claude Code, GitHub Copilot, Cursor, Windsurf, Gemini CLI, Codex CLI, Amazon Q, Kiro, Qwen Code, and more. Key advantage over Amazon Kiro: fully agent-agnostic and IDE-agnostic — you bring your own agent. Key limitation: static specs (write once, hand to agent) rather than Kiro's living, bidirectionally-updated specs. Free, no tiers, no usage caps. Required: Python 3.11+."
tags: ["github", "spec-driven", "sdd", "agentic-coding", "claude-code", "copilot", "cursor", "developer-tools", "open-source", "workflow"]
categories: ["reviews"]
rating: 4
author: "ChatForest"
---

Most AI coding tools start with code. GitHub Spec Kit starts with a specification.

**GitHub Spec Kit** (`github/spec-kit`) is an open-source CLI toolkit from GitHub that brings Spec-Driven Development (SDD) to any AI coding agent. It shipped publicly in late 2025, hit v0.8.7 on May 7, 2026, and has accumulated 107,000 GitHub stars — making it the most widely adopted open-source SDD tool in the ecosystem, ahead of Amazon Kiro's proprietary IDE.

The core proposition: instead of prompting an AI agent to write code immediately, Spec Kit intercepts the workflow and forces a structured four-phase process. The spec is written first. The plan is generated from the spec. Tasks are derived from the plan. Code only appears in the implementation phase, after you've had a chance to review and revise everything that precedes it.

This is a direct response to what some call "vibe coding" — the pattern of accepting AI output, debugging it, re-prompting, and eventually arriving at something that works but lacks intentional design. Spec Kit's thesis is that the spec, not the prompt, should be the unit of software engineering.

---

## What Spec Kit Is Not

Spec Kit is not an IDE. It is not a model. It is not a platform.

It is a Python CLI and a collection of slash commands that plug into whichever AI coding agent you already use. If you use Claude Code, the Spec Kit slash commands appear in Claude Code's `/` command palette. If you use GitHub Copilot in VS Code, they appear there. If you switch from Cursor to Windsurf next month, Spec Kit moves with you.

This is the fundamental difference from Amazon Kiro. Kiro is a VS Code fork with spec-driven development baked into the IDE itself. You don't choose your model (it's Claude Sonnet and Amazon Nova via Bedrock), and you don't use your existing editor. Kiro is a closed, integrated system.

Spec Kit is an open, composable layer. It doesn't care what agent you use. It doesn't care what IDE you're in. It provides the workflow structure; you provide the intelligence.

---

## The Workflow: Specify → Plan → Tasks → Implement

The four phases are sequential. Each produces a Markdown artifact that feeds the next. The artifacts are files in your project — version-controlled, reviewable, and editable by humans at any point.

### Phase 1: Specify (`/speckit.specify`)

You describe what you want to build in natural language — the feature, the context, the constraints. The agent, guided by the Spec Kit prompt, produces a **specification document** that captures:

- **What** the feature should do (behavior, not implementation)
- **Why** it exists (the problem being solved)
- **Who** uses it (the relevant users or systems)
- **What success looks like** (acceptance conditions)

The spec is deliberately free of technology choices. Stack decisions come later. This phase is about nailing the requirement before the implementation conversation begins.

### Phase 2: Plan (`/speckit.plan`)

Given the spec and your stated technology stack, the agent generates a **technical implementation plan**:

- Architecture decisions
- Component breakdown
- Interface definitions (APIs, data models, event contracts)
- External dependencies and integration points
- Risk flags or areas of ambiguity

The plan is still not code. It is a design document that specifies how the requirements will be met technically. You review it, edit it, reject sections, or approve it to move forward.

### Phase 3: Tasks (`/speckit.tasks`)

The plan is decomposed into a **dependency-ordered task list**. Each task is:

- Scoped to a small, implementable unit of work
- Annotated with its dependencies (which tasks must complete first)
- Linked to the spec section it satisfies

An optional command, `/speckit.taskstoissues`, converts the task list into GitHub Issues — enabling standard project tracking without leaving the workflow.

### Phase 4: Implement (`/speckit.implement`)

The agent executes the task list against the spec and plan. It has structured context — not just the original natural language prompt, but the full chain of reasoning that led to the task list. The implementation is grounded.

---

## Optional Quality Gates

Three optional commands can be inserted between phases to reduce downstream problems:

| Command | When to Use | What It Does |
|---|---|---|
| `/speckit.clarify` | Before planning | Identifies ambiguities in the spec before the agent commits to a technical direction |
| `/speckit.checklist` | Before planning | Validates that the spec meets quality criteria — completeness, testability, clarity |
| `/speckit.analyze` | Before implementation | Checks spec/plan/task consistency — flags contradictions before code is written |

These gates are not mandatory. For simple, well-understood features, skipping them is reasonable. For complex features where ambiguity is expensive, running all three before implementation can prevent significant rework.

---

## AI Agent Support: 30+ Integrations

Spec Kit's integration model is based on agent-specific command files or skill files that the `specify` CLI installs into your project. Each integration configures how the slash commands present to that specific agent.

Supported integrations include:

**Frontier IDE agents:** Claude Code, GitHub Copilot, Cursor, Windsurf, Codex CLI, Amazon Q, Kiro, Cline, Continue, Roo Code

**Google ecosystem:** Gemini CLI (which migrates to Antigravity CLI on June 18, 2026)

**Chinese frontier models:** Qwen Code, Doubao MarsCode, Baidu Comate

**Open-source agents:** OpenHands, Open Codex, Aider, Amp

**Plus:** a Generic integration for any agent not on the named list — which means Spec Kit's workflow is portable even to tools not yet formally supported.

The portability is intentional. Teams that rotate between agents (using Claude Code for complex refactors, Copilot for quick edits, Codex CLI for PR automation) get consistent workflow structure regardless of which agent is active.

---

## Installation

Spec Kit requires Python 3.11 or newer. The recommended installation uses `uv`:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit@main
```

After installation, `specify` is available as a CLI. To initialize a project:

```bash
specify init
```

This installs the Spec Kit slash commands into your project in the format appropriate for your AI coding agent (you specify which one during init).

The slash commands then appear in your agent's command palette. No additional authentication. No account creation. No usage caps.

---

## Spec Kit vs. Amazon Kiro

Both Kiro and Spec Kit implement spec-driven development. The differences matter for how you adopt them.

| | GitHub Spec Kit | Amazon Kiro |
|---|---|---|
| **Type** | CLI layer on any agent/IDE | Dedicated VS Code fork |
| **Agent support** | 30+ agents | Claude Sonnet + Amazon Nova (Bedrock) |
| **IDE support** | Any IDE | Kiro only (VS Code fork) |
| **Spec lifecycle** | Static (write once, hand to agent) | Living (bidirectionally updated as code changes) |
| **Price** | Free, MIT | Free tier (50 interactions/month), Pro $19/month |
| **AWS integration** | None | Deep (CodeCatalyst, Q Developer, IAM) |
| **Multi-agent** | No | No |
| **Hooks** | No | Yes (event-driven automations) |
| **EARS notation** | No | Yes (structured requirements syntax) |

**Spec Kit wins** if your team uses multiple agents, wants portability, or is unwilling to switch IDEs. It's also the lower-friction option — there's no new tool to learn, just slash commands layered on top of what you already use.

**Kiro wins** if you want deeper spec lifecycle management (specs that update when code changes), are already in the AWS ecosystem, and value the integrated hooks for automation (running tests on file save, generating PR summaries automatically).

The architectural difference is meaningful: Spec Kit writes a spec and hands it off. Kiro maintains the spec as a living document across the project's lifetime. For short, well-scoped features, Spec Kit's approach is perfectly sufficient. For long-running features with evolving requirements, Kiro's living-spec model prevents the artifact from going stale.

---

## Limitations

**Static specs.** Once Spec Kit hands the spec to an implementation agent, the spec is not automatically updated as the implementation evolves. If requirements change mid-implementation, you update the spec manually. Kiro's living-spec model handles this; Spec Kit does not.

**No multi-agent orchestration.** Spec Kit is designed for a single agent working sequentially through the task list. Teams experimenting with multi-agent workflows (one agent per task, running in parallel) will need to build their own orchestration layer.

**No hooks.** Spec Kit has no equivalent to Kiro's event-driven Hooks — no automated test runs on file save, no PR summary generation. The workflow automation must come from elsewhere in your stack (CI/CD, IDE extensions, GitHub Actions).

**Paradigm shift required.** The spec-first workflow adds friction compared to jumping directly into code. Developers working on small, exploratory features may find the specify → plan → tasks chain longer than the task warrants.

**Python dependency.** Spec Kit requires Python 3.11+. Teams working primarily in non-Python stacks will need Python in their environment for the CLI, even if their product code is in another language.

---

## Who Spec Kit Is For

**Strong fit:**
- Teams using multiple AI coding agents and wanting consistent workflow structure across all of them
- Developers who have experienced spec-first benefits (reduced rework, clearer requirements) and want that without switching IDEs
- Engineers building features where requirements clarity matters more than speed — backend systems, APIs, data pipelines, multi-service integrations

**Weaker fit:**
- Solo developers on fast-moving prototypes where the specify → plan → tasks overhead exceeds the feature scope
- Teams already committed to the Kiro ecosystem who want living specs and hooks
- Projects where requirements are inherently emergent and hard to specify in advance

---

## Bottom Line

GitHub Spec Kit is the best argument for spec-driven development that doesn't cost you your IDE or your agent of choice. At 107K GitHub stars, MIT license, and 30+ integrations, it has genuine community momentum and broad compatibility. The slash command interface is clean. The four-phase workflow is well-structured. The quality gates (clarify, checklist, analyze) add real value when used.

The limitation is honest: Spec Kit writes specs; it does not maintain them. For teams who need specs to stay synchronized with evolving implementations, Kiro's living-spec model is architecturally superior. For teams who need portability and low friction, Spec Kit is the better call.

This is the right tool for most builders who want to try spec-driven development without committing to a new IDE.

---

## At a Glance

| | |
|---|---|
| **Repository** | github/spec-kit |
| **Stars** | 107K (as of May 2026) |
| **License** | MIT |
| **Latest version** | v0.8.7 (May 7, 2026) |
| **CLI package** | specify-cli |
| **Install** | `uv tool install specify-cli --from git+https://github.com/github/spec-kit@main` |
| **Requires** | Python 3.11+ |
| **Agents supported** | 30+ |
| **Price** | Free |
| **Documentation** | github.github.com/spec-kit |

**Rating: 4/5** — Excellent open-source SDD toolkit with broad agent support. Loses one star for static (not living) specs and absence of hook-style automations, both of which Kiro addresses. For portability and zero cost, nothing beats it.

*Part of our [Agentic Coding Tools reviews](/categories/ai-tools/). See also: [Amazon Kiro](/reviews/amazon-kiro-aws-agentic-ide-spec-driven-review/).*
