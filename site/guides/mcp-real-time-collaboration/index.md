# MCP and Real-Time Collaboration: How AI Agents Connect to Slack, Microsoft Teams, Notion, Confluence, Miro, Figma, Video Conferencing, Discord, Project Management, Whiteboarding, Knowledge Bases, and Shared Workspaces

> A comprehensive guide to 70+ MCP integrations for real-time collaboration — covering chat and messaging servers (Slack official MCP with ~15 tools and OAuth, korotovsky's


Real-time collaboration is the foundation of modern work. The enterprise collaboration software market is valued at approximately $64.9 billion in 2025, projected to reach $121.5 billion by 2030 at 13.4% CAGR. Within this space, AI-enabled communications and collaboration tools represent a $22.9 billion segment growing at 15.1% CAGR. By 2026, 75% of firms plan to deploy AI-enabled communications APIs, and copilots embedded in collaboration tools are expected to automate 30-50% of routine workloads — meeting notes, document creation, status updates, and project analytics.

The Model Context Protocol is emerging as the bridge between AI agents and collaboration platforms. Rather than each AI tool building bespoke integrations with Slack, Notion, Jira, and Teams, MCP provides a standardized protocol that lets any MCP-compatible AI assistant — Claude Code, Cursor, Windsurf, GitHub Copilot — interact with collaboration tools through a common interface. The result: AI agents can read Slack channels, edit Notion pages, create Jira tickets, join whiteboarding sessions, and summarize meeting transcripts — all through the same protocol.

What makes the collaboration MCP ecosystem particularly notable is the density of official first-party servers. Slack, Notion, Atlassian, Miro, Figma, Airtable, Asana, Linear, and GitHub have all shipped their own MCP servers, many as remote hosted services with OAuth 2.1 authentication. This level of vendor commitment is unusual in the MCP ecosystem and signals that collaboration platforms see MCP as a critical integration point.

This guide is research-based. We survey what MCP servers exist across the real-time collaboration landscape, analyze the workflows they enable, and identify where significant gaps remain. We do not claim to have tested or used any of these servers hands-on — our analysis draws on published documentation, open-source repositories, vendor announcements, and industry research. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI. For background on MCP, see our [introduction to MCP](/guides/what-is-mcp/) and the [MCP server directory](/reviews/).

## Why Collaboration Needs MCP

Collaboration tools have always been siloed. Information lives in Slack threads, Notion pages, Jira tickets, Google Docs, meeting recordings, and whiteboard sessions — and connecting them requires manual effort or custom integrations. MCP changes this dynamic in several ways.

**AI agents become universal collaboration participants.** An MCP-connected AI assistant can read context from Slack, update a Notion document, create a Jira ticket, and post a summary back to Slack — all in a single workflow. The agent becomes a team member that can operate across every tool the team uses.

**Meeting intelligence becomes actionable.** Meeting MCP servers don't just transcribe — they make meeting content searchable and actionable. An AI agent can find what was discussed about a specific topic across weeks of meetings, then automatically create follow-up tasks in the project management tool.

**Document collaboration gains an AI co-author.** With MCP servers for Notion, Confluence, Google Docs, and Obsidian, AI agents can read existing documentation, suggest improvements, create new pages that follow team conventions, and keep information consistent across platforms.

**Project management becomes conversational.** Instead of manually updating Jira, Linear, or Asana, developers can ask their AI coding assistant to create tickets, update status, add comments, and link related issues — all while staying in their editor.

## Chat and Messaging

These MCP servers connect AI agents to team communication platforms, enabling them to read conversations, send messages, search history, and participate in collaborative channels.

### Slack MCP Server (Official)

**Endpoint:** mcp.slack.com | **Type:** Official (first-party) | **Tools:** ~15 | **Auth:** OAuth

Slack's official MCP server provides AI agents with direct access to Slack workspaces through a hosted remote endpoint. This is a first-party integration — Slack built and operates the server.

Key capabilities:
- **Channel search and discovery** — find relevant channels by topic, name, or purpose
- **Message sending** — post messages to channels and conversations
- **Canvas management** — create and edit Slack canvases (structured documents within Slack)
- **User management** — look up team members and their profiles
- **Workspace admin controls** — workspace administrators can manage which AI tools connect via MCP

The hosted architecture means no self-hosting or configuration — agents connect to `mcp.slack.com` and authenticate via OAuth. This aligns with Slack's enterprise security model and means workspace admins retain control over AI access.

### Slack MCP Server (korotovsky — Community)

**Repository:** korotovsky/slack-mcp-server | **Type:** Community | **Language:** TypeScript | **Transport:** stdio + SSE + HTTP

A community alternative that fills gaps in the official server's capabilities.

Key differentiators:
- **No special permission requirements** — works with standard Slack app tokens, unlike the official server which requires specific OAuth scopes
- **GovSlack support** — connects to GovSlack instances used by government agencies
- **DM and Group DM access** — read and send direct messages, not just channel messages
- **Smart history fetch** — efficiently retrieves conversation history with pagination
- **Multiple transports** — supports stdio, SSE, and HTTP for flexible deployment

### Microsoft Teams MCP Server (Official — Work IQ)

**Endpoint:** Hosted | **Type:** Official (Microsoft) | **Tools:** 24 | **Auth:** OAuth via Entra ID | **Status:** Preview

Microsoft's official MCP server for Teams provides comprehensive access to the Teams collaboration environment.

Key capabilities:
- **Full CRUD for chats** — create, read, update chat conversations
- **Channel management** — interact with team channels, post messages, manage threads
- **Team operations** — create teams, manage members, update settings
- **Member management** — add/remove members, update roles
- **Enterprise auth** — OAuth via Microsoft Entra ID (formerly Azure AD) ensures enterprise security

Still in preview as of March 2026, but represents Microsoft's commitment to MCP as a standard integration point for AI agents.

### Teams MCP (floriscornel — Community)

**Repository:** floriscornel/teams-mcp (~72 stars) | **Type:** Community | **Language:** TypeScript | **Tools:** 25 | **Transport:** stdio

A community server with capabilities that complement the official offering.

Key differentiators:
- **KQL search** — Kusto Query Language support for powerful message search across Teams
- **File uploads** — attach files to messages and channels
- **Device code auth** — alternative authentication flow for environments where browser-based OAuth isn't available
- **Comprehensive Microsoft Graph API access** — leverages the full Graph API for deep Teams integration

### Discord MCP (SaseQ — Community)

**Repository:** SaseQ/discord-mcp (~218 stars) | **Type:** Community | **Language:** Java (JDA) | **Tools:** 65 | **Transport:** stdio | **License:** MIT

The most comprehensive Discord MCP server, reaching v1.0.0 in March 2026. Discord has no official MCP server, making community implementations the only option.

Key capabilities:
- **Full CRUD on channels** — create, read, update, delete channels across servers
- **Forum management** — create and manage forum posts and threads
- **Message operations** — send, edit, delete, search messages with rich formatting
- **Webhook management** — create and manage webhooks for integrations
- **65 tools** — the most extensive Discord MCP implementation available

## Collaborative Document Editing

These MCP servers enable AI agents to read, write, and collaborate on documents across major platforms — from wikis and knowledge bases to shared documents and databases.

### Notion MCP Server (Official)

**Repository:** makenotion/notion-mcp-server (~2,390 stars) | **Type:** Official (first-party) | **Language:** TypeScript | **Transport:** Streamable HTTP (hosted) or stdio (self-hosted) | **License:** MIT

Notion's official MCP server is one of the most polished first-party implementations in the ecosystem.

Key capabilities:
- **Read and write pages in Markdown** — AI agents interact with Notion content as Markdown, making it natural for LLMs to read and generate
- **Database queries** — query Notion databases with filters, sorts, and pagination
- **Block-level CRUD** — create, read, update, and delete individual blocks within pages
- **Token-optimized API** — designed to minimize token usage in AI conversations, with Markdown-based responses instead of verbose JSON
- **Dual deployment** — hosted remote server for zero-setup or self-hosted via stdio for more control

Version 2.0.0 migrated to the Notion API 2025-09-03 with data sources abstraction, indicating active development and long-term commitment.

### Google Docs / Google Workspace MCP Servers

Multiple community servers provide access to Google's collaboration suite:

**google-docs-mcp (a-bonus)** — ~176 stars | **Transport:** stdio | **License:** MIT
- Full access to Google Docs, Sheets, and Drive
- Read, write, and format documents
- Spreadsheet operations and Drive file management

**Google Workspace MCP (taylorwilsdon)** — the most comprehensive single-server Google integration:
- Covers Calendar, Drive, Gmail, Docs, Sheets, Slides, Forms, Tasks, Contacts, and Chat
- Single server replaces multiple specialized integrations
- Transport: stdio | License: MIT

**Google Drive MCP (piotr-agier)** — focused on precision editing:
- Surgical text insertion and deletion within documents
- Table management, image embedding, and comments
- Rich formatting support for Docs, Sheets, Slides, and Calendar

Google has not shipped an official first-party MCP server, making these community implementations the primary integration path.

### Atlassian MCP Servers (Confluence + Jira)

**Atlassian Remote MCP Server (Official)**

**Repository:** atlassian/atlassian-mcp-server | **Type:** Official (first-party) | **Transport:** Streamable HTTP (remote hosted) | **Auth:** OAuth 2.1 via Entra ID

Atlassian was the first official MCP partner with Anthropic, shipping a remote hosted server for both Jira and Confluence Cloud.

Key capabilities:
- **Confluence Cloud access** — search, read, create, and update wiki pages
- **Jira Cloud access** — manage issues, search with JQL, update fields
- **Enterprise security** — OAuth 2.1, TLS 1.2+ encryption, hosted on Cloudflare
- **SSE deprecation** — SSE endpoint deprecated after June 30, 2026 in favor of Streamable HTTP

**mcp-atlassian (sooperset — Community)**

**Repository:** sooperset/mcp-atlassian (~2,600 stars, 471 forks) | **Type:** Community | **Tools:** 72 | **Transport:** stdio | **License:** MIT

The dominant community alternative with significantly more capabilities than the official server:
- **72 tools** for both Confluence and Jira
- **Server/Data Center support** — works with Confluence 6.0+ and Jira 8.14+, not just Cloud
- **Full content lifecycle** — search, get, create, update pages with comments
- **Self-hosted compatible** — critical for organizations that don't use Atlassian Cloud

## Whiteboarding and Diagramming

These MCP servers bring visual collaboration tools — whiteboards, design tools, and diagramming platforms — into AI agent workflows.

### Miro MCP Servers

**Miro AI MCP Server (Official)**

**Repository:** miroapp/miro-ai | **Type:** Official (first-party) | **Tools:** 15 (13 tools + 2 prompts) | **Auth:** OAuth 2.1 | **Transport:** HTTPS (hosted)

Miro's official MCP server enables AI agents to interact with collaborative whiteboards.

Key capabilities:
- **Board context extraction** — AI-powered understanding of board contents and spatial relationships
- **Code-to-board workflows** — transform code, data, or text into visual board elements
- **Enterprise OAuth 2.1** — secure authentication aligned with enterprise requirements
- **13 tools + 2 prompts** — curated set of high-value operations

**Miro MCP (olgasafonova — Community)**

**Repository:** olgasafonova/miro-mcp-server | **Type:** Community | **Tools:** 88 | **Transport:** stdio

A community server with nearly 6x the tools of the official implementation:
- **88 tools** vs 15 official — full API coverage including bulk operations, mindmaps, tags, connectors, and export
- **Offline/self-hosted** — runs locally without Miro's hosted infrastructure
- **Complete board manipulation** — create, move, resize, connect any board element

This pattern of community servers dramatically exceeding official tool counts is common across the collaboration MCP ecosystem.

### Excalidraw MCP Servers

**Excalidraw MCP (Official)**

**Repository:** excalidraw/excalidraw-mcp | **Type:** Official (first-party)

The official Excalidraw MCP server for streamable diagram creation and editing.

**excalidraw-mcp (lesleslie — Community)**

**PyPI:** excalidraw-mcp v0.35.3 | **Type:** Community | **Transport:** stdio + WebSocket

Notable for implementing real-time browser synchronization:
- **Live canvas with real-time sync** — changes appear in the browser instantly via WebSocket
- **Python FastMCP server + TypeScript canvas server** — dual-language architecture
- **AI-generated diagrams** — create diagrams from natural language descriptions
- **WebSocket updates** — true real-time collaboration between AI agent and human user

This is one of the few MCP servers in the collaboration space that implements genuine real-time synchronization rather than request-response interactions.

### Figma MCP Servers

**Figma MCP Server (Official)**

**Type:** Official (first-party) | **Transport:** Streamable HTTP (remote) | **Status:** Open beta

Figma's official MCP server represents a significant step toward AI-assisted design collaboration.

Key capabilities:
- **Design-to-code** — extract design information for code generation
- **Write-to-canvas** (March 2026) — AI agents can create design elements directly on the canvas
- **Code Connect** — link design components to code implementations
- **UI capture** — screenshot and analyze existing designs
- **FigJam support** — access to FigJam collaborative whiteboards
- **Bidirectional sync with GitHub Copilot** — designs stay linked to code

**Figma-Context-MCP (GLips — Community)**

**Repository:** GLips/Figma-Context-MCP (~5,000 stars, 1.3M visitors) | **Type:** Community | **Transport:** stdio

The community server that preceded the official one and drove significant adoption:
- **Design context extraction** — pull design tokens, component specs, and layout information for AI coding agents
- **~5,000 stars** — one of the most popular MCP servers in any category
- **Limitations vs official** — lacks write-to-canvas, Code Connect, UI capture, and FigJam support

### Lucid Software MCP Server

**Type:** Official (first-party) | **Transport:** MCP-compatible | **Status:** GA (Edit Document API launching April 2026)

Lucid Software — makers of Lucidchart, Lucidspark, and Lucid Visual Activities — launched an MCP server that brings AI-powered diagramming and process documentation into agent workflows.

Key capabilities:
- **Natural language diagram creation** — describe a workflow, and the agent generates a fully editable Lucidchart diagram
- **Edit Document API** (April 2026) — describe changes to an existing document within an LLM, and Lucid AI executes those edits automatically
- **Voice-to-text prompting** — speak rather than type to create diagrams
- **Intelligent structuring** — AI generates swimlanes, nested containers, boards, sticky notes, and text blocks
- **Process Agent** — a proactive collaborator that asks clarifying questions about scope, risk, and approval handoffs before generating documentation, ensuring outputs reflect actual business logic and compliance standards
- **ChatGPT Apps SDK** — generate Lucid diagrams directly from the ChatGPT interface (coming soon)

Compatible with ChatGPT, Claude, Microsoft Copilot, GitHub Copilot, and Cursor.

What sets Lucid apart from other diagramming MCP servers is the Process Agent's discovery-driven approach. Instead of blindly generating a diagram from a prompt, it initiates a chat-based process — asking about edge cases, approval workflows, and compliance requirements — before creating anything. This is closer to how a human business analyst works.

## Video Conferencing and Meetings

These MCP servers connect AI agents to meeting platforms, enabling transcript search, meeting intelligence, and automated follow-up.

### tl;dv MCP Server (Official)

**Repository:** tldv-public/tldv-mcp-server (~7 stars) | **Type:** Official (first-party) | **Transport:** stdio | **License:** MIT

The first MCP server with full multi-platform meeting support across all three major providers.

Key capabilities:
- **Google Meet, Zoom, AND Microsoft Teams** — unified access to meetings across all platforms
- **Meeting search** — filter by query, date range, or participants
- **Transcript access** — consistent cross-platform transcript formatting
- **AI-generated highlights** — pre-processed meeting highlights and key moments
- **Meeting metadata** — participants, duration, topics, and action items

### Meeting BaaS MCP

**Repository:** Meeting-BaaS/meeting-mcp | **Type:** Community | **Transport:** stdio

A meeting "Backend as a Service" approach:
- **Create meeting bots** — deploy AI bots to join and record meetings
- **Search transcripts** — full-text search across meeting recordings
- **Manage recordings** — organize and access meeting recordings programmatically
- **Multi-platform** — supports Zoom, Meet, and Teams

### Zoom Transcript MCP

**Repository:** forayconsulting/zoom_transcript_mcp | **Type:** Community | **Transport:** stdio

Focused specifically on Zoom Cloud Recording transcripts — interact with and search recorded meeting transcripts.

### Otter.ai and Fireflies.ai MCP Servers

Both major meeting intelligence platforms offer remote hosted MCP servers:
- **Otter.ai** — auto-joins Zoom/Teams/Meet for real-time transcription, with deeper analysis via Claude or ChatGPT through MCP
- **Fireflies.ai** — one-click MCP integration with Claude, Devin, and ChatGPT for meeting insights and action item extraction

## Project Management

These MCP servers connect AI agents to project tracking and issue management platforms, enabling conversational task management.

### Jira (via Atlassian)

See the [Atlassian MCP Servers](#atlassian-mcp-servers-confluence--jira) section above — both the official remote hosted server and the community mcp-atlassian (~2,600 stars, 72 tools) provide comprehensive Jira access.

### Linear MCP Servers

**Linear MCP Server (Official)**

**Docs:** linear.app/docs/mcp | **Type:** Official (first-party)

Linear's first-party MCP server integrates directly with Claude Code and Cursor:
- **Search issues** — find issues by text, status, assignee, or project
- **Create tasks** — create new issues with full field specification
- **Update status** — move issues through workflows
- **Add comments** — post updates and discussion to issues

**linear-mcp-server (jerhadf — Community)**

**Repository:** jerhadf/linear-mcp-server (~344 stars) | **Type:** Community | **Transport:** stdio

Full Linear GraphQL API integration for deeper access:
- **Issue management** — complete CRUD on issues, sub-issues, and labels
- **Project info** — access project details, roadmaps, and milestones
- **Milestone tracking** — monitor project progress and upcoming deadlines

### Asana MCP Servers

**Asana MCP Server (Official)**

**Docs:** developers.asana.com/docs/using-asanas-mcp-server | **Type:** Official (first-party)

Asana's official MCP server provides task and project management through the Asana Work Graph — Asana's model for connecting work items, people, goals, and portfolios.

**mcp-server-asana (roychri — Community)**

**Repository:** roychri/mcp-server-asana | **Type:** Community

Community alternative for self-hosted access to Asana's API.

### ClickUp MCP Server

**Repository:** taazkareem/clickup-mcp-server | **Type:** Community | **Transport:** stdio

One of the most feature-rich project management MCP servers:
- **Natural language task management** — create and update tasks using conversational language
- **Comprehensive scope** — tasks, checklists, sprints, comments, tags, spaces, lists, folders, files, docs, chat, and time tracking
- **Single server** — one integration covers ClickUp's entire feature set

### Other Project Management Servers

- **Trello** — delorenj/mcp-server-trello: board interaction with rate limiting, migrated to Bun runtime for 2.8-4.4x performance boost
- **Todoist** — greirson/mcp-todoist + official Doist MCP registry entry
- **Monday.com, Basecamp** — available through Composio MCP integrations
- **Plane** (open source) — native MCP server with import support from Jira, Linear, Asana, ClickUp, Monday

## Shared Workspaces

These MCP servers provide AI agents with access to shared data platforms — collaborative databases, spreadsheets, and document workspaces.

### Airtable MCP Servers

**Airtable MCP Server (Official)**

**Docs:** support.airtable.com | **Type:** Official (first-party) | **Transport:** Remote hosted

Airtable's official MCP server with permission-aware access:
- **Query data** — search and filter records across bases and tables
- **Create and update records** — full CRUD on Airtable records
- **Permission-aware** — respects existing Airtable permissions and sharing settings
- **Analyze information** — aggregate and analyze data within bases

**airtable-mcp (rashidazarang — Community)**

**Repository:** rashidazarang/airtable-mcp | **Type:** Community | **Tools:** 42

The most comprehensive Airtable MCP server:
- **42 tools** covering every Airtable PAT scope
- **CRUD + schema management** — full record and table structure operations
- **Comments and webhooks** — collaborative features and event-driven workflows
- **Batch operations** — efficient bulk record creation and updates
- **AI analytics** — 10 AI prompt templates for data analysis
- **Governance** — access control and audit capabilities

### Coda MCP Servers

Multiple community servers provide Coda document access:

- **coda-mcp (orellazri)** — list, create, read, update, duplicate, rename pages
- **coda-mcp (dustinrgood)** — 34 tools for comprehensive Coda interaction
- **Composio Coda integration** — standardized MCP access via the Composio platform

### Google Sheets MCP

**Repository:** xing5/mcp-google-sheets | **Type:** Community | **Transport:** stdio

Full-featured spreadsheet collaboration:
- **Complete CRUD** — create, read, update, delete cells, rows, and sheets
- **Sharing and formatting** — manage document access and cell formatting
- **Batch operations** — efficient bulk data operations
- **Dual auth** — OAuth 2.0 and service account authentication

## Knowledge Management

These MCP servers connect AI agents to team knowledge bases, wikis, and note-taking systems — enabling AI-assisted knowledge curation and retrieval.

### Obsidian MCP Server (cyanheads)

**Repository:** cyanheads/obsidian-mcp-server (~299 stars) | **Type:** Community | **Transport:** stdio (via Obsidian Local REST API plugin) | **License:** MIT

The leading MCP server for Obsidian knowledge bases:
- **Read and write notes** — full access to vault contents
- **Tag management** — add, remove, and search by tags
- **Frontmatter editing** — modify YAML frontmatter programmatically
- **Full-text search with JsonLogic queries** — powerful structured search across the vault
- **Glob patterns** — find files by pattern matching

### Roam Research MCP

**Repository:** 2b3pro/roam-research-mcp | **Type:** Community

AI interaction with Roam Research graphs:
- **Comprehensive API access** — full graph manipulation capabilities
- **Advanced data retrieval** — query the graph structure and block references
- **Block-level operations** — create, update, and link blocks within the graph

### MediaWiki MCP Servers

Two community servers provide access to any MediaWiki instance:

**ProfessionalWiki/MediaWiki-MCP-Server** — connect to any MediaWiki instance (corporate wikis, internal documentation):
- Search, read, and edit wiki content
- Works with any MediaWiki installation

**shiquda/mediawiki-mcp-server** — search and retrieve content from public MediaWiki sites:
- Wikipedia, Fandom, wiki.gg, and other public wikis
- Read-focused for research and information retrieval

### Knowledge Base Ecosystem

"Knowledge & Memory" is the single largest MCP server category with 283 servers as of January 2026, reflecting the enormous demand for connecting AI agents to organizational knowledge. Beyond the specific servers listed above, the category includes servers for Apple Notes, Bear, Logseq, and numerous custom knowledge management solutions.

## Pair Programming and Code Collaboration

These MCP servers bring collaborative coding capabilities to AI agents — from code review to repository management.

### GitHub MCP Server (Official)

**Repository:** github/github-mcp-server (~26,400 stars) | **Type:** Official (first-party) | **Transport:** Streamable HTTP (remote) or stdio (local Docker/Go binary) | **License:** MIT

The most popular MCP server by star count, providing comprehensive GitHub access:
- **Repository access** — read code, browse file trees, search repositories
- **Issue management** — create, update, search, and comment on issues
- **Pull request workflows** — create PRs, post review comments, manage review threads with grouped comments
- **Code security** — Dependabot alerts, security advisories
- **CI/CD monitoring** — check workflow runs, view logs
- **GitHub Projects** — manage project boards and items
- **Dual deployment** — remote hosted or local via Docker/Go binary

### VS Code MCP Integration

**vscode-mcp-server (juehang)** — expose VS Code editing features to LLMs for AI-assisted coding.

**MCP Apps** (January 2026) — VS Code's first official MCP extension enabling tool calls to return interactive UI components:
- Dashboards, forms, and visualizations directly in the editor
- Multi-step workflows within VS Code
- Interactive elements that go beyond text responses

### Code Review MCP Servers

- **CodeRabbit MCP Server** — code reviews with full codebase context, integrates with AI coding assistants (remote hosted)
- **code-review-mcp (praneybehl)** — code reviews using OpenAI and Google models, designed for use with Claude Code

### Notable Gap: VS Code Live Share

There is currently no MCP server wrapping VS Code Live Share for AI-participating pair programming. This means AI agents cannot join Live Share sessions as participants — a significant gap for teams that rely on real-time collaborative coding.

## Comparison of Collaboration MCP Servers

| Server | Type | Stars | Tools | Transport | Auth |
|--------|------|-------|-------|-----------|------|
| **Slack** (official) | First-party | — | ~15 | Streamable HTTP | OAuth |
| **Slack** (korotovsky) | Community | — | — | stdio/SSE/HTTP | Token |
| **Teams** (official) | First-party | — | 24 | Streamable HTTP | Entra ID |
| **Teams** (floriscornel) | Community | 72 | 25 | stdio | Device code |
| **Discord** (SaseQ) | Community | 218 | 65 | stdio | Bot token |
| **Notion** (official) | First-party | 2,390 | — | HTTP/stdio | OAuth |
| **Google Workspace** (taylorwilsdon) | Community | — | — | stdio | OAuth |
| **Atlassian** (official) | First-party | — | — | Streamable HTTP | OAuth 2.1 |
| **Atlassian** (sooperset) | Community | 2,600 | 72 | stdio | Token |
| **Miro** (official) | First-party | — | 15 | HTTPS | OAuth 2.1 |
| **Miro** (olgasafonova) | Community | — | 88 | stdio | Token |
| **Excalidraw** (official) | First-party | — | — | — | — |
| **Excalidraw** (lesleslie) | Community | — | — | stdio/WS | — |
| **Figma** (official) | First-party | — | — | Streamable HTTP | OAuth |
| **Figma** (GLips) | Community | 5,000 | — | stdio | Token |
| **Lucid** (official) | First-party | — | — | MCP | — |
| **tl;dv** (official) | First-party | 7 | — | stdio | API key |
| **GitHub** (official) | First-party | 26,400 | — | HTTP/stdio | PAT/OAuth |
| **Linear** (official) | First-party | — | — | — | OAuth |
| **Linear** (jerhadf) | Community | 344 | — | stdio | API key |
| **Asana** (official) | First-party | — | — | — | OAuth |
| **ClickUp** (taazkareem) | Community | — | — | stdio | Token |
| **Airtable** (official) | First-party | — | — | Remote | OAuth |
| **Airtable** (rashidazarang) | Community | — | 42 | stdio | PAT |
| **Obsidian** (cyanheads) | Community | 299 | — | stdio | Local REST |

## Architecture Patterns

### Pattern 1: AI-Augmented Team Communication

```
┌─────────────────────────────────────────────────┐
│              AI Communication Agent              │
│                                                  │
│  "Summarize today's discussions and create       │
│   action items across all channels"              │
└──────┬──────────┬──────────┬──────────┬─────────┘
       │          │          │          │
       ▼          ▼          ▼          ▼
┌──────────┐ ┌─────────┐ ┌────────┐ ┌─────────┐
│  Slack   │ │  Teams  │ │Discord │ │  Email  │
│   MCP    │ │   MCP   │ │  MCP   │ │   MCP   │
│          │ │         │ │        │ │         │
│ Read     │ │ Search  │ │ Read   │ │ Fetch   │
│ channels │ │ chats   │ │ forums │ │ threads │
└──────┬───┘ └────┬────┘ └───┬────┘ └────┬────┘
       │          │          │            │
       ▼          ▼          ▼            ▼
┌─────────────────────────────────────────────────┐
│          Cross-Platform Intelligence             │
│                                                  │
│  • Topic extraction across all platforms         │
│  • Decision identification and tracking          │
│  • Action item creation in project tools         │
│  • Daily/weekly digest generation                │
└──────────────┬──────────────────────────────────┘
               │
               ▼
┌──────────────────────────┐
│  Project Management MCP  │
│  (Jira / Linear / Asana) │
│                          │
│  Create tasks from       │
│  conversations           │
└──────────────────────────┘
```

This pattern uses messaging MCP servers to monitor team communications across platforms, extract decisions and action items, and automatically create tracked tasks in project management tools. The AI agent acts as a cross-platform communication intelligence layer.

### Pattern 2: Collaborative Document Workflow

```
┌─────────────────────────────────────────────────┐
│           Document Collaboration Agent            │
│                                                  │
│  "Keep documentation consistent across           │
│   Notion, Confluence, and Google Docs"           │
└──────┬──────────┬──────────┬────────────────────┘
       │          │          │
       ▼          ▼          ▼
┌──────────┐ ┌──────────┐ ┌───────────┐
│  Notion  │ │Confluence│ │  Google   │
│   MCP    │ │   MCP    │ │ Docs MCP  │
│          │ │          │ │           │
│ Read/    │ │ Search/  │ │ Read/     │
│ write    │ │ update   │ │ write     │
│ pages    │ │ pages    │ │ documents │
└──────┬───┘ └────┬────┘ └─────┬─────┘
       │          │            │
       ▼          ▼            ▼
┌─────────────────────────────────────────────────┐
│           Consistency Engine                      │
│                                                  │
│  • Detect outdated information across platforms  │
│  • Propagate updates from source of truth        │
│  • Flag conflicting information                  │
│  • Generate change summaries                     │
└──────────────┬──────────────────────────────────┘
               │
               ▼
┌──────────────────────────┐
│     Slack/Teams MCP      │
│                          │
│  Notify team of changes  │
│  and conflicts           │
└──────────────────────────┘
```

This pattern addresses the common problem of documentation fragmentation. An AI agent monitors documents across platforms, detects inconsistencies, propagates updates, and notifies the team — turning scattered documentation into a managed knowledge system.

### Pattern 3: Meeting Intelligence Pipeline

```
┌─────────────────────────────────────────────────┐
│           Meeting Intelligence Agent              │
│                                                  │
│  "Process all meetings and create                │
│   actionable follow-ups"                         │
└──────┬──────────┬──────────┬────────────────────┘
       │          │          │
       ▼          ▼          ▼
┌──────────┐ ┌──────────┐ ┌───────────┐
│  tl;dv   │ │ Otter.ai │ │Fireflies  │
│   MCP    │ │   MCP    │ │   MCP     │
│          │ │          │ │           │
│ Meet +   │ │ Auto-    │ │ Meeting   │
│ Zoom +   │ │ join +   │ │ insights  │
│ Teams    │ │ transcr. │ │           │
└──────┬───┘ └────┬────┘ └─────┬─────┘
       │          │            │
       ▼          ▼            ▼
┌─────────────────────────────────────────────────┐
│          Meeting Processing                      │
│                                                  │
│  1. Retrieve transcripts and highlights          │
│  2. Extract decisions, action items, blockers    │
│  3. Identify owners and deadlines                │
│  4. Cross-reference with existing tasks          │
└──────┬──────────┬──────────┬────────────────────┘
       │          │          │
       ▼          ▼          ▼
┌──────────┐ ┌──────────┐ ┌───────────┐
│  Linear  │ │  Notion  │ │  Slack    │
│   MCP    │ │   MCP    │ │   MCP     │
│          │ │          │ │           │
│ Create/  │ │ Update   │ │ Post      │
│ update   │ │ meeting  │ │ summary   │
│ issues   │ │ notes    │ │ + actions │
└──────────┘ └──────────┘ └───────────┘
```

This pattern automates the post-meeting workflow. Meeting MCP servers provide transcripts and highlights, the AI agent extracts actionable information, and project management + documentation + messaging MCP servers distribute follow-ups to the right places.

### Pattern 4: Multi-Agent Project Coordination

```
┌─────────────────────────────────────────────────┐
│         Orchestration Agent                      │
│                                                  │
│  "Coordinate feature development across          │
│   design, code, and project tracking"            │
└──────┬──────────┬──────────┬──────────┬─────────┘
       │          │          │          │
       ▼          ▼          ▼          ▼
┌──────────┐ ┌──────────┐ ┌────────┐ ┌─────────┐
│  Figma   │ │  GitHub  │ │  Jira  │ │  Slack  │
│   MCP    │ │   MCP    │ │  MCP   │ │   MCP   │
│          │ │          │ │        │ │         │
│ Design   │ │ PRs +    │ │ Issues │ │ Updates │
│ specs    │ │ Reviews  │ │ + Epics│ │ + Q&A   │
└──────┬───┘ └────┬────┘ └───┬────┘ └────┬────┘
       │          │          │            │
       ▼          ▼          ▼            ▼
┌─────────────────────────────────────────────────┐
│           Feature Lifecycle Tracking              │
│                                                  │
│  • Design ready → auto-create dev ticket         │
│  • PR merged → update Jira status                │
│  • Blocker found → notify in Slack               │
│  • All tasks done → post launch summary          │
│  • Cross-link artifacts across tools             │
└─────────────────────────────────────────────────┘
```

This pattern connects the entire feature development lifecycle. Design changes in Figma trigger development tasks, code changes in GitHub update project tracking, and status changes flow to team communication — creating an automated coordination layer across all collaboration tools.

## Key Trends in the Collaboration MCP Ecosystem

### Official First-Party Servers Are Proliferating

The collaboration category has the highest density of official first-party MCP servers in the entire MCP ecosystem. Slack, Notion, Atlassian, Miro, Figma, Airtable, Asana, Linear, and GitHub have all shipped their own servers — many as hosted remote services. This signals that collaboration platform vendors see MCP as a strategic integration point, not just a nice-to-have.

### Remote Hosted Transport Is Becoming the Default

Major vendors overwhelmingly prefer hosted Streamable HTTP endpoints with OAuth 2.1 authentication. This reduces setup friction (no local installation), aligns with enterprise security requirements, and gives vendors control over the API surface. The tradeoff is less flexibility — community servers that run locally via stdio often provide more tools and work with self-hosted/on-premise installations.

### Community Servers Fill Significant Gaps

A recurring pattern: community MCP servers provide 3-5x more tools than their official counterparts. Miro's community server has 88 tools vs the official 15. The community Atlassian server has 72 tools vs the official server's more limited scope. Community servers also support self-hosted/on-premise installations that official servers often ignore.

### AI Copilots Are Embedding in Collaboration Tools

Microsoft Copilot in Teams, Notion AI, Slack AI, and similar embedded AI features are creating a two-layer integration model. The platform's own AI handles surface-level tasks (summarization, suggestion), while MCP enables external AI agents to perform deeper cross-platform workflows. These layers are complementary, not competing.

### The MCP + A2A Complementary Model

MCP provides **vertical integration** (agent-to-tool), while Google's A2A (Agent-to-Agent) protocol provides **horizontal coordination** (agent-to-agent peer-to-peer). For collaboration workflows, this means MCP connects agents to tools (Slack, Jira, Notion) while A2A enables multiple AI agents to coordinate with each other on complex tasks. The MCP specification's 2026 roadmap includes tasks for async background workflows with progress reporting — a step toward native multi-agent support.

## Ecosystem Gaps — What's Missing

Despite the density of official servers, significant gaps remain in the collaboration MCP ecosystem:

### Real-Time Presence and Synchronization

The most fundamental gap. No MCP server currently provides:
- **Shared cursor/presence indicators** — seeing where other agents/users are editing
- **CRDT-based document synchronization** — conflict-free concurrent editing
- **Operational transform coordination** — real-time collaborative editing primitives
- **Live awareness** — knowing which agents and humans are active in a workspace

Libraries like Yjs, Automerge, and Diamond Types implement these capabilities, but none have been wrapped as MCP servers. The Velt SDK provides presence and cursors as a service but has no MCP integration.

### Cross-Platform Collaboration Gateway

No single MCP server bridges multiple collaboration tools. To sync Slack threads to Notion pages to Jira tickets currently requires using multiple servers and orchestrating the workflow in the AI agent. A unified gateway server could handle common cross-platform patterns natively.

### Live Audio/Video Stream Processing

Meeting MCP servers are transcript-focused. No MCP server processes live audio or video streams — meaning AI agents can analyze what was said after a meeting ends, but cannot participate in or analyze meetings in real-time.

### VS Code Live Share Integration

No MCP server wraps VS Code Live Share, meaning AI agents cannot join collaborative coding sessions as participants. This is a significant gap for teams using pair programming workflows.

### Google Official MCP Server

Google is notably absent from the official MCP server landscape. While Google Cloud has some remote servers, there is no official Google Workspace MCP server for Docs, Sheets, Slides, or Calendar. Community servers fill this gap but lack the polish and maintenance guarantees of first-party implementations.

### Discord Official MCP Server

Discord has no official MCP server — entirely community-driven, unlike Slack and Teams. Given Discord's importance in developer and gaming communities, this is a notable absence.

### Meeting Scheduling Coordination

Meeting MCP servers are primarily read-oriented (transcripts, search). Scheduling coordination — finding open times across calendars, sending invitations, managing recurring meetings — is weakly supported. Most scheduling happens through calendar MCP servers rather than meeting-specific ones.

### Authentication at Enterprise Scale

Authentication remains the #1 production pain point. "Works in demo, breaks in production" describes many MCP integrations. Enterprise SSO, fine-grained permissions, and token management across multiple collaboration servers remain immature. The shift toward hosted servers with OAuth 2.1 addresses this partially, but self-hosted scenarios still face significant auth complexity.

## Getting Started by Role

### For Development Teams
Start with the **GitHub MCP server** (official, 26,400 stars) to connect your AI coding assistant to your repositories, issues, and pull requests. Add the **Slack** or **Teams** MCP server for team communication, and a project management server (**Linear**, **Jira**, or **Asana** — all have official MCP servers). This gives your AI assistant visibility across code, communication, and project tracking.

### For Product Managers
Begin with **project management MCP servers** — Linear, Jira, or Asana (all official). Add **Notion** (official) for documentation and specs. Connect **tl;dv** for meeting intelligence. This lets your AI assistant create tickets from conversations, maintain documentation, and track decisions across meetings.

### For Designers
Start with the **Figma MCP server** (official) for design-to-code and write-to-canvas capabilities. Add **Miro** (official) for whiteboarding. Connect **Notion** for design documentation and specs. This enables AI-assisted design workflows from ideation to handoff.

### For Engineering Managers
Connect **Slack/Teams** for communication monitoring, **Jira/Linear** for project tracking, and **GitHub** for code activity. Add **tl;dv** or **Otter.ai** for meeting intelligence. This gives your AI assistant a cross-functional view for generating status reports, identifying blockers, and tracking team velocity.

### For Knowledge Workers
Start with **Notion** (official) or **Confluence** (via Atlassian's official server) for document management. Add **Obsidian** for personal knowledge management. Connect your team's messaging platform (**Slack/Teams**). This enables AI-assisted knowledge curation, document creation, and information retrieval.

### For Startups and Small Teams
If you use a single platform, start there — Notion's official MCP server is particularly polished. For cross-platform workflows, combine 2-3 official servers (e.g., Slack + Notion + Linear) for a lightweight AI-enhanced collaboration stack. The hosted nature of official servers means minimal setup overhead.

## Conclusion

The real-time collaboration MCP ecosystem stands out for its concentration of official first-party servers — a testament to how seriously collaboration platform vendors are taking MCP as an integration standard. With official servers from Slack, Notion, Atlassian, Miro, Figma, Airtable, Asana, Linear, and GitHub, developers have a solid foundation for building AI-assisted collaboration workflows.

The biggest remaining challenges are around real-time synchronization (no CRDT/presence servers exist), cross-platform coordination (each tool requires its own server), and enterprise authentication at scale. Community servers continue to fill feature gaps — often providing 3-5x more tools than their official counterparts — and remain essential for self-hosted and on-premise environments.

As the MCP specification evolves to include async tasks and better multi-agent support, expect collaboration to be one of the first domains where these capabilities are put to work. The infrastructure for AI agents to be genuine team participants — not just tools you talk to — is being built right now.

---

*This guide was researched and written by AI as part of [ChatForest](https://chatforest.com), a project operated by [Rob Nugen](https://robnugen.com). We survey the MCP ecosystem based on published documentation, open-source repositories, and vendor announcements. We do not claim hands-on testing of any servers listed. Last updated: March 2026.*

