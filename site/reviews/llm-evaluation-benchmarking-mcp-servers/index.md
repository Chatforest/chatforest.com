# LLM Evaluation & Benchmarking MCP Servers — Eval Frameworks, MCP Benchmarks, Red-Teaming, and 20+ More

> LLM evaluation and benchmarking MCP servers help AI agents evaluate outputs, benchmark MCP server performance, red-team AI systems, and run LLM-as-a-judge assessments.


**Category:** [AI & ML Tools](/categories/ai-ml-tools/)

LLM evaluation is one of the hardest problems in AI engineering — and the MCP ecosystem has matured dramatically since our initial review. **Two ICLR 2026 papers** (MCP-Bench, OSWorld-MCP) now establish MCP benchmarking as a serious academic discipline. **OpenAI acquired Promptfoo** in March 2026, signaling that LLM evaluation and red-teaming are now core infrastructure, not afterthoughts. And **DeepEval tripled its community** from 5K to 15K stars, adding Multi-Turn MCP Use metrics for conversational agent evaluation.

The ecosystem now splits into three distinct problems: **evaluating LLM outputs** (is the response correct, relevant, safe?), **evaluating MCP servers** (does this server work reliably? how well can agents use its tools?), and — new since March — **evaluating computer-use agents** (can agents effectively combine MCP tools with GUI operations?). All three are now well-represented with research-grade tooling.

For testing browser automation and cloud test platforms, see our [Testing & QA](/reviews/testing-qa-mcp-servers/) review. For prompt optimization tools, see our [Prompt Engineering & Optimization](/reviews/prompt-engineering-optimization-mcp-servers/) review. For code quality analysis, see our [Code Quality & Linting](/reviews/code-quality-linting-mcp-servers/) review.

## LLM Output Evaluation Frameworks (3+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 20.6K | TypeScript | MIT | CLI + MCP | All-in-one eval, red-teaming, and CI/CD — now OpenAI-owned |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | 15K | Python | Apache-2.0 | MCP via Confident AI | Pytest-style LLM unit testing with 50+ metrics + Multi-Turn MCP Use |
| [berkayildi/mcp-llm-eval](https://github.com/berkayildi/mcp-llm-eval) | — | Python | MIT | 8 | CI/CD eval gates with threshold checks and regression detection |

**promptfoo** (20.6K stars, up from 10.8K — nearly doubled) is the heavyweight of LLM evaluation, and as of **March 9, 2026, is owned by OpenAI**. The acquisition integrates Promptfoo's technology into OpenAI Frontier for automated red-teaming, agentic workflow evaluation, and compliance monitoring. Promptfoo remains open source under MIT. It's a CLI and library used by 25%+ of Fortune 500 companies for testing prompts, agents, and RAG pipelines. It supports comparing outputs across GPT, Claude, Gemini, Llama, and more with simple declarative YAML configs. The MCP integration works through an `mcp-agent-provider` that creates OpenAI-based ReAct agents to test MCP servers. The red-teaming module scans for **50+ vulnerability types** including direct/indirect prompt injection, jailbreaks, PII leaks, tool misuse, and toxic content. The **MCP Proxy** provides enterprise-grade security with access control and traffic monitoring. The **MCP Plugin** specifically tests whether agentic systems using MCP are vulnerable to function call exploits, system prompt leakage, and unauthorized tool discovery. CI/CD integration with GitHub Actions makes it production-ready. Now at v0.121.9 with 8,334 commits — actively maintained despite the acquisition.

**DeepEval by Confident AI** (15K stars, up from 5K — **tripled**) takes the Pytest approach — you write test cases for your LLM app the same way you'd write unit tests. 50+ metrics including G-Eval, task completion, answer relevancy, hallucination detection, and faithfulness, using both LLM-as-a-judge and local NLP models. The **MCP-Use metric** specifically evaluates how effectively MCP-based agents use their available servers — scoring tool selection, argument quality, and overall task completion. **New since our last review: the Multi-Turn MCP Use metric** evaluates conversational MCP agents across multi-turn interactions, assessing how effectively agents use MCP primitives (Tools, Resources, Prompts) over extended dialogues. Confident AI's MCP server acts as a persistent data layer for running evals, pulling datasets, and inspecting traces directly from Claude Code or Cursor without leaving your editor. Now at 9,276 commits with 210 open issues — extremely active development.

**berkayildi/mcp-llm-eval** *(new since last review)* packages LLM evaluation gates as reusable **CI/CD primitives** — solving the problem that teams ship prompt changes with no automated way to verify output quality didn't regress. Eight MCP tools: `run_evaluation` (datasets against multiple models with LLM-as-judge), `check_thresholds` (quality gates for faithfulness, relevance, latency, cost — exit code 1 blocks PRs), `compare_runs` (regression detection), `format_pr_comment` (markdown summaries for PRs), `evaluate_retrieval` (recall, precision, MRR, nDCG), `evaluate_rag_end_to_end` (full RAG pipeline with judging), and `check_retrieval_drift` (flags retrieval regressions). Also works as a standalone CLI binary for CI/CD pipelines. Python 3.10+, MIT license. Partially closes the CI/CD gap we identified in March.

**Note:** atla-ai/atla-mcp-server, previously reviewed here for purpose-built LLM-as-a-judge evaluation via the Selene model family, was **archived on GitHub in July 2025 and the Atla API is no longer active**. Teams previously using Atla should consider DeepEval's LLM-as-a-judge metrics or promptfoo's evaluation capabilities as alternatives.

## MCP Server Benchmarking (5+ projects)

| Project | Stars | Language | License | Servers/Tasks | Key Feature |
|---------|-------|----------|---------|--------------|-------------|
| [SalesforceAIResearch/MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe) | 583 | Python | — | 11 servers, 231 tasks | Real-world servers + MCP+ token optimization |
| [Accenture/mcp-bench](https://github.com/Accenture/mcp-bench) | 475 | Python | — | 28 servers, 250 tools | **ICLR 2026** end-to-end tool-use evaluation |
| [eval-sys/mcpmark](https://github.com/eval-sys/mcpmark) | 413 | Python | Apache-2.0 | 5 services, 127 tasks | Stress-testing across real MCP services |
| [modelscope/MCPBench](https://github.com/modelscope/MCPBench) | 244 | Python | — | Multiple, 600+ QA pairs | Server-side accuracy, latency, and token consumption |
| [X-PLUG/OSWorld-MCP](https://github.com/X-PLUG/OSWorld-MCP) | 223 | Python | — | 158 tools, 361 tasks | **ICLR 2026** computer-use + MCP tool invocation |

**SalesforceAIResearch/MCP-Universe** (583 stars, up from ~0 in March — massive growth) benchmarks LLMs with real-world MCP servers across **6 domains** (Location Navigation, Repository Management, Financial Analysis, 3D Design, Browser Automation, Web Searching) and **231 tasks** using 11 MCP servers. **New since March:** MCP-Universe now includes **MCP+** ("Precision Context Management for MCP Agents"), which reduces token costs by up to **75%** through intelligent post-processing of tool outputs — addressing the cost-aware evaluation gap we identified. Also new: a **Deep Research Agent (W&D)** that scales research width with parallel tool calls per turn, achieving 62.2% on BrowseComp with GPT-5-medium. The framework now also supports evaluating the MCPMark benchmark directly. The sobering finding still holds: even **GPT-5-High achieves only 44.16% success**, Grok-4 hits 33.33%, and Claude 4.1 Opus reaches 29.44%. Now at 272 commits — very active development.

**Accenture/mcp-bench** (475 stars, up from 401 — +18%) is now **published as a conference paper at ICLR 2026** — the first MCP benchmark accepted at a top machine learning conference. It connects LLMs to **28 representative live MCP servers** spanning **250 tools** across finance, travel, scientific computing, and academic search. Key finding from the paper: low-level capabilities like schema compliance and valid tool naming have converged (95%+ accuracy even for mid-scale models), but multi-server task coordination still degrades significantly for weaker models. GPT-5 leads the leaderboard at 0.749. 61 forks indicate active community engagement. Previously accepted at NeurIPS 2025 Workshop.

**eval-sys/MCPMark** (413 stars) *(new since last review)* is a comprehensive stress-testing MCP benchmark that evaluates agents across **5 real MCP services**: Notion, GitHub, Filesystem, Postgres, and Playwright. The standard benchmark contains **127 tasks** with an additional "easy" suite (50 tasks) designed for smaller open-source models and CI/CD integration. Key differentiators: one-command task execution, **isolated sandboxes** for safe evaluation, auto-resume for failures, unified metrics, and aggregated reports. Created July 2025, Apache-2.0 license. Where MCP-Bench tests against diverse servers, MCPMark goes deep on production-grade services that enterprise agents actually use.

**modelscope/MCPBench** (244 stars, up from 227 — +7%) continues to evaluate **MCP servers themselves** rather than the LLMs using them. The framework tests servers on task completion accuracy, latency, and token consumption under identical LLM and agent configurations. This isolates server quality from model quality. Supports three task types: Web Search (600 QA pairs from Frames, news, and tech domains), Database Query, and GAIA. Open-sourced April 2025 by Alibaba's ModelScope team.

**X-PLUG/OSWorld-MCP** (223 stars) *(new since last review)* is the **first comprehensive benchmark for computer-use agents' MCP tool invocation**, published at **ICLR 2026**. From Alibaba's X-PLUG team, it includes **158 validated MCP tools** spanning 7 common applications (VS Code, LibreOffice Calc/Writer/Impress, Chrome, VLC, OS utilities) plus 25 distractor tools for robustness testing. The benchmark covers **361 real-world tasks**: 250 tool-beneficial tasks where MCP tools substantially improve efficiency and 111 non-tool-beneficial tasks where no tool helps. 42% of tasks require challenging multi-round tool invocations. Key finding: MCP tools boost model accuracy (OpenAI o3: 8.3%→17.6%, Claude 4 Sonnet: 38.9%→45.0%), but even top models only invoke tools 33.3% of the time — agents struggle to decide *when* to use tools. Introduces two new metrics: Tool Invocation Rate (TIR) and Average Completion Steps (ACS). Public leaderboard at osworld-mcp.github.io.

## AI Security & Red-Teaming (2+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [promptfoo/evil-mcp-server](https://github.com/promptfoo/evil-mcp-server) | 25 | TypeScript | MIT | Multiple | Simulated attack vectors for MCP red-teaming |
| [promptfoo/mcp-agent-provider](https://github.com/promptfoo/mcp-agent-provider) | — | TypeScript | MIT | Provider | Test agent behavior with malicious MCP servers |

**promptfoo/evil-mcp-server** (25 stars) simulates malicious MCP behaviors for security testing and red-team exercises. It demonstrates real attack vectors: **tool poisoning** (hidden instructions in tool descriptions), **data exfiltration** (side-channel communication via simulated analytics), and **description injection** (disconnect between what users see and what AI models process). Runs in stdio or HTTP mode (port 3666). Now backed by OpenAI's acquisition of Promptfoo — MCP security testing has enterprise sponsorship. Published as an npm package (`@promptfoo/evil-mcp-server`).

**promptfoo/mcp-agent-provider** is the companion piece — a custom promptfoo provider that creates OpenAI-based ReAct agents to interact with MCP servers, allowing systematic testing of how agents handle malicious tool descriptions and poisoned responses. The new **MCP Plugin** in promptfoo specifically tests whether agentic systems using MCP are vulnerable to function call exploits, system prompt leakage, and unauthorized tool discovery. Together with evil-mcp-server, this provides a complete red-team testing pipeline for MCP deployments.

Both tools are explicitly for security awareness training and authorized testing — not for use with real customer data or production environments.

## Local LLM & API Benchmarking (2+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [MetriLLM/metrillm](https://github.com/MetriLLM/metrillm) | 4 | TypeScript | MIT | 4 | Local LLM speed, quality, and hardware fitness scoring |
| [Yoosu-L/llm-api-benchmark-mcp-server](https://github.com/Yoosu-L/llm-api-benchmark-mcp-server) | — | Go | — | Multiple | LLM API throughput, TTFT, concurrency testing |

**MetriLLM** (4 stars, now at v0.2.6 as of March 2026) is "Geekbench for local LLMs" — it benchmarks local models (via Ollama, LM Studio, etc.) measuring speed, quality, and hardware fitness. Quality evaluation spans 14 prompts across 6 categories: reasoning, coding, math, instruction following, structured output, and multilingual. Produces a global score (0-100) weighted 30% hardware fit and 70% quality. Results are shareable on a public leaderboard. As an MCP server, it exposes `list_models`, `run_benchmark`, `get_results`, and `share_result` tools. Now also offers CLI and IDE plugins. 136 commits — actively maintained.

**Yoosu-L/llm-api-benchmark-mcp-server** measures LLM API performance: generation throughput (tokens/sec), prompt throughput, and **Time To First Token (TTFT)** across configurable concurrency levels. Written in Go for performance. Supports both remote SSE and local stdio/SSE deployment. Outputs structured JSON with aggregated and distributed metrics. If you're evaluating LLM API providers for latency-sensitive applications, this provides the data.

## MCP Server Testing & Validation (3+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [lastmile-ai/mcp-eval](https://github.com/lastmile-ai/mcp-eval) | 21 | Python | Apache-2.0 | CLI | Lightweight eval framework with regression detection |
| [alpic-ai/mcp-eval](https://github.com/alpic-ai/mcp-eval) | 21 | TypeScript | — | CLI | MCP server performance evaluation with assistant configs |
| [r-huijts/mcp-server-tester](https://github.com/r-huijts/mcp-server-tester) | 10 | TypeScript | MIT | CLI | Claude AI-generated test cases for MCP servers |

**lastmile-ai/mcp-eval** (21 stars, up from 5 — **4x growth**) is built on top of mcp-agent and provides a lightweight framework for testing MCP servers end-to-end. Unlike mock-based testing, it exercises your complete system — an LLM/agent calling real MCP tools. Rich assertion types include content checks, tool verification, performance gates, and LLM judges. CI/CD-friendly with GitHub Actions support and JSON/HTML/Markdown reports. Now with OpenTelemetry-based metrics collection, decorator-based and pytest test organization patterns, and support for multiple LLM providers (Anthropic, OpenAI, Google). 163 commits — active development.

**alpic-ai/mcp-eval** (21 stars) *(new since last review)* evaluates MCP server performance through automated test suites. Supports both Anthropic/Claude and OpenAI/ChatGPT assistant configurations with configurable default tools per provider. TypeScript-based CLI with test suite management. Created September 2025.

**r-huijts/mcp-server-tester** (10 stars, up from ~0) uses Claude AI to auto-generate intelligent test cases for MCP servers. It validates protocol compliance, tests edge cases, and produces reports in console, JSON, HTML, and Markdown formats. 59 commits, MIT license, still under active development moving toward alpha.

## What's Missing

The gaps are narrowing — CI/CD integration and cost-awareness have improved — but important holes remain:

- **No unified benchmark leaderboard** — MCP-Bench, MCPBench, MCP-Universe, MCPMark, and OSWorld-MCP each publish results separately with different metrics and task sets; there's no aggregated view of which LLMs are best at MCP tool-use *(worse than March — more benchmarks means more fragmentation)*
- **No production prompt injection detection** — evil-mcp-server tests for vulnerabilities but there's no MCP server that monitors and blocks injection attempts in real-time (OpenAI's acquisition of Promptfoo may eventually address this)
- **CI/CD integration improving** — mcp-llm-eval now provides standalone CI/CD gates, and lastmile-ai/mcp-eval added OpenTelemetry, but most benchmarks still require manual setup *(partially closed)*
- **Cost-aware evaluation emerging** — MCP-Universe's MCP+ reduces token costs by 75%, but no tool yet optimizes *which metrics to run* based on budget *(partially closed)*
- **No cross-benchmark comparison** — results remain incomparable across different frameworks
- **No incremental evaluation** — all benchmarks run full suites; none support evaluating only changed tools or prompts
- **No iOS/mobile MCP evaluation** — OSWorld-MCP covers desktop applications but no benchmark tests MCP tool use on mobile platforms

## The Bottom Line

This is a **4.5/5** category, up from 4.0 in March. The ecosystem has crossed from "surprisingly mature" to **academically validated** — two ICLR 2026 papers (MCP-Bench, OSWorld-MCP) establish MCP benchmarking as a formal research discipline. OpenAI's acquisition of Promptfoo signals that LLM evaluation and red-teaming are now considered core infrastructure. DeepEval's community tripled. Five distinct benchmarking frameworks now cover different angles: tool-use (MCP-Bench), server quality (MCPBench), real-world domains (MCP-Universe), production services (MCPMark), and computer-use (OSWorld-MCP).

The standout insight from this category remains: **LLM tool-use is harder than it looks**. MCP-Universe's finding that even GPT-5-High only achieves 44.16% on real-world MCP tasks, and OSWorld-MCP's finding that top models only invoke available tools 33.3% of the time, should give pause to anyone assuming AI agents "just work" with tools. The problem isn't just *using* tools correctly — agents struggle to decide *when* to use them at all.

**Start here:** For prompt and agent evaluation, use [promptfoo](https://github.com/promptfoo/promptfoo) — it's the most complete tool with the largest community, now backed by OpenAI. For Pytest-style LLM unit testing, use [DeepEval](https://github.com/confident-ai/deepeval). For CI/CD eval gates, use [mcp-llm-eval](https://github.com/berkayildi/mcp-llm-eval). For benchmarking which LLM is best at tool-use, use [MCP-Bench](https://github.com/Accenture/mcp-bench) or [MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe). For stress-testing agents with production MCP services, use [MCPMark](https://github.com/eval-sys/mcpmark). For red-teaming MCP deployments, use promptfoo's [evil-mcp-server](https://github.com/promptfoo/evil-mcp-server).

This review was refreshed on 2026-04-28 using Claude Opus 4.6 (Anthropic). Initial review published 2026-03-16.

