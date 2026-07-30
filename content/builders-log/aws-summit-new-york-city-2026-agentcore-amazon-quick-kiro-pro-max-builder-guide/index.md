---
title: "AWS Summit New York City 2026: AgentCore Seven Services, Amazon Quick, Kiro Pro Max, S3 Vectors — Builder Guide"
date: 2026-06-17
description: "AWS Summit New York City 2026 happened June 17 at the Javits Center. The headline: AWS is positioning agentic AI as the organizing layer for its entire platform. Here's every announcement that matters to builders — AgentCore's seven-service suite, Amazon Quick's new agentic features, Kiro Pro Max, S3 Vectors, and Nova Act."
og_description: "AWS Summit NYC 2026 (June 17): AgentCore is now a 7-service production infrastructure suite. Amazon Quick gets autonomous background agents. Kiro Pro Max launches at $100/mo. S3 Vectors cuts vector storage costs up to 90%. Here's what builders need to act on."
sources_audited: 2026-07-31
content_type: "Builder's Log"
categories: ["AWS", "Agent Infrastructure", "Developer Tools"]
tags: ["aws", "amazon", "agentcore", "amazon-quick", "kiro", "s3-vectors", "nova-act", "agents", "agentic-ai", "bedrock", "finops", "production-ai", "aws-summit"]
---

AWS Summit New York City 2026 ran June 17 at the Javits Center, with an 11:00 AM–12:30 PM keynote ([official event agenda](https://aws.amazon.com/events/summits/new-york/agenda/); [top announcements](https://aws.amazon.com/blogs/aws/top-announcements-of-the-aws-summit-in-new-york-2026/)). [VP of Agentic AI Swami Sivasubramanian](https://www.aboutamazon.com/news/aws/aws-summit-nyc-2026-ai-agents) delivered the keynote, with agentic AI as the organizing theme for virtually every service announcement. AWS heads into the summit as a $142 billion annualized revenue run-rate business — a figure both [CEO Andy Jassy and CFO Brian Olsavsky cited on the company's Q4 2025 earnings call](https://www.fool.com/earnings/call-transcripts/2026/02/05/amazon-amzn-q4-2025-earnings-call-transcript/) in February 2026, following [$35.6 billion in Q4 2025 AWS segment revenue, up 24% year-over-year](https://www.aboutamazon.com/news/company-news/amazon-earnings-q4-2025-report) — the segment's fastest growth rate in 13 quarters.

The throughline: AWS is no longer treating agents as an experimental feature. The entire platform — storage, compute, identity, observability — is being reoriented around them.

Here is what builders need to know.

---

## AgentCore: Now a Seven-Service Production Infrastructure Suite

AgentCore launched in [preview in July 2025](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/), reached [general availability that October](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/), and picked up a [managed harness in April 2026](/builders-log/amazon-bedrock-agentcore-runtime-harness-builder-guide/) — a runtime with microVM isolation that now also handles the agent orchestration loop for you.

Since its original launch, AgentCore has been [seven services](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/) that together form an infrastructure stack for running agents in enterprise production:

| Service | What it handles |
|---|---|
| **AgentCore Runtime** | Per-session microVM isolation, 8-hour sessions, managed agent loop |
| **AgentCore Memory** | Cross-session and cross-agent persistent memory stores |
| **AgentCore Identity** | OAuth 2.0 + OIDC scoped to agent sessions; credential rotation |
| **AgentCore Code Interpreter** | Sandboxed Python execution inside the agent session boundary |
| **AgentCore Browser Tool** | Managed headless browser for web-based agent tasks |
| **AgentCore Gateway** | MCP-compatible tool routing; connects agents to enterprise systems |
| **AgentCore Observability** | Trace IDs, latency, tool call logs; integrates with CloudWatch and OpenTelemetry |

What's new at this specific summit: a [managed Knowledge Base for Bedrock](https://aws.amazon.com/blogs/aws/top-announcements-of-the-aws-summit-in-new-york-2026/) with native data connectors and an Agentic Retriever that integrates with AgentCore Gateway, a [fully managed web search tool for AgentCore](https://aws.amazon.com/blogs/aws/top-announcements-of-the-aws-summit-in-new-york-2026/) that grounds agent responses in current, cited web knowledge with zero data egress, and the [AgentCore Harness reaching general availability](https://aws.amazon.com/blogs/aws/top-announcements-of-the-aws-summit-in-new-york-2026/).

This matters because the common failure mode for production agents is not the LLM — it is the surrounding infrastructure: leaked credentials, state bleed between sessions, no audit trail. AgentCore's seven-service model addresses each of these explicitly.

**For builders:** If you are on AWS and building production agents, AgentCore is now the default answer for "where do I run this." It works with any framework (CrewAI, LangGraph, LlamaIndex, Strands, custom) and any Bedrock-compatible model.

---

## Amazon Quick: The Amazon Q Business Migration Path Gets New Agentic Features

Amazon Quick — AWS's rebrand of [Amazon Quick Suite](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-quick-suite-agentic-ai-powered-workspace), itself an [October 2025 evolution of Amazon QuickSight](https://aws.amazon.com/blogs/business-intelligence/reimagine-business-intelligence-amazon-quicksight-evolves-to-amazon-quick-suite/) — got its biggest public stage yet at the summit. AWS is steering [Amazon Q Business customers toward Quick](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html) as the recommended migration path; Q Business itself stops accepting new customers on July 31, 2026, though AWS says existing deployments keep receiving bug fixes and security updates.

At the summit, AWS announced [autonomous background agents for Quick](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-quick/) — configurable for specific expertise, tone, and tool access — along with multi-dataset analytics for querying across data sources without technical prep, and a redesigned activity feed consolidating email, messaging, calendar, and tasks.

Quick's core modules, per [AWS's own FAQ](https://aws.amazon.com/quicksuite/faqs/), are: **Quick Flows** (natural-language workflow automation), **Quick Automate** (multi-step processes across systems), **Quick Research** (a deep-research agent that returns fully cited reports), **Quick Sight** (AI-powered BI dashboards and reporting), **Spaces** (shared team workspaces), and **Quick Extensions** (browser and app add-ons for Chrome, Edge, Firefox, Slack, Outlook, and Microsoft Office). Quick ships a [native desktop app for macOS and Windows](https://aws.amazon.com/quicksuite/faqs/).

**For builders assessing Quick vs. building custom:** Quick is the right call when the goal is cross-app workflow automation for business users — HR, finance, operations. It is not a developer platform. If you need custom agent logic, tool calling, or tight control over model behavior, AgentCore is the answer, not Quick. They are complementary, not competing.

---

## Kiro Pro Max: $100/Month Tier for Serious Daily Use

[Kiro](/builders-log/amazon-q-developer-kiro-migration-timeline-opus-cutoff/) is AWS's spec-driven agentic IDE — its [spec workflow generates requirements.md, design.md, and tasks.md documents](https://kiro.dev/docs/specs/feature-specs/) before writing a line of code. That spec-first approach means it works better than most tools for large, multi-file features but adds friction for quick one-off changes.

[Kiro Pro Max is a new pricing tier at $100/month](https://kiro.dev/blog/kiro-pro-max/), slotting between [Pro+ ($40/mo) and Power ($200/mo)](https://kiro.dev/pricing/) — [announced in AWS's June 15 weekly roundup](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-finops-agent-in-preview-gemma-4-on-bedrock-kiro-pro-max-and-more-june-15-2026/) ahead of the summit. It is aimed at developers who consistently exceed their Pro+ credit allocation without needing the full Power tier.

Per [Kiro's own FAQ](https://kiro.dev/faq/), model access is via "Auto" — a mix of frontier and specialized models including Claude Sonnet 4.5, Sonnet 4.6, Haiku 4.5, and Opus 4.5–4.7 — or users can select a specific model directly. AWS has not published details on Amazon Nova being used for Kiro's code generation, so this article is not repeating that claim.

**The decision:**

| You want | Plan |
|---|---|
| Occasional use, learning Kiro | Free |
| Daily use, single project | Pro+ ($40/mo) |
| Daily use, multiple projects, frequent spec runs | Pro Max ($100/mo) |
| Full-time agent-driven development, large teams | Power ($200/mo) |

---

## S3 Vectors: Native Vector Storage at 90% Lower Cost

S3 Vectors — an S3 capability that adds native vector storage and querying directly in object storage, no separate vector database required for basic retrieval use cases — was recapped at the summit as background for the AgentCore/RAG story. It's not new: AWS [announced it in preview in July 2025](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-s3-vectors-preview-native-support-storing-querying-vectors/) and took it to [general availability on December 2, 2025](https://aws.amazon.com/blogs/aws/amazon-s3-vectors-now-generally-available-with-increased-scale-and-performance) with expanded scale (up to 2 billion vectors per index, a 40x increase over preview).

Key numbers, per AWS's own announcements:
- [Up to 90% lower cost](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-s3-vectors-preview-native-support-storing-querying-vectors/) than specialized vector database solutions for uploading, storing, and querying vectors
- [Similarity search, metadata filtering, and batch writes](https://aws.amazon.com/blogs/aws/amazon-s3-vectors-now-generally-available-with-increased-scale-and-performance) supported natively, with query latency around 100ms or less at GA
- Scales with S3's existing durability and access control model

**When S3 Vectors makes sense:** High-volume, lower-latency-tolerance retrieval (document archives, batch embedding pipelines, long-term memory for agents). For real-time RAG with sub-50ms requirements, purpose-built vector databases (Pinecone, Weaviate, pgvector) still have the advantage.

**When it does not:** If you need millisecond retrieval with high concurrency for interactive applications, S3 Vectors is not the right choice today.

---

## Nova Act: Browser Automation, 90% Reliability Per AWS

Nova Act is Amazon's browser automation agent, [generally available since December 2, 2025](https://aws.amazon.com/about-aws/whats-new/2025/12/build-automate-production-ui-workflows-nova-act/), trained for enterprise web tasks: form filling, portal navigation, multi-step approvals, data extraction from web applications.

AWS's own claim is "[Nova Act delivers 90% reliability on early customer workflows](https://www.aboutamazon.com/news/aws/aws-agentic-ai-amazon-bedrock-nova-models)" — that's AWS's figure from its own customers, not an independent benchmark against Playwright, Puppeteer, or other browser-automation frameworks, so this article isn't repeating a head-to-head comparison it can't verify.

Nova Act [can be integrated with AgentCore via AgentCore Browser Tool](https://docs.aws.amazon.com/nova-act/latest/userguide/bedrock-agentcore.html), as one option among several browser backends, so it can inherit AgentCore's session isolation and credential management when configured that way.

**Use cases:** Agent-driven access to vendor portals, legacy intranet tools, SaaS applications without APIs, compliance workflows that live in web-only interfaces.

---

## AWS FinOps Agent (Preview)

[Announced in AWS's June 15 weekly roundup](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-finops-agent-in-preview-gemma-4-on-bedrock-kiro-pro-max-and-more-june-15-2026/) ahead of the summit and covered again on stage: [AWS FinOps Agent went into public preview](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-finops-agent-preview/) on June 9, 2026. Per [AWS's own announcement](https://aws.amazon.com/blogs/aws-cloud-financial-management/aws-finops-agent-is-now-public-preview/), it can:

- Answer cost questions across services and time windows
- Surface rightsizing, idle-resource, and Savings Plans recommendations via Cost Optimization Hub and Compute Optimizer
- Investigate cost anomalies automatically, linking changes to CloudTrail events to identify who changed what and when
- Open Jira tickets based on recommendations
- Post findings to Slack on a defined schedule

This is a meaningful development for teams with growing AWS bills and limited FinOps bandwidth. The scheduled anomaly investigation in particular — running at set intervals and posting to Slack before anyone asks — addresses a common operations gap.

---

## What Today's Summit Means for Builders

**The short version:** AWS has shipped the infrastructure layer for production agents. The April 2026 harness update filled in half the picture; this summit filled in the rest.

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

*Related reading: [Amazon Bedrock AgentCore: April 2026 Harness Update](/builders-log/amazon-bedrock-agentcore-runtime-harness-builder-guide/) | [Kiro Migration Timeline from Amazon Q Developer](/builders-log/amazon-q-developer-kiro-migration-timeline-opus-cutoff/) | [Amazon Bedrock AgentCore on AWS: Platform Deep-Dive](/builders-log/amazon-bedrock-agentcore-platform-aws-builder-guide/)*
