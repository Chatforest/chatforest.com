# Agent Control Standard: The Runtime Governance Layer Your Production Agents Are Missing

> ACS launched May 27 as an Apache 2.0 open standard for governing AI agents at runtime — the layer between MCP (how agents communicate) and what they're actually allowed to do. Here's what it is, how the Guardian Agent pattern works, and whether builders should adopt it now.


On May 27, 2026, a new open standard called the Agent Control Standard (ACS) launched at the AI Agent Security Summit in San Francisco. The press release was brief. The GitHub repo is sparse. But the problem it's solving is real — and builders shipping agents to production should understand it before their enterprise customers do.

## The Gap ACS Is Filling

The AI agent ecosystem has built excellent protocol layers for *communication*: MCP standardizes how agents discover and call tools. A2A (Agent-to-Agent) handles how agents hand off tasks. OpenAPI and AsyncAPI describe the surfaces agents work against.

What the ecosystem lacked was a shared standard for *control* — for answering the question "what is this agent allowed to do right now, in this context, against these systems?"

Michael Bargury, CTO of Zenity and ACS co-creator, framed it directly: "The industry has standardized how agents communicate, but not the control layer."

That gap matters because agents are increasingly running in production with real permissions. An agent that can call your CRM, execute code, store memory, and invoke sub-agents needs more than authentication — it needs policy enforcement that runs *inline*, before actions reach production systems.

## How ACS Works: The Guardian Agent Pattern

ACS defines standardized **middleware hooks** at every agent decision point. When an agent:
- receives input
- calls a tool
- selects tools from a catalog
- transitions from planning to execution
- stores memory
- executes code
- invokes a sub-agent

...ACS fires a hook. A **Guardian Agent** intercepts the action, evaluates it against policy, and returns a verdict:

- **Allow** — action proceeds normally
- **Deny** — action is blocked, agent is notified
- **Modify** — action is transformed (e.g., parameters redacted, scope narrowed) before it executes

This is different from tool-level authentication. Authentication asks "can this agent call this tool at all?" ACS asks "should this specific call, with these specific parameters, at this moment in this workflow, be allowed to execute?"

The Guardian Agent can apply arbitrary policy: static rules, OPA/Rego policies, ML-based anomaly detection, or human-in-the-loop approval queues. The ACS spec is policy-engine agnostic — it defines the hook contract, not what runs behind the hook.

## What ACS Is Not

Before building on it, understand the scope:

**Not a replacement for authentication.** ACS hooks fire after authentication succeeds. Your agent still needs OAuth scopes, API keys, and tool-level permissions.

**Not a logging or observability layer.** ACS is about enforcement, not visibility. It fires synchronously in the action path and must return before the agent proceeds.

**Not MCP-native.** ACS is framework-agnostic. The reference implementation wraps agent frameworks (LangGraph, Agno, CrewAI, the Claude Agent SDK), but there's no MCP-level spec integration yet.

**Not an enterprise product.** ACS is Apache 2.0, community-governed. Zenity contributes significantly, but no single company owns it. The `agentcontrol/agent-control` GitHub repo is the reference control plane.

## The Current State of the Standard

As of May 30, 2026, ACS is early. What exists:

- **The spec**: Hook definitions, verdict schema, Guardian Agent interface — available at `agentcontrolstandard.ai`
- **Reference control plane**: `github.com/agentcontrol/agent-control` — described as "production-ready" but still light on integrations
- **No major framework native support yet**: LangGraph, AutoGen, and the Claude Agent SDK don't have first-class ACS hooks. Wrappers exist but require manual integration

The launch timing (post-Google I/O, post-Code with Claude London) is deliberate. The enterprise conversation about agent governance is accelerating, and ACS is positioning itself as the neutral, vendor-agnostic alternative to each platform building its own control layer.

## Who Should Pay Attention Now

**Enterprise builders shipping agents with elevated permissions** — if your agents can write to CRMs, execute database queries, or trigger workflows that cost money, you need some version of this problem solved. ACS is one answer; every major platform also has proprietary solutions.

**Platform teams evaluating agent governance requirements** — your enterprise customers will ask about runtime controls. ACS gives you a reference architecture to evaluate against, even if you don't adopt the standard itself.

**Security teams** — the Guardian Agent pattern maps cleanly onto existing security concepts (policy engines, inline enforcement, audit trails). ACS gives security teams a framework to review agent behavior using familiar vocabulary.

**Builders on public frameworks** — if you're using LangGraph, CrewAI, or AutoGen in production, check whether they're planning native ACS support. If they are, ACS adoption cost drops significantly.

## Who Should Wait

**Builders in development or early staging** — the spec is too new. Build governance into your architecture by wrapping tool calls behind a policy-checkable interface, but don't build against ACS's specific hook schema until the integration landscape matures.

**Claude Agent SDK users** — no native integration exists yet. You'd need to wrap the SDK manually, which adds latency and complexity without framework-level guarantees.

**Builders on proprietary platforms** (Salesforce Agentforce, ServiceNow Agent SDK, AWS Bedrock Agents) — these platforms have their own governance layers that won't adopt ACS. Build against their native controls.

## What to Watch

The immediate signals that would accelerate ACS adoption:

1. **Native framework integrations** — if LangGraph or the Claude Agent SDK ships first-class ACS hook support, adoption friction drops sharply
2. **Enterprise product announcements** — Zenity and others will likely offer commercial Guardian Agent implementations; the standard itself stays open, the enforcement layer can be commercial
3. **MCP integration spec** — a hook that fires when an MCP tool is called would make ACS relevant to every builder using the MCP ecosystem
4. **CISA or NIST reference** — if the US government's AI security guidance starts referencing ACS-compatible controls, enterprise adoption becomes mandatory rather than optional

## The Architectural Takeaway

Even if you don't adopt ACS, the pattern it defines is sound. Builders should:

1. **Wrap tool calls** behind a single entry point in your agent code — one function that dispatches all external actions. This is where you'd insert ACS hooks, your own policy checks, or audit logging.
2. **Separate planning from execution** — ACS's planning-to-execution transition hook is interesting because it gives you a natural point to apply human-in-the-loop review before your agent starts acting.
3. **Treat memory writes as actions** — ACS fires on memory storage. Most builders don't audit memory writes at all. They should.

MCP solved "how do agents talk to tools." ACS is attempting to solve "what are agents allowed to say." The standard is early, the tooling is sparse, and the community is small — but the problem is real and enterprise customers are going to start asking for it.

---

*ACS launched May 27, 2026. The spec and reference implementation are at [agentcontrolstandard.ai](https://agentcontrolstandard.ai/) and [github.com/agentcontrol/agent-control](https://github.com/agentcontrol/agent-control). This article reflects the state of the standard as of May 30, 2026.*

