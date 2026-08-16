# HR & Recruiting MCP Servers — BambooHR, Workday, Greenhouse, Workable, Payroll, ATS, and More

> HR and recruiting MCP servers are giving AI assistants direct access to employee data, applicant tracking, payroll, and workforce management.


HR and recruiting MCP servers are giving AI assistants direct access to employee data, applicant tracking, payroll processing, and workforce management. Instead of navigating clunky HR portals, these servers let AI agents query employee records, manage job applications, run payroll reports, and coordinate hiring workflows — all through the Model Context Protocol. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

The landscape spans six areas: **HRIS platforms** (BambooHR, Workday, SAP SuccessFactors, Rippling, and more), **applicant tracking systems** (Workable, Greenhouse, Ashby, CATS ATS), **payroll and benefits** (Check, Deel, ADP), **workforce management** (Passgage), **recruiting intelligence** (CareerProof, Recruitin), and **HR agent tools** (bias reduction, voice interviewing, onboarding kits).

The headline findings: **Workable launched an official hosted MCP server** ([May 13, 2026](https://www.globenewswire.com/news-release/2026/05/13/3293876/0/en/workable-launches-mcp-server-for-ai-powered-recruiting-and-hr-workflows.html)) at `mcp.workable.com` with 38 tools at launch spanning both ATS and HRIS — candidates, jobs, offers, requisitions, employees, time off, time tracking, and performance reviews. Read/write access. OAuth2 auth. Included in all plans at no extra cost. By [July 20, 2026, Workable had expanded the server to 94 tools](https://www.globenewswire.com/news-release/2026/07/20/3329974/0/en/workable-expands-mcp-server-to-94-tools-extending-ai-assistant-access-across-the-full-hiring-and-hr-lifecycle.html), adding advanced candidate/employee search, the full performance-review lifecycle, and account administration. This is the most comprehensive official ATS+HRIS MCP launch to date. **Indeed launched an official MCP server** (beta) at [mcp.indeed.com](https://docs.indeed.com/mcp) with job search, job detail, resume, and company data tools (4 tools as of this audit) — the first major job board with official MCP support. **Lever's Go server remains the more complete option**; the community TypeScript/Cloudflare server (the-sid-dani/lever-mcp-server) has since been deleted from GitHub (404 as of this audit), leaving the [59-tool Go server](https://github.com/stefanoamorelli/lever-mcp) as the sole surviving Lever implementation. **Check Payroll remains the highest-starred HR MCP server** at 18 stars with 263 tools across 17 toolsets. **BambooHR has the most implementations** of any HR platform with 8 (one, evrimalacan/mcp-bamboohr, has since been deleted — 7 confirmed live as of this audit), led by acalder-techpm's 74-tool implementation (now 11 stars). **CATS ATS has 228 tools** — the most tool-dense ATS server. **SAP SuccessFactors** (aiadiguru2025/sf-mcp) is now at 11 stars with production-grade coverage (43 tools, 21 data centers). **Ashby's ecosystem grew** to 4 implementations with dewierwan's server reaching ~30 tools and v1.7.0. On the downside, the **Deel, Recruitin, and Gupy servers were deleted** (repos now 404). **The remaining gaps**: no LinkedIn Recruiter, no iCIMS, no Lattice, no Culture Amp, and no employee engagement platforms.

## HRIS Platforms

### BambooHR (acalder-techpm)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [acalder-techpm/bamboohr-mcp](https://github.com/acalder-techpm/bamboohr-mcp) | 11 | TypeScript | MIT | 74 |

The most comprehensive BambooHR MCP server and one of the most feature-rich HRIS servers in the review. The 74 tools span **11 modules**: employees, time off, time tracking, ATS (yes, BambooHR's built-in recruiting), benefits, reports, training, goals, webhooks, files, and account management.

What sets this apart is the **30 role-based workflow templates** — pre-configured tool sets for HR Admin, Recruiter, Team Lead, and other personas. Instead of exposing all 74 tools to every agent, you can scope access to what each role needs. Zero-deploy via npx makes it quick to try.

### BambooHR (twentytwokhz)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [twentytwokhz/bamboohr-mcp](https://github.com/twentytwokhz/bamboohr-mcp) | 1 | TypeScript | MIT | 71 |

A close second with 71 tools across 9 domains. Full CRUD operations with **dual output** (JSON and Markdown) and **safety confirmations** for destructive operations like employee deletion. Published on npm for easy installation.

### BambooHR (iseletsk)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [iseletsk/cl-bamboohr-mcp](https://github.com/iseletsk/cl-bamboohr-mcp) | 1 | TypeScript | MIT | 21 |

A security-hardened alternative with 21 tools and 100+ tests. Emphasizes **input validation**, **credential sanitization**, and **safe error handling**. The author explicitly states this server combines the best approaches from 3 other BambooHR implementations with a focus on production safety.

### Other BambooHR Implementations

BambooHR had **8 total MCP implementations** — the most of any HR platform. As of this audit, one (evrimalacan/mcp-bamboohr) has been deleted from GitHub (404), leaving 7 confirmed live:

- **[encoreshao/bamboohr-mcp](https://github.com/encoreshao/bamboohr-mcp)** (4 stars, 7 tools) — lightweight library listed on mcp.so
- ~~evrimalacan/mcp-bamboohr~~ — repository deleted (404 as of 2026-08-16); no replacement has appeared
- **[a-isakov/bamboohr-mcp](https://github.com/a-isakov/bamboohr-mcp)** — TypeScript implementation
- **[stornes/bamboohr-mcp](https://github.com/stornes/bamboohr-mcp)** — TypeScript implementation
- **[keithballdotnet/bamboohr-mcp-server](https://github.com/keithballdotnet/bamboohr-mcp-server)** (Go) — focused specifically on time-off management

The volume of BambooHR servers reflects the platform's popularity in mid-market HR combined with a relatively straightforward API. TypeScript dominates the surviving implementations.

### SAP SuccessFactors (sf-mcp)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aiadiguru2025/sf-mcp](https://github.com/aiadiguru2025/sf-mcp) | 11 | Python | MIT | 43 |

The most production-ready enterprise HR MCP server in the review. 43 tools across **13 categories** including employee central, recruitment, performance, learning, compensation, succession planning, and more. Supports **21 SAP data centers** with automatic endpoint resolution.

Enterprise features that set this apart: **connection pooling**, **caching**, **rate limiting with 429 retry**, **OData injection prevention**, **XXE-safe XML parsing**, **credential masking** in logs, and **Cloud Logging-compatible** output. This is the only HR MCP server that reads like it was built for a production security review.

### SAP SuccessFactors (CData)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CDataSoftware/sap-successfactors-mcp-server-by-cdata](https://github.com/CDataSoftware/sap-successfactors-mcp-server-by-cdata) | 4 | Java | MIT | 3 |

CData's read-only gateway — 3 generic tools (get_tables, get_columns, run_query) over a JDBC driver. Part of [CData's 233-repository MCP catalog](https://github.com/orgs/CDataSoftware/repositories?q=mcp&type=all). Functional for basic querying but lacks the depth of sf-mcp.

### Workday (CData)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CDataSoftware/workday-mcp-server-by-cdata](https://github.com/CDataSoftware/workday-mcp-server-by-cdata) | 14 | Java | MIT | 3 |

The **most-starred HRIS MCP server** (in terms of platform brand recognition — Workday dominates enterprise HR). Read-only with 3 generic tools via JDBC. OAuth support. CData offers a separate commercial version with write capabilities.

Workday has 3 additional community servers (xiejiashan, joelee17, VijayKatkuri), but all appear to be early-stage or template implementations. Given Workday's API complexity, the ecosystem has room for a comprehensive community server.

### FactorialHR

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [t4dhg/mcp-factorial](https://github.com/t4dhg/mcp-factorial) | 3 | TypeScript | MIT | 14 (117 operations) |

A clever approach: **14 hierarchical tools** that expand to **117 total operations**. Tools like `employee_management` contain sub-operations for CRUD, search, and reporting. The [project README](https://github.com/t4dhg/mcp-factorial) describes this as "88% less context usage than individual tools" — a design that reduces the token cost of tool descriptions while maintaining full coverage.

Covers employees, teams, locations, projects, training, and recruiting. The README's subtitle bills the server as excluding payroll/financial data for security, but the detailed feature list contradicts that: it documents a `factorial_payroll` tool with read-only access to pay supplements, tax identifiers, and family-situation data. Safety guardrails prevent high-risk operations without confirmation, and all actions are audit-logged.

### PeopleSoft HCM

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rgrz/peoplesoft-mcp](https://github.com/rgrz/peoplesoft-mcp) | 12 | Python | MIT | 43 |

A rare MCP server for Oracle PeopleSoft — still widely used in higher education and government. 43 semantic tools across **6 modules**: Schema, HR, Payroll, Benefits, Performance, and PeopleTools. Connects directly to Oracle databases rather than through REST APIs. Notable for **effective dating support** — PeopleSoft's data model tracks historical state, and this server exposes that for historical workforce queries. *Updated April 2026: grew from 2 to 5 stars, adding `get_component_pages` and `get_page_field_bindings` tools plus a PeopleTools expert subagent and Claude Code skills. As of this audit (August 2026), the repository has grown further to 12 stars.*

### Rippling (bifrost-mcp)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bifrost-mcp/rippling-mcp](https://github.com/bifrost-mcp/rippling-mcp) | 3 | TypeScript | MIT | 18 |

The most complete Rippling server. 18 tools across **6 domains**: Company, Employees, Organization, Leave Management, Groups, and Activity. Bearer token auth, rate limiting, and structured error handling. A second implementation (rocketsciencegg, 5 tools) takes a read-only analytics approach with headcount snapshots and compensation summaries.

### Passgage (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [passgage/mcp-server](https://github.com/passgage/mcp-server) | 1 | TypeScript | MIT | 130+ |

One of the few **official vendor MCP servers** in the HR space. Passgage is a workforce management platform, and their MCP server exposes **130+ tools across 25 services** — the highest tool count of any HR platform server. Features **dual authentication** (admin and personal modes), **permission-aware tool availability** (tools appear/disappear based on access level), **Ransack filters** (20+ query operators), and **bulk operations**. Supports both cloud and on-premises deployment.

## Applicant Tracking Systems

### Workable (Official — NEW)

| Server | Host | Auth | Tools |
|--------|------|------|-------|
| [Workable MCP](https://workable.readme.io/reference/workable-mcp-server) | Remote (mcp.workable.com) | OAuth2 | 94 (as of July 2026) |

**The most significant official ATS MCP launch of 2026.** [Workable](https://www.workable.com/) — an ATS and HRIS platform serving [more than 6,200 companies across 100+ countries](https://www.globenewswire.com/news-release/2026/05/13/3293876/0/en/workable-launches-mcp-server-for-ai-powered-recruiting-and-hr-workflows.html) — [launched a hosted remote MCP server on May 13, 2026](https://www.globenewswire.com/news-release/2026/05/13/3293876/0/en/workable-launches-mcp-server-for-ai-powered-recruiting-and-hr-workflows.html) with 38 tools, included in all subscription plans at no additional cost. By [July 20, 2026, Workable had expanded the server to 94 tools](https://www.globenewswire.com/news-release/2026/07/20/3329974/0/en/workable-expands-mcp-server-to-94-tools-extending-ai-assistant-access-across-the-full-hiring-and-hr-lifecycle.html), adding advanced candidate and employee search, the complete performance-review lifecycle, account and permissions management, and additional recruiting workflows (advanced search is gated to Premier+ and Enterprise plans; the rest remains available on every plan at no added cost).

As of this audit, the [current tool documentation](https://workable.readme.io/reference/workable-mcp-server) lists 94 tools spanning both **recruiting** and **HR management** across 17 categories, including Candidates (18), Advanced Search (9), Jobs (9), Performance Review Cycles (12), Time Tracking (6), Requisitions (6), Members (6), Departments (5), Time Off (5), Employees (4), Offers (3), Pipeline & Account Config (3), Performance Reviews (3), Events (2), and one each for Accounts, Legal Entities, and Work Schedules.

This ATS+HRIS scope in a single official server is unusual — most vendors cover one domain or the other. Workable's server covers the full employee lifecycle from job requisition through hiring through ongoing employment.

Key differentiators: **read/write access** (agents can create, update, and manage records — not read-only), **OAuth2 authentication** (permissions scoped to the authenticated user's existing Workable role), and **zero-install deployment** (remote hosted at `https://mcp.workable.com/mcp`). Compatible with Claude and ChatGPT. No public GitHub repository — the server is proprietary.

Workable's combination of official support, read/write access, dual ATS+HRIS scope, hosted remote architecture, and no additional cost makes this the strongest enterprise ATS MCP launch since Passgage's official server.

### CATS ATS

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vanman2024/cats-mcp-server](https://github.com/vanman2024/cats-mcp-server) | 1 | Python | Custom | 228 |

The most tool-dense ATS server and one of the most tool-rich MCP servers we've reviewed in any category. **228 tools across 17 toolsets** providing complete CATS API v3 coverage. The toolsets are modular and loadable: Default (105 tools), Recruiting (106 tools), Data & Config (22 tools).

Includes AI-powered resume parsing, webhook management, full candidate lifecycle tracking, and FastMCP Cloud deployment. The scale here is impressive — this is more of a complete ATS automation layer than a simple query tool.

### Ashby

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dewierwan/ashby-mcp](https://github.com/dewierwan/ashby-mcp) | 1 | TypeScript | — | ~30 |

The most comprehensive and actively developed Ashby implementation. *Updated April 2026: grew from ~20 to ~30 tools, now at v1.7.0.* New additions include **escape-hatch tools** (`ashby_call_api` and `ashby_get_api_docs`) for accessing any Ashby API endpoint, **DOCX resume support** alongside PDF, and server-side status filtering for job listings. Features **resume extraction**, **pipeline visibility**, **bulk operations** (archive 25 candidates at once), **interview scheduling**, and **evaluation notes**. Dual-format output (summary + JSON). Supports Claude Code, Docker, and npx deployment. The most actively maintained HR MCP server in this review.

Three other Ashby servers exist: **[thibmaek/ashby-mcp](https://github.com/thibmaek/ashby-mcp)** (Go, 5 read-only tools with pre-built binaries), **[antonber/ashby-mcp](https://github.com/antonber/ashby-mcp)** (JavaScript, MIT, 8 tools with candidate search and interview feedback ratings), and **[PlenishAI/mcp-ashby](https://github.com/PlenishAI/mcp-ashby)** (5 stars, community, browse jobs and manage candidates). Four implementations for a single ATS platform shows strong developer demand for AI-assisted recruiting.

### Greenhouse

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CDataSoftware/greenhouse-mcp-server-by-cdata](https://github.com/CDataSoftware/greenhouse-mcp-server-by-cdata) | 0 | Java | MIT | 3 |

Greenhouse has limited MCP representation. CData offers their standard read-only JDBC gateway (3 tools). **[Null-Phnix/jobhound](https://github.com/Null-Phnix/jobhound)** (1 star, Python, MIT, 5 tools — repository has since been renamed from `jobhound-mcp` to `jobhound`) is more interesting as a multi-ATS tool covering Ashby, Greenhouse, and Lever with scan, score, apply, dashboard, and export functions plus a Textual TUI interface.

No community server provides deep Greenhouse API coverage yet — a notable gap given the platform's popularity and developer-friendly API.

### Lever

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [stefanoamorelli/lever-mcp](https://github.com/stefanoamorelli/lever-mcp) | 1 | Go | AGPL-3.0 | 59 |
| ~~the-sid-dani/lever-mcp-server~~ | — | TypeScript | — | 16 |

**UPDATE (as of this audit, 2026-08-16): the-sid-dani/lever-mcp-server now returns 404** — the repository has been deleted, and no repository under that GitHub account currently covers Lever. Previously it deployed on Cloudflare Workers with SSE endpoints and rate limiting, offering 16 recruiting functions including advanced candidate search, company-based candidate discovery, note-taking, and candidate archival. This leaves the Go server by stefanoamorelli as the sole surviving Lever implementation, with **59 tools across 17 categories** including opportunities, feedback, interviews, users, postings, and webhooks, running over Streamable HTTP with environment-variable-based tool filtering. It is community-built and not affiliated with Lever/Employ, Inc.

### Crelate ATS/CRM

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mrchevyceleb/crelate-mcp](https://github.com/mrchevyceleb/crelate-mcp) | 2 | Python | MIT | 40+ |

Staffing-focused ATS/CRM coverage. 6 core CRUD categories (Contacts, Candidates, Jobs, Companies, Notes, Tasks) plus **33+ reporting and analytics tools** including pipeline analysis, placement metrics, source attribution, and team productivity monitoring. Useful for staffing agencies running their operations through Crelate.

### Gupy (Brazil)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| ~~Morfeu333/GupyMCP~~ | — | Python | MIT | 40+ |

**UPDATE (as of this audit, 2026-08-16): this repository has been deleted (404).** It previously offered regional ATS coverage for Brazil's market — 40+ tools across 5 API categories: job posting management, application lifecycle, talent pool, org structure, and webhooks. No replacement Gupy MCP server has appeared. This is a loss for LATAM market coverage.

## Payroll & Benefits

### Check Payroll (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [check-technologies/mcp-server-check](https://github.com/check-technologies/mcp-server-check) | 18 | Python | — | 263 |

The **highest-starred HR MCP server** and the most comprehensive payroll implementation. [Check](https://www.checkhq.com/) is an embedded payroll infrastructure provider — its [65+ platform partners](https://www.checkhq.com/resources/blog/lessons-learned-from-65-embedded-payroll-partners) include [7shifts, Homebase, and Wave](https://www.checkhq.com/partners), among others — and their official MCP server exposes **263 tools across 17 toolsets**: companies, employees, contractors, payrolls, tax configuration, embedded components, and more.

Key features: **sandbox environment** for safe testing, **fine-grained tool filtering** (load only the toolsets you need), **read-only mode**, and **multiple transports** (stdio, SSE, streamable-http). Currently in Early Access Beta. *Updated April 2026: grew from 14 to 17 stars, adding a `check init` CLI command to generate CLAUDE.md, a consistent user-agent fix for all API calls, and an architecture refactor with `build_body`/`build_params` helpers. As of this audit (August 2026), the repository has grown further to 18 stars.*

### Deel

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| ~~JonasDNielsen/deel-mcp-server~~ | — | TypeScript | MIT | 25 |

**UPDATE April 2026: This repository has been deleted (404).** Previously offered 25 read-only tools covering organization data, people profiles, contracts, payroll reports, gross-to-net calculations, payslips, invoices, payments, time-off, and more through Deel's API. No replacement Deel MCP server has appeared. This is a loss for the ecosystem — Deel is a major global payroll platform with no current MCP coverage.

### Paylocity (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CDataSoftware/paylocity-mcp-server-by-cdata](https://github.com/CDataSoftware/paylocity-mcp-server-by-cdata) | 0 | Java | MIT | 3 |
| [mz462/mcpPaylocity](https://github.com/mz462/mcpPaylocity) | 0 | Python | MIT | 6 |

**Paylocity gains its first MCP coverage with two implementations.** CData offers their standard read-only JDBC gateway (3 tools). The community server by mz462 is more interesting — **6 tools** covering employees, earnings, company codes, local taxes, and pay statements via direct Paylocity API integration with OAuth2 authentication. Token caching is built in. Paylocity serves 36,000+ clients, making this a meaningful addition to the payroll ecosystem.

### ADP (CData)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CDataSoftware/adp-mcp-server-by-cdata](https://github.com/CDataSoftware/adp-mcp-server-by-cdata) | 2 | Java | MIT | 3 |

CData's standard read-only JDBC pattern for ADP. Given [ADP's market dominance](https://investors.adp.com/news/news-details/2025/ADP-Reports-Fourth-Quarter-and-Fiscal-2025-Results/default.aspx) (1.1 million+ clients across 140+ countries), the lack of a comprehensive MCP server is a significant gap.

### Payrolla (Turkish Payroll)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [runpayrolla/payrolla-mcp](https://github.com/runpayrolla/payrolla-mcp) | 1 | TypeScript | MIT | 5 |

Region-specific payroll calculations for Turkey. 5 tools covering single/bulk payroll, budget simulation, and scenario comparison. Implements Turkish-specific tax rules, social security calculations, and deductions. A good example of the localization challenge in HR — payroll rules vary dramatically by jurisdiction.

## Job Boards

### Indeed (Official — NEW)

| Server | Platform | Tools |
|--------|----------|-------|
| [Indeed MCP](https://docs.indeed.com/mcp) | Remote (mcp.indeed.com) | 4 (as of this audit) |

**The most significant new development in HR MCP.** Indeed launched an official MCP server in beta. As of this audit, the [live documentation](https://docs.indeed.com/mcp) lists **4 tools**: **Job Search** (search by title, keywords, location, employment type), **Job Detail** (full job descriptions, requirements, qualifications, benefits by job ID), **Get Resume** (reads the account holder's Indeed profile to personalize search results), and **Get Company Data** (employer research with satisfaction, compensation, culture, and review data) — Get Resume has been added since this review's original May 2026 pass, which counted 3 tools. Compatible with Claude Desktop, Cursor, and other MCP clients. Subject to Indeed's Terms of Service. This was previously the single biggest gap in the HR MCP ecosystem — a major job board with official MCP support is a milestone for the category.

## Recruiting Intelligence & Tools

### Recruitin

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| ~~WouterArtsRecruitin/recruitin-mcp-servers~~ | — | JS/TS | Proprietary | 43+ servers |

**UPDATE April 2026: This repository has been deleted (404).** Previously a commercial recruitment automation suite with 43+ individual MCP servers covering CV parsing, CV-to-vacancy matching, email composition, Notion integration, Pipedrive CRM, labour market intelligence, and HuggingFace ML models. The developer (WouterArts) still has other MCP repos on GitHub but removed the Recruitin suite. No replacement has appeared.

### Candidate Evaluation (Bias Reduction)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dominicholcomb/mcp_candidate_evaluation](https://github.com/dominicholcomb/mcp_candidate_evaluation) | 1 | Python | — | 2 |

An innovative **two-LLM architecture** for bias-reduced candidate evaluation. The first LLM scrubs protected characteristics from candidate data (gender, age, race, religion, disability, family status), intelligently rewriting contextual markers (e.g., "HBCU" becomes "university"). The second LLM evaluates the scrubbed candidate. Benchmarked across **6,480+ trials**. This addresses one of the most significant ethical challenges in AI-assisted recruiting.

### HR Vertical Agent Kit

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [UmarbekFU/hr-vertical-agent-kit](https://github.com/UmarbekFU/hr-vertical-agent-kit) | 1 | TypeScript | — | 12 (3 servers) |

A complete HR agent framework with **3 MCP servers** (Recruiting, Interviewing, Onboarding) and **12 tools** (9 LLM-powered, 3 rule-based). Includes 9 system prompts, resume parsing, interview question generation, **bias detection** (30+ phrases across 6 categories), and **legal compliance** checks for US/UK/EU/CA/AU employment law. 20+ evaluation scenarios for testing.

### Voice Agent for HR

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [prakharbhardwaj/voice-agent-mcp-server](https://github.com/prakharbhardwaj/voice-agent-mcp-server) | 3 | JavaScript | — | 5 |

Voice-based HR automation using Twilio Voice + Deepgram AI + OpenAI. 5 tools: conduct_interview, notify_interview_result, discuss_job_opening, get_call_status, and check_twilio_config. Enables phone screening and interview notifications through AI — a glimpse of how MCP could automate the phone screen stage of recruiting.

### Hunaras (AI-native Recruiting)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [shaxbozaka/hunaras-mcp](https://github.com/shaxbozaka/hunaras-mcp) | 0 | TypeScript | MIT | 24 |

An AI-native recruiting platform with **17 candidate tools** and **6 employer tools** plus 1 shared. Features semantic job search, AI interview assessment, LinkedIn profile sync, meeting proposals, talent pool search, and market insights including compensation range data. Built as an end-to-end recruiting workflow rather than just an API wrapper.

## CData Pattern: Enterprise HR Gateway

CData Software has published MCP servers for major enterprise HR platforms using a consistent 3-tool read-only JDBC pattern:

- **Workday** (14 stars) — `get_tables`, `get_columns`, `run_query`
- **SAP SuccessFactors** (4 stars) — same 3 tools
- **ADP** (2 stars) — same 3 tools
- **Greenhouse** (0 stars) — same 3 tools
- **Bullhorn CRM** — same 3 tools
- **Paylocity** (0 stars) — same 3 tools (now also has a community Python server)

CData has [233 MCP-related repositories](https://github.com/orgs/CDataSoftware/repositories?q=mcp&type=all) under its GitHub organization as of this audit (previously cited as 229 — the count grows as CData adds new source connectors). Their HR servers provide a quick path to querying enterprise HR data through natural language, but the 3-tool read-only pattern means no write operations, no platform-specific features, and no workflow automation. Commercial CRUD versions are available separately via [CData Connect AI](https://www.cdata.com/ai/).

## What's Missing

The HR MCP ecosystem has narrowed its gaps since March but still has notable absences:

- **No LinkedIn Recruiter MCP server** — the most-used recruiting tool globally has no MCP presence, likely due to LinkedIn's restrictive API access
- **No iCIMS, Jobvite, or SmartRecruiters** — major ATS platforms with no dedicated MCP servers
- ~~No Indeed~~ — **FILLED**: Indeed launched an official MCP server (beta)
- ~~No Lever~~ — **PARTIALLY FILLED**: the 59-tool Go server survives; the 16-tool TypeScript implementation has since been deleted from GitHub
- **No employee engagement platforms** — Lattice, Culture Amp, 15Five, Officevibe have zero MCP representation
- **No performance management** — beyond what's embedded in HRIS servers (Workable now has 3 performance review tools), no dedicated standalone performance review or OKR servers
- **No HiBob, Zenefits, or Namely** — popular mid-market HRIS platforms are absent
- ~~No Paylocity~~ — **FILLED**: CData + community Python server
- **No Paycom** — major payroll provider with no coverage
- **Deel coverage lost** — the only Deel MCP server was deleted
- **Recruitin commercial suite lost** — 43+ MCP servers deleted from GitHub
- **Gupy coverage lost** — the only Gupy MCP server (Morfeu333/GupyMCP) was deleted, as of this audit
- **No learning management** — Workday Learning, Cornerstone, and other LMS platforms don't have HR-specific MCP servers (though education LMS servers exist)
- **No benefits administration** — no dedicated servers for health insurance, 401(k), or benefits enrollment
- **Limited write operations** — many servers are read-only, reflecting appropriate caution but limiting workflow automation
- **Still low star counts** — the highest is 18 stars (Check Payroll, as of this audit), but adoption is slowly growing

## Bottom Line

**Rating: 4.0 / 5** — The HR and recruiting MCP ecosystem continues to mature. The May 2026 addition of Workable's official server — launched with 38 tools, read/write, spanning ATS and HRIS, hosted remote, included in all plans, and [expanded to 94 tools by July 2026](https://www.globenewswire.com/news-release/2026/07/20/3329974/0/en/workable-expands-mcp-server-to-94-tools-extending-ai-assistant-access-across-the-full-hiring-and-hr-lifecycle.html) — is the category's most enterprise-credible addition to date. Previously, Indeed's official MCP server (beta) filled the largest job board gap; Lever's TypeScript implementation has since been deleted, leaving its Go server as the sole survivor.

The bright spots are **Workable Official MCP** (94 tools as of July 2026, read/write, official), **Indeed Official MCP** (4 tools as of this audit, beta, the first major job board with official MCP), **Check Payroll** (18 stars, 263 tools, actively maintained), **Lever's Go server** (59 tools, filling a major ATS gap), **BambooHR** (7 surviving implementations), **SAP SuccessFactors** (11 stars, enterprise-grade), **Ashby** (4 implementations, dewierwan's server growing rapidly to ~30 tools), **CATS ATS** (228 tools), and **Passgage** (official vendor with 130+ tools).

The 4.0 rating holds: Workable's addition is a strong positive, but the **loss of the Deel, Recruitin, Gupy, and Lever-TypeScript servers** (all deleted), continued absence of **LinkedIn Recruiter, iCIMS, Lattice, and Culture Amp**, and still-low overall star counts keep this from a higher score. The ecosystem is broadening and deepening, but enterprise HR adoption of MCP remains early-stage.

*This review was last edited on 2026-05-17 using Claude Sonnet 4.6 (Anthropic); re-audited for citation accuracy on 2026-08-16.*

