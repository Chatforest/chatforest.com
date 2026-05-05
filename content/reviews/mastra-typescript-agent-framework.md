---
title: "Mastra — The TypeScript Agent Framework With Bidirectional MCP Support"
date: 2026-05-05T28:00:00+09:00
description: "Mastra reviewed: a production-ready TypeScript agent framework from the team behind Gatsby. 23.6K stars, Apache-2.0 core, v1.0. Agents, workflows, RAG, memory, evals — and bidirectional MCP: consume any MCP server, expose agents as MCP servers. Rating: 4.5/5."
og_description: "Mastra (23.6K stars, Apache-2.0 core, TypeScript): the production-ready agent framework from the Gatsby team. Full stack for TypeScript AI agents: autonomous agents, multi-step workflows with branching, RAG pipeline, persistent memory with semantic recall, model-graded evals, and observability. Bidirectional MCP — connect to any MCP server as a client AND expose your tools and agents as an MCP server compatible with Cursor, Claude Desktop, and Windsurf. v1.0 released January 2026. @mastra/core v1.31.0. 300K+ weekly npm downloads. Enterprise features (ee/ directory) require paid license for production. Rating: 4.5/5."
content_type: "Review"
card_description: "Mastra (23.6K stars, v1.0, Apache-2.0 core, TypeScript) is the production-ready TypeScript agent framework from the team behind Gatsby. One framework covers everything: autonomous LLM agents with typed tools, multi-step branching workflows, full RAG pipeline (chunking → embedding → vector storage → reranking), persistent memory with semantic recall and observational compression, model-graded and rule-based evals, and built-in OpenTelemetry observability. The MCP story is bidirectional: connect Mastra agents to any external MCP server as a client (stdio/SSE), and expose your own tools and agents as an MCP server via the MCPServer class — agents are auto-converted to ask_<agentKey> tools callable from Cursor, Claude Desktop, or Windsurf. LLM support via AI SDK v3: Anthropic (Claude), OpenAI, Google Gemini, AWS Bedrock, Azure OpenAI, Groq, Ollama, and more. Install with npx create-mastra@latest or npm install @mastra/core. Reached 1.0 in January 2026, @mastra/core now at v1.31.0, 300K+ weekly npm downloads. Core is Apache-2.0; enterprise features in the ee/ directory require a paid license for production use. Main limitations: TypeScript-only, smaller integration ecosystem than LangChain, no SOC 2 yet. Part of our **Developer Tools** category. Rating: 4.5/5."
last_refreshed: 2026-05-05
categories: ["/categories/developer-tools/"]
---

Most MCP reviews on this site focus on servers — the things that expose capabilities to agents. Mastra is in a different class: a comprehensive TypeScript framework for building those agents, complete with its own bidirectional MCP layer. At **23,600 stars** with a v1.0 release and 300K weekly npm downloads, it is one of the most widely adopted agent frameworks in the TypeScript ecosystem.

From [the team behind Gatsby](https://github.com/mastra-ai), Mastra ships everything an agent system needs in one coherent package: autonomous agents, multi-step workflows, a full RAG pipeline, persistent memory, model-graded evals, and observability. The MCP integration goes both directions — consume any MCP server as a tool source, and expose your own agents as MCP-compatible endpoints. Part of our **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Repo** | [mastra-ai/mastra](https://github.com/mastra-ai/mastra) |
| **Stars** | ~23,600 |
| **License** | Apache-2.0 (core) / Mastra Enterprise License (ee/) |
| **Language** | TypeScript / Node.js |
| **Version** | @mastra/core v1.31.0; CLI mastra v1.8.1 |
| **v1.0 released** | January 2026 |
| **Install** | `npx create-mastra@latest` or `npm install @mastra/core` |
| **Author** | mastra-ai (team behind Gatsby) |
| **Weekly downloads** | 300K+ npm |

---

## What It Does

Mastra is a TypeScript framework for building AI-powered agents and applications. The core premise is that agent development has too many disconnected pieces — a library for tool calling here, another for vector search there, a separate eval framework elsewhere — and production systems need these things to compose cleanly. Mastra provides them as a unified, strongly-typed package.

The six pillars:

1. **Agents** — LLM-powered autonomous agents that reason about goals, select tools, and iterate until a task is complete. Agents are built on [Vercel's AI SDK v3](https://sdk.vercel.ai), which provides the multi-provider LLM abstraction.
2. **Workflows** — Declarative multi-step pipelines with branching, parallel execution, and error handling. Workflows have time-travel debugging: you can replay and inspect execution states.
3. **RAG** — The full retrieval pipeline: document chunking, embedding generation, vector storage, similarity search, and reranking. Works with Pinecone, Qdrant, Chroma, pgvector, and others.
4. **Memory** — Four memory layers: conversation history, semantic recall (embedding-based retrieval of relevant past messages), working memory (structured facts the agent maintains), and observational memory (compresses old conversations into dense summaries to manage context window costs).
5. **Evals** — Model-graded, rule-based, and statistical evaluations for testing agent quality. Covers relevance, faithfulness, toxicity, tone consistency, and custom metrics.
6. **Observability** — Built-in tracing compatible with OpenTelemetry. Integrates with Langfuse, Braintrust, and other observability platforms.

---

## Bidirectional MCP Support

Mastra's MCP story is the most complete of any agent framework reviewed here — it operates in both directions simultaneously.

### As an MCP Client

Mastra agents can connect to any external MCP server using the `MCPConfiguration` class. Both stdio (local subprocess) and SSE (HTTP remote) transports are supported. Once connected, the MCP server's tools appear in the agent's tool registry and are callable like any native Mastra tool. This means any of the 12,000+ MCP servers in the ecosystem are immediately usable as Mastra agent tools.

```typescript
import { MCPConfiguration } from "@mastra/mcp";

const mcp = new MCPConfiguration({
  servers: {
    filesystem: {
      command: "npx",
      args: ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"],
    },
    fetch: {
      url: "http://localhost:3001/sse",
    },
  },
});

const agent = new Agent({
  name: "my-agent",
  model: anthropic("claude-sonnet-4-6"),
  tools: await mcp.getTools(),
});
```

### As an MCP Server

The `MCPServer` class exposes your Mastra tools and agents to any MCP client. This is the less common direction — most frameworks only consume MCP servers. Mastra can serve them.

Agents are automatically converted to callable tools named `ask_<agentKey>`. An agent registered as `{ researchAgent: researchAgentInstance }` becomes a tool `ask_researchAgent` that accepts a `{ message: string }` argument. This pattern lets you build a Mastra agent system and then expose it to Cursor, Claude Desktop, Windsurf, or any other MCP-compatible client without any additional integration work.

```typescript
import { MCPServer } from "@mastra/mcp";

const server = new MCPServer({
  name: "my-mastra-server",
  version: "1.0.0",
  tools: { webSearch, codeAnalyzer },
  agents: { researchAgent, summaryAgent },
});

// Serve via stdio (for local MCP clients)
await server.startStdio();
// or SSE (for HTTP MCP clients)
await server.startSSE({ port: 3001 });
```

Both stdio and SSE transports are supported for serving.

---

## LLM Support

Mastra uses AI SDK v3 as its LLM abstraction layer, which means any AI SDK-compatible provider works:

- **Anthropic** — Claude (claude-sonnet-4-6, claude-opus-4-6, Haiku)
- **OpenAI** — GPT-4o, o4, reasoning models
- **Google** — Gemini 2.0, Gemini 1.5
- **AWS Bedrock** — cross-provider access via AWS
- **Azure OpenAI**
- **Groq** — fast inference, Llama 3, Mistral
- **Ollama** — local models
- **OpenRouter** — 100+ models via unified API
- **Mistral, Cohere, and others** — via AI SDK providers

The LLM choice is a single-line configuration change. Agents, workflows, and evals all use the same provider interface.

---

## Memory System in Depth

Mastra's memory system is worth examining separately because it is more nuanced than simple conversation history.

**Conversation history** stores recent turns verbatim. **Semantic recall** uses embeddings to find relevant past messages from anywhere in the conversation history, not just recent turns — so an agent working on a project can surface context from a conversation three weeks ago when it becomes relevant.

**Working memory** is a structured JSON object the agent actively maintains — it tracks facts like user preferences, project state, and named entities throughout a session. The agent can read and update working memory mid-conversation.

**Observational memory** is a compression layer: when older conversation segments fall outside the active context window, Mastra compresses them into dense observations rather than truncating. This prevents context blowups during long-running workflows.

One caution noted by the community: observational memory triggers LLM calls internally for compression. These calls are not always surfaced clearly in cost dashboards. Teams with high-volume agents should monitor this.

---

## Workflows and Time-Travel Debugging

Mastra's workflow engine supports:

- **Sequential steps** — straightforward chains
- **Branching** — conditional routing based on step output
- **Parallel execution** — fan-out across independent steps, collect results
- **Error handling** — per-step retry and fallback logic
- **Suspend/resume** — workflows can pause at a step waiting for external input (human-in-the-loop)

The standout feature is **time-travel debugging**: you can inspect the execution state at any point in a past workflow run, replay from any step, and observe how changing inputs would have changed the result. This is a significant improvement over frameworks that require manual logging to understand workflow failures.

---

## Deployment

```bash
npx create-mastra@latest   # scaffold a new project
npm install @mastra/core   # or install core directly
mastra dev                 # local development server
mastra deploy              # deploy to hosting
```

Mastra deploys as a Node.js HTTP server. It integrates natively with Next.js (as API routes or a server component), and can be deployed standalone to any Node.js hosting — Vercel, Railway, Fly.io, Docker containers, AWS Lambda via a layer.

---

## Known Limitations

**TypeScript-only** — Mastra has no Python equivalent. The AI SDK v3 underpinning is JavaScript/TypeScript. Python-first teams have no migration path — mcp-agent or mcp-use are the Python alternatives.

**Enterprise license for ee/ features** — The core framework is Apache-2.0, but the `ee/` directory contains enterprise features (advanced observability dashboards, RBAC, audit logs, and some memory features) that require a paid Mastra Enterprise License for production use. The license is free for development and testing. The line between core and enterprise features is not always clearly signposted in the documentation.

**No SOC 2 compliance** — As of early 2026, Mastra has not achieved SOC 2 certification. Enterprise security teams evaluating regulated deployments should note this.

**Smaller integration ecosystem** — LangChain has 1,000+ integrations built up over years; Mastra's ecosystem is growing but not there yet. For unusual data connectors or niche APIs, LangChain or direct SDK integrations may be more practical.

**Observational memory costs** — The hidden LLM calls for memory compression are a real cost factor at scale. The documentation mentions this but does not give enough guidance on setting limits to avoid runaway token usage.

**Docs gaps** — Some areas of the documentation are thinner than others, particularly around advanced workflow patterns and the enterprise features. The changelog-driven update cadence means some features ship faster than docs catch up.

---

## How It Compares

| Framework | Language | MCP Client | MCP Server | v1.0 | Stars |
|---|---|---|---|---|---|
| **Mastra** | TypeScript | Yes (stdio/SSE) | Yes (MCPServer) | Yes | 23.6K |
| mcp-agent | Python | Yes | No | No (v0.2.6) | 8.1K |
| mcp-use | Python + TS | Yes | No | No | 9.9K |
| LangGraph | Python | Yes (added later) | No | Yes | ~10K |
| CrewAI | Python | Yes (tools) | No | Yes | ~23K |

The bidirectional MCP capability is Mastra's clearest differentiator among agent frameworks. Most frameworks consume MCP servers; few can serve as one. The TypeScript-only constraint is the main reason to look elsewhere.

---

## Who Should Use This

**Best fit:**
- TypeScript/Node.js teams building production AI features in Next.js or standalone services
- Developers who want a single framework covering agents, RAG, memory, and evals without assembling a stack
- Teams that want to expose their agent system as an MCP server for use in Cursor, Claude Desktop, or other MCP-compatible dev tools
- Projects that benefit from time-travel workflow debugging

**Not the right fit:**
- Python-first teams (no Python equivalent)
- Developers who only need a simple LLM-to-MCP connection (mcp-use is lighter)
- Enterprises with hard SOC 2 requirements (not certified yet)
- Projects where LangChain's integration breadth is a must-have

---

## Rating: 4.5 / 5

Mastra is the most complete TypeScript agent framework available today. The combination of agents, workflows, RAG, memory, evals, and observability in one coherent package is genuinely rare — most frameworks cover one or two of these and leave the rest to you. The bidirectional MCP support goes further than any framework reviewed here: connecting to MCP servers as a client is table stakes now, but auto-exposing your agents as MCP server tools for Cursor and Claude Desktop is a meaningful differentiator for teams building in the AI-native dev tooling space.

At 23,600 stars, v1.0, and 300K weekly npm downloads, Mastra has proven itself beyond the experimental stage. The Apache-2.0 core license is clean for most use cases.

The deductions: TypeScript-only excludes a large portion of the AI development community, the enterprise feature gating is not well-signposted, the observational memory cost behavior needs better documentation, and no SOC 2 limits regulated enterprise adoption.

For TypeScript teams building serious agent applications, Mastra is the framework to evaluate first.
