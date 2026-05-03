---
title: "Mistral AI MCP Server — Europe's Open-Weight Champion Embraces the Model Context Protocol"
date: 2026-03-23T17:00:00+09:00
description: "Mistral AI has no standalone MCP server — instead, they built MCP client support directly into Le Chat (20+ connectors) and the Agents API."
og_description: "Mistral AI integrates MCP as a client in Le Chat (20+ connectors) and Agents API, with Apache 2.0 open-weight models from 3B to 675B. AAIF Silver member. Rating: 3/5."
content_type: "Review"
card_description: "Mistral AI takes a client-first approach to MCP, embedding 20+ MCP-powered connectors into Le Chat and full MCP support in the Agents API and Python SDK. No official MCP server exists — Mistral positions its open-weight models and European data sovereignty as the differentiator."
last_refreshed: 2026-05-03
---

**At a glance:** Mistral AI has **no official MCP server** — instead, they built MCP client support into [Le Chat](https://chat.mistral.ai/) (20+ MCP connectors, now with custom MCP support and a centralized Studio connector registry) and the [Agents API](https://docs.mistral.ai/agents/tools/mcp) (stdio + SSE transport). **May 2026 update:** Mistral Medium 3.5 launched April 29 (128B dense, 77.6% SWE-Bench Verified, $1.50/$7.50/M tokens); Voxtral TTS launched March 23 (4B voice model, $0.016/1K chars, 9 languages); Le Chat got Work Mode (April 29, agentic cross-tool workflows for Pro/Team/Enterprise) and formalized custom MCP connector support (April 15). Community servers remain small: [everaldo/mcp-mistral-ocr](https://github.com/everaldo/mcp-mistral-ocr) (37 stars, MIT) and [itisaevalex/mistr-agent](https://github.com/itisaevalex/mistr-agent) (17 stars, MIT). Part of our **[AI Providers MCP category](/categories/ai-providers/)**.

Mistral AI is **Europe's most prominent AI company** and a champion of open-weight models. Rather than publishing MCP servers that wrap its API, Mistral has taken a **client-first approach**: Le Chat connects to external MCP servers, and the Agents API lets developers wire MCP tools into Mistral-powered agents. The models themselves — from 3B Ministral to 675B Mistral Large 3 — are available under Apache 2.0 and run anywhere.

[Mistral AI](https://mistral.ai/) was founded in April 2023 by Arthur Mensch (ex-Google DeepMind), Guillaume Lample (ex-Meta), and Timothee Lacroix (ex-Meta). Headquartered in Paris with offices in London and Palo Alto. As of early 2026: approximately **EUR 300 million ARR** (September 2025, targeting EUR 1 billion by end of 2026), **$14 billion valuation** (September 2025 Series C), over **$3 billion total funding** (investors include ASML at 11%, General Catalyst, Andreessen Horowitz, Lightspeed), approximately **800+ employees**. Mistral is an **AAIF Silver member** (joined February 2026 expansion).

## What's Changed Since March 2026

**Mistral Medium 3.5** (April 29, 2026): A 128B dense model with 77.6% SWE-Bench Verified performance and a 91.4 τ³-Telecom agentic score. Priced at $1.50/$7.50 per million tokens. 256K context window. Open weights under a modified MIT license. Self-hostable on 4 GPUs. Powers Vibe Remote Agents.

**Voxtral TTS** (March 23, 2026): Mistral's first voice model — a 4B text-to-speech system (3.4B transformer decoder + 390M acoustic transformer + 300M neural audio codec) built on Ministral 3B. Supports 9 languages, voice cloning from 3 seconds of reference audio, and cross-lingual transfer. Priced at $0.016 per 1,000 characters. Available via API and Le Chat. Weights released as CC BY NC 4.0 (non-commercial).

**Connectors formalized** (April 15, 2026): Mistral published a dedicated Connectors API formalizing custom MCP support across Studio, Le Chat, and Vibe. Developers can now create, modify, list, and delete MCP connectors programmatically. The `requires_confirmation` parameter provides human-in-the-loop control on sensitive tools. This is the biggest MCP-specific improvement since the original launch.

**Work Mode** (April 29, 2026, preview): Le Chat's new agentic mode for Pro/Team/Enterprise enables cross-tool workflows spanning email, calendar, messages, and documents in a single persistent session.

**Workflows** (April 27, 2026, public preview): Durable orchestration layer via Python SDK v3.0, backed by Temporal. Supports `wait_for_input()` for human-in-the-loop pauses. Targeted at enterprise deployments; production customers include ASML and CMA-CGM.

**Community servers**: No growth since March — everaldo/mcp-mistral-ocr and itisaevalex/mistr-agent each hold at 37 and 17 stars respectively. The community MCP ecosystem remains thin.

**Architecture note:** Mistral's MCP strategy is the **inverse** of Google's. Where Google published 24+ official MCP servers, Mistral published zero — focusing instead on being a capable MCP **client** that connects to the broader MCP ecosystem. Le Chat's 20+ connectors (Databricks, Snowflake, GitHub, Notion, Stripe, etc.) are all MCP-powered, and any remote MCP server can be added manually.

## What It Does

### Le Chat as MCP Client

Le Chat, Mistral's consumer and enterprise AI assistant, gained MCP support on September 2, 2025 with 20+ built-in connectors:

| Connector Category | Services |
|-------------------|----------|
| Data & Analytics | Databricks, Snowflake |
| Developer Tools | GitHub, Linear, Sentry |
| Productivity | Notion, Asana, Monday.com, Jira, Confluence |
| Infrastructure | Cloudflare, Pinecone, Prisma Postgres |
| Finance | PayPal, Plaid, Square, Stripe |
| Business | Zapier, Brevo, Box |
| Knowledge | DeepWiki |
| Automation | Zapier |

**Key capabilities:**
- Users can connect to **any remote MCP server** beyond the built-in directory
- Admin-level connector control with on-behalf authentication for Enterprise
- Available on all tiers including the Free plan
- 4.2 million active users in the first month after mobile launch

**April 2026 Connectors update:** Mistral formalized a centralized connector registry (April 15, 2026) spanning Studio, Le Chat, and Vibe. New capabilities:
- **Custom MCP connectors** — create, modify, list, and delete via Conversation API, Completions API, and Agent SDK
- **`requires_confirmation` parameter** — human-in-the-loop control on sensitive tools; users explicitly approve before execution
- **Tool exclusion** — disable specific tools per deployment
- Connector registry is shared across Le Chat (consumer), Studio (developer), and Vibe (coding agent)

### Le Chat Work Mode (April 2026)

Le Chat gained an **agentic Work Mode** (April 29, 2026, preview) for Pro, Team, and Enterprise plans:
- Cross-tool orchestration: email, calendar, messaging, documents, and web in a single workflow
- Inbox triage with drafted replies and automatic issue creation in connected trackers
- Research and synthesis across web sources and internal documents
- Persistent multi-turn sessions — work continues across conversations
- Visible tool calls with explicit approval required before sensitive actions execute

### Agents API & Python SDK

Mistral's Agents API (launched May 27, 2025) treats MCP as a first-class tool type:

| Feature | Detail |
|---------|--------|
| Transport | stdio (`MCPClientSTDIO`) and SSE (`MCPClientSSE`) |
| Authentication | OAuth support for remote servers (`build_oauth_params`) |
| Tool types | MCP alongside code execution, web search, image generation, document library |
| Documentation | [docs.mistral.ai/agents/tools/mcp](https://docs.mistral.ai/agents/tools/mcp) |

### Mistral Workflows (April 2026)

Mistral launched **Workflows** (April 27, 2026, public preview) — a durable orchestration layer built on [Temporal](https://temporal.io/):
- Python SDK v3.0 (`mistral-sdk` >= 3.0)
- **`wait_for_input()`** pauses execution for human approval; reviewers respond via Le Chat or webhooks
- Deployment options: Mistral control plane (hosted) + customer-side workers (cloud, on-premises, hybrid)
- Production customers: ASML, ABANCA, CMA-CGM, France Travail, La Banque Postale, Moeve
- No MCP-specific integration details yet; compatible with the existing Agents API MCP tooling

### Vibe Remote Agents (April 2026)

Mistral's coding agent platform Vibe gained **Remote Agents** (April 29, 2026):
- Cloud-based async coding sessions launched from CLI or Le Chat — work continues while you're away
- Isolated sandboxes; session teleportation allows handing off a local session to the cloud
- Integrations: GitHub, Linear, Jira, Sentry, Slack, Teams
- Powered by **Mistral Medium 3.5** (see model updates below)

### No Official MCP Server

A search of the `mistralai` GitHub organization returns zero MCP server repositories. Mistral provides MCP documentation and client SDKs, but **does not publish a server wrapping the Mistral API**. This means developers who want to use Mistral models via MCP must use community servers or multi-provider tools.

## Community Servers

### everaldo/mcp-mistral-ocr (37 stars)

| Aspect | Detail |
|--------|--------|
| GitHub | [everaldo/mcp-mistral-ocr](https://github.com/everaldo/mcp-mistral-ocr) — 37 stars, 13 forks, MIT |
| Language | Python |
| What it does | MCP server for Mistral's OCR API — extract text and structure from PDFs and images |
| Created | March 2025 |
| Known issues | Docker container cleanup bug (open since April 2025) |

### itisaevalex/mistr-agent (17 stars)

| Aspect | Detail |
|--------|--------|
| GitHub | [itisaevalex/mistr-agent](https://github.com/itisaevalex/mistr-agent) — 17 stars, 9 forks, MIT |
| Language | TypeScript |
| What it does | MCP client enabling Mistral AI models to autonomously execute tasks via MCP tools |
| Updated | March 2026 |

### Other Community Projects

| Repo | Stars | What it does |
|------|-------|-------------|
| [hathibelagal-dev/desktop4mistral](https://github.com/hathibelagal-dev/desktop4mistral) | 18 | Desktop client with MCP support for Mistral LLMs (GPL-3.0) |
| [JamesANZ/cross-llm-mcp](https://github.com/JamesANZ/cross-llm-mcp) | 13 | MCP server for multiple LLM APIs including Mistral (MIT) |
| [colinfrisch/chathletique-mcp](https://github.com/colinfrisch/chathletique-mcp) | 12 | Strava Coach — Mistral MCP Hackathon Winner (Sep 2025) |
| [lemopian/mistral-ocr-mcp](https://github.com/lemopian/mistral-ocr-mcp) | 8 | MCP server for Mistral Document OCR |

The community ecosystem is **notably small** — total GitHub search for "mistral mcp" returns ~151 repos, but most are multi-provider projects that mention Mistral alongside other LLMs.

## Mistral MCP Hackathon

Mistral hosted the **first official MCP hackathon** on September 13-14, 2025 at Station F in Paris, co-sponsored with Bria AI and Cerebral Valley, with $10K+ in prizes. This produced several MCP projects but none gained significant traction beyond the event.

## Mistral Model Pricing

All API pricing per 1 million tokens:

### Frontier Models

| Model | Parameters | Active | Context | Input | Output | License |
|-------|-----------|--------|---------|-------|--------|---------|
| Mistral Large 3 | 675B MoE | 41B | 256K | $0.50 | $1.50 | Apache 2.0 |
| **Mistral Medium 3.5** *(NEW Apr 29)* | 128B dense | 128B | 256K | $1.50 | $7.50 | Modified MIT |
| Mistral Small 4 | 119B MoE (128 experts) | 6.5B | 256K | $0.15 | $0.60 | Apache 2.0 |
| Mistral Medium 3.1 | N/A | N/A | 128K | $0.40 | $2.00 | Proprietary |
| Magistral Medium 1.2 | N/A | N/A | N/A | $2.00 | $5.00 | Proprietary |
| Magistral Small 1.2 | 24B | 24B | N/A | Free | Free | Apache 2.0 |

### Small & Edge Models

| Model | Parameters | Input | Output | License |
|-------|-----------|-------|--------|---------|
| Mistral Small 3.2 | 24B | $0.075 | $0.20 | Apache 2.0 |
| Ministral 3 14B | 14B | $0.20 | $0.20 | Apache 2.0 |
| Ministral 3 8B | 8B | $0.15 | $0.15 | Apache 2.0 |
| Ministral 3 3B | 3B | $0.10 | $0.10 | Apache 2.0 |
| Mistral Nemo 12B | 12B (128K ctx) | $0.02 | $0.04 | Apache 2.0 |

### Specialist Models

| Model | Focus | Input | Output | License |
|-------|-------|-------|--------|---------|
| Devstral 2 | Code agents / SWE | $0.40 | $0.90 | Apache 2.0 |
| Codestral (25.08) | Code completion (256K ctx) | $0.30 | $0.90 | Proprietary |
| Pixtral Large | Multimodal (124B, 128K ctx) | $2.00 | $6.00 | Proprietary |
| Pixtral 12B | Multimodal (128K ctx) | $0.10 | $0.10 | Apache 2.0 |
| **Voxtral TTS** *(NEW Mar 23)* | Text-to-speech (4B, 9 languages) | $0.016/1K chars | — | CC BY NC 4.0 |
| Leanstral | Lean 4 formal verification | $36/run (pass@2) | — | Apache 2.0 |

**Key point:** Mistral's major models are **Apache 2.0 open-weight** — you can download and self-host them for free. API pricing is competitive, with Mistral Nemo at $0.02/$0.04 per million tokens being among the cheapest options available. Le Chat Free plan provides unlimited messages (subject to fair use).

### Le Chat Plans

| Plan | Price | Key Features |
|------|-------|-------------|
| Free | $0 | Unlimited messages, web search, MCP connectors, memory |
| Pro | $14.99/month | Priority access, higher limits |
| Team | $24.99/user/month | 200 messages/user, 30GB storage, admin controls |
| Enterprise | Custom | SAML SSO, audit logs, on-premises, GDPR/EU data residency |

## AI Provider MCP Comparison

| Feature | Mistral AI | Anthropic | Google | OpenAI | Meta/Llama | Hugging Face |
|---------|-----------|-----------|--------|--------|------------|-------------|
| Official MCP server | No | No (reference servers) | Yes (3.4k stars) | No | No | Yes (210 stars) |
| Server approach | Client-only | Reference implementations | Managed remote + open-source | Client only | Client only (Llama Stack) | Hub access + Gradio Spaces |
| MCP client | Yes (Le Chat, Agents API) | Yes (all Claude products) | Yes (Gemini CLI, SDKs) | Yes (ChatGPT, Agents SDK) | Yes (Llama Stack) | No |
| AAIF member | Yes (Silver) | Yes (Platinum, co-founder) | Yes (Platinum) | Yes (Platinum, co-founder) | No | No |
| Unique strength | Open-weight + EU sovereignty | Created the protocol | Most official servers (24+) | 900M+ weekly users | Fully free models | 1M+ models, Gradio-as-MCP |
| Open-weight models | Yes (Apache 2.0, 3B-675B) | No | Some (Gemma) | No | Yes (Llama license) | Platform (hosts all) |
| Free tier | Yes (Le Chat Free) | Yes (limited Claude) | Yes (Flash models) | Yes (limited ChatGPT) | Yes (all models free) | Yes (full Hub access) |

## Known Issues

1. **No official MCP server** — Unlike Google (24+ servers) or Hugging Face (official Hub server), Mistral publishes no MCP server wrapping its API. Developers wanting Mistral-via-MCP must rely on community wrappers with single-digit to double-digit star counts.

2. **Tiny community ecosystem** — The largest Mistral-specific MCP server has 37 stars. Compare this to OpenAI community wrappers (2,100+ stars) or even Meta/Llama bridges (972 stars). The ecosystem lacks critical mass.

3. **AAIF Silver tier limits influence** — As a Silver member (joined February 2026), Mistral has less governance influence than Platinum co-founders Anthropic and OpenAI or Platinum members Google, Microsoft, and AWS. This matters as MCP evolves.

4. **Le Chat connectors are curated, not open** — While Le Chat supports adding any remote MCP server, the built-in directory of 20+ connectors is Mistral-curated. There's no open marketplace or community-contributed connector directory.

5. **European positioning creates friction** — Mistral's strong EU data sovereignty pitch (GDPR compliance, EU data residency, on-premises Enterprise deployment) is an advantage for European customers but may create integration complexity for global teams.

6. **Open-weight ≠ open-source** — Mistral's Apache 2.0 models release weights but not training data or full training code. This distinction matters for reproducibility and audit requirements.

7. **Agents API MCP is SDK-only** — MCP integration in the Agents API requires the Mistral Python SDK. There's no hosted MCP proxy or managed server — developers must manage their own MCP server connections.

8. **Hackathon didn't catalyze ecosystem** — The September 2025 MCP Hackathon at Station F produced several projects, but none gained significant traction (highest: 12 stars). The event didn't generate lasting community momentum; community star counts are unchanged six weeks later.

9. **Model naming complexity** — Mistral's lineup (Mistral, Ministral, Magistral, Codestral, Devstral, Pixtral, Voxtral, Leanstral) creates confusion for developers choosing which model to use with MCP tools.

10. **Revenue gap to competitors** — At EUR 300M ARR (September 2025 figure; no update since), Mistral is significantly smaller than Anthropic (~$19B annualized), Google ($402B), or Meta ($201B). This affects long-term investment capacity in MCP ecosystem development.

## Bottom Line

**Rating: 3 out of 5**

Mistral AI brings a **distinctive value proposition** to the MCP ecosystem: genuinely open-weight models (Apache 2.0, from 3B to 675B parameters) combined with strong European data sovereignty guarantees. Le Chat's 20+ MCP connectors — now formalized via the Connectors API with custom MCP support and human-in-the-loop controls — make it an increasingly capable MCP client. The Agents API provides solid MCP integration for developers building custom agents.

The **client-first strategy** continues to deepen. The April 15, 2026 Connectors update is the most significant MCP-specific improvement since launch: developers can now programmatically manage MCP connectors across Studio, Le Chat, and Vibe, with `requires_confirmation` for controlled tool execution. Work Mode (April 29) shows Mistral committing to agentic workflows rather than just model access. Mistral Medium 3.5 (77.6% SWE-Bench Verified) and Voxtral TTS expand the model portfolio significantly.

However, the **absence of an official MCP server** remains the core gap. Developers who want to use Mistral models via MCP from Claude Desktop, Cursor, or other MCP clients still have no official path — only community wrappers with minimal adoption (37 stars for the top server, unchanged over six weeks). This is a missed opportunity given that Mistral's competitive API pricing and open-weight models could make them a popular MCP-accessible model provider.

The 3/5 rating holds. The MCP client infrastructure has meaningfully improved, but the fundamental gap — no official server, tiny community — is unchanged. **Watch for:** An official Mistral API MCP server or a formalized server hosting option would push this to 3.5 or higher.

**Who benefits most from Mistral's MCP ecosystem:**

- **European enterprises** — GDPR compliance, EU data residency, on-premises deployment, with Le Chat's MCP connectors for tool integration
- **Cost-conscious developers** — Mistral Nemo at $0.02/M input tokens and open-weight models you can self-host for free, accessible via Agents API MCP integration
- **Open-weight advocates** — Apache 2.0 models from 3B to 675B, downloadable and runnable anywhere, with MCP client support for connecting to external tools

**Who should be cautious:**

- **Teams wanting to expose Mistral models as MCP tools** — no official server exists; community options have minimal stars and uncertain maintenance
- **Developers building on MCP server infrastructure** — Mistral's investment is entirely on the client side; there's no official server SDK, reference implementation, or server hosting
- **Anyone expecting a large MCP ecosystem** — at ~151 GitHub repos (most multi-provider), Mistral's MCP footprint is among the smallest of the major AI providers

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official Mistral AI announcements. Information is current as of May 2026. See our [About page](/about/) for details on our review process.*
