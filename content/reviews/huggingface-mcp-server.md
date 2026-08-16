---
title: "Hugging Face MCP Server — The AI Community Hub Meets the Model Context Protocol"
date: 2026-03-23T16:30:00+09:00
description: "Hugging Face operates an official MCP server connecting AI assistants to the Hub's 2M+ models, 500K+ datasets, and thousands of Gradio Spaces."
og_description: "Hugging Face's official MCP server (273 stars, v0.3.11 at last refresh) connects AI assistants to 2M+ models, 500K+ datasets, and MCP-compatible Gradio Spaces. Now with repo creation. Rating: 3.5/5."
content_type: "Review"
card_description: "Hugging Face operates the official hf-mcp-server connecting AI assistants to the Hub's 2M+ models, 500K+ datasets, Spaces, and papers. Any Gradio Space can become an MCP tool with one line of code. The server supports Streamable HTTP, OAuth, and includes tools for search, Hub inspection, job management, and repository creation."
last_refreshed: 2026-05-03
sources_audited: 2026-08-16
---

**At a glance:** [huggingface/hf-mcp-server](https://github.com/huggingface/hf-mcp-server) ([273 stars, 93 forks, MIT license](https://github.com/huggingface/hf-mcp-server), v0.3.11 at the May 2026 refresh — [v0.4.9 is current](https://github.com/huggingface/hf-mcp-server/releases) as of this audit) — the official Hugging Face MCP server connecting AI assistants to the Hub. Plus [evalstate/mcp-hfspace](https://github.com/evalstate/mcp-hfspace) (388 stars, 58 forks, MIT) for direct Spaces integration and [shreyaskarnik/huggingface-mcp-server](https://github.com/shreyaskarnik/huggingface-mcp-server) (71 stars, MIT, dormant) for read-only Hub API access. Part of our **[AI Providers MCP category](/categories/ai-providers/)**.

*Refreshed May 2026: [v0.3.11 adds repository creation tool](https://github.com/huggingface/hf-mcp-server/releases/tag/v0.3.11); [v0.3.10 added MCP App proxy support](https://github.com/huggingface/hf-mcp-server/releases/tag/v0.3.10); 293 tagged MCP Spaces; PulseMCP #497 (66K all-time) at the time — [now #602, ~54.3K all-time](https://www.pulsemcp.com/servers/huggingface). Stars 210→229 at refresh, [273 as of this audit](https://github.com/huggingface/hf-mcp-server). Rating holds 3.5/5.*

Hugging Face's MCP server connects your AI assistant — Claude Desktop, Cursor, VS Code, Gemini CLI, ChatGPT, or any MCP-compatible client — directly to what Hugging Face itself describes as [the **largest open-source collection of models, datasets, and demos**](https://huggingface.co/docs/hub/en/index): [2 million+ models, 500,000+ datasets](https://huggingface.co/docs/hub/en/index), and thousands of Gradio Spaces that can each serve as their own MCP tool. The server provides 7 built-in tools for searching and exploring Hub resources, plus a unique ability to dynamically call any MCP-compatible Gradio Space at runtime.

[Hugging Face](https://huggingface.co/) was [founded in 2016](https://www.internethistorypodcast.com/2025/11/clement-delangue-of-hugging-face/) by Clément Delangue, Julien Chaumond, and Thomas Wolf, and has become the **central platform for open-source AI**. As of early-to-mid 2026: approximately **[$130 million revenue](https://getlatka.com/companies/hugging-face)** (2024), **[$4.5 billion valuation](https://www.cnbc.com/2023/08/24/google-amazon-nvidia-amd-other-tech-giants-invest-in-hugging-face.html)** ([August 2023 Series D](https://techcrunch.com/2023/08/24/hugging-face-raises-235m-from-investors-including-salesforce-and-nvidia/), $235M in that round on ~$396M total raised), **[13 million users](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)** (Hugging Face's own "State of Open Source" report, 2025), **[50,000+ organizations](https://huggingface.co/)** on the Hub, **[45+ billion cumulative Hub downloads](https://huggingface.co/blog/lbourdois/huggingface-models-stats)** (as of October 2025). [Investors include Google, Amazon, Nvidia, IBM, Salesforce, and Intel](https://www.cnbc.com/2023/08/24/google-amazon-nvidia-amd-other-tech-giants-invest-in-hugging-face.html).

**Architecture note:** Hugging Face's MCP strategy is **platform-centric** — rather than wrapping a single AI model API (like OpenAI or Google), they connect AI assistants to their entire Hub ecosystem. The official server is hosted as a remote Streamable HTTP service at `https://huggingface.co/mcp`, with a settings page for per-user tool configuration. Any Gradio Space can become an MCP tool by adding `mcp_server=True` to its `launch()` method, creating a potentially **unlimited** supply of community-built MCP tools.

## What It Does

### Built-in Tools (8+)

The official HF MCP server includes configurable tools via your [MCP settings](https://huggingface.co/settings/mcp). As of [v0.3.11 (April 29, 2026)](https://github.com/huggingface/hf-mcp-server/releases/tag/v0.3.11) — the version current at our May 2026 refresh; the project has since shipped through [v0.4.9](https://github.com/huggingface/hf-mcp-server/releases):

| Tool | What It Does |
|------|-------------|
| Model Search | Search for ML models with filters for task, library, and more |
| Dataset Search | Search for datasets with filters for author, tags, and more |
| Spaces Semantic Search | Find AI apps via natural language queries |
| Papers Semantic Search | Find ML research papers via natural language queries |
| Documentation Semantic Search | Search Hugging Face documentation using natural language |
| Hub Repository Details | Get detailed info about models, datasets, and Spaces (optionally includes README) |
| Run and Manage Jobs | Run, monitor, and schedule jobs on Hugging Face infrastructure |
| **Create Repository** *(new v0.3.11)* | Create new Hub repositories via CLI and huggingface.js |

The tool module tree also includes `duplicate-space`, `gradio-files`, `hf-api-call`, `hub-inspect`, `paper-summary`, `repo-search`, `space-files`, `space-info`, `user-summary`, and `dynamic-space-tool` — with configurable subsets exposed depending on your settings. [v0.3.10 added **MCP App proxy support**](https://github.com/huggingface/hf-mcp-server/releases/tag/v0.3.10), enabling hidden tool passthrough for MCP Apps.

### Gradio Spaces as MCP Tools

This is Hugging Face's **unique differentiator** in the MCP ecosystem. Any Gradio Space can become an MCP tool:

- **For Space creators:** [Add `mcp_server=True` to `launch()`](https://www.gradio.app/guides/building-mcp-server-with-gradio) — Gradio automatically converts Python functions into MCP-compatible tools using docstrings for descriptions
- **For users:** Browse [MCP-compatible Spaces](https://huggingface.co/spaces?filter=mcp-server) (293 tagged as of May 2026), click the MCP badge, and add them to your tools
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

### evalstate/mcp-hfspace (388 stars)

| Aspect | Detail |
|--------|--------|
| GitHub | [evalstate/mcp-hfspace](https://github.com/evalstate/mcp-hfspace) — 388 stars, 58 forks, MIT |
| Language | TypeScript |
| What it does | Direct integration between Claude Desktop and Hugging Face Spaces with automatic endpoint discovery |
| Default Space | FLUX.1-schnell for image generation |
| Features | Private Space access via HF token, Claude Desktop mode for optimized image returns, custom API endpoints |
| PulseMCP | [~20K all-time visits, #1,280 globally](https://www.pulsemcp.com/servers/evalstate-mcp-hfspace) (as of Aug 2026 audit; ~17,300 visits/#1,382 at the May 2026 refresh) |
| Status | Superseded by official HF MCP server but stable; no new releases since late 2025 |

### shreyaskarnik/huggingface-mcp-server (71 stars, dormant)

| Aspect | Detail |
|--------|--------|
| GitHub | [shreyaskarnik/huggingface-mcp-server](https://github.com/shreyaskarnik/huggingface-mcp-server) — 71 stars, 12 forks, 6 commits, MIT |
| Language | Python |
| What it does | Read-only access to Hub APIs — search models, datasets, Spaces, papers, collections |
| Tools | 10 tools: search-models, get-model-info, search-datasets, get-dataset-info, search-spaces, get-space-info, get-paper-info, get-daily-papers, search-collections, get-collection-info |
| Features | Custom `hf://` URI schemes, prompt templates for model comparison and paper summarization |
| Status | [Last commit March 19, 2025](https://github.com/shreyaskarnik/huggingface-mcp-server/commits/main) — no activity since. Effectively dormant. (Corrects a prior "March 21, 2026" date, which was a one-year error.) |

### huangxinping/huggingface-daily-paper-mcp (niche)

| Aspect | Detail |
|--------|--------|
| GitHub | [huangxinping/huggingface-daily-paper-mcp](https://github.com/huangxinping/huggingface-daily-paper-mcp) |
| Language | Python |
| What it does | Fetches Hugging Face daily papers — today's, yesterday's, or by specific date |
| Tools | get_papers_by_date, get_today_papers, get_yesterday_papers |

## Hugging Face MCP Course

Hugging Face [partnered with Anthropic](https://huggingface.co/learn/mcp-course/en/unit0/introduction) to create a **free, open-source MCP course** — [huggingface/mcp-course](https://github.com/huggingface/mcp-course) (910 stars, 258 forks as of this audit; 897/250 at the May 2026 refresh). Covers MCP fundamentals, building servers with Gradio and Python SDK, building clients, and a final project. This makes Hugging Face a **leading educational resource** for MCP development, alongside Anthropic's own [MCP documentation and specification](https://modelcontextprotocol.io/). [Recent updates](https://github.com/huggingface/mcp-course/pull/216) updated inference provider references across language translations (Nebius → Novita).

## Hugging Face Pricing

The MCP server itself is **free** — it accesses the Hub's free API. Costs only apply if you use paid Hugging Face services:

| Service | Cost |
|---------|------|
| Hub (free tier) | Free — browse models, datasets, Spaces, papers |
| [Hugging Face Pro](https://huggingface.co/pricing) | $9/month — private repos, faster inference, more compute |
| [Team plan](https://huggingface.co/pricing) | $20/user/month — collaboration features |
| [Enterprise](https://huggingface.co/pricing) | $50/user/month — SSO, audit logs, advanced admin |
| Inference API (free) | Free — rate-limited, for testing |
| Inference API (Pro) | Pay-per-use based on compute time |
| [Inference Endpoints](https://huggingface.co/pricing) | $0.03–$74/hour depending on hardware (CPU up to 8x Nvidia B200) |
| Spaces (free) | Free — CPU-only, community GPU via ZeroGPU |
| [Spaces (paid)](https://huggingface.co/pricing) | $0.03–$23.50/hour for dedicated GPU (CPU upgrade up to 8x Nvidia L40S) |

**Key point:** Unlike OpenAI, Google, or Anthropic, Hugging Face's core value proposition through MCP is **access to open-source models and community tools**, not a proprietary API. Most MCP usage costs nothing.

## AI Provider MCP Comparison

| Feature | Hugging Face | Anthropic | Google | OpenAI | Meta/Llama |
|---------|-------------|-----------|--------|--------|------------|
| Official MCP server | [Yes (273 stars)](https://github.com/huggingface/hf-mcp-server) | No (reference servers) | [Yes (16.2k stars)](https://github.com/googleapis/genai-toolbox) | No | No |
| Server approach | Hub access + Gradio Spaces | Reference implementations | Managed remote + open-source | Client only | Client only (Llama Stack) |
| MCP client | No | Yes (all Claude products) | Yes (Gemini CLI, SDKs) | Yes (ChatGPT, Agents SDK) | Yes (Llama Stack) |
| AAIF member | No | [Yes (platinum, co-founder)](https://aaif.io/members) | [Yes (platinum)](https://aaif.io/members) | [Yes (platinum, co-founder)](https://aaif.io/members) | No |
| Unique strength | 2M+ models, Gradio-as-MCP | Created the protocol | Most official servers (24+) | [900M+ weekly users](https://techcrunch.com/2026/02/27/chatgpt-reaches-900m-weekly-active-users/) | Fully free models |
| MCP course/education | Yes (free course, 910 stars) | Yes (docs + specification) | No | No | No |
| Free tier | Yes (full Hub access) | Yes (limited Claude) | Yes (Flash models) | Yes (limited ChatGPT) | Yes (all models free) |

## Known Issues

1. **Not an AAIF member** — Despite deep MCP investment (official server, free course, Gradio integration), Hugging Face is absent from the [Agentic AI Foundation's member list](https://aaif.io/members). This means no seat at the governance table where MCP's future is decided by [Anthropic, OpenAI, Google, Microsoft, and AWS](https://aaif.io/members) — the foundation's platinum sponsors.

2. **Relatively low GitHub stars (273 as of this audit)** — Compared to [Google's MCP Toolbox (~16.2K stars)](https://github.com/googleapis/genai-toolbox) or [Anthropic's reference servers (~89.6K stars)](https://github.com/modelcontextprotocol/servers), the official HF MCP server has modest adoption. [Active development](https://github.com/huggingface/hf-mcp-server/releases) (through v0.4.9 as of this audit; v0.3.11 on April 29, 2026 at our last refresh) shows commitment, but community awareness lags platform size.

3. **Client timeout issues** — Claude Desktop has been reported to use a hard ~60-second timeout for MCP tool calls without progress-notification keep-alive ([Anthropic's claude-code issue tracker](https://github.com/anthropics/claude-code/issues/22542); [related report](https://github.com/anthropics/claude-code/issues/43791)). Compute-intensive Gradio Spaces (image generation, large model inference) can exceed this limit, causing silent failures.

4. **Dynamic Spaces is experimental** — The feature to auto-discover and call MCP-compatible Spaces at runtime is marked experimental. Reliability and security implications of dynamically executing arbitrary community Spaces are still being evaluated.

5. **No MCP client** — Hugging Face doesn't offer an MCP client product. They build the **tools** (server, Gradio integration, educational content) but rely on Claude, Cursor, VS Code, and other clients for the end-user experience.

6. **VSCode polling bug (fixed)** — During development, when the server returned a web page instead of an HTTP 405 error, VS Code clients would poll the endpoint multiple times per second. Hugging Face [fixed this with browser detection, and the VS Code team shipped a corresponding fix](https://huggingface.co/blog/building-hf-mcp) — noted here as a documented example of client-compatibility rough edges, not a currently open bug.

7. **Gradio Space quality varies** — Community-built Gradio Spaces exposed as MCP tools have no quality guarantees. Tool descriptions may be poor, APIs may break, and Spaces can go offline without notice. The MCP badge indicates compatibility, not reliability.

8. **Session management bugs** — The `add_mcp_server` method in the huggingface_hub library has an open, unresolved issue where new sessions close the read/write streams of previous sessions, causing `anyio.ClosedResourceError` disconnections when using `load_tools()` ([Issue #3221](https://github.com/huggingface/huggingface_hub/issues/3221)).

9. **Server-push notifications limited** — Most MCP clients disconnect after inactivity, meaning push notifications are missed. The server uses a stateless direct-response model, which is simpler but means no real-time updates for long-running operations.

10. **Spaces compute costs can surprise** — While the MCP server is free, calling GPU-intensive Gradio Spaces via MCP consumes ZeroGPU quota (authenticated) or may fail (anonymous). Users may not realize they're burning compute credits when their AI assistant calls a Space tool.

## Bottom Line

**Rating: 3.5 out of 5**

Hugging Face brings something **no other AI company offers** to the MCP ecosystem: access to [what it calls the largest open-source collection of models, datasets, and demos](https://huggingface.co/docs/hub/en/index) through a single protocol. With 2 million+ models, 500,000+ datasets, and the ability to turn any Gradio Space into an MCP tool, the platform's breadth is unmatched. The official server's 7 built-in tools cover the core Hub discovery workflow — finding models, datasets, papers, and documentation — and the Gradio-as-MCP integration creates a potentially unlimited ecosystem of community tools.

The **Gradio integration** is the standout feature. [Adding `mcp_server=True` to a Space's `launch()` call](https://www.gradio.app/guides/building-mcp-server-with-gradio) is arguably the easiest path from "Python function" to "MCP tool" in the entire ecosystem. Combined with free Spaces hosting, this lowers the barrier to MCP server creation below what any other platform offers.

On the **educational side**, Hugging Face's free MCP course (910 stars as of this audit, [built with Anthropic](https://huggingface.co/learn/mcp-course/en/unit0/introduction)) is one of the most comprehensive learning resources for MCP development. Few other AI companies have invested this heavily in MCP education.

The 3.5/5 rating reflects the **gap between potential and current state**. The official server has modest adoption ([273 stars](https://github.com/huggingface/hf-mcp-server), [~54K PulseMCP visits globally, rank #602](https://www.pulsemcp.com/servers/huggingface) as of this audit), Hugging Face isn't in the [AAIF](https://aaif.io/members), there's no MCP client product, Dynamic Spaces is still experimental, and the quality of community Gradio tools varies widely. The server is also a **Hub discovery and management tool**, not a model inference tool — you search for models and now create repos, but running them requires separate Inference API or Endpoints setup.

**Who benefits most from Hugging Face's MCP ecosystem:**

- **ML researchers** — semantic search across papers, models, and datasets from within your AI assistant; daily paper feeds via community servers
- **MCP server builders** — Gradio-as-MCP is the fastest way to create and host an MCP server for free; the MCP course teaches the fundamentals
- **Open-source AI users** — discover and access the entire Hugging Face Hub from Claude Desktop, Cursor, or any MCP client without leaving your workflow

**Who should be cautious:**

- **Teams expecting production model inference via MCP** — the server searches the Hub; running models requires separate Inference API/Endpoints setup and billing
- **Users relying on Dynamic Spaces** — experimental feature; community Spaces may have poor tool descriptions, break without notice, or consume unexpected compute
- **Anyone needing AAIF governance influence** — Hugging Face has no seat at the table where MCP's future direction is decided

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official Hugging Face announcements. Originally published March 2026; refreshed May 2026. See our [About page](/about/) for details on our review process.*
