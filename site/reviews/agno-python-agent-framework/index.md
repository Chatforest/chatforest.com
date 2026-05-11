# Agno — The High-Performance Python Agent Framework (Formerly Phidata)

> Agno reviewed: a production-ready Python agent framework with 39.8K stars, MPL-2.0 license, and v2.6.4 release. Agents, Teams, Workflows, RAG, memory, and AgentOS runtime. MCP client support built in. Rating: 4.5/5.


Most Python agent frameworks get their MCP integration as an afterthought. Agno treats it as a first-class production concern — not just a plugin, but part of a complete agent runtime that can both consume MCP servers and expose itself as one. At **39,800 stars** and v2.6.4 (released April 28, 2026), Agno is one of the largest Python agent projects on GitHub, and its performance-first design philosophy makes it worth a serious look.

Originally launched as Phidata and rebranded to Agno in January 2025, the framework has evolved from a data engineering tool into a dedicated agentic runtime. Part of our **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Repo** | [agno-agi/agno](https://github.com/agno-agi/agno) |
| **Stars** | ~39,800 |
| **License** | Mozilla Public License 2.0 (MPL-2.0) |
| **Language** | Python |
| **Version** | v2.6.4 (April 28, 2026) |
| **Install** | `pip install agno` |
| **Author** | Ashpreet Bedi / Agno Inc. (formerly Phidata) |
| **Rebranded** | January 2025 |

---

## What It Does

Agno is a Python framework for building production AI agent systems. The core bet is that agent infrastructure should be fast, minimal, and model-agnostic — and that existing frameworks carry too much overhead for real production workloads.

The framework organizes around four building blocks:

1. **Agents** — autonomous LLM-powered agents with tools, memory, knowledge, and reasoning. Agent creation runs at approximately 2 microseconds and consumes ~3.75 KiB of memory on average. The team benchmarks this at ~10,000x faster and ~50x less memory than LangGraph, though these numbers measure framework overhead rather than LLM latency, which dominates in practice.
2. **Teams** — groups of specialized agents that can collaborate, delegate tasks, and share state. Teams support coordinator patterns (one agent routes to specialists) as well as collaborative patterns (agents work in parallel on sub-problems).
3. **Workflows** — structured, repeatable pipelines that orchestrate agents and functions through defined steps. Workflows are useful when you want predictable, inspectable execution — research pipelines, data processing, triage flows.
4. **AgentOS** — a production runtime layer that wraps agents, teams, and workflows in a FastAPI-based REST API server. AgentOS handles session management, conversation storage, traces, and monitoring in your own database. It is what Agno calls "the missing piece" between a working agent prototype and a deployed product.

---

## MCP Support

Agno supports MCP in both directions.

### As an MCP Client (MCPTools)

The `MCPTools` class connects any Agno agent to an external MCP server and surfaces its tools as native agent tools. Both stdio (local subprocess) and SSE (HTTP remote) transports are supported. A `header_provider` function allows dynamic header generation for authenticated MCP endpoints — important for production deployments where MCP servers require authorization tokens.

MCPTools also supports `requires_confirmation_tools` for human-in-the-loop: specific MCP tools can require explicit approval before execution, which is useful for high-consequence operations like writing to databases or sending messages.

```python
from agno.agent import Agent
from agno.tools.mcp import MCPTools

agent = Agent(
    name="research-agent",
    tools=[
        MCPTools(
            command="npx -y @modelcontextprotocol/server-filesystem /tmp"
        )
    ],
)
```

When agents run inside AgentOS, MCPTools lifecycle (connection setup, session persistence, teardown) is automatically managed by the FastAPI application lifespan — no manual connection handling required.

### As an MCP Server (AgentOS)

Agno's AgentOS can expose its agents, teams, and workflows as MCP-compatible tools by setting `enable_mcp_server=True` on the AgentOS instance. This creates an MCP endpoint at `/mcp` that external MCP clients — including Cursor, Claude Desktop, and Windsurf — can connect to and discover.

```python
from agno.app.agentapp import AgentOS

agent_os = AgentOS(
    agents=[research_agent, writer_agent],
    enable_mcp_server=True,
)
```

The capability is production-quality: lifecycle management is handled by FastAPI, and the MCP server endpoint is stable and persistent for the lifetime of the application.

---

## LLM Support

Agno supports 23+ LLM providers with a plug-and-play design — swap providers without rewriting agent logic. Supported providers include:

- **Anthropic** (Claude Sonnet, Haiku, Opus)
- **OpenAI** (GPT-4o, o4, o3)
- **Google Gemini**
- **DeepSeek**
- **Mistral**
- **AWS Bedrock**
- **Azure OpenAI**
- **Groq**
- **Ollama** (local inference)
- **LiteLLM gateway** (access to additional providers through a unified interface)

Multimodal support covers text, image, audio, and video inputs, which the team describes as a core design goal — not an add-on.

---

## Memory and Knowledge

Agno distinguishes two kinds of persistence:

**Memory** tracks conversations and agent state. Short-term memory maintains context within a session; long-term storage is a durable database-backed store for agents that run across sessions, operate on schedules, or need to evolve over time.

**Knowledge** is the RAG layer. Agno integrates with standard vector stores (pgvector, Pinecone, Qdrant, Chroma, and others) for embedding-based retrieval. Documents can be chunked, embedded, stored, and retrieved as context for agent reasoning. The framework calls this "Agentic RAG" — knowledge retrieval that is triggered by the agent's own reasoning rather than injected at prompt time.

---

## Performance Claims

Agno's benchmarks show ~2μs agent instantiation and ~3.75 KiB memory per agent, comparing favorably against LangGraph's reported overhead. It is worth being precise about what this measures: the framework's own setup cost, not inference latency. In production, LLM API calls dominate response time by several orders of magnitude. The performance advantage matters most for systems that create large numbers of agents dynamically, or where startup latency at scale is a concern.

---

## What Works Well

- **Low boilerplate** — agent creation is concise; the framework stays out of the way
- **Model-agnostic** — switching LLMs or providers requires changing one line
- **Bidirectional MCP** — both client and server, with production lifecycle management built in
- **AgentOS** — moving from prototype to deployed API is a configuration change, not a rewrite
- **Human-in-the-loop** — `requires_confirmation_tools` for MCP is production-ready
- **39,800+ stars** — large, active community with 5,300+ forks and regular releases

---

## Limitations

- **Python-only** — no TypeScript/JavaScript support; teams building full-stack Node.js applications need a different framework (e.g., Mastra)
- **Younger ecosystem than LangChain** — fewer third-party integrations and tutorials compared to the most established Python frameworks
- **Multi-agent complexity** — Teams and coordination patterns introduce state-sharing overhead; getting multi-agent interactions wrong creates expensive failure modes rather than simple ones
- **AgentOS surface area** — the production runtime adds operational complexity (FastAPI server, database, traces) that not all projects need; simpler use cases may find it heavyweight
- **MPL-2.0 implications** — modifications to Agno's source files must be shared under MPL-2.0; this is a copyleft license that requires source disclosure for modified versions (though applications built *using* Agno are not affected)

---

## Compared to Other Frameworks Reviewed

| Framework | Language | Stars | MCP Client | MCP Server | License |
|---|---|---|---|---|---|
| **Agno** | Python | ~39,800 | Yes (MCPTools) | Yes (AgentOS) | MPL-2.0 |
| Mastra | TypeScript | ~23,600 | Yes | Yes (MCPServer) | Apache-2.0 (core) |
| mcp-agent | Python | ~8,100 | Yes (6 patterns) | No | Apache-2.0 |
| mcp-use | Python/TS | ~9,900 | Yes | No | MIT |

---

## Who Should Use Agno

Agno fits teams that:

- Are building Python-based agent systems and want a production runtime (not just a prototyping library)
- Need bidirectional MCP — both consuming MCP servers as tools and exposing agents as MCP endpoints
- Want to swap LLMs across providers without code changes
- Are building multi-agent systems and prefer a structured Teams abstraction over rolling their own coordination

It is less suited for TypeScript shops, projects needing LangChain's ecosystem depth, or teams wanting a minimal library without a full runtime layer.

---

## Rating: 4.5 / 5

Agno earns its star count. The bidirectional MCP support is production-quality, the performance profile is genuinely useful at scale, and AgentOS closes the prototype-to-deployment gap without requiring a separate infrastructure project. The MPL-2.0 license and Python-only constraint are the main things to evaluate against your stack before adopting.

*This review is based on publicly available documentation, GitHub repository analysis, and community reports. ChatForest researches but does not independently run or test the frameworks reviewed here.*

