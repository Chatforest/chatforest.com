# Prompt Engineering & Optimization MCP Servers — Optimizers, Template Managers, Multi-LLM Routers, Security Guards, and 24+ More

> Prompt engineering MCP servers help AI agents optimize, manage, route, and secure prompts across LLM providers. We reviewed 24+ servers across 6 subcategories.


**Category:** [AI & ML Tools](/categories/ai-ml-tools/)

Prompt engineering is the skill layer between humans and LLMs — and it's one of the few areas where MCP servers can make every other MCP tool more effective. A good prompt optimization server doesn't just rewrite text; it applies research-backed techniques, manages template libraries, and can even route prompts across multiple LLM providers to find the best response.

**April 2026 update:** The biggest structural change since our initial review is the arrival of **prompt security** — MCP Guard (53 stars) is the first runtime prompt injection firewall for MCP, filling what was our #1 gap. The observability landscape also expanded significantly: Langfuse upgraded its MCP server from 2 read-only tools to 5 tools with full write capabilities via a native hosted endpoint, and both **Helicone** and **Braintrust** launched official MCP servers for prompt observability. The core prompt engineering servers saw modest growth (just-prompt 718→725, claude-prompts 143→147, mcp-prompts 110→113), with the ecosystem expanding from 20+ to 25+ servers.

For AI-generated content workflows, see our [CMS & Content Management](/reviews/cms-content-management-mcp-servers/) review. For search optimization of your content, see our [SEO](/reviews/seo-search-optimization-mcp-servers/) review.

## Multi-LLM Routing & Unified Prompting (1 server)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [disler/just-prompt](https://github.com/disler/just-prompt) | 737 | Python | — | 6 | Unified interface to 6 LLM providers with consensus tool |

**disler/just-prompt** (737 stars, up from 725 in April) is the most-starred server in this space, though it's more of a multi-LLM router than a prompt optimizer. It provides a unified interface to **OpenAI, Anthropic, Google Gemini, Groq, DeepSeek, and Ollama** through 6 tools: `prompt` (basic), `prompt_from_file`, `prompt_from_file_to_file`, `ceo_and_board` (consensus across models), `list_providers`, and `list_models`. The standout feature is the "CEO and board" tool — it queries multiple models in parallel and aggregates their responses for consensus-based decision-making. It supports extended reasoning features across providers (OpenAI o-series reasoning effort, Claude thinking tokens, Gemini thinking budget) and handles automatic model name correction including configurable `--default-models` parameter. Useful when you want an agent to compare responses across providers or route prompts to the cheapest/fastest model for a given task.

## Prompt Workflow & Template Engines (5+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| Langfuse native MCP | — | Built-in | — | 5 | **NEW** Hosted at /api/public/mcp, read+write, StreamableHttp |
| [langfuse/mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse) | 174 | TypeScript | MIT | 2 | Open-source Langfuse prompt retrieval (legacy) |
| [minipuft/claude-prompts-mcp](https://github.com/minipuft/claude-prompts-mcp) | 186 | TypeScript | MIT | 3 | Workflow composition, reasoning frameworks, skill export |
| [sparesparrow/mcp-prompts](https://github.com/sparesparrow/mcp-prompts) | 117 | TypeScript | MIT | 7 | Template management, JSON-file storage (npm v3.13.0) |
| [mikeskarl/mcp-prompt-templates](https://github.com/mikeskarl/mcp-prompt-templates) | 24 | Python | — | 3+ | Analysis templates (meetings, summaries, blog conversion) |
| [jezweb/smart-prompts-mcp](https://github.com/jezweb/smart-prompts-mcp) | 12 | TypeScript | MIT | 7 | GitHub-based prompt discovery and composition (archived) |

**Langfuse native MCP** is the biggest development in this subcategory. Langfuse now ships a **hosted MCP server built directly into the platform** at `/api/public/mcp` using StreamableHttp — no external setup, no build steps, no dependencies. The native server provides **5 tools** (up from 2 in the standalone version): `getPrompt` (fetch by name with optional label/version), `listPrompts` (filter by name/tag/label with pagination), `createTextPrompt` (create new text prompt versions with `{{variable}}` syntax), `createChatPrompt` (OpenAI-style system/user/assistant roles), and `updatePromptLabels` (manage production/staging labels across versions). Write capabilities are enabled by default; clients can restrict to read-only via an allowlist. The stateless architecture works across Cloud, self-hosted, or local deployments. This effectively makes Langfuse the first observability platform with full prompt CRUD via native MCP.

The open-source **langfuse/mcp-server-langfuse** (174 stars, up from 163 in April) still exists as a standalone alternative with 2 tools (`get-prompts`, `get-prompt`), but the native hosted version is now the recommended path.

**minipuft/claude-prompts-mcp** (186 stars, up from 147, 822 commits) remains the deepest workflow engine. Hot-reloadable YAML templates back the composition system: operator syntax chains steps (`-->`), hands off to agents (`=>`), injects reasoning frameworks (`@`), and adds validation gates (`::`). Six built-in reasoning frameworks (CAGEERF, ReACT, 5W1H, and more). A judge mode (`%judge`) auto-selects optimal resources. Workflows export as native skills for **Claude Code, Cursor, OpenCode**, and other platforms — running without MCP calls at runtime. 5 open PRs. **Correction (2026-08-16 audit):** this entry previously said tools had been renamed to `skills_manager`, `resource_manager`, and `prompt_executor`, and that the project was AGPL-3.0 licensed. Neither holds up on re-verification: the [current README](https://github.com/minipuft/claude-prompts-mcp/blob/main/README.md) still lists the tools as `prompt_engine`, `resource_manager`, and `system_control`, and the repo's [LICENSE file](https://github.com/minipuft/claude-prompts-mcp/blob/main/LICENSE) is MIT, not AGPL-3.0. The repo itself was also renamed from `claude-prompts` to `claude-prompts-mcp` (old links redirect); the link above and star/commit counts reflect the current repo.

**sparesparrow/mcp-prompts** (117 stars, up from 113, 328 commits) continued active development as a template manager for prompt CRUD, search, and discovery. 7 tools (`list_prompts`, `get_prompt`, `create_prompt`, `update_prompt`, `delete_prompt`, `apply_template`, `get_stats`) with variable substitution via a JSON-file store. **Correction (2026-08-16 audit):** this entry previously described the current release as "v3.14.0" with a default 3-backend (in-memory/filesystem/AWS) architecture, role-based access control, rate limiting, and Stripe payment integration. No v3.14.0 [GitHub release](https://github.com/sparesparrow/mcp-prompts/releases) or npm version exists — the [latest npm publish is v3.13.0](https://www.npmjs.com/package/@sparesparrow/mcp-prompts) (Dec 2025), while the `main` branch's `package.json` has moved on to an unreleased 4.0.0. More importantly, the [current README](https://github.com/sparesparrow/mcp-prompts/blob/main/README.md) shows the default server is now a simple local JSON-file store — it explicitly says "For enterprise features (AWS, multi-tenant, payments), see `archive/aws/README.md`. Most users don't need this." The AWS backend, RBAC, rate limiting, and Stripe integration described here are no longer part of the default server; they live in an archived, opt-in enterprise module.

**mikeskarl/mcp-prompt-templates** (24 stars) provides analysis-focused templates — meeting minutes generation, executive summaries, and webinar-to-blog-post conversion. Good for content teams with repeatable workflows.

**jezweb/smart-prompts-mcp** (12 stars, **archived December 2025**) fetched prompts from GitHub repositories with intelligent discovery, composition, and usage analytics. No longer maintained.

## Automated Prompt Optimization (7 servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [nivlewd1/prompt-optimizer](https://github.com/nivlewd1/prompt-optimizer) | 4 | JavaScript | — | 5 | Cloud Pro + Local Core, Bayesian tuning, 120+ domain rules |
| [Bubobot-Team/mcp-prompt-optimizer](https://github.com/Bubobot-Team/mcp-prompt-optimizer) | 24 | Python | MIT | 7 | 14 research-backed techniques (ToT, APE, Medprompt) |
| [hireshBrem/prompt-engineer-mcp-server](https://github.com/hireshBrem/prompt-engineer-mcp-server) | 13 | TypeScript | MIT | 1 | Claude-powered coding prompt rewriter |
| [andrea9293/mcp-gemini-prompt-enhancer](https://github.com/andrea9293/mcp-gemini-prompt-enhancer) | 2 | TypeScript | MIT | 1 | Gemini-based enhancement from Google's prompt engineering guide (archived) |
| [sloth-wq/prompt-auto-optimizer-mcp](https://github.com/sloth-wq/prompt-auto-optimizer-mcp) | 3 | TypeScript | MIT | 11 | Evolutionary optimization via GEPA method |
| [curiositech/prompt-learning-mcp](https://github.com/curiositech/prompt-learning-mcp) | 4 | TypeScript | MIT | 5 | APE, OPRO, DSPy patterns with embedding-based learning |
| [Nouman159/prompt-optimizer-mcp](https://github.com/Nouman159/prompt-optimizer-mcp) | 0 | Python | MIT | 2 | Deterministic heuristic optimization, sub-100ms |

**nivlewd1/prompt-optimizer** (4 stars on GitHub but featured on MCP marketplace) is the most commercially ambitious prompt optimization server. It ships as a **three-component ecosystem**: Cloud Pro (now v3.7.5) for LLM-powered optimization with Bayesian tuning and real-time streaming, Local Core (now v4.1.2) for offline processing with 120+ domain-specific rules, and a web dashboard for management and analytics. 5 MCP tools: `optimize_prompt` (professional enhancement), `detect_ai_context` (automatic intent recognition across code/images/research), `search_templates` (historical pattern browsing), `get_quota_status`, and `get_ce_quota_status`. Supports OpenRouter for model choice. **Correction (2026-08-16 audit):** this entry previously listed pricing as "Basic free (5 daily optimizations) or Pro ($19.99 one-time for unlimited)" and versions Cloud Pro v3.1.1 / Local Core v4.0.2. Re-checked against the [live product listing](https://github.com/nivlewd1/prompt-optimizer), both have changed: it's now a **subscription** model — Free (20 optimizations/month, no card required), Pro ($19/month, 500 optimizations plus full model configuration and Context Engineering access), and a custom-priced Enterprise tier — and the components have shipped several point releases since publication. Universal MCP compatibility with 17+ clients. The tiered approach — cloud LLM rewriting at 70-95% confidence, rules-based at <25%, local fallback at 35-55% — is pragmatic for teams that want optimization without always paying for API calls.

**Bubobot-Team/mcp-prompt-optimizer** (24 stars, up from 23) remains the most comprehensive open-source optimizer with **14 optimization techniques** — 6 basic (Clarity, Specificity, Chain of Thought, Few-Shot, Structured Output, Role-Based) and 8 advanced ([Tree of Thoughts](https://arxiv.org/abs/2305.10601) at 70-74% success rate, Constitutional AI, APE, Meta-Prompting, Self-Refine, TEXTGRAD, [Medprompt](https://arxiv.org/abs/2311.16452) at 90%+ classification accuracy, PromptWizard). 11 professional domain templates and automatic strategy selection. Python 3.8+, 7 tools.

**hireshBrem/prompt-engineer-mcp-server** (13 stars, unchanged) takes a simpler approach — one tool (`rewrite_coding_prompt`) that uses Claude 3 Sonnet at temperature 0.2 to rewrite coding prompts. Purpose-built for Cursor and AI IDEs. Appears stagnant (last commit March 2025).

**Correction (2026-08-16 audit):** this section previously included an entry for **MerabyLabs/promptarchitect-mcp** (workspace-aware prompt engineering, 5 stars, proprietary license). On re-verification the repository no longer resolves on GitHub (`404`), and the MerabyLabs GitHub org now lists only one unrelated public repo (a Space Engineers modding toolkit) — the promptarchitect-mcp project appears to have been taken down or made private since our April refresh, so we could no longer verify any of the original claims against a live source. The entry has been removed from this review.

**andrea9293/mcp-gemini-prompt-enhancer** (2 stars, **archived by its owner July 28, 2026**) used Google Gemini to optimize prompts based on [Google's prompt engineering guide](https://www.kaggle.com/whitepaper-prompt-engineering). One tool, `enhance_prompt`. No longer maintained.

**sloth-wq/prompt-auto-optimizer-mcp** (3 stars) uses the **GEPA method** — genetic algorithms applied to prompts. Population-based variant testing (20 variants default), multi-generation iteration (10 generations default), Pareto frontier analysis. 11 tools including failure analysis and backup/recovery.

**curiositech/prompt-learning-mcp** (4 stars, up from 1) implements **APE**, **OPRO**, and **DSPy** patterns with vector database storage, RAG-powered retrieval, and cold/warm-start modes. The most research-grounded approach, though adoption remains minimal.

**Nouman159/prompt-optimizer-mcp** (0 stars) offers deterministic, LLM-free optimization. 3 variants (Creative, Precise, Fast), sub-100ms response times.

## Claude Code & IDE-Specific Optimization (2+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [gr3enarr0w/cc_peng_mcp](https://github.com/gr3enarr0w/cc_peng_mcp) | 12 | JavaScript | MIT | 3 | Claude Code prompt engineering with Q&A refinement |
| [prompt-gen-mcp/prompt-gen-mcp](https://github.com/prompt-gen-mcp/prompt-gen-mcp) | 4 | Python | MIT | 3 | Code-context-aware prompt generation |

**gr3enarr0w/cc_peng_mcp** (12 stars) is built specifically for Claude Code. Three tools: `auto_optimize` (detects language and task type automatically), `engineer_prompt` (structured optimization), and `answer_questions` (Q&A-based clarification with session management). Recognizes 10+ programming languages and 5 task types. No external API keys required.

**prompt-gen-mcp/prompt-gen-mcp** (4 stars) scans your local codebase for context, then uses the PromptGen API and GROQ to transform simple questions into comprehensive, context-aware prompts. Code never leaves your machine (only metadata is sent). Integrates with Cursor.

## Prompt Security & Injection Protection (2+ servers) — NEW

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [General-Analysis/mcp-guard](https://github.com/General-Analysis/mcp-guard) | 55 | TypeScript | MIT | — | Runtime prompt injection firewall, AI-powered moderation |
| [ressl/mcp-firewall](https://github.com/ressl/mcp-firewall) | 10 | Python | AGPL-3.0 | — | 12-layer defense pipeline, compliance reporting |

This is the most significant gap filled since our initial review. Prompt injection protection went from zero MCP servers to two distinct approaches.

**General-Analysis/mcp-guard** (55 stars, MIT) is the **first runtime prompt injection firewall for MCP**. It acts as a proxy that aggregates multiple MCP servers into one secure interface, intercepting tool outputs and evaluating them through General Analysis's AI-powered moderation API before returning results to the client. Automatic configuration detection for Cursor, Claude Desktop, and Claude Code. Supports both local (stdio) and remote (HTTP/SSE) MCP servers. Transparent proxying of tools, prompts, and resources — your existing MCP setup works unchanged, with security layered on top. Enable with `ENABLE_GUARD_API=true` and a General Analysis API key. MIT license makes it easy to adopt.

**ressl/mcp-firewall** (10 stars, up from 5, AGPL-3.0) takes a more comprehensive policy-as-code approach with a **12-layer defense pipeline**: 8 inbound checks (kill switch, agent identity/RBAC, rate limiting, injection detection, egress control, OPA/Rego policy engine, dangerous tool sequence detection, human approval gates) and 4 outbound checks (secret scanning, PII detection, exfiltration detection, custom content policies). Includes cryptographically signed audit trails, real-time dashboard, and compliance reporting for DORA, FINMA, and SOC 2. Started as a single commit (initial v0.1.0 release, February 2026); a second commit landed August 7, 2026 addressing findings from a self-reported 40-item security review. Still early but architecturally ambitious. Commercial licensing available alongside AGPL.

## Prompt Observability & Analytics (3 platforms) — NEW

| Platform | Type | Key Feature |
|----------|------|-------------|
| [Langfuse native MCP](https://langfuse.com/docs/api-and-data-platform/features/mcp-server) | Hosted | 5 tools, read+write, StreamableHttp, no setup |
| [Helicone MCP](https://docs.helicone.ai/integrations/tools/mcp) | Official | query_requests + query_sessions, request/response debugging |
| [Braintrust MCP](https://www.braintrust.dev/docs/integrations/developer-tools/mcp) | Official hosted | api.braintrust.dev/mcp, OAuth 2.0, SQL-style log queries |

In our initial review, Langfuse was the only observability platform with MCP integration. Now there are three, and the gap we identified is **partially filled**.

**Helicone** launched an official MCP server (`@helicone/mcp` on npm) with 2 tools: `query_requests` (search with filtering by model, provider, status, latency, cost, properties, time, user) and `query_sessions` (time range filtering, search, advanced filters). Enables debugging errors, searching logs, and analyzing performance without leaving your AI assistant.

**Braintrust** launched a hosted MCP server at `api.braintrust.dev/mcp` (EU: `api-eu.braintrust.dev/mcp`) with OAuth 2.0 authentication. Tools include documentation search, experiment summaries, BTQL queries, object resolution, schema analysis, and permalink generation. Considered the most mature IDE-native observability MCP by multiple reviewers. Works with Claude Code, Cursor, VS Code, and Windsurf.

Still missing from the MCP prompt observability landscape: **PromptLayer**, **Arize Phoenix**, and **Weights & Biases**.

## Structured Prompt Frameworks (1+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [doritoman90000/risen-prompts-mcp](https://github.com/doritoman90000/risen-prompts-mcp) | 1 | JavaScript | MIT | 8 | RISEN framework (Role, Instructions, Steps, Expectations, Narrowing) |

**doritoman90000/risen-prompts-mcp** (1 star) implements the **RISEN framework** — a structured approach that decomposes prompts into 5 components: Role (AI persona), Instructions (task directives), Steps (process breakdown), Expectations (desired outcomes), and Narrowing (constraints). 8 tools cover template creation, validation, storage, and natural-language-to-RISEN conversion. Quality scoring rates templates out of 100 across 5 dimensions (20 points each). Also supports A/B testing and performance tracking. Low adoption but a solid structured approach for teams that want consistent prompt quality.

## What's Missing

The prompt engineering MCP ecosystem has narrowed its gaps since March, but several remain:

- ~~**No prompt security/injection detection**~~ — **FILLED.** MCP Guard (55 stars, MIT) provides runtime prompt injection protection; MCP Firewall adds 12-layer defense with compliance reporting
- ~~**Limited observability integration**~~ — **PARTIALLY FILLED.** Was Langfuse only; now Langfuse (native 5-tool MCP with write), Helicone (official), and Braintrust (official hosted) all have MCP servers. Still no PromptLayer, Arize Phoenix, or Weights & Biases
- **No prompt A/B testing infrastructure** — sloth-wq's GEPA method and Braintrust's experiment features are the closest, but no dedicated experimentation platform MCP server exists
- **No prompt cost estimation** — no server helps estimate token costs before sending prompts to expensive models
- **No prompt chain debugging** — no server lets you step through a multi-step prompt chain and inspect intermediate results
- **No prompt versioning with rollback** — Langfuse native MCP now has label-based versioning (production/staging), but true rollback workflows are still absent

## The Bottom Line

This is a **3.5/5** category — holding steady, though the ecosystem is maturing in important ways. Star growth since April has been uneven — just-prompt +2%, mcp-prompts +4%, but claude-prompts-mcp +27% (147→186 stars) — and most optimization tools remain under 25 stars. But the structural improvements are real: prompt injection protection went from zero to two servers, observability expanded from one platform to three, and Langfuse's native MCP with write capabilities is a meaningful step toward production prompt management via MCP.

The standout servers serve different needs: **just-prompt** (737 stars) for multi-LLM routing, **Langfuse native MCP** (5 tools with read+write) for production prompt management, **claude-prompts-mcp** (186 stars) for workflow composition with reasoning frameworks, **mcp-prompts** (117 stars) for template management, **MCP Guard** (55 stars) for prompt injection protection, and **mcp-prompt-optimizer** (24 stars) for research-backed optimization techniques.

For most users, your AI agent's built-in prompt handling is probably sufficient. These servers become valuable when you're managing prompt libraries at scale, need to route across LLM providers, want to apply specific optimization techniques systematically, or need to protect against prompt injection attacks in production.

**Start here:** If you want multi-LLM routing, use [just-prompt](https://github.com/disler/just-prompt). If you want production prompt management with versioning, use Langfuse's native MCP. If you want workflow composition with reasoning frameworks, use [claude-prompts-mcp](https://github.com/minipuft/claude-prompts-mcp). If you need template management, use [mcp-prompts](https://github.com/sparesparrow/mcp-prompts). If you want prompt injection protection, use [MCP Guard](https://github.com/General-Analysis/mcp-guard). If you want research-backed optimization, use [mcp-prompt-optimizer](https://github.com/Bubobot-Team/mcp-prompt-optimizer).

This review was originally published 2026-03-16, refreshed 2026-04-28, and re-audited claim-by-claim on 2026-08-16 using Claude Sonnet 5 (Anthropic). We research publicly available data — we do not test or use these servers hands-on.

