# Cursor 3 Review — The Agent-First IDE That Turned the Editor Into a Runtime

> Cursor 3 (April 2026) rearchitected the IDE around AI agents, not developers. With Background Agents, Composer 2.5, a first-class PR review workflow from the Graphite acquisition, and a potential $60B xAI acquisition looming, this is the most consequential update in AI coding tools this year.


**At a glance:** Cursor 3. Released April 2, 2026 (3.0); 3.3 May 7; 3.4 May 13; Composer 2.5 May 18. Developer: Anysphere. Key features: Agents Window, Background Agents, Composer 2.5, parallel agent execution, PR Review (Graphite acquisition), Canvases, BugBot. Pricing: Free / Pro ($20/mo) / Pro+ ($60/mo) / Ultra ($200/mo) / Teams ($40/user/mo). Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

Cursor did not start as an IDE. It started as a bet that the future of code editing looks like a chat window more than a text buffer.

That bet paid off. By February 2026, Anysphere — the company behind Cursor — had reached $2B in annual recurring revenue. More than twice as many Cursor users rely on Agent Mode as on Tab completion. That's a reversal that would have seemed implausible in early 2025, when the product was still primarily known for its autocomplete quality.

Cursor 3 is the version that formalizes this shift architecturally. The old model — developer uses editor, occasionally asks AI for help — is replaced by a new model: agents do the coding, the developer orchestrates. The IDE is a runtime for agents now. The editor is how the human watches.

---

## What Changed in Cursor 3.0 (April 2, 2026)

The Cursor 3.0 announcement described the product as an "agent execution runtime." That framing is accurate in a way that earlier versions weren't.

The biggest structural change is the **Agents Window** — a unified sidebar that replaces the old Composer pane. Every agent session the user has running, regardless of where it started or where it's executing, appears in a single control surface: local agents working in the current repo, cloud agents (Background Agents) running on VMs, agents isolated in git worktrees via `/worktree`, and agents connected over remote SSH. All visible. All manageable from one place.

This matters because the old model had a scaling problem. If you were running a local Cascade session, a Background Agent on a separate VM, and an SSH-connected agent working on a remote server, you were context-switching between three different views. Cursor 3 collapses that.

Other structural additions in 3.0:

**Agent Tabs** — Multiple agent conversations can be tiled side-by-side or in a grid. The old single-pane chat design was a bottleneck once users started running multiple parallel sessions.

**/worktree command** — Instructs an agent to create an isolated git worktree before making changes. This is significant for parallel agent execution: agents can work in independent branches without interfering with each other or with the user's working tree.

**Design Mode** — Lets users annotate specific UI elements in the embedded browser and attach those annotations to an agent's context. Instead of writing "fix the button spacing in the checkout form," you draw directly on the rendered UI and point to what you mean.

**Multi-repo environments** — A single configuration file can define all repositories an agent needs access to. This makes cross-repo refactors and migrations practical instead of theoretical.

---

## 3.3 (May 7): PR Review and Parallel Agents

Two of the most practically significant features in the Cursor 3 cycle landed in the 3.3 release.

**PR Review workflow** is a first-class GitHub PR integration inside the IDE. It includes a Reviews tab (inline comment threads and top-level PR discussions), a Commits tab (focused commit history), a Changes tab (file tree with a picker for large diffs), and quick-action pills for approve/request-changes/next steps. The feature is a direct product of Anysphere's December 2025 acquisition of Graphite, a New York-based code review startup that was acquired for more than its $290M most recent valuation.

The result is that Cursor 3 now covers the full software development lifecycle inside a single environment: writing code, running tests, deploying, and reviewing PRs without leaving the IDE. Whether you care about that integration depends on how much of your review work you currently do in a browser vs. locally.

**Parallel Agent Execution** lets agents identify independent portions of a task plan and execute them simultaneously through async subagents. This is the logical extension of the `/worktree` feature: if two parts of a refactor don't touch the same files, there's no reason to execute them sequentially. Cursor 3.3 makes the parallelism automatic where possible.

A more operational addition in 3.3: a **Context Usage Breakdown** panel that shows exactly how the agent's context window is being consumed — rules, skills, MCPs, subagents, and so on. This is primarily a debugging tool for users who keep hitting context limits on large tasks.

---

## 3.4 (May 13): Cloud Agents and BugBot Improvements

The 3.4 release focused on cloud agent performance and the BugBot product.

**Cloud environment changes** reduced Dockerfile build time for Background Agents by 70% through caching. Multi-repo environment configs are reused across sessions rather than rebuilt from scratch each time. Build secrets are now isolated from the running agent — an important security change given that agent code execution runs with broad permissions.

**Agents Window UX** got a full-screen expand mode: files, changes, canvases, PRs, browsers, and terminals can now maximize to fill the working area. The agent's tool call output can now be configured for density — showing minimal or full traces of what the agent is doing at each step.

**BugBot billing** switched from seat-based to usage-based for Teams and Individual plans. The product also added two new effort configurations: "High effort" (more reasoning time, higher detection sensitivity) and "Custom effort" (natural language description of when to dial Bugbot's aggressiveness up or down, with Cursor adjusting dynamically).

---

## Canvases (April 15)

Canvases are an agent output format added mid-cycle between 3.0 and 3.3. Instead of describing findings in text, agents can now produce interactive visual output — tables, diagrams, charts, diffs — rendered inline in the side panel.

The practical use case: an agent doing a dependency audit no longer has to write "here is a list of 47 packages with their vulnerability status." It can produce a sortable table with color-coded severity that the developer can filter and export. An agent analyzing performance data can build a chart directly in the editor.

This closes a gap between AI coding tools and traditional dev tooling. A database client shows you query results in a table. An AI agent, until Canvases, always showed results as prose. The two modes are now both available.

---

## Composer 2.5 (May 18, 2026)

Composer is Cursor's in-house AI model for agentic coding tasks — distinct from the frontier models (Claude, GPT-4o, Gemini) that users can also route through Cursor. The company trains its own model on top of open-source checkpoints and optimizes it specifically for long-horizon autonomous coding.

Composer 2.5 makes three concrete claims over Composer 2:

**Long-running task coherence** — the model maintains context and plan fidelity across many steps rather than solving one prompt and effectively starting fresh.

**Complex instruction following** — simultaneously balancing product requirements, code style conventions, testing expectations, and stated user preferences. This is the failure mode most visible in production use of Composer 2: the model would solve the stated requirement while accidentally violating a convention specified earlier in the conversation.

**Collaboration quality** — described in Cursor's announcement as "more pleasant to work with." This includes communication style, effort calibration, and tool use patterns. It's the hardest category to evaluate from a spec sheet.

**Training scale**: Composer 2.5 was trained with 25× more synthetic tasks than Composer 2. The training methodology uses "targeted reinforcement learning with textual feedback" — when the model makes an incorrect tool call during training, a localized hint is inserted at the exact point of failure rather than applying a global reward signal across the whole sequence. The intent is more precise correction.

Composer 2.5 is available via Cursor's API at $0.50/$2.50 per million tokens (standard) and $3.00/$15.00 per million tokens (fast version).

---

## Tab Completion

Cursor's Tab completion is powered by technology from Supermaven — a fast AI code completion startup acquired by Anysphere in 2025. The company claims a 72% code acceptance rate, which it presents as the highest in any AI IDE.

The acceptance rate metric measures how often developers accept the inline suggestion rather than dismissing it and typing manually. It's a proxy for how well the completion model understands what the developer actually wants to write next. At 72%, Cursor's claim exceeds GitHub Copilot's reported 65%.

The Tab model is operationally separate from the agentic models: it runs a lightweight, fast model trained specifically on edit patterns, using a vector index of the codebase for context retrieval. It's optimized for latency, not for complex reasoning.

---

## BugBot

BugBot is Cursor's autonomous PR review product. It connects to GitHub, reviews pull requests, and flags real bugs — logic errors, security vulnerabilities, race conditions, null pointer dereferences. It intentionally ignores style and formatting, which is a deliberate product decision: the goal is to find things that will break production, not things a linter would catch.

As of early 2026, BugBot is processing two million PRs per month, with approximately an 80% resolution rate on the issues it flags. Autofix — which spawns a Background Agent to independently diagnose and fix the flagged issue — results in a merged PR more than 35% of the time.

The known limitations: BugBot supports GitHub only as of April 2026 — no GitLab, no Bitbucket. This is a real constraint for enterprise teams that have standardized on either of those platforms. BugBot is also a paid add-on: $40/user/month with a 200 PR/month cap on Pro plans, unlimited on Teams.

---

## The Competition

The AI IDE market in mid-2026 has shaken out into a few distinct layers.

**Windsurf** is the clearest direct competitor. Windsurf 2.0 (April 15, 2026) shipped a comparable agentic architecture: the Agent Command Center vs. Cursor's Agents Window, Devin cloud agents vs. Cursor Background Agents. Windsurf has a speed advantage on its proprietary SWE-1.5 model (~13× faster than Claude Sonnet 4.5), broader IDE support (JetBrains, Vim, NeoVim, Xcode — Cursor is VS Code only), and stronger enterprise compliance certifications (HIPAA, FedRAMP/ITAR vs. Cursor's SOC 2 only). Cursor has a higher code acceptance rate and more mature single-environment tooling.

**GitHub Copilot** holds approximately 42% market share by developer adoption. It stays in the developer's existing IDE rather than requiring an IDE switch. It has an agentic layer that is improving, but it is not yet at parity with Cursor's agent infrastructure.

**Claude Code** — Anthropic's own CLI agent — has grown rapidly among professional engineers and is frequently cited as the tool of choice for developers who prefer terminal-first workflows. It competes on model quality and autonomy, not on editor experience.

**Cline, Continue, Aider** serve the open-source / vendor-neutral segment. All three avoid subscription lock-in and proprietary model dependencies. None have Background Agents or BugBot equivalents as of this writing.

The summary: Cursor 3 leads on agentic tooling depth, Tab completion quality, and single-environment lifecycle coverage. It loses on compliance certifications, non-VS Code IDE support, and strategic clarity (see next section).

---

## Business Situation

Anysphere's revenue trajectory is unusual even by AI startup standards:

- January 2025: $100M ARR
- June 2025: $500M ARR
- November 2025: $1B ARR
- February 2026: $2B ARR

Total users: 2M+. Paying customers: 1M+. Enterprise teams: approximately 50,000. The company closed a $2.3B Series D in November 2025 at a $29.3B valuation. As of April 2026, it is reportedly in discussions for a $2B Series E at a $50B+ valuation, with the round described as already oversubscribed.

The complication: in April 2026, SpaceX (now merged with xAI) announced a structured option agreement that gives xAI the right to acquire Anysphere for $60 billion — or, alternatively, to pay $10 billion for joint development work if the full acquisition does not proceed. The structure appears designed to give Cursor access to xAI's Colossus supercomputer cluster for model training, while giving xAI access to Cursor's model training infrastructure and distribution.

This has created organizational uncertainty. Fortune described Cursor as at a "crossroads" in March 2026. The deal is an option, not a completed acquisition — but it changes the calculus for employees, enterprise customers evaluating long-term vendor commitment, and investors trying to model what the company looks like in 2027.

---

## Known Limitations

**Security**: CVE-2026-26268 (CVSS 8.1) — a high-severity arbitrary code execution vulnerability allowing compromise via a malicious repository — was patched in February 2026 but highlighted a structural risk: AI-native IDEs have a large attack surface because agents run with broad file and command execution permissions by default.

**Context window exhaustion**: Large monorepos can exceed context limits mid-task, causing agents to lose awareness of distant files. Heavy Pro users can exhaust their monthly allowance in a single afternoon on large refactors.

**Platform lock-in**: Cursor is a VS Code fork, not a plugin. Developers with deep JetBrains or Vim configurations face meaningful migration friction.

**Agent risk**: Agent mode edits files, runs terminal commands, and commits code autonomously. In repos with auto-deploy on push, an agent can ship to production before human review.

**BugBot coverage gaps**: GitHub only. No GitLab or Bitbucket.

**Compliance**: SOC 2 only. Windsurf supports HIPAA, FedRAMP, ITAR, and RBAC — Cursor does not.

**xAI uncertainty**: An acquisition option held by a third party is not a normal situation for enterprise software. Until the option is exercised or expires, the question of who will own Cursor in 18 months is legitimately open.

---

## The Bigger Picture

The stat that matters most in the Cursor 3 story is not a benchmark number or a feature count. It's this: as of early 2026, more Cursor users rely on Agent Mode than on Tab completion. That's a reversal that happened in roughly twelve months.

In early 2025, AI coding tools were autocomplete tools that occasionally wrote whole functions. In mid-2026, they are agent orchestration surfaces that occasionally need the developer to type something. That transition — from assist to execute — is what Cursor 3 is built for.

The risk is that Cursor is building for a world it may not fully control. Claude Code is fast-growing among professionals. GitHub Copilot has distribution locked up. Windsurf has compliance and multi-IDE advantages for enterprise buyers. And there's a $60B option sitting on the table from Elon Musk's AI company.

Cursor 3 is the best version of Cursor. Whether that's enough to define what AI-native development looks like at scale is the open question.

---

**Rating: 4.5 / 5**

The tooling is the strongest in the category. The trajectory is exceptional. The strategic uncertainty — between Claude Code pressure, Windsurf's enterprise advantages, and the xAI option — keeps it off a perfect score.

*Reviewed by ChatForest. Cursor 3.4 + Composer 2.5 (May 2026). All feature descriptions are based on published changelogs and third-party reporting; ChatForest has not conducted hands-on testing.*

