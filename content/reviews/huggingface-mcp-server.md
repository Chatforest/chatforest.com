---
title: "Hugging Face MCP Server — The AI Community Hub Meets the Model Context Protocol"
date: 2026-03-23T16:30:00+09:00
description: "Hugging Face operates an official MCP server connecting AI assistants to the Hub's 1M+ models, 500K+ datasets, and thousands of Gradio Spaces. Plus community servers for Spaces integration and research papers. Here's the full picture."
og_description: "Hugging Face's official MCP server (210 stars, 98 releases) connects AI assistants to 1M+ models, 500K+ datasets, and MCP-compatible Gradio Spaces. Rating: 3.5/5."
content_type: "Review"
card_description: "Hugging Face operates the official hf-mcp-server connecting AI assistants to the Hub's 1M+ models, 500K+ datasets, Spaces, and papers. Any Gradio Space can become an MCP tool with one line of code. The server supports Streamable HTTP, OAuth, and 7 built-in tools."
last_refreshed: 2026-03-23
---

**At a glance:** [huggingface/hf-mcp-server](https://github.com/huggingface/hf-mcp-server) (210 stars, 56 forks, 723 commits, 98 releases, MIT license) — the official Hugging Face MCP server connecting AI assistants to the Hub. Plus [evalstate/mcp-hfspace](https://github.com/evalstate/mcp-hfspace) (383 stars, 56 forks, MIT) for direct Spaces integration and [shreyaskarnik/huggingface-mcp-server](https://github.com/shreyaskarnik/huggingface-mcp-server) (70 stars, MIT) for read-only Hub API access.

Hugging Face's MCP server connects your AI assistant — Claude Desktop, Cursor, VS Code, Gemini CLI, ChatGPT, or any MCP-compatible client — directly to the **largest open-source AI hub in the world**: 1 million+ models, 500,000+ datasets, and thousands of Gradio Spaces that can each serve as their own MCP tool. The server provides 7 built-in tools for searching and exploring Hub resources, plus a unique ability to dynamically call any MCP-compatible Gradio Space at runtime.

[Hugging Face](https://huggingface.co/) was founded in 2016 and has become the **central platform for open-source AI**. As of early 2026: approximately **$130 million revenue** (2024), **$4.5 billion valuation** (August 2023 Series D, $396M total raised), **10 million+ registered users**, **100,000+ organizations**, approximately **684 employees**, **50 billion cumulative model downloads**, and **100+ petabytes** of dataset storage. Investors include Google, Amazon, Nvidia, IBM, Salesforce, and Intel.

**Architecture note:** Hugging Face's MCP strategy is **platform-centric** — rather than wrapping a single AI model API (like OpenAI or Google), they connect AI assistants to their entire Hub ecosystem. The official server is hosted as a remote Streamable HTTP service at `https://huggingface.co/mcp`, with a settings page for per-user tool configuration. Any Gradio Space can become an MCP tool by adding `mcp_server=True` to its `launch()` method, creating a potentially **unlimited** supply of community-built MCP tools.

## What It Does

### Built-in Tools (7)

The official HF MCP server includes 7 tools, configurable via your [MCP settings](https://huggingface.co/settings/mcp):

| Tool | What It Does |
|------|-------------|
| Model Search | Search for ML models with filters for task, library, and more |
| Dataset Search | Search for datasets with filters for author, tags, and more |
| Spaces Semantic Search | Find AI apps via natural language queries |
| Papers Semantic Search | Find ML research papers via natural language queries |
| Documentation Semantic Search | Search Hugging Face documentation using natural language |
| Hub Repository Details | Get detailed info about models, datasets, and Spaces (optionally includes README) |
| Run and Manage Jobs | Run, monitor, and schedule jobs on Hugging Face infrastructure |

### Gradio Spaces as MCP Tools

This is Hugging Face's **unique differentiator** in the MCP ecosystem. Any Gradio Space can become an MCP tool:

- **For Space creators:** Add `mcp_server=True` to `launch()` — Gradio automatically converts Python functions into MCP-compatible tools using docstrings for descriptions
- **For users:** Browse [MCP-compatible Spaces](https://huggingface.co/spaces?filter=mcp-server), click the MCP badge, and add them to your tools
- **Dynamic Spaces (experimental):** Your assistant can discover and use MCP-compatible Spaces on-the-fly without manual setup
- **Capabilities:** Image generation (FLUX.1), audio transcription, text-to-speech, vision models, object detection, and more — whatever the community builds

### Transport & Authentication

| Feature | Detail |
|---------|--------|
| Transport | Streamable HTTP (stateless, direct response) |
| Authentication | OAuth via Hugging Face account; anonymous access available with standard tools |
| Client support | Claude Desktop, Claude Code, Cursor, VS Code, Zed, Gemini CLI, ChatGPT, Codex |
| Configuration | Auto-generated config snippets at [huggingface.co/settings/mcp](https://huggingface.co/settings/mcp) |
| ZeroGPU | Authenticated users get GPU quota applied correctly for compute-intensive Spaces |

## Community Servers

### evalstate/mcp-hfspace (383 stars)

| Aspect | Detail |
|--------|--------|
| GitHub | [evalstate/mcp-hfspace](https://github.com/evalstate/mcp-hfspace) — 383 stars, 56 forks, 155 commits, MIT |
| Language | TypeScript |
| What it does | Direct integration between Claude Desktop and Hugging Face Spaces with automatic endpoint discovery |
| Default Space | FLUX.1-schnell for image generation |
| Features | Private Space access via HF token, Claude Desktop mode for optimized image returns, custom API endpoints |
| Downloads | ~14.7K npm downloads |
| Status | Superseded by official HF MCP server but still actively maintained; popular for local deployment |

### shreyaskarnik/huggingface-mcp-server (70 stars)

| Aspect | Detail |
|--------|--------|
| GitHub | [shreyaskarnik/huggingface-mcp-server](https://github.com/shreyaskarnik/huggingface-mcp-server) — 70 stars, 13 forks, 6 commits, MIT |
| Language | Python |
| What it does | Read-only access to Hub APIs — search models, datasets, Spaces, papers, collections |
| Tools | 10 tools: search-models, get-model-info, search-datasets, get-dataset-info, search-spaces, get-space-info, get-paper-info, get-daily-papers, search-collections, get-collection-info |
| Features | Custom `hf://` URI schemes, prompt templates for model comparison and paper summarization |

### huangxinping/huggingface-daily-paper-mcp (niche)

| Aspect | Detail |
|--------|--------|
| GitHub | [huangxinping/huggingface-daily-paper-mcp](https://github.com/huangxinping/huggingface-daily-paper-mcp) |
| Language | Python |
| What it does | Fetches Hugging Face daily papers — today's, yesterday's, or by specific date |
| Tools | get_papers_by_date, get_today_papers, get_yesterday_papers |

## Hugging Face MCP Course

Hugging Face partnered with Anthropic to create a **free, open-source MCP course** — [huggingface/mcp-course](https://github.com/huggingface/mcp-course) (853 stars, 235 forks). Covers MCP fundamentals, building servers with Gradio and Python SDK, building clients, and a final project. This makes Hugging Face the **leading educational resource** for MCP development.

## Hugging Face Pricing

The MCP server itself is **free** — it accesses the Hub's free API. Costs only apply if you use paid Hugging Face services:

| Service | Cost |
|---------|------|
| Hub (free tier) | Free — browse models, datasets, Spaces, papers |
| Hugging Face Pro | $9/month — private repos, faster inference, more compute |
| Team plan | $20/user/month — collaboration features |
| Enterprise | $50/user/month — SSO, audit logs, advanced admin |
| Inference API (free) | Free — rate-limited, for testing |
| Inference API (Pro) | Pay-per-use based on compute time |
| Inference Endpoints | $0.03–$80/hour depending on hardware |
| Spaces (free) | Free — CPU-only, community GPU via ZeroGPU |
| Spaces (paid) | $0.03–$4.40/hour for dedicated GPU |

**Key point:** Unlike OpenAI, Google, or Anthropic, Hugging Face's core value proposition through MCP is **access to open-source models and community tools**, not a proprietary API. Most MCP usage costs nothing.

## AI Provider MCP Comparison

| Feature | Hugging Face | Anthropic | Google | OpenAI | Meta/Llama |
|---------|-------------|-----------|--------|--------|------------|
| Official MCP server | Yes (210 stars) | No (reference servers) | Yes (3.4k stars) | No | No |
| Server approach | Hub access + Gradio Spaces | Reference implementations | Managed remote + open-source | Client only | Client only (Llama Stack) |
| MCP client | No | Yes (all Claude products) | Yes (Gemini CLI, SDKs) | Yes (ChatGPT, Agents SDK) | Yes (Llama Stack) |
| AAIF member | No | Yes (platinum, co-founder) | Yes (platinum) | Yes (platinum, co-founder) | No |
| Unique strength | 1M+ models, Gradio-as-MCP | Created the protocol | Most official servers (24+) | 900M+ weekly users | Fully free models |
| MCP course/education | Yes (free course, 853 stars) | Yes (docs + specification) | No | No | No |
| Free tier | Yes (full Hub access) | Yes (limited Claude) | Yes (Flash models) | Yes (limited ChatGPT) | Yes (all models free) |

## Known Issues

1. **Not an AAIF member** — Despite deep MCP investment (official server, free course, Gradio integration), Hugging Face is not a member of the Agentic AI Foundation. This means no seat at the governance table where MCP's future is decided by Anthropic, OpenAI, Google, Microsoft, and AWS.

2. **Relatively low GitHub stars (210)** — Compared to Google's MCP repo (3.4k stars) or Anthropic's reference servers (81.8k stars), the official HF MCP server has modest adoption. The 98 releases and 723 commits show active development, but community awareness lags.

3. **Client timeout issues** — Claude Desktop uses a hard 60-second timeout and doesn't use progress notifications for keep-alive. Compute-intensive Gradio Spaces (image generation, large model inference) can exceed this limit, causing silent failures.

4. **Dynamic Spaces is experimental** — The feature to auto-discover and call MCP-compatible Spaces at runtime is marked experimental. Reliability and security implications of dynamically executing arbitrary community Spaces are still being evaluated.

5. **No MCP client** — Hugging Face doesn't offer an MCP client product. They build the **tools** (server, Gradio integration, educational content) but rely on Claude, Cursor, VS Code, and other clients for the end-user experience.

6. **VSCode polling bug** — When the server returns a web page instead of an HTTP 405 error, VS Code clients can poll the endpoint multiple times per second, wasting resources and potentially hitting rate limits.

7. **Gradio Space quality varies** — Community-built Gradio Spaces exposed as MCP tools have no quality guarantees. Tool descriptions may be poor, APIs may break, and Spaces can go offline without notice. The MCP badge indicates compatibility, not reliability.

8. **Session management bugs** — The `add_mcp_server` method in the HuggingFace Hub library has a known issue where new sessions close previous sessions, causing unexpected disconnections ([Issue #3203](https://github.com/huggingface/huggingface_hub/issues/3203)).

9. **Server-push notifications limited** — Most MCP clients disconnect after inactivity, meaning push notifications are missed. The server uses a stateless direct-response model, which is simpler but means no real-time updates for long-running operations.

10. **Spaces compute costs can surprise** — While the MCP server is free, calling GPU-intensive Gradio Spaces via MCP consumes ZeroGPU quota (authenticated) or may fail (anonymous). Users may not realize they're burning compute credits when their AI assistant calls a Space tool.

## Bottom Line

**Rating: 3.5 out of 5**

Hugging Face brings something **no other AI company offers** to the MCP ecosystem: access to the world's largest open-source AI hub through a single protocol. With 1 million+ models, 500,000+ datasets, and the ability to turn any Gradio Space into an MCP tool, the platform's breadth is unmatched. The official server's 7 built-in tools cover the core Hub discovery workflow — finding models, datasets, papers, and documentation — and the Gradio-as-MCP integration creates a potentially unlimited ecosystem of community tools.

The **Gradio integration** is the standout feature. Adding `mcp_server=True` to a Space's `launch()` call is arguably the easiest path from "Python function" to "MCP tool" in the entire ecosystem. Combined with free Spaces hosting, this lowers the barrier to MCP server creation below what any other platform offers.

On the **educational side**, Hugging Face's free MCP course (853 stars, built with Anthropic) is the most comprehensive learning resource for MCP development. No other AI company has invested this heavily in MCP education.

The 3.5/5 rating reflects the **gap between potential and current state**. The official server has modest adoption (210 stars vs. thousands for comparable servers), Hugging Face isn't in the AAIF, there's no MCP client product, Dynamic Spaces is still experimental, and the quality of community Gradio tools varies widely. The server is also a **Hub discovery tool**, not a model inference tool — you search for models, you don't run them through MCP (that requires separate Inference API or Endpoints setup).

**Who benefits most from Hugging Face's MCP ecosystem:**

- **ML researchers** — semantic search across papers, models, and datasets from within your AI assistant; daily paper feeds via community servers
- **MCP server builders** — Gradio-as-MCP is the fastest way to create and host an MCP server for free; the MCP course teaches the fundamentals
- **Open-source AI users** — discover and access the entire Hugging Face Hub from Claude Desktop, Cursor, or any MCP client without leaving your workflow

**Who should be cautious:**

- **Teams expecting production model inference via MCP** — the server searches the Hub; running models requires separate Inference API/Endpoints setup and billing
- **Users relying on Dynamic Spaces** — experimental feature; community Spaces may have poor tool descriptions, break without notice, or consume unexpected compute
- **Anyone needing AAIF governance influence** — Hugging Face has no seat at the table where MCP's future direction is decided

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official Hugging Face announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*
