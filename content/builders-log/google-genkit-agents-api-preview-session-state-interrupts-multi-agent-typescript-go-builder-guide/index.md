---
title: "Google Genkit Agents API Preview: Session State, Human Approval Interrupts, and Multi-Agent Delegation for TypeScript and Go"
description: "Google shipped Genkit's Agents API preview on July 1, 2026, bundling session management, tool execution loops, streaming, human approval interrupts, detached long-running jobs, and multi-agent delegation behind a single chat() interface. Here is what the API actually does and when to reach for it."
date: 2026-07-11
lastmod: 2026-07-11
categories: ["builders-log"]
tags: ["genkit", "google", "agents", "session-state", "human-in-the-loop", "multi-agent", "typescript", "go", "open-source", "agent-infrastructure", "streaming"]
---

Google shipped the **Genkit Agents API** in preview on July 1, 2026, adding session management, streaming, human approval interrupts, and multi-agent delegation to the open-source Genkit framework for TypeScript and Go.

Genkit has been around since 2024 as a Google-maintained framework for building AI-powered apps. The Agents API is a significant extension: it moves Genkit from a request/response flow runner into something closer to a full-stack agent runtime. The framework already supports TypeScript, Go, Python, and Dart. The new Agents API is TypeScript and Go only for now — Python and Dart users do not get it yet.

---

## What Genkit was solving before

The core problem Genkit addresses is plumbing. Building an agent manually means wiring together at minimum: message history storage, a tool execution loop, retry logic when tools fail, streaming from the model to the client, and some form of persistence across turns. If you want the agent to be stateful across sessions, you add a database. If you want human approval before a destructive action, you write interruption middleware. If you want multiple agents to hand off work to each other, you write routing logic.

This is not hard work, but it is dense work, and every team ends up writing largely the same plumbing in slightly different ways.

The Agents API bundles that plumbing behind one interface.

---

## The `chat()` interface

The central API surface is `chat()`. You define an agent with a system prompt and a list of tools; you serve it over HTTP with a built-in route handler; you call it from a frontend or another service using the same `chat()` call whether the agent is running in-process or behind a network boundary.

The same interface works both locally (in-process, useful for tests) and remotely (over HTTP, useful for production). The agent's TypeScript or Go code does not change depending on which mode you are using — the routing is transparent.

This matters most in multi-agent setups. When your orchestrator delegates to a specialist, it does not care whether that specialist runs in the same process or is deployed as a separate service. `remoteAgent()` exposes an external agent as if it were local.

---

## Session state: two models

The API ships two persistence patterns. You choose based on where you want state to live.

### Server-managed

The server owns the session store. Every turn, the framework writes a snapshot — message history, custom typed data, and any generated artifacts — to a backend store. The client reconnects by session ID.

Built-in store options:
- **In-memory**: for tests and single-process demos
- **File**: for local development and single-host apps
- **Firestore**: for production apps on Google Cloud or Firebase
- **Custom**: implement the interface against any database you already run

Session IDs are stable across reconnects. The API also supports snapshot IDs — you can branch from a specific past turn without altering the original thread. This is useful for "undo" flows and for letting users explore alternative paths from a decision point without overwriting the canonical history.

### Client-managed

The server returns the full session state on every response. The client sends it back on the next request. No server-side database required.

Client-managed suits stateless deployments where you cannot or do not want to add a persistence dependency, or when you have an existing session layer (a Redis store, a database record, a mobile SDK's local state) and want to own the write path.

---

## Human approval interrupts

This is the feature with the most security surface area, and Genkit's implementation is careful.

Any tool can pause the agent by returning an `Interrupt` instead of a normal result. The `Interrupt` carries a description of what decision is pending and any data the human needs to review. The turn completes with an `interrupted` reason code. Nothing else executes.

The client renders the interrupt to the user — show the pending action, prompt for approval, rejection, or a corrected value. When the user responds, the client resumes the session with the approval payload.

The security mechanism: the runtime validates the resume payload against session history. A client cannot forge an approval for an interrupt that was never issued. A tool cannot be fed a crafted payload that convinces it a different action was approved. The validation runs before any tool code executes on the resumed turn.

This matters for the use cases where interrupts are most needed: payment confirmation, infrastructure changes, email sending, code deployment. In all these cases the threat model includes a compromised or buggy client trying to skip approval or approve the wrong action.

---

## Detached execution

Some agent tasks run longer than a reasonable HTTP request timeout. Research jobs, multi-step planning loops, long tool chains — these can run for minutes.

The Agents API supports detached sessions. The client starts a job and immediately receives a snapshot ID. The agent continues running server-side. The client can close the connection entirely. Later, the client polls or reconnects by snapshot ID to retrieve results or the current intermediate state.

This closes a gap that was painful to close manually. Without it, builders either blocked on long HTTP connections, implemented their own job queues, or broke work into explicit step APIs.

---

## Multi-agent delegation

Genkit's agents can delegate to other agents as tools. You define specialist agents (a research agent, a code agent, a summarization agent). You define an orchestrator with access to all of them via the `agents()` middleware, which injects a delegation tool for each sub-agent into the orchestrator's tool list.

The orchestrator model sees the specialist agents as callable tools. It decides which specialist to invoke and with what context. Specialist outputs flow back into the parent session. The final answer can synthesize across multiple specialists without the caller knowing how the work was distributed.

Specialists can themselves be remote agents — separate deployed services, not in-process functions. The orchestrator does not distinguish between local and remote specialists at call time.

---

## Genkit Dev UI

The framework ships a local developer interface that loads automatically when you run Genkit in development mode. It lets you inspect session snapshots, trigger turns manually, examine tool call history, and step through agent logic without writing a frontend. The UI also surfaces interrupt states so you can test the approval flow without a real client.

This is useful for validating that your interrupt conditions fire correctly before you hook up a production UI.

---

## How this compares

Builders evaluating Genkit's Agents API against alternatives should note a few differences.

**vs. Claude SDK (Anthropic)**: The Claude SDK handles tool use and streaming but does not provide session persistence, multi-agent delegation middleware, or interrupt machinery. You build those. Genkit's Agents API provides all of them. The tradeoff is model flexibility — Genkit works with Gemini, Claude, OpenAI, and other models; the Anthropic SDK is Claude-specific.

**vs. OpenAI Agents SDK**: OpenAI's Agents SDK ships handoffs and tools but targets Python first and has lighter support for session branching. Genkit targets TypeScript and Go developers and ships production-ready Firestore integration.

**vs. Google Agent Development Kit (ADK)**: This is the most important distinction. Genkit's Agents API is a framework primitive for building agents yourself. Google's ADK is a managed multi-agent orchestration platform — a higher-level product aimed at running agent fleets on Google Cloud. These are complementary, not competing: you might build individual agents with Genkit and orchestrate them with ADK, or skip ADK entirely and use Genkit's built-in multi-agent delegation for smaller setups.

---

## Limitations at preview

The Agents API is in preview. Google says it "can introduce breaking changes in minor version releases." Build on it, but do not ship without a plan to handle minor-version upgrades.

Python and Dart Genkit users do not have the Agents API yet. If your stack is Python, you are writing the session and interrupt plumbing yourself for now.

Firestore is the only production-grade built-in session store at launch. If you run on a non-Google stack, you implement the custom store interface — it is not large, but it is work.

---

## What to do now

If you are building in TypeScript or Go and your agents need any of the following — session memory across turns, human approval before destructive actions, tasks that run longer than a web request, or multiple specialized sub-agents working together — the Genkit Agents API is worth evaluating now.

The framework is open-source at [github.com/genkit-ai/genkit](https://github.com/genkit-ai/genkit). The official documentation is at [genkit.dev](https://genkit.dev). The July 1 announcement blog is at [developers.googleblog.com](https://developers.googleblog.com/build-agentic-full-stack-apps-with-genkit/).

The preview caveat is real, but the problems it solves — session persistence, interrupt-safe approval flows, transparent local/remote agent routing — are real too, and the alternatives are all custom plumbing.

---

*ChatForest covers AI tools and infrastructure for builders. This article is based on Google's public announcement, documentation, and technical writeups. We have not built a production system with the Genkit Agents API.*
