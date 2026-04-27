# Survey & Forms MCP Servers — Qualtrics, Tally, Typeform, Jotform, Google Forms, and More

> Survey and forms MCP servers reviewed: Qualtrics community (17 stars, 53 tools across 8 domains), Tally official (20+ tools, free, safety-first), Typeform official (beta, PAT auth) + community (47 tools), Jotform official (24 stars, 6 tools, OAuth, hosted), Google Forms community (multiple servers including google_workspace_mcp 2.2K stars), survey-mcp-server (8 tools, skip logic, pluggable storage), SurveyMars official (1 tool), Weavely (AI form generation). Rating: 3.0/5.


Survey and forms platforms are among the most widely used SaaS tools — from customer feedback and market research to academic studies and internal data collection. MCP servers in this space let AI agents create forms, manage questions, distribute surveys, and analyze responses through natural language. The ecosystem is fragmented: a few platforms have invested in official MCP servers while most rely on community implementations of varying quality. Part of our **[Productivity & Office MCP category](/categories/productivity-office/)**.

This review covers **enterprise research platforms** (Qualtrics), **modern form builders** (Tally, Typeform, Jotform), **Google Forms** community servers, **AI-native survey tools** (survey-mcp-server, SurveyMars, Weavely), and the broader landscape of form-adjacent MCP access through workspace integrations. For CRM-related form handling, see our [CRM MCP Servers](/reviews/crm-mcp-servers/) review. For marketing forms and lead capture, see [Marketing Automation MCP Servers](/reviews/marketing-automation-mcp-servers/).

The headline finding: **Qualtrics has the deepest MCP integration** with 53 tools, but it's community-built. **Tally is the best free option** with official MCP, unlimited forms, and safety guardrails. **Typeform's official MCP is still beta** with limited documentation, while a community server fills the gap with 47 tools. **Google Forms has no official MCP** despite being the most-used form tool globally. **SurveyMonkey has no MCP server at all** — only third-party middleware like Zapier MCP. **Most servers have very low star counts**, reflecting how early this category is.

## Enterprise Research Platforms

### Qualtrics

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| qualtrics-mcp-server (yrvelez) | ~17 | TypeScript | MIT | 53 tools | No |

**Qualtrics MCP** ([yrvelez/qualtrics-mcp-server](https://github.com/yrvelez/qualtrics-mcp-server), 17 stars, MIT, TypeScript) is the most comprehensive survey MCP server available. It exposes **53 tools across 8 domains**, giving full control over the Qualtrics platform through natural language:

- **Surveys (8 tools)** — list, get, create, update, delete, activate, deactivate, estimate export size
- **Questions (7 tools)** — list, get, create, update, delete, plus helpers for multiple-choice, text entry, and matrix questions
- **Blocks (4 tools)** — list, create, update, delete survey blocks
- **Survey Flow (7 tools)** — get/update flow, add embedded data, add web services, list embedded data, list web services, piped text reference
- **Responses (7 tools)** — export (full and filtered), check export status, get/create/update/delete individual responses
- **Contacts (7 tools)** — mailing list CRUD, contact management, bulk import
- **Distributions (5 tools)** — list, get, delete, create anonymous links, create email distributions, create reminders
- **Webhooks (3 tools)** — list, create, delete
- **Users (2 tools)** — list and get users
- **Safety** — includes a `set_read_only_mode` tool for restricting to read-only operations

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
- **Free on all plans** including the free tier — unlimited forms, unlimited responses
- **OAuth authentication** with a 2-minute setup process
- **Safety guardrail**: AI **cannot delete forms or submissions** — a deliberate design choice
- Works with Claude Desktop, claude.ai, Claude Code, ChatGPT, Cursor, and any MCP-compatible client

The community server **tally-mcp** ([learnwithcc/tally-mcp](https://github.com/learnwithcc/tally-mcp), 8 stars, ISC, TypeScript) provides an alternative with a three-step safety workflow for bulk operations (preview → confirm → execute), Cloudflare Workers deployment, and 90% test coverage. Tools include `create_form`, `modify_form`, `get_form`, `list_forms`, `delete_form`, `get_submissions`, `analyze_submissions`, `share_form`, `manage_workspace`, and `manage_team`.

### Typeform (Beta Official + Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| Typeform MCP (official) | — | Remote | — | Undocumented | Yes (beta) |
| typeform-mcp (dscovr) | ~0 | Python | MIT | 47 tools | No |

**Typeform's official MCP** ([help.typeform.com](https://help.typeform.com/hc/en-us/articles/47604941815700-Connect-Claude-to-the-Typeform-MCP-server-beta)) is in beta with limited public documentation. Current status:

- Supports Claude and Cursor
- Authentication via Personal Access Token (OAuth planned)
- Tool list is not publicly documented — users must ask their AI assistant to list available actions
- Typeform advises that tools and setup will change as the beta evolves
- Free tier limited to 10 responses/month; paid plans $39–$129+/month

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
| Jotform MCP (official) | ~24 | — | MIT | 6 tools | Yes |

**Jotform** ([jotform/mcp-server](https://github.com/jotform/mcp-server), 24 stars, MIT) ships an official hosted MCP server at `mcp.jotform.com` — no local installation required. Tools:

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
| google_workspace_mcp | ~2,200 | Python | MIT | Forms + 11 services | No |
| google-forms-mcp (matteoantoci) | ~11 | JavaScript | — | 5 tools | No |
| mcp-server-google-forms (HosakaKeigo) | ~0 | TypeScript | MIT | 3 tools | No |
| google-forms-mcp (delorenj) | — | — | — | — | No |
| google-forms-mcp (udecode) | — | — | — | — | No |
| google-form-mcp-server (adarshp14) | — | — | — | — | No |

**Google Forms has no official MCP server.** Google announced MCP support for several Cloud services in 2025, but Google Forms was not included. Multiple community implementations exist, with varying levels of maturity.

The best path to Google Forms MCP access is through **google_workspace_mcp** ([taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp), 2,200 stars, MIT, Python) — a comprehensive Google Workspace server covering 12 services including Forms. Forms capabilities include creation, publish settings, and response management alongside Gmail, Calendar, Drive, Docs, Sheets, Slides, Tasks, Contacts, Chat, and Search. Available on PyPI as `workspace-mcp`. This is the **highest-adoption server in this entire review** by a wide margin, though Forms is just one of its many services.

**google-forms-mcp** ([matteoantoci/google-forms-mcp](https://github.com/matteoantoci/google-forms-mcp), 11 stars, JavaScript) is the most popular Forms-dedicated server with 5 tools: `create_form`, `add_text_question`, `add_multiple_choice_question`, `get_form`, `get_form_responses`. Uses OAuth 2.0.

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

**SurveyMars** ([surveymars/surveymars-mcp](https://github.com/surveymars/surveymars-mcp), Python) is an official MCP server for the SurveyMars platform. Currently minimal — **1 tool** (`survey_create`). Requires SurveyMars Account ID and Secret Key. 3 commits, 0 stars. Last updated January 2025.

### Weavely

**Weavely** ([weavely/mcp](https://github.com/weavely/mcp), TypeScript) generates forms and surveys using the Weavely AI API. **1 tool** (`create-form`) that sends prompts to `api.weavely.ai/v1/forms/generate`. Deploys on Cloudflare Workers. 2 commits, 0 stars. Minimal but represents the AI-generated forms pattern.

## Microsoft Forms

Microsoft Forms has **no dedicated MCP server**, but access is available through broader Microsoft 365 MCP integrations:

- **Softeria/ms-365-mcp-server** — 200+ tools covering the Microsoft Graph API surface, including Forms
- **Aanerud/MCP-Microsoft-Office** — 117 tools across 12 modules (Mail, Calendar, Files, Excel, Word, PowerPoint, Teams, Contacts, To-Do, Groups, People, Search)
- **pnp/cli-microsoft365-mcp-server** — execute any CLI for Microsoft 365 command via natural language

None of these servers have dedicated Forms tools — access is through the broader Microsoft Graph API. See our [Spreadsheet & Office Suite MCP Servers](/reviews/spreadsheet-office-suite-mcp-servers/) review for more Microsoft 365 coverage.

## What's Missing

The survey and forms MCP ecosystem has significant gaps:

- **SurveyMonkey** — the second-most popular survey platform has **no MCP server**. Only accessible through third-party middleware: Zapier MCP (action wrapper), CData (read-only SQL connector), Composio, and viaSocket
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

The survey and forms MCP ecosystem is **functional but immature**. Qualtrics has the deepest integration at 53 tools, but it's community-built and limited to enterprise Qualtrics customers. Tally stands out as the only form builder offering a genuinely free, full-featured official MCP with safety guardrails. Jotform has a clean official implementation but with only 6 tools. Typeform is beta with undocumented tools. Google Forms relies entirely on community servers. The most popular survey platform (SurveyMonkey) has no MCP presence at all.

**Strengths**: Qualtrics community server depth, Tally's free official MCP with safety design, Jotform's hosted OAuth model, Google Workspace MCP providing Forms alongside 11 other services, survey-mcp-server's AI-native approach with pluggable backends.

**Weaknesses**: Most servers have under 20 stars, SurveyMonkey completely absent, no feedback/NPS tools, Typeform beta is underdocumented, Google Forms fragmented across 5+ competing community servers with no clear winner, minimal analytics capabilities.

