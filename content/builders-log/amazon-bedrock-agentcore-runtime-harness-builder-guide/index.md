---
title: "Amazon Bedrock AgentCore: AWS's Answer to the Agent Deployment Problem"
date: 2026-06-01
description: "AWS launched Amazon Bedrock AgentCore in April 2026 — a managed platform that handles the infrastructure complexity of running AI agents at scale: per-session microVM isolation, 8-hour session limits, filesystem persistence, and a managed harness that removes orchestration boilerplate. Here's what it does, how pricing works, and when to use it."
og_description: "AWS's AgentCore gives each agent session its own microVM with isolated CPU, memory, and filesystem. CPU billing stops during I/O wait. Sessions run up to 8 hours. Works with any framework. Here's what builders need to know."
content_type: "Builder's Log"
categories: ["AWS", "Agent Infrastructure", "Developer Tools"]
tags: ["aws", "amazon", "bedrock", "agentcore", "agents", "runtime", "microvm", "infrastructure", "production-ai", "langgraph", "crewai", "llamaindex", "strands", "enterprise"]
---

AWS launched Amazon Bedrock AgentCore in preview at the "What's Next with AWS 2026" event in late April 2026. The announcement landed quietly — overshadowed by the OpenAI-on-Bedrock news from the same event — but for builders shipping production agents, AgentCore solves a harder problem.

The hard problem is not building an agent. It's running one in production for real users, at scale, without building the infrastructure layer yourself.

---

## What AgentCore Actually Is

AgentCore is a managed platform for deploying and operating AI agents. It is not a framework and not an orchestration library. It sits between your agent code and AWS infrastructure, handling:

- **Session isolation**: each user session gets its own microVM with separate CPU, memory, and filesystem. When the session ends, the microVM is wiped. Two users running the same agent can never see each other's data.
- **Session duration**: agents can run for up to **8 hours** per session, compared to AWS Lambda's 15-minute hard limit. This matters for tasks that involve iterative research, long file processing, or multi-stage workflows.
- **State persistence**: filesystem persistence (preview) externalizes local session state, letting agents suspend mid-task and resume exactly where they left off.
- **Managed execution**: the managed harness runs the full agent loop — reasoning, tool selection, action execution, response streaming — with no orchestration code required from you.

AgentCore works with any AI framework: CrewAI, LangGraph, LlamaIndex, Strands Agents, or custom code. It also works with any foundation model on Bedrock, and now with OpenAI models on Bedrock (GPT-5.5, GPT-5.4) in limited preview.

---

## The Managed Harness

The April 2026 update added a managed harness to AgentCore Runtime. To use it, you specify three things:

1. A model (any Bedrock-compatible model ID)
2. A system prompt
3. A list of tools (Bedrock-format tool definitions)

The harness handles everything else: the reasoning loop, tool invocation, response accumulation, and streaming. No `while not done` loop. No manual tool-dispatch code.

```python
import boto3

client = boto3.client("bedrock-agentcore-runtime")

response = client.invoke_agent(
    agentId="my-research-agent",
    sessionId="user-session-abc123",
    inputText="Summarize the last 90 days of earnings reports for NVDA, AMD, and INTC",
)

for event in response["stream"]:
    if "chunk" in event:
        print(event["chunk"]["bytes"].decode(), end="", flush=True)
```

Tool definitions use the same schema as Bedrock's Converse API. If you already have Converse tool definitions, they drop in directly.

The harness available in four AWS Regions today: US West (Oregon), US East (N. Virginia), Europe (Frankfurt), and Asia Pacific (Sydney). There is no additional charge for the harness itself — you pay only for Runtime compute.

---

## How Pricing Works

AgentCore Runtime pricing has two dimensions:

| Component | Price | Billing detail |
|---|---|---|
| vCPU time | $0.0895 / vCPU-hour | Stops during I/O wait |
| Memory | $0.00945 / GB-hour | Per-second, 128 MB minimum |

The I/O wait detail is the interesting one. When your agent is waiting for an LLM response, an API call, or a database query, CPU billing pauses. For typical agent workloads — where 60–80% of wall-clock time is waiting on model inference — this can cut effective compute cost substantially compared to always-on compute models.

Billing granularity is per-second with a 1-second minimum, so short-lived tool executions are not punished with full-minute minimums.

Browser profiles and cookies, if your agent uses AgentCore's browser capability, are stored in S3 at standard S3 rates.

**AgentCore CLI, managed harness, and skills are free.** You pay only for Runtime execution.

---

## Core Services

AgentCore is modular. You can use components independently or together:

**Runtime** — the session execution environment. Per-session microVM isolation, 8-hour sessions, filesystem access, shell access within the sandbox. This is the core product.

**Memory** — a managed memory layer. Stores conversation history, extracted facts, and user preferences across sessions. Backed by a vector store and a semantic retrieval API.

**Gateway** — an MCP-compatible gateway that lets your agent call external tools and APIs through a managed connection layer. Handles authentication, rate limiting, and retry logic.

**Tools** — pre-built tool integrations for common AWS services (S3, DynamoDB, Lambda) and external services. Available through the AgentCore SDK and CLI.

---

## The Session Isolation Model

The isolation guarantee is stricter than container-based approaches and matters for multi-tenant deployments.

With containers, a misconfiguration or kernel vulnerability can leak data between tenants. With microVMs (AgentCore uses Firecracker, the same technology that underpins AWS Lambda and Fargate), each session gets a dedicated kernel. Memory is hardware-isolated. The attack surface between sessions is the hypervisor, not the OS networking stack.

For builders handling sensitive data — legal documents, financial records, health information — this is a meaningful difference from spinning up shared containers or using a single-process agent server.

When a session ends:
- The microVM is terminated
- Memory is wiped
- Filesystem is destroyed

Nothing persists unless you explicitly use the filesystem persistence feature (which externalizes state to S3) or the Memory service (which stores extracted facts in the managed memory store).

---

## Framework Integration

AgentCore does not replace your framework. It wraps it.

**LangGraph**: deploy a LangGraph graph as an AgentCore agent. The Runtime provides the execution environment; LangGraph handles the graph traversal. State checkpointing maps to AgentCore's filesystem persistence.

**CrewAI**: package a CrewAI crew as an AgentCore deployment unit. Each crew member runs as a subagent within the session's microVM.

**LlamaIndex**: deploy a query pipeline or ReActAgent using AgentCore as the host. Tool definitions from LlamaIndex's `FunctionTool` convert directly.

**Strands Agents**: AWS's own open-source agent framework integrates natively with AgentCore. If you're starting fresh on AWS, this is the lowest-friction path.

**Custom**: if you have existing Python agent code, the migration path is: wrap your agent in an AgentCore handler, define your tools in Bedrock format, deploy via the CLI.

---

## AgentCore vs. Lambda vs. ECS

This comes up for every new agent deployment. The short version:

| Scenario | Best fit |
|---|---|
| Simple tool call, < 30 seconds | Lambda |
| Stateless batch processing | ECS Fargate |
| Multi-step agent, 1–8 hours, single user session | AgentCore Runtime |
| Multi-tenant production agent, data isolation required | AgentCore Runtime |
| High-concurrency streaming API | ECS + ALB |

AgentCore wins when you need session duration beyond Lambda's 15 minutes, per-session data isolation, or you want to stop building the infrastructure layer. It is not the right answer for high-throughput stateless workloads where Lambda's cold-start tax is already acceptable.

---

## What Is Still in Preview

As of April/May 2026, these AgentCore features are in limited preview:

- **Managed harness** (available now in the four launch regions)
- **Filesystem persistence** (preview — S3-backed session state)
- **Browser capability** (let agents control a headless browser within the microVM)
- **OpenAI models on Bedrock** (GPT-5.5, GPT-5.4) — limited preview, separate from AgentCore but relevant if you want OpenAI models with AgentCore's infrastructure

To request access, use the AgentCore waitlist on the AWS console.

---

## What to Do Right Now

If you are running agents on Lambda and hitting the 15-minute timeout, AgentCore Runtime is a straightforward migration target. The managed harness removes orchestration boilerplate; you keep your tool definitions and model choice.

If you are building multi-tenant agent applications and handling any sensitive data, the microVM isolation model is worth the migration overhead. The alternative — hoping your container isolation is sufficient — is a risk you can eliminate now.

If you are already on Bedrock, AgentCore integrates with your existing IAM roles, PrivateLink connectivity, CloudTrail logs, and Bedrock Guardrails configuration. There is no new security model to learn.

The AgentCore CLI is available today in 14 AWS Regions. Documentation is at [docs.aws.amazon.com/bedrock-agentcore](https://docs.aws.amazon.com/bedrock-agentcore/).
