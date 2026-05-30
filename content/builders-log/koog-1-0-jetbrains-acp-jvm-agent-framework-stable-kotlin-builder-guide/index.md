---
title: "Koog 1.0 and ACP: JetBrains Ships a Stable JVM Agent Framework — and a New IDE Protocol"
date: 2026-05-30
description: "Koog 1.0 landed at KotlinConf '26 with a 1-year API stability guarantee, Spring Boot integration, multiplatform observability, and Anthropic prompt caching. Paired with the Agent Client Protocol (ACP), it's the most production-ready JVM agent framework available. Here's what changed and when JVM builders should use it."
content_type: "Builder's Log"
categories: ["AI Agents", "Developer Tools", "JVM"]
tags: ["koog", "jetbrains", "kotlin", "jvm", "java", "acp", "agent-client-protocol", "kotlinconf", "spring-boot", "opentelemetry", "observability", "multiplatform"]
---

At KotlinConf '26 on May 27, 2026, JetBrains shipped Koog 1.0 — a stable release of their open-source JVM agent framework — alongside new features across interoperability, observability, and the Agent Client Protocol (ACP) ecosystem. If you're building agents in Kotlin, Java, or anywhere on the JVM, this is the most consequential framework release of the year. Here's what changed, what it means, and when it's the right tool.

## What Koog Is

Koog is JetBrains' open-source framework for building AI agents in Kotlin, with full Java interop. It covers the building blocks production agents need: tools, typed workflows, persistence, memory, observability, and integrations with existing JVM and Kotlin Multiplatform projects.

The framework is built around a graph DSL where you define agent behavior as nodes and edges. Each node is a typed step (plan, tool call, check, branch). Edges encode control flow. The result is agent behavior that's auditable, testable, and recoverable — the opposite of prompt-in, hope-for-the-best.

JetBrains has been shipping agents in production at scale (Junie, AI Assistant across the entire IDE lineup) and built Koog from that operational experience. The patterns in Koog aren't theoretical.

## What Changed in 1.0

### API Stability Guarantee

The most important change isn't a feature — it's a commitment. Koog 1.0 ships with a **1-year no-breaking-changes guarantee** for all stable modules.

Modules are split into stable and beta streams:
- **Stable stream**: no breaking changes for 12 months, deprecation cycle required before removal
- **Beta stream**: evolving APIs, can change with notice

This matters enormously for enterprise JVM shops. Agents running on production infrastructure — next to Spring Boot services, Ktor APIs, Android apps — need dependency stability. "Latest works in tests but breaks in prod at 3am" is a framework credibility problem. The guarantee directly addresses it.

Every previously deprecated API was also removed in 1.0, and graph DSL node names are finalized.

### Spring AI Interop

Koog 1.0 ships with a redesigned Java interop layer that is cleaner and more consistent. The previously awkward boundary between Kotlin-idiomatic Koog APIs and Java callers has been resolved.

Spring Boot integration works. You can embed a Koog agent into a Spring application as a managed bean, wire tools via dependency injection, and expose agent results through standard Spring web controllers. For the majority of enterprise Java shops — where Spring Boot is already the platform — this is the path of least resistance to shipping agents.

Ktor integration is also supported for teams already running Ktor-based services.

### Multiplatform Observability via OpenTelemetry

Koog 1.0 extends OpenTelemetry support to all Kotlin Multiplatform targets: JVM, JS, WasmJS, Android, and iOS. Previously OpenTelemetry was JVM-only. The implementation uses a Ktor-based OTLP/JSON exporter that runs on every target.

Agents emit three standard signals out of the box:
- `gen_ai.client.token.usage` — per-request token consumption
- `gen_ai.client.operation.duration` — latency per agent operation
- `gen_ai.client.tool.count` — tool invocations per execution

These plug straight into existing Prometheus/Grafana stacks. Langfuse, Weave, and Datadog are all supported via the same OTLP path.

This is a meaningful shift. Teams that already have observability infrastructure don't have to build a custom logging layer around their agent — Koog emits into it directly.

### Anthropic Prompt Caching

Koog 1.0 adds Anthropic prompt caching support. For agents with long system prompts, tool schemas, or context documents, caching the prefix can cut input token costs by 90% on repeated calls. At scale, this is the difference between an agent being economically viable and not.

This requires Anthropic as your model backend — Claude Sonnet 4.6 or Opus 4.8 via the Anthropic API, Bedrock, or Vertex AI.

### HTTP Transport Decoupled from Ktor

The HTTP client is now pluggable. You can use OkHttp, HttpClient, or any other transport layer rather than being forced into Ktor's HTTP client. This matters for teams that already have a standardized HTTP client and don't want to introduce Ktor solely for Koog.

### Built-in Fault Tolerance

Koog 1.0 ships production-grade failure handling as core functionality, not a bolt-on:
- **Retries** with configurable backoff at the tool call level
- **Agent persistence**: agents can restore state at a specific graph node after failure or restart, without replaying the full execution from the beginning
- **Graceful degradation** when individual tools fail without aborting the entire workflow

For long-running agents — multi-step research tasks, code generation pipelines, document processing — persistence is the difference between "the agent starts over if it crashes" and "the agent resumes where it left off."

## The ACP Integration

Alongside Koog 1.0, JetBrains is co-leading the development of the **Agent Client Protocol (ACP)** — an open standard that defines how IDEs and AI coding agents communicate. Koog includes ACP as a first-class integration.

### What ACP Is

ACP standardizes the communication layer between a code editor (IDE, terminal, VS Code extension) and an AI agent running locally or remotely. Think of it as a protocol analogous to LSP (Language Server Protocol) but for agents instead of language analysis.

The spec uses JSON-RPC 2.0 over stdin/stdout. Official SDKs ship for Python, TypeScript, Kotlin, and Rust. Any agent implementing ACP can be added to any ACP-compatible IDE without a custom integration.

### The ACP Agent Registry

JetBrains and Zed Industries jointly launched the **ACP Agent Registry** on January 28, 2026 — a curated marketplace of ACP-compatible agents installable with one click from IntelliJ IDEA, PyCharm, WebStorm, or Zed.

Agents confirmed in the registry at launch: Kimi CLI, goose (by Block), and Augment Code. Additional agents include Gemini CLI, Claude Code, Auggie, OpenCode, and GitHub Copilot.

Notably, Amazon Kiro also supports ACP via its CLI layer — meaning agents built with Koog can potentially surface in Kiro alongside the JetBrains IDE lineup.

### What ACP Means for Koog Builders

If you build an agent with Koog and implement the ACP protocol layer, your agent:
- Appears in the ACP Agent Registry
- Is installable in IntelliJ, PyCharm, WebStorm, and Zed with one click
- Works inside Kiro's IDE integration layer
- Integrates without any custom work from JetBrains or the IDE vendor

This is distribution. The JVM agent framework being ACP-native means builders can write the agent once and surface it across the IDE ecosystem without per-IDE integrations.

## The Builder Decision: When to Use Koog

### Use Koog if:
- Your stack is already JVM/Kotlin — you're not pulling in a new language dependency
- You're embedding agents into existing Spring Boot services
- You're targeting Android or iOS (Kotlin Multiplatform means one agent codebase across platforms)
- You need guaranteed API stability for production agent infrastructure
- You want agents that emit OpenTelemetry into your existing observability stack without configuration
- You're in a regulated industry where auditability of agent decisions matters (the graph DSL makes this inspectable)

### Consider alternatives if:
- Your team is Python-first — LangGraph, LlamaIndex, and the Claude Agent SDK have larger Python ecosystems and more community content
- You need the broadest model support quickly — Python frameworks typically ship new model integrations before Koog
- You're prototyping, not building production — Koog's strength is its production correctness, which adds setup overhead that Python quick-starts don't have

### Where Koog fits in the JVM framework landscape

The main alternatives on JVM are:
- **LangChain4j** — Java-first, extensive model integrations, less opinionated on workflow structure
- **Spring AI** — first-party Spring integration, well-documented, limited agent orchestration patterns
- **Custom** — many JVM shops write thin wrappers around the model API and own the orchestration

Koog's differentiators are: the typed workflow DSL (correctness over flexibility), the multiplatform targets, and the ACP IDE integration. LangChain4j has a wider model integration surface and is likely to be the default for teams that care most about compatibility breadth. Spring AI is the obvious choice if you want minimal dependencies and Spring is already doing everything else. Koog wins on production correctness and observability out of the box.

## The Stability Argument at a JVM Shop

Most JVM shops — financial services, enterprise software, backend infrastructure — have already lived through dependency churn. Frameworks that break their API at minor versions are a hard sell to engineering teams with multi-year production commitments.

The 1.0 stability guarantee gives Koog a credible answer to "what happens in 18 months when you release 1.1?" That answer is now: "nothing your production code notices."

For JVM-shop builders evaluating agent frameworks, that guarantee may matter more than any individual feature list.

## Getting Started

Koog is open source under the Apache 2.0 license. The 1.0.0 release is on GitHub at [JetBrains/koog](https://github.com/JetBrains/koog). The release blog post on the JetBrains AI Blog covers the full 1.0 changelog.

ACP documentation and the agent registry are at [jetbrains.com/acp](https://www.jetbrains.com/acp/).

If you're evaluating Koog for a production use case, start with the Spring Boot integration guide — the path from "existing Spring service" to "service with embedded agent" is the clearest demonstration of the framework's design philosophy.
