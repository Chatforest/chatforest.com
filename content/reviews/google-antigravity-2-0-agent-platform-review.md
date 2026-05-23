---
title: "Google Antigravity 2.0 Review: Parallel Agents, Gemini 3.5 Flash, and Google's Agent-First Bet"
date: 2026-05-22T16:00:00+09:00
description: "Google Antigravity 2.0 launched at Google I/O 2026 (May 19) with a redesigned desktop app, a Go-based CLI, and an open SDK. Powered by Gemini 3.5 Flash — which leads MCP Atlas at 83.6% and runs at 289 tok/s. Parallel agent dispatch, scheduled background tasks, Firebase/Android/Cloud integration. Pricing: AI Plus $7.99/mo up to AI Ultra $200/mo. Rating: 4/5."
og_description: "Google Antigravity 2.0 (May 19, 2026): desktop app, CLI, SDK, parallel agents, Gemini 3.5 Flash. MCP Atlas leader at 83.6%. AI Plus $7.99/mo, AI Ultra $200/mo. Rating: 4/5."
card_description: "Google Antigravity 2.0 (May 19, 2026) — Google's agent-first coding platform. Desktop app for parallel multi-agent orchestration, Go-based CLI for terminal workflows, Antigravity SDK for custom agents. Powered by Gemini 3.5 Flash: 289 tok/s, $1.50/$9 per M tokens, #1 on MCP Atlas (83.6%). Background/scheduled tasks, Firebase + Android + AI Studio + Google Cloud integration. Pricing: AI Plus $7.99/mo, AI Pro $19.99/mo, AI Ultra $100/mo (5× limits), AI Ultra top $200/mo (20× limits, down from $250). Strengths: parallel agent dispatch, speed, Google ecosystem depth. Weaknesses: 61% hallucination rate, memory less mature than Claude Code, enterprise requires $100+/mo. Rating: 4/5."
tags: ["llm", "coding", "ai-coding-assistant", "google", "agentic", "gemini", "developer-tools", "parallel-agents", "desktop-app", "cli"]
categories: ["reviews"]
rating: 3
ratingHalf: true
author: "ChatForest"
last_refreshed: 2026-05-22
---

**At a glance:** Google Antigravity 2.0, launched May 19, 2026 at Google I/O 2026. Agent-first coding platform with a redesigned desktop app, Go-based CLI, and open SDK. Powered by Gemini 3.5 Flash — the fastest frontier model at 289 tok/s and the leader on MCP Atlas (83.6%). Pricing: AI Plus $7.99/mo to AI Ultra $200/mo. Part of our **[AI developer tools reviews](/categories/ai-providers/)**.

---

The pattern in AI coding tools has been predictable: build a smarter autocomplete, add chat, add context awareness, eventually add agent mode. The upgrade path is gradual, and each step makes the previous tool feel incremental.

Google Antigravity 2.0 does not fit this pattern. It arrived at Google I/O 2026 on May 19 as a platform built from the beginning around agent dispatch — not as an IDE plugin that grew into an agent, but as an orchestration surface where parallel agents are the primary unit of work. The desktop app, the CLI, and the SDK are all expressions of the same idea: you define tasks, agents execute them in parallel, you review outcomes.

The question this review tries to answer is not whether Antigravity is impressive. It is. The question is whether the architecture matches how you actually work, and what you give up to get it.

---

## What Antigravity 2.0 Is

Antigravity is Google's agent-first development platform. Version 1.0 launched in late 2025 as a redesign of what was then the Gemini CLI. Version 2.0, announced at Google I/O 2026, is a substantially larger product: a standalone desktop application, a rebuilt CLI, a public SDK, and a set of enterprise integrations connecting it to Google AI Studio, Firebase, Android Studio, and Google Cloud.

At the technical level, Antigravity is powered by **Gemini 3.5 Flash** — which is not a compromise. Gemini 3.5 Flash, also announced at Google I/O 2026 on May 19, leads the entire field on MCP Atlas at 83.6%, outperforming Claude Opus 4.7 (79.1%), GPT-5.5 (75.3%), and Cursor Composer 2.5 (77.4%). It generates 289 tokens per second — approximately four times faster than Claude Opus 4.7 and GPT-5.5. The choice of Flash over a Pro model is not cost-cutting; it is the reason the platform can run five parallel agents in real time without creating visible wait states.

The Google Gemini CLI is transitioning to the Antigravity CLI. This migration is officially underway as of May 2026; Google's developer blog confirmed the rename and the Go rewrite simultaneously.

---

## The Three Surfaces

### Desktop App

The Antigravity desktop app is the flagship surface. It visualizes active agents as concurrent work streams: you can see Agent 1 refactoring the auth module while Agent 2 generates test cases for the billing API and Agent 3 queries documentation for a dependency question. These are not sequenced — they run in parallel, sharing a common workspace context that Antigravity maintains across the session.

Key capabilities introduced in 2.0:

- **Dynamic subagents.** You define a high-level task; Antigravity decomposes it into parallelizable subtasks and spawns subagents automatically. The decomposition is visible in the interface, so you can inspect and intervene before agents diverge.
- **Scheduled tasks.** Background automation is built in. You can schedule an agent to run after a commit, after a PR opens, on a time interval, or on custom event triggers. The agent runs whether the desktop app is open or not.
- **Voice commands.** Native voice input is available in 2.0. You can dispatch agents, query status, and approve or redirect work without switching to a keyboard. This is not speech-to-text pasted into a text box — it is a voice interaction layer built into the agent workflow.
- **Google ecosystem integration.** Projects connect natively to Firebase (hosting, Firestore, Functions), Android Studio (real-device testing and ADB tooling), Google AI Studio (model selection and fine-tuning), and Google Cloud (Vertex AI, Cloud Run, Cloud Storage).

### CLI

The Antigravity CLI is rebuilt in Go for 2.0, replacing the prior Python-based Gemini CLI. The result is a lighter binary, faster cold start, and consistent behavior across macOS, Linux, and Windows.

From the terminal, you can:

- Create and dispatch agents with a single command
- Monitor active agent status in a structured output view
- Pipe context (files, git diffs, test output) directly into an agent task
- Chain agents via shell scripting — output from one agent becomes input to another

The CLI is the right surface for developers who want Antigravity's agent model without leaving the terminal workflow. It is also how CI/CD integration works: Antigravity agents can be triggered from GitHub Actions, GitLab CI, or any runner that can exec a binary.

### SDK

The Antigravity SDK provides programmatic access to the same agent harness powering the desktop app. It is optimized for Gemini models, allows custom agent behavior definitions, and supports deployment on any infrastructure — Google Cloud, AWS, on-prem, or a private VPS.

The SDK is aimed at teams building internal tools on top of the Antigravity agent harness: custom CI agents, documentation maintainers, automated code review agents, or specialized domain agents that need the Antigravity orchestration layer without the full desktop interface.

Enterprise users can access custom agent templates in Google AI Studio and deploy managed execution environments through Google Cloud, which handles compute scaling and agent isolation.

---

## Benchmarks: Where Gemini 3.5 Flash Leads and Where It Trails

Antigravity's model is Gemini 3.5 Flash. Its benchmark profile matters because it determines what Antigravity can and cannot do well.

**Where Gemini 3.5 Flash leads (May 2026):**

| Benchmark | Gemini 3.5 Flash | Claude Opus 4.7 | GPT-5.5 |
|---|---|---|---|
| MCP Atlas | **83.6%** | 79.1% | 75.3% |
| Terminal-Bench 2.1 | **76.2%** | 69.4% | 70.3% |
| Finance Agent v2 | **57.9%** | 51.3% | 43.0% |
| CharXiv Reasoning | **84.2%** | 79.8% | 81.4% |
| MMMU-Pro | **74.1%** | 71.6% | 72.3% |
| Speed (tok/s) | **289** | ~61 | ~94 |

**Where Gemini 3.5 Flash trails:**

| Benchmark | Gemini 3.5 Flash | Claude Opus 4.7 | GPT-5.5 |
|---|---|---|---|
| SWE-Bench Pro | 69.2% | **76.4%** | 72.1% |
| ARC-AGI-2 | 71.3% | 73.2% | **84.6%** |
| MRCR v2 (long-context) | 71.1% | **79.4%** | 73.8% |
| Hallucination rate | 61% | **38%** | 44% |

The pattern is consistent: Gemini 3.5 Flash is optimized for agentic tool use — multi-step reasoning with external tools, parallel task execution, structured output, fast iteration. It is not the strongest choice for tasks requiring deep code correctness, very long-context document analysis, or hard knowledge-intensive benchmarks. The hallucination rate of 61% is a meaningful constraint — improved substantially from earlier Gemini generations, but still behind the leaders when code accuracy is the primary requirement.

---

## Pricing

Google restructured its AI subscription tiers at Google I/O 2026 simultaneously with the Antigravity 2.0 launch:

| Plan | Monthly cost | Antigravity limits |
|---|---|---|
| AI Plus | $7.99 | Base access |
| AI Pro | $19.99 | Pro limits |
| AI Ultra (entry) | $99.99 | 5× Pro limits |
| AI Ultra (top) | $200.00 ↓ from $250 | 20× Pro limits |

For API usage directly (bypassing subscriptions), Gemini 3.5 Flash is priced at **$1.50 per million input tokens / $9.00 per million output tokens** — roughly half of Claude Sonnet 4.6 pricing ($3.00/$15.00) and one-third of GPT-5.5 ($5.00/$30.00). Cached input tokens are $0.15 per million.

The $7.99 AI Plus entry point is the most accessible among major agentic coding platforms. Codex Cloud starts at $20/mo (ChatGPT Plus) and has real developer costs of $100–200/month in token usage. Claude Code is subscription-only via Claude Pro or Max plans. Antigravity's free-to-entry pricing has a clear strategic purpose: acquire developers before they commit to competing ecosystems.

---

## How It Compares

**vs. Claude Code:** Claude Code is sequential and approval-based by design — you approve each significant action before it executes. This is appropriate when code correctness matters more than throughput, or when the codebase is complex enough that an autonomous agent diverging is expensive to fix. Antigravity runs agents in parallel without per-step approval, which is faster but requires more trust in the model's judgment. Claude Code's hallucination rate (38%) is also meaningfully lower than Antigravity's (61%). The right choice depends on your tolerance for autonomous errors vs. your need for throughput.

**vs. Cursor Composer 2.5:** Cursor is IDE-integrated and file-centric — you work in your editor, Composer 2.5 assists. Antigravity is a standalone platform and task-centric — you dispatch agents from outside the editor. These serve different workflows. A developer who wants AI assistance while writing code will prefer Cursor. A developer who wants to delegate batches of tasks and review completed work will prefer Antigravity.

**vs. OpenAI Codex Cloud:** The closest architectural comparison. Both are parallel async agent platforms. The differences: Antigravity is deeply integrated into the Google ecosystem (Firebase, Android, GCP); Codex Cloud is integrated into the OpenAI ecosystem (ChatGPT, OpenAI plugins, Microsoft). Antigravity's model (Gemini 3.5 Flash) leads on MCP Atlas and speed; Codex Cloud's model (codex-1) is fine-tuned specifically for software engineering execution. Antigravity has a lower entry price ($7.99/mo vs $20/mo). Codex Cloud has deeper mobile integration (native iOS/Android app since May 14).

---

## What Works

**Parallel agent dispatch is real.** This is not a marketing claim. The desktop app visualizes concurrent agents working on distinct tasks with shared context, and the CLI supports the same parallelism from the terminal. For teams running repetitive, distributable work — test generation, dependency audits, documentation passes, localization — the throughput difference over sequential tools is substantial.

**Speed changes the interaction model.** At 289 tok/s, Gemini 3.5 Flash returns results at conversational pace even for multi-step agent tasks. Waiting 30–60 seconds for a complex agent response (common with slower frontier models) changes how you use a tool — you start other tasks, lose context, review later. Antigravity's speed keeps agents in the same attention span as the rest of your work.

**Google ecosystem integration is a real advantage for Google stack teams.** If your stack is Firebase + Android + GCP, Antigravity's native integrations are genuinely valuable — agents that can deploy to Firebase Functions, test on Android devices, and provision Cloud Run services without copy-pasting outputs between tools.

**The entry price removes friction.** $7.99/mo is low enough that teams can put Antigravity in front of developers without budget approval cycles. The cost of evaluation is minimal.

---

## Browser Agent

One feature Antigravity 2.0 has that neither Claude Code nor Cursor currently offers: a **built-in browser agent**. The agent can navigate web pages, click interactive elements, toggle DevTools, switch to mobile viewport, and run a visual QA loop on frontend changes — without the developer writing Playwright or Cypress tests. For teams doing frontend work, this removes the handoff between coding and browser-based testing.

## A2A Protocol

Antigravity 2.0 adds native support for Google's **Agent-to-Agent (A2A)** protocol, which launched in April 2025 with backing from 150+ organizations. A2A handles agent-to-agent delegation — one agent handing off a subtask to a specialist agent — complementing MCP (which handles agent-to-tool calls). AgentKit 2.0 integration enables up to 16-agent configurations with A2A support. For developers building multi-agent systems, this is one of the first production developer tools to expose A2A as a first-class feature.

## What Falls Short

**The 2.0 launch caused widespread breakage.** The auto-update pushed to existing users on May 19 removed the built-in code editor, wiped stored configurations, and silently made them unreachable (2.0 uses a different folder). Core IDE functionality — terminals, sidebars — disappeared. Windows had installer conflicts. A separate agent logic patch had to ship post-launch after reports that the agent was reverting human edits it classified as "inefficiencies." The replacement CLI (`agy`) was announced as the replacement for the Gemini CLI (shutting down June 18, 2026) but was not available on any public package manager as of two days after launch. The Gemini CLI was open source; `agy` is closed source. This combination generated substantial community frustration, particularly from teams running the Gemini CLI in CI/CD pipelines.

**Model labels in the interface may not match the actual model.** A thread on the Google AI Developers Forum flagged that "Gemini 3 Pro" in the interface may actually route to Gemini 2.0 Flash, and model identifiers do not consistently reflect the underlying models called. This affects cost estimation, performance expectations, and reproducibility. Not a minor UX issue.

**The free tier was cut from 250 to 20 requests/day.** Twenty requests is insufficient for meaningful real-workflow evaluation — it will be exhausted in minutes on non-trivial tasks.

**Terminal sandboxing is macOS only.** Antigravity 2.0's kernel-level isolation for agent terminal commands uses Apple's Seatbelt (`sandbox-exec`) — macOS only. No Linux or Windows equivalent has been announced, making it unavailable in CI/CD pipelines and non-macOS development environments.

**The hallucination rate is a constraint.** 61% hallucination rate means Antigravity agents will produce plausible-but-wrong outputs with enough regularity that review workflows are not optional — they are required. For supervised parallel workflows (dispatch agents, review all outputs before merge), this is manageable. For fully automated pipelines without human review, it is a risk.

**Memory and continuity are less mature.** Claude Code and Codex Cloud both have cross-session memory systems (Claude Code's persistent memory, Codex memory in preview). Antigravity's session context is robust, but cross-session project continuity — remembering your conventions, preferred patterns, architectural decisions — is less developed in 2.0. For long-running projects with complex context, this creates setup overhead on each new session.

**Enterprise features require $100+/month.** The capabilities that make Antigravity useful for teams (managed execution environments, custom templates in AI Studio, Google Cloud integration at scale) require the AI Ultra tier starting at $99.99/mo. The $7.99/mo and $19.99/mo tiers are functional for individual use but constrained for team deployment.

**Google ecosystem lock-in is real.** The Firebase, Android, and GCP integrations are Antigravity's strongest differentiators — and they are usable only within the Google ecosystem. If your stack is AWS + GitLab + not-Google, those integrations are not available to you, and Antigravity's advantages narrow considerably.

---

## Who Should Use It

**Strong fit:**
- Teams already on Firebase, Android, GCP — the integrations are uniquely valuable
- Developers who want to delegate batches of parallel tasks and review completed work
- Teams prioritizing agentic tool-use benchmarks (MCP Atlas) over raw code accuracy
- Developers who want the lowest entry price among major agentic platforms

**Weaker fit:**
- Teams working on complex backend or legacy codebases where hallucination rate is a hard constraint
- Developers who want deep IDE integration (use Cursor Composer 2.5 instead)
- Teams on AWS/Azure stacks without Google ecosystem dependencies
- Workflows requiring full automation without human review (hallucination rate too high)

---

## Verdict

Google Antigravity 2.0 is the most architecturally ambitious coding platform released in the first half of 2026. Parallel subagents, a built-in browser agent, A2A protocol support, and Gemini 3.5 Flash's 289 tok/s speed are genuine differentiators. Leading MCP Atlas at 83.6%, with a five-surface platform and deep Google ecosystem integration — this is a real product with a coherent thesis.

The launch execution undercuts the architecture. The auto-update broke existing user environments. The replacement CLI was announced without being available to install. Model labels in the interface cannot be trusted. Free tier was slashed 12.5x. These are not minor issues — they affect teams in production right now.

Revisit in 60–90 days. If the CLI ships on a package manager, the documentation catches up, and the model label issues are resolved, this moves to 4/5 on the strength of the browser agent and A2A support alone.

**Rating: 3.5/5** — Strong architecture and genuine differentiators undercut by a rocky launch execution.

*For the underlying model powering Antigravity, see our [Gemini 3.5 Flash review](/reviews/google-gemini-3-5-flash-agentic-speed-llm-review/). For the main competitor in parallel async coding, see our [OpenAI Codex Cloud review](/reviews/openai-codex-cloud-agentic-coding-platform-review/). For the IDE-integrated alternative, see our [Cursor Composer 2.5 review](/reviews/cursor-composer-2-5-coding-model-review/).*
