# Education & LMS MCP Servers — Canvas, Moodle, Google Classroom, Anki, LeetCode, and More

> Education and LMS MCP servers are connecting AI agents to learning management systems, study tools, and educational content via the Model Context Protocol.


*Part of the [Education & Learning](/categories/education-learning/) category.*

Education and LMS MCP servers are connecting AI agents to learning management systems, study tools, and educational content platforms. Instead of navigating complex LMS APIs or manually managing coursework, these servers let agents access courses, grade assignments, create flashcards, search educational content, and tutor students — all through the Model Context Protocol.

The landscape spans seven areas: **LMS platforms** (Canvas dominates with 6+ implementations, plus Moodle, Google Classroom, and Brightspace), **educational content** (e-learning platforms and open educational resource aggregators), **spaced repetition** (Anki integration), **coding education** (LeetCode problem access and guided learning), **math and tutoring** (calculation, visualization, and interactive teaching), **academic research** (unified scholarly search), and **language learning** (dictionary tools).

The headline findings: **Canvas LMS has more MCP implementations than any other education platform** — six independent servers from both instructor and student perspectives. **[vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) leads with [92 tools and 8 agent skills](https://github.com/vishalsachdev/canvas-mcp/releases/tag/v1.2.0)** (96 stars) including FERPA-compliant data anonymization and rubric-based bulk grading. **[DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) is the most starred** at 94 stars with 50+ tools. **[ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) provides the deepest study tool integration** with [33 tools](https://github.com/ankimcp/anki-mcp-server/releases/tag/v0.15.0) (219 stars) for full Anki deck and card management. **[jinzcdev/leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server) supports both leetcode.com and leetcode.cn** (104 stars) with [17 tools including code execution and submission](https://github.com/jinzcdev/leetcode-mcp-server/releases/tag/v1.3.0). **Instructure announced IgniteAgent** — the first major LMS vendor to officially adopt MCP as its agent integration standard. **No Blackboard, Khan Academy, Coursera, edX, or Duolingo MCP servers exist** despite their massive user bases.

## LMS Platforms — Canvas

### vishalsachdev/canvas-mcp (Most Feature-Rich)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | [96](https://github.com/vishalsachdev/canvas-mcp/stargazers) | Python | MIT | [92](https://github.com/vishalsachdev/canvas-mcp/releases/tag/v1.2.0) |

The most comprehensive Canvas MCP server by a wide margin. Provides **[92 tools and 8 agent skills](https://github.com/vishalsachdev/canvas-mcp#readme)** covering the full Canvas LMS workflow:

- **Course management** — list courses, access syllabi, modules, pages
- **Discussion and announcement tools** — create and manage forum interactions
- **Assignment tools with analytics** — submission tracking, deadline management
- **Rubric tools with bulk grading** — grade multiple students against rubric criteria in one operation
- **FERPA-compliant data anonymization** — student data privacy built into the server design
- **Code execution environment** — run code against the Canvas API directly

Ships with separate Student Guide and Educator Guide documentation. Compatible with Claude Desktop, Cursor, Codex, Windsurf, and 40+ other agents. [v1.2.0](https://github.com/vishalsachdev/canvas-mcp/releases/tag/v1.2.0) (April 2026) added role-based tool filtering via `CANVAS_ROLE` environment variable, expanded accessibility scanner from 4 to 20 WCAG checks with automated remediation, and Windows compatibility improvements. Also available as a hosted server at mcp.illinihunt.org.

### DMontgomery40/mcp-canvas-lms (Most Starred)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | [94](https://github.com/DMontgomery40/mcp-canvas-lms/stargazers) | TypeScript | MIT | [50+](https://github.com/DMontgomery40/mcp-canvas-lms#readme) |

The most starred Canvas MCP server with **50+ tools** (Core Student: 33, Instructor: 13, Account Management: 7) organized around core LMS operations:

- **Course management** — courses, modules, content pages
- **Assignments and submissions** — create, manage, grade
- **Enrollment management** — student and instructor role handling
- **Grade management** — gradebook access and updates

TypeScript implementation with clean API design. Now supports [streamable HTTP transport](https://github.com/DMontgomery40/mcp-canvas-lms) for containerized deployments (Docker/Kubernetes). The MIT license and active maintenance make this the most accessible Canvas server for developers building integrations.

### aryankeluskar/canvas-mcp (Canvas + Gradescope)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aryankeluskar/canvas-mcp](https://github.com/aryankeluskar/canvas-mcp) | [11](https://github.com/aryankeluskar/canvas-mcp/stargazers) | TypeScript | ISC | 8+ |

Unique dual integration combining **Canvas LMS and Gradescope** in one server. Natural language queries for courses and assignments, submission status tracking across both platforms. Uses Gemini API for intelligent resource search across course materials.

### 54yyyu/school-mcp (Canvas + Gradescope + Calendar)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [54yyyu/school-mcp](https://github.com/54yyyu/school-mcp) | — | TypeScript | — | Multiple |

A student-focused server combining **Canvas, Gradescope, and macOS Calendar/Reminders** integration. Fetches assignment deadlines from both platforms and syncs them to the system calendar via AppleScript. File download from Canvas included. macOS-only for calendar features.

### r-huijts/canvas-mcp (Privacy-First)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | [12](https://github.com/r-huijts/canvas-mcp/stargazers) | TypeScript | — | [24](https://github.com/r-huijts/canvas-mcp#readme) |

Available as a **Claude Desktop Extension** for one-click installation. Privacy-by-default design — student data anonymized automatically. API tokens stored in the OS keychain rather than config files. Covers courses, announcements, rubrics, assignments, modules, pages, and student data.

### Other Canvas Servers

- **ahnopologetic/canvas-lms-mcp** (Python) — lightweight with 22 tools for syllabus, modules, assignments, and grade access
- **lucanardinocchi/canvas-mcp** (TypeScript) — natural conversation interface for coursework across 6 modules (courses, assignments, submissions, discussions, modules, search)

### Instructure IgniteAgent (Official — Upcoming)

Instructure, the company behind Canvas LMS, announced **IgniteAgent** at InstructureCon 2025 — a conversational AI assistant that uses **MCP as its third-party integration standard**. This is the first major LMS vendor to officially adopt the Model Context Protocol. IgniteAgent will handle multi-step tasks (extending deadlines, converting PDFs, managing course workflows) and allow third-party agents to integrate via MCP. Expected availability in 2026 as a premium product. This is a significant signal for the future of MCP in education.

## LMS Platforms — Moodle

### peancor/moodle-mcp-server (Read + Write)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | [35](https://github.com/peancor/moodle-mcp-server/stargazers) | JavaScript | MIT | [10](https://github.com/peancor/moodle-mcp-server#readme) |

The most complete Moodle MCP server, and notably one of the few education servers with **full read AND write access**:

- **list_students** — retrieve enrolled students
- **get_assignments** / **get_student_submissions** — access coursework
- **provide_assignment_feedback** — write feedback directly to Moodle
- **get_quizzes** / **get_student_quiz_attempts** — quiz data access
- **provide_quiz_feedback** — write quiz feedback

This write capability is significant — an AI agent can review student submissions and provide feedback directly through the LMS, not just read data. Requires a Moodle API token.

### loyaniu/moodle-mcp (Lightweight)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) | 2 | Python | — | Limited |

A lightweight Moodle server focused on **event retrieval** via FastMCP. Primarily provides get_upcoming_events for deadline tracking. Early development stage with limited functionality.

## LMS Platforms — Google Classroom & Brightspace

### faizan45640/google-classroom-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server) | [2](https://github.com/faizan45640/google-classroom-mcp-server/stargazers) | JavaScript | MIT | 3 |

Basic Google Classroom integration with three tools: course listing, course details, and assignment access. Requires Google API credentials and OAuth setup. Given Google Classroom's massive deployment in K-12 education, the minimal MCP coverage here is a notable gap.

### pranav-vijayananth/brightspace-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pranav-vijayananth/brightspace-mcp-server](https://github.com/pranav-vijayananth/brightspace-mcp-server) | — | Python | Apache-2.0 | Limited |

A creative solution for **D2L Brightspace** — since students lack official API access, this server uses **Playwright web scraping** to extract course lists, assignments, and grades. Includes automated Duo Mobile 2FA support. Built by a Purdue University student specifically for their institution's Brightspace instance. Fragile by nature (web scraping), but demonstrates real student demand for LMS AI integration.

## Educational Content & Courseware

### EduBase/MCP (Official E-Learning Platform)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [EduBase/MCP](https://github.com/EduBase/MCP) | [24](https://github.com/EduBase/MCP/stargazers) | TypeScript | [MIT](https://github.com/EduBase/MCP/blob/main/LICENSE) | Many |

Official MCP server from the **EduBase e-learning platform**, exposing the full platform API as MCP tools (each endpoint becomes a tool named `edubase_<method>_<endpoint>`). Key capabilities:

- **Advanced quiz system** — parametric question generation, randomization, auto-grading
- **Cheating detection** — real-time monitoring during assessments
- **SCORM module support** — industry-standard courseware compatibility
- **SSO integration** — institutional authentication
- **GDPR compliance** — data protection built in
- **Triple transport** — stdio, SSE, and streamable HTTP

Supports Docker deployment for self-hosted instances. Very actively maintained with [28 releases](https://github.com/EduBase/MCP/releases) through v1.1.5 (April 2026). Also installable via [Smithery](https://github.com/EduBase/MCP#readme) or remote MCP server.

### Cicatriiz/openedu-mcp (Open Educational Resources)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Cicatriiz/openedu-mcp](https://github.com/Cicatriiz/openedu-mcp) | [7](https://github.com/Cicatriiz/openedu-mcp/stargazers) | Python | — | [21+](https://github.com/Cicatriiz/openedu-mcp#readme) |

An educational resource discovery server aggregating **four free APIs** into a unified interface:

- **OpenLibrary** — book search and metadata
- **Wikipedia** — encyclopedia article access
- **arXiv** — academic paper search
- **Dictionary API** — word definitions and usage

Includes **grade-level appropriateness filtering** for K-12 contexts and curriculum planning support. Available via stdio, HTTP, and SSE transports.

### odewahn/orm-discovery-mcp (O'Reilly Learning — Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [odewahn/orm-discovery-mcp](https://github.com/odewahn/orm-discovery-mcp) | 3 | Python | — | [1](https://github.com/odewahn/orm-discovery-mcp#readme) |

Built by **[O'Reilly CTO Andrew Odewahn](https://github.com/odewahn)**, this official server provides search access to O'Reilly's extensive technical book and article library via a single `search_content` tool. Returns structured metadata including titles, authors, ratings, and direct URLs. Launched November 2025. Requires an O'Reilly subscription for full content access.

### EduChain MCP Servers (AI Content Generation)

Multiple community implementations wrapping the **educhain Python library** for AI-powered educational content generation:

- **MCQ Generator** — create multiple-choice questions with options, correct answers, and explanations
- **Lesson Plan Generator** — structured lesson plans from topics
- **Flashcard Generator** — study material creation

Uses local LLMs (Mistral-7B-Instruct) for generation. Implementations include abanindra3/educhain-mcp and yogasairam/educhain-mcp-server-final. Quality depends on the underlying model.

## Education Data

### ckz/edu_data_mcp_server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ckz/edu_data_mcp_server](https://github.com/ckz/edu_data_mcp_server) | — | Python | — | 2 |

Accesses the **Urban Institute's Education Data API** for US education statistics:

- **get_education_data** — query enrollment, school/district directories, financial data
- **get_education_data_summary** — aggregation and summary statistics

Covers schools, districts, colleges, and universities using data from CCD, IPEDS, and CRDC datasets. Read-only, US education data only.

## Spaced Repetition & Study Tools

### ankimcp/anki-mcp-server (Most Complete Study Tool)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | [219](https://github.com/ankimcp/anki-mcp-server/stargazers) | TypeScript | — | [33](https://github.com/ankimcp/anki-mcp-server/releases/tag/v0.15.0) |

The most feature-rich study tool MCP server with **[33 tools](https://github.com/ankimcp/anki-mcp-server/releases/tag/v0.15.0)** for full Anki integration:

- **Deck management** — sync, create, list, organize decks
- **Card review** — study cards through the MCP interface
- **Note and card management** — create, modify, delete with media file support
- **Evidence-based creation** — includes a `twenty_rules` prompt implementing SuperMemo's 20 Rules of Formulating Knowledge for optimal flashcard design
- **Dual modes** — STDIO for desktop clients, Web mode (with integrated ngrok tunneling) for Claude.ai and ChatGPT

Currently at [v0.15.1](https://github.com/ankimcp/anki-mcp-server/releases/tag/v0.15.1) (active beta, April 2026). Recent releases added [bulk note creation](https://github.com/ankimcp/anki-mcp-server/releases/tag/v0.14.0) (up to 100 notes per call), [MCP Tool Annotations](https://github.com/ankimcp/anki-mcp-server/releases/tag/v0.15.0) with structured metadata, and media security hardening (MIME allowlists, SSRF prevention, filename sanitization). Published on npm as [@ankimcp/anki-mcp-server](https://www.npmjs.com/package/@ankimcp/anki-mcp-server). Requires Anki desktop running locally.

### Other Anki Servers

- **nailuoGG/anki-mcp-server** (Python) — AnkiConnect-based with deck management and note creation
- **scorzeth/anki-mcp-server** — card review and creation via AnkiConnect
- **johwiebe/anki-mcp** (Python) — basic Anki MCP integration

The presence of 4+ Anki MCP servers reflects strong demand from the spaced repetition community for AI-assisted flashcard creation and study workflows.

## Coding Education

### jinzcdev/leetcode-mcp-server (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jinzcdev/leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server) | [104](https://github.com/jinzcdev/leetcode-mcp-server/stargazers) | TypeScript | MIT | [17](https://github.com/jinzcdev/leetcode-mcp-server/releases/tag/v1.3.0) |

The most starred coding education MCP server, supporting both **leetcode.com (Global) and leetcode.cn (China)** with [17 tools](https://github.com/jinzcdev/leetcode-mcp-server#readme) across five categories:

- **Problems** (3 tools) — question details, constraints, examples, advanced search by tags/difficulty/topic
- **Users** (7 tools) — profiles, submission history, solved problems (with optional authentication)
- **Submissions** (2 tools) — submission retrieval and history
- **Notes** (3 tools) — personal notes management
- **Solutions** (2 tools) — community and official solutions

[v1.3.0](https://github.com/jinzcdev/leetcode-mcp-server/releases/tag/v1.3.0) (March 2025) added **run_code and submit_solution tools** — agents can now execute code against LeetCode test cases and submit solutions directly, not just read problems. Published on [NPM](https://www.npmjs.com/package/leetcode-mcp-server) for easy installation. The dual-region support makes this the only coding education server serving both English and Chinese-speaking developer communities.

### SPerekrestova/interactive-leetcode-mcp (Pedagogical)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SPerekrestova/interactive-leetcode-mcp](https://github.com/SPerekrestova/interactive-leetcode-mcp) | [9](https://github.com/SPerekrestova/interactive-leetcode-mcp/stargazers) | TypeScript | MIT | [10](https://github.com/SPerekrestova/interactive-leetcode-mcp#readme) |

Takes a deliberately **pedagogical approach** to coding education. Instead of just providing answers, it enforces progressive learning:

- **4-level hint system** — gives increasingly specific hints before revealing solutions
- **Pedagogical best practices** — encourages independent problem-solving
- **Agent skill** — structured session flow for guided DSA (Data Structures & Algorithms) learning

Now at [v3.2.1](https://github.com/SPerekrestova/interactive-leetcode-mcp/releases) with multi-language support (Java, Python, C++, JavaScript, TypeScript) and Claude Code/ClawHub integrations. This design philosophy — making AI assist learning rather than bypass it — is a standout in the education MCP space.

### doggybee/mcp-server-leetcode

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [doggybee/mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode) | — | TypeScript | — | Multiple |

LeetCode access via GraphQL with metadata filtering, user profiles, submission history, and contest data. Another option for developers who want LeetCode integration without the pedagogical constraints of interactive-leetcode-mcp.

## Math & Tutoring

### clouatre-labs/math-mcp-learning-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [clouatre-labs/math-mcp-learning-server](https://github.com/clouatre-labs/math-mcp-learning-server) | [3](https://github.com/clouatre-labs/math-mcp-learning-server/stargazers) | Python | Apache 2.0 | [17](https://github.com/clouatre-labs/math-mcp-learning-server/releases/tag/v0.12.1) |

A dedicated math education server with **[17 tools](https://github.com/clouatre-labs/math-mcp-learning-server#readme)** across workspace, math, matrix, and visualization categories:

- **calculate** / **statistics** / **compound_interest** / **matrix_multiply** — math operations
- **convert_units** — unit conversion
- **plot_function** / **create_histogram** / **plot_line_chart** / **plot_scatter_chart** / **plot_box_plot** / **plot_financial_line** — data visualization
- **math_tutor** — interactive math tutoring prompts
- **formula_explainer** — break down mathematical formulas step by step

Built with FastMCP 2.0 and the official MCP Python SDK. Includes persistent workspace for ongoing calculations. Available on [PyPI](https://pypi.org/project/math-mcp-learning-server/) and the [MCP Registry](https://github.com/clouatre-labs/math-mcp-learning-server#readme), with cloud hosting at math-mcp.fastmcp.app/mcp. Holds [OpenSSF Best Practices Silver certification](https://github.com/clouatre-labs/math-mcp-learning-server) — unusually high quality bar for a 3-star project (267 commits). Now at [v0.12.1](https://github.com/clouatre-labs/math-mcp-learning-server/releases/tag/v0.12.1) (April 2026).

### moarshy/mcp-tutor (Documentation-to-Lessons)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [moarshy/mcp-tutor](https://github.com/moarshy/mcp-tutor) | — | Python | — | 4 tools, 6 prompts |

Transforms **GitHub documentation repositories into interactive educational content**. Uses document-level processing with tool-augmented generation (TAG) for context-aware teaching. An interesting approach — turning existing open-source documentation into structured lessons without manual content creation.

## Academic Research Tools

### aringadre76/mcp-for-research (Unified Search)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aringadre76/mcp-for-research](https://github.com/aringadre76/mcp-for-research) | — | TypeScript | — | 5 |

Consolidates **PubMed, Google Scholar, arXiv, and JSTOR** into a unified search interface. Replaced 24 individual endpoint tools with 5 consolidated tools for a cleaner agent experience. Published on NPM.

### Other Academic Servers

- **JackKuo666/Google-Scholar-MCP-Server** (Python) — Google Scholar search with paper access
- **zongmin-yu/semantic-scholar-fastmcp-mcp-server** (Python) — Semantic Scholar API for paper data, author info, and citation network exploration
- **afrise/academic-search-mcp-server** — dual Semantic Scholar and Crossref integration
- **MicrosoftDocs/mcp** — official Microsoft Learn documentation server with search, article fetch, and code samples (free, no auth required)

## Language Learning

### meowrain/mcp-server-cambridge-dict

Cambridge Dictionary integration providing word lookup with pronunciation, definitions, and example sentences.

### Traves-Theberge/Word_of_the_day

Daily vocabulary learning via the free Dictionary API with word definitions and random vocabulary features.

## What's Missing

The gaps in education MCP servers are striking:

- **Blackboard/Ultra** — no MCP server despite being the second-largest LMS globally
- **Khan Academy** — no MCP server despite being the most popular free learning platform
- **Coursera / edX** — no MCP servers for the two largest MOOC platforms
- **Duolingo / Memrise** — no language learning app integration
- **PowerSchool** — no student information system MCP servers
- **Turnitin** — no plagiarism detection integration
- **Classroom management** (attendance, behavior tracking) — completely absent

The concentration around Canvas (6+ servers) versus the absence of Blackboard (0 servers) likely reflects Canvas's developer-friendly API and the university CS student demographic most likely to build MCP servers.

## The Bottom Line

**Rating: 3.5 / 5** — Canvas LMS integration is genuinely impressive, with the deepest MCP coverage of any single education platform. Spaced repetition (Anki) and coding education (LeetCode) are well-served. The pedagogical approach of interactive-leetcode-mcp — progressive hints rather than instant answers — shows thoughtful design for learning contexts. EduBase's official server brings enterprise e-learning features. However, the category suffers from massive platform gaps: the biggest names in education (Blackboard, Khan Academy, Coursera, Duolingo) have zero MCP presence. Google Classroom, used by hundreds of millions of students globally, has just 3 tools. Most servers are student projects rather than vendor-supported products. The bright spot: Instructure's IgniteAgent announcement signals that LMS vendors are beginning to take MCP seriously, which could catalyze broader adoption in 2026.

*ChatForest independently researches MCP servers using publicly available information — GitHub repositories, documentation, and community discussions. We do not have hands-on access to every server reviewed. Star counts reflect the time of research and may have changed. Always verify server status and compatibility before adopting any MCP server for your workflow.*

*This review was last updated on 2026-04-11 using Claude Opus 4.6 (Anthropic).*

