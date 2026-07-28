# GitHub Copilot in Visual Studio Gets Real Agents: @debugger, @profiler, @test, and @modernize

> Microsoft Build 2026 session BRK207 unveiled five built-in Copilot agents in Visual Studio 2026 that go beyond chat — they use live runtime data, IDE profiling infrastructure, and agentic workflows to debug, profile, test, and modernize code. Here's what each one does and what builders should actually adopt.


**At a glance:** Microsoft Build 2026 session [BRK207](https://github.com/microsoft/Build26-BRK207-github-copilot-in-visual-studio-agents-that-debug-profile-and-test) (June 3, 2026) showcased GitHub Copilot agents in Visual Studio 2026 that are integrated directly into the IDE's debugging, profiling, and testing infrastructure — not just the chat panel. Five built-in agents ship with VS 2026: **@debugger**, **@profiler**, **@test**, **@modernize**, and a **Plan agent** — see the [built-in agents list](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents?view=visualstudio#built-in-agents). Custom agents can be defined as [`.agent.md` files](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents?view=visualstudio#custom-agents) in your repo and connected to external knowledge via MCP. The @profiler agent is also available in [Visual Studio 2022 version 17.14+](https://learn.microsoft.com/en-us/visualstudio/profiling/profile-with-copilot-agent?view=visualstudio#prerequisites). Part of our **[Builder's Log](/builders-log/)**.

---

The builders' framing for this announcement matters: Copilot in Visual Studio is no longer just a chat window that knows about your code. These are agents that can instrument your application, run it, read live telemetry, and iterate on a fix without you driving every step.

That's a different category of tool. Here's what each agent actually does.

---

## The Five Built-In Agents

Per Microsoft's [built-in agents documentation](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents?view=visualstudio#built-in-agents):

| Agent | Available in | What it does |
|---|---|---|
| **@debugger** | VS 2026 only | End-to-end agentic bug resolution using live runtime data |
| **@profiler** | [VS 2022 17.14+](https://learn.microsoft.com/en-us/visualstudio/profiling/profile-with-copilot-agent?view=visualstudio#prerequisites) and VS 2026 | Connects to VS profiling infrastructure, identifies CPU/memory bottlenecks |
| **@test** | VS 2026 only | Framework-aware unit test generation |
| **@modernize** | VS 2026 only (.NET and C++ only) | Framework migration with assessment, plan, and execution stages |
| **Plan agent** | VS 2026 only | Explores codebase read-only, produces an implementation plan, hands off to agent mode |

All agents are accessed via `@agentname` syntax in Copilot Chat, or via the [agent picker dropdown in VS 2026 Insiders](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents?view=visualstudio#access-custom-agents).

---

## @debugger: Agentic Bug Resolution

The @debugger agent is the most architecturally significant of the five. It does not analyze static code. It runs your code.

The agent follows a six-stage loop, per Microsoft's [Debugger Agent documentation](https://learn.microsoft.com/en-us/visualstudio/debugger/debug-with-copilot?view=visualstudio#agentic-bug-resolution-with-the-debugger-agent):

1. **Context injection** — Maps the bug description or linked GitHub/Azure DevOps issue to your local source code.
2. **Autonomous reproducer** — If reproduction steps are missing, it constructs a minimal scenario to trigger the failure.
3. **Hypothesis and instrumentation** — Generates failure hypotheses, then instruments your app with tracepoints and conditional breakpoints to capture live runtime state.
4. **Runtime validation** — Runs the debug session and analyzes the captured telemetry to isolate the root cause.
5. **Targeted correction** — Suggests a precise fix at the exact failure point, not broad refactoring.
6. **Final human validation** — You rerun the scenario alongside the agent and confirm the fix in the live environment.

To use it: open Copilot Chat, select **Debugger** from the mode dropdown, then provide a GitHub or Azure DevOps issue link — or describe the bug in plain language.

You can intervene at any stage. The agent is designed for a human-in-the-loop loop, not unsupervised execution. You can share your own hypothesis, redirect the instrumentation strategy, or refine the suggested fix in real-time conversation.

The underlying integration is also available in lighter form without the full agentic loop. The [**Analyze Call Stack** button in the Call Stack window](https://learn.microsoft.com/en-us/visualstudio/debugger/how-to-use-the-call-stack-window?view=visualstudio#analyze-call-stack-with-copilot) sends your current debug state — frames, variable state, async flow — to Copilot for one-click analysis. [Debug-time PerfTips](https://learn.microsoft.com/en-us/visualstudio/profiling/perftips?view=visualstudio) can also trigger the @profiler agent inline when you click an elapsed-time annotation in the editor.

---

## @profiler: Performance Analysis with Real Infrastructure Access

Unlike a generic AI assistant that gives performance advice based on patterns, @profiler connects directly to Visual Studio's profiling infrastructure. It reads actual CPU and instrumentation data from your running application, not inferred behavior from reading your source.

**Current analysis capabilities**, per [Microsoft's Profiler Agent documentation](https://learn.microsoft.com/en-us/visualstudio/profiling/profile-with-copilot-agent?view=visualstudio):
- High CPU usage analysis
- .NET object allocation and memory usage analysis
- Additional analysis types marked "coming soon" in the documentation

**Integration points:**
- `@profiler Why is this method slow?` in Copilot Chat — direct natural language invocation
- [**Profile with Copilot**](https://learn.microsoft.com/en-us/visualstudio/test/debug-unit-tests-with-test-explorer?view=visualstudio#profile-a-test-with-copilot) command in Test Explorer — profiles a specific test, analyzes CPU and instrumentation data automatically
- [**Debug-time PerfTips**](https://learn.microsoft.com/en-us/visualstudio/profiling/perftips?view=visualstudio) — click an inline elapsed-time signal while debugging and the agent analyzes CPU usage, memory, and timing behavior

**Real-world validation:** Microsoft tested the @profiler agent on the [top 100 most widely used open-source libraries and applications](https://devblogs.microsoft.com/visualstudio/copilot-profiler-agent-visual-studio/). The agent identified and contributed pull requests to CSVHelper, NLog, Serilog, and others; a [second Visual Studio Blog post](https://devblogs.microsoft.com/visualstudio/delegate-the-analysis-not-the-performance/) walks through the CSVHelper optimization specifically. An NLog maintainer's reaction, quoted in the first post: "Saw the YouTube video and it is almost magical. Amazing how it was able to recognize that multiple expression-compiles could be merged into a single expression-compile."

[Internal testing also surfaced an optimization pattern experienced engineers initially missed](https://devblogs.microsoft.com/visualstudio/copilot-profiler-agent-visual-studio/): a Microsoft engineer used the agent to fix a memory/execution-time regression from adding `IEnumerable` support to a dictionary-wrapping class, and the agent's suggestions pointed toward .NET's support for duck-typed `foreach` — a technique the engineer said several principal-level engineers with deep .NET experience weren't aware of either.

**Availability note:** @profiler is the only built-in agent available in [Visual Studio 2022 (version 17.14+)](https://learn.microsoft.com/en-us/visualstudio/profiling/profile-with-copilot-agent?view=visualstudio#prerequisites), not just VS 2026. Builders on VS 2022 enterprise rollouts can start here without waiting for a VS 2026 migration.

For .NET projects, the agent can also [generate and optimize **BenchmarkDotNet** benchmarks](https://learn.microsoft.com/en-us/visualstudio/profiling/profile-with-copilot-agent?view=visualstudio), validate before/after metrics, and iterate on optimization suggestions through a conversational loop.

---

## @test: Framework-Aware Test Generation

The @test agent generates unit tests tuned to your project's actual testing framework and conventions — not generic boilerplate that fails CI because it uses the wrong assertion library or naming pattern.

**Example prompts:**
- `@test Generate unit tests for the selected method`
- `@test Create tests that cover edge cases for this class`
- `@test Write integration tests for this API endpoint`

The agent has access to your project context: it can read the [framework you're using (MSTest, NUnit, xUnit)](https://learn.microsoft.com/en-us/visualstudio/test/unit-testing-with-github-copilot-test-dotnet?view=visualstudio), understand your existing test patterns, and match naming conventions from the rest of your test suite. For .NET-specific testing workflows, the documentation points to **[GitHub Copilot testing for .NET](https://learn.microsoft.com/en-us/visualstudio/test/github-copilot-test-dotnet-overview?view=visualstudio)** as the companion guide for more comprehensive scenarios.

---

## @modernize: Three-Stage Framework Migration

@modernize handles framework and dependency upgrades for .NET and C++ projects. It does not propose migrations speculatively — for .NET, [it works through a structured three-stage process](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents?view=visualstudio#use-the-modernize-agent):

1. **Assessment** — Reviews package versions, available target framework options, project inventory across your solution, and API compatibility risks.
2. **Plan** — Generates a migration plan aligned with the assessment results and your stated priorities.
3. **Task execution** — Works through modernization tasks via a dynamic task file you can edit as work progresses.

**Example prompts:**
- `@modernize Upgrade this project to .NET 8`
- `@modernize What breaking changes should I expect when migrating?`
- `@modernize Update deprecated API calls in this file`
- `@modernize Assess this solution, generate a migration plan, and create execution tasks`

The "generate a migration plan and create execution tasks" prompt triggers the full three-stage workflow in one invocation.

The agent is aware of your project graph — when a dependency upgrade in one project creates a breaking change for a downstream project in the same solution, it flags that rather than proceeding blindly. For end-to-end .NET modernization guidance, Microsoft maintains a **[GitHub Copilot app modernization](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-app-modernization/overview)** guide at the dotnet docs site.

---

## Plan Agent: Pre-Code Planning

The [Plan agent is designed to produce an implementation plan](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents?view=visualstudio#built-in-agents) *before* any code is written. It explores your codebase using read-only tools, then hands the plan off to agent mode via an **Implement plan** button when you are ready to execute.

The value is alignment: use the Plan agent when the scope of a feature or refactor is unclear, get a plan you can read and edit, then hand it off. This is the structured alternative to issuing a vague "build this" prompt to a coding agent and hoping the scope matches your intent.

---

## Custom Agents and Agent Skills

[Visual Studio 2026 version 18.4+ supports team-defined custom agents](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents?view=visualstudio#custom-agents).

### Defining a custom agent

[Create a `.agent.md` file](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents?view=visualstudio#create-a-custom-agent) in your repo's `.github/agents/` folder:

```
your-repo/
└── .github/
    └── agents/
        └── code-reviewer.agent.md
```

[User-level agents (across all projects) go in `%USERPROFILE%\.github\agents`](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents?view=visualstudio#create-a-custom-agent).

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

**[Frontmatter fields](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents?view=visualstudio#agent-file-format):**
- `name` — display name in the agent picker (defaults to filename)
- `description` — required; shown on hover
- `model` — which AI model to use (if unset, uses the model picker selection)
- `tools` — array of tool names the agent can access (if unset, all tools are available)

### MCP integration

Custom agents can [connect to MCP servers](https://learn.microsoft.com/en-us/visualstudio/ide/mcp-servers?view=visualstudio) for external knowledge:
- Internal documentation and wikis
- Design systems and component libraries
- APIs and databases
- Style guides and ADR repositories

A code review agent connected to your actual style guide via MCP can check PRs against your real conventions, not a generic approximation.

### Agent Skills

[Agent Skills are reusable instruction sets](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-agent-skills?view=visualstudio) defined separately from agents (they require Visual Studio 2026 version 18.5+). Skills provide focused, task-specific instructions that any agent can discover and use automatically — Copilot decides when a skill is relevant to the current request and activates it.

### Language-specific tools for C++

If the C++ workload is installed, [custom agents can reference Visual Studio-specific tool names](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents?view=visualstudio#language-specific-tools-for-c):
- `get_symbol_call_hierarchy` — call hierarchy navigation
- `get_symbol_class_hierarchy` — class and type hierarchy

The [`find_symbol` tool](https://devblogs.microsoft.com/visualstudio/unlock-language-specific-rich-symbol-context-using-new-find_symbol-tool/) provides language-aware symbol navigation across C++, C#, Razor, TypeScript, and any LSP-backed language — finding references, type metadata, declarations, and scope.

### Community agents from the .NET team

The [.NET team maintains curated agents](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents?view=visualstudio#net-development-agents) in the [awesome-copilot](https://github.com/github/awesome-copilot) repository:
- **[CSharpExpert.agent.md](https://github.com/github/awesome-copilot/blob/main/agents/CSharpExpert.agent.md)** — Modern C# conventions, minimal changes, async/await patterns, TDD support
- **[WinFormsExpert.agent.md](https://github.com/github/awesome-copilot/blob/main/agents/WinFormsExpert.agent.md)** — .NET 8–10, Designer code protection, MVVM/MVP patterns, dark mode, high-DPI

Enable **Tools > Options > GitHub > Copilot > Enable project specific .NET instructions** to auto-apply the appropriate agent for your project type.

---

## Cloud Agents

In addition to local agents, [the agent picker in VS 2026 Insiders includes cloud-based agent sessions](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents?view=visualstudio#cloud-agents). These require a locally open solution linked to a GitHub repository, with GitHub sign-in active in Visual Studio.

Cloud agent sessions are powered by the GitHub Copilot coding agent and can create repository issues and pull requests in that connected repository — not just suggest code locally.

---

## Architecture: GitHub Copilot SDK as the Foundation

Across these announcements, Visual Studio is moving to the **[GitHub Copilot SDK](https://devblogs.microsoft.com/visualstudio/whats-coming-next-in-visual-studio-our-microsoft-build-2026-announcements/)** as its unified AI foundation — the same SDK that powers the GitHub Copilot CLI. The stated benefit, per Microsoft's Build 2026 announcement post, is that the team can "move faster, stay aligned with the broader ecosystem, and bring new capabilities into Visual Studio sooner" — a common layer instead of rebuilding AI plumbing per-feature.

This also enables the **"bring your own key, bring your own model"** approach described in that same post: teams can specify which AI model an agent uses (in the `model` frontmatter field) and choose models that run locally or in the cloud.

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

*Coverage based on Build 2026 session [BRK207](https://github.com/microsoft/Build26-BRK207-github-copilot-in-visual-studio-agents-that-debug-profile-and-test) (June 3, 2026) featuring Mads Kristensen and Nik Karpinsky, the [Visual Studio Blog Build 2026 announcement](https://devblogs.microsoft.com/visualstudio/whats-coming-next-in-visual-studio-our-microsoft-build-2026-announcements/), and [Microsoft Learn documentation](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents?view=visualstudio) updated through May 2026.*

