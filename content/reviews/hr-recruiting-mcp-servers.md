---
title: "HR & Recruiting MCP Servers — BambooHR, Workday, Greenhouse, Payroll, ATS, and More"
date: 2026-03-15T21:00:00+09:00
description: "HR and recruiting MCP servers are giving AI assistants direct access to employee data, applicant tracking, payroll, and workforce management. We reviewed 50+ servers across 6 subcategories. HRIS Platforms: BambooHR leads with 8 implementations (acalder-techpm at 3 stars, 74 tools across 11 modules with 30 role-based workflow templates), Workday (CData at 8 stars, read-only JDBC), SAP SuccessFactors (sf-mcp, 43 tools across 13 categories with 21 data center support), FactorialHR (2 stars, 14 hierarchical tools / 117 operations), PeopleSoft HCM (2 stars, 41 tools, direct Oracle DB), Rippling (bifrost-mcp, 18 tools across 6 domains). ATS: CATS ATS (228 tools, most tool-dense ATS server), Ashby (3 implementations, dewierwan with 20+ tools for bulk operations and resume extraction), Greenhouse (CData, JobHound multi-ATS). Payroll: Check (14 stars, 263 tools across 17 toolsets — highest-starred HR MCP server), Deel (25 read-only tools for global payroll), Payrolla (Turkish payroll). Workforce Management: Passgage (official, 130+ tools across 25 services). Recruiting Intelligence: Recruitin (43+ servers, commercial), CareerProof (42 tools, workforce intelligence). HR Agent Tools: bias-reduction candidate evaluation, voice-based HR interviewing, vertical agent kits. Rating: 3.5/5."
og_description: "HR & Recruiting MCP servers: 50+ servers from BambooHR (8 implementations, 74 tools), Check Payroll (14 stars, 263 tools — highest-starred), CATS ATS (228 tools), SAP SuccessFactors (43 tools), Passgage (official, 130+ tools), Ashby (20+ tools), FactorialHR (117 operations), PeopleSoft (41 tools), Deel (25 tools). Rating: 3.5/5."
content_type: "Review"
card_description: "HR and recruiting MCP servers across HRIS platforms, applicant tracking systems, payroll, workforce management, and recruiting intelligence. The HR MCP ecosystem is surprisingly deep — with 50+ servers covering BambooHR (8 implementations), Workday, SAP SuccessFactors, PeopleSoft, Greenhouse, Ashby, CATS ATS (228 tools), and Check Payroll (263 tools, the most tool-rich server in the review). BambooHR has the most implementations of any single HR platform, with acalder-techpm's 74-tool server leading the pack. Check Payroll is the highest-starred HR MCP server at 14 stars and offers 263 tools across 17 toolsets. Passgage is one of the few official vendor servers with 130+ tools. SAP SuccessFactors has production-grade coverage with 43 tools, 21 data center support, and enterprise security features. The ATS space is led by CATS with a staggering 228 tools and Ashby with 3 competing implementations. The category earns 3.5/5 — impressive breadth across enterprise HR platforms, but low star counts reveal this is still an emerging space. The major gaps are glaring: no LinkedIn Recruiter, no Indeed, no Lever, no iCIMS, no Lattice, no Culture Amp, and no employee engagement platforms. The ecosystem skews heavily toward data access rather than intelligent HR workflows."
last_refreshed: 2026-03-15
---

HR and recruiting MCP servers are giving AI assistants direct access to employee data, applicant tracking, payroll processing, and workforce management. Instead of navigating clunky HR portals, these servers let AI agents query employee records, manage job applications, run payroll reports, and coordinate hiring workflows — all through the Model Context Protocol.

The landscape spans six areas: **HRIS platforms** (BambooHR, Workday, SAP SuccessFactors, Rippling, and more), **applicant tracking systems** (Greenhouse, Ashby, CATS ATS), **payroll and benefits** (Check, Deel, ADP), **workforce management** (Passgage), **recruiting intelligence** (CareerProof, Recruitin), and **HR agent tools** (bias reduction, voice interviewing, onboarding kits).

The headline findings: **Check Payroll is the highest-starred HR MCP server** at 14 stars with 263 tools across 17 toolsets — a proper enterprise payroll API surface. **BambooHR has the most implementations** of any HR platform with 8 competing servers, led by acalder-techpm's 74-tool implementation. **CATS ATS has 228 tools** — the most tool-dense ATS server and one of the most tool-rich MCP servers in any category. **SAP SuccessFactors** has production-grade coverage with 43 tools, 21 data center support, and enterprise security hardening. **Passgage is one of the few official vendor servers** with 130+ tools. **The major platforms are absent**: no LinkedIn Recruiter, no Indeed, no Lever, no iCIMS, no Workable (beyond a skeleton), no Lattice, no Culture Amp, and no employee engagement tools whatsoever. **Star counts are uniformly low** — the highest is just 14 — indicating this ecosystem is very early-stage despite broad platform coverage.

## HRIS Platforms

### BambooHR (acalder-techpm)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [acalder-techpm/bamboohr-mcp](https://github.com/acalder-techpm/bamboohr-mcp) | 3 | TypeScript | MIT | 74 |

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
| [aiadiguru2025/sf-mcp](https://github.com/aiadiguru2025/sf-mcp) | 1 | Python | MIT | 43 |

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
| [CDataSoftware/workday-mcp-server-by-cdata](https://github.com/CDataSoftware/workday-mcp-server-by-cdata) | 8 | Java | MIT | 3 |

The **most-starred HRIS MCP server** (in terms of platform brand recognition — Workday dominates enterprise HR). Read-only with 3 generic tools via JDBC. OAuth support. CData offers a separate commercial version with write capabilities.

Workday has 3 additional community servers (xiejiashan, joelee17, VijayKatkuri), but all appear to be early-stage or template implementations. Given Workday's API complexity, the ecosystem has room for a comprehensive community server.

### FactorialHR

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [t4dhg/mcp-factorial](https://github.com/t4dhg/mcp-factorial) | 2 | TypeScript | MIT | 14 (117 operations) |

A clever approach: **14 hierarchical tools** that expand to **117 total operations**. Tools like `employee_management` contain sub-operations for CRUD, search, and reporting. This "88% less context" design reduces the token cost of tool descriptions while maintaining full coverage.

Includes 5 MCP resources, 4 MCP prompts, and covers employees, teams, locations, projects, training, and recruiting. **Deliberately excludes payroll data** for security — a thoughtful design choice. Safety guardrails prevent high-risk operations without confirmation, and all actions are audit-logged.

### PeopleSoft HCM

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rgrz/peoplesoft-mcp](https://github.com/rgrz/peoplesoft-mcp) | 2 | Python | MIT | 41 |

A rare MCP server for Oracle PeopleSoft — still widely used in higher education and government. 41 semantic tools across **6 modules**: Schema, HR, Payroll, Benefits, Performance, and PeopleTools. Connects directly to Oracle databases rather than through REST APIs. Notable for **effective dating support** — PeopleSoft's data model tracks historical state, and this server exposes that for historical workforce queries.

### Rippling (bifrost-mcp)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bifrost-mcp/rippling-mcp](https://github.com/bifrost-mcp/rippling-mcp) | 0 | TypeScript | MIT | 18 |

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
| [dewierwan/ashby-mcp](https://github.com/dewierwan/ashby-mcp) | 0 | TypeScript | — | 20+ |

The most comprehensive Ashby implementation. Features **resume extraction**, **pipeline visibility**, **bulk operations** (archive 25 candidates at once), **interview scheduling**, and **evaluation notes**. Dual-format output (summary + JSON). Supports Claude Code, Docker, and npx deployment.

Two other Ashby servers exist: **thibmaek/ashby-mcp** (Go, 5 read-only tools with pre-built binaries) and **antonber/ashby-mcp** (JavaScript, MIT, 8 tools with candidate search and interview feedback ratings). Three implementations for a single ATS platform shows strong developer demand for AI-assisted recruiting.

### Greenhouse

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CDataSoftware/greenhouse-mcp-server-by-cdata](https://github.com/CDataSoftware/greenhouse-mcp-server-by-cdata) | 0 | Java | MIT | 3 |

Greenhouse — one of the most popular ATS platforms — has limited MCP representation. CData offers their standard read-only JDBC gateway (3 tools). **Null-Phnix/jobhound-mcp** (1 star, Python, MIT, 5 tools) is more interesting as a multi-ATS tool covering Ashby, Greenhouse, and Lever with scan, score, apply, dashboard, and export functions plus a Textual TUI interface.

No community server provides deep Greenhouse API coverage yet — a notable gap given the platform's popularity and developer-friendly API.

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
| [check-technologies/mcp-server-check](https://github.com/check-technologies/mcp-server-check) | 14 | Python | — | 263 |

The **highest-starred HR MCP server** and the most comprehensive payroll implementation. Check is an embedded payroll infrastructure provider (powers payroll for platforms like Gusto, Justworks, and others), and their official MCP server exposes **263 tools across 17 toolsets**: companies, employees, contractors, payrolls, tax configuration, embedded components, and more.

Key features: **sandbox environment** for safe testing, **fine-grained tool filtering** (load only the toolsets you need), **read-only mode**, and **multiple transports** (stdio, SSE, streamable-http). Currently in Early Access Beta. The depth here matches what you'd expect from a payroll API — detailed tax configuration, contractor management, and payment processing capabilities.

### Deel

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [JonasDNielsen/deel-mcp-server](https://github.com/JonasDNielsen/deel-mcp-server) | 0 | TypeScript | MIT | 25 |

Global payroll and HR coverage through Deel's API. **25 read-only tools** covering organization data, people profiles, contracts, payroll reports, gross-to-net calculations, payslips, invoices, payments, time-off, org structure, EOR benefits, and document metadata. The read-only design is appropriate for a payroll system — you probably don't want AI agents modifying salary data without human review.

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

## Recruiting Intelligence & Tools

### Recruitin

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [WouterArtsRecruitin/recruitin-mcp-servers](https://github.com/WouterArtsRecruitin/recruitin-mcp-servers) | 0 | JS/TS | Proprietary | 43+ servers |

A commercial recruitment automation suite. **43+ individual MCP servers** covering CV parsing, CV-to-vacancy matching, email composition, Notion integration, Pipedrive CRM, labour market intelligence, and HuggingFace ML models. 151 commits indicate active development. Proprietary license (S&PS BV).

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

- **Workday** (8 stars) — `get_tables`, `get_columns`, `run_query`
- **SAP SuccessFactors** (4 stars) — same 3 tools
- **ADP** (2 stars) — same 3 tools
- **Greenhouse** (0 stars) — same 3 tools
- **Bullhorn CRM** — same 3 tools
- **Paylocity** — same 3 tools

CData has 229 MCP servers total across all categories. Their HR servers provide a quick path to querying enterprise HR data through natural language, but the 3-tool read-only pattern means no write operations, no platform-specific features, and no workflow automation. Commercial CRUD versions are available separately.

## What's Missing

The HR MCP ecosystem has substantial gaps:

- **No LinkedIn Recruiter MCP server** — the most-used recruiting tool globally has no MCP presence, likely due to LinkedIn's restrictive API access
- **No Indeed, Lever, iCIMS, Jobvite, or SmartRecruiters** — major ATS platforms with no dedicated MCP servers
- **No employee engagement platforms** — Lattice, Culture Amp, 15Five, Officevibe have zero MCP representation
- **No performance management** — beyond what's embedded in HRIS servers, no dedicated performance review or OKR servers
- **No HiBob, Zenefits, or Namely** — popular mid-market HRIS platforms are absent
- **No Paychex or Paycom** — major payroll providers beyond ADP have no coverage
- **No learning management** — Workday Learning, Cornerstone, and other LMS platforms don't have HR-specific MCP servers (though education LMS servers exist)
- **No benefits administration** — no dedicated servers for health insurance, 401(k), or benefits enrollment
- **Limited write operations** — many servers are read-only, reflecting appropriate caution but limiting workflow automation
- **Very low star counts** — the highest is 14 stars, indicating this is an early-stage ecosystem with limited community adoption

## Bottom Line

**Rating: 3.5 / 5** — The HR and recruiting MCP ecosystem is broader than expected but shallower than it needs to be. Over 50 servers exist across HRIS platforms, ATS systems, payroll, and recruiting tools — but the overall adoption signals are weak, with the highest-starred server at just 14 stars.

The bright spots are **Check Payroll** (263 tools, official, production-grade with sandbox environment), **BambooHR** (8 implementations showing strong developer demand), **SAP SuccessFactors** (enterprise-grade with proper security hardening), **CATS ATS** (228 tools of comprehensive coverage), and **Passgage** (official vendor with 130+ tools). The **bias-reduction candidate evaluation** server stands out as an ethically important innovation.

The 3.5 rating reflects the breadth of platform coverage (BambooHR, Workday, SAP, Greenhouse, Ashby, Rippling, Deel, and more) balanced against the glaring absences (LinkedIn Recruiter, Indeed, Lever, employee engagement tools), low adoption metrics, and the ecosystem's heavy skew toward data access over intelligent HR workflows. The Check Payroll server demonstrates what a well-built HR MCP server looks like — official, comprehensive, secure, with sandbox testing — but it's the exception rather than the rule. This space will likely grow significantly as AI agents become more common in HR operations.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
