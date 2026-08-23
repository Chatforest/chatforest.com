---
title: "Survey & Forms MCP Servers — Qualtrics, Tally, Typeform, Jotform, Google Forms, and More"
date: 2026-04-26T23:00:00+09:00
description: "Survey and forms MCP servers reviewed: SurveyMonkey official MCP (May 2026), Qualtrics community (32 stars, 112 tools across 14 API areas), Tally official (20+ tools, free, safety-first), Typeform official (beta, OAuth, 50+ documented tools) + community (47 tools), Jotform official (6 tools, OAuth, hosted), Google Forms community (multiple servers including google_workspace_mcp ~3.1K stars), survey-mcp-server (8 tools, skip logic, pluggable storage), SurveyMars official (1 tool), Weavely (AI form generation). Rating: 3.0/5."
og_description: "Survey & forms MCP servers: SurveyMonkey official (May 2026), Qualtrics (112 tools), Tally (20+ tools, free), Typeform (beta + community 47 tools), Jotform (6 tools), Google Forms (community), survey-mcp-server (skip logic). Rating: 3.0/5."
content_type: "Review"
card_description: "Survey and forms MCP servers are a maturing category. SurveyMonkey launched an official Claude MCP integration in May 2026, closing the biggest gap. Qualtrics has the deepest integration through a community server with 112 tools spanning surveys, survey design, questions, blocks, survey flow, quotas, responses, contacts, distributions, libraries, survey import, webhooks, users, and an advanced JSON API escape hatch. Tally is the standout free option with 20+ official MCP tools, unlimited forms, OAuth authentication, and a safety-first design that prevents AI from deleting forms. Jotform ships an official hosted MCP at mcp.jotform.com with OAuth 2.0 and 6 tools covering form creation, editing, submissions, and assignment. Typeform offers a beta official MCP now documenting 50+ tools across form building, automations, contacts, and response analysis, via OAuth, plus a community server exposing 47 tools across forms, responses, webhooks, themes, images, workspaces, and translations. Google Forms has no official MCP but multiple community servers exist, with the google_workspace_mcp (~3.1K stars) providing Forms alongside 11 other Google services. The standalone survey-mcp-server offers 8 tools for conducting AI-driven conversational surveys with skip logic, session resume, and pluggable storage backends including Supabase and Cloudflare KV. Notable gaps: no Microsoft Forms dedicated server, no Hotjar/Survicate/SurveySparrow MCP servers, and most community servers have very low adoption. Rating: 3.0/5 — adequate platform coverage led by SurveyMonkey's official integration and Qualtrics community depth, but low maturity overall."
last_refreshed: 2026-08-23
sources_audited: 2026-08-23
---

Survey and forms platforms are among the most widely used SaaS tools — from customer feedback and market research to academic studies and internal data collection. MCP servers in this space let AI agents create forms, manage questions, distribute surveys, and analyze responses through natural language. The ecosystem is fragmented: a few platforms have invested in official MCP servers while most rely on community implementations of varying quality. Part of our **[Productivity & Office MCP category](/categories/productivity-office/)**.

This review covers **enterprise research platforms** (Qualtrics), **modern form builders** (Tally, Typeform, Jotform), **Google Forms** community servers, **AI-native survey tools** (survey-mcp-server, SurveyMars, Weavely), and the broader landscape of form-adjacent MCP access through workspace integrations. For CRM-related form handling, see our [CRM MCP Servers](/reviews/crm-mcp-servers/) review. For marketing forms and lead capture, see [Marketing Automation MCP Servers](/reviews/marketing-automation-mcp-servers/).

The headline finding: [**SurveyMonkey launched an official Claude MCP integration in May 2026**](https://www.surveymonkey.com/newsroom/surveymonkey-claude-ai-integration/), closing the category's biggest gap. **Qualtrics has the deepest integration** with 112 tools, but it's community-built. **Tally is the best free option** with official MCP, unlimited forms, and safety guardrails. **Typeform's official MCP is still beta**, though (as of this audit) it now documents 50+ tools and uses OAuth; a community server also fills the gap with 47 tools. **Google Forms has no official MCP** despite being the most-used form tool globally. **Most servers have very low star counts**, reflecting how early this category still is.

## Enterprise Research Platforms

### Qualtrics

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| qualtrics-mcp-server (yrvelez) | ~32 | TypeScript | MIT | 112 tools | No |

**Qualtrics MCP** ([yrvelez/qualtrics-mcp-server](https://github.com/yrvelez/qualtrics-mcp-server), 32 stars, MIT, TypeScript) is the most comprehensive survey MCP server available. It exposes **112 tools** (110 Qualtrics action tools across 14 API areas, plus 2 server-permission controls), giving full control over the Qualtrics platform through natural language:

*Correction (2026-08-23): this server has grown substantially since our original write-up. At initial review it had 19 stars and 53 tools across 8 domains; the repository's current [README](https://github.com/yrvelez/qualtrics-mcp-server/blob/main/README.md) now documents 112 tools across the areas below, and stars have grown to 32.*

- **Surveys (8 tools)** — list, get, create, update, delete, activate, deactivate, estimate export size
- **Survey design (11 tools)** — metadata, merged options, versions, enabled languages, translations
- **Questions (13 tools)** — raw CRUD plus helpers for multiple-choice, text entry, descriptive text, Likert, matrix, rank order, and constant-sum questions, and reusable templates
- **Blocks (5 tools)** — list, get, create, update (full definitions), delete
- **Survey flow (12 tools)** — full-tree get/replace, insert/update/move/delete nested elements, validation, embedded data, web services, piped text
- **Quotas (10 tools)** — CRUD for quotas and quota groups
- **Responses (8 tools)** — streamed full/filtered export, export status/download, individual response create/get/delete, queued embedded-data update
- **Contacts (12 tools)** — directory discovery, mailing-list and contact CRUD, cursor pagination, bounded bulk import
- **Distributions (9 tools)** — listing/details/links, delivery history, anonymous links, invitations, reminders, thank-yous, deletion
- **Libraries (11 tools)** — reusable survey assets, multilingual messages, graphic upload/delete
- **Survey import and copy (5 tools)** — survey copy plus QSF, TXT, URL, and base64 DOCX imports
- **Webhooks (3 tools)** — list, create, delete
- **Users (2 tools)** — list and get users
- **Advanced API (1 tool)** — guarded JSON requests to other Qualtrics API v3 endpoints
- **Server control (2 tools)** — least-privilege write-scope toggling and a `set_read_only_mode`-style read-only switch

This is a community server, not official from Qualtrics. It requires a Qualtrics API token and Data Center ID. The rate limiting and timeout controls are configurable. Qualtrics pricing starts at enterprise tiers, so this MCP is primarily relevant for organizations already using the platform for experience management, academic research, or large-scale CX programs.

A second community implementation (ederbuug/qualtrics-mcp, Python) exists for interacting with surveys, libraries, messages, and SMS distributions.

## Modern Form Builders

### Tally (Official)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| Tally MCP (official) | — | Remote | — | 20+ tools | Yes |
| tally-mcp (learnwithcc) | ~8 | TypeScript | ISC | 10+ tools | No |

**Tally** ([tally.so/help/mcp](https://tally.so/help/mcp)) is the standout in this category — the **only form builder offering a free, full-featured official MCP server** with no plan restrictions. Key details:

- **20+ MCP tools** for form creation, editing, workspace browsing, submission fetching, and data analysis
- [**Free on all plans**](https://tally.so/help/mcp) including the free tier — unlimited forms, unlimited responses
- **OAuth authentication** with a roughly [60-second setup](https://tally.so/help/mcp) (*Correction (2026-08-23): originally reported as a "2-minute setup" — Tally's own walkthrough describes the OAuth connect flow as taking about 60 seconds*)
- **Safety guardrail**: AI **cannot delete forms or submissions** — a deliberate design choice, confirmed on [tally.so/help/mcp](https://tally.so/help/mcp)
- Works with Claude Desktop, claude.ai, Claude Code, ChatGPT, Cursor, and any MCP-compatible client

The community server **tally-mcp** ([learnwithcc/tally-mcp](https://github.com/learnwithcc/tally-mcp), 8 stars, ISC, TypeScript) provides an alternative with a three-step safety workflow for bulk operations (preview → confirm → execute), Cloudflare Workers deployment, and 90% test coverage (all confirmed current in the repo as of 2026-08-23). Tools include `create_form`, `modify_form`, `get_form`, `list_forms`, `delete_form`, `get_submissions`, `analyze_submissions`, `share_form`, `manage_workspace`, and `manage_team`. *Note (2026-08-23): this repository is now archived by its maintainer (read-only, no longer actively developed) — treat it as a snapshot rather than a maintained option.*

### Typeform (Beta Official + Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| Typeform MCP (official) | — | Remote | — | 50+ tools | Yes (beta) |
| typeform-mcp (dscovr) | ~0 | Python | MIT | 47 tools | No |

**Typeform's official MCP** ([help.typeform.com](https://help.typeform.com/hc/en-us/articles/47604941815700-Connect-Claude-to-the-Typeform-MCP-server-beta)) is in beta but has matured since our original write-up. Current status, verified against Typeform's developer docs ([typeform.com/developers/get-started/mcp](https://www.typeform.com/developers/get-started/mcp/)):

- Supports Claude and other MCP-compatible clients (Cursor, ChatGPT) via a generally-available beta connector
- **Authentication is now OAuth** — connect and grant access with the required scopes; no Personal Access Token step is documented
- **Tool list is now published**: a documented set of 50+ tools spanning building/editing forms, building/managing automations, read-write contacts access, and analyzing form responses
- Access to specific tools/actions is gated by your Typeform subscription plan
- Free tier limited to 10 responses/month (cut from 100/month in a February 2026 pricing change); paid plans $39–$129+/month billed monthly ($28–$91+/month billed annually)

*Correction (2026-08-23): at initial writing, Typeform's official MCP was described here as PAT-authenticated with an undocumented tool list. Typeform's developer docs now show OAuth authentication and a published tool list (50+ tools) — see [typeform.com/developers/get-started/mcp](https://www.typeform.com/developers/get-started/mcp/).*

The community server **typeform-mcp** ([dscovr/typeform-mcp](https://github.com/dscovr/typeform-mcp), Python, MIT, created March 2026) fills the gap with **47 tools across 8 categories**:

- **Forms (8)** — list, get, create, update, patch, delete, duplicate, get/update messages
- **Responses (4)** — list, export CSV, delete, download file
- **Webhooks (4)** — list, get, upsert, delete
- **Themes (6)** — full CRUD plus patching
- **Images (4)** — list, get, create, delete
- **Workspaces (5)** — full CRUD
- **Translations (5)** — list, get status, update, delete, auto-translate
- **Account (1)** — get account info

Requires Python 3.12+ and a Typeform Personal Access Token. This community server has 11 commits and 0 stars — very early adoption.

### Jotform (Official)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| Jotform MCP (official) | ~27 | — | MIT | 6 tools | Yes |

**Jotform** ([jotform/mcp-server](https://github.com/jotform/mcp-server), 27 stars, MIT) ships an official hosted MCP server at `mcp.jotform.com` — no local installation required. Tools:

- `list_forms` — browse existing forms
- `create_form` — build new forms via natural language
- `edit_form` — modify live forms
- `create_submission` — add form submissions
- `get_submissions` — query submission data
- `assign_form` — assign forms to team members

Authentication is **OAuth 2.0 only** (bearer tokens not supported). Rate limits are 60 requests/minute on the free tier, 600/minute on Enterprise. Access can be revoked via the Jotform dashboard. Jotform says more tools are in development.

Jotform's free tier allows 5 forms and 100 submissions/month. Paid plans range from $34–$99+/month.

A community alternative ([The-AI-Workshops/jotform-mcp-server](https://github.com/The-AI-Workshops/jotform-mcp-server)) wraps the Jotform Python client for those who prefer local execution.

## Google Forms

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| google_workspace_mcp | ~3,050 | Python | MIT | Forms + 11 services | No |
| google-forms-mcp (matteoantoci) | ~17 | JavaScript | — | 5 tools | No |
| mcp-server-google-forms (HosakaKeigo) | ~0 | TypeScript | MIT | 3 tools | No |
| google-forms-mcp (delorenj) | — | — | — | — | No |
| google-forms-mcp (udecode) | — | — | — | — | No |
| google-form-mcp-server (adarshp14) | — | — | — | — | No |

**Google Forms has no official MCP server.** Google announced MCP support for several Cloud services in 2025, but Google Forms was not included. Multiple community implementations exist, with varying levels of maturity.

The best path to Google Forms MCP access is through **google_workspace_mcp** ([taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp), ~3,050 stars as of this audit — up from 2,700 at original writing — MIT, Python) — a comprehensive Google Workspace server covering 12 services including Forms. Forms capabilities include creation, publish settings, and response management alongside Gmail, Calendar, Drive, Docs, Sheets, Slides, Tasks, Contacts, Chat, and Search. Available on PyPI as `workspace-mcp`. This is the **highest-adoption server in this entire review** by a wide margin, though Forms is just one of its many services.

**google-forms-mcp** ([matteoantoci/google-forms-mcp](https://github.com/matteoantoci/google-forms-mcp), 17 stars as of this audit — up from 11 — JavaScript) is the most popular Forms-dedicated server with 5 tools: `create_form`, `add_text_question`, `add_multiple_choice_question`, `get_form`, `get_form_responses`. Uses OAuth 2.0.

**mcp-server-google-forms** ([HosakaKeigo/mcp-server-google-forms](https://github.com/HosakaKeigo/mcp-server-google-forms), TypeScript, MIT, 85 commits) provides `create_form`, `get_form`, and `batch_update_form` for multi-operation requests. Supports quiz creation. Uses Application Default Credentials. Pending features include image/video items, scale/date/time questions, file uploads, and rating questions.

## AI-Native Survey Tools

These servers are not wrappers around existing platforms — they provide standalone survey capabilities designed for AI-first workflows.

### survey-mcp-server

| Server | Stars | Language | License | Tools | Transport |
|--------|-------|----------|---------|-------|-----------|
| survey-mcp-server (cyanheads) | ~4 | TypeScript | Apache 2.0 | 8 tools | HTTP + stdio |

**survey-mcp-server** ([cyanheads/survey-mcp-server](https://github.com/cyanheads/survey-mcp-server), 4 stars, Apache 2.0, TypeScript) transforms LLMs into intelligent interviewers. Rather than managing external survey platforms, it **conducts surveys natively** through the AI conversation. Features:

- **8 tools**: `survey_list_available`, `survey_start_session`, `survey_get_question`, `survey_submit_response`, `survey_get_progress`, `survey_complete_session`, `survey_export_results`, `survey_resume_session`
- **Question types**: free-form, multiple-choice, rating scales, email, numbers, booleans, dates, matrices
- **Conditional logic**: AND/OR multi-condition branching with eligibility tracking
- **Session management**: pause/resume with state persistence
- **Scoring**: optional point-based assessments
- **Validation**: min/max constraints, pattern matching, required fields
- **Export**: CSV and JSON formats

**Pluggable storage backends**: in-memory, filesystem, Supabase, Cloudflare KV, Cloudflare R2. Multi-tenant architecture with JWT/OAuth/none authentication options. Edge-deployable on Cloudflare Workers. Built on Bun v1.3.0+ with 67.82% test coverage. Last updated October 2025.

### SurveyMars (Official)

**SurveyMars** ([surveymars/surveymars-mcp](https://github.com/surveymars/surveymars-mcp), Python) is an official MCP server for the SurveyMars platform. Currently minimal — **1 tool** (`survey_create`). Requires SurveyMars Account ID and Secret Key. 3 commits, 0 stars. *Correction (2026-08-23): previously stated as "last updated January 2025" — the repository's commit history shows its 3 commits all date to April 17–18, 2025; corrected here.*

### Weavely

**Weavely** ([weavely/mcp](https://github.com/weavely/mcp), TypeScript) generates forms and surveys using the Weavely AI API. **1 tool** (`create-form`) that sends prompts to `api.weavely.ai/v1/forms/generate`. Deploys on Cloudflare Workers. 2 commits, 0 stars. Minimal but represents the AI-generated forms pattern.

## Microsoft Forms

Microsoft Forms has **no dedicated MCP server**, but access is available through broader Microsoft 365 MCP integrations:

- **Softeria/ms-365-mcp-server** — 300+ tools covering the Microsoft Graph API surface, including Forms (up from 200+ at original writing, per the project's current [README](https://github.com/Softeria/ms-365-mcp-server))
- **Aanerud/MCP-Microsoft-Office** — 117 tools across 12 modules (Mail, Calendar, Files, Excel, Word, PowerPoint, Teams, Contacts, To-Do, Groups, People, Search)
- **pnp/cli-microsoft365-mcp-server** — execute any CLI for Microsoft 365 command via natural language

None of these servers have dedicated Forms tools — access is through the broader Microsoft Graph API. See our [Spreadsheet & Office Suite MCP Servers](/reviews/spreadsheet-office-suite-mcp-servers/) review for more Microsoft 365 coverage.

## SurveyMonkey (Official — May 2026)

**SurveyMonkey** launched an [**official MCP connector for Claude in May 2026**](https://www.surveymonkey.com/newsroom/surveymonkey-claude-ai-integration/) (independently confirmed by trade press: [CMSWire](https://www.cmswire.com/customer-experience/surveymonkey-embeds-survey-creation-and-analysis-inside-claude/)), closing the biggest gap in this category. The integration enables users to create and send surveys, analyze responses, and surface patterns in Claude conversations directly. SurveyMonkey announced the integration as part of a broader Claude AI partnership, positioning it as a way for researchers and marketers to work with survey data through natural language rather than the SurveyMonkey dashboard. The connector is available to SurveyMonkey customers on Basic plans and above, authenticates via OAuth, and — per CMSWire — does not support editing surveys that are already live and collecting responses.

This is a significant development — SurveyMonkey is the second-most popular survey platform globally, and its absence was previously the most notable gap in this category. Note that the integration was announced through a partnership announcement rather than an open-source GitHub repository; the MCP connector may be hosted/managed rather than self-hosted.

## What's Missing

The survey and forms MCP ecosystem has significant gaps:

- **SurveyMonkey** — now has an official MCP connector (May 2026), but it appears to be a managed/hosted integration rather than an open-source server
- **Hotjar / Survicate / SurveySparrow** — no MCP servers for any major website feedback and in-app survey tools
- **Alchemer (SurveyGizmo)** — no MCP server despite enterprise research focus
- **Qualaroo** — no MCP server for on-site survey widgets
- **Gravity Forms / WPForms** — no MCP servers for major WordPress form plugins
- **Formstack / FormAssembly / Cognito Forms** — no MCP servers (only available through Zapier/CData middleware)
- **Google Forms official support** — most-used form tool globally with no first-party MCP
- **Response analytics** — most servers focus on form creation and submission retrieval, with minimal built-in analysis capabilities (Tally and Qualtrics are exceptions)
- **A/B testing** — no MCP server supports form variant testing
- **NPS/CSAT specialized tools** — no dedicated Net Promoter Score or customer satisfaction MCP tools

## Rating: 3.0 / 5

The survey and forms MCP ecosystem is **functional but maturing**. Qualtrics has the deepest integration at 112 tools, but it's community-built and limited to enterprise Qualtrics customers. Tally stands out as the only form builder offering a genuinely free, full-featured official MCP with safety guardrails. Jotform has a clean official implementation. Typeform is beta, though its tool list (50+ tools) is now documented. Google Forms relies entirely on community servers. The **May 2026 SurveyMonkey official MCP** closes the category's biggest gap.

**Strengths**: Qualtrics community server depth, Tally's free official MCP with safety design, Jotform's hosted OAuth model, SurveyMonkey's official Claude integration (May 2026), Google Workspace MCP providing Forms alongside 11 other services, survey-mcp-server's AI-native approach with pluggable backends.

**Weaknesses**: Most servers have under 20 stars, no feedback/NPS tools, Typeform's connector is still labeled beta and plan-gated even though its tool list is now documented, Google Forms fragmented across 5+ competing community servers with no clear winner, minimal analytics capabilities, SurveyMonkey integration appears managed rather than open-source.
