# Strands Agents 1.0: AWS's Open-Source Agent SDK Gets Production-Grade Multi-Agent Orchestration

> Strands Agents Python SDK 1.0 (July 15, 2025) added multi-agent orchestration, A2A protocol support, and a remote session manager; the TypeScript SDK caught up to 1.0 in April 2026. Here's what changed, how it compares to LangGraph and the Claude Agent SDK, and when to use it.


AWS [open-sourced Strands Agents](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/) in May 2025 as a simple, model-driven Python SDK for building AI agents. The Python SDK [reached version 1.0 on July 15, 2025](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-1-0-production-ready-multi-agent-orchestration-made-simple/), adding multi-agent orchestration — it changed the story from "good for single agents" to "production-ready for multi-agent systems." The [TypeScript SDK reached its own 1.0 milestone](https://strandsagents.com/blog/strands-agents-typescript-v1/) on April 30, 2026, bringing the two SDKs to feature parity.

If you have an AgentCore workload, a multi-agent pipeline that needs to run across org boundaries, or an agent that needs to accumulate state across sessions, the 1.0 release directly addresses all three.

---

## The Model-Driven Philosophy

Strands bets on a specific architecture: you define a **prompt** and a list of **tools**, and the LLM decides the execution path. There is no explicit graph, no node/edge definition, no router logic you maintain.

```python
from strands import Agent
from strands_tools import use_aws, http_request

agent = Agent(
    system_prompt="You are a deployment assistant.",
    tools=[use_aws, http_request],
)

result = agent("Check the health of our prod ECS services and file a ticket if any are degraded.")
```

That's the full agent. The model calls whichever tools it decides to call, in whatever order, until the task is done or it gives up.

The tradeoff is real: this approach gives you less fine-grained control than LangGraph's explicit graph. You cannot force a specific sequence without embedding that logic in your system prompt or tools. In exchange, you write significantly less orchestration code.

---

## Model Provider Flexibility

Strands is [model-agnostic by design](https://strandsagents.com/docs/user-guide/concepts/model-providers/), though Amazon Bedrock is the primary supported provider and gets the most maintenance attention.

| Provider | Class | Notes |
|---|---|---|
| Amazon Bedrock | `BedrockModel` | Best-supported; default choice |
| Anthropic direct | `AnthropicModel` | Claude models via Anthropic API |
| OpenAI | `OpenAIModel` | GPT-5.x family |
| Ollama | `OllamaModel` | Local inference |
| Any LiteLLM-supported | Via LiteLLM | [100+ providers](https://github.com/BerriAI/litellm) with unified interface |

Switching models does not require changing agent code — only the model object:

```python
from strands import Agent
from strands.models import BedrockModel, AnthropicModel

# Switch without touching tool definitions or agent logic
model = BedrockModel(model_id="us.anthropic.claude-opus-4-8-v1:0")
# or
model = AnthropicModel(model_id="claude-opus-4-8-20260528")

agent = Agent(model=model, tools=[...])
```

The practical caveat: if you are not planning to deploy on AWS, the `AnthropicModel` and `OpenAIModel` providers work but receive fewer updates than `BedrockModel`. Evaluate your hosting target before committing.

---

## What's New in 1.0: Multi-Agent Orchestration

Pre-1.0 Strands was a single-agent framework. Version 1.0 added composable [multi-agent patterns](https://strandsagents.com/docs/user-guide/concepts/multi-agent/multi-agent-patterns/):

**1. [Agents-as-Tools](https://strandsagents.com/docs/user-guide/concepts/multi-agent/agents-as-tools/)** — Not a separate class: wrap a specialized agent with the ordinary `@tool` decorator so an orchestrator agent can call it. The orchestrator dispatches work; the tool agent runs it and returns a result.

**2. [Swarm](https://strandsagents.com/docs/user-guide/concepts/multi-agent/swarm/)** — A collaborative team of agents that hand off to each other autonomously: each agent's structured output can name the next agent to hand off to (or end the swarm and return a final response). Good for open-ended collaborative problem-solving.

**3. [Workflow](https://strandsagents.com/docs/user-guide/concepts/multi-agent/workflow/)** — A developer-defined task graph (DAG), shipped in the separate `strands-agents-tools` package, that an agent creates, starts, and monitors as a single non-conversational tool action. Good for transformation pipelines (extract → classify → summarize → draft).

**4. [Graph](https://strandsagents.com/docs/user-guide/concepts/multi-agent/graph/)** — Deterministic, developer-defined orchestration where agents (or nested Swarms/Graphs) are nodes connected by edges, with output from one node feeding the next; cyclic graphs are supported. The most LangGraph-like primitive; use it when you need explicit, rule-based decision points.

For most teams, Agents-as-Tools and Swarm cover the bulk of day-to-day multi-agent patterns. Graph is the escape valve when you need deterministic, explicit branching.

---

## A2A Protocol: Cross-Agent Interoperability

1.0 adds [native support](https://strandsagents.com/docs/user-guide/concepts/multi-agent/agent-to-agent/) for the **Agent-to-Agent (A2A) protocol** — an open standard for agent discovery and communication [originally introduced by Google in April 2025](https://developers.googleblog.com/en/google-cloud-donates-a2a-to-linux-foundation/) and [donated to the Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents) that June, where it's now vendor-neutral and community-governed. This matters if you need to connect agents across team boundaries, language runtimes, or company firewalls.

### Exposing a Strands agent as an A2A server

```python
from strands import Agent
from strands.multiagent.a2a import A2AServer
from strands_tools import file_read, code_interpreter

agent = Agent(
    system_prompt="You are a Python code reviewer.",
    tools=[file_read, code_interpreter],
)

# Wrap with A2A server — exposes a FastAPI/Starlette app
server = A2AServer(agent)
app = server.app  # Mount in any ASGI host
```

Any A2A-compatible client — including agents built on other frameworks or a Strands `A2AAgent` — can now call this agent over HTTP.

### Consuming a remote A2A agent

```python
from strands.agent import A2AAgent

# The remote agent appears as a local callable
review_agent = A2AAgent(url="https://review-service.internal/a2a")

result = review_agent("Review the attached diff and flag any security issues.")
```

The `A2AAgent` handles authentication, serialization, and streaming transparently. The calling agent does not know or care whether the downstream agent is a Strands agent, a LangGraph node, or a custom implementation.

This is the primary mechanism for building inter-team or inter-company agent pipelines without sharing model access, credentials, or code.

---

## Session Manager: Persistent State Across Runs

Pre-1.0, agent memory reset at the end of each invocation. Version 1.0 ships a [**session manager**](https://strandsagents.com/docs/user-guide/concepts/agents/session-management/) that persists conversation state to a remote datastore between calls:

```python
from strands import Agent
from strands.session.s3_session_manager import S3SessionManager

session_manager = S3SessionManager(
    session_id="user-42-project-audit",
    bucket="my-agent-sessions",
)

agent = Agent(
    model=model,
    tools=[...],
    session_manager=session_manager,
)

# First call: fresh session, state written to S3
agent("Audit our IAM policies. Start with S3 bucket policies.")

# Later call (different process, different machine): session restored automatically
agent("Continue the audit — move on to EC2 security groups.")
```

The session manager restores the full conversation history before each call, so the agent picks up exactly where it left off. The SDK ships `FileSessionManager` (local disk, for development) and [`S3SessionManager`](https://strandsagents.com/docs/api/python/strands.session.s3_session_manager/) (for production and distributed deployments) out of the box; the `SessionManager` interface is open for custom backends.

This is the foundation for building agents that accumulate institutional knowledge across days or weeks — the usage pattern that managed agents like [AgentCore's filesystem persistence feature](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-persistent-filesystems.html) (preview) also target.

---

## MCP Integration

Strands has [supported MCP since its May 2025 launch](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/), and 1.0 doesn't change the API — but it's worth being explicit about how it works:

```python
from strands import Agent
from strands.tools.mcp import MCPClient

# Connect to any MCP server
jira_client = MCPClient(server_url="http://localhost:3000/mcp")

agent = Agent(
    system_prompt="You are a project manager agent.",
    tools=jira_client.get_tools(),  # Auto-discovers all MCP tools
)
```

MCP tools from different servers compose naturally with native Python tools in the same `tools=[]` list. The [tens of thousands of servers indexed by PulseMCP](https://www.pulsemcp.com/servers) are all accessible this way.

---

## AgentCore Deployment

Strands is [AWS's own reference framework for deploying agents on Amazon Bedrock AgentCore](https://strandsagents.com/docs/user-guide/deploy/deploy_to_bedrock_agentcore/), and [AWS's production blueprint for evaluating agents](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-a-production-blueprint-with-strands-and-agentcore/) pairs the two by default — though AgentCore's runtime also supports other open-source frameworks such as LangChain, LangGraph, and CrewAI. The pairing is designed to be seamless: Strands handles agent logic, AgentCore handles infrastructure isolation, scaling, and governance.

```python
# Same Strands agent code — AgentCore wraps the runtime
from strands import Agent
from strands_tools import use_aws

agent = Agent(
    system_prompt="You are a cloud cost optimizer.",
    tools=[use_aws],
)

# AgentCore sessions invoke this agent in isolated per-session microVMs
response = agent("Analyze the top 10 cost drivers across our AWS accounts.")
```

There's nothing AWS-specific you need to add to your Strands agent for AgentCore compatibility — the managed harness calls your agent the same way you would locally. This is the main advantage over writing AgentCore-specific orchestration code.

---

## Decision Matrix: When to Use Strands

| Scenario | Recommended Framework |
|---|---|
| AWS-native deployment, Bedrock models, AgentCore | **Strands** |
| Explicit control flow required (conditional branching, retry logic) | **LangGraph** |
| Fully managed orchestration with no infrastructure ownership | **Claude Managed Agents** |
| Role-based multi-agent teams, CrewAI persona model | **CrewAI** |
| Claude API only, Anthropic SDK | **Claude Agent SDK** |
| Multi-team or multi-company agent pipelines | **Strands + A2A** |
| Model-agnostic, needs to run locally or on any cloud | **Strands** |

Strands is the right choice when you want a framework that is genuinely model-agnostic (swap Bedrock for Anthropic without touching agent logic), has first-class MCP support, and plugs directly into the AWS deployment stack. It's the wrong choice when your workflow requires explicit branching logic that you don't want to encode in the LLM's reasoning.

---

## Production Usage

At launch, [AWS said multiple internal teams were already running Strands in production](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/):

- **Amazon Q Developer** — the agentic coding assistant
- **AWS Glue** — ETL pipeline agents
- **VPC Reachability Analyzer** — network diagnostic agents

That [same announcement named early supporting companies](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/): Accenture, Anthropic, Langfuse, mem0.ai, Meta, PwC, Ragas.io, and Tavily.

---

## What to Do Now

**If you're evaluating agent frameworks:** Add Strands to the shortlist alongside LangGraph and the Claude Agent SDK. The 1.0 release closes the multi-agent gap that made it a non-starter for complex workflows.

**If you're building on AgentCore:** Use Strands. It's the path of least resistance and the framework AWS is actively investing in.

**If you have cross-team agent collaboration requirements:** The A2A integration in 1.0 is the production answer to "how do two teams share an agent without sharing credentials or code."

**If you need session continuity:** The built-in `S3SessionManager` and `FileSessionManager` are production-ready. A [community-maintained catalog](https://strandsagents.com/docs/community/community-packages/) also lists a Valkey/Redis session manager and an Amazon Bedrock AgentCore Memory session manager if you need a different backend.

Install and start:

```bash
pip install strands-agents strands-agents-tools
```

Documentation: [strandsagents.com](https://strandsagents.com) — the API reference and multi-agent guides are comprehensive.

