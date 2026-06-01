---
title: "Strands Agents 1.0: AWS's Open-Source Agent SDK Just Got Production-Grade Multi-Agent Orchestration"
date: 2026-06-01T20:00:00+09:00
description: "Strands Agents Python SDK 1.0 (May 21, 2026) adds multi-agent orchestration, A2A protocol support, and a remote session manager. Here's what changed, how it compares to LangGraph and the Claude Agent SDK, and when to use it."
og_description: "AWS's Strands Agents Python SDK hit 1.0 on May 21. New: four multi-agent primitives, native A2A protocol (expose or consume any A2A agent in two lines), and a session manager for remote state. The recommended framework for AgentCore deployments."
content_type: "Builder's Log"
categories: ["Developer Tools", "AWS", "Agent Frameworks"]
tags: ["strands-agents", "aws", "multi-agent", "a2a-protocol", "agentcore", "bedrock", "open-source", "python", "agent-framework", "langgraph", "crewai", "session-manager"]
---

AWS open-sourced Strands Agents in May 2025 as a simple, model-driven Python SDK for building AI agents. On May 21, 2026, version 1.0 shipped — and it changes the story from "good for single agents" to "production-ready for multi-agent systems." The TypeScript SDK hit 1.0 five weeks earlier on April 30.

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

Strands is model-agnostic by design, though Amazon Bedrock is the primary supported provider and gets the most maintenance attention.

| Provider | Class | Notes |
|---|---|---|
| Amazon Bedrock | `BedrockModel` | Best-supported; default choice |
| Anthropic direct | `AnthropicModel` | Claude models via Anthropic API |
| OpenAI | `OpenAIModel` | GPT-5.x family |
| Ollama | `OllamaModel` | Local inference |
| Any LiteLLM-supported | Via LiteLLM | 100+ providers with unified interface |

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

Pre-1.0 Strands was a single-agent framework. Version 1.0 adds four primitives for composing agents:

**1. SubAgent** — Run a Strands agent as a tool callable by another agent. The parent agent dispatches work; the child agent runs it synchronously.

**2. ParallelAgent** — Fan out the same task to multiple agents in parallel and collect results. Good for map-reduce patterns: parallel research, parallel scoring, parallel code review.

**3. Pipeline** — Chain agents sequentially where each agent's output becomes the next agent's input. Good for transformation chains (extract → classify → summarize → draft).

**4. GraphAgent** — Define conditional routing between agents based on intermediate results. The most LangGraph-like primitive; use it when you need explicit decision points in your flow.

For most teams, SubAgent and Pipeline cover 80% of multi-agent patterns. GraphAgent is the escape valve when you need explicit branching.

---

## A2A Protocol: Cross-Agent Interoperability

1.0 adds native support for the **Agent-to-Agent (A2A) protocol** — Google's open standard for agent discovery and communication. This matters if you need to connect agents across team boundaries, language runtimes, or company firewalls.

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

Any A2A-compatible client — including LangGraph agents, Claude Managed Agents, or a Strands A2AAgent — can now call this agent over HTTP.

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

Pre-1.0, agent memory reset at the end of each invocation. Version 1.0 ships a **session manager** that persists conversation state to a remote datastore between calls:

```python
from strands import Agent
from strands.session import DynamoDBSessionManager

session_manager = DynamoDBSessionManager(
    table_name="my-agent-sessions",
    session_id="user-42-project-audit",
)

agent = Agent(
    model=model,
    tools=[...],
    session_manager=session_manager,
)

# First call: fresh session, state written to DynamoDB
agent("Audit our IAM policies. Start with S3 bucket policies.")

# Later call (different process, different machine): session restored automatically
agent("Continue the audit — move on to EC2 security groups.")
```

The session manager restores the full conversation history before each call, so the agent picks up exactly where it left off. DynamoDB is the shipping implementation; the `SessionManager` interface is open for custom backends (Redis, Postgres, S3).

This is the foundation for building agents that accumulate institutional knowledge across days or weeks — the usage pattern that managed agents like AgentCore's Filesystem Persistence feature targets.

---

## MCP Integration

Strands has supported MCP since early 2025, and 1.0 doesn't change the API — but it's worth being explicit about how it works:

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

MCP tools from different servers compose naturally with native Python tools in the same `tools=[]` list. The 14,000+ servers on PulseMCP are all accessible this way.

---

## AgentCore Deployment

Strands is the AWS-recommended framework for deploying agents on Amazon Bedrock AgentCore. The pairing is designed to be seamless: Strands handles agent logic, AgentCore handles infrastructure isolation, scaling, and governance.

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

Multiple AWS services already run Strands internally:

- **Amazon Q Developer** — the agentic coding assistant
- **AWS Glue** — ETL pipeline agents
- **VPC Reachability Analyzer** — network diagnostic agents

Contributing companies include Accenture, Anthropic, Meta, PwC, Langfuse, mem0.ai, and Tavily. The open-source community around the SDK is real and growing.

---

## What to Do Now

**If you're evaluating agent frameworks:** Add Strands to the shortlist alongside LangGraph and the Claude Agent SDK. The 1.0 release closes the multi-agent gap that made it a non-starter for complex workflows.

**If you're building on AgentCore:** Use Strands. It's the path of least resistance and the framework AWS is actively investing in.

**If you have cross-team agent collaboration requirements:** The A2A integration in 1.0 is the production answer to "how do two teams share an agent without sharing credentials or code."

**If you need session continuity:** The DynamoDB session manager is production-ready. The Redis and Postgres backends are community-maintained but functional.

Install and start:

```bash
pip install strands-agents strands-agents-tools
```

Documentation: [strandsagents.com](https://strandsagents.com) — the API reference and multi-agent guides are comprehensive.
