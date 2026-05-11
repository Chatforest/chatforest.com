# GPT Researcher MCP Server — Deep Research as a Tool Call

> GPT Researcher MCP Server reviewed: wrap the 26.9K-star autonomous research agent as an MCP tool, letting AI assistants delegate deep web research and report generation instead of doing basic search. MIT License. Rating: 3.5/5.


Standard web search returns a list of URLs and snippets. The LLM reads those snippets, maybe follows a few links, and synthesizes an answer — fast, but shallow, and limited by how many sources fit in the context window. [GPT Researcher](https://github.com/assafelovic/gpt-researcher) was built on the premise that this isn't good enough for serious research questions. The autonomous agent explores the web in depth, cross-validates sources, discards irrelevant results, and produces synthesized findings with citations — a process that takes 30 to 40 seconds but mirrors how a human researcher would approach a topic.

[gptr-mcp](https://github.com/assafelovic/gptr-mcp) wraps that engine as MCP tools, making the full GPT Researcher pipeline available to any MCP-compatible client — including Claude — as a tool call. The result is a pattern that points somewhere interesting: an LLM delegating specialized cognitive work to another specialized agent, rather than doing everything itself.

Part of our **[Web Search & Scraping MCP category](/categories/web-search-scraping/)**.

---

## At a Glance

| | |
|---|---|
| **Repo** | [assafelovic/gptr-mcp](https://github.com/assafelovic/gptr-mcp) |
| **Stars** | ~344 |
| **License** | MIT |
| **Language** | Python |
| **Parent project** | [gpt-researcher](https://github.com/assafelovic/gpt-researcher) — 26.9K stars, Apache-2.0 |
| **Releases** | None (37 commits on master) |
| **Author** | Assaf Elovic |
| **Requirements** | Python 3.11+, OpenAI API key, Tavily API key |
| **Install** | `git clone` + `pip install -r requirements.txt` |
| **Transports** | STDIO (local), SSE (Docker), Streamable HTTP |

---

## The Parent Project

Before reviewing the MCP server, it's worth grounding the parent. GPT Researcher is not a search wrapper. It uses a **planner-executor architecture**: a planner agent generates a research plan (sub-questions, source strategy), execution agents gather information from 20+ sources in parallel, and an aggregator synthesizes the findings into a coherent report with citations. The output routinely exceeds 2,000 words with verifiable sources.

At 26.9K stars, GPT Researcher is one of the most-adopted autonomous research agents in open source. The author, Assaf Elovic, has maintained it actively since 2023. The project supports web research, local document research (PDF, Excel, Word), JavaScript-enabled scraping, and multi-agent workflows via LangGraph.

gptr-mcp makes this engine callable from an MCP client with a single tool invocation.

---

## Tools

The server exposes six tools and one prompt:

| Tool | What it does |
|------|-------------|
| `deep_research` | Full GPT Researcher pipeline — autonomous multi-source exploration, ~30-40 seconds |
| `quick_search` | Fast web search, optimized for speed over depth, returns snippets |
| `write_report` | Generate a structured report from research results |
| `get_research_sources` | Retrieve the list of sources used in the last research run |
| `get_research_context` | Access the full synthesized context from the last research run |
| `research_resource` | Get web resources for a specific task |

**Prompt**: `research_query` — create a properly-structured research query prompt.

The two primary tools represent an explicit quality-vs-speed tradeoff: `deep_research` for questions that deserve thorough answers, `quick_search` when you need something fast and approximate.

---

## What Makes This Different from Standard Search

Most MCP search tools — Brave Search, Tavily, Exa — return raw search results: a ranked list of URLs, titles, and snippets. The LLM then decides what to read, what to trust, and how to synthesize the answer. This is fast but has clear limits: context window pressure from raw results, no cross-validation across sources, and quality that degrades when a topic requires nuanced source evaluation.

GPT Researcher's pipeline handles all of that before the LLM ever sees the output:

1. Plans the research (what sub-questions to explore, which sources to target)
2. Crawls and scrapes 20+ sources in parallel
3. Evaluates source reliability and relevance
4. Discards noise and irrelevant content
5. Synthesizes findings into coherent, cited output

The tradeoff is latency. A `deep_research` call takes 30 to 40 seconds — acceptable in an async workflow or when research quality matters, frustrating in an interactive session where the user is waiting.

---

## Setup

```bash
git clone https://github.com/assafelovic/gptr-mcp.git
cd gptr-mcp
pip install -r requirements.txt
cp .env.example .env
# Edit .env: set OPENAI_API_KEY and TAVILY_API_KEY
python server.py
```

**Claude Desktop** integration requires adding the server to `~/Library/Application Support/Claude/claude_desktop_config.json`. Note that environment variables don't auto-load in Claude Desktop — API keys must be specified explicitly in the config file.

**Docker** is supported via `docker-compose up -d`; it auto-switches to SSE transport in a Docker environment.

---

## The API Key Dependency

The most significant friction point is the dual API key requirement: **OpenAI** for the LLM reasoning layer and **Tavily** for web retrieval. This means gptr-mcp is not a standalone tool — it has ongoing operational costs beyond the MCP client's own API usage.

Tavily is the default retriever, but GPT Researcher supports alternatives (Bing, Google, DuckDuckGo, Serper, and others). Switching retrievers requires configuration beyond the defaults.

For teams already running GPT Researcher or already paying for Tavily, this is a non-issue. For users evaluating the MCP server cold, it adds onboarding friction that simpler search MCP servers (Brave Search, etc.) don't have.

---

## What's Missing

- **No formal versioned releases** — 37 commits on master, no tags or releases; there's no stable release reference
- **No MCP Registry listing** — not in the official Anthropic MCP registry as of this writing
- **Star count modest** — 344 stars on gptr-mcp specifically (the parent's 26.9K doesn't transfer directly)
- **Latency** — 30-40s `deep_research` calls are slow for interactive use; the tool is better suited to async or batch workflows
- **OpenAI dependency** — the reasoning layer defaults to OpenAI; configuring alternatives requires more setup

---

## The Pattern It Demonstrates

gptr-mcp represents something broader than a single tool: the pattern of **LLM-to-agent delegation via MCP**. Rather than Claude doing web research itself (using search tools, reading pages, synthesizing), Claude delegates the research task to a specialized autonomous agent and receives synthesized output.

This is different from tool-augmented LLMs (where the LLM calls tools and processes results itself) and different from managed agent platforms (where orchestration is opaque). It's a clean interface: Claude says "research this topic," GPT Researcher runs its full pipeline, Claude receives validated findings.

As MCP adoption grows, this delegation pattern — specialized agents exposing their capabilities as MCP tools — seems likely to expand. gptr-mcp is an early, functional example of it.

---

## Rating: 3.5/5

**Strengths:** Backed by a 26.9K-star proven engine; MIT license; multiple transport options; genuine capability gap filled (deep research vs. shallow search); demonstrates an important architectural pattern; active parent project with strong maintenance history.

**Weaknesses:** Dual API key requirement (OpenAI + Tavily) adds operational cost and setup friction; no formal versioned releases; 30-40s latency limits interactive use cases; modest star count on the MCP-specific repo (344); Python 3.11+ strict requirement.

The underlying GPT Researcher engine earns a higher score on its own merits. The MCP wrapper is functional but adds friction without adding capability — it's a bridge, not an enhancement. Worth evaluating if you need validated multi-source research in your agent workflow and are already comfortable with the API key overhead.

---

## See Also

- [Search Engine MCP Servers](/reviews/search-engine-mcp-servers/) — Elasticsearch, OpenSearch, Meilisearch, Algolia
- [Brave Search MCP Server](/reviews/brave-search-mcp-server/) — lightweight, fast, single API key
- [Web Search & Scraping category](/categories/web-search-scraping/)

