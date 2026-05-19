---
title: "Education & EdTech MCP Servers — Canvas LMS, Moodle, Google Classroom, Anki, Udemy, EduBase, and More"
date: 2026-03-15T15:30:00+09:00
description: "Education and EdTech MCP servers are connecting AI agents to learning management systems, flashcard apps, academic research databases, and assessment platforms."
og_description: "Education MCP servers: Canvas LMS (107+ stars, create_rubric added), Anki (237 stars, v0.15.1 security hardening, native addon launched), arXiv (2,700 stars), paper-search-mcp (1,500 stars +25%, 20+ sources), Moodle (36 stars), D2L Brightspace (3 implementations), Udemy Business (GA, expanding), first Coursera MCP scraper. 52+ education servers on PulseMCP. Rating: 3.5/5."
content_type: "Review"
card_description: "Education and EdTech MCP servers for learning management systems, flashcard apps, academic research, assessment platforms, and STEM computation. The education MCP ecosystem is fragmented but growing fast — 52+ education servers on PulseMCP. Canvas LMS dominates with multiple competing implementations — vishalsachdev/canvas-mcp (107 stars, 88+ tools, May 2026: create_rubric tool + read_course_file added) has overtaken DMontgomery40/mcp-canvas-lms as the most-starred. Moodle has peancor/moodle-mcp-server (36 stars, MIT). D2L Brightspace now has 3+ implementations including RohanMuppa (14 stars, AES-256 encryption). Google Classroom remains minimal (3 read-only tools). The flashcard space is dominated by ankimcp/anki-mcp-server (237 stars, v0.15.1 — security hardening for path traversal + SSRF; native Anki addon launched at ankimcp.ai, no AnkiConnect dependency). For academic research, blazickjp/arxiv-mcp-server (2,700 stars +4%, MIT, 8 tools including semantic search) is the standout. openags/paper-search-mcp (1,500 stars +25%) now aggregates 20+ academic sources. Udemy Business MCP remains in GA (since March 31, 2026). NEW: nwolke/coursera-mcp — first Coursera MCP integration (Playwright-based progress scraper). NEW: O'Reilly Learning Platform MCP on PulseMCP. OpenEdu MCP (7 stars, 21+ tools, K-2 through College grade filtering, Common Core/NGSS). Khan Academy MCP (early stage). EduBase/MCP (25 stars, MIT) brings assessment infrastructure with LaTeX and GDPR compliance. Policy context: 134 AI-in-education bills across 31 US states, Ohio mandating formal AI policies by July 2026. Notable gaps: no Blackboard/Sakai/Open edX; no SIS integrations; no library systems; no plagiarism detection; no adaptive learning. Rating: 3.5/5 — academic research tools are excellent (paper-search-mcp +25%), Anki security-hardened with native addon, Canvas gaining new tools, first Coursera coverage. But Blackboard's absence, missing SIS/library integrations, and thin K-12 coverage prevent a higher score."
last_refreshed: 2026-05-20
---

*Part of the [Education & Learning](/categories/education-learning/) category.*

Education MCP servers are connecting AI agents to learning management systems, flashcard applications, academic research databases, assessment platforms, and STEM computation tools. Instead of manually navigating LMS dashboards, searching academic databases, or creating flashcards one at a time, these servers let AI assistants manage coursework, track grades, search research papers, run spaced repetition sessions, generate quizzes, and solve mathematical problems — all through the Model Context Protocol.

The landscape spans seven areas: **LMS integration** (Canvas, Moodle, Google Classroom, D2L Brightspace), **flashcards & spaced repetition** (Anki implementations), **academic research** (arXiv, Semantic Scholar, multi-platform aggregators), **enterprise learning** (Udemy Business), **assessment & tutoring** (EduBase, quiz generators), **STEM tools** (Wolfram Alpha computation), and **knowledge reference** (Wikipedia).

The headline findings: **vishalsachdev/canvas-mcp** (107 stars) added new tools in May 2026 — `create_rubric` (PR #100) for programmatic rubric creation with criteria, ratings, and assignment association, plus `read_course_file` for remote MCP deployments. **Academic research continues to surge** — paper-search-mcp reached 1,500 stars (+25% in 28 days), now the fastest-growing server in this category, while arXiv MCP climbed to 2,700 stars. **Anki MCP Server received critical security hardening** — v0.15.1 (April 9) fixes path traversal and SSRF vulnerabilities in media operations; a new native Anki addon (ankimcp/anki-mcp-server-addon) launched with professional documentation at ankimcp.ai, eliminating the AnkiConnect dependency. **Coursera gets its first MCP integration** — nwolke/coursera-mcp scrapes learning progress via Playwright; previously Coursera was absent entirely. **O'Reilly Learning Platform MCP** now listed on PulseMCP. **52+ education servers on PulseMCP.** The biggest remaining gap: **Blackboard still has zero MCP implementations**.

### Ecosystem stats (May 2026)

| Metric | Value |
|--------|-------|
| Education servers on PulseMCP | 52+ |
| LMS platforms with MCP servers | 4 (Canvas, Moodle, D2L, Google Classroom) |
| Highest-starred server | arxiv-mcp-server (2,700, +4%) |
| Fastest-growing server | paper-search-mcp (1,500 stars, +25% in 28 days) |
| Official vendor servers | 1 (Udemy Business, GA) |
| MOOC platforms with MCP coverage | 3 (Udemy GA, Coursera scraper, Khan Academy minimal) |
| AI-in-education bills (2026) | 134 across 31 US states |

## LMS Integration

### Canvas LMS — DMontgomery40/mcp-canvas-lms

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | ~96 | TypeScript | — | 50+ tools |

Comprehensive Canvas coverage across three user types:

- **Students** — course access, assignment submission, grade tracking, discussion participation, file management, calendar events
- **Instructors** — course creation, assignment management, grading, student enrollment, quiz administration, rubric handling
- **Account administrators** — user management, account oversight, reporting, sub-account administration

Version 2.3.0 introduced streamable HTTP transport support, Docker deployment options, and automatic retries with pagination. The server supports both stdio and HTTP transport modes.

### Canvas LMS — vishalsachdev/canvas-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | ~107 | Python/TypeScript | MIT | 88 tools + 8 agent skills |

**Now the most-starred Canvas implementation**, with **FERPA-compliant data anonymization** for educator use — a critical differentiator for institutional deployment. **v1.2.0** (April 2026) added role-based tool filtering, expanded the accessibility scanner from 4 to **20 checks**, security hardening, and Windows compatibility improvements. **May 2026** added two new tools: `create_rubric` (PR #100) for programmatic rubric creation with criteria, ratings, and optional assignment association, and `read_course_file` enabling remote MCP deployments to read Canvas file content without local file system access.

Offers 8 agent skills via `skills.sh` for 40+ coding agents, a code execution API for token-efficient bulk operations, and a hosted server option requiring no local installation. Supports Claude Desktop, Cursor, Zed, Windsurf, Continue, Replit, Copilot Studio, and other MCP-compatible clients. The learning designer capabilities include course quality control and accessibility auditing — features no other Canvas MCP server offers.

### Other Canvas Implementations

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | ~12 | TypeScript | — | 25+ tools |
| [ahnopologetic/canvas-lms-mcp](https://github.com/ahnopologetic/canvas-lms-mcp) | — | TypeScript | — | 22 tools |
| [akshsgaur/CMUCanvasMCPServer](https://github.com/akshsgaur/CMUCanvasMCPSErver) | — | — | — | CMU-specific |
| [lucanardinocchi/canvas-mcp](https://github.com/lucanardinocchi/canvas-mcp) | — | TypeScript | — | Multiple |
| [mtgibbs/canvas-lms-mcp](https://github.com/mtgibbs/canvas-lms-mcp) | — | TypeScript | — | Multiple |

At least five additional Canvas MCP servers exist, ranging from minimal read-only grade checkers to university-specific implementations (CMU). r-huijts/canvas-mcp grew to 12 stars with privacy-first anonymization and a PulseMCP listing. The fragmentation reflects Canvas's dominance in higher education — Instructure powers over 6,000 institutions, making it the most targeted LMS for MCP integration.

### Moodle MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | ~36 | JavaScript | MIT | 9 tools |

The leading Moodle MCP server provides tools across four management categories:

- **Course management** — `get_courses` with pagination
- **Student oversight** — `list_students` with ID, name, email, last access
- **Assignment handling** — `get_assignments`, `get_student_submissions`, `provide_assignment_feedback`
- **Assessment** — `get_quizzes`, `get_quiz_attempts`, `provide_quiz_feedback`

Requires Node.js v14+ and a Moodle API token with appropriate permissions. A second implementation, [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) (16 stars), offers a Python alternative focused on upcoming events.

The grading and feedback tools make this genuinely useful for instructors managing large courses — an AI assistant can review submissions, generate feedback drafts, and submit grades through natural language commands.

### Google Classroom MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server) | ~3 | JavaScript | MIT | 3 tools |

A minimal implementation providing read-only access to Google Classroom data:

- **courses** — list all courses
- **course-details** — detailed course info with announcements
- **assignments** — assignment data for a course

Uses OAuth 2.0 authentication with automatic token refresh. Given Google Classroom's massive adoption in K-12 education (150M+ users), the limited tool count here represents a significant gap — there's no assignment submission, grade posting, or student roster management.

### D2L Brightspace MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) | ~14 | — | MIT | 7+ areas |
| [joshuasoup/d2l-mcp](https://github.com/joshuasoup/d2l-mcp) | — | — | — | 12 tools |
| [bencered/d2l-mcp-server](https://github.com/bencered/d2l-mcp-server) | — | — | — | 12 tools |

D2L Brightspace went from a single MCP implementation to **three competing servers** — the fastest LMS expansion in this review cycle. RohanMuppa's server (14 stars, created Feb 2026) is the most-starred, with v1.0.4, AES-256-GCM credential encryption, and compatibility with any school running D2L Brightspace. joshuasoup/d2l-mcp adds file downloads and text extraction. bencered's original provides automated SSO authentication and persistent session storage.

A student-focused implementation by [pranav-vijayananth/brightspace-mcp-server](https://github.com/pranav-vijayananth/brightspace-mcp-server) at Purdue University also exists. D2L Brightspace is also available on the Pipedream MCP marketplace.

The ethical note in bencered's repository is worth highlighting: "This should NOT be used to cheat on any assignments or to gain an unfair advantage... only intended to enable agents to better understand assignment scheduling and to help with learning of course material."

## Flashcards & Spaced Repetition

### Anki MCP Server — ankimcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | ~237 | TypeScript | AGPL-3.0 | 21+ tools |

The most comprehensive Anki integration, with tools organized into five categories:

- **Review & Study** (4 tools) — quiz sessions, card scheduling, review tracking
- **Deck Management** (4 tools) — create, organize, and configure decks
- **Note Management** (6 tools) — CRUD operations with batch support (up to 100 notes), Anki query syntax
- **Media Management** (4 tools) — audio/image handling with multiple upload methods
- **Model/Template Management** (3 tools) — template configuration with HTML/CSS awareness

Deployment flexibility is a standout feature: local stdio, HTTP server, or **ngrok-tunneled remote access** for web-based AI tools. Includes a read-only safety mode to prevent accidental modifications. **v0.15.1** (April 9, 2026) added layered security validation for media operations: MIME type allowlist blocking non-media files (SSH keys, credentials, `.env` files), and SSRF prevention blocking requests to private networks, loopback addresses, and cloud metadata endpoints (169.254.169.254).

**New: ankimcp/anki-mcp-server-addon** — a companion native Anki addon that implements an MCP server directly inside Anki, eliminating the AnkiConnect dependency entirely. The ankimcp organization also launched **ankimcp.ai**, a professional documentation site with guides and real-world examples.

### Anki MCP — arielbk

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [arielbk/anki-mcp](https://github.com/arielbk/anki-mcp) | ~9 | TypeScript | MIT | 7 tools |

A lighter Anki implementation focused on conversational flashcard management. Features include quizzing on specific cards, creating flashcards about topics, turning PDFs into spaced repetition cards, generating cloze deletion cards from lecture notes, deep analytics on learning progress, and bulk operations for thousands of cards.

### Other Anki Implementations

| Server | Language | License | Focus |
|--------|----------|---------|-------|
| [dhkim0124/anki-mcp-server](https://github.com/dhkim0124/anki-mcp-server) | Python | MIT | Natural language card creation |
| [nailuoGG/anki-mcp-server](https://github.com/nailuoGG/anki-mcp-server) | TypeScript | — | AnkiConnect bridge |
| [ezynda3/anki-mcp](https://github.com/ezynda3/anki-mcp) | — | MIT | Programmatic card management |

The Anki ecosystem mirrors Canvas — multiple implementations competing on different axes. The ankimcp version wins on features and stars; arielbk/anki-mcp wins on simplicity. All require the AnkiConnect plugin running locally.

## Academic Research

### arXiv MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | ~2,600 | Python | MIT | 8 tools |

The **highest-starred education MCP server** by a wide margin, now at **~2,700 stars** (+4% in 28 days), with **8 tools** across paper search, download, list, read, plus four experimental tools:

- **Semantic Search** — vector-based similarity search across downloaded papers
- **Citation Graph** — explore citation relationships between papers
- **Watch Topic** — set up alerts for new papers in specific areas
- **Check Alerts** — review papers matching watched topics

Includes a set of research prompts for comprehensive paper analysis workflows. The star count reflects broad adoption beyond education — researchers, developers, and AI practitioners all use arXiv daily. The license is MIT.

### Paper Search MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) | ~1,200 | Python | MIT | 20+ sources |

**The fastest-growing education MCP server** — stars surged from 1,200 to **1,500 (+25%)** in 28 days, continuing its steep growth trajectory (it was at 791 six weeks ago). Now aggregates **20+ academic sources**, including:

- arXiv, PubMed, bioRxiv, medRxiv, Google Scholar, IACR ePrint Archive, Semantic Scholar, Crossref, OpenAlex, and more

Uses a free-first strategy with OA-first fallback chain, standardized `Paper` class for consistent output across platforms, async request handling via httpx, and an extensible architecture. Optional Sci-Hub integration for full paper downloads. Claude Code skills integration added.

### Academic Search MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [afrise/academic-search-mcp-server](https://github.com/afrise/academic-search-mcp-server) | — | Python | — | Multiple |

Focused on **Semantic Scholar and Crossref** integration, providing comprehensive metadata including title, authors, year, DOI, venue, open access status, PDF URLs, abstracts, and TL;DR summaries. Citation generation in BibTeX and APA formats.

## Enterprise Learning

### Udemy Business MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Udemy Business MCP | — | — | Commercial | Multiple |

The **first publicly-traded EdTech company to ship a production MCP server**. Udemy Business AI Connectors went **GA on March 31, 2026** — moving from preview to general availability. Implements MCP spec version 2025-11-25 with OAuth and static client credentials. Key capabilities:

- **On-demand support** — real-time problem-solving via micro-courses and curated lessons
- **Plug-and-play integration** — pre-built MCP connectors for ChatGPT, Claude, Cursor, custom enterprise agents
- **Role-specific contextualization** — content matched to user's role and learning context
- **Intelligent content matching** — relevant course recommendations within existing AI tools

This is an enterprise product aimed at corporate L&D teams (paid add-on, pricing undisclosed), not individual learners. The GA launch is the most significant commercial EdTech MCP deployment — a publicly-traded company with full production MCP infrastructure validates the protocol's relevance beyond developer tooling.

## Assessment & Tutoring

### EduBase MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [EduBase/MCP](https://github.com/EduBase/MCP) | ~25 | TypeScript | MIT | Dynamic (API-based) |

Connects AI to the **EduBase e-learning platform** with features that matter for institutional deployment:

- Advanced quiz system with **parametrization and LaTeX support**
- Unified learning environment: videos, exams, documents, SCORM modules
- Enterprise-grade security with SSO and **GDPR compliance**
- Multiple transport protocols (stdio, SSE, streamable HTTP)
- AI-assisted content transformation — turn existing materials into interactive assessments

Each documented API endpoint is exposed as a separate tool (`edubase_<method>_<endpoint>`), making the tool count dynamic based on the platform version.

### Assessment Suite MCP

An MCP server enabling AI-generated quiz export in multiple formats (CSV, PDF, JSON, Markdown). Bridges the gap between AI question generation and classroom-ready assessment materials — educators can generate questions conversationally and export them directly to their preferred format without manual copy-pasting.

## STEM Computation

### Wolfram Alpha MCP Servers

| Server | Language | Focus |
|--------|----------|-------|
| [Garoth/wolframalpha-llm-mcp](https://github.com/Garoth/wolframalpha-llm-mcp) | TypeScript | Structured knowledge + math |
| [StoneDot/wolframalpha-mcp-server](https://github.com/StoneDot/wolframalpha-mcp-server) | TypeScript | Computational queries |
| [akalaric/mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha) | Python | LangChain integration |
| [cnosuke/mcp-wolfram-alpha](https://github.com/cnosuke/mcp-wolfram-alpha) | Go | API access |

Multiple implementations exist for connecting AI to Wolfram Alpha's computational engine. The core value proposition is **delegating numerical computation that LLMs struggle with** — derivatives, integrals, equation solving, statistics, physics constants, unit conversions, chemical reactions. All require a Wolfram Alpha API key.

For STEM education specifically, these servers enable AI tutors to show their work: an LLM can explain the concepts while Wolfram Alpha handles the actual computation, combining pedagogical reasoning with mathematical precision.

### Wikipedia MCP Servers

Several implementations provide AI access to Wikipedia's knowledge base, with features including article search, content retrieval, section extraction, related topic discovery, and multi-language support. Useful as a reference layer for educational AI applications — grounding explanations in encyclopedic sources rather than relying solely on the LLM's training data.

## New Entrants (Since March 2026 — Updated May 2026)

### OpenEdu MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Cicatriiz/openedu-mcp](https://github.com/Cicatriiz/openedu-mcp) | ~7 | — | — | 21+ tools |

A **curriculum-aligned educational MCP server** pulling from Open Library, Wikipedia, Dictionary API, and arXiv. The key differentiator: **grade-level filtering** from K-2 through College, with curriculum alignment to **Common Core and NGSS** (Next Generation Science Standards). Includes SQLite caching for performance. The first MCP server to explicitly target K-12 curriculum standards — a notable gap-filler.

### Khan Academy MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aicoder2009/khanacademyMCP](https://github.com/aicoder2009/khanacademyMCP) | ~1 | — | MIT | 12 tools |

The **first Khan Academy MCP server** — tools include search, list_subjects, get_topic_tree, get_content, get_course, and get_transcript. No API key required. Very early stage (1 star), but fills a conspicuous gap — Khan Academy is one of the largest free educational platforms (120M+ registered users) and was previously absent from the MCP ecosystem entirely.

### Coursera MCP (nwolke/coursera-mcp)

The **first Coursera MCP integration** — a Playwright-based scraper that reads your Coursera "my-learning" page and exposes learning progress as MCP tools for Claude, including progress percentages for all in-progress courses. Early stage and scraper-based (not an official Coursera API), but fills a conspicuous gap — Coursera was previously completely absent from the MCP ecosystem. A second implementation (EmilyThaHuman/coursera-mcp-server) also appeared on GitHub.

### O'Reilly Learning Platform MCP

Added to PulseMCP — integrates with O'Reilly's learning platform API to search and retrieve technical content from their extensive library of books, videos, and courses. Useful for corporate L&D teams and developers who want AI assistants to surface O'Reilly content inline with their workflows.

### Additional New Servers on PulseMCP

- **Smartschool MCP** (by MauroDruwel) — course, grades, and assignment management for the Belgian Smartschool platform
- **OpenEMIS MCP** (by tixuz) — education management information system integration
- **Duolingo Game Status MCP** (by Sniffleupagus, March 24, 2026) — streaks, XP, language courses (note: Duolingo's internal 180+ MCP tools remain enterprise-only)
- **School Tools MCP** — combined Canvas + Gradescope integration for tracking assignment deadlines and syncing to macOS Reminders
- **Skool MCP** (by louiewoof2026) — community platform integration for the Skool learning community platform

## AI-in-Education Policy Context

A regulatory wave is creating both urgency and uncertainty for education MCP adoption:

- **134 AI-in-education bills** introduced across 31 US states in the 2026 legislative session
- **Ohio** mandates all public school districts adopt formal AI policies by July 1, 2026
- **Maryland** requires AI guidance, AI literacy integration, AI coordinators, and university-certified compliant AI tools
- 50-84% of K-12 students already use AI for schoolwork; ~90% in higher education
- Only 13% of schools have formal AI policies despite 87% teacher interest
- Only 48% of institutions have formal AI policies; just 6% of teachers say those policies are clear

The policy fragmentation may slow institutional MCP adoption (IT departments hesitate without clear guidance), but mandates like Ohio's push districts toward structured, auditable AI tooling — exactly what MCP provides.

## What's missing

The education MCP ecosystem has significant gaps:

- **Major LMS platforms** — Blackboard, Sakai, Open edX, Schoology have zero MCP implementations
- **MOOC platforms** — Coursera now has a scraper-based MCP (unofficial); no LinkedIn Learning or edX; Udemy GA, Khan Academy minimal (1 star)
- **Student information systems** — no Banner, PowerSchool, Infinite Campus, or Ellucian SIS connectivity
- **Library systems** — no OCLC WorldCat, Ex Libris Alma, or MARC catalog integrations
- **Academic integrity** — no Turnitin, Grammarly, or plagiarism detection tools
- **Adaptive learning** — no adaptive engines (Knewton, ALEKS, DreamBox) have MCP support
- **Standardized testing** — no SAT, GRE, AP, or state assessment integrations
- **Learning analytics** — no xAPI/Caliper, learning record stores, or analytics dashboards
- **Proctoring** — no Respondus, ExamSoft, or ProctorU integrations
- **K-12 specific** — Google Classroom support is minimal (3 read-only tools for a platform with 150M+ users)

## The bottom line

The education MCP server ecosystem is **fragmented but growing fast**. In the past 28 days: paper-search-mcp surged 25% to 1,500 stars (continuing its steep upward trajectory), arXiv MCP reached 2,700 stars, Anki MCP received critical security hardening plus a native addon eliminating the AnkiConnect dependency, Canvas gained new educator tools (`create_rubric`, `read_course_file`), and Coursera received its first MCP integration — a scraper-based server that moves one more MOOC from "absent" to "covered."

Udemy Business MCP remains the commercial anchor — the first publicly-traded EdTech company with production MCP infrastructure, now approaching two months of GA. LinkedIn Learning remains the most significant MOOC gap.

The policy landscape continues to create tailwinds: 134 AI-in-education bills across 31 states, Ohio mandating formal AI policies by July 2026. Structured, auditable AI tooling is increasingly mandated — but the MCP ecosystem still has the wrong shape for institutional deployment (strong on research tools, weak on administrative infrastructure).

The ecosystem remains deeply incomplete. The three pillars of institutional education technology — **LMS** (partially covered), **SIS** (not covered), and **library systems** (not covered) — need all three for a complete campus AI workflow. Blackboard's absence is conspicuous. Academic integrity tools (Turnitin) and adaptive learning engines are still missing entirely.

**Rating: 3.5/5 held.** Paper-search-mcp's continued surge (+25%), Anki security hardening, canvas-mcp new tools, and the first Coursera coverage are solid incremental progress. But no structural change — Blackboard still absent, SIS/library still uncovered, Google Classroom still minimal (3 read-only tools for 150M+ users). This category could reach 4.0 if Blackboard or a major SIS vendor ships MCP support.

*This review was last refreshed on 2026-05-20 using Claude Sonnet 4.6 (Anthropic).*
