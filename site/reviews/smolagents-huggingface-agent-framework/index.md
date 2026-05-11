# Smolagents — HuggingFace's Minimal Code-First Agent Framework

> Smolagents reviewed: HuggingFace's minimal, code-first agent framework. CodeAgent writes and runs Python instead of calling JSON tools. 27.1K stars, Apache-2.0, MCP client support, GAIA benchmark #1. Rating: 4/5.


Most agent frameworks ask the same question: *what JSON should I call?* HuggingFace's smolagents asks a different one: *what Python code should I write?* That distinction is the entire premise — and it's backed by research.

Part of our **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Repo** | [huggingface/smolagents](https://github.com/huggingface/smolagents) |
| **Stars** | ~27,100 |
| **Forks** | ~2,500 |
| **License** | Apache-2.0 |
| **Language** | Python (≥3.10) |
| **Version** | v1.24.0 (January 2026); releases frequently |
| **Install** | `pip install smolagents` |
| **Authors** | Aymeric Roucher, Merve Noyan, Thomas Wolf (HuggingFace) |
| **Downloads** | ~570,000 monthly PyPI downloads |
| **API stability** | Experimental — subject to change |

---

## The Core Idea: Code as Action

The conventional agent loop works like this: the LLM receives a system prompt with a list of available tools described in JSON schema, generates a JSON tool call, the framework executes it, the result goes back to the LLM, and the loop continues. Smolagents runs a different loop: the LLM generates a Python code snippet, the framework executes it, the output goes back as an observation.

This is the `CodeAgent` — smolagents' default and flagship agent type. Instead of calling a single tool per step via structured JSON, the agent can write a small Python program: call two tools and combine their results, iterate over a list, define a helper function, handle a conditional. Anything you can express in Python, the agent can do in a single step.

Three papers back this approach:
- *Executable Code Actions Elicit Better LLM Agents* (arXiv 2402.01030)
- *If LLM Is the Wizard, Then Code Is the Wand* (arXiv 2401.00812)
- *DynaSaur: Large Language Agents Beyond Predefined Actions* (arXiv 2411.01747)

The empirical result: a smolagents multi-agent system reached **#1 on the GAIA benchmark** at 44.2% — four percentage points ahead of Microsoft's AutoGen at 40%.

Smolagents also includes `ToolCallingAgent` for conventional JSON-based tool calling. It's provided for comparison, compatibility (some models handle JSON better), and dispatcher patterns — but it's not the main character.

---

## Core Abstractions

### Tools

Tools in smolagents are Python callables with structured metadata. The base `Tool` class requires `name`, `description`, `inputs` (a dict of parameter specs), `output_type`, and a `forward()` method. The decorator pattern is more concise:

```python
from smolagents import tool

@tool
def get_current_weather(city: str) -> str:
    """Returns the current weather for a given city.
    
    Args:
        city: Name of the city to check.
    """
    return fetch_weather(city)
```

The docstring and type annotations become the tool's description and schema — what the LLM sees when deciding whether to use it. Smolagents also provides:

- `Tool.from_langchain()` — wraps any LangChain tool directly
- `Tool.from_space()` — turns a HuggingFace Space into a tool
- `Tool.from_hub()` — loads a community tool from the HF Hub
- `Tool.push_to_hub()` — shares your tool as a HF Space

The built-in tools cover common needs: `DuckDuckGoSearchTool`, `WebSearchTool`, a Whisper transcriber, and browser automation.

### Agents

`CodeAgent` and `ToolCallingAgent` both inherit from `MultiStepAgent`, which runs the ReAct (Reason → Act → Observe) loop.

```python
from smolagents import CodeAgent, InferenceClientModel

model = InferenceClientModel("Qwen/Qwen3-32B")
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)
result = agent.run("What are the top Python agent frameworks by GitHub stars in May 2026?")
```

Key parameters:

- `additional_authorized_imports` — Python modules the code executor is allowed to import
- `executor_type` — where generated code runs: `"local"` (default), `"e2b"`, `"blaxel"`, `"modal"`, `"docker"`, `"wasm"`
- `planning_interval` — every N steps, inject a dedicated planning step where the agent summarizes known facts and updates its plan (no tool call, just reasoning)
- `step_callbacks` — hooks fired after each step type for custom logging or monitoring
- `use_structured_outputs_internally` — improves accuracy on models that support structured generation

### Memory

`AgentMemory` holds the complete step history as a Python list:

- `TaskStep` — the user's task
- `ActionStep` — LLM output, tool execution, and observations
- `PlanningStep` — planning summaries (when `planning_interval` is set)
- `FinalAnswerStep` — the agent's final output

Memory is **in-process only**. There is no built-in database backend, no PostgreSQL/MongoDB checkpointing, and no persistence across process restarts. You can call `agent.run(task, reset=False)` to preserve memory within a session (conversation mode), and `agent.memory.return_full_code()` exports all code actions as a single Python script — but if the process dies, the state is gone.

---

## Code Execution Sandboxes

The most distinctive runtime characteristic of smolagents is that it executes code — and where that code runs matters significantly.

| Executor | Isolation | Setup |
|----------|-----------|-------|
| `local` | Low (AST-filtered) | None — included by default |
| `docker` | Medium | Docker + Jupyter Kernel Gateway |
| `e2b` | High (cloud VM) | E2B account + API key |
| `blaxel` | High (cloud VM, <25ms cold start) | Blaxel account |
| `modal` | High (serverless) | Modal account |
| `wasm` | High (WebAssembly/Pyodide) | None — zero external dependencies |

The local executor uses a custom AST-based interpreter with whitelisted imports and iteration caps. The documentation explicitly states: **the local executor is not a security boundary**. For untrusted tasks or production deployments, one of the sandboxed executors is appropriate. The WebAssembly executor is the most portable — no accounts required, runs in-process, strong isolation via Pyodide — though it limits available Python packages.

---

## MCP Support

### As an MCP Client

Smolagents connects to external MCP servers via `ToolCollection.from_mcp()` or the lower-level `MCPClient`:

```python
import mcp
from smolagents import CodeAgent, InferenceClientModel, ToolCollection

# Connect to a stdio MCP server
server_params = mcp.StdioServerParameters(
    command="npx",
    args=["-y", "@modelcontextprotocol/server-filesystem", "/home/user/files"]
)

with ToolCollection.from_mcp(server_params, trust_remote_code=True) as tools:
    agent = CodeAgent(tools=[*tools.tools], model=InferenceClientModel())
    agent.run("List the markdown files in my documents directory")
```

Three transports are supported:

- **stdio** — for local MCP servers running as subprocesses
- **Streamable HTTP** — `{"url": "...", "transport": "streamable-http"}` for remote servers
- **SSE** — `{"url": "...", "transport": "sse"}` (older SSE protocol, deprecated in MCP 1.0 but still supported)

Multiple MCP servers can be connected simultaneously by passing a list of server parameters. Since v1.22.0, smolagents also supports `outputSchema` from MCP tools — structured tool outputs are parsed and forwarded correctly rather than treated as raw strings.

### As an MCP Server

Smolagents does not expose agents or tools as MCP servers. There is no built-in mechanism to run a smolagents agent as an endpoint consumable by Cursor, Claude Desktop, or other MCP clients. This is a gap compared to Agno (which exposes agents as MCP endpoints via AgentOS) and Mastra (which includes a full `MCPServer` class). If you need your agent to appear as an MCP server, you would need to implement that layer yourself.

---

## Multi-Agent Orchestration

Multi-agent in smolagents works by treating sub-agents like tools. Any agent with a `name` and `description` attribute becomes a "managed agent" that the manager can invoke:

```python
web_agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
    name="web_search_agent",
    description="Searches the web for current information. Input: search query string."
)

manager = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[web_agent]
)

manager.run("Research the top 5 AI agent frameworks and compare their GitHub stars")
```

The manager CodeAgent sees `web_search_agent` like any other tool and calls it by generating Python code. The sub-agent has its own memory, its own LLM calls, and its own tools.

The architecture is strictly hierarchical — managers delegate to sub-agents, sub-agents do not communicate peer-to-peer. There is no swarm pattern, no conversational agent loops like AutoGen's `GroupChat`, and no dynamic agent spawning at runtime. The GAIA top-1 result used a two-level hierarchy: a manager CodeAgent with planning interval + a web search ToolCallingAgent wrapped as a managed agent.

One limitation: combining multi-agent with sandboxed code execution (E2B or Blaxel in code-only mode) has friction. The managed agent pattern requires the full agentic system to run inside the sandbox with credential transfer, rather than running the orchestration locally and farming out individual code snippets.

---

## LLM Provider Support

Smolagents abstracts LLM access through a family of model classes:

| Class | Backend |
|-------|---------|
| `InferenceClientModel` | HF Inference API + 11 inference providers (Cerebras, Cohere, SambaNova, Together, etc.) |
| `LiteLLMModel` | 100+ providers via LiteLLM (OpenAI, Anthropic, Gemini, Mistral, Bedrock, Ollama, ...) |
| `TransformersModel` | Local HF transformers pipeline |
| `OpenAIModel` | OpenAI API (direct, separate from LiteLLM path) |
| `AmazonBedrockModel` | AWS Bedrock native (boto3) |
| `AzureOpenAIModel` | Azure OpenAI deployments |
| `MLXModel` | Apple Silicon local inference (mlx-lm) |

The InferenceClientModel is the most HuggingFace-native option — it connects through the HF Hub to a growing list of inference providers without requiring separate API keys beyond `HF_TOKEN`. The default model in recent versions is `Qwen/Qwen3-Next-80B-A3B-Thinking`.

---

## HuggingFace Hub Integration

This is where smolagents is genuinely unique among agent frameworks. Because it's built by HuggingFace, agents and tools are first-class Hub objects:

- `agent.push_to_hub("username/my-research-agent")` — publish your agent as a Gradio Space
- `agent.from_hub("username/my-research-agent")` — load and run a community agent
- `tool.push_to_hub("username/my-tool")` — share tools independently
- `Tool.from_hub("username/my-tool")` — load community tools
- `ToolCollection.from_hub(collection_slug)` — load curated tool collections

This creates an ecosystem around agent sharing that no other framework matches. You can browse and use community-built smolagents agents the same way you use community models on the Hub.

The Gradio integration extends this: `GradioUI(agent).launch()` creates an interactive web interface for any smolagents agent in one line, with step-by-step trace display, file upload support, and an interrupt button.

---

## Limitations

**No persistence.** Memory is a Python list that lives in the current process. There is no PostgreSQL backend, no Redis, no vector DB integration in core. If you need durability — resuming after a crash, sharing state across runs, human-in-the-loop that spans multiple sessions — you must implement it yourself. LangGraph's first-class checkpointing (PostgreSQL, MongoDB, SQLite) is a significant advantage here.

**No MCP server.** Smolagents can consume MCP tools but cannot expose its agents or tools as MCP endpoints. Agno, Mastra, and PydanticAI all offer this in the open-source tier.

**Experimental API.** The documentation labels the API explicitly as experimental and subject to change at any time. This is unusual for a framework at 27K stars — it signals that the team prioritizes moving fast over backward compatibility. Plan for breakage on version bumps.

**Strictly hierarchical multi-agent.** No peer-to-peer, no dynamic agent creation, no swarm routing. For flat teams of specialists or conversational agent networks, smolagents is not the right tool.

**No built-in observability.** No LangSmith equivalent, no OpenTelemetry integration in core. Step callbacks exist for custom logging, but production tracing requires external tooling.

**Local executor is not a security boundary.** If agents might encounter untrusted inputs or run in shared environments, the local AST executor is not sufficient. E2B, Docker, or the WASM executor should be used instead — each adding setup complexity.

**LLM quality dependency.** CodeAgent degrades sharply with weaker models that cannot write valid Python reliably. The docs recommend using the strongest available model first when debugging.

---

## What It's Good For

Smolagents earns its 27K stars in a specific niche: **Python developers who want a minimal, research-backed, HuggingFace-integrated framework for complex reasoning tasks**.

The code-first approach genuinely outperforms JSON tool calling on multi-step reasoning benchmarks. If your use case involves agents that need to combine results from multiple sources, loop over data, or do conditional logic — and you can afford the LLM quality requirement — `CodeAgent` is a meaningful improvement over conventional tool calling.

The HF Hub integration is a real differentiator. If you're building on HF models, using HF Inference API endpoints, or want to share your agents publicly, no other framework integrates as naturally.

For production stateful workflows — multi-session conversations, resumable long-running tasks, human-in-the-loop that spans process restarts — smolagents' lack of persistence is a hard blocker. LangGraph is the better choice there.

---

## Rating: 4/5

Smolagents earns its stars with a genuinely distinctive approach (code-as-action, backed by research), a clean minimal codebase, and the deepest HuggingFace ecosystem integration of any agent framework. The GAIA benchmark result is a concrete demonstration, not marketing. MCP client support covers all current transports.

The deductions: no persistence is a real gap for production use, the experimental API label is honest but requires caution, there's no MCP server capability (a gap versus Agno and Mastra), and the Python-only and strictly hierarchical multi-agent model limit scope. This is a strong framework for its niche — complex reasoning, HF ecosystem, hackable minimal code — not a universal production platform.

| Capability | Notes |
|-----------|-------|
| **MCP Client** | ✓ stdio, SSE, Streamable HTTP |
| **MCP Server** | ✗ Not supported |
| **Multi-agent** | Hierarchical manager pattern |
| **Memory/persistence** | In-process only |
| **Human-in-the-loop** | Limited (answer validation hooks, interrupt button) |
| **Language** | Python only |
| **License** | Apache-2.0 |
| **API stability** | Experimental |

