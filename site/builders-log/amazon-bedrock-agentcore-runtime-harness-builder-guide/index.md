# Amazon Bedrock AgentCore: AWS's Answer to the Agent Deployment Problem

> AWS added a managed harness to Amazon Bedrock AgentCore in April 2026 — a managed platform that handles the infrastructure complexity of running AI agents at scale: per-session microVM isolation, 8-hour session limits, filesystem persistence, and a managed harness that removes orchestration boilerplate. Here's what it does, how pricing works, and when to use it.


AWS launched Amazon Bedrock AgentCore in preview in [July 2025](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-bedrock-agentcore-preview/) and took it to [general availability that October](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/). What's new here is narrower: on [April 22, 2026](https://aws.amazon.com/about-aws/whats-new/2026/04/agentcore-new-features-to-build-agents-faster/), AWS added a managed harness to AgentCore Runtime. That announcement landed quietly — days before [OpenAI's GPT-5.5 and GPT-5.4 models arrived on Bedrock](https://aws.amazon.com/blogs/aws/get-started-with-openai-gpt-5-5-gpt-5-4-models-and-codex-on-amazon-bedrock/) at the "[What's Next with AWS 2026](https://aws.amazon.com/blogs/aws/top-announcements-of-the-whats-next-with-aws-2026/)" event on April 28 — but for builders shipping production agents, AgentCore solves a harder problem.

The hard problem is not building an agent. It's running one in production for real users, at scale, without building the infrastructure layer yourself.

---

## What AgentCore Actually Is

AgentCore is a managed platform for deploying and operating AI agents. It is not a framework and not an orchestration library. It sits between your agent code and AWS infrastructure, handling:

- **Session isolation**: each user session gets its own microVM with separate CPU, memory, and filesystem. [When the session ends, the microVM is terminated and memory is sanitized](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html); AWS states commands and agent code "cannot access other customers' workloads or escape the VM boundary."
- **Session duration**: agents can run for up to **[8 hours](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-bedrock-agentcore-preview/)** per session, compared to [AWS Lambda's 15-minute hard limit](https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html). This matters for tasks that involve iterative research, long file processing, or multi-stage workflows.
- **State persistence**: [managed session storage (preview)](https://aws.amazon.com/about-aws/whats-new/2026/03/bedrock-agentcore-runtime-session-storage) externalizes local session state — up to 1 GB per session, retained for 14 days of idle time — letting agents suspend mid-task and resume exactly where they left off.
- **Managed execution**: [the managed harness runs the full agent loop](https://aws.amazon.com/about-aws/whats-new/2026/04/agentcore-new-features-to-build-agents-faster/) — reasoning, tool selection, action execution, response streaming — with no orchestration code required from you.

[AWS lists LangGraph, LlamaIndex, CrewAI, and Strands Agents](https://aws.amazon.com/about-aws/whats-new/2026/04/agentcore-new-features-to-build-agents-faster/) among the frameworks AgentCore works with out of the box, alongside custom code. It also works with any foundation model on Bedrock, and — as of [June 1, 2026](https://aws.amazon.com/blogs/aws/get-started-with-openai-gpt-5-5-gpt-5-4-models-and-codex-on-amazon-bedrock/) — with OpenAI's GPT-5.5 (US East Ohio) and GPT-5.4 (US East Ohio and US West Oregon) on Bedrock.

---

## The Managed Harness

[The April 22, 2026 update added a managed harness to AgentCore Runtime](https://aws.amazon.com/about-aws/whats-new/2026/04/agentcore-new-features-to-build-agents-faster/). To use it, you specify three things:

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

[Harness tool schemas use JSON Schema for the `inputSchema`](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-tools.html) — the same format used in the [`inputSchema` field of Bedrock's Converse API tool definitions](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use-inference-call.html).

[The harness (in preview) is available in four AWS Regions](https://aws.amazon.com/about-aws/whats-new/2026/04/agentcore-new-features-to-build-agents-faster/): US West (Oregon), US East (N. Virginia), Europe (Frankfurt), and Asia Pacific (Sydney). [There is no separate harness charge](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.html) — you pay only for the underlying AgentCore capabilities you use.

---

## How Pricing Works

AgentCore Runtime pricing has two dimensions:

| Component | Price | Billing detail |
|---|---|---|
| vCPU time | [$0.0895 / vCPU-hour](https://aws.amazon.com/bedrock/agentcore/pricing/) | Stops during I/O wait |
| Memory | [$0.00945 / GB-hour](https://aws.amazon.com/bedrock/agentcore/pricing/) | Per-second, 128 MB minimum |

The I/O wait detail is the interesting one. [AWS states that "if your agent consumes no CPU during I/O wait, there are no CPU charges"](https://aws.amazon.com/bedrock/agentcore/pricing/) — when your agent is waiting for an LLM response, an API call, or a database query, CPU billing pauses, which can cut effective compute cost compared to always-on compute models.

[Billing granularity is per-second with a 1-second minimum](https://aws.amazon.com/bedrock/agentcore/pricing/), so short-lived tool executions are not punished with full-minute minimums.

[Browser profiles and cookies, if your agent uses AgentCore's browser capability, are stored in S3 at standard S3 rates](https://aws.amazon.com/bedrock/agentcore/pricing/).

**[There is no separate charge for the managed harness](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.html)** — you pay only for the underlying AgentCore capabilities (Runtime, Memory, Gateway, etc.) that your agent uses.

---

## Core Services

AgentCore is modular. You can use components independently or together:

**Runtime** — the session execution environment. Per-session microVM isolation, 8-hour sessions, filesystem access, shell access within the sandbox. This is the core product.

**[Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)** — a managed memory layer with two types: short-term memory for turn-by-turn context within a session, and long-term memory that "automatically extracts and stores key insights from conversations across multiple sessions, including user preferences, important facts, and session summaries."

**[Gateway](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/)** — an MCP-compatible gateway that converts APIs and Lambda functions into MCP-compatible tools and lets your agent call them through a managed connection layer, handling inbound and outbound OAuth authentication.

**[Tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)** — Gateway "converts APIs, Lambda functions, and existing services into Model Context Protocol (MCP)-compatible tools," plus AWS's own built-in Browser and Code Interpreter tools, available through the AgentCore SDK and CLI.

---

## The Session Isolation Model

The isolation guarantee is stricter than container-based approaches and matters for multi-tenant deployments.

With containers, a misconfiguration or kernel vulnerability can leak data between tenants. [Each AgentCore Runtime session runs in its own Firecracker microVM](https://aws.amazon.com/blogs/machine-learning/its-safe-to-close-your-laptop-now-hosting-coding-agents-on-amazon-bedrock-agentcore/) — [the same virtualization technology AWS built to underpin Lambda and Fargate](https://aws.amazon.com/blogs/opensource/firecracker-open-source-secure-fast-microvm-serverless/) — giving each session a dedicated kernel and hardware-isolated memory.

For builders handling sensitive data — legal documents, financial records, health information — this is a meaningful difference from spinning up shared containers or using a single-process agent server.

[When a session ends, the microVM is terminated and memory is sanitized](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html); AWS states that commands and agent code "cannot access other customers' workloads or escape the VM boundary."

Nothing persists unless you explicitly use the [managed session storage feature](https://aws.amazon.com/about-aws/whats-new/2026/03/bedrock-agentcore-runtime-session-storage) (which externalizes state to S3-backed storage) or the [Memory service](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) (which stores extracted facts in the managed memory store).

---

## Framework Integration

AgentCore does not replace your framework. It wraps it.

**LangGraph**: deploy a LangGraph graph as an AgentCore agent. [AWS lists LangGraph among the frameworks that work with AgentCore Runtime and the managed harness](https://aws.amazon.com/about-aws/whats-new/2026/04/agentcore-new-features-to-build-agents-faster/). The Runtime provides the execution environment; LangGraph handles the graph traversal.

**CrewAI**: package a CrewAI crew as an AgentCore deployment unit — [also on AWS's supported-framework list](https://aws.amazon.com/about-aws/whats-new/2026/04/agentcore-new-features-to-build-agents-faster/).

**LlamaIndex**: deploy a query pipeline or agent using AgentCore as the host. [LlamaIndex is likewise named as a supported framework](https://aws.amazon.com/about-aws/whats-new/2026/04/agentcore-new-features-to-build-agents-faster/).

**Strands Agents**: [AWS's own open-source agent framework](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/) integrates natively with AgentCore — [the managed harness itself is built on Strands Agents](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.html). If you're starting fresh on AWS, this is the lowest-friction path.

**Custom**: if you have existing Python agent code, [the CLI's code-based path](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-get-started-cli.html) lets you write the agent loop in a framework you choose and deploy it to AgentCore Runtime, with full control over orchestration logic.

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

As of June 2026, these AgentCore features are in preview:

- **[Managed harness](https://aws.amazon.com/about-aws/whats-new/2026/04/agentcore-new-features-to-build-agents-faster/)** (available now in the four launch regions; it reached [general availability on June 17, 2026](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available/))
- **[Managed session storage](https://aws.amazon.com/about-aws/whats-new/2026/03/bedrock-agentcore-runtime-session-storage)** (preview — S3-backed session filesystem state)

AgentCore's Browser and Code Interpreter capabilities are already generally available, not preview — [AgentCore itself reached general availability in October 2025](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/). Separately, [OpenAI's GPT-5.5 and GPT-5.4 on Bedrock](https://aws.amazon.com/blogs/aws/get-started-with-openai-gpt-5-5-gpt-5-4-models-and-codex-on-amazon-bedrock/) are region-limited (Ohio, and Ohio plus Oregon respectively) but not labeled preview as of their June 1, 2026 announcement.

---

## What to Do Right Now

If you are running agents on Lambda and hitting the 15-minute timeout, AgentCore Runtime is a straightforward migration target. The managed harness removes orchestration boilerplate; you keep your tool definitions and model choice.

If you are building multi-tenant agent applications and handling any sensitive data, the microVM isolation model is worth the migration overhead. The alternative — hoping your container isolation is sufficient — is a risk you can eliminate now.

If you are already on Bedrock, [AgentCore integrates with your existing IAM roles, AWS PrivateLink connectivity, CloudTrail logging, and Bedrock Guardrails (applied through the Gateway policy engine)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html). There is no new security model to learn.

[The AgentCore managed harness is available today in 14 AWS Regions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html): US East (N. Virginia, Ohio), US West (Oregon), Canada (Central), Europe (Frankfurt, Ireland, London, Paris, Stockholm), and Asia Pacific (Mumbai, Singapore, Sydney, Tokyo, Seoul). Documentation is at [docs.aws.amazon.com/bedrock-agentcore](https://docs.aws.amazon.com/bedrock-agentcore/).

