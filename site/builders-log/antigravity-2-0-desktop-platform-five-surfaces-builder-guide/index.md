# Antigravity 2.0: Google's Five-Surface Agent Platform Builder Guide

> Google Antigravity 2.0 ships a five-surface agentic dev platform: desktop app, CLI, SDK, Managed Agents API, and Enterprise Agent Platform. The desktop app adds parallel subagent orchestration, cron-scheduled background tasks, and session-persistent context. Here's the builder map.


[Google shipped Antigravity 2.0 at Google I/O 2026 on May 19](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/), and the scope of the release is easy to underestimate if you only read the headline. This is not an IDE plugin update. [Antigravity 2.0 is a five-surface agentic development platform](https://techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool-at-io-2026/) — desktop app, CLI, SDK, Managed Agents API, and an Enterprise Agent Platform — all running on the same underlying agent harness and the same Gemini 3.5 Flash model.

We already have separate guides on two of those surfaces:

- [Google Is Killing Gemini CLI on June 18 — Migration Checklist to Antigravity CLI](/builders-log/gemini-cli-dead-june-18-antigravity-cli-agy-migration/) covers the `agy` CLI replacement and the MCP config trap.
- [Gemini API Managed Agents: Hosted Sandbox Execution in One Call](/builders-log/gemini-api-managed-agents-antigravity-sandbox-builder-guide/) covers the API-based hosted execution model.

This guide covers what those two don't: the desktop app architecture, parallel subagent orchestration, scheduled background tasks, the SDK, the enterprise tier, and the AGENTS.md / `.agents/skills/` conventions that have replaced the old `.gemini/skills/` path.

---

## What Changed Between Antigravity 1.x and 2.0

Antigravity 1.x was fundamentally a single-agent coding assistant that lived inside your IDE — you prompted it, it responded, you reviewed. The implicit mental model was a smarter autocomplete with terminal access.

Antigravity 2.0 changes the model in two ways. First, [agents can now spawn and coordinate subagents](https://antigravity.google/docs/subagents). A single top-level prompt can trigger parallel workstreams — one agent writes code, another runs tests, a third checks documentation consistency — without the main agent blocking on any of them. Second, agents can run without the user present: [scheduled tasks fire on cron syntax](https://antigravity.google/blog/google-io-2026-feature-deep-dive), the agent executes, and results surface when you reopen the desktop app. Together these two changes move Antigravity from a tool you use to infrastructure you operate.

---

## The Desktop App

[The Antigravity 2.0 desktop app is a standalone application](https://antigravity.google/blog/introducing-google-antigravity-2) — not an IDE extension, not a web panel. It functions as a centralized workspace for agent orchestration.

### Parallel Agents

The app's headline feature is multi-agent parallelism. You can launch multiple agents on different tasks simultaneously. Each agent has its own session context and conversation transcript. [Agents can read each other's conversation transcripts](https://antigravity.google/docs/subagents) to audit multi-step workflows, which means a coordinating agent can read the output of a specialist subagent without explicit message-passing boilerplate.

[When an idle agent receives a message](https://antigravity.google/docs/subagents) — from a user or from another agent — it automatically re-awakens to process the new information. Session context persists across re-activations: the agent retains everything from its prior execution turns when awakened.

### Subagent Workflows

Subagents are the mechanism for parallelizing within a single workflow. An agent can delegate subtasks — running tests, searching the codebase, drafting documentation — to dedicated subagents and continue on its own work while they execute. When a subagent finishes, [its output comes back to the main agent's thread as a structured result](https://antigravity.google/docs/subagents) rather than something the main agent has to reload state to interpret.

The practical effect: tasks that previously required sequential attention (write → test → document → review) can be structured as parallel delegations. Latency on a complex task can drop significantly if the bottleneck was context-switching across steps.

### Scheduled Tasks

Scheduled tasks are a new capability in 2.0 with no equivalent in 1.x. [They use standard cron syntax and run agents in the background automatically](https://antigravity.google/blog/google-io-2026-feature-deep-dive) — Google describes them as letting you "set crons for prompts that you would like agents to tackle periodically, without requiring your manual prompting or invocation." The agent keeps running after the desktop app is closed, and results surface when you next open the app.

This converts the agent from a single-turn tool into a persistent automation pipeline. Use cases:

- Nightly codebase consistency checks against a style guide
- Hourly pulls from a data source with summarization to a shared document
- Automated test suite runs on a branch with results posted to a PR comment
- Weekly changelog drafts based on commit history

---

## File Convention: AGENTS.md and .agents/skills/

Global and workspace skills used to live under `.gemini/skills/`. [Antigravity 2.0 now defaults to a `.agents/skills/` directory for custom skills](https://antigravity.google/docs/skills), though `.gemini/` locations still work for backward compatibility rather than being cut off outright.

At the repo root, [Antigravity parses rule constraints from either a `GEMINI.md` or an `AGENTS.md` file](https://antigravity.google/docs/cli/best-practices) — conceptually similar to how `CLAUDE.md` works in Claude Code, containing project-level instructions the agent reads at session start. Skills themselves live in `.agents/skills/<skill-folder>/` as `SKILL.md` files and can be invoked by name in prompts or referenced in scheduled task definitions.

[Custom agent templates are available in the Google AI Studio Agents tab](https://ai.google.dev/gemini-api/docs/aistudio-agents), which pre-configure the base Antigravity agent's tools and environment — for example, the "AI Radio" template links a specialized `AGENTS.md` file and skill set for radio-show production. The templates are open source in the `google-gemini/gemini-managed-agents-templates` repository, giving teams a starting point without writing an `AGENTS.md` from scratch.

---

## The SDK

[The Antigravity SDK provides programmatic access to the same agent harness that powers Google's own products](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/) — Google confirms Gemini Spark itself "runs on Gemini 3.5 and uses the Antigravity harness." [The SDK lets developers define custom agent behaviors and host them on their infrastructure of choice](https://techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool-at-io-2026/).

The SDK is the right surface when:
- You are embedding agent capabilities into an existing product rather than using the desktop app interactively
- You need agents to run inside your own infrastructure (VPC, on-prem, specific cloud region) rather than Google's managed environment
- You want full control over the agent execution loop — retry logic, error handling, state management — without relying on Google's hosted sandbox

The SDK uses the same `AGENTS.md` / `.agents/skills/` conventions as the desktop app, so skills developed interactively can be extracted and deployed programmatically without rewriting.

---

## The Enterprise Agent Platform

The Gemini Enterprise Agent Platform is the fifth surface, aimed at Google Cloud customers. [Google Cloud customers can use their GCP project in Antigravity to make inference through the Gemini Enterprise Agent Platform](https://antigravity.google/blog/google-antigravity-for-enterprises), with sessions running under Google Cloud's enterprise infrastructure, data privacy, and compliance terms. Separately, [Google's own codelabs show Antigravity agents working directly against Cloud Storage and BigQuery](https://codelabs.developers.google.com/build-and-deploy-gcp-with-antigravity) once connected to a GCP project.

Google's enterprise announcement describes [centralized administrative controls over agent capabilities and product features as "coming soon"](https://antigravity.google/blog/google-antigravity-for-enterprises) rather than fully live today — worth checking current status before assuming full governance tooling (audit logs, deployment policies) is already available. This is still the path for teams that need to operate agents inside existing compliance boundaries rather than standing up a separate hosted environment from scratch.

---

## Pricing Changes in AI Ultra

Antigravity 2.0 shipped alongside a pricing restructure for Google's consumer AI plans. [The AI Ultra plan, previously priced at $250/month, dropped to $200/month](https://blog.google/products-and-platforms/products/google-one/google-ai-subscriptions/) and offers 20x higher usage limits in the Gemini app and Antigravity compared to the Pro plan. [A new $100/month AI Ultra tier launched with 5x higher limits than Pro](https://antigravity.google/blog/changes-to-antigravity-plans).

The plans are:

| Plan | Monthly Price | Antigravity Limits |
|---|---|---|
| Pro | $20 | Baseline |
| AI Ultra | $100 | 5x Pro |
| AI Ultra Pro | $200 | 20x Pro (formerly $250) |

For teams doing serious agentic work — multi-agent workflows, scheduled tasks running overnight, long-context sessions — the 5x and 20x multipliers matter in practice. Hitting rate limits mid-session on a scheduled task means the task either fails silently or queues, depending on how error handling is configured.

---

## Choosing the Right Surface

All five surfaces run on the same harness, but they optimize for different contexts:

| Surface | Best for |
|---|---|
| Desktop app | Interactive development, multi-agent orchestration, scheduled background tasks, experimenting with subagent workflows |
| CLI (`agy`) | CI/CD pipelines, scripted automation, terminal-native workflows, git hooks |
| SDK | Embedding agent capabilities in products, custom infrastructure requirements, programmatic orchestration |
| Managed Agents API | Serverless agent execution, no infra to manage, state persistence between calls, compute-free during preview |
| Enterprise Agent Platform | GCP-native deployment, organizational governance, compliance boundaries, Cloud integration |

The typical progression: start with the desktop app to develop and test workflows interactively, extract working patterns into AGENTS.md, then move them to CLI for CI or SDK for product integration. Managed Agents is the alternative to SDK if you don't want to manage the execution environment.

---

## The Broader Ecosystem Signal

The five-surface architecture matters beyond the feature list. [Gemini Spark, Google's always-on AI agent that's deeply integrated with Workspace tools like Gmail, Docs, and Slides](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/), runs on Gemini 3.5 and "uses the Antigravity harness" — the same harness that powers your Antigravity 2.0 desktop app and scheduled tasks.

This alignment is deliberate. It means skills and behaviors developed for Antigravity 2.0 are architecturally compatible with the direction Google is moving its entire product stack. The platform bet Google is making is not "developers build here, consumers experience elsewhere." The platform bet is that the same agent harness underlies both, and developers who build on it are building skills that surface in Google's consumer products.

---

## Action Items for Builders

**1. Migrate skills to `.agents/skills/`.** If you have skills under `.gemini/skills/` in any repo using Antigravity, move them to `.agents/skills/` — [that's now the default path](https://antigravity.google/docs/skills), though `.gemini/` locations still work for backward compatibility. Make sure repo-root instructions live in a `GEMINI.md` or `AGENTS.md` file, both of which Antigravity still parses.

**2. Set up one scheduled task.** The quickest way to evaluate whether scheduled agents make sense for your workflow is to automate one existing manual task. Nightly changelog drafts and weekly dependency audit summaries are low-risk starting points that demonstrate value without requiring significant setup.

**3. Evaluate the AI Ultra tier.** If you're running multi-agent workflows or scheduled tasks that fire multiple times per day, check whether you're hitting rate limits. The $100/month AI Ultra tier's 5x limit multiplier may eliminate interruptions that currently require manual retry.

**4. Read the parallel agents documentation.** The subagent coordination model is different from sequential tool-use. The [Antigravity parallel agents guide](https://antigravity.google/docs/subagents) documents the transcript-sharing mechanism and message-passing conventions. Understanding this before building complex workflows avoids architectural mistakes that are expensive to refactor.

**5. For SDK users: check the AGENTS.md skill compatibility.** Skills defined in `.agents/skills/` as Markdown files are portable across surfaces — skills work in the desktop app, CLI, and SDK. If you have custom behavior defined only in code, consider externalizing it into skill files for easier iteration.

**6. For GCP customers: try the Enterprise Agent Platform.** The enterprise tier connects agents to your GCP project for inference, and Google's own codelabs show it working against Cloud Storage and BigQuery; centralized governance controls are described by Google as coming, not fully live yet. If your team already uses GCP for data infrastructure, the integration path is worth evaluating now.

---

*Sources: [Google I/O 2026 developer highlights](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/); [TechCrunch on Antigravity 2.0](https://techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool-at-io-2026/); [Antigravity official blog](https://antigravity.google/blog/google-io-2026); [MarkTechPost on the five-surface launch](https://www.marktechpost.com/2026/05/19/google-launches-antigravity-2-0-at-i-o-2026-a-standalone-agent-first-platform-with-cli-sdk-managed-execution-and-enterprise-support/).*

