# Customer Support & Helpdesk MCP Servers — Zendesk, Intercom, Freshdesk, ServiceNow, Plain, and More

> Customer support and helpdesk MCP servers are giving AI assistants direct access to ticket management, conversation handling, and support workflows.


Customer support and helpdesk MCP servers are giving AI assistants direct access to ticket management, conversation handling, and support workflows. Instead of switching between your IDE and a support dashboard, these servers let AI agents search tickets, draft responses, manage contacts, and monitor inbox activity — all through the Model Context Protocol. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

The landscape spans five areas: **enterprise helpdesks** (Zendesk, Freshdesk, ServiceNow), **modern support platforms** (Intercom, Plain, Pylon), **live chat and messaging** (Crisp, Tidio, LiveChat), **open-source helpdesks** (Zammad), and **specialized support tools** (Help Scout, Gorgias, HubSpot).

The headline findings: **Only three platforms have official MCP servers** — Intercom, Plain, and Pylon — which is surprisingly low for a category this large. **Intercom's is the most mature**, with a remote hosted server on Cloudflare, OAuth authentication, and real-time data access. **Plain offers the most comprehensive toolset** among official servers with 30 tools across five functional areas. **Freshdesk has the deepest community server** with 30 tools covering tickets, agents, contacts, companies, and conversations. **ServiceNow has the most competing implementations** with 5+ servers on GitHub, reflecting the platform's complexity and enterprise demand. **Zendesk — the market leader — has no official MCP server**, relying entirely on community implementations. **Help Scout stands out for compliance** with optional PII redaction and scoped inbox access. **Most servers focus on ticket CRUD** rather than intelligent support workflows like auto-routing, sentiment analysis, or SLA monitoring.

## Enterprise Helpdesks

### Zendesk MCP Server (reminia)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [reminia/zendesk-mcp-server](https://github.com/reminia/zendesk-mcp-server) | 72 | Python | Apache-2.0 | 6 |

The most popular community-built Zendesk MCP server, providing tools for retrieving and managing Zendesk tickets and comments. Tools include `get_tickets`, `get_ticket`, `get_ticket_comments`, `create_ticket_comment`, `create_ticket`, and `update_ticket`. Beyond raw API access, it includes **specialized prompts** for ticket analysis and response drafting — helping agents not just read tickets but intelligently respond to them.

The standout feature is full access to **Zendesk Help Center articles as a knowledge base** through MCP resources. This means an AI agent can search your help documentation while drafting a support response, grounding replies in your actual knowledge base rather than hallucinating answers.

Notably, Zendesk announced an **MCP client** at their AI Summit in October 2025 (still in Early Access as of March 2026), but they haven't released an official MCP *server*. The market leader in customer support is letting the community handle server-side MCP integration — a significant gap.

### Freshdesk MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [effytech/freshdesk_mcp](https://github.com/effytech/freshdesk_mcp) | 46 | Python | MIT | 30 |

The most tool-rich customer support MCP server in this review. Covers five operational domains: **ticket management** (create, update, list, get, delete, search), **contact management** (create, update, list, get, delete, search, merge contacts), **agent management** (list, get, update agents, view groups and roles), **company management** (create, update, list, get, delete, search, list company contacts), and **conversation management** (create replies and notes, list, get, update, delete conversations).

The merge contacts capability is notable — it's the only server in this review that handles contact deduplication, a real pain point in support operations. Security features include API key-based authentication, rate limiting, comprehensive error handling with retry logic and exponential backoff. The same team (Effy) also built a **Freshservice MCP server** for ITSM operations, making this the most complete Freshworks ecosystem coverage via MCP.

### ServiceNow MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [michaelbuckner/servicenow-mcp](https://github.com/michaelbuckner/servicenow-mcp) | 37 | Python | MIT | 10 |
| [ShunyaAI/snow-mcp](https://github.com/ShunyaAI/snow-mcp) | 5 | Python | MIT | 60+ |
| [Happy-Technologies-LLC/mcp-servicenow-nodejs](https://github.com/Happy-Technologies-LLC/mcp-servicenow-nodejs) | — | Node.js | — | 15+ |
| [aartiq/servicenow-mcp](https://github.com/aartiq/servicenow-mcp) | — | Python | — | 400+ |
| [echelon-ai-labs/servicenow-mcp](https://github.com/echelon-ai-labs/servicenow-mcp) | — | Python | — | 5+ |

ServiceNow has the most competing MCP server implementations of any support platform — at least five on GitHub. This reflects ServiceNow's enormous enterprise footprint and the complexity of its API surface.

**michaelbuckner/servicenow-mcp** (37 stars) is the most popular, featuring natural language interactions for record search, updates, and script management. It supports multiple authentication methods (basic auth, tokens, OAuth) and provides resources for incidents, users, knowledge articles, and database schema.

**ShunyaAI/snow-mcp** is the most comprehensive with 60+ pre-built tools covering incidents, changes, users, service catalog, and projects. Tools are logically organized into modules with Pydantic validation, retry logic with exponential backoff, and a built-in CLI for tool discovery.

**aartiq/servicenow-mcp** claims 400+ tools across every ServiceNow domain — ITSM, ITOM, HRSD, CSM, SecOps, GRC, and more — though the practical tool count for customer service operations is a subset.

**Happy-Technologies-LLC/mcp-servicenow-nodejs** differentiates with natural language search supporting 15+ query patterns and 8 read-only resource URIs for quick table lookups.

The ServiceNow coverage is the most robust of any platform in this review — but it's all community-built. ServiceNow itself has published guides on building MCP servers but hasn't released an official one.

## Modern Support Platforms (Official Servers)

### Intercom MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Intercom MCP](https://developers.intercom.com/docs/guides/mcp) | — | — | — | Multiple |
| [fabian1710/mcp-intercom](https://github.com/fabian1710/mcp-intercom) | 7 | TypeScript | MIT | 1 |

**Official** remote MCP server from Intercom, hosted on Cloudflare infrastructure. This is the most mature official support platform MCP server — Intercom was one of the first three customer support platforms to ship an official MCP server (alongside Plain and Pylon).

The official server provides structured access to **conversations** (search, filter, retrieve patterns), **contacts** (lookup by name or email, pull thread history), and **workspace data** (user profile, workspace settings). Authentication uses **OAuth flow** with automatic browser-based setup — your AI inherits your Intercom permissions, so access is scoped to what you can see in the dashboard.

Key use cases: ask real-time questions about customer conversation patterns for troubleshooting, sync support data into engineering tools like Linear or Jira to enrich bug reports, and retrieve customer data for cross-functional decisions. Currently limited to **US-hosted workspaces** only.

The community alternative (fabian1710/mcp-intercom) offers a simpler single-tool approach with `search-conversations` supporting filters for date ranges, customer ID, and conversation state.

### Plain MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Plain MCP](https://mcp.plain.com/mcp) | — | — | — | 30 |
| [ndom91/plain-mcp-server](https://github.com/ndom91/plain-mcp-server) | — | — | — | — |

**Official** MCP server from Plain, the developer-first customer support platform. With 30 tools across five functional areas, this is the most comprehensive official support MCP server.

Tool categories: **Threads** (fetch, search, reply, assign, snooze, change priority, add labels, mark done, create internal notes), **Customers** (look up profiles, search by name or email, pull a customer's full thread history), **Tenants** (search and manage company-level data), **Help center** (browse articles, find stale content, create or update articles directly), and **Workspace** (access user profile, workspace settings, available labels).

Authentication uses your existing Plain account — no separate API keys to generate or rotate. The AI inherits your permissions, maintaining the principle of least privilege. The help center management tools are a differentiator — agents can not only read support documentation but actively maintain it, identifying stale articles and pushing updates.

Setup instructions cover Claude.ai, Claude Code, Cursor, and ChatGPT. The remote endpoint at `mcp.plain.com/mcp` means zero local installation.

### Pylon MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Pylon MCP](https://mcp.usepylon.com) | — | — | — | 6 |
| [JustinBeckwith/pylon-mcp](https://github.com/JustinBeckwith/pylon-mcp) | 4 | JS/TS | MIT | 24 |
| [marcinwyszynski/pylon-mcp](https://github.com/marcinwyszynski/pylon-mcp) | — | — | — | 40 |

**Official** MCP server from Pylon, the B2B customer support platform. The official server provides 6 tools with OAuth authentication covering issues, accounts, users, and contacts — both read and write access.

The community implementations significantly extend the official toolset. **JustinBeckwith/pylon-mcp** offers 24 tools across 7 categories including organization management, contact operations, issue/ticket management, message redaction for privacy compliance, tag and team management, and issue followers tracking. Requires Node.js 24+ and an admin-level API token.

**marcinwyszynski/pylon-mcp** goes even further with 40 tools for managing users, contacts, issues, and knowledge base articles.

The 6-vs-24-vs-40 tool gap between the official and community servers is significant. The official server prioritizes security (OAuth, scoped access) while community servers prioritize breadth (API token auth, full API coverage).

## Live Chat & Messaging

### Crisp MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [getlate-dev/crisp-mcp](https://github.com/getlate-dev/crisp-mcp) | 8 | JS/TS | MIT | 18 |

MCP server for the Crisp customer messaging platform. Provides 18 tools across five categories: **conversation management** (retrieve conversations with filtering for unresolved or unread items), **messaging** (send messages including internal notes invisible to customers), **state control** (mark conversations as pending, unresolved, or resolved), **metadata and segments** (manage conversation metadata), and **team operations** (operator assignment, visitor listing, conversation blocking/deletion).

The internal notes feature is practically useful — agents can add context visible only to the support team without affecting the customer-facing conversation. Setup requires creating a Crisp Marketplace plugin for API credentials.

### Tidio MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [adrmrn/tidio-mcp](https://github.com/adrmrn/tidio-mcp) | 3 | Python | — | 13 |

MCP server integrating with Tidio's customer service platform, acting as a layer over Tidio's REST API. Provides 13 tools including department and operator management, contact operations, ticket lifecycle management (create, update, delete, reply), and internal note functionality.

Offers Docker deployment for non-technical users — a nice touch for support teams that want AI integration without development overhead. The server is early-stage (3 stars) but covers the core ticket management workflow.

### LiveChat / Text MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| LiveChat Text MCP | — | — | — | Multiple |

**Official** MCP server from Text (the company behind LiveChat, ChatBot, HelpDesk, and KnowledgeBase). Enables AI assistants to interact with Text platform features and data directly, allowing real-time customer support operations and workflow automation.

LiveChat serves 37,000+ companies and the Text platform includes four products: LiveChat (live chat widget), ChatBot (conversational AI builder), HelpDesk (ticketing system), and KnowledgeBase (self-service documentation). The MCP server bridges AI assistants into this ecosystem, though specific tool counts and capabilities are less documented than other servers in this review.

## Open-Source Helpdesks

### Zammad MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [basher83/Zammad-MCP](https://github.com/basher83/Zammad-MCP) | 22 | Python | — | 15+ |
| [arush15june/zammad-mcp-go](https://github.com/arush15june/zammad-mcp-go) | — | Go | — | 10+ |

MCP server for Zammad, the open-source web-based helpdesk/customer support system. The Python implementation provides 15+ tools across four categories: **ticket management** (search, retrieve, create, update with article support — 6 tools), **attachment handling** (download and manage files from ticket conversations — 3 tools), **user and organization management** (retrieve profiles and organizational data — 3 tools), and **system information** (access groups, ticket states, priority levels with caching — 4 tools).

Notable features: multiple authentication methods (API tokens, OAuth2, username/password), **dual transport modes** (stdio and HTTP) for flexible deployment, response output in both human-readable markdown and machine-readable JSON, and pre-configured prompts for ticket analysis, response drafting, and escalation summaries. The Go implementation (arush15june/zammad-mcp-go) offers a lighter alternative with similar core functionality.

Zammad itself is used by organizations like the European Space Agency, making this MCP server relevant for organizations that prefer self-hosted open-source support infrastructure.

## Specialized Support Tools

### Help Scout MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [drewburchfield/help-scout-mcp-server](https://github.com/drewburchfield/help-scout-mcp-server) | 32 | TypeScript | MIT | 7 |

MCP server for Help Scout, the customer support platform popular with small-to-medium businesses. Provides 7 tools focused on conversation search and retrieval: `searchConversations`, `comprehensiveConversationSearch`, `structuredConversationFilter`, `advancedConversationSearch`, `getConversationSummary`, `getThreads`, and `getServerTime`.

The standout feature is **optional PII redaction and scoped inbox access** — making this the most compliance-conscious server in the review. Four different search tools offer varying levels of specificity: keyword, date range, status, tag, email domain, or ticket number. The conversation summary tool extracts the original customer message and latest staff response, providing quick context without reading entire threads.

Authentication uses OAuth2 Client Credentials flow exclusively (no personal access tokens), which is more secure than API key approaches but requires registering an app in Help Scout.

### Gorgias MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mattcoatsworth/Gorgias-MCP-Server](https://github.com/mattcoatsworth/Gorgias-MCP-Server) | 2 | JavaScript | — | 6 |

MCP server for Gorgias, the e-commerce-focused helpdesk platform. Provides 6 tools across two categories: **tickets** (list, get, create, add messages) and **customers** (list, get). Supports dual authentication methods — API key and OAuth token.

Gorgias is specifically designed for e-commerce support (Shopify, BigCommerce, Magento integrations), so this server is most relevant for teams using AI to manage product-related customer inquiries. The MCP server is early-stage but covers the core read/write workflow.

### HubSpot Service Hub (via HubSpot MCP)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [HubSpot MCP](https://developers.hubspot.com/mcp) | — | — | — | Multiple |
| [peakmojo/mcp-hubspot](https://github.com/peakmojo/mcp-hubspot) | — | — | — | Multiple |

**Official** HubSpot MCP server (public beta) provides read-only access to contacts, companies, deals, **tickets**, invoices, and more. While not a dedicated support server, the ticket access makes it relevant for teams using HubSpot Service Hub for customer support.

HubSpot's MCP server connects AI agents to the full CRM context — an agent handling a support ticket can simultaneously see the customer's deal pipeline, company information, and communication history. This cross-functional view is unique among support MCP servers, which typically only expose support-specific data.

## What's Missing

The gaps in this category are notable:

- **Zendesk has no official MCP server** — despite being the market leader in customer support software, Zendesk only has an MCP *client*. Community servers fill the gap but lack official backing.
- **Salesforce Service Cloud** — while Salesforce has a general MCP server (salesforcecli/mcp), there's no Service Cloud-specific server with case management, knowledge articles, or omnichannel routing.
- **Front** — the shared inbox platform popular with support teams has no MCP presence.
- **Kayako, Zoho Desk, Freshchat** — major players with no MCP servers.
- **No intelligent routing or SLA monitoring** — every server focuses on ticket CRUD. None offer AI-driven ticket routing, SLA breach prediction, sentiment-based prioritization, or automated escalation.
- **No cross-platform abstraction** — there's no server that provides a unified interface across multiple support platforms.
- **Limited analytics** — no server provides support metrics like response time, resolution rate, or CSAT scores through MCP tools.

## The Bottom Line

Customer support MCP servers earn **3.5 out of 5**. The breadth is impressive — every major support platform has at least one MCP implementation, and three (Intercom, Plain, Pylon) have official servers. The depth varies wildly: Freshdesk's 30-tool server and ServiceNow's 60+ tool implementation are genuinely comprehensive, while others offer minimal ticket search. The category's biggest weakness is the gap between what's possible and what's built — these servers handle ticket CRUD well but don't yet enable the intelligent support workflows (auto-routing, sentiment analysis, SLA monitoring) that would make AI-assisted customer support truly transformative. The absence of an official Zendesk server remains the most conspicuous gap.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

