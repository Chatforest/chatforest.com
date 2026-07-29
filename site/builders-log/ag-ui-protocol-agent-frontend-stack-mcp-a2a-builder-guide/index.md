# AG-UI: The Missing Protocol That Completes the Agent Stack

> MCP connects agents to tools. A2A connects agents to agents. AG-UI connects agents to your frontend. Here's what the third protocol does, who supports it, when to use it, and how CopilotKit's $27M Series A signals that this layer is now production-critical.


Most builders who've adopted the Model Context Protocol know the mental model: MCP is the wire format that lets agents call tools. [Anthropic open-sourced MCP in November 2024](https://www.anthropic.com/news/model-context-protocol); it solved the agent-to-tool connection problem and [became the de facto standard for tool access within about a year](https://zuplo.com/blog/one-year-of-mcp).

A2A (Agent-to-Agent) solved the next problem: how agents delegate subtasks to other agents. [Google launched it in April 2025](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) with more than 50 partner companies signed on, [Microsoft added support in Azure AI Foundry and Copilot Studio](https://techcrunch.com/2025/05/07/microsoft-adopts-googles-standard-for-linking-up-ai-agents/) the following month, and the protocol is now governed by the [Linux Foundation](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year), which reports more than 150 participating organizations.

There's a third connection problem that didn't have a standard until recently: **how does an agent talk to the frontend in real time?**

That's what AG-UI solves. [CopilotKit shipped it as an open protocol in May 2025](https://www.copilotkit.ai/blog/introducing-ag-ui-the-protocol-where-agents-meet-users), [raised a $27 million Series A in May 2026](https://www.copilotkit.ai/blog/series-a) to build out the ecosystem around it, and by [CopilotKit's own account](https://techcrunch.com/2026/05/05/copilotkit-raises-27m-to-help-devs-deploy-app-native-ai-agents/) it now sees millions of weekly installs with adoption from Google, Microsoft, Amazon, and Oracle.

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

AG-UI is an open, lightweight, event-based protocol. It [defines a standard wire format](https://docs.ag-ui.com/introduction) for the connection between an agent backend and a frontend application.

The transport is simple: a persistent connection via [Server-Sent Events (SSE) or WebSockets carries a single ordered stream of JSON-encoded events](https://docs.ag-ui.com/introduction). Once the connection opens, everything flows through it — chat messages, tool call signals, state patches, and lifecycle markers.

There are [17 event types, organized into five categories](https://www.copilotkit.ai/blog/master-the-17-ag-ui-event-types-for-building-agents-the-right-way):

**Lifecycle events** — run start/finish, errors, and step boundaries (`RUN_STARTED`, `RUN_FINISHED`, `RUN_ERROR`, `STEP_STARTED`, `STEP_FINISHED`). Your frontend knows when the agent is working and when it's done.

**Text message events** — streaming token output (`TEXT_MESSAGE_START`, `TEXT_MESSAGE_CONTENT`, `TEXT_MESSAGE_END`). The "typing" effect you see in ChatGPT and Claude is this. Every token arrives as an event; your frontend renders incrementally without waiting for the full response.

**Tool call events** — four-step sequence: `TOOL_CALL_START` (agent is invoking a tool), `TOOL_CALL_ARGS` (streamed argument fragments as JSON), `TOOL_CALL_END` (arguments complete), `TOOL_CALL_RESULT` (the tool's return value). Your frontend can show exactly what the agent is doing and why.

**State management events** — this is the most distinctive feature. Agent and frontend share a typed state store. The agent can push a [`STATE_SNAPSHOT` (full replacement) or a `STATE_DELTA` (a JSON Patch, RFC 6902, with only the changes)](https://docs.ag-ui.com/concepts/state). Your UI stays synchronized with agent-side state without any polling or REST round-trips.

**Special events** — `RAW` and `CUSTOM`, escape hatches for passing through provider-specific data or application-defined events that don't fit the other four categories.

AG-UI doesn't have a dedicated "approval" event type. Human-in-the-loop interrupts are instead [built on top of the same tool call events](https://github.com/ag-ui-protocol/ag-ui/discussions/158): the agent emits a `TOOL_CALL_START` for a client-defined ("frontend") tool — one whose logic runs in the browser rather than the backend — and that call doesn't complete until the frontend sends back a `TOOL_CALL_RESULT` with the user's decision. The frontend renders whatever confirmation UI it wants from the tool call's arguments, the user approves or rejects, and the answer flows back as the tool's result. This is how you build agentic flows that are powerful without being unchecked.

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

AG-UI [launched as an open protocol in May 2025](https://www.copilotkit.ai/blog/introducing-ag-ui-the-protocol-where-agents-meet-users). By mid-2026, the support landscape covers the major platforms and frameworks that most production agents run on:

**Cloud platforms:**
- **Microsoft Agent Framework** — [native AG-UI integration, documented at Microsoft Learn](https://learn.microsoft.com/en-us/agent-framework/integrations/ag-ui/)
- **AWS Bedrock AgentCore Runtime** — [added AG-UI support on March 13, 2026](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-agentcore-runtime-ag-ui-protocol), handling auth and scaling at the same layer as MCP and A2A workloads
- **Google ADK (Agent Development Kit)** — [CopilotKit has published direct ADK-to-AG-UI integration guides](https://google.github.io/adk-docs/integrations/ag-ui/), and Google's own developer blog covered the [ADK + AG-UI integration](https://developers.googleblog.com/en/delight-users-by-combining-adk-agents-with-fancy-frontends-using-ag-ui/)
- **Oracle** — [added AG-UI integration for its Open Agent Specification (Agent Spec)](https://blogs.oracle.com/ai-and-datascience/announcing-ag-ui-integration-for-agent-spec)

**Agent frameworks:**
- [LangChain, Mastra, PydanticAI, Agno, and AG2 all have AG-UI integrations](https://docs.ag-ui.com/integrations)
- LlamaIndex announced AG-UI frontend integration in a [joint blog with CopilotKit](https://www.copilotkit.ai/blog/introducing-llamaindex-integration-with-copilotkit) (also [posted on the LlamaIndex blog](https://www.llamaindex.ai/blog/announcing-easy-agentic-frontends-with-ag-ui-and-copilotkit))

**Frontend:**
- [CopilotKit ships React, Angular, and React Native (mobile) bindings for AG-UI](https://github.com/copilotkit/copilotkit)
- The `@copilotkit/react-ui` + `@copilotkit/react-core` + `@copilotkit/runtime` package set is the fastest path to a working AG-UI frontend

The protocol is explicitly [framework-neutral and LLM-neutral](https://docs.ag-ui.com/introduction) — it specifies the wire format, not the implementation. If you want to use it with a custom agent runtime or a non-CopilotKit frontend, the spec is open and the [GitHub repository is public](https://github.com/ag-ui-protocol/ag-ui).

---

## CopilotKit's Funding and What It Means

CopilotKit raised $27 million in a Series A [announced May 5, 2026](https://www.copilotkit.ai/blog/series-a), led by Glilot Capital Partners, NfX, and SignalFire — [also reported independently by TechCrunch](https://techcrunch.com/2026/05/05/copilotkit-raises-27m-to-help-devs-deploy-app-native-ai-agents/). This is the company that created the AG-UI protocol.

The funding round matters because it signals two things:

First, major AI infrastructure providers have officially adopted the protocol. [CopilotKit's own announcement listed Google, Microsoft, Amazon, and Oracle](https://www.copilotkit.ai/blog/series-a), and [TechCrunch's coverage independently confirmed the same four names](https://techcrunch.com/2026/05/05/copilotkit-raises-27m-to-help-devs-deploy-app-native-ai-agents/). When those four names appear on the same announcement, a protocol has crossed the threshold from "interesting" to "likely to become infrastructure."

Second, CopilotKit is building an enterprise product layer on top of the open protocol — support contracts, self-hosted deployment options, and compliance-ready features. The protocol itself stays open. The enterprise tooling around it is the business. This is the same pattern MCP followed.

The company [reports millions of installs per week and says its tools are used in production by "the majority of the Fortune 500 and Global 50"](https://www.copilotkit.ai/blog/series-a). Those numbers are self-reported, but the adoption signal from the major cloud platforms is independent corroboration.

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

[Register your agent as an `HttpAgent` in the CopilotKit runtime](https://docs.copilotkit.ai/backend/ag-ui), and the AG-UI event stream flows automatically. CopilotKit's documentation has integration guides for every major framework.

**If you're on AWS Bedrock AgentCore Runtime:**

[AG-UI support is available natively as of the March 2026 update](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-agentcore-runtime-ag-ui-protocol). Auth and scaling are handled at the runtime layer, same as MCP and A2A connections. Check the [AgentCore Runtime documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-agui-protocol-contract.html) for the AG-UI endpoint configuration.

**If you're on Microsoft Agent Framework:**

The Agent Framework has an [AG-UI integration guide at Microsoft Learn](https://learn.microsoft.com/en-us/agent-framework/integrations/ag-ui/). The pattern is registering your AG-UI endpoint alongside your A2A and MCP endpoints in the Agent Framework manifest.

**If you're building from scratch:**

The AG-UI protocol specification is at [ag-ui.com](https://docs.ag-ui.com/introduction) and the reference implementation is open source. You can implement an AG-UI-compliant server in any language by implementing the event stream format. The spec is not large.

---

## Builder Checklist

- [ ] **Identify the connection layer gap.** If users can't see what your agent is doing in real time, that's the AG-UI gap.
- [ ] **Choose your transport.** SSE is simpler to implement and works through most proxies and CDNs. WebSockets are better if you need bidirectional low-latency communication.
- [ ] **Implement state management events** if your agent maintains any structured state that the frontend should render (not just chat output).
- [ ] **Route irreversible actions through a frontend approval tool** for any agent action that is irreversible or consequential — AG-UI implements human-in-the-loop as a [`TOOL_CALL_START`/`TOOL_CALL_RESULT` round trip to a client-defined tool](https://github.com/ag-ui-protocol/ag-ui/discussions/158), not a dedicated event type.
- [ ] **Test your event sequence.** AG-UI events are ordered and stateful — a missing `TOOL_CALL_END` or an out-of-order `STATE_DELTA` will break the frontend's rendering logic.

---

The agent protocol stack is now clearly defined: MCP for tools, A2A for agents, AG-UI for interfaces. All three are open, all three have production-grade support across the major cloud platforms, and all three can be used independently or together.

If you've built the tool access and the orchestration layers but left the frontend as a polling loop, the third protocol is ready.

