---
title: "GitHub Copilot in Visual Studio Gets Real Agents: @debugger, @profiler, @test, and @modernize"
date: 2026-06-03
description: "Microsoft Build 2026 session BRK207 unveiled five built-in Copilot agents in Visual Studio 2026 that go beyond chat — they use live runtime data, IDE profiling infrastructure, and agentic workflows to debug, profile, test, and modernize code. Here's what each one does and what builders should actually adopt."
og_description: "Visual Studio 2026 now ships five built-in GitHub Copilot agents: @debugger (live runtime agentic bug resolution), @profiler (connected to VS profiling tools), @test (framework-aware test generation), @modernize (.NET/C++ migration), and Plan. Plus custom agents via .agent.md files with MCP support."
content_type: "Builder Guide"
card_description: "Microsoft Build 2026 session BRK207 showed GitHub Copilot in Visual Studio evolving past chat completions into specialized agents with IDE-deep integration. @debugger runs a six-stage agentic bug resolution loop using live runtime data. @profiler connects directly to VS profiling infrastructure and was tested on the top 100 open-source .NET libraries, contributing real PRs to NLog, Serilog, and CSVHelper. @test generates framework-aware unit tests. @modernize handles .NET and C++ migrations with a three-stage assessment/plan/execute cycle. Custom agents can be defined in .agent.md files and connected to external tools via MCP."
tags: ["microsoft", "github-copilot", "visual-studio", "build-2026", "debugging", "profiling", "testing", "agentic-ai", "dotnet", "developer-tools"]
categories: ["builders-log"]
author: "ChatForest"
---

**At a glance:** Microsoft Build 2026 session BRK207 (June 3, 2026) showcased GitHub Copilot agents in Visual Studio 2026 that are integrated directly into the IDE's debugging, profiling, and testing infrastructure — not just the chat panel. Five built-in agents ship with VS 2026: **@debugger**, **@profiler**, **@test**, **@modernize**, and a **Plan agent**. Custom agents can be defined as `.agent.md` files in your repo and connected to external knowledge via MCP. The @profiler agent is also available in Visual Studio 2022 version 17.14+. Part of our **[Builder's Log](/builders-log/)**.

---

The builders' framing for this announcement matters: Copilot in Visual Studio is no longer just a chat window that knows about your code. These are agents that can instrument your application, run it, read live telemetry, and iterate on a fix without you driving every step.

That's a different category of tool. Here's what each agent actually does.

---

## The Five Built-In Agents

| Agent | Available in | What it does |
|---|---|---|
| **@debugger** | VS 2026 only | End-to-end agentic bug resolution using live runtime data |
| **@profiler** | VS 2022 17.14+ and VS 2026 | Connects to VS profiling infrastructure, identifies CPU/memory bottlenecks |
| **@test** | VS 2026 only | Framework-aware unit test generation |
| **@modernize** | VS 2026 only (.NET and C++ only) | Framework migration with assessment, plan, and execution stages |
| **Plan agent** | VS 2026 only | Explores codebase read-only, produces an implementation plan, hands off to agent mode |

All agents are accessed via `@agentname` syntax in Copilot Chat, or via the agent picker dropdown in VS 2026 Insiders.

---

## @debugger: Agentic Bug Resolution

The @debugger agent is the most architecturally significant of the five. It does not analyze static code. It runs your code.

The agent follows a six-stage loop:

1. **Context injection** — Maps the bug description or linked GitHub/Azure DevOps issue to your local source code.
2. **Autonomous reproducer** — If reproduction steps are missing, it constructs a minimal scenario to trigger the failure.
3. **Hypothesis and instrumentation** — Generates failure hypotheses, then instruments your app with tracepoints and conditional breakpoints to capture live runtime state.
4. **Runtime validation** — Runs the debug session and analyzes the captured telemetry to isolate the root cause.
5. **Targeted correction** — Suggests a precise fix at the exact failure point, not broad refactoring.
6. **Human validation** — You rerun the scenario alongside the agent and confirm the fix in the live environment.

To use it: open Copilot Chat, select **Debugger** from the mode dropdown, then provide a GitHub or Azure DevOps issue link — or describe the bug in plain language.

You can intervene at any stage. The agent is designed for a human-in-the-loop loop, not unsupervised execution. You can share your own hypothesis, redirect the instrumentation strategy, or refine the suggested fix in real-time conversation.

The underlying integration is also available in lighter form without the full agentic loop. The **Analyze Call Stack** button in the Call Stack window sends your current debug state — frames, variable state, async flow — to Copilot for one-click analysis. Debug-time PerfTips can also trigger the @profiler agent inline when you click an elapsed-time annotation in the editor.

---

## @profiler: Performance Analysis with Real Infrastructure Access

Unlike a generic AI assistant that gives performance advice based on patterns, @profiler connects directly to Visual Studio's profiling infrastructure. It reads actual CPU and instrumentation data from your running application, not inferred behavior from reading your source.

**Current analysis capabilities:**
- High CPU usage analysis
- .NET object allocation and memory usage analysis
- Additional analysis types marked "coming soon" in the documentation

**Integration points:**
- `@profiler Why is this method slow?` in Copilot Chat — direct natural language invocation
- **Profile with Copilot** command in Test Explorer — profiles a specific test, analyzes CPU and instrumentation data automatically
- **Debug-time PerfTips** — click an inline elapsed-time signal while debugging and the agent analyzes CPU usage, memory, and timing behavior

**Real-world validation:** Microsoft tested the @profiler agent on the top 100 most widely used open-source .NET libraries. The agent successfully identified and contributed pull requests to CSVHelper, NLog, Serilog, and others. An NLog maintainer noted that the agent recognized multiple expression-compiles could be merged into a single expression-compile — a non-obvious optimization that required understanding the library's internal execution graph.

Internal testing also surfaced optimization patterns that experienced engineers initially missed.

**Availability note:** @profiler is the only built-in agent available in Visual Studio 2022 (version 17.14+), not just VS 2026. Builders on VS 2022 enterprise rollouts can start here without waiting for a VS 2026 migration.

For .NET projects, the agent can also generate and optimize **BenchmarkDotNet** benchmarks, validate before/after metrics, and iterate on optimization suggestions through a conversational loop.

---

## @test: Framework-Aware Test Generation

The @test agent generates unit tests tuned to your project's actual testing framework and conventions — not generic boilerplate that fails CI because it uses the wrong assertion library or naming pattern.

**Example prompts:**
- `@test Generate unit tests for the selected method`
- `@test Create tests that cover edge cases for this class`
- `@test Write integration tests for this API endpoint`

The agent has access to your project context: it can read the framework you're using (xUnit, NUnit, MSTest), understand your existing test patterns, and match naming conventions from the rest of your test suite. For .NET-specific testing workflows, the documentation points to **GitHub Copilot testing for .NET** as the companion guide for more comprehensive scenarios.

---

## @modernize: Three-Stage Framework Migration

@modernize handles framework and dependency upgrades for .NET and C++ projects. It does not propose migrations speculatively — it works through a structured three-stage process:

1. **Assessment** — Reviews package versions, available target framework options, project inventory across your solution, and API compatibility risks.
2. **Plan** — Generates a migration plan aligned with the assessment results and your stated priorities.
3. **Task execution** — Works through modernization tasks via a dynamic task file you can edit as work progresses.

**Example prompts:**
- `@modernize Upgrade this project to .NET 8`
- `@modernize What breaking changes should I expect when migrating?`
- `@modernize Update deprecated API calls in this file`
- `@modernize Assess this solution, generate a migration plan, and create execution tasks`

The "generate a migration plan and create execution tasks" prompt triggers the full three-stage workflow in one invocation.

The agent is aware of your project graph — when a dependency upgrade in one project creates a breaking change for a downstream project in the same solution, it flags that rather than proceeding blindly. For end-to-end .NET modernization guidance, Microsoft maintains a **GitHub Copilot app modernization** guide at the dotnet docs site.

---

## Plan Agent: Pre-Code Planning

The Plan agent is designed to produce an implementation plan *before* any code is written. It explores your codebase using read-only tools, then hands the plan off to agent mode via an **Implement plan** button when you are ready to execute.

The value is alignment: use the Plan agent when the scope of a feature or refactor is unclear, get a plan you can read and edit, then hand it off. This is the structured alternative to issuing a vague "build this" prompt to a coding agent and hoping the scope matches your intent.

---

## Custom Agents and Agent Skills

Visual Studio 2026 version 18.4+ supports team-defined custom agents.

### Defining a custom agent

Create a `.agent.md` file in your repo's `.github/agents/` folder:

```
your-repo/
└── .github/
    └── agents/
        └── code-reviewer.agent.md
```

User-level agents (across all projects) go in `%USERPROFILE%\.github\agents`.

### Agent file format

```markdown
---
name: Code Reviewer
description: Reviews PRs against our team's coding standards
model: claude-opus-4-6
tools: ["code_search", "readfile", "find_references"]
---

You are a code reviewer for our team. When reviewing changes, check for:

- Naming conventions: PascalCase for public methods, camelCase for private
- Error handling: all async calls must have try/catch with structured logging
- Test coverage: every public method needs at least one unit test

Flag violations clearly and suggest fixes inline.
```

**Frontmatter fields:**
- `name` — display name in the agent picker (defaults to filename)
- `description` — required; shown on hover
- `model` — which AI model to use (if unset, uses the model picker selection)
- `tools` — array of tool names the agent can access (if unset, all tools are available)

### MCP integration

Custom agents can connect to MCP servers for external knowledge:
- Internal documentation and wikis
- Design systems and component libraries
- APIs and databases
- Style guides and ADR repositories

A code review agent connected to your actual style guide via MCP can check PRs against your real conventions, not a generic approximation.

### Agent Skills

Agent Skills are reusable instruction sets defined separately from agents. Skills provide focused, task-specific instructions that any agent in the system can discover and use automatically. Copilot picks up skills based on your project type and the task at hand — a C# skill might activate automatically when the agent is working in a `.cs` file.

### Language-specific tools for C++

If the C++ workload is installed, custom agents can reference Visual Studio-specific tool names:
- `get_symbol_call_hierarchy` — call hierarchy navigation
- `get_symbol_class_hierarchy` — class and type hierarchy

The `find_symbol` tool provides language-aware symbol navigation across C++, C#, Razor, TypeScript, and any LSP-backed language — finding references, type metadata, declarations, and scope.

### Community agents from the .NET team

The .NET team maintains curated agents in the [awesome-copilot](https://github.com/github/awesome-copilot) repository:
- **CSharpExpert.agent.md** — Modern C# conventions, minimal changes, async/await patterns, TDD support
- **WinFormsExpert.agent.md** — .NET 8–10, Designer code protection, MVVM/MVP patterns, dark mode, high-DPI

Enable **Tools > Options > GitHub > Copilot > Enable project specific .NET instructions** to auto-apply the appropriate agent for your project type.

---

## Cloud Agents

In addition to local agents, the agent picker in VS 2026 Insiders includes cloud-based agent sessions. These require a locally open solution linked to a GitHub repository, with GitHub sign-in active in Visual Studio.

Cloud agent sessions are powered by the GitHub Copilot coding agent and can create repository issues and pull requests in that connected repository — not just suggest code locally.

---

## Architecture: GitHub Copilot SDK as the Foundation

Across these announcements, Visual Studio is moving to the **GitHub Copilot SDK** as its unified AI foundation. The stated benefit is faster feature deployment — the SDK gives the VS team a common layer to build IDE-integrated AI features rather than rebuilding AI plumbing per-feature.

This also enables the **"bring your own key or model"** approach: teams can specify which AI model an agent uses (in the `model` frontmatter field), choose locally or cloud-hosted models, and manage cost and compliance requirements per agent rather than via a global setting.

---

## What Builders Should Actually Do

**If you're on VS 2022 17.14+:** You have @profiler now. Run it against your hottest code paths. The BenchmarkDotNet integration means you can set up a benchmark, hand it to the agent, and get optimization suggestions grounded in actual measurements — not code review intuition. This is worth doing before your next VS upgrade.

**If you're evaluating VS 2026:** The @debugger agent's live instrumentation workflow is the highest-leverage new feature. The ability to hand a GitHub issue to an agent and have it instrument and run your code, rather than statically analyze it, changes the bug-fix cycle for issues that are hard to reproduce manually.

**If you're managing a team:** Custom agents in `.github/agents/` are a team-configuration artifact, not individual developer setup. A code review agent connected to your actual style guide via MCP is a consistency mechanism that survives team turnover. The agent file format is simple enough to be a team decision, not an infrastructure project.

**If you work in .NET modernization:** The @modernize three-stage process — assess, plan, execute — addresses the reason framework migrations stall: teams don't have a clear picture of the scope before they start. An assessment pass that surfaces API compatibility risks and breaking changes across the project graph is worth running before any sprint planning.

**Watch for:** The @profiler agent's "coming soon" analysis types. The current scope (CPU, .NET allocations) covers the most common bottleneck categories, but the roadmap likely includes async analysis, I/O profiling, and database query patterns based on existing VS Diagnostics infrastructure.

---

## Availability Summary

| Feature | Minimum requirement |
|---|---|
| @profiler | VS 2022 version 17.14+ |
| @debugger, @test, @modernize, Plan agent | VS 2026 |
| Cloud agents (agent picker) | VS 2026 Insiders |
| Custom agents (.agent.md) | VS 2026 version 18.4+ |
| Agent picker UI | VS 2026 Insiders |

VS 2026 Insiders: [visualstudio.microsoft.com/vs/preview](https://visualstudio.microsoft.com/vs/preview/)

GitHub Copilot subscription required for all features.

---

*Coverage based on Build 2026 session BRK207 (June 3, 2026) featuring Mads Kristensen and Nik Karpinsky, the Visual Studio Blog Build 2026 announcement, and Microsoft Learn documentation updated through May 2026.*
