---
title: "OpenAI MCP Servers — AI Agents for GPT-4o, o3, DALL-E, and the OpenAI API Platform"
date: 2026-03-23T23:45:00+09:00
description: "OpenAI adopted MCP as a client (ChatGPT, Agents SDK, Responses API) but has no official MCP server wrapping their API. Community servers let AI agents access GPT models, image generation, and web search. Here's the honest review."
og_description: "OpenAI MCP servers: strong client-side adoption but no official server. Community fills the gap with chat completions, image generation, and multi-agent orchestration. Rating: 3.5/5."
content_type: "Review"
card_description: "OpenAI embraced MCP in March 2025, joining the steering committee and adding MCP client support to ChatGPT Desktop, the Responses API, and Agents SDK. But OpenAI has no official MCP server exposing their API — community implementations provide chat completions, image generation, and web search access for other AI agents."
last_refreshed: 2026-03-23
---

**At a glance:** [lastmile-ai/openai-agents-mcp](https://github.com/lastmile-ai/openai-agents-mcp) (197 stars, active, MIT) + [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) (79 stars, active, MIT). OpenAI has 900+ million weekly ChatGPT users, a **$730 billion valuation**, and joined the MCP steering committee in March 2025 — but publishes **no official MCP server** wrapping their API. Their focus is on the client side: ChatGPT, Agents SDK, and the Responses API all connect TO MCP servers.

OpenAI MCP servers let AI agents **query GPT-4o/GPT-4.1/o3/GPT-5, generate images with DALL-E and gpt-image-1, search the web, and orchestrate multi-agent workflows** — all through natural language prompts in Claude, Cursor, or other MCP-compatible clients. This enables cross-model collaboration: a Claude agent calling GPT-4o for a second opinion, or using DALL-E for image generation without leaving the MCP workflow.

[OpenAI](https://openai.com/) was founded in December 2015 by **Sam Altman**, **Elon Musk**, **Ilya Sutskever**, **Greg Brockman**, and others as a nonprofit research lab. The company transitioned to a capped-profit structure in 2019 and is moving to a public benefit corporation. As of early 2026: **~$13 billion annualized revenue** (hitting $1B/month in July 2025, projecting $20B+ for full year), **$730 billion pre-money valuation** (February 2026 round, $110B raised), **20+ million ChatGPT paid subscribers**, **900+ million weekly active ChatGPT users**, and approximately **3,500-4,500 employees**. Key products include ChatGPT, GPT-4o, GPT-4.1, GPT-5, o1/o3/o4-mini reasoning models, DALL-E 3/gpt-image-1, Whisper, Sora 2, and the Agents SDK.

**Architecture note:** OpenAI's MCP strategy is fundamentally different from Google, Dropbox, or Microsoft: they are primarily an **MCP client**, not a server provider. The Responses API, Agents SDK (Python + TypeScript), ChatGPT Desktop, and Codex CLI all connect TO external MCP servers. Community MCP servers fill the reverse gap — exposing OpenAI's API so that other AI agents (Claude, Gemini, etc.) can call OpenAI models via MCP.

## What It Does

Community OpenAI MCP servers expose these capability areas:

### Chat Completions

| Capability | What It Does |
|------------|-------------|
| Query GPT models | Send prompts to GPT-4o, GPT-4.1, GPT-5, GPT-4.1-mini/nano |
| Query reasoning models | Use o1, o3, o4-mini for step-by-step reasoning tasks |
| Multi-turn conversations | Maintain conversation context across multiple exchanges |
| Model selection | Choose the appropriate model for cost/capability tradeoffs |
| Temperature/parameter control | Adjust creativity, token limits, and response format |

### Image Generation

| Capability | What It Does |
|------------|-------------|
| Generate images | Create images from text prompts via DALL-E 3 or gpt-image-1 |
| List models | Browse available models and their capabilities |

### Web Search

| Capability | What It Does |
|------------|-------------|
| Search the web | Query the internet through OpenAI's web search tool |
| Grounded responses | Get answers with web-sourced citations |

### Multi-Agent Orchestration

| Capability | What It Does |
|------------|-------------|
| File search | Search across uploaded documents via OpenAI vector stores |
| Computer action | Interact with web interfaces through OpenAI's computer use |
| Agent orchestration | Coordinate multiple specialized OpenAI agents |

### What's Not Commonly Exposed

**Most community servers focus on chat completions only.** These capabilities are available through OpenAI's API but not exposed by existing MCP servers:

- **Text-to-speech (TTS)** — no MCP server wraps OpenAI's voice generation
- **Speech-to-text (Whisper)** — no MCP server provides transcription
- **Embeddings** — no MCP server generates vector embeddings
- **Fine-tuning management** — no MCP server manages model fine-tuning
- **Moderation API** — no MCP server wraps content moderation
- **Sora video generation** — no MCP server provides text-to-video

## OpenAI as MCP Client

OpenAI's primary MCP contribution is on the **client side** — making their products consume MCP servers rather than providing one:

### ChatGPT Desktop/Web (Developer Mode)

- Enable via Settings > Apps & Connectors > Developer Mode
- Connect to remote MCP servers over HTTPS
- Supports read AND write actions (update Jira, trigger workflows, query databases)
- **Requires ChatGPT Plus ($20/mo) or Pro subscription**
- Beta feature as of early 2026

### Responses API

- Native MCP client support for remote servers
- Supports Streamable HTTP and HTTP/SSE transports
- No extra cost for MCP tool calls — just normal token billing
- Can connect to any standards-compliant MCP server (Stripe, Shopify, Twilio, etc.)

### Agents SDK (Python + TypeScript)

- `MCPServerStdio` — connect to local stdio-based MCP servers
- `MCPServerSse` — connect to SSE-based servers (legacy)
- `MCPServerStreamableHttp` — connect to Streamable HTTP servers (preferred)
- `HostedMCPTool` — pushes tool round-trip to OpenAI infrastructure
- Automatic tool discovery, format conversion, caching, and tracing

### Codex CLI

- Supports connecting to MCP servers via `~/.codex/config.toml`
- Can also BE an MCP server itself, exposing `codex()` and `codex-reply()` tools

## Community Implementations

### lastmile-ai/openai-agents-mcp — Agents SDK Extension

- **GitHub:** [lastmile-ai/openai-agents-mcp](https://github.com/lastmile-ai/openai-agents-mcp) — 197 stars, 21 forks, 63 commits, 4 releases
- **Language:** Python
- **License:** MIT

Extends the OpenAI Agents SDK with MCP **server** support — letting other AI agents call OpenAI agents via MCP. The most popular OpenAI MCP server project, bridging OpenAI's agent framework with the broader MCP ecosystem.

**Key limitation:** Focused on the Agents SDK framework rather than raw API access. Requires understanding of OpenAI's agent architecture.

### pierrebrunelle/mcp-server-openai — Cross-Model Queries

- **GitHub:** [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) — 79 stars, 22 forks
- **Language:** Python
- **License:** MIT

Purpose-built to let Claude (or other AI agents) query OpenAI models via MCP. Simple, focused implementation with a single `ask_openai` tool.

**Key limitation:** Single-turn only in the basic configuration. Limited to chat completions — no image generation or web search.

### arthurcolle/openai-mcp — Multi-Provider LLM

- **GitHub:** [arthurcolle/openai-mcp](https://github.com/arthurcolle/openai-mcp) — 35 stars, 15 forks, 7 commits
- **Language:** Python
- **License:** MIT

Multi-provider LLM access through MCP — not limited to OpenAI. Supports routing queries to different providers based on task requirements.

**Key limitation:** Only 7 commits suggests limited maintenance. Multi-provider scope means OpenAI-specific features may be thin.

### billster45/mcp-chatgpt-responses — Responses API

- **GitHub:** [billster45/mcp-chatgpt-responses](https://github.com/billster45/mcp-chatgpt-responses) — 16 stars, 12 forks
- **Language:** Python
- **License:** MIT

Uses OpenAI's Responses API for multi-turn conversations with web search capability. Maintains conversation context across calls.

**Key limitation:** Tightly coupled to the Responses API — not a general chat completions wrapper.

### lroolle/openai-agents-mcp-server — Multi-Agent Orchestration

- **GitHub:** [lroolle/openai-agents-mcp-server](https://github.com/lroolle/openai-agents-mcp-server) — 10 stars, 4 forks
- **Language:** Python
- **License:** MIT

Exposes specialized OpenAI agents (Web Search, File Search, Computer Action, Orchestrator) as MCP tools. The most feature-rich implementation for agentic workflows.

**Key limitation:** Small community. Depends on OpenAI's agent infrastructure which is rapidly evolving.

### akiojin/openai-mcp-server — Image Generation + Model Listing

- **GitHub:** [akiojin/openai-mcp-server](https://github.com/akiojin/openai-mcp-server) — 1 star, 0 forks, 109 commits, 8 releases
- **Language:** JavaScript/TypeScript
- **License:** MIT

The most actively developed implementation by commit count. Supports chat completions, model listing, and **image generation** via gpt-image-1 — a capability most other servers lack.

**Key limitation:** Only 1 star despite 109 commits — low community adoption. Also available as npm package `@fadeaway-ai/openai-mcp-server`.

## Authentication

All OpenAI MCP servers use **API key authentication** — straightforward but with important security considerations:

| Method | Complexity | Security |
|--------|-----------|----------|
| API key via environment variable | **Low** — generate at platform.openai.com | Standard |
| Project-scoped API key | **Low** — scoped to specific project | Better — limits blast radius |
| Organization-level key | **Low** — scoped to org | Enterprise |

**Best practices:**
- Use **project-scoped API keys** to limit permissions to specific endpoints
- Store keys in environment variables, never hardcoded
- Use different keys for different MCP server instances
- Set spending limits in the OpenAI dashboard to prevent runaway costs
- Rotate keys periodically

**Compared to other ecosystems:** OpenAI's API key auth is simpler than Google OAuth 2.0, Dropbox OAuth, or Azure Entra ID — but offers less granular permission control. There's no concept of "read-only" or "chat-only" API keys (though project-scoped keys help).

## OpenAI API Pricing

| Model | Input (per 1M tokens) | Cached Input | Output (per 1M tokens) | Context Window |
|-------|----------------------|--------------|----------------------|----------------|
| GPT-4.1 Nano | $0.10 | $0.025 | $0.40 | 1M |
| GPT-4o-mini | $0.15 | $0.075 | $0.60 | 128K |
| GPT-4.1 Mini | $0.40 | $0.10 | $1.60 | 1M |
| o4-mini | $1.10 | $0.275 | $4.40 | 200K |
| GPT-4.1 | $2.00 | $0.50 | $8.00 | 1M |
| o3 | $2.00 | $0.50 | $8.00 | 200K |
| GPT-4o | $2.50 | $1.25 | $10.00 | 128K |
| o1 | $15.00 | $7.50 | $60.00 | 200K |

| Other Services | Pricing |
|----------------|---------|
| DALL-E 3 | $0.04-$0.12 per image |
| Whisper (speech-to-text) | $0.006/minute |
| TTS | $15.00/1M characters |
| text-embedding-3-small | $0.02/1M tokens |
| text-embedding-3-large | $0.13/1M tokens |
| Web search tool | $10-$25/1K calls |
| Batch API | 50% discount on all models |

**ChatGPT subscriptions:**
- ChatGPT Free — limited access
- ChatGPT Plus — $20/month (required for MCP client support in ChatGPT)
- ChatGPT Pro — $200/month (unlimited access to all models)

**Note:** Using OpenAI through MCP servers incurs standard API costs. There's no MCP-specific pricing — you pay the same per-token rates as direct API usage. Reasoning models (o1, o3) generate "reasoning tokens" billed as output but not visible in responses, which can cause unexpectedly high costs.

## Known Issues

1. **No official MCP server** — OpenAI has invested heavily in MCP client support but publishes no official server exposing their API via MCP. Developers must rely on community implementations of varying quality.

2. **Cost management risk** — MCP enables automated agent loops that can make hundreds of API calls. Reasoning models (o1: $60/M output tokens) can generate large bills quickly. No community MCP server includes built-in spending controls or cost tracking.

3. **API key security** — Simple API key auth means anyone with the key gets full access to all enabled endpoints. No fine-grained permission scoping (e.g., "chat only, no image generation"). Keys stored in MCP config files must be carefully protected.

4. **Rate limiting** — OpenAI imposes separate limits for requests/minute and tokens/minute by API tier. Community MCP servers rarely implement rate limit handling — 429 errors pass through to the calling agent with no backoff logic.

5. **Model deprecation churn** — OpenAI frequently introduces and deprecates models (GPT-4 Turbo → GPT-4o → GPT-4.1). Community MCP servers may reference deprecated models. The model parameter needs regular updating.

6. **Small community servers** — Outside lastmile-ai (197 stars), community implementations have modest adoption. Most have <20 stars and limited maintenance. The ecosystem is fragmented across many small projects.

7. **Reasoning token opacity** — o1, o3, and o4-mini models use "reasoning tokens" that are billed as output but not returned in responses. An MCP call to o3 may cost significantly more than expected because the visible output is only a fraction of the generated tokens.

8. **SSE transport deprecation** — OpenAI recommends Streamable HTTP over SSE for MCP transport. Some community servers still use the deprecated SSE transport, which may stop working in future MCP spec versions.

9. **ChatGPT MCP client requires paid plan** — Using ChatGPT as an MCP client requires ChatGPT Plus ($20/mo) or Pro ($200/mo) and enabling Developer Mode. Free users cannot connect to MCP servers.

10. **No audio/video capabilities via MCP** — Despite OpenAI offering Whisper (speech-to-text), TTS (text-to-speech), and Sora 2 (video generation), no community MCP server exposes these capabilities. The ecosystem is heavily biased toward text-only interactions.

## Bottom Line

**Rating: 3.5 out of 5**

OpenAI's MCP story is split in two. On the **client side**, it's excellent: ChatGPT Desktop, the Responses API, Agents SDK, and Codex CLI all provide first-class MCP client support, letting OpenAI's products connect to the growing universe of MCP servers. OpenAI joined the MCP steering committee, partnered with Anthropic on the MCP Apps Extension, and has made MCP a core part of their agent infrastructure.

On the **server side** — exposing OpenAI's own capabilities via MCP — the ecosystem is community-driven and fragmented. **lastmile-ai/openai-agents-mcp** (197 stars, 63 commits) is the strongest project, extending the Agents SDK with MCP server support. **pierrebrunelle/mcp-server-openai** (79 stars) is the most straightforward for cross-model queries. **akiojin/openai-mcp-server** (109 commits, 8 releases) is the most actively maintained with unique image generation support.

The 3.5/5 rating reflects strong client-side MCP adoption and a functional but fragmented server ecosystem. OpenAI's API is powerful and well-documented, making community MCP servers relatively straightforward to build. But the lack of an official server means no single implementation covers the full API surface — chat completions are well-served, while audio, video, embeddings, and fine-tuning remain inaccessible via MCP.

**Who should use OpenAI MCP servers:**

- **Claude or Gemini users** who want to query GPT models or generate images without leaving their MCP workflow
- **Multi-model architects** who need cross-provider AI capabilities in a single agent pipeline
- **Developers** building agentic workflows that combine OpenAI's models with other MCP-connected services

**Who should wait:**

- **Anyone needing audio/video** — Whisper, TTS, and Sora are not available through any MCP server
- **Cost-sensitive users** — automated MCP loops with reasoning models can generate surprising bills
- **Production teams** — community servers lack the maintenance guarantees needed for reliability-critical deployments

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official OpenAI announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*
