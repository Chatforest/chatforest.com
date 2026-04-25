# HR & Recruiting MCP Servers — BambooHR, Workday, Greenhouse, Payroll, ATS, and More

> HR and recruiting MCP servers are giving AI assistants direct access to employee data, applicant tracking, payroll, and workforce management.


HR and recruiting MCP servers are giving AI assistants direct access to employee data, applicant tracking, payroll processing, and workforce management. Instead of navigating clunky HR portals, these servers let AI agents query employee records, manage job applications, run payroll reports, and coordinate hiring workflows — all through the Model Context Protocol. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

The landscape spans six areas: **HRIS platforms** (BambooHR, Workday, SAP SuccessFactors, Rippling, and more), **applicant tracking systems** (Greenhouse, Ashby, CATS ATS), **payroll and benefits** (Check, Deel, ADP), **workforce management** (Passgage), **recruiting intelligence** (CareerProof, Recruitin), and **HR agent tools** (bias reduction, voice interviewing, onboarding kits).

The headline findings: **Indeed launched an official MCP server** (beta) at `mcp.indeed.com` with job search, job detail, and company data tools — the first major job board with official MCP support. **Lever now has two MCP implementations** — a comprehensive 59-tool Go server and a 16-tool TypeScript/Cloudflare server — filling another major gap. **Check Payroll remains the highest-starred HR MCP server** at 17 stars with 263 tools across 17 toolsets. **BambooHR has the most implementations** of any HR platform with 8 competing servers, led by acalder-techpm's 74-tool implementation (now 5 stars). **CATS ATS has 228 tools** — the most tool-dense ATS server. **SAP SuccessFactors** surged to 5 stars with production-grade coverage (43 tools, 21 data centers). **Ashby's ecosystem grew** to 4 implementations with dewierwan's server reaching ~30 tools and v1.7.0. **Paylocity gained its first MCP coverage** with two new servers. On the downside, the **Deel and Recruitin servers were deleted** (repos now 404). **The remaining gaps**: no LinkedIn Recruiter, no iCIMS, no Lattice, no Culture Amp, and no employee engagement platforms.

## HRIS Platforms

### BambooHR (acalder-techpm)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [acalder-techpm/bamboohr-mcp](https://github.com/acalder-techpm/bamboohr-mcp) | 5 | TypeScript | MIT | 74 |

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
| [iseletsk/cl-bamboohr-mcp](https://github.com/iseletsk/cl-bamboohr-mcp) | 0 | TypeScript | MIT | 21 |

A security-hardened alternative with 21 tools and 100+ tests. Emphasizes **input validation**, **credential sanitization**, and **safe error handling**. The author explicitly states this server combines the best approaches from 3 other BambooHR implementations with a focus on production safety.

### Other BambooHR Implementations

BambooHR has **8 total MCP implementations** — the most of any HR platform:

- **encoreshao/bamboohr-mcp** (3 stars, 7 tools) — lightweight library listed on mcp.so
- **evrimalacan/mcp-bamboohr** — TypeScript implementation
- **a-isakov/bamboohr-mcp** — TypeScript implementation
- **stornes/bamboohr-mcp** — TypeScript implementation
- **keithballdotnet/bamboohr-mcp-server** (Go) — focused specifically on time-off management

The volume of BambooHR servers reflects the platform's popularity in mid-market HR (25,000+ companies) combined with a relatively straightforward API. TypeScript dominates with 7 of 8 implementations.

### SAP SuccessFactors (sf-mcp)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aiadiguru2025/sf-mcp](https://github.com/aiadiguru2025/sf-mcp) | 5 | Python | MIT | 43 |

The most production-ready enterprise HR MCP server in the review. 43 tools across **13 categories** including employee central, recruitment, performance, learning, compensation, succession planning, and more. Supports **21 SAP data centers** with automatic endpoint resolution.

Enterprise features that set this apart: **connection pooling**, **caching**, **rate limiting with 429 retry**, **OData injection prevention**, **XXE-safe XML parsing**, **credential masking** in logs, and **Cloud Logging-compatible** output. This is the only HR MCP server that reads like it was built for a production security review.

### SAP SuccessFactors (CData)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CDataSoftware/sap-successfactors-mcp-server-by-cdata](https://github.com/CDataSoftware/sap-successfactors-mcp-server-by-cdata) | 4 | Java | MIT | 3 |

CData's read-only gateway — 3 generic tools (get_tables, get_columns, run_query) over a JDBC driver. Part of CData's 229-server catalog. Functional for basic querying but lacks the depth of sf-mcp.

### Workday (CData)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CDataSoftware/workday-mcp-server-by-cdata](https://github.com/CDataSoftware/workday-mcp-server-by-cdata) | 10 | Java | MIT | 3 |

The **most-starred HRIS MCP server** (in terms of platform brand recognition — Workday dominates enterprise HR). Read-only with 3 generic tools via JDBC. OAuth support. CData offers a separate commercial version with write capabilities.

Workday has 3 additional community servers (xiejiashan, joelee17, VijayKatkuri), but all appear to be early-stage or template implementations. Given Workday's API complexity, the ecosystem has room for a comprehensive community server.

### FactorialHR

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [t4dhg/mcp-factorial](https://github.com/t4dhg/mcp-factorial) | 4 | TypeScript | MIT | 14 (117 operations) |

A clever approach: **14 hierarchical tools** that expand to **117 total operations**. Tools like `employee_management` contain sub-operations for CRUD, search, and reporting. This "88% less context" design reduces the token cost of tool descriptions while maintaining full coverage.

Includes 5 MCP resources, 4 MCP prompts, and covers employees, teams, locations, projects, training, and recruiting. **Deliberately excludes payroll data** for security — a thoughtful design choice. Safety guardrails prevent high-risk operations without confirmation, and all actions are audit-logged.

### PeopleSoft HCM

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rgrz/peoplesoft-mcp](https://github.com/rgrz/peoplesoft-mcp) | 5 | Python | MIT | 43 |

A rare MCP server for Oracle PeopleSoft — still widely used in higher education and government. 43 semantic tools across **6 modules**: Schema, HR, Payroll, Benefits, Performance, and PeopleTools. Connects directly to Oracle databases rather than through REST APIs. Notable for **effective dating support** — PeopleSoft's data model tracks historical state, and this server exposes that for historical workforce queries. *Updated April 2026: grew from 2 to 5 stars. Added `get_component_pages` and `get_page_field_bindings` tools, plus a PeopleTools expert subagent and Claude Code skills.*

### Rippling (bifrost-mcp)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bifrost-mcp/rippling-mcp](https://github.com/bifrost-mcp/rippling-mcp) | 1 | TypeScript | MIT | 18 |

The most complete Rippling server. 18 tools across **6 domains**: Company, Employees, Organization, Leave Management, Groups, and Activity. Bearer token auth, rate limiting, and structured error handling. A second implementation (rocketsciencegg, 5 tools) takes a read-only analytics approach with headcount snapshots and compensation summaries.

### Passgage (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [passgage/mcp-server](https://github.com/passgage/mcp-server) | 1 | TypeScript | MIT | 130+ |

One of the few **official vendor MCP servers** in the HR space. Passgage is a workforce management platform, and their MCP server exposes **130+ tools across 25 services** — the highest tool count of any HR platform server. Features **dual authentication** (admin and personal modes), **permission-aware tool availability** (tools appear/disappear based on access level), **Ransack filters** (20+ query operators), and **bulk operations**. Supports both cloud and on-premises deployment.

## Applicant Tracking Systems

### CATS ATS

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vanman2024/cats-mcp-server](https://github.com/vanman2024/cats-mcp-server) | 1 | Python | Custom | 228 |

The most tool-dense ATS server and one of the most tool-rich MCP servers we've reviewed in any category. **228 tools across 17 toolsets** providing complete CATS API v3 coverage. The toolsets are modular and loadable: Default (105 tools), Recruiting (106 tools), Data & Config (22 tools).

Includes AI-powered resume parsing, webhook management, full candidate lifecycle tracking, and FastMCP Cloud deployment. The scale here is impressive — this is more of a complete ATS automation layer than a simple query tool.

### Ashby

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dewierwan/ashby-mcp](https://github.com/dewierwan/ashby-mcp) | 0 | TypeScript | — | ~30 |

The most comprehensive and actively developed Ashby implementation. *Updated April 2026: grew from ~20 to ~30 tools, now at v1.7.0.* New additions include **escape-hatch tools** (`ashby_call_api` and `ashby_get_api_docs`) for accessing any Ashby API endpoint, **DOCX resume support** alongside PDF, and server-side status filtering for job listings. Features **resume extraction**, **pipeline visibility**, **bulk operations** (archive 25 candidates at once), **interview scheduling**, and **evaluation notes**. Dual-format output (summary + JSON). Supports Claude Code, Docker, and npx deployment. The most actively maintained HR MCP server in this review.

Three other Ashby servers exist: **thibmaek/ashby-mcp** (Go, 5 read-only tools with pre-built binaries), **antonber/ashby-mcp** (JavaScript, MIT, 8 tools with candidate search and interview feedback ratings), and **PlenishAI/mcp-ashby** (community, browse jobs and manage candidates). Four implementations for a single ATS platform shows strong developer demand for AI-assisted recruiting.

### Greenhouse

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CDataSoftware/greenhouse-mcp-server-by-cdata](https://github.com/CDataSoftware/greenhouse-mcp-server-by-cdata) | 0 | Java | MIT | 3 |

Greenhouse — one of the most popular ATS platforms — has limited MCP representation. CData offers their standard read-only JDBC gateway (3 tools). **Null-Phnix/jobhound-mcp** (1 star, Python, MIT, 5 tools) is more interesting as a multi-ATS tool covering Ashby, Greenhouse, and Lever with scan, score, apply, dashboard, and export functions plus a Textual TUI interface.

No community server provides deep Greenhouse API coverage yet — a notable gap given the platform's popularity and developer-friendly API.

### Lever (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [stefanoamorelli/lever-mcp](https://github.com/stefanoamorelli/lever-mcp) | 1 | Go | AGPL-3.0 | 59 |
| [the-sid-dani/lever-mcp-server](https://github.com/the-sid-dani/lever-mcp-server) | 4 | TypeScript | — | 16 |

**Previously a major gap, Lever now has two MCP implementations.** The Go server by stefanoamorelli is the most comprehensive with **59 tools across 17 categories** including opportunities, feedback, interviews, users, postings, and webhooks. Runs over Streamable HTTP with environment-variable-based tool filtering. The TypeScript server by the-sid-dani deploys on Cloudflare Workers with SSE endpoints and rate limiting, offering **16 recruiting functions** including advanced candidate search, company-based candidate discovery, note-taking, and candidate archival. Both are community-built and not affiliated with Lever/Employ, Inc. The Go server is the more complete option; the TypeScript server is easier to deploy serverlessly.

### Crelate ATS/CRM

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mrchevyceleb/crelate-mcp](https://github.com/mrchevyceleb/crelate-mcp) | 0 | Python | MIT | 40+ |

Staffing-focused ATS/CRM coverage. 6 core CRUD categories (Contacts, Candidates, Jobs, Companies, Notes, Tasks) plus **33+ reporting and analytics tools** including pipeline analysis, placement metrics, source attribution, and team productivity monitoring. Useful for staffing agencies running their operations through Crelate.

### Gupy (Brazil)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Morfeu333/GupyMCP](https://github.com/Morfeu333/GupyMCP) | 0 | Python | MIT | 40+ |

Regional ATS coverage for Brazil's market-leading platform. 40+ tools across 5 API categories: job posting management, application lifecycle, talent pool, org structure, and webhooks. Docker support. Gupy is used by major Brazilian employers, making this relevant for the LATAM market.

## Payroll & Benefits

### Check Payroll (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [check-technologies/mcp-server-check](https://github.com/check-technologies/mcp-server-check) | 17 | Python | — | 263 |

The **highest-starred HR MCP server** and the most comprehensive payroll implementation. Check is an embedded payroll infrastructure provider (powers payroll for platforms like Gusto, Justworks, and others), and their official MCP server exposes **263 tools across 17 toolsets**: companies, employees, contractors, payrolls, tax configuration, embedded components, and more.

Key features: **sandbox environment** for safe testing, **fine-grained tool filtering** (load only the toolsets you need), **read-only mode**, and **multiple transports** (stdio, SSE, streamable-http). Currently in Early Access Beta. *Updated April 2026: grew from 14 to 17 stars. New `check init` CLI command to generate CLAUDE.md, consistent user-agent fix for all API calls, and architecture refactor with `build_body`/`build_params` helpers. Active development continues.*

### Deel

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| ~~JonasDNielsen/deel-mcp-server~~ | — | TypeScript | MIT | 25 |

**UPDATE April 2026: This repository has been deleted (404).** Previously offered 25 read-only tools covering organization data, people profiles, contracts, payroll reports, gross-to-net calculations, payslips, invoices, payments, time-off, and more through Deel's API. No replacement Deel MCP server has appeared. This is a loss for the ecosystem — Deel is a major global payroll platform with no current MCP coverage.

### Paylocity (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CDataSoftware/paylocity-mcp-server-by-cdata](https://github.com/CDataSoftware/paylocity-mcp-server-by-cdata) | — | Java | MIT | 3 |
| [mz462/mcpPaylocity](https://github.com/mz462/mcpPaylocity) | 0 | Python | MIT | 6 |

**Paylocity gains its first MCP coverage with two implementations.** CData offers their standard read-only JDBC gateway (3 tools). The community server by mz462 is more interesting — **6 tools** covering employees, earnings, company codes, local taxes, and pay statements via direct Paylocity API integration with OAuth2 authentication. Token caching is built in. Paylocity serves 36,000+ clients, making this a meaningful addition to the payroll ecosystem.

### ADP (CData)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CDataSoftware/adp-mcp-server-by-cdata](https://github.com/CDataSoftware/adp-mcp-server-by-cdata) | 2 | Java | MIT | 3 |

CData's standard read-only JDBC pattern for ADP. Given ADP's market dominance (920,000+ clients), the lack of a comprehensive MCP server is a significant gap.

### Payrolla (Turkish Payroll)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [runpayrolla/payrolla-mcp](https://github.com/runpayrolla/payrolla-mcp) | 1 | TypeScript | MIT | 5 |

Region-specific payroll calculations for Turkey. 5 tools covering single/bulk payroll, budget simulation, and scenario comparison. Implements Turkish-specific tax rules, social security calculations, and deductions. A good example of the localization challenge in HR — payroll rules vary dramatically by jurisdiction.

## Job Boards

### Indeed (Official — NEW)

| Server | Platform | Tools |
|--------|----------|-------|
| [Indeed MCP](https://docs.indeed.com/mcp) | Remote (mcp.indeed.com) | 3 |

**The most significant new development in HR MCP.** Indeed — the world's largest job site — launched an official MCP server in beta. The remote server at `mcp.indeed.com/claude/mcp` provides **3 tools**: **Job Search** (search by title, keywords, location, employment type), **Job Detail** (full job descriptions, requirements, qualifications, benefits by job ID), and **Get Company Data** (employer research with satisfaction, compensation, culture, and review data). Compatible with Claude Desktop, Cursor, and other MCP clients. Subject to Indeed's Terms of Service. This was previously the single biggest gap in the HR MCP ecosystem — a major job board with official MCP support is a milestone for the category.

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

- **Workday** (10 stars) — `get_tables`, `get_columns`, `run_query`
- **SAP SuccessFactors** (4 stars) — same 3 tools
- **ADP** (2 stars) — same 3 tools
- **Greenhouse** (0 stars) — same 3 tools
- **Bullhorn CRM** — same 3 tools
- **Paylocity** — same 3 tools (now also has a community Python server)

CData has 229 MCP servers total across all categories. Their HR servers provide a quick path to querying enterprise HR data through natural language, but the 3-tool read-only pattern means no write operations, no platform-specific features, and no workflow automation. Commercial CRUD versions are available separately.

## What's Missing

The HR MCP ecosystem has narrowed its gaps since March but still has notable absences:

- **No LinkedIn Recruiter MCP server** — the most-used recruiting tool globally has no MCP presence, likely due to LinkedIn's restrictive API access
- **No iCIMS, Jobvite, or SmartRecruiters** — major ATS platforms with no dedicated MCP servers
- ~~No Indeed~~ — **FILLED**: Indeed launched an official MCP server (beta)
- ~~No Lever~~ — **FILLED**: two community implementations (59-tool Go + 16-tool TypeScript)
- **No employee engagement platforms** — Lattice, Culture Amp, 15Five, Officevibe have zero MCP representation
- **No performance management** — beyond what's embedded in HRIS servers, no dedicated performance review or OKR servers
- **No HiBob, Zenefits, or Namely** — popular mid-market HRIS platforms are absent
- ~~No Paylocity~~ — **FILLED**: CData + community Python server
- **No Paycom** — major payroll provider with no coverage
- **Deel coverage lost** — the only Deel MCP server was deleted
- **Recruitin commercial suite lost** — 43+ MCP servers deleted from GitHub
- **No learning management** — Workday Learning, Cornerstone, and other LMS platforms don't have HR-specific MCP servers (though education LMS servers exist)
- **No benefits administration** — no dedicated servers for health insurance, 401(k), or benefits enrollment
- **Limited write operations** — many servers are read-only, reflecting appropriate caution but limiting workflow automation
- **Still low star counts** — the highest is 17 stars (Check Payroll), but adoption is slowly growing

## Bottom Line

**Rating: 4.0 / 5** — The HR and recruiting MCP ecosystem took a meaningful step forward since March 2026. The Indeed official MCP server (beta) fills the single biggest gap that held the previous rating back — a major job board with vendor-supported MCP is a category milestone. Lever gained two community implementations (up to 59 tools), and Paylocity got its first coverage.

The bright spots are **Indeed Official MCP** (3 tools, beta, the first major job board with official MCP), **Check Payroll** (17 stars, 263 tools, actively maintained), **Lever** (2 implementations filling a major ATS gap), **BambooHR** (8 implementations), **SAP SuccessFactors** (5 stars, enterprise-grade), **Ashby** (4 implementations, dewierwan's server growing rapidly to ~30 tools), **CATS ATS** (228 tools), and **Passgage** (official vendor with 130+ tools).

The upgrade to 4.0 reflects the Indeed and Lever gaps being filled, steady star growth across multiple servers, and Ashby's maturation. The rating is held back by the **loss of the Deel and Recruitin servers** (both deleted), continued absence of **LinkedIn Recruiter, iCIMS, Lattice, and Culture Amp**, and still-low overall star counts. The ecosystem is broadening and deepening, but enterprise HR adoption of MCP remains early-stage.

*This review was last edited on 2026-04-25 using Claude Opus 4.6 (Anthropic).*

