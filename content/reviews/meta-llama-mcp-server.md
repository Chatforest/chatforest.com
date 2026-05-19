---
title: "Meta Llama MCP Servers — AI Agents for Llama 4, Ollama, and the Open-Weight LLM Ecosystem"
date: 2026-03-23T17:00:00+09:00
description: "Meta has no official MCP server and isn't an AAIF member, but Llama Stack includes MCP integration and a thriving community ecosystem connects Ollama and Llama models to MCP. Here's the honest review."
og_description: "Meta Llama MCP servers: no official server, not in AAIF, llama.cpp at 111K stars with active MCP WebUI development, Llama Stack rebranded to OGX (v1.0.2 stable). Rating: 3.5/5."
content_type: "Review"
card_description: "Meta built the most downloaded open-weight LLM family but has no official MCP server and isn't a member of the AAIF. llama.cpp (111K stars) has native MCP client support, and the formerly-Meta Llama Stack rebranded to OGX (v1.0.2 stable) as an independent, model-agnostic framework — enabling fully local, private AI agent workflows."
last_refreshed: 2026-05-19
---

**At a glance:** [OGX (formerly Llama Stack)](https://github.com/ogx-ai/ogx) (v1.0.2 stable, now an independent model-agnostic framework, MCP tool support via Responses API) + [llama.cpp](https://github.com/ggml-org/llama.cpp) (**111K stars**, native MCP client actively evolving with 8+ WebUI PRs since March 2026) + [ollama-mcp-bridge](https://github.com/patruff/ollama-mcp-bridge) (969 stars, TypeScript, MIT, confirmed stale). Meta is **not an AAIF member** at any tier (170+ organizations have joined, but not Meta), has **no official MCP server**, and has made no public announcement about MCP support. Their strategy: build their own agent ecosystem (Meta AI with 1 billion MAU, $2B Manus acquisition) rather than adopt Anthropic's protocol. The community fills the gap — **llama.cpp has native MCP client support with an agentic loop actively improving**, and Ollama bridges let local Llama models participate in the MCP ecosystem. Part of our **[AI Providers MCP category](/categories/ai-providers/)**.

Meta Llama MCP servers let AI agents **run inference on Llama 4 Scout/Maverick, manage local Ollama models, generate embeddings, and use MCP tools through locally-hosted LLMs** — all without sending data to cloud APIs. This enables **fully private, zero-cost AI agent workflows** for users willing to provide the hardware.

[Meta Platforms](https://ai.meta.com/) was founded in 2004 (as Facebook) by **Mark Zuckerberg**. As of April 2026: **$201 billion annual revenue** (FY2025, 22% YoY growth; Q1 2026 guidance $53.5–56.5B), **~$1.59 trillion market cap**, **78,865+ employees**, and **1 billion monthly active Meta AI users** across WhatsApp, Messenger, Instagram, Facebook, and the standalone Meta AI app. Llama has surpassed **1.2 billion cumulative downloads** (averaging 1 million downloads/day since February 2023), with thousands of derivative models. In December 2025, Meta acquired **Manus** (Singapore-based AI agent startup) for **$2 billion**. Meta is planning **$135 billion in AI capex** for 2026.

**Architecture note:** Meta's MCP approach is fundamentally different from every other AI provider we've reviewed. Google, OpenAI, and Anthropic all participate in MCP governance (AAIF members or creators). Meta does not. Instead, Meta invested in **Llama Stack** — their own agent framework that happens to include MCP tool support as one feature among many. The community ecosystem focuses on **Ollama** — the most popular way to run Llama models locally — with bridges that let local LLMs connect to and consume MCP servers.

## What It Does

The Llama/Ollama MCP ecosystem provides capabilities in two directions: **servers** that expose Llama/Ollama to MCP clients, and **bridges** that let local Llama models act as MCP clients consuming external tools.

### Ollama Model Management (via MCP servers)

| Capability | What It Does |
|------------|-------------|
| List models | Browse locally installed Ollama models |
| Pull/push models | Download models from or upload to Ollama registries |
| Show model info | View model parameters, templates, and metadata |
| Copy/delete models | Manage local model library |
| Process status | Check running models and resource usage |

### Local LLM Inference (via MCP servers)

| Capability | What It Does |
|------------|-------------|
| Text generation | Run inference on any locally-hosted Llama model |
| Chat completions | Multi-turn conversations via local models |
| Embeddings | Generate vector embeddings locally |
| Model selection | Route queries to specific local models by name |

### MCP Tool Consumption (via bridges)

| Capability | What It Does |
|------------|-------------|
| Connect to MCP servers | Local Llama models can call external MCP tools |
| Multi-server support | Connect to multiple MCP servers simultaneously |
| Tool detection | Automatic discovery and registration of available MCP tools |
| Structured output | Validate tool call arguments from local model output |

### Llama Stack MCP Integration

| Capability | What It Does |
|------------|-------------|
| Inline tools | Define tools directly in Llama Stack agent config |
| Local MCP tools | Connect to stdio-based MCP servers |
| Remote MCP tools | Connect to SSE-based remote MCP servers |
| Toolgroup registration | Register MCP servers as named toolgroups for agents |

### What's Not Commonly Available

**The local-first nature of the ecosystem creates inherent gaps:**

- **Image generation** — Llama 4 is multimodal (input), but no MCP server exposes local image generation
- **Audio/video** — no local Llama MCP server provides speech or video capabilities
- **Fine-tuning management** — no MCP server manages Llama fine-tuning workflows
- **Cloud-quality reasoning** — local quantized models produce lower quality output than cloud APIs for complex tasks
- **Reliable tool calling** — smaller models (7B-13B) have significantly worse tool-calling accuracy than cloud models

## Meta's Agent Strategy (Not MCP)

Unlike Google, OpenAI, and Anthropic — who actively participate in MCP governance — Meta is building **its own agent infrastructure**:

### Meta AI Assistant
- **1 billion monthly active users** (reached May 2025)
- Available across WhatsApp, Messenger, Instagram, Facebook, meta.ai, standalone app
- Standalone Meta AI app launched April 2025
- Powered by Llama models

### Manus Acquisition ($2B, December 2025)
- Singapore-based AI agent startup
- $100M+ annualized revenue within 8 months of launch
- Desktop app launched March 2026
- Being integrated into Meta AI products

### Llama 4 Behemoth — Delayed
- 288B active parameters / ~2T total (teacher model for Scout and Maverick)
- Originally planned for "early summer 2025," pushed to fall 2025 or later
- **Still not released as of April 2026** — Meta reportedly struggling to improve capabilities enough to justify launch
- Currently used internally as a distillation teacher for smaller models

### AAIF Status: Still Not a Member (April 2026)
Meta remains absent from the [AAIF](https://aaif.io/) (Agentic AI Foundation, Linux Foundation), which has grown to **170+ member organizations** in under four months. Platinum members include AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, and OpenAI. Gold members now include Cisco, Datadog, Docker, IBM, JetBrains, Oracle, Salesforce, SAP, Shopify, and Snowflake. Even Hugging Face joined at the Silver tier. Meta's absence is increasingly conspicuous as the foundation approaches universal industry coverage.

## llama.cpp — Native MCP Client Support (March 2026, Actively Evolving)

**The most significant development in this ecosystem.** On March 6, 2026, [llama.cpp](https://github.com/ggml-org/llama.cpp) merged [PR #18655](https://github.com/ggml-org/llama.cpp/pull/18655) — a massive 15,285-line, 374-commit pull request adding full MCP client support to llama-server's WebUI.

This means **anyone running any GGUF model locally** (Llama, Mistral, Qwen, Gemma, or any other) now has native MCP support with:

| Feature | Description |
|---------|-------------|
| MCP server management | Server selector, settings cards, capability display |
| Agentic loop | Models call tools, process results, and iterate automatically |
| MCP Prompts | Picker UI, argument forms, prompt attachments |
| MCP Resources | File browser, search, tree view, resource previews |
| CORS proxy | Backend proxy enabled with `--webui-mcp-proxy` flag |
| Processing stats | UI for tracking agentic loop performance |

**Update (May 2026):** The MCP WebUI has received **8+ additional PRs since March**, all from contributor `allozaur`: MCP Diagnostics improvements (Apr 13), "Server tools" WebUI integration (Apr 28), MCP information logic and UI refinements (May 6), import/export of MCP settings config (May 8), fix for MCP resource template parameters (May 16), request timeout for MCP tool calls (May 16), MCP service refactoring (May 18). The MCP implementation is clearly in active development, not a one-shot contribution.

**Why this matters:** llama.cpp is the dominant local inference engine — now at **111,000 stars** (up from 74K at the time of the March merge, a 50% jump). Adding native MCP support means local models can browse files, query databases, call APIs, and execute multi-step agentic workflows — the same pattern that makes Claude Code and Cursor's agent mode useful. This largely eliminates the need for separate "bridge" projects for users running llama-server directly.

## Community Implementations

### patruff/ollama-mcp-bridge — Local LLM ↔ MCP Bridge

- **GitHub:** [patruff/ollama-mcp-bridge](https://github.com/patruff/ollama-mcp-bridge) — 969 stars, 113 forks
- **Language:** TypeScript
- **License:** MIT

The most popular TypeScript bridge in the Ollama MCP space. Bridges Ollama-hosted models with MCP servers, enabling local LLMs to discover and use MCP tools. Supports multi-MCP server connections and structured output validation.

**Key limitation:** Last code push April 2025 — now a full year stale. With llama.cpp's native MCP support merged (March 2026), this project's value proposition is diminishing for users who can run llama-server directly. Structured output from smaller models remains unreliable for complex tool schemas.

### jonigl/mcp-client-for-ollama — TUI Client

- **GitHub:** [jonigl/mcp-client-for-ollama](https://github.com/jonigl/mcp-client-for-ollama) — 533 stars, 85 forks
- **Language:** Python
- **License:** MIT

Terminal UI client for MCP servers via Ollama. Features agent mode, multi-server support, model switching, streaming responses, human-in-the-loop confirmation, and thinking mode. Installable via pip (`ollmcp`).

**Key limitation:** Most actively maintained of the Ollama MCP projects (pushed March 2026). Stars slightly declining — may be losing users to llama.cpp's native MCP WebUI.

### jonigl/ollama-mcp-bridge — Drop-in API Proxy (NEW)

- **GitHub:** [jonigl/ollama-mcp-bridge](https://github.com/jonigl/ollama-mcp-bridge)
- **Language:** Python
- **License:** MIT

A newer, lightweight drop-in proxy that transparently adds every MCP server tool to Ollama chat completions API. Fully compatible with the Ollama API, so existing applications get MCP tool access without code changes. Releases up to v0.11.2 (March 2026).

**Key limitation:** Requires Ollama running separately (unlike llama.cpp's all-in-one approach).

### rawveg/ollama-mcp — Ollama SDK as MCP Server

- **GitHub:** [rawveg/ollama-mcp](https://github.com/rawveg/ollama-mcp) — 146 stars, 25 forks
- **Language:** TypeScript
- **License:** AGPL-3.0

Exposes the complete Ollama SDK as an MCP server with **14 tools** covering model management (list, show, pull, push, copy, delete, create), operations (process status, text generation, chat, embeddings), and web tools. 96%+ test coverage. Zero dependencies. Install via `npx -y ollama-mcp`.

**Key limitation:** AGPL-3.0 license may restrict commercial use. Last push November 2025.

### run-llama/mcp-server-llamacloud — LlamaCloud Index Access

- **GitHub:** [run-llama/mcp-server-llamacloud](https://github.com/run-llama/mcp-server-llamacloud) — 86 stars, 19 forks
- **Language:** JavaScript
- **License:** MIT

MCP server connecting to managed indexes on LlamaCloud (by the LlamaIndex team). Not a Llama model server per se, but part of the broader Llama-branded ecosystem.

**Key limitation:** Requires LlamaCloud account (cloud service, not local). Different from Meta's Llama — this is LlamaIndex's cloud product.

### sammcj/mcp-llm — Multi-Provider Local LLM

- **GitHub:** [sammcj/mcp-llm](https://github.com/sammcj/mcp-llm) — 77 stars, 14 forks
- **Language:** JavaScript
- **License:** MIT

MCP server providing LLM access to other LLMs — supports Ollama, Llama, OpenAI, Anthropic, and AWS Bedrock. Useful for cross-model workflows where a cloud-hosted agent needs a "second opinion" from a local model.

**Key limitation:** Multi-provider scope means Llama-specific features are thin.

### BeehiveInnovations/pal-mcp-server — Multi-Provider Agent (Renamed from zen-mcp-server)

- **GitHub:** [BeehiveInnovations/pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server) — **11,500 stars**, 965 forks
- **Language:** Python

The most-starred project in this space (renamed from `zen-mcp-server` to **PAL MCP** — Provider Abstraction Layer). Still a general multi-provider MCP server: supports Claude Code, Gemini CLI, and Codex CLI as orchestrators, with multi-model collaboration across Gemini, OpenAI, Anthropic, Grok, Azure, and Ollama. Ollama support means local Llama models can be used as one provider among many. Modest star growth (+200 since April review).

**Key limitation:** Not Llama-specific — Ollama/Llama is one option among many providers. The rename away from "zen" to "PAL" suggests evolving brand identity, not a change in functionality.

## OGX (Formerly Llama Stack) as MCP Platform

**[OGX](https://github.com/ogx-ai/ogx)** (formerly Llama Stack, formerly at meta-llama/llama-stack) has undergone a significant transformation since the April 2026 review. The project **rebranded as OGX (Open GenAI Stack)** and moved to an independent organization `ogx-ai/ogx`. The new mission: *"model-agnostic, multi-SDK, production-grade."*

**Release history since v0.7.1 (April 8, 2026):**
- **v0.8.0** (May 1): Native Anthropic Messages API support, Gemini integration, OpenAI API conformance up to 91.2%, SSTI prevention fix (Jinja2 sandboxing in RAG query generator), Tornado security patch (GHSA-qjxf-f2mg-c6mc)
- **v1.0.0** (May 12): First stable release — multi-tenancy core for MaaS, gateway-first architecture, Safety API removed in favor of moderation endpoints, **Claude Code compatibility** added
- **v1.0.1** (May 13): Async safety fixes, SQLStore/MongoDB expiration enforcement
- **v1.0.2** (May 14): SQL engine reset fixes, UI lockfile update

**Current capabilities (unchanged):**
- **Responses API** — server-side agentic orchestration with tool calling, MCP server integration, and built-in file search (RAG) in a single API call
- Supports **inline tools, local MCP tools, and remote MCP tools**
- MCP servers registered via toolgroup registration
- Client SDKs in Python, TypeScript, Swift, and Kotlin
- Drop-in replacement for the OpenAI API — runs anywhere (laptop, datacenter, cloud)
- Now also supports Claude/Anthropic and Gemini APIs natively

**What the rebrand means for this review:** OGX is no longer Meta's framework — it's an independent, vendor-agnostic project that happens to work well with Llama models. This weakens the narrative of "Meta's agent framework includes MCP support." On the positive side, v1.0.0 stable release signals production readiness, and the model-agnostic pivot could actually accelerate MCP adoption within the project.

**Known OGX/Llama Stack MCP issues (some may have been addressed in v1.0.x):**
- Issue #2542: Upgrade to Streamable HTTP protocol (SSE deprecated in MCP spec)
- Issue #4452: Responses request calls MCP list tools multiple times
- Issue #2584: "Llama API not working with Tool Calling"

## Hardware Requirements

Running Llama models locally requires significant hardware — the key tradeoff for "free" inference:

| Model | VRAM (Q4_K_M) | GPU Example | Quality |
|-------|---------------|-------------|---------|
| Llama 3.2 1B | ~1-2 GB | Any modern GPU | Basic tasks only |
| Llama 3.2 3B | ~2-3 GB | GTX 1060+ | Simple conversations |
| Llama 3 8B | ~6-7 GB | RTX 4060 | Good general use |
| Llama 3.3 70B | ~40+ GB | Multi-GPU / A100 | Near-cloud quality |
| Llama 4 Scout (109B) | ~60 GB | Single H100 (Int4) | Beats Gemini Flash-Lite |
| Llama 4 Maverick (400B) | ~200+ GB | H100 host | Beats GPT-4o |

**Q4_K_M quantization** is the community standard for consumer hardware — halves VRAM requirements vs FP16 with modest quality loss.

## Llama Model Pricing

| Model | Cost | License | Context Window |
|-------|------|---------|----------------|
| Llama 3 (8B, 70B) | **Free** | Meta Community License | 2K |
| Llama 3.1 (8B, 70B, 405B) | **Free** | Meta Community License | 128K |
| Llama 3.2 (1B, 3B, 11B, 90B) | **Free** | Meta Community License | 128K |
| Llama 3.3 (70B) | **Free** | Meta Community License | 128K |
| Llama 4 Scout (17B active / 109B total) | **Free** | Meta Community License | 10M |
| Llama 4 Maverick (17B active / 400B total) | **Free** | Meta Community License | 1M |
| Llama 4 Behemoth (288B active / ~2T total) | **Free** (delayed, not released) | Meta Community License | TBD |

**Important licensing note:** Llama uses the **Meta Llama Community License**, not a standard open-source license. Companies with **700+ million monthly active users** must request a separate commercial license from Meta. The Open Source Initiative does not consider this "open source." Using model outputs to train other models is allowed (since Llama 3.1) with attribution.

**Cloud API access** (for those who don't want to run locally): Llama models are available through AWS Bedrock, Azure AI, Google Cloud Vertex AI, Together AI, Fireworks AI, Groq, and others — typically at significantly lower prices than proprietary models.

## AI Provider MCP Comparison

| Provider | Official MCP Server | AAIF Role | MCP Client Support | Top Community Server |
|----------|-------------------|-----------|--------------------|--------------------|
| **Anthropic** | Reference servers (85.9k stars) | Created MCP, Platinum | Claude.ai, Desktop, Code, API | N/A (they are the reference) |
| **Google** | 24+ managed + open-source | Platinum | Gemini CLI | jamubc/gemini-mcp-tool |
| **OpenAI** | None | Platinum, Steering Committee | ChatGPT, Agents SDK, Codex CLI | lastmile-ai |
| **Meta** | **None** | **Not a member** | **None** | ollama-mcp-bridge (969, stale) |

## Known Issues

1. **No official MCP server** — Meta has made no public announcement about MCP support. Their agent strategy centers on Meta AI (1B MAU) and the Manus acquisition ($2B), not the MCP ecosystem. Developers must rely entirely on community implementations.

2. **Not an AAIF member** — Meta is the only major AI company absent from the AAIF at every tier. This means no voice in MCP protocol governance, no commitment to maintaining compatibility, and no signal to the community that Llama and MCP will converge.

3. **Tool calling reliability** — Smaller quantized Llama models (7B-13B) have significantly worse tool-calling accuracy than cloud APIs. MCP tool use requires structured JSON output that local models often produce incorrectly, leading to failed tool invocations and broken agent loops.

4. **Hardware barrier** — "Free" Llama inference requires substantial GPU investment. The 8B model needs ~7 GB VRAM (a $300+ GPU), while the 70B model needs 40+ GB (a $1,500+ GPU or multi-GPU setup). Llama 4 Scout requires an H100-class GPU.

5. **OGX/Llama Stack MCP bugs** — Active issues (#4452, #2542, #2584) report redundant MCP tool listing, deprecated SSE transport, and unreliable tool calling. The framework reached v1.0.2 stable but issue status post-rebrand is unclear — monitoring continues.

6. **Licensing ambiguity** — The Meta Llama Community License restricts use by companies with 700M+ MAU and is not OSI-approved open source. Commercial users at scale need separate licensing, creating uncertainty for enterprise MCP deployments.

7. **Community bridge projects losing relevance** — The most popular bridge (ollama-mcp-bridge, 969 stars) was last updated April 2025 — now a full year stale. With llama.cpp merging native MCP support (March 2026), many bridge projects are becoming redundant for users who can run llama-server directly. The ecosystem is consolidating around llama.cpp for direct use and Ollama API proxies for existing Ollama setups.

8. **Quality vs cloud APIs** — Even the best local Llama models (70B quantized) produce noticeably lower quality output than GPT-4o, Claude, or Gemini for complex reasoning tasks. The cost savings of local inference come with measurable quality tradeoffs.

9. **No MCP client support from Meta products** — Meta AI (1B MAU across WhatsApp, Messenger, Instagram) has no MCP client support. Unlike ChatGPT (MCP client in Desktop), Claude (MCP in Desktop/Code/API), or Gemini (MCP in CLI), Meta's consumer products don't connect to MCP servers.

10. **Multimodal gaps** — Llama 4 is natively multimodal (text + image input), but no MCP server exposes multimodal inference. Audio, video, and image generation capabilities are absent from the entire Llama MCP ecosystem.

## Bottom Line

**Rating: 3.5 out of 5** *(held — llama.cpp MCP is maturing well, but Llama Stack's rebrand to independent OGX weakens the Meta ecosystem narrative)*

Meta's Llama MCP story has two distinct threads running in parallel — and they're moving in opposite directions. **llama.cpp** is thriving: 111K stars (+50% since March), with 8+ additional MCP WebUI PRs showing sustained development momentum. Any GGUF model can now participate in the MCP ecosystem with an actively-improving native client — no bridges needed.

**The OGX rebrand is the headline change this cycle.** Llama Stack reached v1.0.0 stable (May 12) and is now model-agnostic — it works with Anthropic, Gemini, OpenAI, and others alongside Llama. The framework is more capable than ever. But it's no longer Meta's framework. The rebrand to `ogx-ai/ogx` with a "model-agnostic" mission means the review's "Llama Stack is Meta's agent framework with MCP support" narrative now needs an asterisk. Meta handed off ownership; the independent project is doing fine, but it's a subtle retreat from Meta's direct ecosystem investment.

**What's unchanged:** No official Meta MCP server, no AAIF membership (still the only major AI company absent), no MCP client support in Meta AI consumer products (WhatsApp, Messenger, Instagram), Llama 4 Behemoth still unreleased, tool-calling reliability issues in smaller local models.

**New this cycle:** Meta launched official Llama API client libraries (`llama-api-python`, `llama-api-typescript` — generated via Stainless) for the hosted Llama API at llama.developer.meta.com. These are REST API clients, not MCP-related, but signal Meta is investing in developer tooling for Llama model access.

Rating held at 3.5/5. The llama.cpp MCP trajectory justifies the March upgrade and the momentum continues. The OGX rebrand is a net neutral-to-negative for this specific review — it's good for the open-source ecosystem broadly, but weakens the "Meta is investing in its agent stack" framing. No change to the known gaps.

**Who should use Llama MCP servers:**

- **Privacy-focused users** who need AI agent workflows that never leave their machine
- **Cost-sensitive developers** running high-volume inference where cloud API costs are prohibitive
- **Llama Stack users** who want MCP tool access within Meta's agent framework
- **Experimenters** who enjoy running local models and don't need cloud-quality reasoning

**Who should wait:**

- **Anyone needing reliable tool calling** — smaller local models frequently produce malformed tool invocations
- **Users without GPU hardware** — meaningful local inference requires $300+ in GPU investment
- **Production teams** — no official support, fragmented community, active bugs in Llama Stack MCP
- **Enterprise users** — licensing ambiguity and lack of AAIF membership create compliance uncertainty

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official Meta announcements. Information is current as of May 2026. See our [About page](/about/) for details on our review process.*
