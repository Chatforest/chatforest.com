---
title: "AWS Summit New York City 2026: AgentCore Seven Services, Amazon Quick, Kiro Pro Max, S3 Vectors — Builder Guide"
date: 2026-06-17
description: "AWS Summit New York City 2026 happened June 17 at the Javits Center. The headline: AWS is positioning agentic AI as the organizing layer for its entire platform. Here's every announcement that matters to builders — AgentCore's seven-service suite, Amazon Quick replacing Q Business, Kiro Pro Max, S3 Vectors, Nova Act, and a new AI Agents Marketplace."
og_description: "AWS Summit NYC 2026 (June 17): AgentCore is now a 7-service production infrastructure suite. Amazon Quick replaces Q Business with 5 agentic modules. Kiro Pro Max launches at $100/mo. S3 Vectors cuts vector storage costs 90%. Here's what builders need to act on."
content_type: "Builder's Log"
categories: ["AWS", "Agent Infrastructure", "Developer Tools"]
tags: ["aws", "amazon", "agentcore", "amazon-quick", "kiro", "s3-vectors", "nova-act", "agents", "agentic-ai", "bedrock", "finops", "production-ai", "aws-summit"]
---

AWS Summit New York City 2026 ran June 17 at the Javits Center. VP of Agentic AI Swami Sivasubramanian led the keynote at 11 AM ET, with AWS at a $142 billion annualized run rate and agentic AI as the organizing theme for virtually every service announcement.

The throughline: AWS is no longer treating agents as an experimental feature. The entire platform — storage, compute, identity, observability — is being reoriented around them.

Here is what builders need to know.

---

## AgentCore: Now a Seven-Service Production Infrastructure Suite

When [AgentCore launched in April 2026](/builders-log/amazon-bedrock-agentcore-runtime-harness-builder-guide/), it was a runtime with microVM isolation and a managed harness. Good start; incomplete picture.

The summit clarified the full architecture. AgentCore is seven services that together form an infrastructure stack for running agents in enterprise production:

| Service | What it handles |
|---|---|
| **AgentCore Runtime** | Per-session microVM isolation, 8-hour sessions, managed agent loop |
| **AgentCore Memory** | Cross-session and cross-agent persistent memory stores |
| **AgentCore Identity** | OAuth 2.0 + OIDC scoped to agent sessions; credential rotation |
| **AgentCore Code Interpreter** | Sandboxed Python execution inside the agent session boundary |
| **AgentCore Browser Tool** | Managed headless browser for web-based agent tasks |
| **AgentCore Gateway** | MCP-compatible tool routing; connects agents to enterprise systems |
| **AgentCore Observability** | Trace IDs, latency, tool call logs; integrates with CloudWatch and OpenTelemetry |

This matters because the common failure mode for production agents is not the LLM — it is the surrounding infrastructure: leaked credentials, state bleed between sessions, no audit trail. AgentCore's seven-service model addresses each of these explicitly.

**For builders:** If you are on AWS and building production agents, AgentCore is now the default answer for "where do I run this." It works with any framework (CrewAI, LangGraph, LlamaIndex, Strands, custom) and any Bedrock-compatible model.

---

## Amazon Quick: Q Business Replaced by a Five-Module Agentic System

Amazon Quick launched April 28, 2026, as a full replacement for Amazon Q Business. The summit gave it its biggest public stage yet.

Where Q Business offered reactive chat against organizational data, Quick is a five-module architecture designed for autonomous workflow execution:

- **Spaces** — collaborative workspaces where teams and agents share context
- **Chat Agents** — autonomous agents that execute cross-app workflows (not just answer questions)
- **Flows** — natural-language automation builder for connecting enterprise tools
- **Research** — deep search across internal and external data simultaneously
- **Automations** — drag-and-drop workflow scheduler with built-in monitoring

Quick ships with 100+ integrations: Microsoft 365, Google Workspace, Slack, Teams, Salesforce, Jira, ServiceNow. Desktop app (macOS and Windows) plus Chrome, Edge, and Firefox extensions.

**For builders assessing Quick vs. building custom:** Quick is the right call when the goal is cross-app workflow automation for business users — HR, finance, operations. It is not a developer platform. If you need custom agent logic, tool calling, or tight control over model behavior, AgentCore is the answer, not Quick. They are complementary, not competing.

---

## Kiro Pro Max: $100/Month Tier for Serious Daily Use

[Kiro](/builders-log/amazon-q-developer-kiro-migration-timeline-opus-cutoff/) is AWS's spec-driven agentic IDE — it generates requirements.md, design.md, and tasks.md documents before writing a line of code. That spec-first approach means it works better than most tools for large, multi-file features but adds friction for quick one-off changes.

Kiro Pro Max is a new pricing tier at $100/month, slotting between Pro+ ($40/mo) and Power ($200/mo). It is aimed at developers who consistently exceed their Pro+ credit allocation without needing the full Power tier.

Under the hood, Kiro uses Claude Sonnet for reasoning-heavy spec generation and Amazon Nova for high-throughput code generation, switching models based on task type.

**The decision:**

| You want | Plan |
|---|---|
| Occasional use, learning Kiro | Free |
| Daily use, single project | Pro+ ($40/mo) |
| Daily use, multiple projects, frequent spec runs | Pro Max ($100/mo) |
| Full-time agent-driven development, large teams | Power ($200/mo) |

---

## S3 Vectors: Native Vector Storage at 90% Lower Cost

S3 Vectors is a new S3 capability that adds native vector storage and querying directly in object storage — no separate vector database required for basic retrieval use cases.

Key numbers:
- **90% cost reduction** compared to conventional vector database approaches for cold or archival retrieval workloads
- Supports similarity search, metadata filtering, and batch writes natively
- Scales with S3's existing durability and access control model

**When S3 Vectors makes sense:** High-volume, lower-latency-tolerance retrieval (document archives, batch embedding pipelines, long-term memory for agents). For real-time RAG with sub-50ms requirements, purpose-built vector databases (Pinecone, Weaviate, pgvector) still have the advantage.

**When it does not:** If you need millisecond retrieval with high concurrency for interactive applications, S3 Vectors is not the right choice today.

---

## Nova Act: Browser Automation with 90%+ Enterprise Task Completion

Nova Act is Amazon's browser automation agent, trained for enterprise web tasks: form filling, portal navigation, multi-step approvals, data extraction from web applications.

The claim is 90%+ task completion on enterprise use cases — notably higher than general-purpose browser automation like Playwright + LLM or Puppeteer-based approaches, which often fall apart on dynamic authentication flows and multi-page state.

Nova Act is built into AgentCore as an optional tool via AgentCore Browser Tool, so it inherits full session isolation and credential management.

**Use cases:** Agent-driven access to vendor portals, legacy intranet tools, SaaS applications without APIs, compliance workflows that live in web-only interfaces.

---

## AWS AI Agents Marketplace

New: a dedicated AI Agents and Tools category in AWS Marketplace. It allows customers to discover, purchase, deploy, and manage pre-built AI agents and MCP-compatible tools from third-party providers — all within the AWS billing and IAM framework.

For ISVs and tool builders, this is a new distribution channel with AWS's enterprise purchasing infrastructure already attached.

---

## AWS FinOps Agent (Preview)

Announced in the June 15 weekly roundup and reinforced at the summit: AWS FinOps Agent is in preview. It can:

- Answer cost questions across services and time windows
- Surface rightsizing recommendations via Cost Optimization Hub and Compute Optimizer
- Investigate cost anomalies automatically
- Open Jira tickets based on recommendations
- Post findings to Slack on a defined schedule

This is a meaningful development for teams with growing AWS bills and limited FinOps bandwidth. The scheduled anomaly investigation in particular — running at set intervals and posting to Slack before anyone asks — addresses a common operations gap.

---

## What Today's Summit Means for Builders

**The short version:** AWS has shipped the infrastructure layer for production agents. The April preview filled in half the picture; today filled in the rest.

| You're building | The AWS path |
|---|---|
| Production agent with isolated sessions + audit trail | AgentCore (seven services) |
| Cross-app workflow automation for business teams | Amazon Quick |
| Spec-driven development with agentic IDE | Kiro (Pro or Pro Max) |
| RAG pipeline with large embedding corpus, cost-sensitive | S3 Vectors |
| Agents that interact with web portals | Nova Act via AgentCore Browser Tool |
| Cost optimization with autonomous monitoring | AWS FinOps Agent (preview) |

The pattern here is not subtle: AWS is betting that agentic AI becomes the interface through which enterprises interact with all of their cloud infrastructure — not just AI services, but storage, security, observability, and operations. Today's summit is the most coherent statement of that bet yet.

---

*Related reading: [Amazon Bedrock AgentCore: April 2026 Launch](/builders-log/amazon-bedrock-agentcore-runtime-harness-builder-guide/) | [Kiro Migration Timeline from Amazon Q Developer](/builders-log/amazon-q-developer-kiro-migration-timeline-opus-cutoff/) | [Amazon Bedrock AgentCore on AWS: Platform Deep-Dive](/builders-log/amazon-bedrock-agentcore-platform-aws-builder-guide/)*
