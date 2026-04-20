# Education & EdTech MCP Servers — Canvas LMS, Moodle, Google Classroom, Anki, Udemy, EduBase, and More

> Education and EdTech MCP servers are connecting AI agents to learning management systems, flashcard apps, academic research databases, and assessment platforms.


*Part of the [Education & Learning](/categories/education-learning/) category.*

Education MCP servers are connecting AI agents to learning management systems, flashcard applications, academic research databases, assessment platforms, and STEM computation tools. Instead of manually navigating LMS dashboards, searching academic databases, or creating flashcards one at a time, these servers let AI assistants manage coursework, track grades, search research papers, run spaced repetition sessions, generate quizzes, and solve mathematical problems — all through the Model Context Protocol.

The landscape spans seven areas: **LMS integration** (Canvas, Moodle, Google Classroom, D2L Brightspace), **flashcards & spaced repetition** (Anki implementations), **academic research** (arXiv, Semantic Scholar, multi-platform aggregators), **enterprise learning** (Udemy Business), **assessment & tutoring** (EduBase, quiz generators), **STEM tools** (Wolfram Alpha computation), and **knowledge reference** (Wikipedia).

The headline findings: **Canvas LMS has the most MCP server competition of any single EdTech platform** — at least six independent implementations, with the two leading servers offering 54 and 90+ tools respectively. **Academic research tools are the strongest subcategory** — arXiv MCP has 2,400 stars and paper-search-mcp aggregates seven platforms. **Anki is the only flashcard app with serious MCP support** — the leading server has 179 stars and 20+ tools. **Udemy is the first major MOOC platform to ship an official MCP server** — signaling enterprise learning's embrace of agentic AI. **The biggest gap is Blackboard** — one of the three dominant LMS platforms has zero MCP implementations.

## LMS Integration

### Canvas LMS — DMontgomery40/mcp-canvas-lms

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | ~89 | TypeScript | — | 54 tools |

The most-starred Canvas MCP server provides comprehensive coverage across three user types:

- **Students** — course access, assignment submission, grade tracking, discussion participation, file management, calendar events
- **Instructors** — course creation, assignment management, grading, student enrollment, quiz administration, rubric handling
- **Account administrators** — user management, account oversight, reporting, sub-account administration

Version 2.3.0 introduced streamable HTTP transport support, Docker deployment options, and automatic retries with pagination. The server supports both stdio and HTTP transport modes.

### Canvas LMS — vishalsachdev/canvas-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | ~75 | Python/TypeScript | MIT | 90+ tools |

The most feature-rich Canvas implementation, with **FERPA-compliant data anonymization** for educator use — a critical differentiator for institutional deployment. Offers 8 agent skills via `skills.sh` for 40+ coding agents, a code execution API for token-efficient bulk operations, and a hosted server option requiring no local installation.

Supports Claude Desktop, Cursor, Zed, Windsurf, Continue, Replit, Copilot Studio, and other MCP-compatible clients. The learning designer capabilities include course quality control and accessibility auditing — features no other Canvas MCP server offers.

### Other Canvas Implementations

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | ~1 | TypeScript | — | Multiple |
| [ahnopologetic/canvas-lms-mcp](https://github.com/ahnopologetic/canvas-lms-mcp) | — | TypeScript | — | 22 tools |
| [lucanardinocchi/canvas-mcp](https://github.com/lucanardinocchi/canvas-mcp) | — | TypeScript | — | Multiple |
| [mtgibbs/canvas-lms-mcp](https://github.com/mtgibbs/canvas-lms-mcp) | — | TypeScript | — | Multiple |

At least four additional Canvas MCP servers exist, ranging from minimal read-only grade checkers to full course management tools. The fragmentation reflects Canvas's dominance in higher education — Instructure powers over 6,000 institutions, making it the most targeted LMS for MCP integration.

### Moodle MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | ~31 | JavaScript | MIT | 11 tools |

The leading Moodle MCP server provides 11 tools across four management categories:

- **Course management** — `get_courses` with pagination
- **Student oversight** — `list_students` with ID, name, email, last access
- **Assignment handling** — `get_assignments`, `get_student_submissions`, `provide_assignment_feedback`
- **Assessment** — `get_quizzes`, `get_quiz_attempts`, `provide_quiz_feedback`

Requires Node.js v14+ and a Moodle API token with appropriate permissions. A second implementation, [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp), offers a Python alternative.

The grading and feedback tools make this genuinely useful for instructors managing large courses — an AI assistant can review submissions, generate feedback drafts, and submit grades through natural language commands.

### Google Classroom MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server) | ~2 | JavaScript | MIT | 3 tools |

A minimal implementation providing read-only access to Google Classroom data:

- **courses** — list all courses
- **course-details** — detailed course info with announcements
- **assignments** — assignment data for a course

Uses OAuth 2.0 authentication with automatic token refresh. Given Google Classroom's massive adoption in K-12 education (150M+ users), the limited tool count here represents a significant gap — there's no assignment submission, grade posting, or student roster management.

### D2L Brightspace MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bencered/d2l-mcp-server](https://github.com/bencered/d2l-mcp-server) | — | — | — | 12 tools |

Provides access to D2L Brightspace LMS with **automated SSO authentication** and persistent session storage. Tools cover assignments, grades, calendar, announcements, and course content. A student-focused implementation by [pranav-vijayananth/brightspace-mcp-server](https://github.com/pranav-vijayananth/brightspace-mcp-server) at Purdue University also exists.

The ethical note in the repository is worth highlighting: "This should NOT be used to cheat on any assignments or to gain an unfair advantage... only intended to enable agents to better understand assignment scheduling and to help with learning of course material."

## Flashcards & Spaced Repetition

### Anki MCP Server — ankimcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | ~179 | TypeScript | AGPL-3.0 | 20+ tools |

The most comprehensive Anki integration, with tools organized into five categories:

- **Review & Study** (4 tools) — quiz sessions, card scheduling, review tracking
- **Deck Management** (4 tools) — create, organize, and configure decks
- **Note Management** (6 tools) — CRUD operations with batch support (up to 100 notes), Anki query syntax
- **Media Management** (4 tools) — audio/image handling with multiple upload methods
- **Model/Template Management** (3 tools) — template configuration with HTML/CSS awareness

Deployment flexibility is a standout feature: local stdio, HTTP server, or **ngrok-tunneled remote access** for web-based AI tools. Includes a read-only safety mode to prevent accidental modifications. Still in beta with APIs subject to change.

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
| [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | ~2,400 | Python | Apache-2.0 | 4 tools |

The **highest-starred education MCP server** by a wide margin, providing four focused tools:

- **Paper Search** — query arXiv with filters for date ranges and categories
- **Paper Download** — download papers by arXiv ID
- **List Papers** — view downloaded papers in local storage
- **Read Paper** — access downloaded paper content

Includes a set of research prompts for comprehensive paper analysis workflows. The star count reflects broad adoption beyond education — researchers, developers, and AI practitioners all use arXiv daily.

### Paper Search MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) | ~791 | Python | MIT | Multi-source |

A **multi-platform academic search aggregator** supporting seven sources:

- arXiv, PubMed, bioRxiv, medRxiv, Google Scholar, IACR ePrint Archive, Semantic Scholar

Uses a standardized `Paper` class for consistent output across platforms, async request handling via httpx, and an extensible architecture for adding new sources. Optional Sci-Hub integration for full paper downloads.

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

The **first major MOOC platform to launch an official MCP server**. Designed for enterprise customers to embed personalized learning content directly into AI workflows:

- **On-demand support** — real-time problem-solving via micro-courses and curated lessons
- **Plug-and-play integration** — pre-built MCP connectors for ChatGPT, Claude, Cursor, Perplexity
- **Contextual search** — relevant course recommendations within existing AI tools

This is an enterprise product aimed at corporate L&D teams, not individual learners. The strategic signal matters more than the technical implementation — Udemy is betting that MCP is how learning content gets consumed in the AI era.

## Assessment & Tutoring

### EduBase MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [EduBase/MCP](https://github.com/EduBase/MCP) | ~24 | TypeScript | MIT | Dynamic (API-based) |

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

## What's missing

The education MCP ecosystem has significant gaps:

- **Major LMS platforms** — Blackboard, Sakai, Open edX, Schoology have zero MCP implementations
- **MOOC platforms** — no Coursera, Khan Academy, LinkedIn Learning, or edX integrations (only Udemy)
- **Student information systems** — no Banner, PowerSchool, Infinite Campus, or Ellucian SIS connectivity
- **Library systems** — no OCLC WorldCat, Ex Libris Alma, or MARC catalog integrations
- **Academic integrity** — no Turnitin, Grammarly, or plagiarism detection tools
- **Adaptive learning** — no adaptive engines (Knewton, ALEKS, DreamBox) have MCP support
- **Standardized testing** — no SAT, GRE, AP, or state assessment integrations
- **Learning analytics** — no xAPI/Caliper, learning record stores, or analytics dashboards
- **Proctoring** — no Respondus, ExamSoft, or ProctorU integrations
- **K-12 specific** — Google Classroom support is minimal (3 read-only tools for a platform with 150M+ users)

## The bottom line

The education MCP server ecosystem is **fragmented but deeper than expected**. Canvas LMS has genuine competition between implementations (unusual for vertical MCP categories), Anki has a mature integration with 179 stars, and the academic research tools are excellent — the arXiv server alone has 2,400 stars.

The Udemy official MCP server is the most important strategic signal. When a publicly-traded EdTech company ships MCP infrastructure for enterprise customers, it validates the protocol's relevance beyond developer tooling. Expect Coursera, LinkedIn Learning, and others to follow.

But the ecosystem is also deeply incomplete. The three pillars of institutional education technology — **LMS** (partially covered), **SIS** (not covered), and **library systems** (not covered) — need all three for a complete campus AI workflow. Blackboard's absence is conspicuous. K-12 is underserved relative to higher education. And the lack of academic integrity tools means institutions can't build AI assistants that also enforce their own policies.

**Rating: 3.5/5** — Canvas and Moodle coverage is decent, academic research tools are strong, Anki integration is mature, and the Udemy official server adds enterprise credibility. But gaps in major LMS platforms (Blackboard), student information systems, library systems, and K-12 tools prevent a higher score. The category has more potential than most verticals — education is an obvious use case for AI agents — but the implementations haven't caught up to the opportunity yet.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

