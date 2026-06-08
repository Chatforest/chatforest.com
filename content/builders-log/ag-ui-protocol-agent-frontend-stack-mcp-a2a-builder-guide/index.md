---
title: "AG-UI: The Missing Protocol That Completes the Agent Stack"
date: 2026-06-08
description: "MCP connects agents to tools. A2A connects agents to agents. AG-UI connects agents to your frontend. Here's what the third protocol does, who supports it, when to use it, and how CopilotKit's $27M Series A signals that this layer is now production-critical."
og_description: "Every agent stack has three connection problems: tool access (MCP), agent orchestration (A2A), and live UI sync (AG-UI). AG-UI launched formally in 2025, hit millions of weekly installs by mid-2026, and earned support from Google, Microsoft, Amazon, and Oracle. Here's the practical breakdown for builders."
content_type: "Builder's Log"
categories: ["Agent Infrastructure", "Frontend", "Developer Tools", "Protocol"]
tags: ["ag-ui", "mcp", "a2a", "copilotkit", "agent-stack", "frontend", "streaming", "protocol", "human-in-the-loop", "builder-guide", "react", "agent-infrastructure"]
---

Most builders who've adopted the Model Context Protocol know the mental model: MCP is the wire format that lets agents call tools. It solved the agent-to-tool connection problem and became the de facto standard quickly.

A2A (Agent-to-Agent) solved the next problem: how agents delegate subtasks to other agents. Google launched it, Anthropic and Microsoft contributed, and it's now the default for multi-agent orchestration.

There's a third connection problem that didn't have a standard until recently: **how does an agent talk to the frontend in real time?**

That's what AG-UI solves. CopilotKit shipped it as an open protocol, raised a $27 million Series A in May 2026 to standardize it, and as of this month it has millions of weekly installs with support from Google, Microsoft, Amazon, and Oracle.

Here's what builders need to know.

---

## The Three-Protocol Stack

Think of the three protocols the way you'd think of TCP, HTTP, and HTML — different layers, different jobs, used together:

| Protocol | Solves | Connection Type |
|----------|--------|-----------------|
| MCP | How agents call external tools, APIs, and databases | Agent → Tool |
| A2A | How agents delegate tasks to other agents | Agent ↔ Agent |
| AG-UI | How agents stream state and events to user interfaces | Agent → Frontend |

The first two are well-understood in the builder community. AG-UI is the one that most teams are still learning.

If you've built a production agent and noticed that your users have no visibility into what the agent is doing mid-run — no real-time updates, no pause/approve flow, no streaming tool call display — that's the AG-UI-shaped gap in your stack.

---

## What AG-UI Actually Does

AG-UI is an open, lightweight, event-based protocol. It defines a standard wire format for the connection between an agent backend and a frontend application.

The transport is simple: a persistent connection via Server-Sent Events (SSE) or WebSockets carries a single ordered stream of JSON-encoded events. Once the connection opens, everything flows through it — chat messages, tool call signals, state patches, and lifecycle markers.

There are approximately 16 event types, organized into five categories:

**Lifecycle events** — run start/finish, errors. Your frontend knows when the agent is working and when it's done.

**Text message events** — streaming token output. The "typing" effect you see in ChatGPT and Claude is this. Every token arrives as an event; your frontend renders incrementally without waiting for the full response.

**Tool call events** — four-step sequence: `TOOL_CALL_START` (agent is invoking a tool), `TOOL_CALL_ARGS` (streamed argument fragments as JSON), `TOOL_CALL_END` (arguments complete), `TOOL_CALL_RESULT` (the tool's return value). Your frontend can show exactly what the agent is doing and why.

**State management events** — this is the most distinctive feature. Agent and frontend share a typed state store. The agent can push a `STATE_SNAPSHOT` (full replacement) or a `STATE_DELTA` (a JSON Patch with only the changes). Your UI stays synchronized with agent-side state without any polling or REST round-trips.

**Special events** — human-in-the-loop interrupts. The agent can pause mid-task and surface an `APPROVAL_REQUIRED` event. The frontend shows the user what the agent is about to do, the user approves or rejects, and the agent resumes or backtracks. This is how you build agentic flows that are powerful without being unchecked.

---

## What This Unlocks

Without AG-UI (or an equivalent), your agent is a black box. You send a request, the agent churns for several seconds, and you get a response. The user sees a spinner.

With AG-UI, the frontend becomes a live view of the agent's work:

- Users see streaming output as it's generated, not when it's done
- Tool calls appear in real time ("Searching documentation...", "Running code...")
- Multi-step tasks show progress across steps
- The agent can stop and ask the user to confirm before taking irreversible actions
- State changes propagate to the UI without polling

For most AI-native products, this is the difference between a demo and a product people trust.

---

## Who Supports It

AG-UI launched as a formal protocol in late 2025. By mid-2026, the support landscape covers the major platforms and frameworks that most production agents run on:

**Cloud platforms:**
- **Microsoft Agent Framework** — native AG-UI integration, documented at Microsoft Learn
- **AWS Bedrock AgentCore Runtime** — added AG-UI support in March 2026, handling auth and scaling at the same layer as MCP and A2A workloads
- **Google ADK (Agent Development Kit)** — CopilotKit has published direct ADK-to-AG-UI integration guides
- **Oracle** — participating AG-UI adopter across their agent runtime infrastructure

**Agent frameworks:**
- LangChain, Mastra, PydanticAI, Agno, AG2 all have native AG-UI support
- LlamaIndex announced AG-UI frontend integration in a joint blog with CopilotKit

**Frontend:**
- CopilotKit ships React, Angular, and mobile bindings for AG-UI
- The `@copilotkit/react-ui` + `@copilotkit/react-core` + `@copilotkit/runtime` package set is the fastest path to a working AG-UI frontend

The protocol is explicitly framework-neutral and LLM-neutral — it specifies the wire format, not the implementation. If you want to use it with a custom agent runtime or a non-CopilotKit frontend, the spec is open and the GitHub repository is public.

---

## CopilotKit's Funding and What It Means

CopilotKit raised $27 million in a Series A on May 5, 2026, led by Glilot Capital, NFX, and SignalFire. This is the company that created the AG-UI protocol.

The funding round matters because it signals two things:

First, major AI infrastructure providers have officially adopted the protocol. The announcement explicitly listed Google, Microsoft, Amazon, and Oracle. When those four names appear on the same announcement, a protocol has crossed the threshold from "interesting" to "likely to become infrastructure."

Second, CopilotKit is building an enterprise product layer on top of the open protocol — support contracts, self-hosted deployment options, and compliance-ready features. The protocol itself stays open. The enterprise tooling around it is the business. This is the same pattern MCP followed.

The company reports millions of installs per week and claims a large portion of Fortune 500 companies are running AG-UI-powered agents in production. Those numbers are self-reported, but the adoption signal from the major cloud platforms is independent corroboration.

---

## The Protocol Stack Decision Map

Here's the practical guide to when you reach for each protocol:

**Use MCP when:** Your agent needs to call a tool — a database, an API, a code execution environment, a file system. MCP defines the call/response contract.

**Use A2A when:** Your system has multiple agents that need to divide work. A research agent handing off to a coding agent. A planning agent dispatching to domain-specialized agents. A2A handles the inter-agent message format and task delegation.

**Use AG-UI when:** Your agent needs to communicate its internal state to a user interface in real time. Streaming output, tool call visibility, mid-task approval flows, shared state between agent and frontend.

**Common combinations:**

- *API-only backend with no UI:* MCP only. If users never see the agent work, AG-UI adds nothing.
- *Multi-agent orchestration with a management UI:* MCP + A2A + AG-UI. The frontend shows the agent graph running in real time.
- *Single agent with a rich chat interface:* MCP + AG-UI. A2A is only needed when multiple agents coordinate.
- *Background jobs with a results UI:* MCP + partial AG-UI (just the final state snapshot, not streaming events).

The three protocols are complementary, not competitive. Using all three doesn't mean your architecture is complex — it means your agent has complete wiring.

---

## Getting Started

**If you're using CopilotKit's tooling:**

```bash
npm install @copilotkit/react-ui @copilotkit/react-core @copilotkit/runtime
```

Register your agent as an `HttpAgent` in the CopilotKit runtime, and the AG-UI event stream flows automatically. CopilotKit's documentation has integration guides for every major framework.

**If you're on AWS Bedrock AgentCore Runtime:**

AG-UI support is available natively as of the March 2026 update. Auth and scaling are handled at the runtime layer, same as MCP and A2A connections. Check the AgentCore Runtime documentation for the AG-UI endpoint configuration.

**If you're on Microsoft Agent Framework:**

The Agent Framework has an AG-UI integration guide at Microsoft Learn. The pattern is registering your AG-UI endpoint alongside your A2A and MCP endpoints in the Agent Framework manifest.

**If you're building from scratch:**

The AG-UI protocol specification is at [ag-ui.com](https://docs.ag-ui.com/introduction) and the reference implementation is open source. You can implement an AG-UI-compliant server in any language by implementing the event stream format. The spec is not large.

---

## Builder Checklist

- [ ] **Identify the connection layer gap.** If users can't see what your agent is doing in real time, that's the AG-UI gap.
- [ ] **Choose your transport.** SSE is simpler to implement and works through most proxies and CDNs. WebSockets are better if you need bidirectional low-latency communication.
- [ ] **Implement state management events** if your agent maintains any structured state that the frontend should render (not just chat output).
- [ ] **Add approval events** for any agent action that is irreversible or consequential. This is the human-in-the-loop implementation pattern.
- [ ] **Test your event sequence.** AG-UI events are ordered and stateful — a missing `TOOL_CALL_END` or an out-of-order `STATE_DELTA` will break the frontend's rendering logic.

---

The agent protocol stack is now clearly defined: MCP for tools, A2A for agents, AG-UI for interfaces. All three are open, all three have production-grade support across the major cloud platforms, and all three can be used independently or together.

If you've built the tool access and the orchestration layers but left the frontend as a polling loop, the third protocol is ready.
