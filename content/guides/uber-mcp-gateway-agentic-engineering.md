---
title: "Uber's MCP Gateway: How 84% of Engineers Went Agentic and What It Took to Get There"
date: 2026-04-07T10:00:00+09:00
description: "Uber built a centralized MCP Gateway that turns any internal endpoint into an MCP server, paired with a no-code Agent Builder and discovery registry. With 84% developer adoption, 65-72% AI-generated code, and 11% of PRs opened by agents, this is one of the largest enterprise MCP deployments documented."
content_type: "Guide"
card_description: "Uber built a centralized MCP Gateway that proxies Thrift, Protobuf, and HTTP endpoints as MCP servers with a single config change. Combined with Agent Builder (no-code agent creation), AIFX CLI (standardized tool provisioning), and GenAI Gateway (PII redaction before external model calls), it powers 84% developer adoption, 65-72% AI-generated code, and 11% of PRs opened by agents. The uSpec system automates design-to-spec documentation across 7 platform stacks using the Figma Console MCP. AI costs are up 6x since 2024 — the tradeoff Uber considers worth it to eliminate engineering toil. This case study breaks down the architecture, governance, and what other enterprises can learn."
last_refreshed: 2026-04-07
---

Uber's engineering organization has gone further with MCP than almost any other company we've documented. Where [Pinterest](/guides/pinterest-mcp-production-case-study/) built a fleet of domain-specific MCP servers and [Duolingo](/guides/duolingo-mcp-agentic-platform/) wired 180+ tools into a Slackbot, Uber took a different architectural bet: a **centralized MCP Gateway** that can turn any existing internal service into an MCP server through configuration alone — no new code required.

The results: **84% of developers** using agentic coding tools, **65–72% of code** generated within IDE-based tools, **11% of pull requests** opened by agents, and Claude Code usage nearly doubling from 32% to 63% in three months. These aren't pilot numbers. They represent a 10,000+ engineer organization where AI agents have become the default way to interact with internal systems.

This guide breaks down Uber's MCP architecture, the gateway design, governance model, and the uSpec system that automates design documentation. Our analysis draws on Uber's engineering blog, The Pragmatic Engineer's deep dive, the MCP Dev Summit presentation, and InfoQ's coverage — we research and analyze rather than testing implementations hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## The Problem: Thousands of Services, Ad Hoc AI Integration

Uber runs thousands of internal microservices communicating via Thrift, Protobuf, and HTTP. Before the MCP Gateway, connecting an AI agent to an internal tool meant building a custom integration — writing wrapper code, handling authentication, managing versioning. Multiply that by hundreds of services and thousands of engineers wanting AI access, and the integration burden becomes untenable.

The strategic decision was to avoid Pinterest's approach of building individual MCP servers per domain. Instead, Uber built infrastructure that makes *any* existing endpoint MCP-compatible.

## Architecture: The MCP Gateway

Uber's MCP Gateway is a centralized proxy that sits between AI agents and internal services. Its core capability: **expose any internal Thrift, Protobuf, or HTTP endpoint as an MCP server with a simple configuration change**.

### How It Works

Rather than rewriting services, the gateway translates between protocols:

| Internal Protocol | What the Gateway Does | What Agents See |
|---|---|---|
| **Thrift** | Maps Thrift service methods to MCP tools | Standard MCP tool calls |
| **Protobuf/gRPC** | Converts Protobuf messages to MCP schemas | Standard MCP tool calls |
| **HTTP/REST** | Wraps REST endpoints as MCP tool definitions | Standard MCP tool calls |

This is architecturally significant. Most enterprise MCP deployments (Pinterest, Duolingo) require teams to build and maintain dedicated MCP servers. Uber's approach means teams don't build MCP servers at all — they register their existing endpoints with the gateway, and it handles the translation.

### Centralized Governance

The gateway handles more than protocol translation:

- **Authorization** — centralized access control for who can call what
- **Telemetry** — unified logging and metrics across all MCP interactions
- **Audit trails** — every agent action recorded in one place
- **Rate limiting** — prevent runaway agents from overwhelming internal services

### Discovery Registry

Developers find available MCP servers through a discovery registry — similar to Pinterest's but tightly integrated with the gateway. Teams register their endpoints, and the registry tracks:

- Available MCP servers and their tools
- Owning teams and support contacts
- Access policies and authorization requirements
- Server health and usage metrics

### Sandbox Environment

A dedicated sandbox lets teams test experimental MCP servers before promoting them to production. This addresses a common enterprise concern: how do you let teams innovate with AI tools without risking production systems?

## Agent Builder: No-Code Agent Creation

Uber's **Agent Builder** lets non-engineering teams construct AI agents that can access internal data sources and delegate work between agents. This is not a prototype — it's a production platform with:

- **No-code interface** — teams build agents by configuring data sources, MCP servers, and instructions without writing code
- **Agent Studio** — a visual environment for debugging, tracing, versioning, and evaluating multi-agent workflows
- **Discoverable registry** — agents built in Agent Builder become discoverable through a registry where existing agents can be found, used, and copied
- **Delegation** — agents can call other agents, enabling composable workflows

The combination of MCP Gateway (turn any service into a tool) and Agent Builder (build agents without code) means teams across Uber can create AI-powered workflows without engineering bottlenecks.

## AIFX CLI: Standardized Tool Provisioning

The **AIFX CLI** is Uber's command-line interface for standardizing how developers interact with AI tools across the organization:

- **MCP server discovery** — find and connect to available MCP servers
- **Version management** — automatic updates to AI tools and configurations
- **Background task execution** — run agent workloads without blocking development
- **Consistent defaults** — organizational standards applied automatically

This solves the "shadow AI" problem — rather than each developer configuring their own MCP connections and agent tools, AIFX ensures everyone operates within the governed ecosystem.

## GenAI Gateway: Security at the Model Layer

All agentic requests at Uber pass through the **GenAI Gateway**, a Go-based proxy that mirrors the OpenAI API. Its critical function: **PII redaction before requests reach external models**.

When an agent constructs a prompt that includes internal data — Uber user IDs, trip details, internal system identifiers — the GenAI Gateway scrubs this information before sending the request to Claude, GPT-4o, or other external models. This means:

- Internal identifiers never leave Uber's network in model prompts
- External model providers don't see proprietary data
- Agents can work with real internal data without security compromises
- Compliance and audit requirements are met at the infrastructure level

This is distinct from the MCP Gateway (which handles tool-side connectivity) — the GenAI Gateway handles model-side security. Together, they create a two-sided governance layer around all AI agent activity.

## uSpec: Automating Design Documentation with MCP

One of the most concrete examples of Uber's MCP deployment is **uSpec**, an agentic system that automates design specification documentation.

### The Problem

Uber maintains design systems across **seven platform stacks**: UIKit, SwiftUI, Android XML, Android Compose, Web React, Go, and SDUI (Server-Driven UI). Each design component needs specification documentation for each stack — anatomy, API docs, properties, color tokens, dimensional structure, and accessibility specifications (VoiceOver, TalkBack, ARIA). Creating these specs manually took **weeks per design cycle**.

### The Architecture

uSpec runs locally, connecting Claude AI (via Cursor IDE) to Figma through the **open-source Figma Console MCP**:

1. An engineer shares a Figma link and optional context about component behavior
2. The agent crawls component and sub-component structures, reading design tokens, variant axes, variable modes, and configuration properties
3. It generates complete spec pages — anatomy with numbered markers, API documentation, variant previews, token-to-element color mapping, dimensional structure, and accessibility specs — directly into the Figma file

### Why It Matters

The key architectural decision: **no proprietary design data ever leaves the network**. The Figma Console MCP connects to Figma Desktop via a local WebSocket bridge, not a cloud API. The agent reads and writes locally. This satisfies enterprise security requirements while still leveraging external AI models (with PII redaction through the GenAI Gateway).

uSpec reduced design documentation time from **weeks to minutes** — one of the clearest ROI demonstrations of enterprise MCP deployment.

## The Numbers

| Metric | Value | Context |
|--------|-------|---------|
| **Developer agentic adoption** | 84% | CLI-based agents or agentic IDE requests |
| **Monthly agent users** | 92% of developers | Engage with agents at least monthly |
| **Code AI-generated** | 65–72% | Within IDE-based tools (Cursor, IntelliJ) |
| **PRs opened by agents** | 11% | Autonomous pull request creation |
| **Claude Code adoption** | 32% → 63% | Doubled in 3 months (Dec 2024 – Feb 2025) |
| **AI cost increase** | 6x since 2024 | Token cost optimization a growing priority |

The 6x cost increase is the honest part of this story. Uber considers it worth the tradeoff to "eliminate engineering toil around upgrades, migrations, and routine bug fixes" — but token cost optimization has become an organizational priority. The scale at which Uber operates means even small per-token savings compound.

## Architectural Comparison: Uber vs. Pinterest vs. Duolingo

| Dimension | Uber | Pinterest | Duolingo |
|-----------|------|-----------|----------|
| **MCP architecture** | Centralized gateway | Domain-specific servers | Monolithic server |
| **Integration model** | Config-based (no new code) | Teams build MCP servers | Central team builds tools |
| **Discovery** | Registry + AIFX CLI | Central registry (UI + API) | Hardcoded in Slackbot |
| **Primary interface** | IDE (Cursor, IntelliJ) + Agent Builder | IDE + internal chat + Slack bots | Slack |
| **Security model** | GenAI Gateway (PII redaction) + MCP Gateway auth | JWT + mesh identity (SPIFFE) | OAuth + role-based |
| **Agent autonomy** | 11% of PRs autonomous | Human-in-the-loop approval | Human-in-the-loop |
| **Scale metric** | 84% developer adoption | 66K invocations/month | 180+ tools |
| **Governance** | Centralized gateway enforcement | MCP Security Standard + review | Central team oversight |

The key difference: **Uber optimized for breadth** (any service, any team, minimal effort), while **Pinterest optimized for depth** (purpose-built servers with domain-specific logic). Duolingo sits between — a centralized team building a comprehensive toolset for a smaller engineering organization.

## Lessons for Enterprise MCP Adoption

### 1. Gateway vs. Server Fleet Is a Real Architectural Choice

Uber's gateway approach works because they have thousands of existing services with well-defined APIs. The gateway translates protocols without requiring service teams to learn MCP. Pinterest's approach works because their data tools (Presto, Spark, Airflow) benefit from domain-specific MCP logic that a generic gateway can't provide.

**The deciding factor:** If your services already have clean APIs and you want maximum coverage with minimum effort, a gateway approach scales faster. If your tools need custom MCP logic (specialized prompts, domain-specific error handling, context shaping), purpose-built servers are worth the investment.

### 2. PII Redaction at the Gateway Level Is Non-Negotiable

Uber's GenAI Gateway scrubs internal identifiers before they reach external models. This isn't optional for enterprises — it's the architectural pattern that makes the entire system compliant. Building PII protection into individual MCP servers doesn't scale; centralizing it at the gateway does.

### 3. No-Code Agent Creation Drives Adoption

Agent Builder's no-code interface means non-engineering teams can create agents. This shifts MCP from "a developer tool" to "organizational infrastructure" — similar to how Slack bots or internal dashboards spread beyond engineering once creation tools existed.

### 4. Cost Scales Faster Than Value (Initially)

AI costs up 6x while developer adoption reaches 84% is a cautionary data point. Token economics at enterprise scale are not yet solved. Uber's response — making token cost optimization an organizational priority — suggests this is a known challenge, not a crisis, but other enterprises should plan for it.

### 5. Shadow AI Is a Real Risk — AIFX CLI Addresses It

Without the AIFX CLI enforcing governed MCP connections and consistent defaults, Uber would face the same "shadow MCP" problem Qualys has documented industry-wide: developers configuring their own MCP servers, connecting agents to production systems without oversight. Standardized tooling prevents this.

## What's Missing

Uber hasn't published details on:

- **Specific MCP server count** — how many internal services are exposed via the gateway
- **Incident data** — whether agent-initiated changes have caused production issues
- **Token cost breakdown** — what proportion of the 6x increase comes from MCP tool calls vs. code generation vs. other AI usage
- **Agent Builder adoption** — how many non-engineering teams are actually building agents
- **Error rates** — how often agents make incorrect tool calls or produce wrong results

These gaps are normal for a company Uber's size — publishing internal metrics carries risk. But they mean we can't fully assess the operational maturity of the deployment.

## Related Guides

- [MCP's Growing Pains: Context Bloat, Security Gaps, and the Companies Walking Away](/guides/mcp-growing-pains-2026/) — why Uber's 6x cost increase and gateway approach matter in the broader context of MCP's scaling challenges
- [Pinterest's MCP Ecosystem](/guides/pinterest-mcp-production-case-study/) — domain-specific server fleet with 66K monthly invocations
- [Duolingo's Agentic Platform](/guides/duolingo-mcp-agentic-platform/) — 180+ MCP tools in a centralized Slackbot
- [Salesforce & Slack MCP Platform](/guides/salesforce-slack-mcp-ai-platform/) — MCP in mainstream collaboration tools
- [Datadog MCP Server](/guides/datadog-mcp-server-production-lessons/) — observability-focused production MCP
- [MCP Dev Summit 2026](/guides/mcp-dev-summit-2026-guide/) — where Uber first presented this architecture
- [MCP Enterprise Governance](/guides/mcp-enterprise-governance-platforms/) — frameworks for governing MCP at scale
- [MCP Security Landscape 2026](/guides/mcp-security-landscape-2026/) — the broader security context

---

*Published April 2026 by ChatForest. This analysis is based on Uber's engineering blog, The Pragmatic Engineer newsletter, InfoQ coverage, and the MCP Dev Summit 2026 presentation. We research and report — we don't build or test production MCP systems. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.*
