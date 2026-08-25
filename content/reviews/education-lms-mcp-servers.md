---
title: "Education & LMS MCP Servers — Canvas, Moodle, Google Classroom, Anki, LeetCode, and More"
date: 2026-03-15T10:26:00+09:00
sources_audited: 2026-08-26
description: "Education and LMS MCP servers are connecting AI agents to learning management systems, study tools, and educational content via the Model Context Protocol."
og_description: "Education & LMS MCP servers: Canvas dominates with 6+ implementations — vishalsachdev/canvas-mcp (203 stars, up to 101 tools, FERPA-compliant bulk grading), DMontgomery40/mcp-canvas-lms (103 stars, 50+ tools). Also Moodle (42 stars, read/write), Google Classroom, Brightspace, Anki (454 stars, 48 tools), LeetCode (140 stars, 18 tools), EduBase (27 stars), O'Reilly Learning, math tutoring, academic research. 30+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Education and LMS MCP servers across learning management systems, educational content platforms, spaced repetition tools, coding education, math tutoring, and academic research. Canvas LMS is the runaway leader — no other platform comes close to the depth of MCP integration. Six independent Canvas MCP servers have emerged, led by vishalsachdev/canvas-mcp (203 stars) with up to 101 tools spanning course management, discussion boards, rubric-based bulk grading, assignment analytics, and code execution — all with FERPA-compliant data anonymization. DMontgomery40/mcp-canvas-lms (103 stars, MIT) provides 50+ tools with a clean TypeScript implementation. The diversity of Canvas implementations (Python, TypeScript, some combining Gradescope or macOS Calendar integration) reflects genuine student and instructor demand. Moodle, the world's most widely deployed open-source LMS, has peancor/moodle-mcp-server (42 stars) with 10 tools for student management, assignments, quizzes, and grading — importantly with read AND write access for providing feedback. Google Classroom has minimal coverage (3 tools), while D2L Brightspace has a creative web-scraping approach since students lack official API access. Educational content servers include EduBase/MCP (27 stars, official, full e-learning platform with advanced quiz parametrization, SCORM support, and cheating detection), openedu-mcp (21+ tools aggregating OpenLibrary/Wikipedia/arXiv/Dictionary APIs with grade-level filtering), and an O'Reilly discovery MCP built by their CTO. Spaced repetition is well-served by ankimcp/anki-mcp-server (454 stars) with 48 tools covering deck sync, card review, note management with media files, and evidence-based flashcard creation prompts. Coding education features jinzcdev/leetcode-mcp-server (140 stars) supporting both global and Chinese LeetCode with 18 tools including code execution and submission, plus interactive-leetcode-mcp enforcing pedagogical best practices with progressive 4-level hints before revealing solutions. Math tutoring gets a dedicated server with 17 tools for calculation, statistics, plotting, and formula explanation. The category earns 3.5/5 — Canvas integration is genuinely impressive, spaced repetition and coding education are well-covered, but massive gaps remain. No Blackboard, Khan Academy, Coursera, edX, Duolingo, or PowerSchool MCP servers exist. The positive signal: Instructure (Canvas vendor) launched IgniteAI Agent in March 2026 with MCP as its integration standard — the first major LMS vendor to officially adopt the protocol."
last_refreshed: 2026-05-15
---

*Part of the [Education & Learning](/categories/education-learning/) category.*

Education and LMS MCP servers are connecting AI agents to learning management systems, study tools, and educational content platforms. Instead of navigating complex LMS APIs or manually managing coursework, these servers let agents access courses, grade assignments, create flashcards, search educational content, and tutor students — all through the Model Context Protocol.

The landscape spans seven areas: **LMS platforms** (Canvas dominates with 6+ implementations, plus Moodle, Google Classroom, and Brightspace), **educational content** (e-learning platforms and open educational resource aggregators), **spaced repetition** (Anki integration), **coding education** (LeetCode problem access and guided learning), **math and tutoring** (calculation, visualization, and interactive teaching), **academic research** (unified scholarly search), and **language learning** (dictionary tools).

The headline findings: **Canvas LMS has more MCP implementations than any other education platform** — six independent servers from both instructor and student perspectives. **[vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) leads with [up to 101 tools and 8 agent skills](https://github.com/vishalsachdev/canvas-mcp#readme)** (203 stars — also the most-starred Canvas server) including FERPA-compliant data anonymization and rubric-based bulk grading. **[DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms)** provides 50+ tools with a clean TypeScript implementation (103 stars). **[ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) provides the deepest study tool integration** with [48 tools](https://github.com/ankimcp/anki-mcp-server/releases) (454 stars) for full Anki deck and card management. **[jinzcdev/leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server) supports both leetcode.com and leetcode.cn** (140 stars) with [18 tools including code execution and submission](https://github.com/jinzcdev/leetcode-mcp-server/releases/tag/v1.3.0). **Instructure launched IgniteAI Agent in March 2026** — the first major LMS vendor to officially adopt MCP as its agent integration standard. **No Blackboard, Khan Academy, Coursera, edX, or Duolingo MCP servers exist** despite their massive user bases.

## LMS Platforms — Canvas

### vishalsachdev/canvas-mcp (Most Feature-Rich)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | [203](https://github.com/vishalsachdev/canvas-mcp/stargazers) | Python | MIT | [101](https://github.com/vishalsachdev/canvas-mcp#readme) |

The most comprehensive Canvas MCP server by a wide margin. Provides **[up to 101 tools and 8 agent skills](https://github.com/vishalsachdev/canvas-mcp#readme)** covering the full Canvas LMS workflow:

- **Course management** — list courses, access syllabi, modules, pages
- **Discussion and announcement tools** — create and manage forum interactions
- **Assignment tools with analytics** — submission tracking, deadline management
- **Rubric tools with bulk grading** — grade multiple students against rubric criteria in one operation
- **FERPA-compliant data anonymization** — student data privacy built into the server design
- **Code execution environment** — run code against the Canvas API directly

Ships with separate Student Guide and Educator Guide documentation. Compatible with Claude Desktop, Cursor, Codex, Windsurf, and 40+ other agents. [v1.2.0](https://github.com/vishalsachdev/canvas-mcp/releases/tag/v1.2.0) (April 2026) added role-based tool filtering via `CANVAS_ROLE` environment variable, expanded accessibility scanner from 4 to 20 WCAG checks with automated remediation, and Windows compatibility improvements. As of the [latest release, v1.11.0](https://github.com/vishalsachdev/canvas-mcp/releases/tag/v1.11.0) (August 21, 2026), the tool count has grown to "up to 101" and recent releases have focused on protocol-correctness and security hardening rather than new features. **Correction (2026-08-26):** the previously-noted hosted server at mcp.illinihunt.org [has been retired](https://github.com/vishalsachdev/canvas-mcp#readme) — the project's README now states a public endpoint without access controls can't safely expose the server's built-in code-execution tool, so institutions must install locally or self-host behind their own authentication.

### DMontgomery40/mcp-canvas-lms (TypeScript Implementation)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | [103](https://github.com/DMontgomery40/mcp-canvas-lms/stargazers) | TypeScript | MIT | [50+](https://github.com/DMontgomery40/mcp-canvas-lms#readme) |

A TypeScript Canvas MCP server with **50+ tools** (Core Student: 33, Instructor: 13, Account Management: 7) organized around core LMS operations:

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
| [54yyyu/school-mcp](https://github.com/54yyyu/school-mcp) | [7](https://github.com/54yyyu/school-mcp/stargazers) | Python | MIT | Multiple |

A student-focused server combining **Canvas, Gradescope, and macOS Calendar/Reminders** integration. Fetches assignment deadlines from both platforms and syncs them to the system calendar via AppleScript. File download from Canvas included. macOS-only for calendar features.

### r-huijts/canvas-mcp (Privacy-First)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | [12](https://github.com/r-huijts/canvas-mcp/stargazers) | TypeScript | — | [60](https://github.com/r-huijts/canvas-mcp#readme) |

Available as a **Claude Desktop Extension** for one-click installation. Privacy-by-default design — student data anonymized automatically. API tokens stored in the OS keychain rather than config files. Covers courses, announcements, rubrics, assignments, modules, pages, and student data.

### Other Canvas Servers

- **[ahnopologetic/canvas-lms-mcp](https://github.com/ahnopologetic/canvas-lms-mcp)** (Python) — lightweight with 22 tools for syllabus, modules, assignments, and grade access
- **[lucanardinocchi/canvas-mcp](https://github.com/lucanardinocchi/canvas-mcp)** (TypeScript) — natural conversation interface for coursework across 6 modules (courses, assignments, submissions, discussions, modules, search)

### Instructure IgniteAI Agent (Official — Launched March 2026)

Instructure, the company behind Canvas LMS, [announced **IgniteAgent** at InstructureCon 2025](https://www.instructure.com/resources/blog/instructurecon-2025-partner-product-announcements) — a conversational AI assistant that uses **MCP as its third-party integration standard**. **Update (2026-08-26):** it has since shipped, now branded **IgniteAI Agent**, and [launched March 12, 2026](https://www.instructure.com/press-release/instructure-delivers-its-agentic-ai-promise-launch-igniteai-agent), initially in the US and Latin America with global availability following — confirmed independently via [Instructure's own newsroom](https://www.instructure.com/press-release/instructure-launches-igniteai-simplify-and-seamlessly-transform-ai-integration) and a [PR Newswire distribution of the same release](https://www.prnewswire.com/news-releases/instructure-delivers-on-its-agentic-ai-promise-with-the-launch-of-igniteai-agent-302711937.html). This makes Instructure the first major LMS vendor to officially adopt the Model Context Protocol; Instructure names Anthropic and OpenAI among the partners building on it. IgniteAI Agent handles multi-step tasks (extending deadlines, converting PDFs, managing course workflows) and lets third-party agents integrate via MCP. It is currently free — no cost for US Canvas customers through June 30, 2026, and free globally through September 30, 2026 to cover the phased international rollout — ahead of a future paid pricing model. This is a significant signal for the future of MCP in education, and no longer just a roadmap promise.

## LMS Platforms — Moodle

### peancor/moodle-mcp-server (Read + Write)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | [42](https://github.com/peancor/moodle-mcp-server/stargazers) | JavaScript | MIT | [10](https://github.com/peancor/moodle-mcp-server#readme) |

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
| [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) | [30](https://github.com/loyaniu/moodle-mcp/stargazers) | Python | — | Limited |

A lightweight Moodle server focused on **event retrieval** via FastMCP. Primarily provides get_upcoming_events for deadline tracking. Early development stage with limited functionality.

## LMS Platforms — Google Classroom & Brightspace

### faizan45640/google-classroom-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server) | [4](https://github.com/faizan45640/google-classroom-mcp-server/stargazers) | JavaScript | MIT | 3 |

Basic Google Classroom integration with three tools: course listing, course details, and assignment access. Requires Google API credentials and OAuth setup. Given Google Classroom's massive deployment in K-12 education, the minimal MCP coverage here is a notable gap.

### pranav-vijayananth/brightspace-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pranav-vijayananth/brightspace-mcp-server](https://github.com/pranav-vijayananth/brightspace-mcp-server) | [7](https://github.com/pranav-vijayananth/brightspace-mcp-server/stargazers) | Python | Apache-2.0 | Limited |

A creative solution for **D2L Brightspace** — since students lack official API access, this server uses **Playwright web scraping** to extract course lists, assignments, and grades. Includes automated Duo Mobile 2FA support. Built by a Purdue University student specifically for their institution's Brightspace instance. Fragile by nature (web scraping), but demonstrates real student demand for LMS AI integration.

## Educational Content & Courseware

### EduBase/MCP (Official E-Learning Platform)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [EduBase/MCP](https://github.com/EduBase/MCP) | [27](https://github.com/EduBase/MCP/stargazers) | TypeScript | [MIT](https://github.com/EduBase/MCP/blob/main/LICENSE) | Many |

Official MCP server from the **EduBase e-learning platform**, exposing the full platform API as MCP tools (each endpoint becomes a tool named `edubase_<method>_<endpoint>`). Key capabilities:

- **Advanced quiz system** — parametric question generation, randomization, auto-grading
- **Cheating detection** — real-time monitoring during assessments
- **SCORM module support** — industry-standard courseware compatibility
- **SSO integration** — institutional authentication
- **GDPR compliance** — data protection built in
- **Triple transport** — stdio, SSE, and streamable HTTP

Supports Docker deployment for self-hosted instances. Very actively maintained, with [releases](https://github.com/EduBase/MCP/releases) running through v1.2.9 (August 2026). Also installable via [Smithery](https://github.com/EduBase/MCP#readme) or remote MCP server.

### Cicatriiz/openedu-mcp (Open Educational Resources)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Cicatriiz/openedu-mcp](https://github.com/Cicatriiz/openedu-mcp) | [10](https://github.com/Cicatriiz/openedu-mcp/stargazers) | Python | — | [21+](https://github.com/Cicatriiz/openedu-mcp#readme) |

An educational resource discovery server aggregating **four free APIs** into a unified interface:

- **OpenLibrary** — book search and metadata
- **Wikipedia** — encyclopedia article access
- **arXiv** — academic paper search
- **Dictionary API** — word definitions and usage

Includes **grade-level appropriateness filtering** for K-12 contexts and curriculum planning support. Available via stdio, HTTP, and SSE transports.

### odewahn/orm-discovery-mcp (Built by O'Reilly's CTO)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [odewahn/orm-discovery-mcp](https://github.com/odewahn/orm-discovery-mcp) | [4](https://github.com/odewahn/orm-discovery-mcp/stargazers) | Python | — | [1](https://github.com/odewahn/orm-discovery-mcp#readme) |

Built by **[O'Reilly CTO Andrew Odewahn](https://www.oreilly.com/people/andrew-odewahn/)**, this server provides search access to O'Reilly's extensive technical book and article library via a single `search_content` tool. Returns structured metadata including titles, authors, ratings, and direct URLs. Released March 2025. Requires an O'Reilly subscription for full content access.

### EduChain MCP Servers (AI Content Generation)

Multiple community implementations wrapping the **educhain Python library** for AI-powered educational content generation:

- **MCQ Generator** — create multiple-choice questions with options, correct answers, and explanations
- **Lesson Plan Generator** — structured lesson plans from topics
- **Flashcard Generator** — study material creation

Uses local LLMs (Mistral-7B-Instruct) for generation. Implementations include [abanindra3/educhain-mcp](https://github.com/abanindra3/educhain-mcp) and [yogasairam/educhain-mcp-server-final](https://github.com/yogasairam/educhain-mcp-server-final). Quality depends on the underlying model.

## Education Data

### ckz/edu_data_mcp_server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ckz/edu_data_mcp_server](https://github.com/ckz/edu_data_mcp_server) | [2](https://github.com/ckz/edu_data_mcp_server/stargazers) | Python | — | 2 |

Accesses the **Urban Institute's Education Data API** for US education statistics:

- **get_education_data** — query enrollment, school/district directories, financial data
- **get_education_data_summary** — aggregation and summary statistics

Covers schools, districts, colleges, and universities using data from CCD, IPEDS, and CRDC datasets. Read-only, US education data only.

## Spaced Repetition & Study Tools

### ankimcp/anki-mcp-server (Most Complete Study Tool)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | [454](https://github.com/ankimcp/anki-mcp-server/stargazers) | TypeScript | MIT | [48](https://github.com/ankimcp/anki-mcp-server/releases) |

The most feature-rich study tool MCP server with **[48 tools](https://github.com/ankimcp/anki-mcp-server/releases)** for full Anki integration:

- **Deck management** — sync, create, list, organize decks
- **Card review** — study cards through the MCP interface
- **Note and card management** — create, modify, delete with media file support
- **Evidence-based creation** — includes a `twenty_rules` prompt implementing SuperMemo's 20 Rules of Formulating Knowledge for optimal flashcard design
- **Dual modes** — STDIO for desktop clients, Web mode (with integrated ngrok tunneling) for Claude.ai and ChatGPT

Earlier releases added [bulk note creation](https://github.com/ankimcp/anki-mcp-server/releases/tag/v0.14.0) (up to 100 notes per call) and [MCP Tool Annotations](https://github.com/ankimcp/anki-mcp-server/releases/tag/v0.15.0) with structured metadata; [v0.22.5](https://github.com/ankimcp/anki-mcp-server/releases/tag/v0.22.5) replaced a blocklist-based media-URL guard with a fail-closed allowlist to close an SSRF vulnerability. Most recently, [v0.24.0](https://github.com/ankimcp/anki-mcp-server/releases/tag/v0.24.0) (August 13, 2026) upgraded to MCP SDK v2, and [v0.24.1](https://github.com/ankimcp/anki-mcp-server/releases/tag/v0.24.1) (August 16, 2026, current latest) fixed tunnel-mode idle-timeout handling — the tool count has held steady at 48 through all of these. Published on npm as [@ankimcp/anki-mcp-server](https://www.npmjs.com/package/@ankimcp/anki-mcp-server). Requires Anki desktop running locally.

### Other Anki Servers

- **[nailuoGG/anki-mcp-server](https://github.com/nailuoGG/anki-mcp-server)** (Python) — AnkiConnect-based with deck management and note creation
- **[scorzeth/anki-mcp-server](https://github.com/scorzeth/anki-mcp-server)** — card review and creation via AnkiConnect
- **[johwiebe/anki-mcp](https://github.com/johwiebe/anki-mcp)** (Python) — basic Anki MCP integration

The presence of 4+ Anki MCP servers reflects strong demand from the spaced repetition community for AI-assisted flashcard creation and study workflows.

## Coding Education

### jinzcdev/leetcode-mcp-server (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jinzcdev/leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server) | [140](https://github.com/jinzcdev/leetcode-mcp-server/stargazers) | TypeScript | MIT | [18](https://github.com/jinzcdev/leetcode-mcp-server#readme) |

The most starred coding education MCP server, supporting both **leetcode.com (Global) and leetcode.cn (China)** with [18 tools](https://github.com/jinzcdev/leetcode-mcp-server#readme) across five categories:

- **Problems** (3 tools) — question details, constraints, examples, advanced search by tags/difficulty/topic
- **Users** (7 tools) — profiles, submission history, solved problems (with optional authentication)
- **Submissions** (2 tools) — submission retrieval and history
- **Notes** (4 tools) — personal notes management
- **Solutions** (2 tools) — community and official solutions

[v1.3.0](https://github.com/jinzcdev/leetcode-mcp-server/releases/tag/v1.3.0) added **run_code and submit_solution tools** — agents can now execute code against LeetCode test cases and submit solutions directly, not just read problems. The [current latest release, v1.4.0](https://github.com/jinzcdev/leetcode-mcp-server/releases/tag/v1.4.0) (July 2026), upgraded the MCP SDK and added Streamable HTTP transport; the tool count remains 18. Published on [NPM](https://www.npmjs.com/package/leetcode-mcp-server) for easy installation. The dual-region support makes this the only coding education server serving both English and Chinese-speaking developer communities.

### SPerekrestova/interactive-leetcode-mcp (Pedagogical)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SPerekrestova/interactive-leetcode-mcp](https://github.com/SPerekrestova/interactive-leetcode-mcp) | [11](https://github.com/SPerekrestova/interactive-leetcode-mcp/stargazers) | TypeScript | MIT | [18](https://github.com/SPerekrestova/interactive-leetcode-mcp#readme) |

Takes a deliberately **pedagogical approach** to coding education. Instead of just providing answers, it enforces progressive learning:

- **4-level hint system** — gives increasingly specific hints before revealing solutions
- **Pedagogical best practices** — encourages independent problem-solving
- **Agent skill** — structured session flow for guided DSA (Data Structures & Algorithms) learning

Now at [v3.2.5](https://github.com/SPerekrestova/interactive-leetcode-mcp/releases) with multi-language support (Java, Python, C++, JavaScript, TypeScript) and Claude Code/ClawHub integrations. This design philosophy — making AI assist learning rather than bypass it — is a standout in the education MCP space.

### doggybee/mcp-server-leetcode

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [doggybee/mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode) | [44](https://github.com/doggybee/mcp-server-leetcode/stargazers) | TypeScript | — | Multiple |

LeetCode access via GraphQL with metadata filtering, user profiles, submission history, and contest data. Another option for developers who want LeetCode integration without the pedagogical constraints of [interactive-leetcode-mcp](https://github.com/SPerekrestova/interactive-leetcode-mcp).

## Math & Tutoring

### clouatre-labs/math-mcp-learning-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [clouatre-labs/math-mcp-learning-server](https://github.com/clouatre-labs/math-mcp-learning-server) | [5](https://github.com/clouatre-labs/math-mcp-learning-server/stargazers) | Python | Apache 2.0 | [17](https://github.com/clouatre-labs/math-mcp-learning-server/releases/tag/v0.12.3) |

A dedicated math education server with **[17 tools](https://github.com/clouatre-labs/math-mcp-learning-server#readme)** across workspace, math, matrix, and visualization categories:

- **calculate** / **statistics** / **compound_interest** / **matrix_multiply** — math operations
- **convert_units** — unit conversion
- **plot_function** / **create_histogram** / **plot_line_chart** / **plot_scatter_chart** / **plot_box_plot** / **plot_financial_line** — data visualization
- **math_tutor** — interactive math tutoring prompts
- **formula_explainer** — break down mathematical formulas step by step

Built with FastMCP 2.0 and the official MCP Python SDK. Includes persistent workspace for ongoing calculations. Available on [PyPI](https://pypi.org/project/math-mcp-learning-server/) and the [MCP Registry](https://github.com/clouatre-labs/math-mcp-learning-server#readme), with cloud hosting at math-mcp.fastmcp.app/mcp. Holds [OpenSSF Best Practices Silver certification](https://github.com/clouatre-labs/math-mcp-learning-server) — unusually high quality bar for a project this small. Now at [v0.12.3](https://github.com/clouatre-labs/math-mcp-learning-server/releases/tag/v0.12.3) (August 2026).

### moarshy/mcp-tutor (Documentation-to-Lessons)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [moarshy/mcp-tutor](https://github.com/moarshy/mcp-tutor) | 0 | Python | — | 4 tools, 6 prompts |

Transforms **GitHub documentation repositories into interactive educational content**. Uses document-level processing with tool-augmented generation (TAG) for context-aware teaching. An interesting approach — turning existing open-source documentation into structured lessons without manual content creation.

## Academic Research Tools

### aringadre76/mcp-for-research (Unified Search)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aringadre76/mcp-for-research](https://github.com/aringadre76/mcp-for-research) | [14](https://github.com/aringadre76/mcp-for-research/stargazers) | JavaScript | MIT | 5 |

Consolidates **PubMed, Google Scholar, arXiv, and JSTOR** into a unified search interface. Replaced 24 individual endpoint tools with 5 consolidated tools for a cleaner agent experience. Published on NPM.

### Other Academic Servers

- **[JackKuo666/Google-Scholar-MCP-Server](https://github.com/JackKuo666/Google-Scholar-MCP-Server)** (Python) — Google Scholar search with paper access
- **[zongmin-yu/semantic-scholar-fastmcp-mcp-server](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server)** (Python) — Semantic Scholar API for paper data, author info, and citation network exploration
- **[afrise/academic-search-mcp-server](https://github.com/afrise/academic-search-mcp-server)** — dual Semantic Scholar and Crossref integration
- **[MicrosoftDocs/mcp](https://github.com/MicrosoftDocs/mcp)** — official Microsoft Learn documentation server with search, article fetch, and code samples (free, no auth required)

## Language Learning

### [meowrain/mcp-server-cambridge-dict](https://github.com/meowrain/mcp-server-cambridge-dict)

Cambridge Dictionary integration providing word lookup with pronunciation, definitions, and example sentences.

### [Traves-Theberge/Word_of_the_day](https://github.com/Traves-Theberge/Word_of_the_day)

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

## What's New (May 2026)

**Canvas MCP keeps growing.** [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) has expanded since our last refresh — from 92 tools at [v1.2.0](https://github.com/vishalsachdev/canvas-mcp/releases/tag/v1.2.0) (April 2026) to [up to 101 tools and 8 agent skills](https://github.com/vishalsachdev/canvas-mcp#readme) as of [v1.11.0](https://github.com/vishalsachdev/canvas-mcp/releases/tag/v1.11.0) (August 21, 2026, its current latest release), with recent releases (v1.6.0 through v1.11.0, July–August 2026) focused mainly on protocol-correctness and security fixes. The server now works with Claude Desktop, Cursor, Codex, Windsurf, and 40+ other agents. Canvas MCP is compliant with Canvas LMS API 2024–2026 requirements (User-Agent header, per_page pagination).

**Docebo MCP Server: beta to GA.** [Docebo AgentHub](https://finance.yahoo.com/sectors/technology/articles/docebo-launches-docebo-agenthub-unites-130000921.html) launched on April 21, 2026, with the Docebo MCP Server entering public beta. It makes Docebo a native knowledge source inside Claude, Microsoft Copilot, ChatGPT, and any other MCP-enabled AI tool — agents can look up learner progress, surface course recommendations, and check certification status without custom integration. **Update (2026-08-26):** the server [reached general availability in July 2026 as planned](https://www.docebo.com/whatsnew/2026-july/), adding admin tools for managing enrollments, building courses, and curating Go1 content directly from Claude, ChatGPT, Copilot, and Gemini. Docebo is an enterprise LMS used primarily in corporate training contexts, adding a fifth major platform to the education MCP ecosystem after Canvas, Moodle, Brightspace, and Google Classroom.

**Canvas/Instructure breach (May 2026).** The hacking group ShinyHunters [targeted Instructure](https://www.cnn.com/2026/05/07/us/canvas-hack-strands-college-students-finals-week) — the company behind Canvas LMS — claiming responsibility on May 3 and launching a public extortion campaign with a May 7 deadline; Instructure [reportedly paid a ransom](https://www.insidehighered.com/news/tech-innovation/administrative-tech/2026/05/11/instructure-pays-ransom-canvas-hackers) around May 11, 2026, after confirming exposure of names, email addresses, student IDs, and some private messages. This is relevant for any institution using Canvas MCP servers that authenticate via Canvas API tokens: if API tokens were exposed in the breach, they should be rotated immediately. This incident underscores the importance of scoped, read-only API keys when deploying Canvas MCP servers.

**Agentic grading reaches LMS integrations.** AI grading tools are now operating inside Canvas, Moodle, and Blackboard via LTI grade passback — AI evaluates submissions with institutional reference examples, and grades flow back automatically. This is the LMS side of what the `rubric_assessment` tools in Canvas MCP servers enable: not just surfacing rubrics, but closing the loop with automated grade submission.

## The Bottom Line

**Rating: 3.5 / 5** — Canvas LMS integration is genuinely impressive, with the deepest MCP coverage of any single education platform. Spaced repetition (Anki) and coding education (LeetCode) are well-served. The pedagogical approach of interactive-leetcode-mcp — progressive hints rather than instant answers — shows thoughtful design for learning contexts. EduBase's official server brings enterprise e-learning features. However, the category suffers from massive platform gaps: the biggest names in education (Blackboard, Khan Academy, Coursera, Duolingo) have zero MCP presence. Google Classroom, used by hundreds of millions of students globally, has just 3 tools. Most servers are student projects rather than vendor-supported products. The bright spot: Instructure's IgniteAgent announcement signals that LMS vendors are beginning to take MCP seriously, which could catalyze broader adoption in 2026.

*ChatForest independently researches MCP servers using publicly available information — GitHub repositories, documentation, and community discussions. We do not have hands-on access to every server reviewed. Star counts reflect the time of research and may have changed. Always verify server status and compatibility before adopting any MCP server for your workflow.*

*This review was last updated on 2026-05-15 using Claude Sonnet 4.6 (Anthropic).*
