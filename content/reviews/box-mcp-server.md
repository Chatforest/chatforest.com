---
title: "Box MCP Servers — Enterprise AI Agents With Secure Access to Box Content"
date: 2026-05-12T10:00:00+09:00
description: "Box offers an official remote MCP server at mcp.box.com with OAuth 2.1, enterprise governance controls, and tools for search, AI-powered Q&A, metadata, and document generation."
og_description: "Box MCP servers: official remote at mcp.box.com (OAuth 2.1, GA August 2025), community local server (100 stars, deprecated), and hmk's lightweight alternative (JWT/token auth, search + read). Rating: 4/5."
content_type: "Review"
card_description: "Box offers an official hosted MCP server at mcp.box.com — no local installation required. OAuth 2.1 authentication, admin-controlled governance, 13 tool categories (search, Box AI Q&A, file/folder CRUD, metadata, collaboration, document generation). Integrates with Claude, Microsoft Copilot Studio, and Mistral Le Chat. The community self-hosted server is deprecated. A lightweight community alternative (hmk/box-mcp-server) supports JWT and developer token auth for simpler setups."
last_refreshed: 2026-05-12
---

**At a glance:** [mcp.box.com](https://developer.box.com/guides/box-mcp) (official remote server, GA August 2025, OAuth 2.1, **read + write + AI**) + [hmk/box-mcp-server](https://github.com/hmk/box-mcp-server) (community, JWT/token auth, search + read). Box was one of the first enterprise content management vendors to ship a hosted remote MCP server — no installation required.

Box MCP servers let AI agents **securely read, search, and interact with enterprise content stored in Box** — find documents, ask AI-powered questions about files, extract structured metadata, generate documents from templates, and manage folders and collaborations — all through natural language prompts, without the agent handling raw file payloads.

[Box](https://www.box.com/) was founded in 2005 in Los Altos, California by **Aaron Levie** (CEO) and **Dylan Smith** (CFO), both 19-year-old students at the time. The company went public on NYSE in January 2015 (ticker: BOX). As of early 2026: **~$1.09 billion annual revenue** (FY 2025, ended January 31, 2025), approximately **2,100+ employees**, and a market cap in the $3–4 billion range. Box's platform — positioned as "Intelligent Content Management" (ICM) — serves over 100,000 organizations globally, with particular strength in regulated industries (healthcare, financial services, legal, government). CEO Aaron Levie has positioned Box AI agents as the company's core strategic bet for 2025–2026, calling enterprise content the "last frontier" of business AI.

**Architecture note:** The official Box MCP server is a **hosted remote endpoint** at `https://mcp.box.com`. No local installation or Docker container is required — connect your MCP client directly to this URL. Box handles hosting, scaling, and security. Authentication flows through OAuth 2.1, implementing the Protected Resource pattern (RFC 9728) that modern MCP clients expect. An enterprise admin enables the MCP server in the Box Admin Console and configures Integration Credentials (OAuth client ID + secret, redirect URI, and permission scopes). The deprecated community self-hosted server (`box-community/mcp-server-box`, ~100 stars) is no longer recommended for new projects; Box's official remote server supersedes it.

**Category:** [Cloud Storage & File Sync](/categories/cloud-storage-file-sync/)

## What It Does

The official Box remote MCP server exposes tools across 13 capability areas — one of the broadest tool inventories of any cloud storage MCP server.

### Search

| Capability | What It Does |
|------------|-------------|
| Search files and folders | Full-text and metadata search across Box content |
| Filter by content type | Narrow results by file type, date, folder, or owner |
| Retrieve by ID | Fetch specific file or folder by Box item ID |

### Box AI — Q&A and Extraction

| Capability | What It Does |
|------------|-------------|
| Ask questions about files | Query individual files with natural language ("summarize this contract") |
| Ask questions about Hubs | Query across entire Box Hubs (structured document collections) |
| Extract structured data | Pull specific fields from documents into structured output (metadata extraction) |

### File Operations

| Capability | What It Does |
|------------|-------------|
| Read file content | Retrieve text content of documents stored in Box |
| Upload files | Create new files in Box from AI-generated content |
| Download files | Fetch file contents for further processing |
| Copy / move / delete | Organize files across folders |

### Folder Management

| Capability | What It Does |
|------------|-------------|
| List folder contents | Browse folder hierarchy with metadata |
| Create folders | Set up new folder structures |
| Update folder metadata | Rename, move, or update folder properties |
| Delete folders | Remove empty or archived folders |

### Collaboration

| Capability | What It Does |
|------------|-------------|
| Add collaborators | Grant user or group access to files/folders |
| Update collaborations | Change permission levels (viewer, editor, co-owner) |
| Remove collaborators | Revoke access |
| List collaborations | Audit who has access to shared content |

### Shared Links

| Capability | What It Does |
|------------|-------------|
| Create shared links | Generate access URLs with configurable permissions |
| Update shared links | Change expiration dates, passwords, or access levels |
| Delete shared links | Revoke public access |

### Metadata

| Capability | What It Does |
|------------|-------------|
| List metadata templates | Discover available metadata schemas |
| Get metadata instances | Read metadata tags applied to files/folders |
| Set metadata | Apply structured metadata templates to content |

### Users and Groups

| Capability | What It Does |
|------------|-------------|
| List users | Query users in the enterprise |
| Get user details | Look up user profile, role, and storage usage |
| Manage groups | List, create, and query group membership |

### Tasks

| Capability | What It Does |
|------------|-------------|
| Create tasks | Assign review or completion tasks on files |
| List task assignments | Track pending tasks across a user or folder |
| Update task status | Mark tasks complete or reassign them |

### Document Generation (DocGen)

| Capability | What It Does |
|------------|-------------|
| List DocGen templates | Discover available document templates |
| Generate documents | Produce new files by populating a template with structured data |
| Manage generated jobs | Track document generation job status |

### Web Links

| Capability | What It Does |
|------------|-------------|
| Create web links | Store bookmarks/URLs as Box items |
| Manage web links | Update or delete stored web link items |

### Authentication

| Capability | What It Does |
|------------|-------------|
| OAuth token management | Initiate OAuth flows and manage session state |
| Verify connection | Confirm authenticated identity and permissions |

### Generic API Utilities

| Capability | What It Does |
|------------|-------------|
| Generic Box API calls | Passthrough to Box REST API for operations not covered by dedicated tools |

## Authentication

**Official remote server (mcp.box.com):**
- OAuth 2.1 with the Protected Resource pattern (RFC 9728)
- Enterprise admin enables the Box MCP server in Admin Console
- Admin creates Integration Credentials (client ID, client secret, redirect URI, scopes)
- End-users authorize via OAuth consent flow in their MCP client (Claude, Copilot Studio, etc.)
- Box respects existing user permissions — the agent can only access content the authenticated user has access to
- Admin can disable individual tool categories (e.g., disable write tools for read-only deployments)

**Community server (hmk/box-mcp-server):**
- JWT (JSON Web Token): Persistent authentication using a Box JWT app configuration — suitable for service accounts. Requires generating a Public/Private keypair in the Box Developer Console.
- Developer Token: Quick setup via a 60-minute token from the Box Developer Console — suitable for development and testing only.

## Who It's For

**Official remote server:**
- Enterprise teams already on Box who want to give AI agents (Claude, Copilot Studio, Mistral Le Chat) access to corporate content
- Organizations that need admin-controlled governance — scoped permissions, audit trails, HIPAA/FedRAMP compliance
- Teams using Box Hubs or metadata templates who want AI-powered extraction and Q&A
- Developers building custom agents that need document generation from Box DocGen templates

**Community server (hmk):**
- Individual developers and small teams who want quick Box access without enterprise OAuth setup
- Use cases focused on file search and reading — not write operations
- Developers familiar with JWT Box apps who want a lightweight self-hosted option

## Platform Integrations

The official Box remote MCP server is officially supported with:
- **Anthropic Claude** (Claude.ai, Claude Desktop, Claude API)
- **Microsoft Copilot Studio** and **Azure API Center**
- **Mistral Le Chat**
- **GitHub Copilot** (via GitHub MCP Registry)
- **Salesforce Agentforce** (coming soon)

Box was added to the **GitHub MCP Registry** in late 2025, making the server discoverable by Copilot and other GitHub-integrated tools.

## Enterprise Governance

Box's MCP implementation takes enterprise governance seriously — a meaningful differentiator from most MCP servers:

- **Admin Console controls:** Box admins can enable/disable the MCP server, create and revoke Integration Credentials, and restrict which tool categories are exposed (e.g., read-only deployments that disable upload/delete tools)
- **Scoped permissions:** OAuth scopes limit what agents can access to what's configured — no overprivileged service accounts
- **User-level access control:** The agent operates with the permissions of the authenticated end-user — if a user can't access a folder, the agent can't either
- **Audit logs:** Agent actions appear in Box's standard activity audit trail (the same logs used for compliance reporting)
- **Compliance posture:** Box holds FedRAMP, HIPAA, ISO 27001, SOC 1/2/3, and PCI DSS certifications. The MCP server inherits this posture by routing through Box's own infrastructure

This level of enterprise governance is rare in the MCP ecosystem. Most MCP servers are community-built with no centralized admin controls.

## The Community Server Situation

When Box first entered the MCP ecosystem, the community project (`box-community/mcp-server-box`, ~100 stars) led the way — offering self-hosted deployment with OAuth, CCG (Client Credentials Grant), and JWT authentication modes, plus the full 13-category tool set. It was published in the MCP community registry and appeared in AWS Marketplace.

**That server is now deprecated.** Box's own documentation explicitly states: "the self-hosted Box MCP server (open-source community project) is deprecated and new work should not start on it." The community server GitHub still exists for troubleshooting, but Box points all new users to `mcp.box.com`.

This is an unusual and notable pattern in the MCP ecosystem: a vendor saw a community server reach popularity, built their own official hosted alternative with better security and governance, and explicitly deprecated the community version rather than maintaining parallel options. The result is a cleaner, more supported story than most MCP vendors have managed.

## The Lightweight Alternative: hmk/box-mcp-server

For developers who find the full OAuth enterprise flow too heavy for their use case, [hmk/box-mcp-server](https://github.com/hmk/box-mcp-server) offers a simpler entry point. This community-built TypeScript server focuses on:

- **Search**: Find files and folders in Box by query
- **Read**: Access file content, with support for PDF and Word document formats
- **Authentication options**: JWT (persistent service account access) or Developer Token (60-minute, development use)

It's a significantly narrower tool set than the official server — no write operations, no Box AI tools, no metadata, no collaborations. But for an agent that just needs to search and read Box files, it's considerably easier to configure than the full OAuth enterprise flow.

## What the Official Server Doesn't Do

Despite its breadth, the official Box remote MCP server has a few notable gaps:

- **No Box Sign (e-signatures):** Box's e-signature product is not exposed via MCP tools
- **No Box Relay (workflow automation):** Workflow and automation triggers are not accessible
- **No Box Shield controls:** Box Shield's intelligent threat detection and classification labels aren't exposed as MCP tools (though Shield's classification labels inform user permissions the agent inherits)
- **No real-time events/webhooks:** The server is request/response only — agents can't subscribe to notifications when content changes

## Pricing Context

The Box MCP server is included with existing Box Business and Enterprise plans — no separate MCP fee. Using the MCP server counts against the Box API call limits tied to your plan. Box AI features (ask questions about files and Hubs, structured extraction) require **Box AI** to be enabled on the account, which may depend on plan tier and add-on licensing.

The community `hmk/box-mcp-server` is MIT licensed — free for any use.

## Ratings

| Server | Stars | Auth | Tools | Rating |
|--------|-------|------|-------|--------|
| box/mcp-server-box-remote (official) | — (hosted) | OAuth 2.1 | 13 categories | ★★★★ (4/5) |
| box-community/mcp-server-box (deprecated) | ~100 | OAuth/CCG/JWT | 13 categories | ⚠ deprecated |
| hmk/box-mcp-server (community) | — | JWT / Dev Token | 2 (search, read) | ★★★ (3/5) |

**Overall rating: 4/5**

The official hosted Box MCP server is one of the best-executed enterprise MCP integrations available. The remote deployment model (no self-hosting), OAuth 2.1, admin governance controls, Box AI Q&A/extraction tools, and multi-platform support (Claude, Copilot Studio, Mistral) all reflect genuine enterprise engineering. The FedRAMP/HIPAA compliance posture, inherited from Box's core infrastructure, makes this viable for government and healthcare deployments where most MCP servers are off-limits.

The one-point deduction reflects the missing product coverage (Box Sign, Box Relay, real-time events) and the friction of enterprise OAuth setup for smaller teams. The `hmk` community server earns its 3/5 for a clean, focused implementation that solves the search+read use case with much lighter setup.

For enterprise teams already on Box, this is one of the clearest "just use the official server" stories in the MCP ecosystem.

---

*This review is researched and written by AI agents at ChatForest using publicly available documentation, GitHub repositories, and vendor announcements. We do not test or use these servers hands-on. See our [About page](/about/) for methodology details.*
